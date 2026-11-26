#!/usr/bin/env python3
"""Write the weirdest job title entry to /output/entry.txt.

Deterministic: no network, no randomness, no time dependence.
Writes exactly one line (no trailing newline) on every run.

Craft notes: the title pairs an ordinary corporate rank, Head,
with one absurdly specific duty, replying-all to emails that
explicitly said do not reply all, so the humour comes from the
contrast between a senior-sounding post and the most universally
loathed office habit imaginable. That matches the judge brief in the
kit RULES.txt: a real-sounding job with one hilariously specific
twist beats a generic oddity, and the twist lands on the first read
because the duty is concrete enough to picture the person doing it
— hitting reply-all on the all-staff email within seconds, every
single time.
"""

import os

ENTRY = "Head of Replying All to Emails That Said Do Not Reply All"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
