#!/usr/bin/env python3
"""Nested-hole implementation independent of impl_formula.py."""

from __future__ import annotations

from math import lcm


def fill_value(p: int, directive: tuple[int, ...], k: int) -> int:
    """Evaluate by successive one-hole filling, without affine exponents."""
    if p < 3 or not directive:
        raise ValueError("invalid p or directive")
    residue = 0
    power = 1
    level = 0
    while True:
        next_residue = residue + power
        next_power = power * p
        if k % next_power != next_residue % next_power:
            return directive[level % len(directive)]
        residue = next_residue
        power = next_power
        level += 1


def center_by_recurrence(p: int, n: int) -> int:
    residue = 0
    power = 1
    for _ in range(n):
        residue += power
        power *= p
    return residue


def _least_period(word: tuple[int, ...]) -> int:
    for d in range(1, len(word) + 1):
        if len(word) % d == 0:
            good = True
            for i, letter in enumerate(word):
                if letter != word[i % d]:
                    good = False
                    break
            if good:
                return d
    raise AssertionError("unreachable")


def _canonical(word: tuple[int, ...]) -> tuple[int, ...]:
    labels: dict[int, int] = {}
    result: list[int] = []
    for letter in word:
        if letter not in labels:
            labels[letter] = len(labels)
        result.append(labels[letter])
    return tuple(result)


def enumerate_directives(max_period: int, max_alphabet: int) -> list[tuple[int, ...]]:
    """Recursive restricted-growth enumeration."""
    found: list[tuple[int, ...]] = []

    def extend(prefix: list[int], target_length: int) -> None:
        if len(prefix) == target_length:
            word = tuple(prefix)
            if max(word) + 1 < 2 or max(word) + 1 > max_alphabet:
                return
            if _least_period(word) != target_length:
                return
            if any(word[i] == word[(i + 1) % target_length] for i in range(target_length)):
                return
            found.append(word)
            return
        upper = min(max(prefix) + 1, max_alphabet - 1)
        for label in range(upper + 1):
            prefix.append(label)
            extend(prefix, target_length)
            prefix.pop()

    for length in range(2, max_period + 1):
        extend([0], length)
    return sorted(set(found), key=lambda w: (len(w), max(w) + 1, w))


def enumerate_partitions(n: int) -> list[tuple[int, ...]]:
    partitions: list[tuple[int, ...]] = []

    def place(item: int, blocks: list[list[int]]) -> None:
        if item == n:
            labels = [0] * n
            for label, block in enumerate(blocks):
                for vertex in block:
                    labels[vertex] = label
            partitions.append(tuple(labels))
            return
        for block in blocks:
            block.append(item)
            place(item + 1, blocks)
            block.pop()
        blocks.append([item])
        place(item + 1, blocks)
        blocks.pop()

    place(1, [[0]])
    return sorted(set(partitions), key=lambda r: (max(r) + 1, r))


def _admissible(directive: tuple[int, ...], partition: tuple[int, ...]) -> bool:
    for i, letter in enumerate(directive):
        if partition[letter] == partition[directive[(i + 1) % len(directive)]]:
            return False
    return True


def graphical_stirling_counts(directive: tuple[int, ...]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for partition in enumerate_partitions(max(directive) + 1):
        if _admissible(directive, partition):
            blocks = max(partition) + 1
            counts[blocks] = counts.get(blocks, 0) + 1
    return dict(sorted(counts.items()))


def proper_coloring_count(directive: tuple[int, ...], colors: int) -> int:
    """Count labeled proper colorings by recursive vertex assignment."""
    if colors < 0:
        raise ValueError("colors must be nonnegative")
    vertices = max(directive) + 1
    assigned = [-1] * vertices
    total = 0

    def extend(vertex: int) -> None:
        nonlocal total
        if vertex == vertices:
            for i, letter in enumerate(directive):
                if assigned[letter] == assigned[directive[(i + 1) % len(directive)]]:
                    return
            total += 1
            return
        for color in range(colors):
            assigned[vertex] = color
            extend(vertex + 1)
        assigned[vertex] = -1

    extend(0)
    return total


def skeleton_sample(p: int, directive: tuple[int, ...], n: int) -> dict:
    modulus = p**n
    hole = center_by_recurrence(p, n)
    periodic = 0
    comparisons = 0
    for residue in range(modulus):
        values = {fill_value(p, directive, residue + t * modulus) for t in range(-3, 4)}
        if residue == hole:
            # A targeted later-stage shift supplies the second adjacent letter.
            witness = center_by_recurrence(p, n + 1)
            values.add(fill_value(p, directive, witness))
            if len(values) < 2:
                raise AssertionError("sampled hole did not vary")
        else:
            if len(values) != 1:
                raise AssertionError("sampled periodic residue varied")
            periodic += 1
        comparisons += 7
    return {
        "N": n,
        "hole_residue": hole,
        "modulus": modulus,
        "periodic_residue_count": periodic,
        "sample_comparisons": comparisons,
    }


def _positions(p: int, dense_radius: int, center_depth: int) -> list[int]:
    points = set(range(-dense_radius, dense_radius + 1))
    for n in range(center_depth + 1):
        points.add(center_by_recurrence(p, n))
    return sorted(points)


def local_constraint(
    p: int,
    source: tuple[int, ...],
    target: tuple[int, ...],
    radius: int,
    dense_radius: int,
    center_depth: int,
) -> dict:
    rule: dict[tuple[int, ...], int] = {}
    consistent = True
    for k in _positions(p, dense_radius, center_depth):
        window = []
        for offset in range(-radius, radius + 1):
            window.append(fill_value(p, source, k + offset))
        key = tuple(window)
        output = fill_value(p, target, k)
        previous = rule.get(key)
        if previous is not None and previous != output:
            consistent = False
            break
        rule[key] = output

    mapping: dict[int, int] = {}
    quotient = True
    horizon = lcm(len(source), len(target))
    for n in range(horizon):
        source_letter = source[n % len(source)]
        target_letter = target[n % len(target)]
        if source_letter in mapping and mapping[source_letter] != target_letter:
            quotient = False
            break
        mapping[source_letter] = target_letter
    if quotient:
        if set(mapping.keys()) != set(source) or set(mapping.values()) != set(target):
            quotient = False
        else:
            for n in range(horizon):
                if mapping[source[n % len(source)]] != target[n % len(target)]:
                    quotient = False
                    break
    return {
        "consistent": consistent,
        "is_surjective_letter_quotient": quotient,
        "observed_window_count": len(rule),
    }
