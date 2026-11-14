#!/usr/bin/env bash
# Checks the tools music-reels needs and prints the fix for anything missing.
ok=0; warn=0
pass() { printf '  \033[32mok\033[0m    %s\n' "$1"; }
fail() { printf '  \033[31mmissing\033[0m %s\n        fix: %s\n' "$1" "$2"; ok=1; }
soft() { printf '  \033[33moptional\033[0m %s\n        fix: %s\n' "$1" "$2"; warn=1; }

echo "Needed for 'make sample' and 'make render':"
if command -v node >/dev/null; then
  major=$(node -p 'process.versions.node.split(".")[0]')
  if [ "$major" -ge 22 ]; then pass "node $(node -v)"; else fail "node >= 22 (found $(node -v))" "install Node 22+ from https://nodejs.org or 'brew install node'"; fi
else fail "node" "install Node 22+ from https://nodejs.org or 'brew install node'"; fi
command -v npx >/dev/null && pass "npx" || fail "npx" "comes with Node; reinstall Node"
command -v ffmpeg >/dev/null && pass "ffmpeg $(ffmpeg -version | head -1 | awk '{print $3}')" || fail "ffmpeg" "'brew install ffmpeg' (macOS) or 'sudo apt install ffmpeg'"
if [ -d "$HOME/.npm/_npx" ] && ls "$HOME"/.npm/_npx/*/node_modules/hyperframes >/dev/null 2>&1; then
  pass "hyperframes CLI cached"
else
  soft "hyperframes CLI not cached yet" "nothing to do: the first 'make sample' downloads hyperframes@0.9.2 and a browser (takes a few minutes once)"
fi

echo "Needed for 'make timing' (your own song):"
command -v python3 >/dev/null && pass "python3 $(python3 -V | awk '{print $2}')" || soft "python3" "install Python 3.12+"
if [ -x .venv/bin/python ] && .venv/bin/python -c 'import librosa, numpy, scipy' 2>/dev/null; then pass ".venv with librosa/numpy/scipy"
else soft ".venv not set up" "make setup"; fi

echo "Only for sung-word alignment (make timing WORDS=1):"
if [ -x .venv-align/bin/python ]; then pass ".venv-align"
else soft ".venv-align not set up" "see GUIDE.md section 2 (python3.12 -m venv .venv-align && .venv-align/bin/pip install -r requirements-align.txt)"; fi

echo
if [ $ok -eq 0 ]; then echo "Ready: run 'make sample'."; else echo "Fix the missing items above, then run 'make doctor' again."; fi
exit $ok
