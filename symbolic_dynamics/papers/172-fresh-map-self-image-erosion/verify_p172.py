#!/usr/bin/env python3
"""Independent exact verifier for P172.

The program imports no scouting or manuscript code.  It enumerates literal
restrictions f|A in small boxes, rebuilds the full labelled transition matrix,
compares quotient powers, and performs exact-rational Jordan tests.  Finite
checks are falsifiers, not proofs of the all-parameter statements or novelty.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def stirling2(n: int, k: int) -> int:
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            table[i][j] = table[i - 1][j - 1] + j * table[i - 1][j]
    return table[n][k]


def subsets(n: int):
    return tuple(mask for mask in range(1 << n))


def size(mask: int) -> int:
    return mask.bit_count()


def matmul(a, b):
    rows, inner, cols = len(a), len(b), len(b[0])
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def identity(n: int):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def matrix_power(a, exponent: int):
    answer = identity(len(a))
    base = a
    while exponent:
        if exponent & 1:
            answer = matmul(answer, base)
        base = matmul(base, base)
        exponent //= 2
    return answer


def rank(matrix) -> int:
    a = [list(map(Fraction, row)) for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivot_row = 0
    for column in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][column]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][column]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][column]:
                scale = a[r][column]
                a[r] = [x - scale * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def endpoint_formula(n: int, a: int, b: int, k: int) -> int:
    r = k - b
    if r < 0 or r > n - a or k > a:
        return 0
    return comb(n - a, r) * factorial(k) * stirling2(a, k)


def quotient(n: int):
    qmat = [[Fraction(0) for _ in range(n + 1)] for _ in range(n + 1)]
    for a in range(n + 1):
        denominator = n**a if a else 1
        for b in range(a + 1):
            numerator = sum(endpoint_formula(n, a, b, k) for k in range(a + 1))
            qmat[a][b] = Fraction(comb(a, b) * numerator, denominator)
        check(sum(qmat[a]) == 1, f"quotient row n={n} a={a}")
    return qmat


def literal_transition(n: int):
    states = subsets(n)
    transition = [[Fraction(0) for _ in states] for _ in states]
    marked = {}
    for source in states:
        elements = tuple(i for i in range(n) if (source >> i) & 1)
        denominator = n ** len(elements) if elements else 1
        counts = {}
        for values in product(range(n), repeat=len(elements)):
            image = 0
            for value in values:
                image |= 1 << value
            target = source & image
            key = (target, size(image))
            counts[key] = counts.get(key, 0) + 1
        for (target, image_size), count in counts.items():
            transition[source][target] += Fraction(count, denominator)
            marked[source, target, image_size] = count
        check(sum(transition[source]) == 1, f"literal row n={n} A={source}")

        a = size(source)
        for target in states:
            b = size(target)
            for k in range(a + 1):
                actual = marked.get((source, target, k), 0)
                expected = endpoint_formula(n, a, b, k) if target & ~source == 0 else 0
                check(actual == expected, f"marked endpoint n={n} A={source} B={target} k={k}")
    return transition


def audit_labelled_powers(n: int) -> None:
    pmat = literal_transition(n)
    qmat = quotient(n)
    states = subsets(n)
    for t in range(5):
        pt = matrix_power(pmat, t)
        qt = matrix_power(qmat, t)
        for source in states:
            a = size(source)
            for target in states:
                b = size(target)
                expected = (
                    qt[a][b] / comb(a, b)
                    if target & ~source == 0 and b <= a
                    else Fraction(0)
                )
                check(pt[source][target] == expected,
                      f"all-time labelled n={n} t={t} A={source} B={target}")


def audit_jordan(n: int) -> None:
    qmat = quotient(n)
    lam = Fraction(factorial(n), n**n)
    check(lam == Fraction(factorial(n - 1), n ** (n - 1)), f"top equality n={n}")
    for a in range(n - 1):
        check(Fraction(factorial(a), n**a) > Fraction(factorial(a + 1), n ** (a + 1)),
              f"strict diagonal n={n} a={a}")
    shifted = [
        [qmat[i][j] - (lam if i == j else 0) for j in range(n + 1)]
        for i in range(n + 1)
    ]
    square = matmul(shifted, shifted)
    check((n + 1) - rank(shifted) == 1, f"Jordan nullity one n={n}")
    check((n + 1) - rank(square) == 2, f"Jordan square nullity two n={n}")
    check(qmat[n][n - 1] > 0, f"positive adjacent coupling n={n}")


def expected_absorption(qmat):
    n = len(qmat) - 1
    e = [Fraction(0) for _ in range(n + 1)]
    for a in range(1, n + 1):
        if qmat[a][a] == 1:
            e[a] = None
        else:
            subtotal = sum(qmat[a][b] * e[b] for b in range(a) if e[b] is not None)
            e[a] = (1 + subtotal) / (1 - qmat[a][a])
    return e


def audit_boundaries() -> None:
    q1 = quotient(1)
    check(q1 == [[1, 0], [0, 1]], "n=1 two fixed states")
    q2 = quotient(2)
    expected = [
        [Fraction(1), 0, 0],
        [Fraction(1, 2), Fraction(1, 2), 0],
        [0, Fraction(1, 2), Fraction(1, 2)],
    ]
    check(q2 == expected, "n=2 quotient")
    check(expected_absorption(q2)[2] == 4, "n=2 mean four")


def main() -> None:
    print("P172 INDEPENDENT EXACT CONTROL")
    print("STATUS HOLD_EXTERNAL")
    for n in range(1, 7):
        audit_labelled_powers(n)
        print(f"literal n={n} states={1<<n} PASS")
    for n in range(2, 10):
        audit_jordan(n)
        e = expected_absorption(quotient(n))
        check(all(value is not None and value >= 0 for value in e), f"finite absorption n={n}")
        print(f"Jordan n={n} nullities=1,2 mean_full={e[n]} PASS")
    audit_boundaries()
    print("THEOREM endpoint/image-size count PASS")
    print("THEOREM all-time labelled quotient PASS")
    print("THEOREM forced top J2 PASS")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("RESULT PASS")


if __name__ == "__main__":
    main()
