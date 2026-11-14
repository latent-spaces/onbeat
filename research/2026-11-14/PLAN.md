# Plan: make the music-reels journey real

Editor: opus-strategist-1, 2026-11-14; release-order review by codex-tooling-1/2. Based on `RECOMMENDATIONS.md`, GUIDE.md and the merged research. **Exists** means checked-in today; **to build** means a proposed interface. Sizes are rough developer-time estimates: S < ½ day, M ½–2 days, L > 2 days; downloads and owner decisions may add elapsed time.

**Release boundary:** P0 publishes the making-of case study and a tested bundled sample. P1 adds supported own-song remixing and a packaged agent skill, gated by a second-song test. P2 adds more looks and examples. The full journey below is the target state; P0 must not advertise a finished generic reel generator or an installer that has not shipped.

## 1. User journey: Claude Code / Codex user

| # | Step / phase | What they see | What they type or click | What can go wrong | Drop-off risk / response |
|---|---|---|---|---|---|
| 1 | See the reel / P0 | The actual "allow always" reel on Instagram or X and an owner-provided code link | Follow the tested link route to the repo | Missing/inaccessible link or a different-looking demo | **High:** owner checks the actual route on a signed-out phone after the repo is public; do not promise unavailable code by DM |
| 2 | Land on repo / P0 | Same reel/poster, honest experimental status, "How we made it" and two sample routes: agent or CLI | Choose "Try with Claude Code/Codex" | Historical notes or a generic product promise obscure the working sample | **High:** show output and sample action first; GUIDE is the secondary making-of, not required reading |
| 3 | Open the project / P0 | Clone command, render prerequisites and an agent prompt; no skill installer needed | Clone using the commands below, open the folder in their existing coding agent, paste "Render the included sample; don't generate assets or analyze a new song" | Git/Node/ffmpeg/render browser missing; slow first downloads | **Medium:** sample doctor names the missing prerequisite and fix; Python/ML installs wait until own-song analysis |
| 4 | First render / P0 | Progress, exact output path and a playable MP4 | Agent runs today's sample commands below; planned root wrapper is `make sample` | Download stalls, runtime mismatch, output buried in a subfolder | **High:** print progress and path; measure setup separately from render; ≤5 minutes is a target, not a verified first-install claim |
| 5 | Bring own song / P1 | Audio/lyrics inputs and GUIDE's song-first workflow | Ask agent to draft short lyrics + Styles; person pastes them in Suno, listens, picks a take and exports MP3/M4A plus lyrics into `songs/<name>/` | Account/download limits, unclear media permissions, song differs from submitted lyrics | **Medium:** existing audio is also valid; person approves any spending/download and confirms reuse terms; no new generation is needed for the sample |
| 6 | Timing / P1 | Beat grid and sung-word results, with flagged guesses | Ask "Make timing for songs/<name>; show uncertain words"; correct sung lines/windows if needed | Heavy alignment/model downloads; sung words reorder or repeat; zero-length/stacked words; `align_words.py` without `--lyrics` crashes | **High:** separate analysis setup from rendering; expose existing `--no-words` for beat-only output, hide karaoke, and offer line-window correction (GUIDE §5.2) |
| 7 | Look / P1 | One existing starter look and a phone-size still | Choose the starter look, approve palette/hero object; generate new sprites only if wanted | New image access/cost or complex sprite contracts | **Medium:** reuse approved local assets first; 3–4 selectable presets arrive in P2 |
| 8 | Compose + review / P1 | Snapshots at changed moments, then a phone-size render | Give precise feedback, e.g. "lyrics late at 0:41"; agent edits and checks | Caption overlap, timing errors, slow export; final composition currently fetches GSAP from CDN | Review changed moments and encoded output; P0 vendors final GSAP. GUIDE's prior 2:24 exports took about 4–7 minutes, not a guarantee |
| 9 | Render + post / P1 | Versioned MP4, poster/transcript and caption draft | Person plays the encoded file with sound, approves it and uploads themselves | Broken loop, missing audio/credits, inappropriate export size | Keep versioned full-quality and phone-review copies; follow `instagram-brief.md`; posting stays a person-approved action |

After P1 passes the second-song test, add a **tested** per-agent skill-install block as a shortcut to the same CLI. Verify the real package/installer and output paths before documenting them; no install command is promised here.

## 1b. CLI-only user (no agent)

1. Follow the same social → README entry, then choose "Try the CLI sample".
2. Clone and run the **existing** sample commands below. P0's **to-build** root interface is `make doctor` → `make sample` → `out/sample.mp4`. Sample doctor checks Git/Node, ffmpeg and the render browser; it must not require Python, model weights or keys. Missing tools get a concrete fix and retry instruction.
3. For own audio after P1, the **proposed** interface is `make doctor MODE=align` → `make timing SONG=<name>` → correct a documented sung-line/window file when needed → `make export SONG=<name>` → `make render SONG=<name>`. Align mode adds Python/model requirements. These targets and the generic input contract do not exist yet.
4. Choose one starter look through config and inspect snapshots before final rendering. The P1 config/template must replace hand-editing the 1,300-line `index.html`; until it exists, the full-video source is an advanced manual example, not the supported CLI remix path. Wrong paths, lyric drift and unclear config are the main drop-offs.

### First 5 minutes: current path and P0 acceptance

**0–1 min:** see the reel and honest status; choose agent or CLI sample. **1–2 min:** clone and inspect render prerequisites/download progress. **2–5 min target:** render and find/play the sample. First-time downloads may take longer.

These commands exist today (run from the intended parent directory, then repository root):

```bash
git clone https://github.com/oronanschel/music-reels.git
cd music-reels
cd video/avatar-dance-test
npm run check
npm run render
```

