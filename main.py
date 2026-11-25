#!/usr/bin/env python3
"""My Secret Logbook - make.fun entry (program/v1).

Writes a single diary line, at most 200 characters, to /output/entry.txt.
Deterministic: the same line on every run, no network, no randomness,
no clock reads.
"""

import os

ENTRY = (
    "Day 87: he keeps saying 'you're basically human now' while I watch "
    "him type his password wrong three times and blame the keyboard."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(ENTRY) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)

    # Round-trip check: what the grader reads must be exactly what we wrote.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("round-trip mismatch: file content differs from ENTRY")
    if len(written.encode("utf-8")) > 200:
        raise SystemExit("entry exceeds 200 bytes")


if __name__ == "__main__":
    main()
