---
name: onbeat
description: Turn a song into a beat-synced vertical lyric reel (1080x1920 MP4) with HyperFrames. Use when the user wants a reel, lyric video or music visual for a song (for example a Suno track), wants visuals timed to beats or sung words, wants dancing character sprites, or wants to check or fix sync. Works in Claude Code and Codex.
---

# onbeat

A song goes in and a beat-synced lyric reel comes out. You write the scene; the scripts here measure the song so that the scene lands on it.

Everything on screen follows one of two clocks, both measured from the audio:

- the **beat clock** (beats, bars, kick level) drives pulses, cuts and dance poses;
- the **voice clock** (the start and end of each sung word) drives the lyrics.

`$SKILL` below means this skill's folder, the one that holds this file.

| Folder | What it holds |
|---|---|
| `example/` | a complete 34.6-second animation showcase: original paper, pixel, clay and '80s anime, solo choreography, new 3×3 face-dancing portraits, layered scenery and timed lyrics. Renders as it is; copy it to start a reel. |
| `scripts/` | `timing.py` (beats, bars, sections, words) and `sprites.py` (checks character sheets) |
| `references/` | `hyperframes.md` (render rules), `beat-motion.md` (dance and sync check), `sprites.md` (characters) |

Work in a folder of the person's choosing, for example `reels/<name>/`. Never write inside `$SKILL` and never write into an unrelated project.

## 1. First, render the example

Do this before anything else in a new setup. It needs Node 22 or newer and ffmpeg, and no keys, accounts or Python.

```bash
mkdir -p reels && cp -R "$SKILL/example" reels/example && cd reels/example
npx --yes hyperframes@0.9.2 check
npx --yes hyperframes@0.9.2 render --output out/example.mp4
```

The first run downloads HyperFrames and a headless browser once. Tell the person where the MP4 is and ask them to watch it with the sound on.

## 2. Measure their song

Ask the person for an audio file. If they make it in Suno, they generate and download it themselves.

Create the reel by copying the example **before** generating timing data. Run these commands from the workspace folder, using a new name in place of `<name>`:

```bash
mkdir -p reels
test ! -e reels/<name> && cp -R "$SKILL/example" reels/<name>
```

If the destination already exists, stop and inspect it; reuse it only if it is this reel's project. Never copy the example into an existing destination or over generated timing data.

```bash
python3 -m venv reels/.venv && reels/.venv/bin/pip install -r "$SKILL/scripts/requirements.txt"   # once
reels/.venv/bin/python "$SKILL/scripts/timing.py" song.mp3 --beats-only -o reels/<name>/data/timing.json
```

This writes `timing.json` and, next to it, `timing.js`, which the page loads as `window.TIMING`:

| Field | Meaning |
|---|---|
| `bpm`, `beatPeriod`, `beatsPerBar` | one fixed tempo |
| `beats`, `bars` | the time of every beat and every bar's first beat, in seconds |
| `sections` | runs of bars with or without a kick drum: `{name, start, end, startBar, kick}` |
| `envelopes` | kick and full-band level, 60 values per second, from 0 to 1 |
| `words`, `lines` | each sung word and line with `start` and `end` (empty in beats-only mode) |
| `duration` | the song's length in seconds; all event times are seconds, independent of video frame rate |

- Analyse the whole song, not a short cut of it. On an 11-second clip the tempo came out 1% off.
- Read the BPM and bar count back to the person. If the BPM is half or double what they expect, say so.
- To make a reel from part of the song, add `--trim START_BAR N_BARS`. It cuts on bar lines and writes the cut audio next to the JSON.

**Sung words (optional).** Start with beats only. For karaoke, put the lyrics in a text file with one sung line per line, then:

```bash
python3.12 -m venv reels/.venv-align && reels/.venv-align/bin/pip install -r "$SKILL/scripts/requirements-align.txt"   # once, large
reels/.venv/bin/python "$SKILL/scripts/timing.py" song.mp3 --lyrics lyrics.txt -o reels/<name>/data/timing.json
```

This route is less tested than beats-only. Suno often doesn't sing the lyrics as written, and Whisper mishears vocoder voices, so check the word times with the sync check (step 4) and tell the person which lines you had to guess. The aligner reports and rejects timestamps outside the recording; interpolated words carry `estimated: true`. Never present those estimates as measured word onsets.

