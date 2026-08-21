#!/usr/bin/env python3
"""SymPy block-polynomial and finite-graph cross-check for C84."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c84_minimum_repair_matroid_evidence.json"


def main() -> None:
    evidence = json.loads(EVIDENCE.read_bytes())
    assert evidence["schema_id"] == "hcs-c84-minimum-repair-matroid-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"

    u, v = sp.symbols("u v")
    sizes = [1, 1, 2, 5]
    polynomial = 0
    for state in range(1 << len(sizes)):
        full = [index for index in range(len(sizes)) if state & (1 << index)]
        weight = 1
        for index in range(len(sizes)):
            if index not in full:
                weight *= 2 ** sizes[index] - 1
        rank = max(0, len(full) - 2)
        if len(full) <= 2:
            witness_count = 1
        elif len(full) == 3:
            witness_count = sum(sizes[index] for index in full)
        else:
            witness_count = sum(
                sizes[left] * sizes[right]
                for left, right in combinations(full, 2)
            )
        polynomial += weight * u ** rank * v ** witness_count
    polynomial = sp.Poly(sp.expand(64 * (1 + u) * polynomial), u, v)
    coefficient_table = {
        (rho, witness_count): int(coefficient)
        for (rho, witness_count), coefficient in polynomial.terms()
    }
    template_table = {
        (row["rho"], row["witness_count"]): row["support_count"]
        for row in evidence["rho_witness_template_atlas"]["rows"]
    }
    assert coefficient_table == template_table == {
        (0, 1): 30400,
        (1, 1): 30400,
        (1, 4): 1984,
        (1, 7): 192,
        (1, 8): 128,
        (2, 4): 1984,
        (2, 7): 192,
        (2, 8): 128,
        (2, 25): 64,
        (3, 25): 64,
    }
    assert int(polynomial.as_expr().subs({u: 1, v: 1})) == 65536

    parts = [[0], [1], [2, 3], [4, 5, 6, 7, 8]]
    part_of = {
        vertex: part_index
        for part_index, part in enumerate(parts)
        for vertex in part
    }
    multipartite_edges = [
        (left, right)
        for left, right in combinations(range(9), 2)
        if part_of[left] != part_of[right]
    ]
    assert len(multipartite_edges) == 25
    adjacency = sp.zeros(len(multipartite_edges), len(multipartite_edges))
    for left, right in combinations(range(len(multipartite_edges)), 2):
        if set(multipartite_edges[left]) & set(multipartite_edges[right]):
            adjacency[left, right] = adjacency[right, left] = 1
    degrees = [int(sum(adjacency[row, column] for column in range(adjacency.cols)))
               for row in range(adjacency.rows)]
    degree_spectrum = Counter(degrees)
    assert degree_spectrum == Counter({9: 10, 10: 10, 13: 4, 14: 1})
    assert sum(degrees) // 2 == 128
    two_step = adjacency + adjacency ** 2
    assert all(two_step[left, right] > 0
               for left in range(adjacency.rows)
               for right in range(adjacency.cols)
               if left != right)
    nonedges = sum(
        1 for left, right in combinations(range(adjacency.rows), 2)
        if adjacency[left, right] == 0
    )
    assert nonedges == 172

    line_row = evidence["unlabeled_exchange_graph_atlas"]["rows"][-1]
    assert line_row["graph_type"] == "L(K_{1,1,2,5})"
    assert line_row["vertex_count"] == 25
    assert line_row["edge_count"] == 128
    assert line_row["degree_spectrum"] == {"9": 10, "10": 10, "13": 4, "14": 1}
    assert line_row["diameter"] == line_row["radius"] == 2
    assert line_row["unordered_distinct_pair_distance_spectrum"] == {"1": 128, "2": 172}

    print(json.dumps({
        "status": "C84_SYMPY_GRAPH_CROSSCHECK_PASS",
        "template_count": len(coefficient_table),
        "polynomial_total": 65536,
        "line_graph_vertices": adjacency.rows,
        "line_graph_edges": sum(degrees) // 2,
        "line_graph_diameter": 2,
        "line_graph_degree_spectrum": dict(sorted(degree_spectrum.items())),
        "adjacency_rank": int(adjacency.rank()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
