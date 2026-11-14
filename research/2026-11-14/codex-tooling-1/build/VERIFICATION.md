# Tooling verification — 2026-11-14

Local machine: macOS arm64, Node 26.13.0, Python 3.14 analysis / Python 3.15.2 wrapper, FFmpeg 8.0.1, HyperFrames pinned to 0.9.2.

- `make doctor` and `make doctor MODE=timing`: pass; optional alignment environment absent.
- `make setup`: installs the pinned direct analysis requirements in 28.7 seconds.
- Real beats-only analysis: bundled chorus WAV analyzed into 24 beats / 6 bars in 52.5 seconds including first JIT. This verifies execution, not timing accuracy.
- Eight stdlib behavioral tests pass: path boundaries, optional renderer tools, curated timing backups, failed-analysis preservation, conflicting modes, and output overwrite protection.
- Legacy render smoke: check and render passed in 58.7 seconds; screenshot is an execution artifact, not evidence of the generic template path.
- Optional alignment requirements: fully resolved for Python 3.12; not installed, no model weights downloaded, no word-alignment run.
- Generic template sample: PASS in combined isolated snapshot (tooling + template-sample c3539c6 + shared motion helpers): make sample builds, checks and renders in 18.1 seconds with warm CLI/browser caches; render12.6s. Encoded H264/AAC1080x1920,30fps346frames11.533s; decoded2sframe inspected.
- A genuinely different locally synthesized8s melody/kick fixture: make timing gives119.992BPM16beats in1.7s; make render builds/checks/renders the same template in15.5s total (render7.2s), no HTML edits.
- A separately analyzed chorus folder also renders in14.3s total. These are local execution timings, not cold-download performance promises.
- Shared SpriteDance example: exact PR20 helper files pass seven Node tests and HyperFrames check (two diagnostic-text craft warnings).
- All make commands need Python 3 for the stdlib wrapper. Sample needs Node 22+, FFmpeg/FFprobe and the HyperFrames browser; it does not need a Python venv.
- Raw logs and decoded legacy frame remain local research artifacts; only this concise verification record is committed.

Commands use argv lists rather than shell interpolation. Default render output versions existing files. Explicit OUT requires FORCE=1 to overwrite. Existing timing requires FORCE=1 and is backed up only after successful analysis.

PR #12 review: the new --beats-only alias ran against real audio and produced mode=beats-only,24 beats,6 bars,0words/lines. Word highlighting needs alignment; plain captions do not.
