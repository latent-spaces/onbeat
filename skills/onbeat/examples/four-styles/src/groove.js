// Recovered animation clock: direct quarter-beat body drawings, no synthetic hop or eased pose lag.
(function (root) {
  "use strict";
  // The strongest silhouettes are drawn in cells 3, 7, 11 and 15. Put those ON the beats;
  // the other drawings recover between hits. Portraits use a separate half-beat clock.
  var patterns = {
    moth: [3, 0, 1, 2, 7, 4, 5, 6, 11, 8, 9, 10, 15, 12, 13, 14],
    beet: [3, 0, 1, 1, 7, 4, 5, 5, 11, 8, 9, 9, 15, 12, 14, 14],
    clay: [3, 0, 1, 1, 7, 4, 5, 5, 11, 8, 9, 9, 15, 12, 13, 13],
    anime: [3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8, 15, 14, 13, 12],
  };
  function schedule(T, style, from, to) {
    var SD = root.SpriteDance;
    return SD.steps(T, from, to, 4).map(function (s) {
      var beat = SD.beatInBar(T, s.beat),
        k = beat * 4 + s.sub;
      return { time: s.t, pose: patterns[style][k], beat: s.beat, sub: s.sub };
    });
  }
  function dance(tl, T, name, from, to) {
    var SD = root.SpriteDance,
      B = root.BeatSync;
    tl.set(
      "#" + name + "-groove",
      { x: 0, y: 0, rotation: 0, scaleX: 1, scaleY: 1 },
      B.at(from, T.fps),
    );
    schedule(T, name, from, to).forEach(function (pose) {
      tl.set(
        "#" + name,
        { backgroundPosition: SD.cellPosition(pose.pose, 4, 4) },
        B.at(pose.time, T.fps),
      );
    });
  }
  root.Groove = { schedule: schedule, dance: dance };
})(typeof window !== "undefined" ? window : globalThis);
