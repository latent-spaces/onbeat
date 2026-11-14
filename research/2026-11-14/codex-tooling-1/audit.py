"""Read-only, standard-library audit of the committed demo inputs.
Run from the repository root; prints JSON and does not render or fetch models.
"""
import json
import math
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
result = {"method": "Static literal src/href/CSS url references; HyperFrames subcomposition assets resolve from project root. Dynamic paths are not exhaustively evaluated.", "base_commit": subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip()}
result["compositions"] = []
for rel in ["video/index.html", "video/scale/index.html", "video/allow-always/index.html", "video/allow-always-final/index.html", "video/avatar-dance-test/index.html", "video/avatar-dance-test/compositions/orbital.html", "video/avatar-dance-test/compositions/karaoke.html"]:
    page = ROOT / rel
    refs = re.findall(r'(?:src|href)="([^"]+)"', page.read_text())
    refs += re.findall(r'''url\(["']?([^\)"']+)["']?\)''', page.read_text())
    local = [r for r in refs if " + " not in r and not re.match(r"https?://|#|data:", r)]
    asset_root = ROOT / "video/avatar-dance-test" if "/compositions/" in rel else page.parent
    result["compositions"].append({"page": rel, "local_references": [{"path": r, "exists": (asset_root / r).exists()} for r in local], "external_references": [r for r in refs if r.startswith("https://")]})
result["timing_data"] = []
for path in sorted((ROOT / "video/data").glob("*.json")):
    data = json.loads(path.read_text())
    twin = path.with_suffix(".js").read_text().strip()
    js_data = json.loads(twin.removeprefix("window.TIMING = ").removesuffix(";"))
    words = data["words"]
    invalid = [i for i, w in enumerate(words) if not (0 <= w["start"] <= w["end"] <= data["duration"])]
    zero = [i for i, w in enumerate(words) if w["start"] == w["end"]]
    bad_lines = [i for i, w in enumerate(words) if not 0 <= w["line"] < len(data["lines"])]
    result["timing_data"].append({"path": str(path.relative_to(ROOT)), "duration": data["duration"], "words": len(words), "json_js_match": data == js_data, "word_intervals_outside_duration_or_reversed": invalid, "zero_duration_words": zero, "invalid_line_indices": bad_lines, "envelope_lengths": {k: len(data["envelopes"][k]) for k in ["kick", "rms"]}, "expected_frames": math.ceil(data["duration"] * data["fps"]), "declared_hop": data["envelopes"]["hop"], "frame_hop": 1 / data["fps"]})
print(json.dumps(result, indent=2))
