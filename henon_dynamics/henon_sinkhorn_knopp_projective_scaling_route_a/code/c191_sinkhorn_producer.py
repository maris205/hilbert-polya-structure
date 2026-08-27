#!/usr/bin/env python3
"""Produce the exact C191 Sinkhorn--Knopp support and scaling ledger."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import permutations
import json
import math
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(os.environ.get("C191_OUTPUT", ROOT / "results/c191_sinkhorn_evidence.json"))
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def q(value: int | str | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def qs(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def qmatrix(matrix: list[list[Fraction]]) -> list[list[str]]:
    return [[qs(value) for value in row] for row in matrix]


def pattern_matrix(mask: int, n: int) -> list[list[int]]:
    return [[(mask >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]


def no_zero_line(pattern: list[list[int]]) -> bool:
    n = len(pattern)
    return all(sum(row) > 0 for row in pattern) and all(sum(pattern[i][j] for i in range(n)) > 0 for j in range(n))


def positive_permutations(pattern: list[list[int]]) -> list[tuple[int, ...]]:
    n = len(pattern)
    return [perm for perm in permutations(range(n)) if all(pattern[i][perm[i]] for i in range(n))]


def support_layers(pattern: list[list[int]]) -> tuple[bool, bool, bool, int]:
    n = len(pattern)
    positive = positive_permutations(pattern)
    support = bool(positive)
    covered = {(i, perm[i]) for perm in positive for i in range(n)}
    positive_edges = {(i, j) for i in range(n) for j in range(n) if pattern[i][j]}
    total_support = support and covered == positive_edges
    if n == 1:
        fully_indecomposable = bool(pattern[0][0])
    else:
        fully_indecomposable = True
        for subset_mask in range(1, (1 << n) - 1):
            rows = [i for i in range(n) if subset_mask >> i & 1]
            neighbours = {j for i in rows for j in range(n) if pattern[i][j]}
            if len(neighbours) < len(rows) + 1:
                fully_indecomposable = False
                break
    return support, total_support, fully_indecomposable, len(positive)


def row_normalize(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    result = []
    for row in matrix:
        total = sum(row, Fraction(0))
        if total == 0:
            raise ZeroDivisionError("zero row")
        result.append([value / total for value in row])
    return result


def column_normalize(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(matrix)
    totals = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
    if any(total == 0 for total in totals):
        raise ZeroDivisionError("zero column")
    return [[matrix[i][j] / totals[j] for j in range(n)] for i in range(n)]


def full_cycle(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return column_normalize(row_normalize(matrix))


def marginal_error(matrix: list[list[Fraction]]) -> tuple[Fraction, Fraction]:
    n = len(matrix)
    row_error = max(abs(sum(row, Fraction(0)) - 1) for row in matrix)
    col_error = max(abs(sum(matrix[i][j] for i in range(n)) - 1) for j in range(n))
    return row_error, col_error


def l1_distance(left: list[list[Fraction]], right: list[list[Fraction]]) -> Fraction:
    return sum((abs(left[i][j] - right[i][j]) for i in range(len(left)) for j in range(len(left))), Fraction(0))


def cross_ratios(matrix: list[list[Fraction]]) -> list[dict[str, object]]:
    n = len(matrix)
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(n):
                for ell in range(k + 1, n):
                    if matrix[i][ell] and matrix[j][k]:
                        rows.append({"indices": [i, j, k, ell], "value": qs(matrix[i][k] * matrix[j][ell] / (matrix[i][ell] * matrix[j][k]))})
    return rows


def projective_theta(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    ratios = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for ell in range(n):
                    ratios.append(matrix[i][k] * matrix[j][ell] / (matrix[i][ell] * matrix[j][k]))
    return max(ratios)


def rational_sqrt(value: Fraction) -> Fraction:
    a = math.isqrt(value.numerator)
    b = math.isqrt(value.denominator)
    if a * a != value.numerator or b * b != value.denominator:
        raise ValueError(f"theta is not a rational square: {value}")
    return Fraction(a, b)


def local_spectrum(target: list[list[Fraction]]) -> list[dict[str, object]]:
    matrix = sp.Matrix([[sp.Rational(value.numerator, value.denominator) for value in row] for row in target])
    gram = matrix.T * matrix
    eigs = gram.eigenvals()
    return [
        {"eigenvalue": str(value), "multiplicity": int(multiplicity)}
        for value, multiplicity in sorted(eigs.items(), key=lambda pair: float(pair[0]), reverse=True)
    ]


def positive_case(case_id: str, target: list[list[Fraction]], left: list[Fraction], right: list[Fraction]) -> dict[str, object]:
    n = len(target)
    source = [[target[i][j] / (left[i] * right[j]) for j in range(n)] for i in range(n)]
    current = [row[:] for row in source]
    source_ratios = cross_ratios(source)
    target_ratios = cross_ratios(target)
    assert source_ratios == target_ratios
    steps = []
    # Exact rational denominators grow doubly exponentially under alternating
    # normalization; four stored states are ample as a regression oracle.
    for iteration in range(4):
        row_error, col_error = marginal_error(current)
        steps.append({
            "iteration": iteration,
            "row_error": qs(row_error),
            "column_error": qs(col_error),
            "l1_to_target": qs(l1_distance(current, target)),
        })
        current = full_cycle(current)
    theta = projective_theta(source)
    root_theta = rational_sqrt(theta)
    kappa = (root_theta - 1) / (root_theta + 1)
    spectrum = local_spectrum(target)
    nontrivial = [q(row["eigenvalue"]) for row in spectrum if row["eigenvalue"] != "1"]
    return {
        "case_id": case_id,
        "dimension": n,
        "source_matrix": qmatrix(source),
        "target_doubly_stochastic": qmatrix(target),
        "left_scaling": [qs(value) for value in left],
        "right_scaling": [qs(value) for value in right],
        "cross_ratios": source_ratios,
        "projective_theta": qs(theta),
        "birkhoff_kappa": qs(kappa),
        "full_cycle_contraction_bound": qs(kappa * kappa),
        "local_gram_spectrum": spectrum,
        "local_projective_rate": qs(max(nontrivial)),
        "iteration_steps": steps,
    }


def boundary_case(case_id: str, pattern: list[list[int]]) -> dict[str, object]:
    support, total, fully, permanent_count = support_layers(pattern)
    matrix = [[Fraction(value) for value in row] for row in pattern]
    steps = []
    current = matrix
    for iteration in range(8):
        row_error, col_error = marginal_error(current)
        steps.append({"iteration": iteration, "row_error": qs(row_error), "column_error": qs(col_error)})
        current = full_cycle(current)
    return {
        "case_id": case_id,
        "pattern": pattern,
        "support": support,
        "total_support": total,
        "fully_indecomposable": fully,
        "positive_diagonal_count": permanent_count,
        "iteration_steps": steps,
        "last_iterate": qmatrix(current),
    }


def payload_digest(data: dict[str, object]) -> str:
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def main() -> None:
    pattern_rows = []
    pattern_counts: dict[str, dict[str, int]] = {}
    for n in (2, 3):
        counts = {"no_zero_line": 0, "support": 0, "total_support": 0, "fully_indecomposable": 0}
        for mask in range(1 << (n * n)):
            pattern = pattern_matrix(mask, n)
            if not no_zero_line(pattern):
                continue
            support, total, fully, permanent_count = support_layers(pattern)
            counts["no_zero_line"] += 1
            counts["support"] += int(support)
            counts["total_support"] += int(total)
            counts["fully_indecomposable"] += int(fully)
            pattern_rows.append({
                "dimension": n,
                "mask": mask,
                "pattern": pattern,
                "positive_edge_count": sum(map(sum, pattern)),
                "positive_diagonal_count": permanent_count,
                "support": support,
                "total_support": total,
                "fully_indecomposable": fully,
            })
        pattern_counts[str(n)] = counts

    positive_cases = [
        positive_case(
            "two_by_two_odds_four",
            [[q("2/3"), q("1/3")], [q("1/3"), q("2/3")]],
            [q(2), q(3)], [q(5), q(7)],
        ),
        positive_case(
            "three_by_three_symmetric",
            [[q("1/2"), q("1/4"), q("1/4")], [q("1/4"), q("1/2"), q("1/4")], [q("1/4"), q("1/4"), q("1/2")]],
            [q(2), q(3), q(5)], [q(7), q(11), q(13)],
        ),
        positive_case(
            "three_by_three_high_contrast",
            [[q("3/5"), q("1/5"), q("1/5")], [q("1/5"), q("3/5"), q("1/5")], [q("1/5"), q("1/5"), q("3/5")]],
            [q(3), q(4), q(7)], [q(5), q(8), q(9)],
        ),
        positive_case(
            "three_by_three_asymmetric_circulant",
            [[q("1/5"), q("1/5"), q("3/5")], [q("3/5"), q("1/5"), q("1/5")], [q("1/5"), q("3/5"), q("1/5")]],
            [q(5), q(7), q(11)], [q(2), q(3), q(13)],
        ),
    ]
    boundary_cases = [
        boundary_case("support_not_total", [[1, 1], [1, 0]]),
        boundary_case("total_not_fully_indecomposable", [[1, 0], [0, 1]]),
        boundary_case("fully_indecomposable_with_zeros", [[1, 1, 0], [0, 1, 1], [1, 0, 1]]),
    ]
    no_support_pattern = [[1, 0, 0], [1, 0, 0], [0, 1, 1]]
    no_support_layers = support_layers(no_support_pattern)
    boundary_cases.append({
        "case_id": "no_support_hall_failure",
        "pattern": no_support_pattern,
        "support": no_support_layers[0],
        "total_support": no_support_layers[1],
        "fully_indecomposable": no_support_layers[2],
        "positive_diagonal_count": no_support_layers[3],
        "iteration_steps": [],
        "last_iterate": [],
    })

    data: dict[str, object] = {
        "schema": "hcs-c191-sinkhorn-evidence-v1",
        "candidate_id": "HCS-C191",
        "date_utc": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "evaluator": {"version": "0.2.0", "path": "flow_systems/skills/route-a-evaluator.md", "sha256": EVALUATOR_SHA256},
        "scope_literal": SCOPE,
        "source_lock": {
            "object": "alternating row and column normalization of a square nonnegative matrix",
            "phase_space": "nonnegative matrices with the declared support pattern and no zero normalization line",
            "clock": "one row-normalization followed by one column-normalization",
            "normalization": "unit row sums and then unit column sums",
            "parameter_provenance": "matrix entries and zero pattern; never target tables",
            "determinant_convention": "ordinary characteristic determinant only for the local Jacobian",
            "precision": "Fraction and SymPy Rational arithmetic",
            "allowed_data": "nonnegative matrices, perfect matchings, marginals, diagonal scalings and projective metrics",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya and Route B",
        },
        "attribution": {
            "sinkhorn_knopp_owned": "support, total-support convergence and scaling criteria",
            "brualdi_parter_schneider_owned": "uniqueness of scaling factors through full indecomposability",
            "franklin_lorenz_owned": "positive-matrix Hilbert-metric geometric convergence",
            "knight_owned": "local asymptotic singular-value rate",
            "package_derived": "one support-stratified theorem ledger, exact zero-pattern census and convention-locked local Jacobian reconstruction",
        },
        "source_registry": [
            {
                "source_id": "SK67",
                "authors": ["Richard Sinkhorn", "Paul Knopp"],
                "title": "Concerning nonnegative matrices and doubly stochastic matrices",
                "venue": "Pacific Journal of Mathematics 21(2), 343--348",
                "year": 1967,
                "doi": "10.2140/pjm.1967.21.343",
                "role": "support and total-support theorem",
            },
            {
                "source_id": "BPS66",
                "authors": ["Richard A. Brualdi", "Seymour V. Parter", "Hans Schneider"],
                "title": "The diagonal equivalence of a nonnegative matrix to a stochastic matrix",
                "venue": "Journal of Mathematical Analysis and Applications 16(1), 31--50",
                "year": 1966,
                "doi": "10.1016/0022-247X(66)90184-3",
                "role": "full-indecomposability and factor-uniqueness theorem",
            },
            {
                "source_id": "FL89",
                "authors": ["Joel Franklin", "Jens Lorenz"],
                "title": "On the scaling of multidimensional matrices",
                "venue": "Linear Algebra and its Applications 114--115, 717--735",
                "year": 1989,
                "doi": "10.1016/0024-3795(89)90490-4",
                "role": "Hilbert-metric geometric convergence",
            },
            {
                "source_id": "K08",
                "authors": ["Philip A. Knight"],
                "title": "The Sinkhorn--Knopp algorithm: convergence and applications",
                "venue": "SIAM Journal on Matrix Analysis and Applications 30(1), 261--275",
                "year": 2008,
                "doi": "10.1137/060659624",
                "role": "convergence synthesis and local rate",
            },
        ],
        "theorem": {
            "support_iff_limit": "the alternating iteration converges to a doubly stochastic limit exactly when the matrix has a positive diagonal",
            "total_support_iff_scalable": "a positive diagonal scaling to the limit exists exactly when every positive entry lies on a positive diagonal",
            "scaled_matrix_unique": "when total support holds, the doubly stochastic matrix in the positive diagonal-equivalence class is unique",
            "factor_gauge": "under total support, positive diagonal factors are unique up to one reciprocal scalar exactly when the support is fully indecomposable",
            "positive_contraction": "strict positivity gives geometric convergence in Hilbert projective metric with a data-dependent Birkhoff bound",
            "local_rate": "at a positive doubly stochastic limit S the log-column full-cycle Jacobian is S^T S; on the gauge quotient its generic asymptotic spectral radius is sigma_2(S)^2",
            "period_boundary": "convergence rules out nonconstant recurrent cycles on every convergent scaling orbit",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "a0_reason": "support matchings and scaling factors have no intrinsic rational-prime or prime-power semantics",
            "a1_reason": "convergent scaling has no nonconstant primitive periodic-orbit owner",
            "a2_reason": "matrix scaling and a local Jacobian do not identify a target divisor",
            "a3_reason": "no target continuation, functional equation, counting law or Weil compression follows",
            "a4_reason": "the nonlinear positive-cone iteration supplies no source-native self-adjoint Hilbert-space operator",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "target_zero_table_used": False,
            "target_prime_table_used": False,
            "arithmetic_local_data_used": False,
            "euler_factor_claimed": False,
            "root_number_claimed": False,
            "automorphy_claimed": False,
            "target_divisor_claimed": False,
            "target_functional_equation_claimed": False,
            "hilbert_polya_operator_claimed": False,
            "route_b_invoked": False,
        },
        "progress_and_boundary": {
            "explicit_progress": "all square nonnegative matrices are separated by support, total support and full indecomposability, with positive geometric and exact local-rate dynamics",
            "proof_boundary": "the finite zero-pattern and rational iterations are regression oracles, not a proof of the all-matrix theorems",
            "rate_boundary": "there is no dimension-only uniform contraction rate as the projective diameter diverges",
            "zero_boundary": "without total support the limiting matrix need not be reachable by finite positive diagonal factors",
            "period_boundary": "a fixed point is an algorithmic scaling target, not an arithmetic primitive orbit",
        },
        "finite_regression": {
            "pattern_rows": pattern_rows,
            "pattern_counts": pattern_counts,
            "positive_cases": positive_cases,
            "boundary_cases": boundary_cases,
            "pattern_row_count": len(pattern_rows),
            "positive_case_count": len(positive_cases),
            "boundary_case_count": len(boundary_cases),
            "iteration_step_count": sum(len(case["iteration_steps"]) for case in positive_cases + boundary_cases),
            "cross_ratio_count": sum(len(case["cross_ratios"]) for case in positive_cases),
        },
        "nonclaims": [
            "priority for matrix-scaling, support, total-support, full-indecomposability or Hilbert-contraction theorems",
            "a dimension-only or zero-pattern-only uniform convergence rate",
            "finite positive scaling factors when total support fails",
            "primitive-orbit arithmetic semantics for an attracting fixed point",
            "intrinsic rational-prime data, a target divisor or a target functional equation",
            "a Hilbert--Polya operator, Route-B authorization, external peer review or an acceptance score",
        ],
    }
    data["payload_sha256"] = payload_digest(data)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C191_PRODUCER_PASS",
        "pattern_rows": len(pattern_rows),
        "positive_cases": len(positive_cases),
        "boundary_cases": len(boundary_cases),
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
