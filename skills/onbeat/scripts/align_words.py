"""Word timing helper for timing.py. Needs Python 3.12 with requirements-align.txt installed.

Usage: python align_words.py <audio.wav> <out.json> [--lyrics lyrics.txt] [--language en]

The vocals are first isolated with Demucs (htdemucs); both steps run on the vocal stem, which is what
makes Whisper hear the sung words at all (on the full mix it skipped most of them).
Always: faster-whisper transcription (large-v3-turbo, CPU int8) of short voiced clips + WhisperX wav2vec2
forced alignment.
With --lyrics: the given text is then force-aligned line by line instead, each line inside the time
window where the transcription heard its words (so the output text is exactly the lyric file).
Writes {"words": [{"text", "start", "end", "line"}]}; "line" is the lyric-file line index, or the
Whisper segment index when no lyrics are given. Words the aligner could not place get start/end null.
"""
import argparse
import difflib
import json
import re
import sys

import demucs.api
import torch
import torchaudio
import whisperx
from faster_whisper import WhisperModel
from word_times import valid_words

ap = argparse.ArgumentParser()
ap.add_argument("audio")
ap.add_argument("out")
ap.add_argument("--lyrics")
ap.add_argument("--language", default="en")
a = ap.parse_args()

sep = demucs.api.Separator(model="htdemucs", device="mps" if torch.backends.mps.is_available() else "cpu")
_, stems = sep.separate_audio_file(a.audio)
vocals = stems["vocals"].mean(0).cpu()
audio = torchaudio.functional.resample(vocals, sep.samplerate, 16000).numpy().astype("float32")
dur = len(audio) / 16000

# Vocal-stem silence mask (5 ms frames, > 35 dB below the loud frames).
hop = 80
x = torch.from_numpy(audio)
env = 20 * torch.log10(x[: len(x) // hop * hop].reshape(-1, hop).pow(2).mean(1).sqrt() + 1e-9)
silent = (env < torch.quantile(env, 0.95) - 35).numpy()
env = env.numpy()

# Whisper on long sung stretches silently drops lines and varies run to run (WhisperX's VAD-batched
# path heard 19 of ~60 words on one reel). Decoding short clips is stable: clips are voiced regions
# (gaps < 0.3 s bridged), split to <= 6 s at the quietest frame in the back 40% of the allowed length.
fps = 16000 / hop
clips, start, last = [], None, None
for i in [*map(int, (~silent).nonzero()[0]), None]:
    if i is not None and start is not None and i - last <= 0.3 * fps:
        last = i
        continue
    if start is not None and last - start >= 0.1 * fps:
        c0, c1 = max(start - 10, 0), min(last + 10, len(env) - 1)
        while c1 - c0 > 6 * fps:
            cut = c0 + int(3.6 * fps) + int(env[c0 + int(3.6 * fps):c0 + int(6 * fps)].argmin())
            clips += [c0 / fps, cut / fps]
            c0 = cut
        clips += [c0 / fps, c1 / fps]
    start = last = i
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")
segs, _ = model.transcribe(audio, language=a.language, vad_filter=False, condition_on_previous_text=False,
                           clip_timestamps=clips or "0")
segments = [{"text": s.text, "start": s.start, "end": s.end} for s in segs]
amodel, meta = whisperx.load_align_model(language_code=a.language, device="cpu")
aligned = whisperx.align(segments, amodel, meta, audio, "cpu")["segments"]

words = []
if not a.lyrics:
    for line, s in enumerate(aligned):
        for w in s["words"]:
            words.append({"text": w["word"], "start": w.get("start"), "end": w.get("end"), "line": line})
else:
    # Force-align the given lyrics line by line. Each line's time window comes from the transcription:
    # lyric words are matched to heard words (difflib, runs of 2+ words), and a line spans its matched words (+-0.3 s);
    # lines with no match fill the gap between their neighbours.
    lines = [l.split() for l in open(a.lyrics, encoding="utf-8").read().splitlines()]
    lines = [l for l in lines if l]
    tokens = [(w, i) for i, l in enumerate(lines) for w in l]
    norm = lambda w: re.sub(r"[^a-z0-9']", "", w.lower())  # noqa: E731
    hw = [w for s in aligned for w in s["words"] if w.get("start") is not None]
    sm = difflib.SequenceMatcher(None, [norm(t) for t, _ in tokens], [norm(w["word"]) for w in hw], autojunk=False)
    span = {}
    for blk in [b for b in sm.get_matching_blocks() if b.size >= 2]:  # lone-word matches are often wrong
        for k in range(blk.size):
            li = tokens[blk.a + k][1]
            w = hw[blk.b + k]
            s0, e0 = span.get(li, (w["start"], w["end"]))
            span[li] = (min(s0, w["start"]), max(e0, w["end"]))
    segs = []
    for i, l in enumerate(lines):
        prev_end = max([span[j][1] for j in span if j < i], default=0.0)
        next_start = min([span[j][0] for j in span if j > i], default=dur)
        s0, e0 = span.get(i, (prev_end, next_start))
        segs.append({"text": " ".join(l), "start": max(prev_end, s0 - 0.3), "end": min(next_start, e0 + 0.3)})
    got = []
    for seg in segs:  # one align call per line so a line's words stay inside its window
        out = whisperx.align([seg], amodel, meta, audio, "cpu")["segments"]
        ws = [w for s in out for w in s["words"]]
        assert len(ws) == len(seg["text"].split()), (seg["text"], len(ws))
        got += ws
    for (text, line), w in zip(tokens, got):
        words.append({"text": text, "start": w.get("start"), "end": w.get("end"), "line": line})

# wav2vec2 often places a word that follows a pause late (up to ~0.2 s) on sung vocals. For such words,
# if the vocal stem goes silent within 0.25 s before the aligned start, move the start to where the
# voice comes back in. Words inside continuous singing are left alone (no evidence to move them).
words, rejected = valid_words(words, dur)
for w in rejected:
    print(f"Skipped out-of-range word: {w}", file=sys.stderr)
prev_end = 0.0
for w in words:
    if w["start"] is None:
        continue
    if w["start"] - prev_end >= 0.15:
        i = min(len(silent), int(w["start"] * 16000 / hop))
        lo = max(int(max(prev_end, w["start"] - 0.25) * 16000 / hop), 0)
        sil = [j for j in range(lo, i) if silent[j]]
        if sil:
            w["start"] = round((sil[-1] + 1) * hop / 16000, 3)
    prev_end = w["end"]

json.dump({"words": words, "language": a.language}, open(a.out, "w"))
