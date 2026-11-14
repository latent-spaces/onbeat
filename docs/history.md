# Project history

> The files named below were removed from `main` at launch; they are on the [`archive` branch](https://github.com/oronanschel/music-reels/tree/archive).

Notes moved out of the README when the repo was packaged (2026-11-14). They describe how the project got here; the current way to use it is in the [README](../README.md) and the story of the first reel is in [GUIDE.md](GUIDE.md).

## Earlier planning notes (2026-11-11)

State on 2026-11-11: the first reel, "allow always", is paused. The story and storyboard exist, four Suno generations exist, and no video was built for the current story. The result so far is not good enough, for two reasons written up in `analysis/playbook.md`:

- **Section 9:** we wrote a long story and asked Suno to perform it bar by bar. It never followed the structure.
- **Section 10:** our frames are a dashboard of small parts, not a drawn place with one big object. Read "Rules for the next build".

**Next step: try the Suno-first approach** (playbook section 8).

1. Read playbook sections 8, 9 and 10.
2. Write short lyrics around one hook and generate a few Suno takes with spare length. Setup notes are in section 2. Ask before spending credits or downloads; about 4 free downloads were left.
3. Pick the best 30–45 s loop by ear, cut it to whole bars, and run `scripts/timing.py` on it.
4. Pick one place and one hero object, make a single still and a five-second test in `video/`, and compare it with a reference frame from `downloads/frames/`.
5. Only then write the storyboard to that loop and build the reel.

What can be reused from "allow always" (`songs/allow-always/`): the story chain and ending in `song.md`, the storyboard page (`storyboard.html`, draft 8), the real-prompt idea, and the agent characters. The takes are kept but none is good enough to build on.

## Repository contents before packaging

- `analysis/playbook.md`: how the reference reels work and what we learned; the main document
- `analysis/runbooks/`: repeatable sprite-reel production workflow, provider-neutral image prompts and cross-session learning log
- `analysis/breakdown/<id>.md`: per-reel breakdowns of the ten studied reels
- `songs/<song>/`: lyrics, takes, storyboard and cut script per song
- `scripts/timing.py`: audio (and lyrics) → timing JSON (BPM, beats, bars, words, envelopes)
- `video/`: the HyperFrames project (`video/CLAUDE.md` has the commands)
  - `video/allow-always-final/`: the "allow always" reel (final take): permission-prompt hook and loop, avatar disco, console/explosion punch, 80s VHS look and karaoke captions; renders go to `video/out/`
  - `video/avatar-dance-test/`: the avatar dance test and its sprite sheets (dance, close-ups, `assets/action/` console and explosion); `video/assets/disco` links to its `assets/` and the reel needs it
- `vendor/page-mascot/` (since removed): MIT avatar tooling and examples; the retained technique is in `analysis/avatar-pipeline.md`, with credit in `THIRD_PARTY_NOTICES.md`.
- `branding/`: robot profile portrait and its generation prompt
- `diagnostics/`: one-off measuring scripts (gitignored)

## Reference research

The early research downloaded reference Instagram reels to study how they were made. Those raw inputs are kept for the owner to decide on; see `analysis/playbook.md` for the aggregated findings.
