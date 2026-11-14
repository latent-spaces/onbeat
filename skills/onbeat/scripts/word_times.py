"""Validate word timestamps without loading audio/model dependencies."""
import math


def valid_words(words, duration):
    """Return (usable, rejected); preserve unaligned words for explicit interpolation.

    Reject model hallucinations beyond the recording rather than clamping them into
    plausible-looking lyrics. Unknown endpoints stay unknown together.
    """
    usable, rejected = [], []
    for original in words:
        word = dict(original)
        start, end = word.get("start"), word.get("end")
        if start is None or end is None:
            word["start"] = word["end"] = None
            usable.append(word)
        elif (not math.isfinite(start) or not math.isfinite(end)
              or start < 0 or end < start or start >= duration or end > duration):
            rejected.append(word)
        else:
            usable.append(word)
    return usable, rejected
