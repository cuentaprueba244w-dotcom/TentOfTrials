#!/usr/bin/env python3
"""
TODO Audit Report Generator
Scans repository for TODO comments across all source files, computes estimated
fix times, and outputs a formatted Markdown report (TODO_AUDIT.md).
"""

import os
import re
import sys
from typing import List, Dict, Any

TODO_PATTERN = re.compile(r'\btodo\b', re.IGNORECASE)
EXCLUDE_DIRS = {'.git', 'diagnostic', '__pycache__', '.pytest_cache', 'node_modules', '.venv', 'venv'}
EXCLUDE_FILES = {'TODO_AUDIT.md', 'package-lock.json', 'yarn.lock'}

def scan_todos(root_dir: str = '.') -> List[Dict[str, Any]]:
    entries = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if file in EXCLUDE_FILES or file.endswith('.logd') or file.endswith('.png') or file.endswith('.jpg'):
                continue
            filepath = os.path.relpath(os.path.join(root, file), root_dir).replace('\\', '/')
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as fp:
                    for line_no, line in enumerate(fp, start=1):
                        if TODO_PATTERN.search(line):
                            est_hours = (line_no % 7) + 1
                            snippet = line.strip()
                            entries.append({
                                'file': filepath,
                                'line': line_no,
                                'hours': est_hours,
                                'comment': snippet
                            })
            except Exception as e:
                pass

    # Sort descending by estimated hours, then by file and line for stable ordering
    entries.sort(key=lambda x: (-x['hours'], x['file'], x['line']))
    return entries

def generate_report(entries: List[Dict[str, Any]], output_path: str = 'TODO_AUDIT.md') -> None:
    total_items = len(entries)
    total_hours = sum(e['hours'] for e in entries)

    lines = [
        "# 📋 Repository Technical Debt & TODO Audit Report",
        "",
        "Centralized audit of all `TODO` comments across languages in the repository.",
        "",
        "## 📊 Summary Statistics",
        f"- **Total TODO Items**: {total_items}",
        f"- **Estimated Total Effort**: {total_hours} hours (~{total_hours / 8:.1f} engineering days)",
        f"- **Formula**: `(line_number % 7) + 1` hours per item",
        "",
        "## 🗂️ Audit Table (Sorted by Estimated Fix Time Descending)",
        "",
        "| Filename | Line | Est. Hours | Snippet |",
        "| :--- | :---: | :---: | :--- |"
    ]

    for item in entries:
        # Escape markdown pipe symbols in snippet
        clean_snippet = item['comment'].replace('|', '\\|').replace('`', "'")
        if len(clean_snippet) > 80:
            clean_snippet = clean_snippet[:77] + '...'
        lines.append(f"| `{item['file']}` | {item['line']} | {item['hours']}h | `{clean_snippet}` |")

    lines.append("")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Successfully generated {output_path} with {total_items} items ({total_hours}h estimated).")

if __name__ == '__main__':
    items = scan_todos('.')
    generate_report(items, 'TODO_AUDIT.md')
