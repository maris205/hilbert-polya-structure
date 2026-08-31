#!/usr/bin/env python3
"""Deterministic exact controls for crossing-component planarisation.

The program uses only Python's standard library.  It exhausts every rooted
chord matching through seven chords, checks the literal finite map and every
target fibre, and independently reconstructs every source from the
sibling-list inverse described in the paper.  These finite controls are
counterexample pressure; the manuscript supplies the all-size proofs.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import comb


class Checks:
    def __init__(self) -> None:
        self.count = 0

    def that(self, condition: bool, payload=None) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(payload)


@lru_cache(maxsize=None)
def matchings_on(points: tuple[int, ...]) -> tuple[tuple[tuple[int, int], ...], ...]:
    if not points:
        return ((),)
    first = points[0]
    out = []
    for position in range(1, len(points)):
        second = points[position]
        rest = points[1:position] + points[position + 1 :]
        for tail in matchings_on(rest):
            out.append(tuple(sorted(((first, second),) + tail)))
    return tuple(out)


def all_matchings(n: int) -> tuple[tuple[tuple[int, int], ...], ...]:
    return matchings_on(tuple(range(2 * n)))


def crosses(left: tuple[int, int], right: tuple[int, int]) -> bool:
    a, b = left
    c, d = right
    return (a < c < b < d) or (c < a < d < b)


def chord_components(matching: tuple[tuple[int, int], ...]) -> tuple[tuple[int, ...], ...]:
    n = len(matching)
    unseen = set(range(n))
    components = []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        stack = [seed]
        component = []
        while stack:
            i = stack.pop()
            component.append(i)
            neighbours = [j for j in sorted(unseen) if crosses(matching[i], matching[j])]
            for j in neighbours:
                unseen.remove(j)
                stack.append(j)
        components.append(tuple(sorted(component)))
    return tuple(sorted(components, key=lambda block: min(matching[i][0] for i in block)))


def support_blocks(matching: tuple[tuple[int, int], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(sorted(endpoint for i in component for endpoint in matching[i]))
        for component in chord_components(matching)
    )


def planarise(matching: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
    output = []
    for support in support_blocks(matching):
        output.extend((support[i], support[i + 1]) for i in range(0, len(support), 2))
    return tuple(sorted(output))


def is_noncrossing_matching(matching: tuple[tuple[int, int], ...]) -> bool:
    return all(not crosses(x, y) for x, y in combinations(matching, 2))


def blocks_cross(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    for a, b in combinations(left, 2):
        for c, d in combinations(right, 2):
            if (a < c < b < d) or (c < a < d < b):
                return True
    return False


def is_noncrossing_partition(blocks: tuple[tuple[int, ...], ...]) -> bool:
    return all(not blocks_cross(left, right) for left, right in combinations(blocks, 2))


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def odd_double_factorial(n: int) -> int:
    value = 1
    for factor in range(1, 2 * n, 2):
        value *= factor
    return value


@lru_cache(maxsize=None)
def rgs_words(n: int) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    out = []

    def extend(prefix: tuple[int, ...], maximum: int) -> None:
        if len(prefix) == n:
            out.append(prefix)
            return
        for value in range(maximum + 2):
            extend(prefix + (value,), max(maximum, value))

    extend((0,), 0)
    return tuple(out)


def rgs_blocks(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    if not word:
        return ()
    return tuple(tuple(i for i, value in enumerate(word) if value == label)
                 for label in range(max(word) + 1))


@lru_cache(maxsize=None)
def nc_partitions(n: int) -> tuple[tuple[tuple[int, ...], ...], ...]:
    return tuple(
        blocks
        for word in rgs_words(n)
        for blocks in (rgs_blocks(word),)
        if is_noncrossing_partition(blocks)
    )


def parent_data(target: tuple[tuple[int, int], ...]) -> tuple[tuple[int, ...], dict[int, tuple[int, ...]]]:
    parents = []
    for i, (a, b) in enumerate(target):
        containers = [
            (d - c, j)
            for j, (c, d) in enumerate(target)
            if c < a < b < d
        ]
        parents.append(min(containers)[1] if containers else -1)
    children = {
        parent: tuple(sorted((i for i, p in enumerate(parents) if p == parent),
                             key=lambda i: target[i][0]))
        for parent in (-1,) + tuple(range(len(target)))
    }
    return tuple(parents), children


def component_groups_are_sibling_nc(
    source: tuple[tuple[int, int], ...],
    target: tuple[tuple[int, int], ...],
) -> bool:
    parents, children = parent_data(target)
    index = {chord: i for i, chord in enumerate(target)}
    groups_by_parent: dict[int, list[tuple[int, ...]]] = defaultdict(list)
    for support in support_blocks(source):
        section = tuple((support[i], support[i + 1]) for i in range(0, len(support), 2))
        group = tuple(index[chord] for chord in section)
        if not group:
            return False
        parent_set = {parents[i] for i in group}
        if len(parent_set) != 1:
            return False
        groups_by_parent[next(iter(parent_set))].append(group)
    for parent, siblings in children.items():
        positions = {chord: i for i, chord in enumerate(siblings)}
        local_blocks = tuple(
            tuple(sorted(positions[chord] for chord in group))
            for group in groups_by_parent.get(parent, [])
        )
        flattened = sorted(i for block in local_blocks for i in block)
        if flattened != list(range(len(siblings))):
            return False
        if not is_noncrossing_partition(local_blocks):
            return False
    return True


def connected_matchings(max_n: int) -> tuple[tuple[tuple[tuple[int, int], ...], ...], ...]:
    rows = [()]
    for n in range(1, max_n + 1):
        rows.append(tuple(matching for matching in all_matchings(n)
                          if len(chord_components(matching)) == 1))
    return tuple(rows)


def transform_coefficients(connected_counts: tuple[int, ...]) -> tuple[int, ...]:
    """Triangular coefficient solution of A=1+C(uA)."""
    maximum = len(connected_counts) - 1
    a = [0] * (maximum + 1)
    a[0] = 1
    for n in range(1, maximum + 1):
        total = 0
        for partition in nc_partitions(n):
            weight = 1
            for block in partition:
                weight *= connected_counts[len(block)]
            total += weight
        a[n] = total
    return tuple(a)


def multiply(left: list[int], right: list[int], degree: int) -> list[int]:
    out = [0] * (degree + 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if i + j <= degree:
                out[i + j] += x * y
    return out


def compose_transform(connected: tuple[int, ...], a: tuple[int, ...]) -> tuple[int, ...]:
    """Coefficients of 1+C(uA), truncated to the supplied degree."""
    degree = len(a) - 1
    result = [0] * (degree + 1)
    result[0] = 1
    ua = [0] + list(a[:-1])
    power = [1] + [0] * degree
    for k in range(1, degree + 1):
        power = multiply(power, ua, degree)
        for i in range(degree + 1):
            result[i] += connected[k] * power[i]
    return tuple(result)


def transport_decoration(
    decoration: tuple[tuple[int, int], ...],
    endpoint_block: tuple[int, ...],
) -> tuple[tuple[int, int], ...]:
    return tuple(sorted((endpoint_block[a], endpoint_block[b]) for a, b in decoration))


def local_sources(
    target: tuple[tuple[int, int], ...],
    siblings: tuple[int, ...],
    connected: tuple[tuple[tuple[tuple[int, int], ...], ...], ...],
):
    if not siblings:
        yield ()
        return
    for partition in nc_partitions(len(siblings)):
        choices = []
        endpoint_blocks = []
        for block in partition:
            selected = tuple(siblings[position] for position in block)
            endpoints = tuple(sorted(endpoint for i in selected for endpoint in target[i]))
            endpoint_blocks.append(endpoints)
            choices.append(connected[len(block)])
        for decorations in product(*choices):
            chords = []
            for decoration, endpoints in zip(decorations, endpoint_blocks):
                chords.extend(transport_decoration(decoration, endpoints))
            yield tuple(sorted(chords))


def reconstructed_sources(
    target: tuple[tuple[int, int], ...],
    connected: tuple[tuple[tuple[tuple[int, int], ...], ...], ...],
):
    _, children = parent_data(target)
    lists = [children[parent] for parent in (-1,) + tuple(range(len(target))) if children[parent]]
    local_families = [tuple(local_sources(target, siblings, connected)) for siblings in lists]
    if not local_families:
        yield ()
        return
    for choice in product(*local_families):
        yield tuple(sorted(chord for local in choice for chord in local))


def run() -> None:
    checks = Checks()
    maximum_n = 7
    connected = connected_matchings(maximum_n)
    connected_counts = tuple(len(row) for row in connected)
    free_counts = transform_coefficients(connected_counts)

    checks.that(connected_counts == (0, 1, 1, 4, 27, 248, 2830, 38232), connected_counts)
    checks.that(free_counts == (1, 1, 2, 8, 52, 464, 5184, 68928), free_counts)
    checks.that(compose_transform(connected_counts, free_counts) == free_counts,
                "formal transform A=1+C(uA)")
    for n in range(maximum_n + 1):
        checks.that(len(nc_partitions(n)) == catalan(n),
                    (n, len(nc_partitions(n)), catalan(n)))
    for i in range(1, maximum_n + 1):
        for j in range(1, maximum_n + 1 - i):
            checks.that(free_counts[i] * free_counts[j] < free_counts[i + j],
                        (i, j, free_counts[i], free_counts[j], free_counts[i + j]))

    print("P130 crossing-component fibre geometry exact verifier")
    total_states = 0
    total_targets = 0
    total_reconstructed = 0

    for n in range(maximum_n + 1):
        states = all_matchings(n)
        total_states += len(states)
        checks.that(len(states) == odd_double_factorial(n),
                    (n, len(states), odd_double_factorial(n)))
        fibres: dict[tuple[tuple[int, int], ...], set[tuple[tuple[int, int], ...]]] = defaultdict(set)
        for source in states:
            target = planarise(source)
            checks.that(is_noncrossing_partition(support_blocks(source)),
                        (n, source, support_blocks(source), "component supports"))
            checks.that(is_noncrossing_matching(target), (n, source, target, "image"))
            checks.that(planarise(target) == target, (n, source, target, "idempotence"))
            checks.that(component_groups_are_sibling_nc(source, target),
                        (n, source, target, "forward sibling extraction"))
            fibres[target].add(source)

        targets = tuple(target for target in states if is_noncrossing_matching(target))
        total_targets += len(targets)
        checks.that(len(targets) == catalan(n), (n, len(targets), catalan(n)))
        checks.that(set(fibres) == set(targets), (n, "image/fixed equality"))

        maximum = 0
        maximizers = []
        reconstructed_here = 0
        for target in targets:
            _, children = parent_data(target)
            degrees = tuple(len(children[parent])
                            for parent in (-1,) + tuple(range(n)))
            checks.that(sum(degrees) == n, (n, target, degrees))
            predicted = 1
            for degree in degrees:
                predicted *= free_counts[degree]
            checks.that(len(fibres[target]) == predicted,
                        (n, target, len(fibres[target]), predicted, degrees))

            reconstructed = tuple(reconstructed_sources(target, connected))
            reconstructed_set = set(reconstructed)
            reconstructed_here += len(reconstructed)
            checks.that(len(reconstructed) == len(reconstructed_set),
                        (n, target, "inverse injectivity"))
            checks.that(reconstructed_set == fibres[target],
                        (n, target, "inverse surjectivity", len(reconstructed_set), len(fibres[target])))
            for source in reconstructed:
                checks.that(planarise(source) == target,
                            (n, target, source, "converse construction"))

            fibre_size = len(fibres[target])
            if fibre_size > maximum:
                maximum = fibre_size
                maximizers = [target]
            elif fibre_size == maximum:
                maximizers.append(target)

        total_reconstructed += reconstructed_here
        adjacent = tuple((2 * i, 2 * i + 1) for i in range(n))
        rainbow = tuple((i, 2 * n - 1 - i) for i in range(n))
        checks.that(maximum == free_counts[n], (n, maximum, free_counts[n]))
        checks.that(maximizers == [adjacent], (n, maximizers, adjacent))
        checks.that(len(fibres[rainbow]) == 1, (n, rainbow, len(fibres[rainbow])))
        checks.that(sum(map(len, fibres.values())) == len(states), (n, "fibre mass"))
        checks.that(reconstructed_here == len(states), (n, reconstructed_here, len(states)))
        gardens = sum(source not in fibres for source in states)
        checks.that(gardens == len(states) - len(targets),
                    (n, gardens, len(states) - len(targets)))

        print(
            f"n={n} | states={len(states)} | targets={len(targets)} | "
            f"connected={connected_counts[n]} | a_n={free_counts[n]} | "
            f"garden={gardens} | reconstructed={reconstructed_here}"
        )

    checks.that(total_reconstructed == total_states,
                (total_reconstructed, total_states, "global inverse mass"))
    print(
        f"TOTAL | n<=7 | states={total_states} | targets={total_targets} | "
        f"reconstructed={total_reconstructed} | assertions={checks.count}"
    )
    print("status: PASS; finite controls only, all-size proofs are in main.tex")


if __name__ == "__main__":
    run()
