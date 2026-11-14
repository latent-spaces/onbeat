# Tooling readiness after the completed reel

Research date: 2026-11-14. Agent: codex-tooling-1. **Current source revision: `6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc`.** This replaces the audit narrative based on `26d9337`; that earlier static result is retained as `audit-results-26d9337.json` for provenance, not as current project status.

## Recommendation for the merged report

Promote the **existing completed-reel source and end-to-end guide**, with the **existing self-contained 11.52-second avatar test** as the first no-key try path. Then package the timing/render contract as a thin CLI and optional agent skill. A full studio is premature. The repo now contains a finished 2:24 composition, its selected song, corrected sung-word timing, source artwork, prompt history and production runbooks. Claims that there is no GUIDE, no completed reel, or no sample audio anywhere in the clone are obsolete.

The remaining gap is turning a documented, human-directed production into a portable remix workflow. Distinguish three routes: render a committed short example; rebuild the final composition using committed timing; analyze and align a new song. Only the third requires the heavyweight ML stack. Do not make Suno access or regeneration a prerequisite for inspecting the existing work.

These are proposed packaging changes, not a CLI or skill delivered by this research. No causal claim about stars follows from this audit.

## What changed on main

| Area | Verified current state | Public-project implication |
|---|---|---|
| Guide | `GUIDE.md` covers concept, Suno, beat/word timing, sprites, code, review, rendering, dead ends and posting | A substantial making-of/tutorial already exists; improve its front door rather than write it from scratch |
| Completed example | `video/allow-always-final/index.html`, 144.4 s, 1080×1920, 60 fps | Use this existing production as hero evidence once an actual render is available for approved embedding |
| Selected take | Tracked `songs/allow-always/take-final-yes.mp3`; ffprobe reports 144.4 s, stereo 48 kHz audio | Full-song WAV can be regenerated locally; the song is not missing |
| Corrected timing | Final JSON/JS pair, 126 words, 29 sung lines, 76 bars; `align_final.py` records line windows | Do not rerun naive forced alignment and overwrite the curated result just to try the example |
| Artwork | Tracked sprite/scene assets; `video/assets/disco` links to the prototype assets | The art pipeline and output are present, not a speculative future feature |
| Short example | `video/avatar-dance-test/` includes WAV, local GSAP, font, scene assets and caption markup | An existing no-key example is ready for a documented, supported quickstart candidate |
| Setup | GUIDE section 2 names versions used on macOS and two Python-environment install commands | Dependencies are documented; portable, pinned installation still needs work |
| Renders | GUIDE and Instagram brief name `video/out/allow-always-final-80s-boom2.mp4` | The output is documented, but `video/out/` is ignored and absent in this checkout; I did not inspect the final encoded file |

The README now leads with GUIDE and runbooks. Its “no video was built” statement is explicitly under **Earlier planning notes (2026-11-11)**. It is historical, not the current state. The Instagram brief is a draft distribution plan requiring owner approval, not proof of publication or public availability; this run posts nothing externally.

## Validation performed on the new code

### Static inputs and timing

Run `python3 docs/research/2026-11-14/codex-tooling-1/audit.py` from the repository root. Saved output: `audit-results.json`. It reads local files only, including literal HTML/CSS references. Subcomposition assets resolve from the HyperFrames project root. Dynamic JavaScript paths are not exhaustively analyzed.

- The three legacy compositions still lack their intended WAVs under the ignored `out/dev` symlink.
- The final composition's literal art/script/timing references exist; its `assets/dev/allow-always-final.wav` does not yet exist in the clone.
- The avatar test's entrypoint, subcompositions, literal assets, local GSAP, font and `assets/chorus.wav` all exist. It has no remote script reference.
- All **four** `video/data` JSON/JS pairs decode identically. All checked word intervals lie within duration and reference valid lines; none are zero-length. Envelope counts match `ceil(duration * fps)`.
- Final data: 144.4 s, 126 words, 8,664 kick samples and 8,664 RMS samples. This is structural validity, not independent confirmation of every sung word.
- Stub envelope hop remains `0.017` instead of `1/60`. This could accumulate drift in a future hop-based consumer; no current visual bug is established.

### Actual prototype check

From `video/avatar-dance-test`, ran **`npm run check`**, which invokes pinned HyperFrames 0.9.2. Exit status **0**. Saved terminal output: `prototype-check.log`.

- Lint: 0 errors, 2 `timeline_track_too_dense` warnings (caption and close-up groups).
- Runtime: 0 errors/warnings. Layout: 0 issues across 9 samples.
- Motion, craft and audio: 0 errors/warnings. Contrast: 20/20 text checks pass.
- Snapshots were disabled by check. I separately captured and inspected frames at 0.4 and 1.8 seconds, then rendered the unchanged prototype; see below. The automated check alone does not establish smooth animation or accurate sung words.

`ffprobe` results are saved in `final-source-audio.json` and `prototype-audio.json`. Prototype WAV duration is 11.519208 s. The source MP3 duration matches the final timing's 144.4 s. Audio was measured, not listened to. No production HTML, timing, art or script was modified by this audit.

### Fresh encoded prototype render

After inspecting the two snapshots, ran from `video/avatar-dance-test`:

```bash
npx --yes hyperframes@0.9.2 render --output ../../research/2026-11-14/codex-tooling-1/prototype-repro-check.mp4 --fps 30 --workers 2
```

Exit status 0. CLI reported 14.4 seconds rendering on this Apple M4 machine with hardware GPU and cached CLI/browser dependencies. This is **not** a timed clean machine install. `prototype-render.log` records the run; `prototype-render-probe.json` confirms H.264 1080×1920, 30 fps, 346 frames, AAC audio, 11.533333 s and 7,059,219 bytes. The tiny duration difference from 11.5192 s is frame rounding. The MP4 is retained locally in this dated folder (gitignored by the repository rule); logs, metadata and extracted evidence are committed.

