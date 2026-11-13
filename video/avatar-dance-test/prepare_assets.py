"""Pack generated transparent sheets on equal cells, anchoring dance feet.

Run from the repository root with .venv/bin/python.
Source art is preserved in assets/source. This only packs/crops sprite assets;
it never generates or redraws a character.
"""
from pathlib import Path
import json
import numpy as np
from PIL import Image
from scipy import ndimage

ROOT = Path(__file__).resolve().parent


def pack(name, grid, dance=False):
    image = Image.open(ROOT / 'assets/source' / f'{name}.png').convert('RGBA')
    tile = 384 if dance else 480
    atlas = Image.new('RGBA', (tile * grid, tile * grid))
    for index in range(grid * grid):
        col, row = index % grid, index // grid
        box = (round(col * image.width / grid), round(row * image.height / grid),
               round((col + 1) * image.width / grid), round((row + 1) * image.height / grid))
        cell = image.crop(box)
        # Remove disconnected alpha specks, retaining character components.
        array = np.array(cell)
        labels, count = ndimage.label(array[:, :, 3] > 80)
        if not count:
            raise ValueError(f'{name}: empty cell {index}')
        sizes = np.bincount(labels.ravel())
        keep = np.flatnonzero(sizes > max(15, sizes[1:].max() * .001))
        keep = keep[keep != 0]
        mask = ndimage.binary_dilation(np.isin(labels, keep), iterations=1)
        array[:, :, 3] = np.where(mask, array[:, :, 3], 0)
        cell = Image.fromarray(array).resize((tile, tile), Image.Resampling.LANCZOS)
        if dance:
            alpha = np.array(cell)[:, :, 3]
            ys, xs = np.where(alpha > 100)
            shift = round(tile * .94) - int(ys.max())
            aligned = Image.new('RGBA', (tile, tile))
            aligned.paste(cell, (0, shift))
            cell = aligned
        atlas.paste(cell, (col * tile, row * tile))
    out = ROOT / 'assets' / f'{name}.webp'
    atlas.save(out, lossless=True)
    if not dance:
        portraits = ROOT / 'assets/portraits'
        portraits.mkdir(exist_ok=True)
        atlas.save(portraits / f'{name}.png')
    print(out.name, atlas.size)


if __name__ == '__main__':
    for name in ('ochre-dance', 'blue-dance', 'robot-dance'):
        pack(name, 4, dance=True)
    for path in sorted((ROOT / 'assets/source').glob('*-closeups.png')):
        pack(path.stem, 3)
    timing = json.loads((ROOT.parent / 'data/allow-always-final.json').read_text())
    start = timing['bars'][14]  # 27.2768, chorus downbeat
    end = timing['bars'][20]    # six complete bars
    local = {'song': 'Allow Always', 'source': '../../out/dev/allow-always-final.wav',
             'sourceStart': start, 'sourceEnd': end, 'duration': end - start,
             'bpm': timing['bpm'], 'beatPeriod': timing['beatPeriod'],
             'beats': [round(t-start, 6) for t in timing['beats'] if start <= t < end],
             'bars': [round(t-start, 6) for t in timing['bars'] if start <= t < end]}
    (ROOT / 'assets/timing.json').write_text(json.dumps(local, indent=2) + '\n')
