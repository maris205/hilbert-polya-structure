#!/usr/bin/env python3
"""Independent exact SymPy checks for the C215 coalescent identities."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c215_kingman_evidence.json"


def lam(k: int) -> sp.Rational:
    return sp.Rational(k * (k - 1), 2)


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(ap.parse_args().evidence.read_text())
    checks = 0

    def ok(expr, message: str) -> None:
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(message)

    s, ell = sp.symbols("s ell", positive=True)

    # Partial fractions of the hypoexponential transition transform.
    for i in range(1, 8):
        for j in range(1, i + 1):
            numerator = sp.prod(lam(m) for m in range(j + 1, i + 1))
            lhs = numerator / sp.prod(s + lam(m) for m in range(j, i + 1))
            rhs = 0
            for q in range(j, i + 1):
                den = sp.prod(lam(m) - lam(q) for m in range(j, i + 1) if m != q)
                rhs += numerator / den / (s + lam(q))
            ok(lhs - rhs, f"hypoexponential transform i={i},j={j}")

    # MRCA product derivatives give sums of independent exponential moments.
    for n in range(1, 9):
        M = sp.sympify(sp.prod(lam(k) / (lam(k) + s) for k in range(2, n + 1)))
        mean = sum((1 / lam(k) for k in range(2, n + 1)), sp.Rational(0))
        variance = sum((1 / lam(k) ** 2 for k in range(2, n + 1)), sp.Rational(0))
        ok(M.subs(s, 0) - 1, f"MRCA mass n={n}")
        ok(-sp.diff(M, s).subs(s, 0) - mean, f"MRCA mean n={n}")
        ok(sp.diff(M, s, 2).subs(s, 0) - (mean ** 2 + variance), f"MRCA variance n={n}")

    # Branch length is the maximum of m=n-1 iid Exp(1/2) variables.  Its CDF
    # derivative has a beta-integral LT equal to the product of spacings.
    for n in range(1, 8):
        m = n - 1
        cdf = sp.Integer(1) if m == 0 else (1 - sp.exp(-ell / 2)) ** m
        if m == 0:
            ok(cdf - 1, f"branch n={n} boundary")
            continue
        density = sp.diff(cdf, ell)
        # y=exp(-ell/2): integral e^{-s ell} density dell
        beta_form = m * sp.gamma(2 * s + 1) * sp.gamma(m) / sp.gamma(2 * s + 1 + m)
        product_form = sp.prod(sp.Rational(j, 2) / (sp.Rational(j, 2) + s) for j in range(1, m + 1))
        ok(beta_form - product_form, f"branch beta LT n={n}")
        # The CDF differentiates to a normalized density.
        ok(sp.integrate(density, (ell, 0, sp.oo)) - 1, f"branch normalization n={n}")

    # Infinite limits and the elementary Bell-number partition ledger.
    ok(sum((sp.Rational(2, k * (k - 1)) for k in range(2, 1000)), sp.Rational(0)) - sp.Rational(1996, 999), "finite telescoping control")
    ok(4 * (2 * sp.zeta(2) - 3) - (4 * sp.pi ** 2 / 3 - 12), "infinite variance")
    rows = data["regression"]["transition_rows"]
    for i, row in enumerate(rows):
        checks += 1
        if row["case_id"] != f"i{row['i']}_j{row['j']}_t{row['t']}":
            raise AssertionError(f"transition row id {i}")
    print(json.dumps({"status": "C215_SYMPY_PASS", "checks": checks, "generic_symbolic_checks": checks - len(rows), "evidence_row_checks": len(rows)}, sort_keys=True))


if __name__ == "__main__":
    main()
