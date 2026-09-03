#!/usr/bin/env python3
"""Exact regression control for P179.

The program compares the literal label-isolation chain with separately coded
closed formulas.  Finite enumeration is counterexample pressure, not proof.
It uses only the Python standard library and emits a deterministic transcript.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial


def partitions(n):
    if n == 0:
        yield ()
        return

    def extend(word, top):
        if len(word) == n:
            yield tuple(word)
            return
        for value in range(top + 2):
            yield from extend(word + [value], max(top, value))

    yield from extend([0], 0)


def block_list(partition):
    out = defaultdict(list)
    for label, block in enumerate(partition):
        out[block].append(label)
    return list(out.values())


def canonical(blocks, n):
    blocks = sorted((sorted(block) for block in blocks if block),
                    key=lambda block: block[0])
    out = [0] * n
    for name, block in enumerate(blocks):
        for label in block:
            out[label] = name
    return tuple(out)


def isolate(partition, label):
    blocks = block_list(partition)
    for j, block in enumerate(blocks):
        if label in block:
            if len(block) == 1:
                return partition
            blocks[j] = [x for x in block if x != label]
            blocks.append([label])
            return canonical(blocks, len(partition))
    raise AssertionError("label absent")


def isolate_support(partition, support):
    out = partition
    for label in support:
        out = isolate(out, label)
    return out


def support_formula(partition, support):
    """Blockwise formula, retaining a nonempty one-label residual."""
    blocks = []
    for block in block_list(partition):
        blocks.extend([[label] for label in block if label in support])
        residual = [label for label in block if label not in support]
        if residual:
            blocks.append(residual)
    return canonical(blocks, len(partition))


def singleton_count(partition):
    return sum(len(block) == 1 for block in block_list(partition))


def associated_bell(n):
    return sum(singleton_count(p) == 0 for p in partitions(n))


def stirling2(n, k):
    if k < 0 or k > n:
        return 0
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for a in range(1, n + 1):
        for b in range(1, min(a, k) + 1):
            table[a][b] = table[a - 1][b - 1] + b * table[a - 1][b]
    return table[n][k]


def elementary(values, degree):
    coefficients = [0] * (degree + 1)
    coefficients[0] = 1
    for value in values:
        for j in range(degree, 0, -1):
            coefficients[j] += value * coefficients[j - 1]
    return coefficients[degree]


def rank_over_q(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    rank = 0
    for column in range(len(a[0]) if a else 0):
        pivot = next((row for row in range(rank, len(a))
                      if a[row][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][column]
        a[rank] = [x / scale for x in a[rank]]
        for row in range(len(a)):
            if row != rank and a[row][column]:
                scale = a[row][column]
                a[row] = [x - scale * y
                          for x, y in zip(a[row], a[rank])]
        rank += 1
    return rank


def subsets(n):
    for size in range(n + 1):
        yield from combinations(range(n), size)


def main():
    assertions = 0
    rows = []

    # Commuting idempotents, diagonal layers, and one-step inverse atlas.
    for n in range(1, 9):
        states = list(partitions(n))
        incoming_states = defaultdict(set)
        incoming_actions = Counter()
        for p in states:
            for i in range(n):
                once = isolate(p, i)
                assert isolate(once, i) == once
                assertions += 1
                incoming_states[once].add(p)
                incoming_actions[once] += 1
            if n <= 7:
                for i in range(n):
                    for j in range(n):
                        assert isolate(isolate(p, i), j) == isolate(isolate(p, j), i)
                        assertions += 1

        layer = Counter(map(singleton_count, states))
        predicted = {
            s: comb(n, s) * associated_bell(n - s)
            for s in range(max(0, n - 1))
        }
        predicted[n] = 1
        predicted = {s: value for s, value in predicted.items() if value}
        assert dict(layer) == predicted
        assert n - 1 not in layer
        assertions += len(states) + 2

        for target in states:
            s = singleton_count(target)
            b = len(block_list(target))
            expected_states = 0 if s == 0 else 1 + s * (b - s) + comb(s, 2)
            assert len(incoming_states[target]) == expected_states
            assert incoming_actions[target] == s * b
            assertions += 2

        rows.append((n, len(states), tuple(sorted(layer.items())),
                     max(map(len, incoming_states.values()))))

    # Directly compare the support lemma's block formula, especially the
    # residual-singleton case, against literal isolation.
    for n in range(1, 8):
        for initial in partitions(n):
            for support_tuple in subsets(n):
                support = set(support_tuple)
                assert isolate_support(initial, support) == support_formula(
                    initial, support
                )
                assertions += 1

    # Direct eigenspace dimensions for the integer matrix nP.
    for n in range(1, 6):
        states = list(partitions(n))
        index = {p: j for j, p in enumerate(states)}
        size = len(states)
        matrix = [[0] * size for _ in range(size)]
        for row, p in enumerate(states):
            for i in range(n):
                matrix[row][index[isolate(p, i)]] += 1
        layers = Counter(map(singleton_count, states))
        for s, multiplicity in sorted(layers.items()):
            shifted = [
                [matrix[row][column] - (s if row == column else 0)
                 for column in range(size)]
                for row in range(size)
            ]
            assert size - rank_over_q(shifted) == multiplicity
            assertions += size

    # All-time absorption formula on every initial partition in finite boxes.
    for n in range(1, 7):
        for initial in partitions(n):
            sizes = [len(block) for block in block_list(initial)]
            for t in range(5):
                actual = 0
                for history in product(range(n), repeat=t):
                    state = initial
                    for label in history:
                        state = isolate(state, label)
                    actual += singleton_count(state) == n
                formula = sum(
                    elementary(sizes, missing) * factorial(n - missing)
                    * stirling2(t, n - missing)
                    for missing in range(len(sizes) + 1)
                )
                assert actual == formula
                assertions += 1

    # Every labelled target: exact-support aggregation versus literal histories.
    for n in range(1, 6):
        states = list(partitions(n))
        universe = set(range(n))
        for initial in states:
            for t in range(5):
                actual = Counter()
                for history in product(range(n), repeat=t):
                    state = initial
                    for label in history:
                        state = isolate(state, label)
                    actual[state] += 1

                predicted = Counter()
                for missing_tuple in subsets(n):
                    missing = set(missing_tuple)
                    seen = universe - missing
                    histories = factorial(len(seen)) * stirling2(t, len(seen))
                    if histories:
                        predicted[isolate_support(initial, seen)] += histories
                for target in states:
                    assert actual[target] == predicted[target]
                    assertions += 1

    print("P179_RANDOM_SINGLETON_ISOLATION")
    for n, bell, layers, max_predecessors in rows:
        print(f"n={n} Bell={bell} layers={layers} max_pred={max_predecessors}")
    print(f"ASSERTIONS={assertions}")
    print("BOXES=n<=8; commute n<=7; spectra n<=5; histories n<=6,t<=4")
    print("SUPPORT_RESIDUAL_SINGLETON=PASS")
    print("RESULT=PASS")
    print("RELEASE_SENTINEL=THEOREM_CONTROL_ONLY/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
