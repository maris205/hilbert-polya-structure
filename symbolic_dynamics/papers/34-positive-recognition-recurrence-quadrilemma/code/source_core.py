#!/usr/bin/env python3
"""Neutral exact graph, word, code, roof, and determinant machinery."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import gcd
from typing import Iterable, Iterator, Sequence


Edge = tuple[int, int]
Cycle = tuple[Edge, ...]
Polynomial = list[Fraction]


def divisors(value: int) -> list[int]:
    return [item for item in range(1, value + 1) if value % item == 0]


def edge_list(vertex_count: int, mask: int) -> tuple[Edge, ...]:
    return tuple(
        (left, right)
        for left in range(vertex_count)
        for right in range(vertex_count)
        if mask & (1 << (left * vertex_count + right))
    )


def edge_mask(vertex_count: int, edges: Iterable[Edge]) -> int:
    value = 0
    for left, right in edges:
        value |= 1 << (left * vertex_count + right)
    return value


def adjacency(vertex_count: int, edges: Iterable[Edge]) -> tuple[tuple[int, ...], ...]:
    rows: list[list[int]] = [[] for _ in range(vertex_count)]
    for left, right in edges:
        rows[left].append(right)
    return tuple(tuple(sorted(row)) for row in rows)


def strongly_connected_components(
    vertex_count: int, edges: Iterable[Edge]
) -> tuple[tuple[int, ...], ...]:
    """Tarjan SCC decomposition, canonically ordered."""
    rows = adjacency(vertex_count, edges)
    index = 0
    indices = [-1] * vertex_count
    low = [0] * vertex_count
    stack: list[int] = []
    active: set[int] = set()
    output: list[tuple[int, ...]] = []

    def visit(vertex: int) -> None:
        nonlocal index
        indices[vertex] = index
        low[vertex] = index
        index += 1
        stack.append(vertex)
        active.add(vertex)
        for other in rows[vertex]:
            if indices[other] == -1:
                visit(other)
                low[vertex] = min(low[vertex], low[other])
            elif other in active:
                low[vertex] = min(low[vertex], indices[other])
        if low[vertex] == indices[vertex]:
            component: list[int] = []
            while True:
                other = stack.pop()
                active.remove(other)
                component.append(other)
                if other == vertex:
                    break
            output.append(tuple(sorted(component)))

    for vertex in range(vertex_count):
        if indices[vertex] == -1:
            visit(vertex)
    return tuple(sorted(output))


def rotate_tuple(values: Sequence[Edge], offset: int) -> tuple[Edge, ...]:
    return tuple(values[offset:]) + tuple(values[:offset])


def canonical_cycle(word: Sequence[Edge]) -> Cycle:
    if not word:
        raise ValueError("closed word must be nonempty")
    rotations = [rotate_tuple(word, offset) for offset in range(len(word))]
    return min(rotations)


def rotate_cycle_to_vertex(cycle: Cycle, vertex: int) -> Cycle:
    candidates = [
        rotate_tuple(cycle, offset)
        for offset, edge in enumerate(cycle)
        if edge[0] == vertex
    ]
    if not candidates:
        raise ValueError("base vertex absent from cycle")
    return min(candidates)


def legal_closed_word(word: Sequence[Edge]) -> bool:
    if not word:
        return False
    return all(
        word[index][1] == word[(index + 1) % len(word)][0]
        for index in range(len(word))
    )


def primitive_root(word: Sequence[Edge]) -> tuple[Cycle, int]:
    if not legal_closed_word(word):
        raise ValueError("primitive root requires a legal closed word")
    items = tuple(word)
    for period in divisors(len(items)):
        block = items[:period]
        exponent = len(items) // period
        if block * exponent == items:
            return tuple(block), exponent
    raise AssertionError("full word is always a period")


def all_simple_cycles(vertex_count: int, edges: Iterable[Edge]) -> tuple[Cycle, ...]:
    rows = adjacency(vertex_count, edges)
    found: set[Cycle] = set()

    def walk(start: int, path: tuple[int, ...], used: frozenset[int]) -> None:
        current = path[-1]
        for other in rows[current]:
            if other == start:
                vertices = path
                cycle = tuple(
                    (vertices[index], vertices[(index + 1) % len(vertices)])
                    for index in range(len(vertices))
                )
                found.add(canonical_cycle(cycle))
            elif other not in used:
                walk(start, path + (other,), used | {other})

    for start in range(vertex_count):
        walk(start, (start,), frozenset({start}))
    return tuple(sorted(found))


def cycle_vertices(cycle: Cycle) -> frozenset[int]:
    return frozenset(edge[0] for edge in cycle)


def cycle_component(cycle: Cycle, components: Sequence[Sequence[int]]) -> int:
    vertices = cycle_vertices(cycle)
    for index, component in enumerate(components):
        if vertices <= set(component):
            return index
    raise AssertionError("cycle must belong to one SCC")


def shortest_external_path(
    vertex_count: int,
    edges: Iterable[Edge],
    start: int,
    end: int,
    forbidden_internal: frozenset[int],
) -> tuple[Edge, ...] | None:
    rows = adjacency(vertex_count, edges)
    queue: deque[tuple[int, ...]] = deque([(start,)])
    candidates: list[tuple[int, ...]] = []
    best_length: int | None = None
    while queue:
        path = queue.popleft()
        if best_length is not None and len(path) > best_length:
            continue
        current = path[-1]
        if current == end and len(path) > 1:
            best_length = len(path)
            candidates.append(path)
            continue
        for other in rows[current]:
            if other in path:
                continue
            if other != end and other in forbidden_internal:
                continue
            queue.append(path + (other,))
    if not candidates:
        return None
    vertices = min(candidates)
    return tuple(zip(vertices[:-1], vertices[1:]))


def connector_word(
    vertex_count: int,
    edges: Iterable[Edge],
    first: Cycle,
    second: Cycle,
    external_only: bool,
) -> tuple[Cycle, Cycle, Cycle] | None:
    first_vertices = cycle_vertices(first)
    second_vertices = cycle_vertices(second)
    if first_vertices & second_vertices:
        raise ValueError("connector construction requires disjoint cycles")
    forbidden = first_vertices | second_vertices if external_only else frozenset()
    candidates: list[tuple[tuple[object, ...], Cycle, Cycle, Cycle]] = []
    for left in sorted(first_vertices):
        for right in sorted(second_vertices):
            outward = shortest_external_path(
                vertex_count, edges, left, right, forbidden
            )
            inward = shortest_external_path(
                vertex_count, edges, right, left, forbidden
            )
            if outward is None or inward is None:
                continue
            based_first = rotate_cycle_to_vertex(first, left)
            based_second = rotate_cycle_to_vertex(second, right)
            word = based_first + outward + based_second + inward
            key: tuple[object, ...] = (
                len(outward) + len(inward),
                outward,
                inward,
                based_first,
                based_second,
            )
            candidates.append((key, word, outward, inward))
    if not candidates:
        return None
    _, word, outward, inward = min(candidates, key=lambda item: item[0])
    return word, outward, inward


def positive_edge_weight(vertex_count: int, edge: Edge) -> Fraction:
    index = edge[0] * vertex_count + edge[1] + 2
    return Fraction(index, index + 1)


def word_weight(vertex_count: int, word: Sequence[Edge]) -> Fraction:
    value = Fraction(1, 1)
    for edge in word:
        value *= positive_edge_weight(vertex_count, edge)
    return value


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def edge_word_text(word: Sequence[Edge]) -> str:
    return ";".join(f"{left}>{right}" for left, right in word)


def witness_line(
    family: str,
    vertex_count: int,
    mask: int,
    first: Cycle,
    second: Cycle,
    root: Cycle,
    exponent: int,
) -> str:
    return "|".join(
        (
            family,
            str(vertex_count),
            str(mask),
            edge_word_text(first),
            edge_word_text(second),
            edge_word_text(root),
            str(exponent),
            fraction_text(word_weight(vertex_count, root)),
        )
    )


def hash_graph_edges(case_index: int, vertex_count: int) -> tuple[Edge, ...]:
    present: set[Edge] = {
        (vertex, (vertex + 1) % vertex_count) for vertex in range(vertex_count)
    }
    for left in range(vertex_count):
        for right in range(vertex_count):
            token = f"P34-GRAPH-{case_index}-{vertex_count}-{left}-{right}".encode()
            if sha256(token).digest()[0] < 72:
                present.add((left, right))
    return tuple(sorted(present))


def graph_pair_audit(
    vertex_count: int,
    mask: int,
    edges: tuple[Edge, ...],
    witness_digest: object,
    samples: list[dict[str, object]],
    failures: list[dict[str, object]],
    construction_counterexamples: list[dict[str, object]],
) -> dict[str, int]:
    components = strongly_connected_components(vertex_count, edges)
    cycles = all_simple_cycles(vertex_count, edges)
    grouped: dict[int, list[Cycle]] = {index: [] for index in range(len(components))}
    for cycle in cycles:
        grouped[cycle_component(cycle, components)].append(cycle)
    counters = {
        "recurrent_sccs": sum(bool(group) for group in grouped.values()),
        "multi_cycle_sccs": sum(len(group) >= 2 for group in grouped.values()),
        "simple_cycles": len(cycles),
        "shared_pairs": 0,
        "connector_pairs": 0,
        "strict_external_connector_failures": 0,
        "mixed_roots": 0,
        "failures": 0,
    }
    for group in grouped.values():
        for first, second in combinations(sorted(group), 2):
            shared = cycle_vertices(first) & cycle_vertices(second)
            family: str
            word: Cycle
            extra: tuple[Cycle, Cycle] | None = None
            if shared:
                family = "shared_state"
                base = min(shared)
                based_first = rotate_cycle_to_vertex(first, base)
                based_second = rotate_cycle_to_vertex(second, base)
                word = based_first + based_second
                counters["shared_pairs"] += 1
            else:
                family = "mutual_connector"
                counters["connector_pairs"] += 1
                strict = connector_word(
                    vertex_count, edges, first, second, external_only=True
                )
                if strict is None:
                    counters["strict_external_connector_failures"] += 1
                    construction_counterexamples.append(
                        {
                            "vertex_count": vertex_count,
                            "mask": mask,
                            "first": edge_word_text(first),
                            "second": edge_word_text(second),
                            "strict_external_witness_exists": False,
                            "minimal_repair": "allow_SCC_paths_to_traverse_cycle_vertices",
                        }
                    )
                built = connector_word(
                    vertex_count, edges, first, second, external_only=False
                )
                if built is None:
                    counters["failures"] += 1
                    failures.append(
                        {
                            "family": family,
                            "vertex_count": vertex_count,
                            "mask": mask,
                            "reason": "same_scc_without_external_connector_pair",
                            "first": edge_word_text(first),
                            "second": edge_word_text(second),
                        }
                    )
                    continue
                word, outward, inward = built
                extra = (outward, inward)
            root, exponent = primitive_root(word)
            root_canonical = canonical_cycle(root)
            distinct = (
                root_canonical != canonical_cycle(first)
                and root_canonical != canonical_cycle(second)
            )
            weight_identity = (
                word_weight(vertex_count, word)
                == word_weight(vertex_count, root) ** exponent
            )
            contains_both = (
                set(first) <= set(root) and set(second) <= set(root)
                if family == "mutual_connector"
                else True
            )
            passed = (
                legal_closed_word(root)
                and distinct
                and weight_identity
                and word_weight(vertex_count, root) > 0
                and contains_both
            )
            line = witness_line(
                family,
                vertex_count,
                mask,
                first,
                second,
                root_canonical,
                exponent,
            )
            witness_digest.update((line + "\n").encode("utf-8"))
            if passed:
                counters["mixed_roots"] += 1
                if len(samples) < 32:
                    sample: dict[str, object] = {
                        "family": family,
                        "vertex_count": vertex_count,
                        "mask": mask,
                        "first": edge_word_text(first),
                        "second": edge_word_text(second),
                        "root": edge_word_text(root_canonical),
                        "root_exponent": exponent,
                        "root_weight": fraction_text(
                            word_weight(vertex_count, root_canonical)
                        ),
                    }
                    if extra is not None:
                        sample["outward"] = edge_word_text(extra[0])
                        sample["inward"] = edge_word_text(extra[1])
                    samples.append(sample)
            else:
                counters["failures"] += 1
                failures.append(
                    {
                        "family": family,
                        "vertex_count": vertex_count,
                        "mask": mask,
                        "reason": "mixed_root_gate",
                        "first": edge_word_text(first),
                        "second": edge_word_text(second),
                        "word": edge_word_text(word),
                        "root": edge_word_text(root_canonical),
                        "root_exponent": exponent,
                        "legal": legal_closed_word(root),
                        "distinct": distinct,
                        "weight_identity": weight_identity,
                        "positive": word_weight(vertex_count, root) > 0,
                        "contains_both": contains_both,
                    }
                )
    return counters


def exhaustive_graph_census() -> dict[str, object]:
    digest = sha256()
    samples: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    construction_counterexamples: list[dict[str, object]] = []
    rows: list[dict[str, object]] = []
    for vertex_count in (1, 2, 3, 4):
        total = 1 << (vertex_count * vertex_count)
        aggregate = {
            "graph_family": "exhaustive",
            "vertex_count": vertex_count,
            "graphs": total,
            "recurrent_sccs": 0,
            "multi_cycle_sccs": 0,
            "simple_cycles": 0,
            "shared_pairs": 0,
            "connector_pairs": 0,
            "strict_external_connector_failures": 0,
            "mixed_roots": 0,
            "failures": 0,
        }
        for mask in range(total):
            counters = graph_pair_audit(
                vertex_count,
                mask,
                edge_list(vertex_count, mask),
                digest,
                samples,
                failures,
                construction_counterexamples,
            )
            for key, value in counters.items():
                aggregate[key] = int(aggregate[key]) + value
        rows.append(aggregate)

    hash_aggregate = {
        "graph_family": "hash_seeded_control",
        "vertex_count": "5..8",
        "graphs": 64,
        "recurrent_sccs": 0,
        "multi_cycle_sccs": 0,
        "simple_cycles": 0,
        "shared_pairs": 0,
        "connector_pairs": 0,
        "strict_external_connector_failures": 0,
        "mixed_roots": 0,
        "failures": 0,
    }
    for case_index in range(64):
        vertex_count = 5 + case_index % 4
        edges = hash_graph_edges(case_index, vertex_count)
        counters = graph_pair_audit(
            vertex_count,
            edge_mask(vertex_count, edges),
            edges,
            digest,
            samples,
            failures,
            construction_counterexamples,
        )
        for key, value in counters.items():
            hash_aggregate[key] = int(hash_aggregate[key]) + value
    rows.append(hash_aggregate)
    return {
        "rows": rows,
        "samples": samples,
        "failures": failures,
        "construction_counterexamples": construction_counterexamples,
        "witness_sha256": digest.hexdigest(),
    }


def base_q_digits(value: int, alphabet_size: int) -> tuple[int, ...]:
    if value < 1 or alphabet_size < 2:
        raise ValueError("positive value and alphabet size at least two required")
    digits: list[int] = []
    remaining = value
    while remaining:
        remaining, digit = divmod(remaining, alphabet_size)
        digits.append(digit)
    return tuple(reversed(digits))


def gamma_payload(value: int, alphabet_size: int) -> tuple[int, ...]:
    digits = base_q_digits(value, alphabet_size)
    return (0,) * (len(digits) - 1) + digits


def is_prefix(left: Sequence[int], right: Sequence[int]) -> bool:
    return len(left) <= len(right) and tuple(left) == tuple(right[: len(left)])


def prefix_collision_count(words: Sequence[Sequence[int]]) -> int:
    ordered = sorted(tuple(word) for word in words)
    return sum(is_prefix(ordered[index], ordered[index + 1]) for index in range(len(ordered) - 1))


def code_clock_audit() -> dict[str, object]:
    cutoffs = (31, 127, 511, 2047)
    summary: list[dict[str, object]] = []
    ledger: list[dict[str, object]] = []
    for alphabet_size in (2, 3, 4):
        full_words = [gamma_payload(value, alphabet_size) for value in range(1, cutoffs[-1] + 1)]
        for value, payload in enumerate(full_words, start=1):
            cycle_length = len(payload) + 1
            share = Fraction(1, cycle_length)
            ledger.append(
                {
                    "alphabet_size": alphabet_size,
                    "value": value,
                    "payload": "".join(str(item) for item in payload),
                    "payload_length": len(payload),
                    "cycle_length": cycle_length,
                    "roof_share": fraction_text(share),
                    "roof_share_sum": fraction_text(share * cycle_length),
                    "powered_clock_certificate": value * value
                    < alphabet_size**cycle_length,
                }
            )
        for cutoff in cutoffs:
            words = full_words[:cutoff]
            kraft = sum(
                (Fraction(1, alphabet_size ** len(word)) for word in words),
                Fraction(0, 1),
            )
            clock_failures = sum(
                not row["powered_clock_certificate"]
                for row in ledger
                if row["alphabet_size"] == alphabet_size
                and int(row["value"]) <= cutoff
            )
            summary.append(
                {
                    "alphabet_size": alphabet_size,
                    "cutoff": cutoff,
                    "code_count": len(words),
                    "max_payload_length": max(map(len, words)),
                    "max_cycle_length": max(len(word) + 1 for word in words),
                    "kraft_sum": fraction_text(kraft),
                    "kraft_at_most_one": kraft <= 1,
                    "prefix_collisions": prefix_collision_count(words),
                    "roof_sum_failures": 0,
                    "powered_clock_failures": clock_failures,
                }
            )
    return {"summary": summary, "ledger": ledger}


def polynomial_add(left: Polynomial, right: Polynomial) -> Polynomial:
    size = max(len(left), len(right))
    output = [Fraction(0, 1) for _ in range(size)]
    for index in range(size):
        output[index] = (
            left[index] if index < len(left) else Fraction(0, 1)
        ) + (right[index] if index < len(right) else Fraction(0, 1))
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    output = [Fraction(0, 1) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def polynomial_evaluate(values: Polynomial, point: Fraction) -> Fraction:
    output = Fraction(0, 1)
    for value in reversed(values):
        output = output * point + value
    return output


def polynomial_text(values: Polynomial) -> list[str]:
    return [fraction_text(value) for value in values]


def trace_powers(
    dimension: int,
    weighted_edges: Sequence[tuple[int, int, Fraction]],
    max_power: int,
) -> list[Fraction]:
    rows: list[list[tuple[int, Fraction]]] = [[] for _ in range(dimension)]
    for left, right, weight in weighted_edges:
        rows[left].append((right, weight))
    output: list[Fraction] = []
    states: list[dict[int, Fraction]] = [{index: Fraction(1, 1)} for index in range(dimension)]
    for _ in range(max_power):
        next_states: list[dict[int, Fraction]] = []
        for distribution in states:
            following: dict[int, Fraction] = {}
            for left, value in distribution.items():
                for right, weight in rows[left]:
                    following[right] = following.get(right, Fraction(0, 1)) + value * weight
            next_states.append(following)
        states = next_states
        output.append(sum((states[index].get(index, Fraction(0, 1)) for index in range(dimension)), Fraction(0, 1)))
    return output


def determinant_from_traces(traces: Sequence[Fraction]) -> Polynomial:
    coefficients: Polynomial = [Fraction(1, 1)]
    for order in range(1, len(traces) + 1):
        total = sum(
            (coefficients[order - index] * traces[index - 1] for index in range(1, order + 1)),
            Fraction(0, 1),
        )
        coefficients.append(-total / order)
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients


def neutral_recurrent_system() -> dict[str, object]:
    node = 0
    weighted_edges: list[tuple[int, int, Fraction]] = []
    cycles: list[dict[str, object]] = []
    for value in range(2, 19):
        length = len(gamma_payload(value, 2)) + 1
        vertices = list(range(node, node + length))
        node += length
        for index, left in enumerate(vertices):
            right = vertices[(index + 1) % length]
            weight = Fraction(1, value * value) if index == length - 1 else Fraction(1, 1)
            weighted_edges.append((left, right, weight))
        cycles.append(
            {
                "value": value,
                "length": length,
                "weight": fraction_text(Fraction(1, value * value)),
                "vertices": vertices,
            }
        )
    recurrent_dimension = node
    for cycle in cycles:
        entry = int(cycle["vertices"][0])
        middle = node
        terminal = node + 1
        node += 2
        weighted_edges.append((entry, middle, Fraction(1, 2)))
        weighted_edges.append((middle, terminal, Fraction(1, 3)))
        cycle["decision_tail"] = [middle, terminal]
    traces = trace_powers(node, weighted_edges, node)
    determinant = determinant_from_traces(traces)
    recurrent_product: Polynomial = [Fraction(1, 1)]
    for cycle in cycles:
        length = int(cycle["length"])
        weight = Fraction(1, int(cycle["value"]) ** 2)
        term = [Fraction(0, 1) for _ in range(length + 1)]
        term[0] = 1
        term[length] = -weight
        recurrent_product = polynomial_multiply(recurrent_product, term)
    return {
        "dimension": node,
        "recurrent_dimension": recurrent_dimension,
        "cycles": cycles,
        "weighted_edges": [
            [left, right, fraction_text(weight)] for left, right, weight in weighted_edges
        ],
        "determinant_newton": polynomial_text(determinant),
        "recurrent_product": polynomial_text(recurrent_product),
        "terminal_extension_equal": determinant == recurrent_product,
        "nonzero_trace_orders": [index + 1 for index, value in enumerate(traces) if value],
    }


def marker_ledger() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for value in range(2, 19):
        length = len(gamma_payload(value, 2)) + 1
        weight = Fraction(1, value * value)
        raw = [Fraction(0, 1) for _ in range(length + 1)]
        raw[0] = 1
        raw[length] = -weight
        induced = [Fraction(1, 1), -weight]
        rows.append(
            {
                "value": value,
                "cycle_length": length,
                "weight": fraction_text(weight),
                "raw_polynomial": ";".join(polynomial_text(raw)),
                "induced_polynomial": ";".join(polynomial_text(induced)),
                "formal_equal": raw == induced,
                "equal_at_z_one": polynomial_evaluate(raw, Fraction(1, 1))
                == polynomial_evaluate(induced, Fraction(1, 1)),
            }
        )
    return rows
