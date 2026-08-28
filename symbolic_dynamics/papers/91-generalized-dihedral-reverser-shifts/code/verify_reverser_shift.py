#!/usr/bin/env python3
"""Exact controls for generalized-dihedral reverser shifts."""

from fractions import Fraction
from itertools import product

import sympy as sp


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def add(a, b, moduli):
    return tuple((x + y) % m for x, y, m in zip(a, b, moduli))


def neg(a, moduli):
    return tuple((-x) % m for x, m in zip(a, moduli))


def scale(sign, a, moduli):
    return a if sign == 1 else neg(a, moduli)


def abelian_elements(moduli):
    return list(product(*[range(m) for m in moduli])) if moduli else [()]


def mul(g, h, moduli):
    a, eps = g
    b, eta = h
    return add(a, scale(1 if eps == 0 else -1, b, moduli), moduli), (eps + eta) % 2


def inv(g, moduli):
    a, eps = g
    return (neg(a, moduli), 0) if eps == 0 else (a, 1)


def conjugate(h, g, moduli):
    return mul(mul(h, g, moduli), inv(h, moduli), moduli)


def adjacency(moduli):
    A = abelian_elements(moduli)
    G = [(a, eps) for eps in (0, 1) for a in A]
    index = {g: i for i, g in enumerate(G)}
    M = [[0] * len(G) for _ in G]
    for g in G:
        target = inv(g, moduli)
        for h in G:
            M[index[g]][index[h]] = int(conjugate(h, g, moduli) == target)
    return G, M


def torsion_two(moduli):
    zero = tuple(0 for _ in moduli)
    return [a for a in abelian_elements(moduli) if add(a, a, moduli) == zero]


def canonical_order(moduli):
    A = abelian_elements(moduli)
    T = set(torsion_two(moduli))
    rt = [(a, 0) for a in sorted(T)]
    ru = [(a, 0) for a in sorted(set(A) - T)]
    unseen = set(A)
    cosets = []
    while unseen:
        x = min(unseen)
        C = sorted(add(x, t, moduli) for t in T)
        cosets.append(C)
        unseen.difference_update(C)
    reflections = [(a, 1) for C in sorted(cosets) for a in C]
    return rt + ru + reflections


def reorder_matrix(G, M, order):
    ix = {g: i for i, g in enumerate(G)}
    return [[M[ix[g]][ix[h]] for h in order] for g in order]


def canonical_formula(N, t):
    c = N // t
    size = 2 * N
    M = [[0] * size for _ in range(size)]
    rt = range(0, t)
    ru = range(t, N)
    refl = range(N, 2 * N)
    for i in rt:
        for j in range(size):
            M[i][j] = 1
    for i in ru:
        for j in refl:
            M[i][j] = 1
    for block in range(c):
        B = range(N + block * t, N + (block + 1) * t)
        for i in B:
            for j in rt:
                M[i][j] = 1
            for j in B:
                M[i][j] = 1
    return M


def rational_rank(M):
    A = [[Fraction(x) for x in row] for row in M]
    rows, cols = len(A), len(A[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        p = A[r][c]
        A[r] = [x / p for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [x - q * y for x, y in zip(A[i], A[r])]
        r += 1
    return r


def matmul(A, B):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*B)] for row in A]


def matvec(A, vector):
    return [sum(x * y for x, y in zip(row, vector)) for row in A]


def check_invariant_decomposition(M, N, t):
    """Check the zero, t-eigen, and three-class quotient spaces exactly."""
    zero = [0] * (2 * N)
    c = N // t
    blocks = [list(range(t)), list(range(t, N))]
    blocks.extend(
        list(range(N + block * t, N + (block + 1) * t))
        for block in range(c)
    )
    for block in blocks:
        if len(block) <= 1:
            continue
        anchor = block[0]
        for index in block[1:]:
            vector = [0] * (2 * N)
            vector[index] = 1
            vector[anchor] = -1
            check(matvec(M, vector) == zero,
                  ("zero subspace", N, t, block, index))

    if c > 1:
        first = list(range(N, N + t))
        for block in range(1, c):
            current = list(range(N + block * t, N + (block + 1) * t))
            vector = [0] * (2 * N)
            for index in first:
                vector[index] = -1
            for index in current:
                vector[index] = 1
            check(matvec(M, vector) == [t * value for value in vector],
                  ("t eigenspace", N, t, block))

    coarse_blocks = [list(range(t)), list(range(t, N)), list(range(N, 2 * N))]
    Q = quotient(N, t)
    for basis_index in range(3):
        vector = [0] * (2 * N)
        for index in coarse_blocks[basis_index]:
            vector[index] = 1
        expected = [0] * (2 * N)
        for output_block, indices in enumerate(coarse_blocks):
            for index in indices:
                expected[index] = Q[output_block][basis_index]
        check(matvec(M, vector) == expected,
              ("quotient action", N, t, basis_index))


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def quotient(N, t):
    return [[t, N - t, N], [0, 0, N], [t, 0, t]]


