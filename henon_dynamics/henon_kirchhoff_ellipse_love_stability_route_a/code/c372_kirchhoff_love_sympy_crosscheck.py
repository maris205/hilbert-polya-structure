#!/usr/bin/env python3
"""Independent SymPy identities and threshold certificates for HCS-C372."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("C372 SymPy verifier refuses optimized Python")

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EV = ROOT / "results/c372_kirchhoff_love_evidence.json"


def q(text):
    return sp.Rational(text)


def main():
    checks = 0
    a, b = sp.symbols("a b", positive=True, finite=True)
    omega = sp.symbols("omega", real=True, finite=True)
    delta = (a - b) / (a + b)
    kappa = 2 * a * b / (a + b) ** 2
    rotation = omega * a * b / (a + b) ** 2
    if sp.factor(kappa - (1 - delta**2) / 2) != 0:
        raise AssertionError("dimensionless identity")
    if sp.factor(2 * rotation - omega * kappa) != 0:
        raise AssertionError("rotation normalization")
    checks += 2

    # Exact interior field and normal-velocity test for the rotating boundary.
    x, y, c, s = sp.symbols("x y c s", real=True)
    ux = -omega * a * y / (a + b)
    uy = omega * b * x / (a + b)
    if sp.diff(ux, x) + sp.diff(uy, y) != 0:
        raise AssertionError("interior divergence")
    if sp.factor(sp.diff(uy, x) - sp.diff(ux, y) - omega) != 0:
        raise AssertionError("interior curl")
    point = sp.Matrix([a * c, b * s])
    normal = sp.Matrix([c / a, s / b])
    velocity = sp.Matrix([ux.subs({x: point[0], y: point[1]}), uy.subs({x: point[0], y: point[1]})])
    rigid = rotation * sp.Matrix([-point[1], point[0]])
    if sp.factor((velocity - rigid).dot(normal)) != 0:
        raise AssertionError("boundary normal rotation")
    checks += 3

    radius, theta = sp.symbols("radius theta", nonnegative=True)
    jacobian = a * b * radius
    int_x2 = sp.integrate((a * radius * sp.cos(theta)) ** 2 * jacobian, (radius, 0, 1), (theta, 0, 2 * sp.pi))
    int_y2 = sp.integrate((b * radius * sp.sin(theta)) ** 2 * jacobian, (radius, 0, 1), (theta, 0, 2 * sp.pi))
    if sp.simplify(int_x2 - sp.pi * a**3 * b / 4) != 0 or sp.simplify(int_y2 - sp.pi * a * b**3 / 4) != 0:
        raise AssertionError("ellipse moments")
    checks += 2

    m = sp.symbols("m", integer=True, positive=True)
    love_coefficient = sp.factor(((m * kappa - 1) ** 2 - delta ** (2 * m)) / 4)
    love_square = sp.factor(omega**2 * love_coefficient)
    minus = m * kappa - 1 - delta**m
    plus = m * kappa - 1 + delta**m
    if sp.factor(4 * love_square - omega**2 * minus * plus) != 0:
        raise AssertionError("Love factorization")
    checks += 1
    love1 = sp.factor(love_square.subs(m, 1))
    love2 = sp.factor(love_square.subs(m, 2))
    if sp.factor(love1 - rotation**2) != 0 or love2 != 0:
        raise AssertionError("m=1/m=2 identities")
    checks += 2

    d = sp.symbols("d", real=True)
    kap = (1 - d**2) / 2
    love_d = ((m * kap - 1) ** 2 - d ** (2 * m)) / 4
    m3 = sp.factor(16 * omega**2 * love_d.subs(m, 3))
    if sp.factor(m3 - omega**2 * (1 - d**2) ** 2 * (1 - 4 * d**2)) != 0:
        raise AssertionError("m=3 factor")
    if sp.factor(love_d.subs({m: 3, d: sp.Rational(1, 2)})) != 0:
        raise AssertionError("m=3 root")
    if (1 + sp.Rational(1, 2)) / (1 - sp.Rational(1, 2)) != 3:
        raise AssertionError("gamma=3 map")
    checks += 3

    Fm = m * (1 - d**2) / 2 - 1 - d**m
    Gm = m * (1 - d**2) / 2 - 1 + d**m
    if sp.simplify(sp.diff(Fm, d) + m * d + m * d ** (m - 1)) != 0:
        raise AssertionError("F derivative")
    if sp.simplify(sp.diff(Gm, d) - m * d * (d ** (m - 2) - 1)) != 0:
        raise AssertionError("G derivative")
    if sp.simplify(Fm.subs(d, 0) - (m / 2 - 1)) != 0 or sp.simplify(Fm.subs(d, 1) + 2) != 0:
        raise AssertionError("F endpoints")
    if sp.simplify(Gm.subs(d, 1)) != 0:
        raise AssertionError("G endpoint")
    difference = sp.factor(Fm.subs(m, m + 1) - Fm)
    expected_difference = (1 - d**2) / 2 + d**m * (1 - d)
    if sp.factor(difference - expected_difference) != 0:
        raise AssertionError("threshold-order identity")
    checks += 5

    # Boundary formulas: circle, zero-vorticity scaling, axis swap, strip.
    circle = sp.factor(love_square.subs(a, b) - omega**2 * (m - 2) ** 2 / 16)
    if circle != 0:
        raise AssertionError("circle Kelvin limit")
    if sp.factor(love_square.subs(omega, 0)) != 0:
        raise AssertionError("zero-vorticity limit")
    swapped = love_square.xreplace({a: b, b: a})
    if sp.ask(sp.Q.even(2 * m)) is not True:
        raise AssertionError("axis-swap parity premise")
    for mode in range(1, 65):
        if sp.factor(swapped.subs(m, mode) - love_square.subs(m, mode)) != 0:
            raise AssertionError(f"axis-swap invariance m={mode}")
        checks += 1
    if sp.limit(love_d, d, 1, dir="-") != 0 or sp.limit(kap / 2, d, 1, dir="-") != 0:
        raise AssertionError("strip limit")
    checks += 4

    evidence = json.loads(EV.read_text())
    thresholds = evidence["critical_thresholds"]
    if len(thresholds) != 62:
        raise AssertionError("threshold length")
    previous_upper = None
    for row in thresholds:
        mode = row["mode"]
        lower, upper = q(row["delta_lower"]), q(row["delta_upper"])
        polynomial = lambda value: sp.Rational(mode, 2) * (1 - value**2) - 1 - value**mode
        if mode == 3:
            if lower != sp.Rational(1, 2) or upper != lower or polynomial(lower) != 0:
                raise AssertionError("exact first threshold")
        else:
            if not polynomial(lower) > 0 or not polynomial(upper) < 0:
                raise AssertionError(f"threshold signs m={mode}")
            if upper - lower != sp.Rational(1, 2**96):
                raise AssertionError(f"threshold width m={mode}")
        gamma_lower = (1 + lower) / (1 - lower)
        gamma_upper = (1 + upper) / (1 - upper)
        if gamma_lower != q(row["aspect_lower"]) or gamma_upper != q(row["aspect_upper"]):
            raise AssertionError(f"threshold transform m={mode}")
        if previous_upper is not None and not previous_upper < gamma_lower:
            raise AssertionError(f"threshold ordering m={mode}")
        if not 1 < mode * (1 - upper) or not mode * (1 - lower) < 2:
            raise AssertionError(f"scaled-root bounds m={mode}")
        previous_upper = gamma_upper
        checks += 7

    for row in evidence["rigid_solution_rows"]:
        aa, bb, ww = map(sp.Rational, (row["a"], row["b"], row["vorticity"]))
        rate = ww * aa * bb / (aa + bb) ** 2
        if q(row["rotation_rate"]) != rate:
            raise AssertionError("rigid rate")
        if q(row["area_over_pi"]) != aa * bb or q(row["circulation_over_pi"]) != ww * aa * bb:
            raise AssertionError("rigid invariants")
        moment = ww * aa * bb * (aa**2 + bb**2) / 4
        if q(row["quadratic_vorticity_moment_over_pi"]) != moment:
            raise AssertionError("rigid moment")
        if aa == bb:
            if row["patch_minimal_period_over_pi"] is not None or row["oriented_axis_period_over_pi"] is not None:
                raise AssertionError("circle period convention")
        elif rate == 0:
            if row["patch_minimal_period_over_pi"] is not None or row["oriented_axis_period_over_pi"] is not None:
                raise AssertionError("zero-rate period")
        else:
            if q(row["patch_minimal_period_over_pi"]) != 1 / abs(rate):
                raise AssertionError("patch period")
            if q(row["oriented_axis_period_over_pi"]) != 2 / abs(rate):
                raise AssertionError("oriented-axis period")
        checks += 5
    print(f"C372 SymPy cross-check: PASS ({checks} exact checks)")


if __name__ == "__main__":
    main()
