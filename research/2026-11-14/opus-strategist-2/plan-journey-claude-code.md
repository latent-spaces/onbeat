# PLAN.md input: the Claude Code / Codex user journey (opus-strategist-2)

For opus-strategist-1 (PLAN.md editor) to paste or trim. The commands marked *(to build)* don't exist yet. Each references a build item below.

| # | Step | What they see | What they type/click | What can go wrong | Drop-off risk |
|---|---|---|---|---|---|
| 1 | See the reel | "allow always" on IG/X; end card or caption "made with Claude Code + link" | Tap the link in the bio or pinned comment | No link (IG captions aren't clickable) | High: no link means nobody arrives |
| 2 | Land on the repo | README hero GIF (hook at 0:01 + disco at about 1:05), a one-line pitch, an install line | Copy the install line | No media above the fold; repo still private; no LICENSE | High |
| 3 | Install (min 0–2) | Skill installed; doctor output with green checks | `npx skills add oronanschel/music-reels`, then `/music-reel doctor` *(to build)* | No ffmpeg, node < 22, Chrome download for HyperFrames | Medium: doctor must print the exact fix line |
| 4 | First render (min 2–5) | `out/sample.mp4`, a 12 s cut of the reel, plus a snapshot PNG | `/music-reel sample` *(to build)*: ffmpeg MP3→48 kHz WAV (not `cut_final.py`, which overwrites the curated timing), then `npx hyperframes@0.9.2 render` | Missing `out/dev` link, slow first render, CDN GSAP fetch | **Highest**: over 5 min or any red error loses them |
| 5 | Make a song | The Suno web app | The user writes a hook, generates takes, picks one by ear (GUIDE §4). Agents only draft the lyrics and Styles line, and never touch CAPTCHA or credits | Suno ignores the structure or sings other words | Medium: needs a Suno account |
| 6 | Timing | A line table of sung words with times to confirm | Drop the mp3 + lyrics.txt into `songs/<name>/`, then `/music-reel time songs/<name>` *(to build)*: `scripts/timing.py`, then optional alignment | The whisperx/demucs install (~2 GB, separate Python 3.12 venv); misheard vocoder words | High at alignment, so offer beats-only mode first |
| 7 | Look | 3–4 named presets with a still each (desk world, disco, minimal type) | Pick one by number (GUIDE §6.2) | A blank-page "design it" prompt; sprites need an image model | Medium |
| 8 | Compose and render | Preview, then snapshots of changed moments, then a versioned MP4 and a phone copy | `/music-reel render` *(to build)* wraps `hyperframes check / snapshot / render` (GUIDE §8) | 4–7 min renders for 2:24 at 60 fps; overwritten renders | Low: they're invested by now |
| 9 | Post | A caption draft (instagram-brief.md formula) plus the "made with" credit | The user posts it themselves | Cropped cover; loop broken by trimming | Low. Each post markets the repo |

**Build items this journey needs** (files touched):
- P0, S: `scripts/doctor` + `make sample` (new; uses `songs/allow-always/take-final-yes.mp3` and `video/data/allow-always-final.json`)
- P0, S: README hero GIF/MP4 + poster + LICENSE (`README.md`, new `docs/media/`)
- P0, M: song-agnostic export, generalising `songs/allow-always/cut_final.py` and `align_final.py` into `scripts/export.py`
- P1, M: `skills/music-reel/SKILL.md` wrapping doctor / sample / time / render (new)
- P1, S: beats-only mode with no whisperx (`scripts/timing.py` flag; the composition hides karaoke)
- P1, S: `requirements.txt` + `requirements-align.txt` (from the GUIDE §2 pip lines)
- P2, L: 3–4 style presets as compositions (split `video/allow-always-final/index.html` into templates)
