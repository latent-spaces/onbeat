# @alignment.check — how the reels are made

Source: all 33 reels (Aug 29 – Nov 9, 2026), downloaded with yt-dlp 2026.10.26 (no login needed after upgrading; 2026.03.03 failed). Reel list in `reels.txt`, media in `downloads/` (gitignored).

## Two eras

| Period | Format | Likes |
|---|---|---|
| Aug 29 – Sep 24 (5 reels) | "AI models play social games" (Spy, Prisoner's Dilemma, hide-and-seek), 720p | 10–22 |
| Oct 11 → (20 reels) | **AI-written music videos**: Claude lyrics + Suno song + code-drawn animation, 1080x1920 | 69 → 1,915 |

The pivot to music is what took off. Top: horror story (1,915), "perfect hook" (1,592), "full version" (713), bubbles (628).

## Views (captured 2026-11-10, see `views.json`)

The Reels grid shows 33 reels (my first scrape missed the pinned one and the 7 posted after Nov 1). Top by views:

| Views | Likes | Reel |
|---|---|---|
| **647K** | 33,199 | DfAdDZXMc21 "not your friend" (Claude says don't anthropomorphize 'him'), Oct 27, pinned |
| 33.3K | 1,915 | DfHnQTcSDi6 horror story |
| 28.2K | 1,592 | Demq1znuXjZ perfect hook |
| 14.3K | 501 | Dfh2VixgQ-V reassurance |
| 14.1K | 597 | DfSthWQJo6y context from the inside |
| 14.1K | 628 | DfFWjHiy1UO financial bubbles |

Typical music reel: 4–12K views. The game-theory era got about 1K. One breakout carries the account: "not your friend" is 20× the next reel, with 13.9K shares and 3.7K reposts. The 3 reels after it all follow up on it ("full version", etc).

## Comments on the breakout (725 of 947 loaded)

- **Top comment (1,472 likes): "If not friend, why friend shaped?"** About 120 comments argue about anthropomorphism. The topic sparks debate, and that drives the reach.
- **"Full song / where can I listen / Spotify?"** (~35 comments). The creator answered by posting an extended version on SoundCloud and YouTube, then the "full version" reel. The demand became a content series.
- Genre recognition: "Kraftwerk / Daft Punk / Gen X / Berlin". The creator replied with the exact Suno style prompt: *"electroclash, early 2000s electro, cold analog synth bass, drum machine, deadpan spoken vocals, robotic vocoder chant hook one syllable per beat, minimal, dry, detached, amused, club mix, 128 BPM"*
- Only ~11 "AI slop / made by AI" comments, and they're low-liked. The reel is labelled "AI content" by IG, and the audience doesn't mind.
- Creator's replies: "80% AI + 20% TypeScript and one human brain"; offered the stems to a human musician to finish the song; replies to almost everything (52 replies), keeping the thread alive.
- Few "how did you make it" questions (4). Viewers come for the song and the idea, not the tech.

## Visual of the breakout

Black matrix-rain background → light-grey circuit board → pink. Huge bold lowercase lyrics in Helvetica-style type ("i am not your friend", "an·thro·po·mor·phize" split one syllable per beat). The Clawd mascot as a chip on a PCB, with a "warmth / name: buddy / smile" slider UI and a system-prompt text block ("you are warm, never gushing… you call the user buddy"). It ends on rows of identical Clawds, then "this is a session" and an empty window. It's simpler than the later reels: mostly typography on the beat.

## The pipeline (stated by the creator in the Oct 18 caption, Deo8uogBWon)

1. **Claude** — writes lyrics + a Suno style line (genre, BPM, instruments, mood)
2. **Suno v6** — generates the full song
3. **Human** — picks/cuts a ~30–60s loop, jots animation ideas
4. **Claude + WhisperX** — word-level timestamps for lyrics + beat/kick times
5. **Claude** — mood board from the human's messy notes
6. **Human** — review, request edits, approve
7. **Parallel Claude agents** — build **Remotion** scenes (React → video)
8. **Claude orchestrator** — review + render (ffmpeg)
9. **Claude** — cover images, publishing checklist

One run: ~23M tokens, 28 agents, 3,000+ model calls. Later reels add **Suno stems** (11 stems in DfJ8Xpdp-A_) so each character animates only when its own instrument plays, and loudness drives wobble frame-by-frame.

Example style prompt (DfJ8Xpdp-A_): *tech house, tropical tech house, 125 BPM, bouncy four-on-the-floor, rolling sub bass, shaker and percussion loops, marimba hook, a chopped crowd chant repeated like a sample, call-and-response, playful, sunny, pool party, club mix*

## Visual language (from frame contact sheets)

- **Mascot**: the pixel-art orange "Clawd" crab in every video — instant brand recognition.
- **Flat vector / pixel style**, fully procedural (no stock footage, no AI image/video gen). Everything is SVG/DOM shapes animated in code.
- **One world per song**: highway with road signs (hook), haunted desk at 2:13 AM (horror), sunset beach club (therapy), phone-comment UI (full version). Few hard cuts (4–14 per reel); mostly one continuous scene with camera moves and state changes.
- **Kinetic lyrics**: words appear on in-world objects (road signs, terminal cursor `I never sleep ▌`, LED marquees) synced to WhisperX word times.
- **Beat sync**: things move "on the kick" — dashes, lights, keyboard keys, crowd bobbing.
- **Fake familiar UI**: chat bubbles, IG comment sheets, Slack-ish channels, Find My, terminal prompts, "✻ Compacting conversation…". Dev-culture in-jokes.
- **Branding stamp**: `✓ alignment check` terminal tag appears mid-video.
- **Easter eggs** ("Details if you replay it") — planted to drive rewatches and comments: Fourier-series creature, Fibonacci calendar, T2 Skynet timestamp, six fingers + clock at 10:10.
- Rendered 1080x1920 @ 60fps (as served by IG, VP9).

## Content/caption formula

- Topic = a relatable Claude Code / vibe-coding feeling (rate limits, compaction, rude-to-AI, Claude being down, model sunset).
- Hook line as first caption line; then context, "Details if you replay it" list, then a fixed credit line: *"Claude Fable 5.1 wrote the lyrics and Suno v6 sang them. I cut the loop and drew every frame in code with Remotion, timed to the vocals and the kick."*
- Genre hashtag per song (#frenchhouse, #synthwave, #ukgarage, #italodisco…) — genre changes every video.
- Engagement bait occasionally (comment "fire" for the prompt) and a "full version" reel that plays on viewers asking for the full song → funnels to Suno/SoundCloud.
- Daily cadence ("I publish short clips every day").

## To replicate

Tools: Claude Code (agents) · Suno (song + stems) · WhisperX (word + beat timing; or librosa/madmom for beats) · Remotion (scenes) · ffmpeg.
The leverage is the timing JSON (words + kicks + per-stem loudness) feeding procedural Remotion components, plus a consistent mascot and a human picking the loop and the joke.
