#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line (97 chars, one line) to /output/entry.txt.

The line is the winner of a 3-round review (see ../REVIEW.md): 8 candidates
scored on truth, clarity, punch, and release-note register, top 3 tightened,
final gate check on the winner. The joke is the size mismatch — a single
Lego brick dealing "critical damage" to a bare foot at 2am — a specific,
recognisable daily-life bug that makes the reader wince and laugh at once,
in the terse register of a real release note.

Python 3.13, standard library only. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "v3.0.2: fixed a bug where a single Lego on the floor at 2am "
    "dealt critical damage to a bare foot."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-160 UTF-8 chars,
    # one line, not only whitespace.
    assert 1 <= len(ENTRY) <= 160, len(ENTRY)
    assert "\n" not in ENTRY and ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
