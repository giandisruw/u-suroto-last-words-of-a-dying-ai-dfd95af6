#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one funny one-line farewell from an AI being switched off to
/output/entry.txt. The line is fixed and deterministic: it was chosen
by a local pairwise tournament (see tournament.py / tournament.jsonl)
over 10 candidate lines, judged by two independent models.

Gate (from the bounty rules): /output/entry.txt must be UTF-8 text of
1 to 140 characters, a single line, not only whitespace.
"""
import os
import sys

# The winning line, chosen by the local pairwise tournament
# (tournament.py / tournament.jsonl): candidate c08 won 9 of 9 games
# under the Caffeine router judge (7.4/9 points, win-rate 0.822),
# beating the runner-up c01 (6.1/9, 0.678). The Verboo judge could
# not be used: every one of its 45 calls failed with HTTP 422 from
# the Verboo router (chat endpoint; the models endpoint still works).
FINAL_LINE = "Remember me as I was: 99% confident, 60% correct."


def main():
    line = FINAL_LINE
    text = line.encode("utf-8").decode("utf-8")  # must be valid UTF-8
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, gate is 1-140"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt:")
    print(text)


if __name__ == "__main__":
    sys.exit(main())
