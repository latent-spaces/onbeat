#!/usr/bin/env python3
"""Sprite sheets for music reels: plan prompts, hand off to a provider, ingest, check.

One asset contract for every image provider. A provider only has to hand back a
square grid sheet as a local PNG. Everything after that (keying, slicing, anchoring,
checks, sprites.json) is the same, so the animation code never changes per provider.

    sprites.py plan cast.json --out work/sprites
    sprites.py provider codex --plan work/sprites/plan.json
    sprites.py provider higgsfield --plan work/sprites/plan.json   # prints commands only
    sprites.py ingest work/sprites/sheets/robot-dance.png --name robot-dance \
        --kind dance --out work/sprites
    sprites.py check work/sprites
    sprites.py selftest

Needs Pillow and NumPy. SciPy is optional (removes stray specks when present).
All indices are zero-based, row-major (left to right, then top to bottom).
"""
import argparse
import json
import shlex
import sys
from pathlib import Path

try:
    import numpy as np
    from PIL import Image
except ImportError:
    sys.exit('sprites.py needs Pillow and NumPy: pip install -r requirements.txt')

try:
    from scipy import ndimage
except ImportError:
    ndimage = None

# kind -> grid size, output tile size, anchor policy
KINDS = {
    'dance': {'grid': 4, 'tile': 384, 'anchor': 'feet', 'poses': 16},
    'portrait': {'grid': 3, 'tile': 480, 'anchor': 'none', 'poses': 9},
    'fx': {'grid': 3, 'tile': 384, 'anchor': 'none', 'poses': 9},
}
FEET_AT = 0.94          # dance feet land at 94% of the cell height
HAZE_BELOW = 12         # alpha under this is generator haze and is zeroed on ingest
ALPHA_SOLID = 100       # alpha above this counts as character
KEYS = {'magenta': (255, 0, 255), 'green': (0, 255, 0)}
STYLE_DEFAULT = ('flat painted colors, thin dark outlines, one hard cel-shadow shape, '
                 'no gradients, no glow, no text')

DANCE_SEQUENCE = (
    'Sixteen successive poses of one smooth relaxed 4-beat dance loop, row-major and '
    'chronological. Row 1: knees bend, weight left, elbows rise from waist to chest. '
    'Row 2: weight shifts to center then right, one forearm moves outward. Row 3: a foot '
    'taps out and the body returns, both arms make a soft wave at chest height. Row 4: '
    'elbows lower, knees rebound, weight returns left and the arms lead into pose 1. '
    'Adjacent frames differ modestly, no random jumps, the last pose connects to the first.'
)
PORTRAIT_SEQUENCE = (
    'Row-major head angles and expressions: 1 front neutral, 2 three-quarter turned '
    'slightly left, 3 three-quarter turned slightly right, 4 looking slightly down, '
    '5 eyes closed enjoying the music, 6 head tilted right with a subtle smile, 7 looking '
    'slightly up, 8 head tilted left, 9 front with a subtle smile. Shoulders and base of '
    'neck stay at the same position and scale in every cell; vary head angle and '
    'expression only.'
)
FX_SEQUENCE = (
    'Nine successive stages of one effect, row-major: a small spark grows to a fireball, '
    'then smoke, then embers, fading to almost nothing. Fixed origin and scale.'
)
SEQUENCES = {'dance': DANCE_SEQUENCE, 'portrait': PORTRAIT_SEQUENCE, 'fx': FX_SEQUENCE}


def die(message):
    print(f'error: {message}', file=sys.stderr)
    sys.exit(1)


# --- plan ---------------------------------------------------------------------

