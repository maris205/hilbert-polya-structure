#!/usr/bin/env python3
"""Exact small-box regression checks for P188."""

from collections import Counter
from itertools import combinations_with_replacement
from math import comb


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def prefix_mask(k):
    return (1 << k) - 1


def update(mask):
    return mask & prefix_mask(mask.bit_count())


def rho(mask, n):
    r = 0
    while r < n and mask & (1 << r):
        r += 1
    return r


def orbit(mask):
    seen = set()
    state = mask
    tail = 0
    while update(state) != state:
        check(state not in seen, "unexpected cycle")
        seen.add(state)
        state = update(state)
        tail += 1
    return tail, state


def one_step_formula(target, n):
    b = target.bit_count()
    maximum = target.bit_length()
    lo = max(b, maximum)
    hi = (n + b) // 2
    return sum(comb(n - k, k - b) for k in range(lo, hi + 1))


def all_time_formula(target, n, t):
    if t == 0:
        return 1
    b = target.bit_count()
    lower = max(b, target.bit_length())
    total = 0
    for increasing in combinations_with_replacement(range(lower, n + 1), t):
        chain = tuple(reversed(increasing))
        extended = chain + (b,)
        next_rank = chain[1] if t > 1 else b
        ways = comb(n - chain[0], chain[0] - next_rank)
        for j in range(1, t):
            ways *= comb(chain[j - 1] - chain[j],
                         chain[j] - extended[j + 1])
        total += ways
    return total


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def run_boxes():
    signatures = []
    for n in range(0, 19):
        states = range(1 << n)
        fibres = Counter(update(mask) for mask in states)
        endpoints = Counter()
        depths = Counter()
        deepest = []
        maximum_tail = -1
        for mask in states:
            tail, endpoint = orbit(mask)
            depths[tail] += 1
            endpoints[endpoint] += 1
            r = rho(mask, n)
            check(endpoint == prefix_mask(r), "terminal initial segment")
            check(update(endpoint) == endpoint, "terminal fixed")

            source = mask
            k = mask.bit_count()
            for _t in range(1, n + 2):
                predicted = mask & prefix_mask(k)
                source = update(source)
                check(source == predicted, "all-time iterate")
                k = (mask & prefix_mask(k)).bit_count()

            if tail > maximum_tail:
                maximum_tail = tail
                deepest = [mask]
            elif tail == maximum_tail:
                deepest.append(mask)

        expected_height = max(0, n - 1)
        check(maximum_tail == expected_height, "sharp height")
        if n >= 2:
            check(deepest == [prefix_mask(n) ^ 1], "unique deepest state")
        else:
            check(deepest == list(states), "small deepest boundary")

        image_count = 0
        mass = 0
        for target in states:
            formula = one_step_formula(target, n)
            check(formula == fibres[target], "every-target one-step fibre")
            condition = 2 * target.bit_length() <= n + target.bit_count()
            check((formula > 0) == condition, "image criterion")
            image_count += formula > 0
            mass += formula
        check(mass == 1 << n, "one-step mass")
        check(image_count == fibonacci(n + 2), "Fibonacci image count")
        check(fibres[0] == fibonacci(n + 1), "empty-target Fibonacci fibre")
        for b in range(n + 1):
            layer = sum(
                fibres[target] > 0
                for target in states if target.bit_count() == b
            )
            check(layer == comb((n + b) // 2, b), "image size layer")
        largest = max(fibres.values())
        check(largest == fibonacci(n + 1), "largest fibre size")
        if n >= 2:
            check([target for target in states if fibres[target] == largest]
                  == [0], "unique largest fibre")

        for r in range(n + 1):
            endpoint = prefix_mask(r)
            expected = 1 if r == n else 1 << (n - r - 1)
            check(endpoints[endpoint] == expected, "terminal fibre")
        check(sum(endpoints.values()) == 1 << n, "terminal mass")
        check(len([x for x in states if update(x) == x]) == n + 1,
              "fixed count")
        if n <= 9:
            current = list(states)
            for t in range(0, min(4, n + 1) + 1):
                actual = Counter(current)
                predicted_mass = 0
                for target in states:
                    predicted = all_time_formula(target, n, t)
                    check(predicted == actual[target],
                          "all-time every-target fibre")
                    predicted_mass += predicted
                check(predicted_mass == 1 << n, "all-time fibre mass")
                current = [update(x) for x in current]
        signatures.append((n, 1 << n, maximum_tail, image_count,
                           fibres[0], len(depths)))
    return signatures


def main():
    signatures = run_boxes()
    print("P188 exact author control")
    print("status=PASS")
    print(f"boxes={len(signatures)} last={signatures[-1]}")
    print(f"assertions={ASSERTIONS}")
    print("finite_checks_are_not_proof_or_novelty=true")


if __name__ == "__main__":
    main()
