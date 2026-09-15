import unittest
from build import parse_module_selection, validate_module_selection, Module
from pathlib import Path

class TestModuleValidation(unittest.TestCase):
    def setUp(self):
        self.mock_modules = [
            Module(name="backend", language="Rust", dir=Path("backend"), build_cmd=["cargo"], clean_cmd=["cargo"]),
            Module(name="frontend", language="TypeScript", dir=Path("frontend"), build_cmd=["npm"], clean_cmd=["npm"]),
            Module(name="market", language="Go", dir=Path("market"), build_cmd=["go"], clean_cmd=["go"])
        ]

    def test_parse_all(self):
        self.assertEqual(parse_module_selection("all"), ["backend", "frontend", "market", "frailbox", "engine", "compliance", "v2-market-stream", "nfc-scanner", "openapi-haskell", "openapi-tools"])
        self.assertEqual(parse_module_selection(""), ["backend", "frontend", "market", "frailbox", "engine", "compliance", "v2-market-stream", "nfc-scanner", "openapi-haskell", "openapi-tools"])

    def test_parse_comma_separated_with_spaces(self):
        result = parse_module_selection("backend, frontend ,  market  ")
        self.assertEqual(result, ["backend", "frontend", "market"])

    def test_validate_valid_modules(self):
        selected, invalid = validate_module_selection(["backend", "market"], self.mock_modules)
        self.assertEqual(len(selected), 2)
        self.assertEqual([m.name for m in selected], ["backend", "market"])
        self.assertEqual(invalid, [])

    def test_validate_invalid_modules(self):
        selected, invalid = validate_module_selection(["backend", "fake_module", "another_fake"], self.mock_modules)
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0].name, "backend")
        self.assertEqual(invalid, ["fake_module", "another_fake"])

if __name__ == "__main__":
    unittest.main()
