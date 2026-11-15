# Privacy

onbeat is an agent skill: a set of instructions, two local scripts and an example. It has no server, no account and no analytics of its own. The author receives nothing from you.

## What stays on your computer

- Your audio, lyrics, reference images and the reels you make. The agent reads and writes them in the folder you work in.
- Beat and word analysis (`timing.py`), which runs locally. Optional word alignment downloads speech and separation models once, then runs locally.
- Rendering, which runs locally in a headless browser through HyperFrames.

## What can leave your computer

- **Your coding agent.** Claude Code, Codex or another agent sends what it reads to its own provider. That is covered by your agent's privacy terms and settings, not by onbeat.
- **Image generation, only when you agree to it.** To draw characters or backgrounds, the agent sends your prompts and any reference images you supply to the image provider you pick (for example Higgsfield, or Codex's built-in generator). Their terms apply, and it may use credits. The skill asks before paid generation.
- **Downloads on first use.** npm packages, a headless browser, Python packages, models and possibly web fonts are fetched from their public registries, which see a normal download request.
- **HyperFrames telemetry.** The HyperFrames CLI that renders the video may send anonymous usage data to its maker. Set `HYPERFRAMES_NO_TELEMETRY=1` or `DO_NOT_TRACK=1` to turn it off.

onbeat never publishes or uploads your reel.

## Personal data

onbeat doesn't ask for, collect or store names, emails or other personal data. Anything personal in your own files stays with those files.

## Contact

Questions: open an issue at https://github.com/latent-spaces/onbeat/issues.
