#!/usr/bin/env python3
"""Exact finite audit for leftmost reassociation of Dyck components.

The audit uses only Python integers and tuples.  It exhausts every Dyck path
of semilength at most MAX_N and checks the literal update, the factor-count
clock, the complete temporal census, and every fixed target's depth-refined
basin.  Enumeration is counterexample pressure; the manuscript proofs carry
the all-parameter claims.
"""

from collections import Counter, defaultdict
from math import comb


MAX_N = 12
U = 1
D = -1


class Audit:
    """Count exact assertions and stop at the first counterexample."""

    def __init__(self):
        self.assertions = 0

    def check(self, condition, context):
        self.assertions += 1
        if not condition:
            raise AssertionError(context)


AUDIT = Audit()


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def dyck_paths(n):
    """Generate every Dyck path of semilength n in lexicographic step order."""

    def rec(prefix, up, down):
        if up == n and down == n:
            yield tuple(prefix)
            return
        if up < n:
            prefix.append(U)
            yield from rec(prefix, up + 1, down)
            prefix.pop()
        if down < up:
            prefix.append(D)
            yield from rec(prefix, up, down + 1)
            prefix.pop()

    yield from rec([], 0, 0)


def is_dyck(path):
    height = 0
    for step in path:
        if step not in (U, D):
            return False
        height += step
        if height < 0:
            return False
    return height == 0


def return_positions(path):
    height = 0
    positions = []
    for index, step in enumerate(path, start=1):
        height += step
        if height == 0:
            positions.append(index)
    return tuple(positions)


def primitive_factors(path):
    """Return the unique factors cut at positive returns to height zero."""
    if not path:
        return ()
    cuts = return_positions(path)
    start = 0
    factors = []
    for stop in cuts:
        factors.append(path[start:stop])
        start = stop
    return tuple(factors)


def is_primitive(path):
    return bool(path) and is_dyck(path) and return_positions(path) == (len(path),)


def flatten(words):
    return tuple(step for word in words for step in word)


def phi(path):
    """Literal leftmost update, implemented from the first two returns."""
    returns = return_positions(path)
    if len(returns) <= 1:
        return path
    first, second = returns[:2]
    return path[: first - 1] + path[first:second] + (path[first - 1],) + path[second:]


def predicted_iterate(path, t):
    """Closed form for Phi^t based only on the initial factorisation."""
    factors = primitive_factors(path)
    first_interior = factors[0][1:-1]
    return (
        (U,)
        + first_interior
        + flatten(factors[1 : t + 1])
        + (D,)
        + flatten(factors[t + 1 :])
    )


def endpoint_and_depth(path):
    seen = set()
    current = path
    depth = 0
    while phi(current) != current:
        AUDIT.check(current not in seen, ("cycle", path, current))
        seen.add(current)
        current = phi(current)
        depth += 1
    return current, depth


def ballot_layer(n, k):
    """Number of semilength-n Dyck paths with exactly k primitive factors."""
    return k * comb(2 * n - k, n) // (2 * n - k)


def source_at_depth(target, depth):
    """The claimed unique source of a fixed target at a prescribed depth."""
    AUDIT.check(is_primitive(target), ("nonfixed-target", target))
    interior_factors = primitive_factors(target[1:-1])
    r = len(interior_factors)
    AUDIT.check(0 <= depth <= r, ("source-depth-domain", target, depth, r))
    cut = r - depth
    return (
        (U,)
        + flatten(interior_factors[:cut])
        + (D,)
        + flatten(interior_factors[cut:])
    )


