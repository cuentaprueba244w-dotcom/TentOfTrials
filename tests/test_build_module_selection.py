import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("tent_build", ROOT / "build.py")
assert SPEC is not None
assert SPEC.loader is not None
build = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = build
SPEC.loader.exec_module(build)


class BuildModuleSelectionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.modules = [
            build.Module(
                name="backend",
                language="Rust",
                dir=build.ROOT / "backend",
                build_cmd=["cargo", "build"],
                clean_cmd=["cargo", "clean"],
            ),
            build.Module(
                name="frontend",
                language="TypeScript",
                dir=build.ROOT / "frontend",
                build_cmd=["npm", "run", "build"],
                clean_cmd=["rm", "-rf", "dist"],
            ),
            build.Module(
                name="market",
                language="Go",
                dir=build.ROOT / "market",
                build_cmd=["go", "build", "."],
                clean_cmd=["rm", "-f", "market"],
            ),
        ]

    def test_parse_module_names_allows_optional_spaces(self) -> None:
        self.assertEqual(
            build.parse_module_names("backend, frontend,market"),
            ["backend", "frontend", "market"],
        )

    def test_select_all_modules(self) -> None:
        selected, invalid = build.select_modules("all", self.modules)

        self.assertEqual([module.name for module in selected], ["backend", "frontend", "market"])
        self.assertEqual(invalid, [])

    def test_select_named_modules_preserves_request_order(self) -> None:
        selected, invalid = build.select_modules("market, backend", self.modules)

        self.assertEqual([module.name for module in selected], ["market", "backend"])
        self.assertEqual(invalid, [])

    def test_select_modules_reports_invalid_name(self) -> None:
        selected, invalid = build.select_modules("backend, typo", self.modules)

        self.assertEqual(selected, [])
        self.assertEqual(invalid, ["typo"])

    def test_select_modules_reports_empty_token(self) -> None:
        selected, invalid = build.select_modules("backend,,market", self.modules)

        self.assertEqual(selected, [])
        self.assertEqual(invalid, ["<empty>"])

    def test_module_detail_lines_include_name_language_and_commands(self) -> None:
        details = build.module_detail_lines(self.modules)

        self.assertIn("backend (Rust)", details)
        self.assertIn("  dir: backend", details)
        self.assertIn("  build: cargo build", details)


if __name__ == "__main__":
    unittest.main()
