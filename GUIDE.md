# How to make a beat-synced lyric reel

This guide shows how we made **"allow always"**: a 2:24 vertical music video for Instagram.

- **The song:** made with Suno.
- **The picture:** drawn entirely in code with [HyperFrames](https://hyperframes.heygen.com) (HTML + GSAP, rendered to MP4).
- **Sync:** every visual is timed to the measured beats and the sung words.
- **Characters:** a cast of illustrated avatars, built from generated sprite sheets.

The guide covers the whole pipeline, the commands that worked, the prompts we used, and the mistakes worth skipping. AI coding agents (Claude Code, Codex) did most of the building. The person directed: they picked the song take, gave feedback on every render, and made the creative calls. We recommend splitting the work the same way.

**Deeper references in this repo:**

| Document | What it covers |
|---|---|
| [`analysis/playbook.md`](analysis/playbook.md) | Why the reference reels work: concept, song structure, the two timing clocks, visual grammar. Measured from ten reels. |
| [`analysis/runbooks/animated-music-reels.md`](analysis/runbooks/animated-music-reels.md) | The sprite and avatar workflow in detail: asset contracts, alpha checks, layering, karaoke. |
| [`analysis/runbooks/image-prompts.md`](analysis/runbooks/image-prompts.md) | Reusable image-generation prompt shapes. |
| [`songs/allow-always/suno-prompts.md`](songs/allow-always/suno-prompts.md) | Every Suno Styles line, lyric file and setting we tried, including the final one. |
| [`video/allow-always-final/index.html`](video/allow-always-final/index.html) | The finished composition, about 1,300 lines, commented by section. |

---

## 1. The pipeline at a glance

```
concept ─► song (Suno) ─► timing JSON ─► look + characters ─► composition ─► review ─► render ─► post
            the person      scripts/        image generation    HyperFrames    snapshots   MP4      caption
            picks the take  timing.py       + sprite sheets     index.html     + check
```

1. **Concept.** One arguable claim that anyone can have an opinion on. Ours: you stop reading the permission prompts and click "allow always".
2. **Song first.** Generate takes in Suno and choose one by ear. The take decides the structure of the video, not the other way round.
3. **Timing.** Measure the beat grid and the sung-word times into one JSON file.
4. **Look and characters.** Pick a place and a hero object. Generate the sprite sheets.
5. **Compose.** Use one paused GSAP timeline. Everything on screen follows either the **beat clock** or the **voice clock**.
6. **Review.** Run `check`, take snapshots at the moments you changed, and send a phone-size render to the person.
7. **Render** a new versioned file each time.
8. **Post** with a caption formula: hook, context, "details if you replay it", credits, one genre tag.

---

## 2. Setup

What we used (macOS). Versions are the ones that worked, not minimums.

| Tool | Version | Used for |
|---|---|---|
| Suno (web) | v6-mini (free), V6 (paid) | the song |
| ffmpeg | 8.0 | audio conversion, phone copies |
| Python `.venv` | 3.14, librosa 1.0, numpy 2.5, scipy 1.18, Pillow 13 | `scripts/timing.py`, sprite packing |
| Python `.venv-align` | 3.12, whisperx 3.8.6, demucs 4.1.0, faster-whisper 1.2.1, torch 2.8 | sung-word alignment |
| Node | 26 | HyperFrames CLI via `npx` |
| HyperFrames | 0.9.2 (pinned) | preview, check, snapshot, render |
| GSAP | 3.15 | the timeline |
| An image generator | we used Codex's built-in `image_gen` | character and effect sprite sheets |

Keep two Python environments. WhisperX pins its own torch and Python version, and it breaks a general audio environment.

```bash
python3 -m venv .venv && .venv/bin/pip install librosa numpy scipy pillow
python3.12 -m venv .venv-align && .venv-align/bin/pip install whisperx demucs faster-whisper
```

Pin the HyperFrames version in every command (`npx --yes hyperframes@0.9.2 …`), so the project renders identically months later.

---

## 3. Concept

The full checklist is in [playbook section 1](analysis/playbook.md). In short:

- **One sentence a stranger could disagree with.** Insider jokes (context windows, prompts) did worse than universal, arguable claims.
- **The picture contradicts or dramatises the claim.** A cute or polite character saying something cold.
- **It works with the sound off.** Use the real interface people know by heart. Our hook is a real-looking permission prompt: `read ../billing-service/.env — outside the approved folder`, with buttons Yes / No / Allow always.
- **One causal chain, not a list of gags.** Every scene causes the next. Ours runs:
  1. The agent asks.
  2. The human says yes.
  3. The human begs it to approve everything by itself.
  4. "allow always".
  5. The agents throw a disco.
  6. A robot hits launch.
  7. The Earth explodes while everyone keeps dancing.
- **The ending loops back to the start** with a twist, not an echo.

---

## 4. The song (Suno)

The full prompt history, including the final Styles line and lyrics, is in [`songs/allow-always/suno-prompts.md`](songs/allow-always/suno-prompts.md). The key lessons:

- **Don't write the story first and ask Suno to perform it.** We wrote a 33-line, bar-by-bar story, and Suno never followed it. What worked:
  1. Write short lyrics around one chant hook.
  2. Generate several takes.
  3. Pick the best by ear.
  4. Write the storyboard to the take that exists.
- **Section tags direct the arrangement.** An a cappella vocoder intro, a one-bar riser, then a full-band drop. Name who sings in every tag. Put answer lines in parentheses.
- **The genre: a strict four-on-the-floor beat with a deadpan robotic vocoder lead.** Add a chant hook with one syllable per beat, and call and response with a tired human voice.
- **Artist names are blocked.** Describe the sound instead.
- **Keep one sound throughout.** Changing instruments per section drifted out of the genre. Use filters, hard stops and silence instead.
- **Measure the tempo.** We asked for 122 BPM and got 125.009.
- **The person picks the take.** After eight agent-prepared generations, the take the reel uses was one the person made and auditioned themselves. The agent's job is to prepare lyrics and Styles lines. The human listens and chooses.
- **Agents driving Suno in a browser:**
  - The lyrics box is a contenteditable DIV. Form-filling fails, so click, select all, delete, then type.
  - The sliders overshoot with the keyboard. Read `aria-valuenow` after each move.
  - Leave bot checks (CAPTCHA, Cloudflare) to the human. Never automate them.
  - Ask before every credit spend and every download.

---

## 5. Timing: beats and sung words

Everything downstream reads one JSON file per song. The contract is in [playbook section 7](analysis/playbook.md): `bpm`, `beats`, `bars` (downbeats), `words`, `lines`, `sections`, per-frame `envelopes`.

### 5.1 Beat grid

```bash
.venv/bin/python scripts/timing.py songs/<song>/<take>.mp3 \
  --lyrics songs/<song>/<lyrics-plain>.txt -o out/timing/<song>.json
```

- It assumes one fixed tempo. The BPM comes from a comb search over the onset envelope, and the kick decides beat versus off-beat.
- It then **moves the grid onto waveform attacks.** The onset envelope runs 35–45 ms late, which makes on-beat visuals look 2–3 frames early.
- Downbeat: the beat position where the sub-80 Hz level jumps most, which is where the kick enters or stops.
- Sections: runs of bars with kick versus without kick. These became our scene boundaries.
- Our result: 125.009 BPM, downbeat at 0.399 s, 76 bars, 14 sections, median onset scatter 8 ms.

### 5.2 Sung words

`scripts/align_words.py` runs in `.venv-align`:

1. **Demucs (htdemucs)** isolates the vocal stem. This is the step that matters: on the full mix, Whisper skipped most of the sung words.
2. **faster-whisper large-v3-turbo** transcribes it (CPU, int8).
3. **WhisperX / wav2vec2** force-aligns each word.

Before you align:

- **Make a plain lyrics file.** Strip `[section]` tags and `(robot)` / `(human)` prefixes, and fix typos. Ours is `songs/allow-always/lyrics-final-plain.txt`.

What went wrong and how we fixed it:

- **Suno doesn't sing what you wrote.** It doubled lines, added words and reordered the second half. The plain forced alignment lost its place after 41 s. The fix:
  1. **Listen first.** Transcribe the vocal stem with word timestamps to see what was really sung.
  2. Write the sung lines down with a time window each, as in `songs/allow-always/align_final.py`.
  3. Force-align each line **inside its own window**.
- **Whisper mishears sung vocoder words.** "Like always" for "allow always", "yo yo yo" for "yes yes yes". Decide what was sung, flag the guesses, and confirm them by watching the render.
- **Watch for stacked or zero-length words.** They mean the aligner placed words that weren't sung. Tighten the windows. Ours had "free" colliding with the next "yes!".
- Back up the timing JSON before each re-run.

### 5.3 Export to the video

`songs/allow-always/cut_final.py` does two things:
- converts the take to a 48 kHz WAV;
- writes `video/data/<song>.json` plus a `.js` copy (`window.TIMING = …`), which the composition loads with a plain `<script>` tag.

---

## 6. Look and characters

### 6.1 The frame is a place

[Playbook section 10](analysis/playbook.md) is the most useful part of the playbook. The reference reels draw **one place from one viewpoint**, with **one big hero object** in the centre carrying the lyric. Small things tick on the beat around it. Our first cut was a dashboard of small UI parts, and it didn't work. The final reel has two places:

- **The desk world:** a big permission dialog as the hero object, a cursor, a log of approved commands and an LED row on the beat.
- **The disco:** a retro orbital discotheque with a window onto space and the Earth. The avatars take over the screen there.

### 6.2 Sprite sheets from an image generator

The full workflow, with contracts, alpha checks and packing, is in the [runbook](analysis/runbooks/animated-music-reels.md). The lessons that mattered most:

- **Audition styles on one grid.** Generate a numbered 4×4 board of styles and let the person pick by number.
- **Show reference images instead of describing a style.** "80s anime" in words came out glossy and exaggerated. Three reference frames fixed it at once.
- **One character per sheet.**
  - Close-ups: a 3×3 sheet of angles and expressions.
  - Dances: a 4×4 sheet of 16 successive poses over one four-beat bar.
  - Describe the motion (weight shifts, foot taps, a last-to-first loop seam), not random poses.
- **Action inserts are sheets too.**
  - The robot at the console: a 3×3 sheet over its shoulder; frames 0–5 press buttons, 6 reaches, 7 hits launch, 8 recoils.
  - The planet explosion: a 3×3 sheet from spark to smoke, peaking at frame 4. Play it once, then hide it.
  - Record the key frame numbers with each file. They changed between revisions.
- **Separate layers:** a starfield, a planet cutout, and a ship interior with a transparent window. This let us drift the planet and put explosions between the planet and the window frame.
- **Check alpha for real.** Look at the sheet over light and dark backgrounds, and check the gutters. A painted checkerboard is not transparency.
- **Pack the sheets.** `video/avatar-dance-test/prepare_assets.py` packs equal cells, removes stray alpha specks, and anchors dancers' feet to one floor line.
- **Prove it small first.** We built an 11.5 s dance test (`video/avatar-dance-test/`) before putting the avatars in the full reel.

Playing a sheet from composition time, for an N×N grid:

```js
// background-size: N*100% N*100%
const pos = (i, N) => `${((i % N) * 100) / (N - 1)}% ${(Math.floor(i / N) * 100) / (N - 1)}%`;
```

The dancers step one pose every quarter beat, so 16 poses fill one bar. Each dancer starts at a different phase (0, 8, 4), so the group doesn't move in lockstep.

---

## 7. The composition (HyperFrames)

### 7.1 Structure

- **One HTML file**, 1080×1920 at 60 fps, `data-duration` set to the song length.
- **One paused GSAP timeline**, registered as `window.__timelines["main"]`.
- **Every time comes from `window.TIMING`.** No hard-coded seconds.
- **Shared helpers** live in `video/src/beatsync.js`:
  - `at(t)`: an event at time *t* shows first on frame `ceil(t × fps)`. Use it for every `set`.
  - `BeatStepper`, `BeatPulse`, `KaraokeLine`.
- **Small local helpers:** `bar(n)`, `L(i)` (a sung line), `W(i)` (its words), `beats(from, to)`.
- **Rules that keep renders identical:**
  - No `Math.random()`: use a seeded generator (we used Lehmer and mulberry32).
  - No timers, no `Date.now()`, no infinite repeats.
  - Every state must be reproducible when seeking backwards.

### 7.2 Two clocks

This is the core idea, measured in the reference reels ([playbook section 3](analysis/playbook.md)).

| Clock | Drives |
|---|---|
| **Beat** | Things that step on the beat: LEDs, pulses, dance poses, console frames, explosions, the approved-commands log, the "yes" clicks. |
| **Voice** | Things that follow the singer: the lyric captions, the big narrative cuts, the close-ups that show one face per sung "yes". |

Lyrics never snap to the beat. They appear when the word is sung.

### 7.3 Patterns we built (find them by their comments in `index.html`)

**Dialog**
- A new prompt for each ask, with real commands in monospace (`git push origin main`, `npm install left-pad`).
- With every ask the Yes button grows and the No button shrinks.

**Cursors**
- The human's cursor slows and droops as the song goes on, then falls asleep (z's rise).
- Then the agent's cursor takes over the mouse.

