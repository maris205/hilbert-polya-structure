#!/usr/bin/env python3
"""Fail-closed Phase-2A verdict emitter for P33 Stage 3-prime Round 5.

The emitter adds only the fixed contract/hash fields, rejects every extra
payload property, validates against the vendored ARS 1.1 schema, and creates
the official verdict artifact exactly once. It never repairs a judgment.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile

from jsonschema import Draft202012Validator


ARS_ROOT = Path("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite")
VERDICT_SCHEMA = ARS_ROOT / "ars/shared/contracts/re_review/verdict_record.schema.json"
PRECOMMITMENT_SCHEMA = ARS_ROOT / "ars/shared/contracts/re_review/precommitment.schema.json"
ROUND_ID = "p33-stage3-prime-round5-2026-09-04"


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def schema_errors(schema: object, instance: object) -> list[dict[str, str]]:
    errors = sorted(
        Draft202012Validator(schema).iter_errors(instance),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    return [
        {
            "path": "/" + "/".join(map(str, error.absolute_path)) if error.absolute_path else "/",
            "message": error.message,
        }
        for error in errors
    ]


def build_candidate(payload: dict[str, object], precommitment: dict[str, object]) -> dict[str, object]:
    allowed = {"round_id", "items", "new_issues", "dissents", "escalation_exceptions"}
    if set(payload) != allowed:
        raise ValueError(f"payload keys must be exactly {sorted(allowed)}; got {sorted(payload)}")
    if payload["round_id"] != ROUND_ID:
        raise ValueError("payload round_id mismatch")
    if precommitment.get("round_id") != ROUND_ID:
        raise ValueError("precommitment round_id mismatch")

    return {
        "contract_version": "1.1",
        "round_id": ROUND_ID,
        "precommitment_hash": sha256_bytes(canonical_bytes(precommitment)),
        "items": payload["items"],
        "new_issues": payload["new_issues"],
        "dissents": payload["dissents"],
        "escalation_exceptions": payload["escalation_exceptions"],
    }


def atomic_create_json(path: Path, value: object) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable verdict: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(value, ensure_ascii=False, indent=2).encode("utf-8") + b"\n"
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.link(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def synthetic_fixture() -> dict[str, object]:
    return {
        "contract_version": "1.1",
        "round_id": "self-test",
        "precommitment_hash": "a" * 64,
        "items": [
            {
                "item_id": "REV-TEST-1",
                "verdict": "FULLY_ADDRESSED",
                "evidence_anchor": ["text: revised block B0001"],
                "change_summary": "The revised fixture adds the required bounded statement.",
                "verified_by": "EIC",
                "applied_criterion": "precommitted",
            },
            {
                "item_id": "REV-TEST-2",
                "verdict": "PARTIALLY_ADDRESSED",
                "evidence_anchor": ["equation: revised block B0002"],
                "change_summary": "The revised fixture closes one conjunct but leaves one explicit obligation.",
                "residual_gap": {"text": "One required witness is absent.", "residual_obligation_class": "must_fix"},
                "verified_by": "R1",
                "applied_criterion": "precommitted",
            },
            {
                "item_id": "REV-TEST-3",
                "verdict": "CANNOT_VERIFY",
                "cannot_verify_reason": "The required fixture is absent from the frozen input set.",
                "change_summary": "No comparable frozen fixture is present.",
                "verified_by": "R2",
                "applied_criterion": "precommitted",
            },
        ],
        "new_issues": [],
        "dissents": [],
        "escalation_exceptions": [],
    }


def run_self_test(receipt: Path, generated_at: str) -> None:
    schema = load_json(VERDICT_SCHEMA)
    fixture = synthetic_fixture()
    errors = schema_errors(schema, fixture)
    if errors:
        raise RuntimeError(f"emitter fixture failed schema validation: {errors}")
    result = {
        "schema_version": "p33-stage3-prime-round5-verdict-emitter-preflight/1.0",
        "generated_at": generated_at,
        "round_id": ROUND_ID,
        "status": "PASS",
        "performed_before_phase2a_evidence_exposure": True,
        "emitter": {
            "path": "tools/p33_stage3_prime_round5_verdict_emitter.py",
            "sha256": sha256_file(Path(__file__).resolve()),
        },
        "verdict_schema": {
            "path": str(VERDICT_SCHEMA),
            "sha256": sha256_file(VERDICT_SCHEMA),
            "draft": "2020-12",
        },
        "precommitment_schema": {
            "path": str(PRECOMMITMENT_SCHEMA),
            "sha256": sha256_file(PRECOMMITMENT_SCHEMA),
        },
        "fixture_cases": ["FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "CANNOT_VERIFY"],
        "schema_error_count": 0,
        "guarantees": [
            "closed top-level payload keys",
            "closed per-item properties through official schema",
            "evidence_anchor array shape",
            "residual_gap object shape",
            "precommitment JCS binding",
            "exclusive create of immutable official verdict",
            "no judgment repair or retry",
        ],
    }
    atomic_create_json(receipt, result)


def emit(payload_path: Path, precommitment_path: Path, output: Path) -> None:
    payload = load_json(payload_path)
    precommitment = load_json(precommitment_path)
    if not isinstance(payload, dict) or not isinstance(precommitment, dict):
        raise ValueError("payload and precommitment must be JSON objects")

    pre_errors = schema_errors(load_json(PRECOMMITMENT_SCHEMA), precommitment)
    if pre_errors:
        raise ValueError(f"precommitment schema failure: {pre_errors}")
    candidate = build_candidate(payload, precommitment)
    errors = schema_errors(load_json(VERDICT_SCHEMA), candidate)
    if errors:
        raise ValueError(f"verdict schema failure: {errors}")
    atomic_create_json(output, candidate)
    print(json.dumps({
        "status": "PASS",
        "output": str(output),
        "raw_sha256": sha256_file(output),
        "jcs_sha256": sha256_bytes(canonical_bytes(candidate)),
        "items": len(candidate["items"]),
    }, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    self_test = subparsers.add_parser("self-test")
    self_test.add_argument("--receipt", type=Path, required=True)
    self_test.add_argument("--generated-at", required=True)

    emitter = subparsers.add_parser("emit")
    emitter.add_argument("--payload", type=Path, required=True)
    emitter.add_argument("--precommitment", type=Path, required=True)
    emitter.add_argument("--output", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "self-test":
        run_self_test(args.receipt, args.generated_at)
    else:
        emit(args.payload, args.precommitment, args.output)


if __name__ == "__main__":
    main()
