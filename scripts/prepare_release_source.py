#!/usr/bin/env python3
"""Create a publication-facing TeX tree without mutating draft sources.

The draft manuscript remains the canonical auditable source. This script copies
its TeX inputs to a generated tree, removes governance-only material, and
rewrites input/resource paths so XeLaTeX compiles the generated copy.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

GOVERNANCE_TOKENS = (
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
    "PROVED-HERE",
    "CITED-EXPLAINED",
    "CITED-FRAMEWORK",
    "CITED-DEFINITION",
    "CITED-CORE",
    "COMPACT-PROTOTYPE",
    "VERSION INTERNAL LIMITED",
    "GitHub",
    "worktree",
    "XeLaTeX",
    "Biber",
    "docs/",
    ".md",
)

STANDALONE_BADGE_RE = re.compile(
    r"(?m)^\s*\\(?:resultid|provedhere|openresult)\b(?:\{[^\n]*\})?\s*$"
)
ARG_BADGE_RE = re.compile(
    r"(?m)^\s*\\(?:citedresult|deferredresult|conditionalresult)\s*\{[^\n]*\}\s*$"
)
INTERNAL_RESULT_ID_RE = re.compile(
    r"ANT-(?:THM|LEM|PROP|COR|DEF|EX|REM|OPEN)-\d{2}-\d{2}"
)

RELEASE_OVERRIDES = r"""
% Publication build: suppress draft-governance badges and stable internal IDs.
\renewcommand{\resultid}[1]{}
\renewcommand{\provedhere}{}
% Keep the optional-argument signature used by manuscript/main.tex. Changing it
% to a mandatory argument makes bare \citedresult calls consume the next token.
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


def strip_status_lines(text: str) -> str:
    """Remove only complete status lines; never span TeX paragraphs or math."""
    kept: list[str] = []
    for line in text.splitlines(keepends=True):
        if "حالة الفصل:" in line and contains_governance(line):
            continue
        kept.append(line)
    return "".join(kept)


def strip_governance_environments(text: str) -> str:
    """Remove list/table environments only when their contents are governance."""
    environment_names = (
        "itemize",
        "enumerate",
        "tabular",
        "tabularx",
        "longtable",
    )
    env_re = re.compile(
        rf"\\begin\{{({'|'.join(environment_names)})\}}.*?\\end\{{\1\}}",
        re.S,
    )
    return env_re.sub(
        lambda match: "\n" if contains_governance(match.group(0)) else match.group(0),
        text,
    )


def strip_governance_blocks(text: str) -> str:
    text = strip_status_lines(text)
    text = strip_governance_environments(text)

    text = STANDALONE_BADGE_RE.sub("", text)
    text = ARG_BADGE_RE.sub("", text)
    text = text.replace(r"\section{نطاق الفصل وحالته}", r"\section{نطاق الفصل}")

    # Internal stable identifiers are useful in the auditable draft but are not
    # publication prose. Remove only the identifier token and retain the entire
    # surrounding scientific sentence, theorem statement, or cross-reference.
    text = INTERNAL_RESULT_ID_RE.sub("", text)

    # TeX prose is paragraph-delimited. Remove governance paragraphs while
    # retaining mathematical/theorem blocks and ordinary scientific prose.
    blocks = re.split(r"(\n\s*\n)", text)
    cleaned: list[str] = []
    for block in blocks:
        if not block.strip() or re.fullmatch(r"\n\s*\n", block):
            cleaned.append(block)
            continue
        protected = any(
            marker in block
            for marker in (
                r"\begin{theorem}", r"\begin{lemma}", r"\begin{proposition}",
                r"\begin{corollary}", r"\begin{definition}", r"\begin{proof}",
                r"\[", r"\begin{align", r"\begin{equation",
            )
        )
        if contains_governance(block) and not protected:
            continue
        cleaned.append(block)
    return "".join(cleaned)


def rewrite_generated_paths(text: str) -> str:
    text = text.replace(r"\input{manuscript/", r"\input{build/release-src/manuscript/")
    text = text.replace(r"\input{volumes/", r"\input{build/release-src/volumes/")
    text = text.replace(r"\addbibresource{manuscript/", r"\addbibresource{build/release-src/manuscript/")
    return text


def inject_release_overrides(text: str) -> str:
    marker = r"\title{"
    if marker not in text:
        raise ValueError("main.tex title marker not found for release overrides")
    return text.replace(marker, RELEASE_OVERRIDES + "\n" + marker, 1)


def process_tex(source: Path, destination: Path, relative: Path) -> None:
    text = source.read_text(encoding="utf-8")
    text = strip_governance_blocks(text)
    text = rewrite_generated_paths(text)
    if relative.as_posix() == "manuscript/main.tex":
        text = inject_release_overrides(text)
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
