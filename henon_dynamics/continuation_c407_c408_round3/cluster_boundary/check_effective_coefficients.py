"""Bounded exact checks of the NEW effective-potential derivation.

No old scripts or frozen artifacts are read or rerun.  This is not a census,
not an independent computation of the original cyclic local algebra, and
not a proof for untested parameters.  The all-parameter argument is written
in PROOF_PACKAGE.md.  The coordinator owns the independent original-algebra
local-standard-basis checks, so those are intentionally not duplicated here.
"""

import json

import sympy as sp


def potential(variables, k, degree, cycle=False):
    """Total-degree truncation of the displayed formal dilogarithm potential."""
    ans = 0
    edges = len(variables) if cycle else len(variables) - 1
    for j in range(edges):
        edge = variables[j] * variables[(j + 1) % len(variables)]
        for power in range(1, degree // 2 + 1):
            ans += edge**power / sp.Integer(power**2)
    for variable in variables:
        for power in range(1, degree // k + 1):
            ans -= (-variable**k) ** power / sp.Integer(power**2)
    return sp.expand(ans)


def valuation(expression, variable):
    polynomial = sp.Poly(sp.expand(expression), variable)
    if polynomial.is_zero:
        return None
    return min(monomial[0] for monomial, _ in polynomial.terms())


def path_check(k, r):
    length = 4 * r - 1
    z = sp.symbols(f"z0:{length}")
    a = sp.Symbol("a")
    p = potential(z, k, 2 * k)
    image = []
    for j in range(length):
        if j % 2 == 0:
            image.append((-1) ** (j // 2) * a)
        elif j % 4 == 1:
            image.append(-k * a ** (k - 1))
        else:
            image.append(sp.Integer(0))
    substitutions = dict(zip(z, image))
    effective_approximation = sp.expand(p.subs(substitutions, simultaneous=True))
    expected = -23 * r if k == 3 else sp.Rational(r * (k * k - 1), 2)
    actual = effective_approximation.coeff(a, 2 * k)
    assert valuation(effective_approximation, a) == 2 * k
    assert actual == expected
    residual_orders = [
        valuation(sp.diff(p, variable).subs(substitutions, simultaneous=True), a)
        for variable in z
    ]
    assert all(order is None or order >= k + 1 for order in residual_orders)
    return {
        "kind": "path",
        "k": k,
        "L": length,
        "leading_degree": 2 * k,
        "leading_coefficient": str(actual),
        "minimum_gradient_residual_order": min(
            order for order in residual_orders if order is not None
        ),
    }


def cycle_axis_check(k):
    z = sp.symbols("z0:4")
    a = sp.Symbol("a")
    c = -sp.Rational(k, 2) * a ** (k - 1)
    substitutions = dict(zip(z, [a, c, -a, c]))
    p = potential(z, k, 2 * k, cycle=True)
    effective_approximation = sp.expand(p.subs(substitutions, simultaneous=True))
    expected = -5 if k == 3 else sp.Rational(k * k - 2, 4)
    actual = effective_approximation.coeff(a, 2 * k)
    assert valuation(effective_approximation, a) == 2 * k
    assert actual == expected
    residual_orders = [
        valuation(sp.diff(p, variable).subs(substitutions, simultaneous=True), a)
        for variable in z
    ]
    assert all(order is None or order >= k + 1 for order in residual_orders)
    return {
        "kind": "cycle_axis",
        "k": k,
        "m": 4,
        "leading_degree": 2 * k,
        "leading_coefficient": str(actual),
        "minimum_gradient_residual_order": min(
            order for order in residual_orders if order is not None
        ),
    }


def cycle_quartic_check(k):
    z = sp.symbols("z0:4")
    a, b = sp.symbols("a b")
    s = -sp.Rational(k, 2) * b ** (k - 1)
    t = -sp.Rational(k, 2) * a ** (k - 1)
    substitutions = dict(zip(z, [a + s, b + t, -a + s, -b + t]))
    p = potential(z, k, 4, cycle=True)
    substituted = sp.Poly(p.subs(substitutions, simultaneous=True), a, b)
    quartic_terms = {
        exponents: coefficient
        for exponents, coefficient in substituted.terms()
        if sum(exponents) <= 4
    }
    expected = -8 if k == 3 else 1
    assert quartic_terms == {(2, 2): expected}
    return {"kind": "cycle_quartic", "k": k, "coefficient": str(expected)}


def combinatorial_check():
    """Symbolic-k labeled-run enumeration, independent of logarithm series."""
    k = sp.Symbol("k")
    companion = sp.Matrix(
        [[1, k - 1, 1, 2 * k], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
    )
    matrix_power = sp.eye(4)
    lengths = []

    def run_weight(length):
        if length % 2 == 0:
            return sp.Integer(1)
        return k - 1 if length % 4 == 1 else 2 * k - 1

    for m in range(1, 9):
        proper_sum = 0
        for bits in range((1 << m) - 1):
            start = next(j for j in range(m) if not bits & (1 << j))
            weight = 1
            run_length = 0
            for offset in range(1, m + 1):
                j = (start + offset) % m
                if bits & (1 << j):
                    run_length += 1
                elif run_length:
                    weight *= run_weight(run_length)
                    run_length = 0
            assert run_length == 0
            proper_sum += weight
        cycle_weight = 4 * k + 1 if m % 4 == 0 else 1
        matrix_power = matrix_power * companion
        proposed = sp.trace(matrix_power) + 1
        if m % 4 == 0:
            proposed += 4 * (k - 1)
        exact = sp.expand(proper_sum + cycle_weight)
        assert sp.expand(exact - proposed) == 0
        lengths.append({"m": m, "ell_m": str(exact)})
    return {"kind": "symbolic_k_run_enumeration", "lengths": lengths}


def main():
    rows = []
    for k in (3, 5, 7):
        for r in (1, 2, 3):
            rows.append(path_check(k, r))
        rows.append(cycle_axis_check(k))
        rows.append(cycle_quartic_check(k))
    rows.append(combinatorial_check())
    print(json.dumps({"status": "all_assertions_passed", "checks": rows}, indent=2))


if __name__ == "__main__":
    main()
