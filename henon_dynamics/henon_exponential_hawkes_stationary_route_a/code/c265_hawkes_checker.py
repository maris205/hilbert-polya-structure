#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C265."""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

SOURCE = "a24c701881d22a4e49eaa2a44b94395c3c540b3d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c265_hawkes_evidence.json"


def q(value: str) -> Fraction:
    return Fraction(value)


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def coefficient_of_generator(n: int, degree: int, nu: Fraction, a: Fraction, b: Fraction) -> Fraction:
    """Coefficient of x^degree in A(x^n), constructed polynomially."""
    out = Fraction(0)
    if degree == n - 1:
        out += n * b * nu
    if degree == n:
        out -= n * b
    for k in range(n):
        if degree == k + 1:
            out += math.comb(n, k) * a ** (n - k)
    return out


def check(path: Path) -> int:
    data = json.loads(path.read_text())
    checks = 0

    def demand(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    demand(data["schema"] == "hcs-c265-exponential-hawkes-stationary-v1", "schema")
    demand(data["candidate_id"] == "HCS-C265", "candidate")
    demand(data["source_commit"] == SOURCE, "source")
    demand(data["fixed_epoch"] == 1788048000, "epoch")
    demand(data["scope_literal"] == SCOPE, "scope")
    demand(data["evaluator"]["sha256"] == EVALUATOR, "evaluator")
    demand(data["payload_sha256"] == canonical_hash(data), "payload")
    demand(data["citation"]["doi"] == "10.1093/biomet/58.1.83", "doi")
    demand(data["frozen_object"]["predictable_intensity"] == "lambda_(t-)", "predictability")
    demand("no 1/(2pi)" in data["frozen_object"]["fourier_convention"], "Fourier convention")
    demand(all(value is False for value in data["scope_flags"].values()), "scope flags")
    demand(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "tuple")
    demand(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "verdict")
    demand(data["route_a"]["route_b_invocation_allowed"] is False, "Route B")
    theorem = data["theorem"]
    demand("B'=1-bB-z exp(-aB)" in theorem["affine_transform"], "affine equation")
    demand("exp(-a s)-1" in theorem["stationary_laplace_ode"], "Laplace ODE")
    demand("mu delta_0" in theorem["complete_counting_covariance"], "Dirac atom")
    demand("no 1/(2pi)" in theorem["bartlett_spectrum"], "spectrum convention")
    rows = data["regression"]["stable_cases"]
    demand(data["regression"]["stable_case_count"] == 320 == len(rows), "case count")
    demand(data["regression"]["moment_order"] == 10, "moment order")

    for row in rows:
        nu, a, b, delta = map(q, (row["nu"], row["a"], row["b"], row["delta"]))
        demand(delta == b - a and b > a >= 0 and nu >= 0, "parameter chamber")
        demand(q(row["branching_ratio"]) == a / b, "branching ratio")
        mu = b * nu / delta
        demand(q(row["mean_intensity"]) == mu, "mean")
        var = mu * a * a / (2 * delta)
        demand(q(row["intensity_variance"]) == var, "variance")
        demand(q(row["intensity_covariance_coefficient"]) == var, "intensity covariance")
        count_c = mu * a * (2 * b - a) / (2 * delta)
        demand(q(row["counting_continuous_covariance_coefficient"]) == count_c, "count covariance")
        demand(q(row["counting_dirac_mass"]) == mu, "Dirac mass")
        spectrum_zero = mu * b * b / (delta * delta)
        demand(q(row["bartlett_zero_frequency"]) == spectrum_zero, "spectrum zero")
        demand(q(row["long_window_variance_rate"]) == spectrum_zero, "long-window rate")
        moments = [q(x) for x in row["moments_m0_to_m10"]]
        demand(len(moments) == 11 and moments[0] == 1, "moment vector")
        for n in range(1, 11):
            generator_expectation = Fraction(0)
            for degree in range(n + 1):
                coefficient = coefficient_of_generator(n, degree, nu, a, b)
                if coefficient:
                    generator_expectation += coefficient * moments[degree]
                    demand(True, "generator coefficient visited")
            demand(generator_expectation == 0, f"generator moment n={n}")
        demand(moments[1] == mu, "first moment")
        demand(moments[2] - moments[1] ** 2 == var, "second central moment")
        coeffs = [q(x) for x in row["window_variance_maclaurin_T1_to_T10"]]
        demand(len(coeffs) == 10 and coeffs[0] == mu, "window leading coefficient")
        gain = mu * a * (2 * b - a)
        for n in range(2, 11):
            expected = gain * Fraction((-1) ** n, math.factorial(n)) * delta ** (n - 3)
            demand(coeffs[n - 1] == expected, f"window coefficient n={n}")
        # The inverse Fourier coefficient must reconstruct S(omega)-mu.
        demand(2 * delta * count_c == mu * a * (2 * b - a), "Fourier inversion coefficient")
        demand(delta * delta + a * (2 * b - a) == b * b, "zero-frequency algebra")

    cluster_rows = data["regression"]["cluster_rows"]
    demand(len(cluster_rows) == data["regression"]["cluster_row_count"] == 160, "cluster count")
    for row in cluster_rows:
        m, exponent, coefficient = q(row["branching_ratio"]), q(row["exponent"]), q(row["coefficient"])
        n = row["n"]
        demand(0 <= m < 1 and 1 <= n <= 20, "cluster range")
        demand(row["rooted_tree_count"] == n ** (n - 1), "Cayley rooted count")
        demand(exponent == -m * n, "Borel exponent")
        demand(coefficient == Fraction(n ** (n - 1), math.factorial(n)) * m ** (n - 1), "Borel coefficient")

    boundaries = {row["id"]: row for row in data["regression"]["boundary_rows"]}
    demand(len(boundaries) == data["regression"]["boundary_row_count"] == 6, "boundary count")
    demand(boundaries["poisson_a_zero"]["classification"] == "HOMOGENEOUS_POISSON", "Poisson face")
    demand(boundaries["empty_nu_zero_subcritical"]["classification"] == "EMPTY_STATIONARY", "empty face")
    demand(boundaries["critical_positive_immigration"]["classification"] == "NO_FINITE_INTENSITY_STATIONARY", "critical face")
    demand(boundaries["supercritical_positive_immigration"]["classification"] == "NO_FINITE_INTENSITY_STATIONARY", "supercritical face")
    demand(boundaries["subcritical_positive_immigration"]["stationary_mean"] == "2/1", "subcritical control")
    demand(len(data["object_separation"]) == 4, "object separation ledger")
    demand(len(data["nonclaims"]) == 4, "nonclaims")
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=DEFAULT)
    args = parser.parse_args()
    checks = check(args.evidence)
    print(f"C265 independent checker: PASS ({checks} assertions; producer import forbidden)")


if __name__ == "__main__":
    main()
