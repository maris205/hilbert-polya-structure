#!/usr/bin/env python3
"""Exact pilot for 01->2, 12->0, 20->1 with a uniform active redex."""

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product


RULES = {"01": "2", "12": "0", "20": "1"}
VALUE = {"0": 1, "1": 2, "2": 3}  # nonzero vectors of F_2^2
ASSERTIONS = 0


def check(condition):
    global ASSERTIONS
    ASSERTIONS += 1
    assert condition


def invariant(word):
    value = 0
    for letter in word:
        value ^= VALUE[letter]
    return value


def successors(word):
    return tuple(
        word[:i] + RULES[word[i : i + 2]] + word[i + 2 :]
        for i in range(len(word) - 1)
        if word[i : i + 2] in RULES
    )


@lru_cache(None)
def recursive_law(word):
    nxt = successors(word)
    if not nxt:
        return ((word, Fraction(1)),)
    out = defaultdict(Fraction)
    for child in nxt:
        for terminal, probability in recursive_law(child):
            out[terminal] += probability / len(nxt)
    return tuple(sorted(out.items()))


def forward_law(word):
    live = {word: Fraction(1)}
    terminal = defaultdict(Fraction)
    while live:
        nxt_live = defaultdict(Fraction)
        for state, mass in live.items():
            nxt = successors(state)
            if not nxt:
                terminal[state] += mass
            else:
                for child in nxt:
                    nxt_live[child] += mass / len(nxt)
        live = nxt_live
    return tuple(sorted(terminal.items()))


@lru_cache(None)
def terminal_support(word):
    nxt = set(successors(word))
    if not nxt:
        return frozenset((word,))
    out = set()
    for child in nxt:
        out.update(terminal_support(child))
    return frozenset(out)


def main():
    for length in range(0, 8):
        for letters in product("012", repeat=length):
            word = "".join(letters)
            law = recursive_law(word)
            check(law == forward_law(word))
            check(sum(probability for _, probability in law) == 1)
            for terminal, probability in law:
                check(probability > 0)
                check(not successors(terminal))
                check(invariant(terminal) == invariant(word))
                check(len(terminal) <= len(word))

    support_counts = []
    histories = []

    @lru_cache(None)
    def history_count(word):
        nxt = successors(word)
        if not nxt:
            return 1
        return sum(history_count(child) for child in nxt)

    for k in range(1, 10):
        word = "012" * k
        support = terminal_support(word)
        support_counts.append(len(support))
        histories.append(history_count(word))
        check(all(invariant(t) == 0 for t in support))
        check(all(not successors(t) for t in support))
        # The complete rational law is substantially larger at k=9; the
        # independent support/history recursion remains exact there.
        if k <= 8:
            check(sum(probability for _, probability in recursive_law(word)) == 1)

    check(support_counts == [2, 4, 9, 21, 49, 114, 265, 616, 1432])
    for i in range(3, len(support_counts)):
        check(
            support_counts[i]
            == 3 * support_counts[i - 1]
            - 2 * support_counts[i - 2]
            + support_counts[i - 3]
        )
    check(histories == [2, 12, 144, 2640, 66240, 2172240, 88583040, 4387582080, 256987987200])

    print("cyclic three-letter fusion pilot: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("all words: length <= 7; recursive law equals forward mass transport")
    print("F_2^2 xor invariant: exact on every reachable terminal")
    print("start words: (012)^k, 1 <= k <= 9 (full rational law through k=8)")
    print("terminal-support counts: " + ",".join(map(str, support_counts)))
    print("support recurrence: a_k=3*a_(k-1)-2*a_(k-2)+a_(k-3)")
    print("unweighted history counts: " + ",".join(map(str, histories)))


if __name__ == "__main__":
    main()
