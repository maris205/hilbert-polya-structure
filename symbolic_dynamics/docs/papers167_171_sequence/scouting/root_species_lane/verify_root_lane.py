#!/usr/bin/env python3
"""Exact negative controls for the coordinator's species/global-statistic lane.

The candidates here are intentionally *not* paper allocations.  The program
checks their strongest small-box signals before the collision gate is applied.
"""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter, defaultdict


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def integer_partitions(n: int, least: int = 1):
    if n == 0:
        yield ()
        return
    for first in range(least, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def equal_size_coalescence(profile: tuple[int, ...]) -> tuple[int, ...]:
    multiplicity = Counter(profile)
    return tuple(sorted(size * count for size, count in multiplicity.items()))


def absorption_depth(profile: tuple[int, ...]) -> int:
    depth = 0
    while True:
        image = equal_size_coalescence(profile)
        if image == profile:
            return depth
        check(len(image) < len(profile), "strict block-count descent")
        profile = image
        depth += 1


def restricted_growth_strings(n: int):
    if n == 0:
        yield ()
        return
    word = [0]

    def rec(position: int, maximum: int):
        if position == n:
            yield tuple(word)
            return
        for value in range(maximum + 2):
            word.append(value)
            yield from rec(position + 1, max(maximum, value))
            word.pop()

    yield from rec(1, 0)


def blocks_of(rgs: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    blocks: dict[int, list[int]] = defaultdict(list)
    for point, block in enumerate(rgs):
        blocks[block].append(point)
    return tuple(tuple(blocks[key]) for key in sorted(blocks))


def canonical_partition(blocks) -> tuple[tuple[int, ...], ...]:
    return tuple(sorted((tuple(sorted(block)) for block in blocks), key=lambda b: b[0]))


def coalesce_partition(partition: tuple[tuple[int, ...], ...]):
    by_size: dict[int, list[tuple[int, ...]]] = defaultdict(list)
    for block in partition:
        by_size[len(block)].append(block)
    return canonical_partition(
        tuple(itertools.chain.from_iterable(group))
        for _, group in sorted(by_size.items())
    )


def equal_block_partition_count(block_size: int, source_size: int) -> int:
    multiplicity = block_size // source_size
    return math.factorial(block_size) // (
        math.factorial(source_size) ** multiplicity * math.factorial(multiplicity)
    )


def coalescence_fibre_formula(target: tuple[tuple[int, ...], ...]) -> int:
    sizes = [len(block) for block in target]

    def rec(index: int, used_source_sizes: frozenset[int]) -> int:
        if index == len(sizes):
            return 1
        total = 0
        b = sizes[index]
        for source_size in range(1, b + 1):
            if b % source_size or source_size in used_source_sizes:
                continue
            total += equal_block_partition_count(b, source_size) * rec(
                index + 1, used_source_sizes | {source_size}
            )
        return total

    return rec(0, frozenset())


def cycle_power_feedback(profile: tuple[int, ...]) -> tuple[int, ...]:
    cycle_count = len(profile)
    image = []
    for length in profile:
        split = math.gcd(length, cycle_count)
        image.extend([length // split] * split)
    return tuple(sorted(image))


def type_tail(profile: tuple[int, ...]) -> int:
    depth = 0
    while True:
        image = cycle_power_feedback(profile)
        if image == profile:
            return depth
        check(len(image) > len(profile), "cycle count strictly rises before type stability")
        profile = image
        depth += 1


def divisor_quadratic_meet(exponent: int, total_exponent: int) -> int:
    # v_p(gcd(d^2, N/d)); this is literally the exponent map occupied by P142.
    return min(2 * exponent, total_exponent - exponent)


def main() -> None:
    coalescence_maxima = {}
    for n in range(1, 33):
        maximum = -1
        witness = None
        for profile in integer_partitions(n):
            depth = absorption_depth(profile)
            check(depth <= n.bit_length() - 1, "doubling upper bound")
            if depth > maximum:
                maximum, witness = depth, profile
        coalescence_maxima[n] = {"height": maximum, "witness": witness}

    for depth in range(0, 10):
        if depth == 0:
            cascade = (1,)
        else:
            cascade = (1, 1) + tuple(2**j for j in range(1, depth))
        check(sum(cascade) == 2**depth, "cascade weight")
        check(absorption_depth(tuple(sorted(cascade))) == depth, "cascade depth")

    fibre_maxima = {}
    for n in range(1, 9):
        states = [blocks_of(rgs) for rgs in restricted_growth_strings(n)]
        actual = Counter(coalesce_partition(state) for state in states)
        maximum = 0
        for target in states:
            predicted = coalescence_fibre_formula(target)
            check(predicted == actual[target], "every-target coalescence fibre")
            maximum = max(maximum, predicted)
        fibre_maxima[n] = maximum

    power_feedback_maxima = {}
    for n in range(1, 41):
        depths = [(type_tail(profile), profile) for profile in integer_partitions(n)]
        maximum = max(depth for depth, _ in depths)
        witness = min(profile for depth, profile in depths if depth == maximum)
        power_feedback_maxima[n] = {"type_tail": maximum, "witness": witness}

    divisor_profiles = {}
    for exponent in range(1, 81):
        tails = []
        periods = set()
        for start in range(exponent + 1):
            seen = {}
            value = start
            while value not in seen:
                seen[value] = len(seen)
                value = divisor_quadratic_meet(value, exponent)
            tails.append(seen[value])
            periods.add(len(seen) - seen[value])
        check(periods <= {1, 2}, "P142 recurrent periods")
        divisor_profiles[exponent] = {
            "maximum_tail": max(tails),
            "periods": sorted(periods),
        }

    report = {
        "assertions": ASSERTIONS,
        "equal_size_block_coalescence": {
            "decision": "KILL_INTERNAL_P147",
            "fixed_n_maxima_1_to_32": coalescence_maxima,
            "maximum_labelled_fibres_1_to_8": fibre_maxima,
            "sharp_on_size_at_most_N": "floor(log2 N), attained at N=2^k",
        },
        "cycle_count_power_feedback": {
            "decision": "KILL_NO_CLEAN_ALL_PARAMETER_CLOCK_OR_INVERSE",
            "type_maxima_1_to_40": power_feedback_maxima,
        },
        "divisor_quadratic_meet": {
            "decision": "KILL_EXACT_EXPONENT_MAP_P142",
            "profiles_1_to_80": divisor_profiles,
        },
        "external_status": "HOLD_EXTERNAL",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

