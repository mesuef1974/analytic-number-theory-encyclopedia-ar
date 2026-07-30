#!/usr/bin/env python3
"""Create a publication-facing TeX tree without mutating draft sources."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

GOVERNANCE_TOKENS = (
    "DRAFT", "REVIEWED", "APPROVED", "RELEASE-READY", "NOT-RELEASE-READY",
    "PASS-FOR-AUTHORING", "REFERENCE-AUDIT", "EVIDENCE-FIRST",
    "PRE-AUTHORING", "POST-AUTHORING", "OWNER-ADOPTED", "ACTIVE-CITABLE",
    "AUTHORED-DRAFT", "NON-CITABLE", "PROVED-HERE", "CITED-EXPLAINED",
    "CITED-FRAMEWORK", "CITED-DEFINITION", "CITED-CORE",
    "COMPACT-PROTOTYPE", "VERSION INTERNAL LIMITED", "GitHub", "worktree",
    "XeLaTeX", "Biber", "docs/", ".md",
)

EDITORIAL_STATUS_LABELS = (
    "حالة الفصل:", "حالة الفصل في الإصدار", "حالة المتن:", "حالة الحزمة:",
    "حالة النسخة:", "حالة الاعتماد:", "وضع الفصل:", "الوضع التحريري:",
    "ملاحظة تحريرية:", "تنبيه تحريري:",
)

ARABIC_GOVERNANCE_SENTENCE_PHRASES = (
    "مسودة غير قابلة للاستشهاد", "حالة المستودع الحالية", "حالة دفعة التأليف",
    "قرار المالك الصريح", "اعتماد المالك", "بعد نجاح البناء",
    "اعتمده مالك المشروع", "أذن بدمجه",
)

STANDALONE_BADGE_RE = re.compile(
    r"(?m)^\s*\\(?:resultid|provedhere|openresult)\b(?:\{[^\n]*\})?\s*$"
)
ARG_BADGE_RE = re.compile(
    r"(?m)^\s*\\(?:citedresult|deferredresult|conditionalresult)\s*\{[^\n]*\}\s*$"
)
AUTHORING_STATUS_HEADING_RE = re.compile(
    r"(?m)^\s*\\section\*?\{حالة دفعة التأليف[^}]*\}\s*$"
)
ANT_ID_RE = re.compile(
    r"ANT-(?:THM|LEM|PROP|COR|DEF|EX|REM|OPEN|COMP)-\d{2}-\d{2}"
)
CROSS_REFERENCE_RE = re.compile(
    r"\\(?:ref|pageref|autoref|eqref)\s*\{"
    r"ANT-(?:THM|LEM|PROP|COR|DEF|EX|REM|OPEN|COMP)-\d{2}-\d{2}\}"
)

PUBLICATION_ANT_ID_LABELS = {
    "ANT-THM-02-04": "نتيجة الجمع الجزئي في الفصل الثاني",
    "ANT-PROP-07-02": "قضية قطب الدالة الرئيسية في الفصل السابع",
    "ANT-PROP-10-01": "تفكيك سلسلة الفئة إلى مشتقات لوغاريتمية للشخصيات",
    "ANT-THM-09-02": "مبرهنة Wiener--Ikehara في الفصل التاسع",
    "ANT-THM-09-03": "مبرهنة الأعداد الأولية النوعية في الفصل التاسع",
}

PUBLICATION_PROSE_REPLACEMENTS = {
    (
        "مع صيغة بيرون وتقديرات تحويل المسار تقود المنطقة الكلاسيكية إلى صيغة\n"
        "فعالة لمبرهنة الأعداد الأولية. سيظهر البرهان الكامل في فصل توزيع\n"
        "الأعداد الأولية، ولن نختزل تلك السلسلة في عبارة «لا أصفار قرب \\(1\\)»."
    ): (
        "مع صيغة بيرون وتقديرات تحويل المسار تقود المنطقة الكلاسيكية إلى صيغة\n"
        "فعالة لمبرهنة الأعداد الأولية. يعرض فصل توزيع الأعداد الأولية نتيجة\n"
        "هذا المسار وحدود ما أُثبت داخليًا، من دون ادعاء اشتقاق الحد الفعّال\n"
        "الكامل ما دامت تفاصيل بيرون وتحويل المسار مؤجلة."
    )
}

RELEASE_OVERRIDES = r"""
% Publication build: suppress draft-governance badges and stable internal IDs.
\renewcommand{\resultid}[1]{}
\renewcommand{\provedhere}{}
\renewcommand{\citedresult}[1][المذكور في الشرح التالي]{}
\renewcommand{\deferredresult}[1]{}
\renewcommand{\conditionalresult}[1]{}
\renewcommand{\openresult}{}
"""


def contains_governance(text: str) -> bool:
    if any(token in text for token in GOVERNANCE_TOKENS):
        return True
    return bool(
        re.search(r"\bPR\s*\\?#?\s*\d+\b", text)
        or re.search(r"\bIssue\s*\\?#?\s*\d+\b", text)
        or re.search(r"\b(?:commit|SHA-?256|Git)\b", text)
    )


def is_editorial_status_paragraph(paragraph: str) -> bool:
    compact = re.sub(r"\s+", " ", paragraph)
    return any(label in compact for label in EDITORIAL_STATUS_LABELS)


def strip_governance_sentences(text: str) -> str:
    paragraphs = re.split(r"(\n\s*\n)", text)
    cleaned: list[str] = []
    for paragraph in paragraphs:
        current = paragraph
        if not current.strip() or re.fullmatch(r"\n\s*\n", current):
            cleaned.append(current)
            continue
        for phrase in ARABIC_GOVERNANCE_SENTENCE_PHRASES:
            if phrase not in re.sub(r"\s+", " ", current):
                continue
            pattern = re.compile(
                rf"(?s)(^|(?<=\.))\s*[^.]*{re.escape(phrase)}[^.]*\."
            )
            current = pattern.sub("", current)
        cleaned.append(current)
    return "".join(cleaned)


def strip_status_paragraphs(text: str) -> str:
    paragraphs = re.split(r"(\n\s*\n)", text)
    return "".join(
        paragraph for paragraph in paragraphs
        if not is_editorial_status_paragraph(paragraph)
    )


def strip_governance_environments(text: str) -> str:
    environment_names = ("itemize", "enumerate", "tabular", "tabularx", "longtable")
    env_re = re.compile(
        rf"\\begin\{{({'|'.join(environment_names)})\}}.*?\\end\{{\1\}}",
        re.S,
    )
    return env_re.sub(
        lambda match: "\n" if contains_governance(match.group(0)) else match.group(0),
        text,
    )


def normalize_publication_headings(text: str) -> str:
    replacements = {
        r"\section{نطاق الفصل وحالته}": r"\section{نطاق الفصل}",
        r"\section*{نطاق الفصل وحالته}": r"\section*{نطاق الفصل}",
        r"\section{نطاق الفصل وحالة المتن}": r"\section{نطاق الفصل}",
        r"\section*{نطاق الفصل وحالة المتن}": r"\section*{نطاق الفصل}",
        r"\section{نطاق الفصل وحالة الحزمة}": r"\section{نطاق الفصل}",
        r"\section*{نطاق الفصل وحالة الحزمة}": r"\section*{نطاق الفصل}",
        r"\section{نطاق الفصل ووضعه}": r"\section{نطاق الفصل}",
        r"\section*{نطاق الفصل ووضعه}": r"\section*{نطاق الفصل}",
        r"\section{نطاق الفصل وحالة النسخة}": r"\section{نطاق الفصل}",
        r"\section*{نطاق الفصل وحالة النسخة}": r"\section*{نطاق الفصل}",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return AUTHORING_STATUS_HEADING_RE.sub("", text)


def strip_governance_blocks(text: str) -> str:
    text = strip_governance_sentences(text)
    text = strip_status_paragraphs(text)
    text = strip_governance_environments(text)
    text = STANDALONE_BADGE_RE.sub("", text)
    text = ARG_BADGE_RE.sub("", text)
    text = normalize_publication_headings(text)

    blocks = re.split(r"(\n\s*\n)", text)
    cleaned: list[str] = []
    protected_markers = (
        r"\begin{theorem}", r"\begin{lemma}", r"\begin{proposition}",
        r"\begin{corollary}", r"\begin{definition}", r"\begin{proof}",
        r"\[", r"\begin{align", r"\begin{equation}",
    )
    for block in blocks:
        if not block.strip() or re.fullmatch(r"\n\s*\n", block):
            cleaned.append(block)
            continue
        protected = any(marker in block for marker in protected_markers)
        if contains_governance(block) and not protected:
            continue
        cleaned.append(block)
    return "".join(cleaned)


def replace_reader_facing_ant_ids(text: str) -> str:
    """Replace visible internal IDs with Arabic reader-facing references.

    The source commonly wraps IDs in ``\textenglish{\texttt{...}}``.  Replacing
    only the ID leaves Arabic text inside a Latin-only font and produces missing
    glyph boxes.  Replace the complete wrapper first, then handle bare IDs.
    """
    for ant_id, label in PUBLICATION_ANT_ID_LABELS.items():
        wrapped_patterns = (
            rf"\\textenglish\s*\{{\s*\\texttt\s*\{{\s*{re.escape(ant_id)}\s*\}}\s*\}}",
            rf"\\texttt\s*\{{\s*{re.escape(ant_id)}\s*\}}",
        )
        for pattern in wrapped_patterns:
            text = re.sub(pattern, lambda _match, value=label: value, text)
        text = text.replace(ant_id, label)
    return text


def strip_display_ant_ids(text: str) -> str:
    protected: list[str] = []

    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"@@ANTREF{len(protected) - 1}@@"

    text = CROSS_REFERENCE_RE.sub(protect, text)
    text = replace_reader_facing_ant_ids(text)
    text = ANT_ID_RE.sub("", text)
    for index, reference in enumerate(protected):
        text = text.replace(f"@@ANTREF{index}@@", reference)
    return text


def apply_publication_prose_replacements(text: str) -> str:
    for old, new in PUBLICATION_PROSE_REPLACEMENTS.items():
        text = text.replace(old, new)
    return text


def rewrite_generated_paths(text: str) -> str:
    text = text.replace(r"\input{manuscript/", r"\input{build/release-src/manuscript/")
    text = text.replace(r"\input{volumes/", r"\input{build/release-src/volumes/")
    text = text.replace(
        r"\addbibresource{manuscript/",
        r"\addbibresource{build/release-src/manuscript/",
    )
    return text


def inject_release_overrides(text: str) -> str:
    marker = r"\title{"
    if marker not in text:
        raise ValueError("main.tex title marker not found for release overrides")
    return text.replace(marker, RELEASE_OVERRIDES + "\n" + marker, 1)


def assert_no_empty_cross_references(text: str, relative: Path) -> None:
    empty = re.search(r"\\(?:ref|pageref|autoref|eqref)\s*\{\s*\}", text)
    if empty:
        raise ValueError(
            f"empty cross-reference generated in {relative}: {empty.group(0)}"
        )


def process_tex(source: Path, destination: Path, relative: Path) -> None:
    text = source.read_text(encoding="utf-8")
    text = strip_governance_blocks(text)
    text = strip_display_ant_ids(text)
    text = apply_publication_prose_replacements(text)
    text = rewrite_generated_paths(text)
    if relative.as_posix() == "manuscript/main.tex":
        text = inject_release_overrides(text)
    assert_no_empty_cross_references(text, relative)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("build/release-src"))
    args = parser.parse_args()

    root = args.root.resolve()
    output = (root / args.output).resolve()
    if output.exists():
        shutil.rmtree(output)

    for directory in ("manuscript", "volumes"):
        source_dir = root / directory
        for source in source_dir.rglob("*"):
            if not source.is_file():
                continue
            relative = source.relative_to(root)
            destination = output / relative
            if source.suffix == ".tex":
                process_tex(source, destination, relative)
            else:
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)

    marker = output / "RELEASE_SOURCE_GENERATED.txt"
    marker.write_text(
        "Generated publication source. Do not edit; regenerate from draft sources.\n",
        encoding="utf-8",
    )
    print(f"Prepared release source at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
