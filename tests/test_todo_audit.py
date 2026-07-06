import tempfile
import unittest
from pathlib import Path

from tools import todo_audit


class TodoAuditTests(unittest.TestCase):
    def test_estimated_hours_uses_line_number_formula(self):
        entry = todo_audit.AuditEntry(Path("example.py"), 13, "# task")

        self.assertEqual(entry.estimated_hours, 7)

    def test_find_entries_is_case_insensitive_and_sorted_by_estimate(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "a.py").write_text("# todo low\n", encoding="utf-8")
            (root / "b.py").write_text("\n\n\n\n\n# ToDo high\n", encoding="utf-8")

            entries = todo_audit.find_entries(root)

        self.assertEqual([entry.path.as_posix() for entry in entries], ["b.py", "a.py"])
        self.assertEqual([entry.estimated_hours for entry in entries], [7, 2])


if __name__ == "__main__":
    unittest.main()
