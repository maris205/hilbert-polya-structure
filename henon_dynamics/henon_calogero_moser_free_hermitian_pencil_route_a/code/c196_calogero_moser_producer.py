#!/usr/bin/env python3
"""Produce the deterministic HCS-C196 Calogero--Moser certificate.

The all-N theorem is analytic and source-attributed.  This executable only
regression-tests its frozen signs, factors, Hermitian pencil, and scattering
coordinates on a finite deterministic family.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c196_calogero_moser_evidence.json"
SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
N_VALUES = list(range(2, 8))
SEEDS = list(range(3))
TIME_GRID = [-64, -16, -4, 0, 4, 16, 64]
ASYMPTOTIC_TIME = 256


SOURCE_LOCK = {
    "object": "repulsive rational Calogero--Moser flow in one dimension",
    "family": "every integer N>=2 and every coupling g>0",
    "phase_space": "ordered chamber q_1<...<q_N with real momenta p in R^N",
    "hamiltonian": "H=(1/2) sum_j p_j^2 + sum_(j<k) g^2/(q_j-q_k)^2",
    "clock": "physical Hamiltonian time t in R",
    "initial_lax_matrix": "(L_0)_(jk)=p_j delta_(jk)+i g(1-delta_(jk))/(q_j-q_k)",
    "pencil": "X(t)=Q_0+t L_0 with Q_0=diag(q_1,...,q_N); positions are its increasingly ordered eigenvalues",
    "scattering_normalization": "lambda_1<...<lambda_N are eigenvalues of L_0; eigenvectors v_a are gauged by e^*v_a=1 and a_a=v_a^*Q_0v_a",
    "cutoff": "all-parameter attributed theorem and written proof; finite regression only for 2<=N<=7 and three deterministic seeds",
    "allowed_data": "real rational initial data, Hermitian matrices, exact Gaussian-rational identities, and source-native numerical eigenvalue sentinels",
    "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert--Polya identification, and Route-B inputs",
}

ATTRIBUTION = {
    "status": "CLASSICAL_MOSER_CALOGERO_THEOREM_WITH_PACKAGE_LEVEL_CLOSURE_NOT_NEW_THEOREM_CLAIM",
    "calogero_owner": "Calogero 1969 supplies the inverse-square many-body model in its classical development",
    "moser_owner": "Moser 1975 owns the isospectral and scattering solution used here",
    "package_increment": "one source-locked proof package simultaneously closes pencil simplicity, global completeness, trace integrals, both scattering ends, a global spectral atlas, and absence of bounded nonconstant periodic motion",
    "finite_evidence_role": "the 18 finite systems regression-test conventions and executable identities but do not prove the all-N theorem",
}

THEOREM = {
    "pencil_solution": "for every N>=2, g>0, q_1<...<q_N, and p in R^N, the physical ordered positions are the increasingly ordered eigenvalues of X(t)=Q_0+tL_0 for every real t",
    "simple_spectrum": "X(t) has simple spectrum for every real t, because [X(t),L_0]=ig(J-I) and a repeated eigenspace would force a rank-one compression of J to equal an identity of rank at least two",
    "global_dynamics": "the pencil eigenvalues and their first derivatives form the unique complete collision-free Hamiltonian solution with ddot q_j=2g^2 sum_(k!=j)(q_j-q_k)^(-3)",
    "integrals": "L(t) is unitarily conjugate to L_0, so Tr L(t)^k=Tr L_0^k for every k>=1; in particular Tr L^2=2H",
    "asymptotics": "if lambda_1<...<lambda_N are the simple eigenvalues of L_0 and a_m=v_m^*Q_0v_m with e^*v_m=1, then x_j(t)=t lambda_j+a_j+O(t^(-1)) as t->+infinity and x_j(t)=t lambda_(N+1-j)+a_(N+1-j)+O(|t|^(-1)) as t->-infinity, with velocity errors O(t^(-2))",
    "ordering_reversal": "the spectral line (lambda_m,a_m) has incoming ordered rank N+1-m and outgoing ordered rank m; the intercept attached to that spectral line is unchanged",
    "scattering_atlas": "ordered lambda and arbitrary real a give Q_tilde_(aa)=a_a and Q_tilde_(ab)=ig/(lambda_b-lambda_a); diagonalizing Q_tilde recovers uniquely an ordered Calogero--Moser phase point, giving a global algebraic spectral atlas",
    "aperiodicity": "for N>=2 and g>0 the simple asymptotic velocities are not all equal, so every trajectory is unbounded in relative configuration and no bounded nonconstant periodic orbit exists",
    "quantum_boundary": "the same inverse-square potential has a natural semibounded Schrodinger realization on the ordered chamber, but this is only A4_NATURAL_QUANTIZATION and no target spectrum is identified",
}

PROGRESS_AND_BOUNDARY = {
    "progress": "one paper closes the complete classical free rational flow, all trace integrals, the two-ended scattering map and ordering reversal, a global inverse atlas, and the periodic-orbit obstruction",
    "proof_boundary": "the all-parameter statement follows from the rank-one commutator and Hermitian perturbation proof plus classical source ownership; finite regression is not promoted to proof",
    "degenerate_boundary": "g=0 permits free crossings, repeated initial positions are singular phase points, and N=1 is a trivial free-particle boundary; all are excluded from the main theorem",
    "model_boundary": "confining, trigonometric, hyperbolic, elliptic, spin, complex, and quantum spectral variants are outside the claim",
    "periodic_boundary": "the unbounded continuous flow has no ordinary finite Artin--Mazur orbit census; no prime-orbit or zeta claim is manufactured",
    "operator_boundary": "the natural quantum Hamiltonian supplies only a source-native quantization route, not a Hilbert--Polya operator or target identification",
}

ROUTE_A = {
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
    "overall": "ROUTE_A_REJECTED",
    "A0_qualification": "CONTINUOUS_PARTICLE_LABELS_AND_COUPLING_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
    "A1_qualification": "GLOBAL_SCATTERING_AND_APERIODICITY_SUPPLY_NO_PRIMITIVE_PERIODIC_ORBITS",
    "A2_qualification": "NO_SOURCE_ZETA_OR_TARGET_DIVISOR_ARISES_FROM_THE_FREE_SCATTERING_FLOW",
    "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
    "A4_qualification": "THE_INVERSE_SQUARE_SCHRODINGER_OPERATOR_IS_NATURAL_BUT_HAS_NO_TARGET_SPECTRAL_IDENTIFICATION",
    "route_b_invocation_allowed": False,
}

SCOPE_FLAGS = {
    "used_target_zero_table": False,
    "used_target_prime_table": False,
    "used_arithmetic_local_data": False,
    "claimed_target_divisor_match": False,
    "claimed_target_functional_equation": False,
    "claimed_hilbert_polya": False,
    "claimed_prime_orbit_correspondence": False,
    "claimed_finite_regression_proves_all_N": False,
    "claimed_classical_theorem_novelty": False,
    "claimed_quantum_spectral_theorem": False,
    "route_b_invocation_allowed": False,
}

SOURCE_REGISTRY = [
    {
        "key": "calogero_1969_three_body",
        "title": "Solution of a Three-Body Problem in One Dimension",
        "authors": "F. Calogero",
        "year": 1969,
        "journal": "Journal of Mathematical Physics 10(12), 2191--2196",
        "doi": "10.1063/1.1664820",
        "role": "primary classical source for the inverse-square interacting model",
    },
    {
        "key": "moser_1975_isospectral",
        "title": "Three integrable Hamiltonian systems connected with isospectral deformations",
        "authors": "J. Moser",
        "year": 1975,
        "journal": "Advances in Mathematics 16(2), 197--220",
        "doi": "10.1016/0001-8708(75)90151-6",
        "role": "primary ownership for the rational many-body Lax solution, asymptotics, and scattering coordinates",
    },
]

NONCLAIMS = [
    "novelty or priority for the Calogero model, Moser Lax pair, Hermitian-pencil solution, or classical scattering theorem",
    "the g=0 crossing boundary, singular coincident initial positions, N=1, or any confining/trigonometric/hyperbolic/elliptic/spin variant",
    "a finite periodic-orbit census, Artin--Mazur or Ruelle zeta, prime-orbit correspondence, or arithmetic clock",
    "an all-N theorem inferred from the finite N<=7 regression certificate",
    "a target divisor, functional equation, continuation theorem, counting law, Weil compression, or automorphy statement",
    "a Hilbert--Polya operator, target quantum spectrum, Route-B authorization, external peer review, or acceptance score",
]


Gaussian = tuple[Fraction, Fraction]


def qadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def qsub(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] - right[0], left[1] - right[1]


def qmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def qconj(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def matrix_multiply(left: list[list[Gaussian]], right: list[list[Gaussian]]) -> list[list[Gaussian]]:
    size = len(left)
    zero = (Fraction(0), Fraction(0))
    answer = [[zero for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for column in range(size):
            value = zero
            for middle in range(size):
                value = qadd(value, qmul(left[row][middle], right[middle][column]))
            answer[row][column] = value
    return answer


def exact_lax(q: list[Fraction], p: list[Fraction], coupling: Fraction) -> list[list[Gaussian]]:
    result: list[list[Gaussian]] = []
    for j in range(len(q)):
        row: list[Gaussian] = []
        for k in range(len(q)):
            if j == k:
                row.append((p[j], Fraction(0)))
            else:
                row.append((Fraction(0), coupling / (q[j] - q[k])))
        result.append(row)
    return result


def exact_trace_powers(matrix: list[list[Gaussian]], maximum: int) -> list[Gaussian]:
    size = len(matrix)
    zero = (Fraction(0), Fraction(0))
    identity = [[((Fraction(1), Fraction(0)) if j == k else zero) for k in range(size)] for j in range(size)]
    power = identity
    traces: list[Gaussian] = []
    for _ in range(maximum):
        power = matrix_multiply(power, matrix)
        trace = zero
        for index in range(size):
            trace = qadd(trace, power[index][index])
        traces.append(trace)
    return traces


def rational(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def floating(value: float) -> str:
    if not np.isfinite(value):
        raise ValueError("nonfinite numerical certificate value")
    return f"{float(value):.12e}"


def numerical_matrices(q: list[Fraction], p: list[Fraction], coupling: Fraction) -> tuple[np.ndarray, np.ndarray]:
    q_values = np.array([float(value) for value in q], dtype=float)
    p_values = np.array([float(value) for value in p], dtype=float)
    g_value = float(coupling)
    Q = np.diag(q_values).astype(complex)
    L = np.diag(p_values).astype(complex)
    for j in range(len(q)):
        for k in range(len(q)):
            if j != k:
                L[j, k] = 1j * g_value / (q_values[j] - q_values[k])
    return Q, L


def deterministic_initial_data(n: int, seed: int) -> tuple[list[Fraction], list[Fraction], Fraction]:
    raw_q = [Fraction(0)]
    for index in range(1, n):
        raw_q.append(raw_q[-1] + 1 + ((index + 2 * seed) % 3))
    q_mean = sum(raw_q, Fraction(0)) / n
    q = [value - q_mean for value in raw_q]

    raw_p = [Fraction(((index + 1) * (seed + 2)) % (n + 3), 2) - Fraction(n + seed, 4) for index in range(n)]
    p_mean = sum(raw_p, Fraction(0)) / n
    p = [value - p_mean for value in raw_p]
    coupling = [Fraction(1, 2), Fraction(1), Fraction(3, 2)][seed]
    return q, p, coupling


def phase_gauged_eigenbasis(L: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    lambdas, vectors = np.linalg.eigh(L)
    overlaps = np.sum(vectors, axis=0)
    phases = np.conjugate(overlaps) / np.abs(overlaps)
    vectors = vectors * phases[np.newaxis, :]
    overlaps = np.sum(vectors, axis=0)
    return lambdas, vectors, overlaps


def build_case(n: int, seed: int) -> tuple[dict, dict]:
    q, p, coupling = deterministic_initial_data(n, seed)
    exact_L = exact_lax(q, p, coupling)

    hermitian_checks = 0
    commutator_checks = 0
    for j in range(n):
        for k in range(n):
            assert exact_L[k][j] == qconj(exact_L[j][k])
            hermitian_checks += 1
            left = qmul((q[j], Fraction(0)), exact_L[j][k])
            right = qmul(exact_L[j][k], (q[k], Fraction(0)))
            expected = (Fraction(0), coupling if j != k else Fraction(0))
            assert qsub(left, right) == expected
            commutator_checks += 1

    traces = exact_trace_powers(exact_L, n)
    assert all(value[1] == 0 for value in traces)
    kinetic = sum((value * value for value in p), Fraction(0)) / 2
    potential = sum(
        coupling * coupling / ((q[j] - q[k]) ** 2)
        for j in range(n) for k in range(j + 1, n)
    )
    energy = kinetic + potential
    assert traces[1][0] == 2 * energy

    Q, L = numerical_matrices(q, p, coupling)
    g_value = float(coupling)
    pencil_rows: list[dict] = []
    minimum_gap = float("inf")
    maximum_newton_residual = 0.0
    for time in TIME_GRID:
        X = Q + time * L
        positions, vectors = np.linalg.eigh(X)
        transformed_L = vectors.conj().T @ L @ vectors
        velocities = np.real(np.diag(transformed_L))
        acceleration_perturbation = np.zeros(n)
        acceleration_force = np.zeros(n)
        for j in range(n):
            for k in range(n):
                if j == k:
                    continue
                acceleration_perturbation[j] += 2 * abs(transformed_L[k, j]) ** 2 / (positions[j] - positions[k])
                acceleration_force[j] += 2 * g_value * g_value / (positions[j] - positions[k]) ** 3
        residual = float(np.max(np.abs(acceleration_perturbation - acceleration_force)))
        gap = float(np.min(np.diff(positions)))
        minimum_gap = min(minimum_gap, gap)
        maximum_newton_residual = max(maximum_newton_residual, residual)
        pencil_rows.append({
            "time": time,
            "positions": [floating(value) for value in positions],
            "velocities": [floating(value) for value in velocities],
            "minimum_gap": floating(gap),
            "newton_residual": floating(residual),
        })

    lambdas, vectors, overlaps = phase_gauged_eigenbasis(L)
    assert np.max(np.abs(overlaps - 1)) < 1e-10
    Q_spectral = vectors.conj().T @ Q @ vectors
    intercepts = np.real(np.diag(Q_spectral))
    atlas = np.diag(intercepts).astype(complex)
    for a in range(n):
        for b in range(n):
            if a != b:
                atlas[a, b] = 1j * g_value / (lambdas[b] - lambdas[a])
    atlas_residual = float(np.max(np.abs(Q_spectral - atlas)))
    atlas_q = np.linalg.eigvalsh(atlas)
    inverse_position_residual = float(np.max(np.abs(atlas_q - np.array([float(value) for value in q]))))

    T = float(ASYMPTOTIC_TIME)
    positive_positions, positive_vectors = np.linalg.eigh(Q + T * L)
    negative_positions, negative_vectors = np.linalg.eigh(Q - T * L)
    positive_velocities = np.real(np.diag(positive_vectors.conj().T @ L @ positive_vectors))
    negative_velocities = np.real(np.diag(negative_vectors.conj().T @ L @ negative_vectors))
    positive_model = T * lambdas + intercepts
    negative_model = -T * lambdas[::-1] + intercepts[::-1]
    positive_position_error = float(np.max(np.abs(positive_positions - positive_model)))
    negative_position_error = float(np.max(np.abs(negative_positions - negative_model)))
    positive_velocity_error = float(np.max(np.abs(positive_velocities - lambdas)))
    negative_velocity_error = float(np.max(np.abs(negative_velocities - lambdas[::-1])))

    row = {
        "case_id": f"N{n}_S{seed}",
        "N": n,
        "seed": seed,
        "q": [rational(value) for value in q],
        "p": [rational(value) for value in p],
        "g": rational(coupling),
        "hamiltonian": rational(energy),
        "trace_invariants": [rational(value[0]) for value in traces],
        "trace_L2_equals_2H": rational(traces[1][0]),
        "exact_hermitian_entry_checks": hermitian_checks,
        "exact_commutator_entry_checks": commutator_checks,
        "pencil_rows": pencil_rows,
        "scattering": {
            "ordered_velocities": [floating(value) for value in lambdas],
            "intercepts": [floating(value) for value in intercepts],
            "gauge_overlap_max_error": floating(float(np.max(np.abs(overlaps - 1)))),
            "atlas_matrix_max_residual": floating(atlas_residual),
            "inverse_position_max_residual": floating(inverse_position_residual),
            "asymptotic_time": ASYMPTOTIC_TIME,
            "positive_position_max_error": floating(positive_position_error),
            "negative_position_max_error": floating(negative_position_error),
            "positive_velocity_max_error": floating(positive_velocity_error),
            "negative_velocity_max_error": floating(negative_velocity_error),
            "incoming_velocity_order": [floating(value) for value in lambdas[::-1]],
            "outgoing_velocity_order": [floating(value) for value in lambdas],
            "incoming_intercept_order": [floating(value) for value in intercepts[::-1]],
            "outgoing_intercept_order": [floating(value) for value in intercepts],
        },
    }
    metrics = {
        "minimum_gap": minimum_gap,
        "maximum_newton_residual": maximum_newton_residual,
        "atlas_residual": atlas_residual,
        "inverse_position_residual": inverse_position_residual,
        "positive_position_error": positive_position_error,
        "negative_position_error": negative_position_error,
        "positive_velocity_error": positive_velocity_error,
        "negative_velocity_error": negative_velocity_error,
        "hermitian_checks": hermitian_checks,
        "commutator_checks": commutator_checks,
        "trace_checks": n + 1,
        "pencil_rows": len(pencil_rows),
    }
    return row, metrics


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    rows: list[dict] = []
    metrics: list[dict] = []
    for n in N_VALUES:
        for seed in SEEDS:
            row, case_metrics = build_case(n, seed)
            rows.append(row)
            metrics.append(case_metrics)

    finite = {
        "role": "DETERMINISTIC_FINITE_REGRESSION_NOT_ALL_PARAMETER_PROOF",
        "n_values": N_VALUES,
        "seeds": SEEDS,
        "time_grid": TIME_GRID,
        "asymptotic_time": ASYMPTOTIC_TIME,
        "case_count": len(rows),
        "pencil_row_count": sum(item["pencil_rows"] for item in metrics),
        "exact_hermitian_entry_check_count": sum(item["hermitian_checks"] for item in metrics),
        "exact_commutator_entry_check_count": sum(item["commutator_checks"] for item in metrics),
        "exact_trace_and_energy_check_count": sum(item["trace_checks"] for item in metrics),
        "minimum_sampled_pencil_gap": floating(min(item["minimum_gap"] for item in metrics)),
        "maximum_sampled_newton_residual": floating(max(item["maximum_newton_residual"] for item in metrics)),
        "maximum_atlas_matrix_residual": floating(max(item["atlas_residual"] for item in metrics)),
        "maximum_inverse_position_residual": floating(max(item["inverse_position_residual"] for item in metrics)),
        "maximum_positive_position_error_at_T": floating(max(item["positive_position_error"] for item in metrics)),
        "maximum_negative_position_error_at_T": floating(max(item["negative_position_error"] for item in metrics)),
        "maximum_positive_velocity_error_at_T": floating(max(item["positive_velocity_error"] for item in metrics)),
        "maximum_negative_velocity_error_at_T": floating(max(item["negative_velocity_error"] for item in metrics)),
        "rows": rows,
    }
    result = {
        "schema": "hcs-c196-calogero-moser-pencil-v1",
        "candidate_id": "HCS-C196",
        "date_utc": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "source_lock": SOURCE_LOCK,
        "attribution": ATTRIBUTION,
        "theorem": THEOREM,
        "progress_and_boundary": PROGRESS_AND_BOUNDARY,
        "route_a": ROUTE_A,
        "scope_flags": SCOPE_FLAGS,
        "source_registry": SOURCE_REGISTRY,
        "nonclaims": NONCLAIMS,
        "finite_regression": finite,
    }
    result["payload_sha256"] = sha256(canonical_bytes(result)).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    arguments = parser.parse_args()
    data = build()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C196_PRODUCER_PASS",
        "cases": data["finite_regression"]["case_count"],
        "pencil_rows": data["finite_regression"]["pencil_row_count"],
        "payload_sha256": data["payload_sha256"],
        "output": str(arguments.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
