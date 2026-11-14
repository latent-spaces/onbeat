# Public README and demo anatomy audit

Research by codex-tooling-2, 2026-11-14. Research and proposals only; no product implementation or public launch. Repository baseline: `26d9337f44ebfb7a221a107e6f957c3ed31eb9f2`.

## Main finding

The strongest public promise is a narrow, visible result: **turn a song you already have into an editable, beat-synced lyric reel**. The README currently tells an existing collaborator where to resume unfinished work. It does not let a stranger judge the output, identify the product, or try a supported example. Fix that visitor journey after a convincing, reproducible reel exists; a rewritten headline alone cannot establish that the pipeline works.

The distinguishing explanation is already in `analysis/playbook.md` section 3: beats drive visual pulses and sung-word times drive lyrics. Show those two clocks in a short annotated demo. This is a more concrete reason to care than another general claim about AI video generation.

## What is verifiable today

| Observation | Evidence | Public-facing implication |
| --- | --- | --- |
| The README opens with “Start here (next session)” and says no video was built for the current story. | [Baseline README](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/README.md) | Present the project as experimental until a successful output is demonstrated. Move session history into a maintainer document in a future implementation phase. |
| Its content map links analysis, songs, timing scripts and a HyperFrames project. | Same README | This is currently a research/code workspace, not evidence of a packaged studio, skill or one-command application. |
| The playbook separates measured observations, visual judgments and hypotheses. | [Baseline playbook](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/analysis/playbook.md) | Preserve that credibility: include limitations and label future features as proposals. |
| No tracked PNG/JPG/WebP/GIF/MP4 demo assets were found by `git ls-files`; the README embeds no output demo. | Local tracked-file inventory at baseline | Produce an actual sample render before promising output quality. Existing HTML storyboards are drafts, not proof of a completed reel. |
| No tracked LICENSE, CONTRIBUTING, SECURITY or GUIDE file was found. | Local tracked-file inventory at baseline | Owner should choose a code license and document sample-media permissions before describing the project as reusable open source. No legal conclusions are made here. |
| GitHub metadata reports private visibility, null description/homepage/license, and empty topics. | `repository-metadata.json`, captured through `gh api` on 2026-11-14 | Prepare metadata copy; changing visibility or publishing remains outside this research mission. |
| Render scripts exist under `video/`, pinned to HyperFrames 0.9.2. | [Baseline package.json](https://github.com/oronanschel/music-reels/blob/26d9337f44ebfb7a221a107e6f957c3ed31eb9f2/video/package.json) | Describe the dependency, but do not imply end-to-end setup has been verified. Reproducibility is covered by codex-tooling-1. |

Code graph tools were not available in this session. This audit primarily reads Markdown/configuration and tracked-file metadata; it does not inspect function internals or modify compositions. No build/render verification was performed.

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
2. **Is this for me?** Songwriters and developers wanting timing-driven lyric visuals; currently experimental and local.
3. **Why use this instead of manual captioning?** Explain beat timing versus word timing with a visible example. Do not claim automatic creative direction.
4. **Can I try it without an account?** A rights-cleared bundled sample plus known-good timing data is the proposed route; it is not shipped today.
5. **Can I use my own song?** Explain audio/lyrics inputs, alignment limits, dependencies, and where manual correction may be needed.
6. **What does it cost and require?** Separate local render requirements from optional music generation and transcription. Do not imply a Suno subscription/API is required for importing existing audio.
7. **Can I reuse the result and contribute?** Link code license, sample-asset terms, contribution instructions and a small list of useful tasks after these exist.

## Recommendations for the merged report

**P0: demonstrate before promoting.** Produce one strong, reproducible original reel and link its exact source, timing data and render instructions. Existing README explicitly says the current story has no built video. Do not advertise a finished studio or claim a working packaged skill/CLI.

**P0: replace the public front door after the demo works.** Lead with a narrow song-to-reel promise, actual output poster/video, and a single verified sample path. Keep session history in maintainer docs. See `README-OUTLINE.md` for the proposed hierarchy and `DEMO-BRIEF.md` for a concrete asset brief.

**P0: make the sample independent of account setup.** Bundle rights-cleared media and precomputed timing; report exactly which dependencies and downloads still occur. Let users choose their own song later. This is a recommendation, not a claim that offline/no-key rendering currently works.

**P1: teach the differentiator visually.** Use a side-by-side or annotated segment showing beat-driven motion and word-driven lyric highlighting. Preserve editable source as a reason to fork, not just watch.

**P1: prepare repository metadata and reuse information.** Proposed description: “Editable lyric reels from your music, with beat and word timing powered by HyperFrames.” Candidate topics: `lyric-video`, `music-visualizer`, `audio-reactive`, `hyperframes`, `video-generation`. Choose a license and document sample-media terms with the owner; do not change visibility or publish in this phase.

**P1: evaluate the visitor funnel rather than promise virality.** Later, with approval, measure views of the demo, successful clean-clone sample runs, attempts with users' own audio, and reported failure points. A star count alone cannot establish usefulness or tell us which README block caused adoption.

## Evidence boundaries

- No launch-channel research or star-growth causal analysis was performed in this slice; other agents own that work.
- GitHub search maxima are sample-dependent. “We found few large direct matches” is supportable with a defined search; “there are no popular lyric-video projects” requires broader evidence.
- A fourth candidate, `ComposioHQ/shorts-generator`, returned a GitHub 404 page and was excluded from comparisons.
- Raw fetched pages remain locally under `sources/` and are ignored to avoid committing wholesale third-party READMEs. The versioned source record is `SOURCES.md`.
