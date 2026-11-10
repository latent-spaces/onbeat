"""Build review.html: the top reels by views, with playable video and good/skip marks.

Usage: python3 -I scripts/build_review.py [N]   (default N=10)
Reads downloads/*.info.json and analysis/views.json; writes review.html at the repo root.
"""
import glob
import html
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOP_N = int(sys.argv[1]) if len(sys.argv) > 1 else 10


def parse_views(s):
    s = s.replace(",", "")
    mult = {"K": 1_000, "M": 1_000_000}.get(s[-1], 1)
    return int(float(s.rstrip("KM")) * mult)


views = json.load(open(os.path.join(ROOT, "analysis/views.json")))
reels = []
for f in glob.glob(os.path.join(ROOT, "downloads/*.info.json")):
    d = json.load(open(f))
    if d["id"] not in views:
        continue
    desc = d.get("description") or ""
    reels.append({
        "id": d["id"],
        "date": f'{d["upload_date"][:4]}-{d["upload_date"][4:6]}-{d["upload_date"][6:]}',
        "views": parse_views(views[d["id"]]),
        "likes": d.get("like_count") or 0,
        "comments": d.get("comment_count") or 0,
        "title": desc.strip().split("\n")[0],
        "caption": desc.strip(),
    })

reels.sort(key=lambda r: r["views"], reverse=True)
reels = reels[:TOP_N]


def fmt(n):
    return f"{n / 1000:.1f}K" if n >= 10_000 else f"{n:,}"


