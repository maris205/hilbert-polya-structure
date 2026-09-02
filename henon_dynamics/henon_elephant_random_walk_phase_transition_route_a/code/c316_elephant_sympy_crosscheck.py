#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C316."""
import sys
import sympy as sp


def main():
    if sys.flags.optimize:
        raise RuntimeError("C316 SymPy cross-check refuses optimized Python")
    a, b, s = sp.symbols("a b s")
    checks = 0
    g = sp.Integer(1)
    y = sp.Integer(1)
    mean = b
    for n in range(1, 14):
        assert sp.cancel(mean - b * g) == 0
        checks += 1
        closed = sp.cancel((2 * a * sp.prod(1 + 2 * a / j for j in range(1, n)) - n) / (2 * a - 1))
        assert sp.cancel(y - closed) == 0
        checks += 1
        mean = sp.expand((1 + a / n) * mean)
        y = sp.expand((1 + 2 * a / n) * y + 1)
        g = sp.expand(g * (1 + a / n))
    for n in range(1, 15):
        harmonic = sum((sp.Rational(1, j) for j in range(1, n + 1)), sp.Integer(0))
        yc = sp.Integer(1)
        for j in range(1, n):
            yc = sp.expand((1 + sp.Rational(1, j)) * yc + 1)
        assert sp.simplify(yc - n * harmonic) == 0
        checks += 1
    n = sp.symbols("n", integer=True, positive=True)
    ex = a * s / n
    for power in range(1, 5):
        conditional = 0
        for j in range(power + 1):
            moment_x = 1 if j % 2 == 0 else ex
            conditional += sp.binomial(power, j) * s ** (power - j) * moment_x
        direct_plus = (1 + ex) * (s + 1) ** power / 2 + (1 - ex) * (s - 1) ** power / 2
        assert sp.expand(conditional - direct_plus) == 0
        checks += 1
    # The first four raw recurrences used in the proof.
    assert sp.expand(((1 + ex)*(s+1)**2 + (1-ex)*(s-1)**2)/2 - (s**2 + 2*a*s**2/n + 1)) == 0
    assert sp.expand(((1 + ex)*(s+1)**3 + (1-ex)*(s-1)**3)/2 - ((1+3*a/n)*s**3 + (3+a/n)*s)) == 0
    assert sp.expand(((1 + ex)*(s+1)**4 + (1-ex)*(s-1)**4)/2 - ((1+4*a/n)*s**4 + (6+4*a/n)*s**2 + 1)) == 0
    checks += 3
    p, q = sp.symbols("p q")
    alpha, beta = 2*p-1, 2*q-1
    conversions = [
        beta,
        1/(2*alpha-1),
        beta*(alpha+1)/(alpha*(2*alpha-1)),
        6*(2*alpha*(alpha+1)-1)/((2*alpha-1)**2*(4*alpha-1)),
    ]
    expected = [
        2*q-1,
        1/(4*p-3),
        2*p*(2*q-1)/((2*p-1)*(4*p-3)),
        6*(8*p**2-4*p-1)/((8*p-5)*(4*p-3)**2),
    ]
    for left, right in zip(conversions, expected):
        assert sp.cancel(left-right) == 0
        checks += 1
    # p=0 reset and p=1 deterministic endpoints.
    for n0 in range(2, 20):
        assert sp.Rational(n0) * (1 - sp.Rational(1, n0)) == n0 - 1
        assert sp.prod(1 - sp.Rational(1, j) for j in range(1, n0)) == 0
        assert sp.prod(1 + sp.Rational(1, j) for j in range(1, n0)) == n0
        checks += 3
    print(f"C316 SymPy cross-check: PASS ({checks} identities; asymptotic laws excluded from finite evidence)")


if __name__ == "__main__":
    main()
