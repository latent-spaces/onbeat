# Original cast revision — review

The person approved the new cast, asked for a more mechanical robot, and explicitly
asked to preserve the old movements. The robot now has exposed joints, segmented
metal limbs and a vented teal chassis, with an orange painted-metal head.

All three dance sheets were generated with the original 4×4 sheets as pose/layout
references and the approved cast study as the identity reference. Separate 3×3
portraits preserve the original head-angle/expression sequence. The original
orbital timeline and layout are unchanged except for robot portrait image paths;
all three old robot close-up cuts now use the same original robot identity.
The karaoke timing and styling preserve the old 11.5192-second chorus
prototype. Packaging substitutes the redistributable Arimo italic font, supplied
with its SIL Open Font License, for the local Arial font used in the approved video. The package encodes the same source chorus as MP3 without shifting its
start, and includes canonical timing JSON/JS for the shared helpers. The approved
WAV-audio render is included as preview.mp4. Body frames step every quarter beat; portraits
step every half beat. No synthetic body bounce or interpolation was added.

Packing uses one shared 0.88 scale for every dance cell, with the same 94% foot
anchor as before, to leave clear margins. It does not resize individual poses.
Generated source files are preserved in assets/source; prompts are in work/.

Validation: all six atlas alpha/clipping/drift checks pass. HyperFrames check has
no runtime, layout, contrast, audio or craft errors; 20/20 contrast checks pass.
Two inherited timeline-density advisories remain intentionally: short close-up
cuts and lyric groups share tracks so this small scene remains easy to compare
against its original. No retiming or track refactor was necessary.

Inspected nine assembled snapshots: two ensemble frames, each human close-up,
robot solo, three robot portraits and the ending ensemble. Cutouts are clean,
close-up faces fill the frame, and text remains above the action. Atlas review
on light/dark backgrounds confirms transparency. The sprite model preserved the
pose sequence closely, but generated contours/proportions are not pixel-identical
tracings; movement preservation means the same choreography and timing, not a
pixel-identical replacement. Exact timeline equality is recorded separately in
MOVEMENT-PRESERVATION.json.

Weakest shot: the original ensemble staging overlaps the robot and woman. Kept to
honor the request for the same example/movements. This is the approved 11.5-second packaged example; the recovered full-song film is a separate project and has not been replaced.
Audio timing is preserved and the encoded stream is probed; sound-on artistic
review belongs to the person.
