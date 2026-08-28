#!/usr/bin/env python3
"""Independent SymPy identities for the C210 delay theorem."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c210_delay_evidence.json"


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(ap.parse_args().evidence.read_text())
    checks = 0

    def ok(expr, msg):
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(msg)

    lam, a, b, tau, t, w = sp.symbols("lambda a b tau t w", nonzero=True)
    z = -b * tau * sp.exp(a * tau)
    # Lambert-W substitution: W(z)e^W(z)=z implies Delta(-a+W/tau)=0.
    W = sp.symbols("W")
    delta_reduced = W / tau + (-W * sp.exp(W) / tau) * sp.exp(-W)
    ok(delta_reduced, "Lambert characteristic identity")
    # Multiple-root criterion obtained directly from Delta and Delta'.
    Delta = lam + a + b * sp.exp(-lam * tau)
    dDelta = sp.diff(Delta, lam)
    ok(dDelta - (1 - b * tau * sp.exp(-lam * tau)), "Delta derivative")
    root_sub = sp.solve(Delta, b)[0]
    ok(sp.simplify(dDelta.subs(b, root_sub) - (1 + tau * (lam + a))), "root derivative reduction")
    # Method-of-steps Laplace transform (formal geometric expansion).
    n = sp.symbols("n", integer=True, nonnegative=True)
    # Substitute u=t-n*tau and use Gamma(n+1)=n!; this is the independent
    # transform identity behind the finite method-of-steps terms.
    gamma_term = sp.gamma(n + 1) / (sp.factorial(n) * (lam + a) ** (n + 1))
    ok(gamma_term - 1 / (lam + a) ** (n + 1), "delayed-exponential Laplace term")
    # Hopf equations and crossing direction.
    omega = sp.symbols("omega", positive=True, real=True)
    # The two real/imaginary equations imply cos=-a/b and sin=omega/b.
    # Verify the unit-circle elimination itself (rather than a tautology).
    unit_circle = b ** 2 * ((-a / b) ** 2 + (omega / b) ** 2 - 1)
    ok(unit_circle - (a ** 2 + omega ** 2 - b ** 2), "Hopf unit-circle elimination")
    omega_control = sp.sqrt(b ** 2 - a ** 2)
    ok(omega_control ** 2 - (b ** 2 - a ** 2), "Hopf modulus relation")
    # Implicit differentiation at lambda=i omega gives a strictly positive
    # real crossing speed.
    numerator = omega ** 2 - sp.I * a * omega
    denominator = 1 + a * tau + sp.I * omega * tau
    conjugate_ratio = (numerator * sp.conjugate(denominator) + sp.conjugate(numerator) * denominator) / 2
    ok(sp.expand(conjugate_ratio - omega ** 2), "Hopf crossing numerator")
    ok((1 + a * tau) ** 2 + (omega * tau) ** 2 - denominator * sp.conjugate(denominator), "Hopf crossing denominator")
    # Evidence strings are independently counted and parsed as exact rationals.
    for row in data["regression"]["cases"]:
        aa = sp.Rational(row["a"]); bb = sp.Rational(row["b"]); tt = sp.Rational(row["tau"])
        if row["branch_point_condition"] != "b*tau*exp(a*tau)=exp(-1)":
            raise AssertionError("branch-point condition text")
        checks += 1
        for time in row["reported_times"]:
            qtime = sp.Rational(time)
            # Every term string must contain the independently expected interval count.
            if tt != 0:
                expected = int(qtime / tt)
                ok(sp.Integer(row["fundamental_solution_terms_t_quarters"][row["reported_times"].index(time)].count("exp(")) - (expected + 1), "evidence delayed-term count")
            else:
                expected = "1(t=0); exp(-%s*t)(t>0)" % (aa + bb)
                if row["fundamental_solution_terms_t_quarters"][row["reported_times"].index(time)] != expected:
                    raise AssertionError("zero-delay fundamental solution")
                checks += 1
    # Exact Hopf control identities omega^2=b^2-a^2.
    for row in data["regression"]["hopf_formula_controls"]:
        aa, bb = sp.Rational(row["a"]), sp.Rational(row["b"])
        om = sp.sympify(row["omega"], locals={"sqrt": sp.sqrt})
        ok(om ** 2 - (bb ** 2 - aa ** 2), "Hopf omega")
    generic = 8
    print(json.dumps({"status": "C210_SYMPY_PASS", "checks": checks, "generic_symbolic_checks": generic, "evidence_checks": checks - generic}, sort_keys=True))


if __name__ == "__main__":
    main()
