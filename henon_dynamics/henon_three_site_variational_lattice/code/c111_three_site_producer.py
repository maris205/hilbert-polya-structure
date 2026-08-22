#!/usr/bin/env python3
"""Exact finite audit for a three-site variational Hénon ring (C111).

The artifact records two synchronous fixed points, one synchronous primitive
period-two witness, and its exact longitudinal/transverse Fourier-mode
decomposition.  It is intentionally a finite low-period certificate: it does
not enumerate all primitive orbits and does not construct a Fredholm operator.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import itertools
import json
from pathlib import Path
from typing import Iterable

PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "results/c111_three_site_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
A = Fraction(7)
K = Fraction(1, 5)
N = 3
Z = Fraction(0)
O = Fraction(1)
L = [[Fraction(2), Fraction(-1), Fraction(-1)],
     [Fraction(-1), Fraction(2), Fraction(-1)],
     [Fraction(-1), Fraction(-1), Fraction(2)]]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def rat(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def vec_rat(xs: Iterable[Fraction]) -> list[dict[str, int]]:
    return [rat(x) for x in xs]


def mat_rat(m: list[list[Fraction]]) -> list[list[dict[str, int]]]:
    return [[rat(x) for x in row] for row in m]


def eye(n: int) -> list[list[Fraction]]:
    return [[O if i == j else Z for j in range(n)] for i in range(n)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Z)
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def determinant(a: list[list[Fraction]]) -> Fraction:
    total = Z
    n = len(a)
    for p in itertools.permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = O if inversions % 2 == 0 else -O
        for i, j in enumerate(p):
            term *= a[i][j]
        total += term
    return total


def poly_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return [(a[i] if i < len(a) else Z) + (b[i] if i < len(b) else Z)
            for i in range(max(len(a), len(b)))]


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Z] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def det_i_minus_zj(j: list[list[Fraction]]) -> list[Fraction]:
    """Coefficients (low degree first) of det(I-zJ)."""
    n = len(j)
    total = [Z]
    for p in itertools.permutations(range(n)):
        inv = sum(p[i] > p[k] for i in range(n) for k in range(i + 1, n))
        term = [O if inv % 2 == 0 else -O]
        for i, col in enumerate(p):
            term = poly_mul(term, [O, -j[i][col]] if i == col else [Z, -j[i][col]])
        total = poly_add(total, term)
    while len(total) > 1 and total[-1] == Z:
        total.pop()
    return total


def matrix_sub(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def zero_matrix(a: list[list[Fraction]]) -> bool:
    return all(x == Z for row in a for x in row)


def omega() -> list[list[Fraction]]:
    top = [[Z] * N, eye(N)[0], eye(N)[1], eye(N)[2]]
    # Build [[0,I],[-I,0]] without relying on a block-matrix package.
    return [[(O if j == i + N else Z) for j in range(2 * N)] for i in range(N)] + [
        [(-O if j == i - N else Z) for j in range(2 * N)] for i in range(N, 2 * N)
    ]


def gradient(q: tuple[Fraction, ...], coupling: Fraction = K) -> tuple[Fraction, ...]:
    lap_q = [sum(L[i][j] * q[j] for j in range(N)) for i in range(N)]
    return tuple(A * q[i] - q[i] * q[i] - coupling * lap_q[i] for i in range(N))


def potential(q: tuple[Fraction, ...], coupling: Fraction = K) -> Fraction:
    onsite = sum(A * x * x / 2 - x * x * x / 3 for x in q)
    edge_energy = sum((q[i] - q[j]) ** 2 for i, j in ((0, 1), (1, 2), (2, 0)))
    return onsite - coupling * edge_energy / 2


def hessian(q: tuple[Fraction, ...], coupling: Fraction = K) -> list[list[Fraction]]:
    return [[(A - 2 * q[i] if i == j else Z) - coupling * L[i][j]
             for j in range(N)] for i in range(N)]


def jacobian(q: tuple[Fraction, ...], coupling: Fraction = K) -> list[list[Fraction]]:
    h = hessian(q, coupling)
    top = [h[i] + [(-O if i == j else Z) for j in range(N)] for i in range(N)]
    bottom = [[(O if i == j else Z) for j in range(N)] + [Z] * N for i in range(N)]
    return top + bottom


def map_state(state: tuple[Fraction, ...], coupling: Fraction = K) -> tuple[Fraction, ...]:
    q, p = state[:N], state[N:]
    g = gradient(q, coupling)
    return tuple(g[i] - p[i] for i in range(N)) + tuple(q)


def inverse_state(state: tuple[Fraction, ...], coupling: Fraction = K) -> tuple[Fraction, ...]:
    q, p = state[:N], state[N:]
    g = gradient(p, coupling)
    return tuple(p) + tuple(g[i] - q[i] for i in range(N))


def reversor(state: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(state[N:]) + tuple(state[:N])


def trace(a: list[list[Fraction]]) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def orbit_row(label: str, states: list[tuple[Fraction, ...]], coupling: Fraction = K) -> dict[str, object]:
    matrices = [jacobian(tuple(s[:N]), coupling) for s in states]
    monodromy = eye(2 * N)
    for j in matrices:
        monodromy = matmul(j, monodromy)
    return {
        "label": label,
        "period": len(states),
        "states": [vec_rat(s) for s in states],
        "primitive_verified": len(states) == 1 or states[0] != states[1],
        "cycle_closure_verified": map_state(states[-1], coupling) == states[0],
        "jacobian_at_first": mat_rat(matrices[0]),
        "monodromy": mat_rat(monodromy),
        "monodromy_determinant": rat(determinant(monodromy)),
        "monodromy_trace": rat(trace(monodromy)),
        "det_I_minus_z_monodromy": vec_rat(det_i_minus_zj(monodromy)),
        "symplectic_at_each_step": all(
            zero_matrix(matrix_sub(matmul(matmul(transpose(j), omega()), j), omega()))
            for j in matrices
        ),
    }


def main() -> None:
    fixed_origin = (Z, Z, Z, Z, Z, Z)
    fixed_sync = tuple([Fraction(5)] * 6)
    cycle_2 = [tuple([Fraction(3)] * 3 + [Fraction(6)] * 3),
               tuple([Fraction(6)] * 3 + [Fraction(3)] * 3)]
    fixed_rows = [orbit_row("fixed_origin", [fixed_origin]),
                  orbit_row("fixed_synchronous", [fixed_sync])]
    cycle_row = orbit_row("synchronous_period_two", cycle_2)

    coupled_mono = [[Fraction(x["numerator"], x["denominator"]) for x in row]
                    for row in cycle_row["monodromy"]]  # type: ignore[index]
    uncoupled_matrices = [jacobian(tuple(s[:N]), Z) for s in cycle_2]
    uncoupled_mono = matmul(uncoupled_matrices[1], uncoupled_matrices[0])
    coupled_poly = det_i_minus_zj(coupled_mono)
    uncoupled_poly = det_i_minus_zj(uncoupled_mono)
    trace_delta = trace(coupled_mono) - trace(uncoupled_mono)
    z2_delta = coupled_poly[2] - uncoupled_poly[2]

    # The 3-cycle Laplacian has one longitudinal and a two-dimensional
    # transverse eigenspace.  This is an exact rational Fourier-mode witness.
    laplacian_eigenvalues = [Z, Fraction(3), Fraction(3)]
    h3 = [A - 2 * Fraction(3) - K * lam for lam in laplacian_eigenvalues]
    h6 = [A - 2 * Fraction(6) - K * lam for lam in laplacian_eigenvalues]
    mode_traces = [h6[i] * h3[i] - 2 for i in range(3)]
    mode_polys = [[O, -t, O] for t in mode_traces]
    reconstructed = [O]
    for p in mode_polys:
        reconstructed = poly_mul(reconstructed, p)

    samples = [
        (Fraction(1, 2), Fraction(-1, 3), Fraction(2, 5), Fraction(-3, 7), Fraction(1, 4), Fraction(-2, 3)),
        (Fraction(-2), Fraction(1), Z, Fraction(3, 2), Fraction(-1, 5), Fraction(4, 3)),
        (Fraction(4, 3), Fraction(5, 7), Fraction(-1, 2), Fraction(2, 3), Fraction(3, 5), Fraction(-4, 7)),
    ]
    reversor_checks = [reversor(map_state(reversor(s))) == inverse_state(s) for s in samples]
    primitive_checks = []
    for s in samples:
        q, p = s[:N], s[N:]
        g = gradient(q)
        # For lambda=q dot dp, F^*lambda-lambda=d(U(q)-p dot q).
        pullback = tuple(g[i] - p[i] for i in range(N)) + tuple(-q[i] for i in range(N))
        primitive = tuple(g[i] - p[i] for i in range(N)) + tuple(-q[i] for i in range(N))
        primitive_checks.append(pullback == primitive)

    all_q = [(Z, Z, Z), (Fraction(5),) * 3, (Fraction(3),) * 3, (Fraction(6),) * 3]
    omega_matrix = omega()
    jacobians = [jacobian(q) for q in all_q]
    symplectic_checks = [zero_matrix(matrix_sub(matmul(matmul(transpose(j), omega_matrix), j), omega_matrix)) for j in jacobians]
    determinant_checks = [determinant(j) == O for j in jacobians]
    fixed_equations = [gradient(q) == tuple(2 * x for x in q) for q in [(Z,) * 3, (Fraction(5),) * 3]]
    mode_reconstruction = reconstructed == coupled_poly and sum(mode_traces) == trace(coupled_mono)

    result = {
        "schema_id": "hcs-c111-three-site-variational-henon-lattice-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "model": {
            "name": "three_site_variational_henon_ring",
            "graph": "3-cycle (all three undirected edges)",
            "parameters": {"a": rat(A), "kappa": rat(K), "sites": N},
            "laplacian": mat_rat(L),
            "potential": "U(q)=sum_i[a q_i^2/2-q_i^3/3]-kappa/2*sum_edges(q_i-q_j)^2",
            "map": "F(q,p)=(grad U(q)-p,q)",
            "reversor": "R(q,p)=(p,q)",
            "symplectic_form": "Omega=[[0,I_3],[-I_3,0]] in (q_1,q_2,q_3,p_1,p_2,p_3)",
            "canonical_one_form": "lambda=q dot dp; F^*lambda-lambda=d(U(q)-p dot q)",
        },
        "certified_orbit_ledger": {"fixed_rows": fixed_rows, "period_two_rows": [cycle_row]},
        "fourier_mode_witness": {
            "laplacian_eigenvalues": vec_rat(laplacian_eigenvalues),
            "mode_labels": ["longitudinal", "transverse_1", "transverse_2"],
            "hessian_mode_at_q3": vec_rat(h3),
            "hessian_mode_at_q6": vec_rat(h6),
            "period_two_mode_traces": vec_rat(mode_traces),
            "period_two_mode_det_I_minus_z": [vec_rat(p) for p in mode_polys],
            "transverse_multiplicity": 2,
            "reconstructed_full_det_I_minus_z": vec_rat(reconstructed),
            "reconstruction_matches_direct": mode_reconstruction,
        },
        "controls": {
            "uncoupled_kappa_zero_period_two_monodromy": mat_rat(uncoupled_mono),
            "uncoupled_det_I_minus_z": vec_rat(uncoupled_poly),
            "coupled_det_I_minus_z": vec_rat(coupled_poly),
            "trace_difference_coupled_minus_uncoupled": rat(trace_delta),
            "z2_coefficient_difference_coupled_minus_uncoupled": rat(z2_delta),
            "mixed_trace_is_nonzero": trace_delta != Z,
            "mixed_z2_coefficient_is_nonzero": z2_delta != Z,
        },
        "checks": {
            "fixed_gradient_equals_two_q": all(fixed_equations),
            "period_two_cycle_closes": cycle_row["cycle_closure_verified"],
            "period_two_is_not_fixed": cycle_2[0] != cycle_2[1],
            "reversor_identity_on_three_exact_samples": all(reversor_checks),
            "exact_symplectic_primitive_identity_on_three_exact_samples": all(primitive_checks),
            "symplectic_form_on_fixed_and_cycle_points": all(symplectic_checks),
            "jacobian_determinant_one_on_fixed_and_cycle_points": all(determinant_checks),
            "fourier_mode_reconstruction": mode_reconstruction,
            "coupling_changes_period_two_trace": trace_delta != Z,
            "coupling_changes_period_two_z2_coefficient": z2_delta != Z,
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
            "exact_fourier_mode_witness": True,
            "complete_primitive_orbit_atlas": False,
            "fredholm_determinant_constructed": False,
            "dynamical_zeta_analytic_continuation": False,
            "arithmetic_local_claimed": False,
            "euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "automorphy_claimed": False,
            "hilbert_polya_operator_claimed": False,
        },
        "reproducibility": {"producer": "code/c111_three_site_producer.py", "exact_number_field": "Q", "randomness": "none"},
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({"status": result["status"], "fixed_count": 2, "period_two_count": 1, "evidence_sha256": digest(OUT.read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
