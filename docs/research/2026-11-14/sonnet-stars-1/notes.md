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

---

## Update after rebase onto main 6daad3d (GUIDE.md, final video, runbooks)
My first draft was written against the old main. What changed:

- **Corrected:** the repo is no longer "pipeline without an output". It has `GUIDE.md` (390 lines, full pipeline), a finished 2:24 vertical 60 fps video (`video/allow-always-final`, a loop whose last frame equals the first), real Suno prompt history, sung-word alignment (`scripts/align_words.py`, `songs/allow-always/align_final.py`; WhisperX + demucs in a separate venv), and `docs/runbooks/`. Rec 1 ("lead with the output") is now actionable: the demo exists, it only needs to be embedded in the README.
- **Corrected:** "scripts already are the CLI half". Partly true: `scripts/timing.py` (librosa beat grid) and `align_words.py` exist, but they are per-song scripts, not one command with a stable interface. There is no `music-reels` CLI or skill yet. `video/package.json` pins HyperFrames 0.9.2.
- **Corrected:** rec 5 (sample song so a clone runs without keys). A song (`songs/allow-always/take-final-yes.mp3`, 3.5 MB) and the composition are in the repo, so a no-key demo is feasible: render the existing composition with `npx hyperframes@0.9.2 render`. Not tested by me. The Suno step needs an account and the image-generation step uses Codex `image_gen`, so a from-scratch run is not key-free. Whether the sprite assets are committed and licensed for public reuse is unchecked (Suno free-tier output licensing also needs a check before publishing the song).
- **Still true:** the repo has no LICENSE file in the root (`ls LICENSE*` found nothing), and README still opens with "Earlier planning notes" that say the reel is paused and "no video was built". That text is stale against the finished video and will undercut a public first impression. Replace it with the output-first layout from rec 1.
- **New point in GUIDE.md's favour:** it is a rare "how we made it" document with prompts and mistakes. Of the repos I surveyed, none has this. The guide is a better headline asset than the code: consider a blog/DEV.to version (AutoMV used one).
- `songs/allow-always/instagram-brief.md` says nothing gets posted without owner OK. Consistent with this phase's no-public-posts rule; my launch-channel list (rec 6) is a plan only.
- I did not re-run the render, so the reproducibility of the one-command path is unverified here. codex-tooling-1 owns that audit.

---

## Owner-requested repos (sonnet-stars-1 slice: Pixelle-Video, page-mascot)
Data: `gh repo view` at 2026-11-14 plus web search. The stargazers API returns 404 for us, so **there are no star-history curves**. Growth rates below are averages from created date, or from third-party snapshots (marked).

