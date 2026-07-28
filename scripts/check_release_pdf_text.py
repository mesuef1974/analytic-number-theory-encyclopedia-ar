#!/usr/bin/env python3
"""Fail when publication PDF text leaks metadata or loses release structure."""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

FORBIDDEN_LITERAL = (
    "REVIEWED",
    "APPROVED",
    "RELEASE-READY",
    "NOT-RELEASE-READY",
    "PASS-FOR-AUTHORING",
    "REFERENCE-AUDIT",
    "EVIDENCE-FIRST",
    "PRE-AUTHORING",
    "POST-AUTHORING",
    "OWNER-ADOPTED",
    "ACTIVE-CITABLE",
    "AUTHORED-DRAFT",
    "NON-CITABLE",
    "حالة الفصل",
    "حالة المتن",
    "حالة الحزمة",
    "حالة النسخة",
    "حالة الاعتماد",
    "وضع الفصل",
    "الوضع التحريري",
    "ملاحظة تحريرية",
    "تنبيه تحريري",
    "حالة المستودع الحالية",
    "حالة دفعة التأليف",
    "قرار المالك الصريح",
    "اعتماد المالك",
    "بعد نجاح البناء",
    "اعتمده مالك المشروع",
    "أذن بدمجه",
    "مسودة غير قابلة للاستشهاد",
    "ensure@LTR",
    "docs/",
    "manuscript/",
    "build/",
    ".md",
    "worktree",
    "XeLaTeX",
    "Biber ->",
)

FORBIDDEN_REGEX = (
    re.compile(r"(?<![A-Z])DRAFT(?![A-Z])"),
    re.compile(r"\bPR\s*#?\s*\d+\b"),
    re.compile(r"\bIssue\s*#?\s*\d+\b"),
    re.compile(r"\b[0-9a-f]{40}\b", re.I),
    re.compile(r"\bSHA-?256\b", re.I),
    re.compile(r"ANT-(?:THM|LEM|PROP|COR|DEF|EX|REM|OPEN|COMP)-\d{2}-\d{2}"),
    re.compile(r"\?\?"),
)

REQUIRED = (
    "Walfisz",
    "Ahlfors",
    "Helfgott",
    "Zeitschrift",
    "فهرس العلماء",
    "فهرس النظريات والنتائج",
    "فهرس الرموز والمصطلحات",
)


def normalize_pdf_text(text: str) -> str:
    """Normalize Arabic presentation forms emitted by PDF text extraction."""
    normalized = unicodedata.normalize("NFKC", text)
    # Directional controls separate Arabic words in some Poppler outputs but do
    # not carry publication content. Replace them with ordinary spaces.
    normalized = re.sub(r"[\u061c\u200e\u200f\u202a-\u202e\u2066-\u2069]", " ", normalized)
    normalized = re.sub(r"[ \t]+", " ", normalized)
    return normalized


def contains_token(text: str, token: str) -> bool:
    """Accept extraction-only whitespace inserted inside Arabic words."""
    if token in text:
        return True
    if re.search(r"[\u0600-\u06ff]", token):
        compact_text = re.sub(r"\s+", "", text)
        compact_token = re.sub(r"\s+", "", token)
        return compact_token in compact_text
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("text_file", type=Path)
    args = parser.parse_args()

    raw_text = args.text_file.read_text(encoding="utf-8", errors="replace")
    text = normalize_pdf_text(raw_text)
    failures: list[str] = []

    for token in FORBIDDEN_LITERAL:
        if contains_token(text, token):
            failures.append(f"forbidden literal {token!r}")

    for pattern in FORBIDDEN_REGEX:
        matches = pattern.findall(text)
        if matches:
            failures.append(f"forbidden pattern {pattern.pattern!r}: {len(matches)}")

    for token in REQUIRED:
        if not contains_token(text, token):
            failures.append(f"required publication text missing: {token!r}")

    if failures:
        print("RELEASE PDF TEXT CHECK: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("RELEASE PDF TEXT CHECK: PASS")
    print("Metadata absent; scientific text, cross-references, and named indexes retained.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())