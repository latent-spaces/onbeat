// Sync-check overlay: beat ticks, bar numbers and sung-word marks on a scrolling ruler, with a
// fixed playhead, a beat flash and the current word. Use it in preview to see whether visuals
// land on the measured beats and words; leave it off for the final render.
// Classic script: defines window.SyncCheck. Like BeatSync, everything goes on the one paused
// GSAP timeline, so every frame is a pure function of time.
(function (root) {
  "use strict";

  var EPS = 1e-4;
  function at(t, fps) {
    fps = fps || 30;
    return Math.max(0, Math.ceil(t * fps - 1e-6) / fps - EPS);
  }

  function el(tag, css, parent, text) {
    var n = document.createElement(tag);
    n.style.cssText = css;
    if (text != null) n.textContent = text;
    parent.appendChild(n);
    return n;
  }

  // On when the page URL has ?synccheck, or the page config (window.REEL or window.REEL_CONFIG) has syncCheck: true.
  function wanted() {
    var cfg = root.REEL || root.REEL_CONFIG || {};
    var q = (root.location && root.location.search) || "";
    return cfg.syncCheck === true || /[?&]synccheck\b/.test(q);
  }

  // overlay(tl, timing, o)
  //   o.parent      element to draw into (the composition root)
  //   o.width       frame width in px (default 1080)
  //   o.top         ruler top in px (default 1560)
  //   o.pxPerSecond ruler scale (default 360: one beat at 125 BPM is about 173 px)
  function overlay(tl, timing, o) {
    var fps = timing.fps || 30;
    var W = o.width || 1080;
    var top = o.top != null ? o.top : 1560;
    var pps = o.pxPerSecond || 360;
    var dur = timing.duration || timing.beats[timing.beats.length - 1] + 2;
    var mono = "font-family:ui-monospace,Menlo,monospace;";

    var box = el(
      "div",
      "position:absolute;left:0;top:" + top + "px;width:" + W + "px;height:300px;z-index:9999;" +
        "background:rgba(0,0,0,0.72);overflow:hidden;pointer-events:none;" + mono,
      o.parent,
    );
    var strip = el("div", "position:absolute;left:0;top:0;height:300px;width:" + Math.ceil(dur * pps + W) + "px;", box);
    // The ruler scrolls past the clipped box on purpose; tell the layout check.
    box.setAttribute("data-layout-allow-overflow", "");
    strip.setAttribute("data-layout-allow-overflow", "");

    var bars = timing.bars || [];
    timing.beats.forEach(function (b) {
      var isBar = bars.some(function (x) { return Math.abs(x - b) < 1e-3; });
      el(
        "div",
        "position:absolute;top:" + (isBar ? 40 : 70) + "px;left:" + (b * pps + W / 2) + "px;width:" +
          (isBar ? 4 : 2) + "px;height:" + (isBar ? 120 : 60) + "px;background:" + (isBar ? "#ffb23f" : "#9aa4ff") + ";",
        strip,
      );
    });
    bars.forEach(function (b, i) {
      el("div", "position:absolute;top:8px;left:" + (b * pps + W / 2 + 8) + "px;color:#ffb23f;font-size:28px;", strip, "bar " + (i + 1));
    });
    (timing.words || []).forEach(function (w) {
      var mark = el(
        "div",
        "position:absolute;top:180px;left:" + (w.start * pps + W / 2) + "px;width:" + Math.max(3, (w.end - w.start) * pps) +
          "px;height:22px;background:#3fd17a;border-left:3px solid #fff;",
        strip,
      );
      mark.setAttribute("data-layout-allow-overflow", "");
      el("div", "position:absolute;top:26px;left:0;color:#d8ffe6;font-size:28px;white-space:nowrap;", mark, w.text);
    });

    // The ruler scrolls linearly with time: the playhead is always at the centre.
    tl.fromTo(strip, { x: 0 }, { x: -dur * pps, duration: dur, ease: "none", immediateRender: true }, 0);
    el("div", "position:absolute;left:" + (W / 2 - 1) + "px;top:0;width:3px;height:300px;background:#ff4d6d;", box);

    // Beat flash (bigger on bar downbeats) and the current word, top right of the frame.
    var flash = el(
      "div",
      "position:absolute;right:40px;top:40px;width:90px;height:90px;border-radius:50%;background:#ffb23f;opacity:0;z-index:9999;",
      o.parent,
    );
    var word = el(
      "div",
      "position:absolute;right:150px;top:62px;color:#fff;font-size:40px;z-index:9999;text-shadow:0 2px 6px #000;" + mono,
      o.parent,
      "",
    );
    timing.beats.forEach(function (b) {
      var isBar = bars.some(function (x) { return Math.abs(x - b) < 1e-3; });
      tl.set(flash, { opacity: 1, scale: isBar ? 1 : 0.55 }, at(b, fps));
      tl.set(flash, { opacity: 0 }, at(b, fps) + 3 / fps);
    });
    (timing.words || []).forEach(function (w) {
      tl.set(word, { textContent: w.text }, at(w.start, fps));
      tl.set(word, { textContent: "" }, at(w.end, fps));
    });
    return box;
  }

  root.SyncCheck = { wanted: wanted, overlay: overlay };
})(typeof window !== "undefined" ? window : globalThis);
