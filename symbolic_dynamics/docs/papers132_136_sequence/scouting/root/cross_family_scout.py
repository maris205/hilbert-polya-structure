#!/usr/bin/env python3
"""Exact breadth scout for the P132--P136 root/cross-family lane.

Every map below is literal.  The finite ranges are counterexample pressure,
not proofs or novelty evidence.  Output is deterministic and uses only the
standard library.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product
from math import factorial


ASSERTIONS = 0


def check(condition: bool, message: str = "assertion failed") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def functional_summary(states, step):
    states = tuple(states)
    state_set = set(states)
    nxt = {}
    indegree = Counter()
    for state in states:
        image = step(state)
        check(image in state_set, f"map escaped carrier: {state!r} -> {image!r}")
        nxt[state] = image
        indegree[image] += 1

    tails = Counter()
    periods = Counter()
    max_tail = 0
    for start in states:
        seen = {}
        path = []
        state = start
        while state not in seen:
            seen[state] = len(path)
            path.append(state)
            state = nxt[state]
        cycle_start = seen[state]
        tail = cycle_start
        period = len(path) - cycle_start
        check(period >= 1)
        probe = start
        for _ in range(tail):
            probe = nxt[probe]
        cycle_probe = probe
        for _ in range(period):
            cycle_probe = nxt[cycle_probe]
        check(cycle_probe == probe)
        tails[tail] += 1
        periods[period] += 1
        max_tail = max(max_tail, tail)

    return {
        "states": len(states),
        "image": len(indegree),
        "fixed": sum(1 for s in states if nxt[s] == s),
        "max_tail": max_tail,
        "periods": tuple(sorted(periods)),
        "max_fibre": max(indegree.values(), default=0),
    }


def emit(identifier: str, scope: str, states, step) -> None:
    before = ASSERTIONS
    summary = functional_summary(states, step)
    used = ASSERTIONS - before
    print(
        f"{identifier} scope={scope} states={summary['states']} "
        f"image={summary['image']} fixed={summary['fixed']} "
        f"max_tail={summary['max_tail']} periods={summary['periods']} "
        f"max_fibre={summary['max_fibre']} assertions={used}"
    )


# ---------------------------------------------------------------------------
# Truncated characteristic-two algebra


def frobenius_square(value: int, truncation: int) -> int:
    out = 0
    for bit in range(truncation - 1):
        if (value >> bit) & 1:
            exponent = bit + 1
            if 2 * exponent < truncation:
                out |= 1 << (2 * exponent - 1)
    return out


def v2(value: int) -> int:
    out = 0
    while value % 2 == 0:
        value //= 2
        out += 1
    return out


def truncated_algebra_states(max_truncation: int):
    return tuple(
        (n, value)
        for n in range(2, max_truncation + 1)
        for value in range(1 << (n - 1))
    )


def run_truncated_algebra() -> None:
    states = truncated_algebra_states(12)

    def shear(state):
        n, value = state
        return n, value ^ frobenius_square(value, n)

    emit("X01", "xF2[x]/(x^N),2<=N<=12; f->f+f^2", states, shear)

    # Fixed points of the t-th iterate depend only on v_2(t).
    for n in range(2, 13):
        local = tuple(range(1 << (n - 1)))
        for t in range(1, 13):
            fixed = 0
            for value in local:
                image = value
                for _ in range(t):
                    image ^= frobenius_square(image, n)
                fixed += image == value
            power = 2 ** (2 ** v2(t))
            dimension = (n - 1) - ((n - 1) // power)
            check(fixed == 2**dimension, f"X01 fixed formula N={n},t={t}")

    def affine(state):
        n, value = state
        return n, 1 ^ frobenius_square(value, n)

    emit("X02", "xF2[x]/(x^N),2<=N<=12; f->x+f^2", states, affine)

    def pure(state):
        n, value = state
        return n, frobenius_square(value, n)

    emit("X03", "xF2[x]/(x^N),2<=N<=12; f->f^2", states, pure)


# ---------------------------------------------------------------------------
# Cyclic binary words


def rotate_left(word: int, n: int) -> int:
    mask = (1 << n) - 1
    return ((word << 1) & mask) | (word >> (n - 1))


def rotate_right(word: int, n: int) -> int:
    return (word >> 1) | ((word & 1) << (n - 1))


def cyclic_word_states(max_n: int):
    return tuple((n, w) for n in range(3, max_n + 1) for w in range(1 << n))


def run_cyclic_words() -> None:
    states = cyclic_word_states(11)

    emit(
        "X04",
        "cyclic binary words 3<=n<=11; w->w xor shift(w)",
        states,
        lambda s: (s[0], s[1] ^ rotate_left(s[1], s[0])),
    )
    emit(
        "X05",
        "cyclic binary words 3<=n<=11; w->w and shift(w)",
        states,
        lambda s: (s[0], s[1] & rotate_left(s[1], s[0])),
    )
    emit(
        "X06",
        "cyclic binary words 3<=n<=11; w->w or shift(w)",
        states,
        lambda s: (s[0], s[1] | rotate_left(s[1], s[0])),
    )

    def majority(state):
        n, word = state
        left = rotate_left(word, n)
        right = rotate_right(word, n)
        out = (word & left) | (word & right) | (left & right)
        return n, out

    emit(
        "X07",
        "cyclic binary words 3<=n<=11; synchronous radius-one majority",
        states,
        majority,
    )

    def disagree_flip(state):
        n, word = state
        return n, word ^ rotate_left(word, n) ^ rotate_right(word, n)

    emit(
        "X08",
        "cyclic binary words 3<=n<=11; flip iff neighbours disagree",
        states,
        disagree_flip,
    )


# ---------------------------------------------------------------------------
# Simple graphs


def graph_edges(n: int):
    return tuple(combinations(range(n), 2))


def graph_adjacency(n: int, mask: int):
    adj = [set() for _ in range(n)]
    for bit, (u, v) in enumerate(graph_edges(n)):
        if (mask >> bit) & 1:
            adj[u].add(v)
            adj[v].add(u)
    return adj


def graph_mask(n: int, pairs) -> int:
    lookup = {edge: bit for bit, edge in enumerate(graph_edges(n))}
    out = 0
    for u, v in pairs:
        if u > v:
            u, v = v, u
        out |= 1 << lookup[(u, v)]
    return out


def graph_states(max_n: int):
    return tuple(
        (n, mask)
        for n in range(1, max_n + 1)
        for mask in range(1 << len(graph_edges(n)))
    )


def common_parity_graph(state):
    n, mask = state
    adj = graph_adjacency(n, mask)
    pairs = []
    for u, v in graph_edges(n):
        if len(adj[u] & adj[v]) % 2:
            pairs.append((u, v))
    return n, graph_mask(n, pairs)


def component_cliques(state):
    n, mask = state
    adj = graph_adjacency(n, mask)
    seen = set()
    pairs = []
    for root in range(n):
        if root in seen:
            continue
        stack = [root]
        component = []
        seen.add(root)
        while stack:
            u = stack.pop()
            component.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        pairs.extend(combinations(sorted(component), 2))
    return n, graph_mask(n, pairs)


def component_complements(state):
    n, mask = state
    adj = graph_adjacency(n, mask)
    seen = set()
    pairs = []
    for root in range(n):
        if root in seen:
            continue
        stack = [root]
        component = []
        seen.add(root)
        while stack:
            u = stack.pop()
            component.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        for u, v in combinations(sorted(component), 2):
            if v not in adj[u]:
                pairs.append((u, v))
    return n, graph_mask(n, pairs)


def odd_degree_induced_toggle(state):
    n, mask = state
    adj = graph_adjacency(n, mask)
    odd = {v for v in range(n) if len(adj[v]) % 2}
    toggle = graph_mask(n, combinations(sorted(odd), 2))
    return n, mask ^ toggle


def odd_k4_cut_switch(state):
    n, mask = state
    adj = graph_adjacency(n, mask)
    selected = set()
    for v in range(n):
        count = 0
        for triple in combinations(adj[v], 3):
            if all(b in adj[a] for a, b in combinations(triple, 2)):
                count += 1
        if count % 2:
            selected.add(v)
    cut = []
    for u in selected:
        for v in range(n):
            if v not in selected and u < v:
                cut.append((u, v))
            elif v not in selected and v < u:
                cut.append((v, u))
    return n, mask ^ graph_mask(n, set(cut))


def run_graphs() -> None:
    states = graph_states(6)
    emit("X09", "simple graphs n<=6; odd common-neighbour graph", states, common_parity_graph)
    emit(
        "X10",
        "simple graphs n<=6; toggle edges of odd common-neighbour graph",
        states,
        lambda s: (s[0], s[1] ^ common_parity_graph(s)[1]),
    )
    emit("X11", "simple graphs n<=6; complete each current component", states, component_cliques)
    emit("X12", "simple graphs n<=6; complement inside each current component", states, component_complements)
    emit("X13", "simple graphs n<=6; toggle induced graph on odd-degree vertices", states, odd_degree_induced_toggle)
    emit("X14", "simple graphs n<=6; switch cut of vertices in an odd number of K4s", states, odd_k4_cut_switch)


# ---------------------------------------------------------------------------
# Permutations


def inverse_permutation(perm):
    out = [0] * len(perm)
    for i, value in enumerate(perm):
        out[value] = i
    return tuple(out)


def compose_permutations(left, right):
    return tuple(left[right[i]] for i in range(len(left)))


def reverse_flagged_runs(perm, flag):
    out = list(perm)
    n = len(out)
    i = 0
    while i < n:
        if not flag(i, out[i]):
            i += 1
            continue
        j = i + 1
        while j < n and flag(j, out[j]):
            j += 1
        out[i:j] = reversed(out[i:j])
        i = j
    return tuple(out)


def permutation_states(max_n: int):
    return tuple((n, p) for n in range(1, max_n + 1) for p in permutations(range(n)))


def run_permutations() -> None:
    states = permutation_states(8)
    emit("X15", "permutations n<=8; inversion", states, lambda s: (s[0], inverse_permutation(s[1])))
    emit(
        "X16",
        "permutations n<=8; reverse-complement conjugation",
        states,
        lambda s: (s[0], tuple(s[0] - 1 - s[1][s[0] - 1 - i] for i in range(s[0]))),
    )
    emit(
        "X17",
        "permutations n<=8; squaring",
        states,
        lambda s: (s[0], compose_permutations(s[1], s[1])),
    )
    emit(
        "X18",
        "permutations n<=8; reverse maximal excedance-position runs",
        states,
        lambda s: (s[0], reverse_flagged_runs(s[1], lambda i, v: v > i)),
    )
    emit(
        "X19",
        "permutations n<=8; reverse maximal parity-agreement runs",
        states,
        lambda s: (s[0], reverse_flagged_runs(s[1], lambda i, v: (v - i) % 2 == 0)),
    )


# ---------------------------------------------------------------------------
# Set partitions as restricted-growth strings


def restricted_growth_strings(n: int):
    if n == 0:
        yield ()
        return

    def rec(prefix, maximum):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for value in range(maximum + 2):
            prefix.append(value)
            yield from rec(prefix, max(maximum, value))
            prefix.pop()

    yield from rec([0], 0)


def canonical_rgs(labels):
    relabel = {}
    out = []
    for label in labels:
        if label not in relabel:
            relabel[label] = len(relabel)
        out.append(relabel[label])
    return tuple(out)


def partition_shift(rgs):
    n = len(rgs)
    if n <= 1:
        return rgs
    out = [0] * n
    for i, label in enumerate(rgs):
        out[(i + 1) % n] = label
    return canonical_rgs(out)


def partition_meet(a, b):
    return canonical_rgs(tuple(zip(a, b)))


def partition_join(a, b):
    n = len(a)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    for labels in (a, b):
        first = {}
        for i, label in enumerate(labels):
            if label in first:
                union(first[label], i)
            else:
                first[label] = i
    return canonical_rgs(find(i) for i in range(n))


def merge_consecutive_minima(rgs):
    blocks = {}
    for i, label in enumerate(rgs):
        blocks.setdefault(label, []).append(i)
    minima = sorted((members[0], label) for label, members in blocks.items())
    parent = {label: label for label in blocks}

    def find(label):
        while parent[label] != label:
            parent[label] = parent[parent[label]]
            label = parent[label]
        return label

    for (m1, b1), (m2, b2) in zip(minima, minima[1:]):
        if m2 == m1 + 1:
            parent[find(b2)] = find(b1)
    return canonical_rgs(find(label) for label in rgs)


def partition_states(max_n: int):
    return tuple((n, rgs) for n in range(max_n + 1) for rgs in restricted_growth_strings(n))


def run_set_partitions() -> None:
    states = partition_states(8)
    emit("X20", "set partitions n<=8; cyclically shift elements", states, lambda s: (s[0], partition_shift(s[1])))
    emit(
        "X21",
        "set partitions n<=8; meet with one-step cyclic shift",
        states,
        lambda s: (s[0], partition_meet(s[1], partition_shift(s[1]))),
    )
    emit(
        "X22",
        "set partitions n<=8; join with reflected partition",
        states,
        lambda s: (s[0], partition_join(s[1], canonical_rgs(reversed(s[1])))),
    )
    emit(
        "X23",
        "set partitions n<=8; merge blocks with consecutive minima",
        states,
        lambda s: (s[0], merge_consecutive_minima(s[1])),
    )
    emit(
        "X24",
        "set partitions n<=8; reflect the ground-set order",
        states,
        lambda s: (s[0], canonical_rgs(reversed(s[1]))),
    )


# ---------------------------------------------------------------------------
# Integer partitions


def integer_partitions(n: int, cap=None):
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for first in range(cap, 0, -1):
        for tail in integer_partitions(n - first, first):
            yield (first,) + tail


def bulgarian(partition):
    if not partition:
        return partition
    reduced = [part - 1 for part in partition if part > 1]
    reduced.append(len(partition))
    return tuple(sorted(reduced, reverse=True))


def ferrers_corner_erosion(partition):
    if not partition:
        return partition
    out = list(partition)
    i = 0
    while i < len(out):
        j = i + 1
        while j < len(out) and out[j] == out[i]:
            j += 1
        out[j - 1] -= 1
        i = j
    return tuple(sorted((x for x in out if x), reverse=True))


def run_integer_partitions() -> None:
    fixed_states = tuple((n, p) for n in range(1, 19) for p in integer_partitions(n))
    emit("X25", "integer partitions 1<=n<=18; Bulgarian solitaire", fixed_states, lambda s: (s[0], bulgarian(s[1])))

    variable_states = tuple((sum(p), p) for n in range(19) for p in integer_partitions(n))
    state_set = set(variable_states)

    def erode(state):
        out = ferrers_corner_erosion(state[1])
        image = (sum(out), out)
        check(image in state_set)
        return image

    emit("X26", "integer partitions of size<=18; delete every Ferrers corner", variable_states, erode)


# ---------------------------------------------------------------------------
# Perfect matchings with simultaneous adjacent-chord deletion


def perfect_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for j in range(1, len(vertices)):
        second = vertices[j]
        rest = vertices[1:j] + vertices[j + 1 :]
        for tail in perfect_matchings(rest):
            yield tuple(sorted(((first, second),) + tail))


def delete_adjacent_chords(matching):
    deleted = {x for a, b in matching if b == a + 1 for x in (a, b)}
    if not deleted:
        return matching
    survivors = [v for pair in matching for v in pair if v not in deleted]
    survivors = sorted(set(survivors))
    rank = {v: i for i, v in enumerate(survivors)}
    return tuple(sorted((rank[a], rank[b]) for a, b in matching if a not in deleted))


def run_matchings() -> None:
    states = tuple(
        (n, matching)
        for n in range(8)
        for matching in perfect_matchings(range(2 * n))
    )
    state_set = set(states)

    def step(state):
        out = delete_adjacent_chords(state[1])
        image = (len(out), out)
        check(image in state_set)
        return image

    emit("X27", "perfect matchings through 7 chords; delete all adjacent chords and standardize", states, step)


# ---------------------------------------------------------------------------
# Endofunction image pruning


def prune_endofunction(function):
    image = sorted(set(function))
    rank = {value: i for i, value in enumerate(image)}
    return tuple(rank[function[value]] for value in image)


def run_endofunctions() -> None:
    states = [(0, ())]
    for n in range(1, 7):
        states.extend((n, f) for f in product(range(n), repeat=n))
    states = tuple(states)
    state_set = set(states)

    def step(state):
        if state[0] == 0:
            return state
        out = prune_endofunction(state[1])
        image = (len(out), out)
        check(image in state_set)
        return image

    emit("X28", "endofunctions n<=6; restrict to current image and standardize", states, step)

    # The pruning depth equals maximum distance from a vertex to its cycle.
    for n in range(1, 7):
        for function in product(range(n), repeat=n):
            height = 0
            for start in range(n):
                seen = {}
                v = start
                time = 0
                while v not in seen:
                    seen[v] = time
                    time += 1
                    v = function[v]
                height = max(height, seen[v])
            current = function
            depth = 0
            while len(set(current)) < len(current):
                current = prune_endofunction(current)
                depth += 1
            check(depth == height, f"X28 height mismatch n={n},f={function}")


def main() -> None:
    run_truncated_algebra()
    run_cyclic_words()
    run_graphs()
    run_permutations()
    run_set_partitions()
    run_integer_partitions()
    run_matchings()
    run_endofunctions()
    print(f"TOTAL_ASSERTIONS={ASSERTIONS}")
    print("SYSTEMS_AUDITED=28")
    print("scope_sentinel=finite breadth search is falsification evidence, never proof")
    print("release_sentinel=owner non-hit is not novelty or priority; external HOLD")


if __name__ == "__main__":
    main()
