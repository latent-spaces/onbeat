# DfHnQTcSDi6 — "2 AM" horror reel (33.3K views, #2 performer)

Legend: **[M]** measured by script (diagnostics/setB/*), **[E]** eyeballed from contact sheets / full frames, **[I]** inferred (interpretation, not measured).
Lyrics are not transcribed here; on-screen phrases are quoted only as 2-4 word identifiers.

## Summary

A Halloween horror story told through a 2 AM home-office desk: the small Clawd says it never sleeps while, app by app, the monitor shows traces of a much bigger hidden Clawd (memories, Slack, smart-lock, Find My), until the big one is revealed, the scene drops into a "cemetery desktop", and a typed punchline undoes the scare. It is a narrative reveal, not a list/explainer like the other four.

| | |
|---|---|
| Length | 61.00 s [M] (60 fps, 1080x1920, VP9/AAC) |
| BPM | 99.975 [M] (kick-attack linear fit on demucs drum stem; beat = 0.60015 s = 36.0 frames; bar = 2.400 s = 144 frames) |
| Bars | ~24.7 bars after the first inferred downbeat (1.6365 s) + a 1.64 s pickup [M]; downbeat phase is [I] (chroma novelty) |
| Genre | Synthwave / darkwave, four-on-the-floor (91.6% of drum-stem kicks on the beat) [M]; caption tag #synthwave [M]; commenters say "Front Line Assembly" [M] |

## Hook (0-3 s), frame by frame

| frame / time | what is on screen | source |
|---|---|---|
| f0 (0.000) | Monitor content flashes near-white (screen-wide wash ~#dfe6f7) with a black crab silhouette, grey shadow of a big Clawd and a curtain: a one-frame "jump-scare" flash. | [E] |
| f1-f2 (0.017-0.033) | Flash collapses to the normal dark desk; frame diff jumps 0.26 -> 3.41 (f2) -> 4.6-4.9 (f3-f4) [M]. First text already present: the terminal line at the bottom of the monitor shows the first word in bright white. | [M]/[E] |
| f3-f9 (0.05-0.15) | Monitor gradient settles to blue; above-threshold change every frame f3-f9 (settle animation, ~7 frames) [M]. | [M] |
| 0.38 s | First motion onset after the settle [M]; second word lights (karaoke). | [M]/[E] |
| 0.90-0.98 s | Third word lights; motion onsets at 0.900 and 0.983 [M]. | [M] |
| 1.42-1.57 s | Onsets [M]; keyboard key-lights step. | [M]/[E] |
| ~2.0 s | Monitor dims blue -> dark (vocal phrase is over; bar 1 is a vocal-silent bar, vocals stem -71 dB) [M]. Line greys out, block cursor blinks. | [M]/[E] |
| 2.18, 2.42, 2.78 s | Onsets: LED strip/keys stepping on beats [M]/[E]. | |

First text: frame 1 (0.017 s) [E]. First motion: frame 2-3 (diff 3.4-4.6, the flash recovery) [M]. Audio starts at sample 0 with vocals at 0.07 s [M]; there is no silent lead-in.

The hook is: a one-frame white flash + the line "I never sleep"-style claim typed karaoke-style on a terminal, inside a cosy-but-creepy scene full of small details (pumpkin with glowing eyes, red 7-segment clock reading 2:13, Finder menu bar "Fri Oct 31 2:13 AM") [E]. Nothing on screen is big or fast; the hook is the *mood and the claim*, not motion.

## Timeline

Bar index = stems.json bar rows (row 0 = 0-1.64 s pickup; row k starts at 1.6365 + 2.4·(k-1) s). Vocal level per row from the demucs vocal stem [M].

| time range | bars | scene / background | text treatment | what moves on what rhythmic unit |
|---|---|---|---|---|
| 0.00-4.27 | 0-1 | Wide desk at night: navy wall panels, blinds left, shelf right, lamp, plant, pumpkin, red clock "2:13", keyboard with blue keys, glass of water. Monitor shows small Clawd in a cracked robot-skull helmet (red eye) with a large dark-navy Clawd silhouette behind it. [E] | Terminal bar at bottom of the monitor: bold monospace, current word white, past words grey, white block cursor. [E] | Words on vocal timing; keyboard key-lights + ceiling LED dots step on beats [E]; motion onsets 45% within ±1 f of a beat overall [M]. Bar 1: vocals silent (-71 dB) [M], screen dims [E]. |
| 4.27-9.65 | 2-3 | Camera push-in on monitor: Photos-style "memory" card ("3 years ago") [E]. | Same terminal karaoke line. | Cut at 4.267 s [M] = vocal phrase start 4.26 [M]. Bar 3 vocal-silent (-73 dB) [M]. |
| 9.65-14.47 | 4-5 | Slack-style #general message at 1:55 AM, "sent via @claude", typing indicator [E]. | same | Cut 9.650 [M] = phrase 9.66 [M]. |
| 14.47-19.25 | 6-7 | Home-app "Server room" lock tile, Locked [E]. | same | Cut 14.467 [M] = phrase 14.45 [M]. |
| 19.25-24.07 | 8-9 | Contacts list scroll + Find My "Home office" [E]. | same | Cut 19.250 [M] = phrase 19.26 [M]. |
| 24.07-28.87 | 10-11 | Pull back to wide desk; desktop wallpaper now a cemetery/trees silhouette [E]. | same | Cut 24.067 [M] = phrase 24.07 [M]. |
| 28.87-32.47 | 12-13 | Big orange Clawd revealed on the monitor; screen brightens [E]. | same | Cut 28.867 [M] = phrase 28.87 [M]. |
| 32.47-38.43 | 14-15 | Breakdown (bar 14: drums -22.6 dB vs -18, bass -28.8 vs -22, vocals -79) [M]. Green "✓ alignment check" terminal tag ~34.5 s [E]; fast camera push into the big Clawd's eye 36-38 s until the frame is orange (#db7758 = 25% of pixels at 37.5 s) [M]. | Terminal line idle | Cut 32.467 [M]; the eye push is a continuous zoom across ~2 s (≈3.3 beats), not stepped [E]. |
| 38.43-54.0 | 16-22 | Drop / hook section (bars 16-21 louder, vocal continuous) [M]. "Cemetery desktop": tombstones are grey skeleton-screen file icons (node_modules, Final_v3, IMG_xxxx.HEIC, a 2016 pdf...), a ghost carries an email subject, bats carry notification pills (Storage almost full, Unread 4,312, Low battery 1%...), loading spinner, small Clawd in the middle; ~51.5 s a swarm of orange Clawds [E]. Palette shifts to near-black navy #060b17-#121826 [M]. | Lyric moves to centered top, monospace [E]. Three black interstitial cards with a huge helmeted Clawd and "(just kidding)" in a thin rounded font [E]. | Cards: in at 40.217 / 45.050 / 49.817, out at 41.067 / 45.850 / 50.667 [M] → 0.80-0.85 s each (≈1.4 beats), spaced exactly ~2 bars (4.83 s, 4.77 s) [M]. |
| 54.0-57.5 | 23 | Drums drop to -50 dB [M]. Zoom out *through* the crab's eye back to the desk monitor (match cut) [E]. | — | Continuous zoom [E]. |
| 57.5-61.0 | 24-25 | Desk; terminal types the punchline; the big Clawd climbs out of the monitor onto the desk [E]. Tail fades (row 25 vocals -85, bass -52) [M]. | Typewriter in terminal [E]. | Ends on the desk = near-loop to frame 0 [E]; audio last-bar-vs-first mel corr 0.655 (not a seamless audio loop) [M]. |

## Visual system

- **Palette [M]** (median-cut on 270x480 frames; % = share of pixels):
  - Desk scenes (t=1, 10.5, 30 s): #191b25 (~22%), #04060a (14%), #0e1320 (11%), #27344a / #293953 (wall-panel navy, 8-12%), #20222a.
  - Eye push (37.5 s): Clawd orange **#db7758** 25%, #17223a 18%.
  - Cemetery (40.5-52 s): #060b17 / #070b17 (30-35%), #121826 (26-28%), #0d1223 (15%), grey tombstones #2c3543 / #333c4b, bone-grey #8997a1 on the interstitial Clawd.
  - Accents [E]: red 7-seg clock, green ✓ tag, white terminal text, blue key LEDs.
- **Typography [E]:** bold monospace (JetBrains Mono-like) for the terminal lyric; thin rounded sans for "(just kidding)"; system-UI sans for the fake app cards (Photos, Slack, Home, Contacts).
- **Layout [E]:** the monitor is the stage (roughly the middle 55% of the frame, x≈10-90%); the lyric lives in a terminal strip at the bottom edge of the monitor (lyric band detected at y≈1210-1430 px [M, wordsync.py]); room props frame it.
- **Mascot [E]:** two Clawds. Small one: wears a cracked robot-skull helmet (red eye + one checkered eye). Big one: dark-navy silhouette at first, then full orange. The story is "small mascot hides big mascot".
- **Background [E]:** static illustrated room; lighting changes come from the monitor glow (dims in vocal-silent bars).
- **UI [E]:** a faithful-looking fake macOS layer: menu bar with date, then app cards. In the second half the "desktop" becomes a graveyard made of skeleton-screen placeholders and notification pills.
- **Camera [E]:** slow push-in on the monitor at each phrase, pull-back at bar 10, a long push into the eye (36-38 s), and a reverse zoom out of the eye (54-57 s). Camera moves are the main motion in this reel.
- **Transitions:** hard cuts on vocal phrase starts (15 cuts, 0 on the beat grid) [M]; 2 zoom-through transitions (into eye, out of eye) [E]; 3 black interstitial cards [M].

## Motion vocabulary

| primitive | trigger | easing | duration |
|---|---|---|---|
| Screen flash (white wash then settle) | frame 0 / scene start | instant on, ~2-frame decay [M diff] | 1 frame peak, ~7 frames settle [M] |
| Karaoke word light (white current, grey past) | each sung word start | step (no tween seen at 20 fps) [E] | holds until next word [E] |
| Line grey-out + cursor blink | vocal-silent bar | fade [E] | ~1 beat fade [E]; cursor blink period not measured |
| Phrase cut + push-in | vocal phrase start (every 2 bars) | ease-out zoom [E] | cut instant; push lasts the phrase [E] |
| Monitor dim/brighten | vocal on/off per bar | ease [E] | ~1 beat [E] |
| Key-light / LED stepping | beat (kick) | step [E] | 1 beat [E] |
| Long push-in into eye | section boundary (pre-drop) | ease-in (accelerating) [E] | ~2 s ≈ 3.3 beats [E] |
| Interstitial card ("just kidding") | vocal phrase in the drop | hard cut in/out [M] | 0.80-0.85 s [M] |
| Swarm (many Clawds) | late drop | linear drift [E] | ~2.5 s [E] |
| Zoom-out through eye (match cut) | bar 23 (drums out) | ease-out [E] | ~3 s [E] |
| Mascot emerges from monitor | final phrase | ease-out [E] | ~2 s [E] |

## Audio structure [M unless marked]

- 99.975 BPM, four-on-the-floor kick (drum-stem 16th histogram: 22/21/21/24 on the four beats, near-zero elsewhere); snare/hat detector also on the beats (21/21/20/24).
- **Call-and-silence vocal layout:** vocals sit in even rows 0,2,4,...,12 (≈-28 dB) and are absent in odd rows 1,3,...,13 (-48 to -76 dB). So every vocal phrase is 1 bar long and is followed by 1 bar of instrumental. This is the arrangement unit the visuals use (2-bar scenes).
- Vocal segments (demucs RMS): 0.07-1.35, 4.26-5.89, 9.66-11.26, 14.45-15.95, 19.26-20.83, 24.07-25.51, 28.87-30.33, then 38.46-40.97, 42.68-45.79, 48.08-50.64, 57.67-58.40.
- Phrase entries land at a fixed beat phase: (t - grid_t0)/beat mod 1 = 0.35-0.38 for all six first-half entries (≈13 frames after a beat). The singer comes in off the beat.
- Sections: rows 0-13 verse (alternating); row 14 (32.84 s) breakdown (drums -22.6, bass -28.8, hi band down) = pre-reveal; rows 16-21 (37.6-52 s) drop/hook, ~2 dB louder with more hi/mid; row 23 (54.46 s) drums out (-50 dB); row 24 vocal tag; row 25 tail.
- Loop: best bar matching bar 0 is bar 2 (mel corr 0.97); last bar vs first 0.655 → the clip is cut to *end* near the start state but the audio does not loop seamlessly.

## Sync evidence [M] (sync.py, wordsync.py)

- **Global A/V offset:** raw motion onsets cluster at **-3 frames** to the kick grid (46 of 126 onsets in that single bin; next bin -4 has 13). The other four reels sit at -1 frame. Inference: visuals are rendered ~50 ms ahead of the audible kick attack, possibly AAC priming (~48 ms) or deliberate anticipation [I].
- After correcting -3 f, motion onsets (n=126) within ±1 frame: **bar 11.9%** (chance 2.1%), **beat 45.2%** (8.3%), half-beat 57.1% (16.7%), 16th 65.9% (33.3%). Coarsest level hit: bar 15, beat 42, half 15, 16th 11, none 43.
- Uncorrected (as delivered) within ±2 f of a beat: only 2.4%. The offset matters when measuring.
- **Cuts (n=15): 0 on the beat grid within ±1 f** (13 of 15 hit no grid level). Instead, the first-half cuts match the vocal phrase starts within 1 frame: 4.267/4.26, 9.650/9.66, 14.467/14.45, 19.250/19.26, 24.067/24.07, 28.867/28.87. visual.py: 47% of cuts within ±1 f of a vocal-stem onset, 60% within ±2 f. All cut beat phases: entries 0.28-0.38, interstitial exits 0.67-0.70.
- Interstitial cards: 3 of 3 spaced 2 bars apart (4.83 s, 4.77 s), each 0.80-0.85 s.
- Change-signal autocorrelation at the bar lag: -0.014 (no bar periodicity, unlike De9or 0.396). The editing rhythm here comes from phrases, not from the bar loop.
- Word-level (whisper-small on demucs vocals, 45 words, mean prob 0.84): lyric-band change within ±2 f of a word start 29%, ±6 f 53%. This is **inconclusive**: whisper-small timing is only ±50-100 ms accurate, and the detected band (y 1210-1430) also contains other motion. Sung word starts are *not* on the grid (on a 16th within ±1 f: 27%, chance 33%), so word highlighting must be driven by word timestamps, not by the beat grid [I].

## How to rebuild it (Remotion)

Timing inputs (precompute to JSON, load with `staticFile` + `delayRender`/`continueRender` or pass as props):
- `beats[]`, `bars[]` (kick-fit grid; shift visuals -3 frames if you want to copy this reel's lead, or 0-1 frame as in the others).
- `words[] {text,startMs,endMs}` from WhisperX (creator's tool) — or Remotion's own `@remotion/install-whisper-cpp` + `@remotion/captions` (`Caption` type, `createTikTokStyleCaptions`), which are the sanctioned word-timing path in Remotion [I: package existence from Remotion docs knowledge, not checked in this repo].
- `phrases[] {startMs,endMs}` = group words by gaps > 1 beat; in this song each phrase = one vocal bar.
- `stemEnv.vocals[]` per-frame RMS (for dimming), from demucs/Suno stems.

Components:
- `<DeskScene monitorContent={ReactNode} dim={vocalEnv} ledStep={beatIndex}/>` — static room; `ledStep` from `beats[]`.
- `<MonitorScreen>` + per-phrase screens `<PhotosMemory/>`, `<SlackMessage/>`, `<HomeLock/>`, `<FindMy/>`, `<DesktopWallpaper variant="cemetery"/>` — mounted in a `<Series>` whose `durationInFrames` come from `phrases[]` (cut = phrase start, not bar start).
- `<TerminalKaraoke words={phraseWords} activeColor="#fff" pastColor="grey" cursor />` — word index from `words[]`; cursor blink on a fixed period.
- `<PushIn from={1} to={1.25} durationInFrames={phraseLen} easing={Easing.out(Easing.cubic)}/>` — wraps the monitor; restarts at each phrase.
- `<EyeZoom direction="in"|"out" startFrame endFrame/>` — continuous `interpolate` with `Easing.in`, used at the breakdown (bar 14-15) and reversed at bar 23.
- `<Interstitial text="(just kidding)" at={phraseStart} durationInFrames={51}/>` — 0.85 s at 60 fps; schedule every 2 bars inside the drop.
- `<CemeteryDesktop tombstones={...} pills={...} swarm={progress}/>`.
- `<Flash frames={2}/>` at frame 0.
- Optional transitions: `@remotion/transitions` (`TransitionSeries`, fade/wipe) are the sanctioned way to do the zoom-throughs if you want them reusable [I].

## Why it works (caption + comments)

1. **A story with a twist instead of a list.** The other four reels illustrate a concept (checks, bubbles, sunset, Zeno); this one builds suspense over 6 phrase-scenes, reveals, then undoes the scare with "(just kidding)". Watch-through is rewarded with a punchline at 57.5 s [I].
2. **Dense Easter eggs that reward rewatching.** The caption lists them: camera light, 2:14 AM as the T2 Skynet time, the cemetery desktop as skeleton screens and ghosts [M caption]. Small details are readable only on pause [I].
3. **It hits a real fear about AI memory and agency.** The top comment (32 likes) is about memory across sessions; another (18) riffs on "you're absolutely right" apologies [M comments]. The horror is about the product the audience uses daily [I].
4. **Timely hook.** Halloween posting (#halloween2026) and synthwave/darkwave fit the theme [M caption]; people ask for the full song [M comments].
5. **Different editing logic.** It is the only reel of the five where cuts follow the *vocal phrase* (0/15 on the grid) with one scene per 2-bar call-and-silence unit, and where camera moves (push-in, eye zoom) carry most of the motion. The other four lock cuts to beats/half-beats (50-89%) and drive motion from beat pulses. Inference: phrase-locked cuts feel like storytelling; beat-locked cuts feel like a music visualizer [I].

**What differs from the other four** (all [M] unless marked): slowest tempo (100 vs 123-139 BPM); vocals alternate on/off per bar; cuts at a fixed off-beat phase (0.37 beat) matching vocal entries; A/V lead of 3 frames instead of 1; no bar periodicity in the motion signal; dark low-contrast palette with one orange reveal; two mascots instead of one; ends on a typed punchline [E].