Inspected the encoded frame at 1.8 s (`prototype-encoded-1.8s.jpg`): the dancers, separate planet/window background and caption appear, with the final word partially highlighted. This is a spot check, not an all-frame visual review or listening-based word-timing verification. The final 2:24 composition has not been rendered by this audit.

## Reproducibility routes and remaining gaps

### 1. Try the existing short example first

The included WAV and prebuilt art mean users should not need Python, Suno, paid keys, stem separation, image generation or repacking to try it. Start the quickstart from `video/avatar-dance-test` and document the pinned check/render commands. I tested check and encoded a fresh MP4 from the committed inputs; see the render evidence below. The prototype begins/ends during lyric words and is a limited-animation test, as the runbook explains; do not market it as the final full-song loop.

The example includes a local font. Its presence is not an audit of redistribution rights. The owner should resolve the code, song, font and artwork distribution terms before publication. Vendored page-mascot has its own MIT notice/provenance; that is not a root project license.

### 2. Rebuild the completed composition with committed timing

The final composition loads its corrected timing pair and tracked art; it needs an intermediate 48 kHz WAV at `out/dev/allow-always-final.wav`. Its audio source MP3 is committed. A minimal proposed preparation route from the root is:

```bash
mkdir -p out/dev
ffmpeg -i songs/allow-always/take-final-yes.mp3 -vn -ar 48000 out/dev/allow-always-final.wav
cd video/allow-always-final
npx --yes hyperframes@0.9.2 check
# After checking and reviewing, render a uniquely named output.
```

**This exact final-preparation/render sequence was not run in this audit.** The `-vn` explicitly drops the MP3's attached picture stream. Keep the committed curated timing untouched. `cut_final.py` documents the audio conversion and JSON/JS export, but requires ignored `out/timing/allow-always-final.json`; it is not the shortest fresh-clone route when the final timing is already committed.

The final composition still loads GSAP 3.15.0 from a CDN, unlike the fully local prototype. Its assets and data are shared through symlinks. Document network/runtime requirements and test portability on supported systems before promising offline or cross-platform operation.

### 3. Analyze a new song

GUIDE now provides versions that worked on macOS (general Python 3.14 environment; alignment Python 3.12 with specific reported libraries) and installation commands. Those pip commands are **unpinned**, and there is still no root lockfile/requirements/pyproject or setup entrypoint for this pipeline. Do not claim the dependencies are undocumented, but do not mistake a version table for a reproducible environment lock.

The two-environment split is intentional. `timing.py` imports librosa/numpy/scipy, decodes with ffmpeg, and invokes the hardcoded `.venv-align/bin/python`. Demucs isolates vocals; transcription and alignment use CPU, with Demucs selecting MPS when available. My system Python is 3.15.2 with the relevant ML/audio packages absent; I did not install/retest that stack.

Important newly documented limit: GUIDE section 11 says `align_words.py` **without `--lyrics` crashes with an IndexError**. Do not advertise a tested transcription-only route. `--no-words` skips alignment, but a new-song beat-only run was not tested here.

The fixed-tempo assumption, roughly 85–170 BPM search, low-band downbeat heuristic and English lyric normalization remain. General support for tempo changes, multilingual vocals and arbitrary music is not established.

## Human correction is a feature of the real workflow

GUIDE explains that Suno changed the sung words/order and the initial alignment lost its place after 41 s. `align_final.py` now follows the sung text in manually selected line windows and marks uncertain interpretations. This is stronger process evidence than an automatic-only claim: the public project can expose those editable windows as a quality-control step.

`cut_final.py` adds a second concrete JSON-to-`window.TIMING` exporter. The handoff is **documented and implemented for this song**. The remaining gap is a general importer that handles arbitrary audio, durations, timing export, visual template selection and output paths. Sprite packing and karaoke generation also have deliberate project-specific constants. Describe them as worked examples until generalized.

`BeatSync.at()` and the paused timeline remain useful differentiators: deterministic frame seeking makes inspection/review possible. A pinned renderer alone does not guarantee musically correct alignments or identical future font/model environments.

## Proposed packaging order

1. Promote GUIDE and the existing finished-reel source; arrange an owner-approved viewable demo from the existing render.
2. Document the now-verified bundled avatar-test render as the no-key quickstart. Test an uncached clean-machine installation before promising an end-to-end duration; the observed 14.4 s render excludes setup.
3. Add a final-example preparation command using the tracked MP3 plus committed timing, avoiding unnecessary ML recomputation.
4. Lock/document the supported analysis environments and add actionable dependency/media preflight checks.
5. Generalize song import, alignment review and template configuration; expose one CLI used by humans and the optional skill.
6. Validate a second song before claiming a reusable tool. Add studio UI only after observing user friction.

## Sources

Pinned primary sources at `6daad3d`:

- [Pipeline guide](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/GUIDE.md), especially sections 2, 5, 8 and 11.
- [Current README](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/README.md).
- [Final composition](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/video/allow-always-final/index.html), [final exporter](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/songs/allow-always/cut_final.py), [sung-line alignment](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/songs/allow-always/align_final.py).
- [Prototype README](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/video/avatar-dance-test/README.md), [production runbook](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/analysis/runbooks/animated-music-reels.md), [learning log](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/analysis/runbooks/learning-log.md).
- [Suno prompt history](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/songs/allow-always/suno-prompts.md), [Instagram draft brief](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/songs/allow-always/instagram-brief.md).

No graph MCP tools were available; discovery fell back to tracked files/direct reads. Competitor counts and launch-history evidence are handled in teammates' slices, not independently endorsed here.
