#!/usr/bin/env python3
"""Fresh symbolic incidence, cut-flow and Hessian checks for HCS-C259."""
from __future__ import annotations

import itertools
import sympy as s


def decode(n, word):
    degree = [1] * n
    for value in word:
        degree[value] += 1
    edges = []
    for value in word:
        leaf = min(i for i, item in enumerate(degree) if item == 1)
        edges.append(tuple(sorted((leaf, value))))
        degree[leaf] -= 1
        degree[value] -= 1
    rest = [i for i, item in enumerate(degree) if item == 1]
    edges.append(tuple(rest))
    return sorted(edges)


def orient(n, edges):
    adjacency = [[] for _ in range(n)]
    for left, right in edges:
        adjacency[left].append(right)
        adjacency[right].append(left)
    parent = {0: 0}
    queue = [0]
    rooted = []
    for vertex in queue:
        for child in sorted(adjacency[vertex]):
            if child in parent:
                continue
            parent[child] = vertex
            queue.append(child)
            rooted.append((vertex, child))
    return rooted


def incidence(n, rooted):
    matrix = s.zeros(n, n - 1)
    for column, (parent, child) in enumerate(rooted):
        matrix[parent, column] = -1
        matrix[child, column] = 1
    return matrix


checks = 0


def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


# The scalar equilibrium and linearization identities.
K, F, delta = s.symbols("K F delta", positive=True, real=True)
check(s.simplify(s.diff(K * s.sin(delta), delta) - K * s.cos(delta)) == 0, "edge derivative")
check(s.simplify(s.sin(s.asin(F / K)) - F / K) == 0, "principal inverse sine")
check(s.simplify(s.sin(s.pi - s.asin(F / K)) - F / K) == 0, "second inverse sine")
check(s.simplify(s.cos(s.pi - s.asin(F / K)) + s.cos(s.asin(F / K))) == 0, "cosine sign")

# For representative Prüfer words at every size, verify the exact incidence
# isomorphism, subtree formula, Hessian congruence and determinant factorization.
for n in range(2, 8):
    words = list(itertools.islice(itertools.product(range(n), repeat=n - 2), 0, min(5, n ** max(n - 2, 0))))
    for word in words:
        rooted = orient(n, decode(n, word))
        B = incidence(n, rooted)
        check(B.rank() == n - 1, f"incidence rank n={n} word={word}")
        check(B.T * s.ones(n, 1) == s.zeros(n - 1, 1), f"gauge kernel n={n}")
        Q = s.zeros(n, n - 1)
        for column in range(n - 1):
            Q[0, column] = -1
            Q[column + 1, column] = 1
        P = B.T * Q
        check(P.det() != 0, f"quotient-edge isomorphism n={n}")
        weights = s.diag(*s.symbols(f"w0:{n-1}", nonzero=True, real=True))
        H = B * weights * B.T
        reduced = Q.T * H * Q
        check(s.simplify(reduced - P.T * weights * P) == s.zeros(n - 1), f"congruence n={n}")
        check(s.factor(reduced.det() - P.det() ** 2 * weights.det()) == 0, f"determinant n={n}")

        flows = s.Matrix(s.symbols(f"f0:{n-1}", real=True))
        eta = B * flows
        check(s.simplify(sum(eta)) == 0, f"centered incidence n={n}")
        children = {vertex: [] for vertex in range(n)}
        for parent, child in rooted:
            children[parent].append(child)
        for edge_index, (_, child) in enumerate(rooted):
            subtree = set()
            stack = [child]
            while stack:
                vertex = stack.pop()
                subtree.add(vertex)
                stack.extend(children[vertex])
            check(s.simplify(sum(eta[vertex] for vertex in subtree) - flows[edge_index]) == 0, f"cut sum n={n} edge={edge_index}")

# Rational Pythagorean receipt used by the producer.
for j in range(1, 9):
    t = s.Rational(j, j + 1)
    sine = 2 * t / (1 + t ** 2)
    cosine = (1 - t ** 2) / (1 + t ** 2)
    check(s.factor(sine ** 2 + cosine ** 2 - 1) == 0, f"Pythagorean row {j}")
    check(0 < sine < 1 and 0 < cosine < 1, f"strict row {j}")

print(f"C259_SYMPY_PASS ({checks} symbolic identities; incidence, cuts, congruence, inertia determinant and branch signs)")
