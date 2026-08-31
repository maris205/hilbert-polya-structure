#!/usr/bin/env python3
"""Independent symbolic identities for the mixed congruential theorem."""
import sympy as sp

a, c, x, t, u = sp.symbols("a c x t u")
checks = 0

# Reconstruct the affine iterate without importing the producer.
state = x
for n in range(1, 11):
    state = sp.expand(a * state + c)
    series = sum(a**j for j in range(n))
    assert sp.expand(state - (a**n * x + c * series)) == 0
    assert sp.expand((a - 1) * series - (a**n - 1)) == 0
    checks += 2

# A single m-cycle has the asserted source determinant.
for m in range(2, 13):
    permutation = sp.zeros(m)
    for j in range(m):
        permutation[(j + 1) % m, j] = 1
    assert sp.simplify((sp.eye(m) - t * permutation).det() - (1 - t**m)) == 0
    assert sp.simplify((u * sp.eye(m) - permutation).det() - (u**m - 1)) == 0
    assert permutation.T * permutation == sp.eye(m)
    checks += 3

# Direct prime-power valuation samples exercise the odd and dyadic LTE faces.
for p, multiplier in ((2, 5), (3, 4), (5, 6), (7, 8)):
    for n in (1, p, p**2, p**3):
        series = sum(multiplier**j for j in range(n))
        lhs = 0
        value = series
        while value % p == 0:
            value //= p
            lhs += 1
        rhs = 0
        value = n
        while value % p == 0:
            value //= p
            rhs += 1
        assert lhs == rhs
        checks += 1

print(
    f"C258_SYMPY_PASS ({checks} symbolic/algebraic identities; "
    "affine iterates, cycle determinants, unitarity, and local valuations)"
)
