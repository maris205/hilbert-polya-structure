#!/usr/bin/env python3
"""One predeclared full-box neighborhood-cardinality scout; no proof claim."""
from collections import Counter
from itertools import product
import json
from pilot import profile


def neighborhood_cardinality(x):
    counts = Counter(x)
    return tuple(counts[a - 1] + counts[a] + counts[a + 1] for a in x)


def main():
    for n in range(1, 7):
        states = list(product(range(1, n + 1), repeat=n))
        output = profile(states, neighborhood_cardinality)
        inverse = Counter(neighborhood_cardinality(x) for x in states)
        maximum = max(inverse.values())
        equal = sorted(b for b, amount in inverse.items() if amount == maximum)
        fixed = sorted(x for x in states if neighborhood_cardinality(x) == x)
        output.update({"candidate": "NCC", "n": n,
                       "all_labelled_maximum_targets": equal,
                       "all_fixed_words": fixed,
                       "full_target_fibre_histogram_nonempty": sorted(Counter(inverse.values()).items())})
        print(json.dumps(output, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
