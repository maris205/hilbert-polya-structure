#!/usr/bin/env python3
"""Independent hostile checks for P179.

Partitions are tuples of integer bit-blocks, not restricted-growth words.
The spectral check uses exact characteristic polynomials (SymPy/Bareiss),
whereas the temporal check propagates count measures and compares them with
an independently generated missing-set expansion using inclusion--exclusion
for surjections.  No paper or scout module is imported.
"""

from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb

import sympy as sp


class Audit:
    def __init__(self):
        self.assertions = 0

    def equal(self, left, right, label=""):
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")

    def true(self, value, label=""):
        self.assertions += 1
        if not value:
            raise AssertionError(label or "assertion failed")


def block_key(mask):
    return (mask & -mask).bit_length()


def canonical(blocks):
    return tuple(sorted((b for b in blocks if b), key=block_key))


def partitions(n):
    states = {()}
    for label in range(n):
        atom = 1 << label
        next_states = set()
        for state in states:
            next_states.add(canonical(state + (atom,)))
            for j in range(len(state)):
                blocks = list(state)
                blocks[j] |= atom
                next_states.add(canonical(blocks))
        states = next_states
    return tuple(sorted(states))


def isolate(state, label):
    atom = 1 << label
    for j, block in enumerate(state):
        if block & atom:
            if block == atom:
                return state
            blocks = list(state)
            blocks[j] ^= atom
            blocks.append(atom)
            return canonical(blocks)
    raise AssertionError("label missing")


def isolate_set(state, seen_mask, n):
    out = state
    for label in range(n):
        if (seen_mask >> label) & 1:
            out = isolate(out, label)
    return out


def singleton_count(state):
    return sum(block & (block - 1) == 0 for block in state)


def onto_words(t, r):
    if r == 0:
        return int(t == 0)
    return sum((-1) ** j * comb(r, j) * (r - j) ** t for j in range(r + 1))


def advance_distribution(initial, n, t):
    mass = Counter({initial: 1})
    for _ in range(t):
        nxt = Counter()
        for state, weight in mass.items():
            for label in range(n):
                nxt[isolate(state, label)] += weight
        mass = nxt
    return mass


def support_distribution(initial, n, t):
    all_labels = (1 << n) - 1
    mass = Counter()
    for missing in range(1 << n):
        seen = all_labels ^ missing
        weight = onto_words(t, seen.bit_count())
        if weight:
            mass[isolate_set(initial, seen, n)] += weight
    return mass


def elementary_by_subsets(values, degree):
    return sum(product_terms(choice) for choice in combinations(values, degree))


