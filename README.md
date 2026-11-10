# music-reels

Research project: download reference Instagram reels (e.g. @alignment.check) with yt-dlp and analyze how they're produced.

- `reels.txt`: reel URLs (download with `yt-dlp -o "downloads/%(id)s.%(ext)s" --write-info-json -a reels.txt`)
- `downloads/`: videos, `*.info.json` metadata, frame sheets, raw comment export (gitignored)
- `analysis/alignment-check.md`: findings (pipeline, visual style, views, comment themes)
- `analysis/views.json`: view counts per reel, copied from the Reels grid
- `analysis/comments/<id>.json`: comments + replies for the top 10 reels, sorted by likes
- `scripts/build_review.py`: builds `review.html`, the top-N reels by views with good/maybe/skip marks (`python3 -I scripts/build_review.py 10`)
- `scripts/split_comments.py`: splits a browser comment export into `analysis/comments/`

Needs yt-dlp 2026.10.26 or newer; older versions fail on Instagram.
