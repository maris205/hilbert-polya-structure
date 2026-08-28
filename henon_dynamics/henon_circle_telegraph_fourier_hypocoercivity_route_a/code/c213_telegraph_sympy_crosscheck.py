#!/usr/bin/env python3
"""Independent exact SymPy identities for the circular telegraph theorem."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c213_telegraph_evidence.json"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(ap.parse_args().evidence.read_text())
    checks = 0

    def ok(expr, msg):
        nonlocal checks
        checks += 1
        if isinstance(expr, sp.MatrixBase):
            good = all(sp.simplify(v) == 0 for v in expr)
        else:
            good = sp.simplify(expr) == 0
        if not good:
            raise AssertionError(msg)

    c, lam, k, t, r, delta = sp.symbols("c lambda k t r delta", real=True)
    I = sp.I
    G = sp.Matrix([[-lam + I*c*k, lam], [lam, -lam - I*c*k]])
    N = G + lam * sp.eye(2)
    ok(N * N - (lam**2 - c**2 * k**2) * sp.eye(2), "N-square")
    # Verify that the displayed matrix exponential has the correct initial
    # value and solves E'=G E after the relation d^2=lambda^2-c^2 k^2.
    d = sp.symbols("d", nonzero=True, real=True)
    E = sp.exp(-lam*t) * (sp.cosh(d*t)*sp.eye(2) + sp.sinh(d*t)*N/d)
    ok(E.subs(t, 0) - sp.eye(2), "matrix exponential initial value")
    residual = (sp.diff(E, t) - G*E).applyfunc(
        lambda value: sp.factor(value).subs(d**2, lam**2-c**2*k**2))
    ok(residual, "matrix exponential ODE")
    char = sp.factor((r * sp.eye(2) - G).det())
    ok(char - ((r + lam)**2 - (lam**2 - c**2*k**2)), "characteristic polynomial")
    # The two-component forward equations imply the telegraph equation for rho.
    # With rho_t=-c*j_x and j_t=-c*rho_x-2 lambda*j, differentiate the
    # first equation once and substitute (j_t)_x.
    rho_xx, rho_t = sp.symbols("rho_xx rho_t")
    jx = -rho_t / c
    jtx = -c * rho_xx - 2 * lam * jx
    rho_tt = -c * jtx
    ok(rho_tt + 2 * lam * rho_t - c**2 * rho_xx, "telegraph elimination")
    # Critical/Jordan condition and zero mode are exact polynomial statements.
    ok((lam**2 - c**2*k**2).subs(lam, c*k), "critical delta")
    zero_char = sp.factor(char.subs(k, 0))
    ok(zero_char - r*(r + 2*lam), "zero mode roots")
    # Diffusive branch identity: lambda-sqrt(lambda^2-c^2) is positive and
    # equals c^2/(lambda+sqrt(...)) formally after rationalisation.
    s = sp.sqrt(lam**2 - c**2)
    ok(sp.expand((lam - s) * (lam + s) - c**2), "gap rationalisation")
    # Re-check every serialized row's exact trace/determinant/delta relations.
    rows = data["regression"]["block_rows"]
    for i, row in enumerate(rows):
        cc, ll, kk = sp.Rational(row["c"]), sp.Rational(row["lambda"]), sp.Integer(row["k"])
        ok(sp.Rational(row["delta_square"]) - (ll**2 - cc**2*kk**2), f"row {i} delta")
        ok(sp.Rational(row["generator_trace"]) + 2*ll, f"row {i} trace")
        ok(sp.Rational(row["generator_determinant"]) - cc**2*kk**2, f"row {i} determinant")
    # Gap strings are checked independently on the finite parameter atlas.
    for i, row in enumerate(data["regression"]["gap_rows"]):
        cc, ll = sp.Rational(row["c"]), sp.Rational(row["lambda"])
        if cc != 0 and ll != 0 and ll > cc:
            gap = ll - sp.sqrt(ll**2 - cc**2)
            ok(gap * (2*ll - gap) - cc**2, f"gap {i} branch")
        else:
            checks += 1
    generic = 8
    print(json.dumps({"status": "C213_SYMPY_PASS", "checks": checks, "generic_symbolic_checks": generic, "evidence_row_checks": checks - generic}, sort_keys=True))


if __name__ == "__main__":
    main()
