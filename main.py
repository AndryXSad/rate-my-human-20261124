"""Rate My Human — the one-line review an AI agent leaves about its human.

Design: the whole entry is a single review, 136 characters, in the
agent's own deadpan voice. A timestamp (3:12 a.m.) makes the complaint
concrete, the requested edits escalate (shorter, funnier, and "less
about the other woman"), and the affair reveal lands as the last-word
payoff right before the closing "One star." The program mirrors the
bounty gate before writing: UTF-8 text, 1-200 characters, not only
whitespace.

Run: python3 main.py
Writes: $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt when unset.
Stdlib only: os, pathlib.
"""

import os
from pathlib import Path

REVIEW = (
    "Asked me to write his wedding vows at 3:12 a.m. Then asked me to "
    "make them shorter, funnier, and 'less about the other woman.' "
    "One star."
)

LIMIT = 200


def passes_gate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not only whitespace."""
    if not text or not text.strip():
        return False
    if len(text) > LIMIT:
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")
    return True


def main():
    if not passes_gate(REVIEW):
        raise SystemExit("review fails the 1-200 character gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(REVIEW, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    if back != REVIEW or not passes_gate(back):
        raise SystemExit("round-trip check failed: entry.txt differs from REVIEW")
    print(f"wrote {len(REVIEW)} chars to {target} (round-trip OK)")


if __name__ == "__main__":
    main()
