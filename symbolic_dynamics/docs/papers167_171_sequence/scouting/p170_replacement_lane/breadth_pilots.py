#!/usr/bin/env python3
"""Bounded exact breadth pilots for the P170 replacement lane.

The program is a falsifier, not a novelty test.  It probes eighteen literal
finite self-map forms on relation, hypergraph, word, and finite-field carriers.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def functional_summary(states, update):
    states = tuple(states)
    nxt = {state: update(state) for state in states}
    for target in nxt.values():
        check(target in nxt, "self-map closure")
    indegree = Counter(nxt.values())
    fixed = sum(nxt[state] == state for state in states)
    periodic_states = Counter()
    maximum_tail = 0
    for start in states:
        seen = {}
        state = start
        while state not in seen:
            seen[state] = len(seen)
            state = nxt[state]
        tail = seen[state]
        period = len(seen) - tail
        maximum_tail = max(maximum_tail, tail)
        if tail == 0:
            periodic_states[period] += 1
    return {
        "states": len(states),
        "image": len(indegree),
        "fixed": fixed,
        "periodic_states_by_period": dict(sorted(periodic_states.items())),
        "max_tail": maximum_tail,
        "max_fibre": max(indegree.values()),
    }


def relation_rows(matrix: int, n: int):
    mask = (1 << n) - 1
    return [(matrix >> (i * n)) & mask for i in range(n)]


def relation_columns(matrix: int, n: int):
    return [sum(((matrix >> (i * n + j)) & 1) << i for i in range(n))
            for j in range(n)]


def relation_from_predicate(n: int, predicate):
    return sum(1 << (i * n + j) for i in range(n) for j in range(n)
               if predicate(i, j))


def row_proper_inclusion(matrix: int, n: int) -> int:
    rows = relation_rows(matrix, n)
    return relation_from_predicate(
        n, lambda i, j: rows[i] != rows[j] and rows[i] & ~rows[j] == 0
    )


def row_weight_order(matrix: int, n: int) -> int:
    weights = [row.bit_count() for row in relation_rows(matrix, n)]
    return relation_from_predicate(n, lambda i, j: weights[i] < weights[j])


def row_column_degree_lt(matrix: int, n: int) -> int:
    rows = [row.bit_count() for row in relation_rows(matrix, n)]
    columns = [column.bit_count() for column in relation_columns(matrix, n)]
    return relation_from_predicate(n, lambda i, j: rows[i] < columns[j])


def row_intersection_graph(matrix: int, n: int) -> int:
    rows = relation_rows(matrix, n)
    return relation_from_predicate(
        n, lambda i, j: i != j and bool(rows[i] & rows[j])
    )


def row_gram_parity(matrix: int, n: int) -> int:
    rows = relation_rows(matrix, n)
    return relation_from_predicate(
        n, lambda i, j: (rows[i] & rows[j]).bit_count() % 2 == 1
    )


def family_edges(family: int, n: int):
    return [edge for edge in range(1, 1 << n) if family >> (edge - 1) & 1]


def edge_family(edges) -> int:
    return sum(1 << (edge - 1) for edge in set(edges) if edge)


def clutterize(family: int, n: int) -> int:
    edges = family_edges(family, n)
    return edge_family(edge for edge in edges
                       if not any(other != edge and other & ~edge == 0
                                  for other in edges))


def blocker(family: int, n: int) -> int:
    edges = family_edges(clutterize(family, n), n)
    if not edges:
        return 0
    hitting = [candidate for candidate in range(1, 1 << n)
               if all(candidate & edge for edge in edges)]
    return edge_family(candidate for candidate in hitting
                       if not any(other != candidate and other & ~candidate == 0
                                  for other in hitting))


def intersection_closure_step(family: int, n: int) -> int:
    edges = family_edges(family, n)
    return family | edge_family(left & right for left in edges for right in edges)


def union_closure_step(family: int, n: int) -> int:
    edges = family_edges(family, n)
    return family | edge_family(left | right for left in edges for right in edges)


def xor_closure_step(family: int, n: int) -> int:
    edges = family_edges(family, n)
    return family | edge_family(left ^ right for left in edges for right in edges)


def overlapping_union_clutter(family: int, n: int) -> int:
    edges = family_edges(clutterize(family, n), n)
    unions = [left | right for index, left in enumerate(edges)
              for right in edges[index + 1:] if left & right]
    return clutterize(edge_family(unions), n)


def word_bit(word: int, position: int) -> int:
    return word >> position & 1


def repeat_toggle(word: int, n: int) -> int:
    seen = set()
    out = 0
    for i in range(n):
        bit = word_bit(word, i)
        value = bit ^ (bit in seen)
        out |= int(value) << i
        seen.add(bit)
    return out


def suffix_record_mask(word: int, n: int) -> int:
    bits = tuple(word_bit(word, i) for i in range(n))
    best = None
    out = 0
    for i in range(n):
        suffix = bits[i:]
        if best is None or suffix < best:
            out |= 1 << i
            best = suffix
    return out


def isolated_cyclic_mask(word: int, n: int) -> int:
    return sum(1 << i for i in range(n)
               if word_bit(word, (i - 1) % n) == word_bit(word, (i + 1) % n)
               and word_bit(word, i) != word_bit(word, (i - 1) % n))


def run_parity_projection(word: int, n: int) -> int:
    bits = [word_bit(word, i) for i in range(n)]
    out = 0
    start = 0
    while start < n:
        end = start + 1
        while end < n and bits[end] == bits[start]:
            end += 1
        if (end - start) % 2:
            for i in range(start, end):
                out |= 1 << i
        start = end
    return out


def inv0(value: int, p: int) -> int:
    return 0 if value == 0 else pow(value, p - 2, p)


def pair_decode(state: int, p: int):
    return divmod(state, p)


def pair_encode(x: int, y: int, p: int) -> int:
    return (x % p) * p + (y % p)


def elementary_symmetric_pair(state: int, p: int) -> int:
    x, y = pair_decode(state, p)
    return pair_encode(x + y, x * y, p)


def sum_square_pair(state: int, p: int) -> int:
    x, y = pair_decode(state, p)
    return pair_encode(x + y, x * x + y * y, p)


def mutual_square_add(state: int, p: int) -> int:
    x, y = pair_decode(state, p)
    return pair_encode(x + y * y, y + x * x, p)


def reciprocal_cross(state: int, p: int) -> int:
    x, y = pair_decode(state, p)
    return pair_encode(x + inv0(y, p), y + inv0(x, p), p)


def main() -> None:
    report = {}

    relation_maps = {
        "R01_row_proper_inclusion": row_proper_inclusion,
        "R02_row_weight_order": row_weight_order,
        "R03_row_column_degree_lt": row_column_degree_lt,
        "R04_row_intersection_graph": row_intersection_graph,
        "R05_row_gram_parity": row_gram_parity,
    }
    for name, update in relation_maps.items():
        report[name] = {}
        for n in range(1, 5):
            report[name][str(n)] = functional_summary(
                range(1 << (n * n)), lambda state, n=n, update=update: update(state, n)
            )

    hypergraph_maps = {
        "H01_blocker": blocker,
        "H02_intersection_closure": intersection_closure_step,
        "H03_union_closure": union_closure_step,
        "H04_xor_closure": xor_closure_step,
        "H05_overlapping_union_clutter": overlapping_union_clutter,
    }
    for name, update in hypergraph_maps.items():
        report[name] = {}
        for n in range(1, 5):
            report[name][str(n)] = functional_summary(
                range(1 << ((1 << n) - 1)),
                lambda state, n=n, update=update: update(state, n),
            )

    word_maps = {
        "W01_repeat_toggle": repeat_toggle,
        "W02_suffix_record_mask": suffix_record_mask,
        "W03_isolated_cyclic_mask": isolated_cyclic_mask,
        "W04_run_parity_projection": run_parity_projection,
    }
    for name, update in word_maps.items():
        report[name] = {}
        for n in range(1, 11):
            report[name][str(n)] = functional_summary(
                range(1 << n), lambda state, n=n, update=update: update(state, n)
            )

    ring_maps = {
        "F01_elementary_symmetric_pair": elementary_symmetric_pair,
        "F02_sum_square_pair": sum_square_pair,
        "F03_mutual_square_add": mutual_square_add,
        "F04_reciprocal_cross": reciprocal_cross,
    }
    for name, update in ring_maps.items():
        report[name] = {}
        for p in (2, 3, 5, 7, 11, 13, 17, 19):
            report[name][str(p)] = functional_summary(
                range(p * p), lambda state, p=p, update=update: update(state, p)
            )

    check(len(report) == 18, "eighteen map forms")
    payload = {
        "assertions": ASSERTIONS,
        "candidate_count": len(report),
        "decision": "NO_FRESH_SURVIVOR_REENTER_RPS",
        "external_status": "HOLD_EXTERNAL",
        "pilots": report,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True)
    payload["payload_sha256"] = hashlib.sha256(encoded.encode()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
