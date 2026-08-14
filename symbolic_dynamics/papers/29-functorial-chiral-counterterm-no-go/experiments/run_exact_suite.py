#!/usr/bin/env python3
"""Canonical two-fresh-run, integrity-audit, and SHA freeze for SD-C31."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
RESULTS = ROOT / "results"
VOLATILE = {"double_run_certificate.json", "integrity_audit.json", "SHA256SUMS.txt"}


def remove_caches() -> None:
    for path in sorted(ROOT.rglob("*"), reverse=True):
        if path.is_dir() and path.name in {"__pycache__", ".pytest_cache"}:
            shutil.rmtree(path)


def clear_results() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    for path in RESULTS.iterdir():
        if path.is_file() or path.is_symlink():
            path.unlink()


def command(script: str, *arguments: str) -> None:
    environment = os.environ.copy()
    environment["PYTHONHASHSEED"] = "0"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    subprocess.run(
        [sys.executable, str(CODE / script), *arguments],
        cwd=ROOT,
        env=environment,
        check=True,
    )


def snapshot() -> dict[str, str]:
    paths = sorted(CODE.glob("*.py"))
    paths.extend(
        sorted(
            path
            for path in RESULTS.iterdir()
            if path.is_file() and path.name not in VOLATILE
        )
    )
    return {
        path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
    }


def run_once() -> dict[str, str]:
    command("generate_results.py", "--output", str(RESULTS))
    command("independent_evaluator.py", "--results", str(RESULTS))
    command("run_tests.py", "--output", str(RESULTS))
    command("analyze_results.py", "--results", str(RESULTS))
    return snapshot()


def main() -> int:
    remove_caches()
    clear_results()
    first = run_once()
    clear_results()
    second = run_once()
    identical = first == second
    certificate = {
        "candidate_id": "SD-C31",
        "byte_identical": identical,
        "first_hashes": first,
        "second_hashes": second,
        "compared_artifacts": len(first),
        "fresh_results_directory_each_run": True,
        "pythonhashseed": "0",
        "pythondontwritebytecode": "1",
        "runs": 2,
        "commands": [
            "generate_results.py --output results",
            "independent_evaluator.py --results results",
            "run_tests.py --output results",
            "analyze_results.py --results results",
        ],
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }
    (RESULTS / "double_run_certificate.json").write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not identical:
        print(json.dumps(certificate, indent=2, sort_keys=True))
        return 1
    remove_caches()
    command("audit_artifact_integrity.py")
    command("freeze_artifacts.py")
    command("freeze_artifacts.py")
    environment = {**os.environ, "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1"}
    check = subprocess.run(
        [sys.executable, str(CODE / "freeze_artifacts.py"), "--check"],
        cwd=ROOT,
        env=environment,
        check=False,
    )
    remove_caches()
    print(json.dumps(certificate, indent=2, sort_keys=True))
    return check.returncode


if __name__ == "__main__":
    raise SystemExit(main())
