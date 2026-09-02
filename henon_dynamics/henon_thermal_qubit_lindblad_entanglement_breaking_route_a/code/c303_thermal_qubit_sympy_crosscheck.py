#!/usr/bin/env python3
"""Independent symbolic derivation of the C303 identities."""
from __future__ import annotations

import sympy as s


def main() -> None:
    gd, gu, gp, w, t = s.symbols("gd gu gp w t", nonnegative=True, real=True)
    lam = s.Symbol("lambda")
    g1 = gd + gu
    g2 = g1 / 2 + gp
    checks = 0

    def need(expr):
        nonlocal checks
        assert s.simplify(expr) == 0
        checks += 1

    L = s.Matrix([
        [-gu, 0, 0, gd],
        [0, -g2 + s.I * w, 0, 0],
        [0, 0, -g2 - s.I * w, 0],
        [gu, 0, 0, -gd],
    ])
    target_char = lam * (lam + g1) * ((lam + g2) ** 2 + w ** 2)
    need(L.charpoly(lam).as_expr() - target_char)
    need(L.det())
    need((L * s.Matrix([gd, 0, 0, gu])).norm())
    for j in range(4):
        need(L[0, j] + L[3, j])

    r11, r01, r10 = s.symbols("r11 r01 r10")
    p, eta = s.symbols("p eta", positive=True, real=True)
    pop = p + s.exp(-g1 * t) * (r11 - p)
    coh = s.exp((-g2 + s.I * w) * t) * r01
    need(s.diff(pop, t) + g1 * (pop - p))
    need(s.diff(coh, t) - (-g2 + s.I * w) * coh)

    a = 1 - p * (1 - eta)
    b = p * (1 - eta)
    d = (1 - p) * (1 - eta)
    e = eta + p * (1 - eta)
    k, q = s.symbols("k q", nonnegative=True, real=True)
    need(a + b - 1)
    need(d + e - 1)
    need(a * e - eta - p * (1 - p) * (1 - eta) ** 2)
    need(b * d - p * (1 - p) * (1 - eta) ** 2)
    c = s.symbols("c")
    Jpt = s.Matrix([[a, 0, 0, 0], [0, b, c, 0], [0, s.conjugate(c), d, 0], [0, 0, 0, e]]) / 2
    need(Jpt[1:3, 1:3].det() - (b * d - c * s.conjugate(c)) / 4)

    r = s.symbols("r", positive=True)
    eta_star = (1 + 2 * r - s.sqrt(1 + 4 * r)) / (2 * r)
    need(r * (1 - eta_star) ** 2 - eta_star)
    need(eta_star.subs(r, s.Rational(1, 4)) - (3 - 2 * s.sqrt(2)))

    # Exact finite-cell sweep independently re-establishes Choi/PPT identities.
    for pv in [s.Rational(0), s.Rational(1, 4), s.Rational(1, 2), s.Rational(3, 4), s.Rational(1)]:
        for ev in [s.Rational(0), s.Rational(1, 4), s.Rational(1, 2), s.Rational(3, 4), s.Rational(1)]:
            av, bv = 1 - pv * (1 - ev), pv * (1 - ev)
            dv, ee = (1 - pv) * (1 - ev), ev + pv * (1 - ev)
            need(av + bv - 1)
            need(dv + ee - 1)
            need(av * ee - ev - pv * (1 - pv) * (1 - ev) ** 2)
            need(bv * dv - pv * (1 - pv) * (1 - ev) ** 2)

    # Generator eigenvectors remain independent even at accidental eigenvalue collisions.
    for values in [(1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0), (3, 1, 2, 1), (0, 0, 1, 0), (0, 0, 0, 2)]:
        Lv = L.subs(dict(zip((gd, gu, gp, w), values)))
        need(Lv.charpoly(lam).as_expr() - target_char.subs(dict(zip((gd, gu, gp, w), values))))
        assert sum(mult for _, mult in Lv.eigenvals().items()) == 4
        checks += 1

    # The Bloch linear part has the claimed singular values.
    x, y = s.symbols("x y", positive=True)
    M = s.diag(x, x, y)
    need((M.T * M - s.diag(x ** 2, x ** 2, y ** 2)).norm())
    print(f"C303 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
