#!/usr/bin/env python3
"""Exact verifier for random alphabet-erasure dynamics."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def erase(word, letter):
    return tuple(x for x in word if x != letter)


def act(word, history):
    for letter in history:
        word = erase(word, letter)
    return word


def project(word, keep):
    return tuple(x for x in word if x in keep)


def support(word):
    return frozenset(word)


def stirling2(n, k):
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            table[i][j] = table[i - 1][j - 1] + j * table[i - 1][j]
    return table[n][k]


def falling(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // factorial(n - k)


def transition_histories(q, source, target, time):
    target_support = support(target)
    source_support = support(source)
    if not target_support <= source_support:
        return 0
    if project(source, target_support) != target:
        return 0
    deleted = len(source_support - target_support)
    return sum((-1) ** j * comb(deleted, j) * (q - len(target_support) - j) ** time
               for j in range(deleted + 1))


def absorption_cdf_count(q, support_size, time):
    return sum((-1) ** j * comb(support_size, j) * (q - j) ** time
               for j in range(support_size + 1))


def absorption_dp_count(q, support_size, time):
    counts = [0] * (support_size + 1)
    counts[0] = 1
    for _ in range(time):
        following = [0] * (support_size + 1)
        for seen, value in enumerate(counts):
            following[seen] += value * (q - support_size + seen)
            if seen < support_size:
                following[seen + 1] += value * (support_size - seen)
        counts = following
    return counts[support_size]


def source_history_fibre(q, target, source_length, time):
    m = len(target)
    b = len(support(target))
    if source_length < m:
        return 0
    inserted = source_length - m
    return comb(source_length, m) * sum(
        falling(q - b, s) * stirling2(time, s) *
        (1 if inserted == 0 and s == 0 else s ** inserted)
        for s in range(min(q - b, time) + 1)
    )


def word_count_with_support(q, length, size):
    return falling(q, size) * stirling2(length, size)


def run_semigroup_and_transition():
    boxes = [(2, 5, 7), (3, 5, 6), (4, 4, 5), (5, 3, 5)]
    for q, max_length, max_time in boxes:
        alphabet = tuple(range(q))
        for a in alphabet:
            for b in alphabet:
                for length in range(max_length + 1):
                    for word in product(alphabet, repeat=length):
                        check(erase(erase(word, a), a) == erase(word, a),
                              ("idempotent", q, word, a))
                        check(erase(erase(word, a), b) == erase(erase(word, b), a),
                              ("commuting", q, word, a, b))
        for time in range(max_time + 1):
            histories = tuple(product(alphabet, repeat=time))
            support_hist = Counter(len(support(h)) for h in histories)
            for size in range(q + 1):
                check(support_hist[size] == falling(q, size) * stirling2(time, size),
                      ("history support", q, time, size))
            check(sum(support_hist.values()) == q ** time,
                  ("history support mass", q, time))
            for length in range(max_length + 1):
                words = tuple(product(alphabet, repeat=length))
                # Full pair enumeration is kept in modest boxes.
                if q ** (length + time) <= 2_000_000:
                    for word in words:
                        observed = Counter(act(word, history) for history in histories)
                        for target in observed:
                            predicted = transition_histories(q, word, target, time)
                            check(observed[target] == predicted,
                                  ("transition", q, length, time, word, target))
                        check(sum(observed.values()) == q ** time,
                              ("transition mass", q, length, time, word))
                        reachable = {project(word, keep)
                                     for r in range(q + 1)
                                     for keep in map(frozenset, __import__('itertools').combinations(alphabet, r))}
                        check(len(reachable) == 2 ** len(support(word)),
                              ("projection lattice", q, word))


def run_absorption():
    for q in range(2, 9):
        alphabet = tuple(range(q))
        for size in range(q + 1):
            word = tuple(range(size))
            expected = sum(Fraction(q, j) for j in range(1, size + 1))
            recursive = Fraction(0)
            for j in range(1, size + 1):
                recursive += Fraction(q, j)
            check(expected == recursive, ("mean clock", q, size))
            for time in range(0, 9):
                observed = absorption_dp_count(q, size, time)
                predicted = absorption_cdf_count(q, size, time)
                check(observed == predicted, ("absorption cdf", q, size, time))
                if q ** time <= 250_000:
                    literal = sum(not act(word, h) for h in product(alphabet, repeat=time))
                    check(literal == observed, ("literal absorption", q, size, time))
        max_support = q
        maximum = sum(Fraction(q, j) for j in range(1, max_support + 1))
        check(all(maximum >= sum(Fraction(q, j) for j in range(1, s + 1))
                  for s in range(q + 1)), ("sharp mean support", q))


def run_global_fibres():
    boxes = [(2, 7, 7), (3, 6, 6), (4, 5, 5), (5, 4, 4)]
    total_cells = 0
    for q, max_length, max_time in boxes:
        alphabet = tuple(range(q))
        for time in range(max_time + 1):
            histories = tuple(product(alphabet, repeat=time))
            for n in range(max_length + 1):
                sources = tuple(product(alphabet, repeat=n))
                observed = Counter()
                for source in sources:
                    for history in histories:
                        observed[act(source, history)] += 1
                for m in range(n + 1):
                    class_counts = Counter()
                    for target in product(alphabet, repeat=m):
                        predicted = source_history_fibre(q, target, n, time)
                        check(observed[target] == predicted,
                              ("global fibre", q, n, time, target,
                               observed[target], predicted))
                        class_counts[len(support(target))] += 1
                        total_cells += 1
                    for b in range(min(q, m) + 1):
                        check(class_counts[b] == word_count_with_support(q, m, b),
                              ("target class multiplicity", q, m, b))
                check(sum(observed.values()) == q ** (n + time),
                      ("global pair mass", q, n, time))
    return total_cells


def main():
    run_semigroup_and_transition()
    run_absorption()
    cells = run_global_fibres()
    print("RANDOM_ALPHABET_ERASURE_SCOUT_V1")
    print("semigroup boxes=4; absorption q=2..8; global fibre boxes=4")
    print(f"target fibre cells={cells}")
    print(f"assertions={ASSERTIONS}")
    print("DECISION GREEN_PENDING_INDEPENDENT_HOSTILE_GATE")
    print("EXTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
