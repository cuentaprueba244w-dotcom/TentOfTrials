#!/usr/bin/env python3
# LEGACY: This file intentionally carries legacy references for compatibility audits.
"""Audit files with legacy references for uppercase LEGACY comment markers."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "target",
}

SKIP_SUFFIXES = {
    ".exe",
    ".hi",
    ".logd",
    ".o",
    ".png",
    ".tsbuildinfo",
}

LINE_COMMENT_PREFIXES = {
    ".c": ("//", "/*", "*"),
    ".cpp": ("//", "/*", "*"),
    ".css": ("/*", "*"),
    ".go": ("//",),
    ".h": ("//", "/*", "*"),
    ".hpp": ("//", "/*", "*"),
    ".hs": ("--",),
    ".java": ("//", "/*", "*"),
    ".js": ("//", "/*", "*"),
    ".lua": ("--",),
    ".md": ("<!--",),
    ".pl": ("#",),
    ".py": ("#",),
    ".rb": ("#",),
    ".rs": ("//", "/*", "*"),
    ".sql": ("--",),
    ".tf": ("#",),
    ".ts": ("//", "/*", "*"),
    ".tsx": ("//", "/*", "*"),
    ".yaml": ("#",),
    ".yml": ("#",),
}

LEGACY_RE = re.compile(r"legacy", re.IGNORECASE)


def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            dirname
            for dirname in dirnames
            if dirname not in SKIP_DIRS and not dirname.startswith(".cache")
        ]
        for filename in filenames:
            path = Path(dirpath) / filename
            if path.suffix in SKIP_SUFFIXES:
                continue
            yield path


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return None
    except OSError:
        return None


def comment_prefixes_for(path: Path) -> tuple[str, ...]:
    if path.name in {"Makefile", ".gitignore"}:
        return ("#",)
    return LINE_COMMENT_PREFIXES.get(path.suffix, ("#",))


def has_legacy_comment_marker(path: Path, text: str) -> bool:
    prefixes = comment_prefixes_for(path)
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(prefixes) and "LEGACY" in stripped:
            return True
    return False


def audit(root: Path) -> list[Path]:
    violations: list[Path] = []
    for path in iter_files(root):
        text = read_text(path)
        if not text or not LEGACY_RE.search(text):
            continue
        if not has_legacy_comment_marker(path, text):
            violations.append(path)
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify files containing legacy references also have an uppercase LEGACY comment marker."
    )
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()

    root = args.root.resolve()
    violations = audit(root)
    if not violations:
        print("legacy caps audit passed: all files with legacy references include a LEGACY comment marker")
        return 0

    print("legacy caps audit failed: missing uppercase LEGACY comment marker", file=sys.stderr)
    for path in violations:
        print(path.relative_to(root), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
