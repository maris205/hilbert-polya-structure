#!/usr/bin/env python3
"""Separate symbolic reconstruction of the C201 heavy-ball theorem."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c201_heavy_ball_evidence.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(expression, message):
        nonlocal checks
        checks += 1
        if sp.simplify(expression) != 0:
            raise AssertionError(message)

    r, alpha, beta, lam = sp.symbols("r alpha beta lambda", real=True)
    p = r ** 2 - (1 + beta - alpha * lam) * r + beta
    check(p.subs(r, 1) - alpha * lam, "p(1)")
    check(p.subs(r, -1) - (2 * (1 + beta) - alpha * lam), "p(-1)")
    s, t = sp.symbols("s t", positive=True)
    q = (s - t) / (s + t)
    alpha_star = 4 / (s + t) ** 2
    beta_star = q ** 2
    a_m = sp.simplify(1 + beta_star - alpha_star * t ** 2)
    a_l = sp.simplify(1 + beta_star - alpha_star * s ** 2)
    check(a_m - 2 * q, "a_m")
    check(a_l + 2 * q, "a_L")
    check((s ** 2 - t ** 2) * (1 + q ** 2) - 2 * q * (s ** 2 + t ** 2), "lower bound")
    check(sp.expand(r ** 2 - a_m * r + beta_star - (r - q) ** 2), "lower factor")
    check(sp.expand(r ** 2 - a_l * r + beta_star - (r + q) ** 2), "upper factor")

    a11, a12, a22 = sp.symbols("a11 a12 a22", real=True)
    A = sp.Matrix([[a11, a12], [a12, a22]])
    I = sp.eye(2)
    M = sp.Matrix.vstack(sp.Matrix.hstack((1 + beta) * I - alpha * A, -beta * I),
                         sp.Matrix.hstack(I, sp.zeros(2)))
    J = sp.Matrix.vstack(sp.Matrix.hstack(sp.zeros(2), I), sp.Matrix.hstack(-I, sp.zeros(2)))
    residual = sp.simplify(M.T * J * M - beta * J)
    for value in residual:
        check(value, "conformal symplectic")

    evidence_checks = 0
    for case in data["regression"]["parameter_cases"]:
        av, bv = sp.Rational(case["alpha"]), sp.Rational(case["beta"])
        for endpoint in case["endpoint_rows"]:
            lv = sp.Rational(endpoint["lambda"])
            aa = 1 + bv - av * lv
            check(sp.Rational(endpoint["trace_a"]) - aa, "evidence trace")
            check(sp.Rational(endpoint["discriminant"]) - (aa ** 2 - 4 * bv), "evidence discriminant")
            check(sp.Rational(endpoint["p_at_plus_one"]) - av * lv, "evidence p1")
            check(sp.Rational(endpoint["p_at_minus_one"]) - (2 * (1 + bv) - av * lv), "evidence pm1")
            evidence_checks += 4
    counter = data["regression"]["jordan_counterexample"]
    for k in range(9):
        value = sp.Rational(counter["terms_k_minus1_to_8"][str(k)])
        check(value - (1 + sp.Rational(2 * k, 3)) * sp.Rational(1, 3) ** k, "counterexample closed form")
        evidence_checks += 1
    for control in data["regression"]["finite_order_controls"]:
        matrix = sp.Matrix([[sp.Rational(value) for value in row] for row in control["state_matrix"]])
        for value in matrix ** control["exact_order"] - sp.eye(2):
            check(value, "finite order")
            evidence_checks += 1
    print(json.dumps({
        "status": "C201_SYMPY_PASS",
        "checks": checks,
        "generic_symbolic_identities": 23,
        "evidence_symbolic_identities": evidence_checks,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
