# Four requested repositories: primary metadata support

Observed 2026-11-14 around 10:28 UTC, using GitHub REST repository metadata. This supplements the team's repo-specific README, launch and credit research; it does not replace those notes.

| Repository | Stars | Created (UTC) | GitHub-detected code license |
| --- | ---: | --- | --- |
| [ATH-MaaS/Pixelle-Video](https://github.com/ATH-MaaS/Pixelle-Video) | 30,079 | 2025-11-07 | Apache-2.0 |
| [nilbuild/page-mascot](https://github.com/nilbuild/page-mascot) | 1,376 | 2026-09-14 | MIT |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 143,414 | 2024-03-11 | MIT |
| [zai-org/CogVideo](https://github.com/zai-org/CogVideo) | 13,201 | 2022-05-29 | Apache-2.0 |

## How fast the stars came

The star-timestamp endpoint was tested once per repository with the star+json Accept header and per_page=1. All four returned HTTP 404. Repository metadata worked. Thus no observed growth curve, first-week velocity, time-to-milestone or launch attribution is available from this check. Creation date plus current stars is not a trajectory. Do not describe lifetime average stars/day as launch speed.

The machine-readable evidence is `four-repos-metadata.json`; no stargazer identities were saved.

## Implications for synthesis

- Pixelle-Video has 30,079 stars in this snapshot. Its creation date does not prove when the product launched or which channel drove adoption.
- page-mascot has 1,376 stars, and GitHub detects MIT. Actual vendored LICENSE/provenance and notice preservation are owned by codex-tooling-1 / sonnet-stars-1; a badge does not itself document the credit obligations.
- MoneyPrinterTurbo has 143,414 stars. The large count is a comparison signal, not proof of which README block or launch channel caused growth. README observations are also in my main notes.
- CogVideo has 13,201 stars and a 2022 repository creation date. Its description distinguishes CogVideo from CogVideoX (2024), so do not equate repository age with the current model launch. GitHub detecting Apache-2.0 for the repo is not evidence that all model weights carry those terms; the repo-specific researcher should check model terms separately.

Team split: sonnet-stars-2 covers MoneyPrinterTurbo/Pixelle-Video; sonnet-stars-1 and codex-tooling-1 cover page-mascot and credit; opus-strategist-2 covers CogVideo; opus-strategist-1 edits RECOMMENDATIONS.md.
