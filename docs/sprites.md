# Sprite sheets: one contract, two providers

The animation code reads local sheets plus `sprites.json`. It never knows which image generator drew them. `scripts/sprites/sprites.py` writes that record for any provider.

| Provider | Status | What you do |
|---|---|---|
| **Codex** built-in image generation | Tested route (free under the Codex subscription) | `generate` writes the prompt; you ask Codex to draw it; `ingest` checks and records the result |
| **Higgsfield** | **Untested, needs owner run.** Dry run only by default | `generate --provider higgsfield` prints the exact `higgsfield` commands; nothing is sent |

## Steps

```bash
S=sprites/example-spec.json                     # copy and edit: style, character, sheets
python3 scripts/sprites/sprites.py doctor
python3 scripts/sprites/sprites.py generate $S robot-dance --provider codex
#   ...Codex draws the image and saves sprites/out/robot-dance-raw.png...
python3 scripts/sprites/sprites.py ingest   $S robot-dance sprites/out/robot-dance-raw.png --provider codex
python3 scripts/sprites/sprites.py check    $S
```

`ingest` copies the sheet to `<outDir>/<id>.png`, keeps the original as `<id>-source.png`, runs the checks and writes `<outDir>/sprites.json`. Exit code 2 means a check failed.

## Spec

```json
{"outDir": "out", "style": "...", "character": "...",
 "sheets": [{"id": "robot-dance", "kind": "dance",
             "grid": {"columns": 4, "rows": 4}, "motion": "...",
             "playback": {"fps": 12, "beatsPerLoop": 4}, "references": ["ref.png"],
             "alpha": true, "keyColor": "magenta #FF00FF",
             "higgsfield": {"model": "<id>", "params": {}}}]}
```

`kind` is `dance` (4x4, 16 poses), `closeup` (3x3 head angles), `action` or `effect` (3x3, successive frames). Cells are read left to right, then top to bottom, zero-based. Details and why: `analysis/runbooks/animated-music-reels.md` section 3, and prompt shapes in `analysis/runbooks/image-prompts.md`.

## sprites.json

Per sheet: `file`, `provider`, `model`, `promptFile`, `references`, `grid`, `dimensions`, `cells` (rounded rects `{i,x,y,w,h}`, so a 1254 px sheet with 4 columns still packs evenly), `bounds` (tight figure box per cell), `playback`, `anchor`, `alphaChecked`. Frame `i` is `cells[i]`; do not compute rects in the animation code.

## Checks (pure Python, no Pillow)

- **No alpha**: fail. The PNG has no alpha channel (a painted checkerboard or solid fill).
- **Corner alpha**: fail if the sheet's four corners are not transparent.
- **Empty cell**: fail.
- **Border contact**: warn when a figure touches its cell edge (cut off, no gutter).
- **Scale drift**: warn when a cell's figure height differs by more than 25% from the median.
- **Ground line**: warn when a cell's feet sit off the median ground line.

The checks read 8-bit PNG only. Convert WebP first (`ffmpeg -i in.webp out.png`). They do not replace looking at the sheet on light and dark backgrounds: a faint coloured fringe passes the numbers.

## Providers without alpha: keying

Set `"alpha": false` (the default for Higgsfield). The prompt then asks for one flat key colour and never mentions transparency. After the image comes back, `ingest --key` runs `vendor/page-mascot/skills/page-mascot/scripts/key.py`, which needs Pillow, NumPy and SciPy in the Python that runs the script. Keep source and keyed output; inspect the edges.

## Higgsfield, when the owner runs it

1. `higgsfield auth login`, then `higgsfield model list --json`.
2. `higgsfield model get <model-id> --json`: check alpha, reference count and output size. Put the model in the spec.
3. Run `generate ... --provider higgsfield` and read the printed command. Add `--run --i-accept-credits` only when you want to spend credits.
4. Save the result image and run `ingest ... --provider higgsfield --model <id> --key`.

This repo's sandbox could not reach the Higgsfield API, so none of the Higgsfield route has been run.

## Verified here

Prompt generation, dry-run output, `ingest`, `check` and `sprites.json` were run against the committed `video/avatar-dance-test/assets/source/robot-dance.png` (16 cells, alpha OK). Not run: `ingest --key` (no Pillow/NumPy/SciPy installable in the sandbox), any Higgsfield call, and a fresh Codex image generation.
