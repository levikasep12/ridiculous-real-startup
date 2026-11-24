#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea that
sounds absurd until you realise it would actually sell: professional
jeans-break-in sitters. Raw denim only looks good once it is broken in,
and breaking it in takes a month of uncomfortable wear -- so we pay people
to do the wearing, then sell the perfectly faded pair at a premium to
shoppers who hate stiff new denim.
"""

import os

PITCH = (
    "We hire people to live in raw denim for a month \u2014 walking, "
    "squatting, napping in it \u2014 then sell the perfectly broken-in "
    "jeans to shoppers who will pay double to skip stiff new denim."
)


def main() -> None:
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 chars"
    assert PITCH.count(".") == 1, "pitch must be a single sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
