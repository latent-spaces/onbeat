"""Build one local HyperFrames project from timing.json and optional reel.json.

python3 scripts/build_reel.py --song songs/my-song --out out/projects/my-song
Uses Python's standard library and ffmpeg. Never deletes an input directory.
"""
import argparse
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "video/template"
SRC = ROOT / "video/src"
MARKER = ".music-reel-project"
DEFAULT_CONFIG = {
    "title": "", "subtitle": "",
    "palette": {"bg1": "#f6f0df", "bg2": "#f6f0df", "accent": "#ed553b", "ink": "#182e33", "sung": "#182e33"},
    "captions": [], "captionBars": 2, "lyricsY": 290,
    "cast": [{"name": "robot-dance", "phase": 0}], "syncCheck": False,
}


def read_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc


def number(value, name, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{name} must be a finite number")
    if value < 0 or (positive and value == 0):
        raise ValueError(f"{name} must be {'positive' if positive else 'non-negative'}")
    return value


def validate_output(raw, song):
    song = song.resolve()
    if raw.is_symlink():
        raise ValueError("output must not be a symlink")
    out = raw.resolve()
    if out == song or song.is_relative_to(out) or out.is_relative_to(song):
        raise ValueError("output must not overlap the song folder")
    if out == ROOT or ROOT.is_relative_to(out) or (out.is_relative_to(ROOT) and not out.is_relative_to(ROOT / 'out')):
        raise ValueError("inside this repo, output must be under out/")
    if out.exists() and (not out.is_dir() or (any(out.iterdir()) and not (out / MARKER).is_file())):
        raise ValueError("output is not an empty or generated project; choose a new directory")
    return out


def load_inputs(song):
    timing = read_json(song / "timing.json")
    if not isinstance(timing, dict):
        raise ValueError("timing.json must be an object")
    duration = number(timing.get("duration"), "duration", positive=True)
    number(timing.get("beatPeriod"), "beatPeriod", positive=True)
    for key in ("beats", "bars"):
        values = timing.get(key)
        if not isinstance(values, list) or not values:
            raise ValueError(f"timing.json needs non-empty {key}")
        for value in values:
            number(value, key)
            if value >= duration:
                raise ValueError(f"{key} must be before duration")
        if values != sorted(set(values)):
            raise ValueError(f"{key} must be sorted without duplicates")
    for key in ("words", "lines", "sections"):
        timing.setdefault(key, [])
        if not isinstance(timing[key], list):
            raise ValueError(f"{key} must be an array")
        for item in timing[key]:
            if not isinstance(item, dict):
                raise ValueError(f"{key} entries must be objects")
            start = number(item.get("start"), f"{key}.start")
            end = number(item.get("end"), f"{key}.end")
            if start >= duration or end < start or end > duration + .05:
                raise ValueError(f"invalid {key} time window")
    timing["fps"] = 30
    supplied = read_json(song / "reel.json") if (song / "reel.json").exists() else {}
    if not isinstance(supplied, dict):
        raise ValueError("reel.json must be an object")
    config = {**DEFAULT_CONFIG, "title": song.name.replace("-", " "), **supplied}
    config["palette"] = dict(DEFAULT_CONFIG["palette"], **supplied.get("palette", {}))
    for key, value in config["palette"].items():
        if not isinstance(value, str) or not re.fullmatch(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?", value):
            raise ValueError(f"palette.{key} must be a hex colour")
    for key in ("title", "subtitle"):
        if not isinstance(config[key], str) or len(config[key]) > 120:
            raise ValueError(f"{key} must be text of at most 120 characters")
    if not isinstance(config["cast"], list) or len(config["cast"]) > 3:
        raise ValueError("cast must be an array with at most three members")
    if not isinstance(config["captions"], list) or not all(isinstance(x, str) for x in config["captions"]):
        raise ValueError("captions must be an array of text")
    number(config["captionBars"], "captionBars", positive=True)
    if not isinstance(config["captionBars"], int):
        raise ValueError("captionBars must be an integer")
    if "captionStartBar" in config:
        number(config["captionStartBar"], "captionStartBar")
        if not isinstance(config["captionStartBar"], int):
            raise ValueError("captionStartBar must be an integer")
    audio_names = [timing.get("audio", ""), "song.mp3", "song.m4a", "song.wav", "song.flac", "song.ogg", "song.aiff"]
    audio = next((song / n for n in audio_names if n and Path(n).name == n and (song / n).is_file()), None)
    if audio is None:
        raise ValueError("no audio: put song.mp3, .m4a, .wav, .flac, .ogg or .aiff in the song folder")
    sprites = song / "sprites"
    if not (sprites / "sprites.json").exists():
        sprites = ROOT / "video/assets/disco"
    manifest = read_json(sprites / "sprites.json") if config["cast"] else {"sprites": {}}
    if config["cast"] and not (SRC / "spritedance.js").exists():
        raise ValueError("shared SpriteDance helper is missing; update the package")
    if config["syncCheck"] and not (SRC / "synccheck.js").exists():
        raise ValueError("shared sync-check helper is missing; update the package")
    for member in config["cast"]:
        if not isinstance(member, dict) or member.get("name") not in manifest.get("sprites", {}):
            raise ValueError("each cast member needs a name present in sprites.json")
        sheet = manifest["sprites"][member["name"]]
        file = (sprites / sheet["file"]).resolve()
        if not file.is_relative_to(sprites.resolve()) or not file.is_file():
            raise ValueError("sprite file must exist within its sprites folder")
    return timing, config, audio, sprites, manifest


def build(song, out, sync_check=False):
    song = song.resolve()
    out = validate_output(out, song)
    timing, config, audio, sprites, manifest = load_inputs(song)
    if sync_check:
        config["syncCheck"] = True
    out.parent.mkdir(parents=True, exist_ok=True)
    # Assemble first. Invalid input or failed conversion leaves an existing project untouched.
    with tempfile.TemporaryDirectory(prefix=".reel-build-", dir=out.parent) as temp:
        project = Path(temp)
        for folder in ("assets", "data", "src"):
            (project / folder).mkdir()
        shutil.copy(TEMPLATE / "assets/gsap.min.js", project / "assets")
        shutil.copy(TEMPLATE / "reel-extras.js", project)
        shutil.copy(TEMPLATE / "hyperframes.json", project)
        scripts = []
        for js in sorted(SRC.glob("*.js")):
            shutil.copy(js, project / "src")
            scripts.append(f'  <script src="src/{js.name}"></script>')
        selected = {member["name"]: manifest["sprites"][member["name"]] for member in config["cast"]}
        (project / "assets/cast").mkdir()
        for sheet in selected.values():
            target = project / "assets/cast" / sheet["file"]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(sprites / sheet["file"], target)
        (project / "data/sprites.js").write_text("window.SPRITES = " + json.dumps({"sprites": selected}) + ";\n")
        scripts.append('  <script src="data/sprites.js"></script>')
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(audio), "-ar", "48000", "-ac", "2", "-t", str(timing["duration"]), str(project / "assets/song.wav")], check=True)
        (project / "data/timing.js").write_text("window.TIMING = " + json.dumps(timing) + ";\n")
        (project / "data/config.js").write_text("window.REEL = " + json.dumps(config) + ";\n")
        html = (TEMPLATE / "index.html").read_text().replace("{{DURATION}}", str(timing["duration"])).replace("{{FPS}}", "30").replace("{{SRC_SCRIPTS}}", "\n".join(scripts))
        (project / "index.html").write_text(html)
        (project / MARKER).write_text("Generated by scripts/build_reel.py\n")
        # Reject link destinations before copying any generated file.
        for source in project.rglob("*"):
            if (out / source.relative_to(project)).is_symlink():
                raise ValueError("generated output contains a symlink; choose a new directory")
        # Update only generated names; unrelated files in a marked project remain intact.
        shutil.copytree(project, out, dirs_exist_ok=True)
    print(f"Built {out} ({timing['duration']:.2f}s). Next: check and render this project.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--song", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--sync-check", action="store_true")
    args = parser.parse_args()
    try:
        build(args.song, args.out, args.sync_check)
    except (ValueError, OSError, subprocess.CalledProcessError, TypeError, KeyError) as exc:
        sys.stderr.write(f"build_reel: {exc}\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
