#!/usr/bin/env python3
"""Exact breadth falsifier for the P157--P161 probabilistic/geometric replacement lane.

Every pilot is finite and exhaustive on the printed small box.  Integer and
Fraction arithmetic are used throughout.  These checks are counterexample
pressure only: they prove neither an all-parameter statement nor novelty.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb


class Audit:
    def __init__(self):
        self.assertions = 0
        self.lanes = []

    def equal(self, left, right, label=""):
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")

    def true(self, condition, label=""):
        self.assertions += 1
        if not condition:
            raise AssertionError(label or "assertion failed")

    def lane(self, code, name, start, signature, decision):
        count = self.assertions - start
        self.lanes.append((code, count, decision))
        print(
            f"[{code} {name}] PASS assertions={count}; "
            f"signature={signature}; decision={decision}"
        )


# ---------------------------------------------------------------------------
# 1. PBL: rooted polygon block shaving


def block_shave_successors(state):
    state = tuple(state)
    n = len(state)
    if n == 1:
        return (state,)
    return tuple(
        state[:left] + state[right + 1 :]
        for left in range(n)
        for right in range(left, n)
        if not (left == 0 and right == n - 1)
    )


def shave_denominator(n):
    return (n - 1) * (n + 2) // 2


@lru_cache(maxsize=None)
def shave_clock_law(n):
    if n == 1:
        return ((0, Fraction(1)),)
    out = defaultdict(Fraction)
    denominator = shave_denominator(n)
    for q in range(1, n):
        multiplicity = q + 1
        for t, mass in shave_clock_law(q):
            out[t + 1] += Fraction(multiplicity, denominator) * mass
    return tuple(sorted(out.items()))


@lru_cache(maxsize=None)
def shave_terminal_law(state):
    state = tuple(state)
    if len(state) == 1:
        return ((state[0], Fraction(1)),)
    successors = block_shave_successors(state)
    out = defaultdict(Fraction)
    for target in successors:
        for survivor, mass in shave_terminal_law(target):
            out[survivor] += mass / len(successors)
    return tuple(sorted(out.items()))


def shave_pgf_product(n, z):
    if n == 1:
        return Fraction(1)
    value = Fraction(2 * z, shave_denominator(n))
    for r in range(2, n):
        value *= 1 + Fraction(z * (r + 1), shave_denominator(r))
    return value


def shave_endpoint_product(n):
    if n == 1:
        return Fraction(1)
    value = Fraction(1, shave_denominator(n))
    for r in range(2, n):
        value *= 1 + Fraction(r, shave_denominator(r))
    return value


def audit_pbl(audit):
    start = audit.assertions
    for n in range(2, 10):
        successors = block_shave_successors(tuple(range(n)))
        audit.equal(len(successors), shave_denominator(n), f"PBL choices n={n}")
        census = Counter(map(len, successors))
        for q in range(1, n):
            audit.equal(census[q], q + 1, f"PBL size multiplicity n={n},q={q}")
        law = dict(shave_clock_law(n))
        audit.equal(sum(law.values(), Fraction(0)), 1, f"PBL clock mass n={n}")
        for z in (Fraction(-1, 2), Fraction(1, 3), Fraction(2, 3)):
            direct = sum((mass * z**t for t, mass in law.items()), Fraction(0))
            audit.equal(direct, shave_pgf_product(n, z), f"PBL PGF n={n},z={z}")
        terminal = dict(shave_terminal_law(tuple(range(n))))
        audit.equal(sum(terminal.values(), Fraction(0)), 1, f"PBL terminal mass n={n}")
        audit.equal(terminal[0], shave_endpoint_product(n), f"PBL endpoint n={n}")
        audit.equal(terminal[0], terminal[n - 1], f"PBL reversal n={n}")
    n = 7
    law = dict(shave_clock_law(n))
    mean = sum((t * p for t, p in law.items()), Fraction(0))
    edge = dict(shave_terminal_law(tuple(range(n))))[0]
    audit.lane(
        "PBL",
        "rooted-polygon block shave",
        start,
        f"interior={n},clock_mean={mean},edge_survival={edge}",
        "KILL_GENERIC_DELETION_P146",
    )


# ---------------------------------------------------------------------------
# Shared convex-polygon triangulation utilities


@lru_cache(maxsize=None)
def interval_triangulations(left, right):
    if right - left < 2:
        return (frozenset(),)
    out = set()
    for middle in range(left + 1, right):
        for first in interval_triangulations(left, middle):
            for second in interval_triangulations(middle, right):
                diagonals = set(first) | set(second)
                if middle - left > 1:
                    diagonals.add((left, middle))
                if right - middle > 1:
                    diagonals.add((middle, right))
                out.add(frozenset(diagonals))
    return tuple(sorted(out, key=lambda value: tuple(sorted(value))))


def triangulations(n):
    return interval_triangulations(0, n - 1)


def polygon_edge(n, edge):
    u, v = sorted(edge)
    return v == u + 1 or (u, v) == (0, n - 1)


def triangulation_triangles(n, diagonal_set):
    edges = set(diagonal_set)
    edges.update((i, i + 1) for i in range(n - 1))
    edges.add((0, n - 1))
    return tuple(
        triple
        for triple in combinations(range(n), 3)
        if all(tuple(sorted(edge)) in edges for edge in combinations(triple, 2))
    )


def flip_diagonal(n, diagonal_set, edge):
    edge = tuple(sorted(edge))
    incident = [triangle for triangle in triangulation_triangles(n, diagonal_set) if set(edge) <= set(triangle)]
    if len(incident) != 2:
        raise AssertionError((n, diagonal_set, edge, incident))
    opposite = tuple(sorted((set(incident[0]) | set(incident[1])) - set(edge)))
    updated = set(diagonal_set)
    updated.remove(edge)
    updated.add(opposite)
    return frozenset(updated), opposite


# 2. RTF: root-directed fan flips


def root_flip_successors(n, diagonal_set):
    out = []
    for edge in sorted(diagonal_set):
        if 0 in edge:
            continue
        target, new_edge = flip_diagonal(n, diagonal_set, edge)
        if 0 in new_edge:
            out.append(target)
    return tuple(out)


@lru_cache(maxsize=None)
def root_flip_histories(n, diagonal_set):
    successors = root_flip_successors(n, diagonal_set)
    if not successors:
        return 1
    return sum(root_flip_histories(n, target) for target in successors)


def audit_rtf(audit):
    start = audit.assertions
    max_histories = 0
    depth_census = None
    for n in range(4, 9):
        states = triangulations(n)
        audit.equal(len(states), comb(2 * (n - 2), n - 2) // (n - 1), f"RTF Catalan n={n}")
        fan = frozenset((0, j) for j in range(2, n - 1))
        census = Counter()
        for state in states:
            root_degree = sum(0 in edge for edge in state)
            depth = n - 3 - root_degree
            census[depth] += 1
            successors = root_flip_successors(n, state)
            audit.equal(bool(successors), state != fan, f"RTF active iff nonfan n={n}")
            for target in successors:
                audit.equal(
                    sum(0 in edge for edge in target), root_degree + 1, f"RTF degree n={n}"
                )
            histories = root_flip_histories(n, state)
            audit.true(histories >= 1, f"RTF histories n={n}")
            max_histories = max(max_histories, histories)
        depth_census = census
    audit.lane(
        "RTF",
        "root-directed triangulation flip",
        start,
        f"n=8,depth_census={dict(sorted(depth_census.items()))},max_histories={max_histories}",
        "KILL_TREE_HOOK_P146",
    )


# 3. LDL: exact Lawson/Delaunay legalization on one generic convex hexagon


def determinant(matrix):
    n = len(matrix)
    total = 0
    for order in permutations(range(n)):
        inversions = sum(order[i] > order[j] for i in range(n) for j in range(i + 1, n))
        term = 1
        for row in range(n):
            term *= matrix[row][order[row]]
        total += (-1) ** inversions * term
    return total


def incircle_det(points):
    return determinant([[x, y, x * x + y * y, 1] for x, y in points])


def delaunay_preferred_diagonal(points, quad):
    q = tuple(sorted(quad))
    value = incircle_det([points[index] for index in q])
    if value == 0:
        raise AssertionError(f"cocircular quadruple {q}")
    return (q[1], q[3]) if value > 0 else (q[0], q[2])


def lawson_successors(points, diagonal_set):
    n = len(points)
    out = []
    for edge in sorted(diagonal_set):
        incident = [triangle for triangle in triangulation_triangles(n, diagonal_set) if set(edge) <= set(triangle)]
        quad = set(incident[0]) | set(incident[1])
        preferred = tuple(sorted(delaunay_preferred_diagonal(points, quad)))
        if tuple(sorted(edge)) != preferred:
            target, other = flip_diagonal(n, diagonal_set, edge)
            if tuple(sorted(other)) != preferred:
                raise AssertionError((edge, preferred, other))
            out.append(target)
    return tuple(out)


def lawson_clock(points, state, visiting=None):
    if visiting is None:
        visiting = set()
    if state in visiting:
        raise AssertionError("Lawson cycle")
    successors = lawson_successors(points, state)
    if not successors:
        return ((0, Fraction(1)),)
    visiting.add(state)
    out = defaultdict(Fraction)
    for target in successors:
        for t, mass in lawson_clock(points, target, visiting):
            out[t + 1] += mass / len(successors)
    visiting.remove(state)
    return tuple(sorted(out.items()))


def audit_ldl(audit):
    start = audit.assertions
    points = tuple((x, x * x) for x in range(6))
    states = triangulations(6)
    sinks = []
    means = []
    for state in states:
        successors = lawson_successors(points, state)
        for target in successors:
            audit.true(target in states, "LDL target triangulation")
        law = dict(lawson_clock(points, state))
        audit.equal(sum(law.values(), Fraction(0)), 1, "LDL clock mass")
        means.append(sum((t * mass for t, mass in law.items()), Fraction(0)))
        if not successors:
            sinks.append(state)
    audit.equal(len(sinks), 1, "LDL unique Delaunay sink")
    audit.lane(
        "LDL",
        "Lawson Delaunay legalization",
        start,
        f"hexagon_states={len(states)},unique_sink=1,max_mean={max(means)}",
        "KILL_DIRECT_LAWSON",
    )


# 4. DPF: domino plaquette-flip walk on a 2 by n rectangle


def domino_states(n):
    out = []

    def visit(column, starts):
        if column == n:
            out.append(frozenset(starts))
            return
        visit(column + 1, starts)
        if column + 1 < n:
            starts.add(column)
            visit(column + 2, starts)
            starts.remove(column)

    visit(0, set())
    return tuple(sorted(set(out), key=lambda state: tuple(sorted(state))))


def domino_vertical(state, column):
    return column not in state and column - 1 not in state


def domino_flip(state, slot):
    state = set(state)
    if slot in state:
        state.remove(slot)
    elif domino_vertical(state, slot) and domino_vertical(state, slot + 1):
        state.add(slot)
    return frozenset(state)


def audit_dpf(audit):
    start = audit.assertions
    states = domino_states(9)
    audit.equal(len(states), 55, "DPF Fibonacci count")
    state_set = set(states)
    rows = {}
    for state in states:
        counts = Counter(domino_flip(state, slot) for slot in range(8))
        audit.true(set(counts) <= state_set, "DPF closure")
        audit.equal(sum(counts.values()), 8, "DPF row mass")
        rows[state] = counts
    for source in states:
        for target in states:
            audit.equal(rows[source][target], rows[target][source], "DPF symmetry")
    seen = {states[0]}
    queue = deque(seen)
    while queue:
        source = queue.popleft()
        for target in rows[source]:
            if target not in seen:
                seen.add(target)
                queue.append(target)
    audit.equal(seen, state_set, "DPF connected")
    active = [sum(target != state for target in (domino_flip(state, s) for s in range(8))) for state in states]
    audit.lane(
        "DPF",
        "domino plaquette-flip walk",
        start,
        f"2x9_states={len(states)},active_range={min(active)}..{max(active)}",
        "KILL_DIRECT_TILING_GLAUBER",
    )


# 5. KCI: Kempe-component interchange on cycle colourings


def proper_cycle_colouring(state):
    return all(state[i] != state[(i + 1) % len(state)] for i in range(len(state)))


def kempe_swap(state, first, second, vertex):
    state = tuple(state)
    if state[vertex] not in (first, second):
        return state
    allowed = {first, second}
    component = {vertex}
    queue = deque([vertex])
    while queue:
        current = queue.popleft()
        for neighbour in ((current - 1) % len(state), (current + 1) % len(state)):
            if neighbour not in component and state[neighbour] in allowed:
                component.add(neighbour)
                queue.append(neighbour)
    out = list(state)
    for index in component:
        out[index] = second if state[index] == first else first
    return tuple(out)


def audit_kci(audit):
    start = audit.assertions
    n, q = 6, 3
    states = tuple(state for state in product(range(q), repeat=n) if proper_cycle_colouring(state))
    audit.equal(len(states), (q - 1) ** n + (q - 1), "KCI chromatic count")
    slots = tuple((a, b, v) for a, b in combinations(range(q), 2) for v in range(n))
    rows = {}
    state_set = set(states)
    for state in states:
        counts = Counter(kempe_swap(state, a, b, v) for a, b, v in slots)
        audit.true(set(counts) <= state_set, "KCI proper closure")
        audit.equal(sum(counts.values()), len(slots), "KCI row")
        rows[state] = counts
    for source in states:
        for target, multiplicity in rows[source].items():
            audit.equal(multiplicity, rows[target][source], "KCI detailed symmetry")
    unseen = set(states)
    orbit_sizes = []
    while unseen:
        seed = min(unseen)
        seen = {seed}
        queue = deque([seed])
        while queue:
            source = queue.popleft()
            for target in rows[source]:
                if target not in seen:
                    seen.add(target)
                    queue.append(target)
        unseen -= seen
        orbit_sizes.append(len(seen))
    audit.lane(
        "KCI",
        "Kempe-component interchange",
        start,
        f"C6_3colourings={len(states)},orbit_sizes={sorted(orbit_sizes)}",
        "KILL_DIRECT_WSK_KEMPE",
    )


# 6. LCW: local-complementation graph walk


def all_graphs(n):
    edges = tuple(combinations(range(n), 2))
    return tuple(frozenset(edge for bit, edge in zip(mask, edges) if bit) for mask in product((0, 1), repeat=len(edges)))


def local_complement(graph, n, vertex):
    graph = set(graph)
    neighbours = [u for u in range(n) if tuple(sorted((u, vertex))) in graph]
    for edge in combinations(neighbours, 2):
        edge = tuple(sorted(edge))
        if edge in graph:
            graph.remove(edge)
        else:
            graph.add(edge)
    return frozenset(graph)


def orbit_census(states, moves):
    unseen = set(states)
    sizes = []
    while unseen:
        seed = min(unseen, key=lambda state: tuple(sorted(state)) if isinstance(state, frozenset) else state)
        seen = {seed}
        queue = deque([seed])
        while queue:
            source = queue.popleft()
            for target in moves(source):
                if target not in seen:
                    seen.add(target)
                    queue.append(target)
        unseen -= seen
        sizes.append(len(seen))
    return sorted(sizes)


def audit_lcw(audit):
    start = audit.assertions
    n = 5
    states = all_graphs(n)
    state_set = set(states)
    for graph in states:
        for vertex in range(n):
            target = local_complement(graph, n, vertex)
            audit.true(target in state_set, "LCW closure")
            audit.equal(local_complement(target, n, vertex), graph, "LCW involution")
    sizes = orbit_census(states, lambda graph: (local_complement(graph, n, v) for v in range(n)))
    audit.equal(sum(sizes), len(states), "LCW orbit partition")
    audit.lane(
        "LCW",
        "labelled-graph local-complement walk",
        start,
        f"n=5,graphs={len(states)},orbits={len(sizes)},largest={max(sizes)}",
        "KILL_LOCAL_COMPLEMENT_P117_P145",
    )


# 7. TSW: binary-table 2 by 2 switch chain


def binary_table_states(n, row_sum):
    row_options = tuple(bits for bits in product((0, 1), repeat=n) if sum(bits) == row_sum)
    return tuple(
        tuple(value for row in rows for value in row)
        for rows in product(row_options, repeat=n)
        if all(sum(rows[r][c] for r in range(n)) == row_sum for c in range(n))
    )


def table_switch(state, n, r1, r2, c1, c2):
    state = list(state)
    indices = (r1 * n + c1, r1 * n + c2, r2 * n + c1, r2 * n + c2)
    pattern = tuple(state[index] for index in indices)
    if pattern in ((1, 0, 0, 1), (0, 1, 1, 0)):
        for index in indices:
            state[index] ^= 1
    return tuple(state)


def audit_tsw(audit):
    start = audit.assertions
    n = 4
    states = binary_table_states(n, 2)
    audit.equal(len(states), 90, "TSW table count")
    state_set = set(states)
    slots = tuple((*rows, *cols) for rows in combinations(range(n), 2) for cols in combinations(range(n), 2))
    rows = {}
    active = []
    for state in states:
        counts = Counter(table_switch(state, n, *slot) for slot in slots)
        audit.true(set(counts) <= state_set, "TSW margins")
        audit.equal(sum(counts.values()), len(slots), "TSW row")
        rows[state] = counts
        active.append(sum(table_switch(state, n, *slot) != state for slot in slots))
    for source in states:
        for target, multiplicity in rows[source].items():
            audit.equal(multiplicity, rows[target][source], "TSW symmetry")
    sizes = orbit_census(states, lambda state: (table_switch(state, n, *slot) for slot in slots))
    audit.equal(sizes, [90], "TSW connected pilot")
    audit.lane(
        "TSW",
        "binary contingency-table switches",
        start,
        f"4x4_2regular_states={len(states)},active_range={min(active)}..{max(active)}",
        "KILL_DIRECT_MARKOV_BASIS",
    )


# 8. MBE: improving graphic-matroid basis exchange


def prufer_tree(sequence, n):
    degree = [1] * n
    for value in sequence:
        degree[value] += 1
    edges = []
    for value in sequence:
        leaf = min(index for index, current in enumerate(degree) if current == 1)
        edges.append(tuple(sorted((leaf, value))))
        degree[leaf] -= 1
        degree[value] -= 1
    last = [index for index, current in enumerate(degree) if current == 1]
    edges.append(tuple(sorted(last)))
    return frozenset(edges)


def tree_path_edges(tree, start, end):
    adjacency = defaultdict(list)
    for u, v in tree:
        adjacency[u].append(v)
        adjacency[v].append(u)
    parent = {start: None}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == end:
            break
        for neighbour in adjacency[current]:
            if neighbour not in parent:
                parent[neighbour] = current
                queue.append(neighbour)
    out = []
    current = end
    while parent[current] is not None:
        out.append(tuple(sorted((current, parent[current]))))
        current = parent[current]
    return tuple(out)


def exchange_successors(tree, n, weights):
    complete = set(combinations(range(n), 2))
    out = []
    for added in sorted(complete - set(tree)):
        for removed in tree_path_edges(tree, *added):
            if weights[removed] > weights[added]:
                out.append(frozenset((set(tree) | {added}) - {removed}))
    return tuple(out)


def tree_clock_law(tree, n, weights, memo):
    if tree in memo:
        return memo[tree]
    successors = exchange_successors(tree, n, weights)
    if not successors:
        memo[tree] = ((0, Fraction(1)),)
        return memo[tree]
    out = defaultdict(Fraction)
    for target in successors:
        for t, mass in tree_clock_law(target, n, weights, memo):
            out[t + 1] += mass / len(successors)
    memo[tree] = tuple(sorted(out.items()))
    return memo[tree]


def audit_mbe(audit):
    start = audit.assertions
    n = 5
    trees = tuple(sorted({prufer_tree(sequence, n) for sequence in product(range(n), repeat=n - 2)}, key=lambda t: tuple(sorted(t))))
    audit.equal(len(trees), n ** (n - 2), "MBE Cayley count")
    all_edges = tuple(combinations(range(n), 2))
    weights = {edge: 1 << index for index, edge in enumerate(all_edges)}
    tree_set = set(trees)
    memo = {}
    terminals = set()
    means = []
    supports = []
    for tree in trees:
        current_weight = sum(weights[edge] for edge in tree)
        successors = exchange_successors(tree, n, weights)
        for target in successors:
            audit.true(target in tree_set, "MBE tree closure")
            audit.true(sum(weights[e] for e in target) < current_weight, "MBE strict weight")
        if not successors:
            terminals.add(tree)
        law = dict(tree_clock_law(tree, n, weights, memo))
        audit.equal(sum(law.values(), Fraction(0)), 1, "MBE clock mass")
        means.append(sum((t * mass for t, mass in law.items()), Fraction(0)))
        supports.append(len(law))
    audit.equal(len(terminals), 1, "MBE unique MST")
    audit.lane(
        "MBE",
        "improving graphic-basis exchange",
        start,
        f"K5_trees={len(trees)},max_clock_support={max(supports)},max_mean={max(means)}",
        "KILL_HISTORICAL_MATROID_BASIS",
    )


# 9. BCD: type-B simple-descent walk


def type_b_length(word):
    inversions = sum(word[i] > word[j] for i in range(len(word)) for j in range(i + 1, len(word)))
    negatives = sum(value < 0 for value in word)
    negative_sums = sum(word[i] + word[j] < 0 for i in range(len(word)) for j in range(i + 1, len(word)))
    return inversions + negatives + negative_sums


def type_b_reflect(word, generator):
    word = list(word)
    if generator == 0:
        word[0] = -word[0]
    else:
        word[generator - 1], word[generator] = word[generator], word[generator - 1]
    return tuple(word)


@lru_cache(maxsize=None)
def type_b_histories(word):
    length = type_b_length(word)
    if length == 0:
        return 1
    return sum(
        type_b_histories(type_b_reflect(word, generator))
        for generator in range(len(word))
        if type_b_length(type_b_reflect(word, generator)) == length - 1
    )


def audit_bcd(audit):
    start = audit.assertions
    n = 4
    states = []
    for order in permutations(range(1, n + 1)):
        for signs in product((-1, 1), repeat=n):
            states.append(tuple(sign * value for sign, value in zip(signs, order)))
    audit.equal(len(states), (2**n) * 24, "BCD group order")
    for state in states:
        length = type_b_length(state)
        descents = [g for g in range(n) if type_b_length(type_b_reflect(state, g)) == length - 1]
        audit.equal(bool(descents), length > 0, "BCD descent iff nonidentity")
        audit.true(type_b_histories(state) >= 1, "BCD histories positive")
    longest = tuple(-i for i in range(1, n + 1))
    audit.equal(type_b_length(longest), n * n, "BCD longest length")
    audit.lane(
        "BCD",
        "type-B Coxeter descent",
        start,
        f"B4_states={len(states)},longest_clock={n*n},longest_histories={type_b_histories(longest)}",
        "KILL_DIRECT_COXETER_DESCENT",
    )


# 10. VMD: positive Markov-triple Vieta descent


def markov_mutations(triple):
    triple = tuple(triple)
    out = set()
    for index in range(3):
        others = [triple[j] for j in range(3) if j != index]
        value = 3 * others[0] * others[1] - triple[index]
        if value > 0:
            out.add(tuple(sorted((*others, value))))
    out.discard(tuple(sorted(triple)))
    return tuple(sorted(out))


def audit_vmd(audit):
    start = audit.assertions
    root = (1, 1, 1)
    depth = {root: 0}
    frontier = [root]
    level_counts = [1]
    for level in range(1, 9):
        new = set()
        for state in frontier:
            for target in markov_mutations(state):
                if target not in depth:
                    depth[target] = level
                    new.add(target)
        frontier = sorted(new)
        level_counts.append(len(frontier))
    children = Counter()
    for state, level in depth.items():
        audit.equal(sum(value * value for value in state), 3 * state[0] * state[1] * state[2], "VMD equation")
        lower = [target for target in markov_mutations(state) if sum(target) < sum(state)]
        if state == root:
            audit.equal(lower, [], "VMD root")
        else:
            audit.equal(len(lower), 1, f"VMD unique parent {state}")
            audit.equal(depth[lower[0]], level - 1, "VMD depth parent")
        children[state] = sum(depth.get(target) == level + 1 for target in markov_mutations(state))
    audit.lane(
        "VMD",
        "Markov-triple Vieta descent",
        start,
        f"levels0..8={level_counts},max_children={max(children.values())}",
        "KILL_DIRECT_MARKOFF_TREE",
    )


# 11. ACD: integral Descartes-quadruple reduction


def descartes_reflections(quadruple):
    quadruple = tuple(quadruple)
    out = set()
    for index in range(4):
        others = [quadruple[j] for j in range(4) if j != index]
        value = 2 * sum(others) - quadruple[index]
        target = tuple(sorted((*others, value)))
        if target != tuple(sorted(quadruple)):
            out.add(target)
    return tuple(sorted(out))


def descartes_valid(quadruple):
    return 2 * sum(value * value for value in quadruple) == sum(quadruple) ** 2


def audit_acd(audit):
    start = audit.assertions
    root = (-1, 2, 2, 3)
    depth = {root: 0}
    frontier = [root]
    level_counts = [1]
    for level in range(1, 7):
        new = set()
        for state in frontier:
            for target in descartes_reflections(state):
                if target not in depth:
                    depth[target] = level
                    new.add(target)
        frontier = sorted(new)
        level_counts.append(len(frontier))
    for state, level in depth.items():
        audit.true(descartes_valid(state), "ACD Descartes equation")
        lower = [target for target in descartes_reflections(state) if sum(target) < sum(state)]
        if state == root:
            audit.equal(lower, [], "ACD root reduced")
        else:
            audit.equal(len(lower), 1, f"ACD unique lower neighbour {state}")
            audit.equal(depth[lower[0]], level - 1, "ACD parent depth")
    audit.lane(
        "ACD",
        "Apollonian Descartes reduction",
        start,
        f"levels0..6={level_counts},states={len(depth)}",
        "KILL_DIRECT_APOLLONIAN_GROUP",
    )


# 12. FCR: random adjacent free cancellation


INVERSE = {0: 1, 1: 0, 2: 3, 3: 2}


def free_reduce(word):
    stack = []
    for letter in word:
        if stack and INVERSE[letter] == stack[-1]:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def cancellation_successors(word):
    return tuple(
        word[:index] + word[index + 2 :]
        for index in range(len(word) - 1)
        if INVERSE[word[index]] == word[index + 1]
    )


@lru_cache(maxsize=None)
def cancellation_histories(word):
    successors = cancellation_successors(word)
    if not successors:
        return 1
    return sum(cancellation_histories(target) for target in successors)


def audit_fcr(audit):
    start = audit.assertions
    endpoint_lengths = Counter()
    max_histories = 0
    for n in range(0, 9):
        for word in product(range(4), repeat=n):
            reduced = free_reduce(word)
            current = word
            # Every branch has the same normal form and deterministic number of deletions.
            queue = [current]
            seen = set()
            while queue:
                state = queue.pop()
                if state in seen:
                    continue
                seen.add(state)
                successors = cancellation_successors(state)
                if not successors:
                    audit.equal(state, reduced, "FCR confluence")
                    audit.equal((n - len(state)) // 2, (n - len(reduced)) // 2, "FCR clock")
                else:
                    queue.extend(successors)
            if n == 8:
                endpoint_lengths[len(reduced)] += 1
            max_histories = max(max_histories, cancellation_histories(word))
    audit.lane(
        "FCR",
        "free-word adjacent cancellation",
        start,
        f"length8_endpoint_census={dict(sorted(endpoint_lengths.items()))},max_histories={max_histories}",
        "KILL_FREE_NORMAL_FORM_DELETION",
    )


# 13. PCR: active-conflict recolouring on a cycle


def colouring_repair_row(state, q):
    n = len(state)
    conflicts = [i for i in range(n) if state[i] == state[(i + 1) % n]]
    if not conflicts:
        return {state: Fraction(1)}
    out = defaultdict(Fraction)
    denominator = len(conflicts) * 2 * (q - 1)
    for edge in conflicts:
        for vertex in (edge, (edge + 1) % n):
            for colour in range(q):
                if colour == state[vertex]:
                    continue
                target = list(state)
                target[vertex] = colour
                out[tuple(target)] += Fraction(1, denominator)
    return dict(out)


def audit_pcr(audit):
    start = audit.assertions
    n, q = 5, 3
    states = tuple(product(range(q), repeat=n))
    for state in states:
        row = colouring_repair_row(state, q)
        audit.equal(sum(row.values(), Fraction(0)), 1, "PCR row mass")
        for target in row:
            audit.equal(len(target), n, "PCR carrier")
    law = {tuple([0] * n): Fraction(1)}
    absorption = []
    for _ in range(8):
        next_law = defaultdict(Fraction)
        for state, mass in law.items():
            for target, probability in colouring_repair_row(state, q).items():
                next_law[target] += mass * probability
        law = dict(next_law)
        audit.equal(sum(law.values(), Fraction(0)), 1, "PCR layer mass")
        absorption.append(sum(mass for state, mass in law.items() if proper_cycle_colouring(state)))
    audit.true(all(x <= y for x, y in zip(absorption, absorption[1:])), "PCR absorption monotone")
    audit.lane(
        "PCR",
        "active-conflict cycle recolouring",
        start,
        f"C5_q3_absorption_t1..8={[str(x) for x in absorption]}",
        "KILL_OWNER_CROWDED_WEAK_CLOCK",
    )


# 14. ZIG: zero-temperature Ising singleton flips on a cycle


def ising_energy(state):
    return sum(state[i] != state[(i + 1) % len(state)] for i in range(len(state)))


def ising_successors(state):
    n = len(state)
    out = []
    for i in range(n):
        left, right = state[(i - 1) % n], state[(i + 1) % n]
        if left == right and state[i] != left:
            target = list(state)
            target[i] = left
            out.append(tuple(target))
    return tuple(out)


@lru_cache(maxsize=None)
def ising_terminal_clock(state):
    successors = ising_successors(state)
    if not successors:
        return {(state, 0): Fraction(1)}
    out = defaultdict(Fraction)
    for target in successors:
        for (terminal, t), mass in ising_terminal_clock(target).items():
            out[(terminal, t + 1)] += mass / len(successors)
    return dict(out)


def audit_zig(audit):
    start = audit.assertions
    absorbing_census = {}
    for n in range(3, 11):
        absorbing = 0
        for state in product((0, 1), repeat=n):
            successors = ising_successors(state)
            for target in successors:
                audit.equal(ising_energy(target), ising_energy(state) - 2, "ZIG energy drop")
            law = ising_terminal_clock(state)
            audit.equal(sum(law.values(), Fraction(0)), 1, "ZIG terminal mass")
            if not successors:
                absorbing += 1
        absorbing_census[n] = absorbing
    seed = tuple(i % 2 for i in range(10))
    law = ising_terminal_clock(seed)
    clock = Counter()
    walls = Counter()
    for (terminal, t), mass in law.items():
        clock[t] += mass
        walls[ising_energy(terminal)] += mass
    audit.lane(
        "ZIG",
        "zero-temperature Ising singleton flip",
        start,
        f"absorbing_counts={absorbing_census},alt10_clock={dict(sorted(clock.items()))},walls={dict(sorted(walls.items()))}",
        "KILL_PRIOR_R06_GLAUBER_MECHANISM",
    )


# 15. MTG: monotone-triangle single-site heat bath


def interlacing_rows(lower):
    length = len(lower) - 1
    out = []

    def visit(index, current):
        if index == length:
            out.append(tuple(current))
            return
        low, high = lower[index], lower[index + 1]
        if current:
            low = max(low, current[-1] + 1)
        for value in range(low, high + 1):
            current.append(value)
            visit(index + 1, current)
            current.pop()

    visit(0, [])
    return tuple(out)


def monotone_triangles(n):
    bottom = tuple(range(1, n + 1))
    out = []

    def visit(rows_bottom_up):
        lower = rows_bottom_up[-1]
        if len(lower) == 1:
            out.append(tuple(reversed(rows_bottom_up)))
            return
        for upper in interlacing_rows(lower):
            visit(rows_bottom_up + [upper])

    visit([bottom])
    return tuple(sorted(out))


def monotone_allowed(triangle, row, column):
    current_row = triangle[row]
    low = triangle[row + 1][column]
    high = triangle[row + 1][column + 1]
    if column > 0:
        low = max(low, current_row[column - 1] + 1)
    if column + 1 < len(current_row):
        high = min(high, current_row[column + 1] - 1)
    if row > 0:
        upper = triangle[row - 1]
        if column > 0:
            low = max(low, upper[column - 1])
        if column < len(upper):
            high = min(high, upper[column])
    return tuple(range(low, high + 1))


def monotone_heatbath_row(triangle):
    sites = tuple((row, column) for row in range(len(triangle) - 1) for column in range(len(triangle[row])))
    out = defaultdict(Fraction)
    for row, column in sites:
        allowed = monotone_allowed(triangle, row, column)
        for value in allowed:
            rows = [list(current) for current in triangle]
            rows[row][column] = value
            target = tuple(tuple(current) for current in rows)
            out[target] += Fraction(1, len(sites) * len(allowed))
    return dict(out)


def audit_mtg(audit):
    start = audit.assertions
    states = monotone_triangles(4)
    audit.equal(len(states), 42, "MTG ASM count")
    state_set = set(states)
    rows = {}
    for state in states:
        row = monotone_heatbath_row(state)
        audit.equal(sum(row.values(), Fraction(0)), 1, "MTG row mass")
        audit.true(set(row) <= state_set, "MTG closure")
        rows[state] = row
    for source in states:
        for target in states:
            audit.equal(rows[source].get(target, 0), rows[target].get(source, 0), "MTG symmetry")
    sizes = orbit_census(states, lambda state: rows[state])
    audit.equal(sizes, [42], "MTG connected")
    holds = [rows[state].get(state, Fraction(0)) for state in states]
    audit.lane(
        "MTG",
        "monotone-triangle heat bath",
        start,
        f"order4_states={len(states)},hold_range={min(holds)}..{max(holds)}",
        "KILL_GENERIC_HEATBATH_STATIC_ASM",
    )


# 16. BKM: deterministic Lloyd--medoid map on a finite path


def path_medoid_update(centres, n):
    first, second = centres
    clusters = [[], []]
    for vertex in range(n):
        d0, d1 = abs(vertex - first), abs(vertex - second)
        clusters[0 if d0 <= d1 else 1].append(vertex)
    updated = tuple(cluster[(len(cluster) - 1) // 2] for cluster in clusters)
    if not updated[0] < updated[1]:
        raise AssertionError((centres, clusters, updated))
    return updated


def deterministic_orbit(start, update):
    seen = {}
    orbit = []
    current = start
    while current not in seen:
        seen[current] = len(orbit)
        orbit.append(current)
        current = update(current)
    return tuple(orbit), seen[current], current


def audit_bkm(audit):
    start = audit.assertions
    n = 16
    states = tuple(combinations(range(n), 2))
    fixed = Counter()
    max_depth = 0
    for state in states:
        orbit, cycle_start, repeated = deterministic_orbit(state, lambda value: path_medoid_update(value, n))
        cycle_length = len(orbit) - cycle_start
        audit.equal(cycle_length, 1, "BKM fixed convergence")
        endpoint = repeated
        audit.equal(path_medoid_update(endpoint, n), endpoint, "BKM endpoint fixed")
        fixed[endpoint] += 1
        max_depth = max(max_depth, cycle_start)
    audit.equal(sum(fixed.values()), len(states), "BKM basin partition")
    audit.lane(
        "BKM",
        "finite-path Lloyd medoid map",
        start,
        f"P16_states={len(states)},fixed={len(fixed)},max_depth={max_depth},largest_basin={max(fixed.values())}",
        "KILL_CLASSICAL_K_MEDIANS_THIN",
    )


def main():
    print("P157-P161 REPLACEMENT PROBABILISTIC/GEOMETRIC EXACT SCOUT")
    print("arithmetic=integers+fractions.Fraction; randomness=none; dependencies=stdlib-only")
    audit = Audit()
    audit_pbl(audit)
    audit_rtf(audit)
    audit_ldl(audit)
    audit_dpf(audit)
    audit_kci(audit)
    audit_lcw(audit)
    audit_tsw(audit)
    audit_mbe(audit)
    audit_bcd(audit)
    audit_vmd(audit)
    audit_acd(audit)
    audit_fcr(audit)
    audit_pcr(audit)
    audit_zig(audit)
    audit_mtg(audit)
    audit_bkm(audit)
    print(f"TOTAL PASS systems=16 assertions={audit.assertions}")
    print("FOCUSED_SURVIVORS none")
    print("EVIDENCE_BOUNDARY finite exhaustive pilots are falsification pressure, not proof or novelty")
    print("EXTERNAL_STATUS HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
