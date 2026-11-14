"""Timing step: audio (or video) file in, one timing JSON out (playbook section 7).

Usage:
  .venv/bin/python scripts/timing.py <audio-or-video> [--lyrics lyrics.txt] [--beats-per-bar 4]
      [--trim START_BAR N_BARS] [--beats-only] -o out/timing/<name>.json

Beats-only mode (--beats-only, same as --no-words) needs no word alignment: no .venv-align, no WhisperX,
no lyrics. The JSON then has "mode": "beats-only" and empty "words" and "lines"; everything else (beats, bars,
sections, envelopes) is identical, so templates can run on it. Start here; add words later.

- Beat grid: one fixed tempo. A comb search over the onset envelope gives BPM and a rough phase; the
  kick decides beat vs off-beat; then the phase is moved onto hi-band waveform attacks (median offset),
  because the onset envelope runs ~35-45 ms late.
- Downbeat: the beat-in-bar position where the <80 Hz level jumps most (kick in/out lands on bar lines);
  with no jump of 6 dB or more, the first beat.
- Sections: per-bar <80 Hz level split into kick / no-kick runs.
- Envelopes: kick (<120 Hz) and full-band RMS, one value per 60 fps frame, normalised 0-1.
- Words: WhisperX via scripts/align_words.py in .venv-align (forced to --lyrics text when given).
- --trim: cut the audio to N whole bars starting at bar START (written next to the JSON as .wav),
  then analyse the cut file.
"""
import argparse
import json
import subprocess
from pathlib import Path

import librosa
import numpy as np
import scipy.signal as ss

SR = 44100
FPS = 60
ROOT = Path(__file__).resolve().parents[1]


def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).astype(np.float64)


def lowpass(y, hz):
    return ss.sosfiltfilt(ss.butter(4, hz, fs=SR, output="sos"), y)


def smooth_env(x):
    """Hilbert amplitude envelope, zero-phase smoothed at 60 Hz."""
    return ss.sosfiltfilt(ss.butter(2, 60, fs=SR, output="sos"), np.abs(ss.hilbert(x)))


def onset_envs(y):
    y22 = librosa.resample(y, orig_sr=SR, target_sr=22050)
    hop = 64
    S = np.abs(librosa.stft(y22, n_fft=1024, hop_length=hop))
    f = librosa.fft_frequencies(sr=22050, n_fft=1024)
    full = librosa.onset.onset_strength(S=librosa.amplitude_to_db(S, ref=np.max), sr=22050, hop_length=hop)
    low = librosa.onset.onset_strength(S=librosa.amplitude_to_db(S[f < 200], ref=np.max), sr=22050, hop_length=hop)
    t = librosa.frames_to_time(np.arange(len(full)), sr=22050, hop_length=hop)
    return t, full / full.max(), low / low.max()


def comb(t, env, bpm, bins=200):
    """Fold env modulo the beat period; return (peak bin mass, phase of the peak)."""
    per = 60.0 / bpm
    h = np.bincount(((t % per) / per * bins).astype(int) % bins, weights=env, minlength=bins)
    h = np.convolve(np.r_[h[-2:], h, h[:2]], np.ones(5) / 5, mode="valid")
    k = int(np.argmax(h))
    return h[k], (k + 0.5) / bins * per


def attack_times(env, grid, w=0.08):
    """Per grid beat: time the envelope first crosses 50% between window min and peak (None if no attack)."""
    out = []
    n = int(w * SR)
    for g in grid:
        c = int(g * SR)
        s0, s1 = max(0, c - n), min(len(env), c + n)
        seg = env[s0:s1]
        if len(seg) < n or seg.max() < 0.02 * env.max():
            out.append(None)
            continue
        pk = int(np.argmax(seg))
        pre = seg[: pk + 1]
        if pre.min() * 2 > seg[pk]:
            out.append(None)
            continue
        thr = pre.min() + 0.5 * (seg[pk] - pre.min())
        out.append((s0 + int(np.argmax(pre >= thr))) / SR)
    return out


