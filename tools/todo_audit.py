#!/usr/bin/env python3

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
}
SKIP_FILES = {
    "TODO_AUDIT.md",
    "test_todo_audit.py",
    "todo_audit.py",
}


@dataclass(frozen=True)
class AuditEntry:
    path: Path
    line_number: int
    text: str

    @property
    def estimated_hours(self) -> int:
        return (self.line_number % 7) + 1


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for current_root, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            dirname for dirname in dirnames
            if dirname not in SKIP_DIRS and not dirname.startswith(".")
        ]
        current_path = Path(current_root)
        for filename in filenames:
            path = current_path / filename
            if filename in SKIP_FILES:
                continue
            if path.suffix.lower() in {".logd", ".png", ".jpg", ".jpeg", ".gif", ".exe"}:
                continue
            files.append(path)
    return sorted(files)


def find_entries(root: Path) -> list[AuditEntry]:
    marker = MARKER.lower()
    entries: list[AuditEntry] = []
    for path in iter_files(root):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        except OSError:
            continue

        relative_path = path.relative_to(root)
        for index, line in enumerate(lines, start=1):
            if marker in line.lower():
                entries.append(AuditEntry(relative_path, index, line.strip()))

    return sorted(
        entries,
        key=lambda entry: (-entry.estimated_hours, str(entry.path), entry.line_number),
    )


def render_report(entries: list[AuditEntry]) -> str:
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
        text = entry.text.replace("|", "\\|")
        path = str(entry.path).replace("\\", "/")
        lines.append(f"| {entry.estimated_hours} | `{path}` | {entry.line_number} | {text} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate repository task-marker audit")
    parser.add_argument(
        "--output",
        default="TODO_AUDIT.md",
        help="Report path relative to the repository root",
    )
    args = parser.parse_args()

    entries = find_entries(ROOT)
    output = ROOT / args.output
    output.write_text(render_report(entries), encoding="utf-8")
    print(f"Wrote {output.relative_to(ROOT)} with {len(entries)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
