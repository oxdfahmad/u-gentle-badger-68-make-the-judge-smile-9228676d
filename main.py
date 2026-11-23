#!/usr/bin/env python3
"""Make the Judge Smile — writes one warm line to /output/entry.txt."""

import os

LINE = "At 7 a.m. the baker slipped an extra warm roll into my bag and winked, 'for the road, today you look like you need two.'"

# The line: a small kindness at 7 a.m., a warm roll, a wink, and a surprise
# second roll — warmth, one concrete detail, and a turn the reader does not
# expect, in the baker's own words rather than a greeting-card sentiment.


def validate_line(text):
    """Check the entry against the gate before writing it out."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("line must not be only whitespace")
    return text


def main():
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == LINE + "\n", "read-back mismatch"
    print(f"entry.txt OK: {len(LINE)} chars")


if __name__ == "__main__":
    main()
