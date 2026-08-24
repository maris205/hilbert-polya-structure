#!/usr/bin/env python3
"""Independent semantic checker for C117; does not import the producer."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c117_markov_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canon(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def ms(a: sp.Matrix) -> list[list[str]]:
    return [[str(sp.factor(a[i, j])) for j in range(a.cols)] for i in range(a.rows)]


def sym2(a: sp.Rational, b: sp.Rational) -> sp.Matrix:
    c = -b
    return sp.Matrix([[a*a, 2*a*c, c*c], [a, c, 0], [1, 0, 0]])


def blocks(p: sp.Matrix, cs: list[sp.Matrix]) -> sp.Matrix:
    return sp.Matrix.vstack(*[
        sp.Matrix.hstack(*[p[i, j] * cs[j] for i in range(2)]) for j in range(2)
    ])


def detpoly(a: sp.Matrix) -> list[str]:
    z = sp.symbols("z")
    q = sp.Poly((sp.eye(a.rows) - z*a).det(), z)
    return [str(sp.factor(x)) for x in reversed(q.all_coeffs())]


def tr(a: sp.Matrix) -> dict[str, str]:
    return {str(n): str(sp.factor(sp.trace(a**n))) for n in range(1, 7)}


def validate(path: Path = EVIDENCE) -> dict[str, object]:
    raw = path.read_bytes()
    d = json.loads(raw)
    assert raw == canon(d)
    assert d["schema_id"] == "hcs-c117-markov-switching-henon-moment-prefreeze-v1"
    assert d["status"] == "PREFREEZE_G3_PASS"
    assert d["scope_literal"] == FIREWALL

    p = sp.Matrix([[sp.Rational(2,3), sp.Rational(1,3)],
                   [sp.Rational(1,4), sp.Rational(3,4)]])
    pars = [(sp.Rational(1,2), sp.Rational(1,3)),
            (sp.Rational(-1), sp.Rational(1,2))]
    bs = [sp.Matrix([[a, -b], [1, 0]]) for a, b in pars]
    ss = [sym2(a, b) for a, b in pars]
    a1, a2 = blocks(p, bs), blocks(p, ss)

    src = d["source_model"]
    assert src["transition_matrix_rows_old_columns_new"] == ms(p)
    assert src["stationary_distribution"] == ["3/7", "4/7"]
    assert sp.Matrix([[sp.Rational(3,7), sp.Rational(4,7)]]) * p == sp.Matrix([[sp.Rational(3,7), sp.Rational(4,7)]])
    assert d["tangent_cocycle"]["jacobians_at_origin"] == [ms(x) for x in bs]
    assert d["tangent_cocycle"]["jacobian_determinants"] == ["1/3", "1/2"]
    assert d["tangent_cocycle"]["first_moment_operator"] == ms(a1)
    assert d["tangent_cocycle"]["first_moment_traces"] == tr(a1)
    assert d["tangent_cocycle"]["first_moment_det_I_minus_z"] == detpoly(a1)
    assert d["tangent_cocycle"]["first_moment_determinant"] == str(a1.det())
    assert d["symmetric_second_moment_cocycle"]["local_symmetric_square_matrices"] == [ms(x) for x in ss]
    assert d["symmetric_second_moment_cocycle"]["operator"] == ms(a2)
    assert d["symmetric_second_moment_cocycle"]["traces"] == tr(a2)
    assert d["symmetric_second_moment_cocycle"]["det_I_minus_z"] == detpoly(a2)

    pi = [sp.Rational(3,7), sp.Rational(4,7)]
    bbar = pi[0]*bs[0] + pi[1]*bs[1]
    sbar = pi[0]*ss[0] + pi[1]*ss[1]
    naive = sym2(bbar[0,0], -bbar[0,1])
    gap = sp.simplify(sbar-naive)
    ctl = d["stationary_averaging_control"]
    assert ctl["average_jacobian"] == ms(bbar)
    assert ctl["average_symmetric_square"] == ms(sbar)
    assert ctl["symmetric_square_of_average"] == ms(naive)
    assert ctl["intermittency_gap"] == ms(gap)
    assert ctl["intermittency_gap_rank"] == 1
    assert ctl["gap_is_nonzero"] is True

    checks = d["checks"]
    assert all(v is True or isinstance(v, int) for v in checks.values())
    assert checks["first_operator_dimension"] == 4
    assert checks["second_operator_dimension"] == 6
    verdict = d["route_a_verdict"]
    assert verdict == {
        "A1": "A1_WEAK",
        "A1_qualification": "COMMON_FIXED_POINT_TANGENT_COCYCLE_ONLY",
        "A2": "A2_CERTIFIED_PREFIX",
        "A2_qualification": "SOURCE_OWNED_FINITE_MARKOV_TANGENT_MOMENT_OPERATORS_ONLY",
        "A3": "A3_NOT_ADDRESSED",
        "A4": "A4_FAIL",
        "overall": "ROUTE_A_EXPLORATORY",
    }
    c = d["claims"]
    for key in ("complete_nonlinear_random_orbit_atlas", "global_nonlinear_transfer_operator",
                "fredholm_or_nuclear_owner", "arithmetic_local_data", "euler_factors",
                "root_numbers", "automorphy", "hilbert_polya_operator", "route_b_authorized"):
        assert c[key] is False
    return d


def main() -> None:
    d = validate()
    print(json.dumps({"status": "C117_INDEPENDENT_CHECK_PASS", "first_dimension": 4,
                      "second_dimension": 6, "schema_id": d["schema_id"]}, sort_keys=True))


if __name__ == "__main__":
    main()
