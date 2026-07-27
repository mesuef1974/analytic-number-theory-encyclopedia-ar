#!/usr/bin/env python3
"""Build UTF-8-safe named LaTeX indexes from imakeidx .idx files.

This intentionally avoids legacy makeindex, whose byte-oriented parser is not
reliable for Arabic UTF-8 index entries. The generated .ind files use the
standard theindex environment consumed by imakeidx/\printindex.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ENTRY_RE = re.compile(r"^\\indexentry\{(.*)\}\{([^{}]+)\}\s*$")


@dataclass(frozen=True)
class Entry:
    raw: str
    page: str

    @property
    def display(self) -> str:
        # Preserve TeX markup after an optional makeindex sort key.
        return self.raw.split("@", 1)[-1]

    @property
    def sort_key(self) -> str:
        key = self.raw.split("@", 1)[0]
        # A stable Unicode-aware approximation: normalize and case-fold while
        # retaining Arabic letters. TeX control syntax sorts after plain text.
        return unicodedata.normalize("NFKC", key).casefold()


def parse_idx(path: Path) -> list[Entry]:
    entries: list[Entry] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = ENTRY_RE.match(line)
        if not match:
            raise ValueError(f"{path}:{number}: unsupported index line: {line!r}")
        entries.append(Entry(match.group(1), match.group(2)))
    return entries


def render(entries: list[Entry]) -> str:
    grouped: dict[str, set[str]] = {}
    order: dict[str, str] = {}
    for entry in entries:
        display = entry.display
        grouped.setdefault(display, set()).add(entry.page)
        order.setdefault(display, entry.sort_key)

    lines = [r"\begin{theindex}", ""]
    for display in sorted(grouped, key=lambda value: (order[value], value)):
        pages = sorted(grouped[display], key=lambda p: (not p.isdigit(), int(p) if p.isdigit() else p))
        lines.append(rf"  \item {display}, {', '.join(pages)}")
    lines.extend(["", r"\end{theindex}", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()

    idx_files = sorted(args.directory.glob("main.*.idx"))
    if not idx_files:
        raise SystemExit(f"No named index files found in {args.directory}")

    expected = {"people", "theorems", "symbols"}
    seen: set[str] = set()
    for idx_path in idx_files:
        name = idx_path.name.removeprefix("main.").removesuffix(".idx")
        if name not in expected:
            continue
        entries = parse_idx(idx_path)
        ind_path = idx_path.with_suffix(".ind")
        ind_path.write_text(render(entries), encoding="utf-8")
        print(f"Built {ind_path} from {len(entries)} entries")
        seen.add(name)

    missing = expected - seen
    if missing:
        raise SystemExit(f"Missing named index inputs: {', '.join(sorted(missing))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
