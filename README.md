<h1 align="center">onbeat</h1>

<p align="center"><strong>Give your coding agent a song. Get back a beat-synced lyric reel.</strong></p>

<p align="center"><img src=".github/sprite-dance.gif" width="840" alt="A 4 by 4 robot sprite sheet with the current pose highlighted, the robot dancing through those poses, and the song's sound bars with a mark on every measured beat"></p>

<p align="center"><sub>Left: the sheet, with the pose on screen highlighted. Right: the same sheet, stepped by the beat. Bottom: the song, with a mark on every beat measured from it.</sub></p>

<details>
<summary><b>▶ Watch with sound</b></summary>

https://github.com/user-attachments/assets/21d5e499-cfd0-425b-9b77-3e270fb0f3f0

</details>

<table>
  <tr>
    <td width="33%"><video src="https://github.com/user-attachments/assets/79c3ae9a-1460-4bc8-b06d-348ebfaf9b23" controls></video></td>
    <td width="33%"><video src="https://github.com/user-attachments/assets/5ffe9794-b99c-476b-b27c-0044d51e0f63" controls></video></td>
    <td width="33%"><video src="https://github.com/user-attachments/assets/ba9085e6-6655-48e6-92cb-39f54c828499" controls></video></td>
  </tr>
  <tr>
    <td align="center"><b>Disco</b><br><sub>agent-directed</sub></td>
    <td align="center"><b>Terminal</b><br><sub>same song, another look</sub></td>
    <td align="center"><b>The sample</b><br><sub>the bundled example</sub></td>
  </tr>
</table>

<p align="center"><sub>Turn the sound on. Every move, cut and word lands on a beat measured from the audio.</sub></p>

onbeat is a skill for **Claude Code** and **Codex**. It teaches your agent to measure the beats and sung words of a song and to write a [HyperFrames](https://hyperframes.heygen.com) scene that moves on those times. The result is a vertical 1080×1920 MP4 for Reels, Shorts and TikTok.

## Sprites, not a video model

The dancers aren't generated video. An image model draws one sheet of 16 poses, once. onbeat measures the beats in the audio and steps through those poses on them: a new pose every quarter beat and a small hop on every beat. So every move lands on the beat, the character looks the same in every frame, and a re-render costs nothing.

## Install

**Any agent, one command** ([skills.sh](https://skills.sh))

```bash
npx skills add latent-spaces/onbeat
```

It asks which agents to install for (Claude Code, Codex and others) and copies the skill into your project. Add `-g` to install it for all projects.

**Claude Code plugin**

```text
/plugin marketplace add latent-spaces/onbeat
/plugin install onbeat@onbeat
```

**Codex plugin**

```bash
codex plugin marketplace add latent-spaces/onbeat
codex plugin add onbeat@onbeat
```

Or copy the [`skills/onbeat`](skills/onbeat) folder into your agent's skills folder. It is self-contained.

## Use it

Ask in plain words:

> Render the onbeat example.

> Make a beat-synced reel for ~/Downloads/my-song.mp3. Neon city at night, karaoke lyrics.

The agent measures the song, then works with you on the concept and a simple story. Supply reference images if you have them: they can guide the actual character/style or provide context. You choose between rough visual directions before production assets are made. A short dancing draft comes next; you review it with sound, then the agent iterates and extends the agreed direction into the full reel.

Higgsfield and Codex's built-in image generator are the main image routes. In Codex, the built-in generator is the default. Dancing avatars keep the character design you approved; friends can join on measured bar downbeats.

## Try it without an agent

The example renders by itself. You need Node 22+ and ffmpeg, and no keys or accounts.

```bash
git clone https://github.com/latent-spaces/onbeat && cd onbeat/skills/onbeat/example
```

```bash
npx --yes hyperframes@0.9.2 render --output out/example.mp4
```

The first render downloads HyperFrames and a headless browser once.

## How it works

```
song.mp3 ──► timing.py ──► timing.js ──► the scene your agent writes ──► HyperFrames ──► reel.mp4
```

There are two clocks, both measured from the audio. The **beat clock** drives the pulses, cuts and dance poses. The **voice clock** drives the lyrics. Every frame is a pure function of the song time, so a render comes out the same every time.

The design of each scene is left to the agent, so the reels get better as models do. The measuring is code, because a model can't hear the beat.

## What's inside

```
skills/onbeat/
  SKILL.md      the method: measure, write one scene, check the sync, render
  references/   render rules, beat motion, character sprites
  scripts/      timing.py (beats, bars, words) and sprites.py (checks character sheets)
  example/      a complete 11.5-second reel to copy and rewrite
```

The disco and terminal videos above are earlier agent-directed demos. The bundled example is the reproducible starting point in this package.

## Setup, data and costs

The agent reads your audio/reference files, writes a reel folder and runs local analysis and rendering commands. Rendering needs Node 22+ and ffmpeg; beat analysis adds a Python environment with the pinned dependencies in `scripts/requirements.txt`. Optional word alignment uses a separate Python 3.12 environment and large local speech/separation models. First use downloads packages, a headless browser, models and potentially fonts; the audio-analysis scripts themselves run locally. Your coding agent's data handling depends on its provider and settings. Image generation sends prompts and supplied reference images to the selected provider and may use credits. The skill asks before paid generation and does not publish your reel.

## Limits and verification

The beat tracker assumes one fixed tempo and defaults to four beats per bar. Kick-based downbeat/section detection suits a clear regular drum pulse; changing tempo, unusual meters, weak percussion and expressive vocals need closer review. Word recognition and alignment can miss or mishear lyrics, so inspect the sync overlay and disclose estimated words. A visual review is not an independent numeric proof of beat accuracy.

Run `node --test tests/` for the helper regressions and `bash skills/onbeat/scripts/smoke.sh` for a scratch-copy check, render and MP4 probe.

## Status

This is an early release (v0.2). The bundled example and helper tests pass. An assisted unfamiliar-song session exercised concept choices, reference-led character graphics, a short three-character dancing draft and a visual revision. It required intervention, so it is not an unedited first-try result. A cold plugin install, fresh word-alignment install, broad genre coverage, independent repeatability and a controlled with/without-OnBeat comparison remain unverified. The Higgsfield sprite route only prints its commands.

## Credits and licence

- **MIT licence.** See [LICENSE](LICENSE). Third-party components retain their own licences.
- The sprite-sheet approach is adapted from [page-mascot](https://github.com/nilbuild/page-mascot) by Kamran Ahmed (MIT). See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- [HyperFrames](https://hyperframes.heygen.com) by HeyGen renders the video and GSAP drives the timeline. Word alignment uses WhisperX, faster-whisper and Demucs.
- The song "allow always" was made with Suno by the repo owner.
