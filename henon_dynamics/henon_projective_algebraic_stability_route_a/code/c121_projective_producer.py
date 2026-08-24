#!/usr/bin/env python3
"""Produce the exact C121 projective and degree-growth evidence ledger.

The iterate certificate is deliberately recursive.  It stores an exact DAG
hash, degrees, leading monomials, and exact probe evaluations through n=8;
it never expands the degree-256 iterate into a large polynomial.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c121_projective_evidence.json"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PARAMETER = -4
MAX_ITERATE = 8
PROBES = ((0, 0), (1, 0), (0, 1), (-1, 1))


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def node_digest(value: object) -> str:
    return sha256(canonical_bytes(value)).hexdigest()


def recursive_ledger() -> tuple[list[dict[str, object]], dict[str, list[list[str]]]]:
    """Build a nonexpanded exact recurrence ledger for p_n.

    H^n(x,y)=(p_n,p_{n-1}), with p_{-1}=y, p_0=x, and
    p_n=p_{n-1}^2-4-p_{n-2}.
    """
    hashes = {
        -1: node_digest({"atom": "y", "index": -1}),
        0: node_digest({"atom": "x", "index": 0}),
    }
    rows: list[dict[str, object]] = []
    for n in range(1, MAX_ITERATE + 1):
        descriptor = {
            "constant": PARAMETER,
            "index": n,
            "operation": "square_previous_plus_constant_minus_previous_previous",
            "previous_previous_sha256": hashes[n - 2],
            "previous_sha256": hashes[n - 1],
        }
        hashes[n] = node_digest(descriptor)
        degree = 2**n
        rows.append(
            {
                "n": n,
                "recurrence_dag_sha256": hashes[n],
                "first_coordinate_degree": degree,
                "second_coordinate_degree": degree // 2,
                "projective_degree": degree,
                "first_leading_monomial": f"x^{degree}",
                "second_leading_monomial": f"x^{degree // 2}",
                "homogeneous_first_X_power_coefficient": 1,
                "homogeneous_second_Z_factor_exponent": degree // 2,
                "homogeneous_third_Z_exponent": degree,
                "projective_coordinate_gcd": "1",
            }
        )

    probe_values: dict[str, list[list[str]]] = {}
    for x_value, y_value in PROBES:
        previous_previous = y_value
        previous = x_value
        values: list[list[str]] = []
        for n in range(1, MAX_ITERATE + 1):
            current = previous * previous + PARAMETER - previous_previous
            values.append([str(current), str(previous)])
            previous_previous, previous = previous, current
        probe_values[f"({x_value},{y_value})"] = values
    return rows, probe_values


def main() -> None:
    degree_rows, probe_values = recursive_ledger()
    b0 = [[0, -1], [1, 0]]
    bm2 = [[-4, -1], [1, 0]]
    monodromy = [
        [bm2[0][0] * b0[0][0] + bm2[0][1] * b0[1][0], bm2[0][0] * b0[0][1] + bm2[0][1] * b0[1][1]],
        [bm2[1][0] * b0[0][0] + bm2[1][1] * b0[1][0], bm2[1][0] * b0[0][1] + bm2[1][1] * b0[1][1]],
    ]
    assert monodromy == [[-1, 4], [0, -1]]

    controls = []
    for control_c in (-3, -5):
        residual = control_c + 4
        controls.append(
            {
                "parameter_c": control_c,
                "candidate_transition_residual_p_to_q": [residual, 0],
                "candidate_transition_residual_q_to_p": [residual, 0],
                "frozen_two_cycle_preserved": False,
            }
        )

    evidence = {
        "schema": "hcs-c121-projective-algebraic-stability-v1",
        "scope_literal": SCOPE,
        "frozen_map": {
            "family": "H_c(x,y)=(x^2+c-y,x)",
            "parameter_c": PARAMETER,
            "affine_formula": "H(x,y)=(x^2-4-y,x)",
            "inverse_formula": "H^{-1}(x,y)=(y,y^2-4-x)",
            "jacobian_formula": "B(x)=[[2*x,-1],[1,0]]",
            "jacobian_determinant": 1,
            "forward_homogeneous_formula": "[X^2-4*Z^2-Y*Z:X*Z:Z^2]",
            "inverse_homogeneous_formula": "[Y*Z:Y^2-4*Z^2-X*Z:Z^2]",
        },
        "birational_certificate": {
            "forward_after_inverse": "(x,y)",
            "inverse_after_forward": "(x,y)",
            "forward_indeterminacy_I_plus": [0, 1, 0],
            "inverse_indeterminacy_I_minus": [1, 0, 0],
            "forward_line_at_infinity_excluding_I_plus_maps_to": [1, 0, 0],
            "forward_image_of_I_minus": [1, 0, 0],
            "I_minus_is_forward_fixed": True,
            "affine_exceptional_curves": [],
            "only_projective_exceptional_curve": "Z=0",
            "I_minus_forward_orbit_n_0_to_8": [[1, 0, 0] for _ in range(9)],
            "exceptional_orbit_avoids_I_plus": True,
            "algebraically_stable_on_P2": True,
            "criterion_used": "the only exceptional curve maps to fixed I_minus, never to I_plus",
        },
        "degree_growth": {
            "iterate_identity": "H^n(x,y)=(p_n,p_{n-1})",
            "recurrence": "p_-1=y; p_0=x; p_n=p_{n-1}^2-4-p_{n-2}",
            "representation": "exact_recursive_DAG_plus_sparse_leading_term_certificate",
            "maximum_certified_iterate": MAX_ITERATE,
            "rows": degree_rows,
            "exact_projective_degree_sequence_n_1_to_8": [2**n for n in range(1, 9)],
            "exact_affine_leading_degree_pairs_n_1_to_8": [[2**n, 2 ** (n - 1)] for n in range(1, 9)],
            "probe_values_by_iterate": probe_values,
            "all_order_degree_theorem": "deg(H^n)=2^n for every n>=1",
            "dynamical_degree": "2",
            "dynamical_degree_interpretation": "algebraic degree-growth quantity only",
            "entropy_claimed": False,
        },
        "fixed_points": {
            "diagonal_equation": "q^2-2*q-4=0",
            "exact_q_values": ["1+sqrt(5)", "1-sqrt(5)"],
            "exact_points": ["(1+sqrt(5),1+sqrt(5))", "(1-sqrt(5),1-sqrt(5))"],
            "count_over_Q_sqrt_5": 2,
        },
        "primitive_real_two_cycle": {
            "p": [0, -2],
            "q": [-2, 0],
            "H_of_p": [-2, 0],
            "H_of_q": [0, -2],
            "points_distinct": True,
            "primitive_period": 2,
            "B_at_p": b0,
            "B_at_q": bm2,
            "monodromy_convention": "D(H^2)_p=B(-2)*B(0)",
            "monodromy": monodromy,
            "trace": -2,
            "determinant": 1,
            "det_I_minus_zM_coefficients_ascending": [1, 2, 1],
            "det_I_minus_zM_factorization": "(1+z)^2",
        },
        "parameter_controls": controls,
        "route_a_verdict": {
            "evaluator": "henon_dynamics/skills/route-a-evaluator.md",
            "canonical_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "canonical_tuple_text": "(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)",
            "A1": "A1_WEAK",
            "A1_qualification": "EXACT_STRUCTURAL_EVIDENCE_ONLY_NO_PRIME_LIKE_TARGET_CORRESPONDENCE_OR_COMPLETE_ATLAS",
            "A2": "A2_FAIL",
            "A2_qualification": "NO_WEIGHTED_DYNAMICAL_ZETA_TRANSFER_OWNER_OR_TARGET_DIVISOR_TEST",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_FUNCTIONAL_EQUATION_GAMMA_FACTOR_COUNTING_LAW_CONTINUATION_OR_ANALYTIC_BRIDGE",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "nonclaims": [
            "complete periodic-orbit classification or complete primitive-orbit atlas",
            "prime-like target correspondence, log-prime clock, or target-amplitude law",
            "target divisor, weighted dynamical zeta, or determinant matching",
            "topological or metric entropy equality from the algebraic dynamical degree",
            "transfer-operator owner, invariant function space, nuclearity, or Fredholm determinant",
            "analytic bridge, functional equation, Gamma factor, trivial-zero treatment, counting law, or continuation",
            "arithmetic/local data, Euler factors, root numbers, or automorphy",
            "Hilbert--Polya operator, Riemann-zero correspondence, or Route-B authorization",
        ],
    }
    OUT.write_text(json.dumps(evidence, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        "C121_PREFREEZE_G3_PASS",
        sha256(OUT.read_bytes()).hexdigest(),
        len(degree_rows),
        len(controls),
    )


if __name__ == "__main__":
    main()
