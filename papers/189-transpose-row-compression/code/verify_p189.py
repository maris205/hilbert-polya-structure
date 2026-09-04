#!/usr/bin/env python3
"""Independent author audit for transpose--row-compression dynamics.

The literal matrix transition is implemented directly from entries.  Closed
forms, image recognizers, partition conjugation, depth predicates, and fibre
formulae are separate functions.  No scouting or earlier-paper module is
imported.  One assertion is one call to Audit.check.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations_with_replacement
from math import comb, factorial, prod


class Audit:
    def __init__(self) -> None:
        self.count = 0

    def check(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(label)


AUDIT = Audit()


def bit(mask: int, n: int, row: int, column: int) -> int:
    return (mask >> (row * n + column)) & 1


def row_sums(mask: int, n: int) -> tuple[int, ...]:
    return tuple(sum(bit(mask, n, i, j) for j in range(n)) for i in range(n))


def diagram(heights: tuple[int, ...], n: int) -> int:
    """Matrix whose j-th column is an initial segment of height heights[j]."""
    answer = 0
    for i in range(n):
        for j, height in enumerate(heights):
            if i < height:
                answer |= 1 << (i * n + j)
    return answer


def update(mask: int, n: int) -> int:
    """Literal update, expressed only through source entries and the rule."""
    answer = 0
    for j in range(n):
        source_row_sum = sum(bit(mask, n, j, k) for k in range(n))
        for i in range(n):
            if i < source_row_sum:
                answer |= 1 << (i * n + j)
    return answer


def conjugate(vector: tuple[int, ...], n: int) -> tuple[int, ...]:
    return tuple(sum(value >= level for value in vector)
                 for level in range(1, n + 1))


def decreasing(vector: tuple[int, ...]) -> bool:
    return all(vector[i] >= vector[i + 1] for i in range(len(vector) - 1))


def column_heights(mask: int, n: int):
    heights = []
    for j in range(n):
        height = 0
        while height < n and bit(mask, n, height, j):
            height += 1
        if any(bit(mask, n, i, j) for i in range(height, n)):
            return None
        heights.append(height)
    return tuple(heights)


def recurrent(mask: int, n: int) -> bool:
    heights = column_heights(mask, n)
    return heights is not None and decreasing(heights)


def predicted_depth(mask: int, n: int) -> int:
    if recurrent(mask, n):
        return 0
    if decreasing(row_sums(mask, n)):
        return 1
    return 2


def first_fibre_formula(target: int, n: int) -> int:
    heights = column_heights(target, n)
    if heights is None:
        return 0
    return prod(comb(n, height) for height in heights)


def second_fibre_formula(target: int, n: int) -> int:
    heights = column_heights(target, n)
    if heights is None or not decreasing(heights):
        return 0
    required_row_multiset = conjugate(heights, n)
    multiplicities = Counter(required_row_multiset)
    arrangements = factorial(n) // prod(factorial(value)
                                         for value in multiplicities.values())
    row_supports = prod(comb(n, value) for value in required_row_multiset)
    return arrangements * row_supports


def partitions_in_square(n: int):
    for weakly_increasing in combinations_with_replacement(range(n + 1), n):
        yield tuple(reversed(weakly_increasing))


def weak_row_sum_population(n: int) -> int:
    """Coefficient [z^n] product_k (1-C(n,k)z)^(-1)."""
    coefficients = [1] + [0] * n
    for k in range(n + 1):
        weight = comb(n, k)
        nxt = [0] * (n + 1)
        for old_degree, old_value in enumerate(coefficients):
            for multiplicity in range(n - old_degree + 1):
                nxt[old_degree + multiplicity] += old_value * weight ** multiplicity
        coefficients = nxt
    return coefficients[n]


def exhaustive_box(n: int):
    states = 1 << (n * n)
    first_fibres = Counter()
    second_fibres = Counter()
    observed_depths = Counter()
    fixed = 0
    recurrent_count = 0
    mapping_bytes = bytearray()

    for mask in range(states):
        sums = row_sums(mask, n)
        sorted_sums = tuple(sorted(sums, reverse=True))
        first = update(mask, n)
        second = update(first, n)
        third = update(second, n)
        fourth = update(third, n)

        predicted = (
            diagram(sums, n),
            diagram(conjugate(sums, n), n),
            diagram(sorted_sums, n),
            diagram(conjugate(sums, n), n),
        )
        literal = (first, second, third, fourth)
        for epoch in range(4):
            AUDIT.check(literal[epoch] == predicted[epoch],
                        f"closed form at epoch {epoch + 1}")
            for i in range(n):
                for j in range(n):
                    AUDIT.check(bit(literal[epoch], n, i, j) ==
                                bit(predicted[epoch], n, i, j),
                                "entrywise closed form")

        AUDIT.check(fourth == second, "F^4=F^2")
        AUDIT.check(update(fourth, n) == third, "post-height odd phase")
        AUDIT.check(update(update(fourth, n), n) == fourth,
                    "post-height even phase")
        AUDIT.check(column_heights(first, n) == sums, "time-one decoder")
        AUDIT.check(column_heights(second, n) == conjugate(sums, n),
                    "time-two decoder")
        AUDIT.check(conjugate(conjugate(sums, n), n) == sorted_sums,
                    "double conjugation sorts")

        literal_recurrent = second == mask
        AUDIT.check(literal_recurrent == recurrent(mask, n),
                    "recurrent recognizer")
        if literal_recurrent:
            recurrent_count += 1
            AUDIT.check(update(update(mask, n), n) == mask,
                        "recurrent period divides two")
        if first == mask:
            fixed += 1
            heights = column_heights(mask, n)
            AUDIT.check(heights is not None and
                        heights == conjugate(heights, n),
                        "fixed/self-conjugate equivalence")

        orbit = mask
        observed_depth = None
        for depth in range(3):
            if recurrent(orbit, n):
                observed_depth = depth
                break
            orbit = update(orbit, n)
        AUDIT.check(observed_depth is not None, "depth exceeds two")
        AUDIT.check(observed_depth == predicted_depth(mask, n),
                    "exact depth predicate")
        observed_depths[observed_depth] += 1

        first_fibres[first] += 1
        second_fibres[second] += 1
        mapping_bytes.extend(first.to_bytes((n * n + 7) // 8, "little"))

    for target in range(states):
        AUDIT.check(first_fibres[target] == first_fibre_formula(target, n),
                    "time-one every-target fibre")
        AUDIT.check(second_fibres[target] == second_fibre_formula(target, n),
                    "time-two every-target fibre")
    AUDIT.check(sum(first_fibres.values()) == states, "time-one fibre mass")
    AUDIT.check(sum(second_fibres.values()) == states, "time-two fibre mass")
    AUDIT.check(len(first_fibres) == (n + 1) ** n, "time-one image count")
    AUDIT.check(len(second_fibres) == comb(2 * n, n), "time-two image count")
    AUDIT.check(recurrent_count == comb(2 * n, n), "recurrent count")
    AUDIT.check(fixed == 2 ** n, "self-conjugate fixed count")
    AUDIT.check((recurrent_count - fixed) % 2 == 0, "two-cycle parity")

    weak = weak_row_sum_population(n)
    expected_depths = {
        0: comb(2 * n, n),
        1: weak - comb(2 * n, n),
        2: states - weak,
    }
    AUDIT.check(dict(observed_depths) ==
                {key: value for key, value in expected_depths.items() if value},
                "depth population formula")
    if n == 1:
        AUDIT.check(expected_depths == {0: 2, 1: 0, 2: 0},
                    "n=1 boundary")
    else:
        AUDIT.check(expected_depths[1] > 0 and expected_depths[2] > 0,
                    "strict height-two realization")

    return {
        "n": n,
        "states": states,
        "image1": len(first_fibres),
        "image2": len(second_fibres),
        "recurrent": recurrent_count,
        "fixed": fixed,
        "cycles2": (recurrent_count - fixed) // 2,
        "depths": tuple(expected_depths.values()),
        "max_fibre1": max(first_fibres.values()),
        "max_fibre2": max(second_fibres.values()),
        "digest": sha256(mapping_bytes).hexdigest()[:20],
    }


def transfer_checks():
    rows = []
    for n in range(1, 13):
        weak = weak_row_sum_population(n)
        AUDIT.check(comb(2 * n, n) <= weak <= 2 ** (n * n),
                    "depth CDF bounds")
        if n <= 9:
            AUDIT.check(weak == sum(
                prod(comb(n, part) for part in partition)
                for partition in partitions_in_square(n)
            ), "partition sum versus coefficient")
        rows.append((n, comb(2 * n, n), 2 ** n, weak,
                     2 ** (n * n) - weak))
    return rows


def inverse_mass_and_conjugation_checks():
    rows = []
    for n in range(1, 10):
        partitions = list(partitions_in_square(n))
        AUDIT.check(len(partitions) == comb(2 * n, n),
                    "rectangle partition census")
        self_conjugate = 0
        second_mass = 0
        for heights in partitions:
            twice = conjugate(conjugate(heights, n), n)
            AUDIT.check(twice == heights, "partition conjugation involution")
            if conjugate(heights, n) == heights:
                self_conjugate += 1
            target = diagram(heights, n)
            AUDIT.check(column_heights(target, n) == heights,
                        "diagram-height injectivity")
            second_mass += second_fibre_formula(target, n)
        AUDIT.check(self_conjugate == 2 ** n,
                    "self-conjugate square partition census")
        AUDIT.check(second_mass == 2 ** (n * n),
                    "time-two formula total mass")
        first_mass = sum(comb(n, h) for h in range(n + 1)) ** n
        AUDIT.check(first_mass == 2 ** (n * n),
                    "time-one formula total mass")
        rows.append((n, len(partitions), self_conjugate, second_mass))
    return rows


def counterexample_attack():
    # Attack the tempting but false identities F^3=F and F^2=F, and the
    # tempting replacement of labelled row order by its multiset at time one.
    witnesses = {}
    for n in range(2, 5):
        for mask in range(1 << (n * n)):
            first = update(mask, n)
            second = update(first, n)
            third = update(second, n)
            if "F3_ne_F" not in witnesses and third != first:
                witnesses["F3_ne_F"] = (n, mask, first, third)
            if "F2_ne_F" not in witnesses and second != first:
                witnesses["F2_ne_F"] = (n, mask, first, second)
            if len(witnesses) == 2:
                break
        if len(witnesses) == 2:
            break
    AUDIT.check(set(witnesses) == {"F3_ne_F", "F2_ne_F"},
                "false-collapse witnesses missing")

    # Same row-sum multiset, different labelled order: time one differs but
    # time two agrees.  Matrices are built directly from the requested rows.
    n = 3
    a_rows = (0b101, 0b010, 0b000)  # row sums (2,1,0), non-left-justified
    b_rows = (0b000, 0b101, 0b010)  # row sums (0,2,1), a row permutation
    a = sum(row << (i * n) for i, row in enumerate(a_rows))
    b = sum(row << (i * n) for i, row in enumerate(b_rows))
    AUDIT.check(sorted(row_sums(a, n)) == sorted(row_sums(b, n)),
                "row-multiset attack setup")
    AUDIT.check(update(a, n) != update(b, n),
                "time one forgot labelled row order")
    AUDIT.check(update(update(a, n), n) == update(update(b, n), n),
                "time two did not forget labelled row order")
    AUDIT.check(predicted_depth(a, n) == 1 and predicted_depth(b, n) == 2,
                "labelled-order depth attack")

    # A hole below a zero in one column is outside both images and must have
    # zero fibre; the all-zero and all-one matrices test height 0 and n.
    hole = 1 << (1 * n + 0)
    AUDIT.check(column_heights(hole, n) is None, "hole recognizer")
    AUDIT.check(first_fibre_formula(hole, n) == 0, "hole first fibre")
    AUDIT.check(second_fibre_formula(hole, n) == 0, "hole second fibre")
    zero = 0
    full = (1 << (n * n)) - 1
    AUDIT.check(first_fibre_formula(zero, n) == 1, "zero-height boundary")
    AUDIT.check(first_fibre_formula(full, n) == 1, "full-height boundary")

    payload = repr(sorted(witnesses.items())).encode()
    return sha256(payload).hexdigest(), witnesses


def main() -> None:
    attack_digest, witnesses = counterexample_attack()
    print(f"counterexample_attack=PASS digest={attack_digest}")
    for name in sorted(witnesses):
        print(f"witness={name}:{witnesses[name]}")

    summaries = []
    for n in range(1, 5):
        before = AUDIT.count
        summary = exhaustive_box(n)
        summaries.append(summary)
        print(f"exhaustive n={n} assertions={AUDIT.count-before} summary={summary}")

    transfer = transfer_checks()
    print("transfer_rows=n,recurrent,fixed,depth_le_1,depth_2")
    for row in transfer:
        print("transfer=" + ",".join(map(str, row)))

    inverse = inverse_mass_and_conjugation_checks()
    print("inverse_rows=n,partitions,self_conjugate,time2_mass")
    for row in inverse:
        print("inverse=" + ",".join(map(str, row)))

    print(f"exact_assertions={AUDIT.count}")
    print("complete_matrix_carriers=n=1..4")
    print("partition_transfer=n=1..12;inverse_mass=n=1..9")
    print("status=PASS_INTERNAL")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
