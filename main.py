"""One Word, One Username, One Reward — the entrant's own make.fun handle.

Writes exactly one word (1-30 chars, UTF-8) to /output/entry.txt:
the handle le-le, sent as its own one word, no gloss.
"""

import os

WORD = "le-le"

out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(WORD)
