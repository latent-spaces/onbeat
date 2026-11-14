# Runbook: illustrated characters in music reels

Last reviewed: 2026-11-14. This records the workflow tested in the avatar session,
with extension points for other generators and future production lessons.

The sequence is **song cut → visual reference → character approval → separate
sprite sheets and scene layers → timed composition → karaoke → frame review →
render → handoff**. Prove a short test before expanding the full video.

## Working examples and boundaries

| Location | Role |
| --- | --- |
| `video/avatar-dance-test/` | Self-contained 11.52 s prototype, generation prompts, source art, processed atlases, karaoke builder and review notes |
| `video/allow-always-final/index.html` | Full-song integration maintained by the other production session; inspect its current state before editing |
| `video/data/allow-always-final.json` | Full-song beats, bars and aligned sung words |
| `video/avatar-dance-test/assets/action/` | Console and explosion sheets, frame rectangles, prompts and integration notes |
| `THIRD_PARTY_NOTICES.md` | MIT notice and credit for the sprite-atlas approach adapted from page-mascot (the vendored copy was removed) |
| `songs/allow-always/branding/instagram-robot-profile.png` | Single-image profile portrait derived from the approved robot |

The tested generator was the built-in `image_gen` tool. Other-generator support
below is an interchange procedure, not an implemented provider adapter or a claim
that those providers have been tested on this project. No new generation is
required to rebuild the existing video.

Before composition changes, read `video/AGENTS.md` and the current HyperFrames
skills. Discover code through the codebase graph when indexed; fall back to local
reads when it is not. Preserve other sessions' edits and staged changes. Do not
regenerate assets or rewrite the full video merely to add a learning-log entry.

## 1. Choose audio and establish one clock

Choose the actual song take and sung lyrics first. The early attempt to script a
long story and make the song obey it failed; see `../playbook.md`, sections 8–10.
Use the recorded performance to determine edit structure and caption words.

The reusable analysis entry point, from the repository root, is:

```bash
.venv/bin/python scripts/timing.py songs/<song>/<take>.mp3 \
  --lyrics songs/<song>/<sung-lyrics>.txt -o out/timing/<song>.json
```

Replace placeholders before running. This needs FFmpeg, the audio-analysis Python
environment, and `.venv-align` for sung-word alignment. `--no-words` does only beat
analysis. Read `scripts/timing.py` and `scripts/align_words.py` before changing the
alignment route; do not install a different transcription stack by assumption.

The prototype uses **125.009 BPM**, beat period **0.479965 s**, and full-song
seconds **27.2768–38.7959**, six four-beat bars. Its render is rounded to 346 frames
at 30 fps, approximately 11.533 s. Small decimal differences at the end are frame
rounding, not an invitation to retime the song.

For every local event, use `localTime = fullSongTime - sourceStart`. Apply the same
offset to beats, words, sound effects and scene actions. Never apply it twice.
Check whether a bar cut truncates a sung word; this prototype starts and ends
during words. For a finished reel, choose a musically and lyrically clean cut or
explicitly handle the partial-word highlights.

The full-song WAV used during development lives under ignored `out/dev/`; the
prototype includes its own tracked `assets/chorus.wav`, so that short composition
can render without the development WAV. A fresh clone does not contain every
ignored full-song audio/render file.

## 2. Approve the visual language using images

Create a contact sheet for choosing a direction, then stop broad exploration once
the person selects one. The initial robot grid was useful; the first human grid
was too glossy, saturated and exaggerated. The actual supplied anime frames
resolved the ambiguity better than the phrase “80s anime.”

The approved language: long narrow faces, small mouths, heavy upper eyelids,
simple shag/bob silhouettes and curled cheek locks; fine ink, opaque flat fills,
hard cel shadows; dusty coral, ochre, steel blue and aubergine. Preserve this in
action inserts as well as portraits. The canonical sources are under
`assets/source/`, not temporary clipboard paths or the generator's cache.

Give every input image a role: identity reference, style reference, environment
palette, or edit target. Ask for precise changes while listing what stays fixed.
Save the selected image and the final prompt in the repository. A generated file
left only under `~/.codex/generated_images/` is not a portable project asset.

