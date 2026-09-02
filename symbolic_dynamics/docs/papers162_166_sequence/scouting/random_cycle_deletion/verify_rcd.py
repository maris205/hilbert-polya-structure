#!/usr/bin/env python3
"""Independent exact scout for random cycle deletion (RCD).

States are literal partial permutations on subsets of [n].  No project code is
imported.  History enumeration, inclusion--exclusion, size-biased order, and
extension counts are computed by separate routines.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial


ASSERTIONS = 0


def check(ok, tag):
    global ASSERTIONS
    ASSERTIONS += 1
    if not ok:
        raise AssertionError(tag)


def partial_permutations(n):
    states = []
    for k in range(n + 1):
        for support in combinations(range(n), k):
            for image in permutations(support):
                state = [-1] * n
                for x, y in zip(support, image):
                    state[x] = y
                states.append(tuple(state))
    return states


def cycles(state):
    active = {i for i, y in enumerate(state) if y >= 0}
    unseen = set(active)
    answer = []
    while unseen:
        start = min(unseen)
        cycle = []
        x = start
        while x not in cycle:
            cycle.append(x)
            unseen.remove(x)
            x = state[x]
        check(x == start, ("partial-permutation", state))
        answer.append(frozenset(cycle))
    return tuple(answer)


def delete_label(state, label):
    if state[label] < 0:
        return state
    doomed = next(c for c in cycles(state) if label in c)
    out = list(state)
    for x in doomed:
        out[x] = -1
    return tuple(out)


def run_history(state, history):
    for label in history:
        state = delete_label(state, label)
    return state


def retained_after(source, retained_cycles):
    keep = set().union(*retained_cycles) if retained_cycles else set()
    return tuple(y if i in keep else -1 for i, y in enumerate(source))


def transition_count_formula(source, target, t):
    n = len(source)
    source_cycles = cycles(source)
    target_active = {i for i, y in enumerate(target) if y >= 0}
    retained = []
    deleted = []
    for c in source_cycles:
        if c <= target_active:
            retained.append(c)
        elif c.isdisjoint(target_active):
            deleted.append(c)
        else:
            return 0
    if retained_after(source, retained) != target:
        return 0
    a = len(target_active)
    total = 0
    for r in range(len(deleted) + 1):
        for chosen in combinations(deleted, r):
            total += (-1) ** r * (n - a - sum(map(len, chosen))) ** t
    return total


def tail_numerator(cycle_sizes, n, t):
    total = 0
    k = len(cycle_sizes)
    for r in range(1, k + 1):
        for chosen in combinations(range(k), r):
            total += (-1) ** (r + 1) * (n - sum(cycle_sizes[i] for i in chosen)) ** t
    return total


def mean_formula(cycle_sizes, n):
    total = Fraction(0)
    k = len(cycle_sizes)
    for r in range(1, k + 1):
        for chosen in combinations(range(k), r):
            mass = sum(cycle_sizes[i] for i in chosen)
            total += (-1) ** (r + 1) * Fraction(n, mass)
    return total


def mean_recursion(cycle_sizes, n):
    memo = {0: Fraction(0)}
    def solve(mask):
        if mask in memo:
            return memo[mask]
        mass = sum(cycle_sizes[i] for i in range(len(cycle_sizes)) if mask >> i & 1)
        value = Fraction(n)
        for i, size in enumerate(cycle_sizes):
            if mask >> i & 1:
                value += size * solve(mask ^ (1 << i))
        memo[mask] = value / mass
        return memo[mask]
    return solve((1 << len(cycle_sizes)) - 1)


def last_formula(cycle_sizes, chosen):
    others = [i for i in range(len(cycle_sizes)) if i != chosen]
    c = cycle_sizes[chosen]
    total = Fraction(0)
    for r in range(len(others) + 1):
        for subset in combinations(others, r):
            total += (-1) ** r * Fraction(c, c + sum(cycle_sizes[i] for i in subset))
    return total


def last_by_orders(cycle_sizes, chosen):
    total = Fraction(0)
    for order in permutations(range(len(cycle_sizes))):
        if order[-1] != chosen:
            continue
        remaining = sum(cycle_sizes)
        probability = Fraction(1)
        for i in order:
            probability *= Fraction(cycle_sizes[i], remaining)
            remaining -= cycle_sizes[i]
        total += probability
    return total


def integer_partitions(n, minimum=1):
    if n == 0:
        yield ()
    for first in range(minimum, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def permutation_cycles(perm):
    unseen = set(range(len(perm)))
    out = []
    while unseen:
        start = min(unseen)
        c = []
        x = start
        while x not in c:
            c.append(x)
            unseen.remove(x)
            x = perm[x]
        out.append(set(c))
    return out


def all_cycles_hit(perm, marked):
    return all(c & marked for c in permutation_cycles(perm))


def all_partial_cycles_hit(state, marked):
    return all(c & marked for c in cycles(state))


def stirling_surjections(t, r):
    return sum((-1) ** j * comb(r, j) * (r - j) ** t for j in range(r + 1))


def partial_extensions_for_support(m, r):
    """Partial permutations whose every active cycle hits a fixed r-set."""
    total = 1  # the empty extension
    for q in range(1, r + 1):
        for s in range(m - r + 1):
            total += comb(r, q) * comb(m - r, s) * q * factorial(q + s - 1)
    return total


def forward_suite():
    total_states = 0
    histories = 0
    for n in range(1, 6):
        states = partial_permutations(n)
        total_states += len(states)
        empty = (-1,) * n
        for source in states:
            source_cycles = cycles(source)
            sizes = tuple(map(len, source_cycles))
            for t in range(6):
                observed = Counter()
                for history in product(range(n), repeat=t):
                    observed[run_history(source, history)] += 1
                    histories += 1
                for target in states:
                    check(observed[target] == transition_count_formula(source, target, t),
                          ("transition", n, source, target, t))
                check(sum(observed.values()) == n ** t, ("kernel-mass", n, source, t))
                if sizes:
                    check(n ** t - observed[empty] == tail_numerator(sizes, n, t),
                          ("absorption-tail", n, source, t))
                else:
                    check(observed[empty] == n ** t, ("empty-absorbing", n, t))
            if sizes:
                check(mean_formula(sizes, n) == mean_recursion(sizes, n),
                      ("mean", n, source))
    return total_states, histories


def last_survivor_suite():
    profiles = 0
    for total in range(1, 10):
        for sizes in integer_partitions(total):
            profiles += 1
            probabilities = []
            for i in range(len(sizes)):
                formula = last_formula(sizes, i)
                direct = last_by_orders(sizes, i)
                check(formula == direct, ("last", sizes, i, formula, direct))
                probabilities.append(formula)
            check(sum(probabilities) == 1, ("last-mass", sizes))
    return profiles


def extension_suite():
    fixed_support_checks = 0
    full_pair_checks = 0
    partial_pair_checks = 0
    for m in range(1, 8):
        perms = tuple(permutations(range(m)))
        for r in range(1, m + 1):
            for marked_tuple in combinations(range(m), r):
                marked = set(marked_tuple)
                observed = sum(all_cycles_hit(perm, marked) for perm in perms)
                check(observed == r * factorial(m - 1),
                      ("marked-cycle-identity", m, marked_tuple, observed))
                fixed_support_checks += 1

    for m in range(1, 6):
        perms = tuple(permutations(range(m)))
        for t in range(1, 6):
            observed = 0
            for perm in perms:
                for history in product(range(m), repeat=t):
                    if all_cycles_hit(perm, set(history)):
                        observed += 1
            expected = sum(
                comb(m, r) * stirling_surjections(t, r) * r * factorial(m - 1)
                for r in range(1, min(m, t) + 1)
            )
            check(observed == expected, ("extension-history", m, t, observed, expected))
            full_pair_checks += 1

    # Every partial source extension of a fixed target is target disjoint-union
    # a partial permutation on the m-label complement.  This independently
    # checks the stronger all-source census, including the empty extension and
    # t=0.
    for m in range(1, 6):
        states = partial_permutations(m)
        for t in range(6):
            observed = 0
            for state in states:
                for history in product(range(m), repeat=t):
                    if all_partial_cycles_hit(state, set(history)):
                        observed += 1
            if t == 0:
                expected = 1
            else:
                expected = sum(
                    comb(m, r)
                    * stirling_surjections(t, r)
                    * partial_extensions_for_support(m, r)
                    for r in range(1, min(m, t) + 1)
                )
            check(observed == expected,
                  ("partial-extension-history", m, t, observed, expected))
            partial_pair_checks += 1
    return fixed_support_checks, full_pair_checks, partial_pair_checks


def main():
    states, histories = forward_suite()
    profiles = last_survivor_suite()
    marked, full_pairs, partial_pairs = extension_suite()
    print("RCD_INDEPENDENT_EXACT_SCOUT_V1")
    print(f"PARTIAL_PERMUTATION_STATES={states}")
    print(f"LITERAL_HISTORIES_REPLAYED={histories}")
    print(f"LAST_SURVIVOR_SIZE_PROFILES={profiles}")
    print(f"MARKED_SUPPORT_IDENTITIES={marked}")
    print(f"FULL_EXTENSION_HISTORY_BOXES={full_pairs}")
    print(f"PARTIAL_EXTENSION_HISTORY_BOXES={partial_pairs}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("MATH_STATUS=PASS")
    print("DECISION=KILL_OWNER_AND_INTERNAL_ENGINE_COLLISION")
    print("EXTERNAL=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
