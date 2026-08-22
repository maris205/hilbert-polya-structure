#!/usr/bin/env python3
"""Exact period-one/two holomorphic Hénon transfer pilot (C108)."""
from __future__ import annotations

from fractions import Fraction
import json
from hashlib import sha256
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c108_holomorphic_evidence.json"
a = sp.Rational(1, 4)
c = sp.Rational(0)
x, y, z, w = sp.symbols("x y z w")


def clean(value):
    value = sp.simplify(value)
    return str(value)


def jacobian_at(second_coordinate):
    return sp.Matrix([[0, 1], [-a, 2 * second_coordinate]])


def main() -> None:
    # F(z,w)=(w,w^2-a z), a=1/4.  It is a polynomial automorphism with a
    # holomorphic inverse, but no finite polynomial subspace is invariant.
    fixed_poly = sp.factor(x - (x**2 + c - a * x))
    fixed_roots = sp.solve(fixed_poly, x)
    fixed = [(r, r) for r in fixed_roots]
    fixed_weights = []
    for r in fixed_roots:
        d = sp.factor((sp.eye(2) - jacobian_at(r)).det())
        fixed_weights.append({"point": [clean(r), clean(r)], "denominator": clean(d), "weight": clean(1 / d)})

    f1 = y - (x**2 + c - a * x)
    f2 = x - (y**2 + c - a * y)
    resultant = sp.factor(sp.resultant(f1, f2, y))
    period2_roots = sp.solve(resultant, x)
    all_period2 = []
    for rx in period2_roots:
        ry = sp.simplify(rx**2 + c - a * rx)
        m = jacobian_at(ry) * jacobian_at(rx)
        d = sp.factor((sp.eye(2) - m).det())
        all_period2.append({"point": [clean(rx), clean(ry)], "denominator": clean(d), "weight": clean(1 / d)})
    trace1 = sp.simplify(sum(sp.sympify(item["weight"]) for item in fixed_weights))
    trace2 = sp.simplify(sum(sp.sympify(item["weight"]) for item in all_period2))
    coeff2 = sp.simplify(trace1**2 / 2 - trace2 / 2)

    # Pulling back polynomial coordinates by F^{-1}(z,w)=((z^2-w)/a,z)
    # exhibits degree growth and is an exact warning against a finite
    # polynomial Galerkin owner.
    inv = {z: (z**2 - w) / a, w: z}
    current = z
    degrees = []
    for _ in range(3):
        current = sp.expand(current.xreplace(inv))
        degrees.append(int(sp.Poly(current, z, w).total_degree()))

    payload = {
        "schema": "hcs-c108-holomorphic-henon-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "map": {"formula": "F(z,w)=(w,w^2-(1/4)z)", "jacobian_determinant": "1/4", "inverse": "F^{-1}(z,w)=(4z^2-4w,z)"},
        "fixed_point_polynomial": clean(fixed_poly),
        "fixed_points": fixed_weights,
        "period_two_resultant": clean(resultant),
        "period_two_fixed_points": all_period2,
        "weighted_traces": {"1": clean(trace1), "2": clean(trace2)},
        "formal_determinant_prefix": ["1/1", clean(-trace1), clean(coeff2)],
        "inverse_pullback_degree_growth": degrees,
        "verdict": {
            "A1": "A1_OPEN",
            "A2": "A2_CERTIFIED_PREFIX",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "reason": "period-one/two holomorphic cycle weights are exact, but a source-native nuclear owner and complete real clock are not proved",
        },
        "nonclaims": ["global complex Hénon repeller", "analytic Fredholm determinant", "prime correspondence", "Riemann zeros", "Route B"],
    }
    raw = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    OUT.write_text(raw)
    print(json.dumps({"evidence_sha256": sha256(raw.encode()).hexdigest(), "trace1": clean(trace1), "trace2": clean(trace2), "degree_growth": degrees}, sort_keys=True))


if __name__ == "__main__":
    main()
