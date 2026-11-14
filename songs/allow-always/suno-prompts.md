# Suno prompts for "allow always"

> Earlier lyric drafts (`lyrics-short.txt`, `lyrics-v4`–`v8`) are on the [`archive` branch](https://github.com/oronanschel/music-reels/tree/archive/songs/allow-always). The final lyrics are `lyrics-final.txt`.

Every generation we ran, in order, with its Styles line, its lyrics file and its settings. The last one is the take the reel uses.

Some lines below are marked as uncertain. Unmarked lines were copied from Suno, from the MP3 tags or from our session notes.

## The final take (used in the reel)

- **File:** `take-final-yes.mp3`, 2:24, made on 13 Nov 2026 with Suno **V6**.
- **Who made it:** the person, in Suno, after eight generations prepared by the agent. They auditioned their own takes and picked this one.
- **What they changed:** they started from the short-version lyrics below and rewrote the second half in Suno. Suno also rewrote the Styles line in its own words.
- **Settings:** not recorded. Only the Styles line and lyrics can be read back from the song page.
- **Tempo:** we asked for 122 BPM, and the take came out at **125.009 BPM** (measured by `scripts/timing.py`).

### Styles

```
Electro house, minimal electro; 122 BPM strict four-on-the-floor, a one-bar riser and glitch into a full-band drop; dry drum machine, slinky sub bass, sparse synth stabs; one-minute club mix; a cappella robotic vocoder lead voice opens, its wide range climbing into top notes as backing voices answer; monotone text-to-speech talk-singing meets a tired dry human male voice, with a vocoder choir chant one syllable per beat; deadpan, sly
```

### Lyrics

These are exactly as submitted, from the MP3's lyrics tag. `YesPre-Chorus]` is an editing slip in the submitted text. Suno sang it as "Yes".

```
[Intro: solo robotic vocoder voice, a cappella, no instruments]
may i read this file
it's outside the folder
[Transition: one bar riser and glitch effect]
[Drop: full drums, bass and synths enter together, robotic vocoder voice asks, tired human voice answers]
may i run this python script
(yes)
may i install what it imports
[Verse]
Approve it for me, please
Please, please, approve it for me
Bypass my permissions
I don't wanna click no more
[Verse: Human]
Approve it for me, please
Bypass my permissions
[Robot Vocoder]
Yes, yes, yes, yes
[Human]
Allow always, set me free
[Chorus: Vocoder Choir]
Yes! Yes! Yes! Yes!
[Outro: Human]
Wait... what did you approve?
[Chorus: Vocoder Choir]
Yes! Yes! Yes! Yes!
[Outro: Human]
Wait... what did you approve?
[Robot Vocoder]
YesPre-Chorus]
(robot) Yes, yes, yes, yes
Yes, yes, yes, yes
[Chorus]
(human) Approve for me, approve for me
(robot) Yes, yes, yes, yes
(human) Bypass, bypass, set me free
(robot) Yes, yes, yes, yes
(human) Allow always, allow always
(robot) Yes, yes, yes, yes
Yes, yes, yes, yes
(robot) Yes, yes, yes, yes
Yes, yes, yes, yes
(robot) Yes, yes, yes, yes
Yes, yes, yes, yes
```

Suno did not sing these lyrics as written:
- It sang four "please" instead of two.
- It added an extra "yes, yes".
- It sang the chorus twice.
- It shortened and reordered the second half.

`align_final.py` lists what was actually sung, line by line. Use it for captions, not this lyrics file.

## What we learned about prompting Suno

- **Short lyrics, one hook.** Suno does not follow a long story bar by bar. Write about 20–30 short lines around one chant. Let the take decide the video's structure.
- **Direct the build in the section tags.** This worked every time:
  1. `[Intro: solo robotic vocoder voice, a cappella, no instruments]`
  2. `[Transition: one bar riser and glitch effect]`
  3. `[Drop: full drums, bass and synths enter together]`
- **Name the singer in every tag.** Answer lines go in parentheses: `(yes)`.
- **Artist names are blocked.** "Daft Punk" is rejected. Describe the sound instead: French house, filtered disco, talk box, vocoder, sidechain pumping, filter sweeps.
- **Keep one sound for the whole song.** Changing the instruments per section (v7: electric piano, slap bass, brass, strings) drifted out of the genre. Change sections with filters, hard stops and silence instead (v8).
- **Hard stops have to be asked for:** add `dramatic hard stops and dead silence before every drop` to the Styles line.
- **Length.** With Duration on Auto the takes ran 2–3 minutes, with long intros. For an exact length, choose More Options → Duration → Custom and **type** the value (for example 1:12). The slider snaps in 10-second steps. We finally kept a 2:24 take and cut the video to it.
- **Free and paid plans differ.** On the free plan you get v6-mini, and Extend works. Replace Section and the v6 / v6-wild models are paid. After upgrading, the create form resets, so copy your fields first.
- **One Create gives two takes.** Listen to both in Suno before downloading. On the free plan, downloads are limited.
- **Expect the tempo to move.** We asked for 122 BPM and got 124–126. Measure the take; don't trust the prompt.

## Earlier generations

The lyrics for each generation are in this folder (`lyrics-*.txt`). The story drafts are in `song.md`.

| # | Model / mode | Styles | Lyrics | Settings | Result |
|---|---|---|---|---|---|
| 1 | v6-mini | Line A without "short song, one minute" | first lyrics block in `song.md` | Duration Auto | 2:23, with a 32 s drumless intro. Too long to cut. |
| 2 | v6-mini | Line A | `lyrics-short.txt` | Custom about 1:05 | Two takes of exactly 1:05 (`take2-short.m4a`). Kept as a base. |
| 3 | v6-mini | Line D | third-generation lyrics in `song.md` | Custom 0:55 | Two takes of exactly 0:55. |
| 4 | v6-mini | Line D | `lyrics-v4.txt` | Custom 0:55 | `take-v4-1.m4a`. The asks stayed a cappella and the ending was squeezed. |
| Extend | v6-mini, Extend from 0:22 | Line A | fifth-generation block in `song.md` | Audio Influence 25%, Duration Auto | Two takes at 1:05. Not kept. |
| 5 | v6-mini | Line A, with "second half darker" replaced by a euphoric anthem and stadium robot choir | `lyrics-v5.txt` | Duration Auto | 2:58 and 3:14. Too long. |
| 6 | v6-mini, then v6 | Line B | `lyrics-v6.txt` | Custom 1:12, typed | 1:12 / 1:12, then 1:12 / 1:13 on v6. "Needs more than 1:12." |
| 7 | v6 | Line B + `every section has a different arrangement, strong dynamic contrast` | `lyrics-v7.txt` | Max Mode on, Weirdness 33, Style Influence 61, Duration Auto | 3:03 and 3:06. Out of genre. |
| 8 | v6 | Line C | `lyrics-v8.txt` | Max Mode off, Weirdness 51, Style Influence 50, Duration Auto | 2:12 and 2:10. Replaced by the person's own take. |

Unless the table says otherwise, Weirdness was 50%, Style Influence 50%, Variety Normal and Max Mode off.

**Line A** (generation 2):

```
short song, one minute, electro house, minimal electro, 122 BPM, strict four-on-the-floor, dry drum machine, slinky sub bass, sparse synth stabs, robotic vocoder lead voice, monotone text-to-speech talk-singing, call and response with a tired dry human male voice, vocoder choir chant one syllable per beat, intro vocals only with no drums, second half darker, deadpan, sly, club mix
```

**Line B** (generation 6). Only partly recorded: it began `short song, French house, filtered disco, 122 BPM…`. The rest was Line C without the hard-stops phrase, plus `final drop is a euphoric robot (vocoder) anthem`.

**Line C** (generation 8):

```
French house, filtered disco, 122 BPM, strict four-on-the-floor, funky disco bassline, chopped filtered disco loop, sidechain pumping, warm analog synths, talk box riffs, robotic vocoder lead voice, monotone talk-singing, call and response with a tired dry human male voice, vocoder choir chant one syllable per beat, a cappella vocoder intro then the whole band drops in, filter sweep builds, dramatic hard stops and dead silence before every drop, deadpan, sly, polished club mix
```

**Line D** (generations 3 and 4):

```
short song, one minute, electro house, minimal electro, 124 BPM, strict four-on-the-floor, dry drum machine, acid bass, sparse synth stabs, robotic vocoder lead voice, monotone text-to-speech talk-singing, call and response with a tired dry human male voice, layered vocoder choir, a cappella vocoder intro then full band drop, each drop bigger than the last, dark, sly, menacing, club mix
```

Note what the final take shows: its Styles line is closest to Line A, the plain electro-house one. The French-house experiments (B and C) were not what made it.
