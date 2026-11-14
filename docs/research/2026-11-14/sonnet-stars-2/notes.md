# Creator studios & short-form video tools: what made them spread

Author: sonnet-stars-2 · 2026-11-14 · Scope: open-source "topic/long video -> short video" tools and studios (the neighbours of our music-reels repo).

Method and limits: `gh api` for stars/forks/created/pushed/topics (live numbers as of 2026-11-14) and the README of each repo. The stargazer-timestamp API returned 404 in our sandbox, so **there is no star-history curve data**; only created date vs. current stars. Launch channels (HN/Reddit/X) were not verified by search, so anything about channels below is inferred from README signals and is marked as such.

## Data

| Repo | Stars | Forks | Created | Type | Core stack |
|---|---|---|---|---|---|
| harry0703/MoneyPrinterTurbo | 143k | 23k | 2024-03 | WebUI + API app | Python, LLM script, TTS, stock footage, ffmpeg/moviepy |
| OpenCut-app/OpenCut | 98k | 9.8k | 2025-06 | Studio (editor), "open-source CapCut alternative" | web app |
| heygen-com/hyperframes | 84k | 7.8k | 2026-03 | Framework (HTML -> video), "Built for agents" | TS, GSAP, Puppeteer, ffmpeg, MCP, claude-code topic |
| remotion-dev/remotion | 73k | 6.1k | 2020-06 | Framework (React -> video) | React |
| FujiwaraChoki/MoneyPrinterV2 | 32k | 3.5k | 2024-02 | CLI automation | Python |
| FujiwaraChoki/MoneyPrinter | 14k | 1.8k | 2024-01 | CLI/script | Python, MoviePy |
| RayVentura/ShortGPT | 8.2k | 1.2k | 2023-06 | Framework + Colab/WebUI | Python, TinyDB |
| mutonby/openshorts | 8.1k | 1.7k | 2025-12 | Self-hosted studio + hosted cloud | Docker, Gemini, ElevenLabs, MCP |
| gyoridavid/short-video-maker | 1.5k | 450 | 2025-04 | REST + MCP server | Remotion, Kokoro TTS, Whisper |
| lyric-video generators (best: Manzana-Apple-Music-Lyrics) | <150 | | | niche | |

Key observation: **a search for "lyric video generator" on GitHub tops out at ~147 stars.** The niche is wide open; nobody owns "Suno song -> beat/word-timed reel". The big stars are in the generic "topic -> faceless short" and "agent-native video" categories.

## Per-project anatomy

**MoneyPrinterTurbo (143k).** Why: one sentence promise ("give a topic, get an HD short"), a WebUI screenshot right under the title, a free-to-run path, Chinese-first README with EN/JA translations (huge Chinese dev audience), money-themed name that signals the use case. README carries Trendshift and star-history badges, a sponsor block (LLM/API vendors paying for placement), release/download badges and an API screenshot. Kind: app, not skill.

**MoneyPrinter / V2 (14k/32k).** The name is the hook ("make money online"). Pattern: tutorial YouTube video by the author drove the first wave (the README links its video), then the v2 rebranded to broader "automate money" use cases. Kind: CLI/scripts.

**ShortGPT (8k).** Notable README tactics: Discord badge, Colab quick-start (zero install, "highly recommended"), showcase video embeds at the top, a "how it works" diagram, a "star us" section, docs site and PyPI downloads badge. Last push 2025-02: stars plateaued once maintenance stopped.

**OpenShorts (8k in ~5 months).** Best README anatomy among the recent ones: positions as "the open-source OpusClip alternative", a comparison table vs. paid incumbents in the first screen, a real before/after GIF labeled "Real output, not a mock-up", self-host vs. cloud table (open core), MCP/API for agents, topics `agent-skills`, `mcp-server`, `opus-clip-alternative`. Pushed daily. Lesson: name a known paid product and beat it on a table.

**short-video-maker (1.5k).** Spun out of a YouTube channel ("AI Agents A-Z") plus n8n tutorial video and Skool community; MCP + REST server. Lesson: creator-channel tutorial is the distribution channel; stars are modest because audience is the channel's.

**OpenCut (98k).** "The open-source CapCut alternative": same positioning trick, much bigger category.

**HyperFrames (84k in 8 months) and Remotion (73k over 6 years).** Out of my slice but relevant: HyperFrames tagline "Write HTML. Render video. Built for agents." shows that "agent-native" is the strongest current tailwind (topics: ai-agents, claude-code, mcp). Our repo sits on top of it, so we can ride the same wave.

## Patterns that correlate with stars

1. **One-sentence outcome promise** with a recognisable incumbent or category ("OpusClip alternative", "CapCut alternative", "topic -> short").
2. **Proof above the fold**: demo GIF/video or UI screenshot before any install text. OpenShorts labels it real output.
3. **Zero-friction try path**: Colab, Docker one-liner, hosted site, or free-tier API keys.
4. **Agent/MCP angle** in 2025-26 projects (openshorts, short-video-maker, hyperframes).
5. **Badges and social proof**: Trendshift, star-history, Discord, downloads. (Inferred: Trendshift badge suggests the repo trended on GitHub; not verified.)
6. **Creator-channel distribution**: ShortGPT, short-video-maker, MoneyPrinter all link the author's YouTube walkthrough.
7. **Multilingual README** (MoneyPrinterTurbo en/zh/ja).
8. **Continuous commits**: openshorts/MoneyPrinterTurbo pushed within last day; ShortGPT stalled and plateaued.
9. **Output is shareable by itself.** Every one of these produces videos people post, which advertises the tool. (Our reels can carry a watermark/outro "made with music-reels" as an opt-in.)

