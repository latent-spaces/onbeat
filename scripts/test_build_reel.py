"""Regression checks for protecting inputs and unrelated output folders."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import build_reel


class OutputSafety(unittest.TestCase):
    def test_refuses_input_overlap_and_unrelated_content(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            song = root / 'song'
            song.mkdir()
            unrelated = root / 'unrelated'
            unrelated.mkdir()
            keep = unrelated / 'keep.txt'
            keep.write_text('owner data')
            for out in (song, song / 'child', root, unrelated, build_reel.ROOT):
                with self.subTest(out=out), self.assertRaises(ValueError):
                    build_reel.validate_output(out, song)
            self.assertEqual(keep.read_text(), 'owner data')

    def test_failed_validation_does_not_touch_previous_project(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            song = root / 'song'
            song.mkdir()
            (song / 'timing.json').write_text(json.dumps({'duration': -1}))
            out = root / 'project'
            out.mkdir()
            (out / build_reel.MARKER).write_text('generated')
            previous = out / 'index.html'
            previous.write_text('previous render')
            with self.assertRaises(ValueError):
                build_reel.build(song, out)
            self.assertEqual(previous.read_text(), 'previous render')

    def test_failed_conversion_does_not_touch_previous_project(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / 'project'
            out.mkdir()
            (out / build_reel.MARKER).write_text('generated')
            (out / 'index.html').write_text('previous render')
            with patch.object(build_reel.subprocess, 'run', side_effect=OSError('ffmpeg unavailable')):
                with self.assertRaises(OSError):
                    build_reel.build(build_reel.ROOT / 'video/sample', out)
            self.assertEqual((out / 'index.html').read_text(), 'previous render')


if __name__ == '__main__':
    unittest.main()
