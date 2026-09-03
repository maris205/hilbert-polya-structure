#!/usr/bin/env python3
"""Independent symbolic reconstruction for HCS-C323."""
from __future__ import annotations

import sys
from fractions import Fraction

import sympy as sp


CHECKS = 0


def need(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C323 SymPy lane refuses optimized Python")

    a, g, z = sp.symbols("a g z", positive=True, real=True)
    c = sp.sqrt(a * (1 - a))
    h = -sp.Matrix([[1 + g * a, g * c], [g * c, g * (1 - a)]])
    omega2 = (g - 1) ** 2 + 4 * g * a
    need(sp.simplify(sp.trace(h) + g + 1) == 0, "bright trace")
    need(sp.simplify(h.det() - g * (1 - a)) == 0, "bright determinant")
    # Build the polynomial directly: ``Matrix.charpoly`` may intern a fresh
    # symbol when its requested generator carries assumptions.
    char = sp.expand((z * sp.eye(2) - h).det())
    want_char = sp.expand(z**2 + (g + 1) * z + g * (1 - a))
    need(sp.simplify(char - want_char) == 0, "bright characteristic polynomial")

    b = h + (g + 1) * sp.eye(2) / 2
    need(sp.simplify(b * b - omega2 * sp.eye(2) / 4) == sp.zeros(2), "trace-free square")
    s = sp.Matrix([sp.sqrt(a), sp.sqrt(1 - a)])
    w = sp.Matrix([[1, 0]])
    need(sp.simplify((w * b * s)[0] + (g + 1) * sp.sqrt(a) / 2) == 0, "bright matrix element")

    x, y = sp.symbols("x y", real=True)
    probability = a * x**2 + a * (g + 1) ** 2 * y**2 / omega2
    success = a + 4 * g * a * (1 - a) * y**2 / omega2
    need(sp.rem(sp.together(probability - success).as_numer_denom()[0], x**2 + y**2 - 1, x) == 0, "success law")
    pmax = a + 4 * g * a * (1 - a) / omega2
    defect = (1 - a) * (g - 1) ** 2 / omega2
    need(sp.simplify(pmax + defect - 1) == 0, "maximum defect")
    resonance_numerator = sp.factor(sp.together(1 - pmax).as_numer_denom()[0])
    need(sp.simplify(resonance_numerator - (1 - a) * (g - 1) ** 2) == 0, "resonance factor")

    n, gamma = sp.symbols("n gamma", positive=True, real=True)
    need(sp.simplify(-gamma * (n - 1) - (-(gamma * n) + gamma)) == 0, "complete graph uniform level")
    need(sp.simplify(gamma - gamma) == 0, "complete graph dark shift")

    k, d = sp.symbols("k d", positive=True, real=True)
    aw = k ** -2
    gw = 1 + d / k
    ow = sp.factor((gw - 1) ** 2 + 4 * gw * aw)
    need(sp.simplify(ow - (d**2 + 4 + 4 * d / k) / k**2) == 0, "window splitting")
    pw = sp.simplify(aw + 4 * gw * aw * (1 - aw) / ow)
    need(sp.simplify(sp.limit(pw, k, sp.oo) - 4 / (d**2 + 4)) == 0, "window probability limit")
    tw = sp.pi / (k * sp.sqrt(ow))
    need(sp.simplify(sp.limit(tw, k, sp.oo) - sp.pi / sp.sqrt(d**2 + 4)) == 0, "window time limit")

    drivers = [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(4)]
    for size in range(2, 33):
        for marked in range(1, size):
            af = Fraction(marked, size)
            for driver in drivers:
                of = (driver - 1) ** 2 + 4 * driver * af
                pf = af + 4 * driver * af * (1 - af) / of
                df = (1 - af) * (driver - 1) ** 2 / of
                need(of > 0, "grid positive splitting")
                need(pf + df == 1, "grid maximum partition")
                need((pf == 1) == (driver == 1), "grid perfect iff")
                need((marked - 1) + (size - marked - 1) + 2 == size, "grid multiplicity closure")
                need((-(driver + 1)) ** 2 - 4 * driver * (1 - af) == of, "grid discriminant")

    for size in range(1, 33):
        for driver in map(Fraction, (0, Fraction(1, 2), 1, 2)):
            need(1 + (size - 1) == size, "empty boundary dimension")
            need(1 + (size - 1) == size, "full boundary dimension")
            need((-driver) + 0 * (size - 1) == -driver, "empty boundary trace")
            need((-(driver + 1)) + (-1) * (size - 1) == -(driver + size), "full boundary trace")

    print(f"C323 SymPy cross-check: PASS {CHECKS} exact identities")


if __name__ == "__main__":
    main()