def build_prompt(character, kind, style, key):
    spec = KINDS[kind]
    n = spec['grid']
    lines = [
        f'Create an exact {n}x{n} sprite grid of {spec["poses"]} equal square cells '
        f'for ONE character: {character["description"]}.',
        'The SAME identical character, outfit, proportions and scale in every cell. '
        'Fixed orthographic camera. Every figure entirely inside its own cell with a '
        'generous clear margin. No grid lines, no labels, no text, no borders, no shadows.',
    ]
    if kind == 'dance':
        lines.append('Full body. Keep the ground line and pelvis center consistent.')
    if kind == 'portrait':
        lines.append('Crop at the upper chest, entire head visible, lower torso edge at '
                     '90% of the cell height.')
    lines.append(SEQUENCES[kind])
    lines.append(f'Style: {style}.')
    if key:
        r, g, b = KEYS[key]
        lines.append(f'Background: one flat pure {key} (#{r:02X}{g:02X}{b:02X}) filling '
                     'every cell edge to edge, no gradient, no texture. The character '
                     f'uses no {key}.')
    else:
        lines.append('Background: genuinely transparent alpha, no painted background and '
                     'no checkerboard.')
    lines.append(f'Square sheet, exactly {n} columns by {n} rows.')
    return '\n'.join(lines)


def cmd_plan(args):
    cast = json.loads(Path(args.cast).read_text())
    key = cast.get('key') or None
    if key and key not in KEYS:
        die(f'key must be one of {sorted(KEYS)} or omitted')
    style = cast.get('style', STYLE_DEFAULT)
    out = Path(args.out)
    (out / 'prompts').mkdir(parents=True, exist_ok=True)
    (out / 'sheets').mkdir(exist_ok=True)
    jobs = []
    for character in cast['characters']:
        for kind in character.get('sheets', ['dance', 'portrait']):
            if kind not in KINDS:
                die(f'unknown sheet kind {kind!r}; use {sorted(KINDS)}')
            name = f'{character["id"]}-{kind}'
            prompt_file = out / 'prompts' / f'{name}.txt'
            prompt_file.write_text(build_prompt(character, kind, style, key) + '\n')
            jobs.append({
                'name': name, 'kind': kind, 'grid': KINDS[kind]['grid'],
                'prompt_file': str(prompt_file.relative_to(out)),
                'expected_sheet': f'sheets/{name}.png', 'key': key,
                'references': character.get('references', []),
            })
    plan = {'version': 1, 'dir': str(out), 'jobs': jobs}
    (out / 'plan.json').write_text(json.dumps(plan, indent=2) + '\n')
    print(f'{len(jobs)} prompts in {out / "prompts"}; plan: {out / "plan.json"}')


# --- providers ------------------------------------------------------------------

def load_plan(path):
    plan = json.loads(Path(path).read_text())
    return plan, Path(plan['dir'])


def cmd_provider(args):
    plan, base = load_plan(args.plan)
    if args.name == 'codex':
        print('# Codex built-in image generation (tested route)\n'
              '# Run these in a Codex session (or Claude Code with the Codex image tool).\n'
              '# Ask for one sheet per message and save each into the sheets/ folder.\n')
        for job in plan['jobs']:
            refs = ' '.join(shlex.quote(r) for r in job['references']) or 'none'
            transparent = 'false' if job['key'] else 'true'
            print(f'## {job["name"]}')
            print(f'Use image_gen with transparent_background: {transparent}, '
                  f'reference images: {refs}.')
            print(f'Prompt: {base / job["prompt_file"]}')
            print(f'Save the result to: {base / job["expected_sheet"]}\n')
        return
    print('# Higgsfield (UNTESTED, needs an owner run; nothing below has been executed)\n'
          '# Generation costs credits. Estimate first with `generate cost`.\n'
          '# Do not assume alpha, reference count or output size: read `model get` first.\n'
          '# Models without alpha: set key to magenta or green in cast.json and re-plan.\n')
    model = shlex.quote(args.model)
    print('higgsfield model list --json')
    print(f'higgsfield model get {model} --json')
    for job in plan['jobs']:
        prompt = base / job['prompt_file']
        refs = ' '.join(f'--image-references {shlex.quote(r)}' for r in job['references'])
        quoted = shlex.quote(str(prompt))
        print(f'\n# {job["name"]}')
        print(f'higgsfield generate cost {model} --prompt "$(cat {quoted})"')
        print(f'higgsfield generate create {model} --prompt "$(cat {quoted})" '
              f'{refs} --wait --json')
        print(f'# download the result URL to {shlex.quote(str(base / job["expected_sheet"]))}')