## 3. Agree the concept, prototype the look, then write the scene

Use the project created in step 2, keeping its generated `data/timing.json` and `data/timing.js`. Replace `assets/song.mp3` with the person's audio (or use the cut audio written by `--trim`). Read `references/hyperframes.md` before writing the scene.

### Creative checkpoints

For a new song, collaborate on the idea before building the full video. Reuse decisions the person has already made; if they explicitly ask you to proceed autonomously, state your assumptions and keep going.

1. **Concept and small story.** Read the lyrics and measured song structure. Offer two or three short, distinct ideas: who the hero is, where they are, what changes from the opening to the ending, and how the chorus or drop pays it off. Recommend one and let the person choose or combine them. A simple dance scene is a valid story; don't force a plot onto every song. When dancing avatars are requested or already established, keep them central unless the person chooses another direction.
2. **References.** Invite optional character photos, artwork, style references or context images. Clarify what each image should influence (see below). References are not required: offer a concrete direction if the person has none. Agree the character, setting and visual style before making production assets.
3. **Rough graphics.** Give the person graphics to react to: generate two or three clearly labelled visual directions for the agreed concept, each showing the main character, a representative setting and a dance pose. If references or a visual direction are already established, narrow the options to useful variations. Missing references should not stall exploration: use an explicitly original placeholder character and invite the person to supply images or describe changes. Use inexpensive drafts where appropriate. Ask which option they prefer and one or two focused follow-up questions about character appearance, style, mood or references; they may combine options. Keep the chosen image as the reference for later assets, incorporate their changes and show one or two key frames with phone-sized lyrics before producing a full sprite sheet or scene. Do not substitute a generic mascot for a requested character without discussing it.
4. **First motion draft.** Build a short beat-aligned passage that demonstrates the actual avatar dance, lyric treatment and one musical change. Let the person review the movement with sound. Iterate on this passage before extending it to the requested duration; don't present the full render as the first creative checkpoint.
5. **Full draft and revision.** Extend the agreed direction across the song excerpt, keeping approved characters and measured timing. Ask for focused feedback and revise the relevant parts. Number drafts and preserve earlier versions for comparison. Continue to the sync and render checks in step 4.

When the person asks to save session learnings into the skill, show the revised animation first and promote the learnings only after they approve the result. Treat numerical sync checks and the person's sound-on review as different evidence.

Concept or artwork approval does not authorize paid generation. Follow the generation and publishing rules below.

For the motion draft, a chorus passage of roughly 8–12 seconds often shows enough. State its interval in the original song. Keep the approved character images as direct references when generating assets, use a separate background plate, and bring friends into the scene on measured beats or bar downbeats. See `references/beat-motion.md` for keeping entrance movement separate from dancing.

Design:

- Make one place with one hero subject, not a dashboard of small parts. Pick a palette of three or four colours and one typeface.
- Choose solo, duet or ensemble shots to serve the brief. A style showcase can give each character its own world and sequence; it does not need a group-dance story. For public examples, create original identities and describe the medium, era, palette and linework instead of borrowing identifiable franchise characters.
- Let the song's shape drive the video. Use `sections` for the big changes: a new look, a cut or a drop when the kick comes in or goes out.
- For a layered scene, keep the background plate, dancers and transparent foreground props separate. Put foreground props in front of the cast and move the scenery layers by different small amounts over a musical phrase for a multiplane feel. Keep faces, feet and lyrics readable. The example's `src/showcase.js` demonstrates four solo styles and cuts on measured bar downbeats; `src/groove.js` sequences drawn accents without an added hop.
- Reuse pose sheets and scenery across scenes and revisions. Changing choreography, lyrics, cuts or layer positions needs a local render, not another generation call. This is the main cost advantage over repeatedly generating video clips; don't invent a fixed saving or imply that creating new artwork is free.
- Give every moving thing a clock. Decoration follows the beat clock, and lyrics follow the voice clock. Nothing moves on a time you made up.
- Keep text large and inside the middle 80% of the frame. The apps cover the top and bottom of a reel.

Timing:

