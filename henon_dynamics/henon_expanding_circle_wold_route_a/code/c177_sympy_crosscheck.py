#!/usr/bin/env python3
"""Independent SymPy checks for HCS-C177."""
from __future__ import annotations

import json
from math import gcd

import sympy as sp


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def main() -> None:
    z = sp.symbols("z")
    checks = 0
    for b in range(2, 13):
        log_series = sp.series(sp.log((1 - z) / (1 - b * z)), z, 0, 13).removeO().expand()
        for n in range(1, 13):
            assert sp.expand(log_series).coeff(z, n) == sp.Rational(b**n - 1, n)
            checks += 1
            exact = sum(sp.mobius(n // d) * (b**d - 1) for d in divisors(n))
            assert exact % n == 0
            checks += 1
            recovered = sum(sum(sp.mobius(d // e) * (b**e - 1) for e in divisors(d)) for d in divisors(n))
            assert recovered == b**n - 1
            checks += 1
        for m in range(-72, 73):
            image = b * m
            if image % b == 0:
                assert image // b == m
                checks += 1
            if m != 0:
                root, level = m, 0
                while root % b == 0:
                    root //= b
                    level += 1
                assert root * b**level == m and gcd(abs(root), b) <= b and root % b != 0
                checks += 1
        for n in range(1, 9):
            for s in range(1, 5):
                assert sp.Rational(1, (b**n) ** s) == sp.Rational(1, b ** (n * s))
                checks += 1
    print(json.dumps({"status": "C177_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
