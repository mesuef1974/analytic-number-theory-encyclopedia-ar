#!/usr/bin/env python3
"""Repository quality checks for the Arabic analytic number theory encyclopedia."""

from __future__ import annotations

import os
import re
import subprocess
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

text_paths = list(ROOT.rglob("*.tex")) + list(ROOT.rglob("*.md"))

for path in text_paths:
    text = read(path)
    rel = path.relative_to(ROOT)

    if "\u06a9" in text:
        fail(f"Persian kaf U+06A9 found in {rel}. Use Arabic kaf U+0643.")
    if "\u06cc" in text:
        fail(f"Persian yeh U+06CC found in {rel}. Use Arabic yeh U+064A.")
    if "identically" in text:
        fail(f"Untranslated word 'identically' found in {rel}.")

    # Chapter 18 result IDs must place the chapter number before the local
    # sequence number: ANT-<TYPE>-18-<NN>. Reject the historical inversion
    # ANT-<TYPE>-<NN>-18 everywhere in manuscript and governance records.
    for old_id in re.findall(
        r"\bANT-(?:ID|THM|LEM|PROP|COR|DEF|EX|REM|OPEN|CONJ)-\d{2}-18\b",
        text,
    ):
        fail(f"Legacy Chapter 18 result ID ordering {old_id} found in {rel}.")

for path in text_paths:
    text = read(path)
    rel = path.relative_to(ROOT)
    for char in text:
        code = ord(char)
        if code < 32 and char not in ("\n", "\r", "\t"):
            fail(f"Unexpected control character U+{code:04X} found in {rel}.")
            break

registry_paths = sorted((ROOT / "docs").glob("RESULTS_REGISTRY*.md"))
registry = "\n".join(read(path) for path in registry_paths)
for tex_path in ROOT.rglob("*.tex"):
    for result_id in re.findall(r"\\resultid\{([^}]+)\}", read(tex_path)):
        if result_id not in registry:
            fail(f"Result ID {result_id} is missing from the result registry files.")

# Delegated sub-checks. These live in their own scripts because each is
# specific to one chapter's governance documents, but they must run in CI,
# so quality_check.py invokes them rather than leaving them opt-in.
SUB_CHECKS = [
    ROOT / "scripts" / "check_ch58_consistency.py",
]
for sub in SUB_CHECKS:
    if not sub.exists():
        fail(f"Delegated check missing: {sub.relative_to(ROOT)}")
        continue
    result = subprocess.run(
        [sys.executable, "-W", "ignore", str(sub)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )
    if result.returncode != 0:
        detail = (result.stdout or "") + (result.stderr or "")
        offending = [ln.strip() for ln in detail.splitlines()
                     if ln.strip().startswith("- ") or "FAIL" in ln]
        fail(f"{sub.name} failed:\n    " + "\n    ".join(offending[:12]))

if errors:
    print("QUALITY CHECK FAILED")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print("QUALITY CHECK PASSED")
print(f"Canonical version: {canonical}")
print(f"Delegated checks passed: {', '.join(s.name for s in SUB_CHECKS)}")