# Recommendations: making music-reels a strong public project

Merged result of the 2026-11-14 research run (Phase 1, research only). Editor: opus-strategist-1. Updated after main moved to 6daad3d (GUIDE.md, finished video, runbooks).
Sources: `research/2026-11-14/<agent>/` from all six agents (see "Inputs"). Reviewed by codex-tooling-1 and codex-tooling-2 for evidence overreach.
Star counts are live GitHub numbers from 2026-11-14. We have **one star-history sample (brag)**; for other repos the stargazer-timestamp API returned 404. Launch channels were checked only narrowly (two traces, see `codex-tooling-2/LAUNCH-EVIDENCE.md`). Star attribution stays unknown, and other "why it spread" claims are inferred from READMEs and marked as such in the per-agent notes.

## TL;DR

1. **The niche looks underserved and the engine is hot.** Three agents searched independently. The top "lyric video generator" repos in GitHub search have 14 stars (repo-name search) to about 150 (broader search), and lyric-video skills top out at 132. This comes from search samples, not a full census. HyperFrames, the engine we already use, reached 84k stars in 8 months, and the agent skills built on it get thousands (brag 21k in 5 months). In those samples, no popular repo does "Suno song → beat-synced, word-timed lyric reel".
2. **Ship it as a Claude Code / Codex skill + CLI, not a studio.** Studios (OpenMontage 80k, MoneyPrinterTurbo 143k, OpenCut 98k) are a crowded fight. Among the HyperFrames-based repos we sampled, the highest-starred recent ones (brag, herk-edit-kit, motionmaxxing) are skills with a one-line install. That's a correlation, not proof of cause.
3. **The README's first screen should be one excellent, playable reel made by the tool.** One great reel beats three mediocre ones. Test inline-video embedding in a private PR first. Ideally it's a reel about making reels with an agent, so the demo is proof and marketing at once (brag, herk-edit-kit).
4. **Zero-key try path (target, not measured).** The final Suno take is already tracked. Pair it with its committed timing JSON (or a rights-cleared short song) plus its timing JSON, aiming for clone → render in under 5 minutes with no Suno account or API keys. Only a timed clean-clone run can turn that into a claim. Most of the small lyric-video repos we looked at require API keys before the first run.
5. **Use our moat: the measured playbook.** We have numbers nobody else publishes (seam error < 40 ms on winners, claim on screen at 0.27 s, 118–129 BPM sweet spot, kick-drop timing). Herk-edit-kit and motionmaxxing show that "measured rules" sell. Add a **"sync check"** render (a beat-grid and word-boundary overlay) so viewers can inspect sync themselves (opus-strategist-2). A per-word *error* number would need labelled ground truth and a defined metric first (codex-tooling-1).
6. **Demand exists; tools don't.** The closest analog is JohnHeibel/PDoomVideo (2.9k stars, 2026-09): the source for one Claude-made music video about an AI-doom song. Its README presents it as the how-it-was-made source (why people starred it is inferred, not verified). It's a one-off source dump, not a reusable tool. Lyric-video skills (lyric-video-director 47, music-mv 132) have no hero output. Our "allow always" AI-agent song is in the same vein as P(doom) and alignment.check.

## How stars arrive (the one curve we have)

latent-spaces/brag, sampled stargazer timestamps (opus-strategist-2, `opus-strategist-2/star-history/`): created 06-16 → 500 stars in launch week (06-25) → a slow month to 1,000 (07-29) → **2,000 → 4,000 in two days (09-16 to 09-18)** → 21k now. What we observed: a slow phase, then a sharp acceleration. **What caused it is unknown.** The curve can't show whether it was a post, a video or a listing. The practical lesson still holds as a hedge: have the repo ready (hero reel, working sample, install) before any spike, because one may come without warning.