def beat_grid(y):
    dur = len(y) / SR
    t, full, low = onset_envs(y)
    env = full + low
    # BPM range 85-170 holds exactly one octave of any tempo, so no half/double ambiguity.
    bpms = np.arange(85.0, 170.0, 0.01)
    best = bpms[int(np.argmax([comb(t, env, b)[0] for b in bpms]))]
    fine = np.arange(best - 0.02, best + 0.02, 0.001)
    fits = [comb(t, env, b) for b in fine]
    bpm = float(fine[int(np.argmax([f[0] for f in fits]))])
    per = 60.0 / bpm
    phase = fits[int(np.argmax([f[0] for f in fits]))][1]
    # The comb peak can sit on the off-beat (hats/claps); the beat is where the kick is:
    # compare the <80 Hz waveform envelope peak just after grid beats vs just after off-beats.
    kick = smooth_env(lowpass(y, 80))
    grid = np.arange(phase, dur - per, per)

    def peak(times):
        return np.mean([kick[int((x - 0.03) * SR):int((x + 0.06) * SR)].max() for x in times if x > 0.03])

    if peak(grid + per / 2) > peak(grid):
        phase += per / 2
    phase %= per
    # Anchor the phase to hi-band (>3 kHz) waveform attacks: median offset of attack from grid beat.
    hi = smooth_env(ss.sosfiltfilt(ss.butter(2, 3000, fs=SR, btype="high", output="sos"), y))
    grid = np.arange(phase, dur, per)
    off = np.array([x - g for x, g in zip(attack_times(hi, grid), grid) if x is not None])
    shift = float(np.median(off))
    return per, (phase + shift) % per, len(off), len(grid), float(np.median(np.abs(off - shift)))


def low_db(y, times, length):
    """<80 Hz RMS in dB over [t, t + length) for each t."""
    lo = lowpass(y, 80)
    return np.array([20 * np.log10(np.sqrt(np.mean(lo[int(t * SR):int((t + length) * SR)] ** 2)) + 1e-9)
                     for t in times])


def downbeat_offset(y, beats, per, bpb):
    """Beat-in-bar position where the low band changes most (kick in/out lands on bar lines).
    Novelty = |mean dB of next 2 beats - previous 2|, kept only at local maxima (+-2 beats), folded mod bpb."""
    L = low_db(y, beats, per)
    nv = np.array([abs(L[j:j + 2].mean() - L[j - 2:j].mean()) if 2 <= j <= len(L) - 2 else 0.0
                   for j in range(len(L))])
    pk = np.where(nv == np.array([nv[max(0, j - 2):j + 3].max() for j in range(len(nv))]), nv, 0.0)
    if pk.max() < 6:  # no clear section change: assume the audio starts on a downbeat
        return 0
    return int(np.argmax([(pk[o::bpb] ** 2).sum() for o in range(bpb)]))


def sections_from(y, bars, bar_len, dur):
    """A bar has kick when its <80 Hz level is within 12 dB of the loud bars (90th percentile)."""
    db = low_db(y, bars, bar_len)
    kick = db > np.percentile(db, 90) - 12
    secs, start = [], 0
    for i in range(1, len(bars) + 1):
        if i == len(bars) or kick[i] != kick[start]:
            secs.append({"start": start, "end": i, "kick": bool(kick[start])})
            start = i
    out = []
    for j, s in enumerate(secs):
        name = "groove" if s["kick"] else ("intro" if j == 0 else "outro" if j == len(secs) - 1 else "break")
        out.append({"name": name, "start": 0.0 if j == 0 else round(float(bars[s["start"]]), 4),
                    "end": round(dur if j == len(secs) - 1 else float(bars[s["end"]]), 4),
                    "startBar": s["start"], "kick": s["kick"]})
    return out


def envelopes(y, dur):
    n = int(np.ceil(dur * FPS))
    half = SR // (2 * FPS)
    centers = (np.arange(n) * SR / FPS).astype(int)

    def rms(x):
        c = np.r_[0, np.cumsum(x**2)]
        a, b = np.clip(centers - half, 0, len(x)), np.clip(centers + half, 0, len(x))
        v = np.sqrt((c[b] - c[a]) / np.maximum(b - a, 1))
        return np.round(np.clip(v / np.percentile(v, 99.5), 0, 1), 4).tolist()

    return {"hop": round(1 / FPS, 6), "kick": rms(lowpass(y, 120)), "rms": rms(y)}


