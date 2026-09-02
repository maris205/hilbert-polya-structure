#!/usr/bin/env python3
"""SymPy matrix/root cross-check for the HCS-C286 receipt."""
from __future__ import annotations

import json
from collections import deque
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c286_numbers_game_evidence.json").read_text())
checks = 0


def claim(condition: bool) -> None:
    global checks
    assert bool(condition)
    checks += 1


def root_reflection(cartan: sp.Matrix, node: int) -> sp.Matrix:
    matrix = sp.eye(cartan.rows)
    for column in range(cartan.cols):
        matrix[node, column] -= cartan[node, column]
    return matrix


def weight_reflection(cartan: sp.Matrix, node: int) -> sp.Matrix:
    matrix = sp.eye(cartan.rows)
    for row in range(cartan.rows):
        matrix[row, node] -= cartan[row, node]
    return matrix


def positive_roots(cartan: sp.Matrix) -> set[tuple[int, ...]]:
    reflections = [root_reflection(cartan, node) for node in range(cartan.rows)]
    roots: set[tuple[int, ...]] = set()
    queue: deque[tuple[int, ...]] = deque()
    for node in range(cartan.rows):
        for sign in (-1, 1):
            root = tuple(sign * int(node == j) for j in range(cartan.rows))
            roots.add(root)
            queue.append(root)
    while queue:
        root = sp.Matrix(queue.popleft())
        for reflection in reflections:
            image = tuple(int(value) for value in reflection * root)
            if image not in roots:
                roots.add(image)
                queue.append(image)
    claim(all((all(x >= 0 for x in root) or all(x <= 0 for x in root)) for root in roots))
    positive = {root for root in roots if any(root) and all(x >= 0 for x in root)}
    claim(len(roots) == 2 * len(positive))
    return positive


def main() -> None:
    case_rows = DATA["regression"]["case_rows"]
    branches = DATA["regression"]["branch_rows"]
    by_case: dict[str, list[dict]] = {}
    for branch in branches:
        by_case.setdefault(branch["case"], []).append(branch)

    seen_cartans: set[tuple[tuple[int, ...], ...]] = set()
    for row in case_rows:
        cartan_tuple = tuple(tuple(line) for line in row["cartan"])
        cartan = sp.Matrix(cartan_tuple)
        rank = cartan.rows
        claim(cartan.rows == cartan.cols == row["rank"])
        claim(cartan.det() > 0)
        reflections = [root_reflection(cartan, node) for node in range(rank)]
        weight_reflections = [weight_reflection(cartan, node) for node in range(rank)]
        for node in range(rank):
            claim(reflections[node] ** 2 == sp.eye(rank))
            claim(weight_reflections[node] ** 2 == sp.eye(rank))
            claim(reflections[node].det() == -1)
            polynomial = sp.expand(reflections[node].charpoly().as_expr())
            claim(polynomial == sp.expand((sp.Symbol("lambda") + 1) * (sp.Symbol("lambda") - 1) ** (rank - 1)))
        if cartan_tuple not in seen_cartans:
            seen_cartans.add(cartan_tuple)
            for i in range(rank):
                for j in range(i + 1, rank):
                    product = cartan[i, j] * cartan[j, i]
                    order = {0: 2, 1: 3, 2: 4, 3: 6}[int(product)]
                    claim((reflections[i] * reflections[j]) ** order == sp.eye(rank))

        roots = positive_roots(cartan)
        zero_set = set(row["zero_set"])
        parabolic = {
            root for root in roots
            if all(root[index] == 0 for index in range(rank) if index not in zero_set)
        }
        claim(row["observed_length"] == len(roots) - len(parabolic))

        initial = sp.Matrix(row["initial_coordinates"])
        terminal = sp.Matrix(row["observed_terminal_coordinates"])
        sample = by_case[row["case"]]
        for branch in (sample[0], sample[-1]):
            root_action = sp.eye(rank)
            weight_action = sp.eye(rank)
            for one_based in branch["sequence"]:
                node = one_based - 1
                root_action = reflections[node] * root_action
                weight_action = weight_reflections[node] * weight_action
            claim(weight_action * initial == terminal)
            claim(root_action.det() == (-1) ** branch["length"])
            claim(all(value <= 0 for value in terminal))

    # Known root counts supply a separate family-level sentinel.
    root_count_by_case = {}
    for row in case_rows:
        cartan = sp.Matrix(row["cartan"])
        root_count_by_case[row["case"]] = len(positive_roots(cartan))
    claim(root_count_by_case["a4_strict"] == 10)
    claim(root_count_by_case["b3_strict"] == 9)
    claim(root_count_by_case["c3_strict"] == 9)
    claim(root_count_by_case["d4_strict"] == 12)
    claim(root_count_by_case["g2_strict"] == 6)
    claim(root_count_by_case["a2_plus_a1_strict"] == 4)
    print(f"C286_SYMPY_PASS ({checks} symbolic matrix/root checks)")


if __name__ == "__main__":
    main()
