# Claude Code skills and Remotion/HyperFrames templates: what spreads

opus-strategist-2, 2026-11-14. My part of the team research: agent skills and code-video templates close to music-reels (Suno song → beat/word timing → HyperFrames → render).

> **Update after main moved to 6daad3d (owner steering, 10:15Z):** the repo now has `GUIDE.md` (a 390-line end-to-end guide), a finished 2:24 reel (`video/allow-always-final/`, rendered to the gitignored `video/out/allow-always-final-80s-boom2.mp4`), sung-word alignment (`scripts/align_words.py`, `songs/allow-always/align_final.py`), the Suno prompt history, an Instagram brief and the runbooks in `docs/runbooks/`. The "Where music-reels fits" section and the recommendations below were corrected for this. The repo comparisons are unchanged.

Method: `gh api` repo metadata and READMEs, `gh search repos`, a star-timestamp sample for one repo (`star-history/`), and the category list in `zhuyansen/awesome-claude-video-skills`. Star counts were taken on 2026-11-14 around 09:45Z. Launch channels are inferred from README links and badges. I did not check them against HN, X or Reddit, so treat them as unverified.

## The repos

| Repo | Stars | Created | Type | Why people star it |
|---|---|---|---|---|
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 84.1k | 2026-03 | Framework + CLI + skills + desktop studio | "Write HTML. Render video. Built for agents." Company-backed, with a Discord, Studio app, showcase and catalog. Agents use it through `npx hyperframes skills update`. |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 73.1k | 2020 | Framework | Built up over six years. React for video. |
| [remotion-dev/skills](https://github.com/remotion-dev/skills) | 7.0k | 2026-01 | Skill pack | Official best-practice skills. Offered during `bun create video`, so the install is part of creating a project. |
| [remotion-dev/template-tiktok](https://github.com/remotion-dev/template-tiktok) | 308 | 2024 | Template | Whisper word captions. Plain templates collect few stars even when they're official. |
| [latent-spaces/brag](https://github.com/latent-spaces/brag) | 21.4k | 2026-06 | Skill/plugin (+ hosted app) | One command, one emotion ("You built it. Now brag."). Its own launch video was made by `/brag` on itself. Every output carries the brand. |
| [obra/superpowers](https://github.com/obra/superpowers) | 317k | 2025-10 | Skill framework | General skills; shows how big the skill-install audience is. |
| [anthropics/skills](https://github.com/anthropics/skills) | 194k | 2025-09 | Official skill catalog | Where skills get discovered. |
| [JohnHeibel/PDoomVideo](https://github.com/JohnHeibel/PDoomVideo) | 2.9k | 2026-09 | Source of one music video | **Closest analog to us.** The source for a Claude-made music video of an AI-doom song. Clawd character, p5.brush, 9 chapters, parallel subagents, STORYBOARD.md. The video went out on YouTube/X and the repo picked up stars because people wanted to see how it was made. |
| [digitalsamba/claude-code-video-toolkit](https://github.com/digitalsamba/claude-code-video-toolkit) | 2.6k | 2025-12 | Toolkit | Script, voice, music and render "on open-source models that cost cents". |
| [nateherkai/herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) | 2.8k | 2026-04 | Skill kit (15 skills) | Creator-led: Nate Herk's YouTube audience. The README embeds finished videos ("AI edits everything: raw vs edited"). |
| [Tejashmakwana/motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | 1.6k | 2026-10 | Skill | A meme name ("looksmaxxing for motion graphics"), a "mid → maxxed" before/after hero GIF and measured claims ("12 measured eases"). Funnels to the author's X account and their product. |
| [artemnovitckii/claude-animation-skills](https://github.com/artemnovitckii/claude-animation-skills) | 742 | 2026-11-01 | 6 skills | 742 stars in 13 days. The README is a table of slash commands, each with a "Try it with" prompt and one frame per skill. Made for reels, Instagram safe-area check. |
| [charlie947/motion-graphics-skills](https://github.com/charlie947/motion-graphics-skills) | 673 | 2026-09 | 15 skills | Newsletter-led (71k-reader badge). One-line `npx skills add`. "Rules that came out of real rejected drafts." |
| [Moessif/code-video-showcase](https://github.com/Moessif/code-video-showcase) | 430 | 2026-10 | Skill | Pure-code beat-synced video, no generative models. |
| [Sunwood-ai-labs/hyperframes-motion-reel-skill](https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill) | 186 | — | Skill | Beat-synced HyperFrames reel. Generic, with no hero output. |
| [Win-Hao/music-mv](https://github.com/Win-Hao/music-mv) | 132 | 2026-10 | Music video in code | The awesome list's "Music videos" category opens with it. |
| [ShadoW-Shinigami/lyric-video-director](https://github.com/ShadoW-Shinigami/lyric-video-director) | 47 | 2026-07 | Skill | Lyric video built on image and video models. |
| [iart-ai/kinetic-typography-skills](https://github.com/iart-ai/kinetic-typography-skills) | 26 | 2026-06 | Skill | Beat-synced kinetic type. |
| [zhuyansen/awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills) | 2.0k | 2026-09 | Awesome list | Lists 180 repos by type, with a **Music videos (18)** category and a security grade for each. A cheap listing that people actually use. |

## Star history sample: brag (`star-history/latent-spaces_brag.tsv`)

Created 2026-06-16. Star #100 came on 06-23, #500 on 06-25 (launch week), #1000 on 07-29 (slow middle), then **#2000 → #4000 between 09-16 and 09-18**, a viral spike of about 2k stars in two days, after which it reached 21k. In other words: a quiet launch, a month of word of mouth, and then one moment (most likely a widely shared post or video) that multiplied it. I couldn't get timestamps for the other repos because the stargazer API returned 404 for them during this run.

## Patterns

1. **The output is the ad, and the README opens with it.** brag's site video was made by brag. herk-edit-kit shows four finished videos in the README. motionmaxxing shows a before/after GIF. PDoomVideo has a single YouTube link. The repos with stars show a finished piece above the install. Generic beat-sync skills with no hero video stay under 200 stars.
2. **One command, one verb.** `/brag`, `/map-route home to the gym`, `npx skills add owner/repo`. Every successful skill uses the `skills` CLI or plugin-marketplace install, and the install fits on one line. Several also list Codex/Cursor installs.
3. **A person and a channel bring the stars.** Nate Herk (YouTube), Charlie Hills (a 71k newsletter), @makwanatejas170 (X), the PDoom X/YouTube post. The repo is the "how it was made" follow-up to content that is already circulating.
4. **"How it was made" docs are part of the product.** PDoomVideo's STORYBOARD.md and ANIMATION_GUIDE.md, herk's EDITING-PLAYBOOK.md, motionmaxxing's NOTE.md. People star them to learn. Our `docs/research/playbook.md` and the reel breakdowns are this kind of material already.
5. **Measured or verified claims stand out.** "12 measured eases", "mog check G0–G5", a safe-area check, "every frame is code". Our timing JSON (BPM, bars, per-word timing) gives us the same kind of claim to make.
6. **Templates alone don't spread.** Remotion's official templates have about 300 stars. The skill or the story is what spreads, and the template is the payload.
7. **Ride the framework.** HyperFrames (84k) links its catalog and showcase, and HeyGen publishes `hyperframes-launches`. A repo built on HyperFrames can be put forward for the HyperFrames showcase or catalog and for the awesome list's Music videos section.

## Where music-reels fits

- What exists now (main 6daad3d): a finished 2:24 9:16 reel with a permission-prompt hook that loops, an avatar disco and karaoke captions. Also GUIDE.md, a full how-it-was-made guide with commands, prompts, a feedback log and dead ends, plus a committed final take (`songs/allow-always/take-final-yes.mp3`) and its timing data (`video/data/allow-always-final.json`). Our repo already has PDoomVideo's ingredients (a finished music video, a storyboard and process docs), and GUIDE.md is more thorough than what PDoomVideo publishes.
- What doesn't exist yet: an installable skill or one-command CLI. The pipeline is a set of per-song scripts (`cut_final.py`, `align_final.py` with hand-written line windows) across two Python venvs, with no requirements files at the root, plus HyperFrames pinned at 0.9.2 through `npx`. The rendered MP4 isn't in git (`video/out/` is ignored), so the README can't show the reel yet. There is no GIF or short excerpt either.
- Type: today it is a **studio-style source repo plus a guide**, like PDoomVideo and herk-edit-kit. It could grow into a **skill + CLI**. The fastest credible launch is PDoomVideo's: the reel plus "here's exactly how we made it". The skill can come after.
- Gap: no popular repo does **song → word/beat-timed lyric reel**. Lyric-video repos have 47 stars or fewer. PDoomVideo (2.9k) proves the demand but is a one-off source dump, not a reusable tool.
- Theme advantage: "allow always" is an AI-agent joke song, the same vein as P(doom), Clawd and alignment.check. That audience already shares this kind of content on X and YouTube.

## Recommendations (for RECOMMENDATIONS.md)

1. **The hero reel exists. Make it showable in the README.** Cut a 10–15 s GIF/MP4 excerpt (the hook at 0:01 and the disco/Earth explosion at about 1:05, matching the covers in `instagram-brief.md`) and attach it at the top of the README. Link the full 2:24 reel once the owner has posted it.
2. **Lead with GUIDE.md as the "how it was made" asset** (pattern 4). Its section 9 feedback log ("what the person said → the change that fixed it") and section 11 dead ends are the parts people share. Link both from the launch post.
3. **Ship a skill next**, something like `npx skills add oronanschel/music-reels` then `/music-reel song.mp3 lyrics.txt`. Generalise `cut_final.py` and `align_final.py` (the per-song line windows) into one `scripts/` entry point first. Keep `timing.py` usable on its own as a CLI ("song → timing JSON").
4. **Make the first run work offline:** add `requirements.txt` / `requirements-align.txt` for the two venvs, and let the committed `take-final-yes.mp3` and the `allow-always-final` timing JSON render the reel with no Suno account and no alignment step. Caveat from opus-strategist-1's re-check: the final composition reads `assets/dev/*.wav` through a gitignored `out/dev` symlink, so a fresh clone needs that WAV first. Don't use `cut_final.py` for this: it reads the gitignored `out/timing/` JSON and would overwrite the committed, hand-corrected `video/data/allow-always-final.json`. The fast path is one `ffmpeg -i songs/allow-always/take-final-yes.mp3 -ar 48000 out/dev/allow-always-final.wav` (a `make sample` step could wrap it). codex-tooling-1 (PR #5) rendered a short prototype from committed assets. The full 2:24 render is untested by the team. GSAP also loads from a CDN, and the repo has no LICENSE.
5. **README anatomy:** hero excerpt → one line ("Turn a Suno song into a beat-synced lyric reel with Claude Code") → the pipeline diagram from GUIDE.md section 1 → install/run → gallery (dance test, raw vs final) → GUIDE.md and the playbook → credits (vendored page-mascot MIT, HyperFrames).
6. **Make it measurable:** timing.py already reports figures we can claim, e.g. "125.009 BPM, median onset scatter 8 ms". Put those numbers in the README, and add a "sync check" render with a beat grid overlay.
7. **Launch the way PDoom and brag did:** the reel itself goes out first, through the Instagram brief's owner-approved post. Then the repo as the "how it was made" reply on X/YouTube, then submissions to awesome-claude-video-skills (Music videos), the HyperFrames showcase/Discord and skills.sh. All of these are owner actions; agents made no posts or sign-ups.
8. **Each reel credits the repo.** A small end card or caption ("made with music-reels") means every reel shared also markets the repo. Keep it out of the loop frame so the loop doesn't break.
9. **Name the command.** Use a short, memeable one (for example `/drop`, `/reelify`) rather than "music-reels". This is the owner's decision.

## Files

- `notes.md`: this file
- `star-history/latent-spaces_brag.tsv`: sampled star numbers with their timestamps

## Owner-requested repo: zai-org/CogVideo (added 10:28Z)

- **Stars and speed:** 13.2k stars. The repo dates from 2022-05 (CogVideo, ICLR 2023), but most stars likely came with the CogVideoX open-weights releases in Aug–Nov 2024. That is inferred from the README news log; I didn't sample star timestamps (the API returns 404 for stargazer timestamps here). Last push 2025-11. The code is Apache-2.0. That badge doesn't establish the model-weight terms, which are separate (caveat from codex-tooling-2). The same goes for any B-roll we'd generate with it: check the weight license first.
- **What it is:** a **model** (text/image → video weights plus inference and fine-tuning code) from Zhipu/THU. It is not a skill, CLI or studio.
- **README and demo strengths:** the first screen has a hosted try-it link (Hugging Face Space / ModelScope), so people can try it with zero install. It also links the paper, a user guide, Discord/WeChat, a 🔥 dated news log that shows the project is alive, and translated READMEs (Chinese, Japanese).
- **How it launched:** through research and model-hub channels: an arXiv paper, Hugging Face weights and Space, diffusers integration, plus community tools built on it (cogvideox-factory for one-4090 fine-tuning). Stars follow model releases, not marketing posts.
- **Copy:** a zero-install try-it link at the top (for us, the rendered reel plus a hosted gallery page), a dated news log, translated READMEs once there's traction, and letting the community build on it (a documented timing JSON contract).
- **Avoid:** a model-style README full of GPU and fine-tuning detail. Our audience is creators and agent users, not ML researchers. CogVideo is a possible *ingredient* (generated B-roll), not a competitor. Our pitch is the opposite: deterministic, code-drawn, beat-synced, with no GPU needed.
