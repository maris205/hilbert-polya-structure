#!/usr/bin/env python3
"""Small exact admission checks; stdout only, no empirical/infinite-proof claim."""

import hashlib
import json
import platform
from pathlib import Path

import sympy as s


def require(condition, label):
    if condition is not True:
        raise RuntimeError(label)


def equal(left, right, label):
    require(s.cancel(left - right) == 0, label)


def main():
    x, w, b, a = s.symbols("x w b a")
    parameters = [s.Rational(1, 4), s.Rational(1, 2),
                  s.Rational(3, 4), s.Integer(1), s.Integer(2)]
    rows = []
    structural = 0
    formula_checks = 0
    for alpha in parameters:
        numerator, denominator = x, s.Integer(1)
        for n in range(1, 5):
            numerator, denominator = (
                s.expand(alpha * numerator**2 - denominator**2),
                s.expand(numerator * denominator),
            )
            common = s.gcd(numerator, denominator)
            require(s.degree(common, x) == 0, "coprime iterate coordinates")
            structural += 1
            fixed = s.Poly(numerator - x * denominator, x, domain=s.QQ)
            den = s.Poly(denominator, x, domain=s.QQ)
            require(s.gcd(fixed, den).degree() == 0, "no fixed pole")
            structural += 1
            if fixed.degree() == 0:
                total_weight = s.Integer(0)
                real_count = 0
            else:
                require(s.gcd(fixed, fixed.diff()).degree() == 0,
                        "finite fixed polynomial squarefree")
                structural += 1
                # If P is squarefree and Q is the iterate denominator,
                # sum Q(r)/P'(r) = coefficient of x^(deg P - 1) in Q mod P,
                # divided by LC(P). This is exact partial fraction algebra.
                remainder = den.rem(fixed)
                total_weight = remainder.nth(fixed.degree() - 1) / fixed.LC()
                real_count = int(fixed.count_roots(-s.oo, s.oo))
            # Only the subcritical two nonreal fixed points are discarded.
            finite_real_weight = total_weight
            if alpha < 1:
                finite_real_weight += 2 / (1 - (2 * alpha - 1)**n)
            if alpha == 1:
                expected = s.Rational(n - 1, 2 * n)
            elif alpha < 1:
                expected = (2 / (1 - (2 * alpha - 1)**n)
                            - 1 / (1 - alpha**n))
            else:
                expected = 1 / (alpha**n - 1)
            equal(finite_real_weight, expected, "all-real weighted sum")
            require(real_count == (2**n if alpha > 1 else 2**n - 2),
                    "Sturm real fixed count")
            formula_checks += 2
            rows.append({"a": str(alpha), "n": n, "real_count": real_count,
                         "weighted_sum": str(s.cancel(finite_real_weight))})

    jet_checks = 0
    jet = w
    for n in range(1, 7):
        jet = s.series(jet / (1 - b * jet**2), w, 0, 7).removeO().expand()
        equal(jet.coeff(w, 3), n * b, "critical cubic coefficient")
        equal(jet.coeff(w, 5), s.Rational(n * (3*n - 1), 2) * b**2,
              "critical quintic coefficient")
        index = s.residue(1 / (w - jet), w, 0)
        equal(index, s.Rational(3*n - 1, 2*n), "critical holomorphic index")
        jet_checks += 3

    algebra_checks = 0
    # The endpoint-residue limit is checked at fixed n only; uniformity is
    # proved analytically in the proof package, not inferred from these cases.
    for n in range(1, 7):
        q = 2*a - 1
        lower = s.cancel(2 / (1-q**n) - 1 / (1-a**n))
        upper_reduced = s.cancel(1 / (a**n-1) - 2 / (q**n-1))
        equal(s.limit(lower, a, 1), s.Rational(n-1, 2*n), "left coefficient limit")
        equal(s.limit(upper_reduced, a, 1), s.Rational(n-1, 2*n),
              "right reduced coefficient limit")
        algebra_checks += 2
    equal((s.Rational(1, 4)), (1-2*s.Rational(1, 4))**2, "first resonance")
    algebra_checks += 1
    # Exact cancellation ownership at the rational first resonance.
    for k in range(1, 9):
        equal(s.Rational(1, 4)**k, (-s.Rational(1, 2))**(2*k),
              "all selected first-resonance denominator matches")
        algebra_checks += 1

    # Exact normal-form identity, using a symbolic c with b=(1-a)c^2.
    c = s.symbols("c", nonzero=True)
    z = s.I*c*(1+w)/(1-w)
    tz = a*z - (1-a)*c**2/z
    equal((tz-s.I*c)/(tz+s.I*c), w*(w+2*a-1)/(1+(2*a-1)*w),
          "Cayley conjugacy")
    algebra_checks += 1

    result = {
        "status": "PASS",
        "scope": "exact finite formula audit, not an all-parameter proof",
        "python": platform.python_version(),
        "sympy": s.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "fixed_count_and_weight_checks": formula_checks,
        "iterate_domain_and_squarefree_checks": structural,
        "critical_jet_and_index_checks": jet_checks,
        "other_exact_algebra_checks": algebra_checks,
        "rows": rows,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
