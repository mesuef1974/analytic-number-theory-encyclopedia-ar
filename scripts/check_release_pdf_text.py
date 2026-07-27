#!/usr/bin/env python3
"""Fail when publication PDF text leaks internal governance/build metadata."""

from __future__ import annotations

import argparse
import re
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
    "docs/",
    "manuscript/",
    "build/",
    ".md",
    "worktree",
    "XeLaTeX",
    "Biber ->",
)

FORBIDDEN_REGEX = (
    re.compile(r"\bPR\s*#?\s*\d+\b"),
    re.compile(r"\bIssue\s*#?\s*\d+\b"),
    re.compile(r"\b[0-9a-f]{40}\b", re.I),
    re.compile(r"\bSHA-?256\b", re.I),
    re.compile(r"ANT-(?:THM|LEM|PROP|COR|DEF|EX|REM|OPEN)-\d{2}-\d{2}"),
)

REQUIRED = (
    "Walfisz",
    "Ahlfors",
    "Helfgott",
    "Zeitschrift",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("text_file", type=Path)
    args = parser.parse_args()

    text = args.text_file.read_text(encoding="utf-8", errors="replace")
    failures: list[str] = []

    for token in FORBIDDEN_LITERAL:
        count = text.count(token)
        if count:
            failures.append(f"forbidden literal {token!r}: {count}")

    for pattern in FORBIDDEN_REGEX:
        matches = pattern.findall(text)
        if matches:
            failures.append(f"forbidden pattern {pattern.pattern!r}: {len(matches)}")

    for token in REQUIRED:
        if token not in text:
            failures.append(f"required publication text missing: {token!r}")

    if failures:
        print("RELEASE PDF TEXT CHECK: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("RELEASE PDF TEXT CHECK: PASS")
    print("Internal governance/build metadata absent; required scientific text present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
