# Instagram brief: "allow always"

Instructions for the agent that runs the Instagram account. **Nothing gets posted without the owner's OK.** Prepare the post as a draft or scheduled post, then send the owner the caption, cover frame and time for approval.

## The file

| | |
|---|---|
| Upload this | `video/out/allow-always-final-80s-boom2.mp4` (1080×1920, 60 fps, 2:24, about 67 MB) |
| Preview copy only | `video/out/allow-always-final-80s-boom2-phone.mp4` (720p, about 12 MB). Don't post this one. |
| Format | Reel, 9:16. Upload it as is: no crop, no speed change, no filter, no Instagram text or stickers. |
| Audio | Keep the original audio. Don't add or swap music from Instagram's library. |

The video loops: the last frame is the same permission prompt as the first. Don't trim the start or the end, or the loop breaks.

## Cover

Use a frame from inside the video, not a separate thumbnail. In order of preference:

1. **About 1:05:** the dancers in the disco with the Earth exploding behind them.
2. **About 0:01:** the opening permission prompt, "read ../billing-service/.env", with the cursor over "Allow always".

In the profile grid the cover is cropped to the centre square, so check that the main subject is in the middle.

## Caption

Follow this structure:

1. **Hook line:** the first line, which shows before "more".
2. One or two lines of context.
3. **"Details if you replay it"**, a short list.
4. Credit line.
5. **One** genre hashtag.

Draft for the owner to edit:

```
You clicked "allow always". What did you approve?

An agent asks for permission so politely, so many times, that you stop reading and give it everything.

Details if you replay it:
- the commands it asked for are real ones you've approved this week
- the robot doesn't click the button once, it clicks it twice
- the Earth keeps exploding behind the dance floor and nobody stops dancing
- the last frame is the first frame

Claude wrote the lyrics and Suno sang them. I cut the loop and drew every frame in code with HyperFrames, timed to the vocals and the kick.

Want the code? Comment LOOP and I'll send you the repo.

#italodisco
```

Hook alternatives to offer the owner:

- "Wait… what did you approve?"
- "It asked for everything. You said yes to everything."
- "POV: your coding agent after you click 'allow always'"

Rules for the caption:

- One genre hashtag only, not a block of tags. `#italodisco` or `#synthwave`, and the owner picks.
- Don't explain the joke past the context lines.
- No personal details, emails, file paths or account names in the caption or comments.

## "Comment LOOP for the repo"

The caption invites people to comment **LOOP** to get the GitHub repo that shows how the reel was made.

**The repo isn't ready yet.** The owner will send the link later.
- Until the owner gives you the link, **remove the "Comment LOOP" line from the caption** before posting.
- If the reel is already up, edit the line in once the link arrives.
- Never invent a link, and never send a link to this working repo.

Once you have the link:

1. **Who gets a DM:** anyone whose comment contains "loop" (any case), plus anyone who asks for the code, the repo or how it was made.
2. **The DM**, sent once per person:
   ```
   Here's how it's made: <REPO LINK>
   The README walks through the whole pipeline: Suno take → beat and word timing → HyperFrames → render. Thanks for watching!
   ```
3. **Reply to the comment** too, so others see it works: "Sent! Check your DMs."
4. **Bio:** put the same repo link in the bio, with the line "how it's made ↓".
5. **Volume:**
   - Up to about 30 requests a day: send the DMs by hand.
   - Above that, stop and tell the owner. Use an auto-DM tool only if it runs on Instagram's official API (for example ManyChat), and only if the owner sets it up. Never use unofficial DM bots or browser scripts.
6. **Log:** keep a simple list of usernames and when each was sent the link. No other personal details. This prevents double-sending.

Don't reply "comment below!" or ask for comments anywhere else. Meta demotes posts that bait engagement, so keep the one plain line in the caption.

## Comments

- Pin a first comment only if the owner asks for one. Once the repo link exists, a good one to suggest is: "Comment LOOP and I'll DM you the code".
- When people ask for the full song, say there's no full version yet and that you've noted the request. Don't promise a release date or a link.
- When people argue about whether "allow always" is fine, let them argue. Reply short, without lecturing, and don't take sides on specific AI products.
- When a comment compares the robots to Daft Punk, don't confirm any link. A neutral reply like "80s robots, all of them" works. Flag any comment that alleges copying to the owner instead of answering it.
- Ignore spam and anything asking you to click a link or DM a code.

## Before posting, check with the owner

These are open questions, not facts:

- **Suno rights.** Posting the song commercially depends on the owner's Suno plan. Confirm before boosting or monetising.
- **The credit line.** It names "Claude" and "Suno" without model versions. Ask whether to name exact versions.
- **The robot helmets** look a lot like Daft Punk's. The owner knows about this. Raise it once if the post gets boosted.
- **Post time.** There's no data in this repo on when the account's audience is online. Use the account's Insights if you can see them; otherwise ask.
- **Length.** The reel is 2:24. The playbook's best performers ran 30–45 s. Post the full version unless the owner asks for a short cut, which would need a new render.

## After posting

Report back to the owner:

- The post link.
- After 24 h and after 72 h: views, average watch time, the percentage who watched to the end, shares, saves, and the 3 most-liked comments.
- After the repo link goes live: how many people asked for it and how many DMs you sent.

Watch time and replays tell us whether the loop works. The comments tell us whether the arguable claim lands.
