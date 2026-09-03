#!/usr/bin/env python3
"""Independent exact verifier for P173.

The small literal audit enumerates every binary endomorphism and every
subspace through ambient dimension three.  Separate exact-rational routines
rebuild the dimension quotient for several prime powers and test its
complementary Jordan ladder.  No scouting or manuscript code is imported.
Finite computation is falsification evidence, not an all-parameter proof or
a novelty certificate.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def gaussian(n: int, k: int, q: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (k - i) - 1
    check(numerator % denominator == 0, f"Gaussian integrality q={q} n={n} k={k}")
    return numerator // denominator


def injective_count(domain: int, codomain: int, q: int) -> int:
    if domain < 0 or domain > codomain:
        return 0
    answer = 1
    for i in range(domain):
        answer *= q ** codomain - q ** i
    return answer


def endpoint_quotient_count(n: int, a: int, b: int, q: int) -> int:
    return injective_count(a - b, n - a, q)


def quotient(n: int, q: int):
    matrix = [[Fraction(0) for _ in range(n + 1)] for _ in range(n + 1)]
    for a in range(n + 1):
        denominator = q ** (a * (n - a))
        for b in range(a + 1):
            matrix[a][b] = Fraction(
                gaussian(a, b, q) * endpoint_quotient_count(n, a, b, q),
                denominator,
            )
        check(sum(matrix[a]) == 1, f"quotient row q={q} n={n} a={a}")
    return matrix


def identity(n: int):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right)))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matrix_power(matrix, exponent: int):
    answer = identity(len(matrix))
    base = matrix
    while exponent:
        if exponent & 1:
            answer = matmul(answer, base)
        base = matmul(base, base)
        exponent //= 2
    return answer


def rational_rank(matrix) -> int:
    work = [list(map(Fraction, row)) for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next((r for r in range(pivot_row, rows) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][column]:
                scale = work[r][column]
                work[r] = [x - scale * y for x, y in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def shifted(matrix, eigenvalue):
    return [
        [entry - (eigenvalue if i == j else 0) for j, entry in enumerate(row)]
        for i, row in enumerate(matrix)
    ]


def enumerate_binary_subspaces(n: int):
    vectors = tuple(range(1 << n))
    spaces = []
    for mask in range(1 << len(vectors)):
        if not (mask & 1):
            continue
        space = frozenset(v for v in vectors if (mask >> v) & 1)
        if all((x ^ y) in space for x in space for y in space):
            spaces.append(space)
    spaces.sort(key=lambda s: (len(s), tuple(sorted(s))))
    check(len(spaces) == sum(gaussian(n, a, 2) for a in range(n + 1)),
          f"binary subspace census n={n}")
    return tuple(spaces)


def binary_dim(space) -> int:
    return len(space).bit_length() - 1


def binary_apply(matrix_mask: int, vector: int, n: int) -> int:
    output = 0
    for row in range(n):
        parity = 0
        for column in range(n):
            parity ^= ((matrix_mask >> (row * n + column)) & 1) & ((vector >> column) & 1)
        output |= parity << row
    return output


def literal_binary_audit(n: int) -> None:
    spaces = enumerate_binary_subspaces(n)
    index = {space: i for i, space in enumerate(spaces)}
    total_maps = 1 << (n * n)
    transition = [[Fraction(0) for _ in spaces] for _ in spaces]
    qmatrix = quotient(n, 2)

    for source_index, source in enumerate(spaces):
        counts = Counter()
        for matrix_mask in range(total_maps):
            target = frozenset(
                vector for vector in source
                if binary_apply(matrix_mask, vector, n) in source
            )
            check(target in index, f"literal endpoint is subspace n={n}")
            counts[target] += 1

        a = binary_dim(source)
        for target in spaces:
            target_index = index[target]
            b = binary_dim(target)
            contained = target.issubset(source)
            expected = (
                (2 ** (n * n - a * (n - a)))
                * endpoint_quotient_count(n, a, b, 2)
                if contained else 0
            )
            actual = counts[target]
            check(actual == expected,
                  f"ambient fibre n={n} U={source_index} B={target_index}")
            transition[source_index][target_index] = Fraction(actual, total_maps)
        check(sum(transition[source_index]) == 1,
              f"literal stochastic row n={n} U={source_index}")
        check(transition[source_index][source_index] == Fraction(1, 2 ** (a * (n - a))),
              f"literal diagonal n={n} U={source_index}")

    for t in range(5):
        full_power = matrix_power(transition, t)
        quotient_power = matrix_power(qmatrix, t)
        for source_index, source in enumerate(spaces):
            a = binary_dim(source)
            for target_index, target in enumerate(spaces):
                b = binary_dim(target)
                expected = (
                    quotient_power[a][b] / gaussian(a, b, 2)
                    if target.issubset(source) else Fraction(0)
                )
                check(full_power[source_index][target_index] == expected,
                      f"all-time labelled n={n} t={t} U={source_index} B={target_index}")


def audit_jordan(n: int, q: int) -> None:
    matrix = quotient(n, q)
    eigenvalues = [Fraction(1, q ** (a * (n - a))) for a in range(n + 1)]
    check(eigenvalues[0] == 1 and eigenvalues[n] == 1,
          f"absorbing eigenvalues q={q} n={n}")
    one_shift = shifted(matrix, Fraction(1))
    expected_endpoint_nullity = 1 if n == 0 else 2
    check(n + 1 - rational_rank(one_shift) == expected_endpoint_nullity,
          f"endpoint Jordan inventory q={q} n={n}")
    if n == 0:
        check(matrix == [[Fraction(1)]], f"single J1 boundary q={q}")
        return

    for b in range(1, (n + 1) // 2):
        a = n - b
        eigenvalue = eigenvalues[b]
        check(eigenvalue == eigenvalues[a],
              f"complementary equality q={q} n={n} b={b}")
        first = shifted(matrix, eigenvalue)
        second = matmul(first, first)
        check(n + 1 - rational_rank(first) == 1,
              f"paired nullity one q={q} n={n} b={b}")
        check(n + 1 - rational_rank(second) == 2,
              f"paired square nullity two q={q} n={n} b={b}")
        for k in range(b + 1, a):
            check(eigenvalues[k] < eigenvalue,
                  f"strict interior concavity q={q} n={n} b={b} k={k}")

    if n % 2 == 0:
        midpoint = n // 2
        middle_shift = shifted(matrix, eigenvalues[midpoint])
        check(n + 1 - rational_rank(middle_shift) == 1,
              f"midpoint simple q={q} n={n}")


def absorption_means(n: int, q: int):
    matrix = quotient(n, q)
    means = [Fraction(0) for _ in range(n)]
    for a in range(1, n):
        means[a] = (
            1 + sum(matrix[a][b] * means[b] for b in range(a))
        ) / (1 - matrix[a][a])
        check(means[a] > 0, f"positive proper mean q={q} n={n} a={a}")
    return means


def audit_boundaries() -> None:
    check(quotient(0, 2) == [[1]], "n=0 single state")
    check(quotient(1, 2) == [[1, 0], [0, 1]], "n=1 two fixed states")
    expected = [
        [Fraction(1), 0, 0],
        [Fraction(1, 2), Fraction(1, 2), 0],
        [0, 0, Fraction(1)],
    ]
    check(quotient(2, 2) == expected, "binary n=2 quotient")
    check(absorption_means(2, 2)[1] == 2, "binary line mean two")


def main() -> None:
    print("P173 INDEPENDENT EXACT CONTROL")
    print("STATUS HOLD_EXTERNAL")
    for n in range(0, 4):
        literal_binary_audit(n)
        print(f"literal q=2 n={n} subspaces={sum(gaussian(n, a, 2) for a in range(n + 1))} PASS")
    for q in (2, 3, 4, 5):
        for n in range(0, 10):
            audit_jordan(n, q)
            absorption_means(n, q)
        print(f"quotient/Jordan q={q} n=0..9 PASS")
    audit_boundaries()
    print("THEOREM ambient every-target fibres PASS")
    print("THEOREM all-time labelled kernel PASS")
    print("THEOREM complementary Jordan ladder PASS")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("RESULT PASS")


if __name__ == "__main__":
    main()
