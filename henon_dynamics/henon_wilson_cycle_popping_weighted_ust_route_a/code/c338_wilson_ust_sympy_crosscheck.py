#!/usr/bin/env python3
"""Independent symbolic-algebra lane for HCS-C338."""
from __future__ import annotations

import itertools
import math
import sys

import sympy as sp


def need(condition, label):
    if condition is not True and condition != sp.S.true:
        raise AssertionError(label)


def incidence(n, edges, root):
    columns = []
    for u, v in edges:
        vector = [sp.Integer(index == u) - sp.Integer(index == v) for index in range(n)]
        columns.append([value for index, value in enumerate(vector) if index != root])
    return sp.Matrix.hstack(*(sp.Matrix(column) for column in columns)) if columns else sp.zeros(n - 1, 0)


def is_tree(n, edges, subset):
    if len(subset) != n - 1:
        return False
    groups = [{i} for i in range(n)]
    for index in subset:
        u, v = edges[index]
        left = next(group for group in groups if u in group)
        right = next(group for group in groups if v in group)
        if left is right:
            return False
        left.update(right)
        groups.remove(right)
    return len(groups) == 1


def main():
    if sys.flags.optimize:
        raise RuntimeError("C338 SymPy lane refuses optimized Python")
    checks = 0
    a, b, c = sp.symbols("a b c", positive=True)
    edges = [(0, 1), (0, 2), (1, 2)]
    weights = sp.diag(a, b, c)
    boundary = incidence(3, edges, 2)
    lap = boundary * weights * boundary.T
    z = sp.expand(a * b + a * c + b * c)
    need(sp.expand(lap.det() - z) == 0, "symbolic triangle matrix tree")
    h = sp.simplify(boundary.T * lap.inv() * boundary * weights)
    need(sp.simplify(h * h - h) == sp.zeros(3), "symbolic projection")
    tree_weights = {(0, 1): a * b, (0, 2): a * c, (1, 2): b * c}
    for order in range(4):
        for subset in itertools.combinations(range(3), order):
            numerator = sum(weight for tree_edges, weight in tree_weights.items()
                            if set(subset).issubset(tree_edges))
            minor = h.extract(subset, subset).det() if subset else sp.Integer(1)
            need(sp.cancel(minor - numerator / z) == 0, f"triangle transfer {subset}")
            checks += 1
    # Three distinctly labelled parallel edges: the kernel has rank one, so
    # every simultaneous two-edge event vanishes.
    parallel_boundary = incidence(2, [(0, 1)] * 3, 1)
    parallel_weights = sp.diag(a, b, c)
    parallel_lap = parallel_boundary * parallel_weights * parallel_boundary.T
    parallel_h = sp.simplify(parallel_boundary.T * parallel_lap.inv()
                             * parallel_boundary * parallel_weights)
    need(sp.simplify(parallel_h * parallel_h - parallel_h) == sp.zeros(3), "parallel projection")
    for i in range(3):
        need(sp.cancel(parallel_h[i, i] - (a, b, c)[i] / (a + b + c)) == 0, "parallel singleton")
        checks += 1
    for i, j in itertools.combinations(range(3), 2):
        need(sp.cancel(parallel_h.extract([i, j], [i, j]).det()) == 0, "parallel pair")
        checks += 1
    # An independent six-edge K4 computation checks every transfer-current
    # minor, including the rank boundary above order three.
    k4_edges = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    numeric_weights = [2, 3, 5, 7, 11, 13]
    k4_boundary = incidence(4, k4_edges, 3)
    k4_c = sp.diag(*numeric_weights)
    k4_lap = k4_boundary * k4_c * k4_boundary.T
    k4_z = int(k4_lap.det())
    k4_h = k4_boundary.T * k4_lap.inv() * k4_boundary * k4_c
    tree_rows = []
    for subset in itertools.combinations(range(6), 3):
        if is_tree(4, k4_edges, subset):
            tree_rows.append((set(subset), math.prod(numeric_weights[i] for i in subset)))
    need(k4_z == sum(weight for _, weight in tree_rows), "K4 matrix tree")
    need(k4_h * k4_h == k4_h and k4_h.trace() == 3, "K4 projection")
    checks += 2
    for mask in range(1 << 6):
        subset = [i for i in range(6) if (mask >> i) & 1]
        numerator = sum(weight for tree_edges, weight in tree_rows if set(subset) <= tree_edges)
        value = k4_h.extract(subset, subset).det() if subset else sp.Integer(1)
        need(sp.cancel(value - sp.Rational(numerator, k4_z)) == 0, f"K4 transfer {mask}")
        checks += 1
    # Root deletion changes coordinates but not edge-space transfer current.
    kernels = []
    for root in range(4):
        matrix = incidence(4, k4_edges, root)
        reduced_lap = matrix * k4_c * matrix.T
        need(reduced_lap.det() == k4_z, "root-independent cofactor")
        kernels.append(matrix.T * reduced_lap.inv() * matrix * k4_c)
        checks += 1
    need(all(kernel == kernels[0] for kernel in kernels), "root-independent kernel")
    checks += 1
    print(f"C338 SymPy cross-check: PASS {checks} symbolic/exact checks")


if __name__ == "__main__":
    main()
