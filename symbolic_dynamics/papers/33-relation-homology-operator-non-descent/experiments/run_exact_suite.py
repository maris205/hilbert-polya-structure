#!/usr/bin/env python3
"""Run two isolated Paper 33 exact suites and certify byte identity."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
RESULTS = ROOT / "results"
PAYLOADS = [
    "cross_square_complex.json",
    "matched_clone.csv",
    "modulus_homology_census.csv",
    "random_action_controls.csv",
    "source_oracle_certificate.json",
    "summary.json",
    "test_report.json",
    "twist_census.csv",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_once(target: Path) -> str:
    cmd = [
        "python3",
        str(CODE / "generate_results.py"),
        "--cutoff",
        "192",
        "--random-trials",
        "64",
        "--seed",
        "330000",
        "--result-dir",
        str(target),
    ]
    completed = subprocess.run(cmd, cwd=str(CODE), check=True, text=True, capture_output=True)
    return completed.stdout


def main() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="paper33_double_"))
    try:
        a = tmp / "a"
        b = tmp / "b"
        stdout_a = run_once(a)
        stdout_b = run_once(b)
        rows = []
        equal = stdout_a == stdout_b
        for name in PAYLOADS:
            da = digest(a / name)
            db = digest(b / name)
            frozen = digest(RESULTS / name)
            rows.append({"path": name, "run_a": da, "run_b": db, "frozen": frozen, "byte_identical": da == db == frozen})
            equal = equal and rows[-1]["byte_identical"]
        payload = {
            "candidate_id": "SD-C35",
            "command": "python3 code/generate_results.py --cutoff 192 --random-trials 64 --seed 330000",
            "stdout_a_sha256": hashlib.sha256(stdout_a.encode("utf-8")).hexdigest(),
            "stdout_b_sha256": hashlib.sha256(stdout_b.encode("utf-8")).hexdigest(),
            "stdout_identical": stdout_a == stdout_b,
            "payloads": rows,
            "payloads_identical_to_frozen": equal,
        }
        (RESULTS / "double_run_certificate.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps({"candidate_id": "SD-C35", "payloads": len(rows), "identical": equal}))
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    main()
