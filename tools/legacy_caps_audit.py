#!/usr/bin/env python3
"""LEGACY uppercase comment marker audit and enforcement tool."""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COMMENT_PREFIXES = {
    ".py": "#", ".rs": "//", ".ts": "//", ".tsx": "//",
    ".js": "//", ".jsx": "//", ".go": "//", ".java": "//",
    ".c": "/*", ".h": "/*", ".cpp": "//", ".hpp": "//",
    ".rb": "#", ".lua": "--", ".hs": "--", ".sh": "#",
    ".yml": "#", ".yaml": "#", ".sql": "--",
    ".css": "/*", ".scss": "/*", ".pl": "#", ".pm": "#",
}

LEGACY_MARKERS = {
    ".py": "# LEGACY", ".rs": "// LEGACY", ".ts": "// LEGACY", ".tsx": "// LEGACY",
    ".js": "// LEGACY", ".jsx": "// LEGACY", ".go": "// LEGACY", ".java": "// LEGACY",
    ".c": "/* LEGACY */", ".h": "/* LEGACY */", ".cpp": "// LEGACY", ".hpp": "// LEGACY",
    ".rb": "# LEGACY", ".lua": "-- LEGACY", ".hs": "-- LEGACY", ".sh": "# LEGACY",
    ".yml": "# LEGACY", ".yaml": "# LEGACY", ".sql": "-- LEGACY",
    ".css": "/* LEGACY */", ".scss": "/* LEGACY */", ".md": "<!-- LEGACY -->",
    ".pl": "# LEGACY", ".pm": "# LEGACY",
}

SKIP_DIRS = {".git", "node_modules", "target", "dist", "build", ".venv", "__pycache__", "diagnostic"}


def find_legacy_files():
    results = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        parts = set(path.relative_to(ROOT).parts)
        if parts & SKIP_DIRS:
            continue
        ext = path.suffix.lower()
        if ext not in COMMENT_PREFIXES and ext != ".md":
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if re.search(r"legacy", content, re.IGNORECASE):
            results.append(path)
    return sorted(results)


def has_legacy_marker(content, ext):
    prefix = COMMENT_PREFIXES.get(ext, "")
    for line in content.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if prefix and stripped.startswith(prefix) and "LEGACY" in stripped:
            return True
        if ext in {".c", ".h", ".css", ".scss"} and "LEGACY" in stripped and ("/*" in stripped or "*/" in stripped):
            return True
        if ext == ".md" and "LEGACY" in stripped and ("<!--" in stripped or "-->" in stripped):
            return True
    return False


def add_legacy_marker(content, ext):
    marker = LEGACY_MARKERS.get(ext)
    if not marker:
        return content
    lines = content.split("\n")
    idx = 0
    if lines and lines[0].startswith("#!"):
        idx = 1
    if idx < len(lines) and lines[idx].startswith("# -*- coding"):
        idx += 1
    if idx < len(lines):
        s = lines[idx].strip()
        triple_double = '"""'
        triple_single = "'''"
        if s.startswith(triple_double) or s.startswith(triple_single):
            q = triple_double if s.startswith(triple_double) else triple_single
            if s.count(q) >= 2:
                idx += 1
            else:
                idx += 1
                while idx < len(lines) and q not in lines[idx]:
                    idx += 1
                if idx < len(lines):
                    idx += 1
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    new_lines = lines[:idx] + [marker, ""] + lines[idx:]
    return "\n".join(new_lines)


def main():
    parser = argparse.ArgumentParser(description="LEGACY uppercase comment marker audit")
    parser.add_argument("--fix", action="store_true", help="Fix violations")
    args = parser.parse_args()
    
    print("LEGACY Caps Audit - Tent of Trials")
    print("=" * 50)
    
    files = find_legacy_files()
    print(f"\nFiles containing 'legacy': {len(files)}")
    
    violations = []
    for f in files:
        ext = f.suffix.lower()
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue
        if not has_legacy_marker(content, ext):
            violations.append(f)
    
    if violations:
        print(f"\nViolations found: {len(violations)}")
        for v in violations:
            print(f"  [FAIL] {v.relative_to(ROOT)}")
        
        if args.fix:
            print(f"\nFixing {len(violations)} files...")
            fixed = 0
            for f in violations:
                ext = f.suffix.lower()
                content = f.read_text(encoding="utf-8")
                new_content = add_legacy_marker(content, ext)
                if new_content != content:
                    f.write_text(new_content, encoding="utf-8")
                    fixed += 1
                    print(f"  [FIXED] {f.relative_to(ROOT)}")
            print(f"\nFixed {fixed} files.")
            files2 = find_legacy_files()
            v2 = [f for f in files2 if not has_legacy_marker(f.read_text(encoding="utf-8", errors="replace"), f.suffix.lower())]
            if v2:
                print(f"Remaining violations: {len(v2)}")
                return 1
            print("All files pass!")
            return 0
        else:
            print(f"\nRun with --fix to automatically add markers.")
            return 1
    else:
        print("\nAll files pass - LEGACY markers present everywhere.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
