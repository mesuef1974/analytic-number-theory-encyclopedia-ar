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
  7. Review-round headings in the minutes are unique, consecutive 1..N, and
     N agrees with the declared round count.

Scope note (after round 11, by owner direction): this gate checks STRUCTURAL
facts only -- counted rows, canonical numeric fields, id parity, heading
sequences. It deliberately does NOT try to judge free Arabic prose.

An earlier version did chase prose: a regex meant to catch "the only proved
result" while eight exist. Every round widened it and every round it missed
the next natural rephrasing ("the sole proved result", "one proved result").
That is an endless road -- a regex cannot carry the semantics of a language.
What replaced it is the structural fact underneath the claim: THEOREMS and
PROVED-HERE are numeric fields, counted from the registry's own tables and
checked wherever they are declared.

The honest cost: a sentence of running prose that contradicts those numbers
is no longer caught by machine. That is human review's job now, and it is
written here so no one mistakes a PASS for a verdict on the prose.

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

# Explicit, auditable opt-out for lines that quote a pattern as an example
# rather than declaring it. Written on the line itself.
GATE_IGNORE = "<!-- gate-ignore -->"

ARABIC_INDIC = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
NUM = r"[0-9٠-٩]{1,3}"
# markdown emphasis / backticks / spaces may sit between number and label
GAP = r"[\s*`ً-ٟ]{0,8}"

# Fields that must EXIST, each anchored to the canonical line that carries
# it. "Somewhere in the file" is not enough: a prose mention elsewhere kept
# standing in for a deleted header field, so the header line itself is what
# is required here.
D = r"[0-9٠-٩]"
REQUIRED_FIELDS = {
    "CHAPTER_58_SCOPE_2026-07-29.md": {
        "THEOREMS": rf"^THEOREMS\s+=\s*{D}",
        "PROVED-HERE": rf"^PROVED-HERE\s+=\s*{D}",
    },
    "CHAPTER_58_PROOF_MAP_2026-07-29.md": {
        "THEOREMS": rf"^THEOREMS\s*=\s*{D}",
        "PROVED-HERE": rf"^PROVED-HERE\s*=\s*{D}",
    },
    "RESULTS_REGISTRY_CHAPTER_58_DRAFT.md": {
        "THEOREMS": rf"^THEOREMS\s+=\s*{D}",
        "PROVED-HERE": rf"^\s*=\s*{D}+\s+PROVED-HERE",
        "METHODOLOGICAL-PRINCIPLE": rf"^\s*\+\s*{D}+\s+METHODOLOGICAL-PRINCIPLE",
        "CITED": rf"^\s*\+\s*{D}+\s+CITED",
        "ROUNDS": rf"^POST-AUTHORING-REVIEW\s+=\s*{D}+\s+ROUNDS BY OWNER",
    },
    "CHAPTER_58_POST_AUTHORING_REVIEW_2026-07-30.md": {
        "ROUNDS": rf"^ROUNDS\s+=\s*{D}",
    },
    "CHAPTER_58_PRE_AUTHORING_AUDIT_2026-07-29.md": {
        "ROUNDS": rf"^POST-AUTHORING-REVIEW\s+=\s*{D}",
    },
}

# Review rounds are written as Arabic ordinals in the minutes' headings.
ORDINALS = {w: i + 1 for i, w in enumerate([
    "الأولى", "الثانية", "الثالثة", "الرابعة", "الخامسة", "السادسة",
    "السابعة", "الثامنة", "التاسعة", "العاشرة", "الحادية عشرة",
    "الثانية عشرة", "الثالثة عشرة", "الرابعة عشرة", "الخامسة عشرة",
])}

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
    # Backticks are stripped UNIFORMLY before extraction, so both
    # "8 `PROVED-HERE`" and "`PROVED-HERE` = 99" are read the same way.
    # The earlier version blanked span interiors for the reverse direction
    # only, which made parsing asymmetric: "`PROVED-HERE` = 99" slipped
    # through while "`99 PROVED-HERE`" was rejected.
    #
    # Genuine illustrations opt out explicitly, per line, with a marker.
    # An opt-out you have to write is auditable; one inferred from
    # formatting is not.
    lines = [ln for ln in text.split("\n") if GATE_IGNORE not in ln]
    scannable = "\n".join(lines).replace("`", "")

    out = [norm(m) for m in re.findall(rf"({NUM}){GAP}(?:{label_pattern})", scannable)]
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
    # How many of those results are theorems is the structural fact that the
    # "only one result" prose kept getting wrong. Counted, not asserted.
    truth["THEOREMS"] = len({i for i in ids if "-THM-" in i})

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
        "THEOREMS": r"`?THEOREMS`?",
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
        r"\*\*(ثلاث|أربع|خمس|ست|سبع|ثمان|تسع|عشر|إحدى عشرة|اثنتا عشرة)"
        r"\s+جول(?:ات|ة)\*\*",
    ]
    WORDNUM = {"ثلاث": 3, "أربع": 4, "خمس": 5, "ست": 6, "سبع": 7, "ثمان": 8,
               "تسع": 9, "عشر": 10, "إحدى عشرة": 11, "اثنتا عشرة": 12}
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

    # --- 3b. the canonical fields must EXIST where they belong ---
    # Checking that declarations agree says nothing about a declaration that
    # is gone: deleting "THEOREMS = 1" from SCOPE, or "ROUNDS = 11" from the
    # minutes header, left nothing to disagree with and passed. Absence is
    # the cheapest way to lose a fact, so presence is required by name.
    print("\ncanonical fields present where required:")
    for name, fields in REQUIRED_FIELDS.items():
        text = read(DOCS / name)
        for field, anchor in fields.items():
            check(f"{name}: declares {field} on its canonical line",
                  re.search(anchor, text, re.M) is not None, "field absent")

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

    # --- 7. round headings: unique, consecutive, as many as declared ---
    # Comparing declared totals says nothing about the minutes themselves:
    # renaming "الجولة العاشرة" to "الجولة التاسعة" left every total intact
    # and passed. A sequence is a structural object, so check it as one.
    print("\nreview-round headings form 1..N:")
    minutes = read(DOCS / "CHAPTER_58_POST_AUTHORING_REVIEW_2026-07-30.md")
    heads = [h.strip() for h in
             re.findall(r"^##\s+الجولة\s+([^\n—–]+?)\s*[—–]", minutes, re.M)]
    unknown = [h for h in heads if h not in ORDINALS]
    check("every round heading uses a known ordinal", not unknown,
          f"unrecognised: {unknown}")
    nums = [ORDINALS[h] for h in heads if h in ORDINALS]
    check("round headings are unique and consecutive from 1",
          nums == list(range(1, len(nums) + 1)), f"found {nums}")
    if all_vals and nums:
        check("heading count equals the declared round count",
              len(nums) == all_vals[-1],
              f"{len(nums)} headings vs declared {all_vals[-1]}")

    print("\nfree prose: NOT CHECKED — human review (see module docstring)")

    print(f"\n{len(failures)} failed")
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(f"  - {f}")
    print(f"\nVERDICT: {'PASS' if not failures else 'FAIL'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
