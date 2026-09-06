#!/usr/bin/env python3
"""Small independent LNR inverse pilot; no imports from root's pilot."""
from collections import Counter, defaultdict
from itertools import product
import json


def update(x):
    n = len(x)
    return tuple(int(x[(i - 1) % n] < x[i]) + int(x[(i + 1) % n] < x[i])
                 for i in range(n))


def bracelet(x):
    rotations = [x[i:] + x[:i] for i in range(len(x))]
    y = tuple(reversed(x))
    rotations.extend(y[i:] + y[:i] for i in range(len(x)))
    return min(rotations)


def main():
    boxes = []
    for n in range(3, 9):
        sources = defaultdict(list)
        for x in product((0, 1, 2), repeat=n):
            sources[update(x)].append(x)
        maximum = max(map(len, sources.values()))
        targets = sorted(b for b, fibre in sources.items() if len(fibre) == maximum)
        representatives = sorted({bracelet(b) for b in targets})
        boxes.append({"n": n, "source_states": 3 ** n,
                      "image_size": len(sources), "maximum_fibre": maximum,
                      "maximizing_targets": targets,
                      "maximizer_bracelets_and_full_sources": [
                          {"target": b, "sources": sorted(sources[b])} for b in representatives],
                      "fibre_histogram": sorted(Counter(map(len, sources.values())).items())})
    print(json.dumps({"scope": "small full inverse discovery, n=3..8; no all-n inference",
                      "literal": "F_i = count of strictly smaller cyclic neighbours",
                      "boxes": boxes}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
