#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

def audit_directory(root_dir: str) -> list[str]:
    violations = []
    
    # Extensions to check
    extensions = {'.py', '.ts', '.js', '.rs', '.go', '.c', '.cpp', '.h', '.java', '.rb', '.lua', '.hs'}
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip node_modules, target, build, etc.
        dirnames[:] = [d for d in dirnames if d not in {'.git', 'node_modules', 'target', 'build', 'diagnostic', 'dist'}]
        
        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext not in extensions:
                continue
                
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # If "legacy" (case-insensitive) is present
                if re.search(r'\blegacy\b', content, re.IGNORECASE):
                    # Check if "LEGACY" (exactly uppercase) is present in a comment context
                    # Simplification: just check if the string "LEGACY" exists in the file.
                    if 'LEGACY' not in content:
                        violations.append(filepath)
            except Exception as e:
                pass
                
    return violations

if __name__ == '__main__':
    root = str(Path(__file__).parent.parent)
    violations = audit_directory(root)
    if violations:
        print("Violations found (file contains 'legacy' but no 'LEGACY' in uppercase):")
        for v in violations:
            print("  " + v)
        sys.exit(1)
    else:
        print("All files passed legacy caps audit.")
        sys.exit(0)
