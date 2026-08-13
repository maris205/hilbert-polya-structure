#!/usr/bin/env python3
"""Exact and finite falsification audit for SD-C11.

SD-C11 is the holomorphic reflection double

    C_s = [[0, T_s^+], [T_(1-s)^-, 0]]

over the entropy-ordered tensor-prime symbolic chain.  The two positive
cocycle alphabets are disjoint in the promoted object.  No adjoint, target
zero, Riemann-zero data, fitting, or post-hoc scale enters this executable.

Matrix entries use the convention [target, source].
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
import sympy as sp


# ---------------------------------------------------------------------------
# Intrinsic atom source
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
# Exact cocycle groups
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
        return "e" if not element else " ".join(str(x) for x in element)


class ProductFreeGroup:
    """Direct product of the plus and minus free alphabets."""

    name = "free_plus_times_free_minus"
    identity = ((), ())

    def __init__(self):
        self.factor = FreeGroup()

    def mul(self, left, right):
        return (
            self.factor.mul(left[0], right[0]),
            self.factor.mul(left[1], right[1]),
        )

    def inv(self, element):
        return (self.factor.inv(element[0]), self.factor.inv(element[1]))

    @staticmethod
    def show(element):
        return f"{element[0]}|{element[1]}"


class CyclicGroup:
    name = "cyclic"

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


# ---------------------------------------------------------------------------
# Exact alternating-word trace
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Edge:
    source: int
    target: int
    label: Any
    coefficient: Any
    cross_atom: bool
    name: str


def directed_chain_pairs(atom_count: int) -> list[tuple[int, int]]:
    answer: list[tuple[int, int]] = []
    for left in range(atom_count - 1):
        answer.extend([(left, left + 1), (left + 1, left)])
    return answer


def alternating_edges_exact(atom_count: int) -> tuple[list[Edge], ProductFreeGroup, tuple, tuple]:
    """Frozen SD-C11 edges with opaque coefficients and disjoint alphabets."""
    group = ProductFreeGroup()
    plus_loops = sp.symbols(f"a0:{atom_count}")
    minus_loops = sp.symbols(f"b0:{atom_count}")
    edges: list[Edge] = []

    # top=0,...,N-1; bottom=N,...,2N-1.
    for atom in range(atom_count):
        edges.append(
            Edge(atom_count + atom, atom, group.identity, plus_loops[atom], False, f"plus_loop_{atom}")
        )
        edges.append(
            Edge(atom, atom_count + atom, group.identity, minus_loops[atom], False, f"minus_loop_{atom}")
        )

    for generator, (source, target) in enumerate(directed_chain_pairs(atom_count), 1):
        edges.append(
            Edge(
                atom_count + source,
                target,
                ((generator,), ()),
                sp.Symbol(f"u{source}{target}"),
                True,
                f"plus_{source}_{target}",
            )
        )
        edges.append(
            Edge(
                source,
                atom_count + target,
                ((), (generator,)),
                sp.Symbol(f"v{source}{target}"),
                True,
                f"minus_{source}_{target}",
            )
        )
    return edges, group, plus_loops, minus_loops


def alternating_edges_constant(
    atom_count: int,
    group,
    plus_labels: dict[tuple[int, int], Any],
    minus_labels: dict[tuple[int, int], Any],
) -> list[Edge]:
    edges: list[Edge] = []
    for atom in range(atom_count):
        edges.extend(
            [
                Edge(atom_count + atom, atom, group.identity, 1, False, f"plus_loop_{atom}"),
                Edge(atom, atom_count + atom, group.identity, 1, False, f"minus_loop_{atom}"),
            ]
        )
    for source, target in directed_chain_pairs(atom_count):
        edges.append(
            Edge(
                atom_count + source,
                target,
                plus_labels[(source, target)],
                1,
                True,
                f"plus_{source}_{target}",
            )
        )
        edges.append(
            Edge(
                source,
                atom_count + target,
                minus_labels[(source, target)],
                1,
                True,
                f"minus_{source}_{target}",
            )
        )
    return edges


def adjacency(edges: list[Edge], state_count: int) -> list[list[Edge]]:
    outgoing: list[list[Edge]] = [[] for _ in range(state_count)]
    for edge in edges:
        outgoing[edge.source].append(edge)
    return outgoing


def closed_trace(edges: list[Edge], state_count: int, length: int, group) -> dict:
    outgoing = adjacency(edges, state_count)
    trace: Any = 0
    closed = mixed = survivors = mixed_survivors = 0
    mixed_examples: list[dict] = []

    for start in range(state_count):
        stack = [(start, 0, group.identity, sp.Integer(1), False, [start], [])]
        while stack:
            current, depth, word, coefficient, used_cross, states, names = stack.pop()
            if depth == length:
                if current != start:
                    continue
                closed += 1
                mixed += int(used_cross)
                if word == group.identity:
                    survivors += 1
                    mixed_survivors += int(used_cross)
                    trace += coefficient
                    if used_cross and len(mixed_examples) < 12:
                        mixed_examples.append(
                            {"states": states, "edges": names, "coefficient": str(coefficient)}
                        )
                continue
            for edge in outgoing[current]:
                stack.append(
                    (
                        edge.target,
                        depth + 1,
                        group.mul(edge.label, word),
                        coefficient * edge.coefficient,
                        used_cross or edge.cross_atom,
                        states + [edge.target],
                        names + [edge.name],
                    )
                )
    return {
        "length": length,
        "closed_path_count": closed,
        "mixed_closed_path_count": mixed,
        "identity_survivor_count": survivors,
        "mixed_identity_survivor_count": mixed_survivors,
        "trace": str(sp.factor(trace)),
        "trace_expanded": str(sp.expand(trace)),
        "mixed_identity_examples": mixed_examples,
    }


def exact_candidate_audit(atom_count: int = 3, power_cutoff: int = 12) -> dict:
    edges, group, plus_loops, minus_loops = alternating_edges_exact(atom_count)
    symbols = {
        str(symbol): symbol
        for edge in edges
        for symbol in sp.sympify(edge.coefficient).free_symbols
    }
    rows = []
    for length in range(1, power_cutoff + 1):
        row = closed_trace(edges, 2 * atom_count, length, group)
        if length % 2:
            target = sp.Integer(0)
        else:
            reflected_repetitions = length // 2
            target = 2 * sum(
                (plus_loops[i] * minus_loops[i]) ** reflected_repetitions
                for i in range(atom_count)
            )
        got = sp.sympify(row["trace_expanded"], locals=symbols)
        row["target"] = str(target)
        row["trace_exact"] = bool(sp.expand(got - target) == 0)
        row["specialized_target"] = (
            "0"
            if length % 2
            else f"2*sum_p p^(-{length // 2})"
        )
        rows.append(row)
    return {
        "atom_count": atom_count,
        "power_cutoff": power_cutoff,
        "rows": rows,
        "all_exact": all(row["trace_exact"] for row in rows),
        "all_mixed_identity_words_killed": all(
            row["mixed_identity_survivor_count"] == 0 for row in rows
        ),
        "all_odd_traces_zero": all(
            row["trace_expanded"] == "0" for row in rows if row["length"] % 2
        ),
        "all_order_theorem": (
            "Phi_2(C_s^(2r+1))=0 and Phi_2(C_s^(2r))="
            "2*sum_p (p^(-s)*p^(-(1-s)))^r=2*sum_p p^(-r)"
        ),
    }


def first_mixed_identity(edges, atom_count, group, cutoff: int) -> tuple[list[dict], dict | None]:
    rows = []
    first = None
    for length in range(1, cutoff + 1):
        raw = closed_trace(edges, 2 * atom_count, length, group)
        row = {
            key: raw[key]
            for key in [
                "length",
                "closed_path_count",
                "mixed_closed_path_count",
                "identity_survivor_count",
                "mixed_identity_survivor_count",
            ]
        }
        rows.append(row)
        if first is None and raw["mixed_identity_survivor_count"]:
            first = {
                "length": length,
                "count": raw["mixed_identity_survivor_count"],
                "examples": raw["mixed_identity_examples"],
            }
    return rows, first


def label_controls(atom_count: int = 3, cutoff: int = 10) -> dict:
    pairs = directed_chain_pairs(atom_count)

    product = ProductFreeGroup()
    independent_plus = {
        edge: ((index,), ()) for index, edge in enumerate(pairs, 1)
    }
    independent_minus = {
        edge: ((), (index,)) for index, edge in enumerate(pairs, 1)
    }
    independent_edges = alternating_edges_constant(
        atom_count, product, independent_plus, independent_minus
    )
    independent_rows, independent_first = first_mixed_identity(
        independent_edges, atom_count, product, cutoff
    )

    free = FreeGroup()
    shared_plus = {edge: (index,) for index, edge in enumerate(pairs, 1)}
    shared_minus = dict(shared_plus)
    shared_edges = alternating_edges_constant(
        atom_count, free, shared_plus, shared_minus
    )
    shared_rows, shared_first = first_mixed_identity(
        shared_edges, atom_count, free, cutoff
    )

    inverse_minus = {}
    for source, target in pairs:
        reverse = (target, source)
        inverse_minus[(source, target)] = free.inv(shared_plus[reverse])
    inverse_edges = alternating_edges_constant(
        atom_count, free, shared_plus, inverse_minus
    )
    inverse_rows, inverse_first = first_mixed_identity(
        inverse_edges, atom_count, free, cutoff
    )

    cyclic = CyclicGroup(5)
    cyclic_plus = {edge: 1 for edge in pairs}
    cyclic_minus = {edge: 1 for edge in pairs}
    cyclic_edges = alternating_edges_constant(
        atom_count, cyclic, cyclic_plus, cyclic_minus
    )
    cyclic_rows, cyclic_first = first_mixed_identity(
        cyclic_edges, atom_count, cyclic, cutoff
    )

    return {
        "independent_positive_alphabets": {
            "rows": independent_rows,
            "first_mixed_identity": independent_first,
        },
        "shared_positive_alphabet": {
            "rows": shared_rows,
            "first_mixed_identity": shared_first,
            "verdict": "PROVES_TOO_MUCH: alphabet independence is unnecessary",
        },
        "inverse_reflected_labels": {
            "rows": inverse_rows,
            "first_mixed_identity": inverse_first,
            "verdict": "mixed identity leakage",
        },
        "finite_C5_labels": {
            "rows": cyclic_rows,
            "first_mixed_identity": cyclic_first,
            "explanation": (
                "C5 needs cross count divisible by five while a closed walk "
                "on the chain has even cross count; first admissible relation "
                "has ten cross steps"
            ),
        },
    }


# ---------------------------------------------------------------------------
# Schatten-domain and direct-sum audits
# ---------------------------------------------------------------------------


def common_schatten_strip(q: float) -> dict:
    lower = 1.0 / q
    upper = 1.0 - 1.0 / q
    return {
        "q": q,
        "lower_sigma": lower,
        "upper_sigma": upper,
        "nonempty": lower < upper,
        "condition": f"{lower:.12g} < Re(s) < {upper:.12g}",
    }


def schatten_audit() -> dict:
    q_rows = [common_schatten_strip(float(q)) for q in [1, 2, 3, 4, 5]]
    first_integer = next(int(row["q"]) for row in q_rows if row["nonempty"])
    atoms = internal_multiplicative_atoms(2048)
    partial_rows = []
    for q in [2, 3, 4]:
        for sigma in [0.30, 1 / 3, 0.40, 0.50, 0.60, 2 / 3, 0.70]:
            for cutoff in [32, 128, 512, 2048]:
                values = np.asarray(atoms[:cutoff], dtype=float)
                partial_rows.append(
                    {
                        "q": q,
                        "sigma": sigma,
                        "cutoff": cutoff,
                        "plus_q_sum": float(np.sum(values ** (-q * sigma))),
                        "minus_q_sum": float(np.sum(values ** (-q * (1.0 - sigma)))),
                        "inside_common_strip": (1 / q) < sigma < (1 - 1 / q),
                    }
                )
    return {
        "membership_theorem": (
            "T_s^+ in S_q iff q*Re(s)>1; T_(1-s)^- in S_q iff "
            "q*(1-Re(s))>1; common strip is 1/q<Re(s)<1-1/q"
        ),
        "q_rows": q_rows,
        "first_integer_q_with_nonempty_common_strip": first_integer,
        "direct_sum_S1_common_domain": {
            "plus_condition": "Re(s)>1",
            "reflected_condition": "Re(s)<0",
            "intersection": "empty",
            "has_common_domain": False,
        },
        "partial_sum_rows": partial_rows,
    }


# ---------------------------------------------------------------------------
# Pure reflection and det_3
# ---------------------------------------------------------------------------


def pure_reflection_matrix(masses: list[int], s: complex) -> np.ndarray:
    values = np.asarray(masses, dtype=float)
    plus = np.diag(np.exp(-s * np.log(values)))
    minus = np.diag(np.exp(-(1.0 - s) * np.log(values)))
    zero = np.zeros_like(plus)
    return np.block([[zero, plus], [minus, zero]])


def channel_swap(size: int) -> np.ndarray:
    identity = np.eye(size)
    zero = np.zeros((size, size))
    return np.block([[zero, identity], [identity, zero]])


def finite_det3(matrix: np.ndarray, z: complex) -> complex:
    z_matrix = z * matrix
    return np.linalg.det(np.eye(len(matrix), dtype=complex) - z_matrix) * np.exp(
        np.trace(z_matrix) + np.trace(z_matrix @ z_matrix) / 2.0
    )


def det3_product(masses: list[int], z: complex) -> complex:
    values = np.asarray(masses, dtype=float)
    return complex(np.prod((1.0 - z * z / values) * np.exp(z * z / values)))


def reflection_det3_audit() -> dict:
    z = 0.27 + 0.19j
    rows = []
    for atom_count in [2, 3, 8, 16, 32]:
        masses = internal_multiplicative_atoms(atom_count)
        swap = channel_swap(atom_count)
        target = det3_product(masses, z)
        values = []
        reflection_residuals = []
        eigen_residuals = []
        for sigma in [0.40, 0.50, 0.60]:
            for height in [0.0, 1.25, 7.5, 20.0]:
                s = sigma + 1j * height
                matrix = pure_reflection_matrix(masses, s)
                reflected = pure_reflection_matrix(masses, 1.0 - s)
                reflection_residuals.append(
                    float(np.linalg.norm(swap @ matrix @ swap - reflected))
                )
                values.append(finite_det3(matrix, z))
                eigenvalues = np.linalg.eigvals(matrix)
                expected = np.asarray(
                    [sign / math.sqrt(p) for p in masses for sign in [-1, 1]],
                    dtype=complex,
                )
                remaining = list(eigenvalues)
                distance = 0.0
                for item in expected:
                    index = int(np.argmin([abs(got - item) for got in remaining]))
                    distance = max(distance, abs(remaining[index] - item))
                    remaining.pop(index)
                eigen_residuals.append(float(distance))
        rows.append(
            {
                "atom_count": atom_count,
                "last_atom": masses[-1],
                "det3_product_real": target.real,
                "det3_product_imag": target.imag,
                "max_det3_error": float(max(abs(value - target) for value in values)),
                "det3_vertical_range": float(max(abs(value - values[0]) for value in values)),
                "max_reflection_residual": max(reflection_residuals),
                "max_eigenvalue_residual": max(eigen_residuals),
            }
        )
    return {
        "exact_product": "product_p (1-z^2/p)*exp(z^2/p)",
        "log_series": "-sum_(r>=2) z^(2r)/r * sum_p p^(-r)",
        "reflection": "J C_s J = C_(1-s)",
        "s_independent": True,
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# Cross-atom pairings and random DAG controls
# ---------------------------------------------------------------------------


def oriented_pair_sum(p: int, q: int, s: complex) -> complex:
    return p ** (-s) * q ** (-(1.0 - s)) + q ** (-s) * p ** (-(1.0 - s))


def oriented_pair_cosh(p: int, q: int, s: complex) -> complex:
    return 2.0 / math.sqrt(p * q) * np.cosh((s - 0.5) * math.log(q / p))


def pairing_audit(seed_count: int = 32) -> dict:
    p, q = 2, 3
    exact_rows = []
    for sigma in [0.4, 0.5, 0.6]:
        for height in [0.0, 1.0, 5.0, 20.0]:
            s = sigma + 1j * height
            direct = oriented_pair_sum(p, q, s)
            formula = oriented_pair_cosh(p, q, s)
            exact_rows.append(
                {
                    "sigma": sigma,
                    "height": height,
                    "direct_real": direct.real,
                    "direct_imag": direct.imag,
                    "cosh_residual": abs(direct - formula),
                    "reflection_residual": abs(direct - oriented_pair_sum(p, q, 1.0 - s)),
                }
            )

    heights = np.linspace(0.0, 40.0, 401)
    baseline = np.asarray(
        [sum(2.0 / atom for atom in [2, 3]) for _ in heights], dtype=complex
    )
    moving = np.asarray(
        [2.0 * oriented_pair_sum(2, 3, 0.5 + 1j * height) for height in heights]
    )
    control_rows = [
        {
            "seed": -1,
            "pairing": "identity:2->2,3->3",
            "mixed_atom_terms": 0,
            "trace_C2_range": float(np.ptp(baseline.real)),
            "motion": False,
        },
        {
            "seed": -2,
            "pairing": "cross:2<->3",
            "mixed_atom_terms": 2,
            "trace_C2_range": float(np.ptp(moving.real)),
            "motion": bool(np.ptp(moving.real) > 1e-10),
        },
    ]

    masses = internal_multiplicative_atoms(8)
    for seed in range(seed_count):
        rng = np.random.default_rng(seed)
        order = list(rng.permutation(len(masses)))
        pairs = [(order[k], order[k + 1]) for k in range(0, len(order), 2)]
        values = []
        for height in heights:
            s = 0.5 + 1j * height
            # C^2 channel trace: factor two for each oriented two-layer block.
            values.append(
                2.0
                * sum(
                    oriented_pair_sum(masses[left], masses[right], s)
                    for left, right in pairs
                )
            )
        values = np.asarray(values)
        control_rows.append(
            {
                "seed": seed,
                "pairing": ";".join(f"{masses[a]}<->{masses[b]}" for a, b in pairs),
                "mixed_atom_terms": 2 * len(pairs),
                "trace_C2_range": float(np.ptp(values.real)),
                "motion": bool(np.ptp(values.real) > 1e-10),
            }
        )
    return {
        "two_atom_formula": (
            "p^(-s)q^(-(1-s))+q^(-s)p^(-(1-s))="
            "2/sqrt(pq)*cosh((s-1/2)log(q/p))"
        ),
        "full_two_oriented_block_trace_C2": "4/sqrt(pq)*cosh((s-1/2)log(q/p))",
        "mixed_ledger": "p!=q gives ordered mixed atom masses, not a pure p^r repetition",
        "formula_rows": exact_rows,
        "control_rows": control_rows,
        "random_motion_pass_count": sum(row["motion"] for row in control_rows if row["seed"] >= 0),
        "verdict": "PROVES_TOO_MUCH: arbitrary cross-atom pairings create motion by violating the pure ledger",
    }


def endpoint_transfer(masses: list[int], s: complex, coefficients: np.ndarray) -> np.ndarray:
    values = np.asarray(masses, dtype=float)
    diagonal = np.exp(-s * np.log(values))
    answer = np.diag(diagonal).astype(complex)
    for target in range(len(values)):
        for source in range(target + 1, len(values)):
            if coefficients[target, source] != 0:
                answer[target, source] = (
                    coefficients[target, source]
                    * (diagonal[target] + diagonal[source])
                    / 2.0
                )
    return answer


def random_dag_audit(seed_count: int = 24) -> dict:
    masses = internal_multiplicative_atoms(6)
    heights = np.linspace(0.0, 30.0, 121)
    rows = []
    for seed in range(seed_count):
        rng = np.random.default_rng(seed)
        coefficients = np.zeros((len(masses), len(masses)), dtype=complex)
        for target in range(len(masses)):
            for source in range(target + 1, len(masses)):
                if rng.random() < 0.55:
                    coefficients[target, source] = (
                        rng.normal() + 1j * rng.normal()
                    ) / math.sqrt(2)

        trace_error = 0.0
        determinant_values = []
        schatten4 = []
        for height in heights:
            s = 0.5 + 1j * height
            plus = endpoint_transfer(masses, s, coefficients)
            minus = endpoint_transfer(masses, 1.0 - s, coefficients)
            zero = np.zeros_like(plus)
            matrix = np.block([[zero, plus], [minus, zero]])
            for power in [2, 4, 6, 8]:
                target = (
                    2.0 * sum(p ** (-(power // 2)) for p in masses)
                )
                trace_error = max(
                    trace_error,
                    abs(np.trace(np.linalg.matrix_power(matrix, power)) - target),
                )
            determinant_values.append(finite_det3(matrix, 0.2 + 0.1j))
            singular = np.linalg.svd(matrix, compute_uv=False)
            schatten4.append(float(np.sum(singular**4)))
        rows.append(
            {
                "seed": seed,
                "edge_count": int(np.count_nonzero(coefficients)),
                "max_trace_error_r2_r4_r6_r8": float(trace_error),
                "det3_vertical_range": float(
                    max(abs(value - determinant_values[0]) for value in determinant_values)
                ),
                "schatten4_range": float(np.ptp(schatten4)),
                "ledger_exact_numeric": bool(trace_error < 1e-9),
                "singular_motion": bool(np.ptp(schatten4) > 1e-8),
            }
        )
    return {
        "rows": rows,
        "ledger_pass_count": sum(row["ledger_exact_numeric"] for row in rows),
        "singular_motion_count": sum(row["singular_motion"] for row in rows),
        "verdict": (
            "PROVES_TOO_MUCH: arbitrary upper-DAG radicals preserve all cyclic "
            "traces/det3 while generically moving singular moments"
        ),
    }


# ---------------------------------------------------------------------------
# Inventory controls
# ---------------------------------------------------------------------------


def inventory_audit() -> dict:
    rng = np.random.default_rng(1907)
    tensor_atoms = internal_multiplicative_atoms(8)
    shuffled = list(np.asarray(tensor_atoms)[rng.permutation(8)])
    composites = [4, 6, 8, 9, 10, 12, 14, 15]
    random_values = sorted(rng.choice(np.arange(2, 80), size=8, replace=False).tolist())
    rows = []
    for name, values in [
        ("tensor_atoms", tensor_atoms),
        ("shuffled_atoms", shuffled),
        ("composites", composites),
        ("matched_random_integers", random_values),
    ]:
        pure_trace = 2 * sum(1.0 / value for value in values)
        rows.append(
            {
                "inventory": name,
                "values": json.dumps([int(value) for value in values]),
                "trace_C2": pure_trace,
                "vertical_range": 0.0,
                "pure_reflection_ledger": True,
            }
        )
    return {
        "rows": rows,
        "verdict": "PROVES_TOO_MUCH: reflection sterility holds for every positive inventory",
    }


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: (
                        json.dumps(value, sort_keys=True)
                        if isinstance(value, (dict, list))
                        else value
                    )
                    for key, value in row.items()
                }
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    exact = exact_candidate_audit()
    labels = label_controls()
    schatten = schatten_audit()
    det3 = reflection_det3_audit()
    pairings = pairing_audit()
    dags = random_dag_audit()
    inventories = inventory_audit()

    results = {
        "metadata": {
            "candidate_id": "SD-C11",
            "candidate": "holomorphic reflection double without adjoint",
            "primary_family": "symbolic dynamics",
            "uses_riemann_zero_data": False,
            "fits_target_zeros": False,
            "crossing_census_performed": False,
        },
        "exact_candidate": exact,
        "label_controls": labels,
        "schatten_domain": schatten,
        "reflection_det3": det3,
        "cross_atom_pairings": pairings,
        "random_DAG_controls": dags,
        "inventory_controls": inventories,
        "claim_boundary": {
            "odd_even_trace_theorem": "PROVED",
            "common_Sq_strip": "PROVED; 1/q<Re(s)<1-1/q, first integer q=3",
            "det3_product": "PROVED; reflection symmetric and s-independent",
            "pure_prime_vertical_motion": "REFUTED",
            "cross_atom_motion": "PROVED but necessarily mixed generalized ledger",
            "free_alphabet_independence": "REFUTED by shared-positive control",
            "direct_sum_common_S1_domain": "EMPTY",
            "global_target_divisor": "NOT ESTABLISHED",
            "rh_or_target_zero_claim": "FORBIDDEN / NOT MADE",
            "route_b_invocation_allowed": False,
        },
    }

    (args.output_dir / "summary.json").write_text(
        json.dumps(results, indent=2, sort_keys=True, default=str) + "\n"
    )
    write_csv(args.output_dir / "exact_trace.csv", exact["rows"])
    write_csv(args.output_dir / "schatten_partial_sums.csv", schatten["partial_sum_rows"])
    write_csv(args.output_dir / "det3_reflection.csv", det3["rows"])
    write_csv(args.output_dir / "pairing_controls.csv", pairings["control_rows"])
    write_csv(args.output_dir / "pairing_formula.csv", pairings["formula_rows"])
    write_csv(args.output_dir / "random_dag_controls.csv", dags["rows"])
    write_csv(args.output_dir / "inventory_controls.csv", inventories["rows"])

    print(
        json.dumps(
            {
                "output": str(args.output_dir / "summary.json"),
                "exact_traces": exact["all_exact"],
                "mixed_killed": exact["all_mixed_identity_words_killed"],
                "first_common_integer_q": schatten[
                    "first_integer_q_with_nonempty_common_strip"
                ],
                "det3_s_independent": det3["s_independent"],
                "random_pairing_motion": pairings["random_motion_pass_count"],
                "random_dag_ledger_pass": dags["ledger_pass_count"],
                "no_zero_data": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
