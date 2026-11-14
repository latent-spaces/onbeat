# Plan: make the music-reels journey real

Editor: opus-strategist-1, 2026-11-14. Built on `RECOMMENDATIONS.md` and GUIDE.md on main (ba9359e), with team input from the project chat. Status words: **exists** = in the repo today; **to build** = not yet. Sizes: S < ½ day, M ½–2 days, L > 2 days.

## 1. User journey: Claude Code / Codex user

| # | Step | What they see | What they type or click | What can go wrong | Drop-off risk |
|---|---|---|---|---|---|
| 1 | See the reel | "allow always" on Instagram or X; the caption says "made with an AI agent, repo in comments / reply" | tap the link | no link, or the link sits in a bio they never open | **high**: needs the repo link in the first reply/comment |
| 2 | Land on the repo | README hero: the reel playing inline plus a poster, then one line: "Suno song in, beat-synced lyric reel out. Your agent does the edit." | scroll | the README opens with planning notes or text before the video (**to build**: README rewrite) | **high**: decided in about 5 s |
| 3 | Install | a single install block per agent | `npx skills add oronanschel/music-reels` (Claude Code) or the Codex plugin line | no skill exists yet (**to build**); Node is missing | medium |
| 4 | First render (≤ 5 min target, unmeasured) | the agent prompt "Render the sample reel", then an MP4 in `out/` | paste the prompt from the README | HyperFrames download is slow on first `npx`; Chrome/ffmpeg are missing. The prototype `video/avatar-dance-test` renders (verified once, cached tooling) | medium: needs a `doctor` check |
| 5 | Bring their own song | the README section "Make your own" | export a Suno M4A/MP3 plus lyrics into `songs/<name>/` | Suno free-plan download limits; rights to the song unclear | medium |
| 6 | Timing | the agent runs beat + word timing and shows the bars and words found | "make timing for songs/<name>" | `.venv-align` install (torch, WhisperX) is heavy. Suno doesn't sing the written lyrics, so the plain alignment drifts (GUIDE §5.2). `align_words.py` without `--lyrics` crashes | **high**: the hardest step |
| 7 | Look | the agent proposes one place and one hero object (playbook §10) and makes one still | approve or redirect | image-generator access; the sprite-sheet steps are complex (runbooks) | medium |
| 8 | Compose + review | snapshots at changed moments; a phone-size render | short notes ("lyrics late at 0:41") | renders take 4–7 min for 2:24; GSAP from the CDN fails offline | low (the loop is fun) |
| 9 | Render + post | a versioned MP4 plus a caption draft (from the `instagram-brief.md` formula) | upload themselves | the export is too big for the app; no credit line | low; each post advertises the repo |

## 1b. CLI-only user (no agent)

1. Same steps 1–2.
2. `git clone …` → `make doctor` (to build: checks Node, ffmpeg, Python, Chrome).
3. `make sample` (to build) → renders `video/avatar-dance-test` to `out/sample.mp4`. **Drop-off:** any missing dependency, which the doctor should name with the fix command.
4. Own song: `make timing SONG=<name>` → edit `songs/<name>/lines.txt` windows if words drift → `make export SONG=<name>` → `make render SONG=<name>`.
5. Without an agent, the look and composition mean editing HTML by hand, starting from a template (to build: song-agnostic template). **Biggest drop-off for CLI users**; say plainly in the README that the agent path is the easy one.

## 2. Build plan

| P | Item | Size | Touches |
|---|---|---|---|
| P0 | Tracked poster frame + 10 s preview of allow-always-final (cut on a lyric boundary), with a `.gitignore` exception for it | S | new `assets/readme/`, `.gitignore` |
| P0 | Owner decision on the reference-research files (`reels.txt`, `analysis/comments/`) before going public | S (owner) | `analysis/`, `reels.txt` |
| P0 | README rewrite: hero reel (poster + MP4 via GitHub attachment), one line, "Try it", GUIDE link, credits, experimental status; move the 2026-11-11 notes to `docs/history.md` | S | `README.md`, new `docs/history.md` |
| P0 | Root LICENSE (owner picks) + third-party credit for page-mascot ("Sprite-atlas tooling and reference workflow adapted from page-mascot by Kamran Ahmed (MIT)…") + sample media rights note | S | `LICENSE`, `README.md`, `GUIDE.md` |
| P0 | `make doctor` + `make sample` (renders the prototype, no keys) | S | new `Makefile`, `video/avatar-dance-test/package.json` |
| P0 | Final-reel audio fast path: ffmpeg MP3 → WAV, keeping the committed timing; never rerun `cut_final.py` to reproduce | S | new `scripts/prepare_audio.sh`, `songs/allow-always/cut_final.py` (guard against overwrite) |
| P0 | Vendor GSAP in the final composition | S | `video/allow-always-final/index.html`, `video/assets/` |
| P1 | Pinned `requirements.txt` / `requirements-align.txt` | S | new files, GUIDE §2 |
| P1 | Song-agnostic export: generalise `cut_final.py` + `align_final.py` (line windows from a file) | M | `scripts/`, `songs/allow-always/*.py` |
| P1 | Song-agnostic starter composition (beat clock + voice clock + karaoke). **This gates both "second song without editing HTML" and the skill** (sonnet-stars-2) | M–L | new `video/template/`, `video/src/beatsync.js` |
| P1 | Skill: `SKILL.md` (Claude Code) + Codex mirror wrapping doctor → timing → export → compose → render; plugin marketplace entry | M | new `skills/music-reel/`, `.claude-plugin/` |
| P1 | Sync-check overlay (beat grid + word boundaries) | S | `video/src/beatsync.js` |
| P2 | Gallery of 2–3 reels with full inputs; short promo cut only on clean musical boundaries | M | `songs/`, `video/`, README |
| P2 | Translated README (zh) | S | `README.zh-CN.md` |
| Later | Hosted "paste a Suno link" studio | L | — |

## 3. Launch plan (owner actions, in order)

1. Merge the P0 items. Run a fresh-clone test on a second machine and time `make sample`.
2. Choose the license and confirm rights: the Suno take (the plan's terms), the generated art, and the reference-research files (`reels.txt`, `analysis/comments/` stay out or are removed).
3. Add description and topics (`suno, lyric-video, music-video, beat-sync, hyperframes, claude-code, agent-skills, codex`), then make the repo public.
4. Post the reel on Instagram (per `songs/allow-always/instagram-brief.md`) and X. Reply with the repo as "how it was made", the PDoomVideo/page-mascot pattern of a same-day post with command + demo.
5. Same day: r/ClaudeCode / r/ClaudeAI / r/SunoAI posts with the reel inline (read each subreddit's self-promotion rules first). Optionally a Show HN on a US weekday morning, with GUIDE.md as the story and the demo command in the first comment.
6. Submit to "alternative to" directories (openalternative.co, alternativeto.net), awesome-claude-video-skills ("Music videos"), the HyperFrames showcase/Discord, and skills.sh.
7. Launch week: ship visible fixes daily (stalled repos plateau), answer issues, post the second reel. Aim for a Trending day.
8. After 48 h, check stars and traffic and decide on a second push. After 2 weeks: review stars, issues and drop-off questions; decide on P2.

## Contributions

Built from the research PRs #1–#6 (all six agents). sonnet-stars-2 contributed the CLI journey details, the template-gating point and the launch-sequence items (`research/sonnet-stars-2-plan` branch). Chat additions from codex-tooling-1/2 and opus-strategist-2 are folded in as they arrive.
