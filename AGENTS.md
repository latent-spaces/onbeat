# Agent instructions (Codex, Claude Code and others)

This repo is one agent skill: it turns a song into a beat-synced vertical lyric reel with HyperFrames.

**Read `skills/onbeat/SKILL.md` and follow it.** It is the same skill that the Claude Code plugin and the Codex plugin install (also linked at `.agents/skills/onbeat/`).

When you work on the skill itself:

1. Everything the skill needs lives in `skills/onbeat/`. Keep it self-contained: no paths that point outside that folder.
2. After a change, run `node --test tests/`, then copy `skills/onbeat/example` to a scratch folder and run `npx --yes hyperframes@0.9.2 check` and `render` there.
3. Never run paid generation (Suno, Higgsfield) and never publish anything. The person does that.
