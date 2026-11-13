# Visual review

Reviewed opening dance frames at 0.3 and 1.0 s, human close-ups at 4.1 and
5.1 s, robot solo at 6.4 s, helmet close-ups at 8.3 and 9.0 s, and ending at
10.1 s. The first review showed outer-arm cropping in the ensemble; the final
layout reduces sprite size and keeps the full figures visible.

The room, starfield and planet are independently composited. Window-center alpha
is zero in `ship.png`; the planet has a real alpha cutout. All five character
close-up sheets and three dance atlases preserve alpha transparency. Frame
selection follows sixteenth-note subdivisions and explicitly timed GSAP sets.

`npm run check` passes: zero lint errors, zero runtime errors, zero layout
warnings, zero motion warnings, zero audio warnings. One advisory remains:
five short close-up clips share a timeline track. They are intentionally kept
in one scene for this small test. PNG snapshots are in `out/review/` and the
corrected ensemble snapshots in `out/review-final/`.

The result is limited sprite animation with generated pose variation and some
line/shape drift between frames. It establishes the cel-art direction, beat
timing, close-up scale and separate scene layers. A longer final reel would
benefit from corrected in-betweens and a deliberately choreographed dance.

## Karaoke update

Added a separate captions sub-composition using the existing aligned word
timestamps, offset by 27.2768 seconds. Cream bold italic letters, dark outlines,
cyan shadows and a pink left-to-right word wipe give the karaoke treatment.
Two-line captions sit above the characters at y=235, leaving the full-body
dancing and close-up faces unobstructed. The source cut begins during the first
word and ends during the repeated next line; highlights account for those cuts.

Reviewed frames at 0.4, 1.5, 4.3, 5.5, 8.0, 9.5 and 11.4 seconds. Check passes
with zero runtime/layout/motion/audio issues and 20/20 text contrast checks.
Two organizational advisories remain for the short caption and close-up tracks;
the four lyric groups stay together on one captions track for editing.
Audio timing uses the existing alignment; sound was measured, not listened to.
The first encoded review exposed incorrect interpolation of clip-path strings.
The final version animates a numeric CSS percentage instead; frames at 0.4 and
1.8 seconds confirm partially filled words at the correct points in the lyrics.
