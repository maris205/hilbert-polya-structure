#!/usr/bin/env python3
"""Producer-independent semantic checker for HCS-C196.

The producer uses LAPACK Hermitian diagonalization.  This checker never
imports it: pencil spectra come from a hand-written Jacobi algorithm on the
realification of a complex Hermitian matrix, intercepts come from polynomial
spectral projectors, and velocities come from centered pencil differences.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import copysign, hypot, sqrt
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c196_calogero_moser_evidence.json"
EXPECTED_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EXPECTED_EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EXPECTED_SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED_ROUTE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
EXPECTED_TIMES = [-64, -16, -4, 0, 4, 16, 64]
EXPECTED_T = 256
EXPECTED_SECTION_HASHES = {
    "source_lock": "a93c950df2fe90895f63787e626c1b2f005b5447d9ca77838bdd118e4c695207",
    "attribution": "43c087d3caa5f11f12ac37196f730173e92d11086d797636a63ade670eb15ebe",
    "theorem": "bda329f66d78d7362db58fcc4cd10ad41b896e3e1db65d2f0014ebbc9410bec6",
    "progress_and_boundary": "78c68177ad10e48820ce9f19af9a21acc5b2fa438b40bab17e682865ce4c739c",
    "route_a": "832244833a55fdf5af8c3e778354f8e865af27ce05fa2ff2d8e90aa911d72c71",
    "scope_flags": "4d9ce4c0c3b6e4006ce12975342eb0a372aba0b6ca7e0ea1650f709cc69658f8",
    "source_registry": "db7c5485e048059fc7d8d0d75da5d739e497d18e880bb69b4af7e9cd6bb1ef2a",
    "nonclaims": "ee3d9856372d3b77c929de35b846dc21c1bf9345c7fa4b451aa599a8b6094f28",
}
EXPECTED_TOP_LEVEL_KEYS = {
    "attribution", "candidate_id", "date_utc", "evaluator",
    "finite_regression", "nonclaims", "payload_sha256",
    "progress_and_boundary", "route_a", "schema", "scope_flags",
    "scope_literal", "source_commit", "source_lock", "source_registry",
    "theorem",
}
EXPECTED_FINITE_KEYS = {
    "asymptotic_time", "case_count", "exact_commutator_entry_check_count",
    "exact_hermitian_entry_check_count", "exact_trace_and_energy_check_count",
    "maximum_atlas_matrix_residual", "maximum_inverse_position_residual",
    "maximum_negative_position_error_at_T",
    "maximum_negative_velocity_error_at_T",
    "maximum_positive_position_error_at_T",
    "maximum_positive_velocity_error_at_T",
    "maximum_sampled_newton_residual", "minimum_sampled_pencil_gap",
    "n_values", "pencil_row_count", "role", "rows", "seeds", "time_grid",
}
EXPECTED_ROW_KEYS = {
    "N", "case_id", "exact_commutator_entry_checks",
    "exact_hermitian_entry_checks", "g", "hamiltonian", "p",
    "pencil_rows", "q", "scattering", "seed", "trace_L2_equals_2H",
    "trace_invariants",
}
EXPECTED_PENCIL_KEYS = {
    "minimum_gap", "newton_residual", "positions", "time", "velocities",
}
EXPECTED_SCATTERING_KEYS = {
    "asymptotic_time", "atlas_matrix_max_residual",
    "gauge_overlap_max_error", "incoming_intercept_order",
    "incoming_velocity_order", "intercepts", "inverse_position_max_residual",
    "negative_position_max_error", "negative_velocity_max_error",
    "ordered_velocities", "outgoing_intercept_order",
    "outgoing_velocity_order", "positive_position_max_error",
    "positive_velocity_max_error",
}


class Counter:
    def __init__(self) -> None:
        self.value = 0

    def check(self, condition: bool, message: str) -> None:
        self.value += 1
        if not condition:
            raise AssertionError(message)


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def section_hash(value) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def parse_fraction(text: str) -> Fraction:
    return Fraction(text)


def format_float(value: float) -> str:
    return f"{float(value):.12e}"


def independent_data(n: int, seed: int) -> tuple[list[Fraction], list[Fraction], Fraction]:
    positions = [Fraction(0)]
    for location in range(1, n):
        positions.append(positions[-1] + Fraction(1 + ((location + 2 * seed) % 3)))
    center = sum(positions, Fraction(0)) / Fraction(n)
    positions = [entry - center for entry in positions]

    momenta = []
    for location in range(n):
        residue = ((location + 1) * (seed + 2)) % (n + 3)
        momenta.append(Fraction(residue, 2) - Fraction(n + seed, 4))
    center_momentum = sum(momenta, Fraction(0)) / Fraction(n)
    momenta = [entry - center_momentum for entry in momenta]
    coupling = (Fraction(1, 2), Fraction(1), Fraction(3, 2))[seed]
    return positions, momenta, coupling


Pair = tuple[Fraction, Fraction]


def add(a: Pair, b: Pair) -> Pair:
    return a[0] + b[0], a[1] + b[1]


def multiply(a: Pair, b: Pair) -> Pair:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gaussian_lax(q: list[Fraction], p: list[Fraction], coupling: Fraction) -> list[list[Pair]]:
    size = len(q)
    return [
        [
            (p[row], Fraction(0)) if row == column
            else (Fraction(0), coupling / (q[row] - q[column]))
            for column in range(size)
        ]
        for row in range(size)
    ]


def exact_traces(matrix: list[list[Pair]]) -> list[Pair]:
    size = len(matrix)
    zero = (Fraction(0), Fraction(0))
    power = [[((Fraction(1), Fraction(0)) if row == column else zero) for column in range(size)] for row in range(size)]
    result: list[Pair] = []
    for _ in range(size):
        next_power = [[zero for _ in range(size)] for _ in range(size)]
        for row in range(size):
            for middle in range(size):
                if power[row][middle] == zero:
                    continue
                for column in range(size):
                    next_power[row][column] = add(
                        next_power[row][column],
                        multiply(power[row][middle], matrix[middle][column]),
                    )
        power = next_power
        trace = zero
        for index in range(size):
            trace = add(trace, power[index][index])
        result.append(trace)
    return result


def numeric_matrices(q: list[Fraction], p: list[Fraction], coupling: Fraction) -> tuple[np.ndarray, np.ndarray]:
    size = len(q)
    qf = np.array([float(value) for value in q])
    Q = np.diag(qf).astype(complex)
    L = np.diag([float(value) for value in p]).astype(complex)
    for row in range(size):
        for column in range(size):
            if row != column:
                L[row, column] = 1j * float(coupling) / (qf[row] - qf[column])
    return Q, L


def jacobi_real_spectrum(matrix: np.ndarray) -> np.ndarray:
    """Eigenvalues via realification and cyclic maximum-pivot Jacobi."""
    real = np.real(matrix)
    imag = np.imag(matrix)
    work = np.block([[real, -imag], [imag, real]]).astype(float)
    dimension = work.shape[0]
    scale = max(1.0, float(np.max(np.abs(work))))
    threshold = 2e-14 * scale
    maximum_iterations = 100 * dimension * dimension
    for _ in range(maximum_iterations):
        upper = np.triu(np.abs(work), 1)
        flat = int(np.argmax(upper))
        row, column = divmod(flat, dimension)
        if float(upper[row, column]) <= threshold:
            break
        off = work[row, column]
        app = work[row, row]
        aqq = work[column, column]
        tau = (aqq - app) / (2.0 * off)
        if tau == 0.0:
            tangent = 1.0
        else:
            tangent = copysign(1.0, tau) / (abs(tau) + hypot(1.0, tau))
        cosine = 1.0 / sqrt(1.0 + tangent * tangent)
        sine = tangent * cosine
        for k in range(dimension):
            if k == row or k == column:
                continue
            old_row = work[k, row]
            old_column = work[k, column]
            new_row = cosine * old_row - sine * old_column
            new_column = sine * old_row + cosine * old_column
            work[k, row] = work[row, k] = new_row
            work[k, column] = work[column, k] = new_column
        work[row, row] = cosine * cosine * app - 2 * sine * cosine * off + sine * sine * aqq
        work[column, column] = sine * sine * app + 2 * sine * cosine * off + cosine * cosine * aqq
        work[row, column] = work[column, row] = 0.0
    else:
        raise AssertionError("Jacobi eigensolver failed to converge")
    doubled = np.sort(np.diag(work))
    if np.max(np.abs(doubled[0::2] - doubled[1::2])) > 2e-8 * scale:
        raise AssertionError("realification eigenvalue pairs split")
    return (doubled[0::2] + doubled[1::2]) / 2.0


def spectral_intercepts(Q: np.ndarray, L: np.ndarray, eigenvalues: np.ndarray) -> np.ndarray:
    """Compute Tr(Q P_m) using Lagrange polynomial projectors."""
    size = len(eigenvalues)
    identity = np.eye(size, dtype=complex)
    result = []
    for index, eigenvalue in enumerate(eigenvalues):
        projector = identity.copy()
        for other, other_value in enumerate(eigenvalues):
            if other == index:
                continue
            projector = projector @ ((L - other_value * identity) / (eigenvalue - other_value))
        result.append(float(np.real(np.trace(Q @ projector))))
    return np.array(result)


def centered_velocity(Q: np.ndarray, L: np.ndarray, time: float, step: float = 2e-4) -> np.ndarray:
    plus = jacobi_real_spectrum(Q + (time + step) * L)
    minus = jacobi_real_spectrum(Q + (time - step) * L)
    return (plus - minus) / (2 * step)


def main() -> None:
    evidence_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(evidence_path.read_text())
    count = Counter()

    count.check(set(data) == EXPECTED_TOP_LEVEL_KEYS, "exact top-level schema")
    count.check(data["payload_sha256"] == canonical_hash(data), "canonical payload hash")
    count.check(data["schema"] == "hcs-c196-calogero-moser-pencil-v1", "schema")
    count.check(data["candidate_id"] == "HCS-C196", "candidate")
    count.check(data["date_utc"] == "2026-08-27", "date")
    count.check(data["source_commit"] == EXPECTED_COMMIT, "source commit")
    count.check(data["scope_literal"] == EXPECTED_SCOPE, "scope literal")
    count.check(data["evaluator"] == {
        "path": "flow_systems/skills/route-a-evaluator.md",
        "version": "0.2.0",
        "sha256": EXPECTED_EVALUATOR,
    }, "evaluator provenance")
    for section, expected_digest in EXPECTED_SECTION_HASHES.items():
        count.check(section_hash(data[section]) == expected_digest, f"semantic section {section}")

    required_source_fragments = {
        "family": "every integer N>=2 and every coupling g>0",
        "clock": "physical Hamiltonian time t in R",
        "hamiltonian": "H=(1/2) sum_j p_j^2 + sum_(j<k) g^2/(q_j-q_k)^2",
        "initial_lax_matrix": "(L_0)_(jk)=p_j delta_(jk)+i g(1-delta_(jk))/(q_j-q_k)",
    }
    for key, expected in required_source_fragments.items():
        count.check(data["source_lock"][key] == expected, f"source lock {key}")
    count.check(len(data["source_lock"]) == 11, "complete source lock")
    count.check(data["attribution"]["status"].startswith("CLASSICAL_MOSER_CALOGERO"), "classical attribution")
    count.check("do not prove" in data["attribution"]["finite_evidence_role"], "finite evidence boundary")
    count.check(len(data["attribution"]) == 5, "attribution field population")
    count.check(len(data["theorem"]) == 9, "theorem field population")
    count.check("rank-one compression" in data["theorem"]["simple_spectrum"], "simplicity theorem")
    count.check("2g^2" in data["theorem"]["global_dynamics"], "force factor")
    count.check("Tr L^2=2H" in data["theorem"]["integrals"], "energy factor")
    count.check("incoming ordered rank N+1-m" in data["theorem"]["ordering_reversal"], "rank reversal")
    count.check("ig/(lambda_b-lambda_a)" in data["theorem"]["scattering_atlas"], "atlas sign")
    count.check(len(data["progress_and_boundary"]) == 6, "boundary population")
    count.check("g=0 permits free crossings" in data["progress_and_boundary"]["degenerate_boundary"], "g=0 boundary")

    count.check(data["route_a"]["tuple"] == EXPECTED_ROUTE, "Route-A tuple")
    count.check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "Route-A overall")
    count.check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B route flag")
    count.check(len(data["route_a"]) == 8, "Route-A population")
    for key, value in data["scope_flags"].items():
        count.check(value is False, f"scope flag {key}")
    count.check(len(data["scope_flags"]) == 11, "scope flag population")
    count.check(len(data["source_registry"]) == 2, "source population")
    count.check(data["source_registry"][0]["doi"] == "10.1063/1.1664820", "Calogero DOI")
    count.check(data["source_registry"][0]["title"] == "Solution of a Three-Body Problem in One Dimension", "Calogero title")
    count.check(data["source_registry"][1]["doi"] == "10.1016/0001-8708(75)90151-6", "Moser DOI")
    count.check(data["source_registry"][1]["title"].startswith("Three integrable Hamiltonian systems"), "Moser title")
    count.check(len(data["nonclaims"]) == 6, "nonclaim population")
    for nonclaim in data["nonclaims"]:
        count.check(len(nonclaim) > 40, "nonclaim substance")

    finite = data["finite_regression"]
    count.check(set(finite) == EXPECTED_FINITE_KEYS, "exact finite-regression schema")
    count.check(finite["role"] == "DETERMINISTIC_FINITE_REGRESSION_NOT_ALL_PARAMETER_PROOF", "finite role")
    count.check(finite["n_values"] == list(range(2, 8)), "N domain")
    count.check(finite["seeds"] == [0, 1, 2], "seed domain")
    count.check(finite["time_grid"] == EXPECTED_TIMES, "time grid")
    count.check(finite["asymptotic_time"] == EXPECTED_T, "asymptotic time")
    count.check(finite["case_count"] == 18, "case count")
    count.check(finite["pencil_row_count"] == 126, "pencil row count")
    count.check(len(finite["rows"]) == 18, "row population")

    total_hermitian = 0
    total_commutator = 0
    total_trace = 0
    all_gaps: list[float] = []
    all_newton: list[float] = []
    all_atlas: list[float] = []
    all_inverse: list[float] = []
    pos_position_errors: list[float] = []
    neg_position_errors: list[float] = []
    pos_velocity_errors: list[float] = []
    neg_velocity_errors: list[float] = []

    for ordinal, row in enumerate(finite["rows"]):
        count.check(set(row) == EXPECTED_ROW_KEYS, "exact case-row schema")
        n = 2 + ordinal // 3
        seed = ordinal % 3
        q, p, coupling = independent_data(n, seed)
        count.check(row["case_id"] == f"N{n}_S{seed}", "case id")
        count.check(row["N"] == n and row["seed"] == seed, "case coordinates")
        count.check([parse_fraction(value) for value in row["q"]] == q, "q data")
        count.check([parse_fraction(value) for value in row["p"]] == p, "p data")
        count.check(parse_fraction(row["g"]) == coupling, "coupling data")
        count.check(all(q[index] < q[index + 1] for index in range(n - 1)), "ordered chamber")
        count.check(sum(p, Fraction(0)) == 0, "centered momentum sentinel")

        L_exact = gaussian_lax(q, p, coupling)
        hermitian = 0
        commutator = 0
        for j in range(n):
            for k in range(n):
                count.check(L_exact[k][j] == (L_exact[j][k][0], -L_exact[j][k][1]), "Hermitian exact")
                hermitian += 1
                difference = q[j] - q[k]
                observed = multiply((difference, Fraction(0)), L_exact[j][k])
                expected = (Fraction(0), coupling if j != k else Fraction(0))
                count.check(observed == expected, "rank-one commutator exact")
                commutator += 1
        count.check(row["exact_hermitian_entry_checks"] == hermitian, "Hermitian check count")
        count.check(row["exact_commutator_entry_checks"] == commutator, "commutator check count")
        total_hermitian += hermitian
        total_commutator += commutator

        kinetic = sum(value * value for value in p) / 2
        potential = sum(
            coupling * coupling / (q[j] - q[k]) ** 2
            for j in range(n) for k in range(j + 1, n)
        )
        energy = kinetic + potential
        count.check(parse_fraction(row["hamiltonian"]) == energy, "Hamiltonian exact")
        traces = exact_traces(L_exact)
        count.check(all(value[1] == 0 for value in traces), "real trace invariants")
        count.check([parse_fraction(value) for value in row["trace_invariants"]] == [value[0] for value in traces], "trace ledger")
        count.check(parse_fraction(row["trace_L2_equals_2H"]) == 2 * energy == traces[1][0], "Tr L2 factor")
        total_trace += n + 1

        Q, L = numeric_matrices(q, p, coupling)
        count.check(np.max(np.abs(L - L.conj().T)) < 1e-14, "numeric Hermitian L")
        count.check(len(row["pencil_rows"]) == len(EXPECTED_TIMES), "case time population")
        for observed_row, time in zip(row["pencil_rows"], EXPECTED_TIMES):
            count.check(set(observed_row) == EXPECTED_PENCIL_KEYS, "exact pencil-row schema")
            count.check(observed_row["time"] == time, "time coordinate")
            positions = jacobi_real_spectrum(Q + time * L)
            stored_positions = np.array([float(value) for value in observed_row["positions"]])
            count.check(np.max(np.abs(positions - stored_positions)) < 3e-9, "Jacobi pencil positions")
            gap = float(np.min(np.diff(positions)))
            count.check(abs(gap - float(observed_row["minimum_gap"])) < 3e-9, "pencil gap")
            velocity = centered_velocity(Q, L, float(time))
            stored_velocity = np.array([float(value) for value in observed_row["velocities"]])
            count.check(np.max(np.abs(velocity - stored_velocity)) < 3e-7, "centered-difference velocity")
            newton = float(observed_row["newton_residual"])
            count.check(0 <= newton < 2e-11, "Newton identity residual bound")
            all_gaps.append(gap)
            all_newton.append(newton)

        scattering = row["scattering"]
        count.check(set(scattering) == EXPECTED_SCATTERING_KEYS, "exact scattering schema")
        lambdas = jacobi_real_spectrum(L)
        stored_lambdas = np.array([float(value) for value in scattering["ordered_velocities"]])
        count.check(np.max(np.abs(lambdas - stored_lambdas)) < 3e-10, "scattering velocities")
        count.check(np.min(np.diff(lambdas)) > 1e-9, "simple L spectrum")
        intercepts = spectral_intercepts(Q, L, lambdas)
        stored_intercepts = np.array([float(value) for value in scattering["intercepts"]])
        count.check(np.max(np.abs(intercepts - stored_intercepts)) < 2e-8, "projector intercepts")
        count.check(float(scattering["gauge_overlap_max_error"]) < 1e-10, "gauge overlap")

        atlas = np.diag(stored_intercepts).astype(complex)
        for a in range(n):
            for b in range(n):
                if a != b:
                    atlas[a, b] = 1j * float(coupling) / (stored_lambdas[b] - stored_lambdas[a])
        inverse_positions = jacobi_real_spectrum(atlas)
        inverse_residual = float(np.max(np.abs(inverse_positions - np.array([float(value) for value in q]))))
        count.check(abs(inverse_residual - float(scattering["inverse_position_max_residual"])) < 3e-9, "inverse atlas")
        atlas_residual = float(scattering["atlas_matrix_max_residual"])
        count.check(0 <= atlas_residual < 2e-11, "atlas identity residual")
        all_atlas.append(atlas_residual)
        all_inverse.append(float(scattering["inverse_position_max_residual"]))

        count.check(scattering["asymptotic_time"] == EXPECTED_T, "case asymptotic time")
        T = float(EXPECTED_T)
        positive_positions = jacobi_real_spectrum(Q + T * L)
        negative_positions = jacobi_real_spectrum(Q - T * L)
        positive_model = T * stored_lambdas + stored_intercepts
        negative_model = -T * stored_lambdas[::-1] + stored_intercepts[::-1]
        pos_error = float(np.max(np.abs(positive_positions - positive_model)))
        neg_error = float(np.max(np.abs(negative_positions - negative_model)))
        count.check(abs(pos_error - float(scattering["positive_position_max_error"])) < 3e-8, "positive asymptotic position")
        count.check(abs(neg_error - float(scattering["negative_position_max_error"])) < 3e-8, "negative asymptotic position")
        positive_velocity = centered_velocity(Q, L, T, 1e-3)
        negative_velocity = centered_velocity(Q, L, -T, 1e-3)
        pos_vel_error = float(np.max(np.abs(positive_velocity - stored_lambdas)))
        neg_vel_error = float(np.max(np.abs(negative_velocity - stored_lambdas[::-1])))
        count.check(abs(pos_vel_error - float(scattering["positive_velocity_max_error"])) < 3e-7, "positive asymptotic velocity")
        count.check(abs(neg_vel_error - float(scattering["negative_velocity_max_error"])) < 3e-7, "negative asymptotic velocity")
        count.check(scattering["incoming_velocity_order"] == list(reversed(scattering["outgoing_velocity_order"])), "velocity order reversal")
        count.check(scattering["incoming_intercept_order"] == list(reversed(scattering["outgoing_intercept_order"])), "intercept order reversal")
        pos_position_errors.append(pos_error)
        neg_position_errors.append(neg_error)
        pos_velocity_errors.append(pos_vel_error)
        neg_velocity_errors.append(neg_vel_error)

    count.check(finite["exact_hermitian_entry_check_count"] == total_hermitian == 417, "aggregate Hermitian count")
    count.check(finite["exact_commutator_entry_check_count"] == total_commutator == 417, "aggregate commutator count")
    count.check(finite["exact_trace_and_energy_check_count"] == total_trace == 99, "aggregate trace count")
    aggregate_pairs = [
        (finite["minimum_sampled_pencil_gap"], min(all_gaps)),
        (finite["maximum_sampled_newton_residual"], max(all_newton)),
        (finite["maximum_atlas_matrix_residual"], max(all_atlas)),
        (finite["maximum_inverse_position_residual"], max(all_inverse)),
        (finite["maximum_positive_position_error_at_T"], max(pos_position_errors)),
        (finite["maximum_negative_position_error_at_T"], max(neg_position_errors)),
        (finite["maximum_positive_velocity_error_at_T"], max(pos_velocity_errors)),
        (finite["maximum_negative_velocity_error_at_T"], max(neg_velocity_errors)),
    ]
    for stored, computed in aggregate_pairs:
        count.check(abs(float(stored) - computed) < 4e-7, "aggregate metric")

    print(json.dumps({
        "status": "C196_CHECKER_PASS",
        "assertions": count.value,
        "cases": len(finite["rows"]),
        "algorithm": "realified-Jacobi spectra plus polynomial projectors plus centered differences",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
