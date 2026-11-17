# Original cast spaceship dance

An 11.5192-second, 1080×1920, 30 fps chorus from "Allow Always": two original human dancers and an articulated mechanical robot in a retro cel-animated spaceship. The original dance sequence, cut times, karaoke and layered background are preserved; the character designs were replaced with the approved original cast.

```bash
npx --yes hyperframes@0.9.2 check
npx --yes hyperframes@0.9.2 render --output out/example.mp4
```

The approved rendered video is included as [`preview.mp4`](preview.mp4).

No keys, generation credits or accounts are required to render. An image model created the artwork; no video model is used. HyperFrames sequences the drawings and renders locally. New artwork may cost provider credits; timing and scene revisions reuse the same images.

## Assets and timing

- `assets/*-dance.webp`: three 4×4 full-body dance atlases, 16 drawings per character.
- `assets/*-closeups.webp`: three separately drawn 3×3 face-dancing atlases.
- `assets/ship.png`, `planet.png`, `space.png`: independent room, planet and starfield layers. The ship's window is genuinely transparent.
- `assets/source/`, `work/`, `cast-concept-v1.png`: generated source sheets, prompts and the approved cast study. Built-in image generation did not expose a model ID.
- `assets/sprites.json`: cell geometry, source/prompt provenance and validation.
- `data/timing.json`, `data/timing.js`: measured beats and existing reviewed sung-word times for this excerpt; word times were not newly force-aligned.

The chorus starts at source second 27.2768. The full recording was measured at 125.009 BPM. Body drawings change every quarter beat; close-ups change every half beat. No synthetic bounce or eased body motion was added. The original choreography and scene cuts live in `compositions/orbital.html`; `compositions/karaoke.html` preserves the word-highlight timing. The overlay is available with `?synccheck` or `window.REEL = {syncCheck:true}`.

Pose sheets were edited with the earlier drawings as movement references and the approved concept as the identity reference. Generated contours and proportions are not pixel-identical tracings. Dance packing applies one shared 0.88 scale to all cells, then anchors the feet at 94% of cell height; no pose is individually resized. These are held drawings, not continuous skeletal animation.

The bundled Arimo italic font (SIL Open Font License, included) and GSAP script are local. Arimo provides an Arial-compatible karaoke layout; the approved video preserves the reviewed lettering. Every runtime asset is included. The separate four-style showcase is available in the skill's `examples/four-styles/` directory.

The atlas approach is adapted from page-mascot (MIT); see the repository's third-party notices.
