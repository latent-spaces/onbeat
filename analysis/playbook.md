# Playbook: beat-synced lyric reels

Built from the ten per-reel breakdowns in `analysis/breakdown/` (top 10 @alignment.check reels by views). Tags: **[M]** measured by script, **[E]** judged by eye from frames, **[H]** hypothesis.

We make our own songs, character and visuals in this format. We do not reuse their mascot, lyrics, scenes or branding.

## 1. The idea comes first [H, strongest evidence in the set]

The breakout (647K views) is visually one of the simplest reels. What differs from the 10–33K reels:

- **One universal, arguable claim**, not an insider joke. Anyone can have an opinion on it. About 120 of 750 comments argue the point [M].
- **The claim is the first thing on screen**, at 0.27 s, as a statement to the viewer [M].
- **The picture contradicts the claim** (a cute character says something cold). The top comment (1,472 likes) is the audience naming that contradiction [M].
- The weaker reels rest on insider ideas (context windows, hooks, prompts) and put their lyrics inside small UI elements.

Checklist for a concept: one sentence; a stranger could disagree with it; the visual undercuts or dramatises it; it works with sound off.

Caveat: this is 1 breakout in 33 reels. The pattern is a best explanation, not proof.

## 2. The song

- Strict four-on-the-floor, one fixed tempo, 100–139 BPM (five of ten sit at 118–129) [M]. 97–100% of kicks on the beat [M].
- A recognisable genre with a deadpan or robotic lead vocal and a **chant hook, one syllable per beat** [M for the breakout]. Commenters named Kraftwerk and Daft Punk and asked for the full song.
- **Open with vocals and no kick**, then drop. Breakout: 4 bars of vocal, kick at 7.5 s. Second-best hook reel: drop at 2.1 s with a colour cut [M].
- One breakdown later (kick out for 2–8 bars) to hang a scene change or a build on [M, all reels].
- **Cut the clip to a whole number of bars** so it loops: 20–24 bars, 30–45 s. The best performers have seam errors under 40 ms; weaker ones 100 ms+ [M]. Ending on a pickup phrase that completes the first line makes the lyric loop too [H].
- **Direct the arrangement, and keep it short** (our rule, from the first Suno runs): ask for a song of about one minute, with only the lyrics the reel needs. Suno's More Options has a Duration setting (Auto / Custom). Spell the build out in the section tags, in this order:
  1. `[Intro: solo synthetic vocoder voice, a cappella, no instruments]`
  2. `[Transition: one riser or glitch effect, one bar]`
  3. `[Drop: full drums, bass and synths enter together]`
- **Suno setup that worked** (suno.com/create, free plan, model v6-mini, second "allow always" run):
  - **Mode:** Advanced, so lyrics and style are separate fields.
  - **Lyrics field:** only the lines the reel needs (27 short lines gave 1:05). Every section gets a tag that names who sings and what plays, e.g. `[Drop: full drums, bass and synths enter together, robotic vocoder voice asks, tired human voice answers]`. Backing or answer lines go in parentheses. Hyphenate chant words by syllable (`no block-ers`). Close with `[End]`.
  - **Styles field:** start with `short song, one minute`, then genre, BPM, drums, bass, the lead voice (`robotic vocoder lead voice, monotone text-to-speech talk-singing`), the second voice, the chant device, the build (`a cappella vocoder intro then full band drop`), mood words, `club mix`.
  - **More Options → Duration → Custom:** drag the slider to about 1:05 (clicking the track does nothing; it must be dragged). Both takes came out at exactly 1:05. Left on Auto, the same concept ran 1:53 and 2:23 with a 32-second drumless intro.
  - **Other options left at default:** Weirdness 50%, Style Influence 50%, Variety Normal, Vocal Gender unset, Max Mode off.
  - **Output:** one Create gives two takes. Download from the take's "…" menu → Download → M4A. The free plan has a limited download count, so pick the take by ear in Suno first.
  - The full lyrics and style line are in `songs/allow-always/song.md`.
