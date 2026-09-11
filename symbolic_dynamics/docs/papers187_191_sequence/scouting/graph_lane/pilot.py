#!/usr/bin/env python3
"""Deterministic exact breadth pilot for the P187--P191 graph lane.

The sixteen candidates are literal carrier/update/scheduler objects.  The
finite checks below are bounded counterexample pressure, not uniform proofs,
owner clearance, novelty evidence, or permission for external release.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def pairs(n: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(n), 2))


@lru_cache(maxsize=None)
def pair_index(n: int) -> dict[tuple[int, int], int]:
    return {edge: index for index, edge in enumerate(pairs(n))}


def graph_has(mask: int, n: int, u: int, v: int) -> bool:
    if u == v:
        return False
    if u > v:
        u, v = v, u
    return bool(mask >> pair_index(n)[u, v] & 1)


def graph_set(mask: int, n: int, u: int, v: int) -> int:
    if u == v:
        return mask
    if u > v:
        u, v = v, u
    return mask | (1 << pair_index(n)[u, v])


def graph_neighbours(mask: int, n: int) -> tuple[frozenset[int], ...]:
    return tuple(
        frozenset(v for v in range(n) if v != u and graph_has(mask, n, u, v))
        for u in range(n)
    )


def graph_components(mask: int, n: int) -> tuple[tuple[int, ...], ...]:
    neighbourhoods = graph_neighbours(mask, n)
    unseen = set(range(n))
    blocks: list[tuple[int, ...]] = []
    while unseen:
        start = min(unseen)
        queue = [start]
        unseen.remove(start)
        block: list[int] = []
        while queue:
            u = queue.pop()
            block.append(u)
            for v in neighbourhoods[u]:
                if v in unseen:
                    unseen.remove(v)
                    queue.append(v)
        blocks.append(tuple(sorted(block)))
    return tuple(sorted(blocks))


def clique_on(block: tuple[int, ...] | set[int], n: int) -> int:
    value = 0
    for u, v in combinations(sorted(block), 2):
        value = graph_set(value, n, u, v)
    return value


def cluster_blocks(mask: int, n: int) -> tuple[tuple[int, ...], ...] | None:
    blocks = graph_components(mask, n)
    expected = 0
    for block in blocks:
        expected |= clique_on(block, n)
    return blocks if expected == mask else None


def complement_graph(mask: int, n: int) -> int:
    return ((1 << len(pairs(n))) - 1) ^ mask


def relation_has(mask: int, n: int, i: int, j: int) -> bool:
    return bool(mask >> (i * n + j) & 1)


def relation_set(mask: int, n: int, i: int, j: int) -> int:
    return mask | (1 << (i * n + j))


def functional_stats(states: range | tuple[int, ...], values: dict[int, int]) -> dict[str, object]:
    state_tuple = tuple(states)
    state_set = set(state_tuple)
    fibres = Counter(values.values())
    depths: Counter[int] = Counter()
    cycles: set[tuple[int, ...]] = set()
    for x in state_tuple:
        check(values[x] in state_set, "functional map left its carrier")
        order: dict[int, int] = {}
        path: list[int] = []
        y = x
        while y not in order:
            order[y] = len(path)
            path.append(y)
            y = values[y]
        mu = order[y]
        cycle = path[mu:]
        depths[mu] += 1
        rotations = [tuple(cycle[k:] + cycle[:k]) for k in range(len(cycle))]
        cycles.add(min(rotations))
    check(sum(fibres.values()) == len(state_tuple), "fibre mass failure")
    check(sum(depths.values()) == len(state_tuple), "depth mass failure")
    cycle_lengths = Counter(len(cycle) for cycle in cycles)
    return {
        "image": len(fibres),
        "fixed": sum(values[x] == x for x in state_tuple),
        "max_depth": max(depths, default=0),
        "cycles": cycle_lengths,
        "max_fibre": max(fibres.values(), default=0),
        "fibres": fibres,
        "depths": depths,
    }


# G01: transpose after row compression on square incidence relations.
def trc(mask: int, n: int) -> int:
    row_sums = [
        sum(relation_has(mask, n, row, col) for col in range(n))
        for row in range(n)
    ]
    out = 0
    for i in range(n):
        for j in range(n):
            if i < row_sums[j]:
                out = relation_set(out, n, i, j)
    return out


def initial_column_heights(mask: int, n: int) -> tuple[int, ...] | None:
    heights: list[int] = []
    for col in range(n):
        bits = [relation_has(mask, n, row, col) for row in range(n)]
        height = sum(bits)
        if bits != [row < height for row in range(n)]:
            return None
        heights.append(height)
    return tuple(heights)


def is_ferrers(mask: int, n: int) -> bool:
    heights = initial_column_heights(mask, n)
    return heights is not None and all(
        heights[i] >= heights[i + 1] for i in range(n - 1)
    )


def trc_second_fibre_formula(target: int, n: int) -> int:
    heights = initial_column_heights(target, n)
    if heights is None or any(heights[i] < heights[i + 1] for i in range(n - 1)):
        return 0
    row_partition = tuple(
        sum(height > j for height in heights) for j in range(n)
    )
    multiplicities = Counter(row_partition)
    assignments = factorial(n)
    for multiplicity in multiplicities.values():
        assignments //= factorial(multiplicity)
    result = assignments
    for size, multiplicity in multiplicities.items():
        result *= comb(n, size) ** multiplicity
    return result


def audit_g01() -> str:
    summaries = []
    for n in range(1, 5):
        states = range(1 << (n * n))
        values = {x: trc(x, n) for x in states}
        stats = functional_stats(states, values)
        first_fibres = Counter(values.values())
        second_values = {x: values[values[x]] for x in states}
        second_fibres = Counter(second_values.values())
        for x in states:
            f1 = values[x]
            f2 = values[f1]
            check(values[values[f2]] == f2, f"G01 F4 != F2 at n={n}")
            check(initial_column_heights(f1, n) is not None, "G01 bad first image")
            check(is_ferrers(f2, n), "G01 bad second image")
            check(
                (values[values[x]] == x) == is_ferrers(x, n),
                "G01 recurrent-set classification",
            )
            row_sums = tuple(
                sum(relation_has(x, n, row, col) for col in range(n))
                for row in range(n)
            )
            check(
                is_ferrers(f1, n)
                == all(row_sums[i] >= row_sums[i + 1] for i in range(n - 1)),
                "G01 depth-at-most-one classification",
            )
        check(stats["image"] == (n + 1) ** n, "G01 first-image size")
        check(
            sum(is_ferrers(x, n) for x in states) == comb(2 * n, n),
            "G01 Ferrers count",
        )
        check(stats["fixed"] == 2**n, "G01 self-conjugate count")
        expected_le_one = 0
        for row_sums in product(range(n + 1), repeat=n):
            if all(row_sums[i] >= row_sums[i + 1] for i in range(n - 1)):
                term = 1
                for row_sum in row_sums:
                    term *= comb(n, row_sum)
                expected_le_one += term
        actual_le_one = sum(
            population for depth, population in stats["depths"].items() if depth <= 1
        )
        check(actual_le_one == expected_le_one, "G01 depth-layer formula")
        check(stats["depths"].get(0, 0) == comb(2 * n, n), "G01 recurrent layer")
        check(
            stats["depths"].get(2, 0) == (1 << (n * n)) - expected_le_one,
            "G01 deepest-layer formula",
        )
        for target, actual in first_fibres.items():
            heights = initial_column_heights(target, n)
            check(heights is not None, "G01 image recognition")
            expected = 1
            for height in heights or ():
                expected *= comb(n, height)
            check(actual == expected, "G01 time-one fibre formula")
        for target in states:
            actual = second_fibres.get(target, 0)
            check(
                actual == trc_second_fibre_formula(target, n),
                "G01 time-two fibre formula",
            )
        summaries.append(
            f"n={n}:states={len(states)},image={stats['image']},"
            f"recurrent={comb(2*n,n)},fixed={stats['fixed']},"
            f"depth={stats['max_depth']},maxfibre={stats['max_fibre']}"
        )
    return ";".join(summaries)


# G02: complete unions of connected components having equal order.
def ecsc(mask: int, n: int) -> int:
    by_size: dict[int, set[int]] = defaultdict(set)
    for block in graph_components(mask, n):
        by_size[len(block)].update(block)
    out = 0
    for block in by_size.values():
        out |= clique_on(block, n)
    return out


def component_size_multiset(mask: int, n: int) -> tuple[int, ...]:
    return tuple(sorted(len(block) for block in graph_components(mask, n)))


def merge_equal_sizes(sizes: tuple[int, ...]) -> tuple[int, ...]:
    multiplicities = Counter(sizes)
    return tuple(sorted(size * multiplicity for size, multiplicity in multiplicities.items()))


def size_stabilization_time(sizes: tuple[int, ...]) -> int:
    time = 0
    current = sizes
    while True:
        successor = merge_equal_sizes(current)
        if successor == current:
            return time
        current = successor
        time += 1


def fixed_ecsc_count(n: int) -> int:
    total = 0
    for selected_sizes in range(1 << n):
        sizes = tuple(
            size for size in range(1, n + 1) if selected_sizes >> (size - 1) & 1
        )
        if sum(sizes) != n:
            continue
        term = factorial(n)
        for size in sizes:
            term //= factorial(size)
        total += term
    return total


@lru_cache(maxsize=None)
def connected_graph_count(n: int) -> int:
    if n == 0:
        return 1
    return sum(
        len(graph_components(mask, n)) == 1
        for mask in range(1 << len(pairs(n)))
    )


def equal_component_fibre_formula(target: int, n: int) -> int:
    blocks = cluster_blocks(target, n)
    if blocks is None:
        return 0
    sizes = [len(block) for block in blocks]
    divisor_lists = [
        tuple(size for size in range(1, block_size + 1) if block_size % size == 0)
        for block_size in sizes
    ]
    total = 0
    for choice in product(*divisor_lists):
        if len(set(choice)) != len(choice):
            continue
        term = 1
        for block_size, component_size in zip(sizes, choice):
            multiplicity = block_size // component_size
            partitions = factorial(block_size) // (
                factorial(component_size) ** multiplicity * factorial(multiplicity)
            )
            term *= partitions * connected_graph_count(component_size) ** multiplicity
        total += term
    return total


def audit_g02() -> str:
    summaries = []
    for n in range(1, 7):
        states = range(1 << len(pairs(n)))
        values = {x: ecsc(x, n) for x in states}
        stats = functional_stats(states, values)
        check(set(stats["cycles"]) <= {1}, "G02 nontrivial cycle")
        for x in states:
            y = values[x]
            check(cluster_blocks(y, n) is not None, "G02 image not cluster")
            z = values[y]
            check((z | y) == z, "G02 post-image evolution not monotone")
            source_sizes = component_size_multiset(x, n)
            check(
                component_size_multiset(y, n) == merge_equal_sizes(source_sizes),
                "G02 size-multiset semiconjugacy",
            )
            blocks = cluster_blocks(x, n)
            expected_fixed = blocks is not None and len(
                {len(block) for block in blocks}
            ) == len(blocks)
            check((values[x] == x) == expected_fixed, "G02 fixed classification")
            actual_time = 0
            current = x
            while values[current] != current:
                current = values[current]
                actual_time += 1
            expected_time = max(
                size_stabilization_time(source_sizes),
                int(cluster_blocks(x, n) is None),
            )
            check(actual_time == expected_time, "G02 exact stopping time")
            if not expected_fixed:
                check(
                    actual_time <= max(1, len(source_sizes) - 1),
                    "G02 stopping bound",
                )
        check(stats["fixed"] == fixed_ecsc_count(n), "G02 fixed-state count")
        if n <= 5:
            fibres = stats["fibres"]
            for target in states:
                check(
                    fibres.get(target, 0)
                    == equal_component_fibre_formula(target, n),
                    "G02 target-local fibre formula",
                )
        summaries.append(
            f"n={n}:states={len(states)},image={stats['image']},"
            f"fixed={stats['fixed']},depth={stats['max_depth']},"
            f"maxfibre={stats['max_fibre']}"
        )
    return ";".join(summaries)


# G03: outdegree-class equivalence on looped binary relations.
def oced(mask: int, n: int) -> int:
    degrees = [
        sum(relation_has(mask, n, i, j) for j in range(n)) for i in range(n)
    ]
    out = 0
    for i in range(n):
        for j in range(n):
            if degrees[i] == degrees[j]:
                out = relation_set(out, n, i, j)
    return out


def equivalence_blocks(mask: int, n: int) -> tuple[tuple[int, ...], ...] | None:
    for i in range(n):
        if not relation_has(mask, n, i, i):
            return None
    for i in range(n):
        for j in range(n):
            if relation_has(mask, n, i, j) != relation_has(mask, n, j, i):
                return None
            if relation_has(mask, n, i, j):
                for k in range(n):
                    if relation_has(mask, n, j, k) and not relation_has(mask, n, i, k):
                        return None
    unseen = set(range(n))
    blocks = []
    while unseen:
        i = min(unseen)
        block = tuple(j for j in range(n) if relation_has(mask, n, i, j))
        unseen.difference_update(block)
        blocks.append(block)
    return tuple(blocks)


def oced_fibre_formula(target: int, n: int) -> int:
    blocks = equivalence_blocks(target, n)
    if blocks is None:
        return 0
    total = 0
    for degrees in permutations(range(n + 1), len(blocks)):
        term = 1
        for block, degree in zip(blocks, degrees):
            term *= comb(n, degree) ** len(block)
        total += term
    return total


def audit_g03() -> str:
    summaries = []
    for n in range(1, 5):
        states = range(1 << (n * n))
        values = {x: oced(x, n) for x in states}
        stats = functional_stats(states, values)
        equivalences = tuple(x for x in states if equivalence_blocks(x, n) is not None)
        check(set(values.values()) == set(equivalences), "G03 image not all equivalences")
        for target in equivalences:
            check(
                stats["fibres"][target] == oced_fibre_formula(target, n),
                "G03 fibre formula",
            )
        for x in states:
            blocks = equivalence_blocks(x, n)
            expected_fixed = blocks is not None and len(
                {len(block) for block in blocks}
            ) == len(blocks)
            check((values[x] == x) == expected_fixed, "G03 fixed classification")
            y = x
            for _ in range(n + 2):
                y = values[y]
            check(values[y] == y, "G03 failed to converge")
        summaries.append(
            f"n={n}:states={len(states)},image={stats['image']},"
            f"fixed={stats['fixed']},depth={stats['max_depth']},"
            f"maxfibre={stats['max_fibre']}"
        )
    return ";".join(summaries)


# G04: asymmetric converse-difference on loopless digraphs.
@lru_cache(maxsize=None)
def arcs(n: int) -> tuple[tuple[int, int], ...]:
    return tuple((i, j) for i in range(n) for j in range(n) if i != j)


@lru_cache(maxsize=None)
def arc_index(n: int) -> dict[tuple[int, int], int]:
    return {arc: index for index, arc in enumerate(arcs(n))}


def arc_has(mask: int, n: int, i: int, j: int) -> bool:
    return bool(mask >> arc_index(n)[i, j] & 1)


def acd(mask: int, n: int) -> int:
    out = 0
    for i, j in arcs(n):
        if arc_has(mask, n, j, i) and not arc_has(mask, n, i, j):
            out |= 1 << arc_index(n)[i, j]
    return out


def oriented_relation(mask: int, n: int) -> bool:
    return all(
        not (arc_has(mask, n, i, j) and arc_has(mask, n, j, i))
        for i, j in pairs(n)
    )


def acd_fibre_formula(target: int, n: int) -> int:
    if not oriented_relation(target, n):
        return 0
    absent = sum(
        not arc_has(target, n, i, j) and not arc_has(target, n, j, i)
        for i, j in pairs(n)
    )
    return 2**absent


def audit_g04() -> str:
    summaries = []
    for n in range(1, 5):
        states = range(1 << len(arcs(n)))
        values = {x: acd(x, n) for x in states}
        stats = functional_stats(states, values)
        for x in states:
            check(acd(acd(acd(x, n), n), n) == acd(x, n), "G04 F3 != F")
        for target in states:
            check(
                stats["fibres"].get(target, 0) == acd_fibre_formula(target, n),
                "G04 fibre formula",
            )
        summaries.append(
            f"n={n}:states={len(states)},image={stats['image']},"
            f"fixed={stats['fixed']},depth={stats['max_depth']},"
            f"maxfibre={stats['max_fibre']}"
        )
    return ";".join(summaries)


# G05: component-separation graph.
def component_separation(mask: int, n: int) -> int:
    component_of = {}
    for index, block in enumerate(graph_components(mask, n)):
        for vertex in block:
            component_of[vertex] = index
    out = 0
    for u, v in pairs(n):
        if component_of[u] != component_of[v]:
            out = graph_set(out, n, u, v)
    return out


def component_separation_fibre_formula(target: int, n: int) -> int:
    complement_blocks = cluster_blocks(complement_graph(target, n), n)
    if complement_blocks is None:
        return 0
    result = 1
    for block in complement_blocks:
        result *= connected_graph_count(len(block))
    return result


def audit_g05() -> str:
    summaries = []
    for n in range(1, 6):
        states = range(1 << len(pairs(n)))
        values = {x: component_separation(x, n) for x in states}
        stats = functional_stats(states, values)
        for x in states:
            f2 = values[values[x]]
            check(values[values[f2]] == f2, "G05 F4 != F2")
        for target in states:
            check(
                stats["fibres"].get(target, 0)
                == component_separation_fibre_formula(target, n),
                "G05 fibre formula",
            )
        summaries.append(
            f"n={n}:states={len(states)},image={stats['image']},"
            f"fixed={stats['fixed']},depth={stats['max_depth']},"
            f"maxfibre={stats['max_fibre']}"
        )
    return ";".join(summaries)


# G06: open-neighbourhood twin-equality graph.
def open_twin_graph(mask: int, n: int) -> int:
    neighbourhoods = graph_neighbours(mask, n)
    out = 0
    for u, v in pairs(n):
        if neighbourhoods[u] == neighbourhoods[v]:
            out = graph_set(out, n, u, v)
    return out


@lru_cache(maxsize=None)
def false_twin_free_graph_count(n: int) -> int:
    return sum(
        len(set(graph_neighbours(mask, n))) == n
        for mask in range(1 << len(pairs(n)))
    )


def open_twin_fibre_formula(target: int, n: int) -> int:
    blocks = cluster_blocks(target, n)
    if blocks is None:
        return 0
    return false_twin_free_graph_count(len(blocks))


def audit_g06() -> str:
    summaries = []
    for n in range(1, 6):
        states = range(1 << len(pairs(n)))
        values = {x: open_twin_graph(x, n) for x in states}
        stats = functional_stats(states, values)
        for x in states:
            f2 = values[values[x]]
            check(values[values[f2]] == f2, "G06 F4 != F2")
        for target in states:
            check(
                stats["fibres"].get(target, 0) == open_twin_fibre_formula(target, n),
                "G06 fibre formula",
            )
        summaries.append(
            f"n={n}:states={len(states)},image={stats['image']},"
            f"fixed={stats['fixed']},depth={stats['max_depth']},"
            f"maxfibre={stats['max_fibre']}"
        )
    return ";".join(summaries)


# G07: exact-distance-two graph operator.
def distance_two_graph(mask: int, n: int) -> int:
    neighbourhoods = graph_neighbours(mask, n)
    out = 0
    for u, v in pairs(n):
        if not graph_has(mask, n, u, v) and neighbourhoods[u] & neighbourhoods[v]:
            out = graph_set(out, n, u, v)
    return out


def audit_g07() -> str:
    summaries = []
    for n in range(1, 6):
        states = range(1 << len(pairs(n)))
        values = {x: distance_two_graph(x, n) for x in states}
        stats = functional_stats(states, values)
        max_cycle = max(stats["cycles"], default=0)
        summaries.append(
            f"n={n}:states={len(states)},image={stats['image']},"
            f"fixed={stats['fixed']},depth={stats['max_depth']},"
            f"maxcycle={max_cycle},maxfibre={stats['max_fibre']}"
        )
    return ";".join(summaries)


# G08: uniform random Warshall-pivot closure on reflexive relations.
def reflexive_relations(n: int) -> tuple[int, ...]:
    off = arcs(n)
    values = []
    diagonal = sum(1 << (i * n + i) for i in range(n))
    for bits in range(1 << len(off)):
        mask = diagonal
        for index, (i, j) in enumerate(off):
            if bits >> index & 1:
                mask = relation_set(mask, n, i, j)
        values.append(mask)
    return tuple(values)


def warshall_action(mask: int, n: int, pivot: int) -> int:
    out = mask
    for i in range(n):
        if relation_has(mask, n, i, pivot):
            for j in range(n):
                if relation_has(mask, n, pivot, j):
                    out = relation_set(out, n, i, j)
    return out


def transitive_closure(mask: int, n: int) -> int:
    out = mask
    for pivot in range(n):
        out = warshall_action(out, n, pivot)
    return out


def audit_g08() -> str:
    summaries = []
    for n in range(1, 4):
        states = reflexive_relations(n)
        state_set = set(states)
        transitions = {
            x: tuple(warshall_action(x, n, pivot) for pivot in range(n))
            for x in states
        }
        absorbing = {
            x for x in states if all(y == x for y in transitions[x])
        }
        for x in states:
            row = Counter(transitions[x])
            check(sum(row.values()) == n, "G08 kernel row mass")
            check(set(row) <= state_set, "G08 kernel closure")
            endpoint = transitive_closure(x, n)
            check(endpoint in absorbing, "G08 closure not absorbing")
            reached = {x}
            queue = deque([x])
            while queue:
                y = queue.popleft()
                for z in transitions[y]:
                    if z not in reached:
                        reached.add(z)
                        queue.append(z)
            reached_absorbing = reached & absorbing
            check(reached_absorbing == {endpoint}, "G08 endpoint not unique")
        summaries.append(
            f"n={n}:states={len(states)},absorbing={len(absorbing)},"
            f"maxsupport={max(len(set(transitions[x])) for x in states)}"
        )
    return ";".join(summaries)


# G09: uniform cyclic-triangle reversal on tournaments.
def tournament_outdegrees(mask: int, n: int) -> tuple[int, ...]:
    degree = [0] * n
    for index, (u, v) in enumerate(pairs(n)):
        if mask >> index & 1:
            degree[u] += 1
        else:
            degree[v] += 1
    return tuple(degree)


def cyclic_triangle(mask: int, n: int, triple: tuple[int, int, int]) -> bool:
    local = [0, 0, 0]
    for a, b in combinations(range(3), 2):
        u, v = triple[a], triple[b]
        if graph_has(mask, n, u, v):
            local[a] += 1
        else:
            local[b] += 1
    return local == [1, 1, 1]


def triangle_reverse(mask: int, n: int, triple: tuple[int, int, int]) -> int:
    if not cyclic_triangle(mask, n, triple):
        return mask
    out = mask
    for u, v in combinations(triple, 2):
        out ^= 1 << pair_index(n)[min(u, v), max(u, v)]
    return out


def audit_g09() -> str:
    summaries = []
    for n in range(3, 6):
        states = tuple(range(1 << len(pairs(n))))
        schedules = tuple(combinations(range(n), 3))
        transitions = {
            x: tuple(triangle_reverse(x, n, triple) for triple in schedules)
            for x in states
        }
        for x in states:
            row = Counter(transitions[x])
            check(sum(row.values()) == len(schedules), "G09 kernel row mass")
            for y, multiplicity in row.items():
                check(
                    tournament_outdegrees(y, n) == tournament_outdegrees(x, n),
                    "G09 score changed",
                )
                check(
                    Counter(transitions[y])[x] == multiplicity,
                    "G09 kernel not symmetric",
                )
        unseen = set(states)
        components = 0
        while unseen:
            start = min(unseen)
            queue = [start]
            unseen.remove(start)
            while queue:
                x = queue.pop()
                for y in transitions[x]:
                    if y in unseen:
                        unseen.remove(y)
                        queue.append(y)
            components += 1
        absorbing = sum(all(y == x for y in transitions[x]) for x in states)
        summaries.append(
            f"n={n}:states={len(states)},components={components},"
            f"absorbing={absorbing},schedulers={len(schedules)}"
        )
    return ";".join(summaries)


# G10: source-to-sink clicks on orientations of a labelled cycle.
def cycle_click(word: int, n: int, vertex: int) -> int:
    previous = (vertex - 1) % n
    if not (word >> previous & 1) and (word >> vertex & 1):
        return word ^ (1 << previous) ^ (1 << vertex)
    return word


def strongly_connected_components(
    states: tuple[int, ...], transitions: dict[int, tuple[int, ...]]
) -> tuple[tuple[int, ...], ...]:
    graph = {x: set(transitions[x]) for x in states}
    reverse = {x: set() for x in states}
    for x in states:
        for y in graph[x]:
            reverse[y].add(x)
    seen: set[int] = set()
    order: list[int] = []

    def visit(start: int) -> None:
        stack = [(start, False)]
        while stack:
            x, closing = stack.pop()
            if closing:
                order.append(x)
                continue
            if x in seen:
                continue
            seen.add(x)
            stack.append((x, True))
            for y in sorted(graph[x], reverse=True):
                if y not in seen:
                    stack.append((y, False))

    for x in states:
        if x not in seen:
            visit(x)
    components = []
    seen.clear()
    for start in reversed(order):
        if start in seen:
            continue
        block = []
        queue = [start]
        seen.add(start)
        while queue:
            x = queue.pop()
            block.append(x)
            for y in reverse[x]:
                if y not in seen:
                    seen.add(y)
                    queue.append(y)
        components.append(tuple(sorted(block)))
    return tuple(components)


def audit_g10() -> str:
    summaries = []
    for n in range(3, 9):
        states = tuple(range(1 << n))
        transitions = {
            x: tuple(cycle_click(x, n, vertex) for vertex in range(n))
            for x in states
        }
        for x in states:
            check(sum(Counter(transitions[x]).values()) == n, "G10 kernel row mass")
            for y in transitions[x]:
                check(y.bit_count() == x.bit_count(), "G10 weight changed")
        sccs = strongly_connected_components(states, transitions)
        by_weight = Counter()
        for block in sccs:
            weights = {x.bit_count() for x in block}
            check(len(weights) == 1, "G10 mixed-weight SCC")
            by_weight[next(iter(weights))] += len(block)
        for weight in range(n + 1):
            check(by_weight[weight] == comb(n, weight), "G10 weight class mass")
        check(len(sccs) == n + 1, "G10 expected one SCC per weight")
        summaries.append(
            f"n={n}:states={len(states)},scc={len(sccs)},"
            f"largest={max(map(len,sccs))},schedulers={n}"
        )
    return ";".join(summaries)


# Hypergraph helpers for G11 and G14.
@lru_cache(maxsize=None)
def triples(n: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(combinations(range(n), 3))


def hyper_degrees(mask: int, n: int) -> tuple[int, ...]:
    degree = [0] * n
    for index, edge in enumerate(triples(n)):
        if mask >> index & 1:
            for vertex in edge:
                degree[vertex] += 1
    return tuple(degree)


# G11: complete every equal-degree triple in a 3-uniform hypergraph.
def hyper_degree_completion(mask: int, n: int) -> int:
    degrees = hyper_degrees(mask, n)
    out = 0
    for index, edge in enumerate(triples(n)):
        if len({degrees[v] for v in edge}) == 1:
            out |= 1 << index
    return out


def audit_g11() -> str:
    summaries = []
    for n in range(3, 6):
        states = range(1 << len(triples(n)))
        values = {x: hyper_degree_completion(x, n) for x in states}
        stats = functional_stats(states, values)
        for x in states:
            y = values[x]
            check(values[y] in states, "G11 closure")
        summaries.append(
            f"n={n}:states={len(states)},image={stats['image']},"
            f"fixed={stats['fixed']},depth={stats['max_depth']},"
            f"maxcycle={max(stats['cycles'],default=0)},"
            f"maxfibre={stats['max_fibre']}"
        )
    return ";".join(summaries)


# G12: merge each edge-cardinality layer by union.
@lru_cache(maxsize=None)
def nonempty_subsets(n: int) -> tuple[int, ...]:
    return tuple(range(1, 1 << n))


def size_layer_union(family: int, n: int) -> int:
    unions: dict[int, int] = defaultdict(int)
    for index, edge in enumerate(nonempty_subsets(n)):
        if family >> index & 1:
            unions[edge.bit_count()] |= edge
    out = 0
    subset_to_index = {edge: index for index, edge in enumerate(nonempty_subsets(n))}
    for edge in set(unions.values()):
        if edge:
            out |= 1 << subset_to_index[edge]
    return out


def family_edge_sizes(family: int, n: int) -> tuple[int, ...]:
    return tuple(
        edge.bit_count()
        for index, edge in enumerate(nonempty_subsets(n))
        if family >> index & 1
    )


def audit_g12() -> str:
    summaries = []
    for n in range(1, 5):
        states = range(1 << len(nonempty_subsets(n)))
        values = {x: size_layer_union(x, n) for x in states}
        stats = functional_stats(states, values)
        for x in states:
            sizes = family_edge_sizes(x, n)
            check(
                (values[x] == x) == (len(sizes) == len(set(sizes))),
                "G12 fixed classification",
            )
            check(values[x].bit_count() <= x.bit_count(), "G12 edge count increased")
        summaries.append(
            f"n={n}:states={len(states)},image={stats['image']},"
            f"fixed={stats['fixed']},depth={stats['max_depth']},"
            f"maxfibre={stats['max_fibre']}"
        )
    return ";".join(summaries)


# G13: classical blocker duality on clutters.
def is_clutter(family: int, n: int) -> bool:
    edges = [edge for edge in range(1 << n) if family >> edge & 1]
    return all(
        not (a != b and (a & b) == a)
        for a in edges
        for b in edges
    )


def blocker(family: int, n: int) -> int:
    edges = [edge for edge in range(1 << n) if family >> edge & 1]
    hitting = [
        subset
        for subset in range(1 << n)
        if all(subset & edge for edge in edges)
    ]
    minimal = [
        subset
        for subset in hitting
        if not any(
            other != subset and (other & subset) == other
            for other in hitting
        )
    ]
    return sum(1 << subset for subset in minimal)


def audit_g13() -> str:
    summaries = []
    for n in range(1, 5):
        clutters = tuple(
            family
            for family in range(1 << (1 << n))
            if is_clutter(family, n)
        )
        for family in clutters:
            image = blocker(family, n)
            check(is_clutter(image, n), "G13 blocker left clutters")
            check(blocker(image, n) == family, "G13 blocker involution failure")
        fixed = sum(blocker(family, n) == family for family in clutters)
        summaries.append(
            f"n={n}:clutters={len(clutters)},fixed={fixed},cycles="
            f"{(len(clutters)-fixed)//2}"
        )
    return ";".join(summaries)


# G14: random vertex-link complementation on 3-uniform hypergraphs.
def link_complement(mask: int, n: int, vertex: int) -> int:
    toggle = 0
    for index, edge in enumerate(triples(n)):
        if vertex in edge:
            toggle |= 1 << index
    return mask ^ toggle


def undirected_action_components(
    states: tuple[int, ...], transitions: dict[int, tuple[int, ...]]
) -> tuple[tuple[int, ...], ...]:
    unseen = set(states)
    components = []
    while unseen:
        start = min(unseen)
        queue = [start]
        unseen.remove(start)
        block = []
        while queue:
            x = queue.pop()
            block.append(x)
            for y in transitions[x]:
                if y in unseen:
                    unseen.remove(y)
                    queue.append(y)
        components.append(tuple(sorted(block)))
    return tuple(components)


def audit_g14() -> str:
    summaries = []
    for n in range(3, 6):
        states = tuple(range(1 << len(triples(n))))
        transitions = {
            x: tuple(link_complement(x, n, v) for v in range(n))
            for x in states
        }
        for x in states:
            check(sum(Counter(transitions[x]).values()) == n, "G14 kernel row mass")
            for u in range(n):
                for v in range(n):
                    check(
                        link_complement(link_complement(x, n, u), n, v)
                        == link_complement(link_complement(x, n, v), n, u),
                        "G14 actions do not commute",
                    )
        components = undirected_action_components(states, transitions)
        sizes = {len(block) for block in components}
        check(len(sizes) == 1, "G14 Cayley cosets have unequal size")
        summaries.append(
            f"n={n}:states={len(states)},classes={len(components)},"
            f"classsize={next(iter(sizes))},schedulers={n}"
        )
    return ";".join(summaries)


# G15: uniform ordered-wedge closure.
@lru_cache(maxsize=None)
def wedge_schedules(n: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        (u, v, w)
        for v in range(n)
        for u, w in combinations([x for x in range(n) if x != v], 2)
    )


def wedge_action(mask: int, n: int, schedule: tuple[int, int, int]) -> int:
    u, v, w = schedule
    if graph_has(mask, n, u, v) and graph_has(mask, n, v, w):
        return graph_set(mask, n, u, w)
    return mask


def component_completion(mask: int, n: int) -> int:
    out = 0
    for block in graph_components(mask, n):
        out |= clique_on(block, n)
    return out


def audit_g15() -> str:
    summaries = []
    for n in range(3, 6):
        states = tuple(range(1 << len(pairs(n))))
        schedules = wedge_schedules(n)
        transitions = {
            x: tuple(wedge_action(x, n, schedule) for schedule in schedules)
            for x in states
        }
        absorbing = 0
        for x in states:
            check(sum(Counter(transitions[x]).values()) == len(schedules), "G15 row")
            for y in transitions[x]:
                check((y | x) == y, "G15 deleted an edge")
                check(
                    graph_components(y, n) == graph_components(x, n),
                    "G15 changed components",
                )
            y = x
            for _ in range(n):
                for schedule in schedules:
                    y = wedge_action(y, n, schedule)
            check(y == component_completion(x, n), "G15 wrong closure endpoint")
            is_absorbing = all(z == x for z in transitions[x])
            check(is_absorbing == (cluster_blocks(x, n) is not None), "G15 absorbing")
            absorbing += is_absorbing
        summaries.append(
            f"n={n}:states={len(states)},absorbing={absorbing},"
            f"schedulers={len(schedules)}"
        )
    return ";".join(summaries)


# G16: adjacent swaps of orientation bits around a labelled cycle.
def orientation_swap(word: int, n: int, edge: int) -> int:
    nxt = (edge + 1) % n
    a = bool(word >> edge & 1)
    b = bool(word >> nxt & 1)
    if a != b:
        return word ^ (1 << edge) ^ (1 << nxt)
    return word


def audit_g16() -> str:
    summaries = []
    for n in range(3, 9):
        states = tuple(range(1 << n))
        transitions = {
            x: tuple(orientation_swap(x, n, edge) for edge in range(n))
            for x in states
        }
        for x in states:
            row = Counter(transitions[x])
            check(sum(row.values()) == n, "G16 kernel row mass")
            for y, multiplicity in row.items():
                check(y.bit_count() == x.bit_count(), "G16 orientation weight")
                check(Counter(transitions[y])[x] == multiplicity, "G16 asymmetry")
        components = undirected_action_components(states, transitions)
        check(len(components) == n + 1, "G16 one component per weight")
        for block in components:
            weight = block[0].bit_count()
            check(len(block) == comb(n, weight), "G16 component size")
        summaries.append(
            f"n={n}:states={len(states)},classes={len(components)},"
            f"largest={max(map(len,components))},schedulers={n}"
        )
    return ";".join(summaries)


def main() -> None:
    audits = (
        ("G01_TRC", "SURVIVE", audit_g01),
        ("G02_ECSC", "SURVIVE", audit_g02),
        ("G03_OCED", "KILL_TRANSFER", audit_g03),
        ("G04_ACD", "KILL_SHALLOW", audit_g04),
        ("G05_CSG", "KILL_COLLISION", audit_g05),
        ("G06_OTEG", "KILL_TRANSFER", audit_g06),
        ("G07_D2G", "KILL_OWNER_WEAK", audit_g07),
        ("G08_RWP", "KILL_DIRECT_OWNER", audit_g08),
        ("G09_CTR", "KILL_DIRECT_OWNER", audit_g09),
        ("G10_CSC", "KILL_DIRECT_OWNER", audit_g10),
        ("G11_HDCC", "KILL_TRANSFER", audit_g11),
        ("G12_SLU", "KILL_WEAK", audit_g12),
        ("G13_HBD", "KILL_DIRECT_OWNER", audit_g13),
        ("G14_RLC", "KILL_COMMUTING_SUPPORT", audit_g14),
        ("G15_RWC", "KILL_CLOSURE", audit_g15),
        ("G16_OES", "KILL_DIRECT_OWNER", audit_g16),
    )
    print("GRAPH_RELATION_RANDOM_LOCAL_BREADTH_PILOT_V1")
    print(f"candidate_denominator={len(audits)}")
    survivors = []
    for identifier, disposition, audit in audits:
        summary = audit()
        print(f"{identifier} disposition={disposition} {summary}")
        if disposition == "SURVIVE":
            survivors.append(identifier)
    check(len(audits) == 16, "candidate denominator changed")
    check(1 <= len(survivors) <= 3, "survivor count outside gate")
    print(f"survivors={','.join(survivors)}")
    print(f"exact_assertions={ASSERTIONS}")
    print("scope=bounded finite counterexample pressure; uniform claims require proofs")
    print("owner_status=OWNER_AMBER")
    print("external_status=HOLD_EXTERNAL")
    print("status=PASS")


if __name__ == "__main__":
    main()
