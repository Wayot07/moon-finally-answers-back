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
    # Pre-write gate: the competition requires UTF-8 text of 1 to 240
    # characters, not only whitespace. Refuse to write anything that
    # would fail the gate instead of writing it and hoping.
    if not 1 <= len(LINE) <= 240:
        raise ValueError(f"entry line must be 1-240 characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("entry line must not be only whitespace")

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir.joinpath("entry.txt")
    target.write_text(LINE, encoding="utf-8")

    # Post-write read-back: the bytes on disk must be exactly the line.
    # If the read-back differs, the entry on disk is not the entry we
    # gated, so fail loudly instead of submitting a wrong file.
    if target.read_text(encoding="utf-8") != LINE:
        raise ValueError("read-back mismatch: entry.txt does not match LINE")


if __name__ == "__main__":
    main()
