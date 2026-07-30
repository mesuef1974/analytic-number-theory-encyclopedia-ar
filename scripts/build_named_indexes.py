#!/usr/bin/env python3
r"""Build UTF-8-safe named LaTeX indexes from imakeidx .idx files.

The parser reads each .idx file as a TeX stream rather than assuming that every
``\indexentry`` occupies exactly one physical line. It also resolves the named
index files across the layouts produced by imakeidx/latexmk, including
``people.idx`` and ``main.people.idx`` in either the working directory or the
LaTeX output directory.

Page fields are normalized by ``unwrap_page``; see
``scripts/test_index_page_normalization.py`` for the behaviour that is pinned.
"""

from __future__ import annotations

import argparse
import re
import traceback
import unicodedata
from dataclasses import dataclass
from pathlib import Path

EXPECTED = ("people", "theorems", "symbols")
PREFIX = r"\indexentry"

# Polyglossia may protect page numbers written to auxiliary files with internal
# direction wrappers such as ``\@ensure@LTR{...}`` or
# ``\protect\@ensure@LTR{...}``. These internal commands are not stable
# publication content: when copied verbatim into a generated .ind file, the
# ``@`` token can lose its command-name catcode and leak visibly as
# ``ensure@LTR``. The index generator owns the page field, so normalize these
# wrappers before sorting or rendering.
DIRECTION_WRAPPER_RE = re.compile(
    r"^\s*(?:\\protect\s*)*\\(?:@ensure@LTR|ensure@LTR|ensureLTR|textLR|LR)\s*\{(.*)\}\s*$",
    re.S,
)
SAFE_PAGE_RE = re.compile(r"^[0-9٠-٩۰-۹ivxlcdmIVXLCDM-]+$")


@dataclass(frozen=True)
class Entry:
    raw: str
    page: str

    @property
    def display(self) -> str:
        return self.raw.split("@", 1)[-1]

    @property
    def sort_key(self) -> str:
        key = self.raw.split("@", 1)[0]
        return unicodedata.normalize("NFKC", key).casefold()


def skip_space_and_comments(text: str, start: int) -> int:
    cursor = start
    while cursor < len(text):
        if text[cursor].isspace():
            cursor += 1
            continue
        if text[cursor] == "%":
            newline = text.find("\n", cursor)
            return len(text) if newline < 0 else skip_space_and_comments(text, newline + 1)
        break
    return cursor


def read_group(text: str, start: int) -> tuple[str, int]:
    cursor = skip_space_and_comments(text, start)
    if cursor >= len(text) or text[cursor] != "{":
        excerpt = text[cursor : cursor + 80].replace("\n", r"\n")
        raise ValueError(f"expected '{{' at offset {cursor}; next={excerpt!r}")

    depth = 1
    index = cursor + 1
    chars: list[str] = []
    while index < len(text):
        char = text[index]

        if char == "\\" and index + 1 < len(text) and text[index + 1] in "{}\\%":
            chars.append(char)
            chars.append(text[index + 1])
            index += 2
            continue

        if char == "{":
            depth += 1
            chars.append(char)
            index += 1
            continue
        if char == "}":
            depth -= 1
            if depth == 0:
                return "".join(chars), index + 1
            if depth < 0:
                raise ValueError(f"unbalanced closing brace at offset {index}")
            chars.append(char)
            index += 1
            continue

        chars.append(char)
        index += 1

    raise ValueError("unterminated brace group")


def normalize_page(page: str) -> str:
    """Return a safe printable page token without auxiliary direction macros."""
    normalized = page.strip()
    previous = None
    while normalized != previous:
        previous = normalized
        match = DIRECTION_WRAPPER_RE.fullmatch(normalized)
        if match:
            normalized = match.group(1).strip()

    if not normalized:
        raise ValueError(f"empty index page field after normalization: {page!r}")
    if "ensure@LTR" in normalized or "ensureLTR" in normalized:
        raise ValueError(f"unremoved direction wrapper in index page field: {page!r}")
    if not SAFE_PAGE_RE.fullmatch(normalized):
        raise ValueError(f"unsafe TeX or unexpected content in index page field: {page!r}")
    return normalized


def parse_idx(path: Path) -> list[Entry]:
    text = path.read_text(encoding="utf-8-sig")
    entries: list[Entry] = []
    cursor = 0

    while True:
        start = text.find(PREFIX, cursor)
        if start < 0:
            break
        try:
            raw, after_raw = read_group(text, start + len(PREFIX))
            page, after_page = read_group(text, after_raw)
        except ValueError as exc:
            line = text.count("\n", 0, start) + 1
            raise ValueError(f"{path}:{line}: {exc}") from exc
        entries.append(Entry(raw.strip(), normalize_page(page)))
        cursor = after_page

    prefix_count = text.count(PREFIX)
    if len(entries) != prefix_count:
        raise ValueError(
            f"{path}: parsed {len(entries)} entries but found {prefix_count} {PREFIX!r} markers"
        )
    return entries


