# music-reels: short entry points. Run `make help`.
SHELL := /bin/bash
HF    := npx --yes hyperframes@0.9.2
PY    := .venv/bin/python
SONG  ?=
WORDS ?= 0

.PHONY: help doctor setup sample timing render check

help:
	@echo "make doctor               check tools and print fixes"
	@echo "make sample               render the bundled no-key sample -> out/sample.mp4"
	@echo "make setup                create .venv with pinned requirements (needed for timing)"
	@echo "make timing SONG=name     songs/<name>/song.(mp3|m4a|wav) -> songs/<name>/timing.json (beats only)"
	@echo "make timing SONG=name WORDS=1   also align sung words (needs .venv-align, see GUIDE.md section 2)"
	@echo "make render SONG=name     render songs/<name> with the template -> out/<name>.mp4"

doctor:
	@scripts/doctor.sh

setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

sample:
	@mkdir -p out
	cd video/avatar-dance-test && $(HF) render --output ../../out/sample.mp4 --fps 30 --workers 2
	@echo "Sample written to out/sample.mp4"

check:
	cd video/avatar-dance-test && $(HF) check

timing:
	@test -n "$(SONG)" || { echo "usage: make timing SONG=<name>  (folder songs/<name>/)"; exit 1; }
	@test -x $(PY) || { echo "No .venv yet. Run: make setup"; exit 1; }
	@AUDIO=$$(ls songs/$(SONG)/song.mp3 songs/$(SONG)/song.m4a songs/$(SONG)/song.wav 2>/dev/null | head -1); \
	test -n "$$AUDIO" || { echo "Put the audio at songs/$(SONG)/song.mp3 (or .m4a/.wav)"; exit 1; }; \
	if [ "$(WORDS)" = "1" ]; then \
	  LYR=""; [ -f songs/$(SONG)/lyrics.txt ] && LYR="--lyrics songs/$(SONG)/lyrics.txt"; \
	  $(PY) scripts/timing.py "$$AUDIO" $$LYR -o songs/$(SONG)/timing.json; \
	else \
	  $(PY) scripts/timing.py "$$AUDIO" --no-words -o songs/$(SONG)/timing.json; \
	fi

render:
	@test -n "$(SONG)" || { echo "usage: make render SONG=<name>"; exit 1; }
	@test -f songs/$(SONG)/timing.json || { echo "No songs/$(SONG)/timing.json. Run: make timing SONG=$(SONG)"; exit 1; }
	@test -x scripts/render_song.sh || { echo "The song template is not installed yet (video/template/)."; exit 1; }
	scripts/render_song.sh $(SONG)
