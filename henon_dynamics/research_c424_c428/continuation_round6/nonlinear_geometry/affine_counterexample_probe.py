#!/usr/bin/env python3
"""Exact bounded strategy counterexample search; see PROBE_CONTRACT.md.

An affine polynomial is (constant, coefficient of t). No guessed numeric
periods, floating point, external services, or integer-height census is used.
"""

from collections import Counter
from itertools import product
import json


def multiply_affine(factors):
    """Return affine product, or None if its exact degree exceeds one."""
    if (0, 0) in factors:
        return (0, 0)
    moving = [p for p in factors if p[1] != 0]
    if len(moving) > 1:
        return None
    scalar = 1
    for constant, coefficient in factors:
        if coefficient == 0:
            scalar *= constant
    if moving:
        constant, coefficient = moving[0]
        return scalar * constant, scalar * coefficient
    return scalar, 0


def check(seed, a, limit):
    state = seed
    ever_nonzero_product = False
    states = [seed]
    products = []
    for tick in range(1, limit + 1):
        window_product = multiply_affine(state[1:])
        if window_product is None:
            return "DEGREE_EXIT", None
        ever_nonzero_product |= window_product != (0, 0)
        c, b = window_product
        old_c, old_b = state[0]
        new = c + a - old_c, b - old_b
        state = state[1:] + (new,)
        products.append(window_product)
        if state == seed:
            kind = "MIXED_IDENTITY" if ever_nonzero_product else "ZERO_PRODUCT_IDENTITY"
            return kind, {"period": tick, "states": states, "products": products}
        states.append(state)
    return "TICK_LIMIT", None


def main():
    rows = []
    totals = Counter()
    for n in (4, 5, 6):
        for a in (-2, -1, 0, 1, 2):
            alphabet = tuple(dict.fromkeys(((-1, 0), (0, 0), (1, 0), (a, 0), (0, 1), (a, -1))))
            counts = Counter()
            witness = None
            for tail in product(alphabet, repeat=n - 1):
                if not any(p[1] != 0 for p in tail):
                    continue
                seed = ((0, 0),) + tail
                kind, detail = check(seed, a, 2 * n + 2)
                counts[kind] += 1
                if kind == "MIXED_IDENTITY" and witness is None:
                    witness = {"seed": seed, **detail}
            totals.update(counts)
            rows.append({"n": n, "a": a, "seed_counts": dict(counts), "first_mixed_witness": witness})
    print(json.dumps({
        "scope": "one bounded affine-family strategy probe, not a complete periodic atlas",
        "totals": dict(totals), "rows": rows,
    }, indent=2))


if __name__ == "__main__":
    main()
