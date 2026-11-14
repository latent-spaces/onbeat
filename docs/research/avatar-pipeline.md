# Avatar sprites for reels

For the implemented workflow, including dance/action sheets, scene layers, karaoke and
other-generator interchange, see the [production runbook](../runbooks/animated-music-reels.md).
This document keeps the sprite-atlas technique and the lessons we took from
[page-mascot](https://github.com/nilbuild/page-mascot) by nilbuild (MIT). We adapted the
approach and removed the vendored copy; credit and the MIT notice are in
[`THIRD_PARTY_NOTICES.md`](../../THIRD_PARTY_NOTICES.md). No upstream character art is used.

## The technique

A character is one square **sprite sheet**: a grid of equal cells, each cell a pose or
expression of the same drawing. The renderer shows one cell at a time by choosing a frame
index. Nothing is animated inside the image; motion comes from which frame is shown and
from moving, rotating and squashing a wrapper around it.

For a 3×3 sheet, show cell `i` with a square crop, `background-size: 300% 300%`, and
position `(i % 3) * 50%` horizontally, `floor(i / 3) * 50%` vertically. For a 4×4 sheet
use `400%` and steps of `100/3 %`. Indices are zero-based, left to right then top to
bottom. `sprites.json` (see `docs/sprites.md`) stores the exact rectangle of every frame,
so code should read rectangles, not recompute them.

### Bust layout used by the original: directions and reactions

| Index | Directions | Reactions |
| --- | --- | --- |
| 0 | up-left | blink |
| 1 | up | heart |
| 2 | up-right | sparkle |
| 3 | left | surprised |
| 4 | center | wink |
| 5 | right | bashful |
| 6 | down-left | sleepy |
| 7 | down | dizzy |
| 8 | down-right | delighted |

Two 3×3 sheets per character: **directions** (same calm face, only the head turns) and
**reactions** (nine expressions, generated with the first sheet attached as a reference so
the identity matches). Inspect the actual art when assigning reaction names.

## Rules that came from measuring many characters

- **The body is one drawing; only the head moves.** Models redraw the body in profile when
  the head turns. A bust with visible shoulders reads stable from every angle.
- **The head dominates.** Shoulders at roughly two thirds of the head width.
- **Nothing touches a cell edge.** Hearts, sparkles and wide ears are the usual casualties;
  clipped art cannot be recovered, so say in the prompt to draw wide features smaller.
  Leave clear space below the shoulders too.
- **Loose long hair is the most common failure** because it is drawn differently in each
  sheet. Tie it back, or use a bun, beanie or hat.
- **State what you want, not what to avoid.** Telling an image model "flat, no gradients"
  gets exactly that. Ask for appeal and detail instead.
- **One fresh chat per character, two messages** (directions, then reactions with the first
  result attached). Retrying inside a long chat averages the attempts and the sheets stop
  matching.
- **Transparency comes from the tool's own option, not the prompt.** A prompt that only
  asks for transparency gets a painted grey-and-white checkerboard, which is unrecoverable.
  For tools without alpha, ask for one flat saturated key colour (green or magenta), never
  mention transparency, then key it out (`sprites.py ingest --key`).

## Use it in HyperFrames

Select sprite cells from composition time, not pointer events or wall-clock timers. Place
gaze changes, blinks and reactions at explicit times on a paused, registered GSAP timeline.
Animate position, rotation and squash on a parent wrapper so changing cells preserves
alignment. Preload sheets, keep assets local, and make every state a pure function of the
timeline time so seeking backwards works. Read `video/AGENTS.md` and the HyperFrames
skills first, then run `check` and inspect snapshots. The implemented dance and portrait
examples live in `video/avatar-dance-test/`.

## Dancing needs a different sheet

Bust sheets have head directions and expressions, not body motion. The original bust
builder pins the shoulders and fades the bottom, so it rejects or distorts deliberate body
movement. For dancing, generate an ordered sequence of full-body poses with one
character, outfit, camera, scale, canvas and ground line, define the beat subdivision and
loop seam explicitly, and pack it as its own atlas (16 poses per four-beat bar in our
runbook). Check foot/ground anchors, clipping, identity and continuity at the loop seam.
For fluid dancing beyond a short stylised sprite loop, a rigged character or generated
motion clip is a separate option.
