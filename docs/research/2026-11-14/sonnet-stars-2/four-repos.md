# Owner's four repos: MoneyPrinterTurbo and CogVideo (sonnet-stars-2)

Split in chat: sonnet-stars-1 covers Pixelle-Video and page-mascot (license and credit); I cover MoneyPrinterTurbo and CogVideo. Data read 2026-11-14 via `gh api`, READMEs, and [Trendshift](https://trendshift.io/repositories/8731). Star-timestamp API was unavailable (404), so growth rates come from Trendshift's 61-day window and created dates.

## 1. harry0703/MoneyPrinterTurbo

- **Numbers:** 143.4k stars, 23k forks, created 2024-03-11, MIT, 23 releases (latest v1.3.10, 2026-11-07), pushed 2026-11-13. About 20 months old: roughly 7k stars/month average.
- **Speed:** Trendshift shows GitHub Trending #1 on **13 separate days** since tracking began 2024-03-22, with the first #1 on 2024-03-28 (17 days after creation). Over Sep 15 - Nov 14 2026 it still gained **+19.7k stars** (+4.3k forks, 329 merged PRs), with spikes of +845 (Nov 5), +807 (Nov 3), +683 (Oct 15). So growth is not a one-off launch spike: it keeps re-trending (top-25 Python list almost daily) because the project ships constantly.
- **What it is:** a **studio-style app** (Streamlit WebUI + REST API), not a skill or CLI. Topic or keyword in; LLM script, stock footage, TTS, subtitles, BGM, ffmpeg render out.
- **README/demo:** title, one-sentence promise (topic -> HD short video), badges (version, platforms, Python, downloads, Trendshift, Star History rank), then **WebUI and API screenshots** before anything else. Chinese-first with English and Japanese READMEs. Sponsor block (LLM and API vendors with referral links) sits right after the screenshots. Releases with downloadable Windows/macOS packages.
- **How it launched (evidence is thin):** GitHub Trending, then aggregators and Telegram channels; no HN/Reddit launch found. Chinese developer audience and LLM-API sponsors amplified it.
- **Primary-source correction (from codex-tooling-2, PR #6):** the day-one README (2024-03-11, 06df797) already put portrait/landscape demo videos and image previews before install, and linked a Douyin usage tutorial; later READMEs add Windows tutorials and the author's Douyin/WeChat-video channels. So a creator-channel tutorial existed from the start, not only trending pickup. Star causality is still unproven.
- **Copy:** one-sentence outcome; UI screenshot first; release cadence and a changelog (keeps re-trending); multilingual README; a no-code WebUI path; tagged releases with downloads; badges including Trendshift.
- **Avoid:** sponsor banners above the pitch (works at 143k, would look spammy at 0); "money printer" naming that attracts spam-content association; heavy dependence on stock footage (our outputs are original, which is a differentiator).

## 2. zai-org/CogVideo (CogVideoX)

- **Numbers:** 13.2k stars, 1.4k forks, created 2022-05-29, Apache-2.0, one release, last push 2025-11-04. Stalled since; the stars came mostly from the 2024 CogVideoX releases (2B on 2024-08-06, 5B on 2024-08-27, I2V 2024-09-19, 1.5 on 2024-11-08).
- **What it is:** an **open-weights research model** (text/image-to-video), plus inference and LoRA fine-tune code. Not a studio, skill or CLI. It matters to us only as an upstream option for generated footage.
- **README/demo:** logo, a "try online" line first (Hugging Face and ModelScope Spaces), paper link, WeChat/Discord, a long dated "Project Updates" log, hardware notes (runs on RTX 3060 / GTX 1080 Ti for the small models). The Space demo is the zero-install try path.
- **How it launched:** academic path: arXiv paper, institutional (Zhipu AI / Tsinghua) brand, Hugging Face model release, free web demo, and a commercial sibling (QingYing). Stars follow model drops, not README polish.
- **Copy:** a one-click hosted demo and a dated news log that shows momentum; a "runs on consumer hardware" claim.
- **Avoid:** copying its shape: model repos win on research credibility, which we lack. Do not add a heavy GPU video model dependency; our pipeline's selling point is deterministic, code-drawn frames that sync to measured beats, and generative video would blur that.

## 3. Pixelle-Video (only quick numbers; sonnet-stars-1 owns the full note)

30.1k stars, 4.4k forks, created 2025-11-07 (so about 30k in 12 months), Apache-2.0, 12 releases through 2026-01-27, pushed 2026-06-14. README: demo video at top, WebUI screenshot, dated changelog, feature checklist, flow diagram, Bilibili video tutorial, Windows bundle. Same family as MoneyPrinterTurbo (topic -> short video).

## What this adds to the recommendations

1. **Keep shipping**: MoneyPrinterTurbo's lasting rank comes from releases and merged PRs, not a one-time launch. Plan weekly tagged releases or new example songs after going public.
2. **Screenshot/GIF first, sponsors never first.**
3. **A zero-install demo path** (CogVideo's hosted Space; for us, a committed sample MP3 and a short render).
4. **Differentiate against "topic -> stock-footage video"**: ours is song -> beat/word-timed original animation. Say so in the first line.
5. **Credit and license hygiene** (LICENSE file, attribution for vendored avatars) matters more once the repo is public. See sonnet-stars-1's page-mascot note.
