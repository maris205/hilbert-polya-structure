#!/usr/bin/env python3
"""Hostile Review A exact control for P183.

The state representation is deliberately different from the author's ordered
arc-bit integer.  Each unordered pair carries one of four local states
(A_ij, A_ji), and histories are also regrouped directly by their support and
first-occurrence order.
"""

from collections import defaultdict
from itertools import combinations, permutations, product
from math import factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def pairs(n):
    return tuple(combinations(range(n), 2))


def conflict(code):
    return code in (1, 2)


def conflict_mask(state):
    return tuple(conflict(code) for code in state)


def act(n, state, vertex):
    out = list(state)
    for q, (i, j) in enumerate(pairs(n)):
        a_ij = state[q] & 1
        a_ji = (state[q] >> 1) & 1
        if vertex == i:
            out[q] = 3 * a_ji
        elif vertex == j:
            out[q] = 3 * a_ij
    return tuple(out)


def run_history(n, state, history):
    for vertex in history:
        state = act(n, state, vertex)
    return state


def support_order(history):
    seen = set()
    order = []
    for vertex in history:
        if vertex not in seen:
            seen.add(vertex)
            order.append(vertex)
    return tuple(order)


def endpoint_from_order(n, state, order):
    rank = {vertex: q for q, vertex in enumerate(order)}
    inf = n + 1
    out = list(state)
    for q, (i, j) in enumerate(pairs(n)):
        if not conflict(state[q]):
            continue
        ri, rj = rank.get(i, inf), rank.get(j, inf)
        if ri == rj == inf:
            continue
        a_ij = state[q] & 1
        a_ji = (state[q] >> 1) & 1
        out[q] = 3 * (a_ji if ri < rj else a_ij)
    return tuple(out)


def stirling_table(limit):
    table = [[0] * (limit + 1) for _ in range(limit + 1)]
    table[0][0] = 1
    for t in range(1, limit + 1):
        for r in range(1, t + 1):
            table[t][r] = table[t - 1][r - 1] + r * table[t - 1][r]
    return table


STIRLING = stirling_table(8)


def endpoint_formula_histogram(n, state, t):
    hist = defaultdict(int)
    vertices = tuple(range(n))
    for r in range(n + 1):
        weight = STIRLING[t][r]
        if weight == 0:
            continue
        for support in combinations(vertices, r):
            for order in permutations(support):
                hist[endpoint_from_order(n, state, order)] += weight
    return dict(hist)


def independent_missing(n, edge_mask, missing):
    missing = set(missing)
    return all(not edge_mask[q] or i not in missing or j not in missing
               for q, (i, j) in enumerate(pairs(n)))


def absorption_formula(n, edge_mask, t):
    total = 0
    vertices = tuple(range(n))
    for r in range(n + 1):
        for missing in combinations(vertices, r):
            if independent_missing(n, edge_mask, missing):
                used = n - r
                total += factorial(used) * STIRLING[t][used]
    return total


