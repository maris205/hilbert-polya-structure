#!/usr/bin/env python3
"""Render the canonical Route-A v0.2 record (JSON-form YAML 1.2)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       allow_nan=False, separators=(",", ": ")) + "\n").encode("ascii")


def commit_for(state: str, commit: str | None) -> str:
    if state == "A":
        if commit is not None:
            raise ValueError("State A forbids commit")
        return PENDING
    if commit is None or not re.fullmatch(r"[0-9a-f]{40}", commit) or commit == "0" * 40:
        raise ValueError("State B commit")
    return commit


def route(state: str, commit: str | None) -> dict[str, Any]:
    value = commit_for(state, commit)
    return {
        "a0": {
            "arithmetic_controls": [
                "exact_dyadic_support", "neighboring_nonedge_controls",
                "composite_power_labels", "no_prime_table_input",
                "marker_weight_type_separation",
            ],
            "evidence_status": "PROVED",
            "verdict": "A0_WEAK_ARITHMETIC_RELATION",
        },
        "a1": {"evidence_status": "PROVED", "verdict": "A1_PASS_ANALYTIC"},
        "a2": {
            "evidence_status": "PROVED",
            "metrics": {
                "Hilbert_Schmidt_wall": "Re_s_gt_one_half",
                "bounded_wall": "Re_s_gt_0",
                "endpoint_inclusions": "none",
                "target_zero_search": "not_applicable",
                "trace_class_wall": "Re_s_gt_1",
            },
            "verdict": "A2_ANALYTIC_DETERMINANT",
        },
        "a3": {
            "evidence_status": "PROVED",
            "verdict": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "weil_compression": {
                "evidence_status": "STOP_SCOPED",
                "status": "no_natural_target_compression_from_dyadic_cycle_ledger",
            },
        },
        "a4": {
            "evidence_status": "OPEN",
            "metrics": {
                "Hilbert_space_named": True,
                "fixed_self_adjoint_operator_defined": False,
                "same_clock_rational_prime_trace_identity": False,
                "target_multiplicity_theorem": False,
            },
            "verdict": "A4_FAIL",
        },
        "artifact_path_base": "papers/46-dyadic-sum-hankel-cycle-calculus",
        "branch_status": "CLOSE_SD_C48_ROUTE_B",
        "candidate_id": "SD-C48",
        "claim_boundary": "FROZEN_DYADIC_SUM_GRAPH_ONLY_NO_PRIME_EMERGENCE_NO_TARGET_DIVISOR_NO_PRIORITY",
        "code_commit": value,
        "evaluation_date": "2026-08-18",
        "literature_disposition": "PROCEED_SEARCH_BOUNDED",
        "overall_verdict": "ROUTE_A_REJECTED",
        "round2_clues": [],
        "route_b": {
            "invocation_allowed": False,
            "reason": "no_completed_target_divisor_and_no_fixed_self_adjoint_lift",
        },
        "route_b_invocation_allowed": False,
        "route_tuple": [
            "A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC",
            "A2_ANALYTIC_DETERMINANT", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL",
        ],
        "skill": "route-a-evaluator",
        "skill_version": "0.2.0",
        "source_commit": value,
        "source_lock": {
            "clock": "one_edge",
            "code_commit": value,
            "function_space": "ell2_positive_integers",
            "marker": "z_counts_one_original_edge",
            "object": "looped_positive_integer_graph_m_plus_n_dyadic",
        },
        "state": state,
        "terminal_codes": {
            "arithmetic_emergence": "STOP_EXPLICIT_DYADIC_INPUT",
            "rational_prime_ledger": "STOP_NO_RATIONAL_PRIME_PRIMITIVES",
            "spectral_target": "STOP_NO_COMPLETED_SELF_ADJOINT_LIFT",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", choices=["A", "B"], required=True)
    parser.add_argument("--commit")
    args = parser.parse_args()
    sys.stdout.buffer.write(canonical(route(args.state, args.commit)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
