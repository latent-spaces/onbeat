# Agent instructions (Codex, Claude Code and others)

This repo turns a song into a beat-synced vertical lyric reel with HyperFrames.

**Read `skills/music-reel/SKILL.md` first and follow it.** It is the same skill that the Claude Code plugin and the Codex plugin install (also at `.agents/skills/music-reel/`).

Short version:

1. `make doctor`, then `make sample` → `out/sample.mp4`. Do this first, with no keys or accounts needed.
2. For an own song: `songs/<name>/song.mp3` → `make setup` → `make timing SONG=<name>` → `make render SONG=<name>`.
3. Never run paid generation (Suno, Higgsfield) and never publish anything. The person does that.
4. Edit compositions under `video/` only after reading `video/AGENTS.md` (HyperFrames rules).
