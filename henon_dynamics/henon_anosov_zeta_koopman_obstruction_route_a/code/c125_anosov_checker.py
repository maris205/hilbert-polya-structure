#!/usr/bin/env python3
"""Independent exact checker for C125; imports no producer code."""
from __future__ import annotations

import json
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
EVIDENCE = BASE / "results/c125_anosov_evidence.json"
MATRIX = ((2, 1), (1, 1))


def multiply(left, right):
    return tuple(
        tuple(sum(left[row][inner] * right[inner][column] for inner in range(2)) for column in range(2))
        for row in range(2)
    )


def power(exponent: int):
    answer = ((1, 0), (0, 1))
    for _ in range(exponent):
        answer = multiply(MATRIX, answer)
    return answer


def det(matrix) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def factorization(integer: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    candidate = 2
    remainder = integer
    while candidate * candidate <= remainder:
        while remainder % candidate == 0:
            factors[candidate] = factors.get(candidate, 0) + 1
            remainder //= candidate
        candidate += 1
    if remainder > 1:
        factors[remainder] = factors.get(remainder, 0) + 1
    return factors


def mu(integer: int) -> int:
    if integer == 1:
        return 1
    factors = factorization(integer)
    if any(exponent > 1 for exponent in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def all_divisors(integer: int) -> list[int]:
    return [value for value in range(1, integer + 1) if integer % value == 0]


def cyclic_trace(iterate: int, modulus: int) -> int:
    iterate_matrix = power(iterate)
    answer = 0
    for first in range(modulus):
        for second in range(modulus):
            first_equation = (iterate_matrix[0][0] - 1) * first + iterate_matrix[0][1] * second
            second_equation = iterate_matrix[1][0] * first + (iterate_matrix[1][1] - 1) * second
            answer += int(first_equation % modulus == 0 and second_equation % modulus == 0)
    return answer


def independent_object() -> dict[str, object]:
    max_period = 12
    traces = [2, 3]
    while len(traces) <= max_period:
        traces.append(3 * traces[-1] - traces[-2])

    rows = []
    for n in range(1, max_period + 1):
        matrix_n = power(n)
        matrix_minus_identity = (
            (matrix_n[0][0] - 1, matrix_n[0][1]),
            (matrix_n[1][0], matrix_n[1][1] - 1),
        )
        signed = det(matrix_minus_identity)
        fixed = -signed
        primitive = sum(mu(n // divisor) * (traces[divisor] - 2) for divisor in all_divisors(n))
        rows.append(
            {
                "n": n,
                "A_power": [list(matrix_n[0]), list(matrix_n[1])],
                "trace_A_power": traces[n],
                "signed_det_A_power_minus_I": signed,
                "fixed_point_count": fixed,
                "primitive_point_count": primitive,
                "primitive_orbit_count": primitive // n,
            }
        )

    coefficients = [1, 1, 3]
    while len(coefficients) <= max_period:
        coefficients.append(3 * coefficients[-1] - coefficients[-2])

    wrap_rows = [
        {
            "iterate_n": n,
            "moduli_2_to_12": list(range(2, 13)),
            "wraparound_traces": [cyclic_trace(n, modulus) for modulus in range(2, 13)],
        }
        for n in (2, 3, 4, 6)
    ]
    basis_rows = [
        {"source_k": [j, 0], "image_A_transpose_k": [2 * j, j]}
        for j in range(1, 13)
    ]

    return {
        "schema": "hcs-c125-anosov-zeta-koopman-obstruction-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_baseline_commit": "ab22333a24eacecdd33c9fb07a9394d9fe0cc99b",
        "frozen_system": {
            "phase_space": "T^2=R^2/Z^2 with normalized Haar measure",
            "matrix_A": [[2, 1], [1, 1]],
            "determinant_A": 1,
            "trace_A": 3,
            "map": "T_A([x])=[A*x]",
            "clock": "one torus iterate",
            "normalization": "unweighted Artin-Mazur fixed-point convention",
            "eigenvalues": ["(3+sqrt(5))/2", "(3-sqrt(5))/2"],
            "hyperbolic": True,
        },
        "all_order_fixed_point_theorem": {
            "statement": "N_n=#Fix(T_A^n)=|det(A^n-I)|=S_n-2 for every n>=1",
            "trace_recurrence": "S_0=2; S_1=3; S_n=3*S_{n-1}-S_{n-2}",
            "reason_kernel_count": "A^n-I is an integer matrix nonsingular over R, so its torus kernel has cardinality |det(A^n-I)|",
            "maximum_replayed_period": max_period,
            "rows": rows,
            "fixed_point_counts_n_1_to_12": [row["fixed_point_count"] for row in rows],
            "primitive_point_counts_n_1_to_12": [row["primitive_point_count"] for row in rows],
            "primitive_orbit_counts_n_1_to_12": [row["primitive_orbit_count"] for row in rows],
            "completeness": "all torus fixed points at every n, not an orbit search cutoff",
        },
        "artin_mazur_zeta": {
            "definition": "zeta_T(z)=exp(sum_{n>=1} #Fix(T_A^n)*z^n/n)",
            "primitive_product": "zeta_T(z)=product_gamma (1-z^period(gamma))^{-1}",
            "exact_rational_function": "(1-z)^2/(1-3*z+z^2)",
            "derivation": "N_n=lambda_+^n+lambda_-^n-2 with lambda_+*lambda_-=1",
            "series_coefficients_z_0_to_12": coefficients,
            "formal_and_meromorphic_identity": True,
            "target_divisor_compared": False,
        },
        "koopman_obstruction": {
            "hilbert_space": "L^2(T^2,Haar)",
            "operator": "U f=f composed with T_A",
            "fourier_basis": "e_k(x)=exp(2*pi*i*k dot x), k in Z^2",
            "fourier_action": "U e_k=e_{A^T k}",
            "index_action_bijective": True,
            "unitary": True,
            "orthonormal_test_sources_and_images": basis_rows,
            "noncompact": True,
            "noncompact_reason": "the bounded orthonormal sequence e_(j,0) maps to the orthonormal sequence e_(2j,j), which has no norm-convergent subsequence",
            "schatten_membership_for_any_finite_p": False,
            "trace_class": False,
            "ordinary_operator_trace_defined": False,
            "ordinary_trace_class_fredholm_determinant_defined": False,
            "artin_mazur_zeta_is_not_declared_equal_to_det_I_minus_zU": True,
        },
        "negative_controls": {
            "parabolic_shear": {
                "matrix_B": [[1, 1], [0, 1]],
                "B_power": "[[1,n],[0,1]]",
                "det_B_power_minus_I": 0,
                "fixed_set_of_B_power": "n disjoint circles: y=j/n mod 1 with x arbitrary",
                "standard_finite_fixed_point_count_available": False,
            },
            "drop_absolute_value": {
                "signed_sequence_n_1_to_12": [row["signed_det_A_power_minus_I"] for row in rows],
                "all_entries_negative": True,
                "valid_as_fixed_point_counts": False,
                "interpretation": "signed Lefschetz data are not unsigned cardinalities",
            },
            "wraparound_fourier_aliasing": {
                "definition": "replace Z^2 by (Z/mZ)^2 and count fixed Fourier indices of A^{Tn} modulo m",
                "rows": wrap_rows,
                "cutoff_independent": False,
                "ordinary_koopman_trace_approximation": False,
                "interpretation": "finite cyclic aliasing creates modulus-dependent pseudo-traces",
            },
        },
        "progress_over_prior_gate": {
            "C121": "upgrades an all-order algebraic degree law plus one two-cycle to an all-order complete fixed/primitive orbit census and exact Artin-Mazur zeta",
            "C119": "puts rich recurrent dynamics and a natural global Hilbert-space action in one source model, then proves that the natural action is unitary rather than determinant class",
            "joint_gate_result": "complete orbit zeta and natural Koopman owner coexist, but they are not the same ordinary Fredholm determinant",
        },
        "route_a_verdict": {
            "evaluator": "henon_dynamics/skills/route-a-evaluator.md",
            "canonical_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "canonical_tuple_text": "(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)",
            "A1": "A1_WEAK",
            "A1_qualification": "COMPLETE_INTRINSIC_PRIMITIVE_ORBIT_CENSUS_BUT_NO_PRIME_LIKE_TARGET_CORRESPONDENCE_OR_AMPLITUDE_LAW",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_INTERNAL_ARTIN_MAZUR_ZETA_BUT_NO_TARGET_DIVISOR_OR_SEALED_ZERO_COMPARISON_AND_NATURAL_KOOPMAN_IS_NOT_DETERMINANT_CLASS",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_GAMMA_FACTOR_COUNTING_LAW_OR_CONTROLLED_TARGET_CONTINUATION",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "NATURAL_UNITARY_KOOPMAN_ACTION_EXISTS_BUT_NO_TRACE_COMPATIBLE_QUANTIZATION_OR_ORBIT_PHASE_LIFT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "prime-like orbit correspondence, logarithmic-prime clock, target amplitude law, or complete arithmetic labeling",
            "target divisor match, missing/extra target-zero census, sealed validation pass, or identification of the Artin-Mazur zeta with a target function",
            "ordinary operator trace or ordinary trace-class Fredholm determinant for the Koopman unitary",
            "functional equation, Gamma factor, trivial-zero treatment, Riemann-von Mangoldt law, or target analytic continuation",
            "arithmetic/local data, Euler factors, root numbers, automorphy, or an adelic assembly",
            "Hilbert--Polya operator, Riemann-zero correspondence, A4 natural quantization, or Route-B authorization",
        ],
    }


def validate(candidate: dict[str, object]) -> None:
    assert candidate == independent_object(), "C125 evidence differs from independent reconstruction"


def main() -> None:
    candidate = json.loads(EVIDENCE.read_text())
    validate(candidate)
    print("C125_CHECK_PASS", 12, "all-order rows", 4, "control families", "koopman_noncompact")


if __name__ == "__main__":
    main()
