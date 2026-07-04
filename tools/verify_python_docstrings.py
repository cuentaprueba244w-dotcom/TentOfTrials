#!/usr/bin/env python3
"""Verify that every Python file in the repository has a module docstring.

Scans tracked source files with Python's AST parser and reports pass/fail lists.
Exits with status 0 when all files pass, or 1 when docstrings are missing.
"""

import ast
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    ".hg",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    "target",
    ".venv",
    "venv",
    "env",
}


def iter_python_files(root: Path) -> list[Path]:
    """Return all Python files under root, skipping generated/cache directories."""
    python_files: list[Path] = []

    for path in root.rglob("*.py"):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        python_files.append(path)

    return sorted(python_files)


def has_module_docstring(path: Path) -> tuple[bool, str | None]:
    """Return whether path has a module-level docstring, plus parse error text."""
    try:
        source = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        source = path.read_text(encoding="utf-8-sig")

    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as exc:
        return False, f"SyntaxError: {exc}"

    return ast.get_docstring(tree) is not None, None


def format_path(path: Path) -> str:
    """Return a repository-relative path using POSIX separators."""
    return path.relative_to(REPO_ROOT).as_posix()


def main() -> int:
    """Run the module-docstring verification check."""
    passed: list[str] = []
    failed: list[str] = []

    for path in iter_python_files(REPO_ROOT):
        ok, error = has_module_docstring(path)
        display_path = format_path(path)

        if ok:
            passed.append(display_path)
            continue

        if error:
            failed.append(f"{display_path} ({error})")
        else:
            failed.append(display_path)

    print("Python module docstring verification")
    print("=" * 38)

    if passed:
        print("\nPASS:")
        for path in passed:
            print(f"  PASS {path}")

    if failed:
        print("\nFAIL:")
        for path in failed:
            print(f"  FAIL {path}")

    print(f"\nSummary: {len(passed)} passed, {len(failed)} failed")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
