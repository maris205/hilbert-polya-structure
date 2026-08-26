#!/usr/bin/env python3
"""SymPy reconstruction of the HCS-C179 algebra, independent of producer code."""
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c179_zsigmondy_return_evidence.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    finite = data["finite_regression_sentinels"]
    z = sp.symbols("z")

    # The fixed ledger a^n-b^n sums to the stated rational source zeta.
    seen_pairs: set[tuple[int, int]] = set()
    for row in finite["global_rows"]:
        a, b = row["a"], row["b"]
        if (a, b) in seen_pairs:
            continue
        seen_pairs.add((a, b))
        logarithm = sp.series(sp.log((1 - b * z) / (1 - a * z)), z, 0, 11).removeO()
        ledger = sum(sp.Rational(a**n - b**n, n) * z**n for n in range(1, 11))
        check(sp.expand(logarithm - ledger) == 0, f"global logarithm {a},{b}")
        check(
            sp.cancel(
                sp.diff(sp.log((1 - b * z) / (1 - a * z)), z)
                - (a / (1 - a * z) - b / (1 - b * z))
            )
            == 0,
            f"global logarithmic derivative {a},{b}",
        )

    # A primitive return prime divides the homogeneous cyclotomic value.
    x = sp.symbols("x")
    for row in finite["zsigmondy_rows"]:
        a, b, n = row["a"], row["b"], row["n"]
        homogeneous = sp.expand(
            b ** sp.totient(n) * sp.cyclotomic_poly(n, x).subs(x, sp.Rational(a, b))
        )
        check(homogeneous.is_Integer is True, f"homogeneous integrality {a},{b},{n}")
        for prime in row["primitive_primes"]:
            check(int(homogeneous) % prime == 0, f"cyclotomic divisor {a},{b},{n},{prime}")
            check(sp.n_order(a * pow(b, -1, prime) % prime, prime) == n, f"return order {a},{b},{n},{prime}")

    # SymPy independently reconstructs every prime-power order lift.
    for row in finite["prime_power_lift_rows"]:
        a, b = row["a"], row["b"]
        modulus = row["modulus"]
        multiplier = a * pow(b, -1, modulus) % modulus
        check(sp.n_order(multiplier, modulus) == row["predicted_order"], f"lift order {a},{b},{modulus}")
        check(sp.totient(modulus) == row["phi"], f"lift totient {a},{b},{modulus}")

    # For representative small fibers, construct permutation and inversion
    # matrices and prove both the cycle determinant and time reversal exactly.
    selected = [
        row
        for row in finite["finite_fiber_rows"]
        if row["modulus"] <= 20 and (row["a"] + 2 * row["b"] + row["modulus"]) % 3 == 0
    ]
    check(len(selected) >= 50, "matrix sentinel population")
    lam = sp.symbols("lambda")
    for row in selected:
        a, b, modulus = row["a"], row["b"], row["modulus"]
        units = [value for value in range(modulus) if gcd(value, modulus) == 1]
        index = {value: position for position, value in enumerate(units)}
        multiplier = row["multiplier"]
        size = len(units)
        permutation = sp.zeros(size)
        inversion = sp.zeros(size)
        for position, value in enumerate(units):
            permutation[index[multiplier * value % modulus], position] = 1
            inversion[index[pow(value, -1, modulus)], position] = 1
        order = row["order"]
        cycles = row["cycle_count"]
        check(
            sp.expand(permutation.charpoly(lam).as_expr() - (lam**order - 1) ** cycles) == 0,
            f"fiber characteristic polynomial {a},{b},{modulus}",
        )
        check(inversion * permutation * inversion == permutation.inv(), f"fiber reversor {a},{b},{modulus}")

    check(data["theorem_ledger"]["prime_power_lift"].endswith("n*p^max(0,k-e)"), "lift theorem ledger")
    check("incompatible fixed ledgers" in data["theorem_ledger"]["owner_nonuniqueness"], "owner theorem ledger")
    check(data["route_a"]["tuple"][0] == "A0_WEAK_ARITHMETIC_RELATION", "Route A0")
    check(data["route_a"]["tuple"][2] == "A2_FAIL", "Route A2")

    print(json.dumps({"status": "C179_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
