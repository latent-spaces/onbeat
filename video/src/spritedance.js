// Beat-synced sprite motion (runbook section 6, docs/beat-motion.md).
// Classic script: defines window.SpriteDance (and module.exports under Node, for tests).
// Steps a sprite sheet through dance poses on the measured beat grid, adds a hop and squash on
// every kick, a bigger accent on bar downbeats, per-character phase offsets, and holds a pose
// through sections without a kick. Everything is placed on the one paused GSAP timeline, so
// every frame is a pure function of timeline time (HyperFrames rules).
(function (root) {
  "use strict";

  // Same time -> frame rule as BeatSync.at: an event at t shows first on frame ceil(t * fps).
  var EPS = 1e-4;
  function at(t, fps) {
    fps = fps || 30;
    return Math.max(0, Math.ceil(t * fps - 1e-6) / fps - EPS);
  }

  function beatPeriodAt(timing, i) {
    var b = timing.beats;
    if (i + 1 < b.length) return b[i + 1] - b[i];
    return timing.beatPeriod;
  }

  // Index of the last beat at or before t (-1 before the first beat).
  function beatIndexAt(timing, t) {
    var b = timing.beats;
    var lo = 0;
    var hi = b.length - 1;
    if (!b.length || t < b[0] - 1e-6) return -1;
    while (lo < hi) {
      var mid = (lo + hi + 1) >> 1;
      if (b[mid] <= t + 1e-6) lo = mid;
      else hi = mid - 1;
    }
    return lo;
  }

  // Position of a beat inside its bar (0 = downbeat), from the measured bar starts.
  function beatInBar(timing, i) {
    var t = timing.beats[i];
    var bars = timing.bars;
    var per = timing.beatsPerBar || 4;
    var barStart = -1;
    for (var k = 0; k < bars.length; k++) {
      if (bars[k] <= t + 1e-6) barStart = k;
      else break;
    }
    if (barStart < 0) return ((i % per) + per) % per;
    var first = beatIndexAt(timing, bars[barStart]);
    return (((i - first) % per) + per) % per;
  }

  // True when t falls in a section the beat tracker marked as having no kick.
  function silentAt(timing, t) {
    var s = timing.sections || [];
    for (var k = 0; k < s.length; k++) {
      if (t >= s[k].start - 1e-6 && t < s[k].end - 1e-6) return s[k].kick === false;
    }
    return false;
  }

  // Sub-beat step times in [from, to): each measured beat split into `perBeat` equal steps,
  // so the steps follow tempo drift instead of a fixed clock.
  function steps(timing, from, to, perBeat) {
    var out = [];
    var n = perBeat || 4;
    var b = timing.beats;
    var start = Math.max(0, beatIndexAt(timing, from));
    for (var i = start; i < b.length; i++) {
      var p = beatPeriodAt(timing, i) / n;
      for (var k = 0; k < n; k++) {
        var t = b[i] + k * p;
        if (t >= to - 1e-6) return out;
        if (t >= from - 1e-6) out.push({ t: t, beat: i, sub: k });
      }
    }
    return out;
  }

  // The pose shown at step (beat i, sub-step k). Poses are counted from the bar's downbeat,
  // so a 16-pose sheet at perBeat 4 fills exactly one 4-beat bar and pose 0 lands on beat 1.
  function poseFor(timing, beat, sub, o) {
    var perBeat = o.perBeat || 4;
    var count = o.frames ? o.frames.length : o.poses;
    var k = (beatInBar(timing, beat) * perBeat + sub + (o.phase || 0)) % count;
    return o.frames ? o.frames[k] : k;
  }

  // Pure query: which pose is on screen at time t for these options (null outside [from, to)).
  function poseAt(timing, t, o) {
    if (t < o.from - 1e-6 || t >= o.to - 1e-6) return null;
    var i = beatIndexAt(timing, t);
    if (i < 0) return o.holdPose || 0;
    if (o.hold !== "none" && silentAt(timing, t)) return o.holdPose || 0;
    var perBeat = o.perBeat || 4;
    var sub = Math.min(perBeat - 1, Math.floor(((t - timing.beats[i]) / beatPeriodAt(timing, i)) * perBeat + 1e-6));
    return poseFor(timing, i, sub, o);
  }

  // background-position for cell i of a cols x rows sheet drawn with
  // background-size: cols*100% rows*100%.
  function cellPosition(i, cols, rows) {
    var c = cols || 4;
    var r = rows || c;
    var x = c > 1 ? ((i % c) * 100) / (c - 1) : 0;
    var y = r > 1 ? (Math.floor(i / c) * 100) / (r - 1) : 0;
    return x + "% " + y + "%";
  }

  // background-position for frame i of a sprites.json sheet entry (frame rects in pixels).
  function rectPosition(sheet, i) {
    var f = sheet.frames[i];
    var dx = sheet.width - f.width;
    var dy = sheet.height - f.height;
    return (dx > 0 ? (f.x / dx) * 100 : 0) + "% " + (dy > 0 ? (f.y / dy) * 100 : 0) + "%";
  }

  // dance(tl, timing, o): pose stepping plus kick bounce for one character.
  //   o.target    element or selector showing the sheet as its background
  //   o.from/o.to time range in seconds
  //   o.cols/rows grid (default 4 x 4); or o.sheet, a sprites.json sheet entry with frame rects
  //   o.poses     poses in the cycle (default cols*rows, or sheet.frames.length)
  //   o.frames    explicit pose list instead of 0..poses-1, e.g. [0, 1, 2, 1]
  //   o.perBeat   pose steps per beat (default 4: one every quarter beat)
  //   o.phase     offset in steps, so a cast doesn't move in lockstep (e.g. 0, 8, 4)
  //   o.hold      "silence" (default): hold o.holdPose through kick-less sections; "none": keep dancing
  //   o.bounce    false, or { target, px, squash, downbeat }: hop and squash on every beat,
  //               multiplied by `downbeat` on bar downbeats (defaults 14 px, 0.06, 1.8)
  function dance(tl, timing, o) {
    var fps = timing.fps || 30;
    var cols = o.cols || 4;
    var rows = o.rows || cols;
    var poses = o.poses || (o.sheet ? o.sheet.frames.length : cols * rows);
    var opts = { perBeat: o.perBeat || 4, phase: o.phase || 0, poses: poses, frames: o.frames };
    var pos = o.sheet
      ? function (i) { return rectPosition(o.sheet, i); }
      : function (i) { return cellPosition(i, cols, rows); };
    var hold = o.hold || "silence";
    var holdPose = o.holdPose || 0;
    var last = null;
    var n = 0;
    steps(timing, o.from, o.to, opts.perBeat).forEach(function (s) {
      var pose = hold !== "none" && silentAt(timing, s.t) ? holdPose : poseFor(timing, s.beat, s.sub, opts);
      if (pose === last) return;
      tl.set(o.target, { backgroundPosition: pos(pose) }, at(s.t, fps));
      last = pose;
      n++;
    });
    if (last === null) tl.set(o.target, { backgroundPosition: pos(holdPose) }, at(o.from, fps));

    if (o.bounce !== false) {
      var b = o.bounce || {};
      var target = b.target || o.target;
      var px = b.px != null ? b.px : 14;
      var squash = b.squash != null ? b.squash : 0.06;
      var accent = b.downbeat != null ? b.downbeat : 1.8;
      tl.set(target, { transformOrigin: "50% 100%" }, at(o.from, fps));
      timing.beats.forEach(function (t, i) {
        if (t < o.from - 1e-6 || t >= o.to - 1e-6) return;
        if (hold !== "none" && silentAt(timing, t)) return;
        var m = beatInBar(timing, i) === 0 ? accent : 1;
        var half = beatPeriodAt(timing, i) / 2;
        var t0 = at(t, fps);
        // Land squashed on the kick, spring up to the top at mid-beat, fall back by the next beat.
        tl.fromTo(
          target,
          { y: 0, scaleY: 1 - squash * m, scaleX: 1 + squash * m * 0.6 },
          { y: -px * m, scaleY: 1, scaleX: 1, duration: half, ease: "power2.out", immediateRender: false },
          t0,
        );
        tl.to(target, { y: 0, duration: half, ease: "power2.in" }, t0 + half);
      });
    }
    return n;
  }

  // cast(tl, timing, members, shared): dance several characters with shared options; each
  // member may override (typically target and phase). Default phases spread the cast: 0, 8, 4, 12.
  function cast(tl, timing, members, shared) {
    var spread = [0, 8, 4, 12, 2, 10, 6, 14];
    return members.map(function (m, k) {
      var o = {};
      var key;
      for (key in shared) o[key] = shared[key];
      for (key in m) o[key] = m[key];
      if (m.phase == null) o.phase = spread[k % spread.length];
      return dance(tl, timing, o);
    });
  }

  var api = {
    at: at,
    steps: steps,
    poseAt: poseAt,
    beatIndexAt: beatIndexAt,
    beatInBar: beatInBar,
    silentAt: silentAt,
    cellPosition: cellPosition,
    rectPosition: rectPosition,
    dance: dance,
    cast: cast,
  };
  root.SpriteDance = api;
  if (typeof module !== "undefined" && module.exports) module.exports = api;
})(typeof window !== "undefined" ? window : globalThis);
