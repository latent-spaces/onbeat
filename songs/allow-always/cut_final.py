"""Write the final take's audio and timing data for the video project.

Run from the repo root:  .venv/bin/python songs/allow-always/cut_final.py
Reads  out/timing/allow-always-final.json (from scripts/timing.py) and songs/allow-always/take-final-yes.mp3.
Writes out/dev/allow-always-final.wav, video/data/allow-always-final.json and video/data/allow-always-final.js.
"""
import json
import subprocess

SRC = "songs/allow-always/take-final-yes.mp3"

t = json.load(open("out/timing/allow-always-final.json"))

subprocess.run(
    ["ffmpeg", "-y", "-v", "error", "-i", SRC, "-ar", "48000", "out/dev/allow-always-final.wav"],
    check=True,
)
t["audio"] = "assets/dev/allow-always-final.wav"

json.dump(t, open("video/data/allow-always-final.json", "w"))
open("video/data/allow-always-final.js", "w").write("window.TIMING = " + json.dumps(t) + ";\n")
print(f"{t['duration']} s, {t['bpm']} bpm, {len(t['bars'])} bars, {len(t['lines'])} lines")
for s in t["sections"]:
    print("section", s["name"], s["startBar"], s["start"], "kick" if s["kick"] else "")
for i, l in enumerate(t["lines"]):
    print(i, l["start"], l["end"], l["text"])
