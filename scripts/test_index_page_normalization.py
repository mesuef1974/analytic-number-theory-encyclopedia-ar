"""Regression test for index page-field normalization (P2-05 / PUB-P0-001).

Background: polyglossia writes every Arabic-document page number into the
.idx files wrapped in a private direction macro, e.g. ``\\@ensure@LTR {٤}``.
That macro is not expandable in a hand-built .ind file printed outside
polyglossia's own page-number machinery, so it leaked into the PDF as
literal text on EVERY index entry across all 26 chapters. The owner caught
it visually; no automated text check had flagged it.

This test pins the normalizer's behaviour so the bug cannot return.

Two independent branches fixed this bug differently. The first attempt on
the P2 branch stripped any single enclosing macro, which handled today's
data but silently failed on the ``\\protect``-ed and nested forms and would
have discarded a legitimate ``\\hyperpage{...}``. The implementation from
PR #63 (branch agent/publication-preview-remediation-v0.30.1) is a
whitelist that loops and validates instead, and is what is now in
build_named_indexes.py. The cases below are exactly the ones that
distinguish the two, so the weaker version cannot be reintroduced.

Run:  python scripts/test_index_page_normalization.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_named_indexes import SAFE_PAGE_RE, unwrap_page  # noqa: E402

# (input, expected output, expected SAFE_PAGE_RE verdict, note)
CASES: list[tuple[str, str, bool, str]] = [
    # the exact form the real .idx files contain today (note the space,
    # and Arabic-Indic digits)
    ("\\@ensure@LTR {٤}", "٤", True, "real .idx form, Arabic-Indic digit"),
    ("\\@ensure@LTR{198}", "198", True, "no space, Western digits"),
    # forms the earlier, weaker implementation got WRONG
    ("\\protect\\@ensure@LTR{198}", "198", True, "protected (LaTeX convention)"),
    ("\\protect \\protect \\@ensure@LTR{198}", "198", True, "repeated \\protect"),
    ("\\@ensure@LTR{\\@ensure@LTR{198}}", "198", True, "nested wrapper"),
    # other direction-wrapper spellings covered by the whitelist
    ("\\textLR{198}", "198", True, "textLR spelling"),
    ("\\LR{198}", "198", True, "LR spelling"),
    ("\\ensureLTR{198}", "198", True, "ensureLTR spelling"),
    # already plain: must pass through untouched
    ("198", "198", True, "plain Western page"),
    ("١٢", "١٢", True, "plain Arabic-Indic page"),
    ("iv", "iv", True, "roman front-matter page"),
    ("\\@ensure@LTR{iv}", "iv", True, "wrapped roman page"),
    # NOT direction wrappers: must be left alone, not silently discarded.
    # The weaker implementation stripped these, which would have thrown away
    # a real page macro or formatting.
    ("\\hyperpage{198}", "\\hyperpage{198}", False, "hyperref page macro preserved"),
    ("\\textbf{198}", "\\textbf{198}", False, "formatting macro preserved"),
]


def main() -> int:
    failures: list[str] = []
    print("index page-field normalization")
    for raw, expected, expect_safe, note in CASES:
        got = unwrap_page(raw)
        safe = bool(SAFE_PAGE_RE.match(got))
        ok = got == expected and safe == expect_safe
        status = "PASS" if ok else "FAIL"
        print(f"  {status}  {raw!r} -> {got!r} (safe={safe})  [{note}]")
        if not ok:
            failures.append(
                f"{raw!r}: expected {expected!r} safe={expect_safe}, "
                f"got {got!r} safe={safe}"
            )

    # No output of the normalizer may still contain the leaking macro name.
    leak = [raw for raw, *_ in CASES
            if "ensure@LTR" in unwrap_page(raw) and "hyperpage" not in raw
            and "textbf" not in raw]
    if leak:
        failures.append(f"macro name still leaks for: {leak}")
        print(f"  FAIL  macro name leaks through for {leak}")
    else:
        print("  PASS  no direction-macro name survives normalization")

    print(f"\n{len(CASES) + 1} checks, {len(failures)} failed")
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(f"  - {f}")
    print(f"\nVERDICT: {'PASS' if not failures else 'FAIL'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
