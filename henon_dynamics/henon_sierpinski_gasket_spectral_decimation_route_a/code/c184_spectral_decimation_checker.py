#!/usr/bin/env python3
"""Producer-independent exact and finite-graph checker for HCS-C184."""
from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c184_spectral_decimation_evidence.json"
EXPECTED_COMMIT = "908a6818caedb0c46195a591873a2ac9c685b55e"
EXPECTED_EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EXPECTED_PATH_BASE = "henon_dynamics/henon_sierpinski_gasket_spectral_decimation_route_a"


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def edge_copy_graph(level: int):
    """Independent IFS edge-copy construction, not the producer triangle recursion."""
    scale = 1
    edges = {
        tuple(sorted(((0, 0), (1, 0)))),
        tuple(sorted(((0, 0), (0, 1)))),
        tuple(sorted(((1, 0), (0, 1)))),
    }
    for _ in range(level):
        refined = set()
        for shift in ((0, 0), (scale, 0), (0, scale)):
            for u, v in edges:
                uu = (u[0] + shift[0], u[1] + shift[1])
                vv = (v[0] + shift[0], v[1] + shift[1])
                refined.add(tuple(sorted((uu, vv))))
        edges = refined
        scale *= 2
    vertices = sorted({vertex for edge in edges for vertex in edge})
    boundary = {(0, 0), (scale, 0), (0, scale)}
    interior = sorted(set(vertices) - boundary)
    index = {vertex: position for position, vertex in enumerate(interior)}
    degree = defaultdict(int)
    matrix = [[0 for _ in interior] for _ in interior]
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
        if u in index and v in index:
            matrix[index[u]][index[v]] = matrix[index[v]][index[u]] = -1
    for vertex, position in index.items():
        matrix[position][position] = degree[vertex]
    return vertices, interior, edges, degree, matrix