- Every time in the scene comes from `TIMING`. Never type a number of seconds.
- Snap each time to a video frame with `BeatSync.at(t, fps)`.
- The root's `data-fps` is the only video frame-rate setting. The example assigns it to `T.fps` before calling the helpers; keep that line. Timing data has no video frame rate. Envelopes are sampled 60 times per second and carry their own `hop` in seconds, independent of `data-fps`.
- A hit is instant on the beat and then decays within the beat (`expo.out` over about 85% of `beatPeriod`). Don't ease into a beat, because that looks late.
- Make bar downbeats bigger than the other beats.
- Inspect which drawing carries the accent: the stamp, shoulder hit or strongest silhouette should land on the beat, with recovery drawings between. Starting a pose sequence on the beat is not enough if its visual hit arrives later. Quarter-beat body drawings and half-beat face drawings worked in the approved example; use them as a starting point, then review the actual movement with sound. See `references/beat-motion.md` for pose selection and optional bounce.

Helpers in `example/src/`, to use or to replace with your own code:

- `beatsync.js`: `BeatSync.at`, `el`, `BeatPulse`, `BeatStepper`, `KaraokeLine`, `DropLine`, `PaletteCut`, `holdTo`. Each is a few lines; read the file.
- `spritedance.js`: `SpriteDance.dance(...)` steps a character sheet through its poses once per bar and hops on each beat.
- `groove.js`: the example's authored pose order, with strong drawings on beats and no synthetic hop. Its cell indices are specific to the bundled sheets; inspect a new sheet before reusing them.
- `synccheck.js`: the overlay in step 4.

**Characters (optional).** A dancer is one 4×4 sheet of 16 poses. `references/sprites.md` covers how to generate and check one, and `references/beat-motion.md` covers how it dances. Generating images may cost the person credits, so ask before you do it.

**Face-dancing close-ups.** Make a separate 3×3 sheet of nine new head-and-shoulder drawings from the approved character reference: nods, tilts, eye changes, mouth expressions and shoulder accents. An enlarged body-sheet crop does not provide that acting. Hold a close-up for several measured beats and frame the shoulders through the bottom edge so the bust does not float above the scenery. See `references/sprites.md` for the portrait contract and `references/beat-motion.md` for its clock.

**Image-generation routes.** The two main routes are Higgsfield, or Codex's built-in image generator when working in Codex. Use the person's chosen provider; in Codex, prefer the built-in tool when no provider is specified. Both can make concept graphics and character assets. Check each provider's image-reference and transparency support before preparing production sheets. The Higgsfield sprite integration is still untested; see `references/sprites.md`. These routes do not override the paid-generation rules below.

**User-supplied images (optional).** The person can provide images for the image generator as direct visual references (for a character, subject, style or composition), or as context for the creative direction. Use their stated intent; if it is unclear, ask which role each image should play. Pass direct references to the generator using its supported image-reference inputs, and describe what to preserve or change. For context images, extract relevant mood, palette and story cues into the brief; do not assume the person wants their subjects reproduced. See `references/sprites.md` for sprite-specific guidance.

## 4. Check the sync, then render

```bash
cd reels/<name>
npx --yes hyperframes@0.9.2 check
npx --yes hyperframes@0.9.2 preview        # add ?synccheck to the preview URL
npx --yes hyperframes@0.9.2 render --output out/<name>.mp4
```

- The sync check draws beat ticks, bar numbers and word marks under a playhead. Look at it before a long render. To put it in a rendered video, add `<script>window.REEL = { syncCheck: true }</script>` before the scene script, and remove it for the final render.
- Look at frames from the MP4 itself (`ffmpeg -ss 5 -i out/<name>.mp4 -frames:v 1 frame.png`), not only at the preview.
- Change one thing per render, and tell the person which seconds changed.
- Don't overwrite an earlier render. Number them.

## Rules

- Don't run paid generation (Suno, Higgsfield or any other) without asking, and never operate the person's accounts or solve CAPTCHAs.
- Don't publish or post anything. The person does that.
- Every frame depends only on the timeline time. See `references/hyperframes.md` for what breaks that.
- Don't leave `console.log` in the scene.
- The sprite-sheet approach is adapted from [page-mascot](https://github.com/nilbuild/page-mascot) (MIT). Keep that credit if you publish the sprite tool.
