import unittest

import build


class BuildModuleSelectionTests(unittest.TestCase):
    def test_parse_module_names_allows_comma_separated_names_with_spaces(self):
        self.assertEqual(
            build.parse_module_names("backend, frontend,market"),
            ["backend", "frontend", "market"],
        )

    def test_select_all_modules(self):
        selected = build.select_modules("all")

        self.assertEqual(selected, build.MODULES)

    def test_select_valid_subset_preserves_requested_order(self):
        selected = build.select_modules("frontend, backend")

        self.assertEqual([module.name for module in selected], ["frontend", "backend"])

    def test_invalid_module_lists_invalid_and_valid_names(self):
        with self.assertRaises(ValueError) as context:
            build.select_modules("backend, typo")

        message = str(context.exception)
        self.assertIn("typo", message)
        self.assertIn("backend", message)
        self.assertIn("frontend", message)

    def test_empty_module_selection_is_invalid(self):
        with self.assertRaises(ValueError) as context:
            build.select_modules(" , ")

        self.assertIn("No module names supplied", str(context.exception))

    def test_format_module_details_includes_name_language_and_build_command(self):
        details = build.format_module_details(build.MODULES[:1])

        self.assertIn("backend (Rust)", details)
        self.assertIn("dir: backend", details)
        self.assertIn("build: cargo build", details)


if __name__ == "__main__":
    unittest.main()
