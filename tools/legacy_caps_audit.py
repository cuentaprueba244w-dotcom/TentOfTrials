#!/usr/bin/env python3
"""
Legacy Caps Audit Tool
Enforces that any file mentioning 'legacy' contains an uppercase 'LEGACY' comment.
Exits 0 if clean, 1 if violations found.
"""
import os
import sys
import re

IGNORE_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'dist', 'build'}
COMMENT_PATTERNS = [
    re.compile(r'#.*?\bLEGACY\b'),             # Python, Shell, YAML, Ruby
    re.compile(r'//.*?\bLEGACY\b'),            # JS, TS, Go, C, C++
    re.compile(r'/\*.*?\bLEGACY\b.*?\*/', re.DOTALL), # Block comments
    re.compile(r'<!--.*?\bLEGACY\b.*?-->', re.DOTALL) # HTML, Markdown
]

def check_file(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception:
        return True, None

    # Check if file mentions legacy (case-insensitive)
    if not re.search(r'\blegacy\b', content, re.IGNORECASE):
        return True, None

    # Verify if it has an uppercase LEGACY comment
    for pat in COMMENT_PATTERNS:
        if pat.search(content):
            return True, None

    return False, f"Missing uppercase LEGACY comment in {path}"

def main():
    root = os.getcwd()
    violations = []
    scanned = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in {'.py', '.js', '.ts', '.sh', '.go', '.rs', '.html', '.md', '.json', '.yaml', '.yml'}:
                full_path = os.path.join(dirpath, f)
                scanned += 1
                passed, msg = check_file(full_path)
                if not passed:
                    violations.append(msg)

    print(f"[legacy_caps_audit] Scanned {scanned} files.")
    if violations:
        print(f"[legacy_caps_audit] Found {len(violations)} violation(s):")
        for v in violations:
            print(f"  - {v}")
        sys.exit(1)
    else:
        print("[legacy_caps_audit] All files pass audit cleanly!")
        sys.exit(0)

if __name__ == '__main__':
    main()
