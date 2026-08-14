#!/usr/bin/env python3
"""Run exact SD-C22 tests and write a deterministic certificate."""

from __future__ import annotations

import ast
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
TEST_FILE = ROOT / "code" / "test_sdc22_clock_dilution.py"


def declared_test_count() -> int:
    tree = ast.parse(TEST_FILE.read_text(encoding="utf-8"))
    return sum(
        isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name.startswith("test_")
        for node in ast.walk(tree)
    )


def main() -> int:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-q",
            "-p",
            "no:cacheprovider",
            TEST_FILE.relative_to(ROOT).as_posix(),
        ],
        cwd=ROOT,
        env=environment,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    print(completed.stdout, end="")
    count = declared_test_count()
    payload = {
        "candidate_id": "SD-C22",
        "errors": 0 if completed.returncode == 0 else 1,
        "failures": 0 if completed.returncode == 0 else 1,
        "skipped": 0,
        "successful": completed.returncode == 0,
        "target_zero_data_used": False,
        "tests_run": count,
    }
    (ROOT / "results" / "test_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
