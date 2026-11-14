# opus-strategist-1: competitive set for music-reels (2026-11-14)

Scope: AI lyric-video / beat-sync tools and the HyperFrames-ecosystem "creator studio" repos that music-reels would sit next to.
Data: `gh search repos` / `gh api repos/...` on 2026-11-14 around 09:45Z (star counts as returned then). Star *history* and launch channels are covered by sonnet-stars-1/2; claims below about why a repo spread are marked **[H]** when they're inferred from the README and not checked.

## 1. The headline finding: the niche looks underserved (search sample, not a census)

| Search (sorted by stars) | Top result | Stars |
|---|---|---|
| "lyric video generator" | chrimage/ai-lyric-video-generator | 14 |
| "music video ai" | AryanMadhavVerma/barp-music-video-ai | 3 |
| "beat sync video" | Meteor8/beats-synced-video-generator | 16 |
| "beat sync video" (agent skill) | ANVEAI/motion-pack (beat-synced films, 2026-10) | 6 |
| "hyperframes" | heygen-com/hyperframes | 84,099 |

In these searches nobody owns "song → word-timed, beat-synced reel" on GitHub. The engine underneath (HyperFrames, created 2026-03-10) is one of the fastest-growing repos of the year, and the skills built on it collect thousands to tens of thousands of stars. music-reels would be the first music-first entry in a hot ecosystem.

## 2. The ecosystem we'd launch into

| Repo | Stars | Created | Type | What it promises (one line) |
|---|---|---|---|---|
| heygen-com/hyperframes | 84.1k | 2026-03 | framework | "Write HTML. Render video. Built for agents." |
| OpenMontageInc/OpenMontage | 80.4k | 2026-03 | agentic studio | "First open-source agentic video production system", 12 pipelines, 700+ skills |
| latent-spaces/brag | 21.4k | 2026-06 | skill (+ hosted app) | `/brag`: turn the project you just built into a launch video |
| nexu-io/html-video | 4.8k | 2026-05 | CLI/framework | HTML → MP4 on your laptop, for coding agents |
| nateherkai/herk-edit-kit | 2.8k | 2026-04 | skill kit | Creator's own editing kit: 15 skills, 406 motion cards |
| zhuyansen/awesome-claude-video-skills | 2.0k | 2026-09 | awesome list | 180 repos of video skills for agents |
| Tejashmakwana/motionmaxxing | 1.6k | 2026-10 | skill | "Looksmaxxing for motion graphics", measured gates |
| ANVEAI/motion-pack | 6 | 2026-10 | skill + parts | Prompt → beat-synced MP4 with music and captions |

Adjacent music repos with real pull: m-bain/whisperX 25k (word timestamps), rzru/nightingale 1.5k (ML karaoke app, 2026-03), fspecii/ace-step-ui 5.2k ("open source Suno alternative", 2026-02), tsoding/musializer 1.5k (built on stream).

## 3. What the winners do (README + demo anatomy)

1. **One verb, one command.** brag: "You built it. Now brag." + `/brag`. Install is a single `npx skills add …` / plugin-marketplace line for Claude Code *and* Codex. The name is the command.
2. **The README demo was made by the tool, about the tool.** brag's launch-site loop "was made by /brag on this very repo". herk-edit-kit's top video is "AI edits everything: the reveal", a reel about how it was edited. Self-reference is the proof and the marketing at once.
3. **Video plays inside the README.** herk-edit-kit embeds `user-attachments` MP4s so you hit Play on GitHub; motion-pack and motionmaxxing use GIF heroes linking to MP4. No click-away.
4. **A copy-paste prompt above the fold.** motion-pack: "Copy this prompt", then shows the exact commands the agent will run. OpenMontage: "Try these prompts" and "Paste a video you already love".
5. **A meme-able frame or rating.** motionmaxxing borrows internet slang ("slop / mid / maxxed", "mog check") and a rating table. **[H]** That framing is why a 1-month-old skill reached 1.6k.
6. **A face behind it.** herk-edit-kit is a creator's personal kit ("how Nate's videos get edited"); motionmaxxing and ace-step-ui put X/YouTube badges at the top. **[H]** The creator's audience is the launch channel.
7. **A no-install path.** brag adds letsbrag.app ("paste your link") while keeping the skill free. OpenMontage has openmontage.video. Most people who star never install.
8. **Measured rules, not vibes.** herk-edit-kit ships an "editing playbook" with "the measured house reel style"; motionmaxxing advertises "12 measured eases" and gates G0–G5. Our `analysis/playbook.md` is already this kind of asset.
9. **Topics tuned for discovery:** `claude-code`, `agent-skills`, `claude-skills`, `hyperframes`, `codex`. Every hit above uses them; awesome-claude-video-skills indexes by them.

## 4. What music-reels already has that they don't

- A **real measured playbook** from 10 breakdowns of a reel account (BPM range, seam error < 40 ms on winners, claim on screen at 0.27 s, kick-drop timing). Nobody else publishes "why this reel got 647K views" with numbers.
- **Word + beat timing** (`scripts/timing.py`, `align_words.py`): the hard part lyric tools skip.
- A **Suno recipe** that controls arrangement (a cappella intro → riser → drop, Duration = Custom).
- Gaps: no finished reel, no one-command path, a README written as a session handoff, Instagram-download research that should stay out of the public story.

## 5. Recommendations (for RECOMMENDATIONS.md)

1. **Position:** "The first HyperFrames skill for music: Suno song in, beat-synced lyric reel out." Type: a Claude Code/Codex **skill + CLI**, not a studio. Studios are a crowded 80k-star fight; a skill is how brag (21k in ~5 months) won.
2. **Name it as a verb:** e.g. `/reel` or `/lyric-reel`. One line: "Your song deserves a video."
3. **Ship one great reel before launch.** It has to be made by the skill about the skill, so the reel's song is about making reels with an agent (the "allow always" concept fits). Embed it as playable MP4 at the top of the README.
4. **Demo input that needs no Suno account:** a bundled CC0/own short song + its timing JSON, so `npx …` → render works offline in under 5 minutes.
5. **Lead with the playbook as the hook:** "We measured 10 viral reels. Here's what the top one did in its first 0.27 s." Publish our own measurements and leave out their media, mascot and lyrics.
6. **Topics:** claude-code, agent-skills, claude-skills, hyperframes, codex, suno, lyric-video, music-video. Submit to awesome-claude-video-skills once it's public (needs owner approval: outside action).
7. **Later, optional:** a hosted "paste a Suno link" path like letsbrag.app. Not for v1.
