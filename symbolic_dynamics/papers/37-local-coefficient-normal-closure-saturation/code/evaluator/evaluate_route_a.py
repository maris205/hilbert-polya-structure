#!/usr/bin/env python3
"""Strict Route-A v0.2 evaluator for the canonical Paper 37 result."""

from __future__ import annotations

import hashlib
import json
import sys
from typing import Any


EXPECTED_SCIENCE_SHA256 = (
    "b17967f294da018e2e045ae70ac7731f5612f4bd4693115ea33dbaebb7fc0d6e"
)
EXPECTED_ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_ANALYTIC_DETERMINANT",
    "A3_FAIL",
    "A4_FAIL",
]


def canonical_bytes(payload: object) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True) + "\n").encode("ascii")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_science(payload: object) -> bytes:
    return canonical_bytes(payload)


def extract_science(packet: object) -> dict[str, Any]:
    if not isinstance(packet, dict):
        raise TypeError("Route input must be a JSON object")
    if "scientific_results" not in packet:
        return packet
    allowed = {"scientific_results", "integration_metadata"}
    unknown = set(packet) - allowed
    if unknown:
        raise ValueError(f"unknown Route envelope keys: {sorted(unknown)!r}")
    science = packet["scientific_results"]
    if not isinstance(science, dict):
        raise TypeError("scientific_results must be a JSON object")
    return science


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def evaluate(payload: dict[str, Any]) -> dict[str, Any]:
    science_sha = sha256(canonical_science(payload))
    checks = payload["check_summary"]
    controls = payload["control_summary"]
    affine = payload["affine_results"]
    random_rows = payload["random_one_relator_results"]
    paired_rows = payload["random_presentations"]

    affine_direct = sum(
        int(row["direct"]["direct_factor_cancels"]) for row in affine
    )
    affine_leaks = sum(
        int(row["mixed"]["shortest_mixed_leak"] is not None) for row in affine
    )
    paired_all_direct = sum(
        int(row["all_direct_factors_cancel"]) for row in paired_rows
    )
    paired_leaks = sum(
        int(row["all_direct_factors_cancel"]
            and row["mixed_leak_after_direct_hit"])
        for row in paired_rows
    )

    counts = {
        "exact_checks_passed": int(checks["passed"]),
        "exact_checks_total": int(checks["total"]),
        "affine_rows": len(affine),
        "affine_direct_cancellations": affine_direct,
        "affine_mixed_leaks": affine_leaks,
        "fixed_one_relator_rows": len(payload["fixed_one_relator_results"]),
        "random_one_relator_rows": len(random_rows),
        "random_direct_cancellations": int(
            controls["random_direct_cancellations"]
        ),
        "random_mixed_leaks_after_direct": int(
            controls["random_mixed_failures_after_direct_cancellation"]
        ),
        "paired_two_relator_rows": len(paired_rows),
        "paired_all_direct_cancellations": paired_all_direct,
        "paired_mixed_leaks_after_all_direct": paired_leaks,
    }

    expected_counts = {
        "exact_checks_passed": 131,
        "exact_checks_total": 131,
        "affine_rows": 8,
        "affine_direct_cancellations": 8,
        "affine_mixed_leaks": 8,
        "fixed_one_relator_rows": 6,
        "random_one_relator_rows": 48,
        "random_direct_cancellations": 9,
        "random_mixed_leaks_after_direct": 9,
        "paired_two_relator_rows": 24,
        "paired_all_direct_cancellations": 2,
        "paired_mixed_leaks_after_all_direct": 2,
    }

    formula_rows = []
    for row in affine:
        exponent = int(row["exponent"])
        witness = row["mixed"]["shortest_mixed_leak"]
        observed = int(witness["first_supertrace"])
        expected = -4 * exponent**4 * (exponent - 1)
        if exponent >= 2:
            require(observed == expected,
                    f"mixed-witness formula mismatch at r={exponent}")
        formula_rows.append({
            "exponent": exponent,
            "observed_first_supertrace": observed,
            "expected_formula_value": expected,
            "formula_required": exponent >= 2,
            "passed": exponent == 1 or observed == expected,
        })

    require(science_sha == EXPECTED_SCIENCE_SHA256,
            "prototype scientific aggregate mismatch")
    require(counts == expected_counts, "canonical count mismatch")
    require(payload["arithmetic_mode"] == "exact_integer_and_fraction",
            "non-exact arithmetic mode")
    require(payload["source_evaluator_separated"] is True,
            "source/evaluator separation flag is false")
    require(payload["decision"]["route_tuple"] == EXPECTED_ROUTE_TUPLE,
            "Route tuple mismatch")
    require(payload["decision"]["overall"] == "ROUTE_A_REJECTED",
            "Route overall mismatch")
    require(payload["decision"]["route_b_invocation_allowed"] is False,
            "Route B was unlocked")

    return {
        "schema": "strict-route-a-evaluation-v0.2",
        "candidate": "SD-C39",
        "evaluator": "independent_exact_route_evaluator",
        "scientific_aggregate_sha256": science_sha,
        "canonical_counts": counts,
        "expected_counts": expected_counts,
        "formula_rows": formula_rows,
        "hard_status": "STOP_LOCAL_COEFFICIENT_SATURATION",
        "route_tuple": EXPECTED_ROUTE_TUPLE,
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "proves_too_much": True,
        "all_gates_exact": True,
    }


def main() -> int:
    packet = json.load(sys.stdin)
    science = extract_science(packet)
    sys.stdout.buffer.write(canonical_bytes(evaluate(science)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
