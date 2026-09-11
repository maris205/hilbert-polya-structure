#!/usr/bin/env python3
"""Bounded local-rule discovery certificates, not a larger cyclic atlas."""
from itertools import product
import json


def shrink(w):
    return tuple(int(w[i - 1] > w[i]) + int(w[i + 1] > w[i])
                 for i in range(1, len(w) - 1))


def extremes(w):
    offset = len(w) // 2
    return {i - offset for i in range(1, len(w) - 1)
            if w[i] < min(w[i - 1], w[i + 1])
            or w[i] > max(w[i - 1], w[i + 1])}


def main():
    tested, violations, examples = 0, 0, []
    for w in product(range(3), repeat=9):
        rows = [w]
        for _ in range(4):
            rows.append(shrink(rows[-1]))
        old = extremes(w)
        new = set().union(*(extremes(row) - old for row in rows[1:4]))
        tested += 1
        if rows[4][0] != rows[2][2] and not new:
            violations += 1
            if len(examples) < 20:
                examples.append({"cone": rows, "original_extremes": sorted(old)})
    print(json.dumps({"test": "if U4_center != U2_center then a new strict extremum in first 3-step dependency cone",
                      "local_words_length": 9, "tested": tested,
                      "violations": violations, "counterexamples": examples}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
