#!/usr/bin/env python3
"""Bounded exact rejection check, not an all-period theorem.

H(x,y) = (y, -x+y+1/y**2) over C.  Only periods 1 and 3 are used.
The period-three cyclic ideal has no zero coordinate, because each
equation becomes 1 when its own coordinate is zero.  Thus no saturation
or deletion of denominator-zero solutions is hidden in this check.
"""

import json
import platform
from collections import deque

import sympy as sp


def standard_monomials(groebner, variables):
    leading = [p.LM(order=groebner.order).exponents for p in groebner.polys]
    zero = (0,) * len(variables)
    queue = deque([zero])
    seen = {zero}
    basis = []
    while queue:
        exponent = queue.popleft()
        if any(all(a >= b for a, b in zip(exponent, lead)) for lead in leading):
            continue
        basis.append(exponent)
        for i in range(len(variables)):
            child = list(exponent)
            child[i] += 1
            child = tuple(child)
            if child not in seen:
                seen.add(child)
                queue.append(child)
        assert len(basis) <= 100, "This is only a bounded, zero-dimensional probe."
    return basis


def multiplication_matrix(expression, groebner, variables, basis):
    positions = {exponent: i for i, exponent in enumerate(basis)}
    matrix = sp.zeros(len(basis))
    for col, exponent in enumerate(basis):
        monomial = sp.prod(v**e for v, e in zip(variables, exponent))
        remainder = groebner.reduce(sp.expand(expression * monomial))[1]
        for exp, coefficient in sp.Poly(remainder, *variables).terms():
            if coefficient:
                matrix[positions[exp], col] = coefficient
    return matrix


def main():
    u, v, epsilon = sp.symbols("u v epsilon")
    order = 4

    def trunc(expression):
        return sp.series(expression, epsilon, 0, order + 1).removeO().expand()

    local_x, local_y = epsilon * u, epsilon * v
    for _ in range(3):
        local_x, local_y = (
            local_y,
            trunc(-local_x + local_y + (1 + local_y) ** -2 - 1),
        )
    displacements = [trunc(local_x - epsilon*u), trunc(local_y - epsilon*v)]
    quadratic = [sp.expand(d).coeff(epsilon, 2) for d in displacements]
    assert quadratic == [3*u**2 + 6*u*v, -6*u*v - 3*v**2]
    assert all(sp.expand(d).coeff(epsilon, 1) == 0 for d in displacements)
    # The two leading homogeneous quadratics have no common projective root.
    assert sp.gcd(quadratic[0], quadratic[1]) == 3
    assert all(sp.total_degree(q) == 2 for q in quadratic)

    derivative = sp.Matrix([[0, 1], [-1, -1]])
    assert derivative**3 == sp.eye(2)
    assert derivative != sp.eye(2)

    x0, x1, x2 = variables = sp.symbols("x0 x1 x2")
    cyclic_equations = [
        variables[i]**3
        - (variables[(i-1) % 3] + variables[(i+1) % 3]) * variables[i]**2
        + 1
        for i in range(3)
    ]
    groebner = sp.groebner(cyclic_equations, *variables, order="lex", domain=sp.QQ)
    assert groebner.is_zero_dimensional
    basis = standard_monomials(groebner, variables)
    separator = x0 + 2*x1 + 4*x2
    m_separator = multiplication_matrix(separator, groebner, variables, basis)
    z = sp.Symbol("z")
    charpoly = sp.Poly(m_separator.charpoly(z).as_expr(), z)
    squarefree = charpoly.sqf_part()
    assert len(basis) == 18
    assert squarefree.degree() == 9
    assert sp.expand(charpoly.as_expr() - (z**3 - 343)**4 * (4*z**6 + 40*z**3 + 343)/4) == 0

    # A second algebraic check on the distinct-point classification.
    t, s = sp.symbols("t s")
    equal_pair_equations = [sp.expand(f.subs({x0:t, x1:t, x2:s})) for f in cyclic_equations]
    assert equal_pair_equations[0] == 1-s*t**2
    assert sp.factor(equal_pair_equations[2].subs(s, 1/t**2)) == (t-1)**2*(t**2+t+1)**2/t**6
    # Three pairwise distinct coordinates force sum zero and sum of pairwise
    # products zero, then every coordinate has cube -1/2.  The following
    # remainders verify that all six permutations actually solve the equations.
    distinct_ideal = sp.groebner(
        [x0+x1+x2, x0*x1+x1*x2+x2*x0, x0*x1*x2+sp.Rational(1,2)],
        *variables, order="lex", domain=sp.QQ,
    )
    assert all(distinct_ideal.reduce(f)[1] == 0 for f in cyclic_equations)
    distinct_basis = standard_monomials(distinct_ideal, variables)
    assert len(distinct_basis) == 6

    result = {
        "status": "PASS_BOUNDED_REJECTION_PROBE",
        "scope": "H_1 only, periods 1 and 3 only; no all-period claim",
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "map": "H(x,y)=(y,-x+y+1/y^2)",
        "fixed_points": "(t,t), t^3=1; all 3 are simple for H",
        "fixed_point_derivative": str(derivative),
        "fixed_point_derivative_cube": str(derivative**3),
        "H_cubed_minus_identity_quadratic_at_1_1": [str(q) for q in quadratic],
        "quadratic_gcd": str(sp.gcd(*quadratic)),
        "isolated_local_intersection_multiplicity_each_fixed_point_for_H_cubed": 4,
        "period3_cyclic_ideal_length": len(basis),
        "separator": str(separator),
        "separator_characteristic_polynomial": str(sp.factor(charpoly.as_expr())),
        "separator_squarefree_degree": squarefree.degree(),
        "period3_distinct_points": 9,
        "period3_decomposition": "3 old fixed points of multiplicity 4; 6 new points, each simple",
        "exact_period3_orbits": 2,
        "conclusion": "Ordinary distinct-point count 9 differs from scheme length 18; a Picard/local-index formula cannot silently identify them.",
        "assertions_passed": True,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
