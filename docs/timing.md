# Timing: beats-only first, words later

`scripts/timing.py` turns a song into one JSON file that every composition reads.

```bash
.venv/bin/python scripts/timing.py songs/<song>/take.mp3 --beats-only -o out/timing/<song>.json     # easy start
.venv/bin/python scripts/timing.py songs/<song>/take.mp3 --lyrics lyrics.txt -o out/timing/<song>.json  # with sung words
```

## Beats-only mode (recommended start)

- Needs only the main Python environment (librosa, NumPy, SciPy) and ffmpeg. No `.venv-align`, no WhisperX, no lyrics.
- Gives the beat grid, bars, downbeat, sections (kick or no kick) and the kick and loudness envelopes. That is
  everything sprites, bounces, cuts and camera moves need.
- Words and lines are empty, and the JSON says `"mode": "beats-only"`. A template should show lyric captions only
  when `words` is not empty.
- `--no-words` is the same flag under its old name.
- Without `--beats-only`, a missing `.venv-align` stops with a message that says so, instead of a traceback.

## Adding words later

Create `.venv-align` (GUIDE.md section 2), then run again without `--beats-only`. Suno rarely sings what you wrote, so
listen first; the fixes are in GUIDE.md section 5.2.

## JSON contract

| Key | Meaning |
|---|---|
| `mode` | `"beats-only"` or `"words"` |
| `audio`, `duration`, `fps` | source file name, seconds, 60 |
| `bpm`, `beatPeriod`, `beatsPerBar` | one fixed tempo |
| `beats`, `bars` | seconds; `bars` are the downbeats |
| `sections` | runs of bars with or without kick |
| `envelopes` | kick and loudness, one value per 60 fps frame, 0 to 1 |
| `words`, `lines` | sung-word times; empty in beats-only mode |

Everything is a plain list so a composition can compute each frame as a pure function of time.
