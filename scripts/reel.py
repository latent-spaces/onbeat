#!/usr/bin/env python3
"""Safe command entry points for music-reels. The bundled sample needs only render tools."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
HF = ["npx", "--yes", "hyperframes@0.9.2"]
AUDIO_SUFFIXES = {".mp3", ".m4a", ".wav", ".flac", ".ogg", ".aiff"}


class UserError(Exception):
    """An actionable input or environment error, without a Python traceback."""


def say(message):
    print(message, flush=True)


def flag(name, default=False):
    value = os.environ.get(name, "").strip().lower()
    if not value:
        return default
    if value not in {"0", "1", "false", "true"}:
        raise UserError(f"{name} must be 0 or 1.")
    return value in {"1", "true"}


def song_name():
    name = os.environ.get("SONG", "").strip()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,79}", name):
        raise UserError("Set SONG to a folder name using letters, digits, - or _: make timing SONG=my-song")
    folder = ROOT / "songs" / name
    if not folder.resolve().is_relative_to((ROOT / "songs").resolve()):
        raise UserError("Song folders must stay inside songs/ (check for an external symlink).")
    return name, folder


def run(command, cwd=ROOT):
    command = [str(part) for part in command]
    say("+ " + shlex.join(command))
    subprocess.run(command, cwd=cwd, check=True)


def capture(command, cwd=ROOT, timeout=90):
    return subprocess.run([str(p) for p in command], cwd=cwd, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)


def venv_python(name=".venv"):
    return ROOT / name / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def check_environment(name, modules, required):
    python = venv_python(name)
    ready = python.is_file()
    if ready:
        result = capture([python, "-c", "; ".join(f"import {module}" for module in modules)])
        ready = result.returncode == 0
    label = "OK" if ready else ("MISSING" if required else "OPTIONAL")
    say(f"[{label}] {name}: " + ("imports ready" if ready else f"run make {'setup-align' if name == '.venv-align' else 'setup'}"))
    return ready or not required


def render_tools():
    good = True
    for name in ("node", "npx", "ffmpeg", "ffprobe"):
        override = os.environ.get(f"HYPERFRAMES_{name.upper()}_PATH") if name in {"ffmpeg", "ffprobe"} else None
        path = override or shutil.which(name)
        exists = bool(path and Path(path).is_file())
        say(f"[{'OK' if exists else 'MISSING'}] {name}" + (f": {path}" if exists else ": install Node 22+ / FFmpeg (including ffprobe)"))
        good = good and exists
    if shutil.which("node"):
        version = capture(["node", "-p", "process.versions.node"]).stdout.strip()
        try:
            supported = int(version.split(".")[0]) >= 22
        except ValueError:
            supported = False
        say(f"[{'OK' if supported else 'MISSING'}] Node version: {version}; 22+ required")
        good = good and supported
    return good


def renderer_report():
    say("Checking HyperFrames 0.9.2 (first use can download the pinned CLI)…")
    result = capture(HF + ["doctor", "--json"], timeout=180)
    if result.returncode:
        raise UserError("HyperFrames diagnostics failed. Run: npx --yes hyperframes@0.9.2 doctor --json\n" + result.stderr[-1200:])
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise UserError("HyperFrames did not return diagnostic JSON. Run its doctor command directly to inspect the error.") from exc


def required_renderer_checks(report):
    """Optional generation tools and update notices do not gate local rendering."""
    checks = {item["name"]: item for item in report.get("checks", [])}
    good = True
    for name in ("Node.js", "FFmpeg", "FFprobe", "Chrome"):
        item = checks.get(name, {})
        ready = item.get("ok") is True
        say(f"[{'OK' if ready else 'MISSING'}] HyperFrames {name}: {item.get('detail', 'not reported')}")
        if not ready:
            say("  Fix: " + ("make browser" if name == "Chrome" else item.get("hint", "install Node 22+ and FFmpeg, then retry make doctor")))
        good = good and ready
    say("[INFO] HyperFrames is pinned to 0.9.2; optional voice/music tools and upgrade notices are not required.")
    return good


def doctor():
    mode = os.environ.get("MODE", "sample").strip() or "sample"
    if mode not in {"sample", "timing", "align"}:
        raise UserError("MODE must be sample, timing or align.")
    say(f"music-reels doctor — {mode} mode")
    say(f"[OK] Python wrapper: {sys.version.split()[0]} (stdlib; no venv needed for sample)")
    good = render_tools()
    if good:
        good = required_renderer_checks(renderer_report()) and good
    good = check_environment(".venv", ["librosa", "numpy", "scipy", "PIL"], mode != "sample") and good
    good = check_environment(".venv-align", ["whisperx", "demucs", "faster_whisper", "torch", "torchaudio"], mode == "align") and good
    if not good:
        raise UserError("Fix the MISSING items, then rerun make doctor. Analysis environments are optional for make sample.")
    say("Ready. " + ("Run make sample; no keys or ML environments needed." if mode == "sample" else "Selected analysis environment is ready."))


def setup(align=False):
    env_name = ".venv-align" if align else ".venv"
    explicit = os.environ.get("PYTHON_SETUP", "").strip()
    candidates = [explicit] if explicit else (["python3.12"] if align else ["python3.14", "python3.12", "python3"])
    chosen = None
    for candidate in candidates:
        path = shutil.which(candidate)
        if not path:
            continue
        result = capture([path, "-c", "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"])
        if result.stdout.strip() in ({"3.12"} if align else {"3.12", "3.13", "3.14"}):
            chosen = path
            break
    if not chosen:
        raise UserError("Install Python 3.12" + (" for alignment." if align else "–3.14, then run make setup PYTHON_SETUP=python3.14. The sample needs no setup."))
    run([chosen, "-m", "venv", ROOT / env_name])
    run([venv_python(env_name), "-m", "pip", "install", "-r", ROOT / ("requirements-align.txt" if align else "requirements.txt")])
    say(f"{env_name} installed. Run make doctor MODE={'align' if align else 'timing'}.")


def input_file(value):
    path = Path(value).expanduser()
    path = path if path.is_absolute() else ROOT / path
    if not path.is_file():
        raise UserError(f"Input file does not exist: {path}")
    return path.resolve()


def timing():
    name, folder = song_name()
    words = flag("WORDS")
    if flag("BEATS_ONLY"):
        if words:
            raise UserError("WORDS=1 conflicts with BEATS_ONLY=1. Choose one mode.")
        words = False
    python = venv_python()
    if not check_environment(".venv", ["librosa", "numpy", "scipy"], True):
        raise UserError("Run make setup before timing your own song. make sample does not need it.")
    if words and not check_environment(".venv-align", ["whisperx", "demucs", "faster_whisper", "torch", "torchaudio"], True):
        raise UserError("Words need make setup-align. Omit WORDS=1 for beats-only timing.")
    explicit_audio = os.environ.get("AUDIO", "").strip()
    candidates = [p for p in folder.glob("song.*") if p.suffix.lower() in AUDIO_SUFFIXES]
    if not explicit_audio and len(candidates) != 1:
        raise UserError(f"Put exactly one song.mp3/.m4a/.wav in songs/{name}/, or set AUDIO=/path/to/song.wav.")
    audio = input_file(explicit_audio) if explicit_audio else candidates[0].resolve()
    if audio.suffix.lower() not in AUDIO_SUFFIXES:
        raise UserError("AUDIO must be an MP3, M4A, WAV, FLAC, OGG or AIFF file.")
    lyrics_value = os.environ.get("LYRICS", "").strip()
    lyrics = input_file(lyrics_value) if lyrics_value else folder / "lyrics.txt"
    if words and not lyrics.is_file():
        raise UserError("WORDS=1 requires the sung lyrics: add songs/<name>/lyrics.txt or set LYRICS=/path/to/lyrics.txt.")
    output = folder / "timing.json"
    if output.exists() and not flag("FORCE"):
        raise UserError(f"{output} already exists. Keep curated timing, or use FORCE=1 to regenerate with a backup.")
    folder.mkdir(parents=True, exist_ok=True)
    local_audio = folder / ("song" + audio.suffix.lower())
    if audio != local_audio.resolve():
        if local_audio.exists() and local_audio.read_bytes() != audio.read_bytes():
            raise UserError(f"{local_audio} already contains different audio. Use another SONG name.")
        if not local_audio.exists():
            shutil.copy2(audio, local_audio)
    if words and lyrics.resolve() != (folder / "lyrics.txt").resolve():
        if (folder / "lyrics.txt").exists() and (folder / "lyrics.txt").read_bytes() != lyrics.read_bytes():
            raise UserError("Song lyrics already exist and differ. Edit the existing file or use another SONG name.")
        shutil.copy2(lyrics, folder / "lyrics.txt")
    fd, pending = tempfile.mkstemp(prefix=".timing-", suffix=".json", dir=folder)
    os.close(fd)
    pending = Path(pending)
    try:
        command = [python, ROOT / "scripts/timing.py", local_audio, "-o", pending]
        command += ["--lyrics", folder / "lyrics.txt"] if words else ["--no-words"]
        run(command)
        data = json.loads(pending.read_text())
        if not isinstance(data, dict) or not data.get("beats"):
            raise UserError("Analysis produced no beat grid; the original timing has been preserved.")
        if output.exists():
            backup = folder / "timing.backup.json"
            index = 1
            while backup.exists():
                backup = folder / f"timing.backup-{index}.json"
                index += 1
            shutil.copy2(output, backup)
            say(f"Previous timing saved: {backup}")
        pending.replace(output)
    finally:
        pending.unlink(missing_ok=True)
    say(f"Timing written: {output}\nNext: make render SONG={name}")


def build_project(song, name):
    builder = ROOT / "scripts/build_reel.py"
    if not builder.is_file():
        raise UserError("Template builder scripts/build_reel.py is missing. Restore the package source and retry.")
    project = ROOT / "out/projects" / name
    command = [sys.executable, builder, "--song", song, "--out", project]
    if flag("SYNC_CHECK"):
        command += ["--sync-check"]
    run(command)
    if not (project / "index.html").is_file():
        raise UserError("Template builder did not create index.html. No render was attempted.")
    return project


def render_project(project, output, check_only=False):
    run(HF + ["check"], cwd=project)
    if not check_only:
        output.parent.mkdir(parents=True, exist_ok=True)
        run(HF + ["render", "--output", output, "--workers", "2"], cwd=project)
        if not output.is_file() or output.stat().st_size == 0:
            raise UserError("Renderer exited without a nonempty MP4. Run make doctor.")
        say(f"Video ready: {output}\nOpen that MP4 and play it with sound.")


def sample(check_only=False):
    if not render_tools():
        raise UserError("Install the missing render tools, then retry. Run make doctor for details.")
    song = ROOT / "video/sample"
    if not song.is_dir():
        raise UserError("Bundled video/sample is missing. Restore the package source and retry.")
    project = build_project(song, "sample")
    render_project(project, ROOT / "out/sample.mp4", check_only)


def render():
    name, folder = song_name()
    if not (folder / "timing.json").is_file():
        raise UserError(f"No songs/{name}/timing.json. Run make timing SONG={name}, or supply precomputed timing.")
    if not render_tools():
        raise UserError("Fix the missing render tools; run make doctor for details.")
    requested = os.environ.get("OUT", "").strip()
    output = Path(requested).expanduser() if requested else ROOT / "out" / f"{name}.mp4"
    output = (ROOT / output).resolve() if not output.is_absolute() else output.resolve()
    if output.suffix.lower() != ".mp4":
        raise UserError("OUT must name an MP4 file.")
    if output.exists() and not flag("FORCE"):
        if requested:
            raise UserError("OUT already exists. Choose a new path, or pass FORCE=1 to overwrite it.")
        index = 2
        while output.exists():
            output = ROOT / "out" / f"{name}-{index}.mp4"
            index += 1
    project = build_project(folder, name)
    render_project(project, output)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["help", "doctor", "browser", "setup", "setup-align", "sample", "check", "timing", "render"])
    args = parser.parse_args(argv)
    actions = {"doctor": doctor, "browser": lambda: run(HF + ["browser", "ensure"]),
               "setup": setup, "setup-align": lambda: setup(True), "sample": sample,
               "check": lambda: sample(True), "timing": timing, "render": render}
    try:
        if args.command == "help":
            say("make doctor [MODE=sample|timing|align]   check tools and print fixes\nmake browser                           install/find the pinned render browser\nmake sample                            check + render bundled media → out/sample.mp4\nmake setup [PYTHON_SETUP=python3.14]    install pinned analysis/sprite dependencies\nmake setup-align                       optional Python 3.12 sung-word environment\nmake timing SONG=name [AUDIO=path]     beats-only → songs/name/timing.json\n  [WORDS=1 LYRICS=path] [FORCE=1]       optional sung-word alignment; back up existing timing\nmake render SONG=name                  render from the song folder and template\nmake check                             check the bundled sample")
        else:
            started = time.monotonic()
            actions[args.command]()
            say(f"Finished in {time.monotonic() - started:.1f}s (includes this command only).")
        return 0
    except UserError as exc:
        print(f"\nError: {exc}", file=sys.stderr)
    except subprocess.CalledProcessError as exc:
        print(f"\nCommand failed (exit {exc.returncode}). Fix the error shown above and retry; existing source/timing files are preserved.", file=sys.stderr)
    except subprocess.TimeoutExpired:
        print("\nDiagnostic command timed out. Check network access and run npx --yes hyperframes@0.9.2 doctor --json directly.", file=sys.stderr)
    except (OSError, ValueError) as exc:
        print(f"\nError: {exc}", file=sys.stderr)
    except KeyboardInterrupt:
        print("\nStopped. Existing source/timing files are preserved.", file=sys.stderr)
        return 130
    return 1


if __name__ == "__main__":
    sys.exit(main())
