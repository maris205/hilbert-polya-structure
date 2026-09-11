#!/usr/bin/env python3
"""CPRM only: CSGD's declared zero carrier is not invariant (preserved v1)."""
from itertools import product
import json
from pilot import profile


def cprm(word):
    n = len(word)
    return tuple(1 + (a - 1) % word[(i + 1) % n] for i, a in enumerate(word))


def main():
    for n in range(2, 7):
        for m in range(1, 7):
            print(json.dumps({"candidate": "CPRM", "n": n, "m": m,
                              **profile(product(range(1, m + 1), repeat=n), cprm)},
                             sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
