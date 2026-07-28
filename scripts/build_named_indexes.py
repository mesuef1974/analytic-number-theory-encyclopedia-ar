#!/usr/bin/env python3
"""Build UTF-8-safe named LaTeX indexes from imakeidx .idx files.

The parser reads each .idx file as a TeX stream rather than assuming that every
``\indexentry`` occupies exactly one physical line. This supports Arabic UTF-8,
nested TeX groups, multiline entries, and formatted page numbers without using
legacy makeindex.
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
    """Read one balanced TeX brace group beginning at or after ``start``."""
    cursor = skip_space_and_comments(text, start)
    if cursor >= len(text) or text[cursor] != "{":
        excerpt = text[cursor : cursor + 80].replace("\n", r"\n")
        raise ValueError(f"expected '{{' at offset {cursor}; next={excerpt!r}")

    depth = 1
    index = cursor + 1
    chars: list[str] = []
    while index < len(text):
        char = text[index]

        # A TeX control symbol such as \{ or \} must not alter brace depth.
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
        entries.append(Entry(raw.strip(), page.strip()))
        cursor = after_page

    prefix_count = text.count(PREFIX)
    if len(entries) != prefix_count:
        raise ValueError(
            f"{path}: parsed {len(entries)} entries but found {prefix_count} {PREFIX!r} markers"
        )
    return entries


def page_sort_key(page: str) -> tuple[int, int | str]:
    plain_digits = re.sub(r"\D", "", page)
    if plain_digits and not re.search(r"[A-Za-z]", page):
        return (0, int(plain_digits))
    return (1, page)


def render(entries: list[Entry]) -> str:
    grouped: dict[str, set[str]] = {}
    order: dict[str, str] = {}
    for entry in entries:
        grouped.setdefault(entry.display, set()).add(entry.page)
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
    ]
    for name in EXPECTED:
        path = input_directory / f"{name}.idx"
        sections.append(f"\n=== {path} ===")
        if path.is_file():
            sections.append(path.read_text(encoding="utf-8-sig", errors="replace"))
        else:
            sections.append("<missing>")

    diagnostic = "\n".join(sections) + "\n"
    (output_directory / "index-generator-error.txt").write_text(diagnostic, encoding="utf-8")
    with (output_directory / "main.log").open("a", encoding="utf-8") as log:
        log.write("\n" + diagnostic)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--input-directory", type=Path, default=Path.cwd())
    args = parser.parse_args()

    args.output_directory.mkdir(parents=True, exist_ok=True)

    try:
        for name in EXPECTED:
            idx_path = args.input_directory / f"{name}.idx"
            if not idx_path.is_file():
                available = ", ".join(str(path) for path in sorted(args.input_directory.glob("*.idx"))) or "none"
                raise FileNotFoundError(
                    f"Missing named index input: {idx_path}; available .idx files: {available}"
                )

            entries = parse_idx(idx_path)
            ind_path = args.output_directory / f"{name}.ind"
            ind_path.write_text(render(entries), encoding="utf-8")
            print(f"Built {ind_path} from {len(entries)} entries in {idx_path}")
    except Exception as exc:
        write_diagnostics(args.output_directory, args.input_directory, exc)
        raise

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
