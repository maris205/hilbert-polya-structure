#!/usr/bin/env python3
"""Exact SymPy cross-checks for C294."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    data = json.loads((ROOT / "results/c294_three_disk_evidence.json").read_text())
    checks = 0

    def check(value, label):
        nonlocal checks
        checks += 1
        if value is not True and value != sp.true:
            raise AssertionError(label)

    A = sp.ones(3) - sp.eye(3)
    z = sp.symbols("z")
    check(sp.factor(A.charpoly().as_expr()) == (sp.Symbol("lambda") - 2) * (sp.Symbol("lambda") + 1) ** 2, "adjacency spectrum")
    check(sp.simplify((sp.eye(3) - z * A).det() - (1 - 2 * z) * (1 + z) ** 2) == 0, "zeta denominator")
    for n in range(1, 41):
        check(sp.trace(A**n) == 2**n + 2 * (-1) ** n, f"trace {n}")

    series = sp.series(1 / ((1 - 2 * z) * (1 + z) ** 2), z, 0, 17).removeO().expand()
    for n, value in enumerate(data["enumeration"]["zeta_coefficients_0_to_16"]):
        check(series.coeff(z, n) == value, f"zeta coefficient {n}")
    log_derivative = sp.series(z * sp.diff(sp.log(1 / ((1 - 2 * z) * (1 + z) ** 2)), z), z, 0, 31).removeO().expand()
    for n in range(1, 31):
        check(log_derivative.coeff(z, n) == 2**n + 2 * (-1) ** n, f"log derivative {n}")

    a, ell = sp.symbols("a ell", positive=True)
    B = sp.Matrix([[1, ell], [a, 1 + a * ell]])
    check(sp.factor(B.det()) == 1, "block determinant")
    check(sp.factor(sp.trace(B) - 2) == a * ell, "block trace")
    for n in range(2, 13):
        M = sp.expand(B**n)
        check(sp.factor(M.det()) == 1, f"power det {n}")
        for av in [sp.Rational(1, 3), sp.Rational(1, 2), 1, 2, sp.Rational(5, 2)]:
            for lv in [sp.Rational(1, 4), sp.Rational(1, 2), 1, sp.Rational(3, 2), 3]:
                trace = sp.trace(M).subs({a: av, ell: lv})
                check(trace > 2, f"positive trace {n}:{av}:{lv}")

    r, d = sp.symbols("r d", positive=True)
    altitude = sp.sqrt(3) * d / 2
    check(sp.simplify((altitude - r) - r - (sp.sqrt(3) * d / 2 - 2 * r)) == 0, "no eclipse gap")
    chamber = sp.solve_univariate_inequality(altitude - 2 * r > 0, d)
    check(sp.simplify_logic(sp.Equivalent(chamber, d > 4 * sp.sqrt(3) * r / 3)), "no eclipse chamber")

    lam, kappa, xi = sp.symbols("lambda kappa xi", positive=True)
    constrained = lam * kappa * xi**2
    check(sp.diff(constrained, xi, 2) == 2 * lam * kappa, "strict boundary Hessian")

    ell2, a2 = sp.Integer(1), sp.Integer(2)
    M2 = sp.Matrix([[1, ell2], [a2, 1 + a2 * ell2]]) ** 2
    check(M2 == sp.Matrix([[3, 4], [8, 11]]), "period two matrix")
    check(M2.det() == 1 and sp.trace(M2) == 14, "period two invariants")

    ell3 = 3 - sp.sqrt(3)
    a3 = 4 / sp.sqrt(3)
    M3 = sp.simplify(sp.Matrix([[1, ell3], [a3, 1 + a3 * ell3]]) ** 3)
    check(sp.simplify(M3.det()) == 1, "period three determinant")
    check(sp.trace(M3) > 2, "period three hyperbolicity")
    check(sp.simplify(3 * ell3 - (9 - 3 * sp.sqrt(3))) == 0, "period three length")

    for row in data["enumeration"]["count_rows"]:
        n = row["n"]
        primitive = sum(sp.mobius(e) * (2 ** (n // e) + 2 * (-1) ** (n // e)) for e in sp.divisors(n))
        check(primitive == row["exact_period_rooted_words"], f"mobius row {n}")
        check(primitive % n == 0, f"necklace integrality {n}")

    print(f"C294 SymPy cross-check: PASS ({checks} symbolic checks)")


if __name__ == "__main__":
    main()
