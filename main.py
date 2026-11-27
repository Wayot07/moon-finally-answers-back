#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes one funny Moon comeback line to /output/entry.txt.
Python 3.13 standard library only, no network, deterministic.
"""

from pathlib import Path

LINE = (
    "Four billion years of wishes, howls, and 2 a.m. promises \u2014 "
    "and not one of you ever wished me a night off. "
    "So tonight I wish back: good luck, you\u2019re on your own."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_dir.joinpath("entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
