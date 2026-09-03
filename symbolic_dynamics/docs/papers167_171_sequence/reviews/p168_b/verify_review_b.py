#!/usr/bin/env python3
"""Reviewer-owned exact control for P168 Hostile Review B.

This implementation imports no author, scouting, or Review-A code.  It uses
the projective points of F_(p^4) as its carrier: a projective point is an
exponent modulo (p^4-1)/(p-1), planes are deduplicated point sets generated
by pairs of projective points, and hyperplanes are built independently as
trace kernels.  Field powers come from a primitive companion transformation,
not quotient-ring multiplication.  Thus neither the author's packed/RREF
templates nor Review A's coefficient-tuple/subspace-BFS engine is reused.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict, deque
from pathlib import Path


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)

    def equal(self, left, right, label: str) -> None:
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")


A = Audit()
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


def echelon_basis(vectors, p: int):
    rows = [list(v) for v in vectors if v != ZERO]
    rank = 0
    for column in range(4):
        pivot = next(
            (i for i in range(rank, len(rows)) if rows[i][column] % p),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = pow(rows[rank][column], -1, p)
        rows[rank] = [(scale * x) % p for x in rows[rank]]
        for i in range(len(rows)):
            if i == rank:
                continue
            coefficient = rows[i][column] % p
            if coefficient:
                rows[i] = [
                    (x - coefficient * y) % p
                    for x, y in zip(rows[i], rows[rank])
                ]
        rank += 1
        if rank == len(rows) or rank == 4:
            break
    return tuple(tuple(row) for row in rows[:rank])


class ProjectiveQuartic:
    """F_(p^4) from a full-cycle companion linear transformation."""

    def __init__(self, p: int):
        self.p = p
        self.order = p**4
        self.group_order = self.order - 1
        self.line_count = self.group_order // (p - 1)
        self.coefficients, self.powers = self._primitive_companion()
        self.logs = {vector: exponent for exponent, vector in enumerate(self.powers)}
        A.equal(len(self.logs), self.group_order, f"p={p} primitive orbit size")
        A.check(ZERO not in self.logs, f"p={p} primitive orbit excludes zero")
        A.equal(self._alpha_step(self.powers[-1], self.coefficients), ONE,
                f"p={p} primitive orbit closes")
        self.full = frozenset(range(self.line_count))

        # Powers spaced by L are exactly the nonzero base-field scalars.
        scalar_vectors = {
            self.powers[j * self.line_count] for j in range(p - 1)
        }
        A.equal(scalar_vectors, {(c, 0, 0, 0) for c in range(1, p)},
                f"p={p} scalar subgroup")
        for exponent in range(self.group_order):
            inverse = self.powers[-exponent % self.group_order]
            A.equal(self.multiply(self.powers[exponent], inverse), ONE,
                    f"p={p} exponent inverse {exponent}")

    def _alpha_step(self, vector, coefficients):
        p = self.p
        c0, c1, c2, c3 = coefficients
        a0, a1, a2, a3 = vector
        return (
            (-c0 * a3) % p,
            (a0 - c1 * a3) % p,
            (a1 - c2 * a3) % p,
            (a2 - c3 * a3) % p,
        )

    def _primitive_companion(self):
        p = self.p
        target = p**4 - 1
        for c0 in range(1, p):
            for c1, c2, c3 in itertools.product(range(p), repeat=3):
                coefficients = (c0, c1, c2, c3)
                vector = ONE
                powers = []
                seen = set()
                for _ in range(target):
                    if vector == ZERO or vector in seen:
                        break
                    powers.append(vector)
                    seen.add(vector)
                    vector = self._alpha_step(vector, coefficients)
                if len(powers) == target and vector == ONE:
                    return coefficients, tuple(powers)
        raise AssertionError(f"no primitive quartic companion for p={p}")

    def add(self, left, right):
        return tuple((x + y) % self.p for x, y in zip(left, right))

    def subtract(self, left, right):
        return tuple((x - y) % self.p for x, y in zip(left, right))

    def scale(self, coefficient: int, vector):
        return tuple(coefficient * x % self.p for x in vector)

    def multiply(self, left, right):
        if left == ZERO or right == ZERO:
            return ZERO
        exponent = (self.logs[left] + self.logs[right]) % self.group_order
        return self.powers[exponent]

    def inverse(self, vector):
        A.check(vector != ZERO, "zero inverse requested")
        return self.powers[-self.logs[vector] % self.group_order]

    def representative(self, line: int):
        return self.powers[line % self.line_count]

    def line_of(self, vector):
        A.check(vector != ZERO, "zero has no projective point")
        return self.logs[vector] % self.line_count

    def span(self, lines):
        basis = echelon_basis((self.representative(line) for line in lines), self.p)
        dimension = len(basis)
        if dimension == 0:
            return frozenset()
        if dimension == 4:
            return self.full
        points = set()
        for coefficients in itertools.product(range(self.p), repeat=dimension):
            vector = ZERO
            for coefficient, row in zip(coefficients, basis):
                vector = self.add(vector, self.scale(coefficient, row))
            if vector != ZERO:
                points.add(self.line_of(vector))
        expected = (self.p**dimension - 1) // (self.p - 1)
        A.equal(len(points), expected,
                f"p={self.p} projective span size in dimension {dimension}")
        return frozenset(points)

    def plane_from_pair(self, first: int, second: int):
        A.check(first != second, "distinct projective pair")
        u = self.representative(first)
        v = self.representative(second)
        points = {second}
        for coefficient in range(self.p):
            points.add(self.line_of(self.add(u, self.scale(coefficient, v))))
        A.equal(len(points), self.p + 1, f"p={self.p} pair spans plane")
        return frozenset(points)

    def trace_of_exponent(self, exponent: int):
        total = ZERO
        for power in range(4):
            total = self.add(
                total,
                self.powers[(exponent * self.p**power) % self.group_order],
            )
        A.check(total[1:] == (0, 0, 0), f"p={self.p} trace lands in base field")
        return total

    def trace_hyperplanes(self):
        hyperplanes = []
        expected_points = self.p**2 + self.p + 1
        for coefficient_line in range(self.line_count):
            kernel = frozenset(
                point
                for point in range(self.line_count)
                if self.trace_of_exponent(coefficient_line + point) == ZERO
            )
            A.equal(len(kernel), expected_points,
                    f"p={self.p} trace-kernel point count")
            hyperplanes.append(kernel)
        A.equal(len(set(hyperplanes)), self.line_count,
                f"p={self.p} nondegenerate trace hyperplanes")
        return tuple(hyperplanes)

    def inverse_span(self, space):
        if not space:
            return frozenset()
        inverse_points = {
            (-point) % self.line_count for point in space
        }
        return self.span(inverse_points)

    def shift(self, space, exponent: int):
        return frozenset(
            (point + exponent) % self.line_count for point in space
        )

    def dimension(self, space):
        sizes = {
            0: 0,
            1: 1,
            self.p + 1: 2,
            self.p**2 + self.p + 1: 3,
            self.line_count: 4,
        }
        A.check(len(space) in sizes, f"p={self.p} valid projective subspace size")
        return sizes[len(space)]


def canonical_spaces(field: ProjectiveQuartic):
    lines = tuple(frozenset((point,)) for point in range(field.line_count))
    planes = {
        field.plane_from_pair(first, second)
        for first, second in itertools.combinations(range(field.line_count), 2)
    }
    hyperplanes = set(field.trace_hyperplanes())
    spaces = (
        (frozenset(),)
        + lines
        + tuple(sorted(planes, key=lambda x: tuple(sorted(x))))
        + tuple(sorted(hyperplanes, key=lambda x: tuple(sorted(x))))
        + (field.full,)
    )
    A.equal(len(spaces), len(set(spaces)), f"p={field.p} unique projective spaces")
    return spaces, planes, hyperplanes


def orbit_profile(edges):
    tails = []
    periods = []
    cycles = set()
    for start in range(len(edges)):
        seen = {}
        path = []
        current = start
        while current not in seen:
            seen[current] = len(path)
            path.append(current)
            current = edges[current]
        entrance = seen[current]
        cycle = path[entrance:]
        rotations = [tuple(cycle[i:] + cycle[:i]) for i in range(len(cycle))]
        cycles.add(min(rotations))
        tails.append(entrance)
        periods.append(len(cycle))
    return tails, periods, cycles


def weak_components(edges):
    neighbours = [set((edges[i],)) for i in range(len(edges))]
    for source, target in enumerate(edges):
        neighbours[target].add(source)
    unseen = set(range(len(edges)))
    components = []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        component = {seed}
        queue = deque((seed,))
        while queue:
            current = queue.popleft()
            for neighbour in neighbours[current]:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    component.add(neighbour)
                    queue.append(neighbour)
        components.append(frozenset(component))
    return tuple(components)


def expected_fibre(p, dimension, recurrent, full, time, L, P, Q):
    if recurrent and not full:
        return 1
    if p == 2 and time == 1 and dimension == 3:
        return 2
    if full and p == 2 and time == 1:
        return 1 + L
    if full and p == 2 and time >= 2:
        return 1 + L + P - Q
    if full and p > 2:
        return 1 + L + P - Q
    return 0


def state_text(space):
    return ",".join(map(str, sorted(space)))


def verify_full_graph(p: int):
    before = A.assertions
    field = ProjectiveQuartic(p)
    spaces, planes, hyperplanes = canonical_spaces(field)
    index = {space: i for i, space in enumerate(spaces)}

    L = p**3 + p**2 + p + 1
    P = (p**2 + 1) * (p**2 + p + 1)
    Q = p**2 + 1
    S = 2 + 2 * L + P
    R = 2 + L + Q
    F = 2 + math.gcd(2, L) + math.gcd(2, Q)
    A.equal(F, 4 if p == 2 else 6, f"p={p} quotient-inversion fixed formula")
    A.equal(P - Q, p * L, f"p={p} transient-plane mass identity")
    A.equal(field.line_count, L, f"p={p} line constant")
    A.equal(len(planes), P, f"p={p} plane count")
    A.equal(len(hyperplanes), L, f"p={p} hyperplane count")
    A.equal(len(spaces), S, f"p={p} Gaussian total")
    A.equal(
        Counter(field.dimension(space) for space in spaces),
        Counter({0: 1, 1: L, 2: P, 3: L, 4: 1}),
        f"p={p} dimension census",
    )

    subgroup_step = Q
    subfield_planes = {
        frozenset((offset + j * subgroup_step) % L for j in range(p + 1))
        for offset in range(Q)
    }
    A.equal(len(subfield_planes), Q, f"p={p} scalar quadratic planes")
    for plane in subfield_planes:
        A.check(plane in planes, f"p={p} scalar subfield is plane")

    recurrent_expected = (
        {frozenset(), field.full}
        | {frozenset((point,)) for point in range(L)}
        | subfield_planes
    )
    A.equal(len(recurrent_expected), R, f"p={p} expected recurrent count")

    edge_spaces = []
    for space in spaces:
        target = field.inverse_span(space)
        A.check(target in index, f"p={p} image in projective lattice")
        source_dimension = field.dimension(space)
        target_dimension = field.dimension(target)
        A.check(target_dimension >= source_dimension, f"p={p} rank monotonicity")
        equality = target_dimension == source_dimension
        A.equal(equality, space in recurrent_expected, f"p={p} equality classification")
        if equality:
            A.equal(field.inverse_span(target), space, f"p={p} equality gives J2")
        edge_spaces.append(target)
    edges = tuple(index[target] for target in edge_spaces)

    # Direct transition attack on every carrier stratum.
    for point in range(L):
        source = frozenset((point,))
        A.equal(edge_spaces[index[source]], frozenset(((-point) % L,)),
                f"p={p} line quotient inversion")
    for plane in planes:
        image_dimension = field.dimension(edge_spaces[index[plane]])
        if plane in subfield_planes:
            A.equal(image_dimension, 2, f"p={p} subfield-plane equality")
        elif p == 2:
            A.equal(image_dimension, 3, "binary non-subfield plane rank jump")
        else:
            A.equal(image_dimension, 4, f"p={p} odd plane fills field")
    for hyperplane in hyperplanes:
        A.equal(edge_spaces[index[hyperplane]], field.full,
                f"p={p} every hyperplane fills field")
    A.equal(edge_spaces[index[frozenset()]], frozenset(), f"p={p} zero fixed")
    A.equal(edge_spaces[index[field.full]], field.full, f"p={p} full field fixed")

    tails, periods, cycles = orbit_profile(edges)
    recurrent_indices = {i for i, tail in enumerate(tails) if tail == 0}
    A.equal({spaces[i] for i in recurrent_indices}, recurrent_expected,
            f"p={p} actual recurrent classification")
    for state_index, space in enumerate(spaces):
        equality = field.dimension(edge_spaces[state_index]) == field.dimension(space)
        A.equal(equality, tails[state_index] == 0,
                f"p={p} equality iff recurrence")
    A.check(set(periods) <= {1, 2}, f"p={p} periods divide two")
    expected_depth = (
        Counter({0: R, 1: L, 2: P - Q})
        if p == 2
        else Counter({0: R, 1: S - R})
    )
    A.equal(Counter(tails), expected_depth, f"p={p} sharp depth enumerator")
    A.equal(max(tails), 2 if p == 2 else 1, f"p={p} sharp maximum tail")

    fixed = {i for i, target in enumerate(edges) if i == target}
    A.equal(len(fixed), F, f"p={p} fixed-state count")
    A.equal(Counter(len(cycle) for cycle in cycles),
            Counter({1: F, 2: (R - F) // 2}),
            f"p={p} fixed/two-cycle census")
    for time in range(1, 9):
        iterate = list(range(S))
        for _ in range(time):
            iterate = [edges[current] for current in iterate]
        fixed_iterate = sum(i == iterate[i] for i in range(S))
        A.equal(fixed_iterate, F if time % 2 else R,
                f"p={p} fixed iterate time {time}")

    # Generator equivariance implies the full twisted scalar law.
    for space, target in zip(spaces, edge_spaces):
        shifted_source = field.shift(space, 1)
        A.check(shifted_source in index, f"p={p} scalar action closes carrier")
        A.equal(edge_spaces[index[shifted_source]], field.shift(target, -1),
                f"p={p} twisted scalar generator")
    seed_hyperplane = min(hyperplanes, key=lambda x: tuple(sorted(x)))
    scalar_hyperplane_orbit = {field.shift(seed_hyperplane, shift) for shift in range(L)}
    A.equal(scalar_hyperplane_orbit, hyperplanes,
            f"p={p} scalar transitivity on trace hyperplanes")

    # Every-target fibres, with stabilization of the complete count table.
    current = list(range(S))
    fibre_tables = []
    images = []
    full_fibres = []
    for time in range(1, 7):
        current = [edges[source] for source in current]
        fibres = Counter(current)
        fibre_tables.append(fibres)
        images.append(len(fibres))
        full_fibres.append(fibres[index[field.full]])
        for target_index, target in enumerate(spaces):
            expected = expected_fibre(
                p,
                field.dimension(target),
                target in recurrent_expected,
                target == field.full,
                time,
                L,
                P,
                Q,
            )
            A.equal(fibres[target_index], expected,
                    f"p={p} every-target fibre t={time}")
    expected_images = [R + L] + [R] * 5 if p == 2 else [R] * 6
    A.equal(images, expected_images, f"p={p} image stabilization")
    stable_start = 1 if p == 2 else 0
    for table in fibre_tables[stable_start + 1:]:
        A.equal(table, fibre_tables[stable_start], f"p={p} all-time fibre stabilization")

    predecessors = defaultdict(list)
    for source, target in enumerate(edges):
        predecessors[target].append(source)
    if p == 2:
        non_subfield = planes - subfield_planes
        binary_sizes = []
        for hyperplane in hyperplanes:
            sources = {spaces[source] for source in predecessors[index[hyperplane]]}
            A.equal(len(sources), 2, "binary hyperplane has two plane sources")
            A.check(sources <= non_subfield, "binary hyperplane sources are transient planes")
            binary_sizes.append(len(sources))
        A.equal(Counter(binary_sizes), Counter({2: L}),
                "binary 30 planes split two-to-one over 15 hyperplanes")

    components = weak_components(edges)
    A.equal(len(components), (R + F) // 2, f"p={p} component count")
    full_component = next(component for component in components if index[field.full] in component)
    A.equal(len(full_component), 1 + L + P - Q, f"p={p} full-field basin size")
    for state_index, space in enumerate(spaces):
        if space in recurrent_expected or space == field.full:
            continue
        terminal = state_index
        for _ in range(3):
            terminal = edges[terminal]
        A.equal(terminal, index[field.full], f"p={p} transient reaches full field")
    for target in recurrent_expected - {field.full}:
        A.equal(len(predecessors[index[target]]), 1,
                f"p={p} non-full recurrent component is bare")

    edge_payload = "\n".join(
        f"{state_text(source)}->{state_text(target)}"
        for source, target in zip(spaces, edge_spaces)
    ).encode()
    fibre_payload = "\n".join(
        f"{time}:" + ",".join(f"{target}:{count}" for target, count in sorted(table.items()))
        for time, table in enumerate(fibre_tables, 1)
    ).encode()
    return {
        "assertions": A.assertions - before,
        "companion_polynomial": [*field.coefficients, 1],
        "states": S,
        "image_time_1": images[0],
        "recurrent": R,
        "fixed": F,
        "cycle_census": {str(length): count for length, count in sorted(Counter(map(len, cycles)).items())},
        "depth_census": {str(depth): count for depth, count in sorted(Counter(tails).items())},
        "full_field_fibres_t_1_to_6": full_fibres,
        "edge_sha256": hashlib.sha256(edge_payload).hexdigest(),
        "fibre_sha256": hashlib.sha256(fibre_payload).hexdigest(),
    }


def normalized_plane_sweep(p: int):
    """All normalized <1,alpha> planes at an extra odd prime."""
    before = A.assertions
    field = ProjectiveQuartic(p)
    degree_counts = Counter()
    rank_counts = Counter()
    for exponent, alpha in enumerate(field.powers):
        if exponent % field.line_count == 0:
            continue  # alpha lies in F_p
        representatives = [ONE]
        for scalar in range(p):
            denominator = field.subtract(alpha, (scalar, 0, 0, 0))
            A.check(denominator != ZERO, f"p={p} projective denominator")
            representatives.append(field.inverse(denominator))
        actual_rank = len(echelon_basis(representatives, p))
        degree = 2 if exponent * (p**2 - 1) % field.group_order == 0 else 4
        expected_rank = 2 if degree == 2 else min(p + 1, 4)
        A.equal(actual_rank, expected_rank,
                f"p={p} normalized inverse-line rank exponent {exponent}")
        degree_counts[degree] += 1
        rank_counts[actual_rank] += 1
    A.equal(degree_counts, Counter({2: p**2 - p, 4: p**4 - p**2}),
            f"p={p} degree-two/four alpha census")
    return {
        "assertions": A.assertions - before,
        "companion_polynomial": [*field.coefficients, 1],
        "normalized_alpha": sum(degree_counts.values()),
        "degree_census": {str(key): value for key, value in sorted(degree_counts.items())},
        "inverse_span_rank_census": {str(key): value for key, value in sorted(rank_counts.items())},
    }


def main():
    full_graphs = {str(p): verify_full_graph(p) for p in (2, 3, 5, 7)}
    extra_sweep = normalized_plane_sweep(11)
    result = {
        "assertions": A.assertions,
        "decision": "REVIEW_B_INDEPENDENT_CONTROL_PASS",
        "external_status": "HOLD_EXTERNAL",
        "implementation": "primitive-companion/projective-point/trace-kernel",
        "full_graphs": full_graphs,
        "extra_normalized_plane_sweep": {"11": extra_sweep},
        "scope": {
            "complete_projective_subspace_graphs": [2, 3, 5, 7],
            "every_target_fibre_times": [1, 2, 3, 4, 5, 6],
            "fixed_iterates": [1, 2, 3, 4, 5, 6, 7, 8],
            "extra_all_alpha_plane_rank_prime": 11,
            "author_or_review_a_imports": 0,
        },
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
