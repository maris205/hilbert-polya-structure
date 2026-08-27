#!/usr/bin/env python3
"""SymPy polynomial-gcd and full-function Koopman controls for C204."""
import itertools
import json
from pathlib import Path

import sympy as sp

PATH = Path(__file__).resolve().parents[1] / "results" / "c204_finite_linear_evidence.json"


def gf4_add(a, b): return a ^ b
def gf4_mul(a, b):
    z = (a if b & 1 else 0) ^ ((a << 1) if b & 2 else 0)
    return z ^ 7 if z & 4 else z


def image(A, v, name, q):
    add = gf4_add if name == "GF4" else lambda a, b: (a + b) % q
    mul = gf4_mul if name == "GF4" else lambda a, b: a * b % q
    return tuple(__import__("functools").reduce(add, (mul(a, b) for a, b in zip(row, v)), 0) for row in A)


def main():
    data = json.loads(PATH.read_text()); x = sp.symbols("x"); gcd_cells = koopman_cases = 0
    saw_nontrivial_transient = False
    for case in data["cases"]:
        name = case["field"]["name"]; q = case["field"]["order"]
        if name != "GF4":
            for n in range(1, 19):
                xp = sp.Poly(x**n - 1, x, modulus=q)
                degs = []
                for coeffs in case["invariant_factors_low_to_high"]:
                    f = sp.Poly(sum(c*x**i for i, c in enumerate(coeffs)), x, modulus=q)
                    degs.append(sp.degree(sp.gcd(f, xp)))
                    gcd_cells += 1
                assert degs == case["gcd_degrees"][str(n)]
        states_count = case["direct_enumeration"]["state_count"]
        if states_count <= 16:
            A = case["matrix_rows"]; states = list(itertools.product(range(q), repeat=len(A)))
            index = {v: i for i, v in enumerate(states)}
            U = sp.zeros(len(states))
            for i, v in enumerate(states): U[i, index[image(A, v, name, q)]] = 1
            expected = x ** case["full_function_koopman_characteristic_polynomial"]["zero_multiplicity"]
            for n, c in case["full_function_koopman_characteristic_polynomial"]["cycle_factor_exponents"].items():
                expected *= (x ** int(n) - 1) ** c
            assert sp.Poly(U.charpoly(x).as_expr() - sp.expand(expected), x).is_zero
            koopman_cases += 1
            saw_nontrivial_transient |= case["max_preperiod"] > 1 and case["full_function_koopman_characteristic_polynomial"]["zero_multiplicity"] > 0
    assert gf4_mul(2, 2) == 3 and gf4_mul(3, 3) == 2 and gf4_mul(2, 3) == 1
    assert saw_nontrivial_transient and koopman_cases >= 5 and gcd_cells > 100
    print(f"C204 SymPy cross-check: PASS ({gcd_cells} gcd cells, {koopman_cases} Koopman charpolys)")
    print("GF(4) irreducible-polynomial table and nontrivial transient zero multiplicity: PASS")


if __name__ == "__main__": main()