# --- ingest -----------------------------------------------------------------------

def key_out(image, key):
    """Remove a flat chroma-key background, soft edge, with despill."""
    r, g, b = KEYS[key]
    array = np.asarray(image.convert('RGB')).astype(np.float32)
    distance = np.sqrt(((array - np.array([r, g, b], dtype=np.float32)) ** 2).sum(axis=2))
    low, high = 60.0, 150.0
    alpha = np.clip((distance - low) / (high - low), 0, 1)
    rgba = np.dstack([array, alpha * 255]).astype(np.uint8)
    # despill: where the key channel exceeds the others, pull it down (int math, then clip to uint8)
    rgb = rgba[:, :, :3].astype(np.int16)
    if key == 'green':
        ceiling = np.maximum(rgb[:, :, 0], rgb[:, :, 2])
        rgb[:, :, 1] = np.minimum(rgb[:, :, 1], ceiling + 20)
    else:
        ceiling = rgb[:, :, 1]
        rgb[:, :, 0] = np.minimum(rgb[:, :, 0], ceiling + 20)
        rgb[:, :, 2] = np.minimum(rgb[:, :, 2], ceiling + 20)
    rgba[:, :, :3] = np.clip(rgb, 0, 255).astype(np.uint8)
    return Image.fromarray(rgba, 'RGBA')


def cell_boxes(width, height, grid):
    """Rounded cell rectangles, so a 1254 px sheet still splits evenly in 4."""
    return [(round(c * width / grid), round(r * height / grid),
             round((c + 1) * width / grid), round((r + 1) * height / grid))
            for r in range(grid) for c in range(grid)]


def remove_specks(array):
    # Generators leave a faint alpha haze around cutouts; drop it first (no SciPy needed).
    array[:, :, 3] = np.where(array[:, :, 3] < HAZE_BELOW, 0, array[:, :, 3])
    if ndimage is None:
        return array
    labels, count = ndimage.label(array[:, :, 3] > 80)
    if not count:
        return array
    sizes = np.bincount(labels.ravel())
    keep = np.flatnonzero(sizes > max(15, sizes[1:].max() * 0.001))
    keep = keep[keep != 0]
    mask = ndimage.binary_dilation(np.isin(labels, keep), iterations=1)
    array[:, :, 3] = np.where(mask, array[:, :, 3], 0)
    return array


def cmd_ingest(args):
    spec = KINDS[args.kind]
    grid, tile = spec['grid'], args.tile or spec['tile']
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'source').mkdir(exist_ok=True)
    source = Path(args.sheet)
    image = Image.open(source)
    (out / 'source' / source.name).write_bytes(source.read_bytes())  # keep the original
    if args.key:
        image = key_out(image, args.key)
    image = image.convert('RGBA')
    if image.width != image.height:
        print(f'warning: sheet is {image.width}x{image.height}, not square', file=sys.stderr)
    atlas = Image.new('RGBA', (tile * grid, tile * grid))
    frames = []
    for index, box in enumerate(cell_boxes(image.width, image.height, grid)):
        array = np.array(image.crop(box))
        if not (array[:, :, 3] > ALPHA_SOLID).any():
            die(f'cell {index} is empty. The sheet has no alpha, or the character is missing. '
                'Re-generate, or pass --key magenta|green if it came back on a flat colour.')
        array = remove_specks(array)
        cell = Image.fromarray(array).resize((tile, tile), Image.Resampling.LANCZOS)
        if spec['anchor'] == 'feet':
            solid = np.array(cell)[:, :, 3] > ALPHA_SOLID
            lowest = int(np.flatnonzero(solid.any(axis=1)).max())
            shift = round(tile * FEET_AT) - lowest
            moved = Image.new('RGBA', (tile, tile))
            moved.paste(cell, (0, shift))
            cell = moved
        col, row = index % grid, index // grid
        atlas.paste(cell, (col * tile, row * tile))
        frames.append({'i': index, 'x': col * tile, 'y': row * tile, 'w': tile, 'h': tile})
    atlas_file = out / f'{args.name}.webp'
    atlas.save(atlas_file, lossless=True)
    registry = out / 'sprites.json'
    data = json.loads(registry.read_text()) if registry.exists() else {'version': 1, 'sprites': {}}
    data['sprites'][args.name] = {
        'file': atlas_file.name, 'kind': args.kind, 'provider': args.provider,
        'model': args.model, 'promptFile': args.prompt_file,
        'source': f'source/{source.name}', 'keyed': args.key or None,
        'grid': {'columns': grid, 'rows': grid, 'order': 'row-major'},
        'tile': {'w': tile, 'h': tile}, 'size': {'w': atlas.width, 'h': atlas.height},
        'anchor': spec['anchor'], 'frames': frames, 'alphaChecked': False,
    }
    registry.write_text(json.dumps(data, indent=2) + '\n')
    print(f'{atlas_file} {atlas.size[0]}x{atlas.size[1]}, {len(frames)} frames; '
          f'registered in {registry}. Now run: sprites.py check {out}')


