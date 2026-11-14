# Proposed public README hierarchy

Draft by codex-tooling-2, 2026-11-14; revised against main `6daad3d`. This is a content specification, not a replacement README or an implemented feature list. GUIDE and the finished reel composition already exist. Verify the existing short prototype before advertising it as a clean-clone sample; the proposed generic skill/CLI still needs implementation.

## First screen

**Title:** music-reels

**Proposed positioning:** Turn your song into an editable, beat-synced lyric reel.

**Current-state qualification:** A documented local production workflow with a completed 2:24 reel, editable HyperFrames source and project-specific helpers. A portable demo artifact and verified sample route are release prerequisites; completing the first reel is no longer outstanding.

**Visual:** use the existing final portrait reel as the hero candidate, with a legible poster and visible play affordance. GUIDE and the Instagram brief document its render; the MP4 remains in ignored output storage, absent from this checkout. Provide a text description and sung-lyric transcript. Link the exact checked-in composition. Avoid presenting a concept or another creator's reel as product output.

**Primary action:** Run the sample. Add the exact verified command and expected output path when the implementation supports it. Do not introduce a fictional `npx music-reels` command or package name.

**Secondary actions:** Watch with sound · Read GUIDE.md · Bring your own audio.

## 1. What you get

Three concrete bullets, verified against the released sample:

- Vertical rendered video; list actual dimensions, frame rate and duration.
- Editable composition source and its media.
- Beat/word timing data used by that composition.

Label unsupported formats and future presets as planned. Explain which parts still require human design choices.

## 2. Try the included sample

Put the recommended clean-clone route first. Show supported environment, dependency installation, one sample command, expected result path and how to preview. Use measured first-run/render times from a named machine only after measuring them.

Include a small table:

| Sample route | Own-audio route |
| --- | --- |
| Existing prototype chorus audio, sprites and timing | User-provided song and optional lyrics |
| State whether any keys/accounts are actually needed | Identify optional external services separately |
| State first-run downloads and local requirements | Explain alignment/model downloads and compute requirements |

Use `video/avatar-dance-test/` as the first sample candidate: it already includes audio, art, local GSAP and pinned commands. Verify it on a clean clone and confirm media terms before claiming the no-key happy path. GUIDE documents two Python environments for regenerating timing, which need not be required merely to render precomputed fixtures. Link codex-tooling-1's refreshed research for full-song asset and setup details.

## 3. How it works

Use a compact diagram:

```text
Your audio + lyrics
       |
       v
Timing: beats/bars + sung-word times
       |
       v
Editable HyperFrames composition
       |
       v
Preview -> render
```

Explain in two sentences: musical beats drive pulses and cuts; word timestamps drive lyric highlighting. Link GUIDE sections 5 and 7, the actual timing data and the final composition. Say which steps are automated today and which involve manual take selection, line-window alignment and creative review.

## 4. Bring your own song

Link the existing GUIDE and Suno prompt history for song selection, timing/correction, assets and rendering. Use `align_final.py` as an example of sung-line windows, explaining that it is song-specific. Use a generic sample path, not a song-specific script disguised as a general importer. Suno can be one source of audio; avoid implying this is an official Suno integration.

## 5. Customize one thing

Show how to change a palette, lyric style or beat motion, with one named editable file and before/after output from the same audio segment. Add an agent-skill route only after a distributable skill exists and has been tested. Keep CLI and agent routes aligned on the same underlying contract.

## 6. Limitations and requirements

Include actual platform requirements and known issues: variable tempo, ambiguous beats, vocals/alignment, language support and hardware dependence where applicable. State that timing can need manual correction. Avoid claims of perfect sync, any-song support, deterministic end-to-end output or one-click creative quality without evidence.

## 7. Reuse, contribute and maintain

Link the chosen code license, sample-media terms, contribution guide and useful small tasks. Suggested first contributions, once interfaces are stable: a timing fixture, a template preset, a documented setup fix. Keep the original research playbook accessible under “Design notes”; retain its measured/judged/hypothesis labels. Link the existing sprite runbook, image-prompt patterns and learning log rather than replacing them with new scaffolding.

## Suggested documentation split

- Root README: product explanation, existing output, verified sample path, limitations and links.
- GUIDE.md (already exists): end-to-end workflow and troubleshooting; production runbooks add sprite detail.
- Timing reference: JSON contract and correction examples.
- Maintainer notes: current story, session history and experiments.
- Contribution guide: checks, sample fixtures, preset interface and review expectations.

Do not create all these documents as empty scaffolding. Split when each contains useful, verified instructions.
