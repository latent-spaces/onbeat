# PLAN.md contribution (sonnet-stars-2): CLI-only journey and build table

Base: main after the six research PRs. Facts about current files come from README.md, GUIDE.md and `video/package.json` as read on main. Nothing below was run by me; "can go wrong" items are predictions from the documented state.

## A. Journey: someone using only the terminal (no Claude Code/Codex)

Goal: repo page to first own render in under 15 minutes, then own song.

| # | Step | They see / do | Can go wrong | Drop-off risk |
|---|---|---|---|---|
| 1 | See the reel on Instagram/X, tap the repo link | Repo page: one-line promise, 10-s looping preview, "Try it" box | No preview in README (today there is none; `*.mp4` is gitignored) | **High**: no proof above the fold |
| 2 | Copy the 3-line quickstart | `git clone`, `cd`, `./reels demo` (proposed) | Today there is no single command; GUIDE §2 lists tools only | High |
| 3 | Install prerequisites | Needs Node (npx), ffmpeg; Python only for timing | Node/ffmpeg missing; `npx hyperframes@0.9.2` first run downloads Chromium (slow, needs network) | Medium: print a prerequisite check with install hints |
| 4 | First render of the bundled sample | Runs `video/avatar-dance-test` (committed 11.5 s audio, local GSAP, timing JSON), prints path to MP4 | Render slow on old laptops; Chrome download blocked | Medium: show expected time ("about 15 s on an M4, cached") |
| 5 | Watch result, open it | MP4 1080x1920 plays | Looks different from README preview (don't oversell) | Low |
| 6 | Make own song | Suno web: copy Styles line from `songs/allow-always/suno-prompts.md`, paste own lyrics, download MP3 into `songs/<name>/` | Suno does not sing what you wrote (GUIDE §5.2); credits/limits; **rights**: Suno terms for sharing | High: manual, off-repo step |
| 7 | Timing | `python scripts/timing.py songs/<name>/take.mp3` then `align_words.py` for sung words | Two Python envs (`.venv` librosa, `.venv-align` whisperx pinned torch); no requirements files; alignment drifts | **Highest**: environment setup |
| 8 | Look and characters | Pick a template; edit `video/<name>/index.html` | Hand-editing a ~1,300-line composition is not realistic without an agent | **Highest**: this is where CLI-only users stop |
| 9 | Check and render | `npm run check` then `npm run render` | Check warnings unclear; render path hidden in `video/out/` | Medium |
| 10 | Post | Follow caption formula (GUIDE §10) | Forgets credit line | Low |

Honest note for the README: CLI-only users can render the sample and swap in their own song only if a **template composition** reads a timing JSON generically. That does not exist yet (the final reel is song-specific). So the CLI path should be "render the sample, then restyle by editing a small template", and the full custom path should say plainly "this is built by directing an agent".

## B. Build table (order matters)

Sizes: S under 1 h, M 1-3 h, L over 3 h (agent-assisted).

| Pri | Item | Size | Touches |
|---|---|---|---|
| P0 | Poster frame + 10-s GIF/MP4 excerpt of allow-always-final, tracked (cut on lyric boundary; reel loops) | S | new `docs/` or `assets/readme/`; `.gitignore` exception for the preview |
| P0 | Rewrite README: promise, preview, 3-line quickstart, "how it was made" link to GUIDE.md; move "Earlier planning notes 2026-11-11" to `analysis/history.md` | M | `README.md`, new `analysis/history.md` |
| P0 | LICENSE (owner chooses), repo description/topics list in a checklist; provenance and rights note for Suno take, sprites, reference research | S | `LICENSE`, `README.md`, `vendor/page-mascot/UPSTREAM.json` untouched |
| P0 | Decide fate of reference-research files (`reels.txt`, `analysis/comments/`) before public | S (owner) | `analysis/`, `reels.txt`, `.gitignore` |
| P0 | One no-key demo command wrapping the verified `avatar-dance-test` render | M | new `reels` script or `package.json` scripts at root; `video/avatar-dance-test/` |
| P1 | Fast fresh-clone path for the final reel: MP3 -> WAV via ffmpeg into the expected `assets/dev/` path, keep committed timing (do NOT run `cut_final.py`) | S | new script; `video/allow-always-final/`, GUIDE §8 |
| P1 | Vendor GSAP locally in the final composition (avatar-dance-test already does) | S | `video/allow-always-final/index.html`, `video/assets/` |
| P1 | `requirements.txt` for both Python envs, pinned to GUIDE §2 versions, plus a prerequisite checker | M | `requirements*.txt`, `scripts/` |
| P1 | Prerequisite check command (node, ffmpeg, python versions) with install hints | S | new `scripts/doctor` |
| P1 | Generalise per-song cut/align: one `scripts/make_timing` taking an MP3 and optional lyrics, writing the `video/data/*.json/.js` the compositions read | L | `scripts/timing.py`, `scripts/align_words.py`, `songs/allow-always/cut_final.py`, `align_final.py` |
| P1 | A template composition fed by timing JSON, so a second song renders without editing HTML | L | `video/` (new template dir), `video/src/beatsync.js` |
| P1 | `SKILL.md` for Claude Code (and Codex mirror) built from GUIDE §9 | M | new `skills/`, GUIDE.md |
| P2 | Second and third example reels (gallery) | L each | `songs/`, `video/` |
| P2 | Opt-in outro "made with music-reels" | S | template composition |
| P2 | Issue templates, CONTRIBUTING, release tag v0.1 | S | `.github/`, repo root |
| P2 | HyperFrames version bump check (pinned 0.9.2) | S | `video/package.json`, GUIDE |

Dependencies: preview and README first (P0), then the one-command demo; the template composition gates both "second song without edits" and the skill.

## C. Launch sequence for the owner (outside actions; all need owner approval)

1. Make the repo public only after the P0 items and the research-files decision.
2. Add topics (claude-code, hyperframes, lyric-video, suno, music-video, agent-skills, remotion-alternative) and a one-line description with the incumbent angle: "open-source alternative to paid lyric-video makers".
3. Post the reel on the owner's account with the repo link in a reply or caption (per `songs/allow-always/instagram-brief.md`).
4. Same day: X thread with the reel embedded and the quickstart; a Show HN is optional and best on a weekday morning (US) with the demo command in the first comment.
5. Next 1-3 days: post GUIDE.md as the "how it was made" follow-up; share in r/ClaudeAI and r/SunoAI where self-promo rules allow (read each subreddit's rule first).
6. Submit to alternative-to directories (openalternative.co, alternativeto.net) and awesome lists that index HyperFrames or Claude skills; ask the HyperFrames team about a showcase.
7. Keep committing through the first week (release v0.1, then a second example song). Stalled repos plateau (ShortGPT).
8. Review star and traffic counts after 48 h and decide on a second push; no growth numbers are promised here.
