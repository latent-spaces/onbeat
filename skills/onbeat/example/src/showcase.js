// An animation anthology: solo choreography, dedicated face animation, four physical styles.
window.OnBeatShowcase = function (tl, T) {
  "use strict";
  var B = window.BeatSync,
    SD = window.SpriteDance;
  var at = function (t) {
    return B.at(t, T.fps);
  };
  var cast = ["moth", "beet", "clay", "anime"],
    worlds = ["paper", "pixel", "clay", "anime"];
  var bar = function (n) {
    return n < T.bars.length ? T.bars[n] : T.duration;
  };
  var span = function (a, b) {
    return Math.max(0, at(b) - at(a));
  };
  var labels = ["PAPER CUT", "PIXEL FUNK", "CLAY GROOVE", "CITY POP / '88"];
  function world(index, t) {
    worlds.forEach(function (w, i) {
      tl.set(
        ["#" + w + "-back", "#" + w + "-front"],
        { opacity: index === i ? 1 : 0 },
        at(t),
      );
    });
  }
  function wide(index, start, end, medium) {
    tl.set("#portrait", { opacity: 0 }, at(start));
    tl.set("#camera", { x: 0, y: 0, scale: 1 }, at(start));
    cast.forEach(function (name, i) {
      tl.set(
        "#" + name + "-actor",
        { x: 180, y: 690, scale: 1, opacity: i === index ? 1 : 0 },
        at(start),
      );
      tl.set("#" + name + "-travel", { x: 0, y: 0, rotation: 0 }, at(start));
    });
    var scale = medium ? 1.26 : 1.04;
    // Controlled camera drift over a musical phrase, separate from the character's groove.
    tl.fromTo(
      "#camera",
      { scale: scale, x: 540 - 540 * scale + 15, y: 1010 - 1010 * scale },
      {
        scale: scale + 0.035,
        x: 540 - 540 * (scale + 0.035) - 15,
        y: 1010 - 1010 * (scale + 0.035),
        duration: span(start, end),
        ease: "none",
        immediateRender: false,
      },
      at(start),
    );
  }
  function closeup(index, start, end, reverse) {
    var name = cast[index];
    // NEW 3x3 head-and-shoulder artwork. This is never a zoom of a full-body drawing.
    tl.set("#camera", { scale: 1.06, x: -32, y: -30 }, at(start));
    cast.forEach(function (other) {
      tl.set("#" + other + "-actor", { opacity: 0 }, at(start));
    });
    tl.set(
      "#portrait",
      {
        opacity: 1,
        x: 0,
        y: 0,
        rotation: 0,
        backgroundImage: "url('assets/cast/" + name + "-close.webp')",
        backgroundPosition: "0% 0%",
        imageRendering: index === 1 ? "pixelated" : "auto",
      },
      at(start),
    );
    // Recovered half-beat portrait rhythm: expressive head hits on beats, recoveries between.
    // Two phrase variants use all nine new drawings without quarter-beat facial flicker.
    var sequence = reverse
      ? [2, 0, 5, 8, 6, 0, 7, 8]
      : [1, 0, 4, 8, 3, 0, 4, 8];
    SD.steps(T, start, end, 2).forEach(function (step, k) {
      tl.set(
        "#portrait",
        {
          backgroundPosition: SD.cellPosition(
            sequence[k % sequence.length],
            3,
            3,
          ),
        },
        at(step.t),
      );
    });
    tl.set("#portrait", { opacity: 0 }, at(end));
  }
  // Each material gets its own sequence, not an ensemble or a forced character story.
  cast.forEach(function (name, i) {
    var start = bar(i * 4),
      end = i === 3 ? T.duration : bar(i * 4 + 4);
    world(i, start);
    tl.set("#chapter", { textContent: labels[i], opacity: 1 }, at(start));
    tl.set("#chapter", { opacity: 0 }, at(bar(i * 4 + 1)));
    if (i < 3) {
      wide(i, start, bar(i * 4 + 1), false);
      closeup(i, bar(i * 4 + 1), bar(i * 4 + 2), false);
      wide(i, bar(i * 4 + 2), bar(i * 4 + 3), true);
      closeup(i, bar(i * 4 + 3), end, true);
    } else {
      // Anime owns the final six bars: expressive face, a stylish full-body phrase, face finale.
      closeup(i, start, bar(13), false);
      wide(i, bar(13), bar(14), false);
      wide(i, bar(14), bar(16), true);
      closeup(i, bar(16), T.duration, true);
    }
    window.Groove.dance(tl, T, name, start, end);
    // Scenery layers move at different depths across each long phrase, without rhythmic jitter.
    tl.fromTo(
      "#" + worlds[i] + "-back .plate",
      { x: 12, y: 0 },
      {
        x: -12,
        y: -5,
        duration: span(start, end),
        ease: "none",
        immediateRender: false,
      },
      at(start),
    );
    tl.fromTo(
      "#" + worlds[i] + "-front .plate",
      { x: -22, y: 4 },
      {
        x: 22,
        y: -4,
        duration: span(start, end),
        ease: "none",
        immediateRender: false,
      },
      at(start),
    );
  });
  T.lines.forEach(function (line, i) {
    B.KaraokeLine(tl, T, {
      line: i,
      parent: document.getElementById("lyrics"),
      y: 0,
      until: i + 1 < T.lines.length ? T.lines[i + 1].start : T.duration,
      unsung: "#fff3d4",
      current: "#ffbd64",
      sung: "#fff3d4",
    });
  });
  if (window.SyncCheck.wanted())
    window.SyncCheck.overlay(tl, T, {
      parent: document.getElementById("root"),
    });
};
