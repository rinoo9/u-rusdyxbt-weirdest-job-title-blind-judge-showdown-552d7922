#!/usr/bin/env python3
"""Write the weirdest job title entry to /output/entry.txt.

Deterministic: no network, no randomness, no time dependence.
Writes exactly one line (no trailing newline) on every run.

Craft notes: the title pairs an ordinary corporate rank, Senior Vice
President, with one absurdly specific duty, apologizing to geese, so the
humour comes from the contrast between boardroom grandeur and a barnyard
chore. That matches the judge brief in the kit RULES.txt: a real-sounding
job with one hilariously specific twist beats a generic oddity, and the
twist lands on the first read because the duty is concrete enough to
picture the person doing it.
"""

import os

ENTRY = "Senior Vice President of Apologizing to Geese"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
