#!/usr/bin/env python3
"""Sprite sheets from any image provider, one asset contract.

    sprites.py prompt   SPEC SHEET            print the generation prompt
    sprites.py generate SPEC SHEET --provider codex|higgsfield [--run]
    sprites.py ingest   SPEC SHEET IMAGE      copy, check and record a returned sheet
    sprites.py check    SPEC [SHEET]          re-run the alpha/drift checks
    sprites.py doctor                         show what this machine can do

SPEC is a JSON file (see docs/sprites.md and sprites/example-spec.json). A sheet is a
grid of equally sized cells read left-to-right, top-to-bottom. Whatever provider drew
it, `ingest` writes the same record into <outDir>/sprites.json, so the animation code
(video/src/sprite-dance.js) never changes per provider.

Pure standard library: PNG sheets are decoded here, so the checks run without Pillow.
Keying a sheet that came back without alpha needs vendor/page-mascot's key.py
(Pillow, NumPy, SciPy); `ingest --key` calls it.
"""
import argparse
import json
import shutil
import struct
import subprocess
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KEY_SCRIPT = ROOT / "vendor/page-mascot/skills/page-mascot/scripts/key.py"
KINDS = {
    "dance": "{n} ordered full-body poses of one character dancing to a steady beat: weight shifts, "
             "foot contacts, arm swings, last pose leads back into the first so the loop has no seam",
    "closeup": "{n} head-and-shoulders views of one character, different angles and expressions, "
               "shoulders and scale steady",
    "action": "{n} successive frames of one action, fixed camera and props, each frame a clear next step",
    "effect": "{n} successive stages of one effect, fixed origin and scale, from first spark to last fade",
}
CONTRACT = (
    "Fixed camera, same character identity, outfit, scale and ground line in every cell. "
    "Equal square cells in a {columns}x{rows} grid read left to right then top to bottom. "
    "Each figure fully inside its cell with empty margin. No labels, numbers, borders or grid lines."
)
ALPHA_TEXT = "Transparent background (real alpha channel)."
KEY_TEXT = "Solid flat {key} background, one pure colour, no gradient, no shadow on the background."


def die(msg):
    sys.stderr.write("error: " + msg + "\n")
    sys.exit(1)


def load_spec(path):
    p = Path(path)
    if not p.is_file():
        die("spec not found: %s" % p)
    spec = json.loads(p.read_text())
    spec["_dir"] = p.resolve().parent
    spec.setdefault("outDir", "sprites-out")
    return spec


def out_dir(spec):
    d = (spec["_dir"] / spec["outDir"]).resolve()
    d.mkdir(parents=True, exist_ok=True)
    return d


def find_sheet(spec, sheet_id):
    for s in spec["sheets"]:
        if s["id"] == sheet_id:
            return s
    die("no sheet %r in spec; have: %s" % (sheet_id, ", ".join(s["id"] for s in spec["sheets"])))


def cell_rects(width, height, columns, rows):
    """Rounded boundaries, so sheets whose width is not divisible by columns still pack evenly."""
    xs = [round(i * width / columns) for i in range(columns + 1)]
    ys = [round(j * height / rows) for j in range(rows + 1)]
    return [{"i": r * columns + c, "x": xs[c], "y": ys[r], "w": xs[c + 1] - xs[c], "h": ys[r + 1] - ys[r]}
            for r in range(rows) for c in range(columns)]


def build_prompt(spec, sheet, use_alpha):
    g = sheet["grid"]
    n = g["columns"] * g["rows"]
    parts = [
        spec.get("style", "").strip(),
        "Character: " + sheet.get("character", spec.get("character", "")).strip(),
        "Sheet: " + KINDS[sheet["kind"]].format(n=n) + ".",
        sheet.get("motion", "").strip(),
        CONTRACT.format(**g),
        ALPHA_TEXT if use_alpha else KEY_TEXT.format(key=sheet.get("keyColor", "magenta #FF00FF")),
    ]
    return "\n".join(p for p in parts if p)


def cmd_prompt(a):
    spec = load_spec(a.spec)
    sheet = find_sheet(spec, a.sheet)
    print(build_prompt(spec, sheet, use_alpha=sheet.get("alpha", True)))


def provider_alpha(provider, sheet):
    # Codex built-in image generation can emit a real alpha channel; Higgsfield models vary
    # and the contract assumes they do not until `higgsfield model get` says otherwise.
    return sheet.get("alpha", provider == "codex")


