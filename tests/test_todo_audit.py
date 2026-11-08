#!/usr/bin/env python3
"""Comprehensive unit tests for tools.todo_audit module."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

# Ensure repository root is on sys.path
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools import todo_audit


class TestTodoAuditEstimateFormula(unittest.TestCase):
    """Test calculation of fix time estimates using formula (line % 7) + 1."""

    def test_formula_values(self):
        expected_mappings = {
            1: 2,   # (1 % 7) + 1 = 2
            2: 3,   # (2 % 7) + 1 = 3
            3: 4,   # (3 % 7) + 1 = 4
            4: 5,   # (4 % 7) + 1 = 5
            5: 6,   # (5 % 7) + 1 = 6
            6: 7,   # (6 % 7) + 1 = 7
            7: 1,   # (7 % 7) + 1 = 1
            8: 2,   # (8 % 7) + 1 = 2
            13: 7,  # (13 % 7) + 1 = 7
            14: 1,  # (14 % 7) + 1 = 1
            34: 7,  # (34 % 7) + 1 = 7
            76: 7,  # (76 % 7) + 1 = 7
            300: 7, # (300 % 7) + 1 = 7
            609: 1, # (609 % 7) + 1 = 1
        }
        for line_num, expected_hours in expected_mappings.items():
            with self.subTest(line_number=line_num):
                hours = todo_audit.calculate_estimated_hours(line_num)
                self.assertEqual(hours, expected_hours)

    def test_audit_entry_property(self):
        entry = todo_audit.AuditEntry(Path("foo/bar.py"), 13, "# task marker")
        self.assertEqual(entry.estimated_hours, 7)
        self.assertEqual(entry.line_number, 13)
        self.assertEqual(entry.path, Path("foo/bar.py"))
        self.assertEqual(entry.text, "# task marker")


class TestPathFiltering(unittest.TestCase):
    """Test skipping logic for directories, binary extensions, and generated files."""

    def test_skippable_directories(self):
        root = Path("/repo")
        self.assertTrue(todo_audit.is_skippable_path(root / ".git" / "config", root))
        self.assertTrue(todo_audit.is_skippable_path(root / ".github" / "ci.yml", root))
        self.assertTrue(todo_audit.is_skippable_path(root / "diagnostic" / "build.json", root))
        self.assertTrue(todo_audit.is_skippable_path(root / "node_modules" / "pkg" / "index.js", root))
        self.assertTrue(todo_audit.is_skippable_path(root / "target" / "debug" / "main.rs", root))
        self.assertTrue(todo_audit.is_skippable_path(root / "build" / "out.txt", root))
        self.assertTrue(todo_audit.is_skippable_path(root / "dist" / "bundle.js", root))
        self.assertTrue(todo_audit.is_skippable_path(root / ".hidden" / "file.py", root))

    def test_skippable_files_and_extensions(self):
        root = Path("/repo")
        self.assertTrue(todo_audit.is_skippable_path(root / "TODO_AUDIT.md", root))
        self.assertTrue(todo_audit.is_skippable_path(root / "tools" / "todo_audit.py", root))
        self.assertTrue(todo_audit.is_skippable_path(root / "tests" / "test_todo_audit.py", root))
        self.assertTrue(todo_audit.is_skippable_path(root / "assets" / "logo.png", root))
        self.assertTrue(todo_audit.is_skippable_path(root / "bin" / "app.exe", root))
        self.assertTrue(todo_audit.is_skippable_path(root / "lib" / "module.so", root))
        self.assertTrue(todo_audit.is_skippable_path(root / "bundle.logd", root))

    def test_valid_source_files_not_skipped(self):
        root = Path("/repo")
        self.assertFalse(todo_audit.is_skippable_path(root / "src" / "main.py", root))
        self.assertFalse(todo_audit.is_skippable_path(root / "backend" / "src" / "lib.rs", root))
        self.assertFalse(todo_audit.is_skippable_path(root / "docs" / "guide.md", root))


class TestTodoDiscoveryAndSorting(unittest.TestCase):
    """Test discovery of case-insensitive markers and sorting rules."""

    def test_case_insensitive_matching(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            test_file = root / "sample.py"
            test_file.write_text(
                "line 1: TODO upper\n"
                "line 2: normal line\n"
                "line 3: todo lower\n"
                "line 4: ToDo mixed\n"
                "line 5: tODo varied\n",
                encoding="utf-8",
            )
            entries = todo_audit.find_entries(root)
            self.assertEqual(len(entries), 4)
            found_lines = [e.line_number for e in entries]
            self.assertIn(1, found_lines)
            self.assertIn(3, found_lines)
            self.assertIn(4, found_lines)
            self.assertIn(5, found_lines)

    def test_sorting_order(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            # Create file A where line 1 -> 2 hours
            (root / "z_file.py").write_text("# TODO low priority\n", encoding="utf-8")
            # Create file B where line 6 -> 7 hours
            (root / "a_file.py").write_text(
                "\n\n\n\n\n# TODO high priority\n", encoding="utf-8"
            )

            entries = todo_audit.find_entries(root)
            self.assertEqual(len(entries), 2)
            # 7 hours should precede 2 hours regardless of filename alphabetical order
            self.assertEqual(entries[0].path.as_posix(), "a_file.py")
            self.assertEqual(entries[0].estimated_hours, 7)
            self.assertEqual(entries[1].path.as_posix(), "z_file.py")
            self.assertEqual(entries[1].estimated_hours, 2)

    def test_secondary_and_tertiary_sort(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            # Both have 7 hours on line 6: (6 % 7) + 1 = 7
            content = "\n\n\n\n\n# TODO item\n"
            (root / "b.py").write_text(content, encoding="utf-8")
            (root / "a.py").write_text(content, encoding="utf-8")

            entries = todo_audit.find_entries(root)
            self.assertEqual(len(entries), 2)
            self.assertEqual(entries[0].path.as_posix(), "a.py")
            self.assertEqual(entries[1].path.as_posix(), "b.py")


class TestReportRendering(unittest.TestCase):
    """Test markdown report generation and formatting."""

    def test_render_report_pipe_escaping(self):
        entry = todo_audit.AuditEntry(
            Path("src/script.py"),
            6,
            "// TODO: handle condition A | condition B",
        )
        report = todo_audit.render_report([entry])

        self.assertIn("# Repository TODO Audit", report)
        self.assertIn("Total entries: 1", report)
        self.assertIn("| Estimated hours | File | Line | Text |", report)
        self.assertIn("`src/script.py`", report)
        self.assertIn("condition A \\| condition B", report)
        self.assertIn("| 7 |", report)


class TestCliExecution(unittest.TestCase):
    """Test CLI main entry point and --check flag."""

    def test_main_generates_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            src_file = root / "app.py"
            src_file.write_text("# TODO first\n", encoding="utf-8")
            out_file = root / "TODO_AUDIT.md"

            ret = todo_audit.main(["--root", str(root), "--output", str(out_file)])
            self.assertEqual(ret, 0)
            self.assertTrue(out_file.exists())
            content = out_file.read_text(encoding="utf-8")
            self.assertIn("Total entries: 1", content)

    def test_main_check_flag(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            src_file = root / "app.py"
            src_file.write_text("# TODO first\n", encoding="utf-8")
            out_file = root / "TODO_AUDIT.md"

            # Check fails when file does not exist
            self.assertEqual(
                todo_audit.main(["--root", str(root), "--output", str(out_file), "--check"]),
                1,
            )

            # Generate file
            self.assertEqual(
                todo_audit.main(["--root", str(root), "--output", str(out_file)]),
                0,
            )

            # Check passes when file is up to date
            self.assertEqual(
                todo_audit.main(["--root", str(root), "--output", str(out_file), "--check"]),
                0,
            )

            # Modify source -> check fails
            src_file.write_text("# TODO first\n# TODO second\n", encoding="utf-8")
            self.assertEqual(
                todo_audit.main(["--root", str(root), "--output", str(out_file), "--check"]),
                1,
            )


class TestRepoAuditIntegration(unittest.TestCase):
    """Test audit against the real repository."""

    def test_repo_has_322_entries_and_valid_structure(self):
        entries = todo_audit.find_entries(REPO_ROOT)
        self.assertEqual(len(entries), 322)

        # Check bounds of estimated hours
        for entry in entries:
            self.assertGreaterEqual(entry.estimated_hours, 1)
            self.assertLessEqual(entry.estimated_hours, 7)
            self.assertGreater(entry.line_number, 0)

        # Verify sorted descending
        hours_list = [e.estimated_hours for e in entries]
        self.assertEqual(hours_list, sorted(hours_list, reverse=True))


if __name__ == "__main__":
    unittest.main()
