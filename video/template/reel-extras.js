// One cast contract for all providers. Scene motion always uses the shared SpriteDance helper.
(function () {
  "use strict";
  function apply(tl, timing, config, root) {
    var members = config.cast || [];
    if (members.length) {
      if (!window.SpriteDance || !window.SpriteDance.dance) throw new Error("SpriteDance is missing; update the package before rendering a cast.");
      var stage = root.querySelector("#cast");
      members.forEach(function (member, i) {
        var entry = window.SPRITES.sprites[member.name];
        var sheet = entry;
        var actor = document.createElement("div");
        actor.id = "actor-" + i;
        var size = members.length === 1 ? 740 : (members.length === 2 ? 610 : 520);
        var left = members.length === 1 ? 170 : (members.length === 2 ? 10 + i * 450 : -10 + i * 290);
        actor.style.cssText = "position:absolute;top:" + (740 - size) + "px;left:" + left + "px;width:" + size + "px;height:" + size + "px;background-repeat:no-repeat;transform-origin:50% 94%";
        actor.style.backgroundImage = "url('assets/cast/" + entry.file + "')";
        actor.style.backgroundSize = window.SpriteDance.backgroundSize(sheet);
        stage.appendChild(actor);
        window.SpriteDance.dance(tl, timing, {
          target: actor, from: 0, to: timing.duration, sheet: sheet, poses: sheet.frames.length,
          perBeat: member.perBeat || 4, phase: member.phase == null ? [0, 8, 4][i] : member.phase,
          bounce: { px: 12, squash: .035, downbeat: 1.5 }
        });
      });
    }
    if (config.syncCheck) {
      if (!window.SyncCheck || !window.SyncCheck.overlay) throw new Error("SyncCheck is missing; update the package before using the overlay.");
      window.SyncCheck.overlay(tl, timing, { parent: root });
    }
  }
  window.ReelExtras = { apply: apply };
})();
