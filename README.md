<p align="center">
  <a href="assets/readme/preview.mp4"><img src="assets/readme/preview.gif" alt="An illustrated robot dances in a spaceship lounge while pink karaoke captions sing 'I don't wanna click no more', cut to the beat" width="320"></a>
</p>

<h1 align="center">music-reels</h1>

<p align="center"><strong>Song in, beat-synced lyric reel out. Your coding agent does the edit.</strong></p>

<p align="center">
  A Claude Code + Codex skill and a small CLI that measure a song's beats and sung words and drive a <a href="https://hyperframes.heygen.com">HyperFrames</a> reel from them. The output is a vertical 1080×1920 MP4, ready for Reels, Shorts and TikTok.
</p>

<p align="center"><sub>Above: 6 s of an 11.5 s render from the chorus of "allow always". <a href="assets/readme/preview.mp4">Watch it with sound</a>. Status: <b>early release (v0.1)</b>.</sub></p>

---

## Quickstart

```bash
git clone https://github.com/oronanschel/music-reels && cd music-reels
make doctor   # checks node, npx, ffmpeg and prints a fix for anything missing
make sample   # renders the bundled sample -> out/sample.mp4 (no keys, no accounts)
```

The first render downloads HyperFrames and a headless browser once. After that, the sample rendered in about 15–17 s on an Apple M4 laptop. Step-by-step, with the expected output for each step: **[docs/TRY-IT.md](docs/TRY-IT.md)**.

### Use it from your agent

<sub>The install commands follow the Claude Code and Codex plugin formats, and their syntax was checked. A fresh install has not been tested yet.</sub>

**Claude Code**

```text
/plugin marketplace add oronanschel/music-reels
/plugin install music-reel@music-reels
```

Then: *"Render the music-reels sample"* or *"Make a beat-synced reel for songs/my-song"*.

**Codex**

```bash
codex plugin marketplace add oronanschel/music-reels
codex plugin add music-reel@music-reels
```

Or open the cloned repo in Codex. It reads `AGENTS.md` and `.agents/skills/music-reel/` by itself.

**Any agent:** point it at [`skills/music-reel/SKILL.md`](skills/music-reel/SKILL.md).

## Make a reel for your own song

```bash
mkdir -p songs/my-song && cp ~/Downloads/my-song.mp3 songs/my-song/song.mp3
make setup                     # once: Python .venv with pinned requirements
make timing SONG=my-song       # beats only: BPM, beats, bars, sections, kick
make render SONG=my-song       # template reel -> out/my-song.mp4
```

Add `WORDS=1` to `make timing` for word-by-word karaoke (needs the alignment environment, see [GUIDE.md §2](GUIDE.md#2-setup)). Change the title, palette, captions and cast in `songs/my-song/reel.json`. You don't need to edit any HTML.

## What you get

- **Beat and word timing**: a fixed-tempo beat grid, downbeats, kick/no-kick sections and envelopes. Sung-word alignment is optional (`scripts/timing.py`, `scripts/align_words.py`).
- **A song-agnostic template** (`video/template/`): a reel driven by `timing.json` plus a small `reel.json`.
- **Beat-synced character motion**: a pose per beat, a bounce on the kick, an accent on the bar downbeat, and a phase offset per character ([docs/beat-motion.md](docs/beat-motion.md)).
- **Sprite generation with one asset contract**: Codex built-in image generation, or Higgsfield (an adapter that only prints its commands; untested). Both write `sprites.json`, with keying plus alpha and drift checks ([docs/sprites.md](docs/sprites.md)).
- **A sync-check overlay**: beat ticks and word marks in preview, so you can check timing before a long render.
- **The full story of a finished reel**: [GUIDE.md](GUIDE.md) shows how the 2:24 "allow always" video was made, with prompts, commands, dead ends and the human–agent feedback loop.

## How it works

```
 song.mp3 ──► make timing ──► timing.json ─┐
 (Suno or any)  beats · bars · words       │
                                           ├─► video/template ──► make render ──► out/<song>.mp4
 reel.json ────────────────────────────────┘    HyperFrames + GSAP    1080×1920
 title · palette · captions · cast              beat clock + voice clock
        ▲
 sprites.json ◄── docs/sprites.md (Codex image gen / Higgsfield)
```

There are two clocks. The **beat clock** drives pulses, cuts and dance poses. The **voice clock** drives the lyrics. Every visual is a pure function of timeline time, so a render is identical every time.

## Repository map

| Path | What |
|---|---|
| `skills/music-reel/` | the agent skill (Claude Code plugin, Codex plugin, `.agents/skills`) |
| `Makefile`, `scripts/` | doctor, sample, timing, render |
| `video/template/` | the song-agnostic reel |
| `video/src/` | shared timing and motion helpers (`beatsync.js`, sprite dance) |
| `video/avatar-dance-test/` | the bundled no-key sample |
| `video/allow-always-final/` | the hero reel from GUIDE.md |
| `songs/` | one folder per song |
| `analysis/` | the playbook (what makes these reels work) and production runbooks |
| `docs/` | try-it script, beat motion, sprites, project history |

## Credits and licence

- **Licence: not chosen yet.** See [LICENSE](LICENSE). Until the owner picks one, no reuse rights are granted.
- Sprite-atlas approach adapted from [page-mascot](https://github.com/nilbuild/page-mascot) by Kamran Ahmed (@nilbuild), MIT licence; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The reel's dance and action art was generated separately.
- **HyperFrames** by HeyGen renders the video. **GSAP** drives the timeline. Word alignment uses **WhisperX**, **faster-whisper** and **Demucs**.
- The song "allow always" was made with Suno by the repo owner.

History of the project before packaging: [docs/history.md](docs/history.md).
