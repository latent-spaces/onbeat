# DfLk4XOhe1y — "fine. the full version." follow-up (10.7K views)

Legend: **[M]** measured by a script in `diagnostics/setA/`, **[E]** eyeballed from contact sheets / 1 fps frames / 20 fps hook sheet, **[I]** inferred.
Lyrics are not transcribed; on-screen phrases quoted only as 2-4 word identifiers.
Artefacts: `downloads/frames/DfLk4XOhe1y/`.

## Summary

A sequel to the breakout (DfAdDZXMc21): a phone on a desk replays the original reel, the comment sheet slides up with recreations of the real top comments ("full version where", the friend-shaped joke, slop vs banger), the viewer types a request for the full version, the creator "is typing" with a progress bar that fills through the breakdown, and the reply on the drop is the SoundCloud free download (CC) with an "extended tracks" playlist. It turns comment demand into the content.

| | |
|---|---|
| Length | 37.151 s [M] |
| BPM | 129.252 [M] (period 464.21 ms) — within 0.13% of DfAd's 129.082 |
| Bars | 20 bars exactly: 80.086 beats, seam +40 ms (part may be AAC padding) [M]; downbeat k≡0 at 0.037 s [M] |
| Genre feel | Same electroclash song family as DfAd [I]: chroma of every 4 s window matches somewhere in DfAd at cos 0.75-0.95 [M xsong.py], consistent with the same song in a different (extended / club) arrangement, but not proof |

## Hook (0-3 s) [E hook sheet, times M]

