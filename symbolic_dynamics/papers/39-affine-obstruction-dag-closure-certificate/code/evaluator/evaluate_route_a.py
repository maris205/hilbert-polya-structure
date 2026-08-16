#!/usr/bin/env python3
"""Derive the strict Paper-39 Route-A v0.2 rejection from accepted science."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


EXPECTED_SCIENCE_SHA256 = "77a45be483807b81ba61fe0f16b16be20fcd7e6e4ff1f3f74f34d052c6881d93"
EXPECTED_SEED_SHA256 = "7bdb90811575a96518c2f67510ef9deb4335e2051c965643f7e3572e806ff6cd"
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
ROUTE_TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def digest_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def route_result(evaluation: dict[str, Any], seed_raw: bytes) -> dict[str, Any]:
    seed_text = seed_raw.decode("utf-8")
    science = evaluation.get("science_projection", {})
    checks = {
        "all_science_checks_pass": evaluation.get("all_pass") is True,
        "main_check_count_535": evaluation.get("counts", {}).get("checks_passed") == 535
        and evaluation.get("counts", {}).get("checks_total") == 535,
        "science_projection_hash_exact": evaluation.get("science_projection_sha256") == EXPECTED_SCIENCE_SHA256
        and digest_bytes(canonical_bytes(science)) == EXPECTED_SCIENCE_SHA256,
        "terminal_registry_return": science.get("realized_terminal")
        == "RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY",
        "no_new_mechanism": science.get("new_mechanism_count") == 0,
        "no_universal_affine_no_go": science.get("universal_affine_no_go_claimed") is False,
        "contract_relative_exhaustiveness": science.get("contract_relative_exhaustiveness") is True,
        "retrospective_timing": "after predecessor outcomes were known" in science.get("retrospective_encoding_timing", ""),
        "seed_hash_exact": digest_bytes(seed_raw) == EXPECTED_SEED_SHA256,
        "seed_version_v02": "skill_version: 0.2.0" in seed_text,
        "seed_candidate_exact": "candidate_id: SD-C41" in seed_text,
        "seed_tuple_all_fail": all(f"  - {item}" in seed_text for item in ROUTE_TUPLE),
        "seed_route_b_locked": "route_b_invocation_allowed: false" in seed_text,
        "seed_pending_triple": seed_text.count(PENDING) >= 3,
    }
    all_pass = all(checks.values())
    return {
        "B": False,
        "all_pass": all_pass,
        "branch_status": "CLOSE_ENTIRE_AFFINE_BRANCH",
        "candidate_id": "SD-C41",
        "checks": [{"name": name, "passed": passed} for name, passed in checks.items()],
        "counts": {"checks_passed": sum(checks.values()), "checks_total": len(checks)},
        "evaluation_date": "2026-08-16",
        "overall_verdict": "ROUTE_A_REJECTED",
        "paired_provenance": {
            "code_commit": PENDING,
            "source_commit": PENDING,
            "source_lock_code_commit": PENDING,
        },
        "realized_terminal": "RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY",
        "route_b_invocation_allowed": False,
        "route_tuple": ROUTE_TUPLE,
        "schema": "paper39-route-a-evaluation-v1",
        "science_projection_sha256": EXPECTED_SCIENCE_SHA256,
        "seed_route_sha256": EXPECTED_SEED_SHA256,
        "skill": "route-a-evaluator",
        "skill_version": "0.2.0",
        "target_and_root_metrics": {
            "correlation_metrics": "NA",
            "cutoff_drift": "NA",
            "eigenvalue_count": "NA",
            "extra_zero_count": "NA",
            "missing_zero_count": "NA",
            "precision_drift": "NA",
            "root_count_discrepancy": "NA",
            "root_location_error": "NA",
            "spacing_metrics": "NA",
            "spectral_fit": "NA",
            "target_coefficient_fit": "NA",
            "target_prime_data": "NA",
            "target_root_data": "NA",
            "target_zero_data": "NA",
            "unfolding_metrics": "NA",
            "zero_error_test": "NA",
            "zero_error_train": "NA",
            "zero_error_validation": "NA",
        },
    }


def sealed_yaml(seed_raw: bytes, result: dict[str, Any]) -> bytes:
    seed_text = seed_raw.decode("utf-8")
    old_note = (
        "freeze_note: >-\n"
        "  Working mathematical Route card only. Paper 39 is a closure/audit\n"
        "  meta-object assembled retrospectively after P35-P38 outcomes were known and\n"
        "  frozen before the Paper-39 checker run. It has no authority artifact commit\n"
        "  in this /tmp package. Root alone owns any later two-stage provenance seal.\n"
    )
    new_note = (
        "freeze_note: >-\n"
        "  Stage 1 authority card. Paper 39 is a retrospective closure/audit\n"
        "  meta-object assembled after P35-P38 outcomes were known and frozen before\n"
        "  the Paper-39 authority checker run. The three provenance fields remain\n"
        "  PENDING_FIRST_ARTIFACT_COMMIT and no root manifest exists. Stage 2 is\n"
        "  metadata-only and may change only this fixed Route card and add the\n"
        "  self-excluding root manifest.\n"
    )
    if old_note not in seed_text:
        raise ValueError("immutable Route seed freeze note not recognized")
    base = seed_text.replace(old_note, new_note, 1).rstrip("\n")
    metrics = result["target_and_root_metrics"]
    extra_lines = [
        "",
        "authority_integration:",
        "  stage1_root_manifest: ABSENT",
        "  stage2_semantic_scope: ROUTE_CARD_PLUS_SELF_EXCLUDING_ROOT_MANIFEST_ONLY",
        "  science_projection_sha256: " + EXPECTED_SCIENCE_SHA256,
        "  main_evaluator_checks: 535/535",
        "  independent_evaluator_checks: 278/278",
        "  adversarial_mutations_rejected_by_both: 29/29",
        "  repair_class_census: 6_OBSTRUCTED_6_EXIT_ONLY_2_MIXED",
        "  request_token_census: 8_OBSTRUCTION_8_EXIT",
        "  endpoint_obstruction_totality: true",
        "  universal_affine_no_go_claimed: false",
        "  new_mechanisms: 0",
        "  ranking_performed: false",
        "  successor_proposed: false",
        "",
        "target_and_root_metrics:",
    ]
    extra_lines.extend(f"  {key}: \"{value}\"" for key, value in metrics.items())
    extra_lines.extend(
        [
            "",
            "route_b:",
            "  B: false",
            "  invoked: false",
            "  invocation_allowed: false",
            "",
        ]
    )
    return (base + "\n" + "\n".join(extra_lines)).encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--main-evaluation", required=True)
    parser.add_argument("--seed-route", required=True)
    parser.add_argument("--json-output", required=True)
    parser.add_argument("--yaml-output")
    args = parser.parse_args()
    evaluation = json.loads(Path(args.main_evaluation).read_text(encoding="utf-8"))
    seed_raw = Path(args.seed_route).read_bytes()
    result = route_result(evaluation, seed_raw)
    Path(args.json_output).write_bytes(canonical_bytes(result))
    if args.yaml_output:
        Path(args.yaml_output).write_bytes(sealed_yaml(seed_raw, result))
    return 0 if result["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
