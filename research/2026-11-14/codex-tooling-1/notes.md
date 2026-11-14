# Tooling readiness: make the first remix work

Research date: 2026-11-14. Agent: codex-tooling-1. Scope: local reproducibility and packaging audit, research only. Base commit: `26d9337f44ebfb7a221a107e6f957c3ed31eb9f2`.

## Recommendation for the merged report

Launch a **remixable HyperFrames template with a thin CLI and an optional agent skill**. The distinctive reusable core is the music timing contract and its deterministic animation helpers. A full studio is premature: a fresh clone currently has no playable sample audio and no general path from the timing command to a rendered composition. Prioritize a rights-cleared, no-key sample that can be rendered without running any ML models. Then support bring-your-own audio and lyrics, with alignment as an optional heavyweight installation. Keep Suno generation manual and optional; do not make a Suno account, free-download allowance or paid credits prerequisites for trying the repository.

These are proposed launch requirements, not features delivered by this research. Reproducibility can improve adoption; this audit provides no causal evidence that it will create stars or virality.

## What exists and why it is appealing

| Piece | Present implementation | Reuse value |
|---|---|---|
| Beat/section extraction | `scripts/timing.py`: ffmpeg decode, librosa onset envelope, fixed-tempo comb search, waveform phase correction, downbeat heuristic, kick/no-kick sections | Turns audio into an inspectable editing plan rather than hiding synchronization in a prompt |
| Word alignment | `scripts/align_words.py`: Demucs vocal isolation, faster-whisper short-clip transcription, WhisperX forced alignment, lyric-line matching and onset correction | Addresses sung vocals, a harder case than ordinary speech subtitles |
| Shared timing contract | `analysis/playbook.md` section 7: beats, bars, words, lines, sections, per-frame kick/RMS envelopes | Supports templates and future alternative aligners without tying visuals to one model |
| Seekable visual helpers | `video/src/beatsync.js`: beat steps/pulses/tickers, lyric drops/karaoke/syllable stacks, palette cuts, character states, progress | Composable primitives for music-driven scenes, with explicit frame-boundary behavior |
| Renderer integration | HyperFrames CLI pinned to `0.9.2`; GSAP `3.15.0` script URL; paused root timelines | Existing preview/check/render commands and a deterministic animation structure |
| Demonstration fixtures | Short/long stub timings plus real `allow-always` timing data | Can support fast, model-free checks once paired with distributable media |

The project is currently a research/creative workspace plus a template and Python scripts. It is **not yet** a packaged CLI, installable skill, generalized song importer or studio. The root README explicitly says the current story has no finished video and the existing results are not good enough. Respect that status in public-facing claims.

## Fresh-clone findings

### 1. No included composition can play its intended audio

All three HTML compositions resolve their local source/timing scripts but reference absent WAV files:

| Composition | Missing media |
|---|---|
| `video/index.html` | `assets/dev/dev8bars.wav` |
| `video/scale/index.html` | `assets/dev/dev24bars.wav` |
| `video/allow-always/index.html` | `assets/dev/allow-always.wav` |

`video/assets/dev` is a tracked symlink to `../../out/dev`; `out/` is gitignored. The nested compositions share `assets`, `src` and `data` through relative symlinks. A clone preserves the link but cannot recover its ignored target. `video/tools/stub-timing.mjs` writes timing JSON and a JavaScript twin, **not audio**. `songs/allow-always/cut.py` requires both an ignored analysis output and an absent `.m4a` take. Merely documenting `npm run render` cannot make this sample reproducible.

Proposed fix: ship one redistributable sample with a provenance/license note, lyrics, timing and a complete composition using ordinary repository-relative assets. A synthetic beat fixture is enough for checks, but a compelling sung sample is necessary to demonstrate sung-word alignment. Treat those as separate fixtures if necessary.

### 2. Installation requirements are split and unmanifested

`timing.py` imports librosa, numpy and scipy before argument parsing and shells out to ffmpeg. Word extraction invokes **exactly** `.venv-align/bin/python`; that helper imports Demucs, torch, torchaudio, WhisperX and faster-whisper. Its docstring names Python 3.12. No tracked requirements file, pyproject, environment lock, Python runtime pin, setup script or root package entrypoint exists in this commit.

Observed machine state, not a universal compatibility finding: system `python3` is 3.15.2; numpy/scipy/librosa/torch/whisperx/demucs are unavailable there; Node is 26.13.0, npm 11.20.0 and ffmpeg is installed. The declared environment directories are absent. Therefore no honest fresh-clone command can be documented as tested end to end in this audit.

Proposed install tiers:

1. **Demo**: Node + supported HyperFrames/browser prerequisites + bundled media/timing. No Suno, API key or model download.
2. **Analyze beats**: pinned, tested Python environment + ffmpeg; `--no-words` already skips the alignment subprocess.
3. **Align lyrics**: separately installed compatible ML dependencies and model downloads; disclose disk/download/runtime expectations after measurement.

Do not invent exact installation versions or performance figures. Establish them on a clean tested environment first. CPU inference is used for transcription/alignment; Demucs chooses MPS when available, otherwise CPU. There is no explicit CUDA selection in this helper.

### 3. The JSON-to-render handoff is still custom per song

