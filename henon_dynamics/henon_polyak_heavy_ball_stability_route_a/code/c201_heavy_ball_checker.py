#!/usr/bin/env python3
"""Independent exact checker with recursive key-set closure for C201."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c201_heavy_ball_evidence.json"
SOURCE_COMMIT = "d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
M, L = F(1), F(4)
EXPECTED_HEADLINE = (
    "Every real-parameter heavy-ball map on an SPD spectral interval "
    "has an exact Jury atlas, a unique minimax root factor, and a "
    "Jordan-correct transient boundary"
)
EXPECTED_CASES = [
    ("stable_negative_momentum", F(1, 8), F(-1, 2)), ("stable_zero_momentum", F(1, 4), F(0)),
    ("stable_positive_momentum", F(1, 2), F(1, 4)), ("alpha_zero_boundary", F(0), F(1, 4)),
    ("flip_boundary", F(5, 8), F(1, 4)), ("beta_one_elliptic", F(1, 4), F(1)),
    ("beta_one_parabolic", F(1), F(1)), ("beta_minus_one_swap", F(0), F(-1)),
    ("beta_above_one", F(1, 8), F(3, 2)), ("beta_below_minus_one", F(1, 8), F(-3, 2)),
    ("alpha_above_flip", F(3, 4), F(1, 4)), ("negative_alpha", F(-1, 8), F(0)),
    ("polyak_optimum_1_4", F(4, 9), F(1, 9)), ("interior_jordan_curve", F(9, 16), F(1, 4)),
]


def payload_hash(data):
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
    answer, base = identity(len(matrix)), matrix
    while exponent:
        if exponent & 1:
            answer = matmul(answer, base)
        base = matmul(base, base)
        exponent //= 2
    return answer


def determinant(matrix):
    work = [row[:] for row in matrix]
    answer = F(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return F(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer *= -1
        value = work[column][column]
        answer *= value
        for j in range(column, len(work)):
            work[column][j] /= value
        for row in range(column + 1, len(work)):
            factor = work[row][column]
            for j in range(column, len(work)):
                work[row][j] -= factor * work[column][j]
    return answer


def root_expression(a, beta):
    discriminant = a * a - 4 * beta
    if beta >= 0 and discriminant <= 0:
        return f"sqrt({beta})"
    return f"(abs({a})+sqrt({discriminant}))/2"


def expected_regime(alpha, beta):
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    assertions = 0

    def check(condition, message):
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    def keys(obj, expected, label):
        check(isinstance(obj, dict), f"{label} mapping")
        check(set(obj) == set(expected), f"{label} exact keys: {set(obj) ^ set(expected)}")

    keys(data, ["schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline",
                "frozen_object", "theorem", "regression", "summary", "route_a", "scope_flags", "citations", "nonclaims",
                "payload_sha256"], "top")
    keys(data["evaluator"], ["path", "version", "sha256"], "evaluator")
    keys(data["frozen_object"], ["objective", "spectral_class", "iteration", "parameters", "phase_state", "clock",
                                  "determinant_convention", "allowed_data", "forbidden_data"], "frozen_object")
    keys(data["theorem"], ["mode_polynomial", "robust_stability", "mode_radius", "endpoint_reduction", "unique_minimax",
                            "degenerate_interval", "jordan_boundary", "characteristic_determinant",
                            "state_trace_and_determinant", "conformal_symplectic_identity", "finite_order_boundary",
                            "continuous_interval_control"], "theorem")
    keys(data["regression"], ["parameter_cases", "optimal_intervals", "jordan_counterexample", "rotated_spd_control",
                               "finite_order_controls"], "regression")
    keys(data["summary"], ["parameter_case_count", "endpoint_block_count", "optimal_interval_count",
                            "jordan_sequence_value_count", "rotated_matrix_dimension", "finite_order_control_count",
                            "exact_certificate_scalar_count"], "summary")
    keys(data["route_a"], ["tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"], "route_a")
    keys(data["scope_flags"], ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data",
                                "claims_euler_factors", "claims_root_numbers", "claims_automorphy",
                                "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator",
                                "invokes_route_b"], "scope_flags")
    for i, citation in enumerate(data["citations"]):
        keys(citation, ["key", "claim", "doi"], f"citation[{i}]")

    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c201-heavy-ball-v1", "schema")
    check(data["candidate_id"] == "HCS-C201", "candidate")
    check(data["evaluation_date"] == "2026-08-27", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["evaluator"]["sha256"] == EVALUATOR_SHA256, "evaluator")
    check(data["headline"] == EXPECTED_HEADLINE, "headline")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(all(value is False for value in data["scope_flags"].values()), "scope flags")
    check([row["doi"] for row in data["citations"]] ==
          ["10.1016/0041-5553(64)90137-5", "10.1016/j.automatica.2023.111129", "10.1137/15M1009597"], "DOIs")

    cases = data["regression"]["parameter_cases"]
    check(len(cases) == len(EXPECTED_CASES), "parameter case count")
    for index, (case_id, alpha, beta) in enumerate(EXPECTED_CASES):
        row = cases[index]
        keys(row, ["case_id", "m", "L", "alpha", "beta", "regime", "robustly_schur_stable", "endpoint_rows"], f"case[{index}]")
        check(row["case_id"] == case_id, "case id")
        check(F(row["m"]) == M and F(row["L"]) == L, "interval")
        check(F(row["alpha"]) == alpha and F(row["beta"]) == beta, "parameters")
        stable = -1 < beta < 1 and alpha > 0 and alpha * L < 2 * (1 + beta)
        check(row["robustly_schur_stable"] is stable, "Jury flag")
        check(row["regime"] == expected_regime(alpha, beta), "regime")
        check(len(row["endpoint_rows"]) == 2, "endpoint count")
        for endpoint, lam in zip(row["endpoint_rows"], [M, L]):
            keys(endpoint, ["lambda", "trace_a", "determinant_beta", "discriminant", "p_at_plus_one",
                            "p_at_minus_one", "root_radius_expression"], "endpoint")
            a = 1 + beta - alpha * lam
            check(F(endpoint["lambda"]) == lam, "lambda")
            check(F(endpoint["trace_a"]) == a, "trace")
            check(F(endpoint["determinant_beta"]) == beta, "determinant")
            check(F(endpoint["discriminant"]) == a * a - 4 * beta, "discriminant")
            check(F(endpoint["p_at_plus_one"]) == alpha * lam, "p(1)")
            check(F(endpoint["p_at_minus_one"]) == 2 * (1 + beta) - alpha * lam, "p(-1)")
            check(endpoint["root_radius_expression"] == root_expression(a, beta), "root expression")

    optimal = data["regression"]["optimal_intervals"]
    check(len(optimal) == 4, "optimal interval count")
    for row, (sqrt_m, sqrt_l) in zip(optimal, [(1, 2), (1, 3), (2, 3), (2, 2)]):
        keys(row, ["m", "L", "sqrt_m", "sqrt_L", "q", "alpha_star", "beta_star", "a_m", "a_L",
                   "lower_bound_residual", "endpoint_factors", "transient_class"], "optimal")
        m, ell = F(sqrt_m * sqrt_m), F(sqrt_l * sqrt_l)
        check(F(row["m"]) == m and F(row["L"]) == ell, "optimal interval")
        if sqrt_m == sqrt_l:
            q, alpha, beta = F(0), F(1, m), F(0)
            check(row["endpoint_factors"] == ["r^2", "r^2"], "nilpotent factors")
        else:
            q = F(sqrt_l - sqrt_m, sqrt_l + sqrt_m)
            alpha, beta = F(4, (sqrt_l + sqrt_m) ** 2), q * q
            check(F(row["a_m"]) == 2 * q and F(row["a_L"]) == -2 * q, "optimal endpoints")
        check(F(row["q"]) == q and F(row["alpha_star"]) == alpha and F(row["beta_star"]) == beta, "optimal parameters")
        check(F(row["lower_bound_residual"]) == (ell - m) * (1 + q * q) - 2 * q * (ell + m) == 0, "lower bound equality")

    counter = data["regression"]["jordan_counterexample"]
    keys(counter, ["m", "L", "alpha_star", "beta_star", "q", "initial_e_minus_one", "initial_e_zero",
                   "terms_k_minus1_to_8", "closed_form", "jordan_square_zero", "jordan_nonzero"], "counterexample")
    keys(counter["terms_k_minus1_to_8"], ["-1"] + [str(k) for k in range(9)], "counterexample terms")
    previous, current = F(1), F(1)
    check(F(counter["terms_k_minus1_to_8"]["-1"]) == previous, "e-1")
    check(F(counter["terms_k_minus1_to_8"]["0"]) == current, "e0")
    for k in range(9):
        check(F(counter["terms_k_minus1_to_8"][str(k)]) == (1 + F(2 * k, 3)) * F(1, 3) ** k, "closed form")
        if k < 8:
            following = F(2, 3) * current - F(1, 9) * previous
            check(F(counter["terms_k_minus1_to_8"][str(k + 1)]) == following, "recurrence")
            previous, current = current, following
    block = [[F(2, 3), F(-1, 9)], [F(1), F(0)]]
    nilpotent = [[block[i][j] - F(1, 3) * F(i == j) for j in range(2)] for i in range(2)]
    check(nilpotent != [[F(0), F(0)], [F(0), F(0)]], "Jordan nonzero")
    check(matmul(nilpotent, nilpotent) == [[F(0), F(0)], [F(0), F(0)]], "Jordan square")
    check(counter["jordan_square_zero"] is True and counter["jordan_nonzero"] is True, "Jordan flags")

    rotated = data["regression"]["rotated_spd_control"]
    keys(rotated, ["A", "alpha", "beta", "state_matrix", "trace", "determinant", "conformal_symplectic_residual_zero"], "rotated")
    a_matrix = [[F(value) for value in row] for row in rotated["A"]]
    alpha, beta = F(rotated["alpha"]), F(rotated["beta"])
    expected = []
    for i in range(2):
        expected.append([(1 + beta) * F(i == j) - alpha * a_matrix[i][j] for j in range(2)] +
                        [-beta * F(i == j) for j in range(2)])
    for i in range(2):
        expected.append([F(i == j) for j in range(2)] + [F(0), F(0)])
    matrix = [[F(value) for value in row] for row in rotated["state_matrix"]]
    check(matrix == expected, "rotated state matrix")
    check(F(rotated["trace"]) == sum(matrix[i][i] for i in range(4)), "rotated trace")
    check(F(rotated["determinant"]) == determinant(matrix) == beta ** 2, "rotated determinant")
    j_matrix = [[F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)],
                [F(-1), F(0), F(0), F(0)], [F(0), F(-1), F(0), F(0)]]
    check(matmul(matmul(transpose(matrix), j_matrix), matrix) == [[beta * value for value in row] for row in j_matrix], "conformal symplectic")
    check(rotated["conformal_symplectic_residual_zero"] is True, "conformal flag")

    controls = data["regression"]["finite_order_controls"]
    check(len(controls) == 3, "finite controls")
    for control in controls:
        keys(control, ["label", "lambda", "alpha", "beta", "state_matrix", "exact_order"], "finite control")
        lam, alpha, beta = F(control["lambda"]), F(control["alpha"]), F(control["beta"])
        matrix = [[F(value) for value in row] for row in control["state_matrix"]]
        check(matrix == [[1 + beta - alpha * lam, -beta], [F(1), F(0)]], "finite matrix")
        check(power(matrix, control["exact_order"]) == identity(2), "finite order")

    summary = data["summary"]
    check(summary["parameter_case_count"] == 14, "summary cases")
    check(summary["endpoint_block_count"] == 28, "summary endpoints")
    check(summary["optimal_interval_count"] == 4, "summary optimum")
    check(summary["jordan_sequence_value_count"] == 10, "summary sequence")
    check(summary["rotated_matrix_dimension"] == 4, "summary dimension")
    check(summary["finite_order_control_count"] == 3, "summary finite order")
    check(summary["exact_certificate_scalar_count"] == 238, "summary exact scalar count")
    print(json.dumps({
        "status": "C201_CHECKER_PASS",
        "assertions": assertions,
        "endpoint_blocks": 28,
        "schema_key_sets": 1 + 1 + 1 + 1 + 1 + 1 + 3 + 14 + 28 + 4 + 1 + 1 + 3,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
