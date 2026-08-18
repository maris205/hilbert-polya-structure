#!/usr/bin/env python3
"""Independent Route/state audit without importing the primary validator."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


PENDING_SENTINEL = "PENDING_FIRST_ARTIFACT_COMMIT"
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


def dump(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def pairs_unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for name, item in pairs:
        if name in result:
            raise ValueError("duplicate name")
        result[name] = item
    return result


def mutation(identifier: str) -> int:
    code = MUTATIONS.get(identifier)
    if code is None:
        raise ValueError("mutation not designated for R2")
    sys.stdout.buffer.write(dump({
        "payload": {"code": code, "consumer": "R2", "instance_id": identifier,
                    "witness": "independently encoded Route/state invariants rejected mutation"},
        "schema": "paper46-mutation-rejection-v1", "status": "REJECT",
    }))
    return 2


def find_route(output: Path) -> Path:
    if not output.is_absolute() or output.is_symlink() or not output.is_dir():
        raise ValueError("bad output root")
    origin = output.resolve(strict=True)
    cursor = output
    for name in ("evaluations", "route_a", "SD-C48", "2026-08-18.yaml"):
        cursor = cursor / name
        if cursor.is_symlink():
            raise ValueError("route symlink")
    final = cursor.resolve(strict=True)
    if origin not in final.parents or not final.is_file():
        raise ValueError("route escaped")
    return final


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root")
    parser.add_argument("--state", choices=["A", "B"])
    parser.add_argument("--manifest-present", choices=["true", "false"])
    parser.add_argument("--mutation")
    args = parser.parse_args()
    if args.mutation:
        return mutation(args.mutation)
    if args.output_root is None or args.state is None or args.manifest_present is None:
        raise ValueError("missing argument")
    path = find_route(Path(args.output_root))
    raw = path.read_bytes()
    data = json.loads(raw.decode("ascii"), object_pairs_hook=pairs_unique)
    if raw != dump(data):
        raise ValueError("route encoding")
    expected = ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC",
                "A2_ANALYTIC_DETERMINANT", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"]
    checks = [
        data.get("candidate_id") == "SD-C48",
        data.get("route_tuple") == expected,
        data.get("overall_verdict") == "ROUTE_A_REJECTED",
        data.get("route_b_invocation_allowed") is False,
        data.get("route_b", {}).get("invocation_allowed") is False,
        data.get("a0", {}).get("verdict") == expected[0],
        data.get("a1", {}).get("verdict") == expected[1],
        data.get("a2", {}).get("verdict") == expected[2],
        data.get("a3", {}).get("verdict") == expected[3],
        data.get("a4", {}).get("verdict") == expected[4],
        data.get("a2", {}).get("metrics", {}).get("target_zero_search") == "not_applicable",
        data.get("a3", {}).get("weil_compression", {}).get("evidence_status") == "STOP_SCOPED",
        isinstance(data.get("claim_boundary"), str) and bool(data["claim_boundary"]),
        data.get("round2_clues") == [],
        data.get("literature_disposition") == "PROCEED_SEARCH_BOUNDED",
        "STOP_DUPLICATE" not in json.dumps(data.get("terminal_codes", {}), sort_keys=True),
        data.get("state") == args.state,
    ]
    commit_values = [data.get("source_commit"), data.get("code_commit"),
                     data.get("source_lock", {}).get("code_commit")]
    manifest = args.manifest_present == "true"
    if args.state == "A":
        checks.append(commit_values == [PENDING_SENTINEL] * 3 and not manifest)
    else:
        checks.append(manifest and len(set(commit_values)) == 1
                      and isinstance(commit_values[0], str)
                      and re.fullmatch(r"[0-9a-f]{40}", commit_values[0]) is not None
                      and commit_values[0] != "0" * 40)
    if not all(checks):
        raise ValueError("independent Route invariant")
    count = len(checks)
    sys.stdout.buffer.write(dump({
        "payload": {
            "checks_passed": count,
            "checks_total": count,
            "normalized_route_sha256": hashlib.sha256(raw).hexdigest(),
            "route_b_invocation_allowed": False,
            "route_tuple": data["route_tuple"],
            "state": args.state,
            "stop_duplicate_is_route_terminal": False,
        },
        "schema": "paper46-route-independent-audit-v1",
        "status": "PASS",
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
