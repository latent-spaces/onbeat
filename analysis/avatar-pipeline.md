# Avatar sprites for reels

The reusable parts of [nilbuild/page-mascot](https://github.com/nilbuild/page-mascot)
are vendored in `vendor/page-mascot/`. The upstream code and assets are unchanged;
`UPSTREAM.json` records the exact commit, selected files and SHA-256 checksums.
Keep its MIT `LICENSE` with copies of the code and assets.

## What we imported

- `skills/page-mascot/reference/`: character descriptions, six drawing styles,
  generation prompts, framing and consistency rules.
- `skills/page-mascot/scripts/`: generation, alpha screening, chroma key removal,
  atlas alignment/building and verification tools.
- `src/mascot.tsx`: the original React renderer, including sprite selection,
  pointer tracking, expressions and squash motion, for reference or web use.
- `characters/{afro,glasses,ballerina,skater}/`: four human examples, each with
  the original directions and reactions PNG sheets.
- `public/mascots/`: ready-to-use WebP atlases for those same examples.

The upstream demo site, deployment setup and other characters were omitted.
No npm dependency or global skill was installed. No new images were generated.

## Rebuild an existing example locally

From the music-reels repository root, the existing `.venv` has Pillow, NumPy and
SciPy. Run the full screening/build/verification pipeline without image generation:

```bash
MASCOT_ROOT="$PWD/vendor/page-mascot" \
  .venv/bin/python vendor/page-mascot/skills/page-mascot/scripts/mascot.py \
  afro --skip-generate --dest "$PWD/out/page-mascot-check"
```

This writes two atlases under `out/`; it does not modify the vendored examples.
For a separate environment, the upstream `scripts/requirements.txt` lists the
dependencies, including the OpenAI client used only for API generation.

## Generate our own human avatars

Use the upstream DIRECTIONS or REFERENCE prompt to create the first sheet. Generate
the EXPRESSIONS sheet with the first sheet attached as an image reference. Preserve
hair, face, clothing, palette, scale and shoulder position. Request actual alpha
transparency in the image tool; a painted checkerboard is not transparency.

Keep new source sheets in `characters/<name>/directions.png` and `reactions.png`
at the repository root, separate from the vendored originals. Then process them:

```bash
.venv/bin/python vendor/page-mascot/skills/page-mascot/scripts/mascot.py \
  my-avatar --skip-generate --dest "$PWD/video/assets/avatars"
```

The upstream `generate.py` is also included, but its hard-coded model default is
upstream-specific. Before using its paid API route, choose a model available on the
account via the `MASCOT_IMAGE_MODEL` environment variable and provide `OPENAI_API_KEY` through
the environment. The orchestrator can retry generation, so use `--skip-generate`
when processing sheets that already exist.

## Use the technique in HyperFrames

The React component is an interactive web mascot. For our rendered reels, select
sprite cells from composition time instead of pointer events or wall-clock timers.
The integration below is a design for the next composition, not an implemented
video adapter.

Both atlases are 3×3. Use a square crop with background size `300% 300%`.
For cell index `i`, the background position is `(i % 3) * 50%` horizontally and
`floor(i / 3) * 50%` vertically.

| Index | Directions | Reactions (renderer names) |
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

The prompt describes reaction 4 as star-shaped eyes although the renderer names it
`wink`; inspect the actual art when assigning reactions.

Use our song timing JSON to place gaze changes, blinks and reactions at explicit
times on a paused, registered GSAP timeline. Animate position, rotation and squash
on a parent wrapper so changing cells preserves alignment. Preload both sheets.
Keep assets local and evaluate every state deterministically when seeking backward
or forward. Read `video/AGENTS.md` and the HyperFrames skills before implementing
the composition, then run its check and inspect snapshots.

## Dancing needs an additional asset pipeline

These are bust portraits, including the ballerina and skater. They contain head
directions and expressions, not full-body motion, a skeleton or dance frames.
The existing pipeline can supply faces, reactions and simple beat-synced bobbing.

For full-body dancing, reuse the reference-image and consistency approach to create
an ordered sequence of full-body poses, with one character, outfit, camera, scale,
canvas and ground line. Define the beat subdivision and loop seam explicitly.
Build a separate pose atlas and drive its frame index from composition time.
Do not pass those poses through the unchanged bust builder: its shoulder alignment,
body-matching checks and bottom fade assume a stationary torso and can distort or
reject deliberate body movement. A dance atlas needs foot/ground anchors and
checks for clipping, identity consistency and continuity at the loop seam.

For fluid dancing beyond a short stylized sprite loop, a rigged character or
generated motion clip is a separate option; page-mascot does not provide either.
