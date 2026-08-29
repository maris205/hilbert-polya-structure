#!/usr/bin/env python3
"""Exact controls for principal-hook partition dynamics.

The script exhausts every integer partition through n=40.  It computes the
update independently from Ferrers columns and Frobenius coordinates, checks
the classical image/fibre layer, the exact gap increments, attraction and
sharp depth, the weighted layer recurrence, conjugation invariance, and the
fixed/zeta census.  Only the Python standard library is used.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


@lru_cache(None)
def partitions(total, maximum):
    if total == 0:
        return ((),)
    return tuple(
        (part,) + rest
        for part in range(min(total, maximum), 0, -1)
        for rest in partitions(total - part, part)
    )


def states_of(n):
    return partitions(n, n)


@lru_cache(None)
def conjugate(partition):
    return tuple(
        sum(part >= column for part in partition)
        for column in range(1, partition[0] + 1)
    )


@lru_cache(None)
def durfee_size(partition):
    size = 0
    while size < len(partition) and partition[size] >= size + 1:
        size += 1
    return size


@lru_cache(None)
def frobenius_coordinates(partition):
    conjugate_partition = conjugate(partition)
    size = durfee_size(partition)
    arms = tuple(partition[i] - i - 1 for i in range(size))
    legs = tuple(conjugate_partition[i] - i - 1 for i in range(size))
    return arms, legs


@lru_cache(None)
def hooks_ferrers(partition):
    conjugate_partition = conjugate(partition)
    size = durfee_size(partition)
    return tuple(
        partition[i] + conjugate_partition[i] - 2 * (i + 1) + 1
        for i in range(size)
    )


@lru_cache(None)
def hooks_frobenius(partition):
    arms, legs = frobenius_coordinates(partition)
    return tuple(arm + leg + 1 for arm, leg in zip(arms, legs))


def has_gap_two(partition):
    return all(
        partition[i] - partition[i + 1] >= 2
        for i in range(len(partition) - 1)
    )


def first_gap(partition):
    return partition[0] - (partition[1] if len(partition) > 1 else 0)


def multiplicity_one(partition):
    return sum(part == 1 for part in partition)


def fibre_weight(hooks):
    weight = hooks[-1]
    for i in range(len(hooks) - 1):
        weight *= hooks[i] - hooks[i + 1] - 1
    return weight


def frobenius_fibre_dp(hooks):
    """Independently count strict arm/leg splittings of a hook type."""

    @lru_cache(None)
    def recurse(index, previous_arm, previous_leg):
        if index == len(hooks):
            return 1
        total = 0
        for arm in range(hooks[index]):
            leg = hooks[index] - 1 - arm
            if arm < previous_arm and leg < previous_leg:
                total += recurse(index + 1, arm, leg)
        return total

    sentinel = hooks[0] + 1
    return recurse(0, sentinel, sentinel)


@lru_cache(None)
def depth(partition):
    if len(partition) == 1:
        return 0
    return 1 + depth(hooks_ferrers(partition))


def iterate(partition, times):
    current = partition
    for _ in range(times):
        current = hooks_ferrers(current)
    return current


def direct_depth(partition):
    current = partition
    seen = set()
    time = 0
    terminal = (sum(partition),)
    while current != terminal:
        AUDIT.check(current not in seen, "nontrivial cycle encountered")
        seen.add(current)
        current = hooks_ferrers(current)
        time += 1
        AUDIT.check(time <= sum(partition), "orbit exceeded elementary bound")
    return time


def zeta_from_fixed(fixed_counts, cutoff):
    coefficients = [Fraction(0) for _ in range(cutoff + 1)]
    coefficients[0] = Fraction(1)
    for degree in range(1, cutoff + 1):
        coefficients[degree] = sum(
            fixed_counts[j] * coefficients[degree - j]
            for j in range(1, degree + 1)
        ) / degree
    return coefficients


def boundary_shell_guess(partition):
    return (
        sum(partition) % 2 == 0
        and len(partition) > 1
        and partition[0] == partition[1]
        and partition[-1] >= 2
    )


def audit_lane(n):
    states = states_of(n)
    terminal = (n,)
    observed_fibres = Counter()
    depth_histogram = Counter()

    for state in states:
        ferrers_image = hooks_ferrers(state)
        frobenius_image = hooks_frobenius(state)
        conjugate_state = conjugate(state)
        image_conjugate = hooks_ferrers(conjugate_state)
        size = durfee_size(state)
        arms, legs = frobenius_coordinates(state)

        AUDIT.check(ferrers_image == frobenius_image, "two hook constructions disagree")
        AUDIT.check(sum(ferrers_image) == n, "principal hooks do not partition weight")
        AUDIT.check(len(ferrers_image) == size, "hook count is not Durfee size")
        AUDIT.check(has_gap_two(ferrers_image), "image gap is smaller than two")
        AUDIT.check(ferrers_image == image_conjugate, "conjugation changed H")
        AUDIT.check(conjugate(conjugate_state) == state, "conjugation is not involutive")
        AUDIT.check(all(arms[i] > arms[i + 1] for i in range(len(arms) - 1)))
        AUDIT.check(all(legs[i] > legs[i + 1] for i in range(len(legs) - 1)))
        AUDIT.check(all(value >= 0 for value in arms + legs))
        AUDIT.check(ferrers_image[0] == state[0] + len(state) - 1, "first-hook formula failed")

        literal_depth = direct_depth(state)
        AUDIT.check(literal_depth == depth(state), "recursive and direct depths disagree")
        AUDIT.check(literal_depth <= (n - first_gap(state)) // 2, "pointwise gap bound failed")
        AUDIT.check(literal_depth <= n // 2, "global depth bound failed")
        depth_histogram[literal_depth] += 1
        observed_fibres[ferrers_image] += 1

        for time in range(1, min(4, literal_depth + 1)):
            AUDIT.check(
                iterate(state, time) == iterate(conjugate_state, time),
                "post-first-step conjugate orbits disagree",
            )

        conjugate_depth = depth(conjugate_state)
        exceptional_pair = n > 1 and {
            state,
            conjugate_state,
        } == {terminal, (1,) * n}
        if exceptional_pair:
            AUDIT.check({literal_depth, conjugate_depth} == {0, 1})
        else:
            AUDIT.check(literal_depth == conjugate_depth, "unexpected depth asymmetry")

        if state == terminal:
            AUDIT.check(ferrers_image == terminal)
            AUDIT.check(literal_depth == 0)
        else:
            AUDIT.check(ferrers_image[0] > state[0], "first part did not increase")
            gap_increment = first_gap(ferrers_image) - first_gap(state)
            if size >= 2:
                lambda_prime_two = sum(part >= 2 for part in state)
                exact_increment = len(state) - lambda_prime_two + 2
                AUDIT.check(exact_increment == 2 + multiplicity_one(state))
                AUDIT.check(gap_increment == exact_increment, "Durfee>=2 gap identity failed")
            else:
                AUDIT.check(all(part == 1 for part in state[1:]))
                b = len(state) - 1
                AUDIT.check(ferrers_image == terminal, "Durfee-one hook did not collapse")
                AUDIT.check(gap_increment == b + 1, "Durfee-one gap identity failed")
            AUDIT.check(gap_increment >= 2, "gap increment smaller than two")

    gap_states = {state for state in states if has_gap_two(state)}
    AUDIT.check(set(observed_fibres) == gap_states, "classical image characterization failed")
    for target in gap_states:
        formula = fibre_weight(target)
        dp_count = frobenius_fibre_dp(target)
        AUDIT.check(observed_fibres[target] == formula, "classical product fibre failed")
        AUDIT.check(dp_count == formula, "independent Frobenius fibre DP failed")

    AUDIT.check(depth_histogram[0] == 1, "fixed layer is not a singleton")
    AUDIT.check(depth_histogram[1] == n - 1, "A_1(n)=n-1 failed")
    AUDIT.check(max(depth_histogram) == n // 2, "sharp maximum depth failed")
    AUDIT.check(sum(depth_histogram.values()) == len(states))
    for time in range(2, max(depth_histogram) + 1):
        recurrence = sum(
            fibre_weight(target)
            for target in gap_states
            if depth(target) == time - 1
        )
        AUDIT.check(depth_histogram[time] == recurrence, "weighted layer recurrence failed")

    a = (n + 1) // 2
    b = n // 2
    balanced = (a, b) if b else (a,)
    current = balanced
    for remaining in range(b, 0, -1):
        if remaining >= 2:
            expected = (a + (b - remaining) + 1, remaining - 1)
        else:
            expected = terminal
        current = hooks_ferrers(current)
        AUDIT.check(current == expected, "balanced two-row path failed")
    AUDIT.check(depth(balanced) == b, "balanced witness did not attain sharp depth")

    cutoff = 8
    fixed_counts = [0] * (cutoff + 1)
    for state in states:
        current = state
        for time in range(1, cutoff + 1):
            current = hooks_ferrers(current)
            if current == state:
                fixed_counts[time] += 1
    for time in range(1, cutoff + 1):
        AUDIT.check(fixed_counts[time] == 1, "iterate fixed count is not one")
    zeta = zeta_from_fixed(fixed_counts, cutoff)
    for coefficient in zeta:
        AUDIT.check(coefficient == 1, "zeta coefficient differs from (1-z)^-1")

    if n == 1:
        AUDIT.check(states == ((1,),))
        AUDIT.check(depth_histogram == Counter({0: 1}))
    if n == 2:
        AUDIT.check(states == ((2,), (1, 1)))
        AUDIT.check(hooks_ferrers((1, 1)) == (2,))
        AUDIT.check(depth_histogram == Counter({0: 1, 1: 1}))

    return {
        "n": n,
        "phase": len(states),
        "image": len(gap_states),
        "maximum": max(depth_histogram),
        "deepest": depth_histogram[max(depth_histogram)],
        "layers": dict(sorted(depth_histogram.items())),
    }


def falsification_audit(limit):
    first_nonprojection = None
    first_depth_conjugacy_failure = None
    first_boundary_failure = None
    for n in range(1, limit + 1):
        for state in states_of(n):
            image = hooks_ferrers(state)
            if first_nonprojection is None and hooks_ferrers(image) != image:
                first_nonprojection = (n, state, image, hooks_ferrers(image))
            conjugate_state = conjugate(state)
            if first_depth_conjugacy_failure is None and depth(state) != depth(conjugate_state):
                first_depth_conjugacy_failure = (
                    n,
                    state,
                    conjugate_state,
                    depth(state),
                    depth(conjugate_state),
                )
            if (
                first_boundary_failure is None
                and boundary_shell_guess(state)
                and depth(state) != n // 2
            ):
                first_boundary_failure = (n, state, depth(state), n // 2)
    return first_nonprojection, first_depth_conjugacy_failure, first_boundary_failure


def main():
    rows = [audit_lane(n) for n in range(1, 41)]
    nonprojection, conjugacy_failure, boundary_failure = falsification_audit(40)
    AUDIT.check(nonprojection == (4, (2, 2), (3, 1), (4,)))
    AUDIT.check(conjugacy_failure == (2, (2,), (1, 1), 0, 1))
    AUDIT.check(boundary_failure == (16, (4, 4, 4, 4), 7, 8))

    print("principal-hook partition dynamics: exact control PASS")
    print(f"first_nonprojection={nonprojection}")
    print(f"first_depth_conjugacy_failure={conjugacy_failure}")
    print(f"first_boundary_shell_failure={boundary_failure}")
    for row in rows:
        print(
            f"lane n={row['n']} p(n)={row['phase']} image={row['image']} "
            f"max_depth={row['maximum']} deepest={row['deepest']} "
            f"layers={row['layers']}"
        )
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
