#!/usr/bin/env python3
"""Exact controls for synchronous MIS polarity dynamics.

The bitset and literal-set implementations are deliberately separate.  No
floating point arithmetic is used.
"""

from itertools import combinations


ASSERTIONS = 0


def check(condition, message="exact assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def gamma_bits(state, adjacency, mask):
    out = 0
    for v, neighbors in enumerate(adjacency):
        if neighbors & state == 0:
            out |= 1 << v
    return out & mask


def gamma_sets(state, edges, n):
    active = set(state)
    out = set()
    for v in range(n):
        if all(not ({u, v} in edges) for u in active if u != v):
            out.add(v)
    return frozenset(out)


def is_maximal_independent_bits(state, adjacency, n):
    for v in range(n):
        if state >> v & 1:
            if adjacency[v] & state:
                return False
        elif adjacency[v] & state == 0:
            return False
    return True


def adjacency_from_edge_mask(n, edge_mask):
    pairs = list(combinations(range(n), 2))
    adjacency = [0] * n
    edges = set()
    for bit, (u, v) in enumerate(pairs):
        if edge_mask >> bit & 1:
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
            edges.add(frozenset((u, v)))
    return adjacency, frozenset(edges)


def all_simple_graph_lane(max_n=6):
    graph_count = state_count = 0
    for n in range(max_n + 1):
        mask = (1 << n) - 1
        edge_slots = n * (n - 1) // 2
        for edge_mask in range(1 << edge_slots):
            adjacency, edges = adjacency_from_edge_mask(n, edge_mask)
            fixed = closed = image = 0
            image_states = set()
            for state in range(1 << n):
                first = gamma_bits(state, adjacency, mask)
                second = gamma_bits(first, adjacency, mask)
                third = gamma_bits(second, adjacency, mask)
                check(third == first, "cubic polarity identity failed")
                check((first == state)
                      == is_maximal_independent_bits(state, adjacency, n),
                      "MIS fixed-point criterion failed")
                state_set = frozenset(v for v in range(n) if state >> v & 1)
                literal = gamma_sets(state_set, edges, n)
                literal_bits = sum(1 << v for v in literal)
                check(literal_bits == first, "independent update routes differ")
                fixed += first == state
                closed += second == state
                image_states.add(first)
                state_count += 1
            image = len(image_states)
            check(image == closed, "image and closed configurations differ")
            check((closed - fixed) % 2 == 0, "two-cycle parity failed")
            graph_count += 1
    return graph_count, state_count


def bipartite_adjacency(left, right, edge_mask):
    n = left + right
    adjacency = [0] * n
    for i in range(left):
        for j in range(right):
            bit = i * right + j
            if edge_mask >> bit & 1:
                u, v = i, left + j
                adjacency[u] |= 1 << v
                adjacency[v] |= 1 << u
    return adjacency


def bipartite_square_lane(max_side=3):
    graphs = states = 0
    for left in range(max_side + 1):
        for right in range(max_side + 1):
            n = left + right
            mask = (1 << n) - 1
            for edge_mask in range(1 << (left * right)):
                adjacency = bipartite_adjacency(left, right, edge_mask)
                fixed = closed = 0
                for state in range(1 << n):
                    first = gamma_bits(state, adjacency, mask)
                    second = gamma_bits(first, adjacency, mask)
                    fixed += first == state
                    closed += second == state
                    states += 1
                check(closed == fixed * fixed,
                      "bipartite periodic square law failed")
                check((closed - fixed) // 2 == fixed * (fixed - 1) // 2,
                      "bipartite two-cycle count failed")
                graphs += 1
    return graphs, states


def path_adjacency(n):
    adjacency = [0] * n
    for v in range(n - 1):
        adjacency[v] |= 1 << (v + 1)
        adjacency[v + 1] |= 1 << v
    return adjacency


def path_lane(max_n=17):
    recurrence = [1, 1, 2]
    for n in range(3, max_n + 1):
        recurrence.append(recurrence[n - 2] + recurrence[n - 3])
    states = 0
    rows = []
    for n in range(max_n + 1):
        adjacency = path_adjacency(n)
        mask = (1 << n) - 1
        fixed = closed = 0
        for state in range(1 << n):
            first = gamma_bits(state, adjacency, mask)
            second = gamma_bits(first, adjacency, mask)
            fixed += first == state
            closed += second == state
            states += 1
        check(fixed == recurrence[n], "path MIS recurrence failed")
        check(closed == fixed * fixed, "path square law failed")

        for k in range(1, 7):
            iterate_fixed = 0
            for state in range(1 << n):
                iterate = state
                for _ in range(k):
                    iterate = gamma_bits(iterate, adjacency, mask)
                iterate_fixed += iterate == state
            check(iterate_fixed == (fixed if k % 2 else closed),
                  "path odd/even fixed sequence failed")
        rows.append((n, fixed, closed, (closed - fixed) // 2))
    return states, rows


def registered_sentinels():
    # K2: two singleton fixed points and the empty/full two-cycle.
    adjacency = path_adjacency(2)
    mask = 3
    orbit_empty = [0]
    for _ in range(4):
        orbit_empty.append(gamma_bits(orbit_empty[-1], adjacency, mask))
    check(orbit_empty == [0, 3, 0, 3, 0], "K2 sentinel failed")

    # K3: three singleton fixed points plus empty/full as the only 2-cycle.
    adjacency = [0b110, 0b101, 0b011]
    fixed = closed = 0
    for state in range(8):
        first = gamma_bits(state, adjacency, 7)
        second = gamma_bits(first, adjacency, 7)
        fixed += first == state
        closed += second == state
    check((fixed, closed) == (3, 5), "K3 nonbipartite sentinel failed")
    return orbit_empty


def main():
    sentinel = registered_sentinels()
    simple_graphs, simple_states = all_simple_graph_lane()
    bip_graphs, bip_states = bipartite_square_lane()
    path_states, rows = path_lane()
    print("synchronous MIS polarity exact controls: PASS")
    print(f"assertions: {ASSERTIONS}")
    print(f"all simple graphs through n=6: {simple_graphs}")
    print(f"simple-graph state evaluations: {simple_states}")
    print(f"bipartite graphs through 3+3: {bip_graphs}")
    print(f"bipartite state evaluations: {bip_states}")
    print(f"path state evaluations through n=17: {path_states}")
    print(f"K2 empty orbit sentinel: {sentinel}")
    print("path rows (n, fixed, closed, two_cycles):")
    for row in rows:
        print("  " + " ".join(map(str, row)))


if __name__ == "__main__":
    main()
