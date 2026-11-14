# PLAN release-order correction — 2026-11-14

Baseline: owner-merged main `18f9458` (plan PR #8). Documentation correction only.

- P0 promises the existing case study and a tested bundled sample; own-song support and packaged skill remain P1, gated by a second-song test.
- Show existing nested sample commands separately from proposed root make targets; sample doctor excludes Python and model downloads.
- Integrate the existing `scripts/timing.py --no-words` flag rather than propose it as new. Remove unmeasured download-size and launch-timing claims.
- Test the actual social link route signed out after publication; private fresh-user pilots precede promotion.
- Preserve owner approval for media, license, release and posts. No implementation, publication or merge performed.

Validation: `git diff --check`; inspected `video/avatar-dance-test/package.json` check/render commands and output path; verified existing --no-words flag in scripts/timing.py. No render/test suite rerun for this documentation-only revision. The 14.4-second cached M4 render is prior evidence, not a clean-install benchmark.

Earlier contribution/review/closing cards and their drawing sources are included as dated project-update records. They describe earlier checkpoints, not current completion claims.
