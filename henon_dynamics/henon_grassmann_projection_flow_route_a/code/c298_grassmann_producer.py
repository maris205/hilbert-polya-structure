#!/usr/bin/env python3
"""Produce deterministic exact evidence for HCS-C298."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c298_grassmann_evidence.json"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200


def canonical_payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def determinant(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    work = [row[:] for row in matrix]
    sign = 1
    denominator = 1
    for pivot_index in range(n - 1):
        pivot_row = next((r for r in range(pivot_index, n) if work[r][pivot_index] != 0), None)
        if pivot_row is None:
            return 0
        if pivot_row != pivot_index:
            work[pivot_index], work[pivot_row] = work[pivot_row], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for i in range(pivot_index + 1, n):
            for j in range(pivot_index + 1, n):
                work[i][j] = (work[i][j] * pivot - work[i][pivot_index] * work[pivot_index][j]) // denominator
        denominator = pivot
        for i in range(pivot_index + 1, n):
            work[i][pivot_index] = 0
    return sign * work[-1][-1]


def rank(matrix: list[list[int | Fraction]]) -> int:
    if not matrix:
        return 0
    work = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(work), len(work[0])
    pivot_row = 0
    for col in range(cols):
        selected = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        pivot = work[pivot_row][col]
        work[pivot_row] = [x / pivot for x in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][col]:
                factor = work[r][col]
                work[r] = [x - factor * y for x, y in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(left, right):
    right_t = transpose(right)
    return [[sum(Fraction(x) * Fraction(y) for x, y in zip(row, col)) for col in right_t] for row in left]


def inverse(matrix):
    n = len(matrix)
    work = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        selected = next(r for r in range(col, n) if work[r][col])
        work[col], work[selected] = work[selected], work[col]
        pivot = work[col][col]
        work[col] = [x / pivot for x in work[col]]
        for r in range(n):
            if r != col and work[r][col]:
                factor = work[r][col]
                work[r] = [x - factor * y for x, y in zip(work[r], work[col])]
    return [row[n:] for row in work]


def projection(frame: list[list[int]]) -> list[list[Fraction]]:
    qt = transpose(frame)
    gram = matmul(qt, frame)
    return matmul(matmul(frame, inverse(gram)), qt)


def plucker_rows(eigenvalues: list[int], frame: list[list[int]]) -> list[dict]:
    k = len(frame[0])
    rows = []
    for subset_zero in itertools.combinations(range(len(frame)), k):
        minor = determinant([[frame[i][j] for j in range(k)] for i in subset_zero])
        if minor:
            rows.append({
                "subset": [i + 1 for i in subset_zero],
                "minor": minor,
                "weight": sum(eigenvalues[i] for i in subset_zero),
            })
    return rows


def tie_groups(eigenvalues: list[int], k: int) -> list[dict]:
    groups = {}
    for subset in itertools.combinations(range(len(eigenvalues)), k):
        weight = sum(eigenvalues[i] for i in subset)
        groups.setdefault(weight, []).append([i + 1 for i in subset])
    return [
        {"weight": weight, "subsets": subsets}
        for weight, subsets in sorted(groups.items()) if len(subsets) > 1
    ]


def stability(eigenvalues: list[int], selected_one: list[int]) -> tuple[list[dict], int, int]:
    selected = {i - 1 for i in selected_one}
    modes = []
    stable = unstable = 0
    for i in sorted(selected):
        for j in range(len(eigenvalues)):
            if j in selected:
                continue
            rate = eigenvalues[j] - eigenvalues[i]
            assert rate != 0
            stable += rate < 0
            unstable += rate > 0
            modes.append({
                "selected_i": i + 1,
                "unselected_j": j + 1,
                "rate_lambda_j_minus_lambda_i": rate,
                "type": "stable" if rate < 0 else "unstable",
            })
    return modes, stable, unstable


def rational_initial_data(eigenvalues: list[int], frame: list[list[int]]) -> dict:
    p = projection(frame)
    n = len(p)
    value = sum(Fraction(eigenvalues[i]) * p[i][i] for i in range(n))
    commutator = [
        [p[i][j] * (eigenvalues[j] - eigenvalues[i]) for j in range(n)]
        for i in range(n)
    ]
    derivative = sum(x * x for row in commutator for x in row)
    return {
        "initial_projection": [[q(x) for x in row] for row in p],
        "trace_A_P0": q(value),
        "commutator_frobenius_square": q(derivative),
        "strict_lyapunov_at_t0": derivative > 0,
    }


SIMPLE_CASES = [
    ("S1-rank-one-sparse", [-3, -1, 2, 5], [[1], [2], [0], [3]]),
    ("S2-subset-sum-tie", [0, 1, 3, 4], [[1, 0], [1, 1], [1, 2], [1, 3]]),
    ("S3-generic-two-plane", [-4, -1, 0, 3, 7], [[1, -2], [1, -1], [1, 0], [1, 1], [1, 3]]),
    ("S4-generic-three-plane-ties", [-3, -2, 0, 2, 3], [[1, 0, 0], [1, 1, 1], [1, 2, 4], [1, 3, 9], [1, 4, 16]]),
    ("S5-proper-schubert-cell", [0, 2, 5, 9, 14], [[1, 0], [1, 1], [1, 2], [1, 4], [0, 0]]),
    ("S6-generic-six-by-three", [-5, -2, 0, 1, 4, 8], [[1, -2, 4], [1, -1, 1], [1, 0, 0], [1, 1, 1], [1, 2, 4], [1, 4, 16]]),
    ("S7-sparse-six-by-two", [-4, -1, 2, 6, 7, 11], [[1, 0], [0, 1], [1, 1], [2, 1], [0, 0], [1, 3]]),
    ("S8-generic-six-by-four", [-7, -3, -1, 2, 5, 9], [[1, 0, 0, 0], [1, 1, 1, 1], [1, 2, 4, 8], [1, 3, 9, 27], [1, 4, 16, 64], [1, 5, 25, 125]]),
]

REPEATED_CASES = [
    ("R1-mixed-two-block", [0, 0, 2, 2], [[1, 0], [0, 1], [1, 2], [0, 0]]),
    ("R2-top-eigenspace", [0, 0, 2, 2], [[1, 0], [0, 1], [1, 1], [1, 2]]),
    ("R3-two-block-multiplicity", [-2, -2, 1, 1, 1], [[1, 0], [0, 1], [1, 1], [2, 2], [0, 0]]),
    ("R4-three-block-associated-grade", [-3, 0, 0, 4, 4], [[1, 0, 0], [0, 1, 0], [0, 2, 1], [0, 0, 1], [0, 0, 1]]),
    ("R5-three-block-six-dimensional", [0, 0, 0, 5, 5, 9], [[1, 0, 0], [1, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]]),
    ("R6-middle-plus-top", [-1, -1, 3, 3, 3, 8], [[0, 0], [0, 0], [1, 0], [1, 0], [0, 1], [1, 2]]),
]

MORSE_CONFIGS = [
    ("M1", [-1, 2], [2, 2], 2),
    ("M2", [-2, 0, 5], [1, 3, 2], 3),
    ("M3", [0, 4, 9], [3, 2, 1], 2),
    ("M4", [-3, 1, 6], [2, 3, 2], 3),
]


def build_simple_cases() -> tuple[list[dict], int, int]:
    output = []
    support_cells = mode_cells = 0
    for case_id, eigenvalues, frame in SIMPLE_CASES:
        n, k = len(frame), len(frame[0])
        assert len(eigenvalues) == n and rank(frame) == k
        support = plucker_rows(eigenvalues, frame)
        ordered = sorted(support, key=lambda row: row["weight"], reverse=True)
        assert len(ordered) >= 2 and ordered[0]["weight"] > ordered[1]["weight"]
        leader = ordered[0]
        second_weight = ordered[1]["weight"]
        modes, stable, unstable = stability(eigenvalues, leader["subset"])
        support_weight_groups = {}
        for row in support:
            support_weight_groups.setdefault(row["weight"], 0)
            support_weight_groups[row["weight"]] += 1
        output.append({
            "case_id": case_id,
            "n": n,
            "k": k,
            "eigenvalues_strictly_increasing": eigenvalues,
            "integer_frame": frame,
            "plucker_support": support,
            "support_size": len(support),
            "ambient_subset_weight_ties": tie_groups(eigenvalues, k),
            "support_tied_nonleading_weight_groups": [
                {"weight": weight, "multiplicity": multiplicity}
                for weight, multiplicity in sorted(support_weight_groups.items())
                if multiplicity > 1 and weight < leader["weight"]
            ],
            "greedy_leading_subset": leader["subset"],
            "leading_weight": leader["weight"],
            "second_nonzero_weight": second_weight,
            "exact_rate_gap": leader["weight"] - second_weight,
            "linear_modes": modes,
            "stable_dimension": stable,
            "unstable_dimension": unstable,
            "grassmann_dimension": k * (n - k),
            "rational_initial_data": rational_initial_data(eigenvalues, frame),
        })
        support_cells += len(support)
        mode_cells += len(modes)
    return output, support_cells, mode_cells


def eigen_blocks(eigenvalues: list[int]) -> tuple[list[int], list[int], list[int]]:
    values, multiplicities, cumulative = [], [], []
    for value, group in itertools.groupby(eigenvalues):
        values.append(value)
        multiplicities.append(len(list(group)))
        cumulative.append(sum(multiplicities))
    return values, multiplicities, cumulative


def filtration_dimensions(frame: list[list[int]], cumulative: list[int]) -> list[int]:
    n, k = len(frame), len(frame[0])
    dimensions = []
    for cutoff in cumulative:
        augmented_rows = []
        for i in range(n):
            augmented_rows.append(frame[i][:] + [int(i == j) for j in range(cutoff)])
        dimensions.append(k + cutoff - rank(augmented_rows))
    return dimensions


def build_repeated_cases() -> tuple[list[dict], int]:
    output = []
    support_cells = 0
    for case_id, eigenvalues, frame in REPEATED_CASES:
        n, k = len(frame), len(frame[0])
        assert len(eigenvalues) == n and rank(frame) == k
        values, multiplicities, cumulative = eigen_blocks(eigenvalues)
        dims = filtration_dimensions(frame, cumulative)
        occupancies = [dims[0]] + [dims[i] - dims[i - 1] for i in range(1, len(dims))]
        support = plucker_rows(eigenvalues, frame)
        top_weight = max(row["weight"] for row in support)
        lower_weights = sorted({row["weight"] for row in support if row["weight"] < top_weight}, reverse=True)
        top_rows = [row for row in support if row["weight"] == top_weight]
        expected_weight = sum(value * occupancy for value, occupancy in zip(values, occupancies))
        assert expected_weight == top_weight
        output.append({
            "case_id": case_id,
            "n": n,
            "k": k,
            "eigenvalues_nondecreasing": eigenvalues,
            "eigenvalue_blocks": [
                {"value": value, "multiplicity": multiplicity, "cumulative_dimension": cutoff}
                for value, multiplicity, cutoff in zip(values, multiplicities, cumulative)
            ],
            "integer_frame": frame,
            "filtration_intersection_dimensions": dims,
            "associated_graded_occupancies": occupancies,
            "top_plucker_weight": top_weight,
            "top_weight_plucker_coordinates": top_rows,
            "top_weight_coordinate_count": len(top_rows),
            "next_distinct_nonzero_weight": lower_weights[0] if lower_weights else None,
            "plucker_weight_gap": top_weight - lower_weights[0] if lower_weights else None,
            "plucker_support": support,
            "support_size": len(support),
            "rational_initial_data": rational_initial_data(eigenvalues, frame),
        })
        support_cells += len(support)
    return output, support_cells


def occupancy_vectors(multiplicities: list[int], k: int):
    for values in itertools.product(*[range(m + 1) for m in multiplicities]):
        if sum(values) == k:
            yield list(values)


def build_morse_atlas() -> tuple[list[dict], int]:
    atlases = []
    total_rows = 0
    for config_id, values, multiplicities, k in MORSE_CONFIGS:
        n = sum(multiplicities)
        rows = []
        for occupancy in occupancy_vectors(multiplicities, k):
            tangent = sum(x * (m - x) for x, m in zip(occupancy, multiplicities))
            stable = sum(
                occupancy[alpha] * (multiplicities[beta] - occupancy[beta])
                for alpha in range(len(values)) for beta in range(alpha)
            )
            unstable = sum(
                occupancy[alpha] * (multiplicities[beta] - occupancy[beta])
                for alpha in range(len(values)) for beta in range(alpha + 1, len(values))
            )
            assert tangent + stable + unstable == k * (n - k)
            rows.append({
                "occupancy": occupancy,
                "critical_value_trace_A_P": sum(x * value for x, value in zip(occupancy, values)),
                "critical_manifold_dimension": tangent,
                "stable_normal_dimension": stable,
                "unstable_normal_dimension": unstable,
                "dimension_closure": tangent + stable + unstable,
            })
        atlases.append({
            "config_id": config_id,
            "eigenvalue_values": values,
            "multiplicities": multiplicities,
            "n": n,
            "k": k,
            "grassmann_dimension": k * (n - k),
            "component_count": len(rows),
            "components": rows,
        })
        total_rows += len(rows)
    return atlases, total_rows


def build() -> dict:
    simple, simple_support_cells, linear_mode_cells = build_simple_cases()
    repeated, repeated_support_cells = build_repeated_cases()
    morse, morse_rows = build_morse_atlas()
    flags = {
        "claims_target_arithmetic_local_data": False,
        "claims_target_euler_factors": False,
        "claims_root_number": False,
        "claims_automorphy": False,
        "claims_target_divisor_or_counting_law": False,
        "claims_target_functional_equation": False,
        "claims_target_zero_match": False,
        "claims_hilbert_polya_operator": False,
        "invokes_route_b": False,
    }
    data = {
        "schema": "hcs-c298-grassmann-projection-flow-v1",
        "candidate_id": "HCS-C298",
        "obstruction_id": "HEN-O282",
        "evaluation_date": "2026-09-02",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "state": "rank-k real orthogonal projection P",
            "generator": "real symmetric n-by-n matrix A",
            "flow": "dot(P)=[P,[P,A]]",
            "exact_range": "Ran(P(t))=exp(tA)Ran(P0)",
            "clock": "continuous real time t",
            "normalization": "orthogonal projector represents an unoriented k-plane",
        },
        "theorem_contract": {
            "global_solution": "P(t)=Y(t)(Y(t)^T Y(t))^(-1)Y(t)^T with Y(t)=exp(tA)Q0",
            "plucker": "p_I(t) is projectively exp(t sum_{i in I}lambda_i)p_I(0)",
            "simple_limit": "each eigenflag Schubert cell converges to its greedy coordinate k-plane",
            "simple_rate": "the actual second nonzero Plucker weight determines the exact exponential rate",
            "equilibria": "all and only A-invariant rank-k orthogonal projections",
            "linearization": "mode Hom(e_i,e_j) has rate lambda_j-lambda_i",
            "repeated_spectrum": "critical sets are product-Grassmann Morse-Bott manifolds and every orbit has an associated-graded limit",
            "recurrence": "Tr(AP) is strict off equilibria, excluding nonconstant recurrence",
        },
        "proof_contract": {
            "quotient_flow": "differentiate the orthogonal projector onto exp(tA)Ran(P0)",
            "matroid_guard": "nonzero Plucker indices are bases of a representable matroid; distinct element weights give a unique greedy maximum",
            "tie_guard": "arbitrary subset sums may tie and are never assumed distinct",
            "rate_guard": "the gap is defined from actual nonzero Plucker support, not from the ambient subset list",
            "degenerate_limit": "an eigenflag-adapted basis yields the associated graded subspace",
            "morse_bott": "within-block modes are tangent and cross-block modes have nonzero eigenvalue differences",
            "finite_role": "finite cases audit formulas and edge conventions but do not prove the global theorem",
        },
        "enumeration": {
            "simple_cases": simple,
            "repeated_cases": repeated,
            "morse_bott_atlases": morse,
            "simple_case_count": len(simple),
            "repeated_case_count": len(repeated),
            "simple_plucker_support_cells": simple_support_cells,
            "repeated_plucker_support_cells": repeated_support_cells,
            "linear_mode_cells": linear_mode_cells,
            "morse_bott_component_rows": morse_rows,
            "audited_cell_count": simple_support_cells + repeated_support_cells + linear_mode_cells + morse_rows,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": flags,
        "nonclaims": [
            "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
            "Plucker weights are finite-dimensional source exponents, not prime norms or target spectral zeros.",
            "The symmetric generator A is not asserted to be a Hilbert--Polya operator.",
            "No literary priority is claimed for Oja, Brockett, Grassmann power-flow, Schubert, or Morse--Bott mechanisms.",
        ],
        "collision_boundary": {
            "C185": "C185 evolves a full symmetric matrix on a fixed isospectral orbit toward a separate diagonal target; C298 fixes A and evolves a rank-k projection/subspace under the induced linear action.",
            "subset_sum_warning": "simple eigenvalues need not have distinct k-fold subset sums; uniqueness uses the representable-matroid greedy basis on actual support.",
        },
        "references": [
            {"identifier": "10.1007/BF00275687", "role": "Oja principal-component-flow lineage"},
            {"identifier": "10.1016/0024-3795(91)90021-N", "role": "Brockett double-bracket lineage"},
            {"identifier": "hdl:2078.5/90452", "role": "direct continuous-time Grassmann subspace-flow owner"},
        ],
    }
    data["payload_sha256"] = canonical_payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C298_PRODUCER_PASS",
        "output": str(args.output),
        "payload_sha256": data["payload_sha256"],
        "simple_cases": data["enumeration"]["simple_case_count"],
        "repeated_cases": data["enumeration"]["repeated_case_count"],
        "audited_cells": data["enumeration"]["audited_cell_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
