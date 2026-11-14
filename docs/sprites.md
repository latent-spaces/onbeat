# Sprite generation: one asset contract, two providers

Characters in a reel are **sprite sheets**: square grids of poses. Any image provider can make
them, because the animation code only reads one file, `sprites.json`, never the provider's output.

```
cast.json ─► plan ─► prompts/*.txt ─► [Codex | Higgsfield] ─► sheets/*.png ─► ingest ─► *.webp + sprites.json ─► check
```

The tool is `skills/music-reel/sprites/sprites.py`. It needs Pillow and NumPy (SciPy is optional and
removes stray specks). Use the repo's Python environment (`make doctor` checks it).

## The contract

| Sheet kind | Grid | Poses | Output cell | Notes |
|---|---|---|---|---|
| `dance` | 4×4 | 16 | 384 px | one character, full body, one 4-beat loop; feet anchored at 94% of the cell height |
| `portrait` | 3×3 | 9 | 480 px | head angles and expressions; shoulders fixed |
| `fx` | 3×3 | 9 | 384 px | one effect, spark to embers, played once |

Indices are zero-based and row-major. `sprites.json` stores every frame rectangle
(`frames: [{i, x, y, w, h}]`), the grid, the anchor, the provider, the model and whether the alpha check passed.

## Steps

```bash
S=skills/music-reel/sprites/sprites.py
python $S plan skills/music-reel/sprites/cast.example.json --out work/sprites   # copy and edit cast.json first
python $S provider codex --plan work/sprites/plan.json                          # or: higgsfield
# ... generate the sheets, save each to work/sprites/sheets/<name>.png ...
python $S ingest work/sprites/sheets/robot-dance.png --name robot-dance --kind dance --out work/sprites
python $S check work/sprites                                                    # exit code 1 on any failure
```

`ingest` keeps the original sheet in `source/`, zeroes the faint alpha haze generators leave around cutouts,
splits the sheet with rounded cell boundaries (a 1254 px sheet still splits evenly in four), and packs equal tiles.

`check` fails on: an empty cell, a character touching the cell edge, opaque pixels in a cell corner (a painted
background), a wide low-alpha fringe, a silhouette whose area is far from the median (scale or identity drift), and
feet or horizontal drift across a dance loop. It cannot see identity or hand contact, so also open the atlas over a
light and a dark background before using it. `python $S selftest` runs the whole pipeline on synthetic sheets.

## Provider A: Codex built-in image generation (tested route)

Free under a Codex subscription. `provider codex` prints one block per sheet: use `image_gen` with
`transparent_background: true`, pass the reference images, and save the result to the printed path.
This is how the shipped characters were made; the checks above pass on them.

## Provider B: Higgsfield (**untested, needs an owner run**)

`provider higgsfield` only **prints** commands: `higgsfield model list --json`, `model get <id> --json`,
then per sheet `generate cost` and `generate create ... --wait --json`. Nothing is executed, and generation costs credits.
Before running anything, read the model's parameters with `model get`. Do not assume alpha, reference-image count
or output size.

If the model has no alpha, set `"key": "magenta"` (or `"green"`) in `cast.json` and re-run `plan`: the prompts then ask
for one flat key colour and never mention transparency. Add `--key magenta` to `ingest` to remove it. The keyer is
tested only on synthetic sheets, so inspect the edges.

## Rules that save time

- One character per sheet. Never normalize each pose to its own bounding box: it makes the scale pump.
- Describe *successive actions*, not a collection of poses; the last pose must connect to the first.
- A checkerboard painted into the PNG is not alpha. Ask for a flat key colour instead.
- Record frame numbers with each file; they change between revisions.
- Longer notes: `analysis/runbooks/animated-music-reels.md` section 9 and `analysis/runbooks/image-prompts.md`.
- The vendored `vendor/page-mascot` has its own keying and consistency checks (MIT, Kamran Ahmed).
