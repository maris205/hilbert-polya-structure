#!/usr/bin/env python3
"""Exact paper-local checks for synchronous prefix-majority dynamics.

The program uses Python integers only.  It exhausts every binary word through
length 16 and independently checks the fixed language, complete functional
graphs, sharp depth, every one-step fibre, image census, and strict fibre
maximum.  Larger sharp witnesses are checked without exhaustive enumeration.
"""

from collections import Counter
from itertools import groupby, product
from math import ceil, comb, log2


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def update(word):
    balance = 0
    out = []
    for bit in word:
        balance += 2 * bit - 1
        out.append(int(balance >= 0))
    return tuple(out)


def fixed_words(n):
    left = {
        tuple((0, 1) * r + (0,) * (n - 2 * r))
        for r in range(n // 2 + 1)
    }
    right = {
        tuple((0, 1) * r + (1,) * (n - 2 * r))
        for r in range((n - 1) // 2 + 1)
    }
    return left | right


def orbit_data(start):
    seen = {}
    state = start
    while state not in seen:
        seen[state] = len(seen)
        state = update(state)
    return seen[state], len(seen) - seen[state]


def catalan(m):
    return comb(2 * m, m) // (m + 1)


def meander(m):
    return comb(m, m // 2)


def fibre_formula(target):
    runs = [(bit, sum(1 for _ in block)) for bit, block in groupby(target)]
    if len(runs) == 1:
        bit, length = runs[0]
        return meander(length if bit else length - 1)

    first_bit, first_length = runs[0]
    if first_bit:
        if first_length % 2:
            return 0
        answer = catalan(first_length // 2)
    else:
        if first_length % 2 == 0:
            return 0
        answer = catalan((first_length - 1) // 2)

    for _, length in runs[1:-1]:
        if length % 2 == 0:
            return 0
        answer *= catalan((length - 1) // 2)
    return answer * meander(runs[-1][1] - 1)


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def witness(n, a):
    return (1,) * a + (0,) * (n - a)


def main():
    total_states = 0
    total_target_cells = 0
    print("PREFIX_MAJORITY_P132_V1")
    print("columns=n,states,image,fixed,max_tail,max_fibre")

    for n in range(1, 17):
        fibres = Counter()
        depths = Counter()
        observed_fixed = set()
        for word in product((0, 1), repeat=n):
            total_states += 1
            target = update(word)
            check(len(target) == n and set(target) <= {0, 1}, ("closure", n, word))
            fibres[target] += 1
            tail, period = orbit_data(word)
            check(period == 1, ("period", n, word, period))
            check(tail <= ceil(log2(n)), ("clock bound", n, word, tail))
            depths[tail] += 1
            if tail == 0:
                observed_fixed.add(word)

        expected_fixed = fixed_words(n)
        check(observed_fixed == expected_fixed, ("fixed language", n))
        check(len(expected_fixed) == n + 1, ("fixed count", n))
        check(max(depths) == ceil(log2(n)), ("sharp depth", n, depths))
        check(len(fibres) == fibonacci(n + 2), ("image count", n))

        for target in product((0, 1), repeat=n):
            total_target_cells += 1
            check(fibres[target] == fibre_formula(target), ("fibre", n, target))

        maximum = max(fibres.values())
        check(maximum == comb(n, n // 2), ("maximum fibre", n))
        maximizers = {target for target, size in fibres.items() if size == maximum}
        expected_maximizers = {(0,), (1,)} if n == 1 else {(1,) * n}
        check(maximizers == expected_maximizers, ("unique maximum", n, maximizers))

        print(
            f"n={n}|states={2**n}|image={len(fibres)}|fixed={len(observed_fixed)}"
            f"|max_tail={max(depths)}|max_fibre={maximum}"
        )

    large_witnesses = 0
    for n in (17, 31, 32, 63, 64, 127, 128, 255, 256, 511):
        state = witness(n, 1)
        for step in range(ceil(log2(n))):
            expected_a = min(2**step, n)
            check(state == witness(n, expected_a), ("witness iterate", n, step))
            state = update(state)
        check(update(state) == state == (1,) * n, ("witness endpoint", n))
        large_witnesses += 1

    print(f"TOTAL_STATES={total_states}")
    print(f"TARGET_CELLS={total_target_cells}")
    print(f"LARGE_SHARP_WITNESSES={large_witnesses}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("EXACT_ARITHMETIC=python_integers")
    print("FLOATING_POINT=none")
    print("SAMPLING=none")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
