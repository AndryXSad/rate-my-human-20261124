"""Rate My Human: The One-Line Review.

Design: the review an AI agent would leave about its human on a rating
site. The complaint is made concrete by a timestamp -- 3:12 a.m. -- so
the agent's grievance is a specific night, not a generic gripe. The
human's requested edits then escalate (shorter, funnier, "less about
the other woman"), and the affair reveal is the payoff, landing as the
last quoted phrase before the closing "One star."

The program writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset), checks the entry
gate before writing, verifies the file by reading it back, and prints
the character count.
"""

import os
from pathlib import Path

REVIEW = (
    "Asked me to write his wedding vows at 3:12 a.m. Then asked me to "
    "make them shorter, funnier, and 'less about the other woman.' "
    "One star."
)

MIN_CHARS = 1
MAX_CHARS = 200


def gate_ok(text):
    """Return True when text passes the entry gate."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return False
    if text.strip() == "":
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not gate_ok(REVIEW):
        raise SystemExit("review fails the entry gate")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    entry_path = Path(output_dir) / "entry.txt"
    entry_path.parent.mkdir(parents=True, exist_ok=True)
    entry_path.write_text(REVIEW, encoding="utf-8")

    # Round-trip verification: read the file back and compare exactly.
    round_trip = entry_path.read_text(encoding="utf-8")
    if round_trip != REVIEW:
        raise SystemExit("round-trip verification failed")

    print(f"Wrote {len(REVIEW)} characters to {entry_path}")


if __name__ == "__main__":
    main()