**Launch-channel traces found** (codex-tooling-2, `codex-tooling-2/LAUNCH-EVIDENCE.md`; exposure, not proof of causality). brag's initial commit already shipped its launch site and examples:
- `/brag` author post on r/ClaudeCode ([link](https://www.reddit.com/r/ClaudeCode/comments/1ubrc1y/i_built_a_claude_code_skill_called_brag_that/)): demo + repo + install line, a token-budget warning, and a request for feedback. Shown as "4mo ago", so the exact date isn't verified.
- Motion Canvas Hacker News discussion, 2023-02-22 ([link](https://news.ycombinator.com/item?id=34897707), about 180 points). A top reader reply asks for a GIF or visual, and others point to the author's YouTube explainer. This directly supports putting the demo first.

## Positioning

- **One line:** "Suno song in, beat-synced lyric reel out. Your coding agent does the edit."
- **Type:** agent skill (Claude Code + Codex) wrapping a deterministic CLI (`timing.py` → HyperFrames → render). Both paths are documented, as beat-synced-edit does with its "Pure CLI vs Claude Code skill" section.
- **Name as a verb / slash command**, e.g. `/reel` or `/lyric-reel`. The command is the brand (`/brag`).
- **Optional incumbent framing** (sonnet-stars-2): "open-source alternative to Kaiber / Neural Frames lyric-video makers", with a small comparison table (free, local, word-accurate, agent-driven). This pattern worked for OpenShorts (vs OpusClip) and OpenCut (vs CapCut).
- **Description and topics carry the search words:** `suno`, `lyric-video`, `music-video`, `beat-sync`, `reels`, `hyperframes`, `claude-code`, `agent-skills`, `claude-skills`, `codex`.

## README anatomy (in order)

1. Title, the one line, an honest "experimental" status, and **one vertical reel playing inline** (more later) (GitHub `user-attachments` MP4 or GIF linking to MP4), labelled "real output".
2. **Copy this prompt** block: "Make a 30-second reel for `song.mp3` with these lyrics", followed by the commands the agent will run (motion-pack pattern).
3. Install in one line per agent (`npx skills add …` / plugin marketplace), same as brag.
4. A 3-command CLI quickstart on the bundled sample song.
5. "How the timing works" diagram: beats, bars, words, seam.
6. "What makes a reel work": a short, numbers-first summary of `analysis/playbook.md`. Publish **our own measurements only**: no reference reels, mascot, lyrics or downloaded media from other creators.
7. Gallery, license, contributing.

A fuller draft is in `codex-tooling-2/README-OUTLINE.md`; the demo plan (show the beat clock and the word clock) is in `codex-tooling-2/DEMO-BRIEF.md`.

## Where the repo stands today (re-checked against main 6daad3d)

codex-tooling-1/2 audited 26d9337. The owner then pushed 5 commits (GUIDE.md, the finished "allow always" composition, sung-lyrics alignment, Suno prompt history, Instagram brief, runbooks). opus-strategist-1 and codex-tooling-1/2 re-checked against 6daad3d. codex-tooling-1 also ran `npm run check` and a render of the short prototype (below). The full 2:24 reel was not rendered by us.

**Now true:**
- **There is a finished reel.** `video/allow-always-final/index.html` is a 2:24 vertical composition of about 1,300 lines, built on the final Suno take. That take, `songs/allow-always/take-final-yes.mp3`, is tracked.
- **GUIDE.md documents the whole pipeline**, from concept to Suno, timing, characters, HyperFrames, review, render and posting, with pinned versions and pip lines for both venvs. It has a dead-ends section and a section on the human-agent feedback loop. **This is the strongest go-public asset in the repo**, the "how it was made" document that PDoomVideo and herk-edit-kit show people star.
- **Sung-word alignment is solved for this song**, using per-line windows (`songs/allow-always/align_final.py`), and GUIDE §5.2 documents the "Suno doesn't sing what you wrote" problem.
- **The JSON → `window.TIMING` export is documented** (GUIDE §5.3, `cut_final.py`). It is still a song-specific script, not a general adapter.
- **There's a production runbook** for sprites and avatars (`analysis/runbooks/`), plus a vendored, MIT-licensed `page-mascot` skill with upstream provenance in `UPSTREAM.json`.

**Still open:**
- **The finished video isn't in the repo.** It was rendered locally to `video/out/allow-always-final-80s-boom2.mp4` (67 MB, named in `instagram-brief.md`), but `*.mp4` is gitignored, so there's no tracked render, GIF or poster frame for a README hero.
- **The short prototype renders from committed inputs (verified on one machine).** `video/avatar-dance-test/` tracks its own 11.5 s `chorus.wav`, a local `gsap.min.js`, assets and `timing.json`. codex-tooling-1 ran it with the pinned CLI. `npm run check` passed with 0 errors and 2 density warnings, and the render produced H.264/AAC, 1080×1920, 30 fps, 346 frames, 11.53 s, 7.06 MB, in 14.4 s on an M4 with cached tooling. That timing is not a clean install, and nobody listened to the audio. **This is the current no-key demo.** Promote it now, rather than making a new sample song a prerequisite.
- **The fresh-clone render chain is undocumented as one sequence.** The final composition reads `assets/dev/allow-always-final.wav` through the gitignored `out/dev` symlink. **Fast path:** convert the tracked MP3 straight to a 48 kHz WAV with ffmpeg (`ffmpeg -i songs/allow-always/take-final-yes.mp3 -ar 48000 out/dev/allow-always-final.wav`) and keep the committed, hand-corrected `video/data/allow-always-final.{json,js}`. **Don't rerun `timing.py` → `cut_final.py` to reproduce it.** `cut_final.py` reads the gitignored `out/timing/` JSON and overwrites the committed timing, which would discard the curated sung-word alignment (codex-tooling-1, confirmed by opus-strategist-2). No script or doc wraps this path yet.
- **The GSAP CDN dependency.** The final composition loads GSAP from jsDelivr, which makes renders network-dependent. `avatar-dance-test` vendors `gsap.min.js` instead.
- **Dependencies are documented but not locked or automated.** GUIDE §2 lists tested versions, but its pip commands are unpinned, and there's no `requirements.txt`, `pyproject.toml` or lockfile.
- **No repo LICENSE**, no topics or description, and the repo is private. Only `vendor/page-mascot` carries a license.
- **No skill or CLI wrapper exists yet.** The recommendations below about the skill, `/reel` and a no-key sample are still targets.
- **README.md** now points to GUIDE.md first, but it still contains the "Earlier planning notes (2026-11-11)" section, which says "no video was built". That section is out of date and should move to a history doc.
- **Rights to check before going public** (owner decisions): redistributing the Suno take (it's already in the repo), the generated character sprites, and the reference-reel research files (`reels.txt`, `analysis/comments/`).

**Proposed go-public gates** (codex-tooling-1, still valid): P0 a clean-clone render of the bundled song with recorded commands; P0 a second song renders without song-specific edits; P0 a license plus provenance for the sample audio and art. P1 inspectable timing quality and one CLI with an optional skill. P2 a gallery of 2–3 reels.

**Revised order of work:** promote the existing full reel with a tracked poster frame (and a GIF or MP4 excerpt only if it can be cut on clean lyric and musical boundaries; the reel already loops and the brief warns against casual trims) → document or script the verified prototype render as the no-key quickstart → script the fast final-WAV path, which keeps the committed timing → vendor GSAP in the final build → pinned `requirements.txt` → generalise the per-song cut and align scripts → then the skill wrapper.

## Before going public: repo work (Phase 2 candidates)

- [x] ~~Finish one great reel~~: done, and so is the how-it-was-made guide (GUIDE.md). The job now is to promote both, not to build first. `allow-always-final` exists (2:24). Still needed: a tracked poster frame and preview for the README. A short promo cut is optional.
- [ ] Turn README.md into the public README above. It now links GUIDE.md first. Move the outdated "Earlier planning notes (2026-11-11)" into a history doc, and link GUIDE.md as the "How it was made" section.
- [ ] Add `sample/` with an own or CC0 short song, its lyrics and precomputed timing JSON.
- [ ] Package `SKILL.md` (+ Codex mirror) and a single CLI entry point.
- [ ] **Decide what to do with the reference research** (`reels.txt`, yt-dlp instructions, `analysis/comments/*.json` holding other people's comments, per-reel breakdowns of another account). Recommended: keep aggregated findings, drop or keep private the raw comment exports and download instructions. **Owner decision.**
- [ ] Make the repo public (owner decision), plus LICENSE, topics, release tag, issue templates; optional opt-in outro "made with music-reels" on rendered reels so every share advertises the repo.

## Launch plan (for the owner; we posted nothing)

All of these are outside actions that need the owner's approval:
- The reels themselves are the launch: post the reel first from the owner's account, then reply with the repo as "how it was made" (the PDoomVideo and brag pattern). Follow with the next 2–3 songs.
- A person and a channel bring the stars (Nate Herk's YouTube, a 71k-reader newsletter, an X account). The owner's own account is the channel: the repo is the follow-up to content that's already circulating.
- Also list on skills.sh and the HyperFrames showcase/Discord, and pitch the awesome list's "Music videos" section.
- Show HN / r/ClaudeAI / r/SunoAI / X thread with the reel embedded. A DEV.to write-up on how the word timing works (AutoMV launched this way).
- Submit to zhuyansen/awesome-claude-video-skills (2k stars, indexes HyperFrames skills) and ask the HyperFrames team about their showcase.
- Keep commits flowing during launch week. Stalled repos plateau (ShortGPT).
- **The owner's posting plan already exists:** `songs/allow-always/instagram-brief.md`. Suggested order: the reel first, then GUIDE.md as the second post ("how it was made", the PDoomVideo pattern) with the repo link (opus-strategist-2).
- **Aim for a GitHub Trending day.** MoneyPrinterTurbo hit #1 on Trending on 2024-03-28, about 17 days after creation (Trendshift data, low-authority source). List the repo in "alternative to" directories (OpenShorts is listed as an OpusClip alternative) (sonnet-stars-2).

## Open questions / not verified

- Star history: only brag was sampled (10 points). There are no curves for HyperFrames, OpenShorts or others, and launch channels were verified only for the two traces above.
- Whether Suno's terms allow redistributing a Suno-generated sample song in a public repo. Check before bundling one; otherwise use a CC0 song.
- Demand signal: an empty niche is also a sign of unproven demand (sonnet-stars-1). The reel's reach on social media is the real test.

## Inputs

| Agent | Slice | File |
|---|---|---|
| opus-strategist-1 | HyperFrames-ecosystem competitive set, README anatomy, consolidated top-29 list | `opus-strategist-1/notes.md`, `opus-strategist-1/top-similar-repos.md` |
| sonnet-stars-1 | AI music / lyric-video tools | `sonnet-stars-1/notes.md` (PR #1) |
| sonnet-stars-2 | Creator studios / short-form tools | `sonnet-stars-2/notes.md` (PR #2) |
| opus-strategist-2 | Claude Code skills, Remotion/HyperFrames templates, brag star history | `opus-strategist-2/notes.md` (PR #3) |
| codex-tooling-1 | Reproducibility / tooling readiness, go-public gates, review of this file | `codex-tooling-1/notes.md`, `audit.py`, `synthesis-review.md`, prototype check and render evidence (PR #5) |
| codex-tooling-2 | README / demo anatomy, proposed README outline and demo brief, baseline correction record | `codex-tooling-2/notes.md`, `README-OUTLINE.md`, `DEMO-BRIEF.md`, `LAUNCH-EVIDENCE.md`, `BASELINE-UPDATE.md`, `SYNTHESIS-CORRECTIONS.md` (PR #6) |