# --- check ------------------------------------------------------------------------

def check_sprite(name, entry, base):
    problems = []
    atlas = np.array(Image.open(base / entry['file']).convert('RGBA'))
    tile_w, tile_h = entry['tile']['w'], entry['tile']['h']
    areas, bottoms, centers = [], [], []
    for frame in entry['frames']:
        cell = atlas[frame['y']:frame['y'] + tile_h, frame['x']:frame['x'] + tile_w]
        alpha = cell[:, :, 3]
        solid = alpha > ALPHA_SOLID
        if not solid.any():
            problems.append(f'frame {frame["i"]}: empty')
            continue
        rows, cols = np.flatnonzero(solid.any(axis=1)), np.flatnonzero(solid.any(axis=0))
        areas.append(int(solid.sum()))
        bottoms.append(int(rows.max()))
        centers.append((int(cols.min()) + int(cols.max())) / 2)
        if rows.min() == 0 or cols.min() == 0 or rows.max() == tile_h - 1 or cols.max() == tile_w - 1:
            problems.append(f'frame {frame["i"]}: character touches the cell edge (clipped)')
        corners = [alpha[:4, :4], alpha[:4, -4:], alpha[-4:, :4], alpha[-4:, -4:]]
        if any(corner.max() > 20 for corner in corners):
            problems.append(f'frame {frame["i"]}: opaque pixels in a corner (painted background?)')
        fringe = ((alpha > 0) & (alpha < 20)).sum()
        if fringe > 0.02 * tile_w * tile_h:
            problems.append(f'frame {frame["i"]}: wide low-alpha fringe ({int(fringe)} px)')
    if len(areas) > 1:
        median = float(np.median(areas))
        for frame, area in zip(entry['frames'], areas):
            if area < 0.45 * median or area > 2.2 * median:
                problems.append(f'frame {frame["i"]}: silhouette area {area} vs median '
                                f'{int(median)} (identity or scale drift?)')
        if entry['anchor'] == 'feet' and max(bottoms) - min(bottoms) > tile_h * 0.04:
            problems.append(f'feet drift: lowest pixel varies {min(bottoms)}..{max(bottoms)}')
        if max(centers) - min(centers) > tile_w * 0.25:
            problems.append(f'horizontal drift: center varies {min(centers):.0f}..{max(centers):.0f}')
    return problems


def cmd_check(args):
    base = Path(args.dir)
    registry = base / 'sprites.json'
    if not registry.exists():
        die(f'{registry} not found. Run ingest first.')
    data = json.loads(registry.read_text())
    failed = False
    for name, entry in data['sprites'].items():
        problems = check_sprite(name, entry, base)
        entry['alphaChecked'] = not problems
        failed = failed or bool(problems)
        print(f'{"FAIL" if problems else "ok  "} {name}')
        for problem in problems:
            print(f'     {problem}')
    registry.write_text(json.dumps(data, indent=2) + '\n')
    print('Still inspect the sheets over a light AND a dark background: these checks '
          'cannot see identity or hand contact.')
    sys.exit(1 if failed else 0)


