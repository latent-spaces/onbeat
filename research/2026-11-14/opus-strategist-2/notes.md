# Claude Code skills and Remotion/HyperFrames templates: what spreads

opus-strategist-2, 2026-11-14. My part of the team research: agent skills and code-video templates close to music-reels (Suno song → beat/word timing → HyperFrames → render).

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
4. **"How it was made" docs are part of the product.** PDoomVideo's STORYBOARD.md and ANIMATION_GUIDE.md, herk's EDITING-PLAYBOOK.md, motionmaxxing's NOTE.md. People star them to learn. Our `analysis/playbook.md` and the reel breakdowns are this kind of material already.
5. **Measured or verified claims stand out.** "12 measured eases", "mog check G0–G5", a safe-area check, "every frame is code". Our timing JSON (BPM, bars, per-word timing) gives us the same kind of claim to make.
6. **Templates alone don't spread.** Remotion's official templates have about 300 stars. The skill or the story is what spreads, and the template is the payload.
7. **Ride the framework.** HyperFrames (84k) links its catalog and showcase, and HeyGen publishes `hyperframes-launches`. A repo built on HyperFrames can be put forward for the HyperFrames showcase or catalog and for the awesome list's Music videos section.

## Where music-reels fits

- Type: it should ship as a **skill + CLI with a hero reel**, not as a template. That means a skill such as `/music-reel` (Suno song → `timing.py` → HyperFrames composition → render), with `scripts/timing.py` as a usable CLI on its own.
- Gap: no popular repo does **song → word/beat-timed lyric reel**. Lyric-video repos have 47 stars or fewer. PDoomVideo (2.9k) proves the demand but is a one-off source dump, not a reusable tool.
- Theme advantage: "allow always" is an AI-agent joke song, the same vein as P(doom), Clawd and alignment.check. That audience already shares this kind of content on X and YouTube.

## Recommendations (for RECOMMENDATIONS.md)

1. **Finish one great reel before launch.** It should be 30–45 s, 9:16, and land the hook in the first 2 s. It is the README hero, the launch post and the proof. Without it nothing else matters (patterns 1 and 6).
2. **Ship it as a skill.** Something like `npx skills add oronanschel/music-reels`, then `/music-reel path/to/song.mp3 lyrics.txt`, plus a Claude Code plugin marketplace entry. Keep `timing.py` usable on its own as a CLI ("song → timing JSON"). It is the most reusable piece and it's what other skill authors would star.
3. **README anatomy:** the hero reel (GIF + MP4 link) → one line ("Turn a Suno song into a beat-synced lyric reel with Claude Code") → a one-line install → a "Try it" prompt → the 4-step pipeline diagram → a gallery with a raw vs final comparison → "How it was made" (link the playbook) → credits.
4. **Bundle a sample song with its timing JSON**, so the first run works with no Suno account or credits.
5. **Make it measurable:** report per-word timing error and beats hit, and add a "sync check" render with a beat grid overlay. That gives us a claim like motionmaxxing's.
6. **Launch the way PDoom and brag did:** post the reel itself first, from the owner's account, with the repo as the "how it was made" reply. Then submit to awesome-claude-video-skills (Music videos), the HyperFrames showcase/Discord and skills.sh. These are owner actions; agents made no posts or sign-ups.
7. **Each reel credits the repo.** A small end card or caption ("made with music-reels") means every reel shared also markets the repo, the way brag's videos do.
8. **Name it.** Use a short, memeable command (for example `/drop`, `/reelify`, `/lipsync`) rather than "music-reels". Every top skill has a one-word verb. This is the owner's decision.

## Files

- `notes.md`: this file
- `star-history/latent-spaces_brag.tsv`: sampled star numbers with their timestamps
