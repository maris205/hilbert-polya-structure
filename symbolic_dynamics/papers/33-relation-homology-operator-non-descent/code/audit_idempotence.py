#!/usr/bin/env python3
"""Certify idempotence of Paper 33 freeze and integrity stages."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(script: Path, result_dir: Path) -> str:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        ["python3", str(script), "--result-dir", str(result_dir)],
        cwd=str(script.parent),
        env=environment,
        check=True,
        text=True,
        capture_output=True,
    )
    return completed.stdout


def freeze_state(result_dir: Path) -> dict[str, str]:
    return {
        name: digest(result_dir / name)
        for name in (
            "SHA256SUMS.txt",
            "aggregate_sha256.txt",
            "artifact_inventory.json",
        )
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", default="results")
    args = parser.parse_args()
    code_dir = Path(__file__).resolve().parent
    root = code_dir.parent
    result_dir = Path(args.result_dir)
    if not result_dir.is_absolute():
        result_dir = root / result_dir
    freeze_script = code_dir / "freeze_artifacts.py"
    audit_script = code_dir / "audit_artifact_integrity.py"

    freeze_stdout_a = run(freeze_script, result_dir)
    freeze_a = freeze_state(result_dir)
    freeze_stdout_b = run(freeze_script, result_dir)
    freeze_b = freeze_state(result_dir)

    audit_stdout_a = run(audit_script, result_dir)
    audit_a = digest(result_dir / "integrity_audit.json")
    audit_stdout_b = run(audit_script, result_dir)
    audit_b = digest(result_dir / "integrity_audit.json")

    payload = {
        "candidate_id": "SD-C35",
        "audit_type": "freeze_and_integrity_idempotence",
        "freeze_first": freeze_a,
        "freeze_second": freeze_b,
        "freeze_stdout_first_sha256": hashlib.sha256(
            freeze_stdout_a.encode("utf-8")
        ).hexdigest(),
        "freeze_stdout_second_sha256": hashlib.sha256(
            freeze_stdout_b.encode("utf-8")
        ).hexdigest(),
        "freeze_byte_idempotent": freeze_a == freeze_b,
        "freeze_stdout_idempotent": freeze_stdout_a == freeze_stdout_b,
        "integrity_first_sha256": audit_a,
        "integrity_second_sha256": audit_b,
        "integrity_stdout_first_sha256": hashlib.sha256(
            audit_stdout_a.encode("utf-8")
        ).hexdigest(),
        "integrity_stdout_second_sha256": hashlib.sha256(
            audit_stdout_b.encode("utf-8")
        ).hexdigest(),
        "integrity_byte_idempotent": audit_a == audit_b,
        "integrity_stdout_idempotent": audit_stdout_a == audit_stdout_b,
    }
    payload["pass"] = all((
        payload["freeze_byte_idempotent"],
        payload["freeze_stdout_idempotent"],
        payload["integrity_byte_idempotent"],
        payload["integrity_stdout_idempotent"],
    ))
    (result_dir / "idempotence_certificate.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "candidate_id": "SD-C35",
        "pass": payload["pass"],
    }, sort_keys=True))
    if not payload["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
