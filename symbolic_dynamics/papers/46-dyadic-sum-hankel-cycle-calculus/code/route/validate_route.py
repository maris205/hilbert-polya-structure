#!/usr/bin/env python3
"""Primary strict Route-A v0.2 and provenance-state validator."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"
MUTATIONS = {
    "F14/prime_selector_claim": "A0_PRIME_SELECTOR_FAILURE",
    "RTE01/tuple_a0": "ROUTE_TUPLE_MISMATCH",
    "RTE02/overall_accept": "ROUTE_OVERALL_MISMATCH",
    "RTE03/route_b_true": "ROUTE_B_LOCK_FAILURE",
    "RTE04/stop_duplicate_terminal": "ROUTE_TERMINAL_VOCABULARY_FAILURE",
    "RTE05/drop_claim_boundary": "ROUTE_SCHEMA_FAILURE",
    "STA01/a_with_manifest": "MIXED_PROVENANCE_STATE",
    "STA02/b_missing_manifest": "MIXED_PROVENANCE_STATE",
    "STA03/b_unequal_commits": "PROVENANCE_COMMIT_MISMATCH",
    "STA04/b_zero_commit": "PROVENANCE_COMMIT_INVALID",
}


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("duplicate key")
        output[key] = value
    return output


def reject(identifier: str) -> int:
    if identifier not in MUTATIONS:
        raise ValueError("mutation not designated for R1")
    sys.stdout.buffer.write(canonical({
        "payload": {"code": MUTATIONS[identifier], "consumer": "R1",
                    "instance_id": identifier,
                    "witness": "primary Route v0.2/state validator rejected mutation"},
        "schema": "paper46-mutation-rejection-v1", "status": "REJECT",
    }))
    return 2


def route_path(output: Path) -> Path:
    if not output.is_absolute() or output.is_symlink() or not output.is_dir():
        raise ValueError("unsafe output")
    base = output.resolve(strict=True)
    path = output / "evaluations" / "route_a" / "SD-C48" / "2026-08-18.yaml"
    cursor = output
    for part in ["evaluations", "route_a", "SD-C48", "2026-08-18.yaml"]:
        cursor /= part
        if cursor.is_symlink():
            raise ValueError("symlink")
    answer = path.resolve(strict=True)
    if base not in answer.parents or not answer.is_file():
        raise ValueError("route containment")
    return answer


def validate(value: dict[str, Any], state: str, manifest_present: bool) -> int:
    checks = 0
    expected_tuple = ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC",
                      "A2_ANALYTIC_DETERMINANT", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"]
    if value.get("skill") != "route-a-evaluator" or value.get("skill_version") != "0.2.0":
        raise ValueError("route version")
    checks += 1
    if value.get("candidate_id") != "SD-C48" or value.get("route_tuple") != expected_tuple:
        raise ValueError("route tuple")
    checks += 1
    if value.get("overall_verdict") != "ROUTE_A_REJECTED":
        raise ValueError("overall")
    checks += 1
    if value.get("route_b_invocation_allowed") is not False \
            or value.get("route_b", {}).get("invocation_allowed") is not False:
        raise ValueError("Route B")
    checks += 1
    if value.get("a0", {}).get("verdict") != expected_tuple[0] \
            or value.get("a0", {}).get("arithmetic_controls") != [
                "exact_dyadic_support", "neighboring_nonedge_controls", "composite_power_labels",
                "no_prime_table_input", "marker_weight_type_separation"]:
        raise ValueError("A0")
    checks += 1
    if value.get("a2", {}).get("metrics") != {
            "Hilbert_Schmidt_wall": "Re_s_gt_one_half", "bounded_wall": "Re_s_gt_0",
            "endpoint_inclusions": "none", "target_zero_search": "not_applicable",
            "trace_class_wall": "Re_s_gt_1"}:
        raise ValueError("A2 metrics")
    checks += 1
    if value.get("a3", {}).get("weil_compression") != {
            "evidence_status": "STOP_SCOPED",
            "status": "no_natural_target_compression_from_dyadic_cycle_ledger"}:
        raise ValueError("A3 Weil")
    checks += 1
    if not value.get("claim_boundary") or value.get("round2_clues") != []:
        raise ValueError("claim/round2")
    checks += 1
    terminals = value.get("terminal_codes", {})
    if "STOP_DUPLICATE" in json.dumps(terminals, sort_keys=True) \
            or value.get("literature_disposition") != "PROCEED_SEARCH_BOUNDED":
        raise ValueError("terminal ownership")
    checks += 1
    if value.get("state") != state:
        raise ValueError("state")
    commits = [value.get("source_commit"), value.get("code_commit"),
               value.get("source_lock", {}).get("code_commit")]
    if state == "A":
        if commits != [PENDING, PENDING, PENDING] or manifest_present:
            raise ValueError("mixed State A")
    else:
        if not manifest_present or len(set(commits)) != 1 \
                or not isinstance(commits[0], str) \
                or not re.fullmatch(r"[0-9a-f]{40}", commits[0]) or commits[0] == "0" * 40:
            raise ValueError("invalid State B")
    checks += 1
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root")
    parser.add_argument("--state", choices=["A", "B"])
    parser.add_argument("--manifest-present", choices=["true", "false"])
    parser.add_argument("--mutation")
    args = parser.parse_args()
    if args.mutation:
        return reject(args.mutation)
    if not args.output_root or not args.state or args.manifest_present is None:
        raise ValueError("route args")
    raw = route_path(Path(args.output_root)).read_bytes()
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if raw != canonical(value):
        raise ValueError("noncanonical route")
    total = validate(value, args.state, args.manifest_present == "true")
    sys.stdout.buffer.write(canonical({
        "payload": {
            "checks_passed": total,
            "checks_total": total,
            "normalized_route_sha256": hashlib.sha256(raw).hexdigest(),
            "route_b_invocation_allowed": False,
            "route_tuple": value["route_tuple"],
            "state": args.state,
            "stop_duplicate_is_route_terminal": False,
        },
        "schema": "paper46-route-primary-audit-v1",
        "status": "PASS",
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
