#!/usr/bin/env python3
"""Produce the exact HCS-C184 finite-gasket spectral certificate."""
from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from math import sqrt
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c184_spectral_decimation_evidence.json"
SOURCE_COMMIT = "908a6818caedb0c46195a591873a2ac9c685b55e"
EVALUATOR_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
LEVEL_MIN, LEVEL_MAX = 1, 5


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def multiply_linear(coefficients: list[int], root: int) -> list[int]:
    """Multiply an ascending coefficient list by (t-root)."""
    answer = [0] * (len(coefficients) + 1)
    for degree, value in enumerate(coefficients):
        answer[degree] -= root * value
        answer[degree + 1] += value
    return answer


def compose_with_R(coefficients: list[int]) -> list[int]:
    """Return p(t(5-t)) by Horner evaluation, ascending coefficients."""
    answer = [0]
    for constant in reversed(coefficients):
        product = [0] * (len(answer) + 2)
        for degree, value in enumerate(answer):
            product[degree + 1] += 5 * value
            product[degree + 2] -= value
        product[0] += constant
        while len(product) > 1 and product[-1] == 0:
            product.pop()
        answer = product
    return answer


def divide_linear_exact(coefficients: list[int], root: int) -> list[int]:
    """Exactly divide an ascending coefficient list by (t-root)."""
    descending = list(reversed(coefficients))
    quotient = [descending[0]]
    for value in descending[1:-1]:
        quotient.append(value + root * quotient[-1])
    remainder = descending[-1] + root * quotient[-1]
    if remainder != 0:
        raise AssertionError("nonexact exceptional-factor division")
    return list(reversed(quotient))


def characteristic_polynomials(max_level: int) -> dict[int, list[int]]:
    coefficients = [1]
    for root in (2, 5, 5):
        coefficients = multiply_linear(coefficients, root)
    result = {1: coefficients}
    for level in range(2, max_level + 1):
        old_dimension = (3**level - 3) // 2
        coefficients = compose_with_R(coefficients)
        previous_six_multiplicity = (3 ** (level - 1) - 3) // 2 if level >= 3 else 0
        for _ in range(previous_six_multiplicity):
            coefficients = divide_linear_exact(coefficients, 2)
        five_birth = (3 ** (level - 1) + 3) // 2
        six_birth = (3**level - 3) // 2
        for _ in range(five_birth):
            coefficients = multiply_linear(coefficients, 5)
        for _ in range(six_birth):
            coefficients = multiply_linear(coefficients, 6)
        if old_dimension % 2:
            coefficients = [-value for value in coefficients]
        result[level] = coefficients
    return result


def inverse_branch(value: float, symbol: str) -> float:
    discriminant = 25.0 - 4.0 * value
    if discriminant < -1e-13:
        raise AssertionError("inverse branch left the real admissible range")
    sign = -1.0 if symbol == "-" else 1.0
    return (5.0 + sign * sqrt(max(0.0, discriminant))) / 2.0


def descendants(seed: float, steps: int):
    states = [(seed, "")]
    for _ in range(steps):
        states = [
            (inverse_branch(value, symbol), word + symbol)
            for value, word in states
            for symbol in ("-", "+")
        ]
    return states


def spectral_lineages(level: int) -> list[dict]:
    rows = []
    for value, word in descendants(2.0, level - 1):
        rows.append({
            "series": "2-series", "birth_generation": 1, "seed": 2,
            "forced_three": False, "branch_word": word or "birth",
            "eigenvalue_decimal": format(value, ".15g"), "multiplicity": 1,
        })
    for birth in range(1, level + 1):
        multiplicity = (3 ** (birth - 1) + 3) // 2
        for value, word in descendants(5.0, level - birth):
            rows.append({
                "series": "5-series", "birth_generation": birth, "seed": 5,
                "forced_three": False, "branch_word": word or "birth",
                "eigenvalue_decimal": format(value, ".15g"), "multiplicity": multiplicity,
            })
    for birth in range(2, level + 1):
        multiplicity = (3**birth - 3) // 2
        if birth == level:
            states = [(6.0, "birth")]
            forced = False
        else:
            states = [(value, "3" + word) for value, word in descendants(3.0, level - birth - 1)]
            forced = True
        for value, word in states:
            rows.append({
                "series": "6-series", "birth_generation": birth, "seed": 6,
                "forced_three": forced, "branch_word": word,
                "eigenvalue_decimal": format(value, ".15g"), "multiplicity": multiplicity,
            })
    return rows


