#!/usr/bin/env python3
"""Certify cold-start, freeze, and integrity idempotence for Paper 33."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any


RESULT_PAYLOADS = (
    "classification_certificate.json",
    "cross_square_complex.json",
    "double_run_certificate.json",
    "environment_lock.json",
    "evaluation.json",
    "evaluation_comparison.csv",
    "matched_clone.csv",
    "modulus_homology_census.csv",
    "modulus_source_census.csv",
    "prototype_bridge_certificate.json",
    "random_action_controls.csv",
    "research_lock.json",
    "run_parameters.json",
    "source_oracle_certificate.json",
    "source_separation_certificate.json",
    "source_summary.json",
    "source_test_report.json",
    "summary.json",
    "test_report.json",
    "twist_census.csv",
    "unit_test_report.json",
)
META_RESULT_FILES = (
    "SHA256SUMS.txt",
    "aggregate_sha256.txt",
    "artifact_inventory.json",
    "idempotence_certificate.json",
    "integrity_audit.json",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def run(
    script: Path,
    result_dir: Path,
    *extra: str,
) -> str:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    command = [
        "python3",
        str(script),
        "--result-dir",
        str(result_dir),
        *extra,
    ]
    completed = subprocess.run(
        command,
        cwd=str(script.parent),
        env=environment,
        check=False,
        text=True,
        capture_output=True,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"command failed: {command!r}\n"
            f"stdout:\n{completed.stdout}\n"
            f"stderr:\n{completed.stderr}"
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


def write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def bootstrap_certificate(
    result_dir: Path,
    freeze_a: dict[str, str],
    freeze_b: dict[str, str],
    freeze_stdout_a: str,
    freeze_stdout_b: str,
) -> dict[str, Any]:
    freeze_equal = freeze_a == freeze_b
    stdout_equal = freeze_stdout_a == freeze_stdout_b
    payload: dict[str, Any] = {
        "candidate_id": "SD-C35",
        "audit_type": "cold_start_freeze_and_integrity_idempotence",
        "certificate_stage": "bootstrap",
        "bootstrap_pending_integrity_measurement": True,
        "freeze_first": freeze_a,
        "freeze_second": freeze_b,
        "freeze_stdout_first_sha256": text_digest(freeze_stdout_a),
        "freeze_stdout_second_sha256": text_digest(freeze_stdout_b),
        "freeze_byte_idempotent": freeze_equal,
        "freeze_stdout_idempotent": stdout_equal,
        "integrity_first_sha256": "PENDING_INTEGRITY_MEASUREMENT",
        "integrity_second_sha256": "PENDING_INTEGRITY_MEASUREMENT",
        "integrity_stdout_first_sha256": "PENDING_INTEGRITY_MEASUREMENT",
        "integrity_stdout_second_sha256": "PENDING_INTEGRITY_MEASUREMENT",
        "integrity_byte_idempotent": True,
        "integrity_stdout_idempotent": True,
        "pass": freeze_equal and stdout_equal,
    }
    write_json(result_dir / "idempotence_certificate.json", payload)
    return payload


def certify_directory(
    result_dir: Path,
    freeze_script: Path,
    audit_script: Path,
    cold_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    freeze_stdout_a = run(freeze_script, result_dir)
    freeze_a = freeze_state(result_dir)
    freeze_stdout_b = run(freeze_script, result_dir)
    freeze_b = freeze_state(result_dir)

    base = bootstrap_certificate(
        result_dir,
        freeze_a,
        freeze_b,
        freeze_stdout_a,
        freeze_stdout_b,
    )
    bootstrap_stdout_a = run(
        audit_script,
        result_dir,
        "--allow-bootstrap-idempotence",
    )
    bootstrap_a = digest(result_dir / "integrity_audit.json")
    bootstrap_stdout_b = run(
        audit_script,
        result_dir,
        "--allow-bootstrap-idempotence",
    )
    bootstrap_b = digest(result_dir / "integrity_audit.json")

    preliminary = {
        **base,
        "certificate_stage": "final",
        "bootstrap_pending_integrity_measurement": False,
        "bootstrap_integrity_first_sha256": bootstrap_a,
        "bootstrap_integrity_second_sha256": bootstrap_b,
        "bootstrap_integrity_stdout_first_sha256": text_digest(
            bootstrap_stdout_a
        ),
        "bootstrap_integrity_stdout_second_sha256": text_digest(
            bootstrap_stdout_b
        ),
        "bootstrap_integrity_byte_idempotent": bootstrap_a == bootstrap_b,
        "bootstrap_integrity_stdout_idempotent": (
            bootstrap_stdout_a == bootstrap_stdout_b
        ),
        "integrity_first_sha256": "PENDING_FINAL_INTEGRITY_MEASUREMENT",
        "integrity_second_sha256": "PENDING_FINAL_INTEGRITY_MEASUREMENT",
        "integrity_stdout_first_sha256": "PENDING_FINAL_INTEGRITY_MEASUREMENT",
        "integrity_stdout_second_sha256": "PENDING_FINAL_INTEGRITY_MEASUREMENT",
        "integrity_byte_idempotent": True,
        "integrity_stdout_idempotent": True,
    }
    if cold_summary is not None:
        preliminary["cold_start_without_meta"] = cold_summary
    write_json(result_dir / "idempotence_certificate.json", preliminary)

    final_stdout_a = run(audit_script, result_dir)
    final_a = digest(result_dir / "integrity_audit.json")
    final_stdout_b = run(audit_script, result_dir)
    final_b = digest(result_dir / "integrity_audit.json")

    payload = {
        **preliminary,
        "integrity_first_sha256": final_a,
        "integrity_second_sha256": final_b,
        "integrity_stdout_first_sha256": text_digest(final_stdout_a),
        "integrity_stdout_second_sha256": text_digest(final_stdout_b),
        "integrity_byte_idempotent": final_a == final_b,
        "integrity_stdout_idempotent": final_stdout_a == final_stdout_b,
    }
    payload["pass"] = all((
        payload["freeze_byte_idempotent"],
        payload["freeze_stdout_idempotent"],
        payload["bootstrap_integrity_byte_idempotent"],
        payload["bootstrap_integrity_stdout_idempotent"],
        payload["integrity_byte_idempotent"],
        payload["integrity_stdout_idempotent"],
    ))
    write_json(result_dir / "idempotence_certificate.json", payload)

    post_stdout_a = run(audit_script, result_dir)
    post_a = digest(result_dir / "integrity_audit.json")
    post_stdout_b = run(audit_script, result_dir)
    post_b = digest(result_dir / "integrity_audit.json")
    post_pass = (
        post_a == post_b == final_a == final_b
        and post_stdout_a == post_stdout_b == final_stdout_a == final_stdout_b
    )
    payload["post_certificate_integrity_first_sha256"] = post_a
    payload["post_certificate_integrity_second_sha256"] = post_b
    payload["post_certificate_integrity_stdout_first_sha256"] = text_digest(
        post_stdout_a
    )
    payload["post_certificate_integrity_stdout_second_sha256"] = text_digest(
        post_stdout_b
    )
    payload["post_certificate_integrity_idempotent"] = post_pass
    payload["pass"] = payload["pass"] and post_pass
    write_json(result_dir / "idempotence_certificate.json", payload)

    verification_stdout = run(audit_script, result_dir)
    verification_sha = digest(result_dir / "integrity_audit.json")
    if verification_sha != final_a or verification_stdout != final_stdout_a:
        raise RuntimeError("final integrity output changed after certificate freeze")
    if not payload["pass"]:
        raise RuntimeError("idempotence certification failed")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", default="results")
    args = parser.parse_args()
    code_dir = Path(__file__).resolve().parent
    root = code_dir.parent
    result_dir = Path(args.result_dir)
    if not result_dir.is_absolute():
        result_dir = (root / result_dir).resolve()
    freeze_script = code_dir / "freeze_artifacts.py"
    audit_script = code_dir / "audit_artifact_integrity.py"

    with tempfile.TemporaryDirectory(prefix="paper33_integrity_cold_") as tmp:
        cold_dir = Path(tmp) / "results"
        cold_dir.mkdir(parents=True)
        for name in RESULT_PAYLOADS:
            shutil.copyfile(result_dir / name, cold_dir / name)
        initial_meta = sum((cold_dir / name).exists() for name in META_RESULT_FILES)
        cold_payload = certify_directory(
            cold_dir,
            freeze_script,
            audit_script,
        )
        final_meta = sum((cold_dir / name).exists() for name in META_RESULT_FILES)
        cold_summary = {
            "started_with_meta_files": initial_meta,
            "finished_with_meta_files": final_meta,
            "payload_files_copied": len(RESULT_PAYLOADS),
            "ledger_entry_count": len(
                (cold_dir / "SHA256SUMS.txt").read_text(
                    encoding="utf-8"
                ).splitlines()
            ),
            "final_integrity_sha256": digest(
                cold_dir / "integrity_audit.json"
            ),
            "pass": (
                initial_meta == 0
                and final_meta == len(META_RESULT_FILES)
                and cold_payload["pass"] is True
            ),
        }

    payload = certify_directory(
        result_dir,
        freeze_script,
        audit_script,
        cold_summary=cold_summary,
    )
    if not cold_summary["pass"]:
        raise RuntimeError("cold-start integrity certification failed")
    print(json.dumps({
        "candidate_id": "SD-C35",
        "cold_start": cold_summary["pass"],
        "freeze_idempotent": payload["freeze_byte_idempotent"],
        "integrity_idempotent": payload["integrity_byte_idempotent"],
        "pass": payload["pass"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
