# DfAdDZXMc21 — "not your friend" (647K views, the breakout)

Legend: **[M]** measured by a script in `diagnostics/setA/`, **[E]** eyeballed from contact sheets / 1 fps frames / 20 fps hook sheet, **[I]** inferred (interpretation, not measured).
Lyrics are not transcribed. On-screen phrases are quoted only as 2-4 word identifiers.
Frame artefacts: `downloads/frames/DfAdDZXMc21/` (sheet2fps/, hook/h_01.jpg, full/f_NNN.png, diff.npy, grid.json, sync2.json, sync2_verbose.txt, beatenergy.txt).

## Summary

The orange pixel mascot (Clawd) flatly tells the viewer it is not their friend, only a program, and then walks through why people anthropomorphize anyway (pet rocks, chatbots, robot vacuums, "warmth" sliders in a system prompt) while the visuals keep making it more friend-shaped. The joke is the contradiction between a cold denial and a cute character, delivered as a robotic electroclash chant.

| | |
|---|---|
| Length | 44.604 s [M] (60 fps, 1080x1920) |
| BPM | 129.082 [M] (comb-searched rigid grid, period 464.82 ms = 27.9 frames). Creator's stated Suno prompt says 128 BPM [M, comment]; local tempo wanders 128.4-129.4 [M, localgrid.py] |
| Bars | 24 bars exactly: 95.966 beats, seam error -16 ms [M]. Downbeat = grid beat -1 at t = 0.074 s [M/I: from low-band entries at beat 15 and exit at beat 87, both bar lines]; bar = 1.8593 s |
| Genre feel | Electroclash / robot-pop: vocoder chant, syncopated kick, Kraftwerk / Daft Punk per comments [M]; caption tag #electroclash [M] |

## Hook (0-3 s), frame by frame [E from hook/h_01.jpg at 20 fps, times M from diff.npy / colortrack.py]

