#!/usr/bin/env python3
# LEGACY
"""Apply #[deprecated] annotations to legacy Rust module public functions."""

from pathlib import Path
import re

ROOT = Path(r"D:\Code\TentOfTrials-bounty\backend\src\legacy")

DEPRECATED_ATTR = '#[deprecated(note = "Use v2 API instead. See migration guide.")]'
IMPL_COMMENT = "// DEPRECATED: All methods in this impl block use legacy types."

FILES = {
    "mod.rs": {
        "tally": 3,
        "module_fns": ["init", "shutdown", "status"],
        "impls": [],
    },
    "migrations.rs": {
        "tally": 7,
        "module_fns": [
            "get_migration_description",
            "get_all_migration_ids",
            "get_dependencies",
            "has_dependency",
            "rollback_migration",
            "validate_migration_sql",
            "intercept_migration",
        ],
        "impls": [],
    },
    "deprecations.rs": {
        "tally": 20,
        "module_fns": [
            "convert_to_legacy",
            "legacy_normalize_phone_number",
            "print_deprecation_warnings",
            "migrate_legacy_module",
            "health_check",
        ],
        "impls": [
            "LegacyUuid",
            "DeprecatedEntity",
            "LegacyPagination",
            "LegacyCache",
        ],
    },
    "v1_compat.rs": {
        "tally": 12,
        "module_fns": [],
        "impls": [
            "V1StatusCode",
            "V1ApiResponse",
            "V1PaginationParams",
            "V1WebhookEvent",
            "V1ResourceMapper",
            "V1ErrorCode",
            "V1UserAgent",
        ],
    },
}


def add_or_update_tally(text: str, tally: int) -> str:
    target = f"// Deprecated functions in this file: {tally}"

    if text.startswith("// Deprecated functions in this file:"):
        return re.sub(
            r"^// Deprecated functions in this file:\s*\d+\s*\n",
            target + "\n",
            text,
            count=1,
        )

    return target + "\n" + text


def has_deprecated_before(lines: list[str], index: int) -> bool:
    j = index - 1

    while j >= 0:
        stripped = lines[j].strip()

        if stripped == "":
            j -= 1
            continue

        if stripped.startswith("#[deprecated"):
            return True

        if stripped.startswith("#[") or stripped.startswith("//"):
            j -= 1
            continue

        break

    return False


def add_deprecated_to_module_fns(text: str, fn_names: list[str]) -> str:
    lines = text.splitlines(keepends=True)
    fn_set = set(fn_names)
    result: list[str] = []

    fn_pattern = re.compile(r"^(\s*)pub\s+fn\s+([A-Za-z0-9_]+)\s*(?:<|\()")

    for i, line in enumerate(lines):
        match = fn_pattern.match(line)

        if match:
            indent, fn_name = match.groups()

            if fn_name in fn_set and not has_deprecated_before(lines, i):
                newline = "\n" if line.endswith("\n") else ""
                result.append(f"{indent}{DEPRECATED_ATTR}{newline}")

        result.append(line)

    return "".join(result)


def add_impl_comments(text: str, impl_names: list[str]) -> str:
    lines = text.splitlines(keepends=True)
    result: list[str] = []

    for i, line in enumerate(lines):
        result.append(line)

        for impl_name in impl_names:
            pattern = re.compile(
                rf"^(\s*)impl(?:\s*<[^>]+>)?\s+(?:[A-Za-z0-9_:]+::)?{re.escape(impl_name)}(?:\s*<[^>]+>)?\s*\{{?\s*$"
            )

            match = pattern.match(line)
            if not match:
                continue

            indent = match.group(1)
            comment_line = f"{indent}    {IMPL_COMMENT}\n"

            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            if next_line.strip() != IMPL_COMMENT:
                result.append(comment_line)

            break

    return "".join(result)


def process_file(filename: str, config: dict) -> None:
    path = ROOT / filename

    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")

    original = path.read_text(encoding="utf-8")

    updated = original
    updated = add_or_update_tally(updated, config["tally"])
    updated = add_deprecated_to_module_fns(updated, config["module_fns"])
    updated = add_impl_comments(updated, config["impls"])

    if updated != original:
        path.write_text(updated, encoding="utf-8")
        print(f"updated: {path}")
    else:
        print(f"unchanged: {path}")


def main() -> None:
    for filename, config in FILES.items():
        process_file(filename, config)

    print("done")


if __name__ == "__main__":
    main()
