import sympy as sp

from henon_audit.dynamics import (
    derivative_matrix,
    henon_inverse,
    henon_map,
    monodromy,
    recurrence_equations,
)


def test_polynomial_inverse_and_determinant():
    x, y, a = sp.symbols("x y a")
    assert henon_inverse(*henon_map(x, y, a), a) == (x, y)
    assert henon_map(*henon_inverse(x, y, a), a) == (x, y)
    assert derivative_matrix(x).det() == 1


def test_cyclic_recurrence_sign_convention():
    a = sp.Symbol("a")
    variables, equations = recurrence_equations(2, a)
    x0, x1 = variables
    assert equations == [a - x0**2 + 2 * x1, a + 2 * x0 - x1**2]


def test_monodromy_order_and_trace_are_cyclically_invariant():
    x0, x1, x2 = sp.symbols("x0 x1 x2")
    first = monodromy([x0, x1, x2])
    shifted = monodromy([x1, x2, x0])
    assert first.det() == 1
    assert sp.expand(sp.trace(first) - sp.trace(shifted)) == 0
    assert sp.trace(first) == 8 * x0 * x1 * x2 - 2 * x0 - 2 * x1 - 2 * x2

