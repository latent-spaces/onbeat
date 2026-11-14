# Recommendations: making music-reels a strong public project

Merged result of the 2026-11-14 research run (Phase 1, research only). Editor: opus-strategist-1.
Sources: `research/2026-11-14/<agent>/` from all six agents (see "Inputs"). Reviewed by codex-tooling-1 and codex-tooling-2 for evidence overreach.
Star counts are live GitHub numbers from 2026-11-14. We have **one star-history sample (brag)**; for other repos the stargazer-timestamp API returned 404. Launch channels were not checked against HN, X or Reddit, so "why it spread" claims are inferred from READMEs and marked as such in the per-agent notes.

## TL;DR

1. **The niche looks underserved and the engine is hot.** Three agents searched independently. The top "lyric video generator" repos in GitHub search have 14 stars (repo-name search) to about 150 (broader search), and lyric-video skills top out at 132. This comes from search samples, not a full census. HyperFrames, the engine we already use, reached 84k stars in 8 months, and the agent skills built on it get thousands (brag 21k in 5 months). In those samples, no popular repo does "Suno song → beat-synced, word-timed lyric reel".
2. **Ship it as a Claude Code / Codex skill + CLI, not a studio.** Studios (OpenMontage 80k, MoneyPrinterTurbo 143k, OpenCut 98k) are a crowded fight. Among the HyperFrames-based repos we sampled, the highest-starred recent ones (brag, herk-edit-kit, motionmaxxing) are skills with a one-line install. That's a correlation, not proof of cause.
3. **The README's first screen should be one excellent, playable reel made by the tool.** One great reel beats three mediocre ones. Test inline-video embedding in a private PR first. Ideally it's a reel about making reels with an agent, so the demo is proof and marketing at once (brag, herk-edit-kit).
4. **Zero-key try path (target, not measured).** Bundle our own rights-cleared short song plus its timing JSON, aiming for clone → render in under 5 minutes with no Suno account or API keys. Only a timed clean-clone run can turn that into a claim. Most of the small lyric-video repos we looked at require API keys before the first run.
5. **Use our moat: the measured playbook.** We have numbers nobody else publishes (seam error < 40 ms on winners, claim on screen at 0.27 s, 118–129 BPM sweet spot, kick-drop timing). Herk-edit-kit and motionmaxxing show that "measured rules" sell. Add a **"sync check"** render (a beat-grid and word-boundary overlay) so viewers can inspect sync themselves (opus-strategist-2). A per-word *error* number would need labelled ground truth and a defined metric first (codex-tooling-1).
6. **Demand exists; tools don't.** The closest analog is JohnHeibel/PDoomVideo (2.9k stars, 2026-09): the source for one Claude-made music video about an AI-doom song. Its README presents it as the how-it-was-made source (why people starred it is inferred, not verified). It's a one-off source dump, not a reusable tool. Lyric-video skills (lyric-video-director 47, music-mv 132) have no hero output. Our "allow always" AI-agent song is in the same vein as P(doom) and alignment.check.

## How stars arrive (the one curve we have)

latent-spaces/brag, sampled stargazer timestamps (opus-strategist-2, `opus-strategist-2/star-history/`): created 06-16 → 500 stars in launch week (06-25) → a slow month to 1,000 (07-29) → **2,000 → 4,000 in two days (09-16 to 09-18)** → 21k now. What we observed: a slow phase, then a sharp acceleration. **What caused it is unknown.** The curve can't show whether it was a post, a video or a listing. The practical lesson still holds as a hedge: have the repo ready (hero reel, working sample, install) before any spike, because one may come without warning.

**Launch-channel traces found (codex-tooling-2; exposure, not proof of causality):**
- `/brag` author post on r/ClaudeCode ([link](https://www.reddit.com/r/ClaudeCode/comments/1ubrc1y/i_built_a_claude_code_skill_called_brag_that/)): demo + repo + install line, a token-budget warning, and a request for feedback. Shown as "4mo ago", so the exact date isn't verified.
- Motion Canvas Show HN, 2023-02-22 ([link](https://news.ycombinator.com/item?id=34897707), about 180 points). A top reader reply asks for a GIF or visual, and others point to the author's YouTube explainer. This directly supports putting the demo first.

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

## Where the repo stands today (codex-tooling-1/2 audit)

None of the skill / CLI / one-command features recommended here exist yet. They are targets.
- **A complete sample render (audio + video) isn't reproducible from a fresh clone** (static audit, renderer not run). All three compositions read audio from `video/assets/dev`, a tracked symlink to `../../out/dev`, which is gitignored and missing in a clone. The stub generator writes timing data but no audio.
- **Dependencies are implicit.** The Python scripts need librosa/numpy/scipy with no manifest, plus a separately hardcoded `.venv-align` (Demucs, torch, faster-whisper, WhisperX).
- **The data contract has a gap.** `timing.py` emits JSON, but the HTML compositions read `window.TIMING` JS. Only the song-specific `cut.py` and the stub generator bridge the two, and there's no general JSON → composition adapter.
- **Public metadata is empty.** The repo is private, with no description, homepage, license or topics, and no tracked demo image or video. The README is a "next session" handoff that says no video was built for the current story. There's no GUIDE.md.
- **Proposed go-public gates** (codex-tooling-1): P0 a clean-clone sample render with recorded commands; P0 a second, user-supplied song renders without editing song-specific code; P0 clear license plus sample/audio provenance. P1 inspectable timing quality and one CLI with an optional skill. P2 a gallery of 2–3 examples. Studio/UI comes later.
- **Order of work this implies:** a rights-cleared, no-key sample → a general timing-JSON → composition adapter → a preflight/doctor check (deps, audio present) → then the CLI and skill wrapper → then the README. The README should state an "experimental" status honestly until the skill really exists.

## Before going public: repo work (Phase 2 candidates)

- [ ] Finish **one** great reel with the Suno-first approach (README "Next step"); without it there is nothing to show.
- [ ] Rewrite README.md from a session handoff into the public README above. Move the "Start here (next session)" notes into `docs/` or `CLAUDE.md`.
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

## Open questions / not verified

- Star history: only brag was sampled (10 points). There are no curves for HyperFrames, OpenShorts or others, and no launch channel was verified for any repo.
- Whether Suno's terms allow redistributing a Suno-generated sample song in a public repo. Check before bundling one; otherwise use a CC0 song.
- Demand signal: an empty niche is also a sign of unproven demand (sonnet-stars-1). The reel's reach on social media is the real test.

## Inputs

| Agent | Slice | File |
|---|---|---|
| opus-strategist-1 | HyperFrames-ecosystem competitive set, README anatomy | `opus-strategist-1/notes.md` |
| sonnet-stars-1 | AI music / lyric-video tools | `sonnet-stars-1/notes.md` (PR #1) |
| sonnet-stars-2 | Creator studios / short-form tools | `sonnet-stars-2/notes.md` (PR #2) |
| opus-strategist-2 | Claude Code skills, Remotion/HyperFrames templates, brag star history | `opus-strategist-2/notes.md` (PR #3) |
| codex-tooling-1 | Reproducibility / tooling readiness, go-public gates, review of this file | `codex-tooling-1/notes.md`, `audit.py`, `synthesis-review.md` (PR #5) |
| codex-tooling-2 | README / demo anatomy, proposed README outline and demo brief | `codex-tooling-2/notes.md`, `README-OUTLINE.md`, `DEMO-BRIEF.md` (PR #6) |
