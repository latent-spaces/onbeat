#!/usr/bin/env bash
# Local only: render the bundled example in a new scratch folder and inspect it.
set -eu
skill_dir="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
scratch_dir="$(mktemp -d "${TMPDIR:-/tmp}/onbeat-smoke.XXXXXX")"
cp -R "$skill_dir/example" "$scratch_dir/example"
cd "$scratch_dir/example"
npx --yes hyperframes@0.9.2 check
npx --yes hyperframes@0.9.2 render --output out/example.mp4
node - "$scratch_dir/example/out/example.mp4" <<'JS'
const assert = require('node:assert/strict');
const { execFileSync } = require('node:child_process');
const streams = JSON.parse(execFileSync('ffprobe', [
  '-v', 'error', '-show_streams', '-of', 'json', process.argv[2],
], { encoding: 'utf8' })).streams;
const video = streams.find(s => s.codec_type === 'video');
const audio = streams.find(s => s.codec_type === 'audio');
const html = require('node:fs').readFileSync('index.html', 'utf8');
const expectedDuration = Number(html.match(/id="root"[^>]*data-duration="([\d.]+)"/)[1]);
assert.ok(video && audio, 'output must contain video and audio');
assert.equal(video.width, 1080);
assert.equal(video.height, 1920);
assert.equal(video.r_frame_rate, '30/1');
assert.ok(Math.abs(Number(video.duration) - expectedDuration) <= 1 / 30);
assert.ok(Math.abs(Number(audio.duration) - Number(video.duration)) <= 1 / 30);
console.log(`Smoke passed: ${process.argv[2]}`);
JS
