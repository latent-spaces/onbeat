"""Cut take2-short to the 31-bar reel and write its timing data for the video project.

Run from the repo root:  .venv/bin/python songs/allow-always/cut.py
Reads  out/timing/allow-always-short.json (from scripts/timing.py) and songs/allow-always/take2-short.m4a.
Writes out/dev/allow-always.wav, video/data/allow-always.json and video/data/allow-always.js.
"""
import json
import subprocess

SRC = "songs/allow-always/take2-short.m4a"
END_BAR = 30  # index in the analysed grid: the kick re-entry after the final "no"
FADE = 0.02

t = json.load(open("out/timing/allow-always-short.json"))
end = t["bars"][END_BAR]

subprocess.run(
    ["ffmpeg", "-y", "-v", "error", "-i", SRC, "-t", f"{end:.4f}",
     "-af", f"afade=t=out:st={end - FADE:.4f}:d={FADE}", "-ar", "48000", "out/dev/allow-always.wav"],
    check=True,
)

# The analysed grid starts one bar late: the song's first downbeat is 19 ms before the file start.
# Add that bar at 0 so bar numbers count from the start of the clip.
t["beats"] = [0.0] + [b for b in t["beats"] if b < end - 1e-3]
t["bars"] = [0.0] + [b for b in t["bars"] if b < end - 1e-3]
t["sections"] = [
    {**s, "startBar": s["startBar"] + (1 if s["start"] > 0 else 0), "end": min(s["end"], end)}
    for s in t["sections"] if s["start"] < end - 1e-3
]

# The aligner misplaced the last two lines. Times below are from a transcription of the last
# 15 s of the full mix (diagnostics/allow-always/tail_words.py) and the vocal-stem level.
FIX = {
    25: [("may", 54.44, 54.62), ("i", 54.62, 54.86), ("read", 54.86, 55.10), ("my", 55.10, 55.44), ("file", 55.44, 56.14)],
    26: [("no", 59.10, 59.40)],
}
words = [w for w in t["words"] if w["line"] not in FIX]
for line, ws in FIX.items():
    words += [{"text": x, "start": s, "end": e, "line": line} for x, s, e in ws]
    t["lines"][line]["start"], t["lines"][line]["end"] = ws[0][1], ws[-1][2]
t["words"] = sorted(words, key=lambda w: w["start"])

n = int(end * t["fps"]) + 1
t["envelopes"]["kick"] = t["envelopes"]["kick"][:n]
t["envelopes"]["rms"] = t["envelopes"]["rms"][:n]
t["duration"] = round(end, 4)
t["audio"] = "assets/dev/allow-always.wav"

json.dump(t, open("video/data/allow-always.json", "w"))
open("video/data/allow-always.js", "w").write("window.TIMING = " + json.dumps(t) + ";\n")
print(f"{t['duration']} s, {len(t['bars'])} bars, {len(t['beats'])} beats, {len(t['lines'])} lines")
for i, l in enumerate(t["lines"]):
    print(i, l["start"], l["text"])