def cmd_generate(a):
    spec = load_spec(a.spec)
    sheet = find_sheet(spec, a.sheet)
    use_alpha = provider_alpha(a.provider, sheet)
    od = out_dir(spec)
    prompt_file = od / (sheet["id"] + "-prompt.txt")
    prompt_file.write_text(build_prompt(spec, sheet, use_alpha) + "\n")
    refs = [str((spec["_dir"] / r).resolve()) for r in sheet.get("references", [])]
    target = od / (sheet["id"] + "-raw.png")
    if a.provider == "codex":
        print("Prompt written to %s" % prompt_file)
        print("In Codex (built-in image generation) ask:\n")
        print('  Generate an image from the prompt in %s%s%s. Save it as %s.' % (
            prompt_file, " using references " + ", ".join(refs) if refs else "",
            " with a transparent background" if use_alpha else "", target))
        print("\nThen: sprites.py ingest %s %s %s%s" % (a.spec, sheet["id"], target, "" if use_alpha else " --key"))
        return
    model = sheet.get("higgsfield", {}).get("model", "<model-id from `higgsfield model list --json`>")
    cmd = ["higgsfield", "generate", "create", model, "--prompt", build_prompt(spec, sheet, use_alpha)]
    for r in refs:
        cmd += ["--image-references", r]
    for k, v in sheet.get("higgsfield", {}).get("params", {}).items():
        cmd += ["--" + k, str(v)]
    cmd += ["--wait", "--json"]
    if not a.run:
        print("UNTESTED, needs owner run. Dry run only; nothing was sent and no credits spent.\n")
        print("1. higgsfield model get %s --json   # check alpha, reference count, sizes first" % model)
        print("2. " + " ".join(shlex_quote(c) for c in cmd))
        print("\nSave the result image as %s, then run ingest%s." % (target, " --key" if not use_alpha else ""))
        return
    if not a.i_accept_credits:
        die("--run spends Higgsfield credits; add --i-accept-credits to confirm")
    rc = subprocess.run(cmd, check=False).returncode
    if rc:
        die("higgsfield exited with status %d" % rc)


def shlex_quote(s):
    import shlex
    return shlex.quote(s)


# ---- PNG decoding (8-bit RGBA/RGB/gray+alpha, non-interlaced) ---------------------------

def read_png(path):
    data = Path(path).read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        die("%s is not a PNG; convert it first (ffmpeg -i in.webp out.png)" % path)
    pos, idat, ihdr = 8, [], None
    while pos < len(data):
        ln, typ = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + ln]
        if typ == b"IHDR":
            ihdr = struct.unpack(">IIBBBBB", body)
        elif typ == b"IDAT":
            idat.append(body)
        pos += 12 + ln
    w, h, depth, ctype, _, _, interlace = ihdr
    if depth != 8 or interlace or ctype not in (2, 4, 6):
        die("%s: need 8-bit non-interlaced RGB, RGBA or gray+alpha PNG" % path)
    ch = {2: 3, 4: 2, 6: 4}[ctype]
    raw = zlib.decompress(b"".join(idat))
    stride = w * ch
    rows, prev = [], bytearray(stride)
    for y in range(h):
        f = raw[y * (stride + 1)]
        line = bytearray(raw[y * (stride + 1) + 1:(y + 1) * (stride + 1)])
        for i in range(stride):
            a = line[i - ch] if i >= ch else 0
            b = prev[i]
            c = prev[i - ch] if i >= ch else 0
            if f == 1:
                line[i] = (line[i] + a) & 255
            elif f == 2:
                line[i] = (line[i] + b) & 255
            elif f == 3:
                line[i] = (line[i] + ((a + b) >> 1)) & 255
            elif f == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        rows.append(line)
        prev = line
    alpha = None
    if ctype == 6:
        alpha = [r[3::4] for r in rows]
    elif ctype == 4:
        alpha = [r[1::2] for r in rows]
    return w, h, ch, rows, alpha


