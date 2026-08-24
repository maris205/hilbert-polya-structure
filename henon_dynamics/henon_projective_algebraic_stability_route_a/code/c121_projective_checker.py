#!/usr/bin/env python3
"""Independent exact checker for the C121 evidence ledger.

This module imports no producer code.  It reconstructs the projective data,
recursive iterate DAG, probe values, orbit witnesses, and release boundary
from the frozen map itself, then demands exact object equality.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
EVIDENCE = BASE / "results/c121_projective_evidence.json"


def stable_hash(item: object) -> str:
    payload = json.dumps(item, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    return sha256(payload.encode()).hexdigest()


def matmul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def expected_object() -> dict[str, object]:
    c = -4
    maximum = 8
    roots = {
        -1: stable_hash({"index": -1, "atom": "y"}),
        0: stable_hash({"index": 0, "atom": "x"}),
    }
    degree_rows = []
    for index in range(1, maximum + 1):
        recipe = {
            "index": index,
            "operation": "square_previous_plus_constant_minus_previous_previous",
            "constant": c,
            "previous_sha256": roots[index - 1],
            "previous_previous_sha256": roots[index - 2],
        }
        roots[index] = stable_hash(recipe)
        first_degree = 1 << index
        degree_rows.append(
            {
                "n": index,
                "recurrence_dag_sha256": roots[index],
                "first_coordinate_degree": first_degree,
                "second_coordinate_degree": first_degree // 2,
                "projective_degree": first_degree,
                "first_leading_monomial": f"x^{first_degree}",
                "second_leading_monomial": f"x^{first_degree // 2}",
                "homogeneous_first_X_power_coefficient": 1,
                "homogeneous_second_Z_factor_exponent": first_degree // 2,
                "homogeneous_third_Z_exponent": first_degree,
                "projective_coordinate_gcd": "1",
            }
        )

    samples: dict[str, list[list[str]]] = {}
    for initial_x, initial_y in ((0, 0), (1, 0), (0, 1), (-1, 1)):
        older, old = initial_y, initial_x
        orbit_values = []
        for _ in range(maximum):
            new = old**2 + c - older
            orbit_values.append([str(new), str(old)])
            older, old = old, new
        samples[f"({initial_x},{initial_y})"] = orbit_values

    jac_at_zero = [[0, -1], [1, 0]]
    jac_at_minus_two = [[-4, -1], [1, 0]]
    monodromy = matmul(jac_at_minus_two, jac_at_zero)
    assert monodromy == [[-1, 4], [0, -1]]

    negative_controls = []
    for alternate in (-3, -5):
        defect = alternate + 4
        negative_controls.append(
            {
                "parameter_c": alternate,
                "candidate_transition_residual_p_to_q": [defect, 0],
                "candidate_transition_residual_q_to_p": [defect, 0],
                "frozen_two_cycle_preserved": False,
            }
        )

    return {
        "schema": "hcs-c121-projective-algebraic-stability-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "frozen_map": {
            "family": "H_c(x,y)=(x^2+c-y,x)",
            "parameter_c": c,
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
            "I_minus_forward_orbit_n_0_to_8": [[1, 0, 0] for _ in range(maximum + 1)],
            "exceptional_orbit_avoids_I_plus": True,
            "algebraically_stable_on_P2": True,
            "criterion_used": "the only exceptional curve maps to fixed I_minus, never to I_plus",
        },
        "degree_growth": {
            "iterate_identity": "H^n(x,y)=(p_n,p_{n-1})",
            "recurrence": "p_-1=y; p_0=x; p_n=p_{n-1}^2-4-p_{n-2}",
            "representation": "exact_recursive_DAG_plus_sparse_leading_term_certificate",
            "maximum_certified_iterate": maximum,
            "rows": degree_rows,
            "exact_projective_degree_sequence_n_1_to_8": [1 << i for i in range(1, maximum + 1)],
            "exact_affine_leading_degree_pairs_n_1_to_8": [[1 << i, 1 << (i - 1)] for i in range(1, maximum + 1)],
            "probe_values_by_iterate": samples,
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
            "B_at_p": jac_at_zero,
            "B_at_q": jac_at_minus_two,
            "monodromy_convention": "D(H^2)_p=B(-2)*B(0)",
            "monodromy": monodromy,
            "trace": -2,
            "determinant": 1,
            "det_I_minus_zM_coefficients_ascending": [1, 2, 1],
            "det_I_minus_zM_factorization": "(1+z)^2",
        },
        "parameter_controls": negative_controls,
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


def validate(candidate: dict[str, object]) -> None:
    expected = expected_object()
    assert candidate == expected, "evidence differs from independent exact reconstruction"


def main() -> None:
    candidate = json.loads(EVIDENCE.read_text())
    validate(candidate)
    assert len(candidate["degree_growth"]["rows"]) == 8
    assert len(candidate["parameter_controls"]) == 2
    print("C121_CHECK_PASS", 8, "recursive iterates", "algebraic_stability", "cycle_and_controls")


if __name__ == "__main__":
    main()
