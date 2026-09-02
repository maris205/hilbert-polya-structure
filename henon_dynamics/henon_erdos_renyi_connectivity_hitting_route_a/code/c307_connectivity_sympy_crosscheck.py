#!/usr/bin/env python3
"""Independent exact SymPy lane for HCS-C307."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import sympy as sp

if sys.flags.optimize:
    raise RuntimeError("HCS-C307 SymPy lane refuses python -O")

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c307_connectivity_evidence.json"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    rows = evidence["finite_connected_atlas"]["rows"]
    z = sp.symbols("z")
    connected = [sp.Integer(0), sp.Integer(1)]
    coefficient_checks = 1
    polynomial_identities = 0
    for n in range(2, 10):
        K = math.comb(n, 2)
        disconnected = sum(sp.binomial(n - 1, s - 1) * connected[s] *
                           (1 + z) ** math.comb(n - s, 2) for s in range(1, n))
        polynomial = sp.Poly(sp.expand((1 + z) ** K - disconnected), z)
        connected.append(polynomial.as_expr())
        expected = rows[n - 1]["entries"]
        for m in range(K + 1):
            check(int(polynomial.nth(m)) == expected[m]["connected_count"], f"coefficient n={n},m={m}")
            coefficient_checks += 1
        check(sp.expand(polynomial.as_expr() + disconnected - (1 + z) ** K) == 0,
              f"component identity n={n}")
        polynomial_identities += 1
        check(int(polynomial.nth(n - 1)) == n ** (n - 2), f"Cayley coefficient n={n}")

    telescoping_checks = 0
    for K in range(1, 13):
        probabilities = sp.symbols(f"p0:{K + 1}")
        substitution = {probabilities[K]: 1 - sum(probabilities[:K])}
        for order in range(1, 5):
            direct = sum(m ** order * probabilities[m] for m in range(K + 1))
            tails = [1 - sum(probabilities[:m + 1]) for m in range(K)]
            tail_sum = sum(((m + 1) ** order - m ** order) * tails[m] for m in range(K))
            check(sp.expand((direct - tail_sum).subs(substitution)) == 0,
                  f"tail moment K={K},r={order}")
            telescoping_checks += 1

    factorial_checks = 0
    for n in range(4, 21):
        K = math.comb(n, 2)
        for r in range(1, 4):
            allowed = math.comb(n - r, 2)
            for m in (0, min(n, allowed), min(2 * n, allowed)):
                # Ordered r-tuples of isolated labels times the exact number of
                # admissible m-edge graphs; all arithmetic stays exact.
                numerator = sp.prod(n - j for j in range(r)) * sp.binomial(allowed, m)
                value = sp.cancel(numerator / sp.binomial(K, m))
                check(value >= 0, "isolated factorial nonnegative")
                if m == 0:
                    check(value == sp.prod(n - j for j in range(r)), "empty-graph factorial moment")
                factorial_checks += 1

    print("C307 SymPy cross-check PASS")
    print(f"connected_coefficient_checks={coefficient_checks} polynomial_identities={polynomial_identities}")
    print(f"tail_moment_identities={telescoping_checks} isolated_factorial_exact_cells={factorial_checks}")


if __name__ == "__main__":
    main()
