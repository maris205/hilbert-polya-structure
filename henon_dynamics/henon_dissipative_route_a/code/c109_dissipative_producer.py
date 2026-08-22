#!/usr/bin/env python3
"""Produce the exact C109 dissipative Hénon low-period witness ledger.

The ledger is deliberately finite.  It records the two rational fixed points,
the genuine rational two-cycle, their Jacobians, and a four-state weighted
cycle graph.  The latter is a discrete transfer *witness* only; it is not
asserted to be a complete coding of the real Hénon map.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "results/c109_dissipative_evidence.json"
x, y, z = sp.symbols("x y z")
a = sp.Rational(-91, 16)
b = sp.Rational(1, 2)


def s(value: object) -> str:
    """Canonical compact SymPy string for JSON."""
    return sp.sstr(sp.factor(sp.sympify(value)))


def matrix_strings(m: sp.Matrix) -> list[list[str]]:
    return [[s(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def main() -> None:
    # F(x,y)=(x^2+a-y,bx), with |b|<1, so area is contracted by 1/2.
    X = sp.expand(x**2 + a - y)
    Y = sp.expand(b * x)
    X2 = sp.expand(X**2 + a - Y)
    Y2 = sp.expand(b * X)
    J = sp.Matrix([[2 * x, -1], [b, 0]])

    fixed_points = [
        (sp.Rational(13, 4), sp.Rational(13, 8)),
        (sp.Rational(-7, 4), sp.Rational(-7, 8)),
    ]
    two_cycle = [
        (sp.Rational(5, 4), sp.Rational(-11, 8)),
        (sp.Rational(-11, 4), sp.Rational(5, 8)),
    ]
    all_f2 = fixed_points + two_cycle

    fixed_poly = sp.factor((X - x).subs(y, b * x))
    resultant = sp.factor(sp.resultant(X2 - x, Y2 - y, y))
    dynatomic_two = sp.factor(resultant / ((4 * x - 13) * (4 * x + 7) / 256))

    cycles = []
    for name, point in [
        ("p_plus", fixed_points[0]),
        ("p_minus", fixed_points[1]),
        ("q_plus", two_cycle[0]),
        ("q_minus", two_cycle[1]),
    ]:
        px, py = point
        jac = J.subs({x: px, y: py})
        denominator = sp.factor((sp.eye(2) - jac).det())
        cycles.append(
            {
                "name": name,
                "point": [s(px), s(py)],
                "jacobian": matrix_strings(jac),
                "jacobian_trace": s(sp.trace(jac)),
                "jacobian_determinant": s(jac.det()),
                "local_denominator_det_I_minus_DF": s(denominator),
                "local_weight": s(1 / denominator),
            }
        )

    # The exact F-transition on these four known points.
    transition = {"p_plus": "p_plus", "p_minus": "p_minus", "q_plus": "q_minus", "q_minus": "q_plus"}
    weights = {item["name"]: sp.sympify(item["local_weight"]) for item in cycles}
    order = ["p_plus", "p_minus", "q_plus", "q_minus"]
    M = sp.zeros(4)
    for i, name in enumerate(order):
        j = order.index(transition[name])
        M[i, j] = weights[name]
    traces = {str(n): s(sp.trace(M**n)) for n in range(1, 7)}
    det_poly = sp.Poly(sp.expand((sp.eye(4) - z * M).det()), z)
    det_coefficients = {str(k): s(det_poly.nth(k)) for k in range(det_poly.degree() + 1)}

    # F^2 monodromies are recorded for the primitive two-cycle and all F^2
    # fixed witnesses, which makes the dissipative multiplier visible.
    monodromy = []
    for name, point in [("q_plus", two_cycle[0]), ("q_minus", two_cycle[1])]:
        px, py = point
        image_x = sp.expand(X.subs({x: px, y: py}))
        m = sp.simplify(J.subs({x: image_x}) * J.subs({x: px}))
        monodromy.append(
            {
                "name": name,
                "DF2": matrix_strings(m),
                "trace": s(sp.trace(m)),
                "determinant": s(m.det()),
                "det_I_minus_DF2": s((sp.eye(2) - m).det()),
            }
        )

    payload = {
        "schema": "hcs-c109-dissipative-henon-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "map": {
            "formula": "F(x,y)=(x^2-(91/16)-y,x/2)",
            "a": s(a),
            "b": s(b),
            "jacobian_determinant": s(b),
            "dissipative_certificate": "abs(det DF)=1/2<1",
        },
        "fixed_point_polynomial": s(fixed_poly),
        "fixed_points": [[s(px), s(py)] for px, py in fixed_points],
        "period_two_resultant": s(resultant),
        "primitive_period_two_factor": s(dynatomic_two),
        "period_two_points": [[s(px), s(py)] for px, py in two_cycle],
        "cycle_ledger": cycles,
        "period_two_monodromy": monodromy,
        "transition": transition,
        "witness_state_order": order,
        "witness_weight_definition": "omega(p)=1/det(I-DF(p)); M_{p,F(p)}=omega(p)",
        "witness_matrix": matrix_strings(M),
        "weighted_trace_sequence_n1_to_6": traces,
        "finite_witness_determinant": s(det_poly.as_expr()),
        "finite_witness_determinant_coefficients": det_coefficients,
        "unweighted_periodic_point_counts": {str(n): (2 if n % 2 else 4) for n in range(1, 7)},
        "primitive_orbit_counts": {"1": 2, "2": 1},
        "verdict": {
            "A1": "A1_PARTIAL_CERTIFIED",
            "A2": "A2_CERTIFIED_PREFIX",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "A1_qualification": "EXACT_FIXED_AND_PRIMITIVE_TWO_CYCLE_WITNESSES_ONLY",
            "A2_qualification": "FOUR_STATE_DISCRETE_WEIGHTED_CYCLE_GRAPH_ONLY",
            "reason": "dissipative low-period algebra and a finite transfer witness are exact; global coding and an analytic operator owner are open",
        },
        "nonclaims": [
            "complete real primitive-orbit atlas or Markov partition",
            "Fredholm determinant, nuclearity, analytic continuation, or zero-count theorem",
            "arithmetic/local data, Euler factors, root numbers, automorphy",
            "Hilbert--Polya operator, Riemann-zero correspondence, or Route B authorization",
        ],
    }
    raw = json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    OUT.write_text(raw)
    print(json.dumps({"evidence_sha256": sha256(raw.encode()).hexdigest(), "traces": traces, "determinant": s(det_poly.as_expr())}, sort_keys=True))


if __name__ == "__main__":
    main()
