#!/usr/bin/env bash
# Compatibility entry point; diagnostic policy lives in the same wrapper as make sample.
exec python3 "$(dirname "$0")/reel.py" doctor "$@"
