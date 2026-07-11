#!/usr/bin/env python3
"""Verify files referencing legacy also include an uppercase LEGACY comment marker."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SCAN_EXTENSIONS = {
    ".py",
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".go",
    ".rs",
    ".lua",
    ".md",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".css",
    ".rb",
    ".hs",
    ".pl",
}

SKIP_DIRS = {
    ".git",
    "node_modules",
    "target",
    "dist",
    "diagnostic",
    ".venv",
    "__pycache__",
}


def should_scan(path: Path) -> bool:
    if path.suffix.lower() not in SCAN_EXTENSIONS:
        return False
    return not any(part in SKIP_DIRS for part in path.parts)


def find_violations(root: Path) -> list[Path]:
    violations: list[Path] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or not should_scan(path):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if "legacy" in text.lower() and "LEGACY" not in text:
            violations.append(path.relative_to(root))
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit that legacy references include an uppercase LEGACY marker.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=ROOT,
        help="Repository root to scan (default: parent of tools/)",
    )
    args = parser.parse_args()
    root = args.repo_root.resolve()
    violations = find_violations(root)
    if violations:
        print(f"Found {len(violations)} file(s) with legacy references but no LEGACY marker:")
        for path in violations:
            print(path)
        return 1
    print("All legacy references include an uppercase LEGACY marker.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
