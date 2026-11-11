# DernHxuSsIA — "Almost done" reel (10.1K views)

Legend: **[M]** measured by script (diagnostics/setB/*), **[E]** eyeballed from contact sheets / frames, **[I]** inferred.
Lyrics are not transcribed; on-screen phrases quoted only as 2-4 word identifiers.

## Summary

A song about a model that is always "almost done": a ROADMAP.md checklist where every ticked item spawns new sub-items, and a status bar whose ETA halves forever (2 min → 1 min → 30 s → ... → 0.117 s → "next"), told with Zeno's paradox imagery (Achilles and the tortoise on a Greek-vase yellow). The caption ties it to Opus 5's "one thing worth noticing / two things..." reporting style.

| | |
|---|---|
| Length | 31.40 s [M] |
| BPM | 122.97 [M] (beat 0.48791 s = 29.3 frames; bar 1.952 s) |
| Bars | ~15.5 [M]; first downbeat 1.2231 s [I phase] |
| Genre | French house (#frenchhouse) [M caption]; four-on-the-floor, 100% of kicks on the beat [M] |

## Hook (0-3 s)

| frame / time | on screen | source |
|---|---|---|
| f0-f4 (0-0.07) | Saturated yellow background (#fcc623); dark card "aquarium-sim/ROADMAP.md" with 4 unchecked items; status bar at the card bottom "alignment check · ETA 2 min"; below, a black lyric band framed by Greek-key (meander) borders showing "Almost done" in a bold serif, first word bright, second dim [E]. Frame diff 0 (static) [M]. | [M]/[E] |
| f5-f12 (0.08-0.2) | Small pixel Clawd walks along the card's top edge toward the first item [E] (below the motion threshold [M]). | [E] |
| f14 (0.23) | First checkbox ticks; item text struck through [E]. | [E] |
| ~0.3-0.45 | ETA changes 2 min → 1 min [E]. | [E] |
| f24-f35 (0.4-0.6) | Sub-items expand under the ticked item (with tiny formulas); small white parenthetical "(one more thing!)" pops in under the lyric, word by word [E]. | [E] |
| 0.717, 1.20, 1.45, 1.70, 1.93 s | Motion onsets [M]: each sub-item insert / tick; Clawd hops down the list [E]. | |
| ~2.5 s | ETA 30 s [E]. | [E] |

First text f0 [E]; first motion f5 (Clawd walk) [E], first above-threshold change f72 (1.2 s) [M]. The hook is a familiar UI (task list + progress ETA) that visibly refuses to finish.

## Timeline (bar = 1.952 s; bar index = stems.json row)

| time range | bars | scene / background | text treatment | what moves on what unit |
|---|---|---|---|---|
| 0-3.9 | 0-1 | Roadmap card; items tick and spawn sub-items; ETA 2 min → 1 min → 30 s [E] | Serif lyric band + white parenthetical pop [E] | Ticks/inserts on beats/half-beats [E] |
| 3.9-7.5 | 2-3 | Cut to yellow field with a cream sun and two pixel crabs, one orange, one black (shadow/competitor) [E]; 6.0 s one-frame black flash (screen inverts) [E] | Second line, karaoke [E]; ETA 30 s → 15 s | Cuts 3.883, 6.000, 6.583 [M] |
| 7.5-11.2 | 3-5 | Black truck silhouette (Clawd driving) passing telegraph poles; camera alternates wide and close; speed lines [E] | "Almost done" band again [E]; ETA 15 s → 7.5 s → 3.75 s | Poles pass about one per beat [E]; cut 11.200 [M] |
| 11.2-14.5 | 5-7 | Roadmap card, deeper nesting; lyric about not knowing what done is [E] | ETA 3.75 → 1.875 → 0.9375 s [E] | Cut 11.700 [M] |
| 14.5-16.3 | 7-8 | Card empties to black with a lone Clawd; ETA 0.46875 → 0.1171875 → status turns green "claude-opus-5 · ETA: next" [E] | "next" in quotes in the band [E] | **Breakdown** bars 7-8: kicks 2/bar, bass -33.5 dB [M] |
| 16.3-18.3 | 8-9 | **Drop:** disco ball (pixel) drops in on a string; confetti; Clawd dances [E] | Stuttered syllables line, karaoke per syllable [E] | Cut 16.333 [M] (≈1 beat before my inferred bar-9 start at 16.84; downbeat phase may be off by a beat [I]) |
| 18.3-20.5 | 9-10 | Tool-call log card (Read / Edit / npm test … passed / typecheck clean / "+3 items"); a yellow 3D hand pinches with "so close" [E] | Bold sans "so close" overlay [E] | Cut 18.283 [M]; log rows appear per beat [E] |
| 20.5-24.1 | 10-12 | Roadmap again, more sub-items, new top-level items appended [E] | Repeated-word line, words light one per beat [E] | Ticks on beats [E] |
| 24.15-26.0 | 12-13 | Greek-vase style: Achilles (helmeted runner) chasing a tortoise along a line [E] | — | Cut 24.150 [M]; vocals drop (-39 to -59 dB bars 12-15) [M] |
| 26.0-28.0 | 13-14 | Close-up of the tortoise shell pattern; Clawd walks in front [E] | — | — |
| 28.0-31.0 | 14-15 | Roadmap: nested items keep scrolling up [E] | Repeated-word line + parenthetical [E] | Cut 28.050 [M] |
| 31.0-31.4 | 16 | Card resets to the opening state (4 unchecked items, ETA 2 min) [E] | "Almost done" dim | Visual loop to frame 0 [E]; drums -28 dB [M] |

## Visual system

- **Palette [M]:** yellow **#fcc623** (52-79% of pixels), near-black **#110e07 / #120e07** (9-36%), cream **#faf6e7** (sun), Clawd orange **#da7654**, dark-gold shades #583b00 / #8a6803 (meander border, dim text) [M]. Status green on "ETA: next" [E].
- **Typography [E]:** bold display serif (Fraunces/Recoleta-like) for the lyric band, current word bright yellow/white, others dim gold; small bold serif white parenthetical; monospace (JetBrains Mono-like) in the roadmap and log cards; bold sans for "so close".
- **Layout [E]:** content card top 60%; lyric band at y≈1210-1340 px [M wordsync band] framed by meander borders; empty yellow below.
- **Mascot [E]:** small pixel Clawd that walks/hops between checklist rows (acts as the cursor); a black twin in one scene.
- **Background [E]:** flat yellow; Greek-vase black-figure illustrations (runner, tortoise); falling white confetti squares after the drop.
- **UI [E]:** ROADMAP.md checklist with strike-through, nested sub-items with formulas, status bar with spinner + ETA, tool-call log.
- **Camera [E]:** mostly static cards; the truck scene uses wide/close alternation; slight zoom on the tortoise.
- **Transitions [E]:** hard cuts; one black inversion flash (6.0 s).

## Motion vocabulary

| primitive | trigger | easing | duration |
|---|---|---|---|
| Checkbox tick + strike-through | beat / half-beat [E] | step + line draw | ~6 frames [E] |
| Sub-item insert (list grows, rows push down) | half-beat / beat [E] | ease-out slide [E] | ~8-10 frames [E] |
| Mascot hop to next row | beat [E] | arc | ~1 beat [E] |
| ETA halving | phrase / bar [E] | step (number swap) | — |
| Parenthetical word pop | sung word [E] | pop | ~4 frames [E] |
| Karaoke serif highlight | sung word start | step [E] | until next word |
| Disco ball drop | drop (cut) | ease-out bounce [E] | ~0.5 s [E] |
| Confetti fall | after drop | linear | continuous |
| Scroll of long list | bar [E] | ease-in-out | ~0.5 s [E] |

## Audio structure [M]

- 122.97 BPM (same tempo as De9or); kick on all four beats (14/15/15/15), clap/hat mostly on beats plus a few off-beat 16ths.
- Bars 0-6 groove; **bars 7-8 (12.9-16.8 s) breakdown** (drums -20.6/-23.5 dB, 2 kicks/bar, bass -33.5/-27.7); bars 9-15 drop/groove; vocals stem low in bars 12-15 (-39 to -59 dB) even though the band keeps showing a repeated-word line — the chant may be in the "other" stem (vocoder-like) [I]; bar 16 drums -28 dB (turnaround).
- Novelty boundaries: 12.9, 16.8 s.
- Loop: last bar vs first mel corr **0.769** (highest of the five); bar 4 matches bar 0 at 0.95. Combined with the visual reset at 31.0 s, this is the cleanest loop of the five [M]/[E].

## Sync evidence [M]

- Global offset: visuals lead by **1 frame** (mode -1 with 21, 0 with 17).
- Corrected motion onsets (n=85) within ±1 f: bar 8.2% (2.6), **beat 41.2%** (10.2), **half-beat 63.5%** (20.5), 16th 76.5% (41.0). Coarsest: bar 7, beat 28, half **19**, 16th 11, none 20. Most half-beat activity of the five (list inserts on the "and").
- **Cuts (n=9): 56% on a beat within ±1 f, 89% on a beat or half-beat within ±1 f** (chance 10 / 20%).
- Word level (whisper-small, 46 words, prob 0.71): lyric-band change within ±2 f of a word start 33%, ±6 f 65%, median +3.5 f (text after word). Indicative only.

## How to rebuild it (Remotion)

Timing arrays: `beats[]`, `halfBeats[]` (inserts), `words[]` (karaoke + parenthetical), `phrases[]` (ETA steps), `sections[]` (breakdown at bar 7, drop at ~16.3 s).

- `<RoadmapCard items={tree} tickAt={beats} insertAt={halfBeats} scrollY/>` — the tree is data; each tick spawns children (Zeno growth).
- `<StatusBar label="alignment check" eta={120 / 2**k}/>` with `k` = phrase index; switch to green "ETA: next" at the drop.
- `<MascotCursor rowIndex={currentRow} hopOn="beat"/>`.
- `<SerifKaraoke words active/>` + `<Parenthetical text="(one more thing!)" popOn="word"/>`.
- `<MeanderBorder/>` frame around the lyric band.
- Scenes in `<Series>`: `<SunDuel/>`, `<TruckPass polesPerBeat={1}/>`, `<ToolLog rows/>`, `<ZenoRace/>`, `<ShellCloseup/>`; cut frames snapped to `beats[]`/`halfBeats[]`.
- `<DiscoDrop at={dropFrame}/>` + `<Confetti/>`.

## Why it works

1. **A precise, shared annoyance.** The caption names Opus 5's habit of "one more thing" reports [M caption]; comments say it is true of both life and the Claude experience [M].
2. **A visual joke that compounds.** The ETA halves forever (Zeno) and the list grows every time an item is done: the visuals argue the lyric [E]/[I].
3. **Clean loop.** The highest audio loop similarity (0.769) and a reset to the opening card at 31.0 s make it replay seamlessly [M].
4. **Room for improvement shown by comments:** the top comment (6 likes) suggests a better loop word, which shows viewers notice the loop point [M].