def convolve(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def factor_power(root: int, power: int) -> list[int]:
    result = [1]
    base = [-root, 1]
    for _ in range(power):
        result = convolve(result, base)
    return result


def substitute_quadratic(coefficients: list[int]) -> list[int]:
    powers = [[1]]
    quadratic = [0, 5, -1]
    for _ in range(1, len(coefficients)):
        powers.append(convolve(powers[-1], quadratic))
    result = [0] * len(powers[-1])
    for coefficient, power in zip(coefficients, powers):
        for degree, value in enumerate(power):
            result[degree] += coefficient * value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def synthetic_remove_two(coefficients: list[int], times: int) -> list[int]:
    result = coefficients[:]
    for _ in range(times):
        descending = result[::-1]
        quotient = [descending[0]]
        for value in descending[1:-1]:
            quotient.append(value + 2 * quotient[-1])
        if descending[-1] + 2 * quotient[-1] != 0:
            raise AssertionError("missing exceptional cancellation")
        result = quotient[::-1]
    return result


def reconstructed_polynomials(max_level: int) -> dict[int, list[int]]:
    result = {1: convolve([-2, 1], convolve([-5, 1], [-5, 1]))}
    for level in range(2, max_level + 1):
        old = result[level - 1]
        current = substitute_quadratic(old)
        previous_six = (3 ** (level - 1) - 3) // 2 if level >= 3 else 0
        current = synthetic_remove_two(current, previous_six)
        current = convolve(current, factor_power(5, (3 ** (level - 1) + 3) // 2))
        current = convolve(current, factor_power(6, (3**level - 3) // 2))
        if ((3**level - 3) // 2) % 2:
            current = [-value for value in current]
        result[level] = current
    return result


def branch(value: float, symbol: str) -> float:
    return (5.0 + (-1.0 if symbol == "-" else 1.0) * sqrt(25.0 - 4.0 * value)) / 2.0


def expand(seed: float, count: int):
    states = [(seed, "")]
    for _ in range(count):
        next_states = []
        for value, word in states:
            for symbol in ("-", "+"):
                next_states.append((branch(value, symbol), word + symbol))
        states = next_states
    return states


def expected_lineages(level: int) -> list[dict]:
    rows = []
    for value, word in expand(2.0, level - 1):
        rows.append({"series": "2-series", "birth_generation": 1, "seed": 2,
                     "forced_three": False, "branch_word": word or "birth",
                     "eigenvalue_decimal": format(value, ".15g"), "multiplicity": 1})
    for birth in range(1, level + 1):
        for value, word in expand(5.0, level - birth):
            rows.append({"series": "5-series", "birth_generation": birth, "seed": 5,
                         "forced_three": False, "branch_word": word or "birth",
                         "eigenvalue_decimal": format(value, ".15g"),
                         "multiplicity": (3 ** (birth - 1) + 3) // 2})
    for birth in range(2, level + 1):
        multiplicity = (3**birth - 3) // 2
        if birth == level:
            states = [(6.0, "birth")]
            forced = False
        else:
            states = [(value, "3" + word) for value, word in expand(3.0, level - birth - 1)]
            forced = True
        for value, word in states:
            rows.append({"series": "6-series", "birth_generation": birth, "seed": 6,
                         "forced_three": forced, "branch_word": word,
                         "eigenvalue_decimal": format(value, ".15g"), "multiplicity": multiplicity})
    return rows


def bareiss_determinant(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    size = len(work)
    if size == 0:
        return 1
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            swap = next((row for row in range(pivot_index + 1, size) if work[row][pivot_index]), None)
            if swap is None:
                return 0
            work[pivot_index], work[swap] = work[swap], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for i in range(pivot_index + 1, size):
            for j in range(pivot_index + 1, size):
                numerator = work[i][j] * pivot - work[i][pivot_index] * work[pivot_index][j]
                if numerator % previous:
                    raise AssertionError("Bareiss exact division failed")
                work[i][j] = numerator // previous
            work[i][pivot_index] = 0
        previous = pivot
    return sign * work[-1][-1]


def evaluate(coefficients: list[int], value: int) -> int:
    answer = 0
    for coefficient in reversed(coefficients):
        answer = answer * value + coefficient
    return answer


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    assertions = 0

    def check(condition: bool, message: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    check(data["schema"] == "HCS-C184-v1", "schema")
    check(data["candidate_id"] == "HCS-C184", "candidate")
    check(data["date_utc"] == "2026-08-26", "date")
    check(data["source_commit"] == EXPECTED_COMMIT, "source commit")
    check(data["artifact_path_base"] == EXPECTED_PATH_BASE, "artifact path base")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["evaluator"] == {"authority_path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "authority_sha256": EXPECTED_EVALUATOR}, "evaluator")
    check(data["payload_sha256"] == canonical_hash(data), "payload hash")
    check(data["source_lock"] == {
        "object": "standard unnormalized graph Laplacian on V_m with the three boundary corners removed",
        "family": "every pre-gasket level m>=1 with Dirichlet boundary values at V_0",
        "arithmetic_origin": "absent; level, branch, and multiplicity data carry no intrinsic rational-prime semantics",
        "clock": "one graph-refinement level for spectral decimation; this is not physical time",
        "normalization": "L_m has full-graph degree on the diagonal and minus one on adjacent interior vertices",
        "determinant_convention": "chi_m(t)=det(tI-L_m), det(L_m), heat trace Tr(exp(-uL_m)), and finite spectral zeta sum(lambda^(-s))",
        "cutoff": "all-level proof; exact coefficient and graph regression uses 1<=m<=5",
        "precision": "integer polynomial and multiplicity identities; IEEE-754 diagonalization is regression only with error below 1e-10",
        "allowed_data": "pre-gasket adjacency, spectral-decimation branches, exact multiplicities, and one verified classical source",
        "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
    }, "source lock")
    check(data["all_level_theorem"]["renormalization_map"] == "R(t)=t(5-t)", "renormalization map")
    check(data["all_level_theorem"]["exceptional_values"] == [2, 5, 6], "exceptional values")
    check("forced to 3" in data["all_level_theorem"]["six_series"], "forced 6-series branch")
    check("(t-2)^b_(m-1)" in data["all_level_theorem"]["characteristic_recurrence"], "characteristic cancellation")
    check("2^((3^m-1)/2)" in data["all_level_theorem"]["determinant"], "determinant theorem")
    check("not an autonomous physical-time map" in data["all_level_theorem"]["owner_boundary"], "owner boundary")

    expected_route = {
        "A0": "A0_FAIL", "A0_qualification": "LEVEL_AND_SPECTRAL_BRANCH_DATA_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
        "A1": "A1_FAIL", "A1_qualification": "THE_INVERSE_BRANCH_TREE_IS_LEVEL_RENORMALIZATION_NOT_A_PHYSICAL_TIME_PRIMITIVE_ORBIT_OWNER",
        "A2": "A2_FAIL", "A2_qualification": "FINITE_LAPLACIAN_DETERMINANTS_HAVE_NO_TARGET_DIVISOR_MATCH",
        "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE", "A3_qualification": "EXACT_FINITE_SPECTRAL_ZETA_AND_DETERMINANT_STRUCTURE_ONLY_WITH_NO_TARGET_FUNCTIONAL_EQUATION",
        "A4": "A4_FORMAL_HINT", "A4_qualification": "THE_SELF_ADJOINT_LAPLACIAN_HAS_A_CANONICAL_UNITARY_EXPONENTIAL_BUT_REFINEMENT_LEVEL_IS_NOT_ITS_TIME_CLOCK",
        "overall": "ROUTE_A_REJECTED", "a0_failure_forces_rejection": True, "route_b_invocation_allowed": False,
    }
    check(data["route_a_verdict"] == expected_route, "Route-A ledger")
    check(data["scope_flags"] == {
        "used_target_zero_table": False, "used_target_prime_table": False,
        "used_arithmetic_local_data": False, "claimed_target_divisor_match": False,
        "claimed_target_functional_equation": False, "claimed_infinite_gasket_spectral_zeta": False,
        "claimed_level_as_physical_time": False, "claimed_hilbert_polya": False,
        "route_b_invocation_allowed": False,
    }, "scope flags")
    check(set(data["integrity_modes"].values()) == {"CLEAR"} and len(data["integrity_modes"]) == 7, "seven integrity modes")
    source = data["source_registry"]
    check(source == [{
        "key": "fukushima_shima_1992_sierpinski",
        "title": "On a spectral analysis for the Sierpiński gasket",
        "authors": "Masatoshi Fukushima and Tadashi Shima",
        "journal": "Potential Analysis", "volume": 1, "issue": 1,
        "pages": "1-35", "year": 1992, "doi": "10.1007/BF00249784",
        "role": "classical ownership of the finite-gasket spectral-decimation method and complete spectrum",
    }], "complete source registry")
    check(data["nonclaims"] == [
        "universal novelty or priority for spectral decimation, the 2/5/6 series, or their multiplicities",
        "interpretation of the inverse-branch genealogy as autonomous physical-time dynamics",
        "an infinite-gasket spectral-zeta theorem or regularized determinant",
        "rational-prime semantics for levels, branch words, eigenvalues, or multiplicities",
        "a target divisor, Gamma factor, functional equation, counting law, or Weil compression",
        "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
    ], "complete nonclaim ledger")

    replay = data["finite_regression"]
    check(replay["level_min"] == 1 and replay["level_max"] == 5, "level range")
    check(replay["level_row_count"] == len(replay["level_rows"]) == 5, "level rows")
    check(replay["lineage_row_count"] == len(replay["lineage_rows"]) == 103, "lineage rows")
    check(replay["characteristic_coefficient_cells"] == 542, "coefficient cells")
    check(replay["graph_eigenvalue_cells"] == 537, "graph eigenvalue cells")
    polynomials = reconstructed_polynomials(5)
    evidence_lineages = defaultdict(list)
    for row in replay["lineage_rows"]:
        evidence_lineages[row["level"]].append({key: value for key, value in row.items() if key != "level"})

    for level, level_row in enumerate(replay["level_rows"], 1):
        dimension = (3 ** (level + 1) - 3) // 2
        full_vertices = (3 ** (level + 1) + 3) // 2
        expected = expected_lineages(level)
        check(level_row["level"] == level, "level label")
        check(level_row["full_vertex_count"] == full_vertices, "full vertex formula")
        check(level_row["boundary_vertex_count"] == 3, "boundary count")
        check(level_row["interior_dimension"] == dimension, "interior dimension")
        check(level_row["multiplicity_sum"] == dimension, "dimension closure")
        check(level_row["lineage_count"] == len(expected), "lineage count")
        check(level_row["heat_trace_at_zero"] == dimension, "heat at zero")
        check(level_row["negative_heat_trace_derivative_at_zero"] == 4 * dimension, "heat derivative")
        check(level_row["spectral_zeta_at_zero"] == dimension, "zeta at zero")
        check(evidence_lineages[level] == expected, "complete lineage ledger")
        for recorded, rebuilt in zip(evidence_lineages[level], expected):
            for field in ("series", "birth_generation", "seed", "forced_three", "branch_word", "multiplicity"):
                check(recorded[field] == rebuilt[field], f"lineage {field}")
            check(abs(float(recorded["eigenvalue_decimal"]) - float(rebuilt["eigenvalue_decimal"])) < 1e-13, "lineage value")

        coefficients = list(map(int, level_row["characteristic_polynomial_coefficients_ascending"]))
        check(coefficients == polynomials[level], "characteristic coefficients")
        check(level_row["characteristic_polynomial_degree"] == dimension == len(coefficients) - 1, "characteristic degree")
        for got, wanted in zip(coefficients, polynomials[level]):
            check(got == wanted, "coefficient cell")
        raw = ",".join(map(str, coefficients)).encode()
        check(level_row["characteristic_polynomial_coefficients_sha256"] == sha256(raw).hexdigest(), "coefficient hash")

        exponents = {
            "prime_2": (3**level - 1) // 2,
            "prime_3": (3 ** (level + 1) - 6 * level - 3) // 4,
            "prime_5": (3**level + 6 * level - 1) // 4,
        }
        determinant = 2 ** exponents["prime_2"] * 3 ** exponents["prime_3"] * 5 ** exponents["prime_5"]
        check(level_row["determinant_prime_exponents"] == exponents, "determinant exponents")
        check(level_row["determinant"] == str(determinant), "determinant value")
        check(coefficients[0] == (-1) ** dimension * determinant, "determinant constant")
        check(float(level_row["graph_diagonalization_max_abs_error"]) < float(level_row["graph_diagonalization_error_bound"]) == 1e-10, "recorded diagonalization bound")

        vertices, interior, edges, degrees, integer_matrix = edge_copy_graph(level)
        check(len(vertices) == full_vertices and len(interior) == dimension, "independent graph counts")
        check(len(edges) == level_row["edge_count"], "independent edge count")
        for vertex in interior:
            check(degrees[vertex] == 4, "interior degree four")
        for row in integer_matrix:
            check(sum(value != 0 for value in row) >= 1, "nonempty Laplacian row")
        numeric_matrix = np.array(integer_matrix, dtype=float)
        numerical = np.linalg.eigvalsh(numeric_matrix)
        theoretical = sorted(float(row["eigenvalue_decimal"]) for row in expected for _ in range(row["multiplicity"]))
        check(len(numerical) == len(theoretical), "numeric spectrum dimension")
        for got, wanted in zip(numerical, theoretical):
            check(abs(got - wanted) < 1e-10, "numeric eigenvalue regression")
        check(abs(sum(numerical) - 4 * dimension) < 1e-9, "numeric trace regression")
        if level <= 4:
            check(bareiss_determinant(integer_matrix) == determinant, "independent exact determinant")
        if level <= 3:
            for probe in range(-2, 9):
                shifted = [[(probe if i == j else 0) - integer_matrix[i][j] for j in range(dimension)] for i in range(dimension)]
                check(bareiss_determinant(shifted) == evaluate(coefficients, probe), "graph characteristic probe")

    print(json.dumps({"status": "C184_CHECKER_PASS", "assertions": assertions}, sort_keys=True))


if __name__ == "__main__":
    main()
