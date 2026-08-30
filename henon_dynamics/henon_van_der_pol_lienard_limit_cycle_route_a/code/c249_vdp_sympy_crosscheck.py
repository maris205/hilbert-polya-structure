#!/usr/bin/env python3
"""Independent exact symbolic reconstruction for HCS-C249."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c249_vdp_evidence.json"


def main() -> None:
    x, y, mu, lam, omega, mu0 = sp.symbols("x y mu lam omega mu0", real=True)
    xdot = y
    ydot = mu * (1 - x**2) * y - x
    checks = 0

    def ck(expr, label):
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(label + ": " + str(sp.simplify(expr)))

    # Vector-field, Lienard, energy and divergence identities.
    E = (x**2 + y**2) / 2
    ck(sp.diff(E, x) * xdot + sp.diff(E, y) * ydot - mu * (1 - x**2) * y**2, "energy")
    ck(sp.diff(xdot, x) + sp.diff(ydot, y) - mu * (1 - x**2), "divergence")
    f = mu * (x**2 - 1)
    F = sp.integrate(f, (x, 0, x))
    ck(F - mu * (x**3 / 3 - x), "Lienard primitive")
    ck(sp.factor(F) - mu * x * (x**2 - 3) / 3, "Lienard factor")

    J = sp.Matrix([[sp.diff(xdot, x), sp.diff(xdot, y)], [sp.diff(ydot, x), sp.diff(ydot, y)]])
    J0 = J.subs({x: 0, y: 0})
    ck(J0.det() - 1, "origin determinant")
    ck(J0.trace() - mu, "origin trace")
    ck(sp.factor((lam * sp.eye(2) - J0).det()) - (lam**2 - mu * lam + 1), "origin characteristic")

    # Time reversal: R(x,y)=(x,-y), with parameter -mu.
    R = sp.diag(1, -1)
    field_plus = sp.Matrix([xdot, ydot])
    field_minus_at_R = sp.Matrix([(-y), (-mu) * (1 - x**2) * (-y) - x])
    ck((R * field_plus + field_minus_at_R)[0], "time reversal x")
    ck((R * field_plus + field_minus_at_R)[1], "time reversal y")

    # Frequency scaling tau=omega*t.
    u1, u2 = sp.symbols("u1 u2")
    scaled = omega**2 * u2 + mu0 * (x**2 - 1) * omega * u1 + omega**2 * x
    normalized = u2 + (mu0 / omega) * (x**2 - 1) * u1 + x
    ck(scaled / omega**2 - normalized, "frequency scaling")

    # Pointwise exact controls over a rational grid.
    for mq in (sp.Rational(-2), sp.Rational(-1), sp.Rational(0), sp.Rational(1, 10), sp.Rational(1, 2), sp.Rational(1), sp.Rational(2), sp.Rational(4)):
        for xq, yq in ((sp.Rational(0), sp.Rational(1)), (sp.Rational(1), sp.Rational(2)), (sp.Rational(2), sp.Rational(-1)), (sp.Rational(-3, 2), sp.Rational(5, 3))):
            rhs_E = (mu * (1 - x**2) * y**2).subs({mu: mq, x: xq, y: yq})
            direct_E = (sp.diff(E, x) * xdot + sp.diff(E, y) * ydot).subs({mu: mq, x: xq, y: yq})
            ck(direct_E - rhs_E, "grid energy")
            direct_div = (sp.diff(xdot, x) + sp.diff(ydot, y)).subs({mu: mq, x: xq, y: yq})
            ck(direct_div - mq * (1 - xq**2), "grid divergence")

    # The evidence must retain the exact formulas and strict route boundary.
    data = json.loads(EVIDENCE.read_text())
    formulas = {row["identity_id"]: row["formula"] for row in data["exact_identities"]}
    expected = {
        "vector_field": "xdot=y; ydot=mu*(1-x^2)*y-x",
        "lienard_form": "xddot+mu*(x^2-1)*xdot+x=0",
        "primitive_F": "F(x)=integral_0^x mu*(s^2-1) ds=mu*(x^3/3-x)",
        "energy": "E=(x^2+y^2)/2; Edot=mu*(1-x^2)*y^2",
        "divergence": "div X=mu*(1-x^2)",
    }
    for key, value in expected.items():
        checks += 1
        if formulas.get(key) != value:
            raise AssertionError("evidence formula " + key)
    checks += 1
    if data["route_a"]["tuple"] != ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]:
        raise AssertionError("route tuple")
    checks += 1
    if data["route_a"]["route_b_invocation_allowed"] is not False:
        raise AssertionError("route B")

    print(f"C249_SYMPY_PASS ({checks} symbolic identities; Lienard, energy, divergence, reversal, scaling)")


if __name__ == "__main__":
    main()