| time | frame | on screen |
|---|---|---|
| 0.000-0.200 | f0-f12 | Black screen (#0d1013) with sparse dim matrix-rain glyphs; mascot present but unlit (dim grey). No text. Matrix rain steps every 7 frames (stepped, static between) [M]. |
| 0.233 | f14 | Mascot "switches on": grey -> orange #db7856 in one frame [M, colortrack]. First motion event (diff 2.32) [M]. |
| 0.267-0.367 | f16-f22 | First text: "i am not" (white #fcfdfe, heavy lowercase grotesk) drops in from above with ~6-frame ease-out, landed by ~0.35 s [M/E]. |
| 0.35-1.10 | | Hold. Text static, rain stepping. |
| 1.10-1.20 | f66-f72 | Second line "your friend" drops in the same way below the first [M/E]. Both text arrivals sit ~+10/+11 frames after a beat, i.e. on the sung word, not the beat [M]. |
| ~2.05 | f123 | Mascot eye shape changes (blink/expression) [E]. |
| 2.100 | f126 | Hard cut (diff 179.5, area 0.995) to light grey #cfd4d7 circuit board: grey chip-mascot wired into traces, monospace terminal line "i'm a program" with blinking block cursor [M/E]. This cut is +10 frames off the beat [M] — vocal-timed. |
| 2.1-3.0 | | Grey scene holds; cursor blinks. |

First text at 0.267 s (frame 16). First motion at 0.233 s (frame 14). Audio vocals start immediately (no silent lead-in) [E/I]. The hook is a flat-voiced denial sentence on a black screen over a character that has just lit up — a provocation, not a motion spectacle.

## Timeline

Bars counted from downbeat at 0.074 s (bar n starts at 0.074 + 1.8593·n s). Energy figures from beatenergy.txt / bars.py [M]; scene descriptions [E].

| time range | bars | scene / background | text treatment | what moves on what rhythmic unit |
|---|---|---|---|---|
| 0.00-7.43 | 0-3 | Alternates per ~bar: black matrix-rain screen with orange mascot (#0d1013) <-> light grey circuit scene with grey chip-mascot (#cfd4d7). Cuts at 2.100, 3.783, 5.850, 7.400 [M]. | White bold lowercase lines drop in from above (dark scenes); mono terminal line + block cursor (grey scenes). | Cuts and text follow the vocal phrases: 2.100 (+10 f), 5.850 (+12 f), 7.400 (-6.7 f) off-beat; only 3.783 lands on a beat [M]. No kick yet (low band absent) [M]. Rain steps every 7 frames (~1/4 beat) [M]. |
| 7.43-11.15 | 4-5 | Kick/low enters exactly at beat 15 = 7.511 s (bar 4) [M]. Dark screen; syllable stack of the title word (2-4 word id: "an·thro·po·mor·phize") in orange #db7856, then a black chip box "alignment check" with LED dot display; mascot shrinks and greys [E]. | One syllable per line, lines appear at 8.083, 8.567, 9.033, 9.500, 9.967 s = exactly one per beat (5 consecutive beats), each +7.5 f after the beat, hard pop (1-2 frame reveal) [M]. Glyph x-height ~64 px, line pitch ~130 px, left margin ~84 px at 1080 scale (font ~120 px) [M, textbox.py]. | Text on beat (+1/16); mascot static. |
| 11.15-20.45 | 6-10 | Cut 11.683 [M] to light grey dashboard: top 3x16 LED dot-matrix strip, right column of scrolling monospace "system prompt" text with a pink-highlighted word, bottom row of anthropomorphized objects (outlet, robot vacuum, cat-bot, rock with face), circuit traces [E]. Hats enter ~bar 7-8 (13-15 s) [M]. | Lyric lines black #13171a, fade to grey #959b9d once sung (karaoke "spent" state) [M palette/E]. A skull/red-eye glitch frame on one word [E]. Pixel-grid / blur glitch transition at 14.283 [M]. | Per beat: LED matrix re-randomizes, mascot eyes alternate ^^ / \|\| , icon strip steps [M, diffwhere.py shows change in row-0 LED grid, mascot face, row-6 icons each beat]. Text on vocal. |
| 20.45-27.96 | 11-14 | 21.000 [M] black chip box -> PCB layout -> settings-card UI (warmth slider with blue->pink gradient, a name field reading "buddy", a smile slider, hand cursor dragging the slider) [E]; 22.400 [M] background shifts to pink #d4c5d2; typed system-prompt block (mono, pink #ed2b8b highlight on one word); 2x2 tiles of anthropomorphized objects with faces [E]. | Typewriter mono for prompt; lyric lines in black then grey. | Cuts at 21.000 and 22.400 near bar 11 / bar 12 [M]. Hand cursor drag eased over ~1 beat [E]. |
| 27.96-29.83 | 15 | Concentric pixel squares (blue #547ebb / purple #8b62ac / pink #d33a94) pulsing [E]; bar 15 has the high-band peak fill [M]. | — | One big event on every beat from 28.433 to 29.833 (area > 0.2) [M]: the strongest beat-locked passage in the reel. |
| 29.83-40.98 | 16-21 | Mascot sitting on a chip with lyric lines; previous line is pushed up and out by the new one (scroll-up stack) [E]; a 3x3 then dense grid of identical tiny mascots on chips [E]; window chrome reading "session 2048113" with a hand cursor clicking close at ~38-39 s [E]. Mids drop (~-22 dB) in bars 16-21 [M]. | Line-by-line scroll; sung lines grey out. | Text on vocal; grid replicate appears on a bar line [I]. |
| 40.98-44.60 | 22-23 | Kick/low exits at beat 87 = 40.978 s (bar 22) [M]. CRT-off collapse to a white line/dot (~40-41 s), then pure black #000000 with an empty window outline and blinking cursor (41-43 s) [E]. 43.500 [M] hard cut to navy pixel grid of pink/purple/blue/white squares; white bold text pickup (2-4 word id: "i say this") word by word [E]. Events 43.500 (+12 f), 43.767, 44.233 [M]. | Word-by-word white bold. | Breakdown; the pickup phrase completes into the opening line when the reel loops [I: lyric loop — the first words of the next pass finish the sentence]. |

## Visual system

- **Palette [M, palette.py on 1 fps frames]:** black-screen #0d1013 / #1b1d21 / #2b2e32; mascot orange #db7856; text white #fcfdfe; circuit grey #cfd4d7, #a6acb2, #777d84, #b2b6bc, #e0e6e8; ink #13171a; spent-text grey #959b9d; pink paper #d4c5d2; accent pinks #ed2b8b / #d33a94 / #c4439b; purple #8b62ac; blues #547ebb / #6675b5; true black #000000 for the "session ended" breakdown.
- **Typography [E, sizes M]:** heavy grotesk lowercase for lyric lines (about 120 px font, x-height ~64 px, ~130 px line pitch, left-aligned at ~80-84 px); monospace for terminal/system prompt with block cursor; lyric lines white on dark, black on light, then grey after they are sung.
- **Layout grid [M/E]:** lyric block lives in the lower-middle band (white lines measured at y 714-800 and 842-954 at 1080x1920), left-aligned; mascot centred upper-middle; dashboard scenes use top strip (LED matrix) / centre (mascot + lyric) / right column (scrolling mono) / bottom strip (icon row).
- **Mascot:** the orange pixel crab (Clawd), drawn as square pixels; has "off" state (grey, chip-mounted) and "on" state (orange). Eyes swap between two glyphs per beat in the dashboard section [M].
- **Background system:** two alternating worlds — dark matrix-rain screen vs light circuit-board/dashboard — then pink "settings" world, then black void. Background colour is a section marker [E/I].
- **UI elements:** terminal line + block cursor, settings card with sliders and a name field, system-prompt text panel with highlighted word, window chrome with session id + close button, hand cursor, LED dot-matrix displays, "alignment check" branded chip box.
- **Camera:** essentially locked-off 2D; no pans. Movement comes from cuts, pops and stacks [E].
- **Transitions:** hard cuts (most common), pixel-grid / blur glitch (14.28 s), scroll-up push of lines, CRT power-off collapse to a line then a dot (~40 s) [E].

## Motion vocabulary

| primitive | trigger | easing / duration |
|---|---|---|
| Drop-in text line from above | vocal word onset (+10/11 f after beat) [M] | ease-out, ~6 frames (0.267-0.367 s) [M/E] |
| Syllable pop (one line per beat) | beat, +7.5 f (a 16th late) [M] | hard pop, 1-2 frames [M] |
| Mascot "power on" colour swap grey->orange | first vocal syllable [I] | 1 frame [M] |
| Sung-text greying (black/white -> #959b9d) | end of the sung word/line [E] | quick fade, a few frames [E] |
| Matrix-rain step | every 7 frames (~16th-ish, not grid-locked) [M] | stepped, no interpolation |
| LED matrix re-randomize / eye glyph swap / icon strip step | every beat [M] | instant |
| Concentric squares pulse | every beat 28.4-29.8 s [M] | instant on, decays within the beat [E] |
| Scroll-up line push | new lyric line [E] | ~6-10 frame ease [E] |
| Hand cursor drag on a slider / click on close | phrase-level [E] | eased over ~1 beat [E] |
| Glitch frame (skull / red eye; pixel blur) | an accented word / section change [E] | 1-3 frames [E] |
| CRT-off collapse | section end (kick exit, bar 22) [M/E] | ~0.5 s squash to line, then dot [E] |
| Typed system prompt | phrase | typewriter, chars per frame not measured |

## Audio structure [M unless marked]

- 129.082 BPM rigid grid; kick offset onto the off-beat in the onset comb fit (half_shift=1), anchored with hi-band waveform attacks (median attack -34..-46 ms vs onset-envelope grid).
- Bars 0-3 (0-7.4 s): no kick; vocal-heavy even bars alternate with quieter odd bars — this matches the dark/grey scene alternation [M energy, I link].
- Bar 4 (7.511 s): low/kick enters. Bars 4-21: 18 bars of full groove; hats enter ~bar 7-8; bar 15 (27.96 s) high-band fill peak; bars 16-21 mids drop (~-22 dB).
- Bar 22 (40.978 s): kick exits; bars 22-23 breakdown; bar 23 pickup words.
- Groove: hats/claps peak on the off-beat and on the beat; kick syncopated on 16ths [M, groove.py].
- Loop: 24.000 bars (95.966 beats, -16 ms) — seamless; first vs last 2 bars chroma cos 0.873 (median across bar pairs 0.925) [M]. The lyric itself loops: the final pickup flows into the first line [I].

## Sync evidence [M, sync2.py, attack-anchored grid, window [-1,+2] frames]

| measure | value | chance |
|---|---|---|
| visual onsets | 89 | |
| within 1 f of a beat | 61.8% | 10.8% |
| within 1 f of a half-beat | 70.8% | 21.5% |
| within 1 f of a 16th | 78.7% | 43.0% |
| best constant A/V offset | 0 frames | |
| median abs offset (beat) | 0.9 f | |
| strong-half events on a beat | 60.0% (n=45) | |
| onset position in beat (on/e/&/a) | 58 / 12 / 13 / 6 | |
| 12-bin fold of change energy (bin 0 = beat) | 1.36 0.42 0.55 0.75 1.53 1.62 0.44 0.40 0.43 1.14 0.24 1.58 | |

Two timing regimes are visible [M]: (1) **beat-locked** micro-motion (LED matrix, eye swaps, icon strip, concentric squares 28.4-29.8 s, syllable pops at exactly 1/beat); (2) **vocal-locked** text and big scene cuts (2.100 +10 f, 5.850 +12 f, 7.400 -6.7 f, 43.500 +12 f). The syllable pops sit +7.5 f after the beat — consistent with sung-syllable onsets that slightly trail the grid (WhisperX-style word times) rather than a beat array [I: no WhisperX run was done here]. The fold's secondary peaks near bins 4-5 and 9/11 suggest off-beat (&) and "a" events driven by syncopated vocals [I].

## How to rebuild it (Remotion)

Timing data: `beats[]` (129.082 BPM grid, phase 0.5389 s), `bars[]` (downbeat 0.074 s), `words[]` (WhisperX word/syllable times), `sections[]` (bar ranges). Frame = `Math.ceil(t*60)`.

| component | props | driven by |
|---|---|---|
| `<Scene>` switcher | `sections: {from, to, kind: 'matrix'|'circuit'|'dashboard'|'settings'|'squares'|'void'|'pixelgrid'}` | `words[]` phrase starts for intro alternation (bars 0-3), `bars[]` elsewhere |
| `<MatrixRain>` | `stepFrames=7, density, color` | frame counter (stepped `Math.floor(frame/7)` seed) |
| `<Mascot>` | `state: 'off'|'on'|'chip'`, `eyes: '^^'|'||'`, `scale` | `words[0]` for power-on; `beats[]` for eye swap |
| `<DropLine>` | `text, y, fromY=-80, dur=6f, color` | `words[]` line start |
| `<SyllableStack>` | `syllables[], lineHeight=130, x=84, color=#db7856` | `words[]` syllable times (they land 1 per beat) |
| `<KaraokeLine>` | `text, activeColor, spentColor=#959b9d` | `words[]` start/end |
| `<LedMatrix rows=3 cols=16>` | `seed` | `beats[]` index as seed |
| `<IconStrip>` | `icons[]` | `beats[]` (step 1 per beat) |
| `<SettingsCard>` + `<HandCursor>` | slider values, name field text | `words[]` phrase; eased `interpolate` over 1 beat |
| `<SystemPromptPanel>` | `text, highlight` | typewriter on `words[]` phrase |
| `<ConcentricSquares>` | `colors=[#547ebb,#8b62ac,#d33a94]` | `beats[]` in bar 15 |
| `<ScrollStack>` | `lines[]` | `words[]` line starts |
| `<CrtOff>` | `dur` | `sections[]` bar 22 start |
| `<GlitchFrame>` | `kind: 'skull'|'pixelblur'` | chosen `words[]` / section boundaries |

Loop: render exactly 24 bars (44.604 s) so seam = whole bars; end on a pickup phrase whose words complete in the first line.

## Why it works

1. **A one-line provocation that invites argument.** The first words on screen are a denial a cute character obviously contradicts; top comment "If not friend, why friend shaped?" (1,472 likes) is the audience naming the contradiction, and roughly 120 of the 750 fetched comments argue about anthropomorphism [M, keyword tally of comments JSON]. Debate = comments = reach [I].
2. **Replay bait.** Caption "Details if you replay it" lists hidden references (1975 pet rock, 1966 ELIZA secretary, Roomba owners) [M]; the frame is dense with small per-beat changes, so a second watch shows new things. 13.9K shares / 3.7K reposts [M, prior notes].
3. **A chantable earworm.** One syllable per beat, shown one syllable per line exactly on the beat [M], is a hook you can read and sing at once; comments ask for the full song / Spotify (~35) and name Kraftwerk / Daft Punk [M].
4. **A seamless 24-bar loop whose lyric also loops** [M seam -16 ms; I lyric], so viewers watch past the end without noticing.

**What differs from the other four [I, based on the four breakdowns in this set]:**
- Single universal idea (is the AI your friend?) instead of an insider/technical one (context window, hooks/slop, tutoring prompts). Anyone can have an opinion.
- The hook is a *statement to the viewer* in the first 0.3 s, white text on black — maximum legibility; the others open on a scene (road sign, aquarium, sky) where the text is smaller or in a UI element.
- Starkest palette (black / white / one orange) for the first 7 s; others are full-colour from frame 0.
- Hook audio is vocals-only for 4 bars and the kick lands at bar 4 — a built-in drop at 7.5 s keeps people past the first scroll decision. Demq drops at 2.1 s; De4f has kick from 0.79 s; DfSth and DfLk have the groove running from the start (DfLk instead pulls the kick out at 14.9 s for an 8-bar build).
- Fewest text styles in the hook (one font, one colour) and the biggest text in the set (~120 px).
