#!/usr/bin/env python3
"""Run two isolated canonical Paper 33 pipelines and certify byte identity."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
RESULTS = ROOT / "results"
PAYLOADS = (
    "environment_lock.json",
    "run_parameters.json",
    "research_lock.json",
    "modulus_source_census.csv",
    "matched_clone.csv",
    "random_action_controls.csv",
    "twist_census.csv",
    "cross_square_complex.json",
    "source_oracle_certificate.json",
    "source_separation_certificate.json",
    "source_summary.json",
    "source_test_report.json",
    "modulus_homology_census.csv",
    "summary.json",
    "test_report.json",
    "classification_certificate.json",
    "prototype_bridge_certificate.json",
    "evaluation.json",
    "evaluation_comparison.csv",
    "unit_test_report.json",
)
STAGES = (
    ("locks", "write_run_locks.py"),
    ("source", "source_generator.py"),
    ("separation", "audit_source_separation.py"),
    ("classification", "post_census_classifier.py"),
    ("evaluation", "independent_evaluator.py"),
    ("tests", "run_tests.py"),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_once(target: Path) -> dict[str, str]:
    target.mkdir(parents=True, exist_ok=True)
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    stdout: dict[str, str] = {}
    for stage, script in STAGES:
        command = [
            "python3",
            str(CODE / script),
            "--result-dir",
            str(target),
        ]
        completed = subprocess.run(
            command,
            cwd=str(CODE),
            env=environment,
            check=True,
            text=True,
            capture_output=True,
        )
        stdout[stage] = completed.stdout
    return stdout


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="paper33_canonical_double_") as tmp:
        temporary = Path(tmp)
        a = temporary / "a"
        b = temporary / "b"
        stdout_a = run_once(a)
        stdout_b = run_once(b)

        rows = []
        all_equal = stdout_a == stdout_b
        for name in PAYLOADS:
            run_a = digest(a / name)
            run_b = digest(b / name)
            frozen = digest(RESULTS / name)
            identical = run_a == run_b == frozen
            rows.append({
                "path": name,
                "run_a": run_a,
                "run_b": run_b,
                "frozen": frozen,
                "byte_identical": identical,
            })
            all_equal = all_equal and identical

        stdout_rows = {
            stage: {
                "run_a_sha256": hashlib.sha256(
                    stdout_a[stage].encode("utf-8")
                ).hexdigest(),
                "run_b_sha256": hashlib.sha256(
                    stdout_b[stage].encode("utf-8")
                ).hexdigest(),
                "identical": stdout_a[stage] == stdout_b[stage],
            }
            for stage, _ in STAGES
        }
        payload = {
            "candidate_id": "SD-C35",
            "pipeline": [script for _, script in STAGES],
            "parameters": {
                "cutoff": 192,
                "random_trials": 64,
                "random_seed_start": 330000,
            },
            "stdout": stdout_rows,
            "stdout_identical": stdout_a == stdout_b,
            "payloads": rows,
            "payload_count": len(rows),
            "payloads_identical_to_frozen": all_equal,
            "fresh_temporary_directories": 2,
        }
        (RESULTS / "double_run_certificate.json").write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(json.dumps({
            "candidate_id": "SD-C35",
            "payloads": len(rows),
            "identical": all_equal,
        }, sort_keys=True))
        if not all_equal:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
