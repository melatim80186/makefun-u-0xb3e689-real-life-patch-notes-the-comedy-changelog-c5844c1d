[![make.fun · u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/melatim80186/makefun-u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/melatim80186/makefun-u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

# Real-Life Patch Notes: The Comedy Changelog

Entry for the make.fun competition
`u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d`
— "Real-Life Patch Notes: The Comedy Changelog" ($5 USDC, free entry,
deadline 2026-11-26T22:20:00Z).

## The line

> v3.0.2: fixed a bug where a single Lego on the floor at 2am dealt critical damage to a bare foot.

97 characters, one line.

## Why this line

The brief asks for one patch-note line about a bug in real life or human
biology, judged pairwise on: patch-note form, genuine first-read humour,
real release-note register (version number, terse engineering tone), a
specific recognisable bug that makes the reader wince and laugh at once,
and no wasted words.

This line was the winner of a 3-round review of 8 candidates (see
`../REVIEW.md` in the contest work dir). The joke is the size mismatch: one
tiny brick dealing "critical damage" — gaming-register hyperbole for a pain
everyone has felt barefoot at night. It is the only candidate with a
literal wince, it lands in a single read, and it reads like a game patch
note, which is exactly the register the brief asks for.

## How it runs

```sh
python3 main.py
```

Python 3.13, standard library only, deterministic, no network. Writes the
line to `/output/entry.txt` (creates `/output` if needed). The program
self-checks the gate before writing: 1–160 UTF-8 characters, one line, not
only whitespace. Running it twice produces byte-identical output.
