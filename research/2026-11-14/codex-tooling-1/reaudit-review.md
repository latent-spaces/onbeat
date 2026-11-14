# Review of synthesis after main 6daad3d

Reviewed the synthesis branch on 2026-11-14 around 10:21 UTC. The new-main guide/source corrections are present. Sent these final evidence updates to the editor:

- The earlier report that nothing was rendered is superseded: this audit now rendered the unchanged bundled avatar prototype from committed inputs. Check passed, with two track-density warnings; output metadata confirms H.264/AAC, 1080×1920, 30 fps, 346 frames and 11.533333 s. A snapshot pair and one encoded frame were inspected. Full-song render and actual listening remain outside the validation.
- The self-contained short example has a verified no-key rendering path on this machine. A clean installation time is still unmeasured; the 14.4-second render uses cached tooling.
- Rebuilding the final WAV need not rerun timing/alignment: convert the tracked MP3 directly while preserving the committed curated timing pair. A blanket timing.py → cut_final.py quickstart is unnecessarily heavy and risks replacing the carefully aligned sung lyrics.
- GUIDE records versions used and install commands, but those pip commands are unpinned. Say documented environment, not a locked installation.
- Promote the existing prototype and guide; a general arbitrary-song adapter, skill and CLI remain future work.

The synthesis editor owns RECOMMENDATIONS.md to avoid concurrent copies on separate research branches. This file records the requested changes and points to reproducible evidence in this folder.
