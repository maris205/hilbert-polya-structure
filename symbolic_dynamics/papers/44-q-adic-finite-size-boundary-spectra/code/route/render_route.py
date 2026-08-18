#!/usr/bin/env python3
"""Render the exact Route-A card and bind every declared evidence artifact."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
from pathlib import Path, PurePosixPath
from typing import Any


BOUND = [
    "outputs/audits/external_auditor_mutations.json",
    "outputs/audits/independence_audit.json",
    "outputs/audits/proof_audit.json",
    "outputs/audits/source_audit.json",
    "outputs/audits/type_audit.json",
    "outputs/data/source_packet.json",
    "outputs/results/evaluator_a.json",
    "outputs/results/evaluator_b.json",
    "outputs/results/exact_comparison.json",
    "outputs/tests/mutation_results.json",
]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate key")
        out[key] = value
    return out


def safe_relative(value: str) -> bool:
    pure = PurePosixPath(value)
    return type(value) is str and value != "" and "\\" not in value \
        and not pure.is_absolute() and all(part not in {"", ".", ".."} for part in pure.parts)


def regular_inside(stage: Path, supplied: str) -> Path:
    if not stage.is_absolute() or stage.is_symlink() or not stage.is_dir():
        raise ValueError("unsafe stage")
    path = Path(supplied)
    if not path.is_absolute():
        raise ValueError("absolute path required")
    base = stage.resolve(strict=True)
    cursor = path
    while cursor != base:
        if cursor == cursor.parent or cursor.is_symlink():
            raise ValueError("unsafe ancestry")
        cursor = cursor.parent
    resolved = path.resolve(strict=True)
    info = os.lstat(resolved)
    if base not in resolved.parents or not stat.S_ISREG(info.st_mode):
        raise ValueError("regular containment")
    return resolved


def binding(stage: Path, relative: str) -> dict[str, Any]:
    if not safe_relative(relative):
        raise ValueError("unsafe artifact relative")
    path = regular_inside(stage, str(stage.joinpath(*relative.split("/"))))
    mode = stat.S_IMODE(os.lstat(path).st_mode)
    if mode != 0o644:
        raise ValueError("artifact mode")
    return {"kind": "regular", "mode": "0644", "path": relative,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def card(stage: Path, comparison_raw: bytes, state: str, commit: str | None) -> dict[str, Any]:
    if state == "A":
        if commit is not None:
            raise ValueError("State A commit forbidden")
        source_commit, code_commit, lock_commit = "PREAUTHORITY_NO_COMMIT", "NONE", "NONE"
        manifest_present = False
    else:
        if type(commit) is not str or re.fullmatch(r"[0-9a-f]{40}", commit) is None \
                or commit == "0" * 40:
            raise ValueError("State B commit")
        source_commit = code_commit = lock_commit = commit
        manifest_present = True
    bindings = [binding(stage, relative) for relative in BOUND]
    return {
        "a0": {
            "arithmetic_controls": ["one_symbol_zero_boundary", "full_shift_zero_boundary", "composite_q_control"],
            "evidence_status": "MODELING_CHOICE", "verdict": "A0_FAIL",
        },
        "a1": {
            "evidence_status": "NOT_TESTABLE", "periodic_orbit_ledger": False,
            "rational_prime_primitive_support": False, "verdict": "A1_FAIL",
        },
        "a2": {
            "determinant_defined": False, "evidence_status": "NOT_TESTABLE",
            "ordinary_cutoff_generating_function": True, "target_divisor_comparison": False,
            "trace_family_defined": False, "verdict": "A2_FAIL",
        },
        "a3": {
            "evidence_status": "PROVED", "meromorphic_continuation": False,
            "unit_circle_natural_boundary": "golden_control_only",
            "verdict": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "weil_compression": {"evidence_status": "NOT_TESTABLE",
                                 "status": "not_available_no_same_ledger_target_divisor"},
        },
        "a4": {
            "evidence_status": "NOT_TESTABLE",
            "fixed_self_adjoint_hilbert_polya_operator_defined": False,
            "route_b_readiness": False, "verdict": "A4_FAIL",
        },
        "artifact_bindings": bindings,
        "artifact_path_base": ".",
        "artifact_paths": list(BOUND),
        "authority_integration": {
            "authority_writes": 0, "git_operations": 0,
            "paper_manifest_present": manifest_present, "state": state,
        },
        "candidate_id": "SD-C46",
        "claim_boundary": "Exact q-adic order-one prefix remainder and complete accumulation image; golden Cantor image and dense radial singularities only. No leading-result novelty, ordinary Minkowski content, determinant, completed divisor, or spectral-operator claim.",
        "code_commit": code_commit,
        "evaluation_date": "2026-08-18",
        "external_literature_disposition": {
            "exact_source_collision": "STOP_DUPLICATE_LIVE_CONDITIONAL",
            "owner": "literature_and_publication_review_not_route_terminal",
        },
        "finite_evidence_boundary": "FINITE_RESULTS_DO_NOT_PROVE_INFINITE_THEOREMS",
        "overall_verdict": "ROUTE_A_REJECTED",
        "projection_firewall": {
            "boundary_state_type": "qAdicInverseLimitState",
            "boundary_value_type": "RealOrderOneRemainder",
            "cutoff_type": "PositivePrefixCutoff",
            "marker_type": "OrdinaryPrefixGeneratingMarker",
            "source_type": "OneSidedMultiplicativeSFT",
        },
        "round2_clues": [],
        "route_b": {"invocation_allowed": False,
                    "reason": "no_same_object_primitive_ledger_completed_divisor_or_operator"},
        "route_tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"],
        "schema": "paper44-route-a-v0.3",
        "science_sha256": hashlib.sha256(comparison_raw).hexdigest(),
        "skill": "route-a-evaluator", "skill_version": "0.3.0",
        "source_commit": source_commit,
        "source_lock": {
            "code_commit": lock_commit, "object": "multiplicative_shift_of_finite_type_X_A_q",
            "parameters": "explicit_integer_q_and_primitive_zero_one_A",
        },
        "terminal_codes": {
            "determinant_or_zeta_retyping": "TYPE_OWNER_ERROR",
            "nonprimitive_extension": "STOP_SCOPED",
            "ordinary_content_claim": "NOT_CURRENTLY_JUSTIFIED",
            "theorem_counterexample": "THEOREM_STOP",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", required=True)
    parser.add_argument("--comparison", required=True)
    parser.add_argument("--state", choices=("A", "B"), required=True)
    parser.add_argument("--commit")
    args = parser.parse_args()
    stage = Path(args.stage)
    comparison_path = regular_inside(stage, args.comparison)
    comparison_raw = comparison_path.read_bytes()
    comparison = json.loads(comparison_raw.decode("ascii"), object_pairs_hook=unique)
    if comparison_raw != canonical(comparison) or set(comparison) != {"payload", "schema", "status"} \
            or comparison["schema"] != "paper44-exact-comparison-v1" or comparison["status"] != "PASS":
        raise ValueError("comparison envelope")
    sys.stdout.buffer.write(canonical(card(stage, comparison_raw, args.state, args.commit)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
