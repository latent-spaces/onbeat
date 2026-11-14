# Try it: first run, step by step

A script for testing music-reels from a brand-new agent session that knows nothing about the repo. Each step lists what to type and what you should see. If a step doesn't match, stop there and note it.

Time: about 10 minutes to the first render (most of it is the one-time HyperFrames download), plus about 10 more for your own song.

## Before you start

- macOS or Linux with **Node 22+**, **ffmpeg** and **git**. Python 3.12+ is only needed from step 5.
- The repo must be readable by your GitHub account. It is private until the owner makes it public.

## Step 1: install the skill

**Claude Code** (in any folder):

```text
/plugin marketplace add oronanschel/music-reels
/plugin install music-reel@music-reels
```

Expected: Claude Code confirms that the `music-reel` plugin is installed. Restart the session if it asks.

**Codex:**

```bash
codex plugin marketplace add oronanschel/music-reels
codex plugin add music-reel@music-reels
```

**No installer:** clone the repo (step 2) and open the folder in your agent. It reads `CLAUDE.md` / `AGENTS.md`, which point to the skill.

## Step 2: ask for the sample

Type exactly:

> Render the music-reels sample.

Expected: the agent asks where to put the repo (or uses the current folder if that's already the clone), then runs:

```bash
git clone https://github.com/oronanschel/music-reels && cd music-reels
make doctor
```

`make doctor` should print something like:

```
Needed for 'make sample' and 'make render':
  ok    node v26.x
  ok    npx
  ok    ffmpeg 8.x
  optional hyperframes CLI not cached yet
        fix: nothing to do: the first 'make sample' downloads hyperframes@0.9.2 ...
Needed for 'make timing' (your own song):
  ok    python3 3.x
  optional .venv not set up
        fix: make setup
...
Ready: run 'make sample'.
```

Any `missing` line comes with a `fix:` command. Run it, then run `make doctor` again.

## Step 3: first render

The agent runs `make sample`.

Expected:
- A progress bar, then `Render complete` and `Sample written to out/sample.mp4`.
- The first run downloads HyperFrames 0.9.2 and a browser, which takes a few minutes. Later runs took about 15–17 s on an Apple M4 laptop.
- `out/sample.mp4`: 1080×1920, about 11.5 s, about 7 MB, with sound.

Open it. You should see the robot dancing in a spaceship lounge, karaoke-style captions ("I DON'T WANNA CLICK NO MORE…"), and cuts and poses landing on the beat.

## Step 4: check the skill knows the rules

Ask:

> What do you need from me to make a reel for my own song?

Expected: the agent asks for an audio file and lyrics (optional), offers to draft a Suno prompt, and says that **you** generate the song in Suno. It shouldn't offer to log in to Suno or to run a paid image generation.

## Step 5: your own song (beats only)

Put an MP3 in a new song folder (any song with a steady beat works):

```bash
mkdir -p songs/my-song && cp ~/Downloads/my-song.mp3 songs/my-song/song.mp3
```

Then ask:

> Make a beat-synced reel for songs/my-song, beats only.

Expected commands and output:

```bash
make setup                   # once, about 1–2 min: .venv with librosa, numpy, scipy, pillow
make timing SONG=my-song     # prints nothing alarming; writes songs/my-song/timing.json
```

The agent should report back the **BPM** and the **number of bars**. Check the BPM against what you hear. Half or double the real tempo is a known failure for songs without a steady kick.

```bash
make render SONG=my-song     # -> out/my-song.mp4
```

Expected: a vertical MP4 the length of the song, with visuals pulsing on the beat and the title from `songs/my-song/reel.json`. The agent creates that file with defaults if it's missing. **No HTML editing should be needed.**

## Step 6 (optional): karaoke words

```bash
python3.12 -m venv .venv-align && .venv-align/bin/pip install -r requirements-align.txt
make timing SONG=my-song WORDS=1
make render SONG=my-song
```

Expected: the lyrics appear word by word, in time with the singing. Whisper mishears some sung words. The agent should list the guessed words and ask you to confirm them on the render (GUIDE.md §5.2).

## Step 7 (optional): sync check and sprites

- Ask: *"Turn on the sync-check overlay and preview."* You should see beat ticks and word marks you can scrub against the audio (see `docs/beat-motion.md`).
- Ask: *"Add a dancing character."* In Codex, it uses the built-in image generation, the tested route. With Higgsfield, the agent prints the commands for you to run (untested, and paid). See `docs/sprites.md`.

## What to report back

For each step: did it match the expectation (yes/no), the time it took, and the exact error text if not. The owner's open decisions are listed in `build/SUMMARY.md`.
