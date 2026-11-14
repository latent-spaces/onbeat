"""Behavior checks for the command boundary; no renderer, ML models or API calls."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("reel", Path(__file__).resolve().parents[1] / "scripts/reel.py")
reel = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reel)


class ToolingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "songs").mkdir()
        self.root_patch = patch.object(reel, "ROOT", self.root)
        self.root_patch.start()
        self.env_patch = patch.dict(os.environ, {}, clear=True)
        self.env_patch.start()
        self.output = contextlib.redirect_stdout(io.StringIO())
        self.output.__enter__()

    def tearDown(self):
        self.output.__exit__(None, None, None)
        self.env_patch.stop()
        self.root_patch.stop()
        self.temp.cleanup()

    def test_optional_renderer_checks_do_not_block_local_render(self):
        report = {"ok": False, "checks": [{"name": name, "ok": True} for name in ["Node.js", "FFmpeg", "FFprobe", "Chrome"]]
                  + [{"name": "Version", "ok": False}, {"name": "TTS (Kokoro)", "ok": False}]}
        self.assertTrue(reel.required_renderer_checks(report))
        report["checks"][3]["ok"] = False
        self.assertFalse(reel.required_renderer_checks(report))
        self.assertFalse(reel.required_renderer_checks({"ok": True}))

    def test_song_names_cannot_traverse_or_become_shell_commands(self):
        for name in ["../escape", "folder/song", "x; touch marker", "$(echo x)", "-flags"]:
            with self.subTest(name=name), patch.dict(os.environ, {"SONG": name}):
                with self.assertRaises(reel.UserError):
                    reel.song_name()
        with patch.dict(os.environ, {"SONG": "demo-01"}):
            self.assertEqual(reel.song_name()[0], "demo-01")

    def test_song_symlink_outside_song_root_is_rejected(self):
        (self.root / "outside").mkdir()
        (self.root / "songs/link").symlink_to(self.root / "outside", target_is_directory=True)
        os.environ["SONG"] = "link"
        with self.assertRaises(reel.UserError):
            reel.song_name()

    def test_curated_timing_requires_explicit_regeneration(self):
        song = self.root / "songs/demo"
        song.mkdir()
        (song / "song.wav").write_bytes(b"source")
        original = '{"beats":[0],"curated":true}'
        (song / "timing.json").write_text(original)
        os.environ["SONG"] = "demo"
        with patch.object(reel, "check_environment", return_value=True), patch.object(reel, "run") as run:
            with self.assertRaises(reel.UserError):
                reel.timing()
            run.assert_not_called()
        self.assertEqual((song / "timing.json").read_text(), original)

    def test_failed_regeneration_keeps_curated_timing(self):
        song = self.root / "songs/demo"
        song.mkdir()
        (song / "song.wav").write_bytes(b"source")
        original = '{"beats":[0],"curated":true}'
        (song / "timing.json").write_text(original)
        os.environ.update(SONG="demo", FORCE="1")
        with patch.object(reel, "check_environment", return_value=True), patch.object(reel, "run", side_effect=subprocess.CalledProcessError(2, ["timing"])):
            with self.assertRaises(subprocess.CalledProcessError):
                reel.timing()
        self.assertEqual((song / "timing.json").read_text(), original)
        self.assertFalse(list(song.glob(".timing-*")))

    def test_audio_with_spaces_is_copied_and_timing_replaced_with_backup(self):
        source = self.root / "a song's mix.wav"
        source.write_bytes(b"source")
        song = self.root / "songs/demo"
        song.mkdir()
        original = '{"beats":[0],"curated":true}'
        (song / "timing.json").write_text(original)
        os.environ.update(SONG="demo", AUDIO=str(source), FORCE="1")
        def analyze(command):
            self.assertIn("--no-words", command)
            self.assertEqual(command[2], song / "song.wav")
            Path(command[command.index("-o") + 1]).write_text(json.dumps({"beats": [0.1, 0.6], "words": []}))
        with patch.object(reel, "check_environment", return_value=True), patch.object(reel, "run", side_effect=analyze):
            reel.timing()
        self.assertEqual((song / "song.wav").read_bytes(), b"source")
        self.assertEqual((song / "timing.backup.json").read_text(), original)
        self.assertEqual(json.loads((song / "timing.json").read_text())["beats"], [0.1, 0.6])

    def test_conflicting_modes_are_actionable(self):
        os.environ.update(SONG="demo", WORDS="1", BEATS_ONLY="1")
        with self.assertRaisesRegex(reel.UserError, "conflicts"):
            reel.timing()

    def test_explicit_existing_render_is_not_overwritten(self):
        song = self.root / "songs/demo"
        song.mkdir()
        (song / "timing.json").write_text('{}')
        output = self.root / "old.mp4"
        output.write_bytes(b"original")
        os.environ.update(SONG="demo", OUT=str(output))
        with patch.object(reel, "render_tools", return_value=True), patch.object(reel, "build_project") as build:
            with self.assertRaisesRegex(reel.UserError, "already exists"):
                reel.render()
            build.assert_not_called()
        self.assertEqual(output.read_bytes(), b"original")


if __name__ == "__main__":
    unittest.main()