def analyse(path, grid):
    """Alpha and drift checks. Returns (info, findings)."""
    w, h, ch, rows, alpha = read_png(path)
    findings = []
    if alpha is None:
        return {"width": w, "height": h, "hasAlpha": False}, [
            ("fail", "no alpha channel; generate on a key colour and run ingest --key")]
    cells = cell_rects(w, h, grid["columns"], grid["rows"])
    corners = [alpha[0][0], alpha[0][w - 1], alpha[h - 1][0], alpha[h - 1][w - 1]]
    if max(corners) > 8:
        findings.append(("fail", "corner alpha %s: background is painted, not transparent" % corners))
    boxes = []
    for c in cells:
        x0, y0, x1, y1 = c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"]
        minx = miny = 10 ** 9
        maxx = maxy = -1
        edge = 0
        for y in range(y0, y1):
            row = alpha[y]
            for x in range(x0, x1):
                if row[x] > 16:
                    minx, maxx = min(minx, x), max(maxx, x)
                    miny, maxy = min(miny, y), max(maxy, y)
                    if x in (x0, x1 - 1) or y in (y0, y1 - 1):
                        edge += 1
        if maxx < 0:
            findings.append(("fail", "cell %d is empty" % c["i"]))
            boxes.append(None)
            continue
        if edge:
            findings.append(("warn", "cell %d touches its border (%d px): figure cut off or no gutter" % (c["i"], edge)))
        boxes.append({"i": c["i"], "x": minx - x0, "y": miny - y0, "w": maxx - minx + 1, "h": maxy - miny + 1,
                      "bottom": maxy - y0})
    good = [b for b in boxes if b]
    if len(good) > 2:
        hs = sorted(b["h"] for b in good)
        med = hs[len(hs) // 2]
        for b in good:
            if abs(b["h"] - med) > 0.25 * med:
                findings.append(("warn", "cell %d height %d vs median %d: scale drift" % (b["i"], b["h"], med)))
        bs = sorted(b["bottom"] for b in good)
        medb = bs[len(bs) // 2]
        for b in good:
            if abs(b["bottom"] - medb) > 0.08 * (h // grid["rows"]):
                findings.append(("warn", "cell %d ground line off by %d px" % (b["i"], b["bottom"] - medb)))
    return {"width": w, "height": h, "hasAlpha": True, "cells": cells, "bounds": boxes}, findings


def report(findings):
    for level, msg in findings:
        print("%s: %s" % (level.upper(), msg))
    if not findings:
        print("OK: alpha, gutters and per-cell scale look consistent (still look at it on light and dark).")
    return not any(l == "fail" for l, _ in findings)


def cmd_ingest(a):
    spec = load_spec(a.spec)
    sheet = find_sheet(spec, a.sheet)
    od = out_dir(spec)
    src = Path(a.image)
    if not src.is_file():
        die("image not found: %s" % src)
    dst = od / (sheet["id"] + ".png")
    shutil.copyfile(src, od / (sheet["id"] + "-source" + src.suffix))
    shutil.copyfile(src, dst)
    if a.key:
        if not KEY_SCRIPT.is_file():
            die("keying needs %s" % KEY_SCRIPT)
        r = subprocess.run([sys.executable, str(KEY_SCRIPT), str(dst), "--in-place"])
        if r.returncode:
            die("key.py failed (needs Pillow, NumPy, SciPy in this Python)")
    info, findings = analyse(dst, sheet["grid"])
    ok = report(findings)
    record = {
        "file": dst.name, "provider": a.provider or sheet.get("provider", "unknown"),
        "model": a.model or "not exposed", "promptFile": sheet["id"] + "-prompt.txt",
        "references": sheet.get("references", []), "kind": sheet["kind"], "id": sheet["id"],
        "grid": dict(sheet["grid"], order="row-major"),
        "dimensions": {"width": info["width"], "height": info["height"]},
        "cells": info.get("cells", []), "bounds": info.get("bounds", []),
        "playback": sheet.get("playback", {"fps": 12}),
        "anchor": sheet.get("anchor", ""), "alphaChecked": bool(ok and info["hasAlpha"]),
    }
    idx = od / "sprites.json"
    doc = json.loads(idx.read_text()) if idx.is_file() else {"version": 1, "sheets": []}
    doc["sheets"] = [s for s in doc["sheets"] if s["id"] != record["id"]] + [record]
    idx.write_text(json.dumps(doc, indent=2) + "\n")
    print("wrote %s (%d sheet(s))" % (idx, len(doc["sheets"])))
    sys.exit(0 if ok else 2)


def cmd_check(a):
    spec = load_spec(a.spec)
    ok = True
    for s in spec["sheets"]:
        if a.sheet and s["id"] != a.sheet:
            continue
        f = out_dir(spec) / (s["id"] + ".png")
        if not f.is_file():
            print("%s: not generated yet" % s["id"])
            continue
        print("== " + s["id"])
        ok &= report(analyse(f, s["grid"])[1])
    sys.exit(0 if ok else 2)


def cmd_doctor(_):
    print("python:", sys.version.split()[0])
    print("higgsfield CLI:", shutil.which("higgsfield") or "not found (only needed for the Higgsfield route)")
    print("codex CLI:", shutil.which("codex") or "not found (only needed for the Codex route)")
    print("key.py:", "present" if KEY_SCRIPT.is_file() else "missing")
    try:
        import numpy, PIL, scipy  # noqa: F401
        print("keying deps: ok")
    except ImportError as e:
        print("keying deps: missing (%s); only `ingest --key` needs them" % e.name)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    x = sub.add_parser("prompt"); x.add_argument("spec"); x.add_argument("sheet"); x.set_defaults(f=cmd_prompt)
    x = sub.add_parser("generate"); x.add_argument("spec"); x.add_argument("sheet")
    x.add_argument("--provider", choices=["codex", "higgsfield"], required=True)
    x.add_argument("--run", action="store_true", help="higgsfield only: actually submit (spends credits)")
    x.add_argument("--i-accept-credits", action="store_true"); x.set_defaults(f=cmd_generate)
    x = sub.add_parser("ingest"); x.add_argument("spec"); x.add_argument("sheet"); x.add_argument("image")
    x.add_argument("--provider"); x.add_argument("--model"); x.add_argument("--key", action="store_true")
    x.set_defaults(f=cmd_ingest)
    x = sub.add_parser("check"); x.add_argument("spec"); x.add_argument("sheet", nargs="?"); x.set_defaults(f=cmd_check)
    x = sub.add_parser("doctor"); x.set_defaults(f=cmd_doctor)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
