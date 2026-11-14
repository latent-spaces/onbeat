// Optional layers for the template, driven by reel.json. Classic script: defines window.ReelExtras.
// Each helper is used only if its script from video/src/ is loaded and reel.json asks for it,
// so the template renders with beats alone.
(function () {
  "use strict";
  function apply(tl, T, C, root) {
    // Sprite cast: reel.json "cast": [{ "sprites": "assets/cast/sprites.json", "name": "robot", ... }]
    if (C.cast && C.cast.length && window.SpriteDance && window.SPRITES) {
      var stage = root.querySelector("#cast");
      C.cast.forEach(function (member, i) {
        window.SpriteDance(tl, T, Object.assign({ parent: stage, index: i, sheets: window.SPRITES }, member));
      });
    }
    // Sync-check overlay: reel.json "syncCheck": true (preview only; turn off for the final render).
    if (C.syncCheck && window.SyncCheck) window.SyncCheck(tl, T, { parent: root });
  }
  window.ReelExtras = { apply: apply };
})();
