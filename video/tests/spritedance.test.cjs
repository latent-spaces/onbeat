// Run: node --test video/tests/spritedance.test.cjs
const test = require("node:test");
const assert = require("node:assert");
const path = require("node:path");
const fs = require("node:fs");
const vm = require("node:vm");
// Load it the way the browser does: a classic script that sets window.SpriteDance.
const win = {};
vm.runInNewContext(fs.readFileSync(path.join(__dirname, "..", "src", "spritedance.js"), "utf8"), { window: win });
const SD = win.SpriteDance;
const T = require(path.join(__dirname, "..", "data", "allow-always-final.json"));

function fakeTimeline() {
  const calls = [];
  return {
    calls,
    set(target, vars, time) { calls.push({ kind: "set", target, vars, time }); return this; },
    fromTo(target, from, to, time) { calls.push({ kind: "fromTo", target, from, to, time }); return this; },
    to(target, vars, time) { calls.push({ kind: "to", target, vars, time }); return this; },
  };
}

const groove = T.sections.find((s) => s.kick);
const quiet = T.sections.find((s) => !s.kick);

test("16 poses fill one bar and pose 0 lands on the downbeat", () => {
  const bar = T.bars.findIndex((b) => b >= groove.start - 1e-6);
  const o = { from: T.bars[bar], to: T.bars[bar + 1], poses: 16 };
  const st = SD.steps(T, o.from, o.to, 4);
  assert.strictEqual(st.length, 16);
  assert.strictEqual(SD.poseAt(T, st[0].t + 0.001, o), 0);
  assert.strictEqual(SD.poseAt(T, st[15].t + 0.001, o), 15);
});

test("phase offsets shift the cycle", () => {
  const t = T.bars[T.bars.findIndex((b) => b >= groove.start - 1e-6)] + 0.001;
  const base = { from: 0, to: T.duration, poses: 16 };
  assert.strictEqual(SD.poseAt(T, t, { ...base, phase: 8 }), 8);
  assert.strictEqual(SD.poseAt(T, t, { ...base, phase: 4 }), 4);
});

test("holds the hold pose through a section without a kick", () => {
  const o = { from: 0, to: T.duration, poses: 16, holdPose: 3 };
  const mid = (quiet.start + quiet.end) / 2;
  assert.strictEqual(SD.poseAt(T, mid, o), 3);
  assert.notStrictEqual(SD.poseAt(T, mid, { ...o, hold: "none" }), null);
});

test("dance() is deterministic, frame-aligned and bounces only on kick beats", () => {
  const run = () => {
    const tl = fakeTimeline();
    SD.dance(tl, T, { target: "#d", from: quiet.start, to: groove.end + 4, poses: 16 });
    return tl.calls;
  };
  const a = run();
  assert.deepStrictEqual(a, run());
  for (const c of a) {
    const f = (c.time + 1e-4) * T.fps;
    assert.ok(c.time === 0 || Math.abs(f - Math.round(f)) < 1e-6 || c.kind === "to", "set/fromTo placed on a frame: " + c.time);
  }
  const hops = a.filter((c) => c.kind === "fromTo");
  for (const h of hops) assert.ok(!SD.silentAt(T, h.time + 2e-4), "no hop in a silent section");
  const big = hops.filter((h) => h.to.y < -14 - 1e-9);
  assert.ok(big.length > 0 && big.length < hops.length, "downbeats get the bigger accent");
});

test("cellPosition and rectPosition agree for a regular grid", () => {
  const sheet = { width: 1254, height: 1254, frames: [] };
  for (let i = 0; i < 9; i++) sheet.frames.push({ x: (i % 3) * 418, y: Math.floor(i / 3) * 418, width: 418, height: 418 });
  for (let i = 0; i < 9; i++) assert.strictEqual(SD.rectPosition(sheet, i), SD.cellPosition(i, 3, 3));
});
