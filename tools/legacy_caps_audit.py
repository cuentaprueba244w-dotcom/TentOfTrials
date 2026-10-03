import os
import sys

def audit():
    violations = []
    # Directories/files to exclude
    exclude = {'.git', 'node_modules', 'target', 'build', '.idea', '.vscode', '.cache'}
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if file == 'legacy_caps_audit.py':
                continue
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if 'legacy' in content.lower():
                        if 'LEGACY' not in content:
                            violations.append(path)
            except Exception:
                continue
                
    if violations:
        print("Files missing LEGACY marker:")
        for v in violations:
            print(f"  {v}")
        return False
    return True

if __name__ == "__main__":
    if not audit():
        sys.exit(1)
