#!/usr/bin/env python3
"""Bounded exact scouts; stdout only, no reads from historical payloads.

Compare a proposed period-independent edge matrix with Groebner normal-form
global residues of the literal cyclic Hénon equations. Finite checks are not
the proof of the all-period assertion. Also reconstruct a historical n=2
counterexample from the declared map, without modifying that package.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import product
import json
import platform
import sympy as sp

x, t, z = sp.symbols("x t z")


def edge_matrix(p, q, a):
    d = sp.degree(p, x)
    m = sp.degree(q, x) if q != 0 else -1
    surplus = max(0, m - d + 1)
    bound = int(sp.floor(sp.Rational(surplus * (d + 1), (d - 1) ** 2)))
    states = list(product(range(bound + 1), repeat=2))
    p_rev = sp.expand(t ** d * p.subs(x, 1 / t))
    max_order = max(0, m + 2 * bound - d + 1)

    @lru_cache(None)
    def local(incoming, outgoing):
        max_k = m + incoming - d * (outgoing + 1) + 1
        if max_k < 0:
            return sp.S.Zero
        rev_power = sp.Poly(
            sp.series(p_rev ** (-outgoing - 1), t, 0, max_order + 1).removeO(), t
        )
        return sp.expand(sum(
            coeff * rev_power.nth(j + incoming - d * (outgoing + 1) + 1)
            for (j,), coeff in sp.Poly(q, x).terms()
            if j + incoming - d * (outgoing + 1) + 1 >= 0
        ))

    matrix = sp.zeros(len(states))
    for i, (r, ell) in enumerate(states):
        for j, (s, v) in enumerate(states):
            matrix[i, j] = sp.binomial(ell + s, ell) * a ** ell * local(r + v, ell + s)
    # This is trace-preserving pruning, not a claim of minimal realization.
    live = set(range(len(states)))
    while True:
        nxt = {i for i in live if any(matrix[i, j] for j in live)
               and any(matrix[j, i] for j in live)}
        if nxt == live:
            break
        live = nxt
    kept = sorted(live)
    reduced = matrix.extract(kept, kept)
    return bound, len(states), [states[i] for i in kept], reduced


def cyclic_system(p, a, n):
    variables = sp.symbols(f"u0:{n}")
    equations = [sp.expand(p.subs(x, variables[i])
                          - variables[(i + 1) % n]
                          - a * variables[(i - 1) % n]) for i in range(n)]
    return variables, equations


def normal_form_residue(p, q, a, n):
    variables, equations = cyclic_system(p, a, n)
    basis = sp.groebner(equations, *variables, order="grlex")
    numerator = sp.prod(q.subs(x, u) for u in variables)
    _, remainder = basis.reduce(sp.expand(numerator))
    return sp.Poly(remainder, *variables).coeff_monomial(
        sp.prod(u ** (sp.degree(p, x) - 1) for u in variables))


def monodromy_sign_check(n):
    a = sp.symbols("a")
    v = sp.symbols(f"v0:{n}")
    cyclic_jac = sp.zeros(n)
    mono = sp.eye(2)
    for i in range(n):
        cyclic_jac[i, i] += v[i]
        cyclic_jac[i, (i + 1) % n] -= 1
        cyclic_jac[i, (i - 1) % n] -= a
        mono = sp.Matrix([[v[i], -a], [1, 0]]) * mono
    difference = sp.expand(cyclic_jac.det() + (sp.eye(2) - mono).det())
    assert difference == 0, (n, difference)
    return {"n": n, "det_cyclic_plus_det_return": str(difference)}


def quotient_weighted_sum(p, q, a, n):
    """Algebraic sum via Tr(m_g m_J^{-1}), not top-coefficient residue."""
    variables, equations = cyclic_system(p, a, n)
    d = sp.degree(p, x)
    basis = sp.groebner(equations, *variables, order="grlex")
    exponents = list(product(range(d), repeat=n))
    monomials = [sp.prod(v ** k for v, k in zip(variables, ex)) for ex in exponents]

    def multiplication(poly):
        columns = []
        for monomial in monomials:
            reduced = sp.Poly(basis.reduce(sp.expand(poly * monomial))[1], *variables)
            columns.append(sp.Matrix([reduced.coeff_monomial(ex) for ex in exponents]))
        return sp.Matrix.hstack(*columns)

    jac = sp.Matrix(equations).jacobian(variables).det()
    numerator = sp.prod(q.subs(x, variable) for variable in variables)
    jac_matrix = multiplication(jac)
    assert jac_matrix.det() != 0  # All roots in this finite case are simple.
    residue_sum = sp.trace(multiplication(numerator) * jac_matrix.inv())
    assert residue_sum == normal_form_residue(p, q, a, n)
    return {"n": n, "quotient_dimension": len(monomials),
            "trace_m_g_times_inverse_m_J": str(residue_sum),
            "negative_literal_stability_trace": str(residue_sum)}


def symbolic_quadratic_weight():
    a, b, c, u, v, w = sp.symbols("a b c u v w")
    _, _, states, matrix = edge_matrix(x ** 2 + b * x + c, u * x ** 2 + v * x + w, a)
    determinant = sp.factor((sp.eye(matrix.rows) - z * matrix).det())
    expected = (1 - u * z) * (1 - a * u * z) * (1 - (v - b * u) * z - a * u ** 2 * z ** 2)
    assert sp.expand(determinant - expected) == 0
    return {"p": "x^2+b*x+c", "q": "u*x^2+v*x+w", "a": "a",
            "states": states, "matrix": str(matrix),
            "determinant": str(determinant),
            "expected_factorization": str(expected), "symbolic_difference": "0"}


def historical_literal_map_check():
    a = sp.Rational(1, 4)
    b = 1 + a
    omega = (-1 + sp.sqrt(3) * sp.I) / 2
    points = [(0, 0), (b, b), (b * omega, b * omega ** 2),
              (b * omega ** 2, b * omega)]

    def f(v):
        zz, ww = v
        return sp.Matrix([ww, ww ** 2 - a * zz])

    def jac(v):
        return sp.Matrix([[0, 1], [-a, 2 * v[1]]])

    weights = []
    for point in points:
        point = sp.Matrix(point)
        residual = (f(f(point)) - point).applyfunc(sp.simplify)
        assert residual == sp.zeros(2, 1)
        denominator = sp.simplify((sp.eye(2) - jac(f(point)) * jac(point)).det())
        weights.append(sp.simplify(1 / denominator))
    assert sum(weights) == 0
    bad = sp.Matrix([(-3 - sp.sqrt(39) * sp.I) / 8,
                     (-3 + sp.sqrt(39) * sp.I) / 8])
    bad_residual = (f(f(bad)) - bad).applyfunc(sp.simplify)
    assert bad_residual != sp.zeros(2, 1)
    return {
        "declared_map": "F(z,w)=(w,w^2-z/4)",
        "correct_period_two_equations": ["w^2-(5/4)z=0", "z^2-(5/4)w=0"],
        "correct_elimination_polynomial_monic": "z^4-(125/64)z",
        "literal_return_fixed_points": 4,
        "literal_return_weights": list(map(str, weights)),
        "literal_return_trace": "0",
        "historical_claimed_trace": "-1664/1725",
        "historical_nonfixed_point_return_residual": list(map(str, bad_residual)),
        "historical_files_read_by_this_script": [],
    }


def main():
    cases = [
        ("quadratic_constant", x ** 2 + 1, sp.S.One, sp.Rational(1, 4), 4),
        ("quadratic_threshold", x ** 2 - x + 2, 2 * x + 3, sp.Rational(2, 3), 4),
        ("quadratic_superthreshold", x ** 2 - x + 2, x ** 2 + x + 1, sp.Rational(2, 3), 5),
        ("cubic_superthreshold", x ** 3 + x + 1, x ** 3 + 2 * x + 1, sp.Rational(-1, 2), 4),
        ("cubic_nondegenerate_weight", x ** 3 + x + 1, x ** 4 + x ** 2 + 1, sp.Rational(-1, 2), 3),
        ("quartic_threshold", x ** 4 - x ** 2 + 1, x ** 3 + x, sp.Rational(3, 2), 3),
        ("parabolic_period_one", x ** 2 + 1, x ** 2 + x + 1, sp.S.One, 4),
    ]
    rows = []
    comparisons = 0
    for name, p, q, a, nmax in cases:
        bound, raw_dimension, states, matrix = edge_matrix(p, q, a)
        power = sp.eye(matrix.rows)
        checks = []
        for n in range(1, nmax + 1):
            power = power * matrix
            tr = sp.simplify(sp.trace(power))
            residue = normal_form_residue(p, q, a, n)
            assert tr == residue, (name, n, tr, residue)
            comparisons += 1
            checks.append({"n": n, "edge_matrix_trace": str(tr),
                           "cyclic_normal_form_residue": str(residue)})
        denominator = sp.factor((sp.eye(matrix.rows) - z * matrix).det())
        rows.append({"name": name, "p": str(p), "q": str(q), "a": str(a),
                     "flow_bound": bound, "raw_edge_dimension": raw_dimension,
                     "trimmed_edge_dimension": matrix.rows,
                     "trimmed_states": states,
                     "det_I_minus_z_W": str(denominator), "comparisons": checks})
    output = {
        "scope": "EXACT_FINITE_SCOUT_NOT_ALL_PERIOD_PROOF",
        "environment": {"python": platform.python_version(), "sympy": sp.__version__},
        "matrix_vs_normal_form_comparisons": comparisons,
        "cases": rows,
        "symbolic_quadratic_weight": symbolic_quadratic_weight(),
        "independent_quotient_weight_sums": [
            quotient_weighted_sum(x ** 2 - x + 2, x ** 2 + x + 1, sp.Rational(2, 3), n)
            for n in (2, 3)
        ],
        "indeterminate_monodromy_sign_checks": [monodromy_sign_check(n) for n in range(1, 7)],
        "historical_literal_map_counterexample": historical_literal_map_check(),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
