// Optional layers for the template, driven by reel.json. Classic script: defines window.ReelExtras.
// Each one runs only when its helper from video/src/ is loaded and reel.json asks for it,
// so the template renders from beats alone.
(function () {
  "use strict";

  // reel.json "cast": [{ "sprite": "robot", "x": 160, "size": 760 }, ...]
  // "sprite" names an entry in songs/<name>/sprites/sprites.json (docs/sprites.md); the sheet image
  // is copied to assets/cast/. Dancers step 16 poses per bar with phases 0, 8, 4, 12 (docs/beat-motion.md).
  function addCast(tl, T, C, root) {
    var sheets = (window.SPRITES && window.SPRITES.sprites) || {};
    var stage = root.querySelector("#cast");
    var members = [];
    C.cast.forEach(function (m, i) {
      var sheet = sheets[m.sprite];
      if (!sheet) return;
      var size = m.size || 760;
      var wrap = document.createElement("div");
      wrap.style.cssText = "position:absolute;top:" + (m.y != null ? m.y : 0) + "px;left:" +
        (m.x != null ? m.x : 160 + (i - (C.cast.length - 1) / 2) * 300) + "px;width:" + size + "px;height:" + size + "px";
      var el = document.createElement("div");
      el.id = "cast-" + i;
      el.style.cssText = "position:absolute;inset:0;background-repeat:no-repeat;background-image:url('assets/cast/" +
        sheet.file + "');background-size:" + window.SpriteDance.backgroundSize(sheet);
      wrap.appendChild(el);
      stage.appendChild(wrap);
      members.push({ target: el, sheet: sheet, bounce: { target: wrap, px: 16, squash: 0.05, downbeat: 1.8 } });
    });
    if (!members.length) return;
    var firstKick = (T.sections || []).filter(function (s) { return s.kick; })[0];
    window.SpriteDance.cast(tl, T, members, { from: firstKick ? firstKick.start : 0, to: T.duration });
  }

  function apply(tl, T, C, root) {
    window.REEL_CONFIG = C;
    if (C.cast && C.cast.length && window.SpriteDance) addCast(tl, T, C, root);
    if (window.SyncCheck && window.SyncCheck.wanted()) window.SyncCheck.overlay(tl, T, { parent: root });
  }
  window.ReelExtras = { apply: apply };
})();