**Karaoke captions, three looks**
- **Neon:** heavy uppercase skewed words with a glow. The human's lines are pink, the agent's cyan.
- **VHS closed captions:** monospace in black boxes, each word appearing when it is sung.
- **RGB glitch:** for the shock lines. Each sung word jolts sideways with a red/cyan split.

**Chant**
- One giant word per sung "yes", stacked four high, then cleared.
- Lines the giant words already spell out get no caption.

**Disco visits**
- The avatar world drops into the lyric video three times: at the first big drop, as close-ups on each sung "yes!", and across the instrumental outro.
- The outro is a six-bar routine played three times so that it lands exactly on the loop cut.

**The punch**
- After the second "wait, wait, what did you approve?", two short console inserts are cut between the dancing: the robot presses a few buttons, and later it reaches for launch and hits it.
- Then the Earth takes one explosion per sung "yes", and after that it keeps exploding every beat, at three nudged spots. The humans dance on, unbothered.

**80s VHS pass**
- Tape tears at every section change.
- A tracking band rolls down the frame.
- Earlier avatars flicker through in torn red/cyan slices.
- A `PLAY ▶` HUD and tape counter play during the disco.
- All of it is seeded, so every render glitches the same way.

**Hook and loop**
- The first frame and the last two seconds are the same permission dialog, with the cursor hovering over "Allow always".
- So when Instagram loops the reel, the end flows into the start.

