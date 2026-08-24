#!/usr/bin/env python3
"""Independent validator for C122.  This file does not import the producer."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results" / "c122_adaptive_evidence.json"


class CheckFailure(AssertionError):
    pass


def parse(x: str) -> sp.Expr:
    return sp.sympify(x, locals={"sqrt": sp.sqrt})


def pvec(xs: list[str]) -> sp.Matrix:
    return sp.Matrix([parse(x) for x in xs])


def pmat(xs: list[list[str]]) -> sp.Matrix:
    return sp.Matrix([[parse(x) for x in row] for row in xs])


def validate(data: dict) -> int:
    checks = 0

    def req(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise CheckFailure(message)

    req(data["schema_id"] == "hcs-c122-adaptive-feedback-henon-prefreeze-v1", "schema")
    req(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    req(data["source_model"]["parameters"] == {"feedback_gain": "3", "parameter_contraction": "1/2", "offset": "-1/2"}, "parameters")

    def F(v: sp.Matrix, gain: sp.Expr = sp.Integer(3)) -> sp.Matrix:
        x, y, a = v
        return sp.Matrix([x**2 + a - y, x, a / 2 + gain * x - sp.Rational(1, 2)])

    def Finv(v: sp.Matrix) -> sp.Matrix:
        X, Y, A = v
        a = 2 * A - 6 * Y + 1
        return sp.Matrix([Y, Y**2 + a - X, a])

    def J(x: sp.Expr) -> sp.Matrix:
        return sp.Matrix([[2 * x, -1, 1], [1, 0, 0], [3, 0, sp.Rational(1, 2)]])

    x, y, a = sp.symbols("x y a")
    symbolic = sp.Matrix([x, y, a])
    req(all(sp.simplify(v) == 0 for v in Finv(F(symbolic)) - symbolic), "left inverse")
    req(all(sp.simplify(v) == 0 for v in F(Finv(symbolic)) - symbolic), "right inverse")
    req(sp.factor(J(x).det()) == sp.Rational(1, 2), "Jacobian determinant")
    req(data["structural_checks"]["constant_jacobian_determinant"] == "1/2", "recorded Jacobian determinant")

    expected_fixed = {
        (-2 + sp.sqrt(5), -2 + sp.sqrt(5), -13 + 6 * sp.sqrt(5)),
        (-2 - sp.sqrt(5), -2 - sp.sqrt(5), -13 - 6 * sp.sqrt(5)),
    }
    rows = data["certified_orbit_ledger"]["fixed_rows"]
    req(len(rows) == 2, "fixed count")
    observed = set()
    for row in rows:
        v = pvec(row["state"])
        observed.add(tuple(v))
        req(F(v).equals(v), "fixed closure")
        req(row["cycle_closes"] is True, "fixed flag")
        req(pmat(row["jacobian"]) == J(v[0]), "fixed Jacobian")
        req(parse(row["jacobian_determinant"]) == sp.Rational(1, 2), "fixed determinant")
    req(observed == expected_fixed, "fixed set")

    prow = data["certified_orbit_ledger"]["period_two_rows"][0]
    cycle = [pvec(v) for v in prow["states"]]
    req(cycle == [sp.Matrix([1, -1, -3]), sp.Matrix([-1, 1, 1])], "cycle states")
    req(F(cycle[0]) == cycle[1] and F(cycle[1]) == cycle[0], "cycle closure")
    req(prow["period"] == 2 and prow["primitive"] is True and cycle[0] != cycle[1], "primitive")
    M = J(-1) * J(1)
    req(M == sp.Matrix([[-2, 2, sp.Rational(-3, 2)], [2, -1, 1], [sp.Rational(15, 2), -3, sp.Rational(13, 4)]]), "monodromy control")
    req(pmat(prow["monodromy"]) == M, "monodromy")
    req(parse(prow["monodromy_trace"]) == sp.Rational(1, 4), "trace")
    req(parse(prow["monodromy_determinant"]) == sp.Rational(1, 4), "monodromy det")
    req([parse(v) for v in prow["det_I_minus_z_monodromy"]] == [1, sp.Rational(-1, 4), sp.Rational(5, 2), sp.Rational(-1, 4)], "det coefficients")

    control = data["feedback_controls"]
    req(control["desired_cycle_forces_gain_and_offset"] == {"gain": "3", "offset": "-1/2"}, "feedback solution")
    req(pvec(control["gain_zero_first_image"]) == F(cycle[0], 0), "zero-gain image")
    req(parse(control["gain_zero_parameter_residual_against_target"]) == -3, "zero-gain residual")
    req(parse(control["neighbor_parameter_residual_against_target"]) == sp.Rational(-1, 2), "neighbor residual")

    deg = data["structural_checks"]["degree_prefix"]
    req(deg == [{"iterate": n, "coordinate_total_degrees": [2**n, 2 ** (n - 1), 2 ** (n - 1)]} for n in range(1, 7)], "degree prefix")
    verdict = data["route_a_verdict"]
    req(
        (verdict["A1"], verdict["A2"], verdict["A3"], verdict["A4"], verdict["overall"])
        == ("A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL", "ROUTE_A_EXPLORATORY"),
        "canonical route verdict",
    )
    req("NO_PRIME_LIKE_TARGET_CORRESPONDENCE" in verdict["A1_qualification"], "A1 target boundary")
    req("NO_TARGET_DIVISOR_OR_ANALYTIC_BRIDGE" in verdict["A2_qualification"], "A2 target boundary")
    req(verdict["A3_qualification"] == "NO_GLOBAL_ANALYTIC_STRUCTURE_OR_CONTINUATION_THEOREM", "A3 boundary")
    for key in ("complete_orbit_atlas", "transfer_or_fredholm_owner", "prime_like_target_correspondence", "target_divisor_match", "analytic_bridge", "arithmetic_local_data", "euler_factors", "root_numbers", "automorphy", "hilbert_polya_operator", "route_b_authorized"):
        req(data["claims"][key] is False, f"nonclaim {key}")
    return checks


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    checks = validate(data)
    print(json.dumps({"status": "C122_INDEPENDENT_CHECK_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
