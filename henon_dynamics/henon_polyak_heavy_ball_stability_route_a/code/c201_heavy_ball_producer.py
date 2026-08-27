#!/usr/bin/env python3
"""Produce the deterministic exact C201 heavy-ball certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


SOURCE_COMMIT = "d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c201_heavy_ball_evidence.json"
M, L = F(1), F(4)
PARAMETER_CASES = [
    ("stable_negative_momentum", F(1, 8), F(-1, 2)),
    ("stable_zero_momentum", F(1, 4), F(0)),
    ("stable_positive_momentum", F(1, 2), F(1, 4)),
    ("alpha_zero_boundary", F(0), F(1, 4)),
    ("flip_boundary", F(5, 8), F(1, 4)),
    ("beta_one_elliptic", F(1, 4), F(1)),
    ("beta_one_parabolic", F(1), F(1)),
    ("beta_minus_one_swap", F(0), F(-1)),
    ("beta_above_one", F(1, 8), F(3, 2)),
    ("beta_below_minus_one", F(1, 8), F(-3, 2)),
    ("alpha_above_flip", F(3, 4), F(1, 4)),
    ("negative_alpha", F(-1, 8), F(0)),
    ("polyak_optimum_1_4", F(4, 9), F(1, 9)),
    ("interior_jordan_curve", F(9, 16), F(1, 4)),
]
OPTIMAL_INTERVALS = [(1, 2), (1, 3), (2, 3), (2, 2)]  # square roots of m,L


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def matmul(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def identity(size):
    return [[F(i == j) for j in range(size)] for i in range(size)]


def power(matrix, exponent):
    result = identity(len(matrix))
    base = matrix
    while exponent:
        if exponent & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        exponent //= 2
    return result


def determinant(matrix):
    work = [row[:] for row in matrix]
    value = F(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return F(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value *= -1
        pivot_value = work[column][column]
        value *= pivot_value
        for j in range(column, len(work)):
            work[column][j] /= pivot_value
        for row in range(column + 1, len(work)):
            factor = work[row][column]
            for j in range(column, len(work)):
                work[row][j] -= factor * work[column][j]
    return value


def scalar_block(lam: F, alpha: F, beta: F):
    return [[F(1) + beta - alpha * lam, -beta], [F(1), F(0)]]


def root_expression(a: F, beta: F) -> str:
    discriminant = a * a - 4 * beta
    if beta >= 0 and discriminant <= 0:
        return f"sqrt({beta})"
    return f"(abs({a})+sqrt({discriminant}))/2"


def regime(alpha: F, beta: F) -> str:
    if -1 < beta < 1 and alpha > 0 and alpha * L < 2 * (1 + beta):
        return "robustly_schur_stable"
    if -1 < beta < 1 and alpha == 0:
        return "alpha_zero_fixed_mode"
    if -1 < beta < 1 and alpha > 0 and alpha * L == 2 * (1 + beta):
        return "flip_endpoint"
    if beta == 1 and 0 < alpha * M and alpha * L < 4:
        return "symplectic_elliptic"
    if beta == 1 and alpha > 0 and alpha * L == 4:
        return "symplectic_parabolic_endpoint"
    if beta == -1 and alpha == 0:
        return "order_two_swap"
    return "unstable_or_nonconvergent"


def endpoint_row(lam: F, alpha: F, beta: F) -> dict:
    a = 1 + beta - alpha * lam
    return {
        "lambda": str(lam),
        "trace_a": str(a),
        "determinant_beta": str(beta),
        "discriminant": str(a * a - 4 * beta),
        "p_at_plus_one": str(alpha * lam),
        "p_at_minus_one": str(2 * (1 + beta) - alpha * lam),
        "root_radius_expression": root_expression(a, beta),
    }


def full_matrix(a_matrix, alpha: F, beta: F):
    size = len(a_matrix)
    top_left = [[(F(1) + beta) * F(i == j) - alpha * a_matrix[i][j]
                 for j in range(size)] for i in range(size)]
    matrix = []
    for i in range(size):
        matrix.append(top_left[i] + [-beta * F(i == j) for j in range(size)])
    for i in range(size):
        matrix.append([F(i == j) for j in range(size)] + [F(0) for _ in range(size)])
    return matrix


def build() -> dict:
    cases = []
    for case_id, alpha, beta in PARAMETER_CASES:
        stable = -1 < beta < 1 and alpha > 0 and alpha * L < 2 * (1 + beta)
        cases.append({
            "case_id": case_id,
            "m": str(M),
            "L": str(L),
            "alpha": str(alpha),
            "beta": str(beta),
            "regime": regime(alpha, beta),
            "robustly_schur_stable": stable,
            "endpoint_rows": [endpoint_row(M, alpha, beta), endpoint_row(L, alpha, beta)],
        })

    optimal_rows = []
    for sqrt_m, sqrt_l in OPTIMAL_INTERVALS:
        m, ell = F(sqrt_m * sqrt_m), F(sqrt_l * sqrt_l)
        if sqrt_m == sqrt_l:
            q, alpha, beta = F(0), F(1, m), F(0)
            a_m = a_l = F(0)
            factors = ["r^2", "r^2"]
            transient = "one-step error annihilation; two-step nilpotent state block"
        else:
            q = F(sqrt_l - sqrt_m, sqrt_l + sqrt_m)
            alpha = F(4, (sqrt_l + sqrt_m) ** 2)
            beta = q * q
            a_m, a_l = 2 * q, -2 * q
            factors = [f"(r-{q})^2", f"(r+{q})^2"]
            transient = "endpoint Jordan blocks give generic O(k q^k), with root factor q"
        residual = (ell - m) * (1 + q * q) - 2 * q * (ell + m)
        optimal_rows.append({
            "m": str(m),
            "L": str(ell),
            "sqrt_m": str(sqrt_m),
            "sqrt_L": str(sqrt_l),
            "q": str(q),
            "alpha_star": str(alpha),
            "beta_star": str(beta),
            "a_m": str(a_m),
            "a_L": str(a_l),
            "lower_bound_residual": str(residual),
            "endpoint_factors": factors,
            "transient_class": transient,
        })

    alpha_star, beta_star = F(4, 9), F(1, 9)
    terms = {"-1": F(1), "0": F(1)}
    previous, current = F(1), F(1)
    a_m = 1 + beta_star - alpha_star
    for k in range(0, 8):
        following = a_m * current - beta_star * previous
        terms[str(k + 1)] = following
        previous, current = current, following
    for k in range(9):
        assert terms[str(k)] == (F(1) + F(2 * k, 3)) * F(1, 3) ** k
    block = scalar_block(F(1), alpha_star, beta_star)
    jordan_residual = [[block[i][j] - F(1, 3) * F(i == j) for j in range(2)] for i in range(2)]
    assert matmul(jordan_residual, jordan_residual) == [[F(0), F(0)], [F(0), F(0)]]

    q_matrix = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
    diagonal = [[F(1), F(0)], [F(0), F(4)]]
    a_matrix = matmul(matmul(q_matrix, diagonal), transpose(q_matrix))
    control_alpha, control_beta = F(1, 2), F(1, 4)
    matrix = full_matrix(a_matrix, control_alpha, control_beta)
    j_matrix = [[F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)],
                [F(-1), F(0), F(0), F(0)], [F(0), F(-1), F(0), F(0)]]
    conformal = matmul(matmul(transpose(matrix), j_matrix), matrix)
    expected_conformal = [[control_beta * value for value in row] for row in j_matrix]
    assert conformal == expected_conformal
    full_control = {
        "A": [[str(value) for value in row] for row in a_matrix],
        "alpha": str(control_alpha),
        "beta": str(control_beta),
        "state_matrix": [[str(value) for value in row] for row in matrix],
        "trace": str(sum(matrix[i][i] for i in range(4))),
        "determinant": str(determinant(matrix)),
        "conformal_symplectic_residual_zero": True,
    }

    finite_controls = []
    for label, alpha, beta, order in [
        ("quarter_turn", F(2), F(1), 4),
        ("sixth_root_rotation", F(1), F(1), 6),
        ("swap", F(0), F(-1), 2),
    ]:
        control = scalar_block(F(1), alpha, beta)
        assert power(control, order) == identity(2)
        finite_controls.append({
            "label": label,
            "lambda": "1",
            "alpha": str(alpha),
            "beta": str(beta),
            "state_matrix": [[str(value) for value in row] for row in control],
            "exact_order": order,
        })

    data = {
        "schema": "hcs-c201-heavy-ball-v1",
        "candidate_id": "HCS-C201",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": (
            "Every real-parameter heavy-ball map on an SPD spectral interval "
            "has an exact Jury atlas, a unique minimax root factor, and a "
            "Jordan-correct transient boundary"
        ),
        "frozen_object": {
            "objective": "f(x)=x^T A x/2-b^T x with A real SPD",
            "spectral_class": "m I <= A <= L I, 0<m<=L",
            "iteration": "x_(k+1)=x_k-alpha grad f(x_k)+beta(x_k-x_(k-1))",
            "parameters": "real alpha and real beta",
            "phase_state": "(e_k,e_(k-1)) in R^(2d)",
            "clock": "integer iteration k",
            "determinant_convention": "D_A(z)=det(I-z M_A), the finite source state determinant",
            "allowed_data": "exact rational SPD controls and symbolic spectral endpoints",
            "forbidden_data": "nonquadratic extrapolation, prime tables, target zeros, fitted arithmetic data",
        },
        "theorem": {
            "mode_polynomial": "r^2-(1+beta-alpha lambda)r+beta",
            "robust_stability": "-1<beta<1 and 0<alpha<2(1+beta)/L",
            "mode_radius": "sqrt(beta) inside the complex plateau; otherwise (|a|+sqrt(a^2-4beta))/2",
            "endpoint_reduction": "the robust radius is max(R_beta(a_m),R_beta(a_L))",
            "unique_minimax": "alpha*=4/(sqrt(L)+sqrt(m))^2, beta*=q^2, q=(sqrt(L)-sqrt(m))/(sqrt(L)+sqrt(m)) for m<L",
            "degenerate_interval": "for m=L, alpha*=1/m and beta*=0 annihilate error in one step and the state block in two",
            "jordan_boundary": "at the minimax endpoints the factors are (r-q)^2 and (r+q)^2, giving generic O(k q^k), not a uniform C q^k bound",
            "characteristic_determinant": "prod_lambda [r^2-(1+beta-alpha lambda)r+beta]",
            "state_trace_and_determinant": "tr M=d(1+beta)-alpha tr A; det M=beta^d",
            "conformal_symplectic_identity": "M^T J M=beta J",
            "finite_order_boundary": "at beta=1 fixed-A elliptic blocks are finite order exactly for rational rotation angles; beta=-1,alpha=0 is the trivial swap",
            "continuous_interval_control": "a nontrivial spectral interval contains irrational-angle beta=1 controls, so no uniform finite order exists",
        },
        "regression": {
            "parameter_cases": cases,
            "optimal_intervals": optimal_rows,
            "jordan_counterexample": {
                "m": "1", "L": "4", "alpha_star": "4/9", "beta_star": "1/9", "q": "1/3",
                "initial_e_minus_one": "1", "initial_e_zero": "1",
                "terms_k_minus1_to_8": {key: str(value) for key, value in terms.items()},
                "closed_form": "e_k=(1+2k/3)3^(-k)",
                "jordan_square_zero": True,
                "jordan_nonzero": True,
            },
            "rotated_spd_control": full_control,
            "finite_order_controls": finite_controls,
        },
        "summary": {
            "parameter_case_count": len(cases),
            "endpoint_block_count": 2 * len(cases),
            "optimal_interval_count": len(optimal_rows),
            "jordan_sequence_value_count": len(terms),
            "rotated_matrix_dimension": 4,
            "finite_order_control_count": len(finite_controls),
            "exact_certificate_scalar_count": 2 * len(cases) * 6 + len(optimal_rows) * 8 + len(terms) + 16 + len(finite_controls) * 4,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "The source map has a complete real-parameter spectral atlas and a conformally symplectic boundary.",
            "strongest_failure": "Neither the SPD spectrum nor the iteration clock carries intrinsic rational-prime or target determinant semantics.",
        },
        "scope_flags": {
            "uses_target_zero_table": False,
            "uses_prime_table": False,
            "claims_arithmetic_local_data": False,
            "claims_euler_factors": False,
            "claims_root_numbers": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {"key": "Polyak1964", "claim": "original heavy-ball iteration and asymptotic acceleration", "doi": "10.1016/0041-5553(64)90137-5"},
            {"key": "UgrinovskiiPetersenShames2023", "claim": "finite-dimensional quadratic worst-case asymptotic optimality", "doi": "10.1016/j.automatica.2023.111129"},
            {"key": "LessardRechtPackard2016", "claim": "control-theoretic analysis and nonlinear-objective scope boundary", "doi": "10.1137/15M1009597"},
        ],
        "nonclaims": [
            "priority for heavy-ball, Jury stability, Polyak parameters, or quadratic asymptotic optimality",
            "a uniform C q^k state bound at the defective minimax endpoints",
            "finite-time minimax optimality or optimality among unrestricted algorithms",
            "global convergence of the Polyak parameters for every nonlinear smooth strongly convex objective",
            "that finite exact regression proves the all-real continuum theorem",
            "a rational-prime orbit law, target divisor, Hilbert--Polya operator, external review, acceptance score, or Route-B authorization",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C201_PRODUCER_PASS",
        "parameter_cases": data["summary"]["parameter_case_count"],
        "endpoint_blocks": data["summary"]["endpoint_block_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
