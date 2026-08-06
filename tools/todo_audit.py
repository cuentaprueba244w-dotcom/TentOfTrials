#!/usr/bin/env python3
"""
TODO Audit Script
=================
Scans the entire repository for TODO comments (case-insensitive)
and generates a comprehensive TODO_AUDIT.md report.

Usage:
    python3 tools/todo_audit.py
"""

import os
import re
from pathlib import Path
from typing import List, Tuple


def estimate_fix_time(line_number: int) -> int:
    """Calculate estimated fix time using the formula: (line_number % 7) + 1"""
    return (line_number % 7) + 1


def find_all_todos(root_dir: str) -> List[Tuple[str, int, str]]:
    """
    Recursively search all files for TODO comments (case-insensitive).
    
    Returns:
        List of tuples: (filename, line_number, line_content)
    """
    # File extensions to scan
    scan_extensions = {
        '.py', '.js', '.ts', '.md', '.yml', '.yaml', '.json',
        '.toml', '.cfg', '.ini', '.txt', '.sh', '.bash', '.html',
        '.css', '.rs', '.go', '.java', '.c', '.cpp', '.h', '.hpp',
        '.rb', '.php', '.swift', '.kt', '.scala', '.r', '.R',
        '.sql', '.graphql', '.proto', '.dockerfile', '.cmake',
        '.xml', '.properties', '.env', '.conf', '.makefile'
    }
    
    # Patterns to skip (binary files, build artifacts, etc.)
    skip_dirs = {
        '__pycache__', '.git', 'node_modules', '.venv', 'venv',
        'target', 'build', 'dist', '.next', '.cache', 'diagnostic'
    }
    
    todos: List[Tuple[str, int, str]] = []
    todo_pattern = re.compile(r'TODO', re.IGNORECASE)
    
    root_path = Path(root_dir)
    
    for file_path in sorted(root_path.rglob('*')):
        # Skip directories
        if file_path.is_dir():
            continue
            
        # Skip if any parent directory should be skipped
        parts = file_path.relative_to(root_path).parts
        if any(part in skip_dirs for part in parts):
            continue
        
        # Skip if not a file with scannable extension
        if file_path.suffix.lower() not in scan_extensions:
            # Also scan files without extension (like Dockerfile, Makefile)
            if file_path.name.lower() not in {'dockerfile', 'makefile', 'readme', 'license'}:
                continue
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    if todo_pattern.search(line):
                        # Use relative path from root
                        rel_path = str(file_path.relative_to(root_path)).replace('\\', '/')
                        todos.append((rel_path, line_num, line.strip()))
        except (PermissionError, IOError):
            pass
    
    return todos


def generate_report(todos: List[Tuple[str, int, str]], output_path: str) -> None:
    """Generate TODO_AUDIT.md report sorted by estimated hours descending."""
    
    # Add estimated hours and sort
    todos_with_estimates = [
        (filename, line_num, content, estimate_fix_time(line_num))
        for filename, line_num, content in todos
    ]
    
    # Sort by estimated hours descending
    todos_with_estimates.sort(key=lambda x: x[3], reverse=True)
    
    # Generate Markdown report
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# TODO Audit Report\n\n")
        f.write(f"Generated automatically by `tools/todo_audit.py`\n\n")
        f.write(f"**Total TODOs found:** {len(todos_with_estimates)}\n\n")
        
        # Summary by estimated hours
        hour_counts = {}
        for _, _, _, hours in todos_with_estimates:
            hour_counts[hours] = hour_counts.get(hours, 0) + 1
        
        f.write("## Summary by Estimated Fix Time\n\n")
        f.write("| Estimated Hours | Count |\n")
        f.write("|-----------------|-------|\n")
        for hours in sorted(hour_counts.keys(), reverse=True):
            f.write(f"| {hours}h | {hour_counts[hours]} |\n")
        f.write("\n")
        
        # Full table
        f.write("## Full TODO List\n\n")
        f.write("Sorted by estimated fix time (descending).\n\n")
        f.write("| # | File | Line | Estimated Hours | TODO Content |\n")
        f.write("|---|------|------|-----------------|--------------|\n")
        
        for idx, (filename, line_num, content, hours) in enumerate(todos_with_estimates, 1):
            # Escape pipe characters in content
            safe_content = content.replace('|', '\\|')
            f.write(f"| {idx} | {filename} | {line_num} | {hours}h | {safe_content} |\n")
        
        # Summary statistics
        f.write("\n## Statistics\n\n")
        total_hours = sum(hours for _, _, _, hours in todos_with_estimates)
        f.write(f"- **Total TODOs:** {len(todos_with_estimates)}\n")
        f.write(f"- **Total estimated hours:** {total_hours}h\n")
        f.write(f"- **Average per TODO:** {total_hours / len(todos_with_estimates):.1f}h\n")
        
        # By file
        file_counts = {}
        for filename, _, _, _ in todos_with_estimates:
            file_counts[filename] = file_counts.get(filename, 0) + 1
        
        f.write("\n## TODOs by File\n\n")
        f.write("| File | Count |\n")
        f.write("|------|-------|\n")
        for filename, count in sorted(file_counts.items(), key=lambda x: x[1], reverse=True):
            f.write(f"| {filename} | {count} |\n")


def main():
    """Main entry point."""
    # Get repository root (parent of tools/)
    script_dir = Path(__file__).parent.resolve()
    repo_root = script_dir.parent
    
    print(f"Scanning repository: {repo_root}")
    print("Searching for TODO comments (case-insensitive)...")
    
    todos = find_all_todos(str(repo_root))
    print(f"Found {len(todos)} TODOs")
    
    output_path = repo_root / "TODO_AUDIT.md"
    generate_report(todos, str(output_path))
    
    print(f"Report generated: {output_path}")
    print(f"Total estimated hours: {sum(estimate_fix_time(ln) for _, ln, _ in todos)}h")


if __name__ == '__main__':
    main()
