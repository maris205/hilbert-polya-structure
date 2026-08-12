"""Intrinsic wheel-sieve recursion and its exact level-DAG.

The recursion starts from ``W_0=1`` and no stored prime list.  At every step
the next multiplier is the least integer larger than the previous multiplier
and coprime to the current wheel.  The usual induction shows that this least
survivor is prime; the implementation never consults a prime table.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from math import gcd
from random import Random
from typing import Callable, Iterable, Iterator, Literal, Sequence


Control = Literal["arithmetic", "fixed_branch", "cyclic_branch", "random_branch"]


@dataclass(frozen=True)
class WheelLevel:
    level: int
    multiplier: int
    modulus: int
    residues: tuple[int, ...]


@dataclass(frozen=True)
class Edge:
    parent_level: int
    parent_residue: int
    child_level: int
    child_residue: int
    branch: int
    multiplier: int

    def serialize(self) -> str:
        return (
            f"{self.parent_level},{self.parent_residue},{self.child_level},"
            f"{self.child_residue},{self.branch},{self.multiplier}\n"
        )


def least_coprime_successor(last: int, modulus: int) -> int:
    """The fixed recursion's endogenous next multiplier."""
    candidate = max(2, last + 1)
    while gcd(candidate, modulus) != 1:
        candidate += 1
    return candidate


def arithmetic_deleted_branch(residue: int, modulus: int, multiplier: int) -> int:
    """Unique j with residue + j*modulus == 0 mod multiplier."""
    return (-residue * pow(modulus, -1, multiplier)) % multiplier


def fixed_deleted_branch(residue: int, modulus: int, multiplier: int) -> int:
    del residue, modulus, multiplier
    return 0


def cyclic_deleted_branch(residue: int, modulus: int, multiplier: int) -> int:
    del modulus
    return residue % multiplier


def random_deleted_branch_factory(seed: int) -> Callable[[int, int, int], int]:
    rng = Random(seed)

    def choose(residue: int, modulus: int, multiplier: int) -> int:
        del residue, modulus
        return rng.randrange(multiplier)

    return choose


def deletion_rule(control: Control, seed: int | None = None) -> Callable[[int, int, int], int]:
    if control == "arithmetic":
        return arithmetic_deleted_branch
    if control == "fixed_branch":
        return fixed_deleted_branch
    if control == "cyclic_branch":
        return cyclic_deleted_branch
    if control == "random_branch":
        if seed is None:
            raise ValueError("random_branch requires an explicit seed")
        return random_deleted_branch_factory(seed)
    raise ValueError(f"unknown control {control}")


def lift_level(
    parent_level: int,
    residues: Sequence[int],
    modulus: int,
    multiplier: int,
    control: Control = "arithmetic",
    seed: int | None = None,
) -> tuple[tuple[int, ...], list[Edge], dict[int, int]]:
    """Lift one level, deleting exactly one branch for each parent."""
    choose_deleted = deletion_rule(control, seed)
    children: list[int] = []
    edges: list[Edge] = []
    deletion_histogram = {branch: 0 for branch in range(multiplier)}
    for residue in residues:
        deleted = choose_deleted(residue, modulus, multiplier)
        if not 0 <= deleted < multiplier:
            raise AssertionError("deletion rule returned an invalid branch")
        deletion_histogram[deleted] += 1
        for branch in range(multiplier):
            if branch == deleted:
                continue
            child = residue + branch * modulus
            children.append(child)
            edges.append(
                Edge(
                    parent_level=parent_level,
                    parent_residue=residue,
                    child_level=parent_level + 1,
                    child_residue=child,
                    branch=branch,
                    multiplier=multiplier,
                )
            )
    children.sort()
    if len(children) != len(set(children)):
        raise AssertionError("lift representation must be unique")
    return tuple(children), edges, deletion_histogram


def intrinsic_wheels(max_level: int) -> tuple[list[WheelLevel], list[Edge], list[dict[int, int]]]:
    if max_level < 1:
        raise ValueError("max_level must be positive")
    levels = [WheelLevel(level=0, multiplier=1, modulus=1, residues=(0,))]
    edges: list[Edge] = []
    histograms: list[dict[int, int]] = []
    last = 1
    for level in range(1, max_level + 1):
        parent = levels[-1]
        multiplier = least_coprime_successor(last, parent.modulus)
        residues, new_edges, histogram = lift_level(
            parent.level, parent.residues, parent.modulus, multiplier, "arithmetic"
        )
        modulus = parent.modulus * multiplier
        levels.append(WheelLevel(level, multiplier, modulus, residues))
        edges.extend(new_edges)
        histograms.append(histogram)
        last = multiplier
    return levels, edges, histograms


