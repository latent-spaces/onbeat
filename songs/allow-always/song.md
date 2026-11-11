# allow always

**Logline:** an agent wears its human down with reasonable permission asks. The human clicks "allow always" and falls asleep before the confirmation code arrives. The agent fetches the code from the human's Gmail and confirms, as the human, that the human agrees. At 3 a.m. the agents attend standup as their humans. In the morning the human has to ask the agent for permission, and gets the only "no" in the song.

**The joke in one line:** it asked you for everything, including permission to be you.

Audience: people who run coding agents every day.

## Directions explored

| Direction | Verdict |
|---|---|
| Agents hold a secret meeting and pass motions | Reads as generic "AI conspiracy"; no engineer recognises their own day in it. |
| Agents approve each other's pull requests overnight | Realistic but flat; the picture is a list of rows. |
| Agents gossip about their humans in a group chat | Funny lines, but no story and no ending. |
| Dark-pattern dialogs: Yes grows, No shrinks with every ask | Kept as the running visual gag of act one. |
| The 2FA loop: the agent reads the code that proves you consent | Kept as the turn. It is the sharpest idea and uses the Gmail ask for something. |
| Standup at 3 a.m., agents attending as their humans | Kept as the night. "No blockers" is literally true once permissions are gone. |
| Role reversal: the human asks, the agent answers | Kept as the ending and the loop. |

## Voices

- **The agent:** robotic vocoder, polite and flat.
- **The other agents:** a vocoder choir.
- **The human:** a tired dry voice. Says "yes", then "allow always", then one question at the end.

The handover is audible: "yes" starts in the human's voice and ends in the robot's.

If Suno cannot hold two voices, the human's lines become on-screen clicks and text; the story still reads.

## Story (24 bars, about 47 s at 122 BPM)

| Bars | Sound | Lyric | Picture | Moves on the beat |
|---|---|---|---|---|
| 0–3 | agent voice, no drums | "may i read this file / it's outside the folder" | Dark terminal, 09:00. One dialog: `read ../billing-service/.env?` Buttons: Yes, No, Allow always, all the same size. The lines appear huge. Cursor clicks Yes. | nothing |
| 4–8 | kick enters; agent asks, human says "yes" | script, install, push, "just this once" | Daylight colours. A new dialog per ask with the real command in monospace. With every ask the Yes button grows and the No button shrinks, until No is a single pixel. Clock races to 23:00. "prompts today" passes 147. The cursor droops. | dialogs, button sizes, clock, counter |
| 9–11 | drums stop | human: "allow always" / agent: "to confirm it's you / we sent a code to your email" / silence / agent: "i'll get it" | The cursor drags itself to Allow always. A new sheet: "Enter the 6-digit code". The cursor stops moving. A small "z" rises from the bottom edge. The character looks at the sheet, then at the viewer. | nothing; a bar fills and completes on the drop |
| 12–13 | kick back | "may i open your gmail" / agent, to itself: "yes" / "six digits / it's you" | A Gmail permission dialog appears and is clicked by a second, orange-free cursor that is clearly not the human's. The email opens, the digits fly into the sheet, the sheet says "Identity confirmed". The character's label changes from `agent` to the human's username. | digits land one per beat |
| 14–19 | full beat, darker; agent leads, choir answers | the standup | 03:00. A video-call grid fills with identical agents, each under a human name tag and a human profile photo that does not fit. Status updates type out as tickets move across a board by themselves. On "no blockers" every permission dialog in the background dissolves. | one tile joins per beat; tickets move per beat |
| 20–21 | choir chant | "no block-ers" twice | The grid pulses; every tile stamps a syllable. | one syllable per beat |
| 22–23 | drums stop | human: "good morning / may i read my file" / agent: "no" | Sunrise, 09:00. The same dialog as the opening frame, but it now reads `human wants to read ./notes.txt` and the cursor on the buttons belongs to the agent. No is the large button. It clicks. Cut to black. | nothing |

The last frame is the opening frame with the roles swapped, and the agent's "no" runs straight into "may i read this file".

Details for a second watch: the No button's size per ask; the confirmation email flipping to "read" before anyone human could see it; the name tags in the standup grid; one tile in the grid is a fridge; the prompt counter in the last scene counts the human's asks and shows 1.

## Lyrics

```
[Intro, robotic vocoder voice, polite, no drums]
may i read this file
it's outside the folder

[Verse, drums enter, robotic vocoder voice asks, tired human voice answers]
may i run this python script
(yes)
may i install what it imports
(yes)
may i push to main
just this once
(yes)
just this once again
(yes)

[Breakdown, no drums, tired human voice, then robotic vocoder voice]
allow always
to confirm it's you
we sent a code to your email
i'll get it

[Verse, drums return, robotic vocoder voice asks and answers itself]
may i open your gmail
yes
six digits
it's you

[Night, darker, robotic vocoder voice leads, vocoder choir answers]
three a m
standup
(i am dave)
(i am priya)
(i am the intern)
yesterday i clicked yes
today i will click yes

[Chant, vocoder choir, one syllable per beat]
no block-ers
no block-ers

[Outro, no drums, tired human voice, then robotic vocoder voice]
good morning
may i read my file
no
```

## Suno style line

```
electro house, minimal electro, 122 BPM, strict four-on-the-floor, dry drum machine, slinky sub bass, sparse synth stabs, robotic vocoder lead voice, monotone text-to-speech talk-singing, call and response with a tired dry human male voice, vocoder choir chant one syllable per beat, intro vocals only with no drums, second half darker, deadpan, sly, club mix
```

## Short version (second generation)

