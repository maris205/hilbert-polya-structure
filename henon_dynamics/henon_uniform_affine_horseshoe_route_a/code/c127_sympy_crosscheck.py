#!/usr/bin/env python3
"""SymPy cross-check of the independent C127 formulas."""
import sympy as sp


def main() -> None:
    lam, mu = sp.symbols("lambda mu", positive=True)
    checks = 0
    r, s = sp.symbols("r s", integer=True, positive=True)
    for lv in [sp.Integer(3), sp.Rational(7, 2), sp.Integer(4)]:
        for mv in [sp.Rational(1, 5), sp.Rational(4, 15), sp.Rational(1, 3)]:
            for n in range(1, 13):
                unstable = sp.summation(lv ** (-n * r), (r, 1, sp.oo))
                stable = sp.summation(mv ** (n * (s - 1)), (s, 1, sp.oo))
                expected = 1 / ((lv**n - 1) * (1 - mv**n))
                assert sp.simplify(unstable * stable - expected) == 0
                checks += 1
    J = sp.Matrix([[1, 1], [1, 1]])
    for n in range(1, 13):
        assert sp.trace(J**n) == 2**n
        checks += 1
    x, y, e = sp.symbols("x y e")
    xp = lam * x - (lam - 1) * e
    yp = mu * y + (1 - mu) * e
    assert sp.det(sp.Matrix([xp, yp]).jacobian([x, y])) == lam * mu
    checks += 1
    print(f"C127 SymPy cross-check: PASS ({checks} exact identities)")


if __name__ == "__main__":
    main()
