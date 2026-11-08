#!/usr/bin/env python3
# LEGACY: Test suite for legacy caps audit tool.
"""
tests/test_legacy_caps_audit.py

Tests for tools/legacy_caps_audit.py ensuring full verification of
uppercase LEGACY comment markers across all supported language formats.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

# Add repo root to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.legacy_caps_audit import (
    has_legacy_comment,
    audit_file,
    audit_repository,
)


class TestLegacyCapsAudit(unittest.TestCase):
    def test_has_legacy_comment_python(self):
        content = "# LEGACY: compatibility marker\ndef old_function(): pass\n"
        self.assertTrue(has_legacy_comment(content))

    def test_has_legacy_comment_c_style(self):
        content = "// LEGACY: compatibility marker\nvoid old_func() {}\n"
        self.assertTrue(has_legacy_comment(content))

    def test_has_legacy_comment_c_block(self):
        content = "/* LEGACY: compatibility marker */\nvoid old_func() {}\n"
        self.assertTrue(has_legacy_comment(content))

    def test_has_legacy_comment_multiline_c_block(self):
        content = "/*\n * LEGACY: compatibility marker\n */\nvoid old_func() {}\n"
        self.assertTrue(has_legacy_comment(content))

    def test_has_legacy_comment_html_markdown(self):
        content = "<!-- LEGACY: compatibility marker -->\n# Title\n"
        self.assertTrue(has_legacy_comment(content))

    def test_has_legacy_comment_lua_sql_haskell(self):
        content = "-- LEGACY: compatibility marker\nSELECT 1;\n"
        self.assertTrue(has_legacy_comment(content))

    def test_has_legacy_comment_negative(self):
        # Contains lowercase legacy or code without comment marker
        self.assertFalse(has_legacy_comment("legacy_var = 123\n"))
        self.assertFalse(has_legacy_comment("# regular comment without the caps tag\n"))
        self.assertFalse(has_legacy_comment("// legacy in lowercase\n"))

    def test_audit_temp_directory_violation_and_pass(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            f1 = tmp_path / "bad.py"
            f1.write_text("def run():\n    # calls legacy function\n    pass\n")

            scanned, violations = audit_repository(tmp_path)
            self.assertEqual(len(violations), 1)
            self.assertEqual(violations[0].name, "bad.py")

            # Fix violation
            f1.write_text("# LEGACY: compatibility note\ndef run():\n    # calls legacy function\n    pass\n")
            scanned, violations = audit_repository(tmp_path)
            self.assertEqual(len(violations), 0)

    def test_cli_execution_on_repository(self):
        script_path = REPO_ROOT / "tools" / "legacy_caps_audit.py"
        result = subprocess.run(
            [sys.executable, str(script_path), "--root", str(REPO_ROOT)],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            f"tools/legacy_caps_audit.py failed with code {result.returncode}.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}",
        )


if __name__ == "__main__":
    unittest.main()
