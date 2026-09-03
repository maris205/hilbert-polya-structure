#!/usr/bin/env python3
"""Deterministic, synthetic-only conformance check for P33 Round-5 fixtures.

This is not BP, CP, an adapter, or the production P33 validator.  It checks
only the canonical bytes and deliberately small failure predicates declared by
the Stage-4-prime synthetic fixture profile.  It consumes no surface output.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ALLOWED_TOP_LEVEL_FIELDS = {
    "schema_version", "proof_registry_digest", "surface_id", "producer_id",
    "run_id", "record_type", "candidate_id", "producer_representation",
    "enumeration_provenance", "oriented_class_digest", "primitive_root_digest",
    "root_exponent", "inverse_class_digest", "owner_id",
    "owner_member_digests", "cutoff", "cutoff_disposition", "proof_type",
    "proof_payload", "input_digest", "theorem_version_digest",
    "implementation_digest", "correction_provenance_digest", "clock_id",
    "subtype_id", "owner_rule_id", "termination_witness", "coverage_digest",
    "unresolved_count", "validator_version", "validator_digest",
    "fixture_set_digest", "predicate_decisions", "rejected_incompatibilities",
    "state",
}

PROOF_TYPES = {
    "exact_conjugator", "canonical_conjugacy_normal_form", "maximal_root",
    "no_proper_power", "systolic_primitive", "exact_cutoff_comparison",
    "exact_trace_comparison", "conjugacy_to_inverse", "termination_measure",
    "coverage_replay",
}

DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")


def canonical_bytes(obj: object) -> bytes:
    return json.dumps(
        obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def disposition(obj: dict, raw: bytes, registry_digest: str) -> str:
    if raw != canonical_bytes(obj):
        return "rejected:noncanonical_serialization"
    unknown = sorted(set(obj) - ALLOWED_TOP_LEVEL_FIELDS)
    if unknown:
        return "rejected:unknown_field"
    if obj.get("schema_version") != "P33-OWNER-CERT/1":
        return "rejected:schema_version_mismatch"
    if obj.get("proof_registry_digest") != registry_digest:
        return "rejected:proof_registry_digest_mismatch"
    proof_type = obj.get("proof_type")
    if proof_type == "search_timeout_negative":
        return "not_evaluable:unsupported_negative_decision"
    if proof_type not in PROOF_TYPES:
        return "not_evaluable:unrecognized_proof_type"
    for field in (
        "input_digest", "theorem_version_digest", "implementation_digest",
        "correction_provenance_digest", "oriented_class_digest",
        "primitive_root_digest", "owner_id", "coverage_digest",
    ):
        if field in obj and not DIGEST_RE.fullmatch(str(obj[field])):
            return "rejected:hash_mismatch"
    if "inverse_class_digest" not in obj:
        return "rejected:missing_inverse_link"
    if not DIGEST_RE.fullmatch(str(obj["inverse_class_digest"])):
        return "rejected:hash_mismatch"
    if obj.get("proof_type") == "no_proper_power" and obj.get("root_exponent") != "1":
        return "rejected:primitive_power_conflict"
    if obj.get("owner_rule_id") == "self_reciprocal" and obj.get("proof_type") != "conjugacy_to_inverse":
        return "rejected:false_reciprocity"
    members = obj.get("owner_member_digests", [])
    if len(members) != len(set(members)):
        return "rejected:duplicate_owner"
    if obj.get("cutoff_disposition") == "unresolved":
        return "bounded_incomplete:unresolved_cutoff"
    if obj.get("record_type") == "coverage" and obj.get("unresolved_count") != "0":
        return "bounded_incomplete:incomplete_coverage"
    if obj.get("record_type") == "termination" and obj.get("termination_witness") != "valid":
        return "rejected:invalid_termination"
    required = {
        "schema_version", "proof_registry_digest", "surface_id", "producer_id",
        "run_id", "record_type", "candidate_id", "oriented_class_digest",
        "primitive_root_digest", "root_exponent", "inverse_class_digest",
        "owner_id", "owner_member_digests", "cutoff", "cutoff_disposition",
        "proof_type", "proof_payload", "input_digest", "theorem_version_digest",
        "implementation_digest", "correction_provenance_digest", "coverage_digest",
        "unresolved_count", "state",
    }
    if required - set(obj):
        return "rejected:missing_mandatory_field"
    if obj.get("state") != "accepted":
        return "rejected:invalid_terminal_state"
    return "accepted:synthetic_conformance"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--support-root", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()

    support = args.support_root.resolve()
    registry_path = support / "synthetic_proof_registry_snapshot.json"
    oracle_path = support / "fixture_oracle_manifest.json"
    registry_raw = registry_path.read_bytes()
    registry_digest = sha256_bytes(registry_raw)
    oracle = json.loads(oracle_path.read_text(encoding="utf-8"))
    expected = {row["relative_path"]: row["expected_disposition"] for row in oracle["fixtures"]}

    results = []
    failures = []
    for relative_path in sorted(expected):
        path = support / "fixtures" / relative_path
        raw = path.read_bytes()
        try:
            obj = json.loads(raw.decode("utf-8"))
            actual = disposition(obj, raw, registry_digest)
        except Exception as exc:  # deterministic parse failure receipt
            actual = f"rejected:json_parse_error:{type(exc).__name__}"
        matched = actual == expected[relative_path]
        row = {
            "relative_path": relative_path,
            "sha256": sha256_bytes(raw),
            "bytes": len(raw),
            "expected_disposition": expected[relative_path],
            "actual_disposition": actual,
            "match": matched,
        }
        results.append(row)
        if not matched:
            failures.append(row)

    fixture_set_digest = sha256_bytes(
        "".join(f"{r['relative_path']}\0{r['sha256']}\n" for r in results).encode("utf-8")
    )
    receipt = {
        "schema_version": "p33-stage4-prime-synthetic-fixture-validation-receipt/1.0",
        "workflow_date": "2026-09-04",
        "paper_id": "P33",
        "status": "PASS_SYNTHETIC_CONFORMANCE_ONLY" if not failures else "FAIL_CLOSED",
        "scope": "Synthetic P33-OWNER-CERT/1 conformance fixtures only; not a surface producer, owner census, scientific validator, or result refresh.",
        "registry": {
            "path": "synthetic_proof_registry_snapshot.json",
            "sha256": registry_digest,
            "interpretation": "synthetic fixture profile only; no production theorem encoding",
        },
        "oracle": {
            "path": "fixture_oracle_manifest.json",
            "sha256": sha256_bytes(oracle_path.read_bytes()),
            "independence_state": oracle["independence_state"],
        },
        "harness": {
            "path": "validate_synthetic_fixtures.py",
            "sha256": sha256_bytes(Path(__file__).read_bytes()),
        },
        "fixture_set_digest": fixture_set_digest,
        "counts": {
            "valid_fixture_files": sum(r["relative_path"].startswith("valid/") for r in results),
            "invalid_fixture_files": sum(r["relative_path"].startswith("invalid/") for r in results),
            "outcomes_matching_oracle": sum(r["match"] for r in results),
            "failures": len(failures),
        },
        "results": results,
        "boundaries": {
            "surface_input_consumed": False,
            "producer_run": False,
            "owner_census_run": False,
            "scientific_result_refreshed": False,
            "production_validator_independence_established": False,
        },
    }
    args.receipt.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
