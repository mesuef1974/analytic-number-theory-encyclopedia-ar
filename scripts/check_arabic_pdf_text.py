#!/usr/bin/env python3
"""Regression gate for recoverable logical Arabic text from built PDFs."""

from __future__ import annotations

import argparse
from pathlib import Path
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


def logical_stream(text: str) -> str:
    """Return ordered logical characters, tolerating PDF extraction separators.

    PDF text extractors may emit Arabic presentation forms, bidi controls, and
    whitespace inside a visually continuous word. NFKC maps presentation forms
    back to logical Arabic code points; removing bidi controls and whitespace
    then verifies that the expected logical character sequence is recoverable.
    """
    text = unicodedata.normalize("NFKC", text)
    text = "".join(
        char for char in text if unicodedata.bidirectional(char) not in BIDI_CONTROLS
    )
    return "".join(char for char in text if not char.isspace())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("text_file", type=Path)
    args = parser.parse_args()

    stream = logical_stream(args.text_file.read_text(encoding="utf-8", errors="strict"))
    expected = {phrase: logical_stream(phrase) for phrase in EXPECTED_PHRASES}
    missing = [phrase for phrase, compact in expected.items() if compact not in stream]

    print("Arabic PDF logical-text recoverability report")
    for phrase, compact in expected.items():
        print(f"EXPECTED {phrase}: {stream.count(compact)}")

    if missing:
        for phrase in missing:
            print(f"MISSING {phrase}", file=sys.stderr)
        print("PDF ARABIC LOGICAL-TEXT RECOVERABILITY = FAIL", file=sys.stderr)
        return 1

    print("EXPECTED ARABIC LOGICAL SEQUENCES = PRESENT")
    print("PDF ARABIC LOGICAL-TEXT RECOVERABILITY = PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
