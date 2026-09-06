#!/usr/bin/env python3
"""Bounded geometric counts; square-free blocks retain multiplicity evidence.

No output files are written by this script. Counts are over algebraic closures,
not finite extensions. The finite horizon does not prove a zeta theorem.
"""

import json
import platform
import flint
from flint import nmod_poly


def decomposition(poly):
    unit, factors = poly.factor_squarefree()
    check = nmod_poly([int(unit)], poly.modulus())
    blocks = []
    for factor, multiplicity in factors:
        assert factor.gcd(factor.derivative()).degree() == 0
        check *= factor ** multiplicity
        blocks.append({"degree": factor.degree(), "multiplicity": multiplicity})
    assert check == poly
    return sum(block["degree"] for block in blocks), sorted(blocks, key=lambda b: b["multiplicity"])


def polynomial_probe(p, coeffs, maximum):
    x = nmod_poly([0, 1], p)
    f = nmod_poly(coeffs, p)
    iterate = x
    rows = []
    for n in range(1, maximum + 1):
        iterate = f.compose(iterate)
        displacement = iterate - x
        count, blocks = decomposition(displacement)
        zero_multiplicity = next(i for i, c in enumerate(displacement) if c)
        rows.append({"n": n, "scheme_length_affine": displacement.degree(),
                     "geometric_count_affine": count, "zero_multiplicity": zero_multiplicity,
                     "squarefree_blocks": blocks})
    return rows


def rational_probe(maximum):
    p = 2
    x = nmod_poly([0, 1], p)
    numerator = x
    denominator = nmod_poly([1], p)
    rows = []
    for n in range(1, maximum + 1):
        numerator, denominator = numerator**3 + denominator**3, numerator**2 * denominator
        assert numerator.gcd(denominator).degree() == 0
        displacement = numerator - x * denominator
        count, blocks = decomposition(displacement)
        infinity_multiplicity = 3**n + 1 - displacement.degree()
        assert infinity_multiplicity > 0
        rows.append({"n": n, "scheme_length_projective": 3**n + 1,
                     "geometric_count_projective": count + 1,
                     "infinity_multiplicity": infinity_multiplicity,
                     "finite_squarefree_blocks": blocks})
    return rows


def multiplicity(poly, factor):
    value = 0
    while poly % factor == 0:
        poly //= factor
        value += 1
    return value


def witness(p, coeffs, n, factor_coeffs, expected_multiplicity):
    x = nmod_poly([0, 1], p)
    f = nmod_poly(coeffs, p)
    q = nmod_poly(factor_coeffs, p)
    assert q.gcd(q.derivative()).degree() == 0
    iterate = x
    divisor_gcds = {}
    for k in range(1, n + 1):
        iterate = f.compose(iterate)
        if n % k == 0 and k < n:
            divisor_gcds[str(k)] = q.gcd(iterate - x).degree()
    actual_multiplicity = multiplicity(iterate - x, q)
    assert actual_multiplicity == expected_multiplicity
    assert q.gcd((iterate - x) // (q ** actual_multiplicity)).degree() == 0
    assert all(value == 0 for value in divisor_gcds.values())
    return {"p": p, "period": n, "factor": str(q), "degree": q.degree(),
            "exact_multiplicity": actual_multiplicity,
            "proper_divisor_gcd_degrees": divisor_gcds,
            "factor_squarefree": True}


def main():
    results = {"scope": "finite exact probe; no all-period inference",
               "python": platform.python_version(), "python_flint": flint.__version__,
               "f1_F3_x_plus_x6": polynomial_probe(3, [0, 1, 0, 0, 0, 0, 1], 6),
               "f2_F2_x_plus_inverse_square": rational_probe(8),
               "f3_F2_x3_plus_x2": polynomial_probe(2, [0, 0, 1, 1], 9),
               "new_period_witnesses": [
                   witness(3, [0, 1, 0, 0, 0, 0, 1], 4,
                           [2, 1, 0, 0, 1], 6),
                   witness(3, [0, 1, 0, 0, 0, 0, 1], 5,
                           [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
                            0, 0, 0, 0, 2, 0, 0, 0, 0, 1], 6),
                   witness(2, [0, 0, 1, 1], 5, [1, 0, 0, 1, 0, 1], 3),
                   witness(2, [0, 0, 1, 1], 7, [1, 0, 1, 0, 0, 1, 1, 1], 2)]}
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
