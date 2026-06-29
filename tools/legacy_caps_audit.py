#!/usr/bin/env python3
# LEGACY: file contains legacy compatibility references for audit tracking.

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "target",
}

SKIP_PATH_PARTS = {
    "diagnostic",
}

TEXT_EXTENSIONS = {
    ".c",
    ".cpp",
    ".css",
    ".go",
    ".h",
    ".hpp",
    ".hs",
    ".html",
    ".java",
    ".js",
    ".json",
    ".lua",
    ".md",
    ".py",
    ".rs",
    ".sql",
    ".toml",
    ".ts",
    ".tsx",
    ".yaml",
    ".yml",
}

LINE_COMMENT_PREFIXES = {
    ".c": ("//",),
    ".cpp": ("//",),
    ".go": ("//",),
    ".h": ("//",),
    ".hpp": ("//",),
    ".hs": ("--",),
    ".java": ("//",),
    ".js": ("//",),
    ".lua": ("--",),
    ".py": ("#",),
    ".rs": ("//",),
    ".sql": ("--",),
    ".toml": ("#",),
    ".ts": ("//",),
    ".tsx": ("//",),
    ".yaml": ("#",),
    ".yml": ("#",),
}

BLOCK_COMMENT_EXTENSIONS = {
    ".c",
    ".cpp",
    ".css",
    ".go",
    ".h",
    ".hpp",
    ".java",
    ".js",
    ".rs",
    ".ts",
    ".tsx",
}


def main() -> int:
    violations = []

    for path in iter_candidate_files():
        text = read_text(path)
        if text is None or not re.search(r"legacy", text, re.IGNORECASE):
            continue

        if not has_uppercase_legacy_comment(path, text):
            violations.append(path)

    if violations:
        print("LEGACY comment audit failed.")
        print("Files containing legacy must also include uppercase LEGACY in a comment:")
        for path in violations:
            print(f"- {path.relative_to(ROOT)}")
        return 1

    print("LEGACY comment audit passed.")
    return 0


def iter_candidate_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if any(part in SKIP_PATH_PARTS for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        yield path


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return None


def has_uppercase_legacy_comment(path: Path, text: str) -> bool:
    suffix = path.suffix.lower()

    for line in text.splitlines():
        stripped = line.lstrip()
        if "LEGACY" not in stripped:
            continue
        if suffix == ".md" and "<!--" in stripped:
            return True
        if suffix == ".html" and "<!--" in stripped:
            return True
        if suffix == ".css" and "/*" in stripped:
            return True
        if any(stripped.startswith(prefix) for prefix in LINE_COMMENT_PREFIXES.get(suffix, ())):
            return True

    if suffix in BLOCK_COMMENT_EXTENSIONS:
        for match in re.finditer(r"/\*.*?\*/", text, re.DOTALL):
            if "LEGACY" in match.group(0):
                return True

    return False


if __name__ == "__main__":
    sys.exit(main())

