#!/usr/bin/env python3
"""Projective-residue grammar used by the Paper 32 prototype.

The only arithmetic input is the finite residue ring Z/nZ and the two fixed
modular transformations S and R.  Classification lives in a separate
evaluator module.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from math import gcd
from typing import Dict, Iterable, List, Sequence, Tuple


Point = Tuple[int, int]


@dataclass(frozen=True)
class ResidueGrammar:
    modulus: int
    points: Tuple[Point, ...]
    s_image: Tuple[int, ...]
    r_image: Tuple[int, ...]

    @property
    def size(self) -> int:
        return len(self.points)


def units_mod(n: int) -> Tuple[int, ...]:
    if n < 2:
        raise ValueError("the frozen grammar starts at modulus 2")
    return tuple(u for u in range(n) if gcd(u, n) == 1)


def projective_line_zn(n: int) -> Tuple[Point, ...]:
    """Return canonical unit-scaling orbits of unimodular residue pairs."""

    units = units_mod(n)
    seen: Dict[Point, Point] = {}
    representatives: List[Point] = []
    for a in range(n):
        for b in range(n):
            pair = (a, b)
            if pair in seen or gcd(gcd(a, b), n) != 1:
                continue
            orbit = {(u * a % n, u * b % n) for u in units}
            representative = min(orbit)
            for member in orbit:
                seen[member] = representative
            representatives.append(representative)
    return tuple(sorted(representatives))


def canonical_point(n: int, point: Point, units: Sequence[int]) -> Point:
    a, b = point
    return min((u * a % n, u * b % n) for u in units)


def build_grammar(n: int) -> ResidueGrammar:
    """Build the S,R Schreier grammar on P^1(Z/nZ).

    S[a:b]=[-b:a] and R[a:b]=[-b:a+b].  Projectively S^2=R^3=1.
    """

    points = projective_line_zn(n)
    index = {point: i for i, point in enumerate(points)}
    units = units_mod(n)
    s_image: List[int] = []
    r_image: List[int] = []
    for a, b in points:
        s_point = canonical_point(n, ((-b) % n, a), units)
        r_point = canonical_point(n, ((-b) % n, (a + b) % n), units)
        s_image.append(index[s_point])
        r_image.append(index[r_point])
    return ResidueGrammar(n, points, tuple(s_image), tuple(r_image))


def compose(mapping: Sequence[int], power: int) -> Tuple[int, ...]:
    out = tuple(range(len(mapping)))
    for _ in range(power):
        out = tuple(mapping[i] for i in out)
    return out


def permutation_cycle_lengths(mapping: Sequence[int]) -> Tuple[int, ...]:
    seen = [False] * len(mapping)
    lengths: List[int] = []
    for start in range(len(mapping)):
        if seen[start]:
            continue
        cur = start
        length = 0
        while not seen[cur]:
            seen[cur] = True
            length += 1
            cur = mapping[cur]
        lengths.append(length)
    return tuple(sorted(lengths))


def forward_component_size(grammar: ResidueGrammar, start: int = 0) -> int:
    seen = {start}
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for image_vertex in (grammar.s_image[vertex], grammar.r_image[vertex]):
            if image_vertex not in seen:
                seen.add(image_vertex)
                queue.append(image_vertex)
    return len(seen)


def trace_word_count(grammar: ResidueGrammar, length: int) -> int:
    """Trace of (P_S+P_R)^length by exact labelled-word enumeration."""

    if length < 1:
        raise ValueError("length must be positive")
    total = 0
    for start in range(grammar.size):
        counts = {start: 1}
        for _ in range(length):
            next_counts: Dict[int, int] = {}
            for vertex, multiplicity in counts.items():
                for image_vertex in (grammar.s_image[vertex], grammar.r_image[vertex]):
                    next_counts[image_vertex] = next_counts.get(image_vertex, 0) + multiplicity
            counts = next_counts
        total += counts.get(start, 0)
    return total


def cusp_index(grammar: ResidueGrammar) -> int:
    """Index of the source-natural projective cusp [1:0]."""

    units = units_mod(grammar.modulus)
    representative = canonical_point(grammar.modulus, (1, 0), units)
    return grammar.points.index(representative)


def canonical_diamonds(cutoff: int) -> Tuple[Tuple[int, int, int, int], ...]:
    """The nonbacktracking cross-modulus diamonds n,2n,6n,3n."""

    if cutoff < 2:
        return ()
    return tuple((n, 2 * n, 6 * n, 3 * n) for n in range(2, cutoff // 6 + 1))


def cross_edge_weight_bases(n: int) -> Tuple[int, int, int, int]:
    """Bases whose -s powers multiply along n->2n->6n->3n->n."""

    return (2 * n, 6 * n, 6 * n, 3 * n)


def validate_grammar(grammar: ResidueGrammar) -> None:
    identity = tuple(range(grammar.size))
    if compose(grammar.s_image, 2) != identity:
        raise AssertionError("S^2 is not projectively the identity")
    if compose(grammar.r_image, 3) != identity:
        raise AssertionError("R^3 is not projectively the identity")
    if sorted(grammar.s_image) != list(identity):
        raise AssertionError("S is not a permutation")
    if sorted(grammar.r_image) != list(identity):
        raise AssertionError("R is not a permutation")


def census_row(grammar: ResidueGrammar, trace_order: int) -> Dict[str, int]:
    validate_grammar(grammar)
    s_lengths = permutation_cycle_lengths(grammar.s_image)
    r_lengths = permutation_cycle_lengths(grammar.r_image)
    row: Dict[str, int] = {
        "modulus": grammar.modulus,
        "state_count": grammar.size,
        "projective_defect": grammar.size - grammar.modulus - 1,
        "s_cycle_count": len(s_lengths),
        "s_fixed_count": s_lengths.count(1),
        "s_two_cycle_count": s_lengths.count(2),
        "r_cycle_count": len(r_lengths),
        "r_fixed_count": r_lengths.count(1),
        "r_three_cycle_count": r_lengths.count(3),
        "forward_component_size": forward_component_size(grammar),
        "overlap_state_count": grammar.size,
    }
    for order in range(1, trace_order + 1):
        row[f"trace_{order}"] = trace_word_count(grammar, order)
    return row
