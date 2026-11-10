"""Split a browser-exported comments dump into analysis/comments/<shortcode>.json.

Usage: python3 -I scripts/split_comments.py path/to/alignment-check-comments.json
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "analysis", "comments")
os.makedirs(OUT, exist_ok=True)

dump = json.load(open(sys.argv[1]))
for sc, reel in dump["reels"].items():
    info_path = os.path.join(ROOT, "downloads", f"{sc}.info.json")
    title = ""
    if os.path.exists(info_path):
        title = (json.load(open(info_path)).get("description") or "").strip().split("\n")[0]
    comments = sorted(reel["comments"], key=lambda c: c["likes"], reverse=True)
    saved = len(comments) + sum(len(c["replies"]) for c in comments)
    out = {
        "shortcode": sc,
        "url": f"https://www.instagram.com/reel/{sc}/",
        "title": title,
        "captured_at": dump["captured_at"],
        "comment_count_on_instagram": reel["comment_count"],
        "comments_saved": saved,
        "comments": comments,
    }
    with open(os.path.join(OUT, f"{sc}.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"{sc}  {saved:>4}/{reel['comment_count']:<4} {title[:55]}")
