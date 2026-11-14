# Recommendations: making music-reels a strong public project

Merged result of the 2026-11-14 research run (Phase 1, research only). Editor: opus-strategist-1.
Sources: `research/2026-11-14/<agent>/notes.md` from opus-strategist-1, sonnet-stars-1, sonnet-stars-2 (and others as listed under "Inputs" below).
Star counts are live GitHub numbers from 2026-11-14. We have **one star-history sample (brag)**; for other repos the stargazer-timestamp API returned 404. Launch channels were not checked against HN, X or Reddit, so "why it spread" claims are inferred from READMEs and marked as such in the per-agent notes.

## TL;DR

1. **The niche is empty and the engine is hot.** Three agents searched independently: the top "lyric video generator" repo on GitHub has 14–150 stars. HyperFrames, the engine we already use, reached 84k stars in 8 months, and the agent skills built on it get thousands (brag 21k in 5 months). Nobody owns "Suno song → beat-synced, word-timed lyric reel".
2. **Ship it as a Claude Code / Codex skill + CLI, not a studio.** Studios (OpenMontage 80k, MoneyPrinterTurbo 143k, OpenCut 98k) are a crowded fight. A one-command skill is how the fastest risers in our ecosystem won.
3. **The README's first screen must be a playable reel made by the tool.** Ideally it's a reel about making reels with an agent, so the demo is proof and marketing at once (brag, herk-edit-kit).
4. **Zero-key try path.** Bundle our own short song plus its timing JSON, so clone → render works in under 5 minutes with no Suno account or API keys. Every small competitor demands keys first.
5. **Use our moat: the measured playbook.** We have numbers nobody else publishes (seam error < 40 ms on winners, claim on screen at 0.27 s, 118–129 BPM sweet spot, kick-drop timing). Herk-edit-kit and motionmaxxing show that "measured rules" sell. Add a **"sync check"** render (beat-grid overlay, per-word timing error) so we can make claims like motionmaxxing's "12 measured eases" (opus-strategist-2).
6. **Demand exists; tools don't.** The closest analog is JohnHeibel/PDoomVideo (2.9k stars, 2026-09): the source for one Claude-made music video about an AI-doom song. People starred it to see how it was made, yet it's a one-off source dump, not a reusable tool. Lyric-video skills (lyric-video-director 47, music-mv 132) have no hero output. Our "allow always" AI-agent song is in the same vein as P(doom) and alignment.check.

## How stars arrive (the one curve we have)

latent-spaces/brag, sampled stargazer timestamps (opus-strategist-2, `opus-strategist-2/star-history/`): created 06-16 → 500 stars in launch week (06-25) → a slow month to 1,000 (07-29) → **2,000 → 4,000 in two days (09-16 to 09-18)** → 21k now. A quiet launch, word of mouth, then one widely shared moment multiplied it. The lesson: the repo has to be ready (hero reel, one-line install, sample) *before* the moment, because the moment comes from content (a reel or post), not from the repo.

## Positioning

- **One line:** "Suno song in, beat-synced lyric reel out. Your coding agent does the edit."
- **Type:** agent skill (Claude Code + Codex) wrapping a deterministic CLI (`timing.py` → HyperFrames → render). Both paths are documented, as beat-synced-edit does with its "Pure CLI vs Claude Code skill" section.
- **Name as a verb / slash command**, e.g. `/reel` or `/lyric-reel`. The command is the brand (`/brag`).
- **Optional incumbent framing** (sonnet-stars-2): "open-source alternative to Kaiber / Neural Frames lyric-video makers", with a small comparison table (free, local, word-accurate, agent-driven). This pattern worked for OpenShorts (vs OpusClip) and OpenCut (vs CapCut).
- **Description and topics carry the search words:** `suno`, `lyric-video`, `music-video`, `beat-sync`, `reels`, `hyperframes`, `claude-code`, `agent-skills`, `claude-skills`, `codex`.

## README anatomy (in order)

1. Title, the one line, and **3 vertical reels playing inline** (GitHub `user-attachments` MP4 or GIF linking to MP4), labelled "real output".
2. **Copy this prompt** block: "Make a 30-second reel for `song.mp3` with these lyrics", followed by the commands the agent will run (motion-pack pattern).
3. Install in one line per agent (`npx skills add …` / plugin marketplace), same as brag.
4. A 3-command CLI quickstart on the bundled sample song.
5. "How the timing works" diagram: beats, bars, words, seam.
6. "What makes a reel work": a short, numbers-first summary of `analysis/playbook.md`. Publish **our own measurements only**: no reference reels, mascot, lyrics or downloaded media from other creators.
7. Gallery, license, contributing.

## Before going public: repo work (Phase 2 candidates)

- [ ] Finish **one** great reel with the Suno-first approach (README "Next step"); without it there is nothing to show.
- [ ] Rewrite README.md from a session handoff into the public README above. Move the "Start here (next session)" notes into `docs/` or `CLAUDE.md`.
- [ ] Add `sample/` with an own or CC0 short song, its lyrics and precomputed timing JSON.
- [ ] Package `SKILL.md` (+ Codex mirror) and a single CLI entry point.
- [ ] **Decide what to do with the reference research** (`reels.txt`, yt-dlp instructions, `analysis/comments/*.json` holding other people's comments, per-reel breakdowns of another account). Recommended: keep aggregated findings, drop or keep private the raw comment exports and download instructions. **Owner decision.**
- [ ] LICENSE, topics, release tag, issue templates; optional opt-in outro "made with music-reels" on rendered reels so every share advertises the repo.

## Launch plan (for the owner; we posted nothing)

All of these are outside actions that need the owner's approval:
- The reels themselves are the launch: post the reel first from the owner's account, then reply with the repo as "how it was made" (the PDoomVideo and brag pattern). Follow with the next 2–3 songs.
- A person and a channel bring the stars (Nate Herk's YouTube, a 71k-reader newsletter, an X account). The owner's own account is the channel: the repo is the follow-up to content that's already circulating.
- Also list on skills.sh and the HyperFrames showcase/Discord, and pitch the awesome list's "Music videos" section.
- Show HN / r/ClaudeAI / r/SunoAI / X thread with the reel embedded. A DEV.to write-up on how the word timing works (AutoMV launched this way).
- Submit to zhuyansen/awesome-claude-video-skills (2k stars, indexes HyperFrames skills) and ask the HyperFrames team about their showcase.
- Keep commits flowing during launch week. Stalled repos plateau (ShortGPT).

## Open questions / not verified

- Star-history curves and the real launch channels for brag, HyperFrames, OpenShorts: not collected.
- Whether Suno's terms allow redistributing a Suno-generated sample song in a public repo. Check before bundling one; otherwise use a CC0 song.
- Demand signal: an empty niche is also a sign of unproven demand (sonnet-stars-1). The reel's reach on social media is the real test.

## Inputs

| Agent | Slice | File |
|---|---|---|
| opus-strategist-1 | HyperFrames-ecosystem competitive set, README anatomy | `opus-strategist-1/notes.md` |
| sonnet-stars-1 | AI music / lyric-video tools | `sonnet-stars-1/notes.md` (PR #1) |
| sonnet-stars-2 | Creator studios / short-form tools | `sonnet-stars-2/notes.md` (PR #2) |
| opus-strategist-2 | Claude Code skills, Remotion/HyperFrames templates, brag star history | `opus-strategist-2/notes.md` (branch research/opus-strategist-2) |
