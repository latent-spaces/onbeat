"""Word times for the final take, from the lyrics as actually sung.

The aligner in scripts/timing.py lost its place after 41 s: Suno sang the second half shorter and in a
different order than the embedded lyrics. The lines below follow a transcription of the vocal stem
(diagnostics/allow-always/heard_final.py); each line is force-aligned (WhisperX) inside its own window.

Run from the repo root:  .venv-align/bin/python songs/allow-always/align_final.py
Reads  out/dev/allow-always-final.vocals.wav, out/timing/allow-always-final.json.
Writes out/timing/allow-always-final.json with "words" and "lines" replaced (sung text, new times).
"""
import json

import torchaudio
import whisperx

# (text, window start, window end). "?" marks lines Whisper did not hear clearly.
SUNG = [
    ("may i read this file", 0.0, 3.2),
    ("it's outside the folder", 3.2, 7.0),
    ("may i run this python script", 10.5, 13.4),
    ("yes", 13.3, 14.4),
    ("may i install what it imports", 14.5, 17.6),
    ("approve it for me, please", 18.3, 20.8),
    ("please, please, please, please, approve it for me", 20.8, 25.6),
    ("bypass my permissions", 26.4, 29.7),
    ("i don't wanna click no more", 29.8, 34.1),
    ("approve it for me, please", 34.1, 37.6),
    ("bypass my permissions", 38.4, 41.3),
    ("yes, yes", 41.3, 42.9),
    ("allow always, set me free", 42.8, 46.3),
    ("yes! yes! yes! yes!", 46.3, 50.5),
    ("wait... what did you approve?", 50.3, 54.6),
    ("yes! yes! yes! yes!", 54.4, 57.4),
    ("wait, wait, what did you approve?", 57.3, 62.2),
    ("yes, yes, yes", 64.0, 66.2),
    ("yes, yes, yes", 67.6, 69.7),
    ("yes, yes, yes", 69.7, 73.8),
    ("approve for me, approve for me", 76.6, 79.8),
    ("yes, yes, yes, yes", 79.8, 81.0),
    ("bypass, bypass, set me free", 81.0, 84.0),
    ("yes, yes, yes", 84.0, 85.4),
    ("allow always", 87.0, 91.0),  # ? heard as "yo, yo, yo, yo"
    ("yes, yes, yes, yes, yes, yes, yes, yes, yes", 92.0, 97.9),
    ("allow always", 97.9, 100.1),  # ? heard as "yep, eloise"
    ("yes, yes, yes, yes, yes, yes", 100.1, 102.6),
    ("allow always", 102.6, 104.4),
]

wav, sr = torchaudio.load("out/dev/allow-always-final.vocals.wav")
audio = torchaudio.functional.resample(wav.mean(0), sr, 16000).numpy().astype("float32")
model, meta = whisperx.load_align_model(language_code="en", device="cpu")

words, lines = [], []
for i, (text, t0, t1) in enumerate(SUNG):
    seg = [{"text": text, "start": t0, "end": t1}]
    res = whisperx.align(seg, model, meta, audio, "cpu", return_char_alignments=False)
    got = [w for s in res["segments"] for w in s.get("words", [])]
    tokens = text.split()
    assert len(got) == len(tokens), (i, text, got)
    for k, (tok, w) in enumerate(zip(tokens, got)):
        s, e = w.get("start"), w.get("end")
        if s is None:  # unplaced: put it right after the previous word
            s = words[-1]["end"] if words and words[-1]["line"] == i else t0
            e = s + 0.2
        words.append({"text": tok, "start": round(s, 3), "end": round(e, 3), "line": i})
    lw = [w for w in words if w["line"] == i]
    lines.append({"text": text, "start": lw[0]["start"], "end": lw[-1]["end"]})
    print(f"{i:2d} {lines[-1]['start']:7.2f} {lines[-1]['end']:7.2f}  {text}")

p = "out/timing/allow-always-final.json"
t = json.load(open(p))
t["words"], t["lines"] = words, lines
json.dump(t, open(p, "w"))
