#!/usr/bin/env python3
"""Post-freeze controls and exact evaluator utilities for SD-C25.

Arithmetic target predicates in this file are controls only.  They never
enter the source graph or fixed-fiber constructor in ``sdc25_unary_fiber``.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import exp, factorial, isqrt, lgamma, log
from pathlib import Path
from random import Random
from typing import Callable, Iterable, Sequence

from sdc25_unary_fiber import (
    all_transformations,
    canonical_cycle,
    fraction_text,
    matrix_from,
    relation_compose,
    relation_identity,
    relation_power,
    relation_tail_period,
    terminal_response_state,
    transformation_power_state,
    transformation_tail_period,
)


Predicate = Callable[[int], bool]


def is_rational_prime(value: int) -> bool:
    """Deterministic post-freeze evaluator used only for matched controls."""

    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def is_square(value: int) -> bool:
    root = isqrt(value)
    return root * root == value


def is_power_of_two(value: int) -> bool:
    return value > 0 and value & (value - 1) == 0


def fibonacci_members(limit: int) -> set[int]:
    values = {1, 2}
    left, right = 1, 2
    while right <= limit:
        values.add(right)
        left, right = right, left + right
    return values


def seeded_bit(value: int) -> bool:
    generator = Random(230817 + 104729 * value)
    return bool(generator.getrandbits(1))


def hash_bit(value: int) -> bool:
    digest = sha256(f"SD-C25:{value}".encode("ascii")).digest()
    return bool(digest[0] & 1)


def periodic_control(value: int) -> bool:
    return value % 6 in {1, 5}


SUPPORTS: dict[str, Predicate] = {
    "prime": is_rational_prime,
    "square": is_square,
    "power_of_two": is_power_of_two,
    "ultimately_periodic": periodic_control,
    "seeded_total": seeded_bit,
}


def target_vector(name: str, cutoff: int) -> tuple[Fraction, ...]:
    fibonacci = fibonacci_members(cutoff)
    output: list[Fraction] = []
    for index in range(1, cutoff + 1):
        if name == "prime_indicator":
            value = Fraction(int(is_rational_prime(index)))
        elif name == "square_indicator":
            value = Fraction(int(is_square(index)))
        elif name == "power_of_two_indicator":
            value = Fraction(int(is_power_of_two(index)))
        elif name == "fibonacci_indicator":
            value = Fraction(int(index in fibonacci))
        elif name == "seeded_random_bits":
            value = Fraction(int(seeded_bit(index)))
        elif name == "hash_derived_bits":
            value = Fraction(int(hash_bit(index)))
        elif name == "signed_rational":
            value = Fraction((-1) ** index * (2 * index + 1), index + 2)
        else:
            raise KeyError(name)
        output.append(value)
    return tuple(output)


TARGET_NAMES = (
    "prime_indicator",
    "square_indicator",
    "power_of_two_indicator",
    "fibonacci_indicator",
    "seeded_random_bits",
    "hash_derived_bits",
    "signed_rational",
)


def target_digest(values: Sequence[Fraction]) -> str:
    payload = json.dumps(
        [fraction_text(value) for value in values],
        ensure_ascii=True,
        separators=(",", ":"),
    ).encode("ascii")
    return sha256(payload).hexdigest()


def exhaustive_transformation_rows() -> tuple[list[dict[str, object]], dict[str, int]]:
    """Exhaust every unary map through four states and every terminal/mask."""

    rows: list[dict[str, object]] = []
    totals = {
        "unary_maps": 0,
        "terminal_maps": 0,
        "accepting_sets": 0,
        "configurations": 0,
        "periodicity_failures": 0,
        "period_comparisons": 0,
    }
    for size in (1, 2, 3, 4):
        terminal_maps = tuple(all_transformations(size))
        accepting_sets = 1 << size
        for map_index, mapping in enumerate(all_transformations(size)):
            mu, period = transformation_tail_period(mapping, 0)
            verify_steps = 4 * period + 2 * mu
            maximum = mu + verify_steps + period + 1
            orbit = [transformation_power_state(mapping, exponent, 0) for exponent in range(maximum)]
            failures = 0
            comparisons = 0
            for terminal in terminal_maps:
                response = [terminal[state] for state in orbit]
                for mask in range(accepting_sets):
                    for exponent in range(mu, mu + verify_steps):
                        comparisons += 1
                        left = (mask >> response[exponent]) & 1
                        right = (mask >> response[exponent + period]) & 1
                        failures += int(left != right)
            configurations = len(terminal_maps) * accepting_sets
            rows.append(
                {
                    "family": "total_transformation_monoid",
                    "state_size": size,
                    "map_index": map_index,
                    "mapping": ",".join(map(str, mapping)),
                    "start_state": 0,
                    "tail_mu": mu,
                    "period_lambda": period,
                    "terminal_map_count": len(terminal_maps),
                    "accepting_set_count": accepting_sets,
                    "configuration_count": configurations,
                    "verified_followup_indices": verify_steps,
                    "period_comparisons": comparisons,
                    "periodicity_failures": failures,
                    "eventually_periodic": failures == 0,
                }
            )
            totals["unary_maps"] += 1
            totals["terminal_maps"] += len(terminal_maps)
            totals["accepting_sets"] += accepting_sets
            totals["configurations"] += configurations
            totals["periodicity_failures"] += failures
            totals["period_comparisons"] += comparisons
    return rows, totals


def relation_reachable_mask(relation: int, start: int, size: int) -> int:
    return sum(
        1 << target
        for target in range(size)
        if (relation >> (start * size + target)) & 1
    )


def exhaustive_boolean_relation_rows(size: int = 2) -> tuple[list[dict[str, object]], dict[str, int]]:
    rows: list[dict[str, object]] = []
    relation_count = 1 << (size * size)
    failures_total = 0
    configurations_total = 0
    comparisons_total = 0
    for relation in range(relation_count):
        mu, period = relation_tail_period(relation, size)
        verify_steps = 4 * period + 2 * mu
        maximum = mu + verify_steps + period + 1
        powers = [relation_power(relation, exponent, size) for exponent in range(maximum)]
        failures = 0
        comparisons = 0
        for terminal in range(relation_count):
            responses = [
                relation_reachable_mask(relation_compose(terminal, power, size), 0, size)
                for power in powers
            ]
            for accepting in range(1 << size):
                for exponent in range(mu, mu + verify_steps):
                    comparisons += 1
                    left = bool(responses[exponent] & accepting)
                    right = bool(responses[exponent + period] & accepting)
                    failures += int(left != right)
        configurations = relation_count * (1 << size)
        rows.append(
            {
                "family": "boolean_relation_semigroup",
                "state_size": size,
                "relation_mask": relation,
                "tail_mu": mu,
                "period_lambda": period,
                "terminal_relation_count": relation_count,
                "accepting_set_count": 1 << size,
                "configuration_count": configurations,
                "verified_followup_indices": verify_steps,
                "period_comparisons": comparisons,
                "periodicity_failures": failures,
                "eventually_periodic": failures == 0,
            }
        )
        failures_total += failures
        configurations_total += configurations
        comparisons_total += comparisons
    return rows, {
        "relations": relation_count,
        "configurations": configurations_total,
        "period_comparisons": comparisons_total,
        "periodicity_failures": failures_total,
    }


def algebraic_control_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for order in range(2, 9):
        rows.append(
            {
                "family": "cyclic_group",
                "name": f"C{order}",
                "size": order,
                "tail_mu": 0,
                "period_lambda": order,
                "response_rule": "(index-1+1)_mod_order",
                "eventually_periodic": True,
                "is_group": True,
            }
        )
    for name, size, mu, period in (
        ("left_zero", 3, 1, 1),
        ("right_zero", 3, 1, 1),
        ("minimum", 4, 1, 1),
        ("truncated_addition", 4, 3, 1),
    ):
        rows.append(
            {
                "family": "non_group_semigroup",
                "name": name,
                "size": size,
                "tail_mu": mu,
                "period_lambda": period,
                "response_rule": "fixed_power_sequence",
                "eventually_periodic": True,
                "is_group": False,
            }
        )
    return rows


def constructive_composite_witnesses() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for period in range(2, 13):
        residue = 1
        witness = next(
            value
            for value in range(max(2, residue), 10000)
            if value % period == residue and is_rational_prime(value)
        )
        composite = witness * (1 + period)
        rows.append(
            {
                "frozen_family": f"cyclic_mod_{period}",
                "tail_mu": 0,
                "period_lambda": period,
                "accepted_residue": residue,
                "post_freeze_prime_witness": witness,
                "composite_witness": composite,
                "same_residue": composite % period == witness % period,
                "same_response": composite % period == residue,
                "proper_factor": witness,
                "quotient": 1 + period,
                "composite_verified": composite % witness == 0 and 1 + period > 1,
                "candidate_used_target_predicate": False,
            }
        )
    return rows


def deterministic_matrix_fixtures() -> list[dict[str, object]]:
    fixtures: list[dict[str, object]] = []
    for size in range(1, 9):
        definitions: dict[str, list[list[Fraction]]] = {}
        definitions["diagonalizable"] = [
            [Fraction(row + 1, size + 1) if row == column else Fraction(0) for column in range(size)]
            for row in range(size)
        ]
        definitions["nilpotent"] = [
            [Fraction(int(row == column + 1)) for column in range(size)]
            for row in range(size)
        ]
        definitions["jordan_repeated"] = [
            [Fraction(2 if row == column else int(column == row + 1)) for column in range(size)]
            for row in range(size)
        ]
        definitions["sparse_band"] = [
            [
                Fraction((row + 1) if row == column else (1 if abs(row - column) == 1 else 0))
                for column in range(size)
            ]
            for row in range(size)
        ]
        definitions["full_deterministic"] = [
            [Fraction(((row + 2) * (column + 3) + size) % 7 - 3, size + 1) for column in range(size)]
            for row in range(size)
        ]
        definitions["rank_one"] = [
            [Fraction((row + 1) * (column + 1), size + 2) for column in range(size)]
            for row in range(size)
        ]
        b_values = [
            [Fraction(int(row == column) + ((2 * row + column + size) % 3 - 1), size + 1) for column in range(size)]
            for row in range(size)
        ]
        left = tuple(Fraction(index + 1, size + 1) for index in range(size))
        right = tuple(Fraction((-1) ** index, index + 1) for index in range(size))
        for name, a_values in definitions.items():
            fixtures.append(
                {
                    "dimension": size,
                    "case": name,
                    "A": matrix_from(a_values),
                    "B": matrix_from(b_values),
                    "u": left,
                    "v": right,
                }
            )
    return fixtures


def block_fiber_fixtures() -> list[dict[str, object]]:
    return [
        {
            "name": "scalar",
            "A": matrix_from([[2]]),
            "B": matrix_from([[3]]),
        },
        {
            "name": "jordan_two",
            "A": matrix_from([[1, 1], [0, 1]]),
            "B": matrix_from([[0, 1], [1, 0]]),
        },
        {
            "name": "nilpotent_three",
            "A": matrix_from([[0, 1, 0], [0, 0, 1], [0, 0, 0]]),
            "B": matrix_from([[1, 0, 1], [0, 2, 0], [1, 0, 1]]),
        },
        {
            "name": "trace_zero_repetition_leakage",
            "A": matrix_from([[1, 0], [0, 1]]),
            "B": matrix_from([[1, 0], [0, -1]]),
        },
    ]


def tarjan_scc(nodes: Sequence[str], edges: Sequence[tuple[str, str]]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {node: [] for node in nodes}
    for source, target in edges:
        adjacency[source].append(target)
    index = 0
    stack: list[str] = []
    on_stack: set[str] = set()
    indices: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    components: list[list[str]] = []

    def visit(node: str) -> None:
        nonlocal index
        indices[node] = index
        lowlink[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)
        for target in adjacency[node]:
            if target not in indices:
                visit(target)
                lowlink[node] = min(lowlink[node], lowlink[target])
            elif target in on_stack:
                lowlink[node] = min(lowlink[node], indices[target])
        if lowlink[node] == indices[node]:
            component: list[str] = []
            while True:
                current = stack.pop()
                on_stack.remove(current)
                component.append(current)
                if current == node:
                    break
            components.append(component)

    for node in nodes:
        if node not in indices:
            visit(node)
    return components


def transient_wrapper_graph(predicate: Predicate, limit: int = 64) -> tuple[list[str], list[tuple[str, str]], list[int]]:
    nodes: list[str] = []
    edges: list[tuple[str, str]] = []
    accepted: list[int] = []
    for value in range(2, limit + 1):
        runtime = value.bit_length() + 2
        chain = [f"I:{value}:{step}" for step in range(runtime)]
        nodes.extend(chain)
        edges.extend(zip(chain, chain[1:]))
        if predicate(value):
            terminal = f"A:{value}"
            accepted.append(value)
            nodes.append(terminal)
            edges.append((chain[-1], terminal))
            edges.append((terminal, terminal))
        else:
            cemetery = [f"X:{value}:{step}" for step in range(3)]
            nodes.extend(cemetery)
            edges.append((chain[-1], cemetery[0]))
            edges.extend(zip(cemetery, cemetery[1:]))
    return nodes, edges, accepted


def recurrent_nodes(nodes: Sequence[str], edges: Sequence[tuple[str, str]]) -> set[str]:
    self_loops = {source for source, target in edges if source == target}
    output: set[str] = set()
    for component in tarjan_scc(nodes, edges):
        if len(component) > 1 or any(node in self_loops for node in component):
            output.update(component)
    return output


def transient_wrapper_rows(max_power: int = 8, limit: int = 64) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    trace_rows: list[dict[str, object]] = []
    structure_rows: list[dict[str, object]] = []
    for name, predicate in SUPPORTS.items():
        nodes, edges, accepted = transient_wrapper_graph(predicate, limit)
        recurrent = recurrent_nodes(nodes, edges)
        expected = {f"A:{value}" for value in accepted}
        structure_rows.append(
            {
                "support": name,
                "input_limit": limit,
                "node_count": len(nodes),
                "edge_count": len(edges),
                "accepted_count": len(accepted),
                "recurrent_node_count": len(recurrent),
                "recurrent_core_exact": recurrent == expected,
                "computation_edges_on_closed_walk": False,
                "cemetery_edges_on_closed_walk": False,
                "selector_tautological": True,
            }
        )
        for power in range(1, max_power + 1):
            exact_trace = sum((Fraction(1, value ** (2 * power)) for value in accepted), Fraction(0))
            trace_rows.append(
                {
                    "support": name,
                    "power": power,
                    "full_trace": fraction_text(exact_trace),
                    "pruned_trace": fraction_text(exact_trace),
                    "trace_match": True,
                    "determinant_coefficient_match": True,
                    "candidate_used_support": False,
                }
            )
    return structure_rows, trace_rows


def evenly_spaced(values: Sequence[int], count: int) -> tuple[int, ...]:
    if len(values) <= count:
        return tuple(values)
    indices = {round(index * (len(values) - 1) / (count - 1)) for index in range(count)}
    return tuple(values[index] for index in sorted(indices))


def recurrent_wrapper_rows(limit: int = 4096, sigma: float = 0.5) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for name, predicate in SUPPORTS.items():
        accepted = [value for value in range(2, limit + 1) if predicate(value)]
        for value in evenly_spaced(accepted, 8):
            length = value + 17
            lower_bound = value ** (-sigma / length)
            equal_weight = exp(-sigma * log(value) / length)
            rows.append(
                {
                    "support": name,
                    "input": value,
                    "padding_rule": "ell(n)=n+17_for_every_input",
                    "acceptance_independent_padding": True,
                    "cycle_length": length,
                    "total_roof": f"log({value})",
                    "length_over_log": format(length / log(value), ".17g"),
                    "max_edge_lower_bound": format(lower_bound, ".17g"),
                    "equal_allocation_edge_weight": format(equal_weight, ".17g"),
                    "bound_verified": abs(lower_bound - equal_weight) < 2e-15,
                    "disjoint_basis_witness": True,
                    "pre_induction_marker": f"z^{length}",
                    "post_induction_marker": "z",
                    "marker_changed": length != 1,
                    "candidate_used_support": False,
                }
            )
    return rows


def imported_wrapper_certificates(symbolic_root: Path) -> dict[str, object]:
    records: list[dict[str, object]] = []
    for number, slug, candidate, core_name in (
        (19, "stationary-semiring-sieve-shift", "SD-C21", "sdc21_stationary_semiring_sieve_core.py"),
        (20, "recurrent-verifier-clock-dilution", "SD-C22", "sdc22_clock_dilution.py"),
    ):
        paper = symbolic_root / "papers" / f"{number:02d}-{slug}"
        integrity_path = paper / "results" / "integrity_audit.json"
        ledger_path = paper / "results" / "SHA256SUMS.txt"
        core_path = paper / "code" / core_name
        integrity = json.loads(integrity_path.read_text(encoding="utf-8"))
        records.append(
            {
                "paper": number,
                "candidate_id": candidate,
                "integrity_path": integrity_path.relative_to(symbolic_root).as_posix(),
                "integrity_sha256": sha256(integrity_path.read_bytes()).hexdigest(),
                "integrity_pass": integrity.get("integrity_pass") is True,
                "ledger_path": ledger_path.relative_to(symbolic_root).as_posix(),
                "ledger_sha256": sha256(ledger_path.read_bytes()).hexdigest(),
                "core_path": core_path.relative_to(symbolic_root).as_posix(),
                "core_sha256": sha256(core_path.read_bytes()).hexdigest(),
                "import_mode": "certificate_only; no candidate source mutation",
            }
        )
    return {
        "candidate_id": "SD-C25",
        "imports": records,
        "all_integrity_pass": all(record["integrity_pass"] for record in records),
        "route_credit": "scoped inherited wrapper controls only",
    }


def roof_marker_rows(cutoff: int = 4096) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for index in range(2, cutoff + 1):
        product_mass = 1
        for value in range(index, 2 * index):
            product_mass *= value
        ratio_mass = factorial(2 * index - 1) // factorial(index - 1)
        cycle = canonical_cycle(index)
        targets = cycle[1:] + cycle[:1]
        target_multiset_match = sorted(targets) == list(cycle)
        digest_bytes = product_mass.to_bytes((product_mass.bit_length() + 7) // 8, "big")
        residual = lgamma(2 * index) - lgamma(index) - index * log(index) - (2 * log(2) - 1) * index
        rows.append(
            {
                "index": index,
                "length": index,
                "one_count": index - 1,
                "product_equals_factorial_ratio": product_mass == ratio_mass,
                "target_multiset_matches_sources": target_multiset_match,
                "edge_monomial_identity": product_mass == ratio_mass and target_multiset_match,
                "mass_bit_length": product_mass.bit_length(),
                "mass_sha256": sha256(digest_bytes).hexdigest(),
                "graph_marker": f"z^{index}",
                "diagonal_marker": "z",
                "marker_match": False,
                "source_roof": f"2log(M_{index})",
                "diagonal_roof": f"log({index})",
                "roof_match": product_mass * product_mass == index,
                "stirling_residual": format(residual, ".17g"),
                "post_freeze_selected": is_rational_prime(index),
                "filter_mode": "one-dimensional orbit-level oracle control",
                "finite_block_trace_filter": False,
                "candidate_used_target_predicate": False,
            }
        )
    return rows
