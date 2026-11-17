# Beat-synced sprite motion

`example/src/spritedance.js` makes sprite characters dance on the song's measured beats. `example/src/synccheck.js` draws an overlay so you can check that they do. Both are classic scripts that define a window global, like `example/src/beatsync.js`. Both only add tweens to the composition's one paused GSAP timeline, so every frame is a pure function of timeline time, as HyperFrames requires.

Working example: `example/index.html` in this skill. The reusable helpers are `beatsync.js`, `spritedance.js` and `synccheck.js`; The default spaceship scene in `example/compositions/orbital.html` steps through its original pose order on quarter beats and its separate close-ups on half beats. In `examples/four-styles/`, `showcase.js` builds the alternate solo showcase, layered scenery and dedicated close-ups; `groove.js` supplies its authored body-pose order.

## The rule

Measured on reference reels:

- **16 poses per 4-beat bar.** The pose steps every quarter beat (`beatPeriod / 4`), about 8.3 sprite frames per second at 125 BPM, inside a 30 or 60 fps video. Don't raise the sprite rate to the render frame rate; the choreography should follow the music.
- **The downbeat selects an authored pose.** The helper defaults to pose 0. With an explicit `frames` list, choose the drawing that should carry the accent; a 16-step sequence loops once per four-beat bar.
- **Hop is optional.** The helper's default lands squashed on the beat, springs up at mid-beat and falls back by the next beat, with larger bar accents. Use `bounce: false` when the drawings already contain weight shifts or when added bobbing hides their rhythm. The approved showcase uses direct pose changes without synthetic hop, torso rotation or eased pose lag.
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
.clay   { background-image: url("assets/cast/clay.webp"); }
```

Then, in the timeline script:

```js
// One character
SpriteDance.dance(tl, TIMING, { target: "#clay", from: 0, to: TIMING.duration, cols: 4 });

// A cast: shared options, per-member overrides; phases default to 0, 8, 4, 12...
SpriteDance.cast(tl, TIMING, [{ target: "#moth" }, { target: "#beet" }, { target: "#clay" }, { target: "#anime" }], {
  from: 0,
  to: TIMING.duration,
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

### Directing body and face animation

Inspect the drawings before choosing their order. Put the clearest stamp, shoulder hit, point or held silhouette on a beat, then use the surrounding drawings to recover between hits. Do not assume an arbitrary first cell is the visual accent. The indices in `example/src/groove.js` were chosen for those particular sheets, not for every generated character.

The approved example uses direct GSAP sets for body drawings every quarter beat, with no extra hop or eased movement over the pose changes. This preserves the timing already drawn into the character. Other treatments remain valid when the person's sound-on review supports them; tests of frame placement alone cannot prove that a dance feels on the beat.

For a face-dancing close-up, use a new 3×3 portrait sheet and hold each drawing for roughly half a beat as a starting point. Alternate expressive head poses with recoveries, and keep the shot running for several beats. For example, after choosing the indices from that sheet:

```js
SpriteDance.dance(tl, TIMING, {
  target: "#face", from: TIMING.bars[1], to: TIMING.bars[2],
  cols: 3, rows: 3, frames: [1, 0, 4, 8, 3, 0, 4, 8],
  perBeat: 2, bounce: false, hold: "none",
});
```

Set the face element's background size to `300% 300%`. The portrait drawings supply facial and shoulder acting; a camera push into a body atlas does not. Let scenery layers drift by different small amounts over measured musical phrases, separately from the character clock, so depth motion does not obscure the accents.

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
