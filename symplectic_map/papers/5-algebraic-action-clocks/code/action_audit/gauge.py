"""Exact gauge-telescoping identities with an explicit endpoint ledger."""

from __future__ import annotations

from typing import Any, Iterable

import sympy as sp


def _exact(value: sp.Expr | int | str) -> sp.Expr:
    expression = sp.sympify(value)
    if expression.has(sp.Float):
        raise ValueError("floating values are forbidden in the exact gauge audit")
    return expression


def gauge_shift_record(
    *,
    base_action: sp.Expr | int | str,
    gauge_values: Iterable[sp.Expr | int | str],
    constants: Iterable[sp.Expr | int | str],
    values_declared_algebraic: bool,
) -> dict[str, Any]:
    """Evaluate a finite formal telescope and retain the endpoint term.

    ``gauge_values`` contains ``chi_0(P_0),...,chi_n(P_n)`` and therefore
    has one more entry than ``constants``.
    """

    base = _exact(base_action)
    chis = [_exact(value) for value in gauge_values]
    constants_exact = [_exact(value) for value in constants]
    if len(chis) != len(constants_exact) + 1:
        raise ValueError("gauge_values must have length len(constants)+1")

    step_shifts = [chis[index + 1] - chis[index] + constants_exact[index] for index in range(len(constants_exact))]
    direct_shift = sp.expand(sum(step_shifts, sp.Integer(0)))
    endpoint_mismatch = sp.expand(chis[-1] - chis[0])
    constant_sum = sp.expand(sum(constants_exact, sp.Integer(0)))
    predicted_shift = sp.expand(endpoint_mismatch + constant_sum)
    shifted_action = sp.expand(base + direct_shift)
    compatible = endpoint_mismatch == 0
    classification = (
        "COMPATIBLE_ENDPOINT_GAUGE_SHIFT"
        if compatible
        else "ALGEBRAIC_ENDPOINT_MISMATCH_RETAINED"
    )
    if not values_declared_algebraic:
        classification = "STOP_UNCERTIFIED_OR_TRANSCENDENTAL_GAUGE_DATA"

    return {
        "period": len(constants_exact),
        "base_action": sp.sstr(base),
        "gauge_values": [sp.sstr(value) for value in chis],
        "constants": [sp.sstr(value) for value in constants_exact],
        "step_shifts": [sp.sstr(value) for value in step_shifts],
        "direct_shift": sp.sstr(direct_shift),
        "endpoint_mismatch": sp.sstr(endpoint_mismatch),
        "constant_sum": sp.sstr(constant_sum),
        "predicted_shift": sp.sstr(predicted_shift),
        "shifted_action": sp.sstr(shifted_action),
        "endpoint_compatible": compatible,
        "short_sum_constants_formula_allowed": compatible,
        "values_declared_algebraic": values_declared_algebraic,
        "classification": classification,
        "pass": direct_shift == predicted_shift and values_declared_algebraic,
    }


def symbolic_telescoping_audit(period: int) -> dict[str, Any]:
    """Verify the general endpoint formula for a symbolic period."""

    if period < 1:
        raise ValueError("period must be positive")
    chis = sp.symbols(f"chi_0:{period + 1}")
    constants = sp.symbols(f"C_0:{period}")
    direct = sp.expand(
        sum(
            (chis[index + 1] - chis[index] + constants[index]
             for index in range(period)),
            sp.Integer(0),
        )
    )
    expected = sp.expand(chis[-1] - chis[0] + sum(constants, sp.Integer(0)))
    compatible_specialization = sp.simplify(direct.subs(chis[-1], chis[0]))
    expected_compatible = sp.expand(sum(constants, sp.Integer(0)))
    return {
        "period": period,
        "direct_sum": sp.sstr(direct),
        "general_endpoint_formula": sp.sstr(expected),
        "general_residual": sp.sstr(sp.expand(direct - expected)),
        "compatible_endpoint_specialization": sp.sstr(compatible_specialization),
        "compatible_residual": sp.sstr(sp.expand(compatible_specialization - expected_compatible)),
        "pass": sp.expand(direct - expected) == 0 and sp.expand(compatible_specialization - expected_compatible) == 0,
    }
