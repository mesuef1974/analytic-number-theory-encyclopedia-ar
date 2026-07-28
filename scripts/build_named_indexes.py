#!/usr/bin/env python3
"""Build UTF-8-safe named LaTeX indexes from imakeidx .idx files.

imakeidx writes the named ``people.idx``, ``theorems.idx``, and ``symbols.idx``
files in the current working directory even when the PDF auxiliary files are
sent to an output directory. This script reads those UTF-8 inputs and writes the
matching ``.ind`` files into the requested LaTeX output directory.
"""

from __future__ import annotations

import argparse
import re
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


def read_group(text: str, start: int) -> tuple[str, int]:
    """Read one balanced TeX brace group beginning at ``start``."""
    if start >= len(text) or text[start] != "{":
        raise ValueError(f"expected '{{' at column {start + 1}")

    depth = 0
    escaped = False
    chars: list[str] = []
    for index in range(start, len(text)):
        char = text[index]
        if escaped:
            if depth >= 1:
                chars.append(char)
            escaped = False
            continue
        if char == "\\":
            if depth >= 1:
                chars.append(char)
            escaped = True
            continue
        if char == "{":
            depth += 1
            if depth > 1:
                chars.append(char)
            continue
        if char == "}":
            depth -= 1
            if depth < 0:
                raise ValueError(f"unbalanced closing brace at column {index + 1}")
            if depth == 0:
                return "".join(chars), index + 1
            chars.append(char)
            continue
        if depth >= 1:
            chars.append(char)

    raise ValueError("unterminated brace group")


def parse_index_line(line: str) -> Entry:
    text = line.strip()
    if not text.startswith(PREFIX):
        raise ValueError("line does not begin with \\indexentry")

    cursor = len(PREFIX)
    raw, cursor = read_group(text, cursor)
    page, cursor = read_group(text, cursor)
    if text[cursor:].strip():
        raise ValueError(f"unexpected trailing content: {text[cursor:]!r}")
    return Entry(raw, page)


def parse_idx(path: Path) -> list[Entry]:
    entries: list[Entry] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            entries.append(parse_index_line(line))
        except ValueError as exc:
            raise ValueError(f"{path}:{number}: {exc}; line={line!r}") from exc
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output_directory",
        type=Path,
        help="LaTeX output directory that must receive people.ind, theorems.ind, and symbols.ind",
    )
    parser.add_argument(
        "--input-directory",
        type=Path,
        default=Path.cwd(),
        help="Directory containing people.idx, theorems.idx, and symbols.idx (default: current directory)",
    )
    args = parser.parse_args()

    args.output_directory.mkdir(parents=True, exist_ok=True)

    for name in EXPECTED:
        idx_path = args.input_directory / f"{name}.idx"
        if not idx_path.is_file():
            available = ", ".join(str(path) for path in sorted(args.input_directory.glob("*.idx"))) or "none"
            raise SystemExit(f"Missing named index input: {idx_path}; available .idx files: {available}")

        entries = parse_idx(idx_path)
        ind_path = args.output_directory / f"{name}.ind"
        ind_path.write_text(render(entries), encoding="utf-8")
        print(f"Built {ind_path} from {len(entries)} entries in {idx_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