### 7.4 Gotchas

- **GSAP can't tween between `textShadow` lists of different lengths.** Always keep three shadows. At rest the red and cyan ones have zero alpha.
- **Animate a number, not a `clip-path` string.** Karaoke fills interpolated wrongly as strings. Tween a CSS custom percentage instead.
- **Keep captions off faces and helmets.**
  - Move the caption to a top band during close-ups.
  - Hide a line early when an insert cuts in over it.
  - Check every close-up frame.
- **Make the loop frame match frame 0 exactly.** Turn off the beat layer, the pulse and the LEDs before the loop cut, or the seam blinks.
- **Mind the z-order of effects.** Explosions go above the planet and below the ship's window frame. Inside the disco the order is space, planet, explosions, ship, then the close-up shots.
- **Extend a scene until its last effect finishes.** The third explosion was cut off until the scene ran two beats longer.
- **Uninstalled registry items still clutter.** We installed HyperFrames registry blocks for ideas (`camcorder-hud`, `caption-glitch-rgb`, …), wrote our own versions inline, and then had to remove the unused installs.
- **A Node script reading the `.js` timing file hung.** Read the JSON file instead.

---

## 8. Review and render

```bash
cd video/<project>
npx --yes hyperframes@0.9.2 check
npx --yes hyperframes@0.9.2 snapshot --at 1.5,13.5,64.7 --no-end -o ../../diagnostics/<dir>
npx --yes hyperframes@0.9.2 render -o ../out/<name>-v3.mp4      # ~4–7 min for 2:24 at 60 fps
ffmpeg -i ../out/<name>-v3.mp4 -c:v libx264 -crf 26 -vf scale=720:-2 -c:a aac -b:a 160k ../out/<name>-v3-phone.mp4
```

