# sonnet-stars-1: AI music / lyric-video tools on GitHub

Data pulled 2026-11-14 with `gh search repos` / `gh repo view` and web search. Star counts are live at pull time. Launch channels and timing are NOT verified for most repos. I had no time to build star-history curves, so those are marked "unverified".

## Headline finding
**The exact niche (Suno song -> word timing -> lyric/reel video) is nearly empty.** The top results for "lyric video generator" on GitHub have 14, 9, 8, 6 and 5 stars. Nobody owns it. That's an opportunity (no incumbent to beat) and a warning (no proven demand signal in this exact niche). The stars sit in adjacent categories.

## Table
| Repo | Stars | Created | Type | What it is |
|---|---|---|---|---|
| fspecii/ace-step-ui | 5,216 (802 forks) | 2026-02-04 | Studio/UI | "The Ultimate Open Source Suno Alternative". React/TS/SQLite web UI over ACE-Step 1.5 |
| gcui-art/suno-api | 3,312 (927 forks) | 2024-03-27 | API server | Unofficial Suno API, OpenAI-compatible, Vercel/Docker one-click, GPTs/Coze plugin schema |
| paperfoot/suno-cli | 62 | 2026-04-06 | CLI (Rust) | Suno from the terminal, JSON output for agents, embeds synced lyrics in MP3s |
| remotion-dev/template-music-visualization | 27 | 2025-04-02 | Template | Official Remotion spectrum/waveform template |
| chrimage/ai-lyric-video-generator | 14 | 2025-03-20 | Script | Top "lyric video generator" hit |
| ZiadAbdelkarim/beat-synced-edit | 14 | 2026-08-07 | CLI + Claude Code skill | Song + footage -> beat-cut edit, demos embedded in README |
| ANVEAI/motion-pack | 6 | 2026-10-13 | Skill pack (HyperFrames) | Prompt -> finished MP4 with music, sound, captions |
| YinTokey/AutoMV | unknown (not in search top) | ~2025-08 | Script | GPT + Runware + Suno + FFmpeg, ~$0.08-0.12/video; announced via a DEV.to post |
| gouveags/ai-music-video-generator | ~14 (indexer, stale) | 2024 | Script | OpenAI lyrics + DALL-E + Suno + FFmpeg + auto-upload |

Reference point from the HyperFrames ecosystem (same engine as ours): heygen-com/hyperframes 84k stars (created 2026-03-10), latent-spaces/brag 21k (created 2026-06-16, "turn your project into a launch video with one command"), nexu-io/html-video 4.8k, nateherkai/herk-edit-kit 2.8k, zhuyansen/awesome-claude-video-skills 2.0k (curated list, created 2026-09-27), Tejashmakwana/motionmaxxing 1.6k.

## What made the high-star ones work
1. **ace-step-ui: a one-line enemy/promise.** "Stop paying for Suno! Free, local, unlimited." Cost-saving + anti-incumbent + topic `suno-alternative`. Riding a search term people already use (Suno) is the cheapest discovery channel. README: centered logo, badges, nav links to #demo / #features / #installation, demo near the top, MIT license badge, live star badge, and creator's YouTube / X badges (the author funnels attention to their own channels).
2. **suno-api: filled a gap with demand.** Suno has no official API; the repo says so in line 1 of "Introduction". Gives a live demo URL, one-click Vercel/Docker deploy, multi-language READMEs (EN/CN/RU), Product Hunt badge, "We update quickly, please star" CTA, and cross-promo of the author's next project. Most stars came from agents/GPT-plugin builders in 2024.
3. **paperfoot/suno-cli: agent-friendly by design.** JSON output, `agent-info`, `guide`, an offline `prompt` command, installs from crates.io. Only 62 stars, but this is the pattern the skills ecosystem rewards: tool is described for agents, not only humans.
4. **motion-pack and beat-synced-edit**: both have a "paste this prompt" section (motion-pack) or two-modes section, "Pure CLI vs Claude Code skill" (beat-synced-edit), with inline MP4s/GIFs at the top. Still low stars (6, 14), so demo quality alone does not make a repo spread; distribution does.
5. **brag (21k) shows the viral pattern in this ecosystem**: one command, output that people *want to post*, so every user advertises the repo. (Details for the skills agents to confirm.)

## Why small lyric-video repos stay small (patterns to avoid)
- Empty descriptions, no demo, no license, multi-step API-key setup, README is install steps first and output last.
- Positioned as a generic "tool", not as a result ("make this exact video").
- Static-image output (AutoMV: "static image videos for now"), so there's nothing visually striking to share.
- No agent/skill packaging, no "open it in Claude Code and say X".

## Recommendations for music-reels (my slice)
1. **Lead with the output, not the pipeline.** First screen: 3 vertical reels as autoplaying GIF/MP4 (GitHub user-attachments video embed works, see beat-synced-edit), then one sentence: "Suno song in, word-synced lyric reel out. Claude Code does the work."
2. **Own the empty niche with a name that matches search**: topics `suno`, `lyric-video`, `hyperframes`, `claude-code-skill`, `ai-music-video`, `reels`, `beat-sync`. Description should contain "Suno" and "lyric video".
3. **Ship as a skill + CLI, both.** Copy-paste prompt block ("Make a reel for song.mp3") like motion-pack, plus a deterministic CLI path like beat-synced-edit. The scripts in the repo (beat/word timing) already are the CLI half.
4. **Cost/anti-incumbent hook**: "No Premiere, no CapCut, no per-render fees; runs locally." (HyperFrames is Apache-2.0 and local; ace-step-ui and html-video both lean on "free, local".)
5. **Include a sample song + sample output in the repo** (CC0 / own song) so a clone produces a video in under 5 minutes with zero API keys. Every small competitor requires keys first.
6. **Distribution plan (not executed, no public posts allowed this phase):** DEV.to/Hashnode write-up (AutoMV did this), Show HN with the video, r/SunoAI, r/ClaudeAI, X thread with the reel itself, submit to zhuyansen/awesome-claude-video-skills and awesome lists, ask HeyGen/HyperFrames to list it in their showcase. Post the reels of the songs the project makes: the product is its own marketing.
7. **Make the output shareable by default**: watermark/credit line "made with music-reels" on the final frame (brag-style loop), toggleable.
8. Add multi-language README (suno-api and motion-pack both did; CN has big audience for Suno-like tools).

## Gaps / unverified
- No star-history curves collected; launch dates of viral spikes unknown.
- brag and hyperframes launch channels left to opus-strategist-2 / others.
- AutoMV star count not retrieved.
