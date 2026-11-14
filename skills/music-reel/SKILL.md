---
name: music-reel
description: Turn a song into a beat-synced vertical lyric reel (1080x1920 MP4) with HyperFrames. Use when the user wants to render the music-reels sample, make a reel or lyric video for their own song (e.g. a Suno track), time visuals to beats or sung words, generate dancing character sprites, or check/fix sync. Works in Claude Code and Codex.
---

# music-reel

Song in, beat-synced lyric reel out. Everything on screen follows one of two clocks measured from the audio: the **beat clock** (beats, bars, kick) and the **voice clock** (sung words). The scripts are deterministic; you, the agent, direct them and make the creative calls with the person.

## 0. Find or get the repo

All commands run from the root of the `music-reels` repository (the folder with `Makefile`, `GUIDE.md`, `video/`).

- If the current folder is not that repo, ask the person where they want it and clone it:
  `git clone https://github.com/oronanschel/music-reels && cd music-reels`
- Never write into the person's unrelated project.

## 1. First success: the bundled sample (no keys, no accounts)

In a new checkout, do this first, before anything else. Don't generate assets or analyse a new song yet.

```bash
make doctor     # checks node >= 22, npx, ffmpeg; python is only needed later
make sample     # renders the bundled no-key sample -> out/sample.mp4
```

- The first `make sample` downloads `hyperframes@0.9.2` and a headless browser, which takes a few minutes once. Later renders take about 15-30 s.
- If `make doctor` prints `missing`, run the fix it prints and run it again. Do not continue with a red item.
- Tell the person where the file is (`out/sample.mp4`) and ask them to watch it with sound.

## 2. Their own song

Ask the person for an audio file. If they make it in Suno, **they** generate and download it; never operate their Suno account, credits or CAPTCHAs. You may draft lyrics and a Styles line (see `songs/allow-always/suno-prompts.md` for a proven one: four-on-the-floor, 118-129 BPM, a cappella vocoder intro, then a full-band drop).

Lay the song out like this:

```
songs/<name>/song.mp3      # or .m4a / .wav
songs/<name>/lyrics.txt    # optional, one sung line per line
songs/<name>/reel.json     # template config (title, palette, captions, cast); see video/template/README.md
```

### 2a. Timing

```bash
make setup                       # once: .venv with pinned requirements.txt
make timing SONG=<name>          # beats only (easy start): BPM, beats, bars, sections, kick envelope
make timing SONG=<name> WORDS=1  # also sung-word times (needs .venv-align, GUIDE.md section 2)
```

Output: `songs/<name>/timing.json`. Read back the BPM and bar count to the person.

Start with **beats-only**. The template then shows lyrics per line or per bar instead of word-by-word karaoke. Add word alignment only if the person wants karaoke. Watch for these known problems (GUIDE.md section 5.2): Suno doesn't sing the lyrics as written, and Whisper mishears vocoder words. Align each line inside its own time window and mark guesses as guesses.

### 2b. Look

Make one place and one hero object (`docs/research/playbook.md` section 10), not a dashboard of small parts. Start from the template's default look. Change the palette, title and captions in `reel.json` before you touch any HTML.

Characters are optional. To add dancing sprites, follow `docs/sprites.md`:
- **Codex built-in image generation** is the tested route.
- **Higgsfield** is untested. The adapter prints the commands, and the owner must run any paid generation themselves.

Both routes write sheets plus `sprites.json` (frame rects), so the animation code is the same for either provider. Put them in `songs/<name>/sprites/` and list the dancers in `reel.json` (`"cast": [{"sprite": "robot"}]`). Cast members dance automatically through `SpriteDance`: 16 poses per bar, a hop on every beat, a bigger hop on downbeats and a phase offset per character (`docs/beat-motion.md`).

### 2c. Render and review

```bash
make render SONG=<name>          # -> out/<name>.mp4
```

- **Sync check before a long render:** set `"syncCheck": true` in `reel.json`, or build with `python3 scripts/build_reel.py --song songs/<name> --out out/projects/<name> --sync-check`, or open the preview with `?synccheck`. It draws beat ticks, bar labels and word marks under a playhead. Turn it off for the final render.
- Change one thing per render, and tell the person exactly which seconds changed.
- `make render` writes `out/<name>.mp4`. Copy a render you want to keep to a versioned name before you render again.
- Inspect the encoded MP4 itself, not only the preview.

## 3. Rules

- HyperFrames rule: every visual is a pure function of timeline time. No `Date.now()`, no timers, and no randomness unless it's seeded.
- All times come from `timing.json`. Never hard-code seconds.
- Don't add `console.log` to committed code.
- Don't run paid generation (Suno, Higgsfield) yourself, and don't publish or post anything. The person does that.
- Credit page-mascot (MIT) for the sprite-atlas approach. See the README credits.

## 4. Where to read more

- `docs/TRY-IT.md`: the step-by-step first run, with the expected output at each step.
- `GUIDE.md`: how "allow always" was made, including prompts, dead ends and the feedback loop.
- `docs/runbooks/animated-music-reels.md`: sprite and avatar production details.
