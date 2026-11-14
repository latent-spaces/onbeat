# Production learning log

Append dated observations here, then promote verified repeatable steps into
[the runbook](animated-music-reels.md). This is also the place for the person's
notes from the other process. Keep that session's findings distinct from ours.

## 2026-11-13 — avatar/sprite session, documented 2026-11-14

| Observation | Evidence | Reusable change |
| --- | --- | --- |
| “80s anime” was too ambiguous; first humans were glossy and exaggerated | Rejected human grid and supplied anime-frame references in the chat; approved casting at `video/avatar-dance-test/assets/source/casting.png` | Approve actual image references and concrete face/hair/palette rules before producing animation |
| A selection board is not a usable per-character atlas | User requested separate transparent 3×3 sheets after mixed boards | One identity per production sheet; explicit expression/angle order |
| A single panel finger-tap felt too slow/simple | First console versus `assets/action/robot-controls-over-shoulder-3x3-v2.png` | Dense controls, two-handed traversal, button contact, visible indicators and explicit launch frame |
| Specific camera language matters | User corrected front/whole-body interpretation to behind-neck view | Describe foreground neck/shoulder, camera direction, hand contact and screen in the prompt |
| “Transparent” text alone is not an alpha guarantee | Generated sources varied in alpha; native alpha/background extraction was requested | Inspect alpha plus composites on light and dark; retain source and cleanup provenance |
| Original 4×4 sheets were 1254 px, not divisible by four | Source dimensions versus 1536 px packed dance atlases | Rounded crop boundaries, equal packed cells, constant scale and feet anchors |
| Generated sprites have line/shape drift | Prototype `REVIEW.md` and frame contact sheets under ignored output | Treat as a limited-animation test; budget manual correction or a different motion pipeline for final polish |
| Outer hands clipped in the initial ensemble | Prototype review changed 940 px actor boxes to 760 px | Inspect extended limbs across the sequence, not only a neutral pose |
| Planet/window separation made action compositing possible | `ship.png`, `planet.png`, `space.png` | Keep masking foreground and outside world independent from generation onward |
| Completed-word screenshots missed a karaoke fill bug | Incorrect first MP4; corrected samples at 0.4/1.8 s recorded in `REVIEW.md` | Animate numeric CSS percentage and inspect partial fills in encoded output |
| Console launch frame changed across revisions | v1 frame 8; v2 frame 7, zero-based, in `assets/action/sprites.json` | Every handoff needs versioned path and event-frame metadata |
| Audio presence/levels were measured, not listened to in this session | H.264/AAC output; prior measured mean −18.9 dB, peak −6.0 dB | Distinguish measurement from listening; don't claim every sung word was heard/verified |

The main prototype uses an 11.52 s cut from 27.2768 s. Its timing/generation
helpers contain project-specific constants. They are useful examples, not a
finished reusable provider/asset framework.

## Other full-video/process session — pending contribution

The full-video integration exists in `video/allow-always-final/index.html` and
was already committed separately. Its current uncommitted edits belong to that
ongoing session. This log does not claim those edits were reviewed or validated
as part of the runbook task.

**2026-11-14, full-video session:** findings are written up in [`GUIDE.md`](../../docs/GUIDE.md)
(sections 4–9: Suno, alignment against what was actually sung, the composition patterns,
gotchas, the feedback table) and in `songs/allow-always/suno-prompts.md`. The final render
is `video/out/allow-always-final-80s-boom2.mp4`.

## Entry template

```text
Date / session / author:
Goal and source revision:
What we tried (provider/model if relevant):
Observed result and evidence paths/timestamps:
What failed or remained uncertain:
Decision and exact reusable change:
Checks performed / actually listened or only measured:
Runbook section to update:
Next experiment, if still untested:
```

Future provider experiments should compare the same reference and action contract,
not unrelated images. Save the chosen output, exact prompt, references, actual
dimensions/alpha findings and provider/model provenance. Do not record a proposed
generator as “tested” until its outputs have been inspected in the composition.
