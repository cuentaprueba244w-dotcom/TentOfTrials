#!/usr/bin/env python3
"""Deterministic repository task audit generator.

Scans the repository for case-insensitive task markers and generates
a structured TODO_AUDIT.md report with deterministic effort estimates.
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKER = "TO" + "DO"

SKIP_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    "node_modules",
    "target",
    "dist",
    "build",
    "diagnostic",
}

SKIP_FILES = {
    "TODO_AUDIT.md",
    "test_todo_audit.py",
    "todo_audit.py",
}

SKIP_EXTENSIONS = {
    ".logd",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".ico",
    ".svg",
    ".exe",
    ".dll",
    ".so",
    ".dylib",
    ".bin",
    ".zip",
    ".tar",
    ".gz",
    ".bz2",
    ".xz",
    ".7z",
    ".rar",
    ".pdf",
    ".ttf",
    ".woff",
    ".woff2",
    ".eot",
}


def calculate_estimated_hours(line_number: int) -> int:
    """Calculate deterministic fix time estimate in hours: (line_number % 7) + 1."""
    return (line_number % 7) + 1


@dataclass(frozen=True)
class AuditEntry:
    path: Path
    line_number: int
    text: str

    @property
    def estimated_hours(self) -> int:
        return calculate_estimated_hours(self.line_number)


def is_skippable_path(path: Path, root: Path) -> bool:
    """Determine whether a given file path should be excluded from audit."""
    try:
        relative = path.relative_to(root)
    except ValueError:
        relative = path

    for part in relative.parts:
        if part in SKIP_DIRS or (part.startswith(".") and part not in {".", ".."}):
            return True

    if relative.name in SKIP_FILES:
        return True

    if relative.suffix.lower() in SKIP_EXTENSIONS:
        return True

    return False


def iter_candidate_files(root: Path) -> list[Path]:
    """Yield all candidate source text files under root in sorted order."""
    candidate_files: list[Path] = []
    for current_dir, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames
            if d not in SKIP_DIRS and not d.startswith(".")
        ]
        dirnames.sort()

        current_path = Path(current_dir)
        for filename in sorted(filenames):
            path = current_path / filename
            if not is_skippable_path(path, root):
                candidate_files.append(path)

    return sorted(candidate_files)


def find_entries(root: Path) -> list[AuditEntry]:
    """Scan candidate files for task markers and return sorted audit entries."""
    marker = MARKER.lower()
    entries: list[AuditEntry] = []

    for path in iter_candidate_files(root):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue

        relative_path = path.relative_to(root)
        for index, line in enumerate(lines, start=1):
            if marker in line.lower():
                entries.append(AuditEntry(relative_path, index, line.strip()))

    return sorted(
        entries,
        key=lambda entry: (
            -entry.estimated_hours,
            entry.path.as_posix(),
            entry.line_number,
        ),
    )


def render_report(entries: list[AuditEntry]) -> str:
    """Render audit entries into formatted markdown report."""
    lines = [
        "# Repository TODO Audit",
        "",
        "This report lists case-insensitive TODO markers found in repository text files.",
        "Estimated fix time uses `(line_number % 7) + 1` hours, sorted descending.",
        "",
        f"Total entries: {len(entries)}",
        "",
        "| Estimated hours | File | Line | Text |",
        "| ---: | --- | ---: | --- |",
    ]
    for entry in entries:
        escaped_text = entry.text.replace("|", "\\|")
        file_path = entry.path.as_posix()
        lines.append(
            f"| {entry.estimated_hours} | `{file_path}` | {entry.line_number} | {escaped_text} |"
        )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate repository task audit report (TODO_AUDIT.md)"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root directory to scan",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "TODO_AUDIT.md",
        help="Destination markdown file path",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify if the output file is up to date without modifying it",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    entries = find_entries(root)
    content = render_report(entries)

    output = args.output
    if not output.is_absolute():
        output = root / output

    if args.check:
        if not output.exists():
            print(f"Error: {output} does not exist.")
            return 1
        existing = output.read_text(encoding="utf-8")
        if existing != content:
            print(f"Error: {output} is out of date.")
            return 1
        print(f"Check passed: {output} is up to date with {len(entries)} entries.")
        return 0

    output.write_text(content, encoding="utf-8")
    print(f"Wrote {output} with {len(entries)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
