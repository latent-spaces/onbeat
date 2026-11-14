# page-mascot: packaging lessons and vendor credit

Observed 2026-11-14. Complement to sonnet-stars-1's broader repo study; local-credit verification owned by codex-tooling-1.

## Primary evidence

[Repository](https://github.com/nilbuild/page-mascot): GitHub API reports **1,376 stars**, creation **2026-09-14T06:55:59Z**, last push **2026-09-15T10:07:44Z**. Saved metadata is `page-mascot-metadata.json`. That is roughly 61 days of repository age, not a measured growth curve. Timestamped stargazers returned HTTP 404 (`page-mascot-first-star.json`); releases returned an empty array. We cannot identify launch-week growth or attribute stars to a channel from these observations.

**Type:** React/npm component plus optional agent skill and generation/build/verification scripts, not a video studio or generative video model. The [README](https://github.com/nilbuild/page-mascot/blob/main/README.md) starts with a mascot image, one clear behavioral promise, and a prominent [demo/gallery link](https://koboyo.com/page-mascot). It offers `npm i page-mascot`, a two-prop component example and existing mascot sheets before asking users to generate anything. The optional skill adds an agent-facing path; prompt examples make the outcome concrete. Diagrams show the two 3×3 atlases and six visual styles. Pointer/reduced-motion behavior is documented. The demo's actual interaction was not tested in this slice, and the later follow-up `page-mascot-launch.md` verifies a same-day author announcement on X; the README's link is evidence of a distribution destination, not its impact.

**Copy:** a small inspectable runtime contract, existing assets before paid generation, component and skill sharing one asset format, outcome-first README, illustrated explanation and explicit generation dependency. For music-reels, use the existing short prototype and timing contract in the same way.

**Avoid:** treating pointer-driven bust portraits as ready-made full-body dancing or dropping wall-clock interaction into a deterministic render. Our existing `docs/research/avatar-pipeline.md` already distinguishes those constraints.

## License and actual import

Current upstream LICENSE matches `vendor/page-mascot/LICENSE` byte for byte. It is **MIT**, copyright **2026 Kamran Ahmed** ([upstream license](https://github.com/nilbuild/page-mascot/blob/main/LICENSE)). The notice requires preserving its copyright and permission notice in copies or substantial portions of the software. A README shout-out is useful attribution but does not replace the license text.

The import is pinned in `vendor/page-mascot/UPSTREAM.json` to **76a44ed9180063bf4852b9dd724b656f4a828ac7**, imported 2026-11-13. It records selected code, tools, prompt references and four original human examples. I recalculated all **36** listed SHA-256 hashes: every one matches (`page-mascot-vendor-check.json`). Preserve the existing LICENSE and provenance alongside copied source/assets, including when packaging a skill or source archive.

`docs/research/avatar-pipeline.md` says the vendor files are unmodified, while new reel images were generated later outside the vendor directory. Credit the adapted tooling/reference method accurately; do not imply all final reel artwork was drawn by the upstream author or that this license establishes the rights to every independently generated asset, song or font.

## Suggested credit text for README / third-party notices

> Sprite-atlas tooling and reference workflow adapted from [page-mascot](https://github.com/nilbuild/page-mascot) by Kamran Ahmed, licensed under MIT. Vendored source, selected examples, license and pinned upstream provenance are preserved in `vendor/page-mascot/`. The reel's later dance and action artwork was generated separately; see its recorded prompts and production runbooks.

Keep the complete existing MIT notice with the distributed vendor material. Add this visible credit in the public README and a third-party notices section/file when packaging. A root project license remains a separate decision. The MIT text does not itself prescribe an on-screen watermark; recommending a visible README credit is an attribution practice, not an invented requirement to burn a credit into every video.

## Synthesis recommendation

page-mascot is a directly relevant **component + skill** packaging example, with 1,376 observed stars and unknown star-growth speed and attribution; a same-day author announcement is verified in `page-mascot-launch.md`. Copy its ready-to-use asset path, minimal interface, concrete prompt examples and illustrated mechanics. Preserve the already-retained MIT notice/provenance and credit Kamran Ahmed's adapted tooling/workflow, distinguishing newly generated reel art. No source or license files were changed by this research.