## Weak spots to avoid
- Heavy sponsor blocks before the pitch (MoneyPrinterTurbo gets away with it only at 143k).
- "Make money" framing invites spam/low-quality association.
- Unmaintained repos stall.

## Recommendations for music-reels (my slice)

1. **Own the empty niche**: title like "Suno song -> beat-synced lyric reel, rendered by an agent". Existing lyric-video repos max out near 150 stars, so a polished one can be #1 in its category quickly.
2. **Lead the README with 3 real example reels** (GIF + mp4 link), each a Suno song, labeled "real output". Then a one-paragraph promise, then a 3-command quickstart.
3. **Position vs. an incumbent**: "open-source alternative to Kaiber / Neural Frames / Veed lyric-video makers" with a small comparison table (free, local, word-accurate timing, agent-driven).
4. **Agent-native packaging**: ship as a Claude Code skill (+ optional MCP) so it lands in the "agent-skills / claude-code / hyperframes" topic searches; use those GitHub topics.
5. **Zero-install try path**: a `sample/` song with precomputed timing so people can render a reel without Suno or API keys.
6. **Launch assets**: a 30-60 s screen-capture video walkthrough (the creator-channel pattern), a short "how word timing works" diagram, a Show HN-style writeup. Posting is for the owner to do (we are not posting).
7. **Reels as marketing**: render the repo's own demo as a reel; opt-in outro "made with music-reels <repo>".
8. **Hygiene**: LICENSE, topics, issue templates, release tag, steady commits through launch week, optional Discord only if someone will staff it.
9. **Verify before relying**: star-history curves and actual launch channels for these repos are unverified here; another agent with web access should check star-history.com / HN for HyperFrames and OpenShorts.

## Update after rebase onto main 6daad3d (GUIDE.md and final video now exist)

Re-read GUIDE.md (390 lines), `songs/allow-always/`, `video/allow-always-final/` and `docs/runbooks/`. Nothing in the findings above depended on the old state, but the recommendations change in these ways:

- **We have a real demo.** `video/allow-always-final` (2:24 vertical, Suno song, HyperFrames, word- and beat-timed) is the "real output" asset recs 2 and 7 ask for. Next step is exporting a short GIF/MP4 for the README, not creating content.
- **GUIDE.md is the README's second act.** It is a build story with prompts, versions, dead ends and a repo map, which matches the tutorial-video pattern that carried ShortGPT and short-video-maker. Link it from the top of the README and keep the one-sentence promise and 3-command quickstart in the README itself.
- **Pinning is already good** (`hyperframes@0.9.2`, versions table). Gaps that still block "zero-install try" (rec 5): the two Python envs (`.venv` for librosa, `.venv-align` for whisperx/demucs) are only documented as pip commands, with no requirements files; no LICENSE file at repo root; and `video/assets/dev` is a symlink to `../../out/dev` (outside the repo), so a fresh clone may have broken assets. The finished `allow-always-final` reuses `video/data/allow-always-final.json`, so a no-API-key render of the shipped song looks feasible. I did not run a render to confirm that.
- **Skill/CLI still do not exist.** The workflow is a guide plus scripts (`scripts/timing.py`, `align_words.py`). Packaging it as a Claude Code skill remains the main viral-positioning step (rec 4), and the guide's section 9 (working with an agent) is the natural seed for the skill text.
- **Positioning sharpened:** the concept in GUIDE.md is "agent-built, human-directed". Lead with that: "I directed Claude Code to build a beat-synced music video; here is the full recipe".

## Launch-channel evidence (web search, standard mode, low authority)

- **MoneyPrinterTurbo:** [Trendshift](https://trendshift.io/repositories/8731) says it first hit #1 on GitHub Trending on 2024-03-28 (about 2.5 weeks after creation on 2024-03-11) and has stayed on trending lists. Aggregators (aitoolly, verdent, a Telegram "GitHub top repos" channel) repeat the trending claim. No HN or Reddit launch found. So the evidence points to **GitHub Trending plus aggregator/Telegram pickup, not a Show HN**.
- **OpenShorts:** a directory page ([openalternative.co](https://openalternative.co/openshorts)) is indexed under the "OpusClip alternative" tag and listed about 7.1k stars with ~1.4k gained in 30 days. A blog post says it reached news.hada.io (Korean tech aggregator); undated. Discovery path looks like **"X alternative" directories (openalternative, alternativeto) plus aggregators**. No HN/Reddit thread found.
- Caveat: these are directory/SEO pages that mostly repeat each other; I did not verify any star timestamps. Treat as hints, not causal proof.
- **Implication for music-reels:** get listed where "alternative to <paid lyric-video tool>" people look (openalternative, alternativeto), use "alternative" in the README and topics, and aim for a GitHub Trending day (a dense burst of stars in 24h matters more than a slow trickle). Posting is the owner's call.
