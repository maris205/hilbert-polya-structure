#!/usr/bin/env python3
"""Independent checker for the C115 McMillan evidence receipt.

This module deliberately does not import the producer.  An optional evidence
path is accepted so the hostile-mutation test can exercise this same checker.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = PROJECT / "results/c115_mcmillan_evidence.json"


def expr(value: str) -> sp.Expr:
    return sp.sympify(value)


def matrix(rows: list[list[str]]) -> sp.Matrix:
    return sp.Matrix([[expr(value) for value in row] for row in rows])


def same(left: object, right: object) -> bool:
    return sp.simplify(sp.sympify(left) - sp.sympify(right)) == 0


def run(path: Path) -> int:
    data = json.loads(path.read_text())
    checks = 0

    def require(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    x, y, z, lam = sp.symbols("x y z lam")
    mu = sp.Integer(-2)
    f = -4 * x / (1 + x**2)
    X, Y = f - y, x
    inverse = (y, -4 * y / (1 + y**2) - x)
    invariant = x**2 * y**2 + x**2 + y**2 + 4 * x * y
    derivative = sp.diff(f, x)
    jacobian = sp.Matrix([[derivative, -1], [1, 0]])

    require(data["schema"] == "hcs-c115-mcmillan-rational-v1", "schema")
    require(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    require(data["source_model"]["mu"] == "-2", "mu")
    require(data["source_model"]["forward_pole_divisor"] == "x**2 + 1 = 0", "forward pole")
    require(data["source_model"]["inverse_pole_divisor"] == "y**2 + 1 = 0", "inverse pole")

    # Check both rational inverse compositions from scratch.
    left = (
        sp.cancel((-4 * inverse[0] / (1 + inverse[0] ** 2)) - inverse[1]),
        sp.cancel(inverse[0]),
    )
    A, B = X, Y
    right = (sp.cancel(B), sp.cancel(-4 * B / (1 + B**2) - A))
    require(all(same(q, r) for q, r in zip(left, (x, y))), "left inverse")
    require(all(same(q, r) for q, r in zip(right, (x, y))), "right inverse")
    recorded_left = data["birational_certificates"]["left_inverse_composition"]
    recorded_right = data["birational_certificates"]["right_inverse_composition"]
    require(all(same(q, r) for q, r in zip(recorded_left, (x, y))), "recorded left inverse")
    require(all(same(q, r) for q, r in zip(recorded_right, (x, y))), "recorded right inverse")
    require(data["birational_certificates"]["equals_inverse_on_common_domain"] is True, "reversor qualification")
    require(all(same(q, r) for q, r in zip(data["birational_certificates"]["S_M_S"], inverse)), "reversor")

    require(same(jacobian.det(), 1), "Jacobian determinant")
    require(matrix(data["jacobian_certificate"]["matrix"]).equals(jacobian), "Jacobian matrix")
    require(data["jacobian_certificate"]["determinant"] == "1", "recorded Jacobian determinant")
    require(same(invariant.subs({x: X, y: Y}, simultaneous=True) - invariant, 0), "first integral")
    require(same(data["first_integral_certificate"]["formula"], invariant), "recorded invariant")
    require(data["first_integral_certificate"]["I_after_M_minus_I"] == "0", "recorded invariant difference")

    fixed = data["fixed_point_certificate"]
    require(same(fixed["cleared_numerator"], -2 * x * (x**2 + 3)), "fixed numerator")
    require(same(fixed["denominator"], x**2 + 1), "fixed denominator")
    expected_fixed = [(sp.Integer(0), sp.Integer(0)), (sp.I * sp.sqrt(3), sp.I * sp.sqrt(3)), (-sp.I * sp.sqrt(3), -sp.I * sp.sqrt(3))]
    rows = fixed["valid_fixed_points"]
    require(len(rows) == 3 and fixed["valid_fixed_count_over_C"] == 3, "fixed count")
    require(fixed["real_fixed_count"] == 1 and fixed["nonreal_fixed_count"] == 2, "fixed field split")
    for row, point in zip(rows, expected_fixed):
        px, py = map(expr, row["point"])
        require(same(px, point[0]) and same(py, point[1]), f"fixed point {row['name']}")
        require(not same(px**2 + 1, 0), f"fixed point domain {row['name']}")
        image = (-4 * px / (1 + px**2) - py, px)
        require(all(same(a, b) for a, b in zip(image, point)), f"fixed closure {row['name']}")
        require(row["map_closes"] is True, f"recorded fixed closure {row['name']}")

    # Recompute the F^2 elimination and separate pole roots from valid roots.
    X2 = sp.cancel(-4 * X / (1 + X**2) - Y)
    Y2 = X
    n1 = sp.factor(sp.together(X2 - x).as_numer_denom()[0])
    n2 = sp.factor(sp.together(Y2 - y).as_numer_denom()[0])
    resultant = sp.factor(sp.resultant(n1, n2, y))
    period = data["period_two_elimination"]
    require(same(period["raw_resultant_in_x"], resultant), "F2 resultant")
    require(same(period["pole_factor_in_raw_resultant"], (x**2 + 1) ** 2), "pole factor")
    require(same(period["valid_factor_after_pole_exclusion"], x * (x - 1) * (x + 1) * (x**2 + 3)), "valid F2 factor")
    require(same(period["primitive_period_two_factor"], x**2 - 1), "primitive factor")
    require(period["valid_F2_fixed_count_over_C"] == 5 and period["valid_real_F2_fixed_count"] == 3, "F2 counts")
    invalid = period["invalid_cleared_denominator_roots"]
    require(len(invalid) == 2, "invalid root count")
    for row, root in zip(invalid, (sp.I, -sp.I)):
        require(same(row["x"], root), "invalid root identity")
        require(same(root**2 + 1, 0), "invalid root pole")
        require(row["excluded"] is True and "undefined" in row["reason"], "invalid root exclusion")

    cycle = data["primitive_period_two_cycle"]
    q_plus = (sp.Integer(1), sp.Integer(-1))
    q_minus = (sp.Integer(-1), sp.Integer(1))
    require(all(same(a, b) for a, b in zip(cycle["q_plus"], q_plus)), "q plus")
    require(all(same(a, b) for a, b in zip(cycle["q_minus"], q_minus)), "q minus")

    def M(point: tuple[sp.Expr, sp.Expr]) -> tuple[sp.Expr, sp.Expr]:
        a, b = point
        return (sp.cancel(-4 * a / (1 + a**2) - b), a)

    require(M(q_plus) == q_minus and M(q_minus) == q_plus, "cycle closure")
    require(cycle["cycle_closes"] is True and cycle["points_are_distinct"] is True, "cycle flags")
    require(cycle["forward_denominators"] == ["2", "2"], "cycle domains")
    require(same(cycle["first_integral_value"], -1), "cycle invariant")

    J_plus = jacobian.subs(x, 1)
    J_minus = jacobian.subs(x, -1)
    P2 = sp.simplify(J_minus * J_plus)
    mono = data["period_two_monodromy"]
    require(matrix(mono["matrix"]).equals(P2), "monodromy matrix")
    require(same(mono["determinant"], P2.det()), "monodromy determinant")
    require(same(mono["trace"], sp.trace(P2)), "monodromy trace")
    require(same(mono["characteristic_polynomial"], P2.charpoly(lam).as_expr()), "monodromy characteristic polynomial")
    require(same(mono["det_I_minus_zP2"], (sp.eye(2) - z * P2).det()), "monodromy z polynomial")
    require("not a transfer determinant" in mono["interpretation"], "monodromy boundary")

    J0 = jacobian.subs(x, 0)
    control = data["fixed_origin_control"]
    require(matrix(control["matrix"]).equals(J0), "control matrix")
    require(same(control["characteristic_polynomial"], J0.charpoly(lam).as_expr()), "control characteristic polynomial")
    require(same(control["det_I_minus_zDM"], (sp.eye(2) - z * J0).det()), "control z polynomial")

    verdict = data["verdict"]
    require(verdict["A1"] == "A1_PARTIAL_CERTIFIED", "A1")
    require("LOW_PERIOD" in verdict["A1_qualification"], "A1 qualification")
    require(verdict["A2"] == "A2_FAIL", "A2")
    require(verdict["A3"] == "A3_NOT_ADDRESSED" and verdict["A4"] == "A4_FAIL", "A3/A4")
    require(any("transfer operator" in claim for claim in data["nonclaims"]), "transfer nonclaim")
    require(any("Euler factors" in claim for claim in data["nonclaims"]), "arithmetic nonclaim")

    print(f"C115_CHECK_PASS {checks}")
    return checks


if __name__ == "__main__":
    run(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE)
