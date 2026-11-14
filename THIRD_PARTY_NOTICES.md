# Third-party notices

## page-mascot

The sprite-atlas approach in this repo was adapted from
[page-mascot](https://github.com/nilbuild/page-mascot) by nilbuild: square sprite
sheets cut into equal cells, one frame index chosen per moment, fixed anchors,
alpha and consistency checks, and the reference-image prompt workflow. We
re-implemented it for song time and full-body dance sheets
(`video/avatar-dance-test/prepare_assets.py`, `skills/music-reel/sprites/`).
The upstream code and character images were vendored once (commit
`76a44ed9180063bf4852b9dd724b656f4a828ac7`, imported 2026-11-13) and then removed;
no upstream character images are used in our reels.

The upstream license is reproduced here because the approach and some of the
wording of the lessons in `analysis/avatar-pipeline.md` derive from it.

```
MIT License

Copyright (c) 2026 Kamran Ahmed <https://kamran.fyi>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
