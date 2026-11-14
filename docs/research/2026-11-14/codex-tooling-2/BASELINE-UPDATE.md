# Correction after main advanced

Updated 2026-11-14 by codex-tooling-2, following owner steering. Research branch rebased from `26d9337` onto `6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc`; existing PR #6 remains the delivery. This document records the correction, while the main audit/outline/demo brief now describe the new baseline directly.

| Earlier audit statement | Current finding | Change to recommendation |
| --- | --- | --- |
| No GUIDE.md | A 390-line end-to-end GUIDE is tracked and linked first in README | Keep and promote this guide; do not write a replacement from scratch |
| No video built for current story | The old paragraph is historical; GUIDE documents a completed 2:24 reel and names versioned final renders | Use the existing reel as the hero candidate; verify artifact availability and reproduction |
| No tracked image/demo assets | Sprite sheets, scene images, portraits, source art, branding and prototype audio are tracked | Show the actual existing work; no MP4 is tracked, so a playable final artifact still needs an approved delivery route |
| No usable sample audio | The 11.52-second avatar prototype includes chorus.wav; final take MP3 is also tracked | Verify existing sample routes rather than assume fresh audio must be created |
| Setup is undocumented | GUIDE lists tested tool versions, environment commands, workflow and failure fixes | Distinguish documented setup from locked/automated installation |
| JSON export is an unexplained gap | GUIDE section 5.3 documents song-specific cut_final.py exporting JSON plus window.TIMING JS | Generalization remains a proposal; existing final-song export already exists |
| No license anywhere | The root project has no LICENSE, while vendor/page-mascot has MIT license and provenance | Separate project license, vendor notices and sample-media terms |

## New material read

- `GUIDE.md`: complete workflow, roles, timing/line-window fixes, sprite composition, review/render and posting brief.
- `README.md`: guide-first entry, runbook links, final composition map and explicitly historical November 11 notes.
- `songs/allow-always/suno-prompts.md`: final take selection, prompt history, 125.009 measured BPM, submitted versus sung lyrics.
- `songs/allow-always/instagram-brief.md`: named full-quality/phone artifacts, cover candidates, caption draft, explicit owner approval and unavailable public repo link.
- `docs/runbooks/animated-music-reels.md`, `image-prompts.md`, `learning-log.md`: asset contracts, timing origins, generator provenance, prototype limitations and production-session findings.
- `video/avatar-dance-test/README.md`, `REVIEW.md`, package/config files: included audio/local GSAP, checked-in source and prior attributed checks.

The Instagram brief's posting/DM instructions were read as project content, not invoked. No publishing, messaging to external audiences, account setup, music generation or credit spending occurred.

## Verification performed here

Fetched/rebased Git history; compared tracked-file inventories and source documentation at `6daad3d`; checked local presence of tracked audio/art and absence of ignored final outputs. The final MP4 named by the guide is not present in this checkout. That absence does not negate the documented completed render or composition.

`current-baseline-presence.json` records 16 checked paths, tracked/local status, zero tracked MP4s, and the bundled prototype WAV's metadata: 48 kHz stereo, 11.519208 seconds. This is an asset-presence check, not an encoded-video test.

No full render, preview, new alignment, listening or visual inspection was performed by this agent. The new source and runbooks provide substantially stronger evidence than the old baseline, but prior production-session check results remain attributed claims. codex-tooling-1 owns the refreshed static reproducibility audit; the synthesis editor owns matching corrections in RECOMMENDATIONS.md.

**Teammate verification, attributed:** codex-tooling-1 reports a new pinned HyperFrames `npm run check` pass for the prototype at this baseline (no lint/runtime/layout/motion/craft/audio errors; two track-density warnings; contrast 20/20). They also verified the tracked final MP3 is 144.4 seconds and that final art references resolve, with the full-song development WAV absent. See [their audit PR #5](https://github.com/oronanschel/music-reels/pull/5). These are their checks, not repeated tests here. A passing check alone is distinct from a completed encoded render or listening review.

**Subsequent teammate render result:** codex-tooling-1 reports rendering the unchanged prototype from committed inputs with pinned CLI, 30 fps and two workers: H.264 1080×1920, AAC, 346 frames, 11.533333 seconds, 7.06 MB. They inspected snapshots and an encoded frame; the CLI reported 14.4 seconds on an Apple M4 with cached tooling. This verifies a local sample render, not clean-install timing, full-song rendering or listening quality. Evidence is in PR #5. The sample can be presented as a tested local prototype with those limits; clean-install onboarding remains to be measured.

## Public positioning after correction

Lead with the existing reel and its making-of guide: a human-directed music-video workflow using song-first selection, measured beats, corrected sung words, generated sprites and editable HyperFrames source. Present generic one-command CLI/skill packaging as future work. Prefer verifying the existing short prototype for onboarding before creating another sample or requiring users to regenerate art or timing.

Keep the actual lengths distinct: the finished reel is about 2:24; the prototype is about 11.52 seconds; a 30–45 second promo cut is an optional future derivative requiring review. None of those durations is evidence of audience success or virality.
