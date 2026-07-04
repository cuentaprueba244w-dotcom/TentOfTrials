#!/usr/bin/env python3
# LEGACY
"""
Audit and fix LEGACY comment markers.

Rules:
- Scan all files under repository root except .git and node_modules.
- Any text file containing "legacy" case-insensitively must contain the proper
  uppercase LEGACY comment marker for its language.
- Default mode fixes missing markers in place.
- --check mode only audits and exits non-zero when violations exist.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


EXCLUDED_DIRS = {".git", "node_modules", "target", "__pycache__", ".venv", "venv", "dist", "build", ".mypy_cache", ".pytest_cache", ".ruff_cache"}

RUST_EXTS = {".rs"}
PYTHON_EXTS = {".py", ".pyw"}
JS_TS_EXTS = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"}
C_CPP_EXTS = {".c", ".h", ".cpp", ".hpp", ".cc", ".cxx", ".hh", ".hxx"}
JAVA_EXTS = {".java"}
GO_EXTS = {".go"}
RUBY_EXTS = {".rb", ".rake", ".gemspec"}
LUA_EXTS = {".lua"}
HASKELL_EXTS = {".hs", ".lhs"}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def should_skip(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.parts)


def is_probably_binary(data: bytes) -> bool:
    if b"\x00" in data:
        return True

    sample = data[:4096]
    if not sample:
        return False

    text_chars = bytearray({7, 8, 9, 10, 12, 13, 27})
    text_chars.extend(range(0x20, 0x100))
    non_text = sample.translate(None, bytes(text_chars))
    return len(non_text) / max(len(sample), 1) > 0.30


def read_text(path: Path) -> str | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None

    if is_probably_binary(data):
        return None

    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue

    return None


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def comment_prefix(path: Path) -> str:
    suffix = path.suffix.lower()

    if suffix in PYTHON_EXTS:
        return "#"
    if suffix in RUBY_EXTS:
        return "#"
    if suffix in LUA_EXTS:
        return "--"
    if suffix in HASKELL_EXTS:
        return "--"
    if suffix in RUST_EXTS:
        return "//"
    if suffix in JS_TS_EXTS:
        return "//"
    if suffix in C_CPP_EXTS:
        return "//"
    if suffix in JAVA_EXTS:
        return "//"
    if suffix in GO_EXTS:
        return "//"

    return "//"


def marker_for(path: Path) -> str:
    return f"{comment_prefix(path)} LEGACY"


def contains_legacy(text: str) -> bool:
    return "legacy" in text.lower()


def has_required_marker(path: Path, text: str) -> bool:
    marker = marker_for(path)

    for line in text.splitlines():
        stripped = line.strip()
        if stripped == marker or stripped.startswith(marker + " "):
            return True

    return False


def newline_for(text: str) -> str:
    if "\r\n" in text:
        return "\r\n"
    return "\n"


def is_comment_line_for_path(path: Path, line: str) -> bool:
    stripped = line.lstrip()
    prefix = comment_prefix(path)

    if stripped.startswith(prefix):
        return True

    if stripped.startswith("/*"):
        return True

    if stripped.startswith("*"):
        return True

    if stripped.startswith("<!--"):
        return True

    return False


def find_legacy_comment_index(path: Path, lines: list[str]) -> int | None:
    for index, line in enumerate(lines):
        if "legacy" in line.lower() and is_comment_line_for_path(path, line):
            return index

    return None


def insertion_index_for_header(path: Path, lines: list[str]) -> int:
    index = 0

    if not lines:
        return 0

    first = lines[0]

    if first.startswith("#!"):
        index = 1

    if path.suffix.lower() in PYTHON_EXTS:
        while index < len(lines):
            stripped = lines[index].strip()
            lowered = stripped.lower()

            if lowered.startswith("# -*- coding:") or lowered.startswith("# coding=") or lowered.startswith("# coding:"):
                index += 1
                continue

            break

    return index


def marker_nearby(path: Path, lines: list[str], index: int) -> bool:
    marker = marker_for(path)
    start = max(0, index - 2)
    end = min(len(lines), index + 3)

    for nearby in lines[start:end]:
        stripped = nearby.strip()
        if stripped == marker or stripped.startswith(marker + " "):
            return True

    return False


def add_marker(path: Path, text: str) -> str:
    if has_required_marker(path, text):
        return text

    newline = newline_for(text)
    marker_line = marker_for(path) + newline
    lines = text.splitlines(keepends=True)

    legacy_comment_index = find_legacy_comment_index(path, lines)

    if legacy_comment_index is not None:
        if marker_nearby(path, lines, legacy_comment_index):
            return text

        lines.insert(legacy_comment_index, marker_line)
        return "".join(lines)

    insert_at = insertion_index_for_header(path, lines)
    lines.insert(insert_at, marker_line)
    return "".join(lines)


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []

    for path in root.rglob("*"):
        if should_skip(path):
            continue

        if not path.is_file():
            continue

        files.append(path)

    return files


def audit(root: Path) -> tuple[list[Path], list[Path]]:
    legacy_files: list[Path] = []
    violations: list[Path] = []

    for path in iter_files(root):
        text = read_text(path)

        if text is None:
            continue

        if not contains_legacy(text):
            continue

        legacy_files.append(path)

        if not has_required_marker(path, text):
            violations.append(path)

    return legacy_files, violations


def fix_files(paths: list[Path]) -> list[Path]:
    fixed: list[Path] = []

    for path in paths:
        text = read_text(path)

        if text is None:
            continue

        updated = add_marker(path, text)

        if updated != text:
            write_text(path, updated)
            fixed.append(path)

    return fixed


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit and fix uppercase LEGACY comment markers."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Only audit. Do not modify files. Exit non-zero when violations exist.",
    )
    args = parser.parse_args()

    root = repo_root()

    legacy_files, violations = audit(root)

    if args.check:
        if violations:
            print("LEGACY audit failed. Missing uppercase LEGACY marker:")
            for path in violations:
                print(f" - {rel(path, root)}")
            return 1

        print(f"LEGACY audit passed. Checked {len(legacy_files)} legacy file(s).")
        return 0

    if violations:
        print("Fixing files missing uppercase LEGACY marker:")
        for path in violations:
            print(f" - {rel(path, root)}")

        fixed = fix_files(violations)
        print(f"Fixed {len(fixed)} file(s).")

    legacy_files_after, violations_after = audit(root)

    if violations_after:
        print("LEGACY audit failed after fix. Still missing uppercase LEGACY marker:")
        for path in violations_after:
            print(f" - {rel(path, root)}")
        return 1

    print(f"LEGACY audit passed. Checked {len(legacy_files_after)} legacy file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
