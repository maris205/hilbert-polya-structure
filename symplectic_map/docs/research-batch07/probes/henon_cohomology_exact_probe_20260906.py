"""Finite exact checks, not a proof or a paper-acceptance certificate.

The rank checks use ordinary x,y monomials, independently of the orbit-word
normal-form argument. No floating point, fitted thresholds, or file writes.
Run with: python3 docs/research-batch07/probes/henon_cohomology_exact_probe_20260906.py
"""

from __future__ import annotations

import json

import sympy as sp


x, y = sp.symbols("x y")


def predicted_filtered_dimension(d: int, degree: int) -> int:
    # 1 + t(1+...+t^(d-2))/((1-t)(1-t^(d+1))).
    return 1 + sum(
        (grade - j - 1) // (d + 1) + 1
        for grade in range(1, degree + 1)
        for j in range(min(d - 1, grade))
    )


def ordinary_matrix_check(p: sp.Expr, degree: int, *, images=None, expected=None, label=None) -> dict:
    basis = [x**a * y**b for a in range(degree + 1) for b in range(degree - a + 1)]
    first, second = images if images is not None else (p - y, x)
    differences = [sp.Poly(f.subs({x: first, y: second}, simultaneous=True) - f, x, y) for f in basis]
    all_keys = sorted(set().union(*(poly.monoms() for poly in differences)))
    high_keys = [key for key in all_keys if sum(key) > degree]
    columns = [poly.as_dict() for poly in differences]
    full = sp.Matrix([[column.get(key, 0) for column in columns] for key in all_keys])
    high = (
        sp.Matrix([[column.get(key, 0) for column in columns] for key in high_keys])
        if high_keys
        else sp.zeros(0, len(basis))
    )
    # Admissible primitives have zero high-degree part. Delta has the same
    # kernel on that subspace as on the full degree-bounded input space.
    primitive_dimension = len(basis) - high.rank()
    invariant_dimension = len(basis) - full.rank()
    image_dimension = primitive_dimension - invariant_dimension
    observed = len(basis) - image_dimension
    if expected is None:
        expected = predicted_filtered_dimension(int(sp.degree(p, x)), degree)
    assert invariant_dimension == 1
    assert observed == expected, (p, degree, observed, expected)
    return {
        "p_or_word": label if label is not None else str(p),
        "degree": degree,
        "observed_filtered_quotient_dimension": observed,
        "expected": expected,
        "invariant_kernel_dimension": invariant_dimension,
    }


def multi_phase_checks() -> list[dict]:
    results = []
    for factors in ((x**2 + x + 1, x**2 - x + 2), (x**2 + x + 1, x**3 + x + 1)):
        degrees = [int(sp.degree(p, x)) for p in factors]
        delta = int(sp.prod(degrees))
        reversal = []
        for residue in range(delta):
            digits, rest = [0] * len(degrees), residue
            for phase in reversed(range(len(degrees))):
                digits[phase], rest = rest % degrees[phase], rest // degrees[phase]
            value, place = 0, 1
            for digit, radix in zip(digits, degrees):
                value += digit * place
                place *= radix
            reversal.append(value)
        assert sorted(reversal) == list(range(delta))
        first, second = x, y
        for p in factors:
            first, second = sp.expand(p.subs(x, first) - second), first
        for degree in range(1, 6):
            intersection_dimension = sum(
                a + delta * q + residue <= degree
                and delta * a + q + reversal[residue] <= degree
                for a in range(degree + 1)
                for q in range(degree // delta + 1)
                for residue in range(delta)
            )
            expected = (degree + 1) * (degree + 2) // 2 - intersection_dimension + 1
            results.append(ordinary_matrix_check(
                factors[0], degree, images=(first, second), expected=expected,
                label="; ".join(map(str, factors)),
            ))
    return results


def cyclic_sum_checks() -> list[dict]:
    results = []
    # These are literal finite-ring equalities. Different infinite-word
    # classes in the two sharpness examples are established in the proofs,
    # not inferred by this test.
    for length, phase_step, alphabet_degree, case in [
        (4, 1, 3, "unequal_endpoint_digits"),
        (3, 1, 2, "binary_short_fold"),
        (6, 2, 2, "macro_phase_alias"),
    ]:
        variables = sp.symbols(f"z0:{length}")
        if case == "unequal_endpoint_digits":
            g = variables[0] * variables[2] ** 2 - variables[0] ** 2 * variables[2]
        elif case == "binary_short_fold":
            g = variables[0] * variables[2] - variables[0] * variables[1]
        else:
            g = variables[0] * variables[3] - variables[1] * variables[4]
        norm = sum(
            g.xreplace({variables[i]: variables[(i + j * phase_step) % length] for i in range(length)})
            for j in range(length // phase_step)
        )
        assert sp.expand(norm) == 0
        assert all(max(sp.degree(g, variable), 0) < alphabet_degree for variable in variables)
        results.append({"case": case, "length": length, "phase_step": phase_step, "cyclic_sum_zero": True})

    # At a parabolic fixed point, geometric values are not the full scheme:
    # H=(x^2+2x-y,x), Fix(H) has coordinate algebra Q[x]/(x^2).
    parabolic_relations = sp.groebner([x**2 + x - y, x - y], y, x)
    remainder = parabolic_relations.reduce(x)[1]
    assert remainder == x
    assert parabolic_relations.reduce(x**2)[1] == 0
    results.append({"case": "parabolic_fixed_scheme", "x_is_nonzero_nilpotent": True})
    return results


def main() -> None:
    rank_checks = [
        ordinary_matrix_check(p, degree)
        for p in (x**2, x**2 + x + 1, x**3 - 2 * x**2 + x + 3)
        for degree in range(1, 9)
    ]
    print(json.dumps({"scalar_rank_checks": rank_checks, "multi_phase_rank_checks": multi_phase_checks(), "cyclic_checks": cyclic_sum_checks(), "status": "finite_exact_checks_passed"}, indent=2))


if __name__ == "__main__":
    main()