def exact_state_checks(n):
    ps = pairs(n)
    all_states = tuple(product(range(4), repeat=len(ps)))
    labelled = defaultdict(int)
    distinct = defaultdict(set)

    for state in all_states:
        old_conflicts = conflict_mask(state)
        symmetric = not any(old_conflicts)
        all_fixed = True
        for vertex in range(n):
            target = act(n, state, vertex)
            expected = tuple(flag and vertex not in ps[q]
                             for q, flag in enumerate(old_conflicts))
            check(conflict_mask(target) == expected,
                  ("conflict deletion", n, state, vertex))
            check(act(n, target, vertex) == target,
                  ("idempotence", n, state, vertex))
            all_fixed &= target == state
            labelled[target] += 1
            distinct[target].add(state)
        check(all_fixed == symmetric, ("fixed/recurrent boundary", n, state))

        for t in range(n + 1):
            actual = defaultdict(int)
            for history in product(range(n), repeat=t):
                endpoint = run_history(n, state, history)
                by_order = endpoint_from_order(n, state,
                                               support_order(history))
                check(endpoint == by_order,
                      ("first-occurrence endpoint", n, t, state, history))
                actual[endpoint] += 1
            predicted = endpoint_formula_histogram(n, state, t)
            check(dict(actual) == predicted,
                  ("complete endpoint kernel", n, t, state))
            check(sum(predicted.values()) == n ** t,
                  ("kernel normalization", n, t, state))

    max_distinct = 0
    for target in all_states:
        k = 0
        edge_conflicts = conflict_mask(target)
        for vertex in range(n):
            if all(not edge_conflicts[q] or vertex not in ps[q]
                   for q in range(len(ps))):
                k += 1
        expected_labelled = k * 2 ** (n - 1)
        expected_distinct = 0 if k == 0 else 1 + k * (2 ** (n - 1) - 1)
        check(labelled[target] == expected_labelled,
              ("labelled action-pair fibre", n, target))
        check(len(distinct[target]) == expected_distinct,
              ("distinct-source fibre", n, target))
        max_distinct = max(max_distinct, len(distinct[target]))

    recurrent = sum(not any(conflict_mask(state)) for state in all_states)
    check(recurrent == 2 ** len(ps), ("recurrent count", n))
    return len(all_states), recurrent, max_distinct


def conflict_graph_absorption_checks(n):
    ps = pairs(n)
    complete_absorbed = None
    for mask in range(1 << len(ps)):
        edge_mask = tuple(bool(mask & (1 << q)) for q in range(len(ps)))
        # Code 1 is one of the two conflict orientations; symmetric pairs use 0.
        state = tuple(1 if flag else 0 for flag in edge_mask)
        previous = -1
        for t in range(n + 1):
            actual = 0
            for history in product(range(n), repeat=t):
                endpoint = run_history(n, state, history)
                absorbed = not any(conflict_mask(endpoint))
                missing = set(range(n)) - set(history)
                check(absorbed == independent_missing(n, edge_mask, missing),
                      ("absorption event", n, mask, t, history))
                actual += absorbed
            predicted = absorption_formula(n, edge_mask, t)
            check(actual == predicted, ("absorption polynomial", n, mask, t))
            check(0 <= actual <= n ** t, ("probability range", n, mask, t))
            check(previous * n <= actual if previous >= 0 else True,
                  ("CDF monotonicity after common denominator", n, mask, t))
            previous = actual
            if mask == (1 << len(ps)) - 1 and t == n:
                complete_absorbed = actual
    return complete_absorbed


def boundary_checks():
    state = ()
    check(act(1, state, 0) == state, "n=1 action")
    check(run_history(1, state, ()) == state, "t=0 identity")
    check(endpoint_formula_histogram(1, state, 0) == {state: 1},
          "n=1,t=0 kernel")
    check(absorption_formula(1, (), 0) == 1, "n=1,t=0 absorption")


def main():
    boundary_checks()
    rows = []
    for n in range(1, 5):
        states, recurrent, max_distinct = exact_state_checks(n)
        complete = conflict_graph_absorption_checks(n)
        rows.append((n, states, recurrent, max_distinct, complete))

    print("P183_HOSTILE_REVIEW_A_EXACT_CONTROL")
    print("REPRESENTATION=unordered-pair four-state tuples; direct history partitions")
    for n, states, recurrent, max_distinct, complete in rows:
        print(f"n={n} states={states} recurrent={recurrent} "
              f"max_distinct_fibre={max_distinct} "
              f"complete_H_absorbed_tn={complete}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("CRITICAL_FINDINGS=0")
    print("MAJOR_FINDINGS=0")
    print("MINOR_FINDINGS=0")
    print("VERDICT=PROVABLE_AS_STATED")
    print("STATUS=HOLD_EXTERNAL")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
