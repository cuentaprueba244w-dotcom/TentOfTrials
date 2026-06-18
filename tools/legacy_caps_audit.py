#!/usr/bin/env python3
"""Audit LEGACY comment markers for source and documentation files.

The audit checks text files that can carry comments. If a scanned file contains
``legacy`` in any casing, it must also contain an uppercase ``LEGACY`` marker on
a comment line that fits the file type.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    "diagnostic",
    "node_modules",
    "target",
    "dist",
    "build",
    "__pycache__",
}

SKIP_FILES = {
    "frontend/tsconfig.tsbuildinfo",
}

COMMENT_PREFIXES = {
    ".c": ("//", "/*", "*"),
    ".cpp": ("//", "/*", "*"),
    ".css": ("/*", "*"),
    ".go": ("//", "/*", "*"),
    ".h": ("//", "/*", "*"),
    ".hpp": ("//", "/*", "*"),
    ".hs": ("--",),
    ".java": ("//", "/*", "*"),
    ".js": ("//", "/*", "*"),
    ".json": (),
    ".lua": ("--",),
    ".md": ("<!--", ">", "#"),
    ".py": ("#", '"""', "'''"),
    ".rb": ("#",),
    ".rs": ("//", "/*", "*"),
    ".sh": ("#",),
    ".sql": ("--",),
    ".tf": ("#", "//", "/*", "*"),
    ".toml": ("#",),
    ".ts": ("//", "/*", "*"),
    ".tsx": ("//", "/*", "*"),
    ".yaml": ("#",),
    ".yml": ("#",),
}


def is_skipped(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if rel in SKIP_FILES:
        return True
    return any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)


def is_text_candidate(path: Path) -> bool:
    return path.suffix in COMMENT_PREFIXES and COMMENT_PREFIXES[path.suffix]


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def has_legacy_comment_marker(path: Path, text: str) -> bool:
    prefixes = COMMENT_PREFIXES[path.suffix]
    for raw_line in text.splitlines():
        line = raw_line.lstrip()
        if any(line.startswith(prefix) for prefix in prefixes) and "LEGACY" in line:
            return True
    return False


def audited_files() -> list[Path]:
    return [
        path
        for path in sorted(ROOT.rglob("*"))
        if path.is_file() and not is_skipped(path) and is_text_candidate(path)
    ]


def main() -> int:
    violations: list[str] = []
    checked = 0
    containing_legacy = 0
    for path in audited_files():
        text = read_text(path)
        if text is None:
            continue
        checked += 1
        if "legacy" not in text.lower():
            continue
        containing_legacy += 1
        if not has_legacy_comment_marker(path, text):
            violations.append(path.relative_to(ROOT).as_posix())

    if violations:
        print("LEGACY comment marker audit failed:")
        for relpath in violations:
            print(f"- {relpath}")
        print(f"checked={checked} files_with_legacy={containing_legacy} violations={len(violations)}")
        return 1

    print(f"LEGACY comment marker audit passed: checked={checked} files_with_legacy={containing_legacy}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
