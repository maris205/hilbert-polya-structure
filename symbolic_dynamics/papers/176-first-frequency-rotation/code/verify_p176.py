#!/usr/bin/env python3
"""Paper-local author/scout-derived regression control for first-frequency rotation.

Carrier: binary words w of length n.  If the first symbol occurs c times,
rotate w left by c.  The verifier checks the literal functional graph against
a separate pointed-necklace prediction path, a target-resolved inverse formula,
the complete possible-period inventory, the sharp clock, and a fixed-point
Möbius census.  Finite checks are falsifiers and regression controls, not proofs.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import comb, gcd


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def divisors(n: int):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def mobius(n: int) -> int:
    prime_count = 0
    p = 2
    remaining = n
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            prime_count += 1
            if remaining % p == 0:
                return 0
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def rotate(word, amount: int):
    if not word:
        return word
    amount %= len(word)
    return word[amount:] + word[:amount]


def step(word):
    if not word:
        return word
    return rotate(word, word.count(word[0]))


def least_period(word) -> int:
    n = len(word)
    return next(
        d
        for d in divisors(n)
        if all(word[index] == word[index % d] for index in range(n))
    )


def functional_data(states, successor):
    orbit = {}
    cycle_count = Counter()
    for start in states:
        if start in orbit:
            continue
        path = []
        position = {}
        point = start
        while point not in orbit and point not in position:
            position[point] = len(path)
            path.append(point)
            point = successor[point]
        if point in position:
            cycle_start = position[point]
            period = len(path) - cycle_start
            cycle_count[period] += 1
            for state in path[cycle_start:]:
                orbit[state] = (0, period)
            path = path[:cycle_start]
        for state in reversed(path):
            tail, period = orbit[successor[state]]
            orbit[state] = (tail + 1, period)
    check(len(orbit) == len(states), "functional coverage")
    return orbit, cycle_count


def predicted_preimages(target):
    """The two labelled inverse branches, with absent colours suppressed."""
    n = len(target)
    k = sum(target)
    if k == 0 or k == n:
        return {target}
    candidates = set()
    # A source beginning in 1 rotates by k.
    source_one = rotate(target, -k)
    if source_one[0] == 1:
        candidates.add(source_one)
    # A source beginning in 0 rotates by n-k.
    source_zero = rotate(target, -(n - k))
    if source_zero[0] == 0:
        candidates.add(source_zero)
    return candidates


def predicted_fibre_histogram(n: int):
    histogram = Counter()
    # The two constant targets each have their unique constant source.
    histogram[1] += 2
    for k in range(1, n):
        if (2 * k) % n == 0:
            histogram[1] += comb(n, k)
        else:
            corner = comb(n - 2, k - 1)
            histogram[0] += corner
            histogram[2] += corner
            histogram[1] += comb(n, k) - 2 * corner
    return histogram


def primitive_weight_count(length: int, weight: int) -> int:
    """Linear binary words of least period length and indicated weight."""
    return sum(
        mobius(e) * comb(length // e, weight // e)
        for e in divisors(gcd(length, weight))
    )


def predicted_fixed_count(n: int) -> int:
    total = 0
    for d in divisors(n):
        repetitions = n // d
        for block_weight in range(d + 1):
            if (repetitions * block_weight) % d == 0:
                total += primitive_weight_count(d, block_weight)
    return total


def longest_cyclic_run(bits) -> int:
    if len(set(bits)) == 1:
        return len(bits)
    doubled = bits + bits
    best = run = 1
    for index in range(1, len(doubled)):
        if doubled[index] == doubled[index - 1]:
            run += 1
        else:
            run = 1
        best = max(best, run)
    return min(best, len(bits) - 1)


def component_prediction(representative):
    """Predict the pointed-necklace graph from generator cycles.

    The representative is an n-letter word; only its d distinct rotations
    matter, where d is its least period.  On Z/d, a 1 takes +k and a 0 takes
    -k, because n-k is congruent to -k modulo d.
    """
    n = len(representative)
    d = least_period(representative)
    k = sum(representative)
    generator_gcd = gcd(k, d)
    component_length = d // generator_gcd
    cycles = Counter()
    maximum_tail = 0

    for residue in range(generator_gcd):
        positions = tuple((residue + offset * k) % d for offset in range(component_length))
        bits = tuple(representative[position] for position in positions)
        check(len(set(positions)) == component_length, "generator component size")
        if component_length == 1:
            cycles[1] += 1
        elif component_length == 2:
            # +k and -k are the same neighbour on a two-cycle.
            cycles[2] += 1
        elif len(set(bits)) == 1:
            cycles[component_length] += 1
        else:
            cycles[2] += sum(
                bits[index] == 1 and bits[(index + 1) % component_length] == 0
                for index in range(component_length)
            )
            maximum_tail = max(maximum_tail, longest_cyclic_run(bits) - 1)
    return maximum_tail, cycles


def audit_rotation_classes(n: int, states, successor, orbit_data) -> None:
    seen = set()
    for representative in states:
        if representative in seen:
            continue
        d = least_period(representative)
        rotations = tuple(rotate(representative, shift) for shift in range(d))
        check(len(set(rotations)) == d, "distinct pointed necklace states")
        seen.update(rotations)

        index_of = {word: index for index, word in enumerate(rotations)}
        local_successor = {}
        k = sum(representative)
        for index, word in enumerate(rotations):
            predicted_index = (index + (k if word[0] else n - k)) % d
            check(successor[word] == rotations[predicted_index], "pointed-necklace conjugacy")
            local_successor[index] = index_of[successor[word]]

        local_orbit, local_cycles = functional_data(tuple(range(d)), local_successor)
        predicted_tail, predicted_cycles = component_prediction(representative)
        check(max(tail for tail, _ in local_orbit.values()) == predicted_tail, "component tail formula")
        check(local_cycles == predicted_cycles, "component cycle classification")
        for word in rotations:
            check(orbit_data[word] == local_orbit[index_of[word]], "global/local orbit agreement")
    check(len(seen) == len(states), "rotation-class coverage")


def possible_periods(n: int):
    if n == 1:
        return {1}
    return {1, 2} | {d for d in divisors(n) if 3 <= d < n}


def audit_order(n: int) -> str:
    states = tuple(product((0, 1), repeat=n))
    successor = {word: step(word) for word in states}
    reverse = {target: set() for target in states}
    for source, target in successor.items():
        check(len(target) == n and set(target) <= {0, 1}, "carrier closure")
        check(sum(source) == sum(target), "weight preservation")
        reverse[target].add(source)

    for target in states:
        check(reverse[target] == predicted_preimages(target), "labelled inverse formula")

    literal_fibres = Counter(len(reverse[target]) for target in states)
    expected_fibres = predicted_fibre_histogram(n)
    check(literal_fibres == expected_fibres, "fibre histogram formula")

    orbit_data, cycle_count = functional_data(states, successor)
    audit_rotation_classes(n, states, successor, orbit_data)

    maximum_tail = max(tail for tail, _ in orbit_data.values())
    expected_tail = max(0, n - 2)
    check(maximum_tail == expected_tail, "sharp global clock")
    deepest = sum(tail == maximum_tail for tail, _ in orbit_data.values())
    expected_deepest = len(states) if n == 1 else (4 if n == 2 else 2)
    check(deepest == expected_deepest, "deepest-state census")

    periods = {period for _, period in orbit_data.values()}
    check(periods == possible_periods(n), "complete possible-period inventory")
    fixed = sum(successor[word] == word for word in states)
    check(fixed == predicted_fixed_count(n), "fixed-point Mobius census")

    image = sum(size > 0 for size, count in literal_fibres.items() for _ in range(count))
    # The expanded expression above deliberately counts target states, not
    # merely the number of fibre sizes represented.
    check(image == len(set(successor.values())), "image census")
    return (
        f"n={n} states={len(states)} image={image} fixed={fixed} "
        f"tail={maximum_tail} deepest={deepest} periods={sorted(periods)} "
        f"cycles={dict(sorted(cycle_count.items()))} "
        f"fibres={dict(sorted(literal_fibres.items()))}"
    )


def main() -> None:
    print("P176 FIRST-FREQUENCY ROTATION AUTHOR/SCOUT-DERIVED REGRESSION CONTROL")
    print("STATUS AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL")
    rows = []
    for n in range(1, 19):
        rows.append(audit_order(n))
    for row in rows:
        print(row)
    print("THEOREM pointed-necklace generator decomposition PASS")
    print("THEOREM every-target two-branch fibre PASS")
    print("THEOREM possible periods and sharp n-2 clock PASS")
    print("THEOREM deepest census two for n>=3 PASS")
    print("THEOREM fixed-point Mobius census PASS")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("AUTHOR_REGRESSION PASS")


if __name__ == "__main__":
    main()
