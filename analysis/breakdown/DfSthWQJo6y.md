# DfSthWQJo6y — context-window aquarium (14.1K views)

Legend: **[M]** measured by a script in `diagnostics/setA/`, **[E]** eyeballed from contact sheets / 1 fps frames / 20 fps hook sheet, **[I]** inferred.
Lyrics are not transcribed; on-screen phrases quoted only as 2-4 word identifiers.
Artefacts: `downloads/frames/DfSthWQJo6y/`.

## Summary

The mascot lives in a glass tank (labelled CTX-07) that fills with the words of a conversation; a token counter and a dollar counter climb with every line, until a compaction drains the tank — tokens crash, dollars do not. It explains, from the model's side, that every reply means rereading the whole chat, and frames that cost as devotion rather than complaint.

| | |
|---|---|
| Length | 50.200 s [M] |
| BPM | 118.020 [M] (period 508.39 ms = 30.5 frames); caption style prompt says 118 BPM [M] |
| Bars | 98.795 beats = 24.7 bars; seam -104 ms, **not a whole number of beats** [M]; downbeat **undetermined** (see Audio) |
| Genre feel | Indie dance / dark disco, slow, deep analog bass, hypnotic arpeggio — caption style prompt verbatim [M]; #darkdisco |

## Hook (0-3 s) [E hook sheet, times M where noted]

