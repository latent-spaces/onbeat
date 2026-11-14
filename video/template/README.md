# One template, any song

The bundled sample and your own song use the same composition. Edit a small config; keep the HTML unchanged.

```bash
python3 scripts/build_reel.py --song video/sample --out out/projects/sample
cd out/projects/sample
npx --yes hyperframes@0.9.2 check
```

For your own song, put `song.mp3` (or `.m4a` / `.wav`) and `timing.json` in `songs/<name>/`, then use that folder with `--song`. `make render SONG=<name>` wraps the builder and renderer. Beats-only timing is enough.

Optional `reel.json`:

```json
{
  "title": "YOUR SONG",
  "subtitle": "A line about the track.",
  "palette": {"bg1": "#f6f0df", "bg2": "#f6f0df", "accent": "#ed553b", "ink": "#182e33"},
  "captions": ["One phrase", "Then the next"],
  "captionBars": 2,
  "cast": [{"name": "robot-dance", "phase": 0}],
  "syncCheck": false
}
```

Keep titles short (roughly 2–4 words) and captions under five words per line. Text stays above the social UI. Aligned words use karaoke; timed lines use line reveals; otherwise optional captions change on bars. Unaligned captions are a design choice, not a claim of lyric alignment. Omit captions for a beat-only reel.

The default robot uses local project artwork. Set `cast: []` for type only, or use up to three cast members from your song's `sprites/sprites.json` (see [sprites](../../docs/sprites.md)). Assets are copied from that manifest, independent of the image provider. Each member can set `phase` and `perBeat`; [SpriteDance](../../docs/beat-motion.md) supplies stepping, kick bounce, bar accents and silence holds.

Add `--sync-check` to the builder for beat ticks and word marks; disable it for the final export. Every visible state comes from one paused timeline. No generation or model download occurs during the build.

Output must be a new/empty directory or a previously generated project. Inside this repo it must live under `out/`. Input folders and unrelated non-empty output directories are refused. Existing unrelated files in a marked project are retained.
