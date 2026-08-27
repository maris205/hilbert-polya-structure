#!/usr/bin/env python3
"""Separate symbolic reconstruction of the C198 SIR theorem."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c198_sir_evidence.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if sp.simplify(condition) != sp.S.true:
            raise AssertionError(message)

    x, y, x0, y0, q = sp.symbols("x y x0 y0 q", positive=True)
    beta, gamma, S, I = sp.symbols("beta gamma S I", positive=True)
    vector = sp.Matrix([-x*y, y*(x-1)])
    invariant = x + y - sp.log(x)
    derivative = sp.diff(invariant, x)*vector[0] + sp.diff(invariant, y)*vector[1]
    check(sp.Eq(sp.simplify(derivative), 0), "first integral")
    phase_y = y0 + x0 - x + sp.log(x/x0)
    check(sp.Eq(sp.simplify(x + phase_y - sp.log(x)), x0+y0-sp.log(x0)), "phase curve")
    peak_y = sp.simplify(phase_y.subs(x, 1))
    check(sp.Eq(peak_y, y0+x0-1-sp.log(x0)), "peak")
    jac = vector.jacobian([x, y]).subs(y, 0)
    check(sp.Eq(sp.factor(jac.charpoly().as_expr()), sp.Symbol("lambda")*(sp.Symbol("lambda")-x+1)), "equilibrium spectrum")
    implicit = q - sp.log(q) - x0 - y0 + sp.log(x0)
    sensitivity = -sp.diff(implicit, y0) / sp.diff(implicit, q)
    check(sp.Eq(sp.simplify(sensitivity), q/(q-1)), "final sensitivity")
    kappa = gamma/beta
    x_phys, y_phys = S/kappa, I/kappa
    dx_dtau = sp.simplify((-beta*S*I)/(kappa*gamma)).subs({S: kappa*x, I: kappa*y})
    dy_dtau = sp.simplify((beta*S*I-gamma*I)/(kappa*gamma)).subs({S: kappa*x, I: kappa*y})
    check(sp.Eq(sp.simplify(dx_dtau), -x*y), "physical x scaling")
    check(sp.Eq(sp.simplify(dy_dtau), y*(x-1)), "physical y scaling")

    for row in data["regression"]["cases"]:
        xv = sp.Rational(row["x0"])
        yv = sp.Rational(row["y0"])
        final = sp.Float(row["final_x_W0"], 95)
        companion = sp.Float(row["companion_x_Wminus1"], 95)
        constant = xv + yv - sp.log(xv)
        check(abs(sp.N(final-sp.log(final)-constant, 85)) < sp.Float("2e-79"), "final residual")
        check(abs(sp.N(companion-sp.log(companion)-constant, 85)) < sp.Float("2e-79"), "companion residual")
        check(final > 0, "positive final")
        check(companion > 1, "upper branch")
        reported_sensitivity = sp.Float(row["d_final_x_d_y0"], 95)
        check(abs(sp.N(reported_sensitivity-final/(final-1), 85)) < sp.Float("2e-79"), "numeric sensitivity")

    print(json.dumps({
        "status": "C198_SYMPY_PASS",
        "checks": checks,
        "symbolic_identities": 7,
        "evidence_cases": len(data["regression"]["cases"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
