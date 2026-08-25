#!/usr/bin/env python3
"""Independent SymPy reconstruction of the C159 formal identities."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c159_s_gap_evidence.json"


def tm(n: int) -> int:
    return bin(n).count("1") % 2


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    replay = data["finite_replay"]
    z = sp.symbols("z")
    limit = 24
    checks = 0

    product = sp.Integer(1)
    exponent = 1
    while exponent <= limit:
        product = sp.Poly(product * (1 - z**exponent), z)
        product = sp.Poly(sum(product.nth(n) * z**n for n in range(limit + 1)), z).as_expr()
        exponent *= 2
    for n in range(limit + 1):
        coefficient = int(sp.expand(product).coeff(z, n))
        assert coefficient == replay["P_coefficients"][n] == (-1) ** tm(n)
        checks += 2

    zeta_series = sum(replay["zeta_coefficients"][n] * z**n for n in range(limit + 1))
    renewal_denominator = (1-z) * (1-sum(tm(s)*z**(s+1) for s in range(limit)))
    product_denominator = (2-3*z+z*(1-z)*product) / 2
    residual_renewal = sp.Poly(sp.expand(renewal_denominator*zeta_series-1), z)
    residual_product = sp.Poly(sp.expand(product_denominator*zeta_series-1), z)
    for n in range(limit + 1):
        assert residual_renewal.nth(n) == 0
        assert residual_product.nth(n) == 0
        checks += 2

    fixed = [0] + [row["fixed_points"] for row in replay["fixed_rows"]]
    fixed_log_derivative = sum(fixed[n] * z**(n-1) for n in range(1, 19))
    log_residual = sp.Poly(sp.expand(sp.diff(zeta_series, z)-fixed_log_derivative*zeta_series), z)
    for n in range(18):
        assert log_residual.nth(n) == 0
        checks += 1

    print(json.dumps({"status": "C159_SYMPY_PASS", "checks": checks, "formal_degree": limit}, sort_keys=True))


if __name__ == "__main__":
    main()