cards = []
for i, r in enumerate(reels, 1):
    rate = r["likes"] / r["views"] * 100 if r["views"] else 0
    cards.append(f"""
<article class="card" data-id="{r['id']}" data-views="{r['views']}" data-likes="{r['likes']}" data-date="{r['date']}">
  <video src="downloads/{r['id']}.mp4" controls playsinline preload="metadata"></video>
  <div class="body">
    <div class="rank">#{i}</div>
    <h2>{html.escape(r['title'])}</h2>
    <div class="stats">
      <span><b>{fmt(r['views'])}</b> views</span>
      <span><b>{fmt(r['likes'])}</b> likes</span>
      <span><b>{r['comments']:,}</b> comments</span>
      <span><b>{rate:.1f}%</b> like rate</span>
    </div>
    <div class="meta">{r['date']} · <a href="https://www.instagram.com/reel/{r['id']}/" target="_blank" rel="noopener">open on Instagram</a></div>
    <details><summary>Caption</summary><p>{html.escape(r['caption']).replace(chr(10), '<br>')}</p></details>
    <div class="marks">
      <button data-mark="good">Good</button>
      <button data-mark="maybe">Maybe</button>
      <button data-mark="skip">Skip</button>
    </div>
    <textarea placeholder="Notes: what works here?"></textarea>
  </div>
</article>""")

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Top Reels Review</title>
<style>
:root {{
  --bg: #f6f5f2; --surface: #ffffff; --text: #1d1d1b; --muted: #6b6a66; --line: #e2e0da;
  --accent: #d9774b; --good: #2e8b57; --maybe: #c99a1e; --skip: #9a9a96;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg: #161614; --surface: #21211e; --text: #ecebe6; --muted: #9c9b95; --line: #34332f;
    --accent: #e8895c; --good: #4fb37b; --maybe: #e0b43a; --skip: #77766f;
  }}
}}
:root[data-theme="dark"] {{
  --bg: #161614; --surface: #21211e; --text: #ecebe6; --muted: #9c9b95; --line: #34332f;
  --accent: #e8895c; --good: #4fb37b; --maybe: #e0b43a; --skip: #77766f;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--text); font: 15px/1.45 -apple-system, BlinkMacSystemFont, "Inter", sans-serif; }}
header {{ position: sticky; top: 0; z-index: 2; background: var(--bg); border-bottom: 1px solid var(--line);
  padding: 14px 16px; display: flex; flex-wrap: wrap; gap: 10px 16px; align-items: center; }}
header h1 {{ font-size: 18px; margin: 0 auto 0 0; }}
header .tally {{ color: var(--muted); font-variant-numeric: tabular-nums; }}
select, header button {{ font: inherit; padding: 6px 10px; border-radius: 8px; border: 1px solid var(--line); background: var(--surface); color: var(--text); cursor: pointer; }}
main {{ max-width: 1200px; margin: 0 auto; padding: 16px; display: grid; gap: 16px; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); }}
.card {{ background: var(--surface); border: 1px solid var(--line); border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; border-top: 4px solid var(--line); }}
.card[data-mark="good"] {{ border-top-color: var(--good); }}
.card[data-mark="maybe"] {{ border-top-color: var(--maybe); }}
.card[data-mark="skip"] {{ border-top-color: var(--skip); opacity: .6; }}
video {{ width: 100%; aspect-ratio: 9 / 16; max-height: 560px; background: #000; display: block; object-fit: contain; }}
.body {{ padding: 12px 14px 14px; display: flex; flex-direction: column; gap: 8px; }}
.rank {{ color: var(--accent); font-weight: 700; font-size: 13px; }}
h2 {{ font-size: 16px; margin: 0; }}
.stats {{ display: flex; flex-wrap: wrap; gap: 4px 12px; font-size: 13px; color: var(--muted); font-variant-numeric: tabular-nums; }}
.stats b {{ color: var(--text); }}
.meta {{ font-size: 13px; color: var(--muted); }}
.meta a {{ color: var(--accent); }}
details {{ font-size: 13px; color: var(--muted); }}
details summary {{ cursor: pointer; }}
.marks {{ display: flex; gap: 6px; }}
.marks button {{ flex: 1; font: inherit; font-size: 14px; padding: 8px 0; border-radius: 8px; border: 1px solid var(--line); background: transparent; color: var(--text); cursor: pointer; }}
.card[data-mark="good"] [data-mark="good"] {{ background: var(--good); border-color: var(--good); color: #fff; }}
.card[data-mark="maybe"] [data-mark="maybe"] {{ background: var(--maybe); border-color: var(--maybe); color: #1d1d1b; }}
.card[data-mark="skip"] [data-mark="skip"] {{ background: var(--skip); border-color: var(--skip); color: #fff; }}
textarea {{ font: inherit; font-size: 13px; min-height: 52px; resize: vertical; padding: 8px; border-radius: 8px; border: 1px solid var(--line); background: var(--bg); color: var(--text); }}
.toast {{ position: fixed; bottom: 16px; left: 50%; transform: translateX(-50%); background: var(--text); color: var(--bg); padding: 8px 14px; border-radius: 8px; opacity: 0; transition: opacity .2s; pointer-events: none; }}
.toast.show {{ opacity: 1; }}
</style>
</head>
<body>
<header>
  <h1>@alignment.check: top {len(reels)} by views</h1>
  <span class="tally" id="tally"></span>
  <select id="sort">
    <option value="views">Sort: views</option>
    <option value="likes">Sort: likes</option>
    <option value="date">Sort: newest</option>
  </select>
  <select id="filter">
    <option value="all">Show: all</option>
    <option value="unmarked">Show: unmarked</option>
    <option value="good">Show: good</option>
  </select>
  <button id="copy">Copy marks</button>
</header>
<main id="grid">{''.join(cards)}
</main>
<div class="toast" id="toast"></div>
<script>
const KEY = "reel-marks-v1";
let state = {{}};
try {{ state = JSON.parse(localStorage.getItem(KEY) || "{{}}"); }} catch (e) {{}}
const save = () => {{ try {{ localStorage.setItem(KEY, JSON.stringify(state)); }} catch (e) {{}} }};
const cards = [...document.querySelectorAll(".card")];

function render() {{
  const counts = {{ good: 0, maybe: 0, skip: 0 }};
  cards.forEach(c => {{
    const s = state[c.dataset.id] || {{}};
    if (s.mark) {{ c.dataset.mark = s.mark; counts[s.mark]++; }} else delete c.dataset.mark;
    const ta = c.querySelector("textarea");
    if (document.activeElement !== ta) ta.value = s.note || "";
  }});
  document.getElementById("tally").textContent =
    `${{counts.good}} good · ${{counts.maybe}} maybe · ${{counts.skip}} skip · ${{cards.length - counts.good - counts.maybe - counts.skip}} left`;
  applyFilter();
}}

function applyFilter() {{
  const f = document.getElementById("filter").value;
  cards.forEach(c => {{
    const m = c.dataset.mark;
    c.style.display = f === "all" || (f === "unmarked" && !m) || f === m ? "" : "none";
  }});
}}

cards.forEach(c => {{
  const id = c.dataset.id;
  c.querySelectorAll("[data-mark]").forEach(b => b.addEventListener("click", () => {{
    state[id] = state[id] || {{}};
    state[id].mark = state[id].mark === b.dataset.mark ? undefined : b.dataset.mark;
    save(); render();
  }}));
  c.querySelector("textarea").addEventListener("input", e => {{
    state[id] = state[id] || {{}}; state[id].note = e.target.value; save(); render();
  }});
  c.querySelector("video").addEventListener("play", e => {{
    document.querySelectorAll("video").forEach(v => {{ if (v !== e.target) v.pause(); }});
  }});
}});

document.getElementById("sort").addEventListener("change", e => {{
  const k = e.target.value, grid = document.getElementById("grid");
  [...cards].sort((a, b) => k === "date" ? b.dataset.date.localeCompare(a.dataset.date) : b.dataset[k] - a.dataset[k])
    .forEach(c => grid.appendChild(c));
}});
document.getElementById("filter").addEventListener("change", applyFilter);

document.getElementById("copy").addEventListener("click", async () => {{
  const out = cards.map(c => ({{ id: c.dataset.id, title: c.querySelector("h2").textContent, ...(state[c.dataset.id] || {{}}) }}))
    .filter(r => r.mark || r.note);
  const text = JSON.stringify(out, null, 2);
  const t = document.getElementById("toast");
  try {{ await navigator.clipboard.writeText(text); t.textContent = "Marks copied. Paste them to Claude."; }}
  catch (e) {{ window.prompt("Copy your marks:", text); t.textContent = "Marks shown for copying."; }}
  t.classList.add("show"); setTimeout(() => t.classList.remove("show"), 2200);
}});

render();
</script>
</body>
</html>
"""

open(os.path.join(ROOT, "review.html"), "w").write(page)
print(f"wrote review.html with {len(reels)} reels")
for r in reels:
    print(f"  {r['views']:>8,} views  {r['likes']:>6,} likes  {r['id']}  {r['title'][:60]}")
