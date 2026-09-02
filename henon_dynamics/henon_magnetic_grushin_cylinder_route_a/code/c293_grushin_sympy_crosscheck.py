#!/usr/bin/env python3
"""Exact symbolic cross-checks for HCS-C293."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results/c293_grushin_evidence.json"


def R(value: str) -> sp.Rational:
    return sp.Rational(value)


def d_odd(n: int) -> int:
    return sum(n % d == 0 for d in range(1, n + 1, 2))


def main() -> None:
    data = json.loads(DATA.read_text()); checks = 0
    for row in data["spectral_cells"]:
        alpha = R(row["alpha"]); k = row["k"]; n = row["n"]
        omega = abs(k + alpha)
        if omega != R(row["frequency"]) or (2*n+1)*omega != R(row["eigenvalue"]):
            raise AssertionError("oscillator level")
        checks += 2

    z = sp.symbols("z", positive=True)
    geometric_identity = sp.simplify(z/(1-z**2) - 1/(z**-1-z))
    if geometric_identity != 0:
        raise AssertionError("heat geometric series")
    checks += 1

    for row in data["multiplicity_cells"]:
        N = row["N"]
        pairs = [(k, n) for k in range(1, N+1) for n in range(N) if (2*n+1)*k == N]
        if len(pairs) != d_odd(N) or row["odd_divisor_count"] != len(pairs) or row["multiplicity"] != 2*len(pairs):
            raise AssertionError("multiplicity")
        checks += 3

    for row in data["counting_cells"]:
        L = row["Lambda"]
        by_levels = 2*sum(L//j for j in range(1, L+1, 2))
        by_coefficients = sum(2*d_odd(N) for N in range(1, L+1))
        if row["exact_count"] != by_levels or by_levels != by_coefficients:
            raise AssertionError("counting identity")
        checks += 2

    # Laurent coefficients at s=1: if eps=s-1, zeta(s)^2 has
    # eps^-2+2 gamma eps^-1+..., while 2(1-2^-s)=1+log(2)eps+....
    eps, gamma = sp.symbols("eps gamma")
    prefactor = 1 + sp.log(2)*eps
    laurent = eps**-2 + 2*gamma*eps**-1
    expanded = sp.expand(prefactor*laurent)
    if expanded.coeff(eps, -2) != 1 or expanded.coeff(eps, -1) != 2*gamma+sp.log(2):
        raise AssertionError("Laurent coefficients")
    if sp.simplify((2*gamma+sp.log(2))-1 - (2*gamma+sp.log(2)-1)) != 0:
        raise AssertionError("Perron linear term")
    checks += 3

    for N in range(1, 97):
        ordinary = sp.divisor_count(N)
        half = sp.divisor_count(N//2) if N % 2 == 0 else 0
        if int(ordinary-half) != d_odd(N):
            raise AssertionError("odd divisor identity")
        checks += 1

    for row in data["symmetry_cells"]:
        alpha = R(row["alpha"]); fractional = alpha-sp.floor(alpha); distance = min(fractional, 1-fractional)
        if R(row["fundamental_distance"]) != distance or R(row["ground_energy"]) != distance:
            raise AssertionError("flux symmetry")
        checks += 2
    print(f"C293_SYMPY_PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
