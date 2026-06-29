#!/usr/bin/env python3
"""Audit legacy references for an uppercase LEGACY marker."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXCLUDED_DIRS = {
    ".git",
    "__pycache__",
    "node_modules",
    "target",
    "dist",
    "build",
    "diagnostic",
    "tools/encryptly",
}

TEXT_SUFFIXES = {
    ".c",
    ".cpp",
    ".css",
    ".go",
    ".h",
    ".hpp",
    ".html",
    ".java",
    ".js",
    ".json",
    ".lua",
    ".md",
    ".py",
    ".rb",
    ".rs",
    ".sh",
    ".sql",
    ".tf",
    ".ts",
    ".tsx",
    ".yaml",
    ".yml",
}

LEGACY_RE = re.compile(r"legacy", re.IGNORECASE)
COMMENT_MARKER_RE = re.compile(
    r"(^\s*(#|//|/\*|\*|<!--|--|;)|\"\"\"|'''|/\*|<!--).*LEGACY"
)


def is_excluded(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return any(rel == excluded or rel.startswith(f"{excluded}/") for excluded in EXCLUDED_DIRS)


def iter_text_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if path.is_dir() or is_excluded(path):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return files


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has_legacy_reference(text: str) -> bool:
    return LEGACY_RE.search(text) is not None


def has_legacy_marker(text: str) -> bool:
    return any(COMMENT_MARKER_RE.search(line) for line in text.splitlines())


def find_violations(root: Path) -> list[Path]:
    violations: list[Path] = []
    for path in iter_text_files(root):
        text = read_text(path)
        if has_legacy_reference(text) and not has_legacy_marker(text):
            violations.append(path)
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ensure files with legacy references include an uppercase LEGACY marker."
    )
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root to audit")
    args = parser.parse_args()

    root = args.root.resolve()
    violations = find_violations(root)
    if violations:
        print("Files containing legacy references without an uppercase LEGACY marker:")
        for path in violations:
            print(f"- {path.relative_to(root).as_posix()}")
        return 1

    print("All legacy references include an uppercase LEGACY marker.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