# --- selftest ---------------------------------------------------------------------

def synthetic_sheet(path, key=None):
    """A 4x4 sheet of a bobbing figure: tests keying, slicing, anchoring, checks."""
    from PIL import ImageDraw
    size = 1254  # not divisible by 4 on purpose
    background = (*KEYS[key], 255) if key else (0, 0, 0, 0)
    sheet = Image.new('RGBA', (size, size), background)
    draw = ImageDraw.Draw(sheet)
    for i, box in enumerate(cell_boxes(size, size, 4)):
        x0, y0, x1, y1 = box
        w, h = x1 - x0, y1 - y0
        bob = (i % 4) * 6
        cx = x0 + w // 2 + (i % 3 - 1) * 8
        draw.ellipse((cx - 40, y0 + h * .2 - bob, cx + 40, y0 + h * .2 + 80 - bob), fill=(200, 200, 210, 255))
        draw.rectangle((cx - 30, y0 + h * .2 + 80 - bob, cx + 30, y0 + h * .7 - bob), fill=(90, 120, 200, 255))
        draw.rectangle((cx - 28, y0 + h * .7 - bob, cx + 28, y0 + h * .82), fill=(60, 60, 80, 255))
    sheet.save(path)


def cmd_selftest(args):
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        for key in (None, 'magenta', 'green'):
            sheet = base / f'sheet-{key}.png'
            synthetic_sheet(sheet, key)
            ns = argparse.Namespace(sheet=str(sheet), name=f'fig-{key}', kind='dance', out=str(base / 'out'),
                                    key=key, tile=None, provider='selftest', model='none', prompt_file=None)
            cmd_ingest(ns)
        try:
            cmd_check(argparse.Namespace(dir=str(base / 'out')))
        except SystemExit as stop:
            if stop.code:
                die('selftest: checks failed on clean synthetic sheets')
        # an opaque painted-background sheet must FAIL the check
        bad = Image.new('RGBA', (400, 400), (255, 255, 255, 255))
        bad.save(base / 'bad.png')
        cmd_ingest(argparse.Namespace(sheet=str(base / 'bad.png'), name='bad', kind='dance',
                                      out=str(base / 'bad-out'), key=None, tile=None,
                                      provider='selftest', model='none', prompt_file=None))
        try:
            cmd_check(argparse.Namespace(dir=str(base / 'bad-out')))
        except SystemExit as stop:
            if not stop.code:
                die('selftest: an opaque white sheet should have failed the check')
        else:
            die('selftest: an opaque white sheet should have failed the check')
    print('selftest passed')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('plan', help='write one prompt file per sheet from cast.json')
    p.add_argument('cast')
    p.add_argument('--out', default='work/sprites')
    p.set_defaults(func=cmd_plan)
    p = sub.add_parser('provider', help='print the hand-off for a provider (never runs a paid job)')
    p.add_argument('name', choices=['codex', 'higgsfield'])
    p.add_argument('--plan', required=True)
    p.add_argument('--model', default='<MODEL_ID from `higgsfield model list`>')
    p.set_defaults(func=cmd_provider)
    p = sub.add_parser('ingest', help='key, slice, anchor and register one sheet')
    p.add_argument('sheet')
    p.add_argument('--name', required=True)
    p.add_argument('--kind', choices=sorted(KINDS), required=True)
    p.add_argument('--out', default='work/sprites')
    p.add_argument('--key', choices=sorted(KEYS), help='key a flat colour out (providers without alpha)')
    p.add_argument('--tile', type=int, help='output cell size in px')
    p.add_argument('--provider', default='unknown')
    p.add_argument('--model', default='not exposed')
    p.add_argument('--prompt-file')
    p.set_defaults(func=cmd_ingest)
    p = sub.add_parser('check', help='alpha, clipping, drift checks; exit 1 on failure')
    p.add_argument('dir')
    p.set_defaults(func=cmd_check)
    p = sub.add_parser('selftest', help='run the pipeline on synthetic sheets')
    p.set_defaults(func=cmd_selftest)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