def get_words(path, lyrics, out_json):
    aligner = ROOT / ".venv-align/bin/python"
    if not aligner.exists():
        raise SystemExit(f"Word alignment needs {aligner} (WhisperX; run make setup-align, see docs/GUIDE.md, Timing). "
                         "Re-run with --beats-only to skip words: beats, bars and sections still work.")
    tmp = out_json.with_suffix(".words.tmp.json")
    cmd = [str(ROOT / ".venv-align/bin/python"), str(ROOT / "scripts/align_words.py"), str(path), str(tmp)]
    if lyrics:
        cmd += ["--lyrics", str(lyrics)]
    subprocess.run(cmd, check=True, capture_output=True)
    words = json.load(open(tmp))["words"]
    tmp.unlink()
    # Fill words the aligner could not place by interpolating between placed neighbours.
    known = [i for i, w in enumerate(words) if w["start"] is not None]
    for i, w in enumerate(words):
        if w["start"] is None:
            ks = np.array(known)
            w["start"] = w["end"] = float(np.interp(i, ks, [words[k]["start"] for k in known]))
        w["start"], w["end"] = round(w["start"], 3), round(w["end"], 3)
        w["text"] = w["text"].strip()
    if not lyrics:  # group by gaps instead of Whisper segments
        line = 0
        for i, w in enumerate(words):
            if i and w["start"] - words[i - 1]["end"] > 0.4:
                line += 1
            w["line"] = line
    else:  # renumber so lines[] indices are dense
        ids = {l: j for j, l in enumerate(sorted({w["line"] for w in words}))}
        for w in words:
            w["line"] = ids[w["line"]]
    lines = []
    for l in range(max((w["line"] for w in words), default=-1) + 1):
        ws = [w for w in words if w["line"] == l]
        lines.append({"text": " ".join(w["text"] for w in ws), "start": ws[0]["start"], "end": ws[-1]["end"]})
    return words, lines


def trim(path, t0, length, out_wav):
    s0, s1 = int(round(t0 * SR)), int(round((t0 + length) * SR))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(path), "-af",
                    f"aresample={SR},atrim=start_sample={s0}:end_sample={s1},asetpts=PTS-STARTPTS", str(out_wav)],
                   check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--lyrics")
    ap.add_argument("--beats-per-bar", type=int, default=4)
    ap.add_argument("--trim", nargs=2, type=int, metavar=("START_BAR", "N_BARS"))
    ap.add_argument("--beats-only", "--no-words", dest="no_words", action="store_true",
                    help="skip word alignment (no .venv-align needed)")
    a = ap.parse_args()
    out, bpb, path = Path(a.out), a.beats_per_bar, Path(a.audio)
    out.parent.mkdir(parents=True, exist_ok=True)

    y = load(path)
    per, phase, n_fit, n_grid, resid = beat_grid(y)
    beats = np.arange(phase, len(y) / SR, per)
    off = downbeat_offset(y, beats, per, bpb)
    if a.trim:  # cut whole bars, then shift the full-song grid so bar 0 starts at t=0
        t0 = beats[off] + a.trim[0] * bpb * per
        path = out.with_suffix(".wav")
        trim(a.audio, t0, a.trim[1] * bpb * per, path)
        y = load(path)
        phase, off = 0.0, 0  # t0 is a grid beat
    dur = len(y) / SR
    beats = np.arange(phase, dur, per)
    bars = beats[off::bpb]
    bar_len = per * bpb
    sections = sections_from(y, bars, bar_len, dur)
    words, lines = ([], []) if a.no_words else get_words(path, a.lyrics, out)

    res = {
        "audio": path.name, "duration": round(dur, 4), "fps": FPS,
        "bpm": round(60 / per, 4), "beatPeriod": round(per, 6), "beatsPerBar": bpb,
        "beats": np.round(beats, 4).tolist(), "bars": np.round(bars, 4).tolist(),
        "mode": "beats-only" if a.no_words else "words",
        "words": words, "lines": lines, "sections": sections, "envelopes": envelopes(y, dur),
    }
    json.dump(res, open(out, "w"))
    secs = " ".join(f"{s['name']}@bar{s['startBar']}" for s in sections)
    print(f"{out}: {res['bpm']:.3f} BPM, downbeat {bars[0]:.3f}s, bar {bar_len:.4f}s, {len(bars)} bars "
          f"({(dur - bars[0]) / bar_len:.3f} after downbeat), attacks {n_fit}/{n_grid} beats "
          f"(median scatter {resid * 1000:.1f} ms), sections {secs}, {len(words)} words")


if __name__ == "__main__":
    main()
