const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const example = path.join(__dirname, "../skills/onbeat/examples/four-styles");

function build() {
  const window = {};
  const context = vm.createContext({
    window,
    document: {
      getElementById: (id) => ({ id, dataset: { fps: "30" } }),
    },
  });
  for (const file of [
    "data/timing.js",
    "src/beatsync.js",
    "src/spritedance.js",
    "src/groove.js",
    "src/showcase.js",
  ]) {
    vm.runInContext(fs.readFileSync(path.join(example, file), "utf8"), context);
  }
  window.BeatSync.KaraokeLine = () => {};
  window.TIMING.fps = 30;
  window.SyncCheck = { wanted: () => false };
  const calls = [];
  const tl = Object.fromEntries(
    ["set", "to", "fromTo"].map((kind) => [
      kind,
      (...args) => {
        const time = args[kind === "fromTo" ? 3 : 2];
        assert.ok(
          Number.isFinite(time) &&
            time >= 0 &&
            time <= window.TIMING.duration + 1 / 30,
          "finite in-range timeline time",
        );
        calls.push({ kind, args: JSON.parse(JSON.stringify(args)), time });
        return tl;
      },
    ]),
  );
  window.OnBeatShowcase(tl, window.TIMING);
  return { calls, timing: window.TIMING, window };
}

test("showcase uses dedicated nine-pose portraits for every material", () => {
  const { calls, timing: T } = build();
  const manifest = JSON.parse(
    fs.readFileSync(path.join(example, "assets/cast/sprites.json"), "utf8"),
  );
  const portraits = calls.filter(
    (c) => c.args[0] === "#portrait" && c.args[1].backgroundImage,
  );
  assert.ok(
    T.duration > 30 && T.duration < 40,
    "longer showcase, not a looped short excerpt",
  );
  for (const name of ["moth", "beet", "clay", "anime"]) {
    const entry = manifest.sprites[name + "-close"];
    assert.equal(entry.kind, "portrait");
    assert.equal(entry.grid.columns, 3);
    assert.equal(entry.grid.rows, 3);
    assert.equal(entry.frames.length, 9);
    assert.ok(entry.alphaChecked);
    assert.ok(
      portraits.some((c) =>
        c.args[1].backgroundImage.includes(name + "-close.webp"),
      ),
    );
    for (const key of ["file", "source", "promptFile"])
      assert.ok(
        fs.existsSync(path.resolve(example, "assets/cast", entry[key])),
      );
  }
  const positions = new Set(
    calls
      .filter((c) => c.args[0] === "#portrait")
      .map((c) => c.args[1].backgroundPosition)
      .filter(Boolean),
  );
  assert.equal(positions.size, 9, "all nine facial drawings take part");
  for (const shot of portraits) {
    const end = calls.find(
      (c) =>
        c.time > shot.time &&
        c.args[0] === "#portrait" &&
        c.args[1].opacity === 0,
    );
    assert.ok(
      end && end.time - shot.time >= T.beatPeriod * 4 - 1 / 30,
      "face dance holds at least four beats",
    );
  }
});

test("the anthology always shows one solo dancer or one face, never an ensemble", () => {
  const { calls, timing: T } = build();
  const states = { moth: 0, beet: 0, clay: 0, anime: 0, portrait: 0 };
  const events = calls
    .filter((c) => c.kind === "set")
    .sort((a, b) => a.time - b.time);
  let next = 0;
  for (let frame = 0; frame / 30 < T.duration; frame++) {
    const t = frame / 30;
    while (next < events.length && events[next].time <= t + 1e-8) {
      const [target, vars] = events[next++].args;
      if (typeof target !== "string" || vars.opacity == null) continue;
      const match = /^#(moth|beet|clay|anime)-actor$/.exec(target);
      if (match) states[match[1]] = vars.opacity;
      if (target === "#portrait") states.portrait = vars.opacity;
    }
    assert.equal(
      Object.values(states).filter((opacity) => opacity > 0.5).length,
      1,
      "one visual lead at t=" + t,
    );
  }
});

test("pose choreography is deterministic and strong drawings land on measured beats", () => {
  const a = build();
  assert.deepEqual(a.calls, build().calls);
  for (const name of ["moth", "beet", "clay", "anime"]) {
    const poses = a.window.Groove.schedule(
      a.timing,
      name,
      0,
      a.timing.duration,
    );
    assert.ok(poses.length > 200);
    for (const pose of poses) {
      assert.ok(pose.pose >= 0 && pose.pose < 16);
      if (pose.sub === 0) {
        assert.ok(a.timing.beats.some((b) => Math.abs(b - pose.time) < 1e-6));
        assert.equal(
          pose.pose % 4,
          3,
          "the strong drawn pose lands on the beat, not the last subdivision",
        );
      }
    }
  }
});