def product_terms(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


def refines(target, source):
    return all(any(block & ~old == 0 for old in source) for block in target)


def admissible_missing(source, target, n):
    if not refines(target, source):
        return ()
    choices = []
    for old in source:
        inside = [block for block in target if block & ~old == 0]
        if sum(block.bit_count() for block in inside) != old.bit_count():
            return ()
        large = [block for block in inside if block.bit_count() >= 2]
        if len(large) > 1:
            return ()
        if large:
            choices.append((large[0],))
        else:
            choices.append((0,) + tuple(1 << label for label in range(n) if old & (1 << label)))
    return tuple(sorted({sum(option) for option in product(*choices)}))


def expected_charpoly(n, states, symbol):
    layers = Counter(singleton_count(state) for state in states)
    polynomial = sp.Poly(1, symbol, domain=sp.QQ)
    for singleton_number, multiplicity in sorted(layers.items()):
        polynomial *= sp.Poly((symbol - singleton_number) ** multiplicity, symbol, domain=sp.QQ)
    return polynomial


def main():
    audit = Audit()
    rows = []
    cache = {n: partitions(n) for n in range(1, 9)}

    # Literal idempotence/commutation, singleton layers, and both inverse notions.
    for n in range(1, 9):
        states = cache[n]
        incoming_sources = defaultdict(set)
        incoming_labelled = Counter()
        for state in states:
            for i in range(n):
                image = isolate(state, i)
                audit.equal(isolate(image, i), image, f"idempotence n={n}")
                incoming_sources[image].add(state)
                incoming_labelled[image] += 1
            if n <= 7:
                for i in range(n):
                    for j in range(i + 1, n):
                        audit.equal(isolate(isolate(state, i), j),
                                    isolate(isolate(state, j), i),
                                    f"commutation n={n}")

        layers = Counter(singleton_count(state) for state in states)
        predicted_layers = Counter()
        for s in range(n + 1):
            complement_states = cache[n - s] if n - s >= 1 else ((),)
            d_value = sum(singleton_count(state) == 0 for state in complement_states)
            if s == n:
                d_value = 1
            predicted_layers[s] = comb(n, s) * d_value
        predicted_layers = +predicted_layers
        audit.equal(layers, predicted_layers, f"singleton-layer census n={n}")
        audit.true(n - 1 not in layers, f"missing n-1 layer n={n}")

        for target in states:
            s = singleton_count(target)
            b = len(target)
            expected_sources = 0 if s == 0 else 1 + s * (b - s) + comb(s, 2)
            audit.equal(len(incoming_sources[target]), expected_sources,
                        f"distinct predecessors n={n}")
            audit.equal(incoming_labelled[target], s * b,
                        f"labelled predecessors n={n}")

        rows.append((n, len(states), tuple(sorted(layers.items())),
                     max((len(value) for value in incoming_sources.values()), default=0)))

    # Exact characteristic polynomials of nP=sum E_i, a different spectral
    # diagnostic from the author's eigenspace-rank computation.
    x = sp.Symbol("x")
    spectral_rows = []
    for n in range(1, 6):
        states = cache[n]
        index = {state: i for i, state in enumerate(states)}
        matrix = sp.zeros(len(states), len(states))
        for row, state in enumerate(states):
            for label in range(n):
                matrix[row, index[isolate(state, label)]] += 1
        observed = matrix.charpoly(x).as_poly()
        predicted = expected_charpoly(n, states, x)
        audit.equal(sp.expand(observed.as_expr()), sp.expand(predicted.as_expr()),
                    f"characteristic polynomial n={n}")
        audit.equal(observed.degree(), len(states), f"charpoly degree n={n}")
        spectral_rows.append((n, sp.factor(observed.as_expr())))

    # Count-measure propagation versus exact missing support, including t=0.
    for n in range(1, 6):
        for initial in cache[n]:
            reachable = {isolate_set(initial, support, n) for support in range(1 << n)}
            for target in cache[n]:
                admissible = admissible_missing(initial, target, n)
                audit.equal(bool(admissible), target in reachable,
                            f"eventual reachability n={n}")
            for t in range(0, 6):
                literal = advance_distribution(initial, n, t)
                support = support_distribution(initial, n, t)
                audit.equal(literal, support, f"exact-support kernel n={n},t={t}")
                audit.equal(sum(literal.values()), n**t, f"kernel mass n={n},t={t}")
                for target in cache[n]:
                    predicted_target = sum(
                        onto_words(t, n - missing.bit_count())
                        for missing in admissible_missing(initial, target, n)
                    )
                    audit.equal(literal[target], predicted_target,
                                f"target formula n={n},t={t}")
                    exact_time_possible = any(
                        (n - missing.bit_count() == 0 == t)
                        or (1 <= n - missing.bit_count() <= t)
                        for missing in admissible_missing(initial, target, n)
                    )
                    audit.equal(literal[target] > 0, exact_time_possible,
                                f"exact-time criterion n={n},t={t}")

    # Arbitrary-block absorption law and elementary-symmetric compression.
    for n in range(1, 8):
        discrete = tuple(1 << label for label in range(n))
        for initial in cache[n]:
            sizes = tuple(block.bit_count() for block in initial)
            for t in range(0, 7):
                literal = advance_distribution(initial, n, t)[discrete]
                formula = sum(
                    elementary_by_subsets(sizes, missing_count)
                    * onto_words(t, n - missing_count)
                    for missing_count in range(len(sizes) + 1)
                )
                audit.equal(literal, formula, f"absorption formula n={n},t={t}")

    # Smallest boundary: at t=0 the unique n=1 state uses missing set {1};
    # at positive time it uses missing set empty, and both give probability one.
    only = cache[1][0]
    audit.equal(advance_distribution(only, 1, 0), Counter({only: 1}), "n=1,t=0")
    audit.equal(support_distribution(only, 1, 0), Counter({only: 1}), "n=1 support t=0")
    audit.equal(advance_distribution(only, 1, 4), Counter({only: 1}), "n=1 positive time")

    print("P179_REVIEW_A_BITBLOCK_CHARPOLY_AUDIT")
    for n, bell, layers, maximum in rows:
        print(f"n={n} Bell={bell} singleton_layers={layers} max_distinct_predecessors={maximum}")
    print("CHARPOLY_FACTORS=" + ";".join(f"n{n}:{factor}" for n, factor in spectral_rows))
    print("BOUNDARIES=t0_and_n1_PASS;missing_n_minus_1_PASS")
    print("KERNEL=exact_support_and_exact_time_PASS;n<=5,t<=5")
    print("ABSORPTION=all_sources_n<=7,t<=6_PASS")
    print(f"ASSERTIONS={audit.assertions}")
    print("RESULT=PASS")
    print("EXTERNAL_STATUS=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
