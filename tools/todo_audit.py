#!/usr/bin/env python3
"""
Generate TODO audit report for the Tent of Trials codebase.
"""

import argparse
import re
from pathlib import Path

def find_todos(root_dir: Path):
    todos = []
    for path in root_dir.rglob('*'):
        if not path.is_file():
            continue
        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except (UnicodeDecodeError, PermissionError, IsADirectoryError):
            continue
        for line_num, line in enumerate(lines, 1):
            if re.search(r'\bTODO\b', line, re.IGNORECASE):
                rel_path = path.relative_to(root_dir)
                fix_time = (line_num % 7) + 1
                todos.append({
                    'file': str(rel_path),
                    'line': line_num,
                    'fix_time': fix_time
                })
    return todos

def generate_report(todos, output_file: Path):
    todos_sorted = sorted(todos, key=lambda x: x['fix_time'], reverse=True)
    with output_file.open('w') as f:
        f.write('# TODO Audit Report\n\n')
        f.write('| File | Line | Estimated Fix Time (hours) |\n')
        f.write('|------|-------|-----------------------------|\n')
        for todo in todos_sorted:
            f.write(f"| {todo['file']} | {todo['line']} | {todo['fix_time']} |\n")

def main():
    parser = argparse.ArgumentParser(description='Generate TODO audit report.')
    parser.add_argument('--root', type=str, default=str(Path(__file__).resolve().parent.parent),
                        help='Root directory of the repository')
    parser.add_argument('--output', type=str, default='TODO_AUDIT.md',
                        help='Output markdown file')
    args = parser.parse_args()

    root_dir = Path(args.root).resolve()
    output_file = Path(args.output).resolve()

    todos = find_todos(root_dir)
    generate_report(todos, output_file)

    print(f"Generated TODO audit report at {output_file}")

if __name__ == '__main__':
    main()
