#!/usr/bin/env python3
"""Separate SymPy reconstruction of C191 scaling identities and spectra."""
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c191_sinkhorn_evidence.json"
CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def rat(value: str | int) -> sp.Rational:
    fraction = Fraction(str(value))
    return sp.Rational(fraction.numerator, fraction.denominator)


def smatrix(values: list[list[str | int]]) -> sp.Matrix:
    return sp.Matrix([[rat(value) for value in row] for row in values])


def ryser_permanent(pattern: list[list[int]]) -> int:
    n = len(pattern)
    total = 0
    for mask in range(1, 1 << n):
        product = 1
        for i in range(n):
            product *= sum(pattern[i][j] for j in range(n) if mask >> j & 1)
        total += (-1) ** (n - mask.bit_count()) * product
    return total


def normalize_rows(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(matrix.rows, matrix.cols, lambda i, j: sp.cancel(matrix[i, j] / sum(matrix[i, k] for k in range(matrix.cols))))


def normalize_cols(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(matrix.rows, matrix.cols, lambda i, j: sp.cancel(matrix[i, j] / sum(matrix[k, j] for k in range(matrix.rows))))


def main() -> None:
    data = json.loads(EVIDENCE.read_text())

    u, v, p = sp.symbols("u v p", positive=True)
    p_expr = u / (u + v)
    S2 = sp.Matrix([[p_expr, 1 - p_expr], [1 - p_expr, p_expr]])
    check(all(sp.simplify(sum(S2[i, j] for j in range(2)) - 1) == 0 for i in range(2)), "symbolic rows")
    check(all(sp.simplify(sum(S2[i, j] for i in range(2)) - 1) == 0 for j in range(2)), "symbolic cols")
    check(sp.simplify(S2[0, 0] * S2[1, 1] / (S2[0, 1] * S2[1, 0]) - u**2 / v**2) == 0, "odds ratio")
    gram2 = sp.simplify(S2.T * S2)
    one = sp.Matrix([1, 1])
    anti = sp.Matrix([1, -1])
    check(sp.simplify(gram2 * one - one) == sp.zeros(2, 1), "gauge eigenvector")
    check(sp.simplify(gram2 * anti - ((u - v) / (u + v)) ** 2 * anti) == sp.zeros(2, 1), "projective eigenvector")

    x1, x2 = sp.symbols("x1 x2")
    x = sp.Matrix([x1, x2])
    # The log full-cycle map is -log(S^T exp(-log(S exp(x)))).
    row_sums = S2 * sp.Matrix([sp.exp(x1), sp.exp(x2)])
    col_map = sp.Matrix([
        -sp.log(sum(S2[i, j] / row_sums[i] for i in range(2)))
        for j in range(2)
    ])
    jac = sp.simplify(col_map.jacobian(x).subs({x1: 0, x2: 0}))
    check(sp.simplify(jac - gram2) == sp.zeros(2), "symbolic log Jacobian")

    finite = data["finite_regression"]
    support_count = total_count = fully_count = 0
    for row in finite["pattern_rows"]:
        pattern = row["pattern"]
        permanent = ryser_permanent(pattern)
        check(permanent == row["positive_diagonal_count"], "Ryser permanent")
        check((permanent > 0) is row["support"], "support from permanent")
        edge_membership = []
        n = len(pattern)
        for i in range(n):
            for j in range(n):
                if not pattern[i][j]:
                    continue
                minor = [source_row[:j] + source_row[j + 1 :] for source_row in pattern[:i] + pattern[i + 1 :]]
                edge_membership.append(ryser_permanent(minor) > 0 if minor else True)
        check((permanent > 0 and all(edge_membership)) is row["total_support"], "total support minors")
        support_count += int(row["support"])
        total_count += int(row["total_support"])
        fully_count += int(row["fully_indecomposable"])
    check(support_count == sum(counts["support"] for counts in finite["pattern_counts"].values()), "support total")
    check(total_count == sum(counts["total_support"] for counts in finite["pattern_counts"].values()), "total-support total")
    check(fully_count == sum(counts["fully_indecomposable"] for counts in finite["pattern_counts"].values()), "fully total")

    for case in finite["positive_cases"]:
        A = smatrix(case["source_matrix"])
        S = smatrix(case["target_doubly_stochastic"])
        left = sp.diag(*[rat(value) for value in case["left_scaling"]])
        right = sp.diag(*[rat(value) for value in case["right_scaling"]])
        check(left * A * right == S, "exact diagonal equivalence")
        check(all(sum(S[i, j] for j in range(S.cols)) == 1 for i in range(S.rows)), "case rows")
        check(all(sum(S[i, j] for i in range(S.rows)) == 1 for j in range(S.cols)), "case cols")
        gram = S.T * S
        log_variables = sp.symbols(f"u0:{S.cols}")
        exponentials = sp.Matrix([sp.exp(value) for value in log_variables])
        row_totals = S * exponentials
        log_column_map = sp.Matrix([
            -sp.log(sum(S[i, j] / row_totals[i] for i in range(S.rows)))
            for j in range(S.cols)
        ])
        direct_jacobian = sp.simplify(log_column_map.jacobian(log_variables).subs({value: 0 for value in log_variables}))
        check(sp.simplify(direct_jacobian - gram) == sp.zeros(S.rows), "direct case Jacobian")
        if case["case_id"] == "three_by_three_asymmetric_circulant":
            check(S != S.T, "asymmetric case")
            check(gram != S * S, "transpose blind-spot sentinel")
        lam = sp.symbols("lam")
        check(sp.expand(gram.charpoly(lam).as_expr()) == sp.expand(sp.prod((lam - rat(row["eigenvalue"])) ** row["multiplicity"] for row in case["local_gram_spectrum"])), "characteristic polynomial")
        current = A
        for step in case["iteration_steps"]:
            row_error = max(abs(sum(current[i, j] for j in range(current.cols)) - 1) for i in range(current.rows))
            col_error = max(abs(sum(current[i, j] for i in range(current.rows)) - 1) for j in range(current.cols))
            distance = sum(abs(current[i, j] - S[i, j]) for i in range(current.rows) for j in range(current.cols))
            check(row_error == rat(step["row_error"]), "SymPy row error")
            check(col_error == rat(step["column_error"]), "SymPy col error")
            check(distance == rat(step["l1_to_target"]), "SymPy distance")
            current = normalize_cols(normalize_rows(current))
        # Every stored 2x2 cross-ratio is invariant under the declared factors.
        for ratio in case["cross_ratios"]:
            i, j, k, ell = ratio["indices"]
            value = A[i, k] * A[j, ell] / (A[i, ell] * A[j, k])
            check(value == rat(ratio["value"]), "SymPy cross ratio")
            check(value == S[i, k] * S[j, ell] / (S[i, ell] * S[j, k]), "scaled ratio")

    print(json.dumps({
        "status": "C191_SYMPY_PASS",
        "checks": CHECKS,
        "pattern_rows": finite["pattern_row_count"],
        "positive_cases": finite["positive_case_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
