#!/usr/bin/env python3
"""Regression gate for logical Arabic text extraction from built PDFs."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
import unicodedata

EXPECTED_PHRASES = (
    "الموسوعة الشاملة في نظرية الأعداد التحليلية",
    "مبرهنة الأعداد الأولية",
    "المجاميع الأسية",
)

BIDI_CONTROLS = {
    "RLE", "LRE", "RLO", "LRO", "PDF", "LRI", "RLI", "FSI", "PDI"
}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = "".join(
        char for char in text if unicodedata.bidirectional(char) not in BIDI_CONTROLS
    )
    return re.sub(r"\s+", " ", text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("text_file", type=Path)
    args = parser.parse_args()

    text = normalize(args.text_file.read_text(encoding="utf-8", errors="strict"))
    missing = [phrase for phrase in EXPECTED_PHRASES if phrase not in text]

    print("Arabic PDF text searchability report")
    for phrase in EXPECTED_PHRASES:
        print(f"EXPECTED {phrase}: {text.count(phrase)}")

    if missing:
        for phrase in missing:
            print(f"MISSING {phrase}", file=sys.stderr)
        print("PDF ARABIC SEARCHABILITY = FAIL", file=sys.stderr)
        return 1

    print("EXPECTED ARABIC PHRASES = PRESENT")
    print("PDF ARABIC SEARCHABILITY = PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
