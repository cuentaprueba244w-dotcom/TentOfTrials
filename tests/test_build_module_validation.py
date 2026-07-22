"""Unit tests for build.py module selection parsing and validation.

Run with: python3 -m pytest tests/test_build_module_validation.py -v
"""

import sys
from pathlib import Path

# Add project root to path so we can import from build.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from build import parse_module_selection, validate_module_names, Module, MODULES


# --- parse_module_selection tests ---

def test_parse_single_valid():
    valid, invalid = parse_module_selection("backend", {"backend", "frontend"})
    assert valid == ["backend"]
    assert invalid == []


def test_parse_multiple_valid():
    valid, invalid = parse_module_selection("backend,frontend", {"backend", "frontend"})
    assert valid == ["backend", "frontend"]
    assert invalid == []


def test_parse_with_spaces():
    valid, invalid = parse_module_selection("backend, frontend", {"backend", "frontend"})
    assert valid == ["backend", "frontend"]
    assert invalid == []


def test_parse_all_keyword():
    valid, invalid = parse_module_selection("all", {"backend", "frontend"})
    assert valid == ["all"]
    assert invalid == []


def test_parse_all_keyword_case_insensitive():
    valid, invalid = parse_module_selection("All", {"backend", "frontend"})
    assert valid == ["all"]
    assert invalid == []


def test_parse_invalid_name():
    valid, invalid = parse_module_selection("nope", {"backend", "frontend"})
    assert valid == []
    assert invalid == ["nope"]


def test_parse_mixed_valid_invalid():
    valid, invalid = parse_module_selection("backend, nope", {"backend", "frontend"})
    assert valid == ["backend"]
    assert invalid == ["nope"]


def test_parse_empty_string():
    valid, invalid = parse_module_selection("", {"backend"})
    assert valid == []
    assert invalid == []


def test_parse_trailing_comma():
    valid, invalid = parse_module_selection("backend,", {"backend"})
    assert valid == ["backend"]
    assert invalid == []


def test_parse_comma_only():
    valid, invalid = parse_module_selection(",", {"backend"})
    assert valid == []
    assert invalid == []


def test_parse_extra_spaces():
    valid, invalid = parse_module_selection("  backend  ,  frontend  ", {"backend", "frontend"})
    assert valid == ["backend", "frontend"]
    assert invalid == []


# --- validate_module_names tests ---

def test_validate_single_valid():
    selected, invalid = validate_module_names(["backend"], MODULES)
    assert len(selected) == 1
    assert selected[0].name == "backend"
    assert invalid == []


def test_validate_multiple_valid():
    selected, invalid = validate_module_names(["backend", "frontend"], MODULES)
    assert len(selected) == 2
    assert {m.name for m in selected} == {"backend", "frontend"}
    assert invalid == []


def test_validate_invalid_returns_empty_selection():
    selected, invalid = validate_module_names(["nope"], MODULES)
    assert selected == []
    assert invalid == ["nope"]


def test_validate_mixed_fails_fast():
    """If any name is invalid, no modules are selected — fail fast."""
    selected, invalid = validate_module_names(["backend", "nope"], MODULES)
    assert selected == []
    assert "nope" in invalid


def test_validate_against_real_modules():
    """All real module names should validate successfully."""
    for m in MODULES:
        selected, invalid = validate_module_names([m.name], MODULES)
        assert len(selected) == 1
        assert invalid == []


def test_validate_all_real_module_names():
    all_names = [m.name for m in MODULES]
    selected, invalid = validate_module_names(all_names, MODULES)
    assert len(selected) == len(MODULES)
    assert invalid == []


if __name__ == "__main__":
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))
