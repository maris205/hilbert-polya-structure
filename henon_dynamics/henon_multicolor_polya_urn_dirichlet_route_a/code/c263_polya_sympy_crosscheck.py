#!/usr/bin/env python3
"""Symbolic reconstruction independent of the HCS-C263 producer."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c263_polya_evidence.json"


def main():
    checks = 0
    n, A, ai, aj = sp.symbols("n A ai aj", positive=True)
    # Conditional martingale identity.
    xi = sp.symbols("xi", nonnegative=True)
    expr = ((ai + xi) / (A + n)) * ((ai + xi + 1) / (A + n + 1))
    expr += (1 - (ai + xi) / (A + n)) * ((ai + xi) / (A + n + 1))
    assert sp.simplify(expr - (ai + xi) / (A + n)) == 0
    checks += 1
    # Dirichlet-mixture covariance formulas imply the count covariance formulas.
    var_theta = ai * (A - ai) / (A**2 * (A + 1))
    mean_binomial_noise = n * (ai / A - (ai**2 + ai) / (A * (A + 1)))
    total_var = sp.simplify(mean_binomial_noise + n**2 * var_theta)
    target_var = n * ai * (A - ai) * (A + n) / (A**2 * (A + 1))
    assert sp.simplify(total_var - target_var) == 0
    checks += 1
    cov_theta = -ai * aj / (A**2 * (A + 1))
    conditional_cov = -n * ai * aj / (A * (A + 1))
    total_cov = sp.simplify(conditional_cov + n**2 * cov_theta)
    target_cov = -n * ai * aj * (A + n) / (A**2 * (A + 1))
    assert sp.simplify(total_cov - target_cov) == 0
    checks += 1
    # Finite Vandermonde checks for symbolic alpha,beta.
    x, y = sp.symbols("x y")
    for degree in range(0, 8):
        lhs = sum(sp.binomial(degree, k) * sp.rf(x, k) * sp.rf(y, degree - k) for k in range(degree + 1))
        assert sp.simplify(lhs - sp.rf(x + y, degree)) == 0
        checks += 1
    data = json.loads(EVIDENCE.read_text())
    # Reconstruct a deterministic spread of exact stored identities through SymPy Rational.
    pools = [
        data["regression"]["composition_rows"],
        data["regression"]["marginal_rows"],
        data["regression"]["factorial_rows"],
        data["regression"]["martingale_rows"],
        data["regression"]["de_finetti_rows"],
    ]
    keys = [
        ("recursive_probability", "closed_probability"),
        ("observed", "closed"),
        ("observed", "closed"),
        ("current", "expected_next"),
        ("ordered_word_probability", "dirichlet_monomial_moment"),
    ]
    for pool, pair in zip(pools, keys):
        stride = max(1, len(pool) // 29)
        for row in pool[::stride][:29]:
            left = sp.Rational(Fraction(row[pair[0]]).numerator, Fraction(row[pair[0]]).denominator)
            right = sp.Rational(Fraction(row[pair[1]]).numerator, Fraction(row[pair[1]]).denominator)
            assert sp.simplify(left - right) == 0
            checks += 1
    print(f"C263_SYMPY_PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