def triangle_graph(level: int):
    scale = 1 << level
    triangles = [((0, 0), (scale, 0), (0, scale))]
    for _ in range(level):
        refined = []
        for left, right, top in triangles:
            lr = ((left[0] + right[0]) // 2, (left[1] + right[1]) // 2)
            lt = ((left[0] + top[0]) // 2, (left[1] + top[1]) // 2)
            rt = ((right[0] + top[0]) // 2, (right[1] + top[1]) // 2)
            refined.extend(((left, lr, lt), (lr, right, rt), (lt, rt, top)))
        triangles = refined
    edges = set()
    for a, b, c in triangles:
        for u, v in ((a, b), (a, c), (b, c)):
            edges.add(tuple(sorted((u, v))))
    vertices = sorted({vertex for edge in edges for vertex in edge})
    boundary = {(0, 0), (scale, 0), (0, scale)}
    interior = sorted(set(vertices) - boundary)
    index = {vertex: position for position, vertex in enumerate(interior)}
    degrees = defaultdict(int)
    matrix = np.zeros((len(interior), len(interior)), dtype=float)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
        if u in index and v in index:
            matrix[index[u], index[v]] = matrix[index[v], index[u]] = -1.0
    for vertex, position in index.items():
        matrix[position, position] = degrees[vertex]
    return vertices, interior, edges, degrees, matrix


def determinant_exponents(level: int) -> dict[str, int]:
    return {
        "prime_2": (3**level - 1) // 2,
        "prime_3": (3 ** (level + 1) - 6 * level - 3) // 4,
        "prime_5": (3**level + 6 * level - 1) // 4,
    }


def determinant_from_exponents(exponents: dict[str, int]) -> int:
    return 2 ** exponents["prime_2"] * 3 ** exponents["prime_3"] * 5 ** exponents["prime_5"]


def build() -> dict:
    polynomials = characteristic_polynomials(LEVEL_MAX)
    level_rows = []
    lineage_rows = []
    graph_eigenvalue_cells = 0
    for level in range(LEVEL_MIN, LEVEL_MAX + 1):
        dimension = (3 ** (level + 1) - 3) // 2
        vertices, interior, edges, degrees, matrix = triangle_graph(level)
        lineages = spectral_lineages(level)
        lineage_rows.extend({"level": level, **row} for row in lineages)
        theoretical = sorted(
            float(row["eigenvalue_decimal"])
            for row in lineages
            for _ in range(row["multiplicity"])
        )
        numerical = np.linalg.eigvalsh(matrix)
        maximum_error = max(abs(a - b) for a, b in zip(theoretical, numerical))
        coefficients = polynomials[level]
        exponent_record = determinant_exponents(level)
        determinant = determinant_from_exponents(exponent_record)
        if len(interior) != dimension or len(theoretical) != dimension:
            raise AssertionError("dimension ledger mismatch")
        if maximum_error >= 1e-10:
            raise AssertionError("finite graph regression failed")
        if any(degrees[vertex] != 4 for vertex in interior):
            raise AssertionError("interior degree is not four")
        if coefficients[0] != (-1) ** dimension * determinant:
            raise AssertionError("determinant/constant coefficient mismatch")
        if abs(sum(float(row["eigenvalue_decimal"]) * row["multiplicity"] for row in lineages) - 4 * dimension) > 1e-9:
            raise AssertionError("heat derivative/trace mismatch")
        coefficient_bytes = ",".join(map(str, coefficients)).encode()
        level_rows.append({
            "level": level,
            "full_vertex_count": len(vertices),
            "boundary_vertex_count": 3,
            "interior_dimension": dimension,
            "edge_count": len(edges),
            "lineage_count": len(lineages),
            "series_lineage_counts": {
                name: sum(row["series"] == name for row in lineages)
                for name in ("2-series", "5-series", "6-series")
            },
            "multiplicity_sum": sum(row["multiplicity"] for row in lineages),
            "heat_trace_at_zero": dimension,
            "negative_heat_trace_derivative_at_zero": 4 * dimension,
            "spectral_zeta_at_zero": dimension,
            "determinant_prime_exponents": exponent_record,
            "determinant": str(determinant),
            "characteristic_polynomial_degree": len(coefficients) - 1,
            "characteristic_polynomial_coefficients_ascending": list(map(str, coefficients)),
            "characteristic_polynomial_coefficients_sha256": sha256(coefficient_bytes).hexdigest(),
            "graph_diagonalization_max_abs_error": format(maximum_error, ".3e"),
            "graph_diagonalization_error_bound": "1e-10",
        })
        graph_eigenvalue_cells += dimension

    data = {
        "schema": "HCS-C184-v1",
        "candidate_id": "HCS-C184",
        "date_utc": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "artifact_path_base": "henon_dynamics/henon_sierpinski_gasket_spectral_decimation_route_a",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {
            "authority_path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "authority_sha256": EVALUATOR_SHA,
        },
        "source_lock": {
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
        },
        "all_level_theorem": {
            "renormalization_map": "R(t)=t(5-t)",
            "inverse_branches": "phi_-(u)=(5-sqrt(25-4u))/2 and phi_+(u)=(5+sqrt(25-4u))/2",
            "exceptional_values": [2, 5, 6],
            "interior_dimension": "N_m=(3^(m+1)-3)/2",
            "two_series": "birth generation 1, seed 2, multiplicity 1, then both inverse branches",
            "five_series": "birth generation j>=1, seed 5, multiplicity (3^(j-1)+3)/2, then both inverse branches",
            "six_series": "birth generation j>=2, seed 6, multiplicity (3^j-3)/2; if continued, the next value is forced to 3 before both inverse branches resume",
            "dimension_identity": "the sum over every admissible lineage at level m, weighted by its birth multiplicity, equals N_m",
            "characteristic_base": "chi_1(t)=(t-2)(t-5)^2",
            "characteristic_recurrence": "chi_m(t)=(-1)^N_(m-1)*(t-5)^a_m*(t-6)^b_m*chi_(m-1)(R(t))/(t-2)^b_(m-1)",
            "birth_exponents": "a_m=(3^(m-1)+3)/2 and b_m=(3^m-3)/2, with b_1=0",
            "exceptional_cancellation": "the divisor (t-2)^b_(m-1) cancels exactly because R(t)-6=-(t-2)(t-3)",
            "determinant": "det(L_m)=2^((3^m-1)/2)*3^((3^(m+1)-6m-3)/4)*5^((3^m+6m-1)/4)",
            "heat_trace": "H_m(u)=sum_over_lineages multiplicity*exp(-u*lambda), so H_m(0)=N_m and -H_m'(0)=4N_m",
            "finite_spectral_zeta": "zeta_m(s)=sum_over_lineages multiplicity*lambda^(-s), an entire finite exponential sum with zeta_m(0)=N_m and exp(-zeta_m'(0))=det(L_m)",
            "owner_boundary": "the inverse-branch genealogy is a level-renormalization correspondence, not an autonomous physical-time map",
        },
        "finite_regression": {
            "level_min": LEVEL_MIN,
            "level_max": LEVEL_MAX,
            "level_rows": level_rows,
            "lineage_rows": lineage_rows,
            "level_row_count": len(level_rows),
            "lineage_row_count": len(lineage_rows),
            "characteristic_coefficient_cells": sum(len(polynomials[level]) for level in polynomials),
            "graph_eigenvalue_cells": graph_eigenvalue_cells,
        },
        "progress_and_boundary": {
            "progress": "one all-level certificate joins complete 2/5/6 genealogy, multiplicities, dimension closure, characteristic recurrence, determinant, heat trace, and finite spectral zeta",
            "proof_boundary": "finite graph diagonalization is regression evidence only; the all-level claim rests on the written spectral-decimation and multiplicity proof",
            "classical_ownership": "spectral decimation and the complete finite-gasket spectrum are attributed to Fukushima and Shima",
            "package_increment": "a content-addressed Route-A synthesis makes the refinement-clock owner boundary and exact finite analytic consequences executable",
            "priority_boundary": "no universal novelty or priority is claimed",
        },
        "route_a_verdict": {
            "A0": "A0_FAIL",
            "A0_qualification": "LEVEL_AND_SPECTRAL_BRANCH_DATA_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
            "A1": "A1_FAIL",
            "A1_qualification": "THE_INVERSE_BRANCH_TREE_IS_LEVEL_RENORMALIZATION_NOT_A_PHYSICAL_TIME_PRIMITIVE_ORBIT_OWNER",
            "A2": "A2_FAIL",
            "A2_qualification": "FINITE_LAPLACIAN_DETERMINANTS_HAVE_NO_TARGET_DIVISOR_MATCH",
            "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A3_qualification": "EXACT_FINITE_SPECTRAL_ZETA_AND_DETERMINANT_STRUCTURE_ONLY_WITH_NO_TARGET_FUNCTIONAL_EQUATION",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "THE_SELF_ADJOINT_LAPLACIAN_HAS_A_CANONICAL_UNITARY_EXPONENTIAL_BUT_REFINEMENT_LEVEL_IS_NOT_ITS_TIME_CLOCK",
            "overall": "ROUTE_A_REJECTED",
            "a0_failure_forces_rejection": True,
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "used_arithmetic_local_data": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_infinite_gasket_spectral_zeta": False,
            "claimed_level_as_physical_time": False,
            "claimed_hilbert_polya": False,
            "route_b_invocation_allowed": False,
        },
        "source_registry": [{
            "key": "fukushima_shima_1992_sierpinski",
            "title": "On a spectral analysis for the Sierpiński gasket",
            "authors": "Masatoshi Fukushima and Tadashi Shima",
            "journal": "Potential Analysis",
            "volume": 1,
            "issue": 1,
            "pages": "1-35",
            "year": 1992,
            "doi": "10.1007/BF00249784",
            "role": "classical ownership of the finite-gasket spectral-decimation method and complete spectrum",
        }],
        "integrity_modes": {
            "implementation_bug": "CLEAR",
            "hallucinated_citation": "CLEAR",
            "hallucinated_result": "CLEAR",
            "shortcut_reliance": "CLEAR",
            "bug_reframed_as_insight": "CLEAR",
            "methodology_fabrication": "CLEAR",
            "frame_lock": "CLEAR",
        },
        "nonclaims": [
            "universal novelty or priority for spectral decimation, the 2/5/6 series, or their multiplicities",
            "interpretation of the inverse-branch genealogy as autonomous physical-time dynamics",
            "an infinite-gasket spectral-zeta theorem or regularized determinant",
            "rational-prime semantics for levels, branch words, eigenvalues, or multiplicities",
            "a target divisor, Gamma factor, functional equation, counting law, or Weil compression",
            "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
        ],
    }
    data["payload_sha256"] = sha256(canonical_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C184_PRODUCER_PASS",
        "levels": data["finite_regression"]["level_row_count"],
        "lineages": data["finite_regression"]["lineage_row_count"],
        "coefficient_cells": data["finite_regression"]["characteristic_coefficient_cells"],
        "graph_eigenvalue_cells": data["finite_regression"]["graph_eigenvalue_cells"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
