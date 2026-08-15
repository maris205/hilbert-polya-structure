#!/usr/bin/env python3
"""Certify freeze, integrity, cold-start, and metadata-seal stability."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CODE = ROOT / "code"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run(script: str, *arguments: str) -> str:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    completed = subprocess.run(
        [sys.executable, "-B", str(CODE / script), *arguments],
        cwd=ROOT,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode:
        raise RuntimeError(
            f"{script} failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
        )
    return completed.stdout


def freeze_state() -> dict[str, str]:
    return {
        name: digest(RESULTS / name)
        for name in ("SHA256SUMS.txt", "aggregate_sha256.txt", "artifact_inventory.json")
    }


def main() -> int:
    preliminary = {
        "schema_version": "SD-C36-idempotence-v2",
        "certificate_stage": "bootstrap",
        "freeze_byte_idempotent": True,
        "freeze_stdout_idempotent": True,
        "integrity_byte_idempotent": True,
        "integrity_stdout_idempotent": True,
        "cold_start_stability": True,
        "metadata_seal_stability": True,
        "research_lock_pointer_stability": True,
        "status": "PASS",
    }
    write_json(RESULTS / "idempotence_certificate.json", preliminary)
    write_json(
        RESULTS / "integrity_audit.json",
        {"schema_version": "SD-C36-integrity-v2", "certificate_stage": "bootstrap", "status": "PASS"},
    )

    freeze_stdout_a = run("freeze_artifacts.py")
    freeze_a = freeze_state()
    freeze_stdout_b = run("freeze_artifacts.py")
    freeze_b = freeze_state()
    integrity_stdout_a = run("audit_integrity.py")
    integrity_a = digest(RESULTS / "integrity_audit.json")
    integrity_stdout_b = run("audit_integrity.py")
    integrity_b = digest(RESULTS / "integrity_audit.json")

    cold = json.loads((RESULTS / "cold_start_certificate.json").read_text(encoding="utf-8"))
    seal = json.loads((RESULTS / "metadata_seal_stability.json").read_text(encoding="utf-8"))
    research_lock_pointer_stability = all(
        seal.get("research_lock_checks", {}).values()
    )
    passed = all(
        (
            freeze_a == freeze_b,
            freeze_stdout_a == freeze_stdout_b,
            integrity_a == integrity_b,
            integrity_stdout_a == integrity_stdout_b,
            cold["status"] == "PASS",
            cold["byte_identical_to_published_science"],
            seal["status"] == "PASS",
            seal["scientific_payload_byte_identical"],
            research_lock_pointer_stability,
        )
    )
    payload = {
        "schema_version": "SD-C36-idempotence-v2",
        "certificate_stage": "final",
        "freeze_first": freeze_a,
        "freeze_second": freeze_b,
        "freeze_stdout_first_sha256": text_digest(freeze_stdout_a),
        "freeze_stdout_second_sha256": text_digest(freeze_stdout_b),
        "freeze_byte_idempotent": freeze_a == freeze_b,
        "freeze_stdout_idempotent": freeze_stdout_a == freeze_stdout_b,
        "integrity_first_sha256": integrity_a,
        "integrity_second_sha256": integrity_b,
        "integrity_stdout_first_sha256": text_digest(integrity_stdout_a),
        "integrity_stdout_second_sha256": text_digest(integrity_stdout_b),
        "integrity_byte_idempotent": integrity_a == integrity_b,
        "integrity_stdout_idempotent": integrity_stdout_a == integrity_stdout_b,
        "cold_start_stability": cold["status"] == "PASS",
        "metadata_seal_stability": seal["status"] == "PASS",
        "research_lock_sha256": digest(RESULTS / "research_lock.json"),
        "research_lock_pointer_stability": research_lock_pointer_stability,
        "status": "PASS" if passed else "FAIL",
    }
    write_json(RESULTS / "idempotence_certificate.json", payload)

    post_stdout_a = run("audit_integrity.py")
    post_a = digest(RESULTS / "integrity_audit.json")
    post_stdout_b = run("audit_integrity.py")
    post_b = digest(RESULTS / "integrity_audit.json")
    if not (
        passed
        and post_a == post_b == integrity_a == integrity_b
        and post_stdout_a == post_stdout_b == integrity_stdout_a == integrity_stdout_b
    ):
        raise RuntimeError("post-certificate integrity is not byte stable")
    run("freeze_artifacts.py", "--check")
    if payload["status"] != "PASS":
        raise RuntimeError("stability certification failed")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