def trace_formula(N, t, k):
    if N == t:
        return (2 * N) ** k
    Q = quotient(N, t)
    Qk = [[int(i == j) for j in range(3)] for i in range(3)]
    for _ in range(k):
        Qk = matmul(Qk, Q)
    return (N // t - 1) * t**k + trace(Qk)


def expected_charpoly(N, t, lam):
    if N == t:
        return lam ** (2 * N - 1) * (lam - 2 * N)
    c = N // t
    cubic = lam**3 - 2*t*lam**2 + t*(t-N)*lam - N*t*(N-t)
    return lam ** (2*N-c-2) * (lam-t) ** (c-1) * cubic


def reachable(M, start):
    seen = {start}
    frontier = [start]
    while frontier:
        i = frontier.pop()
        for j, edge in enumerate(M[i]):
            if edge and j not in seen:
                seen.add(j)
                frontier.append(j)
    return seen


def recover_parameters(f1, f2):
    roots = [x for x in range(1, f1 + 1) if 2*x*x - 3*f1*x + f2 == 0 and 2*x <= f1]
    check(len(roots) == 1, (f1, f2, roots))
    t = roots[0]
    return f1 - t, t


def check_group(moduli, charpoly=False):
    G, M = adjacency(moduli)
    N = len(G) // 2
    t = len(torsion_two(moduli))
    order = canonical_order(moduli)
    C = reorder_matrix(G, M, order)
    expected_canonical = canonical_formula(N, t)
    for i in range(2 * N):
        for j in range(2 * N):
            check(C[i][j] == expected_canonical[i][j], (moduli, N, t, i, j))
    check_invariant_decomposition(C, N, t)
    check(rational_rank(M) == (1 if N == t else N // t + 2), (moduli, N, t))
    for i in range(2 * N):
        check(len(reachable(M, i)) == 2 * N, (moduli, i))
    identity_rotation = G.index((tuple(0 for _ in moduli), 0))
    check(M[identity_rotation][identity_rotation] == 1)
    P = [[int(i == j) for j in range(2 * N)] for i in range(2 * N)]
    for k in range(1, 11):
        P = matmul(P, M)
        check(trace(P) == trace_formula(N, t, k), (moduli, k, trace(P)))
    f1, f2 = trace_formula(N, t, 1), trace_formula(N, t, 2)
    check(f1 == N + t)
    check(f2 == t * (3 * N + t))
    check(recover_parameters(f1, f2) == (N, t))
    if charpoly:
        lam = sp.symbols("lam")
        actual = sp.Matrix(M).charpoly(lam).as_expr()
        check(sp.expand(actual - expected_charpoly(N, t, lam)) == 0, moduli)
        z = sp.symbols("z")
        # Reuse the independently computed characteristic polynomial instead
        # of asking a symbolic determinant routine to expand a second large
        # polynomial matrix.
        det = sp.cancel(z ** (2 * N) * actual.subs(lam, 1 / z))
        if N == t:
            expected_det = 1 - 2 * N * z
        else:
            c = N // t
            expected_det = (1-t*z)**(c-1) * (
                1-2*t*z+t*(t-N)*z**2-N*t*(N-t)*z**3
            )
        check(sp.expand(det - expected_det) == 0, (moduli, det, expected_det))
    return N, t, C


def main():
    families = [
        (), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,),
        (2, 2), (2, 4), (2, 6), (2, 8), (3, 3), (3, 6), (4, 4),
        (2, 2, 2), (2, 2, 4), (3, 3, 3),
    ]
    registry = {}
    for moduli in families:
        N = 1
        for m in moduli:
            N *= m
        result = check_group(moduli, charpoly=N <= 16)
        key = result[:2]
        if key in registry:
            check(result[2] == registry[key], (moduli, key))
        else:
            registry[key] = result[2]
    _, _, z9 = check_group((9,), charpoly=True)
    _, _, z3sq = check_group((3, 3), charpoly=True)
    check(z9 == z3sq, "Z/9 and (Z/3)^2 should collapse")
    print(f"PASS: {ASSERTIONS:,} exact assertions")
    print(f"{len(families)} finite-abelian presentations: conjugation rule, invariant decomposition, canonical collapse, rank, and mixing verified")
    print("period traces k<=10 and all small characteristic/zeta polynomials verified")
    print("same-parameter collapses include Z/9 vs (Z/3)^2 and Z/2 x Z/8 vs Z/4 x Z/4")


if __name__ == "__main__":
    main()
