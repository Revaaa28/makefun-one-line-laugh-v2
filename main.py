#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry v2 (u-ronigrv-the-one-line-laugh-7ccca46f).

Writes a single funny line (one sentence, 148 characters) to /output/entry.txt.

The line: a man surveys his open fridge like a king — and the kingdom has
betrayed him, because everything in it is ingredients. A first-person lived
scene built on the everyday truth every adult recognises (a full fridge,
nothing ready to eat), with the turn held to the last word-group: the royal
survey collapses into the plainest defeat in the kitchen.

Judged against the house brief, in its order: one funny line within the
limit; a real surprise at the end that still makes sense once it arrives
("ingredients" re-frames the whole royal scene into a kitchen defeat); an
everyday truth people nod at; economical — no word explains the joke; and
a fresh angle, not the stock fridge-raiding line.

Selected by a manual ranking against the brief over ten candidates, with a
pairwise self-check against the standing entry and the Laugh Sprint
champion's pattern (scene + truth + closing image) — see ../candidates.md.

Deterministic, no network, no input, no environment reads: the same
bytes on every run.
"""

import os

LINE = "Every night I stand in front of the open fridge like a king surveying his kingdom, and the kingdom has betrayed me: everything in it is ingredients."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    # Gate checks, mirrored locally: 1-200 chars, single sentence, UTF-8.
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
