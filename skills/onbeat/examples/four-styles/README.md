# Four styles in motion

A 34.5575-second, 1080×1920 animation showcase using the existing "Allow Always" recording, source 27.2768–61.8343 seconds. Paper-cut moth, pixel beet, handmade clay pebble and original '80s anime dancer each get a solo sequence. There is no ensemble routine.

```bash
npx --yes hyperframes@0.9.2 check
npx --yes hyperframes@0.9.2 render --output out/four-styles-v2.mp4
```

No keys or image-generation accounts are needed to render. Artwork was created with Codex's built-in image generator; it did not expose a model ID. Original source images and prompts are in `artwork/`. Render assets are local WebP files in `assets/`.

## Direction and timing

The full 144.4-second recording was analyzed again: 125.009 BPM, attack timing median scatter 8.2 ms. This replaces the previous 123.78 BPM estimate measured from the short excerpt. The excerpt contains 18 bars / 72 beats. Low-band checks over the later strong drum passages favored this beat phase over the half-beat alternative. The early sparse passage is less conclusive. These are numerical checks, not a guarantee of perfect perceptual sync.

Existing reviewed word times were reused and clipped to the new excerpt. They were not newly force-aligned. All event times remain in seconds; `data-fps` is the frame-rate authority.

Paper (bars 0–4), pixel (4–8) and clay (8–12) alternate one-bar full-body and face sequences. The full-body return uses a medium framing. Anime gets the final six bars: face introduction, full-body setup, a longer grounded funk phrase and a two-bar face-dancing finish. Cuts come from measured bars; word highlighting uses the existing voice clock.

`src/groove.js` sequences body drawings directly on quarter beats; face drawings change on half beats. Strong body silhouettes land on beats; recovery drawings fill the subdivisions. Added synthetic hopping, torso rotation and easing were removed so they cannot delay or obscure the drawn accents. The reusable `spritedance.js` hop remains available for other reels.

Every close-up uses a separate 3×3 portrait atlas: nine NEW head-and-shoulder drawings, not an enlarged body crop. Each portrait drawing holds for a half beat, using two expression sequences across repeated shots. Portrait shoulders extend through the frame's bottom edge. Background and transparent foreground scenery move independently over musical phrases, rather than jittering each quarter beat.

The single paused timeline and shared stage are deliberate: only one character or portrait is visible at a time. Open the preview with `?synccheck` for beat/word marks. `SPEC.md` records the accepted direction.

## Artwork and reuse

`assets/cast/sprites.json` records geometry, provider, source, prompt and validation for each sheet. Dance atlases use 4×4 grids; portrait atlases use 3×3 grids. Ingestion uses fixed cell sizes, not per-pose bounding-box resizing. A final alpha cleanup zeroes values under 20 on newly prepared atlases to remove faint cutout haze; source images are unchanged.

The example makes no image/video-generation calls. Timing, pose order, camera framing, lyrics and scenery positions can be revised and rendered locally using the existing files. New artwork may cost provider credits; rendering uses your own compute. No fixed saving against generated video has been benchmarked.

The sprite-atlas approach is adapted from page-mascot (MIT), credited in the repository's third-party notices. No upstream character images are bundled.
