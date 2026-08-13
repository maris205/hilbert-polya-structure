"""Static exact identities for the Hénon specialization.

No function in this module solves a periodic-point equation or substitutes
the inherited candidate parameter.
"""

from __future__ import annotations

from typing import Any, Iterable

import sympy as sp


def henon_static_identity_audit() -> dict[str, Any]:
    """Verify the one-form, type-1, graph-sign, and inverse identities."""

    q, p, a, Q, P = sp.symbols("q p a Q P")
    q_image = q**2 - a - p
    p_image = q
    potential = sp.Rational(2, 3) * q**3 - p * q
    lagrangian = sp.Rational(1, 3) * q**3 - a * q - q * Q

    pullback_minus_theta = sp.Matrix([2 * q**2 - p, -q])
    d_potential = sp.Matrix([sp.diff(potential, q), sp.diff(potential, p)])
    one_form_residual = (pullback_minus_theta - d_potential).applyfunc(sp.expand)
    type1_q_residual = sp.expand(sp.diff(lagrangian, q).subs(Q, q_image) - p)
    type1_Q_residual = sp.expand((-sp.diff(lagrangian, Q)).subs(P, p_image) - p_image)
    graph_sign_residual = sp.expand((lagrangian + potential).subs(Q, q_image))

    inverse_q, inverse_p = p, p**2 - a - q
    inverse_after_forward = (
        sp.expand(p_image),
        sp.expand(p_image**2 - a - q_image),
    )
    forward_after_inverse = (
        sp.expand(inverse_q**2 - a - inverse_p),
        sp.expand(inverse_q),
    )
    jacobian = sp.Matrix([[2 * q, -1], [1, 0]])

    residuals = {
        "one_form_dq": sp.sstr(one_form_residual[0]),
        "one_form_dp": sp.sstr(one_form_residual[1]),
        "type1_partial_q": sp.sstr(type1_q_residual),
        "type1_minus_partial_Q": sp.sstr(type1_Q_residual),
        "graph_L_plus_G": sp.sstr(graph_sign_residual),
    }
    return {
        "run_id": "R020",
        "map": [sp.sstr(q_image), sp.sstr(p_image)],
        "inverse": [sp.sstr(inverse_q), sp.sstr(inverse_p)],
        "inverse_after_forward": [sp.sstr(value) for value in inverse_after_forward],
        "forward_after_inverse": [sp.sstr(value) for value in forward_after_inverse],
        "potential": sp.sstr(potential),
        "type1_generating_function": sp.sstr(lagrangian),
        "jacobian": [[sp.sstr(value) for value in row] for row in jacobian.tolist()],
        "jacobian_determinant": sp.sstr(jacobian.det()),
        "residuals": residuals,
        "candidate_parameter_substituted": False,
        "periodic_equation_solved": False,
        "pass": (
            one_form_residual == sp.zeros(2, 1)
            and type1_q_residual == 0
            and type1_Q_residual == 0
            and graph_sign_residual == 0
            and inverse_after_forward == (q, p)
            and forward_after_inverse == (q, p)
            and jacobian.det() == 1
        ),
    }


def _cyclic_recurrence_polynomials(period: int) -> tuple[tuple[sp.Symbol, ...], list[sp.Expr]]:
    if period < 1:
        raise ValueError("period must be positive")
    a = sp.Symbol("a")
    coordinates = sp.symbols(f"q_0:{period}")
    equations = [
        sp.expand(
            coordinates[index] ** 2
            - a
            - coordinates[(index + 1) % period]
            - coordinates[(index - 1) % period]
        )
        for index in range(period)
    ]
    return coordinates, equations


