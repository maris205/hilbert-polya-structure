#!/usr/bin/env python3
"""Certify SD-C38 freeze idempotence and mutable-metadata stability."""

from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

import yaml

from freeze_artifacts import LEDGER_PATHS


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
ROUTE_RELATIVE = "evaluations/route_a/SD-C38/2026-08-15.yaml"
ROUTE_CARD = ROOT / ROUTE_RELATIVE
MANIFEST = ROOT / "PAPER_MANIFEST.sha256"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
DUMMY_COMMIT = "0123456789abcdef0123456789abcdef01234567"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def environment(root: Path) -> dict[str, str]:
    values = dict(os.environ)
    values["PYTHONDONTWRITEBYTECODE"] = "1"
    values["PYTHONHASHSEED"] = "0"
    values["PYTHONPATH"] = str(root / "code")
    return values


def run_script(root: Path, name: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-B", str(root / "code" / name)],
        cwd=root,
        env=environment(root),
        check=True,
        capture_output=True,
        text=True,
    )


def ledger_valid(root: Path, expected_bytes: bytes) -> bool:
    ledger = root / "results" / "SHA256SUMS.txt"
    if ledger.read_bytes() != expected_bytes:
        return False
    rows: list[tuple[str, str]] = []
    for line in expected_bytes.decode("utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if match is None:
            return False
        rows.append((match.group(1), match.group(2)))
    return (
        len(rows) == len(LEDGER_PATHS) == 43
        and [relative for _, relative in rows] == list(LEDGER_PATHS)
        and ROUTE_RELATIVE not in {relative for _, relative in rows}
        and "PAPER_MANIFEST.sha256" not in {relative for _, relative in rows}
        and all(
            (root / relative).is_file()
            and digest(root / relative) == expected
            for expected, relative in rows
        )
    )


def manifest_state(path: Path) -> tuple[bool, str | None]:
    return (path.is_file(), digest(path) if path.is_file() else None)


def route_variants(original: dict[str, object]) -> tuple[dict[str, object], dict[str, object]]:
    pending = copy.deepcopy(original)
    pending["source_commit"] = PENDING
    pending["code_commit"] = PENDING
    pending["source_lock"]["code_commit"] = PENDING
    pending["freeze_note"] = (
        "Two-stage provenance is intentionally pending. The Stage-1 canonical "
        "SHA ledger excludes this mutable Route card. All three provenance fields "
        "carry PENDING_FIRST_ARTIFACT_COMMIT and may later be replaced "
        "simultaneously by one identical lowercase 40-hex artifact commit in a "
        "metadata-only Stage 2."
    )
    sealed = copy.deepcopy(pending)
    sealed["source_commit"] = DUMMY_COMMIT
    sealed["code_commit"] = DUMMY_COMMIT
    sealed["source_lock"]["code_commit"] = DUMMY_COMMIT
    sealed["freeze_note"] = (
        "Two-stage provenance is sealed for metadata-stability testing at "
        f"{DUMMY_COMMIT}. All three provenance fields bind the same immutable "
        "dummy commit. The Route card remains excluded from the Stage-1 canonical "
        "SHA ledger."
    )
    return pending, sealed


def write_yaml(path: Path, value: dict[str, object]) -> None:
    text = yaml.safe_dump(value, sort_keys=False, allow_unicode=True)
    path.write_text(text.rstrip("\n") + "\n", encoding="utf-8")


def run_projected_integrity(root: Path) -> bytes:
    run_script(root, "audit_integrity.py")
    payload = (root / "results" / "integrity_audit.json").read_bytes()
    parsed = json.loads(payload)
    if parsed["status"] != "PASS" or parsed["pass"] is not True:
        raise RuntimeError("projected integrity audit did not pass")
    return payload


def main() -> int:
    double = json.loads((RESULTS / "double_run_certificate.json").read_text(encoding="utf-8"))
    cold = json.loads((RESULTS / "cold_start_certificate.json").read_text(encoding="utf-8"))
    current_science = {name: digest(RESULTS / name) for name in double["run_a_hashes"]}
    science_unchanged = current_science == double["run_a_hashes"] == cold["cold_hashes"]

    authority_route_before = ROUTE_CARD.read_bytes()
    authority_manifest_before = manifest_state(MANIFEST)
    write_json(
        RESULTS / "idempotence_certificate.json",
        {
            "schema": "SD-C38-idempotence-certificate-v2",
            "candidate_id": "SD-C38",
            "status": "PENDING_METADATA_STABILITY_AUDIT",
        },
    )

    run_script(ROOT, "freeze_artifacts.py")
    first_ledger = (RESULTS / "SHA256SUMS.txt").read_bytes()
    first_aggregate = (RESULTS / "aggregate_sha256.txt").read_bytes()
    run_script(ROOT, "freeze_artifacts.py")
    second_ledger = (RESULTS / "SHA256SUMS.txt").read_bytes()
    second_aggregate = (RESULTS / "aggregate_sha256.txt").read_bytes()
    ledger_43_of_43 = ledger_valid(ROOT, first_ledger)

    original_route = yaml.safe_load(authority_route_before.decode("utf-8"))
    pending_route, sealed_route = route_variants(original_route)
    metadata_outputs: dict[str, bytes] = {}
    copied_ledgers_valid: list[bool] = []
    with tempfile.TemporaryDirectory(prefix="paper36-metadata-stability-") as temporary:
        copied_root = Path(temporary) / ROOT.name
        shutil.copytree(ROOT, copied_root)
        copied_route = copied_root / ROUTE_RELATIVE
        copied_manifest = copied_root / "PAPER_MANIFEST.sha256"
        present_manifest_bytes = (
            copied_manifest.read_bytes()
            if copied_manifest.is_file()
            else b"0" * 64 + b"  metadata-stability-placeholder\n"
        )

        states = (
            ("pending_manifest_present", pending_route, True),
            ("pending_manifest_absent", pending_route, False),
            ("sealed_manifest_absent", sealed_route, False),
            ("sealed_manifest_present", sealed_route, True),
        )
        for name, route_value, manifest_present in states:
            write_yaml(copied_route, route_value)
            if manifest_present:
                copied_manifest.write_bytes(present_manifest_bytes)
            elif copied_manifest.exists():
                copied_manifest.unlink()
            copied_ledgers_valid.append(ledger_valid(copied_root, first_ledger))
            metadata_outputs[name] = run_projected_integrity(copied_root)

    route_seal_stable = (
        metadata_outputs["pending_manifest_absent"]
        == metadata_outputs["sealed_manifest_absent"]
        and metadata_outputs["pending_manifest_present"]
        == metadata_outputs["sealed_manifest_present"]
    )
    manifest_toggle_stable = (
        metadata_outputs["pending_manifest_present"]
        == metadata_outputs["pending_manifest_absent"]
        and metadata_outputs["sealed_manifest_present"]
        == metadata_outputs["sealed_manifest_absent"]
    )
    all_metadata_outputs_equal = len(set(metadata_outputs.values())) == 1
    projected_integrity = next(iter(metadata_outputs.values()))
    actual_integrity_before_finalize = run_projected_integrity(ROOT)

    checks = {
        "scientific_payloads_unchanged": science_unchanged,
        "fresh_a_b_pass": double["status"] == "PASS",
        "cold_c_pass": cold["status"] == "PASS",
        "ledger_byte_identical": first_ledger == second_ledger,
        "aggregate_byte_identical": first_aggregate == second_aggregate,
        "ledger_43_of_43": ledger_43_of_43,
        "copied_ledgers_43_of_43": all(copied_ledgers_valid),
        "route_card_excluded_from_stage1_ledger": ROUTE_RELATIVE not in set(LEDGER_PATHS),
        "paper_manifest_excluded_from_stage1_ledger": "PAPER_MANIFEST.sha256" not in set(LEDGER_PATHS),
        "integrity_byte_stable_under_route_dummy_seal": route_seal_stable,
        "integrity_byte_stable_under_manifest_toggle": manifest_toggle_stable,
        "four_metadata_states_byte_identical": all_metadata_outputs_equal,
        "authority_integrity_matches_metadata_projection": actual_integrity_before_finalize == projected_integrity,
        "authority_route_untouched": ROUTE_CARD.read_bytes() == authority_route_before,
        "authority_manifest_untouched": manifest_state(MANIFEST) == authority_manifest_before,
    }
    payload = {
        "schema": "SD-C38-idempotence-certificate-v2",
        "candidate_id": "SD-C38",
        "scientific_payload_count": len(current_science),
        "freeze_runs": 2,
        "metadata_integrity_states_tested": 4,
        **checks,
        "integrity_byte_stable_after_certificate_finalize": True,
        "sha256sums_sha256": hashlib.sha256(first_ledger).hexdigest(),
        "aggregate_sha256": first_aggregate.decode("utf-8").strip(),
        "projected_integrity_audit_sha256": hashlib.sha256(projected_integrity).hexdigest(),
    }
    payload["status"] = "PASS" if all(checks.values()) else "FAIL"
    write_json(RESULTS / "idempotence_certificate.json", payload)
    actual_integrity_after_finalize = run_projected_integrity(ROOT)
    finalize_stable = actual_integrity_after_finalize == projected_integrity
    if not finalize_stable:
        payload["integrity_byte_stable_after_certificate_finalize"] = False
        payload["status"] = "FAIL"
        write_json(RESULTS / "idempotence_certificate.json", payload)
        run_projected_integrity(ROOT)

    print(json.dumps({"candidate_id": "SD-C38", "status": payload["status"]}, sort_keys=True))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
