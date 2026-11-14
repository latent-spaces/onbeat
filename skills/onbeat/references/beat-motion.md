# Beat-synced sprite motion

`example/src/spritedance.js` makes sprite characters dance on the song's measured beats. `example/src/synccheck.js` draws an overlay so you can check that they do. Both are classic scripts that define a window global, like `example/src/beatsync.js`. Both only add tweens to the composition's one paused GSAP timeline, so every frame is a pure function of timeline time, as HyperFrames requires.

Working example: `example/index.html` in this skill. Copy the three files in `example/src/` into your reel.

## The rule

Measured on reference reels:

- **16 poses per 4-beat bar.** The pose steps every quarter beat (`beatPeriod / 4`), about 8.3 sprite frames per second at 125 BPM, inside a 30 or 60 fps video. Don't raise the sprite rate to the render frame rate; the choreography should follow the music.
- **Pose 0 lands on the downbeat.** Poses count from the bar's first beat, so a 4×4 sheet loops exactly once per bar.
- **Every kick gets a hop.** The body lands squashed on the beat, springs up to its highest point at mid-beat and falls back by the next beat. Bar downbeats get a bigger accent (×1.8 by default).
- **Phase offsets.** Characters start at different steps (0, 8, 4, 12…) so the cast doesn't move in lockstep.
- **Hold on silence.** In sections the beat tracker marked `kick: false` (intros, breaks, a cappella), dancers hold a pose and stop bouncing.
- **Measured beats, not a metronome.** Each beat from `timing.beats` is split into sub-steps, so the motion follows the real grid, including tempo drift.

## Use it

Load the script after GSAP and your timing data:

```html
<script src="src/spritedance.js"></script>
```

Make each dancer an element whose background is the sheet, sized `cols*100% rows*100%`:

```css
.sprite { background-repeat: no-repeat; background-size: 400% 400%; }
.robot  { background-image: url("assets/robot-dance.webp"); }
```

Then, in the timeline script:

```js
// One character
SpriteDance.dance(tl, TIMING, { target: "#robot", from: 12.0, to: 29.2, cols: 4 });

// A cast: shared options, per-member overrides; phases default to 0, 8, 4, 12...
SpriteDance.cast(tl, TIMING, [{ target: "#ochre" }, { target: "#blue" }, { target: "#robot" }], {
  from: 12.0,
  to: 29.2,
  cols: 4,
  bounce: { px: 16, squash: 0.05, downbeat: 1.8 },
});
```

### Options

| Option | Default | Meaning |
|---|---|---|
| `target` | required | Element or selector that shows the sheet |
| `from`, `to` | required | Time range in seconds |
| `cols`, `rows` | 4, `cols` | Grid of the sheet |
| `sheet` | none | A `sprites.json` sheet entry: uses its frame rects instead of a regular grid (see `sprites.md`) |
| `poses` | `cols*rows` | Poses in the cycle |
| `frames` | none | Explicit pose list, e.g. `[0, 1, 2, 1]` for a 3-frame bob |
| `perBeat` | 4 | Pose steps per beat (2 = eighth notes, 1 = one pose per beat) |
| `phase` | 0 | Offset in steps |
| `hold` | `"silence"` | `"none"` keeps dancing through kick-less sections |
| `holdPose` | 0 | Pose held on silence |
| `bounce` | on | `false`, or `{ target, px: 14, squash: 0.06, downbeat: 1.8 }`. Put the bounce on a wrapper (`target`) if the sprite element already has its own transforms |

### Pure helpers

These are for planning and tests; none of them touch the DOM.

- `SpriteDance.poseAt(timing, t, opts)`: the pose on screen at time `t` (`null` outside `from`–`to`).
- `SpriteDance.steps(timing, from, to, perBeat)`: the step times.
- `SpriteDance.silentAt(timing, t)`, `beatIndexAt`, `beatInBar`.
- `SpriteDance.cellPosition(i, cols, rows)` and `rectPosition(sheet, i)`: `background-position` for a grid cell or a `sprites.json` frame.

Tests: `node --test tests/spritedance.test.cjs`.

## Timing data it reads

The timing data from `scripts/timing.py` (it writes `timing.js`, which sets `window.TIMING`): `beats`, `bars`, `beatPeriod`, optional `fps` (default 30), optional `beatsPerBar` (default 4) and optional `sections` (`start`, `end`, `kick`). It works in beats-only mode, because it never needs `words`.

## A cast joining the dance

Keep each character's sprite inside a wrapper. Animate the wrapper's `x`, `y` and opacity for an entrance, and let `SpriteDance.dance` own the inner sprite's pose and hop. This prevents entrance travel from fighting the beat bounce. Choose entry times from `timing.bars` or `timing.beats`; stagger phases such as 0, 8 and 4 so the cast shares the music without identical poses.

For a short draft, report its source interval and preserve the full-song grid. If the person requests an exact seconds interval rather than whole bars, crop the audio to that interval and subtract its start from every retained beat, bar, section and word; clip section/word endpoints to the excerpt and rebuild line indices. Do not reset beat phase to zero unless the excerpt actually starts on a measured beat. A later visual revision should reuse the same cropped audio and timing data.

## Sync check

```html
<script src="src/synccheck.js"></script>
```

```js
if (SyncCheck.wanted()) SyncCheck.overlay(tl, TIMING, { parent: document.getElementById("root") });
```

It's on when the preview URL has `?synccheck`, or when the page sets `window.REEL = { syncCheck: true }` before this code runs (use that to render a check video). It draws:

- a ruler along the bottom that scrolls under a fixed red playhead: thin ticks for beats, tall amber ticks and "bar N" labels for downbeats, green bars for each sung word, with the word text;
- an amber flash at top right on every beat (full size on downbeats);
- the word being sung right now, next to the flash.

If a hop or a cut lands visibly before or after the flash and the tick under the playhead, the timing or the animation is off. Turn it off before the final render.
