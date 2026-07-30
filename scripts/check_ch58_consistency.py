"""Cross-file consistency gate for chapter 58's governance documents.

Why this exists: across seven owner review rounds on chapter 58, the
mathematics held up but the same failure recurred almost every time -- a
correction applied in one file and not propagated to the others that carry
the same fact. Attention alone did not prevent it, so it is checked here.

What it enforces:
  1. The result classification (8 PROVED-HERE + 2 METHODOLOGICAL-PRINCIPLE
     + 4 CITED = 14) is stated identically wherever it appears, and matches
     the registry's actual tables.
  2. The registry's ID tables really contain 8 / 2 / 4 entries.
  3. The post-authoring round count agrees across every file that states it.
  4. No file still calls the norm equality B_N = Q_N a numerical result --
     it is proved generally in ANT-PROP-58-07.
  5. No file still lists the fourth confirmation as outstanding.
  6. Every ANT-*-58-* id used in the chapter appears in the draft registry,
     and vice versa (no orphans in either direction).

Run:  python scripts/check_ch58_consistency.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CHAPTER = (ROOT / "volumes" / "volume-57-zeros-moments-modern-statistics"
           / "chapters" / "chapter-58-hilbert-inequality-large-values.tex")

REGISTRY = DOCS / "RESULTS_REGISTRY_CHAPTER_58_DRAFT.md"
GOVERNANCE = [
    DOCS / "CHAPTER_58_SCOPE_2026-07-29.md",
    DOCS / "CHAPTER_58_PROOF_MAP_2026-07-29.md",
    DOCS / "CHAPTER_58_EVIDENCE_LEDGER_2026-07-29.md",
    DOCS / "CHAPTER_58_PRE_AUTHORING_AUDIT_2026-07-29.md",
    DOCS / "CHAPTER_58_POST_AUTHORING_REVIEW_2026-07-30.md",
    REGISTRY,
]

EXPECTED_PROVED, EXPECTED_PRINCIPLE, EXPECTED_CITED = 8, 2, 4
EXPECTED_TOTAL = EXPECTED_PROVED + EXPECTED_PRINCIPLE + EXPECTED_CITED
EXPECTED_ROUNDS = 7

failures: list[str] = []


def read(path: Path) -> str:
    if not path.exists():
        failures.append(f"missing file: {path.name}")
        return ""
    return path.read_text(encoding="utf-8")


def check(label: str, ok: bool, detail: str = "") -> None:
    print(f"  {'PASS' if ok else 'FAIL'}  {label}" + (f"   {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(f"{label} {detail}".strip())


def main() -> int:
    print("chapter 58 cross-file consistency\n")
    reg = read(REGISTRY)

    # 1/2. registry tables must actually contain the claimed split
    proved = len(re.findall(r"\|\s*`PROVED-HERE`\s*\|", reg))
    cited = len(re.findall(r"`DRAFT / CITED`", reg))
    principle = len(re.findall(r"\|\s*مبدأ منهجي[^|]*\|", reg))
    ids = sorted(set(re.findall(r"ANT-(?:PRIN|LEM|PROP|THM)-58-\d+", reg)))

    print("registry tables:")
    check(f"PROVED-HERE rows == {EXPECTED_PROVED}", proved == EXPECTED_PROVED, f"found {proved}")
    check(f"METHODOLOGICAL-PRINCIPLE rows == {EXPECTED_PRINCIPLE}",
          principle == EXPECTED_PRINCIPLE, f"found {principle}")
    check(f"CITED rows == {EXPECTED_CITED}", cited == EXPECTED_CITED, f"found {cited}")
    check(f"distinct ids == {EXPECTED_TOTAL}", len(ids) == EXPECTED_TOTAL, f"found {len(ids)}")

    # 3. the stated split must be identical wherever it is written.
    # Allow markdown emphasis/backticks between the number and the label,
    # so "**10** `PROVED-HERE`" is caught as readily as "10 PROVED-HERE".
    GAP = r"[\s*`]{0,6}"
    stale_split = re.compile(rf"(?<!\d)10{GAP}(?:مبرهَنة|PROVED-HERE)")
    good_split = re.compile(rf"(?<!\d)8{GAP}(?:PROVED-HERE|`PROVED-HERE`)")
    print("\nstated split, across files:")
    for path in GOVERNANCE:
        text = read(path)
        if "PROVED-HERE" not in text:
            continue
        stale = stale_split.search(text)
        check(f"{path.name}: no superseded 10+N split", stale is None,
              f"found {stale.group(0)!r}" if stale else "")
        # where a split is stated at all, it must be the 8 / 2 / 4 one
        if "METHODOLOGICAL-PRINCIPLE" in text:
            check(f"{path.name}: states the 8+2+4 split",
                  bool(good_split.search(text)))

    # 3b. principle 11 must not sit in the PROVED-HERE list
    pm = read(DOCS / "CHAPTER_58_PROOF_MAP_2026-07-29.md")
    proved_line = re.search(r"\*\*PROVED-HERE[^:]*:\*\*([^\n]*(?:\n(?!-)[^\n]*)*)", pm)
    check("PROOF_MAP: principle 11 not listed under PROVED-HERE",
          proved_line is not None and "١١" not in proved_line.group(1),
          "result 11 found in the PROVED-HERE enumeration")

    # 4. round count agreement
    print("\npost-authoring round count:")
    for path in GOVERNANCE:
        text = read(path)
        for m in re.finditer(r"(\d+)\s*(?:ROUNDS BY OWNER|جولات مُنجَزة)", text):
            n = int(m.group(1))
            check(f"{path.name}: rounds == {EXPECTED_ROUNDS - 1} done",
                  n == EXPECTED_ROUNDS - 1, f"found {n}")

    # 5. the norm equality must never be presented as numerical
    print("\nnorm equality B_N = Q_N presented as proved, not numerical:")
    bad_phrase = re.compile(r"تحقَّق عدديًّا أن المعيارين")
    for path in GOVERNANCE:
        text = read(path)
        check(f"{path.name}: not attributed to numerics",
              bad_phrase.search(text) is None)

    # 6. fourth confirmation must not still be listed as outstanding
    print("\nfourth confirmation not still outstanding:")
    for path in GOVERNANCE:
        text = read(path)
        bad = re.search(r"تأكيد (?:مستقل )?رابع[^\n]{0,40}\(لم يُجرَ\)", text)
        check(f"{path.name}: not demanded as pending", bad is None)

    # 7. id parity between chapter and registry
    print("\nid parity, chapter vs registry:")
    chap = read(CHAPTER)
    chap_ids = sorted(set(re.findall(r"\\resultid\{(ANT-[A-Z]+-58-\d+)\}", chap)))
    only_chap = [i for i in chap_ids if i not in ids]
    only_reg = [i for i in ids if i not in chap_ids]
    check("every chapter id is registered", not only_chap, f"unregistered: {only_chap}")
    check("every registered id is used", not only_reg, f"orphaned: {only_reg}")

    print(f"\n{len(failures)} failed")
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(f"  - {f}")
    print(f"\nVERDICT: {'PASS' if not failures else 'FAIL'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
