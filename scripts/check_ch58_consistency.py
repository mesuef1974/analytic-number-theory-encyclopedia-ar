"""Cross-file consistency gate for chapter 58's governance documents.

Why this exists: across eight owner review rounds on chapter 58, the
mathematics held up but the same failure recurred almost every time -- a
correction applied in one file and not propagated to the others carrying
the same fact. Attention alone did not prevent it, so it is checked here.

Design note (after round 8): the first version of this gate pattern-matched
the specific wrong values it had already seen ("10" where 8 was meant). That
catches yesterday's bug and nothing else -- negative controls showed it
missed 2->3, 4->5 and a 6->5 header drift. This version instead DERIVES the
ground truth by counting the registry's own tables, then extracts every
number declared anywhere near a label and compares it. Any drift in any
direction fails, including values never seen before.

Checks:
  1. Ground truth from the registry tables: how many PROVED-HERE,
     METHODOLOGICAL-PRINCIPLE and CITED rows actually exist.
  2. Every declared count of those three categories, in every governance
     file, matches the ground truth. Arabic-Indic digits are normalised.
  3. Every declared post-authoring round count agrees with every other.
  4. No file presents B_N = Q_N as a numerical result (it is proved).
  5. No file still lists the fourth confirmation as outstanding.
  6. Chapter ids and registry ids match in both directions.
  7. No file claims a single proved result while more than one exists.

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

ARABIC_INDIC = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
NUM = r"[0-9٠-٩]{1,3}"
# markdown emphasis / backticks / spaces may sit between number and label
GAP = r"[\s*`ً-ٟ]{0,8}"

failures: list[str] = []


def norm(s: str) -> int:
    return int(s.translate(ARABIC_INDIC))


def read(path: Path) -> str:
    if not path.exists():
        failures.append(f"missing file: {path.name}")
        return ""
    return path.read_text(encoding="utf-8")


def check(label: str, ok: bool, detail: str = "") -> None:
    print(f"  {'PASS' if ok else 'FAIL'}  {label}" + (f"   {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(f"{label} {detail}".strip())


def declared(text: str, label_pattern: str) -> list[int]:
    """Every number written immediately before the given label."""
    return [norm(m) for m in re.findall(rf"({NUM}){GAP}(?:{label_pattern})", text)]


def main() -> int:
    print("chapter 58 cross-file consistency\n")
    reg = read(REGISTRY)

    # --- 1. ground truth, counted from the registry's own tables ---
    truth = {
        "PROVED-HERE": len(re.findall(r"\|\s*`PROVED-HERE`\s*\|", reg)),
        "METHODOLOGICAL-PRINCIPLE": len(re.findall(r"\|\s*مبدأ منهجي[^|]*\|", reg)),
        "CITED": len(re.findall(r"`DRAFT / CITED`", reg)),
    }
    ids = sorted(set(re.findall(r"ANT-(?:PRIN|LEM|PROP|THM)-58-\d+", reg)))
    total = sum(truth.values())

    print("ground truth from registry tables:")
    for k, v in truth.items():
        print(f"    {k}: {v}")
    check(f"category counts sum to the id count ({len(ids)})", total == len(ids),
          f"sum={total} ids={len(ids)}")

    # --- 2. every declared count must match ground truth ---
    print("\ndeclared counts vs ground truth:")
    label_for = {
        "PROVED-HERE": r"`?PROVED-HERE`?",
        "METHODOLOGICAL-PRINCIPLE": r"`?METHODOLOGICAL-PRINCIPLE`?",
        "CITED": r"`?CITED`?",
    }
    for path in GOVERNANCE:
        text = read(path)
        for key, pat in label_for.items():
            for n in declared(text, pat):
                check(f"{path.name}: '{n} {key}'", n == truth[key],
                      f"expected {truth[key]}")

    # total, wherever a total is declared
    for path in GOVERNANCE:
        text = read(path)
        for n in declared(text, r"(?:DRAFT / NON-CITABLE|معرِّفًا|مسجَّلة)"):
            if n in (total, truth["PROVED-HERE"], truth["CITED"],
                     truth["METHODOLOGICAL-PRINCIPLE"]):
                continue
            check(f"{path.name}: stray total '{n}'", False, f"expected {total}")

    # --- 3. post-authoring round counts must agree everywhere ---
    # Only DECLARATIONS count: a number bound to an explicit post-authoring
    # round label. Prose mentions and historical quotations of past wrong
    # values are not declarations and must not be compared.
    print("\npost-authoring round counts agree:")
    decl_patterns = [
        rf"POST-AUTHORING-REVIEW\s*=\s*({NUM})",
        rf"ROUNDS\s*=\s*({NUM})",
        rf"({NUM}){GAP}ROUNDS BY OWNER",
        rf"({NUM}){GAP}جولات مُنجَزة",
        r"\*\*(سبع|ست|خمس|أربع|ثلاث)\s+جولات\*\*",
    ]
    WORDNUM = {"ثلاث": 3, "أربع": 4, "خمس": 5, "ست": 6, "سبع": 7, "ثمان": 8}
    rounds: dict[str, list[int]] = {}
    for path in GOVERNANCE:
        text = read(path)
        vals: list[int] = []
        for pat in decl_patterns:
            for m in re.findall(pat, text):
                vals.append(WORDNUM[m] if m in WORDNUM else norm(m))
        if vals:
            rounds[path.name] = vals
    all_vals = sorted({v for vs in rounds.values() for v in vs})
    check("a single post-authoring round count is declared everywhere",
          len(all_vals) <= 1,
          f"found {all_vals} in {rounds}")

    # --- 4. norm equality must never be called numerical ---
    print("\nB_N = Q_N presented as proved, not numerical:")
    bad = re.compile(r"تحقَّق عدديًّا أن المعيار")
    for path in GOVERNANCE:
        check(f"{path.name}: not attributed to numerics", bad.search(read(path)) is None)

    # --- 5. fourth confirmation not still pending ---
    print("\nfourth confirmation not still outstanding:")
    pend = re.compile(r"تأكيد (?:مستقل )?رابع[^\n]{0,40}\(لم يُجرَ\)")
    for path in GOVERNANCE:
        check(f"{path.name}: not demanded as pending", pend.search(read(path)) is None)

    # --- 6. id parity ---
    print("\nid parity, chapter vs registry:")
    chap = read(CHAPTER)
    chap_ids = sorted(set(re.findall(r"\\resultid\{(ANT-[A-Z]+-58-\d+)\}", chap)))
    check("every chapter id is registered",
          not [i for i in chap_ids if i not in ids],
          f"unregistered: {[i for i in chap_ids if i not in ids]}")
    check("every registered id is used",
          not [i for i in ids if i not in chap_ids],
          f"orphaned: {[i for i in ids if i not in chap_ids]}")

    # --- 7. no 'only one proved result' claim while several exist ---
    print("\nno 'single proved result' claim:")
    single = re.compile(r"النتيجة الوحيدة (?:المبرهَنة|التي تُثبَت)"
                        r"|نتيجةً واحدة من الصفر")
    for path in [CHAPTER, *GOVERNANCE]:
        text = read(path)
        hit = None
        for m in single.finditer(text):
            window = text[max(0, m.start() - 200): m.end() + 200]
            quoted = (text[max(0, m.start() - 2): m.start()].strip().endswith("«")
                      or "«" + m.group(0) in text)
            historical = "تاريخي" in window or "وقت تلك" in window
            if quoted or historical:
                continue  # a quotation of a past finding, not a live claim
            hit = m
            break
        check(f"{path.name}: no unqualified single-result claim",
              hit is None or truth["PROVED-HERE"] <= 1,
              f"found {hit.group(0)!r}" if hit else "")

    print(f"\n{len(failures)} failed")
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(f"  - {f}")
    print(f"\nVERDICT: {'PASS' if not failures else 'FAIL'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
