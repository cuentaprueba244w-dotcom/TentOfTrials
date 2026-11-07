import unittest
import sys
import os
import importlib.util

spec = importlib.util.spec_from_file_location("build", "build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

class TestModuleValidation(unittest.TestCase):
    def test_parse_module_selection(self):
        self.assertEqual(build.parse_module_selection("backend"), ["backend"])
        self.assertEqual(build.parse_module_selection("frontend, market"), ["frontend", "market"])
        self.assertEqual(build.parse_module_selection("  api  ,  core"), ["api", "core"])
        self.assertEqual(build.parse_module_selection(""), [])

    def test_validate_modules(self):
        available = ["frontend", "backend", "market"]
        
        is_valid, not_found = build.validate_modules(["frontend"], available)
        self.assertTrue(is_valid)
        self.assertEqual(len(not_found), 0)
        
        is_valid, not_found = build.validate_modules(["frontend", "unknown"], available)
        self.assertFalse(is_valid)
        self.assertIn("unknown", not_found)

if __name__ == "__main__":
    unittest.main()
