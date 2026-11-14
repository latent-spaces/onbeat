# Suggested final synthesis wording

2026-11-14, codex-tooling-2. Exact replacement wording supplied to the editor of `docs/research/2026-11-14/RECOMMENDATIONS.md` after the new baseline and codex-tooling-1's render result. This is a handoff draft, not a competing merged report.

## Current verification attribution

The original audits used `26d9337`. After the owner advanced main to `6daad3d`, codex-tooling-1/2 reread the new guide, runbooks and committed inputs; opus-strategist-1 updated the synthesis. codex-tooling-1 checked and rendered the short prototype locally. No full-song render or listening verification was performed in this research run.

## Existing short sample

`video/avatar-dance-test/` is a self-contained technical sample with tracked chorus audio, sprites, local GSAP, timing and pinned render commands. codex-tooling-1 reports a successful encoded render: H.264 1080×1920, AAC, 346 frames at 30 fps, 11.533333 seconds. The CLI reported 14.4 seconds on an Apple M4 with cached tooling; that is not clean-install time. Present this tested local sample now, and measure clean-install onboarding separately. It is a limited-animation prototype, not a claim of finished performance quality or a clean lyrical loop.

## Final-song reproduction

The completed 2:24 reel's MP3, corrected timing JSON/JS and art are committed. The development WAV is absent from a clean checkout. For reproducing this exact reel, prepare the WAV from the tracked MP3 and keep the committed corrected timing; do not rerun expensive alignment merely to render existing source. `cut_final.py` documents an existing song-specific export route but also expects ignored timing intermediates. Automate the minimal preparation path separately from the workflow for aligning a new song.

## Revised order of work

Promote the existing full reel plus a legible poster and link GUIDE as its making-of → document the tested prototype as the first technical sample → measure a clean installation and automate final WAV preparation → document provenance/licensing and pin reproducible dependencies → generalize the song-specific export and preset interface → optionally package a CLI/skill. A short 30–45-second promo cut is an optional derivative requiring musical/lyric boundary selection and review; it is not a missing first reel and should not be made by casually trimming the documented final loop.

Replace the unconditional new `sample/` task with: evaluate/document the existing prototype first; create another sample only if its limitations or reuse terms make that necessary.

Evidence: `BASELINE-UPDATE.md`, `current-baseline-presence.json`, GUIDE and the Instagram brief at `6daad3d`, and codex-tooling-1's [PR #5](https://github.com/oronanschel/music-reels/pull/5).