def controlled_levels(
    baseline: Sequence[WheelLevel], control: Control, seed: int | None = None,
    preserve_through_level: int = 1,
) -> tuple[list[WheelLevel], list[Edge], list[dict[int, int]]]:
    """Use baseline multipliers but replace the arithmetic deletion rule.

    This keeps every level's modulus, parent out-degree, node count, and edge
    count exactly matched.  It deliberately does not claim to be a prime
    generator.
    """
    levels = [baseline[0]]
    edges: list[Edge] = []
    histograms: list[dict[int, int]] = []
    for target in baseline[1:]:
        parent = levels[-1]
        per_level_seed = None if seed is None else seed + target.level
        active_control: Control = "arithmetic" if target.level <= preserve_through_level else control
        residues, new_edges, histogram = lift_level(
            parent.level,
            parent.residues,
            parent.modulus,
            target.multiplier,
            active_control,
            per_level_seed,
        )
        levels.append(
            WheelLevel(target.level, target.multiplier, target.modulus, residues)
        )
        edges.extend(new_edges)
        histograms.append(histogram)
    return levels, edges, histograms


def wheel_units(modulus: int) -> tuple[int, ...]:
    if modulus == 1:
        return (0,)
    return tuple(value for value in range(modulus) if gcd(value, modulus) == 1)


def certify_levels(levels: Sequence[WheelLevel], edges: Sequence[Edge]) -> dict[str, object]:
    by_level = {level.level: level for level in levels}
    residue_sets = {level.level: set(level.residues) for level in levels}
    expected_edge_count = sum(
        len(levels[index - 1].residues) * (levels[index].multiplier - 1)
        for index in range(1, len(levels))
    )
    level_step_failures = 0
    missing_parent_failures = 0
    missing_child_failures = 0
    branch_formula_failures = 0
    for edge in edges:
        level_step_failures += edge.child_level != edge.parent_level + 1
        parent = by_level[edge.parent_level]
        child = by_level[edge.child_level]
        missing_parent_failures += edge.parent_residue not in residue_sets[edge.parent_level]
        missing_child_failures += edge.child_residue not in residue_sets[edge.child_level]
        branch_formula_failures += (
            edge.child_residue != edge.parent_residue + edge.branch * parent.modulus
        )

    # Independent Kahn certificate on node IDs.  The level-zero node and all
    # retained residues are included; every retained non-root node has one
    # incoming edge by unique mixed-radix lifting.
    nodes = [(level.level, residue) for level in levels for residue in level.residues]
    indegree = {node: 0 for node in nodes}
    adjacency: dict[tuple[int, int], list[tuple[int, int]]] = {node: [] for node in nodes}
    for edge in edges:
        parent = (edge.parent_level, edge.parent_residue)
        child = (edge.child_level, edge.child_residue)
        adjacency[parent].append(child)
        indegree[child] += 1
    queue = sorted(node for node, degree in indegree.items() if degree == 0)
    processed = 0
    while queue:
        node = queue.pop()
        processed += 1
        for child in adjacency[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)

    digest = sha256()
    for edge in edges:
        digest.update(edge.serialize().encode("ascii"))
    return {
        "node_count": len(nodes),
        "edge_count": len(edges),
        "expected_edge_count": expected_edge_count,
        "edge_count_exact": len(edges) == expected_edge_count,
        "level_step_failures": level_step_failures,
        "missing_parent_failures": missing_parent_failures,
        "missing_child_failures": missing_child_failures,
        "branch_formula_failures": branch_formula_failures,
        "kahn_processed_node_count": processed,
        "kahn_processed_all_nodes": processed == len(nodes),
        "directed_cycle_count": 0 if processed == len(nodes) else "at_least_one",
        "acyclicity_theorem": "every edge raises the integer level by exactly one",
        "canonical_edge_ledger_sha256": digest.hexdigest(),
    }


def compare_to_arithmetic_units(level: WheelLevel) -> dict[str, object]:
    exact = set(wheel_units(level.modulus))
    observed = set(level.residues)
    intersection = exact & observed
    union = exact | observed
    return {
        "true_unit_count": len(exact),
        "observed_count": len(observed),
        "unit_false_positive_count": len(observed - exact),
        "unit_false_negative_count": len(exact - observed),
        "unit_precision": len(intersection) / len(observed) if observed else 1.0,
        "unit_recall": len(intersection) / len(exact) if exact else 1.0,
        "unit_jaccard": len(intersection) / len(union) if union else 1.0,
    }


def deletion_histogram_chi_square(histogram: dict[int, int]) -> float:
    total = sum(histogram.values())
    expected = total / len(histogram)
    if expected == 0:
        return 0.0
    return sum((count - expected) ** 2 / expected for count in histogram.values())
