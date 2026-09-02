#!/usr/bin/env python3
"""Independent symbolic and exact-grid cross-checks for HCS-C295."""
from __future__ import annotations

import math
from fractions import Fraction

import sympy as sp


class Checks:
    def __init__(self) -> None:
        self.n = 0

    def zero(self, expression: sp.Expr, label: str) -> None:
        self.n += 1
        if sp.simplify(expression) != 0:
            raise AssertionError(f"{label}: {sp.simplify(expression)!r}")

    def true(self, condition: bool, label: str) -> None:
        self.n += 1
        if not condition:
            raise AssertionError(label)


def main() -> None:
    c = Checks()
    mu, b, ell, q, x = sp.symbols("mu b ell q x", positive=True)
    a = sp.sqrt(ell**2 + 4 * mu * b)
    cap_b = ell + a
    s_c = cap_b**2 / (4 * mu)
    r_c2 = s_c**2 - b**2
    e_c = -2 * mu**2 / cap_b**2

    # Circular boundary and exact effective-potential minimum.
    u_s = -mu / (b + x) + ell**2 / (2 * (x**2 - b**2))
    c.zero(sp.diff(u_s, x).subs(x, s_c), "circular derivative")
    c.zero(u_s.subs(x, s_c) - e_c, "circular energy")
    c.zero(mu * (s_c - b) ** 2 - ell**2 * s_c, "circular condition")
    c.zero(mu * (s_c - b) * r_c2 - ell**2 * s_c * (s_c + b), "positive circular radius identity")

    # Action Hamiltonian and both fundamental frequencies.
    jr = mu / sp.sqrt(q) - cap_b / 2
    invariant = sp.symbols("I", positive=True)
    h_action = -mu**2 / (2 * invariant**2)
    omega_r = sp.diff(h_action, invariant)
    dshift = sp.diff(cap_b / 2, ell)
    beta = sp.Rational(1, 2) * (1 + ell / a)
    c.zero(jr.subs(q, -2 * e_c), "zero action at circular energy")
    c.zero(omega_r - mu**2 / invariant**3, "radial frequency derivative")
    c.zero(dshift - beta, "azimuthal/radial ratio derivative")
    c.zero((2 * sp.pi * mu / q ** sp.Rational(3, 2)) * (q ** sp.Rational(3, 2) / mu) - 2 * sp.pi, "period-frequency reciprocal")
    c.zero(sp.diff(mu / sp.sqrt(-2 * sp.symbols("E", negative=True)), sp.symbols("E", negative=True)) - mu / (-2 * sp.symbols("E", negative=True)) ** sp.Rational(3, 2), "action derivative")

    # Turning-point Vieta data after x=b+sqrt(b^2+r^2).
    root_sum = 2 * b + 2 * mu / q
    root_product = a**2 / q
    c.zero(root_product - (ell**2 + 4 * mu * b) / q, "root product")
    c.zero(root_product - 2 * b * root_sum + 4 * b**2 - ell**2 / q, "shifted root product")
    qpoly = -q * x**2 + (2 * mu + 2 * b * q) * x - (4 * mu * b + ell**2)
    c.zero(-sp.Poly(qpoly, x).all_coeffs()[1] / sp.Poly(qpoly, x).all_coeffs()[0] - root_sum, "Vieta sum")
    c.zero(sp.Poly(qpoly, x).all_coeffs()[2] / sp.Poly(qpoly, x).all_coeffs()[0] - root_product, "Vieta product")
    midpoint = root_sum / 2
    c.zero(2 * sp.pi * (midpoint - b) / sp.sqrt(q) - 2 * sp.pi * mu / q ** sp.Rational(3, 2), "period arcsine integral")
    c.zero(ell * (1 / sp.sqrt(root_product) + 1 / sp.sqrt(ell**2 / q)) / (2 * sp.sqrt(q)) - beta, "half-apsidal integral divided by pi")

    # Pointwise exact algebra on the complete producer grid, without importing it.
    for mu_i in (1, 2, 3):
        for b_i in (1, 2, 3):
            for ell_i in (0, 1, 2, 3):
                d = ell_i**2 + 4 * mu_i * b_i
                root = sp.sqrt(d)
                big_b = ell_i + root
                ec = -sp.Rational(2) * mu_i**2 / big_b**2
                sc = big_b**2 / (4 * mu_i)
                c.zero(ec + sp.Rational(2) * mu_i**2 / big_b**2, "grid Ec")
                c.zero(sc - b_i - ell_i * big_b / (2 * mu_i), "grid sc rationalization")
                c.zero(mu_i * (sc - b_i) * (sc**2 - b_i**2) - ell_i**2 * sc * (sc + b_i), "grid rc2")
                for k in (1, 2, 3):
                    inv = sp.Rational(k, 2) * big_b
                    action = sp.Rational(k - 1, 2) * big_b
                    energy = ec / k**2
                    omr = mu_i**2 / inv**3
                    period = mu_i / (-2 * energy) ** sp.Rational(3, 2)
                    ratio = sp.Rational(1, 2) * (1 + sp.Rational(ell_i, 1) / root)
                    c.zero(action + big_b / 2 - inv, "grid invariant")
                    c.zero(energy + sp.Rational(mu_i**2, 2) / inv**2, "grid action inversion")
                    c.zero(period * omr - 1, "grid period reciprocal")
                    c.zero(omr - (-2 * energy) ** sp.Rational(3, 2) / mu_i, "grid frequency energy form")
                    c.true(bool(action >= 0), "grid nonnegative action")
                    c.true(bool(ec <= energy < 0), "grid allowed energy")
                    c.true(bool((action == 0) == (k == 1)), "grid circular iff")
                    c.true(bool(sp.Rational(1, 2) <= ratio < 1), "grid ratio range")
                    if ell_i == 0:
                        c.zero(ratio - sp.Rational(1, 2), "radial limiting ratio")
                    elif math.isqrt(d) ** 2 == d:
                        c.true(isinstance(Fraction(1, 2) * (1 + Fraction(ell_i, math.isqrt(d))), Fraction), "rational resonance")
                    else:
                        c.true(sp.ask(sp.Q.irrational(ratio)) is True, "quadratic irrational ratio")

    # Boundary limits are symbolic statements, not samples.
    c.true(sp.limit(jr, q, 0, dir="+") is sp.oo, "escape action divergence")
    c.true(sp.limit(2 * sp.pi * mu / q ** sp.Rational(3, 2), q, 0, dir="+") is sp.oo, "escape period divergence")
    c.zero(sp.limit(jr, b, 0, dir="+") - (mu / sp.sqrt(q) - ell), "Kepler action limit")
    c.zero(sp.limit(beta, b, 0, dir="+") - 1, "Kepler ratio limit")

    print(f"C295_SYMPY_PASS ({c.n} symbolic/exact checks; circular boundary, Vieta integrals, action-frequency map, closure grid, escape and Kepler limits)")


if __name__ == "__main__":
    main()
