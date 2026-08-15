#!/usr/bin/env python3
"""Certify scientific stability and repeated ledger freezing for SD-C38."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    double = json.loads((RESULTS / "double_run_certificate.json").read_text(encoding="utf-8"))
    cold = json.loads((RESULTS / "cold_start_certificate.json").read_text(encoding="utf-8"))
    current_science = {name: digest(RESULTS / name) for name in double["run_a_hashes"]}
    science_unchanged = current_science == double["run_a_hashes"] == cold["cold_hashes"]
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    command = [sys.executable, "-B", str(ROOT / "code" / "freeze_artifacts.py")]
    subprocess.run(command, cwd=ROOT, env=environment, check=True, capture_output=True, text=True)
    first_ledger = (RESULTS / "SHA256SUMS.txt").read_bytes()
    first_aggregate = (RESULTS / "aggregate_sha256.txt").read_bytes()
    subprocess.run(command, cwd=ROOT, env=environment, check=True, capture_output=True, text=True)
    second_ledger = (RESULTS / "SHA256SUMS.txt").read_bytes()
    second_aggregate = (RESULTS / "aggregate_sha256.txt").read_bytes()
    payload = {
        "schema": "SD-C38-idempotence-certificate-v1",
        "candidate_id": "SD-C38",
        "scientific_payload_count": len(current_science),
        "scientific_payloads_unchanged": science_unchanged,
        "fresh_a_b_status": double["status"],
        "cold_c_status": cold["status"],
        "freeze_runs": 2,
        "ledger_byte_identical": first_ledger == second_ledger,
        "aggregate_byte_identical": first_aggregate == second_aggregate,
        "sha256sums_sha256": hashlib.sha256(first_ledger).hexdigest(),
        "aggregate_sha256": first_aggregate.decode("utf-8").strip(),
    }
    payload["status"] = "PASS" if all((science_unchanged, payload["ledger_byte_identical"], payload["aggregate_byte_identical"], double["status"] == "PASS", cold["status"] == "PASS")) else "FAIL"
    write_json(RESULTS / "idempotence_certificate.json", payload)
    print(json.dumps({"candidate_id": "SD-C38", "status": payload["status"]}, sort_keys=True))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
