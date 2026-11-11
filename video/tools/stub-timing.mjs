// Writes a stub timing JSON (playbook section 7 contract) for the dev audio grid of the
// breakout reel: 129.082 BPM, first downbeat 0.074 s, kick at bar 4. Words are our own
// placeholders, deliberately placed off the beat grid to exercise the vocal layer.
//
//   node tools/stub-timing.mjs short data/stub-short.json   (8 bars, ~14.9 s)
//   node tools/stub-timing.mjs long  data/stub-long.json    (24 bars, ~44.7 s, 120 words)
import { writeFileSync } from "node:fs";

const [mode = "short", outPath = "data/stub-short.json"] = process.argv.slice(2);
const FPS = 60;
const PERIOD = 0.46482;
const DOWNBEAT = 0.074;
const BPB = 4;
const bars = mode === "long" ? 24 : 8;
const r3 = (x) => Math.round(x * 1000) / 1000;

const beats = [];
for (let i = 0; i < bars * BPB; i++) beats.push(r3(DOWNBEAT + i * PERIOD));
const barTimes = beats.filter((_, i) => i % BPB === 0);
const duration = r3(DOWNBEAT + bars * BPB * PERIOD);
const beat = (i) => DOWNBEAT + i * PERIOD;

// Each phrase: words placed at beat index + fractional offset (never a multiple of 1/4 beat).
// [text, firstBeat, spacingInBeats, offsetBeats]
const shortPhrases = [
  ["test line one", 0, 0.55, 0.42],
  ["drops in here", 2, 0.6, 0.31],
  ["each word lights", 8, 0.7, 0.37],
  ["then it greys", 11, 0.65, 0.29],
  ["pla ce hol der", 17, 1, 0.27], // syllable stack, one per beat, a 16th-and-a-bit late
  ["back to start", 24, 0.6, 0.35],
  ["and loop it", 27, 0.55, 0.41],
];
const longVocab = ["test", "word", "line", "ping", "loop", "grid", "beat", "step", "code", "draw", "blip", "tick"];

function makePhrases() {
  if (mode !== "long") return shortPhrases;
  const out = [];
  // 40 lines of 3 short words = 120 words, one line every 2.4 beats (lines fit 1080 px).
  for (let l = 0; l < 40; l++) {
    const words = [];
    for (let w = 0; w < 3; w++) words.push(longVocab[(l * 3 + w * 5) % longVocab.length]);
    out.push([words.join(" "), l * 2.4, 0.6, 0.33 + (l % 3) * 0.04]);
  }
  return out;
}

const words = [];
const lines = [];
makePhrases().forEach(([text, b0, step, off], li) => {
  const parts = text.split(" ");
  parts.forEach((w, wi) => {
    const start = beat(b0 + off + wi * step);
    words.push({ text: w, start: r3(start), end: r3(start + step * PERIOD * 0.85), line: li });
  });
  const lw = words.filter((w) => w.line === li);
  lines.push({ text, start: lw[0].start, end: lw[lw.length - 1].end });
});

const sections = [
  { name: "hook", start: 0, end: r3(barTimes[4]), startBar: 0 },
  { name: "drop", start: r3(barTimes[4]), end: duration, startBar: 4 },
];
const nFrames = Math.ceil(duration * FPS);
const timing = {
  audio: mode === "long" ? "assets/dev/dev24bars.wav" : "assets/dev/dev8bars.wav",
  duration, fps: FPS, bpm: 129.082, beatPeriod: PERIOD, beatsPerBar: BPB,
  beats, bars: barTimes, words, lines, sections,
  envelopes: { hop: r3(1 / FPS), kick: new Array(nFrames).fill(0), rms: new Array(nFrames).fill(0) },
};
writeFileSync(outPath, JSON.stringify(timing));
// Classic-script twin so the composition can load the data without a fetch.
writeFileSync(outPath.replace(/\.json$/, ".js"), `window.TIMING = ${JSON.stringify(timing)};\n`);
process.stdout.write(`${outPath}: ${beats.length} beats, ${words.length} words, ${lines.length} lines, ${duration} s\n`);
