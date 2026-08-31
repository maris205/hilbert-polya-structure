#!/usr/bin/env python3
"""Exact verifier for cyclic rotation of canonical finite CF digit words.

The carrier at weight N consists of positive compositions ending in a part at
least two.  Rotate the first digit to the end and apply the canonical identity
(...,b,1)=(...,b+1).  The script checks the proposed orbit normal form,
temporal layers, fibres, image, and recurrent-cycle formula through N=18.
"""

from __future__ import annotations

from collections import Counter
from math import comb, gcd


ASSERTIONS = 0


def check(condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message or f"assertion {ASSERTIONS} failed")


def compositions(n: int):
    if n == 0:
        yield ()
        return
    for first in range(1, n + 1):
        for rest in compositions(n - first):
            yield (first,) + rest


def states(n: int):
    return tuple(word for word in compositions(n) if word and word[-1] >= 2)


def update(word):
    if len(word) == 1:
        return word
    rotated = list(word[1:] + word[:1])
    if rotated[-1] == 1:
        rotated[-2] += 1
        rotated.pop()
    check(rotated and rotated[-1] >= 2)
    return tuple(rotated)


def tail_formula(word) -> int:
    return max((i + 1 for i, part in enumerate(word) if part == 1), default=0)


def terminal_core(word):
    if 1 not in word:
        return word
    k = len(word)
    nonones = [i for i, part in enumerate(word) if part > 1]
    values = {}
    for i in nonones:
        count = 0
        j = (i + 1) % k
        while word[j] == 1:
            count += 1
            j = (j + 1) % k
        values[i] = word[i] + count
    last_one = max(i for i, part in enumerate(word) if part == 1)
    start = last_one + 1
    ordered = [i for i in nonones if i >= start] + [i for i in nonones if i < start]
    return tuple(values[i] for i in ordered)


def primitive_rotation_period(word) -> int:
    for period in range(1, len(word) + 1):
        if len(word) % period == 0 and word == word[period:] + word[:period]:
            return period
    raise AssertionError("unreachable")


def orbit(word):
    seen = {}
    x = word
    while x not in seen:
        seen[x] = len(seen)
        x = update(x)
    return seen[x], len(seen) - seen[x], x


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def depth_count(n: int, depth: int) -> int:
    if depth == 0:
        return fibonacci(n - 1)
    degree = n - depth - 2
    if degree < 0:
        return 0
    if depth == 1:
        return fibonacci(degree + 1)
    return sum(
        comb(p + depth - 2, depth - 2) * fibonacci(degree - p + 1)
        for p in range(degree + 1)
    )


def euler_phi(n: int) -> int:
    answer = n
    p = 2
    remaining = n
    while p * p <= remaining:
        if remaining % p == 0:
            answer -= answer // p
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        answer -= answer // remaining
    return answer


def recurrent_cycles(n: int) -> int:
    total = 0
    for length in range(1, n // 2 + 1):
        burnside = 0
        for divisor in range(1, gcd(n, length) + 1):
            if n % divisor or length % divisor:
                continue
            reduced_n = n // divisor
            reduced_length = length // divisor
            if reduced_length == 1:
                linear = int(reduced_n >= 2)
            else:
                linear = comb(reduced_n - reduced_length - 1, reduced_length - 1)
            burnside += euler_phi(divisor) * linear
        check(burnside % length == 0)
        total += burnside // length
    return total


def predicted_preimages(target):
    answer = []
    if len(target) == 1:
        answer.append(target)
    elif target[-2] >= 2:
        answer.append((target[-1],) + target[:-1])
    if target[-1] >= 3:
        answer.append((1,) + target[:-1] + (target[-1] - 1,))
    return tuple(answer)


def main() -> None:
    for n in range(2, 19):
        carrier = states(n)
        carrier_set = set(carrier)
        depth_census = Counter()
        cycle_representatives = set()
        fibres = Counter()

        for word in carrier:
            image = update(word)
            check(image in carrier_set)
            fibres[image] += 1
            tail, period, recurrent = orbit(word)
            predicted_tail = tail_formula(word)
            core = terminal_core(word)
            check(tail == predicted_tail)
            check(period == primitive_rotation_period(core))
            x = word
            for _ in range(tail):
                x = update(x)
            check(x == core)
            check(recurrent in {core[i:] + core[:i] for i in range(len(core))})
            depth_census[tail] += 1

        for target in carrier:
            literal = predicted_preimages(target)
            expected = 0
            if len(target) == 1 or target[-2] >= 2:
                expected += 1
            if target[-1] >= 3:
                expected += 1
            check(len(literal) == expected)
            check(len(set(literal)) == len(literal))
            for source in literal:
                check(source in carrier_set)
                check(update(source) == target)
            check(fibres[target] == expected)

        for depth in range(0, n - 1):
            check(depth_census[depth] == depth_count(n, depth))
        check(max(depth_census) == n - 2)
        check(sum(depth_census.values()) == 1 << (n - 2))
        check(depth_census[0] == fibonacci(n - 1))

        recurrent = [word for word in carrier if 1 not in word]
        unseen = set(recurrent)
        while unseen:
            word = min(unseen)
            cycle = {word[i:] + word[:i] for i in range(len(word))}
            cycle &= set(recurrent)
            cycle_representatives.add(min(cycle))
            unseen -= cycle
        check(len(cycle_representatives) == recurrent_cycles(n))

        image_formula = 1 if n <= 3 else 3 * (1 << (n - 4))
        check(len(fibres) == image_formula)
        check(max(fibres.values()) <= 2)

        fixed = sum(update(word) == word for word in carrier)
        fixed_formula = sum(n % divisor == 0 for divisor in range(2, n + 1))
        check(fixed == fixed_formula)

        print(
            f"N={n} states={len(carrier)} image={len(fibres)} recurrent={len(recurrent)} "
            f"max_depth={max(depth_census)} cycles={len(cycle_representatives)} "
            f"fixed={fixed} max_fibre={max(fibres.values())}"
        )

    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