## 3. Define an asset contract before generation

Use [image-prompts.md](image-prompts.md) for reusable prompt shapes.

| Asset | Contract and playback |
| --- | --- |
| Selection board | Several designs; for approval, not direct animation |
| Close-ups | **One character per 3×3 sheet**, nine head angles/expressions, steady shoulders and scale |
| Dance | One character per 4×4 sheet, 16 ordered poses; fixed camera, identity, outfit, world scale and ground line |
| Console insert | One 3×3 over-the-shoulder action sequence; fixed robot neck, console and camera; fingers contact buttons |
| Explosion | One 3×3 effect evolving spark → fireball → smoke → embers; fixed origin/scale; play once, then hide |
| Scene | Independent opaque space, transparent planet cutout, opaque ship foreground with a transparent window hole |

All sprite indices are zero-based and read left-to-right, then top-to-bottom.
Require actual PNG alpha, empty gutters, full figures inside cells, no labels or
grid lines. The console itself remains opaque; only the surrounding background
is transparent. Likewise, the ship floor stays opaque while the window opens to
the layer behind it.

Describe **successive actions**, not a collection of random poses. For dancing,
give weight shifts, foot contacts, arm movement and a last-to-first loop seam.
For an effect, give distinct growth and dissipation stages. Many buttons alone
do not create frantic clicking: require two hands moving across distant banks,
button depression, indicator changes and a specific launch/contact frame.

The preferred console is `robot-controls-over-shoulder-3x3-v2.png`: 3×3,
1254×1254 overall, 418×418 cells. It has dense button banks, Earth on the CRT,
and faint changing reflections of the two dancers. Repeat frames 0–5 at 10–12 fps,
then play 6–8 once; **frame 7 presses launch**. Version 1 launches on frame 8:
never transfer a frame number between revisions without looking.

## 4. Inspect transparency, alignment and identity

Inspect files over both light and dark backgrounds, and inspect the alpha channel.
RGBA mode or a minimum alpha of zero alone is insufficient: a painted background
or low-alpha colored fringe can survive around the real cutout. Do not infer
quality from the tool's thumbnail background. Check gutters and interior holes,
not just the four outer corners. Keep the original file before cleanup.

Measure dimensions and cell rectangles. Some generated 4×4 sources were 1254 px
wide, which is not divisible by four. Use rounded cell boundaries and pack equal
output cells; do not repeatedly crop by truncated integer division. The original
3×3 action sheets are evenly divisible, with rectangles in `sprites.json`.

`video/avatar-dance-test/prepare_assets.py` is the tested project-specific packer:

```bash
.venv/bin/python video/avatar-dance-test/prepare_assets.py
```

It requires Pillow, NumPy and SciPy. It packs dance cells at 384 px and close-ups
at 480 px, removes disconnected alpha specks, anchors dance feet at 94% of cell
height, and writes lossless WebP atlases plus close-up PNGs. It also rewrites the
prototype timing metadata from hard-coded song/bar selections. Review those
constants before reuse: it is **not** a generic CLI for arbitrary songs/sheets.

Do not feed explosion smoke/debris through the character cleanup blindly:
disconnected components are part of that effect. Do not normalize every pose to
its own bounding box: it destroys constant scale and can cause visible pumping.

The sprite-atlas approach comes from page-mascot (nilbuild, MIT): square grids,
equal cells, fixed anchors and alpha checks per cell. Its bust builder expects a
stationary torso, so it does not suit full-body dance; our packer and
`skills/music-reel/sprites/sprites.py` do that part. Credit and notice are in
`../../THIRD_PARTY_NOTICES.md`; the lessons we kept are in `../avatar-pipeline.md`.

## 5. Compose the place from separate layers

The tested back-to-front stack is:

1. Space background.
2. Planet, moved independently for parallax.
3. Planet impact explosions and the distant part of the laser.
4. Ship interior/window frame, masking the outside world through its alpha hole.
5. Characters, console inserts and any interior beam section.
6. Karaoke captions.

