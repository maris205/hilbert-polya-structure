#!/usr/bin/env python3
"""Falsification spikes for two owner-heavy integer-partition candidates."""

from collections import Counter
from functools import lru_cache


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(None)
def partitions(total, maximum):
    if total == 0:
        return ((),)
    return tuple(
        (part,) + rest
        for part in range(min(total, maximum), 0, -1)
        for rest in partitions(total - part, part)
    )


def multiplicity_profile(partition):
    return tuple(sorted(Counter(partition).values(), reverse=True))


@lru_cache(None)
def profile_depth(partition):
    if partition == (1,):
        return 0
    return 1 + profile_depth(multiplicity_profile(partition))


def equal_part_coagulation(partition):
    multiplicities = Counter(partition)
    return tuple(
        sorted((part * count for part, count in multiplicities.items()), reverse=True)
    )


@lru_cache(None)
def coagulation_depth(partition):
    image = equal_part_coagulation(partition)
    if image == partition:
        return 0
    return 1 + coagulation_depth(image)


def main():
    profile_rows = []
    coagulation_rows = []
    first_log_failure = None

    for n in range(1, 36):
        states = partitions(n, n)
        profile_histogram = Counter(profile_depth(state) for state in states)
        coagulation_histogram = Counter(coagulation_depth(state) for state in states)

        for state in states:
            first = multiplicity_profile(state)
            second = multiplicity_profile(first)
            check(sum(first) == len(state), "profile weight is not source length")
            check(sum(second) == len(set(state)), "second profile weight is not distinct-part count")
            check(sum(equal_part_coagulation(state)) == n, "coagulation did not preserve weight")

        naive_log = n.bit_length() - 1
        if first_log_failure is None and max(coagulation_histogram) != naive_log:
            first_log_failure = (n, max(coagulation_histogram), naive_log)

        profile_rows.append((n, max(profile_histogram), dict(sorted(profile_histogram.items()))))
        coagulation_rows.append((n, max(coagulation_histogram), dict(sorted(coagulation_histogram.items()))))

    check(first_log_failure == (5, 1, 2), "unexpected first floor-log depth failure")
    for power in (2, 4, 8, 16, 32):
        deepest = max(coagulation_depth(state) for state in partitions(power, power))
        witnesses = [
            state for state in partitions(power, power)
            if coagulation_depth(state) == deepest
        ]
        expected = tuple(
            list(reversed([2 ** exponent for exponent in range(power.bit_length() - 1)]))
            + [1]
        )
        check(witnesses == [expected], "power-of-two deepest coagulation witness was not unique")

    print("owner-heavy partition kill spikes: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"first_floor_log_counterexample={first_log_failure}")
    print("profile_rows")
    for row in profile_rows:
        print(row)
    print("coagulation_rows")
    for row in coagulation_rows:
        print(row)


if __name__ == "__main__":
    main()
