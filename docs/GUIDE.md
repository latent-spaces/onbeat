# How "allow always" was made

The short making-of for the 2:24 vertical music video behind this repo: a Suno song, measured beats and sung words, and a picture drawn in code with [HyperFrames](https://hyperframes.heygen.com). AI coding agents (Claude Code, Codex) did most of the building. The person picked the take, gave notes on every render and made the creative calls.

The full 390-line version, with every prompt, pattern and gotcha, is [here (permalink)](https://github.com/oronanschel/music-reels/blob/c32e45a/docs/GUIDE.md). The playbook and runbooks it cites are on the [`archive` branch](https://github.com/oronanschel/music-reels/tree/archive). To make your own reel, start with the [README](../README.md) and [TRY-IT](TRY-IT.md) instead.

## 1. The pipeline

```
concept ─► song (Suno) ─► timing JSON ─► look + characters ─► composition ─► review ─► render ─► post
            person picks   make timing     sprite sheets        one GSAP        check +     MP4      caption
            the take                       (docs/sprites.md)    timeline        snapshots
```

Everything on screen follows one of two clocks. The **beat clock** drives pulses, dance poses, console frames and explosions. The **voice clock** drives lyrics and the big narrative cuts. Lyrics never snap to the beat; they appear when the word is sung.

## 2. Setup

Tested on macOS: ffmpeg 8.0, Node 26, HyperFrames 0.9.2 (pinned in every command), GSAP 3.15, Python 3.14 for `.venv` (librosa, numpy, scipy, Pillow) and Python 3.12 for `.venv-align` (WhisperX 3.8.6, Demucs 4.1.0, faster-whisper 1.2.1, torch 2.8). `make setup` and `make setup-align` install the pinned versions. Keep two environments, because WhisperX pins its own torch and breaks a general audio environment.

## 3. Concept

- **One sentence a stranger could disagree with.** Ours: you stop reading the permission prompts and click "allow always". Insider jokes did worse than universal, arguable claims.
- **The picture contradicts or dramatises the claim**, and it works with the sound off. Our hook is a real-looking permission prompt with Yes / No / Allow always.
- **One causal chain, not a list of gags.** The agent asks → the human says yes → begs it to approve everything → "allow always" → the agents throw a disco → a robot hits launch → the Earth explodes while everyone keeps dancing.
- **The ending loops back to the start**, so Instagram's loop flows into frame 0.

## 4. The song

Prompts and settings: [`songs/allow-always/suno-prompts.md`](../songs/allow-always/suno-prompts.md).

- **Song first, story second.** A 33-line bar-by-bar story was never followed. What worked: short lyrics around one chant hook, several takes, pick by ear, then storyboard the take that exists.
- **Section tags direct the arrangement:** an a cappella vocoder intro, a one-bar riser, then a full-band drop. Name who sings in every tag.
- **Four-on-the-floor, a deadpan vocoder lead, one syllable per beat in the chant, call and response with a tired human voice.** Keep one sound; change sections with filters and hard stops.
- **Measure the tempo.** We asked for 122 BPM and got 125.009.
- **The person generates and picks the take.** Agents prepare lyrics and Styles lines; they never touch CAPTCHAs, credits or downloads without asking.

## 5. Timing

```bash
make timing SONG=<name>                  # beats only (easy start)
make timing SONG=<name> WORDS=1 FORCE=1  # add sung words (needs make setup-align and lyrics.txt)
```

### 5.1 Beat grid (beats-only mode)

One fixed tempo from a comb search over the onset envelope. The grid is then **moved onto waveform attacks**, because the envelope runs 35–45 ms late and on-beat visuals would look 2–3 frames early. The downbeat is where the sub-80 Hz level jumps most. Sections are runs of bars with or without kick, which became our scene boundaries. Beats-only needs no lyrics and no `.venv-align`, and it is enough for sprites, bounces, cuts and bar-placed captions.

### 5.2 Sung words

Demucs isolates the vocal stem (on the full mix, Whisper skipped most words), faster-whisper transcribes it, and WhisperX force-aligns each word. What went wrong:

- **Suno doesn't sing what you wrote.** It doubled lines and reordered the second half, so plain alignment lost its place after 41 s. Fix: transcribe the stem first, write down the *sung* lines with a time window each (`songs/allow-always/align_final.py`), and align each line inside its window.
- **Whisper mishears vocoder words** ("like always" for "allow always"). Flag guesses and confirm them on the render.
- **Stacked or zero-length words** mean the aligner placed words that weren't sung. Tighten the windows.

### 5.3 The timing JSON

| Key | Meaning |
|---|---|
| `mode` | `"beats-only"` or `"words"` |
| `audio`, `duration`, `fps` | source file name, seconds, frame rate |
| `bpm`, `beatPeriod`, `beatsPerBar` | one fixed tempo |
| `beats`, `bars` | seconds; `bars` are the downbeats |
| `sections` | runs of bars with or without kick (`kick: false` = hold dancers) |
| `envelopes` | kick and loudness, one value per frame, 0–1 |
| `words`, `lines` | sung-word times; empty in beats-only mode |

## 6. Look and characters

- **The frame is a place with one big hero object**, not a dashboard of small UI parts (that first cut failed). Ours: a desk world with a giant permission dialog, and a retro orbital disco with the Earth in the window.
- **Show reference images instead of describing a style.** "80s anime" in words came out glossy; three reference frames fixed it.
- **One character per sheet:** 3×3 close-ups, and 4×4 dances of 16 successive poses over one bar. Action inserts (console, explosion) are sheets too; record their key frame numbers.
- **Check alpha for real** over light and dark backgrounds. A painted checkerboard isn't transparency. Sheet tooling: [docs/sprites.md](sprites.md). Motion: [docs/beat-motion.md](beat-motion.md).

## 7. Composition

One HTML file, one paused GSAP timeline, every time taken from the timing JSON. No `Math.random()` (seed it), no timers, no `Date.now()`, and every state reproducible when seeking backwards. Helpers live in `video/src/` (`beatsync.js`, `spritedance.js`, `synccheck.js`); `video/template/` is the song-agnostic version of what we built by hand in `video/allow-always-final/`.

Gotchas worth knowing: GSAP can't tween between `textShadow` lists of different lengths; animate a number, not a `clip-path` string; keep captions off faces; make the loop frame match frame 0 exactly; extend a scene until its last effect finishes.

## 8. Review and render

`hyperframes check` caught overlaps and hidden text; snapshot the exact moments you changed before rendering; send a 720p phone copy for review; inspect the encoded MP4, not only the preview; never overwrite a render. The full reel took 4–7 minutes to render at 60 fps.

## 9. Working with an agent

Most of the quality came from short, blunt notes on renders: "too frantic … divide into two parts", "make sure the captions are not on the faces", "the earth should explode all the time after the first explosion". Habits that worked: the agent proposes two or three options with a recommendation and the person decides; ask before anything that costs money or can't be undone; change one thing per render and say which seconds changed; mark guesses as guesses.

## 10. Posting

Upload the full-quality file unchanged so the loop holds; pick a cover from inside the video; caption = hook, one or two lines of context, "details if you replay it", a tools credit, one genre hashtag. Keep the bottom third quiet (Instagram's UI covers it). Links in captions aren't clickable, so point to the bio. Nothing is posted without the person's approval.

## 11. Dead ends

A bar-by-bar story for Suno; a different instrument per section; Whisper on the full mix; plain alignment against lyrics Suno didn't sing; a dashboard of small parts; text-only character style prompts; a title card that gave the ending away; frantic console clicking.

## 12. Rebuild the hero reel

`video/allow-always-final/` uses `songs/allow-always/take-final-yes.mp3` and the committed, hand-corrected `video/data/allow-always-final.{json,js}`:

```bash
mkdir -p out/dev
ffmpeg -i songs/allow-always/take-final-yes.mp3 -ar 48000 out/dev/allow-always-final.wav
cd video/allow-always-final
npx --yes hyperframes@0.9.2 check
npx --yes hyperframes@0.9.2 render -o ../../out/allow-always-final.mp4    # ~4–7 min for 2:24 at 60 fps
```

Keep the committed timing. Don't rerun `cut_final.py` for this, because it overwrites the curated alignment. If the composition still loads GSAP from a CDN, the render needs network access.