def recurrence_multiplicity_audit() -> dict[str, Any]:
    """Verify that periods one and two retain two neighbor slots."""

    q1, equations_1 = _cyclic_recurrence_polynomials(1)
    q2, equations_2 = _cyclic_recurrence_polynomials(2)
    q5, equations_5 = _cyclic_recurrence_polynomials(5)
    a = sp.Symbol("a")
    expected_1 = q1[0] ** 2 - a - 2 * q1[0]
    expected_2 = [
        q2[0] ** 2 - a - 2 * q2[1],
        q2[1] ** 2 - a - 2 * q2[0],
    ]
    checks = {
        "period_1_two_neighbor_slots": sp.expand(equations_1[0] - expected_1) == 0,
        "period_2_first_two_neighbor_slots": sp.expand(equations_2[0] - expected_2[0]) == 0,
        "period_2_second_two_neighbor_slots": sp.expand(equations_2[1] - expected_2[1]) == 0,
        "period_5_distinct_neighbors": equations_5[0].has(q5[1]) and equations_5[0].has(q5[4]),
    }
    return {
        "run_id": "R021",
        "period_1_equation": sp.sstr(equations_1[0]),
        "period_2_equations": [sp.sstr(value) for value in equations_2],
        "period_5_first_equation": sp.sstr(equations_5[0]),
        "neighbor_semantics": "ordered cyclic argument slots; equal values are counted twice",
        "checks": checks,
        "candidate_parameter_substituted": False,
        "periodic_equation_solved": False,
        "pass": all(checks.values()),
    }


def projective_infinity_audit(periods: Iterable[int] = (1, 2, 3, 5)) -> dict[str, Any]:
    """Audit only the leading homogeneous system at infinity."""

    records: list[dict[str, Any]] = []
    for period in periods:
        if period < 1:
            raise ValueError("period must be positive")
        a, z = sp.symbols("a Z")
        coordinates = sp.symbols(f"Q_0:{period}")
        homogeneous = [
            sp.expand(
                coordinates[index] ** 2
                - z * coordinates[(index + 1) % period]
                - z * coordinates[(index - 1) % period]
                - a * z**2
            )
            for index in range(period)
        ]
        infinity = [sp.expand(value.subs(z, 0)) for value in homogeneous]
        forced_squares = infinity == [value**2 for value in coordinates]
        records.append(
            {
                "period": period,
                "homogeneous_equations": [sp.sstr(value) for value in homogeneous],
                "at_infinity": [sp.sstr(value) for value in infinity],
                "all_projective_coordinates_forced_zero": forced_squares,
                "projective_point_at_infinity_exists": False if forced_squares else None,
                "pass": forced_squares,
            }
        )
    return {
        "run_id": "R022",
        "records": records,
        "dimension_inference": "a positive-dimensional projective component would meet Z=0; the audited leading system has no projective point there",
        "proof_not_orbit_enumeration": True,
        "candidate_parameter_substituted": False,
        "periodic_equation_solved": False,
        "pass": all(record["pass"] for record in records),
    }


def s_integral_denominator_ledger() -> dict[str, Any]:
    """Record the orbit-field valuation proof and the exact denominator."""

    q, p = sp.symbols("q p")
    potential = sp.Rational(2, 3) * q**3 - p * q
    three_potential = sp.expand(3 * potential)
    sharp_q = sp.Integer(1)
    sharp_p = sp.Integer(1)
    sharp_a = sp.Integer(-1)
    fixed_residual = sp.expand(sharp_q**2 - sharp_a - 2 * sharp_q)
    sharp_action = sp.expand(potential.subs({q: sharp_q, p: sharp_p}))
    return {
        "run_id": "R023",
        "base_field": "K0 contains a",
        "base_integrality": "a in O_(K0,S0)",
        "orbit_field": "finite K/K0 containing every orbit coordinate",
        "extended_places": "S is the set of places of K above S0, including archimedean places",
        "valuation_contradiction": {
            "assumption": "R=max_j |q_j|_v > 1 at v outside S",
            "left_side": "|q_j^2-a|_v=R^2",
            "recurrence_bound": "|q_(j+1)+q_(j-1)|_v<=R",
            "conclusion": "R^2<=R contradicts R>1",
        },
        "three_times_potential": sp.sstr(three_potential),
        "denominator_support": [3],
        "claim": "3*A_G lies in O_(K,S); A_G is integral outside S and places above 3",
        "sharpness_control": {
            "parameter": sp.sstr(sharp_a),
            "fixed_point": [sp.sstr(sharp_q), sp.sstr(sharp_p)],
            "fixed_recurrence_residual": sp.sstr(fixed_residual),
            "action": sp.sstr(sharp_action),
            "three_times_action": sp.sstr(3 * sharp_action),
            "shows_A_need_not_be_integral_away_from_3": sharp_action == -sp.Rational(1, 3),
        },
        "candidate_parameter_substituted": False,
        "pass": (
            three_potential == 2 * q**3 - 3 * p * q
            and fixed_residual == 0
            and sharp_action == -sp.Rational(1, 3)
        ),
    }
