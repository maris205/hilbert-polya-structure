#!/usr/bin/env python3
"""SymPy matrix-tree and finite-permutation cross-checks for C181."""
from __future__ import annotations

import json
from math import gcd
from functools import reduce
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def permutation_from_order(graph: dict, row: dict) -> tuple[list[tuple[int, ...]], list[int]]:
    n = graph["n"]
    arcs = [tuple(x) for x in graph["arcs"]]
    order = [tuple(x) for x in row["cyclic_orders"]]
    states = []
    from itertools import product
    for positions in product(*(range(len(order[v])) for v in range(n))):
        successor = [arcs[order[v][positions[v]]][1] for v in range(n)]
        # Direct functional-cycle extraction by eventual periodicity.
        cycles = set()
        for start in range(n):
            path, u = [], start
            while u not in path:
                path.append(u)
                u = successor[u]
            cyc = path[path.index(u):]
            rotations = [tuple(cyc[j:] + cyc[:j]) for j in range(len(cyc))]
            cycles.add(min(rotations))
        if len(cycles) == 1:
            cycle_nodes = set(next(iter(cycles)))
            states.extend((chip, *positions) for chip in sorted(cycle_nodes))
    states = sorted(states)
    index = {s: i for i, s in enumerate(states)}
    perm = []
    for state in states:
        chip, positions = state[0], list(state[1:])
        positions[chip] = (positions[chip] + 1) % len(order[chip])
        edge = order[chip][positions[chip]]
        target = (arcs[edge][1], *positions)
        perm.append(index[target])
    return states, perm


def main() -> None:
    evidence = json.loads((ROOT / "results/c181_rotor_router_evidence.json").read_text())
    checks = 0
    graph_map = {g["graph_id"]: g for g in evidence["graph_rows"]}
    for graph in evidence["graph_rows"]:
        n = graph["n"]
        arcs = [tuple(x) for x in graph["arcs"]]
        adjacency = sp.zeros(n)
        outd = [0] * n
        for u, v in arcs:
            adjacency[u, v] += 1
            outd[u] += 1
        lap = sp.diag(*outd) - adjacency
        trees = [int(lap.minor_submatrix(v, v).det()) if n > 1 else 1 for v in range(n)]
        assert trees == graph["arborescence_t"]
        checks += 1
        assert (lap.T * sp.Matrix(trees)).is_zero_matrix
        checks += n
        common = reduce(gcd, trees)
        period = sum(outd[v] * trees[v] for v in range(n)) // common
        assert common == graph["M_gcd"] and period == graph["common_orbit_length_L"]
        checks += 2
        for v in range(n):
            assert (outd[v] * trees[v]) % common == 0 and trees[v] % common == 0
            checks += 2
        if graph["eulerian"]:
            assert len(set(trees)) == 1 and period == len(arcs)
            checks += 2

    z = sp.symbols("z")
    first_rows = {}
    for row in evidence["cyclic_order_rows"]:
        first_rows.setdefault(row["graph_id"], row)
    selected = [g for g in evidence["graph_rows"] if g["n"] <= 3 or g["kind"].startswith("directed multigraph")]
    for graph in selected:
        row = first_rows[graph["graph_id"]]
        states, perm = permutation_from_order(graph, row)
        size = len(states)
        matrix = sp.zeros(size)
        for i, j in enumerate(perm):
            matrix[j, i] = 1
        lhs = sp.det(sp.eye(size) - z * matrix)
        rhs = (1 - z ** graph["common_orbit_length_L"]) ** graph["M_gcd"]
        assert sp.expand(lhs - rhs) == 0
        checks += 1
        L, M = graph["common_orbit_length_L"], graph["M_gcd"]
        for k in range(1, 2 * L + 1):
            fixed = sum(1 for i in range(size) if (lambda j=i: j)() == i) if False else (M * L if k % L == 0 else 0)
            traced = sum(1 for i in range(size) if (lambda start=i: start)() == i and _iterate(perm, i, k) == i)
            assert traced == fixed
            checks += 1

    print(json.dumps({"status": "C181_SYMPY_PASS", "checks": checks, "determinant_graphs": len(selected), "sympy_version": sp.__version__}, sort_keys=True))


def _iterate(perm: list[int], i: int, n: int) -> int:
    for _ in range(n):
        i = perm[i]
    return i


if __name__ == "__main__":
    main()