**What `check` caught for us:**
- giant chant words overlapping the character (fixed by hiding the character during chants);
- UI text hidden under the disco layer;
- decorative marks flagged as overlaps (marked `data-layout-ignore`).

Two warnings are fine to accept:
- `line_unread` on deliberately short flashes (rule of thumb: hold a line 0.5 s plus 0.3 s per word);
- a few pixels of text below the safe floor.

**Snapshot the exact moments you changed** and look at them before rendering. A passing check doesn't show how it looks.

**Never overwrite a render.** Give each version a new name (`-80s`, `-80s-boom`, `-80s-boom2`) so you can compare. Copy the HTML to a backup before each big pass.

**Send the phone copy** (720p, about 11 MB instead of 67 MB) for review. That is how the reel will be watched.

**Inspect the encoded MP4, not only the preview.** Some bugs, like the karaoke fill, only show up there.

---

## 9. Working with an AI agent: what the feedback loop looked like

Most of the quality came from short, blunt notes on rendered videos. What the person said, and the change that fixed it:

| Feedback | Fix |
|---|---|
| "not viral enough" / "not smart or sophisticated, we need to capture the current" | Lyrics reframed around agents taking over the developer's job. |
| "the style is different from daft punk now" | Back to one sound; sections change with filters and stops instead. |
| "we need more dramatic stops" | `dramatic hard stops and dead silence before every drop` in the Styles line. |
| "slowly somewhere in the video we move to this" (the avatar test) | Three disco visits instead of one long scene. |
| "80s style, glitches, camera effects, karaoke all the way" | The VHS pass and the three caption looks. |
| "when there are already subtitles, like in the yes yes yes, we don't need captions on top" | No captions over the giant chant words. |
| "the first hook tells what's going to happen" | The loop hook: the same hesitating "Allow always" dialog at both ends. |
| "make sure the captions are not on the faces or helmets" | A top caption band for close-ups; lines hidden early before inserts. |
| "not sure we need the lasers" | No lasers: the launch goes straight to explosions. |
| "maybe after it asks the second time 'wait what did you approve'" | The punch moved to answer that line. |
| "too frantic … divide into two parts" | Console frames every half beat; two inserts with dancing between. |
| "the earth should explode all the time after the first explosion" | A seeded explosion every beat until the scene ends, again in the outro. |