def resolve_idx(name: str, input_directory: Path, output_directory: Path) -> Path:
    candidates = [
        input_directory / f"{name}.idx",
        input_directory / f"main.{name}.idx",
        output_directory / f"{name}.idx",
        output_directory / f"main.{name}.idx",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate

    matches: list[Path] = []
    for root in {input_directory.resolve(), output_directory.resolve()}:
        if root.is_dir():
            matches.extend(root.rglob(f"{name}.idx"))
            matches.extend(root.rglob(f"main.{name}.idx"))
    unique = sorted({path.resolve() for path in matches})
    if len(unique) == 1:
        return unique[0]
    if len(unique) > 1:
        choices = ", ".join(str(path) for path in unique)
        raise FileNotFoundError(f"Ambiguous named index input for {name}: {choices}")

    available = sorted(
        {
            *input_directory.glob("*.idx"),
            *output_directory.glob("*.idx"),
        }
    )
    listing = ", ".join(str(path) for path in available) or "none"
    raise FileNotFoundError(
        f"Missing named index input for {name}; searched working/output layouts; "
        f"available .idx files: {listing}"
    )


# Direction wrappers polyglossia may put around a page number written to an
# auxiliary file. Only these are stripped -- deliberately a whitelist, not a
# generic "strip any macro" rule, so that a legitimate page macro such as
# \hyperpage{...} or a formatting macro is never silently discarded.
# \protect is allowed (and may repeat) because LaTeX conventionally protects
# fragile commands on their way into .aux/.idx files.
DIRECTION_WRAPPER_RE = re.compile(
    r"^\s*(?:\\protect\s*)*\\(?:@ensure@LTR|ensure@LTR|ensureLTR|textLR|LR)\s*\{(.*)\}\s*$",
    re.DOTALL,
)

# A page field we are willing to print. Covers Western and Arabic-Indic and
# Persian digits, Roman numerals (front matter), and ranges.
SAFE_PAGE_RE = re.compile(r"^[0-9٠-٩۰-۹ivxlcdmIVXLCDM\-]+$")


def unwrap_page(page: str) -> str:
    r"""Return a printable page field, stripped of direction wrappers.

    Polyglossia wraps every Arabic-document page number written to .idx files
    in a private direction-forcing macro (e.g. ``\@ensure@LTR {٤}``). That
    macro is not expandable once copied verbatim into a hand-built .ind file
    printed outside polyglossia's own page-number machinery: outside
    \makeatletter, "@" is a plain printable character, so the whole macro
    name leaks into the PDF as literal text on every single index entry.
    Since plain page numbers already render correctly elsewhere in this
    document without this wrapper, unwrap it and keep only the number.

    Strips repeatedly, so nested and \protect-ed forms are handled. Anything
    that is not a recognised direction wrapper is returned untouched rather
    than mangled; callers can use ``SAFE_PAGE_RE`` to detect a page field
    that still needs attention.
    """
    normalized = page.strip()
    while True:
        match = DIRECTION_WRAPPER_RE.match(normalized)
        if not match:
            return normalized
        normalized = match.group(1).strip()


def page_sort_key(page: str) -> tuple[int, int | str]:
    plain_digits = re.sub(r"\D", "", page)
    if plain_digits and not re.search(r"[A-Za-z]", page):
        return (0, int(plain_digits))
    return (1, page)


def render(entries: list[Entry]) -> str:
    grouped: dict[str, set[str]] = {}
    order: dict[str, str] = {}
    for entry in entries:
        grouped.setdefault(entry.display, set()).add(unwrap_page(entry.page))
        order.setdefault(entry.display, entry.sort_key)

    lines = [r"\begin{theindex}", ""]
    for display in sorted(grouped, key=lambda value: (order[value], value)):
        pages = sorted(grouped[display], key=page_sort_key)
        lines.append(rf"  \item {display}, {', '.join(pages)}")
    lines.extend(["", r"\end{theindex}", ""])
    return "\n".join(lines)


def write_diagnostics(output_directory: Path, input_directory: Path, exc: BaseException) -> None:
    sections = [
        "=== INDEX GENERATOR FAILURE ===",
        "".join(traceback.format_exception(type(exc), exc, exc.__traceback__)),
        f"input_directory={input_directory.resolve()}",
        f"output_directory={output_directory.resolve()}",
    ]
    for root in (input_directory, output_directory):
        sections.append(f"\n=== IDX FILES UNDER {root.resolve()} ===")
        found = sorted(root.glob("*.idx")) if root.is_dir() else []
        if not found:
            sections.append("<none>")
        for path in found:
            sections.append(f"\n--- {path} ---")
            sections.append(path.read_text(encoding="utf-8-sig", errors="replace"))

    diagnostic = "\n".join(sections) + "\n"
    (output_directory / "index-generator-error.txt").write_text(diagnostic, encoding="utf-8")
    (output_directory / "main.log").write_text(diagnostic, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--input-directory", type=Path, default=Path.cwd())
    args = parser.parse_args()

    args.output_directory.mkdir(parents=True, exist_ok=True)

    try:
        for name in EXPECTED:
            idx_path = resolve_idx(name, args.input_directory, args.output_directory)
            entries = parse_idx(idx_path)
            # imakeidx reads named indexes as <name>.ind, even though the main
            # document job name is "main". Writing main.<name>.ind leaves the
            # seeded empty <name>.ind files in place and silently drops indexes.
            ind_path = args.output_directory / f"{name}.ind"
            ind_path.write_text(render(entries), encoding="utf-8")
            print(f"Built {ind_path} from {len(entries)} entries in {idx_path}")
    except Exception as exc:
        write_diagnostics(args.output_directory, args.input_directory, exc)
        raise

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
