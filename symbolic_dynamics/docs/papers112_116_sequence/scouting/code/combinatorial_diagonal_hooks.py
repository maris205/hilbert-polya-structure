#!/usr/bin/env python3
"""Exact spike for iterating the principal-diagonal-hook partition map."""

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


def conjugate(partition):
    return tuple(
        sum(part >= column for part in partition)
        for column in range(1, partition[0] + 1)
    )


def diagonal_hooks(partition):
    durfee = 0
    while durfee < len(partition) and partition[durfee] >= durfee + 1:
        durfee += 1
    return tuple(
        partition[index]
        + sum(part >= index + 1 for part in partition)
        - 2 * index
        - 1
        for index in range(durfee)
    )


def is_rr_partition(partition):
    return all(
        partition[index] - partition[index + 1] >= 2
        for index in range(len(partition) - 1)
    )


def dominates(left, right):
    left_sum = right_sum = 0
    for index in range(max(len(left), len(right))):
        left_sum += left[index] if index < len(left) else 0
        right_sum += right[index] if index < len(right) else 0
        if left_sum < right_sum:
            return False
    return True


def first_gap(partition):
    """Difference between the first two parts, padding the second by zero."""

    return partition[0] - (partition[1] if len(partition) > 1 else 0)


@lru_cache(None)
def depth(partition):
    if len(partition) == 1:
        return 0
    return 1 + depth(diagonal_hooks(partition))


def frobenius_fibre_count(hooks):
    """Count strict arm/leg splittings a_i+b_i+1=hooks_i."""

    @lru_cache(None)
    def rec(index, previous_arm, previous_leg):
        if index == len(hooks):
            return 1
        total = 0
        for arm in range(hooks[index]):
            leg = hooks[index] - 1 - arm
            if arm < previous_arm and leg < previous_leg:
                total += rec(index + 1, arm, leg)
        return total

    sentinel = hooks[0] + 1
    return rec(0, sentinel, sentinel)


def boundary_shell_guess(partition):
    # A deliberately overstrong early guess, retained to locate its first failure.
    return (
        sum(partition) % 2 == 0
        and len(partition) > 1
        and partition[0] == partition[1]
        and partition[-1] >= 2
    )


def lane(n):
    states = partitions(n, n)
    image_fibres = Counter()
    depth_histogram = Counter()

    for state in states:
        image = diagonal_hooks(state)
        check(sum(image) == n, "diagonal hooks did not partition the diagram")
        check(is_rr_partition(image), "image does not have adjacent gaps at least two")
        check(image == diagonal_hooks(conjugate(state)), "conjugation changed diagonal hooks")
        check(dominates(image, state), "diagonal-hook image did not dominate its source")
        if len(state) > 1:
            check(image[0] > state[0], "largest part did not strictly increase")
            check(
                first_gap(image) >= first_gap(state) + 2,
                "first-two-part gap did not increase by at least two",
            )
        image_fibres[image] += 1
        depth_histogram[depth(state)] += 1

    rr_states = {state for state in states if is_rr_partition(state)}
    check(set(image_fibres) == rr_states, "image is not exactly the Rogers--Ramanujan partitions")
    for target, observed in image_fibres.items():
        check(observed == frobenius_fibre_count(target), "Frobenius-coordinate fibre count failed")
    check(depth_histogram[0] == 1, "there is not a unique fixed point")
    check(max(depth_histogram) == n // 2, "observed sharp depth floor(n/2) failed")
    balanced_two_row = ((n + 1) // 2, n // 2) if n > 1 else (1,)
    check(depth(balanced_two_row) == n // 2, "balanced two-row depth witness failed")

    return {
        "n": n,
        "phase": len(states),
        "image": len(image_fibres),
        "max_depth": max(depth_histogram),
        "deepest": depth_histogram[max(depth_histogram)],
        "depths": dict(sorted(depth_histogram.items())),
    }


def falsification_audit(limit):
    first_nonprojection = None
    first_shell_failure = None
    for n in range(1, limit + 1):
        for state in partitions(n, n):
            image = diagonal_hooks(state)
            if first_nonprojection is None and diagonal_hooks(image) != image:
                first_nonprojection = (n, state, image, diagonal_hooks(image))
            if (
                first_shell_failure is None
                and boundary_shell_guess(state)
                and depth(state) != n // 2
            ):
                first_shell_failure = (n, state, depth(state), n // 2)
    return first_nonprojection, first_shell_failure


def main():
    rows = [lane(n) for n in range(1, 36)]
    nonprojection, shell_failure = falsification_audit(35)
    check(nonprojection == (4, (2, 2), (3, 1), (4,)), "unexpected first projection counterexample")
    check(shell_failure == (16, (4, 4, 4, 4), 7, 8), "unexpected first shell counterexample")

    print("principal diagonal-hook partition dynamics spike: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"first_nonprojection={nonprojection}")
    print(f"first_boundary_shell_failure={shell_failure}")
    for row in rows:
        print(
            "lane"
            f" n={row['n']} p(n)={row['phase']} image={row['image']}"
            f" max_depth={row['max_depth']} deepest={row['deepest']}"
            f" depths={row['depths']}"
        )


if __name__ == "__main__":
    main()