Habits that made this work:
- **The agent proposes, the person decides.** On open questions, give two or three options with a recommendation, not a survey.
- **Ask before anything that costs money or can't be undone:** Suno credits, downloads, posting.
- **Mark guesses as guesses**, such as misheard lyrics, likeness concerns or rights, and confirm them on the render.
- **Change one thing per render** and say exactly which seconds changed, so the person knows where to look.
- **Keep the person's words close.** "Too frantic" meant slower *and* split in two. Ask when a note could mean two things.

---

## 10. Posting

[`songs/allow-always/instagram-brief.md`](songs/allow-always/instagram-brief.md) is a ready-made brief for an agent that runs the Instagram account. The essentials:

- **Upload the full-quality file** as a Reel, unchanged, with the original audio. Don't trim the ends, or the loop breaks.
- **Cover:** a strong frame from inside the video.
- **Caption formula:**
  1. hook line;
  2. one or two lines of context;
  3. "Details if you replay it" (three or four small things only a second watch catches);
  4. a credit line naming the tools;
  5. **one** genre hashtag.
- **Keep the bottom third quiet.** Instagram's caption and buttons cover it.
- **"Comment LOOP for the code"** plus a link in the bio. Links in captions and comments aren't clickable.
- **Nothing gets posted without the person's approval.**

Open questions to settle before you post your own:
- **Rights:** commercial use of a Suno song depends on your Suno plan.
- **Likenesses:** our robot helmets resemble a famous duo's. We flagged it and kept them, which is a judgment call.

---

## 11. Dead ends (skip these)

**Story and song**
- A long, bar-by-bar story for Suno to perform.
- Suno on Duration Auto with "stadium anthem" styles: 3-minute takes.
- A different instrument for every section: out of genre.
- Extend on the free plan to rewrite a second half: Replace Section is paid, and starting over was faster.

**Alignment**
- Whisper on the full mix.
- Plain forced alignment against lyrics Suno didn't sing as written.
- `align_words.py` without `--lyrics`: it crashes (an IndexError). Transcribe the stem with timestamps instead.

**Picture**
- A dashboard of small UI parts instead of one place with one hero object.
- A text-only style prompt for characters.
- A big title-card hook that gave the ending away.
- Fast, frantic console clicking.

---

## 12. Repo map

| Path | What |
|---|---|
| `scripts/timing.py`, `scripts/align_words.py` | Beat grid and sung-word alignment. |
| `songs/<song>/` | Lyrics, Suno prompts, take, alignment and cut scripts, storyboard, Instagram brief. |
| `video/src/beatsync.js` | Shared timing helpers. |
| `video/data/` | Timing JSON and JS per song. |
| `video/allow-always-final/` | The finished reel. |
| `video/avatar-dance-test/` | Avatar prototype, sprite sheets, prompts, packer, karaoke builder. |
| `vendor/page-mascot/` | MIT avatar tools we adapted ([notes](analysis/avatar-pipeline.md)). |
| `analysis/` | Playbook, runbooks, per-reel breakdowns. |
| `video/out/`, `out/`, `diagnostics/` | Renders, intermediate audio, one-off scripts (all gitignored). |
