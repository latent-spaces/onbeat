# Orbital dance test

An 11.52-second, 1080×1920 test using the chorus of **Allow Always** at
125.009 BPM, source seconds 27.2768–38.7959. The source timing comes from
`../data/allow-always-final.json`. The song cut is included as `assets/chorus.wav`.

## Assets

- `assets/portraits/`: five independent transparent 3×3 close-up PNG sheets:
  two humans and silver, ivory and plum robots. Each sheet contains one character.
- `assets/*-dance.webp`: three transparent 4×4 full-body dance sequences.
- `assets/ship.png`: opaque room foreground with a genuinely transparent window.
- `assets/planet.png`: separate transparent planet cutout.
- `assets/space.png`: separate opaque starfield behind the window.
- `assets/source/`: original generated character sheets, preserved for revision.
- `GENERATION-PROMPTS.json`: image generation prompts and tool provenance.

Assets were generated with the built-in image generation tool using the approved
cel-animation references. `prepare_assets.py` packs equal sprite cells, removes
disconnected alpha specks and aligns dance feet to a shared floor. Its dependencies
are Pillow, NumPy and SciPy, available in the repository's `.venv`.

This adapts the page-mascot sprite-atlas technique to song time: 16 full-body
poses per four-beat bar, with offset phases for the three dancers. Close-ups use
separate 3×3 angle/expression atlases. There are no cursor events or wall-clock
timers. The planet moves independently behind the room's transparent window.
The video deliberately uses limited sprite animation; this is a visual and timing
prototype, not skeletal motion capture or a finished character performance.

## Run

From this directory:

```bash
npm run check
npm run preview
npm run render
```

Preview: `http://localhost:3028/#project/avatar-dance-test`.
Output: `out/avatar-dance-test.mp4`.

To repack assets from the repository root:

```bash
.venv/bin/python video/avatar-dance-test/prepare_assets.py
```

The local GSAP script is included so rendering does not fetch runtime assets.
The existing video projects and song files are untouched.

## Karaoke version

`compositions/karaoke.html` adds uppercase cream italic lyrics, cyan offset
shadows, dark outlines and a pink wipe across each word. It adapts the registry's
`caption-clip-wipe` technique to the aligned song words, using the original song
offset. Captions sit above the dancers and close-up faces. The last repeated line
appears as a karaoke lead-in, with only the audible portion highlighted at the cut.

Rebuild the static caption markup with `build_karaoke.py` using the repository's
Python environment. Word timings are saved in `assets/karaoke-words.json`.
Run `npm run render:karaoke` to write `out/avatar-dance-karaoke.mp4`.
