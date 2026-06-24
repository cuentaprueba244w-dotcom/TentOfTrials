#!/usr/bin/env python3
"""Generate TODO_AUDIT.md from all TODO comments in the repository."""

import os
import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).parent

# File extensions to search
EXTENSIONS = {
    ".rs": "Rust",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".go": "Go",
    ".c": "C",
    ".cpp": "C++",
    ".h": "C/C++",
    ".hpp": "C++",
    ".java": "Java",
    ".py": "Python",
    ".lua": "Lua",
    ".rb": "Ruby",
    ".hs": "Haskell",
}

def find_todos():
    """Find all TODO comments case-insensitively."""
    todos = []
    for root, dirs, files in os.walk(REPO_ROOT):
        # Skip .git and diagnostic directories
        dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules', '__pycache__')]

        for fname in files:
            ext = os.path.splitext(fname)[1]
            if ext not in EXTENSIONS:
                continue

            filepath = os.path.join(root, fname)
            relpath = os.path.relpath(filepath, REPO_ROOT).replace("\\", "/")

            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        # Case-insensitive search for TODO
                        if re.search(r'TODO', line, re.IGNORECASE):
                            # Extract the description after TODO
                            match = re.search(r'TODO[:\s]*(.*)', line, re.IGNORECASE)
                            description = match.group(1).strip() if match else ""
                            # Clean up comment markers
                            description = re.sub(r'^[/*#\-\s]+', '', description).strip()
                            description = re.sub(r'[/*#]+$', '', description).strip()
                            if not description:
                                description = "(no description)"

                            # Estimate fix time: (line_number % 7) + 1
                            estimated_hours = (line_num % 7) + 1

                            todos.append({
                                "filename": relpath,
                                "line_number": line_num,
                                "description": description,
                                "estimated_hours": estimated_hours,
                                "language": EXTENSIONS[ext],
                            })
            except Exception:
                continue

    # Sort by estimated hours descending
    todos.sort(key=lambda x: (-x["estimated_hours"], x["filename"], x["line_number"]))
    return todos

def generate_audit_md(todos):
    """Generate the TODO_AUDIT.md content."""
    lines = []
    lines.append("# TODO Audit Report")
    lines.append("")
    lines.append("Comprehensive listing of all TODO comments found in the repository.")
    lines.append("Search is case-insensitive for TODO.")
    lines.append("")
    lines.append(f"**Total TODOs found:** {len(todos)}")
    lines.append(f"**Estimate formula:** `(line_number % 7) + 1` hours")
    lines.append(f"**Sort order:** Estimated hours descending")
    lines.append("")

    # Summary by language
    lang_counts = {}
    for t in todos:
        lang = t["language"]
        lang_counts[lang] = lang_counts.get(lang, 0) + 1

    lines.append("## Summary by Language")
    lines.append("")
    lines.append("| Language | Count |")
    lines.append("|----------|-------|")
    for lang, count in sorted(lang_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| {lang} | {count} |")
    lines.append("")

    # Summary by estimated hours
    hours_counts = {}
    for t in todos:
        h = t["estimated_hours"]
        hours_counts[h] = hours_counts.get(h, 0) + 1

    lines.append("## Summary by Estimated Fix Time")
    lines.append("")
    lines.append("| Estimated Hours | Count |")
    lines.append("|-----------------|-------|")
    for h, count in sorted(hours_counts.items(), key=lambda x: -x[0]):
        lines.append(f"| {h}h | {count} |")
    lines.append("")

    # Detailed listing
    lines.append("## Detailed TODO Listing")
    lines.append("")
    lines.append("| # | Filename | Line | Description | Est. Hours |")
    lines.append("|---|----------|------|-------------|------------|")

    for i, t in enumerate(todos, 1):
        # Truncate long descriptions for table readability
        desc = t["description"]
        if len(desc) > 80:
            desc = desc[:77] + "..."
        # Escape pipe characters in description
        desc = desc.replace("|", "\\|")
        lines.append(f"| {i} | `{t['filename']}` | {t['line_number']} | {desc} | {t['estimated_hours']}h |")

    lines.append("")
    return "\n".join(lines)

def main():
    todos = find_todos()
    content = generate_audit_md(todos)

    output_path = REPO_ROOT / "TODO_AUDIT.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Generated TODO_AUDIT.md with {len(todos)} entries at {output_path}")

if __name__ == "__main__":
    main()
