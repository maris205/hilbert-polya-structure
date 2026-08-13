"""Exact polynomial Hénon dynamics and monodromy identities."""

from __future__ import annotations

import sympy as sp


def henon_map(x: sp.Expr, y: sp.Expr, parameter: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    """Return ``H_a(x,y)=(x^2-a-y,x)`` exactly."""

    return sp.expand(x**2 - parameter - y), x


def henon_inverse(x: sp.Expr, y: sp.Expr, parameter: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    """Return the exact polynomial inverse."""

    return y, sp.expand(y**2 - parameter - x)


def derivative_matrix(x: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[2 * x, -1], [1, 0]])


def dissipative_derivative(x: sp.Expr, delta: sp.Expr) -> sp.Matrix:
    """Derivative of ``J_(a,delta)(x,y)=(x^2-a-delta*y,x)``."""

    return sp.Matrix([[2 * x, -delta], [1, 0]])


def monodromy(coordinates: list[sp.Expr]) -> sp.Matrix:
    """Return ``A(x[n-1]) ... A(x[0])`` for one cyclic orbit."""

    result = sp.eye(2)
    for coordinate in coordinates:
        result = derivative_matrix(coordinate) * result
    return result.applyfunc(sp.expand)


def cyclic_shift(values: list[sp.Expr], offset: int = 1) -> list[sp.Expr]:
    offset %= len(values)
    return values[offset:] + values[:offset]


def recurrence_equations(period: int, parameter: sp.Expr) -> tuple[list[sp.Symbol], list[sp.Expr]]:
    """Build ``x[j+1]+x[j-1]-x[j]^2+a=0`` with cyclic indices."""

    if period < 1:
        raise ValueError("period must be positive")
    variables = list(sp.symbols(f"x0:{period}"))
    equations = []
    for index, variable in enumerate(variables):
        equations.append(
            sp.expand(
                variables[(index + 1) % period]
                + variables[(index - 1) % period]
                - variable**2
                + parameter
            )
        )
    return variables, equations


def trace_formula(coordinates: list[sp.Expr]) -> sp.Expr:
    return sp.expand(sp.trace(monodromy(coordinates)))


def characteristic_from_trace(trace: sp.Expr, multiplier: sp.Symbol) -> sp.Poly:
    return sp.Poly(multiplier**2 - trace * multiplier + 1, multiplier)

