#!/usr/bin/env python3
"""Independent hostile-review verifier for P174.

This implementation uses integer bit masks and reconstructs every projective
map and inverse candidate directly.  It imports no paper or scouting code.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import comb


CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def masks_of_size(size: int, universe: int):
    for chosen in combinations(range(universe), size):
        mask = 0
        for point in chosen:
            mask |= 1 << point
        yield mask


def points(mask: int):
    bit = 0
    while mask:
        if mask & 1:
            yield bit
        mask >>= 1
        bit += 1


def inverse_mod(x: int, p: int) -> int:
    return pow(x, p - 2, p)


def gamma(point: int, pivot: int, p: int) -> int:
    infinity = p
    if point == pivot:
        return infinity
    if point == infinity:
        return 0
    return inverse_mod((point - pivot) % p, p)


def inverse_gamma(point: int, pivot: int, p: int) -> int:
    infinity = p
    if point == infinity:
        return pivot
    if point == 0:
        return infinity
    return (pivot + inverse_mod(point, p)) % p


def transform(mask: int, pivot: int, p: int, inverse: bool = False) -> int:
    answer = 0
    action = inverse_gamma if inverse else gamma
    for point in points(mask):
        answer |= 1 << action(point, pivot, p)
    return answer


def step(mask: int, p: int):
    finite = mask & ((1 << p) - 1)
    pivot = (finite & -finite).bit_length() - 1
    return transform(mask, pivot, p), pivot


def predicted_height(target: int, p: int) -> int:
    beta = 0
    for point in points(target):
        if 0 < point < p:
            beta = max(beta, inverse_mod(point, p))
    return p - beta


def predicted_fixed(p: int, k: int) -> int:
    r = k - 2
    total = 0
    pairs = (p - 3) // 2
    for singletons in range(3):
        if 0 <= r - singletons <= 2 * pairs and (r - singletons) % 2 == 0:
            total += comb(2, singletons) * comb(pairs, (r - singletons) // 2)
    return total


def audit_box(p: int, k: int) -> tuple[int, int, int]:
    infinity_bit = 1 << p
    zero_bit = 1
    states = tuple(masks_of_size(k, p + 1))
    state_set = set(states)
    edge = {}
    pivot = {}
    fibres = defaultdict(list)
    marked = defaultdict(list)

    for source in states:
        target, chosen = step(source, p)
        check(target in state_set, f"carrier p={p} k={k}")
        edge[source] = target
        pivot[source] = chosen
        fibres[target].append(source)
        marked[target].append(chosen)
        check(step(target, p)[0] in state_set, f"second carrier p={p} k={k}")
        check(edge[source] & infinity_bit, f"first image infinity p={p} k={k}")

    image1 = set(edge.values())
    image2 = {edge[edge[source]] for source in states}
    expected1 = {state for state in states if state & infinity_bit}
    expected2 = {state for state in states if state & infinity_bit and state & zero_bit}
    check(image1 == expected1, f"first image p={p} k={k}")
    check(image2 == expected2, f"second image p={p} k={k}")

    depth_hist = Counter()
    fixed = 0
    for source in states:
        second = edge[edge[source]]
        fourth = edge[edge[second]]
        check(fourth == second, f"M4=M2 p={p} k={k}")
        if source in expected2:
            expected_depth = 0
            check(edge[edge[source]] == source, f"core inversion p={p} k={k}")
        elif source in expected1:
            expected_depth = 1
        else:
            expected_depth = 2
        depth_hist[expected_depth] += 1
        if edge[source] == source:
            fixed += 1
    check(depth_hist == Counter({0: comb(p - 1, k - 2),
                                 1: comb(p - 1, k - 1),
                                 2: comb(p, k)}),
          f"depth census p={p} k={k}")
    expected_fixed_count = 1 if p == 2 else predicted_fixed(p, k)
    check(fixed == expected_fixed_count, f"fixed count p={p} k={k}")

    fibre_hist = Counter()
    maximum_targets = []
    maximum = p - k + 2
    for target in states:
        actual = set(fibres[target])
        if not (target & infinity_bit):
            predicted = set()
        else:
            height = predicted_height(target, p)
            predicted = {transform(target, a, p, inverse=True) for a in range(height)}
            check(sorted(marked[target]) == list(range(height)),
                  f"pivot interval p={p} k={k} target={target}")
            for a, source in enumerate(sorted(predicted, key=lambda x: step(x, p)[1])):
                check(step(source, p)[1] == a, f"least pivot p={p} k={k} a={a}")
                check(step(source, p)[0] == target, f"inverse edge p={p} k={k} a={a}")
        check(actual == predicted, f"every-target fibre p={p} k={k} target={target}")
        fibre_hist[len(actual)] += 1
        if len(actual) == maximum:
            maximum_targets.append(target)

    check(fibre_hist[0] == comb(p, k), f"zero fibres p={p} k={k}")
    for q in range(1, p + 1):
        check(fibre_hist[q] == comb(p - q, k - 2) if p - q >= k - 2 else fibre_hist[q] == 0,
              f"positive distribution p={p} k={k} q={q}")
    check(len(maximum_targets) == 1, f"unique max target p={p} k={k}")
    check(sum(size * count for size, count in fibre_hist.items()) == len(states),
          f"fibre mass p={p} k={k}")
    return len(states), fixed, maximum


def main() -> None:
    print("P174 HOSTILE REVIEW A INDEPENDENT CONTROL")
    print("STATUS HOLD_EXTERNAL")
    boxes = 0
    states = 0
    for p in (2, 3, 5, 7, 11, 13):
        for k in range(2, p + 1):
            count, fixed, maximum = audit_box(p, k)
            boxes += 1
            states += count
            print(f"p={p} k={k} states={count} fixed={fixed} max_fibre={maximum} PASS")
    print(f"BOXES {boxes}")
    print(f"STATES {states}")
    print(f"ASSERTIONS {CHECKS}")
    print("RESULT PASS")


if __name__ == "__main__":
    main()
