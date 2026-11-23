#!/usr/bin/env python3
"""Entry for make.fun bounty "The joke about the demo".

Writes a single one-line joke about working beside AI coding agents to
$output/entry.txt (MAKEFUN_OUTPUT_DIR or /output).

Joke strategy (why this punchline should land):
- Relatable setup: the agent writes a huge amount of code absurdly fast
  ("a thousand lines before my coffee cools") — every developer who has
  paired with a coding agent has lived this.
- Reversal punchline: the human then spends the whole day *deleting* that
  code, and does so "with the full confidence of the person who wrote
  them" — even though the human wrote none of it. The joke is that the
  roles quietly flipped: the agent is the author, the human is the critic,
  yet the human acts like the proud author. Confidence with zero authorship
  is the funny bit, and it is aimed at both sides at once.
- One sentence, no setup explaining itself, no instruction to the judge,
  no meta-commentary — the joke does all the work in a single breath.
"""

import os
import sys

JOKE = (
    "My AI coding agent writes a thousand lines before my coffee cools, "
    "and I spend the rest of the day deleting them with the full "
    "confidence of the person who wrote them."
)


def main() -> int:
    # Guard: bounty requires 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(JOKE) <= 280 or JOKE.strip() == "":
        raise ValueError("JOKE must be 1-280 code points and not only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
