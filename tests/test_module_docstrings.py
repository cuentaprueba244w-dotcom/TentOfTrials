"""Tests verifying that all Python files in the repository have module-level docstrings."""

import ast
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

EXCLUDE_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
    "dist",
    "build",
    "target",
    ".venv",
    "venv",
}


class TestModuleDocstrings(unittest.TestCase):
    """Test case verifying module-level docstrings across all Python modules."""

    def test_all_python_files_have_module_docstrings(self):
        """Ensure every .py file in the repository has a non-empty module-level docstring."""
        python_files = []
        for path in REPO_ROOT.rglob("*.py"):
            if any(part in EXCLUDE_DIRS for part in path.parts):
                continue
            python_files.append(path)

        self.assertGreater(len(python_files), 0, "No Python files found")

        missing_docstrings = []
        for py_path in sorted(python_files):
            rel_path = py_path.relative_to(REPO_ROOT)
            with open(py_path, "r", encoding="utf-8") as f:
                content = f.read()

            try:
                tree = ast.parse(content, filename=str(rel_path))
            except SyntaxError as e:
                missing_docstrings.append(f"{rel_path}: SyntaxError - {e}")
                continue

            docstring = ast.get_docstring(tree)
            if not docstring or not docstring.strip():
                missing_docstrings.append(f"{rel_path}: Missing module docstring")

        self.assertEqual(
            missing_docstrings,
            [],
            f"The following Python files lack module docstrings:\n" + "\n".join(missing_docstrings),
        )


if __name__ == "__main__":
    unittest.main()
