#!/usr/bin/env python3
"""Reproduce a bounded algebraic diagnostic; output is not a proof certificate.

Run from any directory.  The diagnostic scope is fixed to the actual initial
transient run: 3 <= s <= 20 and 1 <= r <= s/2, gcd(r,s)=1.
No files are written; JSON is emitted on stdout.
"""

import json
import math
import platform

import numpy as np
import sympy as sp
from numpy.polynomial.polynomial import polyadd, polymul


def sum_poly(polys):
    out = np.array([0.0])
    for poly in polys:
        out = polyadd(out, poly)
    return out


def floating_coefficient(r, s):
    v = [np.array([0.0])]
    e = [np.array([1.0])]
    for n in range(1, s):
        e2 = sum_poly(polymul(e[j], e[n - 2 - j]) for j in range(n - 1))
        numerator = polyadd(0.5 * e[n - 1], np.r_[0.0, e2])
        denominator = 4.0 * math.sin(math.pi * r * n / s) ** 2
        v.append(-numerator / denominator)
        e.append(sum_poly(k * polymul(v[k], e[n - k])
                          for k in range(1, n + 1)) / n)
    e2 = sum_poly(polymul(e[j], e[s - 2 - j]) for j in range(s - 1))
    return np.trim_zeros(-polyadd(e[s - 1], 2.0 * np.r_[0.0, e2]), "b")


def exact_coefficient(r, s):
    lam = sp.Symbol("lambda")
    v = [sp.Integer(0)]
    e = [sp.Integer(1)]
    for n in range(1, s):
        denominator = sp.simplify(4 * sp.sin(sp.pi * r * n / s) ** 2)
        e2 = sum(e[j] * e[n - 2 - j] for j in range(n - 1))
        v.append(sp.expand(-(e[n - 1] / 2 + lam * e2) / denominator))
        e.append(sp.simplify(sum(k * v[k] * e[n - k]
                                 for k in range(1, n + 1)) / n))
    return sp.simplify(-e[s - 1] - 2 * lam *
                       sum(e[j] * e[s - 2 - j] for j in range(s - 1)))


def main():
    numerical = []
    for s in range(3, 21):
        for r in range(1, s // 2 + 1):
            if math.gcd(r, s) != 1:
                continue
            coef = floating_coefficient(r, s)
            roots = np.polynomial.polynomial.polyroots(coef)
            numerical.append({
                "r": r, "s": s,
                "coefficients_ascending_double": coef.tolist(),
                "roots_double_real_imag": [[float(z.real), float(z.imag)]
                                           for z in roots],
                "count_imag_above_1e-7": sum(abs(z.imag) > 1e-7 for z in roots),
                "min_real_part": float(min(z.real for z in roots)),
                "minimum_pair_separation_double":
                    float(min(abs(roots[j] - roots[i])
                              for i in range(len(roots))
                              for j in range(i + 1, len(roots))))
                    if len(roots) > 1 else None,
            })
    lam = sp.Symbol("lambda")
    exact = []
    for r, s in [(1, 3), (1, 4), (1, 5), (2, 5), (1, 6)]:
        poly = exact_coefficient(r, s)
        disc = sp.simplify(sp.expand(sp.discriminant(poly, lam)))
        exact.append({"r": r, "s": s, "polynomial": str(poly),
                      "discriminant": str(disc),
                      "discriminant_positive_exact": bool(disc > 0)})
    report = {
        "purpose": "bounded algebraic diagnostic, not an experiment or acceptance",
        "record_kind": "reproduction of initial transient numerical run plus exact checks",
        "scope": {"s_min": 3, "s_max": 20, "r_min": 1,
                  "r_max": "floor(s/2)", "condition": "gcd(r,s)=1"},
        "versions": {"python": platform.python_version(),
                     "numpy": np.__version__, "sympy": sp.__version__},
        "normalization": "C=-[t^(s-1)]exp(v)-2*lambda*[t^(s-2)]exp(2*v)",
        "numerical_cases": len(numerical),
        "numerical_nonreal_flags": int(sum(case["count_imag_above_1e-7"]
                                            for case in numerical)),
        "numeric_certification": False,
        "all_denominator_real_root_claim_proved": False,
        "numerical_results": numerical,
        "exact_small_denominator_results": exact,
    }
    print(json.dumps(report, indent=2, default=int))


if __name__ == "__main__":
    main()
