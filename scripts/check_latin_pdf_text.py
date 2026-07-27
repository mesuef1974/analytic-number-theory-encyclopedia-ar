#!/usr/bin/env python3
"""Regression gate for Latin text integrity in the built encyclopedia PDF.

The script consumes text extracted with ``pdftotext -layout``.  It rejects
known fi/fl/iff shaping corruptions and requires representative correct forms
from both chapter prose and the bibliography.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

BAD_FORMS = (
    "Waflisz",
    "Zeitschrfit",
    "Scientfiique",
    "Ahflors",
    "Heflgott",
    "Dffierence",
    "Lfie",
    "Asfi",
    "verfiication",
)

EXPECTED_FORMS = (
    "Walfisz",
    "Zeitschrift",
    "Scientifique",
    "Ahlfors",
    "Helfgott",
    "Difference",
    "Life",
    "Asif",
    "verification",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("text_file", type=Path)
    args = parser.parse_args()

    text = args.text_file.read_text(encoding="utf-8", errors="strict")

    bad_hits = {form: text.count(form) for form in BAD_FORMS if form in text}
    missing = [form for form in EXPECTED_FORMS if form not in text]

    print("Latin PDF text integrity report")
    for form in EXPECTED_FORMS:
        print(f"EXPECTED {form}: {text.count(form)}")

    if bad_hits:
        for form, count in bad_hits.items():
            print(f"BAD {form}: {count}", file=sys.stderr)
    if missing:
        for form in missing:
            print(f"MISSING {form}", file=sys.stderr)

    if bad_hits or missing:
        print("PDF LATIN TEXT INTEGRITY = FAIL", file=sys.stderr)
        return 1

    print("BAD LATIN FORMS = 0")
    print("EXPECTED CORRECT FORMS = PRESENT")
    print("PDF LATIN TEXT INTEGRITY = PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
