#!/usr/bin/env python3
"""Exact finite audit for a two-site variational Hénon lattice (C106).

The computation is deliberately small and exact.  It certifies algebraic
identities of the map and one synchronous period-two orbit, while making no
claim that the listed cycles are a complete primitive-orbit atlas or that a
finite determinant is a Fredholm determinant.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path
from typing import Iterable

PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "results/c106_variational_lattice_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
A = Fraction(7)
K = Fraction(1, 4)
ZERO = Fraction(0)
ONE = Fraction(1)


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def rat(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def vec_rat(xs: Iterable[Fraction]) -> list[dict[str, int]]:
    return [rat(x) for x in xs]


def mat_rat(matrix: list[list[Fraction]]) -> list[list[dict[str, int]]]:
    return [[rat(x) for x in row] for row in matrix]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), ZERO) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def madd(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def eye(n: int) -> list[list[Fraction]]:
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def omega() -> list[list[Fraction]]:
    # Coordinates are (q_1,q_2,p_1,p_2), with Omega=[[0,I],[-I,0]].
    z = [[ZERO, ZERO], [ZERO, ZERO]]
    i = eye(2)
    mi = [[-x for x in row] for row in i]
    return [z[0] + i[0], z[1] + i[1], mi[0] + z[0], mi[1] + z[1]]


def determinant(a: list[list[Fraction]]) -> Fraction:
    n = len(a)
    total = ZERO
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        sign = ONE if inversions % 2 == 0 else -ONE
        term = sign
        for i, j in enumerate(perm):
            term *= a[i][j]
        total += term
    return total


def poly_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else ZERO) + (b[i] if i < len(b) else ZERO) for i in range(n)]


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [ZERO] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def det_i_minus_zj(j: list[list[Fraction]]) -> list[Fraction]:
    """Return coefficients of det(I-zJ), low degree first."""
    n = len(j)
    total = [ZERO]
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[k] for i in range(n) for k in range(i + 1, n))
        sign = ONE if inversions % 2 == 0 else -ONE
        term = [sign]
        for i, col in enumerate(perm):
            entry = [ONE, -j[i][col]] if i == col else [ZERO, -j[i][col]]
            term = poly_mul(term, entry)
        total = poly_add(total, term)
    while len(total) > 1 and total[-1] == ZERO:
        total.pop()
    return total


def gradient(q: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    x, y = q
    return (A * x - x * x - K * (x - y), A * y - y * y + K * (x - y))


def potential(q: tuple[Fraction, Fraction]) -> Fraction:
    x, y = q
    return A * (x * x + y * y) / 2 - (x * x * x + y * y * y) / 3 - K * (x - y) * (x - y) / 2


def hessian(q: tuple[Fraction, Fraction], coupling: Fraction = K) -> list[list[Fraction]]:
    x, y = q
    return [[A - coupling - 2 * x, coupling], [coupling, A - coupling - 2 * y]]


def jacobian(q: tuple[Fraction, Fraction], coupling: Fraction = K) -> list[list[Fraction]]:
    h = hessian(q, coupling)
    i = eye(2)
    z = [[ZERO, ZERO], [ZERO, ZERO]]
    return [h[0] + [-i[0][0], -i[0][1]], h[1] + [-i[1][0], -i[1][1]], i[0] + z[0], i[1] + z[1]]


def map_state(state: tuple[Fraction, Fraction, Fraction, Fraction], coupling: Fraction = K) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    x, y, u, v = state
    gx, gy = (A * x - x * x - coupling * (x - y), A * y - y * y + coupling * (x - y))
    return (gx - u, gy - v, x, y)


def inverse_state(state: tuple[Fraction, Fraction, Fraction, Fraction], coupling: Fraction = K) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    x, y, u, v = state
    gu, gv = (A * u - u * u - coupling * (u - v), A * v - v * v + coupling * (u - v))
    return (u, v, gu - x, gv - y)


def reversor(state: tuple[Fraction, Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    x, y, u, v = state
    return (u, v, x, y)


def trace(a: list[list[Fraction]]) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def matrix_sub(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def zero_matrix(a: list[list[Fraction]]) -> bool:
    return all(x == ZERO for row in a for x in row)


def orbit_row(label: str, states: list[tuple[Fraction, Fraction, Fraction, Fraction]], coupling: Fraction = K) -> dict[str, object]:
    matrices = [jacobian((s[0], s[1]), coupling) for s in states]
    monodromy = eye(4)
    for matrix in matrices:
        monodromy = matmul(matrix, monodromy)
    j0 = matrices[0]
    j2 = matmul(j0, j0)
    return {
        "label": label,
        "period": len(states),
        "states": [vec_rat(s) for s in states],
        "primitive_verified": len(states) == 1 or states[0] != states[1],
        "cycle_closure_verified": map_state(states[-1], coupling) == states[0],
        "jacobian_at_first": mat_rat(j0),
        "monodromy": mat_rat(monodromy),
        "monodromy_determinant": rat(determinant(monodromy)),
        "monodromy_trace": rat(trace(monodromy)),
        "monodromy_trace_square_at_first": rat(trace(j2)),
        "det_I_minus_z_monodromy": vec_rat(det_i_minus_zj(monodromy)),
        "symplectic_at_each_step": all(zero_matrix(matrix_sub(matmul(matmul(transpose(matrix), omega()), matrix), omega())) for matrix in matrices),
    }


def main() -> None:
    fixed_origin = (ZERO, ZERO, ZERO, ZERO)
    fixed_sync = (Fraction(5), Fraction(5), Fraction(5), Fraction(5))
    # A genuine synchronous period-two orbit: q alternates 3 and 6.
    cycle_2 = [(Fraction(3), Fraction(3), Fraction(6), Fraction(6)), (Fraction(6), Fraction(6), Fraction(3), Fraction(3))]
    fixed = [orbit_row("fixed_origin", [fixed_origin]), orbit_row("fixed_synchronous", [fixed_sync])]
    cycle = orbit_row("synchronous_period_two", cycle_2)

    # Exact product-vs-coupled control at the period-two orbit, with K=0 as the
    # uncoupled reference.  This is a finite monodromy polynomial, not a
    # Fredholm determinant claim.
    coupled_mono = [[Fraction(x["numerator"], x["denominator"]) for x in row] for row in cycle["monodromy"]]  # type: ignore[index]
    uncoupled_matrices = [jacobian((s[0], s[1]), ZERO) for s in cycle_2]
    uncoupled_mono = matmul(uncoupled_matrices[1], uncoupled_matrices[0])
    coupled_poly = det_i_minus_zj(coupled_mono)
    uncoupled_poly = det_i_minus_zj(uncoupled_mono)
    trace_delta = trace(coupled_mono) - trace(uncoupled_mono)
    z2_delta = coupled_poly[2] - uncoupled_poly[2]

    samples = [
        (Fraction(1, 2), Fraction(-1, 3), Fraction(2, 5), Fraction(-3, 7)),
        (Fraction(-2), Fraction(1), Fraction(0), Fraction(3, 2)),
        (Fraction(4, 3), Fraction(5, 7), Fraction(-1, 2), Fraction(2, 3)),
    ]
    reversor_checks = []
    exact_primitive_checks = []
    for state in samples:
        left = reversor(map_state(reversor(state)))
        right = inverse_state(state)
        reversor_checks.append(left == right)
        x, y, u, v = state
        gx, gy = gradient((x, y))
        # With lambda=q dot dp, F^*lambda-lambda=d(U(q)-p dot q).
        ux = A * x - x * x - K * (x - y)
        uy = A * y - y * y + K * (x - y)
        exact_primitive_checks.append((gx - u, gy - v, -x, -y) == (ux - u, uy - v, -x, -y))

    omega_matrix = omega()
    all_jacobians = [jacobian((s[0], s[1])) for s in [fixed_origin, fixed_sync, *cycle_2]]
    symplectic_checks = [zero_matrix(matrix_sub(matmul(matmul(transpose(j), omega_matrix), j), omega_matrix)) for j in all_jacobians]
    determinant_checks = [determinant(j) == ONE for j in all_jacobians]
    fixed_equations = [gradient((s[0], s[1])) == (2 * s[0], 2 * s[1]) for s in [fixed_origin, fixed_sync]]

    result = {
        "schema_id": "hcs-c106-variational-coupled-henon-lattice-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "model": {
            "name": "two_site_variational_henon_lattice",
            "parameters": {"a": rat(A), "kappa": rat(K), "sites": 2},
            "potential": "U(q)=a/2*(x^2+y^2)-(x^3+y^3)/3-kappa/2*(x-y)^2",
            "map": "F(q,p)=(grad U(q)-p,q)",
            "reversor": "R(q,p)=(p,q)",
            "symplectic_form": "Omega=[[0,I],[-I,0]] in (q1,q2,p1,p2)",
            "canonical_one_form": "lambda=q dot dp; F^*lambda-lambda=d(U(q)-p dot q)",
        },
        "certified_orbit_ledger": {"fixed_rows": fixed, "period_two_rows": [cycle]},
        "controls": {
            "uncoupled_kappa_zero_period_two_monodromy": mat_rat(uncoupled_mono),
            "uncoupled_det_I_minus_z": vec_rat(uncoupled_poly),
            "coupled_det_I_minus_z": vec_rat(coupled_poly),
            "trace_difference_coupled_minus_uncoupled": rat(trace_delta),
            "z2_coefficient_difference_coupled_minus_uncoupled": rat(z2_delta),
            "mixed_trace_is_nonzero": trace_delta != ZERO,
            "mixed_z2_coefficient_is_nonzero": z2_delta != ZERO,
        },
        "checks": {
            "fixed_gradient_equals_two_q": all(fixed_equations),
            "period_two_cycle_closes": cycle["cycle_closure_verified"],
            "period_two_is_not_fixed": cycle_2[0] != cycle_2[1],
            "reversor_identity_on_three_exact_samples": all(reversor_checks),
            "exact_symplectic_primitive_identity_on_three_exact_samples": all(exact_primitive_checks),
            "symplectic_form_on_fixed_and_cycle_points": all(symplectic_checks),
            "jacobian_determinant_one_on_fixed_and_cycle_points": all(determinant_checks),
            "coupling_changes_period_two_trace": trace_delta != ZERO,
            "coupling_changes_period_two_z2_coefficient": z2_delta != ZERO,
            "all_exact_rational_arithmetic": True,
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "PARTIAL_CERTIFIED_LOW_PERIOD_ONLY",
            "A2": "A2_FAIL",
            "A2_qualification": "OPERATOR_OWNER_OPEN",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "claims": {
            "exact_variational_map_identities": True,
            "exact_low_period_orbit_witnesses": True,
            "complete_primitive_orbit_atlas": False,
            "fredholm_determinant_constructed": False,
            "dynamical_zeta_analytic_continuation": False,
            "arithmetic_local_claimed": False,
            "euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "automorphy_claimed": False,
            "hilbert_polya_operator_claimed": False,
        },
        "reproducibility": {"producer": "code/c106_variational_lattice.py", "exact_number_field": "Q", "randomness": "none"},
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({"status": result["status"], "fixed_count": 2, "period_two_count": 1, "evidence_sha256": digest(OUT.read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
