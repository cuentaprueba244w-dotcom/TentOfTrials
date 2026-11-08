import os
import subprocess
import sys
import unittest
from pathlib import Path

# Ensure repo root is in python path
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import build
from build import (
    MODULES,
    Module,
    list_modules,
    parse_and_validate_modules,
    parse_module_selection,
    validate_modules,
)


class TestParseModuleSelection(unittest.TestCase):
    def test_single_module(self):
        self.assertEqual(parse_module_selection("backend"), ["backend"])

    def test_multiple_comma_separated(self):
        self.assertEqual(
            parse_module_selection("backend,frontend,market"),
            ["backend", "frontend", "market"],
        )

    def test_optional_spaces(self):
        self.assertEqual(
            parse_module_selection("backend, frontend"),
            ["backend", "frontend"],
        )
        self.assertEqual(
            parse_module_selection("backend , market"),
            ["backend", "market"],
        )
        self.assertEqual(
            parse_module_selection("  backend  ,   frontend  ,  market  "),
            ["backend", "frontend", "market"],
        )

    def test_empty_and_whitespace(self):
        self.assertEqual(parse_module_selection(""), [])
        self.assertEqual(parse_module_selection("   "), [])
        self.assertEqual(parse_module_selection(None), [])

    def test_consecutive_commas(self):
        self.assertEqual(
            parse_module_selection("backend,,frontend, ,market"),
            ["backend", "frontend", "market"],
        )


class TestValidateModules(unittest.TestCase):
    def test_all_valid(self):
        is_valid, invalid = validate_modules(
            ["backend", "frontend"], ["backend", "frontend", "market"]
        )
        self.assertTrue(is_valid)
        self.assertEqual(invalid, [])

    def test_some_invalid(self):
        is_valid, invalid = validate_modules(
            ["backend", "invalid_mod", "frontend", "not_real"],
            ["backend", "frontend", "market"],
        )
        self.assertFalse(is_valid)
        self.assertEqual(invalid, ["invalid_mod", "not_real"])

    def test_module_objects_as_available(self):
        mock_modules = [
            Module(name="mod_a", language="C", dir=ROOT, build_cmd=[], clean_cmd=[]),
            Module(name="mod_b", language="Go", dir=ROOT, build_cmd=[], clean_cmd=[]),
        ]
        is_valid, invalid = validate_modules(["mod_a"], mock_modules)
        self.assertTrue(is_valid)
        self.assertEqual(invalid, [])

        is_valid, invalid = validate_modules(["mod_c"], mock_modules)
        self.assertFalse(is_valid)
        self.assertEqual(invalid, ["mod_c"])

    def test_default_available(self):
        is_valid, invalid = validate_modules(["backend", "compliance"])
        self.assertTrue(is_valid)
        self.assertEqual(invalid, [])

        is_valid, invalid = validate_modules(["unknown_xyz"])
        self.assertFalse(is_valid)
        self.assertEqual(invalid, ["unknown_xyz"])


class TestParseAndValidateModules(unittest.TestCase):
    def test_all_keyword(self):
        valid, invalid = parse_and_validate_modules("all", MODULES)
        self.assertEqual(valid, [m.name for m in MODULES])
        self.assertEqual(invalid, [])

    def test_valid_comma_string_with_spaces(self):
        valid, invalid = parse_and_validate_modules(
            "backend ,  market,  frontend", MODULES
        )
        self.assertEqual(valid, ["backend", "market", "frontend"])
        self.assertEqual(invalid, [])

    def test_invalid_names_reported(self):
        valid, invalid = parse_and_validate_modules(
            "backend , bogus_one, market, bogus_two", MODULES
        )
        self.assertEqual(valid, ["backend", "market"])
        self.assertEqual(invalid, ["bogus_one", "bogus_two"])

    def test_empty_selection(self):
        valid, invalid = parse_and_validate_modules("", MODULES)
        self.assertEqual(valid, [])
        self.assertEqual(invalid, [])

        valid, invalid = parse_and_validate_modules(None, MODULES)
        self.assertEqual(valid, [])
        self.assertEqual(invalid, [])

    def test_list_input(self):
        valid, invalid = parse_and_validate_modules(
            ["backend", "bad_mod"], ["backend", "market"]
        )
        self.assertEqual(valid, ["backend"])
        self.assertEqual(invalid, ["bad_mod"])

    def test_default_modules(self):
        valid, invalid = parse_and_validate_modules("backend, market")
        self.assertEqual(valid, ["backend", "market"])
        self.assertEqual(invalid, [])


class TestListModules(unittest.TestCase):
    def test_list_modules_default(self):
        output = list_modules()
        self.assertIn("Available modules:", output)
        for m in MODULES:
            self.assertIn(m.name, output)
            self.assertIn(m.language, output)
            self.assertIn(str(m.dir.relative_to(ROOT)), output)

    def test_list_modules_custom(self):
        custom = [
            Module(
                name="custom-service",
                language="Python",
                dir=ROOT / "custom",
                build_cmd=["python3", "setup.py"],
                clean_cmd=["rm", "-rf", "dist"],
            )
        ]
        output = list_modules(custom)
        self.assertIn("custom-service", output)
        self.assertIn("Python", output)
        self.assertIn("custom", output)
        self.assertIn("python3 setup.py", output)


class TestCliIntegration(unittest.TestCase):
    def run_build_py(self, *args):
        cmd = [sys.executable, str(ROOT / "build.py"), *args]
        return subprocess.run(
            cmd,
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )

    def test_cli_list_modules_flag(self):
        res = self.run_build_py("--list-modules")
        self.assertEqual(res.returncode, 0)
        self.assertIn("Available modules:", res.stdout)
        self.assertIn("backend (Rust)", res.stdout)
        self.assertIn("dir: backend", res.stdout)
        self.assertIn("build: cargo build", res.stdout)

    def test_cli_list_flag_backward_compatible(self):
        res = self.run_build_py("--list")
        self.assertEqual(res.returncode, 0)
        self.assertIn("Available modules:", res.stdout)
        self.assertIn("market (Go)", res.stdout)

    def test_cli_invalid_module_fails_fast(self):
        res = self.run_build_py("-m", "invalid_module_xyz")
        self.assertEqual(res.returncode, 1)
        self.assertIn("✗ Unknown modules: invalid_module_xyz", res.stdout)
        self.assertIn("Available: backend, frontend", res.stdout)
        # Verify it failed fast before running prerequisites or build commands
        self.assertNotIn("Checking prerequisites...", res.stdout)
        self.assertNotIn("Building", res.stdout)

    def test_cli_multiple_invalid_modules_with_spaces(self):
        res = self.run_build_py("-m", "backend , bad1 , market , bad2")
        self.assertEqual(res.returncode, 1)
        self.assertIn("✗ Unknown modules: bad1, bad2", res.stdout)
        self.assertIn("Available: backend", res.stdout)
        self.assertNotIn("Checking prerequisites...", res.stdout)

    def test_cli_help_includes_list_modules(self):
        res = self.run_build_py("--help")
        self.assertEqual(res.returncode, 0)
        self.assertIn("--list-modules", res.stdout)


if __name__ == "__main__":
    unittest.main()
