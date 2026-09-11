#!/usr/bin/env python3
"""Factored exhaustive local certificate, preserving all earlier failures.

All eleven-letter words are checked first. Only failed inner windows need
their nine possible one-letter extensions on each side. This covers every
thirteen-letter word without a full thirteen-letter traversal.
"""
from collections import Counter
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


def cone(w):
    rows = [w]
    for _ in range(4):
        rows.append(shrink(rows[-1]))
    old = extremes(w)
    events = [(t, i) for t, row in enumerate(rows[1:], 1)
              for i in sorted(extremes(row) - old)]
    return rows, old, events


def main():
    inner_tested, exceptions, extensions, violations = 0, 0, 0, 0
    examples, witnesses = [], Counter()
    for w in product(range(3), repeat=11):
        rows, old, events = cone(w)
        inner_tested += 1
        if rows[4][1] == rows[2][3]:
            continue
        if events:
            witnesses[events[0]] += 1
            continue
        exceptions += 1
        for a, b in product(range(3), repeat=2):
            v = (a,) + w + (b,)
            rr, ee, ev = cone(v)
            extensions += 1
            if not ev:
                violations += 1
                if len(examples) < 30:
                    examples.append({"cone": rr, "original_extremes": sorted(ee)})
            else:
                witnesses[ev[0]] += 1
    print(json.dumps({"test": "U4_center != U2_center forces new strict extremum within four steps, radius-six initial window",
                      "inner_words_length": 11, "inner_words_tested": inner_tested,
                      "inner_exceptions": exceptions, "outer_extensions_checked": extensions,
                      "thirteen_letter_words_covered_logically": 3 ** 13,
                      "violations": violations, "counterexamples": examples,
                      "first_event_census": [list(k) + [v] for k, v in sorted(witnesses.items())]},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
