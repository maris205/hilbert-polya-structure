#!/usr/bin/env python3
"""Separate SymPy reconstruction of C193 Vieta and tree identities."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c193_markoff_evidence.json"
CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def triple(values: list[str] | None) -> tuple[sp.Integer, sp.Integer, sp.Integer] | None:
    if values is None:
        return None
    return tuple(sp.Integer(value) for value in values)  # type: ignore[return-value]


def polynomial(values: tuple[sp.Integer, sp.Integer, sp.Integer]) -> sp.Integer:
    x, y, z = values
    return sp.expand(x * x + y * y + z * z - 3 * x * y * z)


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    x, y, z, t = sp.symbols("x y z t")
    P = x**2 + y**2 + z**2 - 3 * x * y * z
    replacement = 3 * x * y - z
    check(sp.expand(P.subs(z, replacement) - P) == 0, "Vieta polynomial invariance")
    check(sp.expand(3 * x * y - replacement - z) == 0, "Vieta involution")
    quadratic = t**2 - 3 * x * y * t + x**2 + y**2
    check(sp.expand(quadratic.subs(t, z) - P) == 0, "quadratic equation")
    check(sp.expand(z + replacement - 3 * x * y) == 0, "Vieta root sum")
    check(sp.rem(sp.expand(z * replacement - (x**2 + y**2)), P, z) == 0, "Vieta root product on surface")
    check(sp.expand(quadratic.subs(t, y) - (x**2 - (3 * x - 2) * y**2)) == 0, "between-roots sentinel")
    check(sp.factor(P.subs({y: z})) == x**2 - 3 * x * z**2 + 2 * z**2, "tied-maximum polynomial")
    check(
        sp.expand((3 * y * z - x - z) - ((2 * z - x) + 3 * z * (y - 1))) == 0,
        "first upward-difference decomposition",
    )
    check(
        sp.expand((3 * x * z - y - z) - ((2 * z - y) + 3 * z * (x - 1))) == 0,
        "second upward-difference decomposition",
    )

    finite = data["finite_regression"]
    nodes = {}
    for row in finite["tree_rows"]:
        node = triple(row["triple"])
        assert node is not None
        nodes[node] = row
        check(polynomial(node) == 0, "row polynomial")
        check(0 < node[0] <= node[1] <= node[2], "row order")
        check(sp.Integer(row["height"]) == node[2], "height")
        check(sp.Integer(row["coordinate_sum"]) == sum(node), "sum")
        if node != (1, 1, 1):
            check(node.count(node[2]) == 1, "unique maximum")
            other_root = 3 * node[0] * node[1] - node[2]
            parent = tuple(sorted((node[0], node[1], other_root)))
            check(triple(row["parent"]) == parent, "parent formula")
            check(polynomial(parent) == 0, "parent polynomial")
            check(0 < other_root <= node[1] < node[2], "strict descent inequalities")
            check(node[2] * other_root == node[0] ** 2 + node[1] ** 2, "root product")
            first_up = tuple(sorted((3 * node[1] * node[2] - node[0], node[1], node[2])))
            second_up = tuple(sorted((node[0], 3 * node[0] * node[2] - node[1], node[2])))
            check(first_up[2] > node[2] and polynomial(first_up) == 0, "first nonparent edge ascends")
            check(second_up[2] > node[2] and polynomial(second_up) == 0, "second nonparent edge ascends")
        for child_values in row["children"]:
            child = triple(child_values)
            assert child is not None
            check(polynomial(child) == 0, "child polynomial")
            check(child[2] > node[2], "child growth")

    for row in finite["tree_rows"]:
        node = triple(row["triple"])
        assert node is not None
        for child_values in row["children"]:
            child = triple(child_values)
            if child in nodes:
                check(triple(nodes[child]["parent"]) == node, "two-sided tree edge")

    for values in finite["brute_solutions"]:
        node = triple(values)
        assert node is not None
        check(polynomial(node) == 0, "bounded polynomial")
        check(node[2] <= finite["brute_bound"], "bounded height")

    for record in finite["descent_traces"]:
        trace = [triple(values) for values in record["trace"]]
        check(trace[0] == triple(record["seed"]), "trace seed")
        check(trace[-1] == (1, 1, 1), "trace root")
        heights = [node[2] for node in trace if node is not None]
        check(all(left > right for left, right in zip(heights, heights[1:])), "trace Lyapunov")
        check(len(trace) - 1 == record["depth"], "trace depth")
        for child, parent in zip(trace, trace[1:]):
            assert child is not None and parent is not None
            expected = tuple(sorted((child[0], child[1], 3 * child[0] * child[1] - child[2])))
            check(parent == expected, "trace Vieta edge")

    print(json.dumps({
        "status": "C193_SYMPY_PASS",
        "checks": CHECKS,
        "tree_rows": finite["tree_row_count"],
        "brute_solutions": finite["brute_solution_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