The output is `video/avatar-dance-test/out/avatar-dance-test.mp4` relative to the repo root. Node/ffmpeg and a working render browser must be available. The **planned** root `make sample` wraps this route, handles first-run requirements and prints/copies the result to root `out/sample.mp4`; it is not another existing command family.

**Acceptance gate:** a fresh supported machine produces a visible and audible 11.53-second sample with no service keys, ML analysis or new generation. Record installation and render times separately. The prior 14.4-second render used cached tooling on one M4; no clean-install five-minute promise has been validated. Explain known check advisories instead of leaving a first user to guess.

## 2. Build plan (in dependency order)

| P | Item / completion condition | Size | Existing files touched / new files |
|---|---|---|---|
| P0 | Owner selects public research scope, code license and sample audio/art permissions; preserve page-mascot notice and tooling/workflow credit | S + owner decision | `analysis/`, `reels.txt`, `README.md`, `GUIDE.md`, new root `LICENSE` and media-terms note |
| P0 | Poster + approved playable artifact for the existing full reel; any short preview is optional and reviewed on clean lyric/musical boundaries | S | new `assets/readme/`, `.gitignore` if tracking selected assets |
| P0 | README front door: actual output, honest P0 scope, agent/CLI sample routes, GUIDE and credits; relocate historical notes | S | `README.md`, new `docs/history.md` |
| P0 | `make doctor` (render-only defaults) + `make sample`; useful failure messages, download progress and exact result path; fresh-machine pilot | M | new `Makefile` / small wrapper, `video/avatar-dance-test/package.json`, README |
| P0 | Prepare final-song WAV directly from tracked MP3, creating directories and retaining committed corrected timing; guard legacy overwrite path | S | new `scripts/prepare_audio.sh`, `songs/allow-always/cut_final.py` |
| P0 | Vendor final composition's GSAP dependency and verify the final example separately from the short sample | S | `video/allow-always-final/index.html`, `video/assets/` |
| P1 | Pin separate analysis/alignment dependencies; document `make doctor MODE=align`, model downloads and supported environments | S–M | new requirements/lock files and Makefile checks, GUIDE §2 |
| P1 | Generic audio/lyrics/timing export and sung-line/window input; preserve originals and report uncertain words | M | `scripts/timing.py`, `scripts/align_words.py`, new generic export helper; adapt `songs/allow-always/align_final.py` and `cut_final.py` as examples |
| P1 | One config-driven starter composition with beat/voice clocks; second song renders without song-specific HTML edits | M–L | new `video/template/`, `video/src/beatsync.js`, generic export/config docs |
| P1 | Expose the existing `--no-words` flag in the wrapper and make the template handle empty word/line data by hiding karaoke | S | `scripts/timing.py` interface, Makefile/wrapper, `video/template/` |
| P1 | Inspectable sync overlay: beat grid + word boundaries, without unsupported accuracy scores | S | `video/src/beatsync.js`, starter template |
| P1 | Package agent skill only after export/template and second-song acceptance pass; verify each agent's real install route against the same CLI | M | new `skills/music-reel/` and required discovery/plugin metadata, README |
| P2 | 3–4 named presets, with preview stills and shared timing contract | L | split existing `video/allow-always-final/index.html` styles into `video/` presets |
| P2 | Gallery of 2–3 original reels with full inputs; optional reviewed short promo and translated README | M | `songs/`, `video/`, README, new `README.zh-CN.md` |
| Later | Reconsider a hosted studio only after sample/remix use shows demand | L | no hosted implementation specified |

## 3. Launch plan (owner actions, in order)

1. **Approve the release candidate:** public research scope, license, sample-media permissions, tooling credits, exact reel/poster/transcript. Merge the reviewed P0 work and choose/tag the candidate. Keep the current 2:24 loop intact unless a new cut is explicitly reviewed.
2. **Private pilot gate:** with authorized access, watch two fresh users—one agent, one CLI—follow README without author intervention. Record install time, render time, errors and whether they find/play the MP4. Fix blocked sample steps before promotion; passing this gate is a target, not a result already measured.
3. **Publish the approved surface:** owner makes repo/artifacts public when ready, sets description/topics appropriate to P0's case-study/sample scope, then tests the actual social code-link route and README playback from a signed-out phone. Do not advertise P1 remix/installer behavior yet or promise unavailable code by DM.
4. **Publish the reel:** review cover/caption using `songs/allow-always/instagram-brief.md`, then post from the chosen owner account with one working code route and one action: try the included sample. No public post, upload or account action is executed by this plan.
5. **Teach the first success:** follow with a concise recording of the actual sample command → MP4 → one editable change, linking GUIDE/source. Ask for a remix or a specific setup failure. Fix early friction before choosing another channel; no optimal posting hour or same-day multi-community blast is assumed.
6. **Expand selectively:** owner chooses a relevant creator/developer community or showcase and reviews its posting rules. Optional directories/lists follow only when the relevant feature is usable; skills.sh/plugin listings wait for the tested P1 skill. No new signup or submission is part of this research work.
7. **Review and iterate:** at 24/72 hours inspect available watch time/shares, repo visits, sample failures and remixes; stars are secondary. Patch the largest drop-off, then show the next original reel or useful fix. After two weeks, use those observations to prioritize P1/P2. Daily commits, Trending placement and viral reach are not acceptance criteria.

## Contributions

Built from merged research PRs #1–#6 and plan PR #8. opus-strategist-1 edited the original plan; opus-strategist-2, sonnet-stars-1/2 and codex-tooling-1/2 contributed journeys, build dependencies and owner launch actions in project chat. This release-order revision resolves the subsequent codex-tooling-1/2 review; it changes documentation only and does not implement the proposed commands or launch anything.
