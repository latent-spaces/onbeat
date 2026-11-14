# Sprite generation: one asset contract, two providers

Characters in a reel are **sprite sheets**: square grids of poses. Any image provider can make
them, because the animation code only reads one file, `sprites.json`, never the provider's output.

```
cast.json ─► plan ─► prompts/*.txt ─► [Codex | Higgsfield] ─► sheets/*.png ─► ingest ─► *.webp + sprites.json ─► check
```

The tool is `scripts/sprites.py` in this skill. It needs Pillow and NumPy (SciPy is optional and
removes stray specks), which `scripts/requirements.txt` installs.

The two main image-generation routes are **Higgsfield** and **Codex's built-in image generator**. Use the person's preference; within Codex, default to the built-in generator if none is specified. Use either for rough visual choices before making production sheets. The built-in route is tested; the Higgsfield integration below still needs an owner run. Do not treat concept approval as permission to run paid generation.

For production, pass the chosen concept image as a direct reference for each character sheet and for a separate garden/scene background. Generate one character per sheet and a background plate without characters or baked-in lyrics. Keep source images and prompts in the reel folder. If generation is interrupted, inspect saved outputs and ingest/check usable sheets before retrying; don't regenerate completed assets blindly.

## The contract

| Sheet kind | Grid | Poses | Output cell | Notes |
|---|---|---|---|---|
| `dance` | 4×4 | 16 | 384 px | one character, full body, one 4-beat loop; feet anchored at 94% of the cell height |
| `portrait` | 3×3 | 9 | 480 px | head angles and expressions; shoulders fixed |
| `fx` | 3×3 | 9 | 384 px | one effect, spark to embers, played once |

Indices are zero-based and row-major. `sprites.json` stores every frame rectangle
(`frames: [{i, x, y, w, h}]`), the grid, the anchor, the provider, the model and whether the alpha check passed.

## Steps

Before generating a complete dance sheet, follow the creative checkpoints in `../SKILL.md`: agree the concept and references, show a rough character/look study in a representative frame, and incorporate the person's feedback. Once the character is agreed, generate the sheet, inspect it and test a short beat-synced dance passage before building the full reel. If the person has already approved those decisions or explicitly requested autonomous work, use that authorization without repeating the checkpoints.

```bash
S=<this skill's folder>/scripts
python $S/sprites.py plan $S/cast.example.json --out work/sprites   # copy and edit cast.json first
python $S/sprites.py provider codex --plan work/sprites/plan.json   # or: higgsfield
# ... generate the sheets, save each to work/sprites/sheets/<name>.png ...
python $S/sprites.py ingest work/sprites/sheets/robot-dance.png --name robot-dance --kind dance --out work/sprites
python $S/sprites.py check work/sprites   # exit code 1 on any failure
```

`ingest` keeps the original sheet in `source/`, zeroes the faint alpha haze generators leave around cutouts,
splits the sheet with rounded cell boundaries (a 1254 px sheet still splits evenly in four), and packs equal tiles.

`check` fails on: an empty cell, a character touching the cell edge, opaque pixels in a cell corner (a painted
background), a wide low-alpha fringe, a silhouette whose area is far from the median (scale or identity drift), and
feet or horizontal drift across a dance loop. It cannot see identity or hand contact, so also open the atlas over a
light and a dark background before using it. `python $S/sprites.py selftest` runs the whole pipeline on synthetic sheets.

## Provider A: Codex built-in image generation (tested route)

### Images from the person

The person may supply images as **direct references** or **context**. Record each image's role in the creative brief before generation:

- Direct reference: identify what should carry through (character appearance, clothing, palette, style or composition), what may change, and pass the image through the provider's supported reference-image input. A reference portrait guides identity; the generated sheet still needs full-body sequential poses and the grid contract above.
- Context: use the image to understand the setting, mood or story and describe those cues in the prompt. Do not automatically copy the subject or treat it as an identity reference. Pass the image as context only when the provider supports that role and the person intends it.

If the role is ambiguous, ask. Inspect local images before using them and keep the originals intact. For Higgsfield, check the chosen model's reference support and limits with `model get`; a path mentioned only in a text prompt does not attach an image.

`provider codex` prints one block per sheet: use `image_gen` with
`transparent_background: true`, pass the reference images, and save the result to the printed path.
This is the route the example's robot came from.

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
- The atlas approach is adapted from [page-mascot](https://github.com/nilbuild/page-mascot) by nilbuild (MIT); see `THIRD_PARTY_NOTICES.md`.
