"""Tests for module selection helpers in build.py."""

import unittest
from unittest.mock import patch

import build


class ParseModuleNamesTests(unittest.TestCase):
    """Unit tests for parse_module_names()."""

    def test_single_module(self):
        result = build.parse_module_names("backend")
        self.assertEqual(result, ["backend"])

    def test_comma_separated(self):
        result = build.parse_module_names("backend,frontend,market")
        self.assertEqual(result, ["backend", "frontend", "market"])

    def test_spaces_around_commas(self):
        result = build.parse_module_names("backend, frontend , market")
        self.assertEqual(result, ["backend", "frontend", "market"])

    def test_trailing_whitespace(self):
        result = build.parse_module_names("  backend  ")
        self.assertEqual(result, ["backend"])

    def test_empty_string(self):
        result = build.parse_module_names("")
        self.assertEqual(result, [])

    def test_whitespace_only(self):
        result = build.parse_module_names("   ")
        self.assertEqual(result, [])

    def test_all_keyword(self):
        result = build.parse_module_names("all")
        self.assertEqual(result, ["all"])

    def test_duplicate_names_preserved(self):
        result = build.parse_module_names("backend,backend")
        self.assertEqual(result, ["backend", "backend"])

    def test_case_sensitivity(self):
        result = build.parse_module_names("Backend,BACKEND")
        self.assertEqual(result, ["Backend", "BACKEND"])


class ValidateModuleNamesTests(unittest.TestCase):
    """Unit tests for validate_module_names()."""

    def setUp(self):
        self.modules = build.MODULES

    def test_all_valid(self):
        names = ["backend", "frontend"]
        selected, invalid = build.validate_module_names(names, self.modules)
        self.assertEqual(len(selected), 2)
        self.assertEqual(invalid, [])

    def test_all_invalid(self):
        names = ["typo1", "typo2"]
        selected, invalid = build.validate_module_names(names, self.modules)
        self.assertEqual(selected, [])
        self.assertEqual(invalid, ["typo1", "typo2"])

    def test_mixed_valid_invalid(self):
        names = ["backend", "typo"]
        selected, invalid = build.validate_module_names(names, self.modules)
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0].name, "backend")
        self.assertEqual(invalid, ["typo"])

    def test_empty_name_list(self):
        selected, invalid = build.validate_module_names([], self.modules)
        self.assertEqual(selected, [])
        self.assertEqual(invalid, [])

    def test_case_mismatch_is_invalid(self):
        names = ["Backend"]
        selected, invalid = build.validate_module_names(names, self.modules)
        self.assertEqual(selected, [])
        self.assertEqual(invalid, ["Backend"])

    def test_preserves_selection_order(self):
        names = ["frontend", "backend", "market"]
        selected, _ = build.validate_module_names(names, self.modules)
        self.assertEqual([m.name for m in selected], names)

    def test_all_valid_modules_accepted(self):
        names = [m.name for m in self.modules]
        selected, invalid = build.validate_module_names(names, self.modules)
        self.assertEqual(len(selected), len(self.modules))
        self.assertEqual(invalid, [])


class ModuleFullListTests(unittest.TestCase):
    """Sanity checks on the MODULES registry."""

    def test_all_modules_are_loaded(self):
        self.assertGreater(len(build.MODULES), 0)
        names = {m.name for m in build.MODULES}
        self.assertIn("backend", names)
        self.assertIn("frontend", names)

    def test_no_duplicate_module_names(self):
        names = [m.name for m in build.MODULES]
        self.assertEqual(len(names), len(set(names)))


if __name__ == "__main__":
    unittest.main()
