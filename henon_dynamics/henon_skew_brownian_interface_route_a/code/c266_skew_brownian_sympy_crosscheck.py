#!/usr/bin/env python3
"""Independent symbolic reconstruction for HCS-C266."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c266_skew_brownian_evidence.json"


def main():
    checks = 0

    def ok(expr):
        nonlocal checks
        assert s.simplify(expr) == 0
        checks += 1

    p, t, x, y = s.symbols("p t x y", positive=True)
    theta = 2 * p - 1
    gauss = lambda z: s.exp(-z**2 / (2 * t)) / s.sqrt(2 * s.pi * t)

    # Backward heat equation and skew interface, first for y>0.
    q_xplus = gauss(y - x) + theta * gauss(x + y)
    q_xminus = 2 * p * gauss(y - x)
    ok(s.diff(q_xplus, t) - s.diff(q_xplus, x, 2) / 2)
    ok(s.diff(q_xminus, t) - s.diff(q_xminus, x, 2) / 2)
    ok(s.limit(q_xplus, x, 0, dir="+") - s.limit(q_xminus, x, 0, dir="-"))
    ok(p * s.limit(s.diff(q_xplus, x), x, 0, dir="+") - (1 - p) * s.limit(s.diff(q_xminus, x), x, 0, dir="-"))

    # Repeat for a negative terminal point, represented by its positive modulus y.
    q2_xplus = 2 * (1 - p) * gauss(y + x)
    q2_xminus = gauss(x + y) - theta * gauss(y - x)
    ok(s.diff(q2_xplus, t) - s.diff(q2_xplus, x, 2) / 2)
    ok(s.diff(q2_xminus, t) - s.diff(q2_xminus, x, 2) / 2)
    ok(s.limit(q2_xplus, x, 0, dir="+") - s.limit(q2_xminus, x, 0, dir="-"))
    ok(p * s.limit(s.diff(q2_xplus, x), x, 0, dir="+") - (1 - p) * s.limit(s.diff(q2_xminus, x), x, 0, dir="-"))

    # Speed-density detailed balance in the two cross-interface directions.
    z = s.symbols("z", positive=True)
    cross_pos_to_neg = 2 * (1 - p) * gauss(x + z)
    cross_neg_to_pos = 2 * p * gauss(x + z)
    ok(cross_pos_to_neg / (2 * (1 - p)) - cross_neg_to_pos / (2 * p))

    # Resolvent solves (lambda-A)r=0 away from its pole in every quadrant.
    lam = s.symbols("lam", positive=True)
    k = s.sqrt(2 * lam)
    r_pp_left = (s.exp(-k * (y - x)) + theta * s.exp(-k * (x + y))) / k
    r_pp_right = (s.exp(-k * (x - y)) + theta * s.exp(-k * (x + y))) / k
    r_cross = 2 * p * s.exp(-k * (y - x)) / k
    for expr in (r_pp_left, r_pp_right, r_cross):
        ok(lam * expr - s.diff(expr, x, 2) / 2)

    # Hitting probability and mean exit time solve their two BVPs.
    a, b = s.symbols("a b", positive=True)
    D = p * a + (1 - p) * b
    h_minus = p * (x + a) / D
    h_plus = (p * a + (1 - p) * x) / D
    ok(h_minus.subs(x, -a))
    ok(h_plus.subs(x, b) - 1)
    ok(h_minus.subs(x, 0) - h_plus.subs(x, 0))
    ok(p * s.diff(h_plus, x).subs(x, 0) - (1 - p) * s.diff(h_minus, x).subs(x, 0))
    ok(s.diff(h_minus, x, 2))
    ok(s.diff(h_plus, x, 2))

    Dm = (1 - p) * b + p * a
    A = (1 - p) * (b**2 - a**2) / Dm
    C = p * (b**2 - a**2) / Dm
    B = a * b * (p * b + (1 - p) * a) / Dm
    m_minus, m_plus = -x**2 + C * x + B, -x**2 + A * x + B
    ok(m_minus.subs(x, -a))
    ok(m_plus.subs(x, b))
    ok(m_minus.subs(x, 0) - m_plus.subs(x, 0))
    ok(p * s.diff(m_plus, x).subs(x, 0) - (1 - p) * s.diff(m_minus, x).subs(x, 0))
    ok(s.diff(m_minus, x, 2) / 2 + 1)
    ok(s.diff(m_plus, x, 2) / 2 + 1)

    # Discounted right-exit transform: boundaries, interface, and ODE.
    rho = (1 - p) / p
    den = s.cosh(k * b) * s.sinh(k * a) + rho * s.sinh(k * b) * s.cosh(k * a)
    e_minus = s.sinh(k * (x + a)) / den
    e_plus = (s.cosh(k * x) * s.sinh(k * a) + rho * s.sinh(k * x) * s.cosh(k * a)) / den
    ok(e_minus.subs(x, -a))
    ok(e_plus.subs(x, b) - 1)
    ok(e_minus.subs(x, 0) - e_plus.subs(x, 0))
    ok(p * s.diff(e_plus, x).subs(x, 0) - (1 - p) * s.diff(e_minus, x).subs(x, 0))
    ok(s.diff(e_minus, x, 2) / 2 - lam * e_minus)
    ok(s.diff(e_plus, x, 2) / 2 - lam * e_plus)

    # Occupation density: reflection identity and Brownian specialization.
    u = s.symbols("u", positive=True)
    occ = p * (1 - p) / (s.pi * s.sqrt(u * (1 - u)) * (p**2 * (1 - u) + (1 - p) ** 2 * u))
    reflected = occ.xreplace({p: 1 - p, u: 1 - u})
    ok(occ - reflected)
    ok(occ.subs(p, s.Rational(1, 2)) - 1 / (s.pi * s.sqrt(u * (1 - u))))

    # Exact regression rows are independently reconstructed as rationals.
    data = json.loads(EVIDENCE.read_text())
    for row in data["regression"]["exit_rows"]:
        pp, aa, bb, xx = map(s.Rational, (row["p"], row["a"], row["b"], row["x"]))
        DD = pp * aa + (1 - pp) * bb
        hh = pp * (xx + aa) / DD if xx <= 0 else (pp * aa + (1 - pp) * xx) / DD
        ok(hh - s.Rational(row["right_probability"]))
        DDm = (1 - pp) * bb + pp * aa
        AA = (1 - pp) * (bb**2 - aa**2) / DDm
        CC = pp * (bb**2 - aa**2) / DDm
        BB = aa * bb * (pp * bb + (1 - pp) * aa) / DDm
        mm = -xx**2 + (CC if xx <= 0 else AA) * xx + BB
        ok(mm - s.Rational(row["mean_exit_time"]))

    assert data["regression"]["counts"]["exit_rows"] == 50
    checks += 1
    print(f"C266_SYMPY_PASS ({checks} symbolic checks)")


if __name__ == "__main__":
    main()
