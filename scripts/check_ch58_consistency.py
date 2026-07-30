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


def declared(text: str, label_pattern: str, reverse: bool = True) -> list[int]:
    """Every number bound to the given label.

    Both "8 PROVED-HERE" and "PROVED-HERE = 8" are declarations; matching
    only the first direction let "PROVED-HERE = 99" through, which a
    negative control exposed. The reverse direction is restricted to the
    SAME LINE, and is disabled entirely for totals (which are always
    written number-first, e.g. "14 identifiers = 8 + 2 + 4" -- reading
    across the newline there wrongly captured the 8).
    """
    # Inline code spans are illustrations, not declarations: documentation
    # that quotes a bad pattern like `PROVED-HERE = 99` must not trip the
    # gate on itself. Legitimate declarations put the number outside the
    # span ("8 `PROVED-HERE`"), so blanking span INTERIORS is safe.
    scannable = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), text)

    out = [norm(m) for m in re.findall(rf"({NUM}){GAP}(?:{label_pattern})", text)]
    if reverse:
        out += [norm(m) for m in
                re.findall(rf"(?:{label_pattern})[ \t]*[:=][ \t]*({NUM})", scannable)]
    return out


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

    # The declared TOTAL must equal the true total exactly. An earlier
    # version exempted any value that happened to match a category count,
    # which let a 14 -> 8 change pass; a negative control exposed that.
    for path in GOVERNANCE:
        text = read(path)
        for n in declared(text, r"(?:DRAFT / NON-CITABLE|معرِّفًا|مسجَّلة)",
                          reverse=False):
            check(f"{path.name}: declared total '{n}'", n == total,
                  f"expected {total}")

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
        # An exemption must apply to THIS occurrence only. The earlier
        # version tested "«" + phrase anywhere in the file, so one quoted
        # instance silently exempted every other live claim in the same
        # file -- a negative control exposed that.
        hit = None
        for m in single.finditer(text):
            before = text[max(0, m.start() - 3): m.start()]
            after = text[m.end(): m.end() + 3]
            quoted = "«" in before and "»" in after
            # a same-sentence historical marker, not a whole-file one
            line_start = text.rfind("\n", 0, m.start()) + 1
            line_end = text.find("\n", m.end())
            line = text[line_start: line_end if line_end != -1 else len(text)]
            historical = "تاريخي" in line or "وقت تلك" in line
            if quoted or historical:
                continue
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