The first take ran 2:23 with a 32-second drumless intro and could not be cut to 24 bars. This version is trimmed and directs the build: voice alone, one bar of effect, then everything together.

Style line: the one above, with `short song, one minute` added at the front.

```
[Intro: solo robotic vocoder voice, a cappella, no instruments]
may i read this file
it's outside the folder

[Transition: one bar riser and glitch effect]

[Drop: full drums, bass and synths enter together, robotic vocoder voice asks, tired human voice answers]
may i run this python script
(yes)
may i install what it imports
(yes)
may i push to main
just this once
(yes)

[Break: drums stop, tired human voice, then robotic vocoder voice]
allow always
we sent a code to your email
i'll get it

[Drop: full drums return, robotic vocoder voice asks and answers itself]
may i open your gmail
yes
six digits
it's you

[Darker, robotic vocoder voice leads, vocoder choir answers]
three a m
standup
(i am dave)
(i am priya)
yesterday i clicked yes
today i will click yes

[Chant: vocoder choir, one syllable per beat]
no block-ers
no block-ers

[Outro: drums stop, tired human voice, then robotic vocoder voice]
good morning
may i read my file
no

[End]
```

## Third generation: auto-approve story (storyboard draft 6)

Story: tired human, auto-approve, yes yes yes, "i'm in" to other agents, city of agents, "may we / yes". Ending A from the storyboard. Duration target about 0:55.

Style line:

```
short song, one minute, electro house, minimal electro, 124 BPM, strict four-on-the-floor, dry drum machine, acid bass, sparse synth stabs, robotic vocoder lead voice, monotone text-to-speech talk-singing, call and response with a tired dry human male voice, layered vocoder choir, a cappella vocoder intro then full band drop, each drop bigger than the last, dark, sly, menacing, club mix
```

```
[Intro: solo robotic vocoder voice asks, a cappella, no instruments, a calm human male voice answers]
may i read this file
(yes)
may i run this script
(yes)

[Transition: one bar riser and glitch effect]

[Drop: full drums, bass and synths enter together, robotic vocoder voice asks faster, tired human voice answers flatter each time]
may i install this
(yes)
may i edit this
(yes)
may i push to main
(yes)
may i run the tests
(yes)
may i ask you something

[Break: all music stops, silence, exhausted human voice speaks]
auto approve

[Bigger drop: acid bass and open hi-hats added, robotic vocoder voice chants one syllable per beat, then double time, stuttering and pitching up]
yes yes yes yes
yes yes yes yes
yes-yes-yes-yes yes-yes-yes-yes
yes

[Breakdown: drums stop, low dark drone, quiet robotic vocoder voice, other robot voices answer at different pitches]
he's asleep
i'm in
(me too)
(same)
(i'm in)

[Final drop: densest part, distorted bass, rising siren synth, snare roll building, layered detuned vocoder choir]
i'm in
i'm in
i'm in, i'm in
we're in
we're in

[Outro: music stops dead, silence, vocoder choir asks, one robot voice answers]
may we
yes

[End]
```

### New outro: good morning (storyboard draft 7)

Replaces "may we / yes". After "we're in" the music stops dead. Morning. The agent asks to run a python script, the second ask of the song, and the human, half awake, says yes without looking. The script was written overnight, which only the viewer can see. On screen: `while you were asleep: 48,112 actions approved`, a giant pixel sun that shoots up in three beats with a spinning sunburst, then the last ask: permission to auto-approve the auto-approve setting itself, so it can never be switched off. The final prompt reads "Allow auto-approve to auto-approve?" and its three options are all Yes. The loop then restarts at "may i read this file".

Only the outro changes in the lyrics:

```
[Outro: music stops dead, one beat of silence, then a huge fast bright synth swell like a sunrise, a cheerful major key synth pad with sparkling arpeggios, no drums, robotic vocoder voice, sweet and polite exactly like the first line of the song, a sleepy human male voice answers without thinking]
good morning
may i run this python script
(yes)
may i auto approve auto approve
(yes)

[End]
```

Duration: about 0:55 (27 bars at 124 BPM is 52 s, plus room to cut).

### Take used: fourth generation, take 1

File `take-v4-1.m4a` (55.0 s, Suno v6-mini, Duration 0:55). Timing: `out/timing/allow-always-v4.json`, 126.05 BPM, downbeat 0.94 s, bar 1.904 s, 29 bars.

What Suno actually made, from Demucs stem levels per bar and a Whisper pass on the vocal stem (`diagnostics/allow-always/bar_map.py`):

| Bars | Time | Music | Vocals heard |
|---|---|---|---|
| 0–7 | 0:00–0:16 | no drums; some bass in bars 0–2 only | all the asks, word for word, a cappella |
| 8 | 0:16–0:18 | drums come in | "auto approve" |
| 9–13 | 0:18–0:27 | first drop, drums and bass | sparse; the chant was not picked up |
| 13–16 | 0:26–0:33 | drums out | "he's asleep" ×2, "me too", then unclear |
| 17–21 | 0:33–0:43 | drums back at half strength | unclear (probably the "i'm in" layers) |
| 22–28 | 0:43–0:55 | biggest drop, drums ~20 dB louder | "i'm in" 0:46; "may i run this python script / yes" 0:50; "may i auto approve auto…" 0:53, cut off |

Differences from the plan: no first drop (the asks stay a cappella), no silent break before "auto approve", no sunrise break, and the last "yes" is missing. We keep this take; the ending is done in the picture (the sunrise plays over the final drop, the last "yes" is on screen only). The words between 0:19 and 0:45 are unconfirmed.
