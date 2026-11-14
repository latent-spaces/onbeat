# Tooling verification — 2026-11-14

Local machine: macOS arm64, Node 26.13.0, Python 3.14.4, FFmpeg 8.0.1, HyperFrames pinned to 0.9.2.

- `make doctor` and `make doctor MODE=timing`: pass; optional alignment environment absent.
- `make setup`: installs the complete pinned analysis dependency set in 28.7 seconds.
- Real beats-only analysis: bundled chorus WAV analyzed into 24 beats / 6 bars in 52.5 seconds including first JIT. This verifies execution, not timing accuracy.
- Eight stdlib behavioral tests pass: path boundaries, optional renderer tools, curated timing backups, failed-analysis preservation, conflicting modes, and output overwrite protection.
- Legacy render smoke: check and render passed in 58.7 seconds; screenshot is an execution artifact, not evidence of the generic template path.
- Optional alignment requirements: fully resolved for Python 3.12; not installed, no model weights downloaded, no word-alignment run.
- Generic template sample and second-song render: pending shared template/sample integration.

Commands use argv lists rather than shell interpolation. Default render output versions existing files. Explicit OUT requires FORCE=1 to overwrite. Existing timing requires FORCE=1 and is backed up only after successful analysis.
