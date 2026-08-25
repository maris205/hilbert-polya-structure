#!/usr/bin/env python3
"""Independent SymPy quotient-ring reconstruction for HCS-C150."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c150_rule90_mersenne_evidence.json"


def powmod(base: sp.Poly, exponent: int, modulus: sp.Poly) -> sp.Poly:
    result = sp.Poly(1, base.gens[0], modulus=2)
    while exponent:
        if exponent & 1:
            result = result.mul(base).rem(modulus)
        base = base.mul(base).rem(modulus)
        exponent >>= 1
    return result


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else EVIDENCE
    data = json.loads(path.read_text())
    x = sp.symbols("x")
    checks = 0

    def ck(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    for receipt in data["mersenne_replay"]["family_rows"]:
        length = receipt["ring_length_L"]
        modulus = sp.Poly(x ** length + 1, x, modulus=2)
        multiplier = sp.Poly(x + x ** (length - 1), x, modulus=2).rem(modulus)
        ck(powmod(multiplier, length + 1, modulus) == multiplier, f"Frobenius identity L={length}")
        kernel_gcd = sp.gcd(modulus, sp.Poly(x ** 2 + 1, x, modulus=2))
        ck(kernel_gcd.degree() == 1, f"kernel degree L={length}")
        ck(sp.gcd(modulus, modulus.diff()).degree() == 0, f"squarefree L={length}")
        fixed_lookup = {}
        for row in receipt["divisor_period_rows"]:
            n = row["period_n"]
            cleared = sp.Poly((x ** 2 + 1) ** n + x ** n, x, modulus=2)
            dimension = sp.gcd(modulus, cleared).degree()
            fixed_lookup[n] = 1 << dimension
            ck(row["gcd_degree"] == dimension, f"gcd degree L={length} n={n}")
            ck(row["fixed_points"] == fixed_lookup[n], f"fixed L={length} n={n}")
        for row in receipt["divisor_period_rows"]:
            n = row["period_n"]
            exact = sum(int(sp.mobius(n // d)) * fixed_lookup[d] for d in sp.divisors(n))
            ck(row["exact_period_points"] == exact, f"Mobius L={length} n={n}")
            ck(row["primitive_cycles"] == exact // n, f"cycles L={length} n={n}")
        ck(sum(row["exact_period_points"] for row in receipt["divisor_period_rows"]) == 1 << (length - 1), f"periodic image L={length}")

    for receipt in data["power_of_two_negative_control"]["rows"]:
        length = receipt["ring_length_L"]
        modulus = sp.Poly(x ** length + 1, x, modulus=2)
        multiplier = sp.Poly(x + x ** (length - 1), x, modulus=2).rem(modulus)
        ck(powmod(multiplier, length // 2, modulus).is_zero, f"nilpotency L={length}")
        for n, fixed in enumerate(receipt["fixed_counts_period_1_through_16"], 1):
            cleared = sp.Poly((x ** 2 + 1) ** n + x ** n, x, modulus=2)
            ck((1 << sp.gcd(modulus, cleared).degree()) == fixed == 1, f"power control fixed L={length} n={n}")

    print(json.dumps({"status": "C150_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