An exterior explosion should disappear behind the opaque window frame. A beam
that starts inside the room can need separate interior/exterior segments rather
than one overlay above everything. Anchor the effect where it hits the planet,
not to the viewport if the planet is moving.

The gag is causal: button mashing → launch press → beam → planet impacts, while
the humans remain oblivious and keep dancing. On a console close-up they can
remain visible as screen reflections; on wide shots keep their dance sequences
running through the action. Reflections baked into a sprite are illustrative,
not a live reflection of the currently rendered characters. A dynamic reflection
layer is a future extension if exact synchronization matters.

## 6. Drive sprites from composition time

Use one paused registered GSAP timeline per composition. No pointer events,
wall-clock timers, unseeded randomness, network fetches or infinite animation loops.
Every visible state must reproduce when seeking forward and backward.

For an `N×N` sheet, use `background-size: N*100% N*100%` and frame `i` at:

```js
const x = (i % N) * 100 / (N - 1);
const y = Math.floor(i / N) * 100 / (N - 1);
// backgroundPosition: `${x}% ${y}%`
```

The dance test advances 16 poses per four-beat bar: one frame every
`beatPeriod / 4`, about 8.33 sprite frames/s at 125 BPM, inside a 30 fps video.
Different phase offsets keep the cast from moving identically. Do not simply
raise sprite speed to the render frame rate: choreography should fit the music.

Write timed clips in markup with IDs, `data-start`, `data-duration` and `class=clip`.
Keep sub-composition styles/scripts inside its `<template>`, and match its ID to
the host and timeline registration. Animate inner wrappers rather than fighting
framework clip visibility. Preload local atlases; inspect their actual size in the
vertical frame before planning a full sequence.

## 7. Add karaoke from sung-word timings

`build_karaoke.py` generates editable static markup and a word manifest from the
existing song alignment. It is specific to this cut: duration, source file, lyric
line numbers and line breaks are constants. Change those deliberately for a new
song. Repeated words are identified by position/ID, not by matching their text.

```bash
.venv/bin/python video/avatar-dance-test/build_karaoke.py
```

The tested look is 82 px uppercase bold italic cream lettering, dark outlines,
cyan offset shadows and pink word fills. Place captions where they remain readable
through both wide shots and close-ups; this test uses the upper part of the frame
because lower placement covered faces or dancing feet. Check phone-size output.

An exported review exposed incorrect interpolation of `clip-path` strings.
The fix was to animate a numeric CSS custom percentage and let CSS derive the mask:

```css
.karaoke-fill {
  --karaoke-progress: 0%;
  clip-path: inset(0 calc(100% - var(--karaoke-progress)) 0 0);
}
```

Tween that percentage linearly over each aligned word. Account for a word already
underway at the cut. Compare a partially sung word in the actual MP4 with the
expected fraction; completed-word screenshots alone missed this bug.

## 8. Check, preview, render, inspect the encoded file

For the existing prototype:

```bash
cd video/avatar-dance-test
npm run check
npx --yes hyperframes@0.9.2 snapshot --at 0.4,1.8,4.3,8,9.5 --no-end \
  --output out/review-new
npm run preview
npm run render:karaoke
```

Look at the snapshots before rendering. Keep the persistent preview alive while
the person reviews it. The current scripts pin HyperFrames 0.9.2; verify current
skills/CLI help before changing versions. A passing check does not prove the
dance looks smooth or the lyric alignment sounds right.

Inspect the **encoded MP4**, not only the source preview. Check runtime/layout,
caption fit and contrast, all important cuts, loop seams, hand-button contact,
transparent edges, foot sliding, effect occlusion, partial word fills, and audio:

```bash
ffprobe -v error -show_entries stream=codec_type,width,height \
  -show_entries format=duration -of json out/avatar-dance-karaoke.mp4
```

Write the findings in the project's `REVIEW.md`, distinguishing numerical checks,
visual inspection and actual listening. The earlier session measured audio and
used existing alignment; it did not listen to verify every word. Keep new exports
versioned. Outputs/caches belong in ignored directories; source assets and final
prompts belong in Git. Fix meaningful failures, rather than repeatedly rerunning
checks after a clean unchanged result.

