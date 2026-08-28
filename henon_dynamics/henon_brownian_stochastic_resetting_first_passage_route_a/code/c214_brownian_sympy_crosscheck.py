#!/usr/bin/env python3
"""Independent symbolic identities for the C214 renewal theorem."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c214_brownian_evidence.json"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(ap.parse_args().evidence.read_text())
    checks = 0

    def ok(expr, message: str) -> None:
        nonlocal checks
        checks += 1
        if isinstance(expr, sp.MatrixBase):
            good = all(sp.simplify(v) == 0 for v in expr)
        else:
            good = sp.simplify(expr) == 0
        if not good:
            raise AssertionError(message)

    D, r, a, s, z, t, x = sp.symbols("D r a s z t x", positive=True)
    pi = sp.pi
    G = sp.exp(-x**2 / (4 * D * t)) / sp.sqrt(4 * pi * D * t)
    # Heat equation and normalization of the free kernel.
    ok(sp.diff(G, t) - D * sp.diff(G, x, 2), "heat kernel PDE")
    ok(sp.integrate(G, (x, -sp.oo, sp.oo)) - 1, "free kernel normalization")

    # Renewal algebra: F=f/(1-r(1-f)/(s+r)) reduces to the displayed form,
    # while S=(1-F)/s.  Keeping f symbolic avoids branch assumptions.
    f = sp.symbols("f")
    renewal = sp.factor(f / (1 - r * (1 - f) / (s + r)))
    ok(renewal - (s + r) * f / (s + r * f), "renewal transform")
    Fsym = (s + r) * f / (s + r * f)
    ok(sp.factor((1 - Fsym) / s - (1 - f) / (s + r * f)), "survival transform")

    # Substitution f=exp(-a*sqrt((s+r)/D)) gives the Brownian first-passage
    # transform; the derivative at s=0 is evaluated by an exact limit.
    fb = sp.exp(-a * sp.sqrt((s + r) / D))
    Fb = (s + r) * fb / (s + r * fb)
    Sb = (1 - fb) / (s + r * fb)
    mfpt_expr = sp.simplify(-sp.limit(sp.diff(Fb, s), s, 0, dir="+"))
    expected_mfpt = (sp.exp(a * sp.sqrt(r / D)) - 1) / r
    ok(mfpt_expr - expected_mfpt, "MFPT derivative")
    ok(sp.limit(Sb, s, 0, dir="+") - expected_mfpt, "survival zero limit")

    # Dimensionless optimality derivative.  The positive factor is omitted;
    # its numerator has the unique nonzero root z=2(1-exp(-z)).
    g = (sp.exp(z) - 1) / z**2
    numerator = sp.factor(sp.diff(g, z) * z**3 * sp.exp(-z))
    ok(numerator - (z - 2 * (1 - sp.exp(-z))), "optimality numerator")
    checks += 1
    if sp.limit(g, z, 0, dir="+") != sp.oo:
        raise AssertionError("zero-reset limit")
    checks += 1
    if sp.limit(g, z, sp.oo) != sp.oo:
        raise AssertionError("infinite-reset limit")

    # Stationary Laplace law and its two-sided mass.
    y = sp.symbols("y", real=True)
    root = sp.sqrt(r / D)
    ppos = root * sp.exp(-root * sp.Abs(y)) / 2
    # Split at zero so SymPy does not need a distributional Abs rule.
    norm = sp.integrate(root * sp.exp(root * y) / 2, (y, -sp.oo, 0)) + sp.integrate(root * sp.exp(-root * y) / 2, (y, 0, sp.oo))
    ok(norm - 1, "stationary normalization")

    # Exact moment identities for the stated survival convention.  From
    # F(s)=1-s*S(s), differentiation at zero gives
    # (-1)^n F^(n)(0)=n(-1)^(n-1)S^(n-1)(0); integration by parts identifies
    # the right side with E[T^n].  Verify the first three orders on a formal
    # Taylor jet, independently of the numerical rows.
    s0, s1, s2, s3 = sp.symbols("s0 s1 s2 s3")
    Sjet = s0 + s1 * s + s2 * s**2 / 2 + s3 * s**3 / 6
    Fjet = 1 - s * Sjet
    for n in (0, 1, 2, 3):
        if n == 0:
            ok(Fjet.subs(s, 0) - 1, "zeroth F moment")
            continue
        lhs = (-1) ** n * sp.diff(Fjet, s, n).subs(s, 0)
        rhs = n * (-1) ** (n - 1) * sp.diff(Sjet, s, n - 1).subs(s, 0)
        ok(lhs - rhs, f"moment derivative relation {n}")

    # Structural rows are checked without importing producer code.
    rows = data["regression"]["fpt_rows"]
    for i, row in enumerate(rows):
        checks += 1
        if not (row["case_id"].startswith("D") and row["case_id"].count("_s") == 1):
            raise AssertionError(f"fpt row id {i}")
    print(json.dumps({"status": "C214_SYMPY_PASS", "checks": checks, "generic_symbolic_checks": 14, "evidence_row_checks": len(rows)}, sort_keys=True))


if __name__ == "__main__":
    main()
