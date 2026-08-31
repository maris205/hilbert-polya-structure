#!/usr/bin/env python3
"""Independent hostile audit for the two combinatorial P132--P136 finalists.

This deliberately does not import either candidate verifier.  Prefix-majority
is recomputed from literal prefix sums.  Border arrays are recomputed by a
literal prefix/suffix search.  Exhaustive ranges are smaller than the frozen
candidate audits because the point is implementation independence, not a
second copy of their optimized enumeration.
"""

from __future__ import annotations

from collections import Counter
from itertools import groupby, product
from math import ceil, comb, factorial, log2
from random import Random


CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def literal_prefix_majority(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        int(2 * sum(word[: i + 1]) >= i + 1) for i in range(len(word))
    )


def pm_fixed(n: int) -> set[tuple[int, ...]]:
    left = {
        tuple((0, 1) * r + (0,) * (n - 2 * r))
        for r in range(n // 2 + 1)
    }
    right = {
        tuple((0, 1) * r + (1,) * (n - 2 * r))
        for r in range((n - 1) // 2 + 1)
    }
    return left | right


def orbit_data(start: tuple[int, ...], update) -> tuple[int, int]:
    seen: dict[tuple[int, ...], int] = {}
    current = start
    while current not in seen:
        seen[current] = len(seen)
        current = update(current)
    return seen[current], len(seen) - seen[current]


def catalan(m: int) -> int:
    return comb(2 * m, m) // (m + 1)


def meander(m: int) -> int:
    return comb(m, m // 2)


def pm_fibre_formula(target: tuple[int, ...]) -> int:
    run_data = [(bit, sum(1 for _ in run)) for bit, run in groupby(target)]
    if len(run_data) == 1:
        bit, length = run_data[0]
        return meander(length if bit else length - 1)
    first_bit, first_length = run_data[0]
    if first_bit:
        if first_length % 2:
            return 0
        answer = catalan(first_length // 2)
    else:
        if first_length % 2 == 0:
            return 0
        answer = catalan((first_length - 1) // 2)
    for _, length in run_data[1:-1]:
        if length % 2 == 0:
            return 0
        answer *= catalan((length - 1) // 2)
    return answer * meander(run_data[-1][1] - 1)


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def audit_prefix_majority() -> tuple[int, int]:
    states = 0
    for n in range(1, 15):
        fibres: Counter[tuple[int, ...]] = Counter()
        maximum_depth = 0
        fixed = pm_fixed(n)
        for word in product((0, 1), repeat=n):
            states += 1
            image = literal_prefix_majority(word)
            fibres[image] += 1
            tail, period = orbit_data(word, literal_prefix_majority)
            check(period == 1, f"PM period at n={n}, word={word}")
            maximum_depth = max(maximum_depth, tail)
            check((image == word) == (word in fixed), f"PM fixed at n={n}")
        check(len(fixed) == n + 1, f"PM fixed count at n={n}")
        check(maximum_depth == ceil(log2(n)), f"PM depth at n={n}")
        check(len(fibres) == fib(n + 2), f"PM image at n={n}")
        for target in product((0, 1), repeat=n):
            check(
                fibres[target] == pm_fibre_formula(target),
                f"PM fibre at n={n}, target={target}",
            )
        maximum = max(fibres.values())
        maximizers = {target for target, size in fibres.items() if size == maximum}
        check(maximum == comb(n, n // 2), f"PM maximum fibre at n={n}")
        expected = set(product((0, 1), repeat=1)) if n == 1 else {(1,) * n}
        check(maximizers == expected, f"PM maximizers at n={n}")

    rng = Random(132136)
    random_cases = 0
    for n in (15, 31, 64, 127, 256):
        witness = (1,) + (0,) * (n - 1)
        tail, period = orbit_data(witness, literal_prefix_majority)
        check((tail, period) == (ceil(log2(n)), 1), f"PM sharp witness n={n}")
        for _ in range(250):
            word = tuple(rng.randrange(2) for _ in range(n))
            tail, period = orbit_data(word, literal_prefix_majority)
            check(period == 1 and tail <= ceil(log2(n)), f"PM random n={n}")
            random_cases += 1
    return states, random_cases


def literal_border_array(word: tuple[int, ...]) -> tuple[int, ...]:
    answer = []
    for end in range(len(word)):
        prefix = word[: end + 1]
        best = 0
        for length in range(1, end + 1):
            if prefix[:length] == prefix[-length:]:
                best = length
        answer.append(best)
    return tuple(answer)


def inversion_sequences(n: int):
    return product(*(range(i + 1) for i in range(n)))


def a_template(n: int, r: int) -> tuple[int, ...]:
    return tuple(i if i <= r else 0 for i in range(n))


def b_template(n: int, k: int) -> tuple[int, ...]:
    return tuple(0 if i < k else 1 for i in range(n))


def border_recurrent(n: int) -> set[tuple[int, ...]]:
    if n == 1:
        return {(0,)}
    return {
        template
        for r in range(1, n)
        for template in (a_template(n, r), b_template(n, r + 1))
    }


def canonical_info(array: tuple[int, ...]):
    n = len(array)
    if n == 1:
        return "S", 0, (0,), n
    if array[1] == 1:
        r = 1
        while r + 1 < n and array[r + 1] == r + 1:
            r += 1
        kind, parameter, template = "A", r, a_template(n, r)
    else:
        k = next((i for i in range(1, n) if array[i] != 0), n)
        kind, parameter, template = "B", k, b_template(n, k)
    agreement = next(
        (i for i, (left, right) in enumerate(zip(array, template)) if left != right),
        n,
    )
    return kind, parameter, template, agreement


def audit_border_arrays() -> tuple[int, int]:
    states = 0
    for n in range(1, 9):
        fibres: Counter[tuple[int, ...]] = Counter()
        image: set[tuple[int, ...]] = set()
        observed_recurrent: set[tuple[int, ...]] = set()
        maximum_tail = 0
        for state in inversion_sequences(n):
            states += 1
            target = literal_border_array(state)
            fibres[target] += 1
            image.add(target)
            tail, period = orbit_data(state, literal_border_array)
            maximum_tail = max(maximum_tail, tail)
            check(period == (1 if n == 1 else 2), f"BA period at n={n}")
            if tail == 0:
                observed_recurrent.add(state)
        check(observed_recurrent == border_recurrent(n), f"BA recurrent n={n}")
        expected_depth = 0 if n <= 2 else (1 if n == 3 else 2 * n - 4)
        check(maximum_tail == expected_depth, f"BA depth n={n}")
        maximum = max(fibres.values())
        check(maximum == factorial(n - 1), f"BA maximum fibre n={n}")
        maximizers = {target for target, size in fibres.items() if size == maximum}
        expected_targets = {(0,)} if n == 1 else {
            (0,) * n,
            a_template(n, 1),
        }
        check(maximizers == expected_targets, f"BA maximizers n={n}")

        for table in image:
            if n == 1:
                continue
            kind, parameter, _, agreement = canonical_info(table)
            successor = literal_border_array(table)
            next_kind, next_parameter, _, next_agreement = canonical_info(successor)
            expected_partner = (
                ("B", parameter + 1) if kind == "A" else ("A", parameter - 1)
            )
            check((next_kind, next_parameter) == expected_partner, f"BA partner n={n}")
            if agreement == n:
                check(next_agreement == n, f"BA recurrent partner n={n}")
                continue
            check(agreement >= 3, f"BA short mismatch n={n}")
            actual = table[agreement]
            if kind == "A":
                check(actual == 1, f"BA A mismatch n={n}")
                check(next_agreement == agreement, f"BA A1 agreement n={n}")
                check(successor[next_agreement] == 2, f"BA A1 to B2 n={n}")
            elif actual == 0:
                check(next_agreement == agreement, f"BA B0 agreement n={n}")
                check(successor[next_agreement] == 1, f"BA B0 to A1 n={n}")
            else:
                check(actual == 2, f"BA B mismatch n={n}")
                check(next_agreement > agreement, f"BA B2 extension n={n}")

    witness_cases = 0
    for n in range(4, 31):
        source = (0, 1, 0, 2) + (1,) * (n - 4)
        valid = (0, 0, 1) + (0,) * (n - 3)
        source_tail, source_period = orbit_data(source, literal_border_array)
        valid_tail, valid_period = orbit_data(valid, literal_border_array)
        check((source_tail, source_period) == (2 * n - 4, 2), f"BA source witness n={n}")
        check((valid_tail, valid_period) == (2 * n - 5, 2), f"BA valid witness n={n}")
        witness_cases += 2
    return states, witness_cases


def main() -> None:
    pm_states, pm_random = audit_prefix_majority()
    ba_states, ba_witnesses = audit_border_arrays()
    print("INDEPENDENT HOSTILE AUDIT: PASS")
    print(f"prefix_majority_exhaustive_states={pm_states}")
    print(f"prefix_majority_random_cases={pm_random}")
    print(f"border_array_exhaustive_states={ba_states}")
    print(f"border_array_large_witness_cases={ba_witnesses}")
    print(f"checks={CHECKS}")
    print("scope=independent falsification only; all-n claims require proof")


if __name__ == "__main__":
    main()
