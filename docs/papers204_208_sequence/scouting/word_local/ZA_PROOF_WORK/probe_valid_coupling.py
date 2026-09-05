#!/usr/bin/env python3
"""Directed falsification of a prospective valid-Z prefix contraction."""
from itertools import product
import json
from probe_prefix import zstep


def orbit(x):
    path, where = [], {}
    while x not in where:
        where[x] = len(path)
        path.append(x)
        x = zstep(x)
    return where[x], len(path)-where[x], path


def main():
    rows = []
    for n in range(2, 16):
        valid = set()
        maximum = 0
        deepest = None
        periods = set()
        for bits in product((0, 1), repeat=n-1):
            word = (0,)+bits
            valid.add(zstep(word))
            h, p, _ = orbit(word)
            periods.add(p)
            if h > maximum:
                maximum, deepest = h, word
        reference, witness = {}, None
        failures = 0
        for x in sorted(valid):
            target = zstep(zstep(x))
            mask = tuple(a == 0 for a in x)
            for i in range(1, n):
                key = mask, x[:i], i
                if key in reference and reference[key][0] != target[i]:
                    failures += 1
                    if witness is None:
                        witness = {"x": reference[key][1], "y": x, "i": i,
                                   "Gx": zstep(zstep(reference[key][1])), "Gy": target}
                else:
                    reference[key] = target[i], x
        rows.append({"n": n, "binary_sources": 2**(n-1), "distinct_valid_images": len(valid),
                     "binary_max_tail": maximum, "binary_deepest": deepest,
                     "periods": sorted(periods), "valid_two_step_coupling_failures": failures,
                     "witness": witness})
    print(json.dumps({"scope": "binary-source images only; not every valid Z array at these sizes", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
