#!/usr/bin/env python3
"""Exact cycle-quotient core for Paper 33 / SD-C35.

This module contains no arithmetic classification.  It constructs the same
projective-residue actions as Paper 32, their presentation-relation quotient,
the cross-modulus square complex, and generic presentation-action controls.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from math import gcd
from random import Random
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple


Point = Tuple[int, int]
SparseVector = Dict[int, int]


@dataclass(frozen=True)
class Action:
    modulus: int
    points: Tuple[Point, ...]
    s_image: Tuple[int, ...]
    r_image: Tuple[int, ...]

    @property
    def size(self) -> int:
        return len(self.points)


def units_mod(n: int) -> Tuple[int, ...]:
    if n < 2:
        raise ValueError("modulus must be at least two")
    return tuple(a for a in range(n) if gcd(a, n) == 1)


def canonical_point(n: int, point: Point, units: Sequence[int]) -> Point:
    a, b = point
    return min((u * a % n, u * b % n) for u in units)


def projective_line(n: int) -> Tuple[Point, ...]:
    units = units_mod(n)
    seen = set()
    points: List[Point] = []
    for a in range(n):
        for b in range(n):
            if (a, b) in seen or gcd(gcd(a, b), n) != 1:
                continue
            orbit = {(u * a % n, u * b % n) for u in units}
            seen.update(orbit)
            points.append(min(orbit))
    return tuple(sorted(points))


def build_action(n: int) -> Action:
    points = projective_line(n)
    index = {point: i for i, point in enumerate(points)}
    units = units_mod(n)
    s_image = []
    r_image = []
    for a, b in points:
        s_image.append(index[canonical_point(n, ((-b) % n, a), units)])
        r_image.append(index[canonical_point(n, ((-b) % n, (a + b) % n), units)])
    action = Action(n, points, tuple(s_image), tuple(r_image))
    validate_action(action.s_image, action.r_image)
    return action


def compose(mapping: Sequence[int], power: int) -> Tuple[int, ...]:
    out = tuple(range(len(mapping)))
    for _ in range(power):
        out = tuple(mapping[i] for i in out)
    return out


def validate_action(s_image: Sequence[int], r_image: Sequence[int]) -> None:
    if len(s_image) != len(r_image) or not s_image:
        raise AssertionError("action maps must have one common nonempty state set")
    identity = tuple(range(len(s_image)))
    if tuple(sorted(s_image)) != identity or tuple(sorted(r_image)) != identity:
        raise AssertionError("action maps must be permutations")
    if compose(s_image, 2) != identity:
        raise AssertionError("the first generator does not square to the identity")
    if compose(r_image, 3) != identity:
        raise AssertionError("the second generator does not cube to the identity")


def permutation_orbits(mapping: Sequence[int]) -> Tuple[Tuple[int, ...], ...]:
    seen = set()
    orbits: List[Tuple[int, ...]] = []
    for start in range(len(mapping)):
        if start in seen:
            continue
        orbit = []
        cur = start
        while cur not in seen:
            seen.add(cur)
            orbit.append(cur)
            cur = mapping[cur]
        orbits.append(tuple(orbit))
    return tuple(orbits)


def component_count(s_image: Sequence[int], r_image: Sequence[int]) -> int:
    unseen = set(range(len(s_image)))
    components = 0
    s_inv = [0] * len(s_image)
    r_inv = [0] * len(r_image)
    for i, j in enumerate(s_image):
        s_inv[j] = i
    for i, j in enumerate(r_image):
        r_inv[j] = i
    while unseen:
        components += 1
        start = next(iter(unseen))
        unseen.remove(start)
        queue = deque([start])
        while queue:
            x = queue.popleft()
            for y in (s_image[x], r_image[x], s_inv[x], r_inv[x]):
                if y in unseen:
                    unseen.remove(y)
                    queue.append(y)
    return components


def relation_quotient_dimension(s_image: Sequence[int], r_image: Sequence[int]) -> int:
    """Dimension over characteristic zero of the S^2/R^3 relation quotient.

    For each connected component this is the cycle rank of the bipartite
    incidence graph whose vertices are S-orbits and R-orbits and whose edges
    are action states.
    """

    states = len(s_image)
    components = component_count(s_image, r_image)
    return states + components - len(permutation_orbits(s_image)) - len(permutation_orbits(r_image))


def cusp_index(action: Action) -> int:
    units = units_mod(action.modulus)
    cusp = canonical_point(action.modulus, (1, 0), units)
    return action.points.index(cusp)


def cusp_rs_witness(action: Action) -> Tuple[int, int, int]:
    """Return cusp -> R(cusp) -> S(R(cusp)) indices."""

    c = cusp_index(action)
    middle = action.r_image[c]
    end = action.s_image[middle]
    return c, middle, end


def divisors(n: int) -> Tuple[int, ...]:
    small: List[int] = []
    large: List[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return tuple(small + list(reversed(large)))


def euler_phi(n: int) -> int:
    return sum(1 for a in range(1, n + 1) if gcd(a, n) == 1)


def cusp_count_gamma0(n: int) -> int:
    return sum(euler_phi(gcd(d, n // d)) for d in divisors(n))


def relation_vectors(s_image: Sequence[int], r_image: Sequence[int]) -> Tuple[SparseVector, ...]:
    vectors: List[SparseVector] = []
    for orbit in permutation_orbits(s_image):
        vectors.append({i: 1 for i in orbit})
    for orbit in permutation_orbits(r_image):
        vectors.append({i: 1 for i in orbit})
    return tuple(vectors)


def adjacency_image(vector: Mapping[int, int], s_image: Sequence[int], r_image: Sequence[int], prime: int) -> SparseVector:
    out: SparseVector = {}
    for i, coefficient in vector.items():
        for target in (s_image[i], r_image[i]):
            out[target] = (out.get(target, 0) + coefficient) % prime
            if out[target] == 0:
                del out[target]
    return out


def sparse_rank(vectors: Iterable[Mapping[int, int]], prime: int) -> int:
    pivots: Dict[int, SparseVector] = {}
    for original in vectors:
        vector = {i: value % prime for i, value in original.items() if value % prime}
        while vector:
            pivot = min(vector)
            if pivot not in pivots:
                inverse = pow(vector[pivot], prime - 2, prime)
                vector = {i: value * inverse % prime for i, value in vector.items()}
                pivots[pivot] = vector
                break
            factor = vector[pivot]
            basis = pivots[pivot]
            for i, value in basis.items():
                updated = (vector.get(i, 0) - factor * value) % prime
                if updated:
                    vector[i] = updated
                elif i in vector:
                    del vector[i]
    return len(pivots)


def adjacency_descent_certificate(action: Action, prime: int = 1_000_003) -> Tuple[int, int]:
    relations = relation_vectors(action.s_image, action.r_image)
    images = tuple(adjacency_image(v, action.s_image, action.r_image, prime) for v in relations)
    return sparse_rank(relations, prime), sparse_rank(relations + images, prime)


def relabel_action(action: Action, seed: int) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    rng = Random(seed)
    permutation = list(range(action.size))
    rng.shuffle(permutation)
    inverse = [0] * action.size
    for old, new in enumerate(permutation):
        inverse[new] = old
    s_new = [0] * action.size
    r_new = [0] * action.size
    for new in range(action.size):
        old = inverse[new]
        s_new[new] = permutation[action.s_image[old]]
        r_new[new] = permutation[action.r_image[old]]
    return tuple(s_new), tuple(r_new)


def random_involution(size: int, rng: Random) -> Tuple[int, ...]:
    items = list(range(size))
    rng.shuffle(items)
    mapping = list(range(size))
    while len(items) >= 2:
        if rng.randrange(5) == 0:
            items.pop()
            continue
        a = items.pop()
        b = items.pop()
        mapping[a] = b
        mapping[b] = a
    return tuple(mapping)


def random_order_three(size: int, rng: Random) -> Tuple[int, ...]:
    items = list(range(size))
    rng.shuffle(items)
    mapping = list(range(size))
    while len(items) >= 3:
        if rng.randrange(6) == 0:
            items.pop()
            continue
        a = items.pop()
        b = items.pop()
        c = items.pop()
        mapping[a] = b
        mapping[b] = c
        mapping[c] = a
    return tuple(mapping)


def random_transitive_action(size: int, seed: int) -> Tuple[Tuple[int, ...], Tuple[int, ...], int]:
    rng = Random(seed)
    for attempt in range(1, 20_001):
        s_image = random_involution(size, rng)
        r_image = random_order_three(size, rng)
        if component_count(s_image, r_image) == 1:
            validate_action(s_image, r_image)
            return s_image, r_image, attempt
    raise RuntimeError("failed to sample a transitive presentation action")


def cross_square_complex(cutoff: int, prime: int = 1_000_003) -> Dict[str, object]:
    nodes = tuple(range(2, cutoff + 1))
    edges = tuple(sorted((n, k * n) for n in nodes for k in (2, 3) if k * n <= cutoff))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    squares = tuple((n, 2 * n, 6 * n, 3 * n) for n in nodes if 6 * n <= cutoff)

    adjacency = {n: set() for n in nodes}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen = set(nodes)
    components = 0
    while unseen:
        components += 1
        start = unseen.pop()
        queue = deque([start])
        while queue:
            x = queue.popleft()
            for y in adjacency[x]:
                if y in unseen:
                    unseen.remove(y)
                    queue.append(y)

    boundaries: List[SparseVector] = []
    for n, n2, n6, n3 in squares:
        directed = ((n, n2, 1), (n2, n6, 1), (n3, n6, -1), (n, n3, -1))
        vector: SparseVector = {}
        for a, b, sign in directed:
            vector[edge_index[(a, b)]] = sign % prime
        boundaries.append(vector)

    graph_betti = len(edges) - len(nodes) + components
    square_rank = sparse_rank(boundaries, prime)
    return {
        "cutoff": cutoff,
        "nodes": len(nodes),
        "edges": len(edges),
        "components": components,
        "diamonds": len(squares),
        "graph_betti_before_filling": graph_betti,
        "diamond_boundary_rank": square_rank,
        "homology_after_filling": graph_betti - square_rank,
        "component_invariant": "remove_all_factors_2_and_3",
    }
