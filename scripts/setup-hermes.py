#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Launch Hermes Agent with Tent of Trials project context pre-loaded.

Usage:
    python3 scripts/setup-hermes.py                # Generate context file
    python3 scripts/setup-hermes.py --launch       # Generate + launch instructions
    python3 scripts/setup-hermes.py --openclaw     # Generate OpenClaw-compatible context

This script prepares the repo for AI agent work by extracting the project
context from CLAUDE.md (and supplementary sources) into a structured format
that Hermes Agent or OpenClaw can consume on startup.

Output:
    .hermes/context.json    — Structured project context (JSON)
    .hermes/prompt.txt      — Ready-to-paste system prompt for Hermes/OpenClaw
"""

import argparse
import json
import io
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parents[1]
HERMES_DIR = REPO_ROOT / ".hermes"
CLAUDE_MD = REPO_ROOT / "CLAUDE.md"


def extract_section(markdown: str, heading: str) -> str:
    """Extract a markdown section by heading name."""
    marker = f"## {heading}"
    lines = markdown.split("\n")
    in_section = False
    result: list[str] = []

    for line in lines:
        if line.startswith(marker):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section:
            result.append(line)

    return "\n".join(result).strip()


def build_context() -> dict:
    """Build a structured project context from CLAUDE.md and repo inspection."""
    if not CLAUDE_MD.exists():
        print("Error: CLAUDE.md not found. Run the CLAUDE.md bounty first?")
        sys.exit(1)

    claude_md = CLAUDE_MD.read_text(encoding="utf-8")

    # Detect available build tools
    tools_available: dict[str, bool] = {}
    for cmd, name in [
        ("cargo", "rust"),
        ("node", "nodejs"),
        ("npm", "npm"),
        ("go", "go"),
        ("make", "make"),
        ("cmake", "cmake"),
        ("javac", "java"),
        ("ruby", "ruby"),
        ("lua5.4", "lua"),
        ("luac", "luac"),
        ("ghc", "haskell"),
        ("python3", "python"),
    ]:
        import shutil
        tools_available[name] = shutil.which(cmd) is not None

    # Count Python files for scale awareness
    py_files = sorted(REPO_ROOT.rglob("*.py"))
    py_file_list = [
        str(p.relative_to(REPO_ROOT)).replace("\\", "/")
        for p in py_files
        if ".git" not in str(p) and "node_modules" not in str(p)
        and "target" not in str(p) and "__pycache__" not in str(p)
    ]

    context = {
        "project": "Tent of Trials",
        "description": "Polyglot trading and risk platform",
        "repository_root": str(REPO_ROOT),
        "generated_from": "CLAUDE.md",
        "overview": extract_section(claude_md, "Project Overview"),
        "repository_structure": extract_section(claude_md, "Repository Structure"),
        "tech_stack": extract_section(claude_md, "Tech Stack"),
        "where_to_start": extract_section(claude_md, "Where to Start"),
        "common_commands": extract_section(claude_md, "Common Commands"),
        "coding_conventions": extract_section(claude_md, "Coding Conventions"),
        "known_pitfalls": extract_section(claude_md, "Known Pitfalls & Gotchas"),
        "build_workflow": extract_section(claude_md, "Build & Diagnostic Workflow"),
        "git_workflow": extract_section(claude_md, "Git Workflow"),
        "bounty_flow": extract_section(claude_md, "Bounty Flow"),
        "environment": {
            "tools_available": tools_available,
            "python_files": py_file_list,
            "python_file_count": len(py_file_list),
            "modules": [
                {"name": "backend", "language": "Rust", "dir": "backend"},
                {"name": "frontend", "language": "TypeScript", "dir": "frontend"},
                {"name": "market", "language": "Go", "dir": "market"},
                {"name": "frailbox", "language": "C", "dir": "frailbox"},
                {"name": "engine", "language": "C++", "dir": "frailbox/engine"},
                {"name": "compliance", "language": "Java", "dir": "compliance"},
                {"name": "v2-market-stream", "language": "Ruby", "dir": "v2/services"},
                {"name": "nfc-scanner", "language": "Lua", "dir": "frailbox/nfc"},
                {"name": "openapi-haskell", "language": "Haskell", "dir": "docs/openapi"},
                {"name": "openapi-tools", "language": "Lua", "dir": "tools"},
            ],
        },
    }
    return context


def generate_prompt(context: dict) -> str:
    """Generate a ready-to-use system prompt for Hermes/OpenClaw."""
    env = context["environment"]
    tools = [k for k, v in env["tools_available"].items() if v]

    return f"""You are working on the Tent of Trials repository, a polyglot trading
and risk platform. You have access to these build tools: {', '.join(tools)}.

## Project Context
{context['overview'][:500]}

## Key Commands
- Build all: python3 build.py
- Build specific: python3 build.py --module <names>
- List modules: python3 build.py --list-modules

## Critical Rules
1. Always run `python3 build.py` after changes and include diagnostic artifacts
2. Do not modify backend/src/legacy/ (deprecated, v1 compat)
3. Use #[deprecated] for Rust public API that will be removed
4. All serde types use #[serde(rename_all = "snake_case")]
5. LEGACY comment markers must be uppercase
6. Never commit secrets, tokens, or credentials

## Module Map
- backend/ → Rust microservices (start at src/protocol/events.rs)
- frontend/ → React 19 + TypeScript (start at src/components/OrderBook.tsx)
- market/ → Go market data (start at pricing/models.go)
- frailbox/ → C hardware layer (start at connector/api.h)
- compliance/ → Java auditor (one file: ComplianceAuditor.java)

For full context, read CLAUDE.md at the repo root.
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Set up Hermes/OpenClaw project context for Tent of Trials"
    )
    parser.add_argument(
        "--launch", action="store_true",
        help="Generate context and print launch instructions"
    )
    parser.add_argument(
        "--openclaw", action="store_true",
        help="Generate OpenClaw-compatible output (default: Hermes)"
    )
    args = parser.parse_args()

    HERMES_DIR.mkdir(exist_ok=True)

    context = build_context()

    # Write structured JSON
    json_path = HERMES_DIR / "context.json"
    json_path.write_text(json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✓ Context written to {json_path}")

    # Write launch prompt
    prompt = generate_prompt(context)
    prompt_path = HERMES_DIR / "prompt.txt"
    prompt_path.write_text(prompt, encoding="utf-8")
    print(f"✓ Launch prompt written to {prompt_path}")

    if args.launch:
        print()
        print("=" * 60)
        print("To launch with this context:")
        print()
        if args.openclaw:
            print("  OpenClaw (paste as system prompt):")
            print(f"    cat {prompt_path}")
            print()
            print("  Or use the OpenClaw CLI:")
            print(f"    openclaw agent --context-file {json_path}")
        else:
            print("  Hermes Agent (paste as initial context):")
            print(f"    cat {prompt_path}")
            print()
            print("  For AI infra Hermes integration:")
            print(f"    Copy .hermes/context.json to your Hermes memory directory")
            print(f"    Add CLAUDE.md to Hermes project registry")
        print("=" * 60)

    # Verify CLAUDE.md is valid (basic check)
    claude_text = CLAUDE_MD.read_text(encoding="utf-8")
    if len(claude_text.splitlines()) > 500:
        print("⚠ Warning: CLAUDE.md exceeds 500 lines")
    if "Where to Start" not in claude_text:
        print("⚠ Warning: CLAUDE.md missing 'Where to Start' section")
    if "python3 build.py" not in claude_text:
        print("⚠ Warning: CLAUDE.md missing build diagnostic workflow")

    return 0


if __name__ == "__main__":
    sys.exit(main())
