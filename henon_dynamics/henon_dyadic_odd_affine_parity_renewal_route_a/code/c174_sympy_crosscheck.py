#!/usr/bin/env python3
"""Independent SymPy derivation checks for C174."""
from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    a, b, x, z = sp.symbols("a b x z", nonzero=True)
    checks = 0

    for n in range(1, 8):
        for word in range(2**n):
            bits = tuple((word >> j) & 1 for j in range(n))
            iterate = x
            derivative = sp.Integer(1)
            for bit in bits:
                if bit:
                    iterate = (a * iterate + b) / 2
                    derivative *= a / 2
                else:
                    iterate = iterate / 2
                    derivative /= 2
            total = sum(bits)
            prefix = 0
            polynomial = 0
            for j, bit in enumerate(bits):
                prefix += bit
                if bit:
                    polynomial += 2**j * a ** (total - prefix)
            expected = (a**total * x + b * polynomial) / 2**n
            assert sp.simplify(iterate - expected) == 0
            checks += 1
            fixed = b * polynomial / (2**n - a**total)
            assert sp.simplify(iterate.subs(x, fixed) - fixed) == 0
            checks += 1
            assert sp.simplify(derivative - a**total / 2**n) == 0
            checks += 1

    for k in range(1, 17):
        fixed_return = b / (2**k - a)
        assert sp.simplify((a * fixed_return + b) / 2**k - fixed_return) == 0
        checks += 1

    first_return = z / (1 - z)
    roof_zeta = sp.simplify(1 / (1 - first_return))
    assert sp.simplify(roof_zeta - (1 - z) / (1 - 2 * z)) == 0
    checks += 1
    assert sp.simplify(roof_zeta / (1 - z) - 1 / (1 - 2 * z)) == 0
    checks += 1

    log_roof = sp.series(sp.log((1 - z) / (1 - 2 * z)), z, 0, 34).removeO().expand()
    log_original = sp.series(-sp.log(1 - 2 * z), z, 0, 34).removeO().expand()
    log_stability = sp.series(-sp.log(1 - z), z, 0, 34).removeO().expand()
    for n in range(1, 33):
        assert sp.expand(log_roof).coeff(z, n) == sp.Rational(2**n - 1, n)
        checks += 1
        assert sp.expand(log_original).coeff(z, n) == sp.Rational(2**n, n)
        checks += 1
        assert sp.expand(log_stability).coeff(z, n) == sp.Rational(1, n)
        checks += 1

    for n in range(1, 17):
        exact = sum(sp.mobius(n // d) * 2**d for d in sp.divisors(n))
        assert exact % n == 0
        checks += 1
        reconstructed = sum(
            sum(sp.mobius(d // e) * 2**e for e in sp.divisors(d))
            for d in sp.divisors(n)
        )
        assert reconstructed == 2**n
        checks += 1

    point = sp.Rational(1, 5)
    orbit = [point]
    for _ in range(3):
        current = orbit[-1]
        if current.p % 2 == 0:
            orbit.append(current / 2)
        else:
            orbit.append((3 * current + 1) / 2)
    assert orbit == [sp.Rational(1, 5), sp.Rational(4, 5), sp.Rational(2, 5), sp.Rational(1, 5)]
    checks += 1

    y = sp.symbols("y")
    assert sp.simplify(b * (y / 2) - (b * y) / 2) == 0
    checks += 1
    assert sp.simplify(b * (a * y + 1) / 2 - (a * b * y + b) / 2) == 0
    checks += 1

    print(json.dumps({"status": "C174_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
