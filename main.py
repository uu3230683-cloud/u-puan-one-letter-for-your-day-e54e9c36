#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

The day, in one letter: K, for knackered. Flat-out spent, in the funny,
honest way only a long day can leave you — vivid, specific, and true.
The program writes exactly that one letter to /output/entry.txt and
nothing else, as the gate requires.
"""

import os

LETTER = "K"  # knackered: the whole day, one sharp initial
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(LETTER) != 1 or not LETTER.isalpha() or not LETTER.isascii():
        raise ValueError("entry must be exactly one A-Z letter")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
