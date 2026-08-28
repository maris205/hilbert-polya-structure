#!/usr/bin/env python3
"""Exact symbolic checks for the Kelvin--Voigt theorem."""
import sympy as sp


def main() -> None:
    lam, b, n = sp.symbols("lam b n", positive=True)
    t = sp.symbols("t", real=True)
    Delta = b**2*n**4 - 4*n**2
    checks = []
    checks.append(sp.expand((lam - (-b*n**2 + sp.sqrt(Delta))/2) *
                            (lam - (-b*n**2 - sp.sqrt(Delta))/2)) ==
                  lam**2 + b*n**2*lam + n**2)
    checks.append(sp.simplify(sp.discriminant(lam**2+b*n**2*lam+n**2, lam) - Delta) == 0)
    slow = -2*n**2/(b*n**2 + sp.sqrt(Delta))
    checks.append(sp.simplify(slow - (-b*n**2 + sp.sqrt(Delta))/2) == 0)
    checks.append(sp.simplify(Delta.subs(b, 2/n)) == 0)
    # The two gap branches meet only at the positive optimizer.
    checks.append(sp.simplify((b/2-1/b).subs(b, sp.sqrt(2))) == 0)
    checks.append(sp.diff(b/2, b) == sp.Rational(1, 2))
    checks.append(sp.diff(1/b, b) == -1/b**2)
    x = sp.Function("x")(t)
    energy = sp.Rational(1, 2)*(sp.diff(x, t)**2 + n**2*x**2)
    # Modal energy identity, with q'' substituted from the pencil.
    qdd = -b*n**2*sp.diff(x, t) - n**2*x
    checks.append(sp.simplify(sp.diff(energy, t).subs(sp.diff(x, t, 2), qdd)
                              + b*n**2*sp.diff(x, t)**2) == 0)
    checks.append(sp.limit((-b*n**2 + sp.sqrt(Delta))/2, n, sp.oo) == -1/b)
    checks.append(sp.limit((-b*n**2 - sp.sqrt(Delta))/2, n, sp.oo) == -sp.oo)
    checks.append(sp.factor((lam**2+b*n**2*lam+n**2).subs(lam, 0)) == n**2)
    assert all(checks)
    print(f"C218 SymPy cross-check: PASS ({len(checks)} symbolic identities)")
    print("quadratic pencil, discriminant/Jordan face, rationalized slow root, gap optimizer, energy, and limits: PASS")


if __name__ == "__main__":
    main()