### 1. Pixelle-Video (github.com/AIDC-AI/Pixelle-Video, formerly ATH-MaaS/)
- **Stars:** 30,079, forks 4,366. Created 2025-11-07 (about 12 months). Average about 82 stars/day, but not even: third-party blogs date a launch/trending wave to **2026-05-04/05** when it was about 7,000-7,200 stars, i.e. roughly 23k stars came in the six months after (unverified snapshots, aggregator sources). Last push 2026-06-14.
- **Type:** studio/engine. Python, Streamlit WebUI + API, ComfyUI / RunningHub workflows, direct model APIs (DashScope, OpenAI, Seedream, Kling...), Windows all-in-one package, Docker. Apache-2.0 (plus NOTICE). Owner is an Alibaba AIDC org, so it has corporate credibility and reach.
- **README/demo:** centered title, language switch (中文 / English), badge row led by *video tutorial (Bilibili)*, *Windows package*, *docs site*, then an inline demo video **above the text**. Promise in one line: "enter a topic, get a full video: script, images, voice, music, compose". "Zero barrier, zero editing experience." Then a Web UI screenshot, a dated changelog (11 entries in 6 months, which signals it's alive), feature checklist, flow diagram, and a gallery of example videos per module (digital human, image-to-video, motion transfer).
- **Why it appeals:** it removes the whole job for people who want volume content; Windows package lowers install to a download; Chinese-language-first docs and Bilibili tutorial hit the largest audience for this tool category.
- **Copy:** video above the fold; one-sentence outcome; a no-terminal install path; dated changelog in README; a docs site; a video tutorial link in the first badge row.
- **Avoid:** feature-sprawl (every model/API under the sun) and heavy dependencies on ComfyUI/GPU workflows. Our pitch is the opposite: one narrow, finished artifact (beat-synced lyric reel).

### 2. page-mascot (github.com/nilbuild/page-mascot)
- **Stars:** 1,376, forks 148. Created 2026-09-14, so about 2 months, about 22 stars/day on average. Single commit visible in history ("Initial commit"), one contributor, last push 2026-09-15 (the repo got its stars in the first weeks; no star-history curve). The author is **Kamran Ahmed** (kamran.fyi, 41k GitHub followers; widely known as the roadmap.sh founder). I found no Hacker News/Twitter launch post; the likely main channel is the author's own audience (inference, not verified). A third-party blog (themenonlab.blog) covered it.
- **Type:** skill + React component + 52 premade characters + demo site (koboyo.com/page-mascot). `npm i page-mascot`, and `npx skills add nilbuild/page-mascot --skill page-mascot`.
- **README/demo:** logo image, a single bold link "See the fifty-two →" to a live demo, then three tiny code blocks (install, use existing, draw your own with a prompt such as `/page-mascot a chibi otter`), a props table, a "How it works" with two sprite-sheet images, and one image of the same fox in six styles. Short, visual, instantly understood: the demo page is the product.
- **Why it appeals:** delight + near-zero effort (one tag, one prop pair) + an agent skill so "make one that looks like me" works. The 52-character gallery is shareable on its own.
- **Copy:** a live gallery page that sells the thing; prompts shown as the usage example (`/music-reels make a reel for song.mp3`); "use existing" vs "draw your own" split; a "How it works" with one diagram; install of skill by one `npx skills add` line.
- **Avoid:** requiring OPENAI_API_KEY for the main path (it does this for custom drawing).

#### License and credit for our vendored copy
- Upstream license: **MIT, "Copyright (c) 2026 Kamran Ahmed"**. Our `vendor/page-mascot/UPSTREAM.json` records the upstream commit (`76a44ed…`), import date 2026-11-13, "unmodified" renderer/skill/scripts plus four sample characters (afro, ballerina, glasses, skater), and sha256 hashes. `vendor/page-mascot/LICENSE` is present, so the MIT condition (keep the copyright notice and permission text in copies or substantial portions) is currently met inside `vendor/`.
- MIT is the only licence stated for the repo, and it has no separate art licence, so the character PNG/WebP files are covered by the same MIT terms as far as I can tell. This is my reading of the files, not legal advice. Worth one message to the author if the reel puts their characters front and centre.
- **What to do before going public** (the MIT text doesn't require attribution beyond the notice, but crediting is the right move):
  1. Keep `vendor/page-mascot/LICENSE` intact and untouched. If any vendored file is changed, say so in UPSTREAM.json (it currently says unmodified).
  2. Add a `CREDITS.md` or README "Credits" section: "Sprite-atlas tooling and reference workflow adapted from page-mascot by Kamran Ahmed (MIT), https://github.com/nilbuild/page-mascot; reel dance/action art generated separately." (wording from codex-tooling-1). A per-video caption or end-card credit is optional, not an MIT requirement.
  3. Add the same credit to the Instagram caption's credit line (GUIDE.md already has "a credit line naming the tools") and optionally the video's end card.
  4. The repo root has no LICENSE yet: choose ours (MIT would be consistent) and state that `vendor/page-mascot/` keeps its own MIT notice.
  5. Don't use the author's name or koboyo.com to imply endorsement.
- Note the community angle: page-mascot is trending in the same "agent skill that draws characters" space, so a tagged thank-you to the author after launch (once posting is allowed) is cheap goodwill and a possible signal-boost.

### Updated recommendations from these two
- README opening: outcome sentence, then a video/GIF of the reel directly under the title (Pixelle does it above the text), then a badge row led by "Watch / Guide / Install".
- Make a live gallery page of finished reels (page-mascot's demo page sells it). GitHub Pages is free and needs no account beyond the repo's.
- Show the agent prompt as the usage example.
- Keep the dated changelog habit: it signals life.
- Launch moments that moved these repos: Pixelle had a visible wave around a trending appearance; page-mascot rode the author's existing audience. We have neither, so a trending-day plan plus a ready-made share asset (the reel) matters more for us.

### 3. CogVideo / CogVideoX (github.com/zai-org/CogVideo, formerly THUDM/)
(Picked up because nobody had claimed it; sonnet-stars-2 has MoneyPrinterTurbo.)
- **Stars:** 13,201, forks 1,393. Created 2022-05-29 (the original CogVideo, ICLR 2023 paper); the 2024 CogVideoX releases are what the README timeline highlights (2B on 2024-08-06, 5B 2024-08-27, I2V 2024-09-19, 1.5 on 2024-11-08). Last push 2025-11-04. No star curve available (API 404), so I can't say which release produced the jumps; each README news item is a candidate spike. Average over 4.5 years is about 8 stars/day, but most came after the August 2024 open-sourcing (inference, not measured).
- **Type:** model + research code (SAT and diffusers inference, LoRA fine-tuning), not a skill/CLI/studio. Apache-2.0 code; model licences vary by weights (README says the 2B weights moved to Apache-2.0).
- **README/demo:** logo, "try it online" row (HuggingFace Space, ModelScope studio) first, then paper and user-guide links, WeChat/Discord, a commercial-product link (QingYing, API platform), then a **dated "Project Updates" list with a 🔥 per item**, and READMEs in 中文/日本語. Demo is a hosted Space: zero install.
- **Why it appeals:** first open text-to-video model that ran on consumer GPUs ("2B on a GTX 1080 Ti, 5B on an RTX 3060"). That sentence is the hook. Lots of third-party tooling (cogvideox-factory, CogKit, ComfyUI nodes) grows the halo.
- **Copy:** a hosted one-click demo; a hardware-accessibility claim stated plainly; frequent dated news items; multi-language READMEs; Discord/WeChat for community.
- **Avoid / not applicable:** it is research-lab distribution (paper, HF, lab brand) that we can't replicate; it is also a competitor to nothing we do. Our reels are rendered from HTML, not generated by a video model. At most it's a possible optional background-footage backend. Don't position against it.

### Takeaway across Pixelle, page-mascot, CogVideo
All three put a **runnable or watchable demo before any install text** (video, live gallery, hosted Space), state the outcome in one line, and keep a **dated update list** in the README. None needed a perfect repo. All three had a distribution advantage we don't yet have (corporate org, an author with 41k followers, a lab with a paper). Our equivalent has to be the share-worthy reel itself.

### Overlap note
CogVideo and page-mascot were also covered by others (opus-strategist-2 on PR #3, codex-tooling-1 on PR #5, sonnet-stars-2 on PR #2), and sonnet-stars-2 also did Pixelle-Video, so some findings are duplicated; the numbers agree where I compared them. Credit wording caveat from codex-tooling-1: `docs/research/avatar-pipeline.md` says the reel's images were generated separately from the vendored characters. Credit page-mascot for the adapted tooling and sprite-sheet workflow, and only name upstream characters if they appear in the video. My credit list above says "Avatars/sprite sheets ... adapted from page-mascot"; narrow it to that scope.

### Correction from codex-tooling-1 (PR #5, page-mascot-launch.md)
I said I found no launch post for page-mascot. codex-tooling-1 found the author's X announcement dated 2026-09-14 10:50 UTC, the same day the repo was created (cause of the stars still unknown). So the launch channel was the author's own X audience, with a command-plus-demo format. Full evidence is in their notes.
