#!/usr/bin/env python3
"""Independent exact symbolic checks for HCS-C337."""
from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c337_kicked_rotor_evidence.json"
CHECKS = 0


def need(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def q(value: str) -> sp.Rational:
    item = Fraction(value)
    return sp.Rational(item.numerator, item.denominator)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C337 SymPy lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())

    x, u = sp.symbols("x u", real=True)
    characteristic = sp.besselj(0, 2*x*sp.sin(u/2))
    expected = [1, 0, x**2/2, 0, x**2/2 + 3*x**4/8, 0,
                x**2/2 + 15*x**4/8 + 5*x**6/16]
    for order, target in enumerate(expected):
        moment = sp.simplify(sp.diff(characteristic, u, order).subs(u, 0) / sp.I**order)
        need(sp.expand(moment-target) == 0, f"characteristic moment {order}")

    for ell in range(1, 13):
        for n in range(-16, 17):
            free = sp.exp(-sp.I*sp.pi*ell*n*n)
            target = 1 if ell % 2 == 0 else (-1)**n
            need(sp.simplify(free-target) == 0, "free parity")

    for q_index in range(-14, 15):
        order = abs(q_index)
        for degree in range(15):
            if degree < order or (degree-order) % 2:
                coefficient = sp.S.Zero
            else:
                j = (degree-order)//2
                coefficient = (-sp.I)**q_index * (-1)**j / (
                    2**degree * sp.factorial(j) * sp.factorial(order+j))
                if q_index < 0:
                    coefficient *= (-1)**order
            row = data["formal_kernel_coefficients"][(q_index+14)*15+degree]
            encoded = q(row["bessel_formula"][0]) + sp.I*q(row["bessel_formula"][1])
            need(sp.simplify(coefficient-encoded) == 0, "formal Bessel coefficient")

    # Independently reconstruct all exact moment polynomials carried by the evidence.
    for row in data["moment_rows"]:
        kappa = q(row["kappa"])
        time = row["time"]
        effective = kappa*time if row["face"] == "even_resonance" else (kappa if time % 2 else 0)
        center = [sp.Integer(1), sp.Integer(0), effective**2/2, sp.Integer(0),
                  effective**2/2+3*effective**4/8, sp.Integer(0),
                  effective**2/2+15*effective**4/8+5*effective**6/16]
        for got, target in zip(row["central_moments_0_to_6"], center):
            need(sp.simplify(q(got)-target) == 0, "centered moment row")
        m = sp.Integer(row["m"])
        for order, got in enumerate(row["raw_moments_0_to_6"]):
            target = sum(sp.binomial(order, j)*m**(order-j)*center[j] for j in range(order+1))
            need(sp.simplify(q(got)-target) == 0, "raw moment row")

    # The half-turn conjugation sends cos(theta) to its negative.
    theta, kappa = sp.symbols("theta kappa", real=True)
    need(sp.simplify(sp.cos(theta+sp.pi)+sp.cos(theta)) == 0, "half-turn cosine")
    need(sp.simplify(sp.exp(sp.I*kappa*sp.cos(theta))*sp.exp(-sp.I*kappa*sp.cos(theta))-1) == 0,
         "kick inverse")
    print(f"C337 SymPy cross-check: PASS {CHECKS} exact identities")


if __name__ == "__main__":
    main()