`timing.py` writes JSON containing an audio **basename**. HTML instead loads a classic script assigning `window.TIMING`; audio source and composition duration are hardcoded in the HTML. The stub generator and song-specific `cut.py` write the JS twin. There is no general importer that copies audio, emits the twin, updates duration, selects a visual template and renders it.

`cut.py` also prepends a missing downbeat and hand-corrects word timings for two lyric lines. This is useful production evidence that an explicit review/correction step matters; it is not proof of fully automatic alignment.

Proposed interface, illustrative and **not implemented**:

```text
music-reels demo
music-reels analyze ./song.wav --lyrics ./lyrics.txt --out ./work
music-reels inspect ./work/timing.json
music-reels render ./work --template one-place --out ./reel.mp4
```

The CLI should own files, dependency checks and validation. The skill should orchestrate the same commands, explain the song-first creative process and require a five-second visual review before a full render. Avoid two separate implementations for humans and agents.

### 4. Timing assumptions should become a clear contract

The beat finder searches one tempo octave, roughly 85–170 BPM, and assumes a fixed tempo. Downbeat inference uses low-band changes and falls back to the first beat when evidence is weak. This fits the current four-on-the-floor creative direction but does not establish accuracy on tempo changes, rubato, sparse acoustic music or every meter. `--beats-per-bar` is configurable; that alone is not validation of arbitrary musical structure.

The alignment helper defaults to English, and lyric matching normalizes to ASCII letters, numbers and apostrophes. The top-level timing command has no language flag. Do not advertise multilingual lyric support without separate evaluation.

Missing word timings are interpolated and may become zero-duration events. The current checked-in files have none, but public tooling should expose warnings/confidence or an inspectable correction file. Recommend checks for finite/bounded times, sorted grids, valid line references, zero-duration/overlapping words and alignment coverage. `analysis/playbook.md` section 9 already warns that an aligner can place words that were never sung.

### 5. Determinism is a useful differentiator with practical limits

`BeatSync.at()` snaps events to the first eligible video frame, with a small epsilon to avoid floating point boundaries; helpers add animation to the shared paused timeline. This is a strong, explainable feature: seek to the same frame and get the same visual state. It does not guarantee a musically correct beat grid or reproducibility across changing model/tool/font environments.

HyperFrames scripts use an exact CLI pin, but invoke it through npx; GSAP loads from a CDN. No npm lockfile/dependency tree is committed. Recommend pinning the supported environment and bundling or explicitly documenting network-dependent runtime assets. A clean render check should catch missing media before a lengthy render.

## Validation performed

Run `python3 research/2026-11-14/codex-tooling-1/audit.py` from the repository root. The script only reads local files and prints JSON; it does not fetch anything, run ML or render. Saved output is in `audit-results.json`.

Observed checks:

- Three compositions: all local source and timing script references exist; all three intended audio files are missing.
- All three JSON/JS timing pairs decode to identical objects.
- 22 stub-short, 120 stub-long and 85 allow-always word intervals are bounded, ordered within each word and have valid line indices; no zero-duration words in these fixtures.
- Kick/RMS envelope counts equal `ceil(duration * fps)` for all three fixtures.
- Stub envelope hop is `0.017`, whereas 60 fps means `1/60` (~0.016667). That discrepancy would accumulate if a future consumer used hop as its clock; this audit does **not** show a current visual bug, and the stub envelopes are all zero.

Not validated: actual audio/word accuracy, model installation, HyperFrames check, browser appearance, rendering, Windows symlink behavior or performance. No HTML/production source was modified. Missing assets and dependency setup were sufficient to establish that an end-to-end demo is unavailable in this checkout; installing ML stacks or downloading songs would not be appropriate proof of the committed sample.

## Proposed go-public gates

| Priority | Gate | Evidence required before claiming it |
|---|---|---|
| P0 | First successful sample render | A clean clone can render the bundled song; a maintainer records exact commands/environment and checks audio+video |
| P0 | Generic timing-to-template handoff | A second, user-supplied song renders without editing source paths or song-specific Python |
| P0 | Clear distribution terms | Repository license plus separately clear sample/audio/model/source provenance, reviewed by the owner |
| P1 | Inspectable timing quality | Human review workflow plus representative beat/word fixtures and surfaced weak alignments |
| P1 | One CLI, optional skill | Both use the same contract and command paths; neither requires paid generation to try the demo |
| P2 | Template gallery | Two or three visually strong, audibly distinct examples with remix instructions and complete inputs |
| Later | Studio/UI | Only after observing where users struggle with a working template/CLI |

## Source map

All findings above derive from the checked-out commit; links below are pinned primary sources rather than claims about current main:

- [README and current creative status](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/README.md)
- [Timing extraction](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/scripts/timing.py)
- [Word alignment](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/scripts/align_words.py)
- [Animation helpers](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/video/src/beatsync.js)
- [Renderer scripts](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/video/package.json)
- [Stub generator](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/video/tools/stub-timing.mjs)
- [Song-specific integration and corrections](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/songs/allow-always/cut.py)
- [Timing contract and known creative/alignment limitations](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/analysis/playbook.md)
- [Ignored local outputs](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/.gitignore)

No graph MCP tools were available in this session, so discovery fell back to the tracked file inventory and direct file reads. This slice deliberately leaves competitor/star-history research to teammates; it does not repeat or endorse unverified star counts.
