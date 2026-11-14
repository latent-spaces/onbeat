"""Build a renderable HyperFrames project for one song from the song-agnostic template.

Usage (from anywhere):
  python3 scripts/build_reel.py --song songs/<name> --out out/projects/<name>

Reads   songs/<name>/timing.json   (from `make timing`; beats only is enough)
        songs/<name>/song.(mp3|m4a|wav)
        songs/<name>/reel.json     (template config; written with defaults if missing)
        songs/<name>/sprites/      (optional: sprites.json + sheets, see docs/sprites.md)
Writes  <out>/index.html, assets/song.wav, data/timing.js, data/config.js, src/*.js
Then:   cd <out> && npx --yes hyperframes@0.9.2 render --output ../../<name>.mp4

Standard library only, plus ffmpeg on PATH for the audio conversion.
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "video" / "template"
SRC = ROOT / "video" / "src"
AUDIO_NAMES = ("song.mp3", "song.m4a", "song.wav")
RENDER_FPS = 30

DEFAULT_CONFIG = {
    "title": "",
    "subtitle": "",
    "palette": {"bg1": "#1b1033", "bg2": "#3a1450", "accent": "#ff4fa3", "ink": "#fff2c4", "sung": "#ffd34d"},
    "captions": [],
    "captionBars": 2,
    "lyricsY": 260,
    "cast": [],
    "syncCheck": False,
}


SENTINEL = ".music-reel-build"
GENERATED = ("index.html", "reel-extras.js", "hyperframes.json", "assets", "data", "src", SENTINEL)


def guard_output(out, song_dir):
    """Refuse output folders that could hold the person's files: only a new or empty folder,
    or one this script built before (it has the sentinel file), and never one that overlaps
    the repo's sources or the song folder."""
    for src in (ROOT / "video", ROOT / "scripts", ROOT / "songs", song_dir):
        if out.is_relative_to(src) or src.is_relative_to(out):
            fail("refusing --out " + str(out) + ": it overlaps " + str(src))
    if out == ROOT or ROOT.is_relative_to(out):
        fail("refusing --out " + str(out) + ": it contains the repo")
    if out.exists() and any(out.iterdir()) and not (out / SENTINEL).exists():
        fail("refusing --out " + str(out) + ": not empty and not built by build_reel.py (no " + SENTINEL + ")")


def fail(msg):
    sys.stderr.write("build_reel: " + msg + "\n")
    sys.exit(1)


def load_config(song_dir):
    path = song_dir / "reel.json"
    if not path.exists():
        cfg = dict(DEFAULT_CONFIG, title=song_dir.name.replace("-", " "))
        lyrics = song_dir / "lyrics.txt"
        if lyrics.exists():  # beats-only captions: one lyric line per two bars
            cfg["captions"] = [l.strip() for l in lyrics.read_text().splitlines() if l.strip() and not l.startswith("[")]
        path.write_text(json.dumps(cfg, indent=2) + "\n")
        print("wrote default " + str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path))
    cfg = json.loads(path.read_text())
    merged = dict(DEFAULT_CONFIG, **cfg)
    merged["palette"] = dict(DEFAULT_CONFIG["palette"], **cfg.get("palette", {}))
    return merged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--song", required=True, help="song folder, e.g. songs/my-song")
    ap.add_argument("--out", required=True, help="project folder to (re)build, e.g. out/projects/my-song")
    ap.add_argument("--sync-check", action="store_true", help="force the sync-check overlay on")
    a = ap.parse_args()

    song_dir = Path(a.song).resolve()
    out = Path(a.out).resolve()
    if not song_dir.is_dir():
        fail("no song folder " + a.song)
    timing_path = song_dir / "timing.json"
    if not timing_path.exists():
        fail("no " + str(timing_path) + " (run: make timing SONG=" + song_dir.name + ")")
    audio = next((song_dir / n for n in AUDIO_NAMES if (song_dir / n).exists()), None)
    if audio is None:
        fail("no audio in " + str(song_dir) + " (expected one of " + ", ".join(AUDIO_NAMES) + ")")

    timing = json.loads(timing_path.read_text())
    for key in ("duration", "beats", "bars", "beatPeriod"):
        if key not in timing:
            fail("timing.json has no '" + key + "'")
    timing.setdefault("words", [])
    timing.setdefault("lines", [])
    timing.setdefault("sections", [])
    timing["fps"] = RENDER_FPS
    cfg = load_config(song_dir)
    if a.sync_check:
        cfg["syncCheck"] = True

    guard_output(out, song_dir)
    if out.exists():
        for name in GENERATED:  # replace only what this script wrote; leave anything else alone
            p = out / name
            if p.is_dir() and not p.is_symlink():
                shutil.rmtree(p)
            elif p.exists() or p.is_symlink():
                p.unlink()
    (out / "data").mkdir(parents=True)
    (out / "src").mkdir()
    shutil.copytree(TEMPLATE / "assets", out / "assets")
    shutil.copy(TEMPLATE / "reel-extras.js", out / "reel-extras.js")
    shutil.copy(TEMPLATE / "hyperframes.json", out / "hyperframes.json")
    scripts = []
    for js in sorted(SRC.glob("*.js")):
        shutil.copy(js, out / "src" / js.name)
        scripts.append('  <script src="src/' + js.name + '"></script>')

    sprites_dir = song_dir / "sprites"
    if sprites_dir.is_dir() and (sprites_dir / "sprites.json").exists():
        shutil.copytree(sprites_dir, out / "assets" / "cast")
        sheets = json.loads((sprites_dir / "sprites.json").read_text())
        (out / "data" / "sprites.js").write_text("window.SPRITES = " + json.dumps(sheets) + ";\n")
        scripts.append('  <script src="data/sprites.js"></script>')

    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(audio), "-ar", "48000", "-ac", "2",
                    "-t", str(timing["duration"]), str(out / "assets" / "song.wav")], check=True)
    (out / "data" / "timing.js").write_text("window.TIMING = " + json.dumps(timing) + ";\n")
    (out / "data" / "config.js").write_text("window.REEL = " + json.dumps(cfg) + ";\n")

    html = (TEMPLATE / "index.html").read_text()
    html = (html.replace("{{DURATION}}", str(round(float(timing["duration"]), 4)))
                .replace("{{FPS}}", str(RENDER_FPS))
                .replace("{{SRC_SCRIPTS}}", "\n".join(scripts)))
    (out / "index.html").write_text(html)
    (out / SENTINEL).write_text("generated by scripts/build_reel.py; safe to delete\n")
    mode = "karaoke" if timing["words"] else ("lines" if timing["lines"] else ("captions" if cfg["captions"] else "beats only"))
    print("built %s: %.1f s, %s bpm, %d bars, lyrics: %s" % (out, timing["duration"], timing.get("bpm", "?"), len(timing["bars"]), mode))


if __name__ == "__main__":
    main()
