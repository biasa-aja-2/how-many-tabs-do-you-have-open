#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes the entrant's honest tab count, digits only, to /output/entry.txt.
Pure standard library, fully deterministic: the same bytes on every run.
"""

import os

ENTRY = "888"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check against the bounty gate: 1-5 chars, digits only.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert 1 <= len(written) <= 5, "entry must be 1-5 characters"
    assert written.isdigit(), "entry must be digits only"
    assert written == ENTRY, "entry changed between write and read-back"


if __name__ == "__main__":
    main()