| time | on screen |
|---|---|
| 0.00-0.20 | Top-down desk: cream surface (#fcedcc / #e8ddc9) with a diagonal shadow, wall tiles and an outlet (#f3efe8), a coffee cup, a toaster-like device top right; a black phone (#0b0d11) shows DfAd's opening frame — unlit grey mascot on matrix rain; a cartoon hand's finger is on the screen [E]. |
| 0.200 | First event (+9.7 f) [M]: the tap. |
| ~0.23-0.27 | On the phone, the mascot turns orange and "i am not" appears — the DfAd hook replayed at DfAd's own timing [E, cf. DfAd 0.233/0.267]. |
| 0.30-0.50 | Hand slides out bottom-right (eased) [E]. |
| ~1.1-1.2 | "your friend" lands on the phone [E]. |
| ~2.1 | Phone shows DfAd's grey circuit scene [E]. |

First text: the replayed DfAd lyric at ~0.27 s (small, inside the phone). First motion: the hand, from frame 0.

## Timeline

Bar n starts at 0.037 + 1.8568·n s.

| time range | bars | scene / background | text treatment | what moves on what rhythmic unit |
|---|---|---|---|---|
| 0.00-3.75 | 0-1 | Desk, phone small in frame, replaying DfAd. Fake IG side rail with likes ~84K and comments ~1.2K ticking up [E]. | DfAd's text inside the phone. | Like counter increments [E]. |
| 3.75-5.82 | 2-3 | 3.750 (beat 8 = bar 2, +0.0 f) camera zooms in so the phone fills the frame [M/E]. | | Zoom on the bar line. |
| 5.82-14.89 | 3-7 | 5.817 (+12.5 f, off-beat) comment sheet slides up over the lower half [M/E]: four mock comments with like counts recreating real top-comment themes [E]; DfAd's syllable stack keeps playing above. 7.367 (-5.8 f) keyboard rises; a reply ("seriously, where...") is typed letter by letter, then sent [E]. | System sans, comment layout; typing with caret. | Typing on vocal-ish rhythm [E]; events off-grid [M]. |
| 14.89-29.75 | 8-15 | **Low/kick out from beat 32 (14.89 s) to beat 64 (29.75 s)**, 8 bars [M]. The sent comment sits pinned with its like count rising quickly; "alignment.check is typing" with animated dots; ~22.5 s a segmented progress bar appears under it and fills until ~29.5 s [E]; meanwhile DfAd's middle scenes (settings card, pink system prompt, 2x2 object tiles, concentric squares) play in the phone [E]. | Comment UI. | Progress bar = the riser: it completes on the drop [E/I]. Like counts climb continuously [E]. |
| 29.75-34.0 | 16-18 | Low re-enters +30 dB at beat 64 [M]. Full-phone reply screen: black #111317 with flashing pink/purple/blue/white pixel squares (#d52c77, #8a4bb1, #5a6bb5, #fdfdfe) [M palette], "alignment check replied", big bold white "soundcloud" and lines added one by one ("download for free.", "play it.", "own it (CC)"), then a tilted pink sticker [E]. | Heavy bold sans, line-by-line append. | **Pixel squares re-randomize on every beat: events at beats 65-71 (30.217-33.000), all -0.3..+0.6 f** [M]. Lines append on vocal [E]. |
| 34.0-37.15 | 18-19 | SoundCloud-style playlist screen "extended tracks" with four tracks and a mini-player [E]; loops to the desk [I]. | List UI. | — |

## Visual system

- **Palette [M]:** desk cream #fcedcc / #e8ddc9 / #f3efe8; phone black #0b0d11 / #1a1a1c / #111317; screen white #fdfdfd; grey #ccd3d4; reply squares pink #d52c77, purple #8a4bb1, blue #5a6bb5; inside the phone, DfAd's own palette.
- **Typography [E]:** platform-like UI sans for comments and keyboard; heavy bold sans for the reply screen; DfAd's lyric typography inside the phone.
- **Layout [E]:** phone centred; after the zoom it fills ~85% of the frame; comment sheet on the lower ~55%; inner video upper ~45%.
- **Mascot:** only inside the replayed video, plus as the creator avatar in comments.
- **Background:** flat-illustration desk with hard diagonal shadow; the "content" is a phone UI mock (not the real app).
- **UI elements:** fake reel side rail (likes, comments), comment sheet, keyboard, typing indicator, progress bar, reply notification, playlist.
- **Camera:** one zoom-in at bar 2; otherwise locked [E].
- **Transitions:** sheet slide-up, keyboard slide-up, full-screen swap to reply, swap to playlist.

## Motion vocabulary

| primitive | trigger | easing / duration |
|---|---|---|
| Cartoon hand tap + exit | start | ~0.3 s ease-out [E] |
| Camera zoom to phone | bar line (beat 8) [M] | eased ~0.5 s [E] |
| Bottom-sheet slide-up / keyboard slide-up | phrase (off-beat) [M] | iOS-like ease ~0.25-0.3 s [E] |
| Typing with caret | per letter [E] | ~2-4 frames per char (not measured) |
| Counter tick-up (likes / comment count) | continuous [E] | integer steps |
| Typing dots | loop [E] | ~3-phase cycle |
| Progress bar fill | build section; completes on the drop [E/I] | segmented, ~linear over ~7 s |
| Pixel-square randomize | every beat after the drop [M] | instant |
| Line-by-line append | vocal [E] | instant pop |

## Audio structure [M]

- 129.252 BPM, phase 0.0373 s, downbeat k≡0.
- Groove from the start; kick/low out for 8 bars (beats 32-64, 14.89-29.75 s); +30 dB re-entry at 29.75 s.
- 20 bars exactly (80.086 beats); first/last 2 bars chroma cos 0.988 — near-identical ends [M]; tail last 50 ms -29.9 dB [M] (mild fade or encoder padding).

## Sync evidence [M, sync2.py]

| measure | value | chance |
|---|---|---|
| visual onsets | 39 | |
| within 1 f of a beat | 38.5% | 10.8% |
| within 1 f of a half-beat | 38.5% | 21.5% |
| within 1 f of a 16th | 56.4% | 43.1% |
| strong-half events on a beat | 65.0% (n=20) | |
| per-beat pixel-square events after the drop | 7 of 7 within -0.3..+0.6 f | |

This is the least beat-locked reel: most motion is UI (typing, sliding sheets) on human/vocal timing, and the inner phone video carries DfAd's own sync at a small scale [I]. The beat-locking is saved for the drop.

## How to rebuild it (Remotion)

| component | props | driven by |
|---|---|---|
| `<Desk>` + `<Phone zoom>` | zoom 0->1 | `bars[2]` |
| `<PhoneVideo src=DfAd render>` | `startFrom` | plays the earlier composition inside the phone (`<OffthreadVideo>` or re-render the DfAd composition as a child) |
| `<ReelRail likes comments>` | rising counts | frame-driven counter |
| `<CommentSheet comments[]>` | slide-up time | phrase |
| `<Keyboard>` + `<TypedComment text>` | chars/sec | phrase |
| `<TypingIndicator>` + `<ProgressBar>` | `from`, `to` | `to` = drop time (`beats[64]`) |
| `<ReplyScreen lines[]>` + `<PixelSquares>` | seed | `beats[]` after the drop; lines on `words[]` |
| `<PlaylistScreen tracks[]>` | | last section |

## Why it works

1. **It answers the crowd.** The original's comments asked for the full song again and again; this reel stages that exact exchange and ends on the download [M caption "fine. the full version." + links]. Top comments are gratitude: "YES!! Full Version!" (27 likes), "put it on youtube" (18) [M].
2. **Familiarity:** it reuses DfAd's frames and song, so it rides recognition for people who saw the hit [I].
3. **Built-in build/drop:** the "is typing" progress bar is a riser that completes on the kick's return [E/M], so the payoff (download screen) lands on the drop.
4. **Limits [I]:** it is a service post for existing fans; its views (10.7K) are typical of the account's non-breakout reels, not of the hit.
