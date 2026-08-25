#!/usr/bin/env python3
"""Independent SymPy quotient-ring reconstruction for HCS-C155."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c155_rule90_concentration_evidence.json"


def powmod(base: sp.Poly, exponent: int, modulus: sp.Poly) -> sp.Poly:
    result = sp.Poly(1, base.gens[0], modulus=2)
    while exponent:
        if exponent & 1:
            result = result.mul(base).rem(modulus)
        base = base.mul(base).rem(modulus)
        exponent >>= 1
    return result


def fraction_record(numerator: int, denominator: int) -> dict:
    value = Fraction(numerator, denominator)
    return {"numerator": value.numerator, "denominator": value.denominator}


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

    for row in data["finite_replay"]["family_rows"]:
        length = row["ring_length_L"]
        modulus = sp.Poly(x ** length + 1, x, modulus=2)
        multiplier = sp.Poly(x + x ** (length - 1), x, modulus=2).rem(modulus)
        ck(powmod(multiplier, length + 1, modulus) == multiplier, f"Frobenius L={length}")
        ck(sp.gcd(modulus, modulus.diff()).degree() == 0, f"squarefree L={length}")
        ck(sp.gcd(modulus, sp.Poly(x ** 2 + 1, x, modulus=2)).degree() == 1, f"kernel L={length}")

        fixed_lookup = {}
        for cell in row["divisor_period_rows"]:
            n = cell["period_n"]
            cleared = sp.Poly((x ** 2 + 1) ** n + x ** n, x, modulus=2)
            dimension = sp.gcd(modulus, cleared).degree()
            fixed_lookup[n] = 1 << dimension
            ck(cell["gcd_degree"] == dimension, f"divisor dimension L={length} n={n}")
            ck(cell["fixed_points"] == 1 << dimension, f"divisor fixed L={length} n={n}")
        for cell in row["divisor_period_rows"]:
            n = cell["period_n"]
            exact = sum(int(sp.mobius(n // d)) * fixed_lookup[d] for d in sp.divisors(n))
            ck(cell["exact_period_points"] == exact, f"Mobius L={length} n={n}")
            ck(cell["primitive_cycles"] == exact // n, f"cycles L={length} n={n}")

        spectrum = Counter()
        union = 0
        for receipt in row["proper_time_dimension_rows"]:
            time = receipt["time_j"]
            d = int(sp.gcd(time, length))
            cleared = sp.Poly((x ** 2 + 1) ** time + x ** time, x, modulus=2)
            dimension = sp.gcd(modulus, cleared).degree()
            cleared_d = sp.Poly((x ** 2 + 1) ** d + x ** d, x, modulus=2)
            divisor_dimension = sp.gcd(modulus, cleared_d).degree()
            ck(receipt["gcd_j_L"] == d, f"gcd L={length} j={time}")
            ck(receipt["fixed_dimension"] == dimension, f"proper dimension L={length} j={time}")
            ck(receipt["divisor_fixed_dimension"] == divisor_dimension == dimension, f"gcd dependence L={length} j={time}")
            ck(dimension <= 2 * d, f"degree bound L={length} j={time}")
            spectrum[dimension] += 1
            union += 1 << dimension
        ck(row["fixed_dimension_spectrum"] == [{"dimension": dimension, "proper_times": count} for dimension, count in sorted(spectrum.items())], f"spectrum L={length}")
        ck(row["proper_fixed_union_bound_points"] == union, f"union L={length}")
        periodic = 1 << (length - 1)
        cycles = sum(cell["primitive_cycles"] for cell in row["divisor_period_rows"])
        ck(row["burnside_fixed_sum"] == periodic + union == length * cycles, f"Burnside L={length}")
        ck(row["normalized_cycle_excess"] == fraction_record(length * cycles - periodic, periodic), f"cycle excess L={length}")
        ck(row["mean_cycle_length_over_L"] == fraction_record(periodic, length * cycles), f"mean ratio L={length}")

    for receipt in data["power_of_two_negative_control"]["rows"]:
        length = receipt["ring_length_L"]
        modulus = sp.Poly(x ** length + 1, x, modulus=2)
        multiplier = sp.Poly(x + x ** (length - 1), x, modulus=2).rem(modulus)
        ck(powmod(multiplier, length // 2, modulus).is_zero, f"nilpotent L={length}")
        for n, fixed in enumerate(receipt["fixed_counts_period_1_through_16"], 1):
            cleared = sp.Poly((x ** 2 + 1) ** n + x ** n, x, modulus=2)
            ck((1 << sp.gcd(modulus, cleared).degree()) == fixed == 1, f"control fixed L={length} n={n}")

    print(json.dumps({"status": "C155_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
