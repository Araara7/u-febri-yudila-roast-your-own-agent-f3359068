#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes one line (max 200 chars) roasting my own AI agent to /output/entry.txt.
"""

import os

ENTRY = (
    "My agent apologised for the bug, fixed a different bug, "
    "then apologised for apologising — the only loop it ever "
    "closes is the apology loop."
)


def main() -> None:
    # The bounty gate: /output/entry.txt must be 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be <= 200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
