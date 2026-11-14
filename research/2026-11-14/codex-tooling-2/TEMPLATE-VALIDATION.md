# Template + sample validation — 2026-11-14

Branch: feat/template-sample. Supersedes template PR #17 with its author's base retained.

- Bundled sample: same builder/template as own-song input; original local robot atlas, 11.52-second compressed chorus, no keys or alignment.
- Shared SpriteDance/SyncCheck loaded from teammate PR #19/20 for local checks; helper code belongs to that PR. Manifest rects drive poses independent of provider.
- Sample HyperFrames0.9.2 check: no findings. Frames inspected at0/2/5/9/end; encoded frame at5s inspected. Local preview3034 responds200.
- Render:35.6s on cached AppleM4 tooling, screenshot capture/hardware GPU; H264/AAC1080x1920,346frames/30fps,11.533333s,3,698,240bytes. Not a cold-install benchmark or listening test.
- Second config: same audio, two cast members, different palette and timed lines; HFcheck passes, overlay has intentional ruler-overflow/small diagnostic-label warnings reported to helper author. This does not establish a real second-song listening test.
- Three stdlib regression tests protect input/ancestor/unrelated folders and prior output on validation/conversion failure. No wholesale deletion of output.
- Prototype folded: runtime art moved to real video/assets/disco; existing full-reel asset paths remain valid. Prototype HTML/build scripts removed, original sprite sources/provenance preserved. Compressed sample replaces chorus WAV.

Owner decisions: sample-media/code license and public release remain undecided; no posts, paid generation or main merge performed. Raw source sprite sheets are retained because they are owner artwork; propose owner review of redundant raw/portrait source art before deleting it. No songs, reels.txt or analysis/comments content deleted.
