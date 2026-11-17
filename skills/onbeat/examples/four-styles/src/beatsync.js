// Beat-sync timeline builder and animation pieces (playbook sections 3, 6, 7).
// Classic script: defines window.BeatSync. Every piece is (tl, timing, opts) and only adds
// tweens/sets to the one paused GSAP timeline, so the render is a pure function of time.
(function () {
  "use strict";

  // Time -> frame rule: an event at time t shows first on frame ceil(t * fps).
  // The renderer seeks frame f to time f / fps, so we place the event a hair (0.1 ms) before
  // that frame's time: frame f sees it, frame f - 1 (1/fps earlier) never does, whatever the
  // float rounding of t * fps.
  var EPS = 1e-4;
  function frameOf(t, fps) {
    return Math.ceil(t * fps - 1e-6);
  }
  function at(t, fps) {
    return Math.max(0, frameOf(t, fps) / fps - EPS);
  }

  function el(tag, cls, parent, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    parent.appendChild(n);
    return n;
  }

  function beatsIn(timing, from, to) {
    return timing.beats.filter(function (b) {
      return b >= from - 1e-6 && b < to - 1e-6;
    });
  }

  function lineWords(timing, line) {
    return timing.words.filter(function (w) {
      return w.line === line;
    });
  }

  // BeatStepper: one target lit per step, stepping every `every` beats in [from, to); instant.
  // targets: elements cycled in order; on/off: GSAP props for the lit / unlit state.
  function BeatStepper(tl, timing, o) {
    var every = o.every || 1;
    var steps = beatsIn(timing, o.from, o.to).filter(function (_, i) {
      return i % every === 0;
    });
    var n = o.targets.length;
    steps.forEach(function (b, i) {
      if (i > 0) tl.set(o.targets[(i - 1) % n], o.off, at(b, timing.fps));
      tl.set(o.targets[i % n], o.on, at(b, timing.fps));
    });
    if (steps.length) tl.set(o.targets[(steps.length - 1) % n], o.off, at(o.to, timing.fps));
    return steps.length;
  }

  // BeatTicker: a text element whose content is a function of the beat index; instant.
  function BeatTicker(tl, timing, o) {
    var bs = beatsIn(timing, o.from, o.to);
    bs.forEach(function (b) {
      var i = timing.beats.indexOf(b);
      tl.set(o.target, { textContent: o.text(i, timing) }, at(b, timing.fps));
    });
    return bs.length;
  }

  // BeatPulse: instant on at each beat, exponential decay inside the beat.
  function BeatPulse(tl, timing, o) {
    var bs = beatsIn(timing, o.from, o.to);
    var decay = timing.beatPeriod * (o.decay || 0.85);
    bs.forEach(function (b) {
      tl.fromTo(
        o.target,
        { opacity: o.peak || 1, scale: o.scaleFrom || 1 },
        { opacity: 0, scale: 1, duration: decay, ease: "expo.out", immediateRender: false },
        at(b, timing.fps),
      );
    });
    return bs.length;
  }

  // DropLine: a whole lyric line drops in from above on its first word, ~6-frame ease-out.
  function DropLine(tl, timing, o) {
    var line = timing.lines[o.line];
    var node = el("div", "lyric", o.parent, line.text);
    node.style.top = o.y + "px";
    // Opacity snaps on the word's frame (so it is visible there); only the drop is eased.
    tl.set(node, { opacity: 1 }, at(line.start, timing.fps));
    tl.fromTo(
      node,
      { y: -(o.dropPx || 80) },
      { y: 0, duration: 6 / timing.fps, ease: "power3.out", immediateRender: false },
      at(line.start, timing.fps),
    );
    if (o.until != null) tl.set(node, { opacity: 0 }, at(o.until, timing.fps));
    return node;
  }

  // SyllableStack: each word of a line (a syllable) pops in on its own line, 2-frame pop.
  function SyllableStack(tl, timing, o) {
    var pitch = o.pitch || 130;
    return lineWords(timing, o.line).map(function (w, i) {
      var node = el("div", "lyric " + (o.cls || ""), o.parent, w.text);
      node.style.top = o.y + i * pitch + "px";
      tl.fromTo(
        node,
        { opacity: 1, scale: 1.12 },
        { opacity: 1, scale: 1, duration: 2 / timing.fps, ease: "none", immediateRender: false },
        at(w.start, timing.fps),
      );
      if (o.until != null) tl.set(node, { opacity: 0 }, at(o.until, timing.fps));
      return node;
    });
  }

  // KaraokeLine: line appears on its first word; each word goes unsung -> current -> sung.
  function KaraokeLine(tl, timing, o) {
    var line = timing.lines[o.line];
    var node = el("div", "lyric", o.parent);
    node.style.top = o.y + "px";
    lineWords(timing, o.line).forEach(function (w, i) {
      if (i > 0) node.appendChild(document.createTextNode(" "));
      var s = el("span", "", node, w.text);
      s.style.color = o.unsung;
      tl.set(s, { color: o.current }, at(w.start, timing.fps));
      tl.set(s, { color: o.sung }, at(w.end, timing.fps));
    });
    tl.set(node, { opacity: 1 }, at(line.start, timing.fps));
    if (o.until != null) tl.set(node, { opacity: 0 }, at(o.until, timing.fps));
    return node;
  }

  // PaletteCut: hard swap of the colour world (CSS custom properties) at a bar.
  function PaletteCut(tl, timing, o) {
    var t = timing.bars[o.bar];
    tl.set(o.target, o.palette, at(t, timing.fps));
    return t;
  }

  // CharacterStates: power-on (off -> on body colour) at the first word; eye swap per beat.
  function CharacterStates(tl, timing, o) {
    var on = o.powerOn != null ? o.powerOn : timing.words[0].start;
    tl.set(o.target, { "--char-body": o.onColor, "--char-eye": o.eyeColor }, at(on, timing.fps));
    var bs = beatsIn(timing, o.eyesFrom, o.eyesTo);
    bs.forEach(function (b, i) {
      var a = i % 2 === 0;
      tl.set(o.eyesA, { opacity: a ? 0 : 1 }, at(b, timing.fps));
      tl.set(o.eyesB, { opacity: a ? 1 : 0 }, at(b, timing.fps));
    });
    return bs.length;
  }

  // ProgressRiser: a fill that rises linearly and completes exactly on the frame of `to`.
  function ProgressRiser(tl, timing, o) {
    var t0 = at(o.from, timing.fps);
    var t1 = at(o.to, timing.fps);
    tl.fromTo(o.target, { scaleX: 0 }, { scaleX: 1, duration: t1 - t0, ease: "none", immediateRender: false }, t0);
    if (o.hideAt != null) tl.set(o.hideTarget || o.target, { opacity: 0 }, at(o.hideAt, timing.fps));
  }

  // Our pixel character "Blip": a tall capsule with an antenna and a cable tail, no legs
  // (12 x 15 px grid). Body uses --char-body, eyes --char-eye. Returns the two eye groups
  // (A: open squares, B: closed lines).
  var BODY = [
    ".....##.....",
    "......#.....",
    "...######...",
    "..########..",
    "..########..",
    "..########..",
    "..########..",
    "..########..",
    "..########..",
    "..########..",
    "..########..",
    "...######...",
    "......#.....",
    "......##....",
    ".......####.",
  ];
  var EYES_A = [[3, 5], [4, 5], [3, 6], [4, 6], [7, 5], [8, 5], [7, 6], [8, 6]];
  var EYES_B = [[3, 6], [4, 6], [7, 6], [8, 6]];
  var MOUTH = [[5, 9], [6, 9]];
  function drawCharacter(svg, px) {
    var ns = "http://www.w3.org/2000/svg";
    svg.setAttribute("viewBox", "0 0 12 15");
    svg.setAttribute("width", 12 * px);
    svg.setAttribute("height", 15 * px);
    svg.setAttribute("shape-rendering", "crispEdges");
    function rect(g, x, y, fill) {
      var r = document.createElementNS(ns, "rect");
      r.setAttribute("x", x);
      r.setAttribute("y", y);
      r.setAttribute("width", 1);
      r.setAttribute("height", 1);
      r.setAttribute("fill", fill);
      g.appendChild(r);
    }
    function group() {
      var g = document.createElementNS(ns, "g");
      svg.appendChild(g);
      return g;
    }
    var body = group();
    BODY.forEach(function (row, y) {
      row.split("").forEach(function (c, x) {
        if (c === "#") rect(body, x, y, "var(--char-body)");
      });
    });
    var a = group();
    var b = group();
    EYES_A.forEach(function (p) { rect(a, p[0], p[1], "var(--char-eye)"); });
    EYES_B.forEach(function (p) { rect(b, p[0], p[1], "var(--char-eye)"); });
    MOUTH.forEach(function (p) { rect(body, p[0], p[1], "var(--char-eye)"); });
    b.style.opacity = 0;
    return { eyesA: a, eyesB: b };
  }

  // Hold the timeline open to the song's end so its length equals the timing data's.
  function holdTo(tl, timing) {
    tl.set({}, {}, timing.duration);
  }

  window.BeatSync = {
    at: at,
    frameOf: frameOf,
    el: el,
    BeatStepper: BeatStepper,
    BeatTicker: BeatTicker,
    BeatPulse: BeatPulse,
    DropLine: DropLine,
    SyllableStack: SyllableStack,
    KaraokeLine: KaraokeLine,
    PaletteCut: PaletteCut,
    CharacterStates: CharacterStates,
    ProgressRiser: ProgressRiser,
    holdTo: holdTo,
    drawCharacter: drawCharacter,
  };
})();
