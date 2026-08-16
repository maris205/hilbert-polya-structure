#!/usr/bin/env python3
"""Independent strict Route-A v0.2 evaluator for Paper 38."""

from __future__ import annotations

import hashlib
import json
import sys
from typing import Any


EXPECTED_SCIENCE_SHA256 = (
    "a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24"
)
EXPECTED_ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_FAIL",
    "A3_FAIL",
    "A4_FAIL",
]


def canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(payload, sort_keys=True, separators=(",", ":"),
                   ensure_ascii=True) + "\n"
    ).encode("ascii")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def evaluate_route(science: dict[str, Any]) -> dict[str, Any]:
    science_bytes = canonical_bytes(science)
    science_sha = sha256(science_bytes)
    checks = science["check_summary"]
    decision = science["decision"]
    parameters = science["parameter_results"]
    gbs = science["gbs_results"]
    random_rows = science["random_one_relator_results"]
    markers = science["marker_results"]
    finite_trees = science["finite_tree_results"]
    noncompact = science["noncompact_results"]

    counts = {
        "exact_checks_passed": int(checks["passed"]),
        "exact_checks_total": int(checks["total"]),
        "parameter_rows": len(parameters),
        "balanced_rows": sum(int(row["r"] == 1) for row in parameters),
        "prime_rows": sum(
            int(row["declared_class"] == "prime_control")
            for row in parameters
        ),
        "composite_rows": sum(
            int(row["declared_class"].startswith("composite"))
            for row in parameters
        ),
        "finite_tree_rows": len(finite_trees),
        "noncompact_rows": len(noncompact),
        "gbs_rows": len(gbs),
        "gbs_empty_ledgers": sum(
            int(row["full_tree_closed_ledger_empty"]) for row in gbs
        ),
        "gbs_fredholm_owned": sum(
            int(row["full_tree_fredholm_owned"]) for row in gbs
        ),
        "random_one_relator_rows": len(random_rows),
        "random_eligible_cyclic_gbs": sum(
            int(row["canonical_cyclic_gbs_split_detected"])
            for row in random_rows
        ),
        "marker_rows": len(markers),
        "marker_compatible_rows": sum(
            int(row["markers_compatible"]) for row in markers
        ),
        "generic_necklace_rows": sum(
            int(row["r"] >= 2 and row["orbital_group_conjugacy_ledger"]
                == "FINITE_BUT_GENERIC_NECKLACE_LEDGER")
            for row in parameters
        ),
        "source_selective_rows": sum(
            int(row.get("source_selective", False)) for row in parameters
        ),
    }
    expected_counts = {
        "exact_checks_passed": 277,
        "exact_checks_total": 277,
        "parameter_rows": 11,
        "balanced_rows": 1,
        "prime_rows": 4,
        "composite_rows": 6,
        "finite_tree_rows": 3,
        "noncompact_rows": 5,
        "gbs_rows": 18,
        "gbs_empty_ledgers": 18,
        "gbs_fredholm_owned": 0,
        "random_one_relator_rows": 64,
        "random_eligible_cyclic_gbs": 0,
        "marker_rows": 5,
        "marker_compatible_rows": 0,
        "generic_necklace_rows": 10,
        "source_selective_rows": 0,
    }

    theorem = science["theorem_boundary"]
    require(science_sha == EXPECTED_SCIENCE_SHA256,
            "prototype scientific aggregate mismatch")
    require(science["schema"] == "paper38-scientific-results-v1",
            "science schema mismatch")
    require(science["arithmetic_mode"] == "exact_integer_and_fraction",
            "non-exact arithmetic mode")
    require(science["source_evaluator_separated"] is True,
            "source/evaluator separation flag is false")
    require(counts == expected_counts, "canonical count mismatch")
    require(decision["route_tuple"] == EXPECTED_ROUTE_TUPLE,
            "Route tuple mismatch")
    require(decision["overall"] == "ROUTE_A_REJECTED",
            "Route overall mismatch")
    require(decision["route_b_invocation_allowed"] is False,
            "Route B was unlocked")
    require(decision["hard_status"] == "STOP_BASS_SERRE_TREE_BRANCH",
            "hard stop mismatch")
    require(decision["branch_status"] == "CLOSE_ENTIRE_AFFINE_BRANCH",
            "branch closure mismatch")
    require(decision["full_tree_primitive_ledger"] == "EMPTY",
            "full-tree ledger is not empty")
    require(decision["full_tree_fredholm"] == "NOT_OWNED_NON_TRACE_CLASS",
            "Fredholm ownership mismatch")
    require(decision["tree_lattice_formula_applicable"] is False,
            "tree-lattice formula was improperly enabled")
    require(decision["old_marker_compatible"] is False,
            "old marker was improperly inherited")
    require(theorem["finite_checks_used_as_infinite_proof"] is False,
            "finite checks were promoted to an infinite proof")
    require(theorem["tree_has_no_positive_reduced_closed_path"] is True,
            "tree emptiness boundary missing")
    require(theorem["full_tree_hashimoto_noncompact"] is True,
            "noncompactness boundary missing")
    require(theorem["ordinary_full_tree_fredholm_not_defined"] is True,
            "ordinary Fredholm boundary missing")
    require(theorem["r_ge_2_faithful_image_non_discrete"] is True,
            "r>=2 image-topology boundary missing")
    require(theorem["r1_image_discrete_but_infinite_kernel"] is True,
            "r=1 image/kernel boundary missing")
    require(theorem["all_r_bass_serre_action_nonproper"] is True,
            "all-r nonproperness boundary missing")
    require(theorem["tree_lattice_finite_stabilizer_hypotheses_fail"] is True,
            "finite-stabilizer boundary missing")
    r1 = next(row for row in parameters if row["r"] == 1)
    r_ge_2 = [row for row in parameters if row["r"] >= 2]
    require(
        r1["aut_tree_image_discrete"] is True
        and r1["bass_serre_action_faithful"] is False
        and r1["action_kernel"] == "infinite_cyclic"
        and r1["action_proper"] is False,
        "r=1 action topology was normalized incorrectly",
    )
    require(
        all(
            row["aut_tree_image_discrete"] is False
            and row["bass_serre_action_faithful"] is True
            and row["action_kernel"] == "trivial"
            and row["action_proper"] is False
            for row in r_ge_2
        ),
        "r>=2 action topology was normalized incorrectly",
    )

    gates = {
        "A0": {
            "verdict": "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "evidence": "r_is_HNN_index_and_modulus_is_r_to_signed_height",
        },
        "A1": {
            "verdict": "A1_FAIL",
            "evidence": "full_tree_ledger_empty_orbital_substitute_generic_or_divergent",
        },
        "A2": {
            "verdict": "A2_FAIL",
            "evidence": "full_tree_hashimoto_noncompact_non_trace_class",
        },
        "A3": {
            "verdict": "A3_FAIL",
            "evidence": "no_source_selective_arithmetic_primitive_sector",
        },
        "A4": {
            "verdict": "A4_FAIL",
            "evidence": "bass_serre_marker_incompatible_with_old_generator_clock",
        },
    }
    return {
        "schema": "strict-route-a-evaluation-v0.2",
        "candidate": "SD-C40",
        "evaluator": "independent_exact_route_evaluator",
        "scientific_aggregate_sha256": science_sha,
        "canonical_counts": counts,
        "expected_counts": expected_counts,
        "gates": gates,
        "hard_status": "STOP_BASS_SERRE_TREE_BRANCH",
        "branch_status": "CLOSE_ENTIRE_AFFINE_BRANCH",
        "route_tuple": EXPECTED_ROUTE_TUPLE,
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "proves_too_much_risk": "RECIPROCAL_INFINITE_STABILIZER_AS_ZERO",
        "all_gates_exact": True,
    }


def main() -> int:
    packet = json.load(sys.stdin)
    science = extract_science(packet)
    sys.stdout.buffer.write(canonical_bytes(evaluate_route(science)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
