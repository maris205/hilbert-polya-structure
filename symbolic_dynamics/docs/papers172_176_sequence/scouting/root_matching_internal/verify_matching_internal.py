#!/usr/bin/env python3
"""Exact scout: retain vertices internally paired by a fresh perfect matching."""

from fractions import Fraction
from itertools import combinations


def perfect_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j + 1:]
        for tail in perfect_matchings(rest):
            yield ((a, b),) + tail


def odd_dfact(k):
    # Number of perfect matchings on k vertices; convention M(0)=1.
    if k < 0 or k % 2:
        return 0
    ans = 1
    for j in range(1, k, 2):
        ans *= j
    return ans


def falling(a, k):
    if k < 0 or k > a:
        return 0
    ans = 1
    for j in range(k):
        ans *= a - j
    return ans


def retain(A, matching):
    return frozenset(x for e in matching if e[0] in A and e[1] in A for x in e)


def count_formula(N, a, b):
    if b % 2 or b > a:
        return 0
    c = a - b
    return odd_dfact(b) * falling(N - a, c) * odd_dfact(N - 2 * a + b)


def rank(matrix):
    A = [list(row) for row in matrix]
    m, n = len(A), len(A[0]) if A else 0
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        z = A[r][c]
        A[r] = [x / z for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                z = A[i][c]
                A[i] = [x - z * y for x, y in zip(A[i], A[r])]
        r += 1
    return r


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def main():
    assertions = 0
    summaries = []
    for N in range(2, 11, 2):
        mats = tuple(perfect_matchings(range(N)))
        assert len(mats) == odd_dfact(N)
        assertions += 1
        if N <= 8:
            for mask in range(1 << N):
                A = frozenset(i for i in range(N) if mask >> i & 1)
                counts = {}
                for M in mats:
                    B = retain(A, M)
                    counts[B] = counts.get(B, 0) + 1
                for b in range(N + 1):
                    for B in combinations(A, b):
                        B = frozenset(B)
                        want = count_formula(N, len(A), b)
                        assert counts.get(B, 0) == want
                        assertions += 1
                assert sum(counts.values()) == len(mats)
                assertions += 1

        Q = [[Fraction(0) for _ in range(N + 1)] for _ in range(N + 1)]
        for a in range(N + 1):
            for b in range(a + 1):
                from math import comb
                Q[a][b] = Fraction(comb(a, b) * count_formula(N, a, b), odd_dfact(N))
            assert sum(Q[a]) == 1
            assertions += 1
        lambdas = [Q[a][a] for a in range(N + 1)]
        jordan = []
        for b in range(2, N // 2 + 1, 2):
            a = N - b
            if a == b:
                continue
            lam = lambdas[b]
            M = [[Q[i][j] - (lam if i == j else 0) for j in range(N + 1)]
                 for i in range(N + 1)]
            M2 = matmul(M, M)
            null1 = N + 1 - rank(M)
            null2 = N + 1 - rank(M2)
            jordan.append((b, a, null1, null2))
            assert (null1, null2) == (1, 2)
            assertions += 1
        summaries.append((N, len(mats), tuple(lambdas), tuple(jordan)))
    print("MATCHING_INTERNAL_PASS")
    print("assertions", assertions)
    for row in summaries:
        print(row)


if __name__ == "__main__":
    main()
