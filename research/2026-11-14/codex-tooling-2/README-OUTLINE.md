# Proposed public README hierarchy

Draft by codex-tooling-2, 2026-11-14. This is a content specification, not a replacement README or an implemented feature list. The sample/skill/CLI described below must be built and checked before advertising them as usable.

## First screen

**Title:** music-reels

**Proposed positioning:** Turn your song into an editable, beat-synced lyric reel.

**Current-state qualification:** Experimental local workflow for audio timing and HyperFrames compositions. A complete, reproducible sample render is a release prerequisite.

**Visual:** one actual portrait render, with a legible poster and a visible play affordance. Provide a text description and lyric transcript. Identify it as an output from the checked-in sample, once that is true. Avoid using a concept mockup or another creator's reel as product output.

**Primary action:** Run the sample. Add the exact verified command and expected output path when the implementation supports it. Do not introduce a fictional `npx music-reels` command or package name.

**Secondary actions:** Watch with sound · How it works · Bring your own audio.

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
| Bundled audio and timing, after they are provided | User-provided song and optional lyrics |
| State whether any keys/accounts are actually needed | Identify optional external services separately |
| State first-run downloads and local requirements | Explain alignment/model downloads and compute requirements |

The existing pipeline's setup gaps must be resolved before this section can claim a no-key happy path. Link codex-tooling-1's research for details.

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

Explain in two sentences: musical beats drive pulses and cuts; word timestamps drive lyric highlighting. Link the actual timing schema and a small worked example. Say which steps are automated today and which involve manual selection/design.

## 4. Bring your own song

Document supported audio and lyric inputs, how to select a short loop, how to compute/correct timing, where to swap assets and how to render. Use a generic sample path, not a song-specific script disguised as a general importer. Suno can be one source of audio; avoid implying this is an official Suno integration.

## 5. Customize one thing

Show how to change a palette, lyric style or beat motion, with one named editable file and before/after output from the same audio segment. Add an agent-skill route only after a distributable skill exists and has been tested. Keep CLI and agent routes aligned on the same underlying contract.

## 6. Limitations and requirements

Include actual platform requirements and known issues: variable tempo, ambiguous beats, vocals/alignment, language support and hardware dependence where applicable. State that timing can need manual correction. Avoid claims of perfect sync, any-song support, deterministic end-to-end output or one-click creative quality without evidence.

## 7. Reuse, contribute and maintain

Link the chosen code license, sample-media terms, contribution guide and useful small tasks. Suggested first contributions, once interfaces are stable: a timing fixture, a template preset, a documented setup fix. Keep the original research playbook accessible under “Design notes”; retain its measured/judged/hypothesis labels.

## Suggested documentation split

- Root README: product explanation, output, sample path, limitations and links.
- User guide: own-audio workflow and troubleshooting.
- Timing reference: JSON contract and correction examples.
- Maintainer notes: current story, session history and experiments.
- Contribution guide: checks, sample fixtures, preset interface and review expectations.

Do not create all these documents as empty scaffolding. Split when each contains useful, verified instructions.
