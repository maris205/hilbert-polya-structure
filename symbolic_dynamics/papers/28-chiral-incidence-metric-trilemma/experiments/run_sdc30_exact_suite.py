#!/usr/bin/env python3
"""Canonical fresh double-run, integrity audit, and SHA freeze for SD-C30."""

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
VOLATILE = {
    "double_run_certificate.json",
    "integrity_audit.json",
    "SHA256SUMS.txt",
}


def remove_caches() -> None:
    for path in sorted(ROOT.rglob("*"), reverse=True):
        if path.is_dir() and path.name in {"__pycache__", ".pytest_cache"}:
            shutil.rmtree(path)


def command(script: str) -> None:
    environment = os.environ.copy()
    environment["PYTHONHASHSEED"] = "0"
    subprocess.run(
        [sys.executable, str(CODE / script)],
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
    command("generate_sdc30_artifacts.py")
    command("run_sdc30_tests.py")
    command("analyze_sdc30_results.py")
    return snapshot()


def main() -> int:
    RESULTS.mkdir(parents=True, exist_ok=True)
    for path in RESULTS.iterdir():
        if path.is_file():
            path.unlink()
    remove_caches()
    first = run_once()
    second = run_once()
    identical = first == second
    certificate = {
        "candidate_id": "SD-C30",
        "byte_identical": identical,
        "first_hashes": first,
        "second_hashes": second,
        "compared_artifacts": len(first),
        "fresh_results_directory": True,
        "pythonhashseed": "0",
        "runs": 2,
        "commands": [
            "generate_sdc30_artifacts.py",
            "run_sdc30_tests.py",
            "analyze_sdc30_results.py",
        ],
    }
    (RESULTS / "double_run_certificate.json").write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not identical:
        print(json.dumps(certificate, indent=2, sort_keys=True))
        return 1
    remove_caches()
    command("audit_sdc30_artifact_integrity.py")
    command("freeze_sdc30_artifacts.py")
    command("freeze_sdc30_artifacts.py")
    check = subprocess.run(
        [sys.executable, str(CODE / "freeze_sdc30_artifacts.py"), "--check"],
        cwd=ROOT,
        env={**os.environ, "PYTHONHASHSEED": "0"},
        check=False,
    )
    remove_caches()
    print(json.dumps(certificate, indent=2, sort_keys=True))
    return check.returncode


if __name__ == "__main__":
    raise SystemExit(main())
