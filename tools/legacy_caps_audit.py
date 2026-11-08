#!/usr/bin/env python3
# LEGACY: Audit tool enforcing uppercase LEGACY comment markers.
"""
tools/legacy_caps_audit.py

Acceptance criteria:
- Verifies every file containing the word 'legacy' (case-insensitive) also contains
  uppercase 'LEGACY' in a comment.
- Supports comments in Python (#), JS/TS/Go/Rust/C/C++ (// and /* */), Shell (#),
  Markdown (<!-- -->), Lua/SQL/Haskell (--), etc.
- Scans all files in the repository and verifies compliance.
- Returns zero (exit code 0) when all files pass, or non-zero when violations exist.
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Directories to skip during repo traversal
SKIP_DIRS = {
    ".git",
    ".github",
    "node_modules",
    "target",
    "build",
    "dist",
    "__pycache__",
    ".venv",
    "venv",
    ".cache",
    ".system_generated",
}

# Non-source / binary file extensions to skip
SKIP_EXTENSIONS = {
    ".exe",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".ico",
    ".logd",
    ".o",
    ".hi",
    ".tsbuildinfo",
    ".pyc",
    ".bin",
    ".dylib",
    ".so",
    ".a",
    ".tar",
    ".gz",
    ".zip",
    ".wasm",
}

# Regex patterns for legacy reference and uppercase LEGACY in comments
LEGACY_WORD_RE = re.compile(r"legacy", re.IGNORECASE)
LEGACY_CAPS_RE = re.compile(r"\bLEGACY\b")

# Line comments: #, //, --, ;, or * (block comment continuation)
LINE_COMMENT_RE = re.compile(r"^\s*(?://|#|--|;|\*).*?\bLEGACY\b", re.MULTILINE)
INLINE_COMMENT_RE = re.compile(r"(?<!https:)(?<!http:)(?://|#|--|;)[^\n]*?\bLEGACY\b")

# Block comments: /* ... */ and <!-- ... -->
C_BLOCK_COMMENT_RE = re.compile(r"/\*(?:[^*]|\*(?!/))*\*/")
HTML_BLOCK_COMMENT_RE = re.compile(r"<!--(?:(?!-->).)*?-->", re.DOTALL)


def is_binary_file(path: Path) -> bool:
    """Check if file appears to be binary by searching for null bytes."""
    try:
        with open(path, "rb") as f:
            chunk = f.read(8192)
            return b"\x00" in chunk
    except OSError:
        return True


def has_legacy_comment(content: str) -> bool:
    """Check if content has uppercase LEGACY within a supported comment structure."""
    if LINE_COMMENT_RE.search(content):
        return True
    if INLINE_COMMENT_RE.search(content):
        return True
    for match in C_BLOCK_COMMENT_RE.finditer(content):
        if LEGACY_CAPS_RE.search(match.group(0)):
            return True
    for match in HTML_BLOCK_COMMENT_RE.finditer(content):
        if LEGACY_CAPS_RE.search(match.group(0)):
            return True
    return False


def audit_file(path: Path) -> tuple[bool, str]:
    """
    Audit a single file.
    Returns (True, "pass") if compliant or not applicable.
    Returns (False, reason) if it contains 'legacy' but lacks an uppercase 'LEGACY' comment.
    """
    if path.suffix.lower() in SKIP_EXTENSIONS or path.name.startswith("."):
        return True, "skipped"
    if is_binary_file(path):
        return True, "binary"

    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return True, f"unreadable: {e}"

    if not LEGACY_WORD_RE.search(content):
        return True, "no_legacy"

    if has_legacy_comment(content):
        return True, "pass"

    return False, "missing uppercase LEGACY comment"


def audit_repository(root_dir: Path, verbose: bool = False) -> tuple[int, list[Path]]:
    """Scan all files in root_dir and return (scanned_count, violations)."""
    violations: list[Path] = []
    scanned_count = 0

    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for filename in sorted(filenames):
            p = Path(dirpath) / filename
            passed, reason = audit_file(p)
            if reason not in ("skipped", "binary"):
                scanned_count += 1
            if not passed:
                violations.append(p)
            elif verbose and reason == "pass":
                print(f"[OK] {p.relative_to(root_dir)}")

    return scanned_count, violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit repository for uppercase LEGACY comments in files referencing legacy."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Root directory of repository to audit",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Print verbose scanning output"
    )
    args = parser.parse_args()

    root = args.root.resolve()
    scanned_count, violations = audit_repository(root, verbose=args.verbose)

    if violations:
        print(f"[FAIL] Found {len(violations)} violation(s) across {scanned_count} scanned file(s):", file=sys.stderr)
        for v in violations:
            try:
                rel = v.relative_to(root)
            except ValueError:
                rel = v
            print(f"  - {rel}: contains legacy reference without uppercase LEGACY comment", file=sys.stderr)
        return 1

    print(f"[PASS] Legacy caps audit passed: {scanned_count} files scanned, all legacy references have uppercase LEGACY comments.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
