# Demo asset brief for a future public release

Prepared 2026-11-14 by codex-tooling-2. Proposed assets only: this research does not produce, render or publish a reel.

## The core demonstration

Use one original or otherwise redistributable 30–45 second song loop. Pair the source with a small, clean composition: one clear setting, one dominant object and large readable lyrics. This follows the repo's existing playbook rather than adding an unrelated visual language. Do not reuse reference creators' characters, lyrics or branding.

The full sample should demonstrate a vocal opening, a beat-driven drop, a short contrasting section, and a return that loops. Choose a song whose actual performance supports those moments; the existing playbook warns that asking generated music to follow a long predetermined story failed.

## Assets to prepare

| Asset | Purpose | Proof required |
| --- | --- | --- |
| Full portrait render with sound | Let visitors judge the actual reel | Produced from the checked-in sample, exact source revision and command recorded |
| Small poster or short silent preview | Make the README legible before playback | Large lyric/hero-object frame from the real output; not an aspirational mockup |
| Short annotated excerpt | Explain why timing matters | Beat markers align with visual pulses; sung-word highlights follow the vocal timing |
| Editable source link | Let developers inspect and remix | Same composition and timing used for the shown output |
| Clean-clone reproduction note | Let users know what was checked | Environment, dependencies, downloads, command, result path and measured time |
| Media/source manifest | Make sample provenance clear | Audio, lyric, font and artwork origins plus applicable reuse terms |

Preview dimensions, length and codec should be selected after testing actual GitHub rendering behavior. Do not assume a Markdown `<video>` tag or local MP4 link will embed correctly. Test on a private branch/PR first; use a poster linked to playable media if necessary. Hosting or making artifacts public needs separate approval.

## Proposed 15-second explanatory cut

1. **0–3 s:** the finished reel immediately, with a clear lyric hook. Keep useful on-screen information readable with sound off.
2. **3–8 s:** the same output with unobtrusive beat and word markers; explain the two timing layers in plain language.
3. **8–12 s:** briefly show the editable composition or a palette change on the same segment. Avoid unrelated dashboard footage.
4. **12–15 s:** final output and one action: try the included sample. Only show this action after that path works.

This cut is a teaching/README asset, not a claim that 15 seconds is empirically optimal for launch reach.

## Review criteria

- The video matches the referenced source and can be rerendered from a clean clone.
- The first frame is legible on a phone; the main lyric is not inside tiny UI.
- Lyrics match the audio and do not follow the beat grid when the singer does not.
- The visual pulse follows audible attacks; inspect the render and listen rather than relying on a passing linter.
- The loop has been reviewed with sound and through repeated playback.
- The transcript/caption and sample manifest are included.
- README wording accurately states current automation and manual work.

No tests of these criteria were run in this research phase. codex-tooling-1 separately documents the implementation work needed for reproducibility.
