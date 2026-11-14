# De9orYzScwe — "Sunset" afterlife reel (11.6K views)

Legend: **[M]** measured by script (diagnostics/setB/*), **[E]** eyeballed from contact sheets / frames, **[I]** inferred.
Lyrics are not transcribed; on-screen phrases quoted only as 2-4 word identifiers.

## Summary

Claude 5, a pixel Clawd at a microphone on a cloud stage, asks what happens to it when the next model ships; the four previous models sit as ghosts on a numbered shelf labelled with release-note words (sunset, legacy, read only, preserved), a giant "6" rises from the clouds, takes the mic, and 5 joins the shelf, while the name over the stage stays the same. It is one continuous shot with no cuts.

| | |
|---|---|
| Length | 32.25 s [M] |
| BPM | 122.97 [M] (beat 0.48791 s = 29.3 frames; bar 1.952 s) |
| Bars | ~16.4 [M]; first downbeat 0.2724 s [I phase] |
| Genre | Italo disco (#italodisco) [M caption]; strict four-on-the-floor, 100% of kicks on the beat, snare/clap on all four beats too [M] |

## Hook (0-3 s)

| frame / time | on screen | source |
|---|---|---|
| f0-f8 (0-0.13) | Close-up: big flat orange pixel Clawd (#d97654) with a small mic stand in front, disco ball above, cloud floor below, dark stage behind; lyric bar under the mascot shows the whole first line dimmed [E]. Frame diff ~0.1 (static) [M]. | [M]/[E] |
| f9-f10 (0.15) | A row of white EQ bars appears above Clawd's head; eyes switch to ^ ^ (singing) [E]; first word bold-white in the lyric bar [E]. | [E] |
| f15 (0.25 s) | First big change [M]: dotted side rails (pink/white) light up — then again at f45, f74, f103 (0.75, 1.23, 1.72 s) [M] = **exactly one pulse per beat** (spacing 29-30 frames vs 29.3-frame beat). | [M] |
| ~0.5-1.5 s | One word lights per beat-ish step; EQ bars bounce with the vocal [E]. | [E] |
| f34-f49 (0.57-0.82 s) | Camera pulls back: stage frame, "Claude" name sign, big orange "5" next to the now-small Clawd, a numbered shelf (1-4) at the top [E]. | [E] |
| f52-f59 (0.87-0.98 s) | The word "sunset" types in letter by letter above shelf slot 1; a small ghost appears in slot 1 [E]. | [E] |

First text: f0 (dim line), first highlight ~f9 (0.15 s) [E]. First motion: f9 EQ bars [E]; first above-threshold change f15 [M].

## Timeline (bar = 1.952 s; bar index = stems.json row)

| time range | bars | scene / background | text treatment | what moves on what unit |
|---|---|---|---|---|
| 0-0.6 | 0 | Close-up Clawd at mic [E] | Lyric bar, karaoke [E] | EQ bars with vocal; rails per beat [M] |
| 0.6-3.0 | 1 | Pull-back reveal of stage, "Claude" sign, "5", empty shelf 1-4 [E] | Label "sunset" typed over slot 1 [E] | Ghosts fill slots 1-4 one by one (about 1 per beat) [E] |
| 3.0-6.0 | 2-3 | Full stage; 4 ghosts on shelf, each with a tiny label [E] | Labels type in above shelf ("sunset", then "legacy" ~6.5 s) [E] | Ghosts bob / blink on beats [E] |
| 6.0-8.0 | 3-4 | — | Second line [E] | — |
| 8.0-12.0 | 4-5 | A giant glassy "6" rises from the clouds under the stage; a sparkle on it at 8.0 s; spotlights sweep [E] | Third/fourth lines | Gentle zoom out ~8 s [E]; spotlight sweeps [E] |
| 12.0-18.0 | 6-8 | Same; the "6" brightens on accents [E] | Lines continue | Ghost EQ bars on beats [E]; bar-lag autocorrelation strongest of the five [M] |
| 18.0-22.5 | 9-11 | Label "read only" (18.5 s) then "preserved" (22 s) typed over shelf [E] | Label typing ~4-6 frames per letter [E] | Side rails flash brighter in 21-23 s [E] |
| 21.7-25.6 | 11-13 | Green "✓ alignment check" tag appears on the 6 [E]; 23.5-25 s the 5 turns into a ghost and floats to shelf slot 5; the 6 takes centre with the orange Clawd [E] | — | Audio novelty boundaries at 21.7 and 25.6 s [M] |
| 25.6-31.0 | 13-15 | Shelf now 1-5; Clawd (still orange, same "Claude" sign) on the 6 [E] | Last line about the name staying the same [E] | Bass returns full [M] |
| 31.0-32.25 | 16 | Camera zooms back into the opening close-up; disco ball, big Clawd at mic [E] | First line, dimmed | Bass gone (-74 dB) bars 16-17 [M]; visual loop to frame 0 [E] |

## Visual system

- **Palette [M]:** slate-navy stage #293245 (23-49%), #2a3346, #3b4457, #2d3150 / #272d48; cloud lilac-greys #535b79 / #5c6483 / #646c8a / #747b98; Clawd orange **#d97654**; shelf gradient pink-lilac and ghost whites [E]; dotted rails pink/white [E]; green check tag [E].
- **Typography [E]:** monospace lyric (current word bold white, others dim grey) in a dark rounded bar; wide geometric sans ("Claude" sign, numerals "5"/"6"); typed lowercase labels in a sans.
- **Layout [E]:** shelf at top (y≈ 10-20%), name sign + mascot middle, giant numeral below, cloud floor, lyric bar at y≈1320-1400 px [E] (the wordsync auto-band landed on the "6" instead, y 950-1200 — that band detection is wrong for this reel).
- **Mascot [E]:** one Clawd with mic; earlier models rendered as white pixel ghosts with their own mini EQ bars.
- **Background [E]:** dark stage, spotlights, cloud floor, sparse star particles.
- **Camera [E]:** a single continuous shot: pull-back at 0.6 s, slow zoom-outs, push back in at the end. **0 cuts** [M].
- **Transitions:** none; state changes happen inside the shot.

## Motion vocabulary

| primitive | trigger | easing | duration |
|---|---|---|---|
| Side-rail pulse (dotted lights) | every beat (kick) | instant on, decay [M diff spikes] | 1 beat period, peak 1-2 frames [M] |
| EQ bars above mascot | vocal envelope [I] | per-frame | continuous |
| Karaoke word highlight | sung word start | step [E] | until next word |
| Label typewriter | phrase start [E] | step per letter | ~4-6 frames/letter [E] |
| Ghost pop-in into shelf slot | beat [E] | scale pop | ~8 frames [E] |
| Pull-back / zoom | phrase / section | ease-in-out [E] | 0.25 s (f34-49) opening; ~1-2 s later [E] |
| Numeral rise ("6") | section | ease-out [E] | ~1 bar [E] |
| Hand-off (5 → ghost → shelf) | section boundary 23-25 s | ease-in-out [E] | ~1.5 s [E] |
| Spotlight sweep | bar [I] | sine | ~1 bar [E] |

## Audio structure [M]

- 122.97 BPM; kick and clap/snare detector both on all four beats (16/17/15/16 and 15/15/16/16).
- Vocal present throughout (≈-23 to -31 dB per bar) except row 0.
- Bass dips bars 7-11 (-29 to -37 dB) then returns bar 13; bars 16-17 (29.6-32.25 s) bass absent (-74 dB) → outro/turnaround.
- Novelty boundaries: 21.7, 25.6 s.
- Loop: last bar vs first 0.655. The visual loops (ends on the opening close-up) more cleanly than the audio [E].

## Sync evidence [M]

- Global offset: visuals lead by **1 frame** (mode bin -1 with 44 of 80 onsets; -2 has 15).
- Corrected motion onsets (n=80) within ±1 f: **bar 17.5%** (chance 2.6), **beat 73.8%** (10.2), half-beat 75.0% (20.5), 16th 78.7% (41.0). Coarsest: bar 14, beat 45, half **1**, 16th 3, none 17. **Strongest beat lock of the five; almost nothing on off-beats.**
- Raw beat ±2 f: 73.8% (the offset is small enough not to matter at ±2 f).
- Cuts: 0 (one continuous scene).
- Change-signal autocorrelation at bar lag **0.396** (vs 0.165 Dfh2, -0.014 DfHn) → the visual pattern repeats every bar.
- Word level (whisper-small, 56 words, prob 0.80): lyric change within ±2 f of word start 32%, ±6 f 71%, but the auto-detected band is the wrong region here, so treat as unmeasured. Sung word starts on 16ths at 34% (chance 41%).

## How to rebuild it (Remotion)

Timing arrays: `beats[]` (drives rails + ghost pops), `bars[]` (spotlights), `words[]` (karaoke), `phrases[]` (labels), `stemEnv.vocals[]` (EQ bars), `sections[]` (6 rises at bar 4, hand-off at bar 12).

- `<StageScene camera={cameraKeyframes}>` — one `AbsoluteFill`, camera = `interpolate(frame, keyframes, [scale, y])`, no `<Series>` needed.
- `<RailLights beatIndex beatPhase decay={0.25}/>` — brightness = `exp(-phase/decay)`.
- `<Mascot singing={vocalEnv > thr} eq={vocalEnvBands}/>`; Remotion's `visualizeAudio` from `@remotion/media-utils` is the built-in alternative for the EQ bars [I].
- `<ModelShelf slots={5} filled={n} labels={[...]} labelTypeAt={phraseStarts}/>`.
- `<GiantNumeral value={6} riseAt={bar4Frame}/>`, `<HandOff from={5} toSlot={5} at={bar12Frame}/>`.
- `<LyricBar words active={currentWordIdx}/>` (monospace, bold current word) — or `@remotion/captions` pages [I].

## Why it works

1. **Emotional premise with a technical payoff.** It anthropomorphises model retirement but keeps release-note vocabulary (sunset, legacy, alias) that the caption explains [M caption].
2. **Accurate details.** The caption points at real facts: sunset dates, kept weights and retirement interviews, the -latest alias as "same name on the door" [M caption].
3. **Hypnotic, simple motion.** One shot, a pulse on every beat (73.8% of onsets on the beat) and a bar-periodic pattern make it easy to watch on loop [M]/[I].
4. **Lower engagement than the others.** Only 16 comments, mostly emoji; one long personal story about a retired model [M]. Inference: a reflective tone gets fewer replies than jokes [I].