## 9. Switch image generators without changing the animation system

The boundary is **local image + explicit metadata**, not a particular API. Keep
the same approved references, identity description, frame order, camera, anchors,
palette, margins and alpha requirements. Change only the provider-specific call.

| Route | How to use it |
| --- | --- |
| Built-in image generation, tested | Use `image_gen` with explicit references and `transparent_background: true` for cutouts; copy outputs into the project and record prompts |
| Another connected generator / Higgsfield, untested here | Use its available tool/skill, discover its current model and input schema, pass the same reference images and prompt contract, then save local outputs |
| Provider API/CLI, untested here | Select this route explicitly, use that provider's supported client and environment credentials, record the actual model/options; do not silently substitute a different model |
| Tool with no native alpha | Generate on one pure saturated key color, then key it out and inspect edges; never accept a painted transparency checkerboard |

For a future Higgsfield run, read the installed `higgsfield-generate` skill first.
Discover models with `higgsfield model list --json`, then inspect the selected
model with `higgsfield model get <model-id> --json` before submitting. Do not assume
alpha, reference-image count, output size, model availability or auth from this
document. This runbook does not install, authenticate or invoke a paid provider.

For a generator without reference-image support, use a fixed approved identity
description and inspect drift especially carefully; generating per-frame images
can worsen identity consistency. An image-to-video route is a separate motion
pipeline, not a drop-in replacement for an atlas.

For keying, choose green or magenta absent from the subject; **remove every request
for transparency from the keyed prompt**. Keep both source and keyed output.
`skills/music-reel/sprites/sprites.py ingest --key magenta` is the keying route
(see `docs/sprites.md`). Never key against white/black when those colors are
in the robot or its outlines.

Record at least this beside each new asset (a proposed interchange record, not a
new loader implemented here):

```json
{
  "file": "robot-console-v3.png",
  "provider": "actual provider used",
  "model": "actual model or not exposed",
  "promptFile": "robot-console-v3-prompt.txt",
  "references": ["../source/robot-silver-closeups.png"],
  "grid": {"columns": 3, "rows": 3, "order": "row-major"},
  "dimensions": {"width": 1254, "height": 1254},
  "anchor": "fixed console and robot neck",
  "playback": {"fps": 12, "loopFrames": [0, 5], "launchFrame": 7},
  "alphaChecked": false
}
```

Dimensions/frame numbers above describe our v2 example, not guaranteed future
outputs. Measure the actual new sheet, update metadata and set `alphaChecked`
only after inspection. Compare providers on one representative action sheet using
the same references: identity, hand contact, cell alignment, alpha, small-size
readability and loop quality. Passing a still-image beauty test is not enough.

## 10. Handoff and extend

Give the integrating session exact paths, grid/cell dimensions, zero-based frame
order, loop/one-shot ranges, contact/launch/peak frame, timing origin and z-order.
Say whether an asset includes the console/reflections or expects separate layers.
Reference the current source revision; don't ask it to infer timing from a PNG.

```text
Asset: video/avatar-dance-test/assets/action/robot-controls-over-shoulder-3x3-v2.png
Grid: 3×3, 418 px cells, row-major, indices 0–8.
Loop: 0–5 at 10–12 fps; then 6–8 once; launch on frame 7.
Screen: Earth plus baked changing dancer reflections; console included.
Explosion: planet-explosion-3x3.png, peak frame 4, hide after frame 8.
Layer explosion over planet and behind ship/window frame. Keep humans dancing.
Integrate into current full-video state; export a new MP4 and inspect it.
```

Record new findings in [learning-log.md](learning-log.md). Add an entry from the
other process/session with its evidence and source paths; then promote a verified
lesson into the relevant step above. Keep untested ideas marked as experiments.
Useful next experiments: cleaner hand in-betweens, a generic sheet importer,
separate live dancer-reflection layers, and a controlled other-generator comparison.
