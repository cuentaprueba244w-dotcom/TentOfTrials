#!/usr/bin/env python3

import argparse
import datetime
import getpass
import json
import os
import platform
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent
DIAGNOSTIC_DIR = ROOT / "diagnostic"
DIAGNOSTIC_CHUNK_SIZE = 40 * 1024 * 1024
ENCRYPTLY_BLOCKER_MESSAGE = "encryptly could not create an archive. You may have timed out; try launching it in the background and waiting for it to finish with no timeout due to a bug in encryptly."


def current_commit_id() -> str:
    """Return the first 4 bytes (8 hex chars) of HEAD for stable per-commit diagnostics."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--verify", "HEAD"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=5,
        )
        commit = result.stdout.strip()
        if result.returncode == 0 and len(commit) >= 8:
            return commit[:8]
    except Exception:
        pass
    return "00000000"


def diagnostic_paths_for_commit() -> tuple[Path, Path, str]:
    """Return stable diagnostic artifact paths under diagnostic/ for the current commit."""
    DIAGNOSTIC_DIR.mkdir(parents=True, exist_ok=True)
    commit_id = current_commit_id()
    logd_path = DIAGNOSTIC_DIR / f"build-{commit_id}.logd"
    metadata_path = DIAGNOSTIC_DIR / f"build-{commit_id}.json"
    return logd_path, metadata_path, commit_id


def split_diagnostic_logd(logd_path: Path, chunk_size: int = DIAGNOSTIC_CHUNK_SIZE) -> list[Path]:
    """Split an oversized .logd into numbered .logd chunks and remove the original."""
    if logd_path.stat().st_size <= chunk_size:
        return [logd_path]

    chunks: list[Path] = []
    stem = logd_path.stem
    with logd_path.open("rb") as source:
        index = 1
        while True:
            data = source.read(chunk_size)
            if not data:
                break
            chunk_path = logd_path.with_name(f"{stem}-part{index:03d}.logd")
            chunk_path.write_bytes(data)
            chunks.append(chunk_path)
            index += 1

    logd_path.unlink()
    return chunks


@dataclass
class Module:
    name: str
    language: str
    dir: Path
    build_cmd: list[str]
    clean_cmd: list[str]
    build_dir: Optional[Path] = None
    env: Optional[dict[str, str]] = None

MODULES = [
    Module(
        name="backend",
        language="Rust",
        dir=ROOT / "backend",
        build_cmd=["cargo", "build"],
        clean_cmd=["cargo", "clean"],
        build_dir=ROOT / "backend" / "target",
        env={"CARGO_TERM_COLOR": "always"},
    ),
    Module(
        name="frontend",
        language="TypeScript",
        dir=ROOT / "frontend",
        build_cmd=["npm", "run", "build"],
        clean_cmd=["rm", "-rf", "node_modules", "dist"],
        build_dir=ROOT / "frontend" / "dist",
        env={"NODE_ENV": "production"},
    ),
    Module(
        name="market",
        language="Go",
        dir=ROOT / "market",
        build_cmd=["go", "build", "-o", "market", "."],
        clean_cmd=["rm", "-f", "market"],
        build_dir=ROOT / "market" / "market",
    ),
    Module(
        name="frailbox",
        language="C",
        dir=ROOT / "frailbox",
        build_cmd=["make"],
        clean_cmd=["make", "distclean"],
        build_dir=ROOT / "frailbox" / "frailbox",
    ),
    Module(
        name="engine",
        language="C++",
        dir=ROOT / "frailbox" / "engine",
        build_cmd=["cmake", "--build", "build"],
        clean_cmd=["rm", "-rf", "build"],
        build_dir=ROOT / "frailbox" / "engine" / "build" / "trial-engine",
    ),
    Module(
        name="compliance",
        language="Java",
        dir=ROOT / "compliance",
        build_cmd=["javac", "-d", "build", "ComplianceAuditor.java"],
        clean_cmd=["rm", "-rf", "build"],
        build_dir=ROOT / "compliance" / "build",
    ),
    Module(
        name="v2-market-stream",
        language="Ruby",
        dir=ROOT / "v2" / "services",
        build_cmd=["ruby", "-c", "market_stream.rb"],
        clean_cmd=["echo", "Ruby has no build artifacts to clean"],
        build_dir=None,
    ),
    Module(
        name="nfc-scanner",
        language="Lua",
        dir=ROOT / "frailbox" / "nfc",
        build_cmd=["luac", "-p", "scanner.lua"],
        clean_cmd=["echo", "Lua has no build artifacts to clean"],
        build_dir=None,
    ),
    Module(
        name="openapi-haskell",
        language="Haskell",
        dir=ROOT / "docs" / "openapi",
        build_cmd=["ghc", "-fno-code", "Types.hs", "Server.hs", "Validate.hs", "Generate.hs"],
        clean_cmd=["rm", "-f", "*.hi", "*.o", "*.hie"],
        build_dir=None,
    ),
    Module(
        name="openapi-tools",
        language="Lua",
        dir=ROOT / "tools",
        build_cmd=["luac", "-p", "openapi_diff.lua", "openapi_mock.lua", "openapi_pact.lua"],
        clean_cmd=["echo", "Nothing to clean"],
        build_dir=None,
    ),
]

ENCRYPTLY_DIR = ROOT / "tools" / "encryptly"
ENCRYPTLY_BINARIES = {
    "linux-x64": ENCRYPTLY_DIR / "linux-x64" / "encryptly",
    "linux-arm64": ENCRYPTLY_DIR / "linux-arm64" / "encryptly",
    "macos-arm64": ENCRYPTLY_DIR / "macos-arm64" / "encryptly",
    "macos-x64": ENCRYPTLY_DIR / "macos-x64" / "encryptly",
    "windows-x64": ENCRYPTLY_DIR / "windows-x64" / "encryptly.exe",
    "windows-arm64": ENCRYPTLY_DIR / "windows-arm64" / "encryptly.exe",
}
LEGACY_ENCRYPTLY_BIN = ENCRYPTLY_DIR / "encryptly"


def _normalize_arch(machine: str) -> Optional[str]:
    machine = machine.lower()
    if machine in {"x86_64", "amd64"}:
        return "x64"
    if machine in {"aarch64", "arm64"}:
        return "arm64"
    return None


def _normalize_os() -> Optional[str]:
    system = platform.system().lower()
    if system == "linux":
        return "linux"
    if system == "darwin":
        return "macos"
    if system == "windows":
        return "windows"
    return None
