#!/usr/bin/env python3
"""Producer-independent exact checker with recursive key-set closure for C200."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c200_jacobi_evidence.json"
SOURCE_COMMIT = "d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
PARAMETERS = [F(1, 2), F(1), F(3, 2)]
MAX_DEGREE = 8
EXPECTED_HEADLINE = (
    "Every positive-mutation canonical Jacobi diffusion has an exact "
    "boundary atlas, Beta-reversible Jacobi spectrum, heat determinant, "
    "and closed moment hierarchy"
)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def lam(n: int, a: F, b: F) -> F:
    return F(n) * (F(n - 1) + a + b)


def down(n: int, a: F) -> F:
    return F(n) * (F(n - 1) + a)


def monic(n: int, a: F, b: F) -> list[F]:
    c = [F(0)] * (n + 1)
    c[n] = F(1)
    for j in range(n - 1, -1, -1):
        c[j] = -c[j + 1] * down(j + 1, a) / (lam(n, a, b) - lam(j, a, b))
    return c


def apply_l(c: list[F], a: F, b: F) -> list[F]:
    out = [F(0)] * len(c)
    for k, value in enumerate(c):
        out[k] -= value * lam(k, a, b)
        if k:
            out[k - 1] += value * down(k, a)
    return out


def moment(k: int, a: F, b: F) -> F:
    answer = F(1)
    for j in range(k):
        answer *= (a + j) / (a + b + j)
    return answer


def matmul(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


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
        check(isinstance(obj, dict), f"{label} is mapping")
        check(set(obj) == set(expected), f"{label} exact keys: {set(obj) ^ set(expected)}")

    keys(data, ["schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator",
                "headline", "frozen_object", "theorem", "regression", "summary", "route_a", "scope_flags",
                "citations", "nonclaims", "payload_sha256"], "top")
    keys(data["evaluator"], ["path", "version", "sha256"], "evaluator")
    keys(data["frozen_object"], ["sde", "generator", "parameters", "realization", "clock", "normalization",
                                  "determinant_convention", "allowed_data", "forbidden_data"], "frozen_object")
    keys(data["theorem"], ["scale_density", "speed_and_invariant_density", "boundary_at_zero", "boundary_at_one",
                            "divergence_form", "eigenbasis", "eigenvalues", "spectral_gap", "heat_kernel",
                            "trace_class_determinant", "moment_closure", "stationary_moments",
                            "semigroup_periodicity", "path_recurrence"], "theorem")
    keys(data["regression"], ["maximum_degree", "parameter_cases"], "regression")
    keys(data["summary"], ["parameter_case_count", "boundary_decision_count", "eigenpolynomial_count",
                            "coefficient_identity_count", "moment_identity_count", "gram_symmetry_identity_count",
                            "exact_scalar_identity_count"], "summary")
    keys(data["route_a"], ["tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"], "route_a")
    keys(data["scope_flags"], ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data",
                                "claims_euler_factors", "claims_root_numbers", "claims_automorphy",
                                "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator",
                                "invokes_route_b"], "scope_flags")
    for i, citation in enumerate(data["citations"]):
        keys(citation, ["key", "claim", "doi"], f"citation[{i}]")

    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c200-jacobi-v1", "schema")
    check(data["candidate_id"] == "HCS-C200", "candidate")
    check(data["evaluation_date"] == "2026-08-27", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["evaluator"]["sha256"] == EVALUATOR_SHA256, "evaluator sha")
    check(data["headline"] == EXPECTED_HEADLINE, "headline")
    check(data["frozen_object"]["realization"] == "canonical conservative no-flux Jacobi diffusion on [0,1]", "realization")
    check("twice" in data["frozen_object"]["clock"], "clock normalization")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(all(value is False for value in data["scope_flags"].values()), "scope flags")
    check([row["doi"] for row in data["citations"]] ==
          ["10.1137/090766152", "10.1534/genetics.111.136929", "10.2307/1426842"], "DOIs")

    cases = data["regression"]["parameter_cases"]
    check(data["regression"]["maximum_degree"] == MAX_DEGREE, "maximum degree")
    check(len(cases) == 9, "case count")
    coefficient_count = moment_count = gram_count = 0
    for index, (a, b) in enumerate((a, b) for a in PARAMETERS for b in PARAMETERS):
        row = cases[index]
        keys(row, ["case_id", "alpha", "beta", "left_boundary", "right_boundary",
                   "stationary_moments_0_to_8", "polynomial_rows", "gram_generator_symmetry_zero"], f"case[{index}]")
        check(F(row["alpha"]) == a and F(row["beta"]) == b, "parameter order")
        check(row["case_id"] == f"alpha_{a}_beta_{b}", "case id")
        check(row["left_boundary"] == ("regular_reflecting" if a < 1 else "entrance"), "left boundary")
        check(row["right_boundary"] == ("regular_reflecting" if b < 1 else "entrance"), "right boundary")
        expected_moments = [moment(k, a, b) for k in range(MAX_DEGREE + 1)]
        check([F(value) for value in row["stationary_moments_0_to_8"]] == expected_moments, "moments")
        for k in range(1, MAX_DEGREE + 1):
            check(down(k, a) * expected_moments[k - 1] == lam(k, a, b) * expected_moments[k], "moment stationarity")
            moment_count += 1
        check(len(row["polynomial_rows"]) == MAX_DEGREE + 1, "polynomial row count")
        for n, poly in enumerate(row["polynomial_rows"]):
            keys(poly, ["degree", "eigenvalue", "coefficients_ascending", "ode_residual_zero"], f"case[{index}].poly[{n}]")
            expected = monic(n, a, b)
            check(poly["degree"] == n, "degree")
            check(F(poly["eigenvalue"]) == lam(n, a, b), "eigenvalue")
            check([F(value) for value in poly["coefficients_ascending"]] == expected, "coefficients")
            generated = apply_l(expected, a, b)
            residual = [generated[j] + lam(n, a, b) * expected[j] for j in range(n + 1)]
            for value in residual:
                check(value == 0, "ODE coefficient")
                coefficient_count += 1
            check(poly["ode_residual_zero"] is True, "ODE flag")
        size = MAX_DEGREE + 1
        c = [[F(0) for _ in range(size)] for _ in range(size)]
        h = [[moment(i + j, a, b) for j in range(size)] for i in range(size)]
        for k in range(size):
            c[k][k] = -lam(k, a, b)
            if k:
                c[k - 1][k] = down(k, a)
        residual = [[matmul(h, c)[i][j] - matmul(transpose(c), h)[i][j]
                     for j in range(size)] for i in range(size)]
        for residual_row in residual:
            for value in residual_row:
                check(value == 0, "Gram-generator symmetry")
                gram_count += 1
        check(row["gram_generator_symmetry_zero"] is True, "Gram flag")

    summary = data["summary"]
    check(summary["parameter_case_count"] == len(cases), "summary cases")
    check(summary["boundary_decision_count"] == 18, "summary boundaries")
    check(summary["eigenpolynomial_count"] == 81, "summary polynomials")
    check(summary["coefficient_identity_count"] == coefficient_count, "summary coefficients")
    check(summary["moment_identity_count"] == moment_count, "summary moments")
    check(summary["gram_symmetry_identity_count"] == gram_count, "summary Gram")
    check(summary["exact_scalar_identity_count"] == coefficient_count + moment_count + gram_count, "summary total")
    print(json.dumps({
        "status": "C200_CHECKER_PASS",
        "assertions": assertions,
        "exact_scalar_identities": summary["exact_scalar_identity_count"],
        "schema_key_sets": 1 + 1 + 1 + 1 + 1 + 1 + 1 + len(data["citations"]) + len(cases) + 81,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
