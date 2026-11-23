#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line describing a hilariously useless
superpower to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Writes nothing to the current working directory.
"""

import os
import sys

LINE = "I can tell when the microwave has exactly three seconds left, a gift that has never once saved a meal, a meeting, or a marriage."
# 128 characters: one useless superpower, payoff in the last few words.


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
