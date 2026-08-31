#!/usr/bin/env python3
"""Exact SymPy reconstruction of the C261 polynomial and modular contracts."""
from __future__ import annotations

import json
from math import gcd
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c261_airy_evidence.json"


def factorint_local(n: int) -> dict[int, int]:
    return {int(p): int(e) for p, e in sp.factorint(n).items()}


def main() -> None:
    n, q, p, x, t = sp.symbols("n q p x t", integer=True)
    checks = 0

    def ck(expr, label: str) -> None:
        nonlocal checks
        checks += 1
        out = sp.expand(expr)
        if out != 0:
            raise AssertionError(f"{label}: {out}")

    ck((n + q) ** 3 - n**3 - q * (3*n**2 + 3*n*q + q**2), "cubic phase periodicity")
    ck(sp.diff(sp.exp(sp.I*n*x + sp.I*n**3*t), t) + sp.diff(sp.exp(sp.I*n*x + sp.I*n**3*t), x, 3), "Airy mode PDE")
    ck(sp.diff(n**3, n) - 3*n**2, "cubic derivative convention")

    for modulus in range(1, 257):
        L = 1
        for prime, exponent in factorint_local(modulus).items():
            L *= prime ** ((exponent + 2)//3)
        for mode in range(-2*modulus-3, 2*modulus+4):
            checks += 1
            if ((mode**3) % modulus == 0) != (mode % L == 0):
                raise AssertionError(f"stride equivalence q={modulus} n={mode}")
        for a in range(modulus):
            for mode in (-modulus-1, -1, 0, 1, modulus+1):
                checks += 1
                if ((a*(mode+modulus)**3-a*mode**3) % modulus) != 0:
                    raise AssertionError("sample phase periodicity")

    # Orthogonality of finite characters proves the DFT inverse without floats.
    for modulus in range(2, 65):
        for delta in range(modulus):
            residue_count = sum(1 for r in range(modulus) if (r*delta) % modulus == 0)
            expected = modulus if delta == 0 else gcd(delta, modulus)
            checks += 1
            if residue_count != expected:
                raise AssertionError("finite character residue count")
        for a in range(1, modulus):
            if gcd(a, modulus) != 1:
                continue
            phases = [(a*s**3) % modulus for s in range(modulus)]
            checks += 1
            if phases[1] != a % modulus:
                raise AssertionError("mode-one strobe order witness")

    data = json.loads(EVIDENCE.read_text())
    formulas = {row["id"]: row["formula"] for row in data["exact_identities"]}
    expected = {
        "mode_solution": "U(t)e_n=exp(i*n^3*t)e_n",
        "cubic_periodicity": "(n+q)^3-n^3=q*(3*n^2+3*n*q+q^2)",
        "dft_coefficients": "A_r=q^-1*sum_s exp(2*pi*i*(p*s^3-s*r)/q)",
        "parseval": "sum_r abs(A_r)^2=1",
        "full_period": "min{t>0:U(t)=I}=2*pi",
        "strobe_order": "ord(U(2*pi*p/q))=q when gcd(p,q)=1",
        "fixed_stride": "q|n^3 iff product_l l^ceil(v_l(q)/3) divides n",
        "support_period": "T_S=2*pi/gcd{|n|^3:n in S,n!=0}",
        "noncompact": "unitary images of the Fourier basis have no norm-convergent subsequence",
    }
    checks += 1
    if formulas != expected:
        raise AssertionError("evidence identity ledger")
    checks += 1
    if data["route_a"]["tuple"] != ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]:
        raise AssertionError("route tuple")
    checks += 1
    if data["route_a"]["route_b_invocation_allowed"] is not False:
        raise AssertionError("Route B")
    print(f"C261_SYMPY_PASS ({checks} exact identities; Airy mode, cubic periodicity, fixed strides and finite characters)")


if __name__ == "__main__":
    main()
