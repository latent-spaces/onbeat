# HyperFrames rules for a reel

[HyperFrames](https://hyperframes.heygen.com) renders an HTML page to video by seeking one paused timeline frame by frame. If the HyperFrames skill is installed, read it too; it is the full reference. These are the rules a reel needs.

## The page

- One root element carries the video's size and length:
  `<div id="root" data-composition-id="onbeat" data-width="1080" data-height="1920" data-duration="<seconds>" data-fps="30">`.
  Set `data-duration` to the song's `duration` from the timing data.
- The root's `data-fps` is the authoritative video frame rate. Before building the timeline, assign it to `T.fps` as the example does. Timing files contain event times in seconds; the envelope sampling rate is separate and given by `envelopes.hop`.
- The song is an `<audio>` inside the root. It needs `class="clip"`, an `id`, `data-start="0"`, `data-duration` and `data-track-index`. Without an `id` it is left out of the mix. MP3, WAV and M4A all work.
- Build one GSAP timeline with `gsap.timeline({ paused: true })`, add every tween to it, then register it last:
  `window.__timelines["onbeat"] = tl` (the key is the root's `data-composition-id`).
- Asset paths are relative with no leading slash: `assets/song.mp3`.

## What breaks a render

- `Date.now()`, timers, `requestAnimationFrame` loops, network fetches, unseeded `Math.random()` and `repeat: -1`. Every frame must depend only on the timeline time.
- Calling `play()`, `pause()` or seeking the audio yourself.
- A CSS `transform` on an element that GSAP also transforms. Let GSAP own the transform, and animate transforms and opacity instead of `left`, `top`, `width` or `height`.
- A timeline shorter than the video. End with `BeatSync.holdTo(tl, T)` so it runs to the song's end.
- Fonts that aren't bundled. Inter and the other bundled families resolve by name; any other font needs an `@font-face` that points at a file in `assets/`.

## Commands

Run these inside the reel's folder (the one with `index.html`). The version is pinned so a render stays the same.

```bash
npx --yes hyperframes@0.9.2 check                          # lint, layout and contrast; fix every error
npx --yes hyperframes@0.9.2 snapshot --at 5                # one still frame, to look before rendering
npx --yes hyperframes@0.9.2 preview                        # live preview in the browser; add ?synccheck to the URL
npx --yes hyperframes@0.9.2 render --output out/reel.mp4   # the MP4
```

The first run downloads HyperFrames and a headless browser once. It needs Node 22 or newer and ffmpeg.