def audit_size(n):
    before = AUDIT.assertions
    states = 0
    fixed = 0
    layers = Counter()
    basins = defaultdict(Counter)
    deepest = []

    for path in dyck_paths(n):
        states += 1
        AUDIT.check(is_dyck(path), ("generator", n, path))
        factors = primitive_factors(path)
        k = len(factors)
        AUDIT.check(flatten(factors) == path, ("factor-concatenation", n, path, factors))
        AUDIT.check(all(is_primitive(factor) for factor in factors),
                    ("factor-primitivity", n, path, factors))

        image = phi(path)
        AUDIT.check(is_dyck(image), ("closure", n, path, image))
        if k == 1:
            fixed += 1
            AUDIT.check(image == path, ("fixed-if-primitive", n, path))
        else:
            AUDIT.check(image != path, ("moves-if-composite", n, path))
            AUDIT.check(len(primitive_factors(image)) == k - 1,
                        ("factor-drop", n, path, k, image))
            AUDIT.check(image == predicted_iterate(path, 1),
                        ("one-step-formula", n, path, image))

        current = path
        for t in range(k):
            AUDIT.check(current == predicted_iterate(path, t),
                        ("iterate-formula", n, path, t, current))
            if t + 1 < k:
                current = phi(current)

        endpoint, depth = endpoint_and_depth(path)
        AUDIT.check(depth == k - 1, ("pointwise-clock", n, path, depth, k))
        AUDIT.check(endpoint == predicted_iterate(path, k - 1),
                    ("endpoint-formula", n, path, endpoint))
        AUDIT.check(is_primitive(endpoint) and phi(endpoint) == endpoint,
                    ("terminal-fixed", n, path, endpoint))
        layers[depth] += 1
        basins[endpoint][depth] += 1
        if depth == n - 1:
            deepest.append(path)

    AUDIT.check(states == catalan(n), ("Catalan-total", n, states, catalan(n)))
    AUDIT.check(fixed == catalan(n - 1),
                ("primitive-fixed-count", n, fixed, catalan(n - 1)))
    for k in range(1, n + 1):
        AUDIT.check(layers[k - 1] == ballot_layer(n, k),
                    ("ballot-layer", n, k, layers[k - 1], ballot_layer(n, k)))
    AUDIT.check(sum(layers.values()) == states, ("layer-partition", n, layers, states))

    sharp_source = tuple(step for _ in range(n) for step in (U, D))
    AUDIT.check(deepest == [sharp_source],
                ("unique-deepest", n, deepest, sharp_source))

    max_fibre = 0
    max_targets = []
    for target, observed in basins.items():
        AUDIT.check(is_primitive(target), ("basin-target-fixed", n, target))
        r = len(primitive_factors(target[1:-1]))
        expected = Counter({d: 1 for d in range(r + 1)})
        AUDIT.check(observed == expected,
                    ("depth-fibre-polynomial", n, target, observed, expected))
        for depth in range(r + 1):
            source = source_at_depth(target, depth)
            AUDIT.check(is_dyck(source), ("inverse-source-valid", n, target, depth, source))
            source_endpoint, source_depth = endpoint_and_depth(source)
            AUDIT.check(source_endpoint == target,
                        ("inverse-source-endpoint", n, target, depth, source))
            AUDIT.check(source_depth == depth,
                        ("inverse-source-depth", n, target, depth, source_depth))
        fibre_size = sum(observed.values())
        if fibre_size > max_fibre:
            max_fibre = fibre_size
            max_targets = [target]
        elif fibre_size == max_fibre:
            max_targets.append(target)

    largest_target = (U,) + tuple(step for _ in range(n - 1) for step in (U, D)) + (D,)
    AUDIT.check(max_fibre == n, ("maximum-fibre-size", n, max_fibre))
    AUDIT.check(max_targets == [largest_target],
                ("unique-maximum-target", n, max_targets, largest_target))
    AUDIT.check(sum(sum(profile.values()) for profile in basins.values()) == states,
                ("basin-partition", n, states))

    return {
        "states": states,
        "fixed": fixed,
        "targets": len(basins),
        "max_depth": max(layers),
        "max_fibre": max_fibre,
        "assertions": AUDIT.assertions - before,
    }


def main():
    print("P144 EXACT CONTROL")
    print(f"RANGE n=1..{MAX_N}")
    total_states = 0
    total_targets = 0
    for n in range(1, MAX_N + 1):
        result = audit_size(n)
        total_states += result["states"]
        total_targets += result["targets"]
        print(
            f"n={n:02d} | states={result['states']} | fixed={result['fixed']} | "
            f"targets={result['targets']} | max_depth={result['max_depth']} | "
            f"max_fibre={result['max_fibre']} | assertions={result['assertions']}"
        )
    print(f"TOTAL_STATES={total_states}")
    print(f"TOTAL_FIXED_TARGETS={total_targets}")
    print(f"TOTAL_ASSERTIONS={AUDIT.assertions}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
