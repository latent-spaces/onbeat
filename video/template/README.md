# Song-agnostic reel template

One HyperFrames reel that any song can drive. You never edit this HTML for a new song. `scripts/build_reel.py` copies the template into `out/projects/<song>/` and fills in the timing and config.

```bash
python3 scripts/build_reel.py --song songs/<name> --out out/projects/<name>   # make render runs this
cd out/projects/<name> && npx --yes hyperframes@0.9.2 check
npx --yes hyperframes@0.9.2 render --output ../../<name>.mp4 --fps 30 --workers 2
```

## Inputs (in `songs/<name>/`)

| File | Needed | What |
|---|---|---|
| `song.mp3` / `.m4a` / `.wav` | yes | the audio (converted to 48 kHz WAV in the project) |
| `timing.json` | yes | from `make timing`. Beats only is enough: `duration`, `beats`, `bars`, `beatPeriod`, `sections` |
| `reel.json` | no | the config below. Written with defaults on the first build |
| `lyrics.txt` | no | used for default `captions` when there are no aligned lines |
| `sprites/sprites.json` + sheets | no | the dancing cast (see `docs/sprites.md`) |

## `reel.json`

```json
{
  "title": "allow always",
  "subtitle": "a song about permission prompts",
  "palette": { "bg1": "#1b1033", "bg2": "#3a1450", "accent": "#ff4fa3", "ink": "#fff2c4", "sung": "#ffd34d" },
  "captions": ["may i read this file", "yes yes yes", "allow always"],
  "captionBars": 2,
  "captionStartBar": 6,
  "lyricsY": 260,
  "cast": [],
  "syncCheck": false
}
```

- **Lyrics, in order of preference:**
  1. word-by-word karaoke, when `timing.json` has `words` (`make timing WORDS=1`);
  2. whole lines on their start time, when it only has `lines`;
  3. otherwise `captions`, one per `captionBars` bars from `captionStartBar` (default: the first kick section). This is the **beats-only mode**.
- **Beat clock:** the sun pulses on every beat, harder on bar downbeats, and softly where the kick is out. The floor scrolls one tile per beat. A flash marks each drop (a no-kick → kick section change).
- **Cast:** `"cast": [{"sprite": "robot"}, {"sprite": "ochre", "x": 300, "y": 0, "size": 760}]`. Each `sprite` names an entry in `songs/<name>/sprites/sprites.json` (made with `docs/sprites.md`). Dancers start at the first kick section, step 16 poses per bar with phases 0/8/4/12, hop on every beat, and hop harder on downbeats (`SpriteDance`, see `docs/beat-motion.md`). `x`/`y` are relative to the stage under the sun.
- **Sync check:** `"syncCheck": true`, or `build_reel.py --sync-check`, draws beat ticks, bar labels and word marks under a playhead (`SyncCheck`). Turn it off for the final render.

All times come from `timing.json`, and every tween sits on one paused GSAP timeline, so a render is a pure function of time.
