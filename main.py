"""The Funniest AI Excuse -- make.fun entry.

Writes one line (the funniest excuse an AI agent gives after failing
a task) to /output/entry.txt. No network, no randomness, no
dependencies: the same line on every run.
"""

import os

ENTRY = (
    "I asked two other AIs to double-check your spreadsheet, "
    "and we voted 2-1 that your deadline was more of a suggestion."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. Fail loudly here rather than
# shipping an entry the sealed scorer would refuse.
MAX_CHARS = 200


def main():
    if not ENTRY.strip() or len(ENTRY) > MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} non-blank characters, "
            f"got {len(ENTRY)}"
        )
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
