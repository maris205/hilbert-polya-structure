#!/usr/bin/env python3
"""Run the data-free exact construction and control preflight."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import sympy as sp

from _common import add_output_argument, output_path, write_json_new
from branch_baker.algebra import exact_identity_audit
from branch_baker.controls import (
    FuturePoint,
    LabelErasureControl,
    binary_primitive_necklace_counts,
    inspect_anti_symplectic_derivatives,
    make_all_positive_sign_null,
    make_candidate,
    make_dyadic_baker,
    make_folded_tent_baker,
    make_matched_dissipative,
)
from branch_baker.cycles import (
    boundary_quotient_ledger,
    exact_candidate_cycle_audit,
)
from branch_baker.protocol import (
    CODE_ROOT,
    SOURCE_LOCK_PATH,
    sha256_file,
)
from branch_baker.zeta import exact_zeta_audit


def static_isolation_audit() -> dict[str, object]:
    lock = json.loads(SOURCE_LOCK_PATH.read_text(encoding="utf-8"))
    forbidden = lock["static_isolation_forbidden_tokens"]
    violations: list[str] = []
    for path in CODE_ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".py", ".md"}:
            continue
        text = path.read_text(encoding="utf-8")
        for token in forbidden:
            if token in text:
                violations.append(
                    f"{path.relative_to(CODE_ROOT).as_posix()}:{token}"
                )
    return {"forbidden_tokens": forbidden, "violations": violations, "passed": not violations}


def control_audit() -> dict[str, object]:
    candidate = make_candidate()
    dyadic = make_dyadic_baker()
    folded = make_folded_tent_baker()
    dissipative = make_matched_dissipative()
    sign_null = make_all_positive_sign_null()
    anti = inspect_anti_symplectic_derivatives()
    future = FuturePoint(2, 0.3)

    candidate_determinants = {
        f"{edge.source}->{edge.target}": candidate.determinant(
            edge.source, edge.target
        )
        for edge in candidate.edges
    }
    dissipative_determinants = {
        f"{edge.source}->{edge.target}": dissipative.determinant(
            edge.source, edge.target
        )
        for edge in dissipative.edges
    }
    anti_determinants = {
        f"{edge.source}->{edge.target}": determinant
        for edge, determinant in anti.items()
    }
    positive_weight_matrix = sp.Matrix(
        [
            [
                sign_null.unstable_signs.get((source, target), 0)
                if sign_null.adjacency[source][target]
                else 0
                for target in range(3)
            ]
            for source in range(3)
        ]
    )
    z = sp.Symbol("z")
    gates = {
        "candidate_symplectic": candidate.is_symplectic(),
        "dyadic_symplectic": dyadic.is_symplectic(),
        "dyadic_ledger_total": sum(binary_primitive_necklace_counts(12)) == 747,
        "folded_branch_symplectic": folded.determinant(1) == 1.0,
        "matched_dissipative_same_graph": dissipative.adjacency == candidate.adjacency,
        "matched_dissipative_det_half": all(
            determinant == 0.5 for determinant in dissipative_determinants.values()
        ),
        "matched_dissipative_non_surjective": all(
            dissipative.destination_image(edge)[1]
            < dissipative.destination_strip(edge)[1]
            for edge in dissipative.edges
        ),
        "label_erasure_loses_past": LabelErasureControl.loses_unique_past(future),
        "anti_symplectic_rejected_signature": any(
            determinant == -1.0 for determinant in anti_determinants.values()
        ),
        "all_positive_null_same_unsigned_graph": sign_null.adjacency
        == candidate.adjacency,
        "all_positive_null_changes_signs": sign_null.unstable_signs
        != candidate.unstable_signs,
        "all_positive_null_weight_matrix_is_A": positive_weight_matrix
        == sp.Matrix(candidate.adjacency),
        "all_positive_null_removes_nilpotent_cancellation": sp.factor(
            (sp.eye(3) - z * positive_weight_matrix).det()
        )
        == 1 - 2 * z**2,
    }
    return {
        "candidate_determinants": candidate_determinants,
        "dissipative_determinants": dissipative_determinants,
        "anti_symplectic_determinants": anti_determinants,
        "gates": gates,
        "passed": all(gates.values()),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    add_output_argument(parser, "results/exact_preflight.json")
    args = parser.parse_args()

    algebra = exact_identity_audit()
    cycles = exact_candidate_cycle_audit(20)
    boundary = boundary_quotient_ledger(20)
    zeta = exact_zeta_audit()
    controls = control_audit()
    isolation = static_isolation_audit()
    gates = {
        "algebra": all(algebra.values()),
        "candidate_cycle_ledger": cycles.passed,
        "single_boundary_quotient": boundary.sole_declared_collapse_verified,
        "zeta_conventions": all(zeta.values()),
        "controls": bool(controls["passed"]),
        "static_isolation": bool(isolation["passed"]),
    }
    payload = {
        "candidate_id": "pcf_markov_baker_v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_lock_sha256": sha256_file(SOURCE_LOCK_PATH),
        "execution_type": "data-free exact preflight",
        "external_prime_or_zero_data_accessed": False,
        "algebra": algebra,
        "cycle_audit": cycles.as_dict(),
        "boundary_quotient": boundary.as_dict(),
        "zeta": zeta,
        "controls": controls,
        "static_isolation": isolation,
        "gates": gates,
        "passed": all(gates.values()),
    }
    write_json_new(output_path(args.output), payload)


if __name__ == "__main__":
    main()
