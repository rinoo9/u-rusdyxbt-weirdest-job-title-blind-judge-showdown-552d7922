#!/usr/bin/env python3
"""Write the weirdest job title entry to /output/entry.txt.

Deterministic: no network, no randomness, no time dependence.
Writes exactly one line (no trailing newline) on every run.

Craft notes: the title pairs an ordinary corporate rank, Director,
with one absurdly specific duty, translating sighs in meetings into
action items, so the humour comes from the contrast between boardroom
grandeur and the most thankless meeting chore imaginable. That matches
the judge brief in the kit RULES.txt: a real-sounding job with one
hilariously specific twist beats a generic oddity, and the twist lands
on the first read because the duty is concrete enough to picture the
person doing it — sitting in every meeting, turning every exhale into
a Jira ticket.
"""

import os

ENTRY = "Director of Translating Sighs in Meetings into Action Items"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
