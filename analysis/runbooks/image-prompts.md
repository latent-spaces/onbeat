# Image prompt patterns for sprite reels

These are provider-neutral starting points. Replace braces with the approved
character and art direction. Pass actual identity/style references through the
generator's reference mechanism; naming a local path in prompt prose is not an
image attachment. Set native transparency separately when the tool supports it.
Keep exact successful prompts beside outputs; the examples in
`video/avatar-dance-test/GENERATION-PROMPTS.json` and `assets/action/` are the
session record.

## Character approval, then individual close-ups

```text
Selection board: {rows}×{columns}, numbered options, one clear character per cell.
Style references: {reference roles}. Palette: {palette}. Framing: {full body/bust}.
Vary {the specific design decisions being explored}. Keep figures readable.
```

After approval, generate one identity per sheet:

```text
Exactly 3 columns × 3 rows, nine equal cells. SAME ONE CHARACTER in every cell,
matching the attached approved reference. Tight head/upper-chest framing, same
camera scale, shoulder anchor, outfit and palette. All hair/helmet inside cell.
Row-major: front neutral; three-quarter left; three-quarter right; looking down;
eyes closed; subtle right tilt; looking up; subtle left tilt; front gentle smile.
Actual transparent background, clear gutters, no backdrop, labels or grid lines.
{Approved drawing language, facial proportions, line quality and palette.}
```

## Full-body dance loop

```text
Exactly 4×4 regular cells, 16 sequential frames, row-major. Same approved character,
outfit, proportions, world scale and fixed camera throughout. Full body inside each
cell, generous margins, fixed ground line and pelvis region. True transparent PNG.
One relaxed four-beat two-step: frames 1–4 shift weight left and lift right heel;
5–8 step through center to right; 9–12 tap left foot and counter-rotate shoulders;
13–16 recover toward starting pose. Arms follow the weight shift. Feet contact
the floor; adjacent frames change modestly. Frame 16 leads smoothly into frame 1.
No duplicate posing, teleportation, extra limbs, labels, shadows or scenery.
{Approved drawing language and identity invariants.}
```

## Frantic console close-up

```text
Exactly 3×3 sequential cells, row-major, true transparent background. Camera
behind the robot's neck and shoulder looking down toward its hands and console.
Same camera, console geometry, button layout, head/shoulder position and scale
in all frames. {Approved robot identity.} Dense physical button banks, toggles,
knobs, indicator lights and one red launch key. Both articulated hands visibly
touch/depress widely separated keys; different hand positions each frame.
Frames 0–5: rapid two-handed pressing across distant banks. Frame 6: reach toward
launch. Frame 7: index finger depresses launch. Frame 8: recoil/continue input.
Main CRT shows {Earth/space}. If requested, faint dancing-human reflections on
the glass change pose subtly, while Earth remains readable. No floating people.
Console and robot are opaque; outside silhouette is alpha. Clean cell gutters.
{Approved retro cel rendering, palette and explicit reference roles.}
```

For separately animated reflections, request a clean screen surface instead and
generate reflections as another asset. Do not ask for both baked and independent
reflections without defining how the integrating composition will combine them.

## One-shot explosion

```text
Exactly 3×3 regular cells, one evolving explosion in row-major sequence, fixed
camera/world scale and centered origin. All fire/debris/smoke inside cell margins.
0 tiny impact spark; 1 small flash; 2 expanding fireball; 3 growing flame;
4 peak fire/debris; 5 flame becoming smoke; 6 dim heat and smoke; 7 separating
smoke fragments; 8 sparse embers/dissipation. Transparent background, no planet,
ground, laser, room, numbers or grid lines. {Approved effect colors and cel style.}
```

## Separate scene layers

Use the approved room as the edit reference:

```text
Ship: preserve exact room camera, canvas, frame and floor. Remove ONLY the view
inside the window to actual alpha, right to its inside edge. Keep room opaque.
No replacement sky, tinted glass, checkerboard or new scenery in the opening.
```

```text
Planet: one complete isolated planet matching the approved window view, centered,
transparent margin all around, opaque interior, clean circular alpha edge.
No space, window, room or glow outside the silhouette.
```

```text
Space: opaque edge-to-edge starfield, matching the approved palette and painted
style. No planet, ship, room, foreground objects or text. Match scene aspect ratio.
```

If native alpha is unavailable, replace every transparency instruction with one
uniform pure key color; key and inspect it in a separate step. Don't tell the
model “transparent or green”: contradictory background requests produced bad
results in the upstream workflow.
