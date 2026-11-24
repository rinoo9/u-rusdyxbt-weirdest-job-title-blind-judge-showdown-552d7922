#!/usr/bin/env python3
"""Write the weirdest job title entry to /output/entry.txt.

Deterministic: no network, no randomness, no time dependence.
Writes exactly one line (no trailing newline) on every run.
"""

import os

ENTRY = "Senior Vice President of Apologizing to Geese"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
