# Public README and demo anatomy audit

Research by codex-tooling-2, 2026-11-14. Research and proposals only; no product implementation or public launch. Current repository baseline: `6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc`. Updated after the owner supplied five new main commits. The earlier `26d9337` audit is superseded for current-state claims; see [baseline update](BASELINE-UPDATE.md).

## Main finding

The strongest public promise is a narrow, visible result: **turn a song you already have into an editable, beat-synced lyric reel**. The new baseline already has a completed 2:24 reel composition and a full production guide. The opportunity is to make that existing work easy for strangers to see, understand and reproduce, then generalize it into a reusable workflow. It is no longer accurate to say that the repo has no guide or that no video was built.

The distinguishing explanation is explicit in `GUIDE.md` sections 5 and 7: beats drive visual pulses and sung-word times drive lyrics. Show those two clocks in an annotated excerpt of the existing reel. The human chooses the take and gives creative feedback; an agent builds much of the composition. This is a more concrete promise than fully automatic creative direction.

## What is verifiable today

| Observation | Evidence at current baseline | Public-facing implication |
| --- | --- | --- |
| The README leads with GUIDE.md and production runbooks. Its old unfinished-state paragraph is explicitly dated as earlier planning notes. | [Current README](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/README.md) | Keep the guide; move historical session notes below a concise public explanation and output preview. Do not read the old paragraph as current status. |
| GUIDE documents a completed 2:24 reel, human/agent roles, commands, alignment fixes, sprite workflow and render review. | [GUIDE](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/GUIDE.md) | Reuse it as the user guide and production case study rather than propose writing it from scratch. |
| Full composition source, final song MP3, timing JSON/JS, generated scene/sprite assets and prompt history are tracked. | `video/allow-always-final/`, `video/data/allow-always-final.*`, `songs/allow-always/take-final-yes.mp3`, `video/avatar-dance-test/assets/` | The existing work is a credible source-linked demo candidate. Asset presence alone is not visual or audio quality verification. |
| The Instagram brief names a completed full-quality render and phone copy under ignored `video/out/`. No MP4 is tracked, and those outputs are absent in this checkout. README embeds no output video. | [Instagram brief](https://github.com/oronanschel/music-reels/blob/6daad3d1a74c4ff2de645a7b86b4fdeae79be3dc/songs/allow-always/instagram-brief.md), tracked-file inventory | Distinguish documented completed render from a portable, visible demo artifact. Use the existing final reel for a poster/playable demo once an approved artifact is available. |
| An 11.52-second prototype includes its chorus audio, local GSAP, sprites, timing and pinned render scripts. | `video/avatar-dance-test/README.md`, assets and package.json | codex-tooling-1 reports a successful local prototype render from committed inputs, with cached tooling. Use it as the current technical sample; separately verify clean-install setup. This agent did not render it. |
| No root project LICENSE, CONTRIBUTING or SECURITY file was found. The vendored page-mascot subtree has an MIT license and provenance. | Tracked-file inventory | Separate project licensing and sample-media terms from the existing vendor license. No legal conclusions are made here. |
| GitHub metadata was private, with null description/homepage/license and empty topics at the initial capture. | `repository-metadata.json` | This timestamped metadata snapshot is distinct from the newly fetched source changes. Publishing/visibility changes remain outside this mission. |
| Render scripts are pinned to HyperFrames 0.9.2; GUIDE now lists tested tool versions and two Python environment setup commands. | `video/package.json`, prototype package.json, GUIDE section 2 | Setup documentation exists. A locked dependency manifest and general-purpose workflow are separate improvements; reproducibility details are owned by codex-tooling-1. |

Code graph tools were not available in this session. This audit reads documentation/configuration, tracked-file metadata and local asset presence. No product source or composition was modified. No build/render or listening verification was performed here. Prior production-session checks in the guide/runbooks are attributed documentation, not new tests by this agent.

The local presence/WAV metadata recheck is saved in `current-baseline-presence.json`. codex-tooling-1 additionally reports a newly passing prototype HyperFrames check and encoded sample render; see [their refreshed audit PR #5](https://github.com/oronanschel/music-reels/pull/5) and the attributed details in `BASELINE-UPDATE.md`. Their render validates the committed-input sample on this machine, not clean-install timing or listening quality.

## Primary-source comparison

These are current README observations, not reconstructed launch-era pages. Their presence does not prove a contribution to stars. Rendered demos were linked in the captured pages; I did not play or independently validate their media.

### Remotion: library, CLI entrypoint, editor and agent workflows

[Source README](https://github.com/remotion-dev/remotion#readme), accessed 2026-11-14 with Firecrawl.

Observed: a visual hero precedes three modes of use; a short Node prerequisite and `npx create-video@latest` appear under Get started. Later sections route readers to templates, skills, docs, rendering and contribution information, with a dedicated license notice.

Lesson for music-reels: give visitors one initial action, then route advanced needs to deeper documentation. State what the user receives. Do not copy a mature framework's enormous navigation surface into a small prototype.

### Motion Canvas: explicit library/editor identity

[Source README](https://github.com/motion-canvas/motion-canvas#readme), accessed 2026-11-14 with Firecrawl.

Observed: its introduction separately identifies a TypeScript animation library and an editor with real-time preview, describes a specific animation use case, then links a user quickstart before monorepo development instructions.

Lesson for music-reels: distinguish using a sample from developing the pipeline. State that the output is editable HTML/CSS/animation plus a render, rather than calling the repo an all-purpose studio. An agent skill can be a later interface to the same pipeline.

### MoneyPrinterTurbo: studio with several interfaces

[Source README](https://github.com/harry0703/MoneyPrinterTurbo#readme), accessed 2026-11-14 with Firecrawl.

Observed: a plain input-to-output promise, interface screenshots, language links, and an output gallery with portrait/landscape examples. The gallery labels sample languages and durations. Setup routes distinguish agent use, Python package, source, Windows and Docker paths; requirements are explicit.

Lesson for music-reels: show actual outputs and useful sample metadata, then give one recommended starting path. Avoid copying the long provider list and many installation routes before there is demand for them. An output-first layout is our proposed adaptation; this source itself shows interface previews before its output gallery.

## Visitor questions the README must answer

1. **What does it make?** One real vertical reel with a short explanation of editable outputs.
2. **Is this for me?** Songwriters and developers wanting timing-driven lyric visuals; currently a documented, local production workflow with project-specific helpers.
3. **Why use this instead of manual captioning?** Explain beat timing versus word timing with a visible example. Do not claim automatic creative direction.
4. **Can I try it without an account?** The existing short prototype bundles chorus audio and timing and was rendered locally by codex-tooling-1 without paid generation; verify clean-install setup and sample-media terms separately.
5. **Can I use my own song?** Explain audio/lyrics inputs, alignment limits, dependencies, and where manual correction may be needed.
6. **What does it cost and require?** Separate local render requirements from optional music generation and transcription. Do not imply a Suno subscription/API is required for importing existing audio.
7. **Can I reuse the result and contribute?** Link code license, sample-asset terms, contribution instructions and a small list of useful tasks after these exist.

## Recommendations for the merged report

**P0: promote the existing finished work accurately.** Use the completed 2:24 reel documented by GUIDE and its exact composition/timing as the hero case study. Make an approved output artifact easy to view and verify its reproduction path. Do not say the first reel still needs to be built, or advertise a generic studio or packaged end-to-end skill/CLI that does not exist.

**P0: improve the public front door around the existing GUIDE.** Lead with a narrow song-to-reel promise, an actual output poster/video, and a single verified sample path. Keep the GUIDE prominent and session history in maintainer docs. See `README-OUTLINE.md` for the proposed hierarchy and `DEMO-BRIEF.md` for a concrete asset brief.

**P0: verify the existing short sample before inventing another.** The avatar prototype already has tracked audio, visuals and timing, and codex-tooling-1 rendered it locally from those inputs. Present that tested local route, measure clean-install setup and document media terms. Report dependencies/downloads separately. The cached-tooling render time is not first-run installation time; this agent did not render or listen.

**P1: teach the differentiator visually.** Use a side-by-side or annotated segment showing beat-driven motion and word-driven lyric highlighting. Preserve editable source as a reason to fork, not just watch.

**P1: prepare repository metadata and reuse information.** Proposed description: “Editable lyric reels from your music, with beat and word timing powered by HyperFrames.” Candidate topics: `lyric-video`, `music-visualizer`, `audio-reactive`, `hyperframes`, `video-generation`. Choose a license and document sample-media terms with the owner; do not change visibility or publish in this phase.

**P1: evaluate the visitor funnel rather than promise virality.** Later, with approval, measure views of the demo, successful clean-clone sample runs, attempts with users' own audio, and reported failure points. A star count alone cannot establish usefulness or tell us which README block caused adoption.

## Evidence boundaries

- The original README slice did not investigate launch channels. A later [launch evidence addendum](LAUNCH-EVIDENCE.md) verifies specific public discussions without attributing star growth to them.
- GitHub search maxima are sample-dependent. “We found few large direct matches” is supportable with a defined search; “there are no popular lyric-video projects” requires broader evidence.
- A fourth candidate, `ComposioHQ/shorts-generator`, returned a GitHub 404 page and was excluded from comparisons.
- Raw fetched pages remain locally under `sources/` and are ignored to avoid committing wholesale third-party READMEs. The versioned source record is `SOURCES.md`.
