#!/usr/bin/env python3
"""Producer-independent checker for the C191 Sinkhorn ledger."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c191_sinkhorn_evidence.json"
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def f(value: Any) -> Fraction:
    return Fraction(str(value))


def matrix(values: list[list[Any]]) -> list[list[Fraction]]:
    return [[f(value) for value in row] for row in values]


def canonical_hash(data: dict[str, Any]) -> str:
    copy = dict(data)
    copy.pop("payload_sha256", None)
    raw = json.dumps(copy, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def find_matching(pattern: list[list[int]], forced: tuple[int, int] | None = None) -> bool:
    n = len(pattern)
    match_col: dict[int, int] = {}
    blocked_row = blocked_col = None
    if forced is not None:
        blocked_row, blocked_col = forced
        if not pattern[blocked_row][blocked_col]:
            return False
        match_col[blocked_col] = blocked_row

    def augment(row: int, seen: set[int]) -> bool:
        for col in range(n):
            if col in seen or not pattern[row][col] or col == blocked_col:
                continue
            seen.add(col)
            if col not in match_col or augment(match_col[col], seen):
                match_col[col] = row
                return True
        return False

    for row in range(n):
        if row == blocked_row:
            continue
        if not augment(row, set()):
            return False
    return len(match_col) == n


def independent_layers(pattern: list[list[int]]) -> tuple[bool, bool, bool, int]:
    n = len(pattern)
    support = find_matching(pattern)
    total = support and all(
        find_matching(pattern, (i, j))
        for i in range(n) for j in range(n) if pattern[i][j]
    )
    # On a square pattern, total support plus connected bipartite support is
    # equivalent to full indecomposability (the n=1 convention is positive).
    vertices = [("r", i) for i in range(n)] + [("c", j) for j in range(n)]
    adjacency = {vertex: set() for vertex in vertices}
    for i in range(n):
        for j in range(n):
            if pattern[i][j]:
                adjacency[("r", i)].add(("c", j))
                adjacency[("c", j)].add(("r", i))
    seen = set()
    stack = [vertices[0]]
    while stack:
        vertex = stack.pop()
        if vertex in seen:
            continue
        seen.add(vertex)
        stack.extend(adjacency[vertex] - seen)
    fully = total and len(seen) == len(vertices)
    # Permanent count by a dynamic-programming matching count, not permutations.
    counts = {0: 1}
    for row in range(n):
        nxt: dict[int, int] = {}
        for used, count in counts.items():
            for col in range(n):
                if pattern[row][col] and not (used >> col & 1):
                    nxt[used | (1 << col)] = nxt.get(used | (1 << col), 0) + count
        counts = nxt
    permanent = counts.get((1 << n) - 1, 0)
    return support, total, fully, permanent


def row_normalize(values: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[entry / sum(row) for entry in row] for row in values]


def col_normalize(values: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(values)
    sums = [sum(values[i][j] for i in range(n)) for j in range(n)]
    return [[values[i][j] / sums[j] for j in range(n)] for i in range(n)]


def cycle(values: list[list[Fraction]]) -> list[list[Fraction]]:
    return col_normalize(row_normalize(values))


def errors(values: list[list[Fraction]]) -> tuple[Fraction, Fraction]:
    n = len(values)
    return (
        max(abs(sum(row) - 1) for row in values),
        max(abs(sum(values[i][j] for i in range(n)) - 1) for j in range(n)),
    )


def l1(left: list[list[Fraction]], right: list[list[Fraction]]) -> Fraction:
    n = len(left)
    return sum(abs(left[i][j] - right[i][j]) for i in range(n) for j in range(n))


def ratio_rows(values: list[list[Fraction]]) -> list[dict[str, Any]]:
    n = len(values)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(n):
                for ell in range(k + 1, n):
                    result.append({
                        "indices": [i, j, k, ell],
                        "value": str(values[i][k] * values[j][ell] / (values[i][ell] * values[j][k])),
                    })
    return result


def theta(values: list[list[Fraction]]) -> Fraction:
    n = len(values)
    return max(
        values[i][k] * values[j][ell] / (values[i][ell] * values[j][k])
        for i in range(n) for j in range(n) for k in range(n) for ell in range(n)
    )


def verify(data: dict[str, Any]) -> int:
    global CHECKS
    CHECKS = 0
    check(data["payload_sha256"] == canonical_hash(data), "payload hash")
    check(data["schema"] == "hcs-c191-sinkhorn-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C191", "candidate")
    check(data["date_utc"] == "2026-08-27", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["evaluator"] == {"version": "0.2.0", "path": "flow_systems/skills/route-a-evaluator.md", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    expected_lock = {
        "object": "alternating row and column normalization of a square nonnegative matrix",
        "phase_space": "nonnegative matrices with the declared support pattern and no zero normalization line",
        "clock": "one row-normalization followed by one column-normalization",
        "normalization": "unit row sums and then unit column sums",
        "parameter_provenance": "matrix entries and zero pattern; never target tables",
        "determinant_convention": "ordinary characteristic determinant only for the local Jacobian",
        "precision": "Fraction and SymPy Rational arithmetic",
        "allowed_data": "nonnegative matrices, perfect matchings, marginals, diagonal scalings and projective metrics",
        "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya and Route B",
    }
    check(data["source_lock"] == expected_lock, "source lock")
    expected_attribution = {
        "sinkhorn_knopp_owned": "support, total-support convergence and scaling criteria",
        "brualdi_parter_schneider_owned": "uniqueness of scaling factors through full indecomposability",
        "franklin_lorenz_owned": "positive-matrix Hilbert-metric geometric convergence",
        "knight_owned": "local asymptotic singular-value rate",
        "package_derived": "one support-stratified theorem ledger, exact zero-pattern census and convention-locked local Jacobian reconstruction",
    }
    check(data["attribution"] == expected_attribution, "attribution")
    expected_sources = [
        {"source_id": "SK67", "authors": ["Richard Sinkhorn", "Paul Knopp"], "title": "Concerning nonnegative matrices and doubly stochastic matrices", "venue": "Pacific Journal of Mathematics 21(2), 343--348", "year": 1967, "doi": "10.2140/pjm.1967.21.343", "role": "support and total-support theorem"},
        {"source_id": "BPS66", "authors": ["Richard A. Brualdi", "Seymour V. Parter", "Hans Schneider"], "title": "The diagonal equivalence of a nonnegative matrix to a stochastic matrix", "venue": "Journal of Mathematical Analysis and Applications 16(1), 31--50", "year": 1966, "doi": "10.1016/0022-247X(66)90184-3", "role": "full-indecomposability and factor-uniqueness theorem"},
        {"source_id": "FL89", "authors": ["Joel Franklin", "Jens Lorenz"], "title": "On the scaling of multidimensional matrices", "venue": "Linear Algebra and its Applications 114--115, 717--735", "year": 1989, "doi": "10.1016/0024-3795(89)90490-4", "role": "Hilbert-metric geometric convergence"},
        {"source_id": "K08", "authors": ["Philip A. Knight"], "title": "The Sinkhorn--Knopp algorithm: convergence and applications", "venue": "SIAM Journal on Matrix Analysis and Applications 30(1), 261--275", "year": 2008, "doi": "10.1137/060659624", "role": "convergence synthesis and local rate"},
    ]
    check(data["source_registry"] == expected_sources, "source registry")
    expected_theorem = {
        "support_iff_limit": "the alternating iteration converges to a doubly stochastic limit exactly when the matrix has a positive diagonal",
        "total_support_iff_scalable": "a positive diagonal scaling to the limit exists exactly when every positive entry lies on a positive diagonal",
        "scaled_matrix_unique": "when total support holds, the doubly stochastic matrix in the positive diagonal-equivalence class is unique",
        "factor_gauge": "under total support, positive diagonal factors are unique up to one reciprocal scalar exactly when the support is fully indecomposable",
        "positive_contraction": "strict positivity gives geometric convergence in Hilbert projective metric with a data-dependent Birkhoff bound",
        "local_rate": "at a positive doubly stochastic limit S the log-column full-cycle Jacobian is S^T S; on the gauge quotient its generic asymptotic spectral radius is sigma_2(S)^2",
        "period_boundary": "convergence rules out nonconstant recurrent cycles on every convergent scaling orbit",
    }
    check(data["theorem"] == expected_theorem, "theorem ledger")
    expected_route = {
        "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        "overall": "ROUTE_A_REJECTED",
        "a0_reason": "support matchings and scaling factors have no intrinsic rational-prime or prime-power semantics",
        "a1_reason": "convergent scaling has no nonconstant primitive periodic-orbit owner",
        "a2_reason": "matrix scaling and a local Jacobian do not identify a target divisor",
        "a3_reason": "no target continuation, functional equation, counting law or Weil compression follows",
        "a4_reason": "the nonlinear positive-cone iteration supplies no source-native self-adjoint Hilbert-space operator",
        "route_b_invocation_allowed": False,
    }
    check(data["route_a"] == expected_route, "route ledger")
    expected_flags = {
        "target_zero_table_used": False, "target_prime_table_used": False,
        "arithmetic_local_data_used": False, "euler_factor_claimed": False,
        "root_number_claimed": False, "automorphy_claimed": False,
        "target_divisor_claimed": False, "target_functional_equation_claimed": False,
        "hilbert_polya_operator_claimed": False, "route_b_invoked": False,
    }
    check(data["scope_flags"] == expected_flags, "scope flags")
    expected_progress = {
        "explicit_progress": "all square nonnegative matrices are separated by support, total support and full indecomposability, with positive geometric and exact local-rate dynamics",
        "proof_boundary": "the finite zero-pattern and rational iterations are regression oracles, not a proof of the all-matrix theorems",
        "rate_boundary": "there is no dimension-only uniform contraction rate as the projective diameter diverges",
        "zero_boundary": "without total support the limiting matrix need not be reachable by finite positive diagonal factors",
        "period_boundary": "a fixed point is an algorithmic scaling target, not an arithmetic primitive orbit",
    }
    check(data["progress_and_boundary"] == expected_progress, "progress and boundary")
    expected_nonclaims = [
        "priority for matrix-scaling, support, total-support, full-indecomposability or Hilbert-contraction theorems",
        "a dimension-only or zero-pattern-only uniform convergence rate",
        "finite positive scaling factors when total support fails",
        "primitive-orbit arithmetic semantics for an attracting fixed point",
        "intrinsic rational-prime data, a target divisor or a target functional equation",
        "a Hilbert--Polya operator, Route-B authorization, external peer review or an acceptance score",
    ]
    check(data["nonclaims"] == expected_nonclaims, "nonclaims")

    finite = data["finite_regression"]
    rows = finite["pattern_rows"]
    expected_rows = []
    independent_counts: dict[str, dict[str, int]] = {}
    for n in (2, 3):
        counts = {"no_zero_line": 0, "support": 0, "total_support": 0, "fully_indecomposable": 0}
        for mask in range(1 << (n * n)):
            pattern = [[(mask >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
            if not all(sum(row) for row in pattern) or not all(sum(pattern[i][j] for i in range(n)) for j in range(n)):
                continue
            support, total, fully, permanent = independent_layers(pattern)
            counts["no_zero_line"] += 1
            counts["support"] += int(support)
            counts["total_support"] += int(total)
            counts["fully_indecomposable"] += int(fully)
            expected_rows.append((n, mask, pattern, support, total, fully, permanent))
        independent_counts[str(n)] = counts
    check(len(rows) == len(expected_rows) == finite["pattern_row_count"], "pattern population")
    for row, expected in zip(rows, expected_rows):
        n, mask, pattern, support, total, fully, permanent = expected
        check(row["dimension"] == n, "pattern dimension")
        check(row["mask"] == mask, "pattern mask")
        check(row["pattern"] == pattern, "pattern matrix")
        check(row["positive_edge_count"] == sum(map(sum, pattern)), "edge count")
        check(row["positive_diagonal_count"] == permanent, "permanent")
        check(row["support"] is support, "support")
        check(row["total_support"] is total, "total support")
        check(row["fully_indecomposable"] is fully, "fully indecomposable")
    check(finite["pattern_counts"] == independent_counts, "pattern counts")

    check(finite["positive_case_count"] == len(finite["positive_cases"]) == 4, "positive cases")
    check([case["case_id"] for case in finite["positive_cases"]] == [
        "two_by_two_odds_four", "three_by_three_symmetric",
        "three_by_three_high_contrast", "three_by_three_asymmetric_circulant"
    ], "positive case IDs")
    calculated_steps = 0
    calculated_ratios = 0
    for case in finite["positive_cases"]:
        source = matrix(case["source_matrix"])
        target = matrix(case["target_doubly_stochastic"])
        left = [f(value) for value in case["left_scaling"]]
        right = [f(value) for value in case["right_scaling"]]
        n = case["dimension"]
        check(len(source) == len(target) == n, "case dimension")
        for i in range(n):
            check(sum(target[i]) == 1, "target row")
            check(sum(target[j][i] for j in range(n)) == 1, "target col")
            for j in range(n):
                check(left[i] * source[i][j] * right[j] == target[i][j], "scaling identity")
        ratios = ratio_rows(source)
        check(case["cross_ratios"] == ratios, "source ratios")
        check(ratio_rows(target) == ratios, "target ratios")
        calculated_ratios += len(ratios)
        theta_value = theta(source)
        check(f(case["projective_theta"]) == theta_value, "theta")
        root = Fraction(math.isqrt(theta_value.numerator), math.isqrt(theta_value.denominator))
        check(root * root == theta_value, "theta square")
        kappa = (root - 1) / (root + 1)
        check(f(case["birkhoff_kappa"]) == kappa, "kappa")
        check(f(case["full_cycle_contraction_bound"]) == kappa * kappa, "cycle bound")
        S = sp.Matrix([[sp.Rational(value.numerator, value.denominator) for value in row] for row in target])
        if case["case_id"] == "three_by_three_asymmetric_circulant":
            check(S != S.T, "asymmetric transpose sentinel")
            check(S.T * S != S * S, "S-transpose-S differs from S-squared")
        eigs = (S.T * S).eigenvals()
        expected_spectrum = [
            {"eigenvalue": str(value), "multiplicity": int(mult)}
            for value, mult in sorted(eigs.items(), key=lambda pair: float(pair[0]), reverse=True)
        ]
        check(case["local_gram_spectrum"] == expected_spectrum, "local spectrum")
        projective = max(Fraction(str(value)) for value in eigs if str(value) != "1")
        check(f(case["local_projective_rate"]) == projective, "local rate")
        current = source
        previous_distance = None
        for index, step in enumerate(case["iteration_steps"]):
            row_error, col_error = errors(current)
            distance = l1(current, target)
            check(step["iteration"] == index, "iteration index")
            check(f(step["row_error"]) == row_error, "row error")
            check(f(step["column_error"]) == col_error, "column error")
            check(f(step["l1_to_target"]) == distance, "target distance")
            if previous_distance is not None:
                check(distance < previous_distance, "strict positive-case convergence sentinel")
            previous_distance = distance
            current = cycle(current)
            calculated_steps += 1

    check(finite["boundary_case_count"] == len(finite["boundary_cases"]) == 4, "boundary cases")
    check([case["case_id"] for case in finite["boundary_cases"]] == [
        "support_not_total", "total_not_fully_indecomposable",
        "fully_indecomposable_with_zeros", "no_support_hall_failure",
    ], "boundary case IDs")
    check([case["pattern"] for case in finite["boundary_cases"]] == [
        [[1, 1], [1, 0]],
        [[1, 0], [0, 1]],
        [[1, 1, 0], [0, 1, 1], [1, 0, 1]],
        [[1, 0, 0], [1, 0, 0], [0, 1, 1]],
    ], "boundary patterns")
    for case in finite["boundary_cases"]:
        pattern = case["pattern"]
        support, total, fully, permanent = independent_layers(pattern)
        check(case["support"] is support, "boundary support")
        check(case["total_support"] is total, "boundary total")
        check(case["fully_indecomposable"] is fully, "boundary fully")
        check(case["positive_diagonal_count"] == permanent, "boundary permanent")
        if support:
            current = [[Fraction(entry) for entry in row] for row in pattern]
            for index, step in enumerate(case["iteration_steps"]):
                row_error, col_error = errors(current)
                check(step == {"iteration": index, "row_error": str(row_error), "column_error": str(col_error)}, "boundary step")
                current = cycle(current)
                calculated_steps += 1
            check(matrix(case["last_iterate"]) == current, "boundary last")
        else:
            check(case["iteration_steps"] == [] and case["last_iterate"] == [], "no-support stop")
    check(finite["iteration_step_count"] == calculated_steps, "step count")
    check(finite["cross_ratio_count"] == calculated_ratios, "ratio count")
    return CHECKS


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assertions = verify(data)
    print(json.dumps({
        "status": "C191_CHECKER_PASS",
        "assertions": assertions,
        "pattern_rows": data["finite_regression"]["pattern_row_count"],
        "positive_cases": data["finite_regression"]["positive_case_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
