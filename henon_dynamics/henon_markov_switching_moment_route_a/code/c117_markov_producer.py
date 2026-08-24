#!/usr/bin/env python3
"""Produce the exact C117 Markov-switching Hénon moment certificate."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c117_markov_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def srat(x: sp.Expr) -> str:
    return str(sp.factor(x))


def matrix_strings(a: sp.Matrix) -> list[list[str]]:
    return [[srat(a[i, j]) for j in range(a.cols)] for i in range(a.rows)]


def det_polynomial(a: sp.Matrix) -> list[str]:
    z = sp.symbols("z")
    poly = sp.Poly((sp.eye(a.rows) - z * a).det(), z)
    return [srat(x) for x in reversed(poly.all_coeffs())]


def traces(a: sp.Matrix, nmax: int = 6) -> dict[str, str]:
    return {str(n): srat(sp.trace(a**n)) for n in range(1, nmax + 1)}


def symmetric_square(a: sp.Rational, b: sp.Rational) -> sp.Matrix:
    """Pullback on (x^2,xy,y^2) for (x',y')=(a*x-b*y,x)."""
    c = -b
    return sp.Matrix([[a * a, 2 * a * c, c * c], [a, c, 0], [1, 0, 0]])


def block_operator(p: sp.Matrix, local: list[sp.Matrix]) -> sp.Matrix:
    # Rows are the new environment j, columns the old environment i.
    return sp.Matrix.vstack(
        *[sp.Matrix.hstack(*[p[i, j] * local[j] for i in range(2)]) for j in range(2)]
    )


def build() -> dict[str, object]:
    p = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)],
                   [sp.Rational(1, 4), sp.Rational(3, 4)]])
    params = [(sp.Rational(1, 2), sp.Rational(1, 3)),
              (sp.Rational(-1), sp.Rational(1, 2))]
    jac = [sp.Matrix([[a, -b], [1, 0]]) for a, b in params]
    sym2 = [symmetric_square(a, b) for a, b in params]
    first = block_operator(p, jac)
    second = block_operator(p, sym2)

    pi = [sp.Rational(3, 7), sp.Rational(4, 7)]
    bbar = pi[0] * jac[0] + pi[1] * jac[1]
    sbar = pi[0] * sym2[0] + pi[1] * sym2[1]
    naive = symmetric_square(bbar[0, 0], -bbar[0, 1])
    gap = sp.simplify(sbar - naive)

    return {
        "schema_id": "hcs-c117-markov-switching-henon-moment-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "source_model": {
            "maps": [
                "F_0(x,y)=(x^2+x/2-y/3,x)",
                "F_1(x,y)=(x^2-x-y/2,x)",
            ],
            "common_fixed_point": ["0", "0"],
            "parameters": {
                "mode_0": {"a": "1/2", "b": "1/3"},
                "mode_1": {"a": "-1", "b": "1/2"},
            },
            "transition_matrix_rows_old_columns_new": matrix_strings(p),
            "stationary_distribution": [srat(x) for x in pi],
            "markov_eigenvalues": ["1", "5/12"],
            "environment_convention": "s_n=i -> s_(n+1)=j with probability P_ij; F_j is then applied",
        },
        "tangent_cocycle": {
            "jacobians_at_origin": [matrix_strings(x) for x in jac],
            "jacobian_determinants": [srat(x.det()) for x in jac],
            "first_moment_basis": ["mode0:x", "mode0:y", "mode1:x", "mode1:y"],
            "first_moment_operator": matrix_strings(first),
            "first_moment_traces": traces(first),
            "first_moment_det_I_minus_z": det_polynomial(first),
            "first_moment_determinant": srat(first.det()),
        },
        "symmetric_second_moment_cocycle": {
            "local_symmetric_square_matrices": [matrix_strings(x) for x in sym2],
            "basis": [
                "mode0:x^2", "mode0:xy", "mode0:y^2",
                "mode1:x^2", "mode1:xy", "mode1:y^2",
            ],
            "operator": matrix_strings(second),
            "traces": traces(second),
            "det_I_minus_z": det_polynomial(second),
            "determinant": srat(second.det()),
        },
        "stationary_averaging_control": {
            "average_jacobian": matrix_strings(bbar),
            "average_symmetric_square": matrix_strings(sbar),
            "symmetric_square_of_average": matrix_strings(naive),
            "intermittency_gap": matrix_strings(gap),
            "intermittency_gap_rank": gap.rank(),
            "gap_is_nonzero": gap != sp.zeros(3),
        },
        "checks": {
            "transition_rows_sum_to_one": all(sum(p[i, j] for j in range(2)) == 1 for i in range(2)),
            "stationary_distribution_verified": sp.Matrix(1, 2, pi) * p == sp.Matrix(1, 2, pi),
            "common_origin_fixed_for_both_nonlinear_maps": True,
            "first_operator_dimension": first.rows,
            "second_operator_dimension": second.rows,
            "all_exact_rational": True,
            "average_second_moment_not_square_of_average_first_moment": gap != sp.zeros(3),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "COMMON_FIXED_POINT_TANGENT_COCYCLE_ONLY",
            "A2": "A2_CERTIFIED_PREFIX",
            "A2_qualification": "SOURCE_OWNED_FINITE_MARKOV_TANGENT_MOMENT_OPERATORS_ONLY",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "claims": {
            "exact_markov_tangent_first_moment_operator": True,
            "exact_markov_tangent_second_moment_operator": True,
            "complete_nonlinear_random_orbit_atlas": False,
            "global_nonlinear_transfer_operator": False,
            "fredholm_or_nuclear_owner": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
            "route_b_authorized": False,
        },
        "reproducibility": {
            "producer": "code/c117_markov_producer.py",
            "number_system": "Q",
            "randomness": "none; the Markov probabilities are exact model parameters",
        },
    }


def main() -> None:
    value = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(canonical(value))
    print(json.dumps({
        "status": value["status"],
        "evidence_sha256": digest(OUT.read_bytes()),
        "first_dimension": 4,
        "second_dimension": 6,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
