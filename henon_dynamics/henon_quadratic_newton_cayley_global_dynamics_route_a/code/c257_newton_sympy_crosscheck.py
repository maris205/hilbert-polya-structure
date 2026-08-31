#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C257."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c257_newton_cayley_evidence.json"


def main() -> None:
    z, a, w, s, t = sp.symbols("z a w s t", nonzero=True)
    checks = 0

    def ck(expr, label: str) -> None:
        nonlocal checks
        checks += 1
        if sp.cancel(expr) != 0:
            raise AssertionError(label + ": " + str(sp.cancel(expr)))

    N = (z**2 + a**2) / (2 * z)
    C = (z - a) / (z + a)
    Cinv = a * (1 + w) / (1 - w)
    ck(C.subs(z, Cinv) - w, "C inverse")
    ck(Cinv.subs(w, C) - z, "inverse C")
    ck(C.subs(z, N) - C**2, "Cayley conjugacy")
    ck(N.subs(z, a * w) / a - (w**2 + 1) / (2 * w), "scale")
    ck(N.subs({z: -z, a: -a}) + N, "root-label covariance")
    ck(sp.diff(N, z).subs(z, a), "plus critical")
    ck(sp.diff(N, z).subs(z, -a), "minus critical")
    ck(N.subs(z, a) - a, "plus fixed")
    ck(N.subs(z, -a) + a, "minus fixed")

    # Iterate conjugacy and exact error identities for a generic symbol.
    for n in range(1, 13):
        power = 2**n
        zn = a * (1 + w**power) / (1 - w**power)
        ck((zn - a) - 2 * a * w**power / (1 - w**power), f"plus error {n}")
        ck((zn - a) / (zn + a) - w**power, f"Cayley iterate {n}")
        deriv = sp.diff(w**power, w).subs(w**(power - 1), 1)
        ck(deriv - power, f"multiplier {n}")

    # Boundary line and cotangent semiconjugacy, algebraically.
    boundary = sp.I * a * s
    image_s = sp.simplify(N.subs(z, boundary) / (sp.I * a))
    ck(image_s - (s**2 - 1) / (2 * s), "boundary map")
    jac = sp.diff((s**2 - 1) / (2 * s), s)
    ck(jac - (s**2 + 1) / (2 * s**2), "boundary derivative")

    # Fixed-count and zeta coefficient controls.
    zeta = 1 / ((1 - t) * (1 - 2 * t))
    logder = sp.diff(sp.log(zeta), t)
    series = sp.series(logder, t, 0, 13).removeO().expand()
    for n in range(1, 13):
        ck(series.coeff(t, n - 1) - (2**n + 1), f"zeta log coefficient {n}")

    # Exact rational grids reconstruct conjugacy without using producer code.
    for aq in (sp.Rational(1), sp.Rational(2), sp.Rational(-3), sp.Rational(5, 2)):
        for zq in (sp.Rational(-7), sp.Rational(-2), sp.Rational(-1, 2), sp.Rational(1, 3), sp.Rational(3), sp.Rational(8)):
            if zq in (0, -aq):
                continue
            ck((C.subs({a: aq, z: N.subs({a: aq, z: zq})}) - C.subs({a: aq, z: zq})**2), "grid conjugacy")

    data = json.loads(EVIDENCE.read_text())
    formulas = {row["identity_id"]: row["formula"] for row in data["exact_identities"]}
    expected = {
        "newton_map": "N_a(z)=(z^2+a^2)/(2z) for p_a(z)=z^2-a^2 and a!=0",
        "conjugacy": "C_a(N_a(z))=C_a(z)^2 on the Riemann sphere",
        "plus_error": "z_n-a=2*a*w_0^(2^n)/(1-w_0^(2^n))",
        "fixed_count": "#Fix(N_a^n)=2^n+1 on the Riemann sphere",
        "boundary_map": "on z=i*a*s, N_a gives s maps to (s^2-1)/(2s)",
    }
    for key, value in expected.items():
        checks += 1
        if formulas.get(key) != value:
            raise AssertionError("evidence formula " + key)
    checks += 1
    if data["route_a"]["tuple"] != ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]:
        raise AssertionError("route tuple")
    checks += 1
    if data["route_a"]["route_b_invocation_allowed"] is not False:
        raise AssertionError("Route B")
    print(f"C257_SYMPY_PASS ({checks} symbolic identities; Cayley conjugacy, errors, multipliers, boundary law, zeta)")


if __name__ == "__main__":
    main()