- Suno style line format (the creator's, for the breakout): genre, era, bass sound, drums, vocal delivery, hook device, mood words, "club mix", BPM.

## 3. Two timing layers [M]

This is the core technical finding. Everything on screen belongs to one of two clocks.

| Layer | Driven by | What uses it | Measured |
|---|---|---|---|
| **Beat layer** | beat grid | background steps, LED/pixel grids, eye swaps, pulses, montage cuts, palette changes on 8-bar lines | 62% of visual onsets within 1 frame of a beat in the breakout (chance 11%); 98% of strong events in the "perfect hook" reel |
| **Vocal layer** | word times | lyric text, and the big narrative cuts in vocal-led sections | hook cuts land 10–12 frames after the beat, on the sung word; text appears 1–3.5 frames after word start |

Rules:
- Lyrics never snap to the beat. Sung words sit at or below chance on the 16th-note grid [M].
- The beat is the pulse, not the bar. Bar-line locking is weak (6–18%) except for palette and section changes [M].
- Build the grid from **waveform attacks**, not the onset envelope. The envelope runs 34–46 ms late, which makes on-beat visuals look 2–3 frames early [M]. With an attack-anchored grid the audio/video offset is 0 frames.
- Frame for a time: `ceil(t * 60)`.

## 4. Structure of a reel [M/E]

1. **0–0.3 s:** near-empty frame, character present. First motion by frame 14, first text by frame 16.
2. **Hook (to the drop):** biggest type of the reel, one font, one colour, high contrast. Lines arrive on the sung words.
3. **Drop:** kick enters; the beat layer switches on (something steps every beat). Often a hard palette cut.
4. **Body:** one "world" per section; background colour marks the section. Dense small per-beat changes reward a second watch.
5. **Breakdown:** kick out; one visual event (zoom-out, theme wipe, progress bar that completes on the re-entry).
6. **End:** return to the opening picture so the video loops.

## 5. Visual system [M palette, E rest]

- Flat shapes and text drawn in code. No footage, no generated images.
- **One dominant flat background per section** (52–79% of pixels in one colour), two or three accents, one character colour that never changes.
- **Type:** heavy lowercase grotesk for lyrics, about 120 px at 1080 wide (x-height ~64 px, line pitch ~130 px), left-aligned ~84 px from the edge; monospace for any "interface" text.
- **Lyric states:** unsung, current (highlight), sung (greyed).
- Camera is locked off. Movement comes from cuts, pops and stacks; push-ins and pull-outs are saved for drops.
- A pixel character with a few states (off/on, two eye shapes, hop).

## 6. Animation pieces to build first

Minimum set, enough for a breakout-style reel:

| Piece | Clock | Behaviour |
|---|---|---|
| `BeatStepper` | beat | background or texture changes once per beat (or every N beats); instant, no easing |
| `BeatPulse` | beat | instant on, exponential decay within the beat |
| `DropLine` | vocal | text line drops in from above, ~6-frame ease-out |
| `SyllableStack` | vocal | one line per syllable, hard pop in 1–2 frames |
| `KaraokeLine` | vocal | unsung → current → sung-grey |
| `PaletteCut` | bar | hard swap of the whole colour world at a section start |
| `CharacterStates` | both | power-on colour swap on first word; eye swap per beat |
| `CrtOff` / `ProgressRiser` | section | end-of-section collapse; a fill that completes exactly at the drop |

Later: typewriter, counter, ticker, fake-UI cards with a hand cursor, glitch frame, replicate grid, stem-driven characters.

Durations and easing above are judged by eye, not fitted.

## 7. Timing data contract

One JSON file per song, produced by the timing step and read by the video project:

```json
{
  "audio": "song.wav", "duration": 44.6, "fps": 60,
  "bpm": 129.08, "beatPeriod": 0.46482, "beatsPerBar": 4,
  "beats": [0.074, 0.539],
  "bars": [0.074, 1.933],
  "words": [{"text": "word", "start": 0.27, "end": 0.61, "line": 0}],
  "lines": [{"text": "full line", "start": 0.27, "end": 1.9}],
  "sections": [{"name": "hook", "start": 0.0, "end": 7.51, "startBar": 0}],
  "envelopes": {"hop": 0.016667, "kick": [0.0], "rms": [0.0]}
}
```

`bars` holds downbeat times. `envelopes` are sampled once per video frame.

## 8. Production steps

Song first (changed after "allow always"; see sections 9 and 10).

1. Concept (section 1 checklist): the claim, the hook line, a rough story in three or four sentences. No scene list yet.
2. Short lyrics and a Suno style line (section 2). Generate a few takes with room to spare.
3. Pick the best 30–45 s loop by ear and cut it to whole bars.
4. Timing step → timing JSON. Check the BPM, the drops and the bar count by ear and against the waveform; check the words with a transcription.
5. Pick the place and the hero object (section 10), then make one still and a five-second test. Compare with a reference frame.
6. Storyboard as an animated HTML page, written to the loop that exists: what changes state on which bar.
7. Build in HyperFrames; render; measure the render's sync with the same scripts used on the reference reels.
8. Caption: hook line, context, "details if you replay it", credits, genre tag.

## 9. Lessons from making "allow always"

Tags as above, plus **[R]**: from our own review of storyboard drafts (the creator's judgement, not data).

**Story**
- **One causal chain, no loose gags [R].** Every scene must cause the next one. Draft 3 (2FA code, standup, "i am dave") had funny pieces that did not follow from each other, and read as illogical rather than funny. Draft 6 is a single chain: tired human, auto-approve, the agent answers itself, the human sleeps, the agents talk, the city.
- **The ending needs a twist, not an echo [R].** "may we / yes" repeated the opening more quietly and fell flat after the biggest drop. The ending that worked is a punchline the viewer recognises: morning, nothing seems to have happened, the human still says yes, and the last ask is recursive ("may i auto approve auto approve"). Funny because it is true of the audience; scary because nothing visibly changed and the loop restarts.
- **Use the real interface [R].** The actual Claude Code prompt (`Do you want to proceed?` / `1. Yes` / `2. Yes, and don't ask again` / `3. No`) and its status line beat any invented dialog. Engineers know it by heart, so editing it (three Yes options, no No) is a joke that works with the sound off.
- **Details only the viewer reads [H].** Small text the character ignores (`created 03:02 by 4,096 authors`, `48,112 actions approved`) rewards a second watch.

**Picture**
- **Escalate [R].** Start quiet and plain; each loud section must be visibly wilder than the last (bar 10: palette flash and shake; bars 17–21: houses, city, swarm, glitch, ∞). Quiet sections between them make the next one hit. Even the calm ending can be loud in a different colour (a sunrise that is too fast and too big).
- **Mix looks [R].** Not only illustration: a real terminal, giant type, pixel characters, a chat, a street of houses, a city. A change of look marks a change of section.
- **Characters you can tell apart [R].** The main agent is a fixed design; the others share its body but each gets its own colour, its own hat and a cryptic name (`0x7F3A`, `nul_void`), not "Priya's agent". Different people need different hair, skin and shirt colours. Whether colour and hat read at phone size is still unchecked.
- **The human wears out visibly [R]:** pixel states awake, tired (eye bags, coffee cups), asleep.

**Music**
- **Write the escalation into the song too [H, not yet confirmed by ear].** Each drop's section tag adds layers (`acid bass and open hi-hats added`, then `densest part, distorted bass, rising siren synth, snare roll`), with `each drop bigger than the last` in the style line, and silent breaks before each drop (`all music stops`).
- **Duration Custom 0:55 gave two takes of exactly 0:55 [M]** for 30 short lines (third generation).
- **Leave room for the ending [M].** With 33 lines and Duration 0:55 (fourth generation, take 1), Suno never made the drumless sunrise outro. It squeezed the last two asks into the final drop at 50–54.6 s, with the kick still running, and the last "approve" ends right at the cut. Planned length (27 bars ≈ 52 s at 124 BPM) plus about 10 s is a safer Duration.
- **Check word timing with a transcription [M].** The forced aligner in `timing.py` still places words Suno never sang, stacking them on top of each other (the whole "yes yes yes" chant landed at 16.3 s). Stacked or zero-length lines mean the words need checking. A Whisper pass on the Demucs vocal stem (`diagnostics/allow-always/tail_words.py`) shows what was actually sung.
- **Change lyrics before generating, not after.** An ending changed after generation costs a whole new Suno run and a download.

**Workflow**
- **Storyboard first, as one animated HTML page [R].** Lyrics and picture side by side per scene, frames that step at the song's tempo, a 24–27 bar strip whose bar heights show how wild each section gets, a character sheet, and one open question per scene. The creator iterates on this page; only then lyrics go to Suno.
- **Two-pass sync [H].** The storyboard animates on an assumed tempo. Once the take exists, run the timing step and move every step to the measured beats and words, then adjust beat-level moments by eye.

## 10. Visual grammar: how their frames are built, and why ours fell short [E]

Graphic study of three reference reels against our own first cut and storyboard. Everything here is judged by eye from the 2 fps contact sheets in `downloads/frames/<id>/` and from full frames; nothing is measured. Reels studied: `DfHnQTcSDi6` (2 AM desk, a story reel like ours), `Demq1znuXjZ` (road signs, one world), `DfAdDZXMc21` (the breakout, mostly type). Ours: `video/out/aa-snaps/contact-sheet-*.jpg` and `songs/allow-always/storyboard.html`.

### What they do

- **The frame is a place, not a layout.** Every reel is one drawn location seen from one fixed viewpoint: a desk with a monitor, lamp, blinds, shelf, pumpkin and clock; a highway in one-point perspective; a circuit board. The viewer always knows where they are. There is no header, no margin column and no stack of panels.
- **One hero object at the centre, and it is big.** The monitor, the road sign or the chip sits on the vertical centre line in the upper-middle of the frame and is roughly 40–70% of the frame width. Everything else is set dressing around it.
- **The lyric lives on the hero object.** Road reel: the words are the road sign, and the sign's shape changes with the line (stop sign, green guide sign, warning diamond). Desk reel: the words type into the monitor's terminal line with a block cursor. Only the breakout uses free-floating type, and it uses nothing else. The lyric is never a caption under the picture.
- **One line on screen at a time**, replaced in place. Current word bright, sung words grey. The eye never has to move to find the text.
- **The world holds still; state changes inside it.** For 10–30 seconds the layout does not change at all. What changes: the screen content, the sign, the sky colour, lights on or off, a second character appearing. The 2 AM reel holds the same desk for about 45 seconds and only the monitor contents change.
- **Cuts are rare and are the story beats.** Road reel: a hard swap from lime day to black night at the turn, same road. Desk reel: one cut into the "cemetery desktop", then a zoom out of the big character's eye back to the desk for the ending. Each big move happens once.
- **The camera move is saved for the reveal**, and it is a real move (a pull-back through an object), not a scene change.
- **Small things tick on the beat, the hero follows the voice.** Keyboard keys light in patterns, lane dashes and roadside posts scroll, an LED strip steps, a clock digit changes, a countdown number drops. These are small and at the edges. The hero object changes on the sung word.
- **A tight palette with one owned colour.** One dark or one loud background, greys for the world, and the character's orange as the only saturated warm colour in the frame. Accents (red clock, lime sky, pink highlight) are single-purpose.
- **Shapes are flat vector with real drawing in them**: perspective, overlapping layers, soft fog, a vignette, light falloff from the monitor, thin outlines on signs. Only the character is pixel art, so it stands out from the world it lives in.
- **The character is small but always in the same spot**, at the centre, and reacts with tiny changes (eye shape, a hop, a second eye colour). When it becomes large, that is the scare or the punchline.
- **Empty space is allowed.** The bottom third of the desk reel is plain dark desk; the road reel's lower half is plain asphalt. Instagram's caption and buttons cover that area anyway.
- **Details are real things drawn accurately**: road signs in the right shapes and typeface, a macOS menu bar with a date, notification pills, file names on tombstones. These are the replay details.

### What ours did

- **A dashboard, not a place.** Path and clock at the top, an LED row, a counter, a character, a panel, a lyric line: a column of UI parts on a flat colour. Nothing says where we are.
- **Too many small things of equal weight.** Six or seven elements, none dominant. Their frames have one.
- **The lyric is a caption** under the panel, in the same position in every scene, competing with the panel text above it.
- **A new look per scene.** The first cut changes background colour and content every few seconds (navy, pink, black, grid); the storyboard goes further with seven looks (terminal, giant type, chat, houses, city, swarm, sunrise). Their reels change one thing at a time inside one look.
- **Everything is pixel or monospace**, so the character does not stand out from its surroundings, and the frame has no depth: no perspective, no overlap, no light.
- **Mid-size type.** Ours is neither their giant single line nor their small in-world text; it reads as a slide.
- **The story needs a human**, which is the one thing the creator says they cannot draw well. Our pixel human bust is the weakest drawing in the set.

### Rules for the next build

1. **Pick the place first.** One location, one viewpoint, drawn once with depth (perspective or layers, a light source, set dressing). Write down what it is before any scene list. For "allow always" the obvious place is a desk at night with one monitor, seen from the chair.
2. **Pick the hero object** and put it on the centre line, 40–70% of the width. For us: the monitor showing the real permission prompt.
3. **Put the lyric on the hero object.** The ask is the prompt's own text; the "yes" is the option being selected. No caption line.
4. **List what changes state**, not what scenes exist: screen content, clock, room light, window colour (night to sunrise), cups on the desk, who is in the chair.
5. **Budget the big moves:** at most one palette swap, one cut to a second place, and one camera move, each on a section start. Our city reveal should be the one camera move (pull back out of the window).
6. **Show the human by traces, not as a portrait:** a hand or cursor, a chair back, a head silhouette that slumps, coffee cups, a "z". Only the agent is a full character.
7. **Pixel art only for the characters.** Draw the world in flat vector shapes.
8. **Leave the bottom third quiet.**
9. **Before building the reel, make one still and one five-second test** of the main place at full size, and put it next to a reference frame. Only continue if it holds up.

### Their process, from the creator's own replies [M, comments]

- The engine is their own: frames rendered in code (Remotion, TypeScript), synced with WhisperX word times. "80% AI + 20% TypeScript and one human brain".
- **Song first.** They let Suno make a full song, then cut a 30–60 s loop from the best part, and only then write the animation ideas. Full songs "still sound like slop"; often no longer version exists.
- Later reels use Suno stems so each character moves with its own instrument.
- They say they have not worked out how to draw humans.

**What this means for us:** we wrote a 33-line story and asked Suno to perform it bar by bar, and it never did (section 9). Next iteration goes Suno first: a short lyric with a strong hook, a few generations, pick the best 30–45 s loop by ear, measure it, and then write the storyboard to the loop that exists.

## 11. Not yet known

- Word times in the breakdowns came from whisper-small or from visuals, not WhisperX. Text-lag figures are approximate.
- Whether lyric-looping matters is inferred from one reel.
- Stem-driven characters are stated by the creator but not verified in frames.
- Driving a HyperFrames timeline from hundreds of timed events is untested until the round 2 proof.
