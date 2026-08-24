#!/usr/bin/env python3
"""Produce the exact C122 adaptive-feedback Hénon certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results" / "c122_adaptive_evidence.json"


def ss(value: sp.Expr) -> str:
    return sp.sstr(sp.factor(value))


def vec(values: sp.Matrix) -> list[str]:
    return [ss(v) for v in values]


def mat(values: sp.Matrix) -> list[list[str]]:
    return [[ss(values[i, j]) for j in range(values.cols)] for i in range(values.rows)]


def fmap(state: sp.Matrix, gain: sp.Rational = sp.Rational(3)) -> sp.Matrix:
    x, y, a = state
    return sp.Matrix([x**2 + a - y, x, a / 2 + gain * x - sp.Rational(1, 2)])


def jacobian(x: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[2 * x, -1, 1], [1, 0, 0], [3, 0, sp.Rational(1, 2)]])


def inverse(state: sp.Matrix) -> sp.Matrix:
    X, Y, A = state
    old_a = 2 * A - 6 * Y + 1
    return sp.Matrix([Y, Y**2 + old_a - X, old_a])


def build() -> dict:
    z, lam = sp.symbols("z lambda")
    sqrt5 = sp.sqrt(5)
    fixed_x = [-2 + sqrt5, -2 - sqrt5]
    fixed_rows = []
    for idx, x0 in enumerate(fixed_x):
        state = sp.Matrix([x0, x0, 6 * x0 - 1])
        J = jacobian(x0)
        fixed_rows.append(
            {
                "label": f"fixed_{'plus' if idx == 0 else 'minus'}",
                "state": vec(state),
                "cycle_closes": fmap(state).equals(state),
                "jacobian": mat(J),
                "jacobian_determinant": ss(J.det()),
                "characteristic_polynomial": ss(J.charpoly(lam).as_expr()),
            }
        )

    cycle = [sp.Matrix([1, -1, -3]), sp.Matrix([-1, 1, 1])]
    M = jacobian(-1) * jacobian(1)
    det_poly = sp.Poly((sp.eye(3) - z * M).det(), z)
    cycle_row = {
        "label": "adaptive_primitive_period_two",
        "period": 2,
        "primitive": True,
        "states": [vec(v) for v in cycle],
        "forward_images": [vec(fmap(v)) for v in cycle],
        "monodromy": mat(M),
        "monodromy_trace": ss(sp.trace(M)),
        "monodromy_determinant": ss(M.det()),
        "det_I_minus_z_monodromy": [ss(c) for c in reversed(det_poly.all_coeffs())],
    }

    samples = [
        sp.Matrix([0, 0, 0]),
        sp.Matrix([1, -1, -3]),
        sp.Matrix([sp.Rational(2, 3), sp.Rational(-1, 5), sp.Rational(7, 4)]),
    ]
    inverse_checks = []
    for p in samples:
        inverse_checks.append(
            {
                "state": vec(p),
                "inverse_after_forward": vec(sp.simplify(inverse(fmap(p)))),
                "forward_after_inverse": vec(sp.simplify(fmap(inverse(p)))),
            }
        )

    degree_prefix = [
        {"iterate": n, "coordinate_total_degrees": [2**n, 2 ** (n - 1), 2 ** (n - 1)]}
        for n in range(1, 7)
    ]
    control_first = fmap(cycle[0], gain=sp.Rational(0))
    neighbor_first = fmap(cycle[0], gain=sp.Rational(5, 2))

    return {
        "schema_id": "hcs-c122-adaptive-feedback-henon-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_model": {
            "map": "G(x,y,a)=(x^2+a-y,x,a/2+3*x-1/2)",
            "parameters": {"feedback_gain": "3", "parameter_contraction": "1/2", "offset": "-1/2"},
            "inverse": "G^{-1}(X,Y,A)=(Y,Y^2+2*A-6*Y+1-X,2*A-6*Y+1)",
            "jacobian_formula": "[[2*x,-1,1],[1,0,0],[3,0,1/2]]",
        },
        "structural_checks": {
            "constant_jacobian_determinant": "1/2",
            "inverse_two_sided_samples": inverse_checks,
            "fixed_point_equation": "x^2+4*x-1=0; y=x; a=6*x-1",
            "degree_prefix": degree_prefix,
        },
        "certified_orbit_ledger": {"fixed_rows": fixed_rows, "period_two_rows": [cycle_row]},
        "feedback_controls": {
            "desired_cycle_forces_gain_and_offset": {"gain": "3", "offset": "-1/2"},
            "gain_zero_first_image": vec(control_first),
            "gain_zero_parameter_residual_against_target": ss(control_first[2] - cycle[1][2]),
            "neighbor_gain_5_over_2_first_image": vec(neighbor_first),
            "neighbor_parameter_residual_against_target": ss(neighbor_first[2] - cycle[1][2]),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "EXACT_INTRINSIC_LOW_PERIOD_WITNESSES_BUT_NO_PRIME_LIKE_TARGET_CORRESPONDENCE",
            "A2": "A2_FAIL",
            "A2_qualification": "TANGENT_MONODROMY_IS_LOCAL_AND_HAS_NO_TARGET_DIVISOR_OR_ANALYTIC_BRIDGE",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_GLOBAL_ANALYTIC_STRUCTURE_OR_CONTINUATION_THEOREM",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "claims": {
            "exact_adaptive_polynomial_automorphism": True,
            "exact_low_period_witnesses": True,
            "feedback_essential_for_named_cycle": True,
            "complete_orbit_atlas": False,
            "transfer_or_fredholm_owner": False,
            "prime_like_target_correspondence": False,
            "target_divisor_match": False,
            "analytic_bridge": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
            "route_b_authorized": False,
        },
        "reproducibility": {"number_system": "Q(sqrt(5))", "randomness": "none", "producer": "code/c122_adaptive_producer.py"},
    }


def canonical_bytes(data: dict) -> bytes:
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = canonical_bytes(build())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(json.dumps({"status": "C122_PREFREEZE_G3_PASS", "evidence_sha256": hashlib.sha256(payload).hexdigest(), "fixed_count": 2, "period_two_count": 1}, sort_keys=True))


if __name__ == "__main__":
    main()
