# Short, deterministic entry points; no generated media or analysis dependencies for the sample.
.DEFAULT_GOAL := help
PYTHON ?= python3
export SONG AUDIO LYRICS WORDS BEATS_ONLY MODE OUT SYNC_CHECK FORCE PYTHON_SETUP
.PHONY: help doctor browser setup setup-align sample check timing render
help doctor browser setup setup-align sample check timing render:
	@$(PYTHON) scripts/reel.py $@
