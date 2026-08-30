#!/usr/bin/env python3
"""Secondary exact pilots: factor descents, fence deletion, sandwich rewrite."""

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import isqrt


ASSERTIONS = 0


def check(condition):
    global ASSERTIONS
    ASSERTIONS += 1
    assert condition


def factor_pairs(n):
    return tuple((a, n // a) for a in range(2, isqrt(n) + 1) if n % a == 0)


def make_factor_law(update):
    @lru_cache(None)
    def law(n):
        children = tuple(update(a, b) for a, b in factor_pairs(n))
        if not children:
            return (((n, 0), Fraction(1)),)
        out = defaultdict(Fraction)
        for child in children:
            for (terminal, time), probability in law(child):
                out[(terminal, time + 1)] += probability / len(children)
        return tuple(sorted(out.items()))

    return law


SUM_LAW = make_factor_law(lambda a, b: a + b - 1)
GAP_LAW = make_factor_law(lambda a, b: b - a)


def factor_forward(start, update):
    live = {start: Fraction(1)}
    terminal = defaultdict(Fraction)
    time = 0
    while live:
        nxt = defaultdict(Fraction)
        for n, mass in live.items():
            children = tuple(update(a, b) for a, b in factor_pairs(n))
            if not children:
                terminal[(n, time)] += mass
            else:
                for child in children:
                    nxt[child] += mass / len(children)
        live = nxt
        time += 1
    return tuple(sorted(terminal.items()))


def fence_predecessors(n):
    predecessors = [set() for _ in range(n)]
    for i in range(n - 1):
        if i % 2 == 0:
            predecessors[i + 1].add(i)
        else:
            predecessors[i].add(i + 1)
    return predecessors


def fence_last_law(n):
    predecessors = fence_predecessors(n)

    def maximal(mask):
        return tuple(
            i
            for i in range(n)
            if mask >> i & 1
            and not any(mask >> j & 1 and i in predecessors[j] for j in range(n))
        )

    @lru_cache(None)
    def law(mask):
        if mask.bit_count() == 1:
            return ((mask.bit_length(), Fraction(1)),)
        active = maximal(mask)
        out = defaultdict(Fraction)
        for i in active:
            for last, probability in law(mask ^ (1 << i)):
                out[last] += probability / len(active)
        return tuple(sorted(out.items()))

    return law((1 << n) - 1)


def sandwich_successors(word):
    return tuple(
        word[:i] + word[i + 1] + word[i + 3 :]
        for i in range(len(word) - 2)
        if word[i] == word[i + 2]
    )


@lru_cache(None)
def sandwich_terminals(word):
    children = set(sandwich_successors(word))
    if not children:
        return frozenset((word,))
    result = set()
    for child in children:
        result.update(sandwich_terminals(child))
    return frozenset(result)


def main():
    sum_best = (0, 0)
    gap_best = (0, 0)
    for n in range(1, 401):
        for law, update in (
            (SUM_LAW, lambda a, b: a + b - 1),
            (GAP_LAW, lambda a, b: b - a),
        ):
            exact = law(n)
            check(sum(probability for _, probability in exact) == 1)
            check(all(probability > 0 for _, probability in exact))
            for (terminal, time), _ in exact:
                check(not factor_pairs(terminal))
                check(time <= n - 1)
            if n <= 120:
                check(exact == factor_forward(n, update))
        sum_support = len({terminal for (terminal, _), _ in SUM_LAW(n)})
        gap_support = len({terminal for (terminal, _), _ in GAP_LAW(n)})
        if sum_support > sum_best[1]:
            sum_best = (n, sum_support)
        if gap_support > gap_best[1]:
            gap_best = (n, gap_support)

    fence_snapshots = {}
    for n in range(2, 13):
        law = fence_last_law(n)
        check(sum(probability for _, probability in law) == 1)
        check(all(last % 2 == 1 for last, _ in law))
        if n % 2 == 1:
            reflected = tuple((n + 1 - last, probability) for last, probability in law[::-1])
            check(law == reflected)
        fence_snapshots[n] = law

    sandwich_best = ("", 0)
    for length in range(0, 11):
        for letters in product("012", repeat=length):
            word = "".join(letters)
            terminals = sandwich_terminals(word)
            check(all(not sandwich_successors(t) for t in terminals))
            check(all((len(word) - len(t)) % 2 == 0 for t in terminals))
            if len(terminals) > sandwich_best[1]:
                sandwich_best = (word, len(terminals))

    check(SUM_LAW(36) == (((3, 4), Fraction(1, 8)), ((5, 3), Fraction(1, 4)), ((7, 2), Fraction(1, 8)), ((11, 1), Fraction(1, 4)), ((19, 1), Fraction(1, 4))))
    check(GAP_LAW(36) == (((0, 1), Fraction(1, 4)), ((0, 2), Fraction(3, 8)), ((1, 3), Fraction(1, 8)), ((5, 1), Fraction(1, 4))))

    print("secondary stochastic/rewrite pilots: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("factor-sum and factor-gap descents: 1 <= n <= 400")
    print(f"largest terminal support through 400 (sum): n={sum_best[0]}, size={sum_best[1]}")
    print(f"largest terminal support through 400 (gap): n={gap_best[0]}, size={gap_best[1]}")
    print("factor-sum n=36 law: " + repr(SUM_LAW(36)))
    print("factor-gap n=36 law: " + repr(GAP_LAW(36)))
    print("fence maximal-deletion last laws: 2 <= n <= 12")
    print("fence n=9: " + repr(fence_snapshots[9]))
    print(f"sandwich-center collapse max through length 10: {sandwich_best[0]} -> {sandwich_best[1]} terminals")


if __name__ == "__main__":
    main()
