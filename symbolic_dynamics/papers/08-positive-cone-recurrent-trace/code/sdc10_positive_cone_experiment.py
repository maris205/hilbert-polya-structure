#!/usr/bin/env python3
"""SD-C10 recurrent positive-cone symbolic-transfer prototype.

The distinct-positive-free-generator model is the frozen universal
realization.  The positive-abelian control proves that the exact base
ledger is a positive-cone theorem, not a free-group-specific theorem.

All atom inventories are generated internally.  The experiment uses no
Riemann-zero data, target ordinates, zero fitting, or post-hoc scale.

Convention: matrix entries are indexed [target, source].  A directed edge
i -> j labelled g contributes c_ij lambda(g) to L[j,i].  Along a path the
group labels therefore compose by left multiplication.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import scipy.sparse as sparse
import sympy as sp


# ---------------------------------------------------------------------------
# Intrinsic inventories
# ---------------------------------------------------------------------------


def internal_multiplicative_atoms(count: int) -> list[int]:
    atoms: list[int] = []
    candidate = 2
    while len(atoms) < count:
        if not any(
            candidate % divisor == 0
            for divisor in range(2, math.isqrt(candidate) + 1)
        ):
            atoms.append(candidate)
        candidate += 1
    return atoms


# ---------------------------------------------------------------------------
# Exact group laws
# ---------------------------------------------------------------------------


class FreeGroup:
    name = "free_group"
    identity: tuple[int, ...] = ()

    @staticmethod
    def reduce(word: Iterable[int]) -> tuple[int, ...]:
        stack: list[int] = []
        for letter in word:
            if stack and stack[-1] == -letter:
                stack.pop()
            else:
                stack.append(int(letter))
        return tuple(stack)

    def mul(self, left, right):
        return self.reduce(tuple(left) + tuple(right))

    @staticmethod
    def inv(element):
        return tuple(-letter for letter in reversed(element))

    @staticmethod
    def show(element):
        return "e" if not element else " ".join(f"g{abs(q)}{'^-1' if q < 0 else ''}" for q in element)


class FreeAbelian:
    name = "free_abelian_Z"

    def __init__(self, rank: int):
        self.rank = rank
        self.identity = (0,) * rank

    def mul(self, left, right):
        return tuple(a + b for a, b in zip(left, right))

    @staticmethod
    def inv(element):
        return tuple(-value for value in element)

    @staticmethod
    def show(element):
        return str(tuple(element))


class CyclicGroup:
    name = "cyclic_group"

    def __init__(self, order: int):
        self.order = order
        self.identity = 0

    def mul(self, left, right):
        return (left + right) % self.order

    def inv(self, element):
        return (-element) % self.order

    @staticmethod
    def show(element):
        return str(element)


class SymmetricGroup3:
    name = "symmetric_group_S3"
    identity = (0, 1, 2)

    @staticmethod
    def mul(left, right):
        # Composition left after right.
        return tuple(left[right[index]] for index in range(3))

    @staticmethod
    def inv(element):
        answer = [0, 0, 0]
        for index, value in enumerate(element):
            answer[value] = index
        return tuple(answer)

    @staticmethod
    def show(element):
        return str(tuple(element))

    @staticmethod
    def elements():
        return list(itertools.permutations(range(3)))


# ---------------------------------------------------------------------------
# Labelled graphs and exact path trace
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Edge:
    source: int
    target: int
    label: Any
    coefficient: Any
    name: str
    cross: bool


def positive_chain_labels(size: int) -> dict[tuple[int, int], tuple[int, ...]]:
    labels = {}
    generator = 1
    for left in range(size - 1):
        labels[(left, left + 1)] = (generator,)
        generator += 1
        labels[(left + 1, left)] = (generator,)
        generator += 1
    return labels


def inverse_paired_labels(size: int) -> dict[tuple[int, int], tuple[int, ...]]:
    labels = {}
    for left in range(size - 1):
        generator = left + 1
        labels[(left, left + 1)] = (generator,)
        labels[(left + 1, left)] = (-generator,)
    return labels


def symbolic_chain_edges(size: int, labels: dict, group) -> tuple[list[Edge], tuple]:
    loop_variables = sp.symbols(f"x0:{size}", real=True)
    edges: list[Edge] = []
    for vertex in range(size):
        edges.append(
            Edge(vertex, vertex, group.identity, loop_variables[vertex], f"loop_{vertex}", False)
        )
    for source, target in sorted(labels):
        coefficient = sp.Symbol(f"y{source}{target}", real=True)
        edges.append(
            Edge(source, target, labels[(source, target)], coefficient, f"edge_{source}_{target}", True)
        )
    return edges, loop_variables


def constant_chain_edges(size: int, labels: dict, group) -> list[Edge]:
    edges = [Edge(i, i, group.identity, 1, f"loop_{i}", False) for i in range(size)]
    for source, target in sorted(labels):
        edges.append(Edge(source, target, labels[(source, target)], 1, f"edge_{source}_{target}", True))
    return edges


def adjacency(edges: list[Edge], state_count: int) -> list[list[Edge]]:
    answer: list[list[Edge]] = [[] for _ in range(state_count)]
    for edge in edges:
        answer[edge.source].append(edge)
    return answer


def closed_path_trace(edges: list[Edge], state_count: int, length: int, group) -> dict:
    outgoing = adjacency(edges, state_count)
    identity_sum: Any = 0
    closed_count = identity_count = mixed_closed_count = mixed_identity_count = 0
    reduced_words = set()
    identity_examples = []
    mixed_identity_examples = []

    for start in range(state_count):
        stack = [(start, 0, group.identity, sp.Integer(1), False, [], [start])]
        while stack:
            current, depth, word, coefficient, used_cross, names, states = stack.pop()
            if depth == length:
                if current != start:
                    continue
                closed_count += 1
                mixed_closed_count += int(used_cross)
                reduced_words.add(group.show(word))
                if word == group.identity:
                    identity_count += 1
                    mixed_identity_count += int(used_cross)
                    identity_sum += coefficient
                    example = {
                        "start": start,
                        "edge_names": names,
                        "states": states,
                        "coefficient": str(coefficient),
                    }
                    if len(identity_examples) < 16:
                        identity_examples.append(example)
                    if used_cross and len(mixed_identity_examples) < 16:
                        mixed_identity_examples.append(example)
                continue
            for edge in outgoing[current]:
                stack.append(
                    (
                        edge.target,
                        depth + 1,
                        group.mul(edge.label, word),
                        coefficient * edge.coefficient,
                        used_cross or edge.cross,
                        names + [edge.name],
                        states + [edge.target],
                    )
                )
    return {
        "length": length,
        "closed_path_count": closed_count,
        "mixed_closed_path_count": mixed_closed_count,
        "tau_surviving_path_count": identity_count,
        "tau_surviving_mixed_path_count": mixed_identity_count,
        "distinct_closed_reduced_words": len(reduced_words),
        "tau_trace": str(sp.factor(identity_sum)),
        "tau_trace_expanded": str(sp.expand(identity_sum)),
        "identity_examples": identity_examples,
        "mixed_identity_examples": mixed_identity_examples,
    }


def chiral_edges(base_edges: list[Edge], atom_count: int, group) -> list[Edge]:
    """Edges of B=[[0,L],[L*,0]] on top+bottom atom states."""
    answer = []
    for edge in base_edges:
        # bottom(source) -> top(target), the L block
        answer.append(
            Edge(
                atom_count + edge.source,
                edge.target,
                edge.label,
                edge.coefficient,
                f"L:{edge.name}",
                edge.cross,
            )
        )
        # top(target) -> bottom(source), the adjoint block
        coefficient = sp.conjugate(edge.coefficient)
        answer.append(
            Edge(
                edge.target,
                atom_count + edge.source,
                group.inv(edge.label),
                coefficient,
                f"L*:{edge.name}",
                edge.cross,
            )
        )
    return answer


def exact_candidate_audit(atom_count: int = 3, base_cutoff: int = 10, chiral_cutoff: int = 6) -> dict:
    group = FreeGroup()
    labels = positive_chain_labels(atom_count)
    edges, loops = symbolic_chain_edges(atom_count, labels, group)
    symbol_locals = {
        str(symbol): symbol
        for edge in edges
        for symbol in sp.sympify(edge.coefficient).free_symbols
    }
    base_rows = []
    for length in range(1, base_cutoff + 1):
        row = closed_path_trace(edges, atom_count, length, group)
        target = sum(variable**length for variable in loops)
        row["target"] = str(target)
        row["trace_exact"] = bool(
            sp.expand(
                sp.sympify(row["tau_trace_expanded"], locals=symbol_locals) - target
            )
            == 0
        )
        base_rows.append(row)

    block_edges = chiral_edges(edges, atom_count, group)
    chiral_rows = []
    first_mixed_identity = None
    for length in range(1, chiral_cutoff + 1):
        row = closed_path_trace(block_edges, 2 * atom_count, length, group)
        loop_baseline = sp.Integer(0) if length % 2 else 2 * sum(q**length for q in loops)
        expression = sp.sympify(row["tau_trace_expanded"], locals=symbol_locals)
        row["loop_only_baseline"] = str(loop_baseline)
        row["mixed_identity_extra"] = str(sp.factor(expression - loop_baseline))
        if row["tau_surviving_mixed_path_count"] and first_mixed_identity is None:
            first_mixed_identity = {
                "length": length,
                "mixed_identity_extra": row["mixed_identity_extra"],
                "examples": row["mixed_identity_examples"],
            }
        chiral_rows.append(row)

    z = sp.Symbol("z")
    log_series_target = -sum(
        z**length * sum(variable**length for variable in loops) / length
        for length in range(1, base_cutoff + 1)
    )
    product_log_series = sp.series(
        sum(sp.log(1 - z * variable) for variable in loops), z, 0, base_cutoff + 1
    ).removeO()
    return {
        "group": "free group on one generator per directed cross edge",
        "atom_count": atom_count,
        "cross_generator_count": len(labels),
        "base_cutoff": base_cutoff,
        "chiral_cutoff": chiral_cutoff,
        "base_rows": base_rows,
        "all_base_traces_exact": all(row["trace_exact"] for row in base_rows),
        "all_mixed_closed_paths_tau_killed": all(
            row["tau_surviving_mixed_path_count"] == 0 for row in base_rows
        ),
        "formal_tau_determinant": {
            "definition": "D_tau(z)=exp(-sum_(r>=1) z^r (Tr tensor tau)(L^r)/r)",
            "target": "product_i(1-z*x_i)",
            "series_cutoff": base_cutoff,
            "log_series_exact": bool(sp.expand(log_series_target - product_log_series) == 0),
            "scope": (
                "formal scalar identity; at z=1 the scalar trace series is "
                "absolutely convergent for Re(s)>1; an operator-analytic "
                "determinant reading requires a selected small-norm/invertible "
                "logarithm branch"
            ),
        },
        "chiral_rows": chiral_rows,
        "first_mixed_identity_contribution": first_mixed_identity,
    }


# ---------------------------------------------------------------------------
# Group-label controls
# ---------------------------------------------------------------------------


def first_mixed_identity(edges, state_count, group, cutoff):
    rows = []
    first = None
    for length in range(1, cutoff + 1):
        row = closed_path_trace(edges, state_count, length, group)
        compact = {
            key: row[key]
            for key in [
                "length",
                "closed_path_count",
                "mixed_closed_path_count",
                "tau_surviving_path_count",
                "tau_surviving_mixed_path_count",
                "tau_trace",
            ]
        }
        rows.append(compact)
        if first is None and row["tau_surviving_mixed_path_count"]:
            first = {
                "length": length,
                "mixed_count": row["tau_surviving_mixed_path_count"],
                "examples": row["mixed_identity_examples"],
            }
    return rows, first


def label_controls(atom_count: int = 3, cutoff: int = 12, seed_count: int = 32) -> dict:
    free = FreeGroup()
    candidate_edges = constant_chain_edges(atom_count, positive_chain_labels(atom_count), free)
    candidate_rows, candidate_first = first_mixed_identity(candidate_edges, atom_count, free, cutoff)

    inverse_edges = constant_chain_edges(atom_count, inverse_paired_labels(atom_count), free)
    inverse_rows, inverse_first = first_mixed_identity(inverse_edges, atom_count, free, cutoff)

    abelian = FreeAbelian(1)
    abelian_labels = {
        key: (1,) for key in positive_chain_labels(atom_count)
    }
    abelian_edges = constant_chain_edges(atom_count, abelian_labels, abelian)
    abelian_rows, abelian_first = first_mixed_identity(abelian_edges, atom_count, abelian, cutoff)

    cyclic = CyclicGroup(5)
    cyclic_labels = {key: 1 for key in positive_chain_labels(atom_count)}
    cyclic_edges = constant_chain_edges(atom_count, cyclic_labels, cyclic)
    cyclic_rows, cyclic_first = first_mixed_identity(cyclic_edges, atom_count, cyclic, cutoff)

    s3 = SymmetricGroup3()
    # Four distinct nonidentity elements, assigned without an inverse pair on
    # either undirected edge.  Finite relations still create a later identity.
    s3_values = [(1, 0, 2), (0, 2, 1), (2, 1, 0), (1, 2, 0)]
    s3_labels = {
        key: value
        for key, value in zip(sorted(positive_chain_labels(atom_count)), s3_values)
    }
    s3_edges = constant_chain_edges(atom_count, s3_labels, s3)
    s3_rows, s3_first = first_mixed_identity(s3_edges, atom_count, s3, cutoff)

    random_rows = []
    for seed in range(seed_count):
        rng = np.random.default_rng(seed)
        random_labels = {
            key: (int(rng.integers(1, 4)),)
            for key in positive_chain_labels(atom_count)
        }
        edges = constant_chain_edges(atom_count, random_labels, free)
        _, first = first_mixed_identity(edges, atom_count, free, cutoff=8)
        random_rows.append(
            {
                "seed": seed,
                "labels": {f"{a}->{b}": value[0] for (a, b), value in random_labels.items()},
                "first_mixed_identity": first,
                "passes_through_r8": first is None,
            }
        )

    return {
        "candidate_distinct_positive_free_labels": {
            "rows": candidate_rows,
            "first_mixed_identity": candidate_first,
        },
        "inverse_paired_free_labels": {
            "rows": inverse_rows,
            "first_mixed_identity": inverse_first,
        },
        "positive_free_abelian_Z_labels": {
            "rows": abelian_rows,
            "first_mixed_identity": abelian_first,
            "verdict": "PROVED CONCLUSION: free-group specificity is refuted; the base theorem uses only a conical/positive monoid cocycle",
        },
        "finite_cyclic_C5_labels": {
            "rows": cyclic_rows,
            "first_mixed_identity": cyclic_first,
            "why_first_at_10": "C5 requires cross-edge count divisible by 5, while a closed walk in the bidirectional chain has even cross-edge count; min positive count is lcm(5,2)=10",
        },
        "finite_nonabelian_S3_labels": {
            "assignment": {
                f"{a}->{b}": s3.show(value) for (a, b), value in s3_labels.items()
            },
            "rows": s3_rows,
            "first_mixed_identity": s3_first,
            "why_first_at_4": "on edge pair 1<->2, the two-step label composite is a transposition of order 2; its square is an admissible four-cross-edge closed path, while no paired two-step product is identity",
        },
        "random_positive_free_labels": {
            "seed_count": seed_count,
            "pass_count": sum(row["passes_through_r8"] for row in random_rows),
            "rows": random_rows,
            "verdict": "PROVES_TOO_MUCH if exact ledger alone is treated as selective",
        },
    }


def exact_atom_cutoff_audit(maximum_length: int = 8) -> dict:
    """Word-level cutoff audit without symbolic coefficients."""
    group = FreeGroup()
    rows = []
    for atom_count in [2, 3, 4]:
        edges = constant_chain_edges(
            atom_count, positive_chain_labels(atom_count), group
        )
        for length in range(1, maximum_length + 1):
            row = closed_path_trace(edges, atom_count, length, group)
            rows.append(
                {
                    "atom_count": atom_count,
                    "generator_rank": 2 * (atom_count - 1),
                    "length": length,
                    "closed_path_count": row["closed_path_count"],
                    "mixed_closed_path_count": row["mixed_closed_path_count"],
                    "tau_surviving_path_count": row["tau_surviving_path_count"],
                    "tau_surviving_mixed_path_count": row[
                        "tau_surviving_mixed_path_count"
                    ],
                    "passes": row["tau_surviving_path_count"] == atom_count
                    and row["tau_surviving_mixed_path_count"] == 0,
                }
            )
    return {
        "maximum_length": maximum_length,
        "rows": rows,
        "all_pass": all(row["passes"] for row in rows),
    }


# ---------------------------------------------------------------------------
# Numeric tau moments and endpoint/cutoff controls
# ---------------------------------------------------------------------------


def numeric_chain_edges(masses, height, alpha, labels, group) -> list[Edge]:
    masses = np.asarray(masses, dtype=float)
    diagonal = np.exp(-(0.5 + 1j * height) * np.log(masses))
    edges = [
        Edge(i, i, group.identity, diagonal[i], f"loop_{i}", False)
        for i in range(len(masses))
    ]
    for source, target in sorted(labels):
        coefficient = alpha * diagonal[source] + (1.0 - alpha) * diagonal[target]
        edges.append(
            Edge(source, target, labels[(source, target)], coefficient, f"edge_{source}_{target}", True)
        )
    return edges


def numeric_chiral_edges(base_edges, atom_count, group) -> list[Edge]:
    answer = []
    for edge in base_edges:
        answer.append(
            Edge(atom_count + edge.source, edge.target, edge.label, edge.coefficient, f"L:{edge.name}", edge.cross)
        )
        answer.append(
            Edge(edge.target, atom_count + edge.source, group.inv(edge.label), np.conjugate(edge.coefficient), f"L*:{edge.name}", edge.cross)
        )
    return answer


def numeric_tau_trace(edges, state_count, length, group) -> complex:
    outgoing = adjacency(edges, state_count)
    answer = 0.0j
    for start in range(state_count):
        stack = [(start, 0, group.identity, 1.0 + 0.0j)]
        while stack:
            current, depth, word, coefficient = stack.pop()
            if depth == length:
                if current == start and word == group.identity:
                    answer += coefficient
                continue
            for edge in outgoing[current]:
                stack.append(
                    (
                        edge.target,
                        depth + 1,
                        group.mul(edge.label, word),
                        coefficient * edge.coefficient,
                    )
                )
    return answer


def endpoint_alpha_sweep() -> dict:
    group = FreeGroup()
    masses = internal_multiplicative_atoms(3)
    labels = positive_chain_labels(3)
    heights = np.linspace(0.0, 40.0, 401)
    rows = []
    for alpha in [0.0, 0.125, 0.25, 0.5, 0.75, 0.875, 1.0]:
        moment2, moment4 = [], []
        for height in heights:
            base = numeric_chain_edges(masses, float(height), alpha, labels, group)
            block = numeric_chiral_edges(base, len(masses), group)
            moment2.append(float(numeric_tau_trace(block, 2 * len(masses), 2, group).real))
            moment4.append(float(numeric_tau_trace(block, 2 * len(masses), 4, group).real))
        rows.append(
            {
                "alpha": alpha,
                "tau_trace_B2_min": min(moment2),
                "tau_trace_B2_max": max(moment2),
                "tau_trace_B2_range": max(moment2) - min(moment2),
                "tau_trace_B4_min": min(moment4),
                "tau_trace_B4_max": max(moment4),
                "tau_trace_B4_range": max(moment4) - min(moment4),
                "motion": max(moment4) - min(moment4) > 1e-10,
            }
        )
    return {
        "masses": masses,
        "height_grid": {"start": 0.0, "stop": 40.0, "points": len(heights)},
        "rows": rows,
        "endpoint_identities": {
            "alpha_0_target": "L_(0,t)=U_t L_(0,0)",
            "alpha_1_source": "L_(1,t)=L_(1,0) U_t",
        },
    }


def atom_cutoff_sweep() -> dict:
    group = FreeGroup()
    heights = np.linspace(0.0, 40.0, 161)
    rows = []
    for atom_count in [2, 3, 4, 8, 16, 32]:
        masses = internal_multiplicative_atoms(atom_count)
        labels = positive_chain_labels(atom_count)
        moment2, moment4 = [], []
        for height in heights:
            base = numeric_chain_edges(masses, float(height), 0.5, labels, group)
            block = numeric_chiral_edges(base, atom_count, group)
            moment2.append(float(numeric_tau_trace(block, 2 * atom_count, 2, group).real))
            moment4.append(float(numeric_tau_trace(block, 2 * atom_count, 4, group).real))
        rows.append(
            {
                "atom_count": atom_count,
                "last_atom": masses[-1],
                "generator_rank": 2 * (atom_count - 1),
                "tau_trace_B2_range": max(moment2) - min(moment2),
                "tau_trace_B4_range": max(moment4) - min(moment4),
                "strict_motion": max(moment4) - min(moment4) > 1e-10,
            }
        )
    return {
        "height_grid": {"start": 0.0, "stop": 40.0, "points": len(heights)},
        "rows": rows,
    }


def inventory_controls(seed: int = 2808) -> dict:
    rng = np.random.default_rng(seed)
    base = internal_multiplicative_atoms(8)
    inventories = {
        "entropy_ordered_atoms": base,
        "shuffled_same_atoms": list(map(int, np.asarray(base)[rng.permutation(8)])),
        "composites_only": [4, 6, 8, 9, 10, 12, 14, 15],
        "matched_count_random_integers": sorted(
            map(int, rng.choice(np.arange(2, 100), size=8, replace=False))
        ),
    }
    group = FreeGroup()
    labels = positive_chain_labels(8)
    heights = np.linspace(0.0, 40.0, 201)
    rows = []
    for name, masses in inventories.items():
        moment4 = []
        for height in heights:
            base_edges = numeric_chain_edges(masses, float(height), 0.5, labels, group)
            block = numeric_chiral_edges(base_edges, 8, group)
            moment4.append(float(numeric_tau_trace(block, 16, 4, group).real))
        rows.append(
            {
                "inventory": name,
                "masses": masses,
                "base_tau_ledger_exact_by_positive_cone": True,
                "tau_trace_B4_range": max(moment4) - min(moment4),
                "strict_motion": max(moment4) - min(moment4) > 1e-10,
                "a0_status": "intrinsic tensor source" if name == "entropy_ordered_atoms" else "control; not the source-locked inventory",
            }
        )
    return {
        "seed": seed,
        "rows": rows,
        "verdict": "PROVES_TOO_MUCH for ledger-plus-motion without the independent tensor-source gate",
    }


# ---------------------------------------------------------------------------
# Finite regular and word-ball approximants
# ---------------------------------------------------------------------------


def free_group_ball(rank: int, radius: int) -> list[tuple[int, ...]]:
    ball = [tuple()]
    frontier = [tuple()]
    letters = list(range(1, rank + 1)) + list(range(-1, -rank - 1, -1))
    for _ in range(radius):
        following = []
        for word in frontier:
            for letter in letters:
                if word and word[-1] == -letter:
                    continue
                following.append(word + (letter,))
        ball.extend(following)
        frontier = following
    return ball


def compressed_left_regular(rank: int, radius: int):
    group = FreeGroup()
    basis = free_group_ball(rank, radius)
    index = {word: position for position, word in enumerate(basis)}
    matrices = {}
    for letter in list(range(1, rank + 1)) + list(range(-1, -rank - 1, -1)):
        rows, columns = [], []
        for column, word in enumerate(basis):
            target = group.reduce((letter,) + word)
            if target in index:
                rows.append(index[target])
                columns.append(column)
        matrices[letter] = sparse.csr_matrix(
            (np.ones(len(rows)), (rows, columns)), shape=(len(basis), len(basis)), dtype=complex
        )
    return basis, matrices


def word_ball_transfer(masses, height, alpha, radius):
    atom_count = len(masses)
    rank = 2 * (atom_count - 1)
    basis, regular = compressed_left_regular(rank, radius)
    identity = sparse.identity(len(basis), dtype=complex, format="csr")
    diagonal = np.exp(-(0.5 + 1j * height) * np.log(np.asarray(masses, dtype=float)))
    labels = positive_chain_labels(atom_count)
    blocks = [[None for _ in range(atom_count)] for _ in range(atom_count)]
    for vertex in range(atom_count):
        blocks[vertex][vertex] = diagonal[vertex] * identity
    for source, target in sorted(labels):
        generator = labels[(source, target)][0]
        coefficient = alpha * diagonal[source] + (1.0 - alpha) * diagonal[target]
        blocks[target][source] = coefficient * regular[generator]
    return sparse.bmat(blocks, format="csr"), basis


def weighted_quantiles(values, weights, quantiles=(0.1, 0.5, 0.9)):
    order = np.argsort(values)
    sorted_values = np.asarray(values)[order]
    sorted_weights = np.asarray(weights)[order]
    cumulative = np.cumsum(sorted_weights)
    cumulative /= cumulative[-1]
    return [float(sorted_values[np.searchsorted(cumulative, q)]) for q in quantiles]


def word_ball_row(atom_count: int, radius: int, height: float, alpha: float, z_probe: complex):
    masses = internal_multiplicative_atoms(atom_count)
    transfer_sparse, basis = word_ball_transfer(masses, height, alpha, radius)
    transfer = transfer_sparse.toarray()
    group_dimension = len(basis)
    total_dimension = transfer.shape[0]
    identity_index = basis.index(tuple())
    root_indices = [vertex * group_dimension + identity_index for vertex in range(atom_count)]

    singular_values = np.linalg.svd(transfer, compute_uv=False)
    gram = transfer.conj().T @ transfer
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    eigenvalues = np.maximum(eigenvalues.real, 0.0)
    root_weights = np.sum(np.abs(eigenvectors[root_indices, :]) ** 2, axis=0)
    root_probability = root_weights / atom_count

    shifted = np.eye(total_dimension, dtype=complex) - z_probe * transfer
    shifted_gram = shifted.conj().T @ shifted
    shifted_eigenvalues, shifted_eigenvectors = np.linalg.eigh(shifted_gram)
    shifted_eigenvalues = np.maximum(shifted_eigenvalues.real, 0.0)
    shifted_root_weights = np.sum(
        np.abs(shifted_eigenvectors[root_indices, :]) ** 2, axis=0
    )
    epsilon = 1e-8
    rooted_fk_log = 0.5 * float(
        np.sum(shifted_root_weights * np.log(shifted_eigenvalues + epsilon**2)).real
    )
    sign, finite_logabsdet = np.linalg.slogdet(shifted)
    normalized_finite_logabsdet = float(finite_logabsdet / group_dimension)
    diagonal = np.exp(-(0.5 + 1j * height) * np.log(np.asarray(masses, dtype=float)))
    euler_logabs = float(np.sum(np.log(np.abs(1.0 - z_probe * diagonal))))

    ordinary_eigenvalues = np.linalg.eigvals(transfer)
    distance_to_loop_spectrum = [
        min(abs(value - loop_value) for loop_value in diagonal)
        for value in ordinary_eigenvalues
    ]
    return {
        "atom_count": atom_count,
        "free_rank": 2 * (atom_count - 1),
        "radius": radius,
        "group_ball_dimension": group_dimension,
        "operator_dimension": total_dimension,
        "height": height,
        "alpha": alpha,
        "singular_min": float(singular_values.min()),
        "singular_q10": float(np.quantile(singular_values, 0.1)),
        "singular_median": float(np.median(singular_values)),
        "singular_q90": float(np.quantile(singular_values, 0.9)),
        "singular_max": float(singular_values.max()),
        "root_singular_q10_q50_q90": weighted_quantiles(
            np.sqrt(eigenvalues), root_probability
        ),
        "empirical_tau_gram": float(np.trace(gram).real / group_dimension),
        "root_tau_gram": float(np.trace(gram[np.ix_(root_indices, root_indices)]).real),
        "ordinary_eigen_max_distance_from_loop_values": float(max(distance_to_loop_spectrum)),
        "z_probe": [float(z_probe.real), float(z_probe.imag)],
        "finite_section_logabsdet_per_group_dim": normalized_finite_logabsdet,
        "euler_loop_logabs": euler_logabs,
        "finite_logabsdet_error_vs_euler": normalized_finite_logabsdet - euler_logabs,
        "rooted_regularized_fk_log_proxy": rooted_fk_log,
        "rooted_fk_minus_euler": rooted_fk_log - euler_logabs,
        "fk_epsilon": epsilon,
        "warning": "finite-ball normalized determinant is a non-Folner finite-section proxy; rooted hermitization is a separate local proxy",
    }


def word_ball_experiments() -> dict:
    rows = []
    z_probes = [0.25 + 0.0j, 1.0 + 0.0j]
    # Distribution/motion sweep on the smallest recurrent two-atom graph.
    for radius in [1, 2, 3, 4]:
        for height in [0.0, 3.0, 9.0]:
            for alpha in [0.0, 0.5, 1.0]:
                for z_probe in z_probes:
                    rows.append(word_ball_row(2, radius, height, alpha, z_probe))
    # Atom/rank cutoff probes at modest radii.
    for atom_count, radius in [(3, 1), (3, 2), (4, 1), (4, 2)]:
        for height in [0.0, 9.0]:
            for z_probe in z_probes:
                rows.append(word_ball_row(atom_count, radius, height, 0.5, z_probe))
    return {
        "rows": rows,
        "nonamenability_warning": (
            "free-group balls are not a Folner sequence; normalized finite-section spectra/determinants "
            "are not certified limits of the group von Neumann algebra"
        ),
        "brown_measure_boundary": (
            "ordinary finite-section eigenvalues collapse to loop diagonal values because the compressed "
            "positive skew graph is acyclic; they are not accepted as Brown-measure approximants. "
            "Rooted regularized hermitization and singular quantiles are reported instead."
        ),
    }


def finite_regular_s3_audit() -> dict:
    group = SymmetricGroup3()
    elements = group.elements()
    index = {element: position for position, element in enumerate(elements)}
    matrices = {}
    for label in elements:
        matrix = np.zeros((6, 6))
        for column, element in enumerate(elements):
            target = group.mul(label, element)
            matrix[index[target], column] = 1.0
        matrices[label] = matrix

    labels_values = [(1, 0, 2), (0, 2, 1), (2, 1, 0), (1, 2, 0)]
    labels = {
        key: value
        for key, value in zip(sorted(positive_chain_labels(3)), labels_values)
    }
    blocks = [[np.zeros((6, 6)) for _ in range(3)] for _ in range(3)]
    for vertex in range(3):
        blocks[vertex][vertex] = np.eye(6)
    for (source, target), label in labels.items():
        blocks[target][source] = matrices[label]
    transfer = np.block(blocks)
    edges = constant_chain_edges(3, labels, group)
    rows = []
    power = np.eye(18)
    for length in range(1, 13):
        power = power @ transfer
        normalized_regular_trace = float(np.trace(power) / 6.0)
        exact = closed_path_trace(edges, 3, length, group)
        exact_value = float(sp.N(sp.sympify(exact["tau_trace"])))
        rows.append(
            {
                "length": length,
                "normalized_regular_trace": normalized_regular_trace,
                "exact_group_tau_trace": exact_value,
                "residual": normalized_regular_trace - exact_value,
                "mixed_identity_count": exact["tau_surviving_mixed_path_count"],
            }
        )
    return {
        "group": "S3",
        "regular_dimension": 6,
        "matrix_dimension": 18,
        "rows": rows,
        "max_trace_residual": max(abs(row["residual"]) for row in rows),
    }


# ---------------------------------------------------------------------------
# Output tables
# ---------------------------------------------------------------------------


def write_csv(path: Path, rows: list[dict]):
    if not rows:
        return
    keys = []
    for row in rows:
        for key in row:
            if key not in keys:
                keys.append(key)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=keys, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: json.dumps(value, sort_keys=True)
                    if isinstance(value, (dict, list))
                    else value
                    for key, value in row.items()
                }
            )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
    )
    arguments = parser.parse_args()
    arguments.output_dir.mkdir(parents=True, exist_ok=True)

    exact = exact_candidate_audit()
    labels = label_controls()
    exact_cutoffs = exact_atom_cutoff_audit()
    alpha = endpoint_alpha_sweep()
    cutoffs = atom_cutoff_sweep()
    inventories = inventory_controls()
    word_ball = word_ball_experiments()
    finite_regular = finite_regular_s3_audit()
    results = {
        "metadata": {
            "candidate_id": "SD-C10",
            "candidate": "finite recurrent prime-atom graph with a positive-cone cocycle; distinct positive free generators are the frozen universal realization",
            "primary_family": "symbolic dynamics",
            "atom_generation": "multiplicative indecomposables ordered by entropy",
            "uses_riemann_zero_data": False,
            "fits_target_zeros": False,
            "base_trace_cutoff": exact["base_cutoff"],
            "chiral_trace_cutoff": exact["chiral_cutoff"],
        },
        "exact_candidate": exact,
        "label_controls": labels,
        "exact_atom_cutoff_audit": exact_cutoffs,
        "endpoint_alpha_sweep": alpha,
        "atom_cutoff_sweep": cutoffs,
        "inventory_controls": inventories,
        "finite_regular_S3": finite_regular,
        "word_ball_approximants": word_ball,
        "claim_boundary": {
            "exact_base_tau_ledger": "PROVED at all orders by positive-word argument; enumerated through r=10",
            "first_chiral_backtracking": "PROVED at r=2",
            "free_group_specificity": "REFUTED by positive free-abelian control",
            "actual_base_mechanism": "PROVED: a cocycle into any conical/positive monoid P with identity excluded from nonempty products kills every mixed base word",
            "finite_group_all_order_ledger": "REFUTED by group relations",
            "fk_global_determinant": "OPEN; only local trace-log identity and uncontrolled finite/rooted proxies",
            "brown_measure": "NOT_ESTABLISHED",
            "rh_or_target_zero_claim": "FORBIDDEN / NOT MADE",
        },
    }

    output = arguments.output_dir / "summary.json"
    output.write_text(json.dumps(results, indent=2, sort_keys=True, default=str) + "\n")
    write_csv(arguments.output_dir / "exact_base_trace.csv", exact["base_rows"])
    write_csv(arguments.output_dir / "exact_chiral_trace.csv", exact["chiral_rows"])
    write_csv(arguments.output_dir / "exact_atom_cutoffs.csv", exact_cutoffs["rows"])
    write_csv(arguments.output_dir / "alpha_motion.csv", alpha["rows"])
    write_csv(arguments.output_dir / "atom_cutoffs.csv", cutoffs["rows"])
    write_csv(arguments.output_dir / "inventories.csv", inventories["rows"])
    write_csv(arguments.output_dir / "word_ball.csv", word_ball["rows"])
    write_csv(arguments.output_dir / "finite_regular_s3.csv", finite_regular["rows"])
    print(
        json.dumps(
            {
                "output": str(output),
                "base_exact": exact["all_base_traces_exact"],
                "mixed_killed": exact["all_mixed_closed_paths_tau_killed"],
                "first_chiral_mixed_identity": exact["first_mixed_identity_contribution"]["length"],
                "no_zero_data": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
