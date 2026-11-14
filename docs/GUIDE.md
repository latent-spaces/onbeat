# How "allow always" was made

**"allow always"** is a 2:24 vertical music video: a Suno song, drawn entirely in code with [HyperFrames](https://hyperframes.heygen.com) (HTML + GSAP → MP4), every visual timed to the measured beats and sung words. AI coding agents did most of the building; the person picked the take, gave a note on every render and made the creative calls.

This page is the short version: the pipeline, the lessons that mattered, and how to rebuild the reel. The full making-of (every pattern, gotcha and prompt) is the [original guide on the archive branch](https://github.com/oronanschel/music-reels/blob/archive/GUIDE.md).

## The pipeline

```
concept ─► song (Suno) ─► timing JSON ─► look + characters ─► composition ─► review ─► render ─► post
            person picks    scripts/        image generation    HyperFrames    snapshots   MP4
            the take        timing.py       + sprite sheets     index.html     + check
```

1. **Concept.** One claim a stranger could disagree with, shown with an interface everyone knows. Ours: a real permission prompt — `read ../billing-service/.env` — and the button you stop reading: *Allow always*.
2. **Song first.** Generate takes, choose one by ear, then write the storyboard to the take that exists.
3. **Timing.** Measure beats and sung words into one JSON file.
4. **Look.** One place, one hero object, characters from sprite sheets.
5. **Compose** on one paused GSAP timeline; **review** snapshots and phone-size renders; **render** a new versioned file each time.

## The song

Prompts, lyrics files and settings for every generation are in [`songs/allow-always/suno-prompts.md`](../songs/allow-always/suno-prompts.md). What worked:

- **Short lyrics around one chant hook**, not a bar-by-bar story — Suno never followed the story.
- **Section tags direct the arrangement**: an a cappella vocoder intro, a one-bar riser, a full-band drop. Name who sings in every tag.
- **One sound throughout** (four-on-the-floor, deadpan vocoder lead, a tired human answering). Change sections with filters, hard stops and silence, not new instruments.
- **Measure the tempo.** We asked for 122 BPM and got 125.009.
- **The person picks the take.** The agent drafts lyrics and Styles lines; the person generates, listens and chooses.

## Timing: beats first, words later

`scripts/timing.py` turns the song into one JSON file that every composition reads (`make timing SONG=<name>` wraps it).

- **Beats-only (start here).** Needs only the main Python environment and ffmpeg. Gives the beat grid, bars, sections (kick or no kick) and envelopes — everything sprites, bounces and cuts need. The template shows captions per line or per bar.
- **Sung words (karaoke).** `make setup-align`, then `make timing SONG=<name> WORDS=1`. Demucs isolates the vocal, faster-whisper transcribes, WhisperX aligns each word.
- **Suno doesn't sing what you wrote.** Listen first, write down the lines actually sung with a time window each, and align each line inside its window (`songs/allow-always/align_final.py`). Whisper mishears vocoder words ("like always" for "allow always"): mark guesses and confirm them on the render.
- The grid is moved onto waveform attacks: the onset envelope runs 35–45 ms late, which makes on-beat visuals look early.

| Key | Meaning |
|---|---|
| `mode` | `"beats-only"` or `"words"` |
| `audio`, `duration`, `fps` | source file, seconds, frame rate |
| `bpm`, `beatPeriod`, `beatsPerBar` | one fixed tempo |
| `beats`, `bars` | seconds; `bars` are the downbeats |
| `sections` | runs of bars with or without kick (`start`, `end`, `kick`) |
| `envelopes` | kick and loudness per frame, 0 to 1 |
| `words`, `lines` | sung-word times; empty in beats-only mode |

## The look

- **The frame is a place.** One viewpoint, one big hero object carrying the lyric, small things ticking on the beat around it. Our first cut was a dashboard of small UI parts and it didn't work. The final reel has two places: a desk with a giant permission dialog, and a retro orbital disco with the Earth in the window.
- **Characters are sprite sheets** — 16 dance poses per sheet, close-ups and action inserts as 3×3 sheets. Audition styles on one numbered grid, show reference images instead of describing a style, check alpha over light and dark. How to make and check them: [sprites.md](sprites.md). How they dance: [beat-motion.md](beat-motion.md).

## The composition

- **One HTML file, one paused GSAP timeline, every time from `window.TIMING`.** No hard-coded seconds, no `Math.random()` (use a seeded generator), no timers — every frame must be reproducible when seeking.
- **Two clocks.** The **beat clock** drives pulses, dance poses, console frames and explosions. The **voice clock** drives lyrics and the big narrative cuts. Lyrics never snap to the beat; they appear when the word is sung.
- **Loop it.** The first frame and the last two seconds are the same permission dialog, so the reel flows back into its start.
- **Gotchas:** keep the same number of `textShadow` entries when tweening; animate a number, not a `clip-path` string; keep captions off faces; make the loop frame match frame 0 exactly.

## What the feedback loop looked like

Most of the quality came from short notes on rendered videos:

| The person said | The fix |
|---|---|
| "we need more dramatic stops" | `dramatic hard stops and dead silence before every drop` in the Styles line |
| "80s style, glitches, camera effects, karaoke all the way" | a seeded VHS pass and three caption looks |
| "the first hook tells what's going to happen" | the loop hook: the same hesitating dialog at both ends |
| "make sure the captions are not on the faces" | a top caption band during close-ups |
| "too frantic … divide into two parts" | console frames every half beat; two inserts with dancing between |
| "the earth should explode all the time after the first explosion" | a seeded explosion on every beat until the scene ends |

Habits: the agent proposes and the person decides; ask before anything that costs money or can't be undone; change one thing per render and say which seconds changed; never overwrite a render.

## Rebuild the hero reel

The take, the curated timing and the composition are in the repo. Convert the take once (don't rerun `timing.py` or `cut_final.py` — that would overwrite the hand-corrected word timing), then render:

```bash
mkdir -p out/dev
ffmpeg -i songs/allow-always/take-final-yes.mp3 -ar 48000 out/dev/allow-always-final.wav
cd video/allow-always-final
npx --yes hyperframes@0.9.2 check
npx --yes hyperframes@0.9.2 render -o ../../out/allow-always-final.mp4    # ~4–7 min for 2:24 at 60 fps
```

The composition loads GSAP from a CDN, so the render needs network access.

## Dead ends

- A long story for Suno to perform; Duration Auto with "stadium anthem" styles (3-minute takes); a new instrument per section.
- Whisper on the full mix; plain forced alignment against lyrics Suno didn't sing.
- A dashboard of small parts; a text-only style prompt for characters; a title card that gave the ending away.
