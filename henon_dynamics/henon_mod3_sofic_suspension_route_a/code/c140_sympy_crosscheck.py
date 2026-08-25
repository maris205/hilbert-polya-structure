#!/usr/bin/env python3
"""Independent SymPy reconstruction of C140 cover correction and zeta."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c140_sofic_evidence.json"


def main():
    data = json.loads(EVIDENCE.read_text())
    checks = 0

    def ck(condition, label):
        nonlocal checks
        if not bool(condition):
            raise AssertionError(label)
        checks += 1

    u, v, t = sp.symbols("u v t")
    matrix = sp.Matrix([[u, v, 0], [0, 0, v], [v, 0, 0]])
    determinant = sp.expand((sp.eye(3) - matrix).det())
    ck(determinant == 1 - u - v ** 3, "cover determinant")
    zeta = (1 + v + v ** 2) / determinant
    inverse = sp.cancel(1 / zeta)
    ck(sp.cancel(zeta - (1 + v + v ** 2) / (1 - u - v ** 3)) == 0, "intrinsic zeta")
    ck(sp.cancel(inverse - (1 - u - v ** 3) / (1 + v + v ** 2)) == 0, "inverse zeta")
    ck(sp.cancel(inverse - determinant * (1 - v) / (1 - v ** 3)) == 0, "correction ratio")

    for n, row in enumerate(data["replay_prefix"]["rows"], start=1):
        cover_trace = sp.Poly(sp.expand(sp.trace(matrix ** n)), u, v)
        cover_receipt = {f"{monomial[0]},{monomial[1]}": int(coefficient) for monomial, coefficient in cover_trace.terms()}
        ck(cover_receipt == row["cover_weighted_trace_coefficients"], f"cover trace n={n}")
        intrinsic = sp.expand(sp.trace(matrix ** n) + (1 - 3 * int(n % 3 == 0)) * v ** n)
        intrinsic_receipt = {f"{monomial[0]},{monomial[1]}": int(coefficient) for monomial, coefficient in sp.Poly(intrinsic, u, v).terms()}
        ck(intrinsic_receipt == row["intrinsic_weighted_fixed_coefficients"], f"intrinsic trace n={n}")

    log_series = sp.series(-sp.log(1 - t * u - t ** 3 * v ** 3) + sp.log(1 + t * v + t ** 2 * v ** 2), t, 0, 16).removeO().expand()
    for n, row in enumerate(data["replay_prefix"]["rows"], start=1):
        coefficient = sp.expand(n * log_series.coeff(t, n))
        receipt = {f"{monomial[0]},{monomial[1]}": int(value) for monomial, value in sp.Poly(coefficient, u, v).terms()}
        ck(receipt == row["intrinsic_weighted_fixed_coefficients"], f"log zeta coefficient n={n}")

    h = sp.symbols("h", positive=True)
    entropy_expression = 1 - sp.exp(-h) - sp.exp(-3 * sp.sqrt(2) * h)
    ck(sp.limit(entropy_expression, h, 0, dir="+") == -1, "entropy at zero")
    ck(sp.limit(entropy_expression, h, sp.oo) == 1, "entropy at infinity")
    ck(sp.simplify(sp.diff(entropy_expression, h)) > 0, "entropy monotonicity")
    sqrt2_polynomial = sp.Poly(sp.minpoly(sp.sqrt(2)))
    ck(sqrt2_polynomial.degree() == 2 and sqrt2_polynomial.all_coeffs() == [1, 0, -2], "nonlattice irrationality")

    print(json.dumps({"status": "C140_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
