"""Bounded exact checks; none of the all-period statements rely on these data.

Run with Python and python-flint. Prints JSON; does not write or mutate files.
All polynomial computations are over the exact prime field, not finite-field
point enumeration. Squarefree-factor degrees count geometric points.
"""

import json
import flint
from flint import nmod_poly


def vp(n, p):
    r = 0
    while n % p == 0:
        n //= p
        r += 1
    return r


def run_case(p, h_coeffs, nmax, label):
    x = nmod_poly([0, 1], p)
    h = nmod_poly(h_coeffs, p)
    assert h[0] == 1 and h.degree() >= 1
    m0 = next(i for i in range(1, h.degree() + 1) if h[i])
    f = x * h**p
    d = f.degree()
    assert x * f.derivative() == f
    g = x
    first_return = {}
    primitive_weighted = {}
    rows = []
    for n in range(1, nmax + 1):
        g = f.compose(g)
        fixed = g - x
        unit, sf = fixed.factor_squarefree()
        rebuilt = nmod_poly([int(unit)], p)
        for factor, multiplicity in sf:
            rebuilt *= factor**multiplicity
        assert rebuilt == fixed
        old_divisors = [m for m in range(1, n) if n % m == 0]
        for m in old_divisors:
            for factor, initial_mult in first_return[m]:
                expected_mult = initial_mult * p**vp(n // m, p)
                divisor = factor**expected_mult
                quotient, remainder = divmod(fixed, divisor)
                assert remainder.is_zero()
                assert quotient.gcd(factor).degree() == 0
        current = []
        primitive_weighted[n] = 0
        for factor, multiplicity in sf:
            factor = factor // factor.gcd(x)
            if factor.degree() <= 0:
                continue
            assert multiplicity % p == 0
            for m in old_divisors:
                for old_factor, _ in first_return[m]:
                    factor //= factor.gcd(old_factor)
            if factor.degree() > 0:
                current.append((factor, int(multiplicity)))
                primitive_weighted[n] += factor.degree() * (multiplicity // p)
        first_return[n] = current
        w_exact = sum(primitive_weighted[m] for m in range(1, n + 1) if n % m == 0)
        r = vp(n, p)
        correction = sum(d ** (n // p**j) - 1 for j in range(1, r + 1))
        numerator = d**n - 1 - (p - 1) * correction
        assert numerator % p == 0
        w_formula = numerator // p - m0
        assert w_formula == w_exact
        zero_mult = next(i for i in range(1, fixed.degree() + 1) if fixed[i])
        assert zero_mult == 1 + m0 * p ** (r + 1)
        ordinary_nonzero = sum(factor.degree() for factor, _ in sf) - 1
        rows.append({
            "n": n,
            "fixed_scheme_length_A1": fixed.degree(),
            "squarefree_degree_multiplicity_pairs": [[factor.degree(), int(mult)] for factor, mult in sf],
            "ordinary_nonzero": ordinary_nonzero,
            "weighted_nonzero_exact": int(w_exact),
            "weighted_nonzero_formula": int(w_formula),
            "primitive_nonzero_degree_multiplicity_pairs": [[factor.degree(), mult] for factor, mult in current],
            "all_prior_return_multiplicity_checks": True,
        })
    return {"label": label, "p": p, "H_coefficients_ascending": h_coeffs,
            "d": d, "m0": m0, "nmax": nmax, "rows": rows}


if __name__ == "__main__":
    cases = [
        (3, [1, 1], 6, "nonaffine_degree_four"),
        (3, [1, 1, 1], 4, "quadratic_H"),
        (3, [1, 1, 1, 1], 3, "double_nonzero_fixed_root_H_minus_one"),
        (5, [1, 0, 1], 3, "origin_order_two"),
        (5, [1, 1, 1], 3, "characteristic_five_quadratic_H"),
    ]
    result = {"arithmetic": "exact F_p polynomials via python-flint",
              "flint_version": flint.__version__,
              "scope": "bounded checks, not an all-period proof",
              "cases": [run_case(*case) for case in cases]}
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
