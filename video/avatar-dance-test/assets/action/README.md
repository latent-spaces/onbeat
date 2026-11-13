# Control-panel and explosion sprites

Two independent RGBA PNG sheets, each 3 columns × 3 rows. Read frames 0–8 from
left to right, then top to bottom. Exact cell rectangles are in `sprites.json`.
Original generated pixels and alpha are preserved.

- `robot-controls-over-shoulder-3x3.png`: camera behind the silver robot's neck,
  with shoulder foreground and hand pressing a fixed console. Frames 0–2 press
  cyan; 3–5 move to and press mustard; 6 presses coral; 7 approaches launch;
  8 presses the large red launch button. The console is included and opaque;
  surrounding background is transparent. Use this as a close-up shot insert.
- `planet-explosion-3x3.png`: impact spark → growing fireball → peak fire/debris
  → smoke → fading embers. Play once, then hide the sprite; do not loop directly
  from the final smoke frame back to the spark. Place this layer over the planet
  behind the ship/window foreground. Frame 4 is the peak; frames 5–8 dissipate.

CSS sprite selection: `background-size: 300% 300%`; frame `i` uses
`background-position: (i % 3) * 50% floor(i / 3) * 50%`.
Suggested timing: console changes on eighth-note hits at 125 BPM (~0.24 s),
hold launch frame on the laser hit; explosion 9–12 fps (~0.75–1 s), then hide.
These are generated animation frames; minor drawing/registration variation
remains. Full generation prompts are in `PROMPTS.json`.

Assets only: the full-video composition was not modified in this task.

## Revised frantic console (preferred)

`robot-controls-over-shoulder-3x3-v2.png` has dense button banks, knobs and
toggles, two-handed frantic input, Earth/space on the CRT, and ghosted dancing
human reflections on the glass. Use this instead of the first control sheet.
Grid order remains row-major, 418×418 px per cell. Frames 0–5 mash different
controls; 6 reaches toward launch; **7 presses launch**; 8 recoils/continues
input with coral target brackets. The original sheet and explosion are preserved.
For frantic playback, try 10–12 fps; repeat frames 0–5 as needed, then play 6–8
once and time the laser to frame 7. Minor generated registration variation remains.
