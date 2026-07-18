#!/usr/bin/env python3
"""Repository quality checks for the Arabic analytic number theory encyclopedia."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


version_text = read(ROOT / "docs" / "VERSION.md")
match = re.search(r"```text\s+(\d+\.\d+\.\d+-dev)\s+```", version_text)
if not match:
    fail("Could not parse the canonical version from docs/VERSION.md.")
    canonical = None
else:
    canonical = match.group(1)

if canonical:
    checks = {
        ROOT / "README.md": f"v{canonical}",
        ROOT / "docs" / "PROGRESS.md": canonical,
        ROOT / "manuscript" / "main.tex": canonical.removesuffix("-dev"),
    }
    for path, expected in checks.items():
        if expected not in read(path):
            fail(f"Version mismatch: {path.relative_to(ROOT)} does not contain {expected!r}.")

for path in list(ROOT.rglob("*.tex")) + list(ROOT.rglob("*.md")):
    text = read(path)
    rel = path.relative_to(ROOT)

    if "\u06a9" in text:
        fail(f"Persian kaf U+06A9 found in {rel}. Use Arabic kaf U+0643.")
    if "\u06cc" in text:
        fail(f"Persian yeh U+06CC found in {rel}. Use Arabic yeh U+064A.")
    if "identically" in text:
        fail(f"Untranslated word 'identically' found in {rel}.")

for path in list(ROOT.rglob("*.tex")) + list(ROOT.rglob("*.md")):
    text = read(path)
    rel = path.relative_to(ROOT)
    for char in text:
        code = ord(char)
        if code < 32 and char not in ("\n", "\r", "\t"):
            fail(f"Unexpected control character U+{code:04X} found in {rel}.")
            break

registry = read(ROOT / "docs" / "RESULTS_REGISTRY.md")
for tex_path in ROOT.rglob("*.tex"):
    for result_id in re.findall(r"\\resultid\{([^}]+)\}", read(tex_path)):
        if result_id not in registry:
            fail(f"Result ID {result_id} is missing from docs/RESULTS_REGISTRY.md.")

if errors:
    print("QUALITY CHECK FAILED")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print("QUALITY CHECK PASSED")
print(f"Canonical version: {canonical}")
