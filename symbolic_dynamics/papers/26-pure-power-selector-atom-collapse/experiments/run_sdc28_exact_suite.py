#!/usr/bin/env python3
"""Canonical deterministic double-run for the SD-C28 exact suite."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
EXCLUDED = {"double_run_certificate.json", "integrity_audit.json", "SHA256SUMS.txt"}


def run(relative: str) -> None:
    environment = dict(os.environ)
    environment["PYTHONHASHSEED"] = "0"
    subprocess.run([sys.executable, str(ROOT / relative)], cwd=ROOT, env=environment, check=True)


def snapshot() -> dict[str, str]:
    paths = sorted((ROOT / "code").glob("*.py"))
    paths.extend(sorted(path for path in RESULTS.iterdir() if path.is_file() and path.name not in EXCLUDED))
    return {
        path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
    }


def combined_digest(items: dict[str, str]) -> str:
    text = "\n".join(f"{digest}  {path}" for path, digest in sorted(items.items())) + "\n"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def clean_caches() -> None:
    for path in ROOT.rglob("__pycache__"):
        if path.is_dir():
            shutil.rmtree(path)
    for path in ROOT.rglob(".pytest_cache"):
        if path.is_dir():
            shutil.rmtree(path)


def execute() -> None:
    run("code/generate_sdc28_artifacts.py")
    run("code/run_sdc28_tests.py")
    run("code/analyze_sdc28_results.py")
    clean_caches()


def main() -> int:
    execute()
    first = snapshot()
    execute()
    second = snapshot()
    identical = first == second
    payload = {
        "candidate_id": "SD-C28",
        "scope": "code_and_generated_results_only",
        "artifact_count": len(first),
        "first_combined_sha256": combined_digest(first),
        "second_combined_sha256": combined_digest(second),
        "byte_identical": identical,
        "differing_paths": sorted(set(first) | set(second)) if not identical else [],
        "pythonhashseed": "0",
    }
    (RESULTS / "double_run_certificate.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not identical:
        raise SystemExit("double-run mismatch")
    run("code/audit_sdc28_artifact_integrity.py")
    run("code/freeze_sdc28_artifacts.py")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