| time | on screen |
|---|---|
| 0.00-0.25 | Close-up of a lit aquarium: mint water (#a4d3d3 / #8bc3c3) with caustic ripples, a wall clock labelled CTX-07, a big orange pixel mascot (#d58363) floating mid-tank, a small purple chip block on the floor. Dark teal surround (#021314 / #0b242b) with vignette. Pink glyph particles drift. |
| 0.25-0.30 | First text: dark-purple label box (#2b1535-ish) at top-left with white condensed caps, the first word [E]. |
| 0.5-2.0 | Words append to the same label one at a time on the sung words; the label box widens with each word; pink word-particles stream down the left side into the tank [E]. Event 0.500 s exactly on a beat (+0.0 f) [M]. |
| ~2.0-2.4 | Second line starts in a new label box, indented under the first [E]. |
| ~2.4-3.0 | A pile of glowing words ("lol", "pls"-style) rises along the tank floor [E]. |
| 3.550 | Hard cut (area 0.639) to the wide shot: tank in a server rack with a large mint mono counter "N tok $X" below it — exactly on beat 7 (+0.0 f) [M]. |

First text at ~0.27 s; first motion = water shimmer from frame 0 (continuous) and word particles; first cut 3.55 s on the beat.

## Timeline [cuts M; content E]

Beat k at -0.0074 + 0.50839·k s. Bars counted from file start (k/4) because the downbeat is ambiguous.

| time range | beats | scene / background | text treatment | what moves on what rhythmic unit |
|---|---|---|---|---|
| 0.00-3.55 | 0-7 | Tank close-up, word pile begins. | Stacked label boxes, word-by-word append. | Words on vocal; water shimmer continuous. |
| 3.55-9.65 | 7-19 | Wide rack shot: tank, side tube/bottle, pipes; counter reading ~50K tok, ~$1.60 and climbing [E]. | Labels above the tank. | Counter values change between every 2 fps sample (~per beat at 508 ms) [E]; an attempt to measure counter ticks was confounded by the water animation (region changes every ~67 ms) [M regionticks.py]. |
| 9.65-11.68 | 19-23 | Cut (beat 19, +0.0 f) to dark circuit view: a "{ }" tool-call box with traces; a thin packet goes out and a fat one returns (per caption) [E/M caption]. | Labels persist. | — |
| 11.68-16.77 | 23-33 | Cut (beat 23, +0.0 f, area 0.908) to extreme close-up of the mascot sinking into the word pile; counter blurred in the foreground (rack focus) [E]. | — | Slow push-in / mascot sinking (continuous) [E]. |
| 16.77-24.90 | 33-49 | Cut (beat 33, -0.3 f) to wide rack: counter ~212K -> ~412K tok, ~$4.20 -> ~$6.00 [E]; a "train" of chips loops the tank (per caption). | Labels. | Counter ticks; tank fill rises [E]. |
| 24.90-30.48 | 49-60 | Cut (beat 49, -0.3 f) to close-up; tank nearly full, big counter in foreground ~$6.8-9.1 [E]. | Labels, a parenthetical line appears. | — |
| 30.48-35.35 | 60-70 | Cut (beat 60, -0.6 f) to wide: 688,920 tok; then **compaction** ~32.5-33 s: pile drains, counter drops to ~41K tok while dollars hold ~$9.84 [E]. Low band out from beat 63 (32.02 s) — breakdown [M]. | Lyric with an "a-do-do" filler line. | — |
| 35.35-48.53 | 70-95 | Cut (35.350, -13.7 f, **off-beat**) [M] to a clean white-tiled tank close-up, small new pile; rack focus and a slow pull-out back to the rack (46-48 s) [E]. Hat bursts at beats 69/77/85/93 (8-beat cycle) [M]. | Labels. | Slow pull-out; counter ticks ~41,207 -> 41,233 [E]. |
| 48.53-50.20 | 95-98 | Cut (48.533, +14.6 f, off-beat) [M] to a tall scrolling wall of identical tanks (every conversation is a tank) [E/I]. | Final line word by word. | Vertical scroll. Audio tail -32.9 dB in last 50 ms (fade) [M]. |

## Visual system

- **Palette [M]:** surround #021314 / #0b242b / #13353b / #010b0c; water #a4d3d3 / #8bc3c3 / #b4dcda; mascot #d58363; label box dark purple #2b1535 (white text); counter mint (similar to water, brighter) [E]; word-pile neons pink/purple/yellow [E].
- **Typography [E]:** condensed sans caps in dark label boxes, 1-2 lines, top-left (second line indented); counter in large mono digits with small "tok" suffix; pile words in mixed neon handwriting/mono.
- **Layout [E]:** labels top 15%; tank centre; counter in the bottom third (wide shots); close-ups fill the frame with the mascot.
- **Mascot:** large pixel Clawd, floats/sinks; eyes shift [E].
- **Background:** dark server-room teal, rack hardware, pipes, glowing tube on the right (the coolant bottle).
- **UI elements:** token + dollar counter, "alignment check" footer under the counter [E], tool-call box.
- **Camera [E]:** the most "cinematic" in the set — cuts between close-up and wide, rack focus with a blurred foreground counter, push-ins and pull-outs, a final vertical scroll.
- **Transitions:** hard cuts, mostly on the beat.

## Motion vocabulary

| primitive | trigger | easing / duration |
|---|---|---|
| Label box word append (box grows to fit) | sung word [E] | instant append, box width springs [E] |
| Word particles falling into tank | continuous / per word [E] | linear drift |
| Pile rise (fill level) | cumulative tokens [I] | smooth |
| Token / dollar counter | per beat or per line [E] | stepped values |
| Compaction drain | section (breakdown at beat 63) [M/I] | ~1 s drain |
| Rack focus (blur foreground counter) | close-up shots [E] | slow ease |
| Push-in / pull-out | scene [E] | slow ease over bars |
| Water caustics | continuous | looping noise |

## Audio structure [M unless marked]

- 118.020 BPM, phase -0.0074 s (file starts on a beat).
- Low/kick present from the start; out from beat 63 (32.02 s) for the breakdown; hat bursts in 8-beat cycles at beats 69, 77, 85, 93.
- **Downbeat undetermined:** the 8-beat hat cycle (69, 77...) and big cuts at beats 33 and 49 suggest downbeat k≡1, but cuts at 7, 19, 23 (k≡3) and 60 (k≡0) do not agree [M numbers, I conclusion].
- Loop: 98.795 beats, seam -104 ms — not whole-beat; last 50 ms at -32.9 dB vs ~-15 dB body suggests a short fade-out at the seam [M], so the loop is audibly less seamless than DfAd/Demq [I]. Chroma cos first/last 2 bars 0.844 [M].

## Sync evidence [M, sync2.py]

| measure | value | chance |
|---|---|---|
| visual onsets | 50 | |
| within 1 f of a beat | 36.0% (40.0% at best offset -2 f) | 9.8% |
| within 1 f of a half-beat | 46.0% | 19.7% |
| within 1 f of a 16th | 76.0% | 39.3% |
| strong-half events on a beat | 56.0% (n=25) | |
| position on/e/&/a | 22 / 11 / 8 / 9 | |
| **big cuts (area > 0.5) on a beat** | **6 of 8 within 0.6 f** (3.550, 9.650, 11.683, 16.767, 24.900, 30.483); 35.350 and 48.533 off-beat | |

Most of this reel's motion is continuous (water, particles, camera eases), so few discrete events exist; the discrete ones (scene cuts) are beat-locked [M]. The two off-beat cuts are in the breakdown/outro and probably follow the vocal [I].

## How to rebuild it (Remotion)

| component | props | driven by |
|---|---|---|
| `<Tank>` | `fill` 0-1, `clean` bool, `label='CTX-07'` | `fill` = cumulative token curve keyed to `words[]` (reset at compaction section) |
| `<WordPile>` | `words[]` (chat filler words), `level` | same token curve |
| `<LabelStack>` | `lines[]` (max 2), `boxColor=#2b1535` | `words[]` word starts |
| `<Counter>` | `tokens`, `dollars` | tokens from `words[]`/`beats[]`, dollars monotonic (never drops) |
| `<Camera>` | `shot: 'close'|'wide'|'circuit'|'wall'`, `focus` | cut list on `beats[]` |
| `<ToolCallBox>` | packet size in/out | phrase |
| `<TankWall>` | rows of tanks, scroll speed | outro section |

Trim to a whole number of bars (e.g. 24 bars = 48.80 s or 25 bars = 50.84 s) to fix the seam.

## Why it works

1. **An insider truth made visible:** caption explains that the model rereads the whole chat; the counter makes cost tangible, and the compaction gag (tokens drop, dollars don't) is a payoff for people who use Claude daily [M caption, I].
2. **Production polish** — the camera language here is the richest in the set; commenters praise the music + lyrics + visuals coming together and a parent says their daughter dances to it [M].
3. **But the audience is narrow:** 25 comments, top one asking for long format / Spotify (17 likes) [M]. The concept needs knowledge of context windows and caching to land [I]; slower 118 BPM dark disco is less immediate than the 128-129 BPM reels [I].
