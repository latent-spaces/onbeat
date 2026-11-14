# music-reels

## Start here

**[GUIDE.md](GUIDE.md)** walks through the whole process end to end: concept, Suno song, timing, characters,
HyperFrames composition, review, render and posting, with the commands, prompts and mistakes from making
"allow always". The Suno prompts are in [`songs/allow-always/suno-prompts.md`](songs/allow-always/suno-prompts.md).

The avatar/sprite workflow and full-video integration now exist. For this kind of
illustrated music reel, start with the [production runbook](analysis/runbooks/animated-music-reels.md),
its [image prompt patterns](analysis/runbooks/image-prompts.md), and the append-only
[learning log](analysis/runbooks/learning-log.md). The full-video session is still
making changes; inspect its current files before extending it.

### Earlier planning notes (2026-11-11)

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

## Contents

- `analysis/playbook.md`: how the reference reels work and what we learned; the main document
- `analysis/runbooks/`: repeatable sprite-reel production workflow, provider-neutral image prompts and cross-session learning log
- `analysis/breakdown/<id>.md`: per-reel breakdowns of the ten studied reels
- `songs/<song>/`: lyrics, takes, storyboard and cut script per song
- `scripts/timing.py`: audio (and lyrics) → timing JSON (BPM, beats, bars, words, envelopes)
- `video/`: the HyperFrames project (`video/CLAUDE.md` has the commands)
  - `video/allow-always-final/`: the "allow always" reel (final take): permission-prompt hook and loop, avatar disco, console/explosion punch, 80s VHS look and karaoke captions; renders go to `video/out/`
  - `video/avatar-dance-test/`: the avatar dance test and its sprite sheets (dance, close-ups, `assets/action/` console and explosion); `video/assets/disco` links to its `assets/` and the reel needs it
- `THIRD_PARTY_NOTICES.md`: credit for the sprite-atlas approach adapted from page-mascot (MIT)
- `branding/`: robot profile portrait and its generation prompt
- `diagnostics/`: one-off measuring scripts (gitignored)

## Reference research

Research project: download reference Instagram reels (e.g. @alignment.check) with yt-dlp and analyze how they're produced.

- `reels.txt`: reel URLs (download with `yt-dlp -o "downloads/%(id)s.%(ext)s" --write-info-json -a reels.txt`)
- `downloads/`: videos, `*.info.json` metadata, frame sheets, raw comment export (gitignored)
- `analysis/alignment-check.md`: findings (pipeline, visual style, views, comment themes)
- `analysis/views.json`: view counts per reel, copied from the Reels grid
- `analysis/comments/<id>.json`: comments + replies for the top 10 reels, sorted by likes
- `scripts/build_review.py`: builds `review.html`, the top-N reels by views with good/maybe/skip marks (`python3 -I scripts/build_review.py 10`)
- `scripts/split_comments.py`: splits a browser comment export into `analysis/comments/`

Needs yt-dlp 2026.10.26 or newer; older versions fail on Instagram.
