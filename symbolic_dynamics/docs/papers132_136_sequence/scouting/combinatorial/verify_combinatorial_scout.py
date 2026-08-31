#!/usr/bin/env python3
"""Exact breadth pilot for the P132--P136 combinatorial/geometric lane.

The program enumerates each advertised finite phase space, constructs the
literal map, verifies closure, and scans the complete functional graph.  It
also subjects the three strongest early signals to independent formula
checks.  Nothing here is a novelty certificate or a paper allocation.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, permutations, product
from math import ceil, comb, factorial, log2


class Checks:
    def __init__(self) -> None:
        self.n = 0

    def that(self, condition: bool, payload=None) -> None:
        self.n += 1
        if not condition:
            raise AssertionError(payload)


CHECKS = Checks()


@dataclass(frozen=True)
class AuditRow:
    ident: str
    parameters: int
    states: int
    periods: tuple[int, ...]
    max_tail: int
    last_image: int
    last_fixed: int
    assertions: int


def audit_family(ident, instances):
    """Run an exact functional-graph census over parameter instances."""
    before = CHECKS.n
    all_periods = set()
    max_tail = 0
    state_total = 0
    last_image = last_fixed = 0
    parameter_count = 0
    for label, raw_states, phi in instances:
        parameter_count += 1
        states = tuple(raw_states)
        universe = set(states)
        CHECKS.that(bool(states), (ident, label, "empty phase space"))
        CHECKS.that(len(states) == len(universe), (ident, label, "duplicates"))
        state_total += len(states)
        nxt = {}
        for state in states:
            image = phi(state)
            CHECKS.that(image in universe, (ident, label, state, image, "closure"))
            nxt[state] = image
        CHECKS.that(len(nxt) == len(states), (ident, label, "map coverage"))

        image_set = set(nxt.values())
        fixed = {state for state in states if nxt[state] == state}
        last_image, last_fixed = len(image_set), len(fixed)
        CHECKS.that(fixed <= image_set, (ident, label, "fixed not image"))

        for start in states:
            seen = {}
            cur = start
            step = 0
            while cur not in seen:
                seen[cur] = step
                cur = nxt[cur]
                step += 1
            tail = seen[cur]
            period = step - tail
            CHECKS.that(period >= 1, (ident, label, start, period))
            cycle_state = cur
            for _ in range(period):
                cycle_state = nxt[cycle_state]
            CHECKS.that(cycle_state == cur, (ident, label, start, tail, period))
            CHECKS.that(tail <= len(states), (ident, label, start, tail))
            all_periods.add(period)
            max_tail = max(max_tail, tail)

    row = AuditRow(
        ident,
        parameter_count,
        state_total,
        tuple(sorted(all_periods)),
        max_tail,
        last_image,
        last_fixed,
        CHECKS.n - before,
    )
    print(
        f"{row.ident} | params={row.parameters} | states={row.states} | "
        f"periods={','.join(map(str, row.periods))} | max_tail={row.max_tail} | "
        f"last_image={row.last_image} | last_fixed={row.last_fixed} | "
        f"assertions={row.assertions}"
    )
    return row


# ---------------------------------------------------------------------------
# Permutations


def canonical_cycles(p):
    seen = set()
    cycles = []
    for seed in range(len(p)):
        if seed in seen:
            continue
        cycle = []
        cur = seed
        while cur not in seen:
            seen.add(cur)
            cycle.append(cur)
            cur = p[cur]
        pivot = cycle.index(min(cycle))
        cycle = cycle[pivot:] + cycle[:pivot]
        cycles.append(tuple(cycle))
    return tuple(sorted(cycles, key=lambda c: c[0]))


def cycles_to_permutation(cycles, n):
    out = list(range(n))
    for cycle in cycles:
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            out[a] = b
    return tuple(out)


def pair_cycles_concat(p):
    cycles = canonical_cycles(p)
    merged = []
    for i in range(0, len(cycles), 2):
        if i + 1 == len(cycles):
            merged.append(cycles[i])
        else:
            merged.append(cycles[i] + cycles[i + 1])
    return cycles_to_permutation(tuple(merged), len(p))


def interleave(left, right):
    out = []
    for i in range(max(len(left), len(right))):
        if i < len(left):
            out.append(left[i])
        if i < len(right):
            out.append(right[i])
    return tuple(out)


def pair_cycles_interleave(p):
    cycles = canonical_cycles(p)
    merged = []
    for i in range(0, len(cycles), 2):
        if i + 1 == len(cycles):
            merged.append(cycles[i])
        else:
            merged.append(interleave(cycles[i], cycles[i + 1]))
    return cycles_to_permutation(tuple(merged), len(p))


def canonicalize_cycle_tails(p):
    cycles = tuple((cycle[0],) + tuple(sorted(cycle[1:]))
                   for cycle in canonical_cycles(p))
    return cycles_to_permutation(cycles, len(p))


def rotate_one_line_to_one(p):
    pivot = p.index(0)
    return p[pivot:] + p[:pivot]


def inverse_permutation(p):
    out = [0] * len(p)
    for i, value in enumerate(p):
        out[value] = i
    return tuple(out)


def gated_inverse(p):
    inversions = sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i + 1, len(p)))
    return inverse_permutation(p) if inversions % 2 else p


def prefix_max_reversal(p):
    pivot = p.index(len(p) - 1)
    return tuple(reversed(p[:pivot + 1])) + p[pivot + 1:]


def reverse_increasing_run_list(p):
    runs = []
    start = 0
    for i in range(1, len(p)):
        if p[i - 1] > p[i]:
            runs.append(p[start:i])
            start = i
    runs.append(p[start:])
    return tuple(value for run in reversed(runs) for value in run)


def permutation_instances(phi, max_n=7):
    return [(f"n={n}", tuple(permutations(range(n))), phi)
            for n in range(1, max_n + 1)]


# ---------------------------------------------------------------------------
# Set partitions


@lru_cache(maxsize=None)
def set_partitions_rgs(n):
    if n == 0:
        return ((),)
    out = []

    def rec(prefix):
        if len(prefix) == n:
            out.append(tuple(prefix))
            return
        ceiling = 0 if not prefix else max(prefix) + 1
        for value in range(ceiling + 1):
            rec(prefix + [value])

    rec([0])
    return tuple(out)


def rgs_blocks(rgs):
    blocks = [[] for _ in range(max(rgs, default=-1) + 1)]
    for value, block in enumerate(rgs):
        blocks[block].append(value)
    return blocks


def blocks_to_rgs(blocks, n):
    nonempty = [sorted(block) for block in blocks if block]
    nonempty.sort(key=lambda block: block[0])
    out = [0] * n
    for index, block in enumerate(nonempty):
        for value in block:
            out[value] = index
    return tuple(out)


def block_batch_merge(rgs, width):
    blocks = rgs_blocks(rgs)
    merged = [sum((blocks[j] for j in range(i, min(i + width, len(blocks)))), [])
              for i in range(0, len(blocks), width)]
    return blocks_to_rgs(merged, len(rgs))


def transfer_block_extrema(rgs, direction):
    blocks = [set(block) for block in rgs_blocks(rgs)]
    old = [set(block) for block in blocks]
    if direction == "left":
        for i in range(1, len(old)):
            value = min(old[i])
            blocks[i].remove(value)
            blocks[i - 1].add(value)
    else:
        for i in range(len(old) - 1):
            value = max(old[i])
            blocks[i].remove(value)
            blocks[i + 1].add(value)
    return blocks_to_rgs(blocks, len(rgs))


def parity_pair_merge(rgs):
    blocks = rgs_blocks(rgs)
    out = []
    i = 0
    while i < len(blocks):
        if i + 1 < len(blocks) and len(blocks[i]) % 2 == len(blocks[i + 1]) % 2:
            out.append(blocks[i] + blocks[i + 1])
            i += 2
        else:
            out.append(blocks[i])
            i += 1
    return blocks_to_rgs(out, len(rgs))


def gated_partition_reflection(rgs):
    if (max(rgs) + 1) % 2 == 0:
        return rgs
    n = len(rgs)
    blocks = [[n - 1 - value for value in block] for block in rgs_blocks(rgs)]
    return blocks_to_rgs(blocks, n)


def balanced_block_split(rgs):
    out = []
    for block in rgs_blocks(rgs):
        cut = len(block) // 2
        if cut == 0:
            out.append(block)
        else:
            out.extend((block[:cut], block[cut:]))
    return blocks_to_rgs(out, len(rgs))


def partition_instances(phi, max_n=7):
    return [(f"n={n}", set_partitions_rgs(n), phi)
            for n in range(1, max_n + 1)]


# ---------------------------------------------------------------------------
# Parking functions


@lru_cache(maxsize=None)
def parking_functions(n):
    return tuple(a for a in product(range(1, n + 1), repeat=n)
                 if all(value <= i for i, value in enumerate(sorted(a), 1)))


def parking_outcome(preferences):
    n = len(preferences)
    occupied = set()
    outcome = []
    for preference in preferences:
        spot = preference
        while spot in occupied:
            spot += 1
        if spot > n:
            raise AssertionError((preferences, "not a parking function"))
        occupied.add(spot)
        outcome.append(spot)
    return tuple(outcome)


def parking_fibre_formula(outcome):
    seen = set()
    value = 1
    for spot in outcome:
        left = spot - 1
        while left in seen:
            left -= 1
        value *= spot - left
        seen.add(spot)
    return value


def parking_instances(max_n=7):
    return [(f"n={n}", parking_functions(n), parking_outcome)
            for n in range(1, max_n + 1)]


# ---------------------------------------------------------------------------
# Chord and bipartite matchings


@lru_cache(maxsize=None)
def chord_matchings(n):
    if n == 0:
        return ((),)

    def rec(points):
        if not points:
            yield ()
            return
        first = points[0]
        for j in range(1, len(points)):
            partner = points[j]
            rest = points[1:j] + points[j + 1:]
            for tail in rec(rest):
                yield tuple(sorted(((first, partner),) + tail))

    return tuple(rec(tuple(range(2 * n))))


def chords_cross(left, right):
    a, b = left
    c, d = right
    return (a < c < b < d) or (c < a < d < b)


def relation_components(items, relation):
    unseen = set(range(len(items)))
    components = []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        stack = [seed]
        component = []
        while stack:
            i = stack.pop()
            component.append(i)
            neighbors = [j for j in sorted(unseen) if relation(items[i], items[j])]
            for j in neighbors:
                unseen.remove(j)
                stack.append(j)
        components.append(tuple(sorted(component)))
    return tuple(components)


def rotate_crossing_component_partners(matching):
    replacement = []
    for component in relation_components(matching, chords_cross):
        chords = sorted((matching[i] for i in component), key=lambda x: x[0])
        if len(chords) == 1:
            replacement.extend(chords)
            continue
        lefts = [chord[0] for chord in chords]
        rights = [chord[1] for chord in chords]
        shifted = rights[1:] + rights[:1]
        replacement.extend(tuple(sorted((a, b))) for a, b in zip(lefts, shifted))
    return tuple(sorted(replacement))


def first_crossing_uncross(matching):
    for i in range(len(matching)):
        for j in range(i + 1, len(matching)):
            if chords_cross(matching[i], matching[j]):
                endpoints = sorted(matching[i] + matching[j])
                replacement = [(endpoints[0], endpoints[1]), (endpoints[2], endpoints[3])]
                retained = [tuple(chord) for k, chord in enumerate(matching)
                            if k not in (i, j)]
                return tuple(sorted(retained + replacement))
    return matching


def first_nesting_flatten(matching):
    for i in range(len(matching)):
        for j in range(i + 1, len(matching)):
            a, d = matching[i]
            b, c = matching[j]
            if b < a:
                a, d, b, c = b, c, a, d
            if a < b < c < d:
                replacement = [(a, b), (c, d)]
                retained = [tuple(chord) for k, chord in enumerate(matching)
                            if k not in (i, j)]
                return tuple(sorted(retained + replacement))
    return matching


def matching_instances(phi, max_n=5):
    return [(f"n={n}", chord_matchings(n), phi)
            for n in range(1, max_n + 1)]


# ---------------------------------------------------------------------------
# Simple graphs


@lru_cache(maxsize=None)
def graph_pairs(n):
    return tuple(combinations(range(n), 2))


def graph_adjacency(mask, n):
    adjacency = [set() for _ in range(n)]
    for bit, (u, v) in enumerate(graph_pairs(n)):
        if (mask >> bit) & 1:
            adjacency[u].add(v)
            adjacency[v].add(u)
    return adjacency


def graph_mask(edges, n):
    lookup = {edge: bit for bit, edge in enumerate(graph_pairs(n))}
    mask = 0
    for u, v in edges:
        if u > v:
            u, v = v, u
        mask |= 1 << lookup[(u, v)]
    return mask


def graph_distances(mask, n, source):
    adjacency = graph_adjacency(mask, n)
    distance = [-1] * n
    distance[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if distance[v] < 0:
                distance[v] = distance[u] + 1
                queue.append(v)
    return distance


def graph_power(mask, n, exponent):
    edges = []
    for u in range(n):
        distance = graph_distances(mask, n, u)
        for v in range(u + 1, n):
            if 0 < distance[v] <= exponent:
                edges.append((u, v))
    return graph_mask(edges, n)


def triangle_edge_filter(mask, n, keep):
    adjacency = graph_adjacency(mask, n)
    edges = []
    for u, v in graph_pairs(n):
        present = v in adjacency[u]
        triangular = present and bool(adjacency[u] & adjacency[v])
        if present and (triangular == keep):
            edges.append((u, v))
    return graph_mask(edges, n)


def component_sets(mask, n):
    adjacency = graph_adjacency(mask, n)
    unseen = set(range(n))
    out = []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        stack = [seed]
        component = []
        while stack:
            u = stack.pop()
            component.append(u)
            for v in sorted(adjacency[u] & unseen):
                unseen.remove(v)
                stack.append(v)
        out.append(tuple(sorted(component)))
    return tuple(out)


def bridge_delete(mask, n):
    original_components = len(component_sets(mask, n))
    retained = []
    for bit, edge in enumerate(graph_pairs(n)):
        if not ((mask >> bit) & 1):
            continue
        without = mask & ~(1 << bit)
        if len(component_sets(without, n)) == original_components:
            retained.append(edge)
    return graph_mask(retained, n)


def even_component_complement(mask, n):
    edges = set(edge for bit, edge in enumerate(graph_pairs(n)) if (mask >> bit) & 1)
    for component in component_sets(mask, n):
        if len(component) % 2 == 0:
            for edge in combinations(component, 2):
                if edge in edges:
                    edges.remove(edge)
                else:
                    edges.add(edge)
    return graph_mask(edges, n)


def add_distance_exactly_three(mask, n):
    edges = set(edge for bit, edge in enumerate(graph_pairs(n)) if (mask >> bit) & 1)
    for u in range(n):
        distance = graph_distances(mask, n, u)
        for v in range(u + 1, n):
            if distance[v] == 3:
                edges.add((u, v))
    return graph_mask(edges, n)


def graph_instances(phi_factory, max_n=6):
    out = []
    for n in range(1, max_n + 1):
        states = tuple(range(1 << len(graph_pairs(n))))
        out.append((f"n={n}", states, lambda mask, n=n: phi_factory(mask, n)))
    return out


# ---------------------------------------------------------------------------
# Labelled trees and moving roots


def prufer_tree(sequence, n):
    if n == 1:
        return 0
    degree = [1] * n
    for value in sequence:
        degree[value] += 1
    edges = []
    for value in sequence:
        leaf = min(i for i, d in enumerate(degree) if d == 1)
        edges.append((leaf, value))
        degree[leaf] -= 1
        degree[value] -= 1
    leaves = [i for i, d in enumerate(degree) if d == 1]
    edges.append(tuple(leaves))
    return graph_mask(edges, n)


@lru_cache(maxsize=None)
def labelled_trees(n):
    if n == 1:
        return (0,)
    return tuple(prufer_tree(sequence, n)
                 for sequence in product(range(n), repeat=n - 2))


def rooted_parent(mask, n, root):
    adjacency = graph_adjacency(mask, n)
    parent = [-1] * n
    parent[root] = root
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if parent[v] < 0:
                parent[v] = u
                queue.append(v)
    return tuple(parent)


def parent_jump(parent):
    return tuple(parent[parent[v]] for v in range(len(parent)))


def tree_heights(parent):
    heights = []
    for v in range(len(parent)):
        h = 0
        cur = v
        while parent[cur] != cur:
            cur = parent[cur]
            h += 1
        heights.append(h)
    return tuple(heights)


def component_size_across(mask, n, root, neighbor):
    adjacency = graph_adjacency(mask, n)
    seen = {root}
    stack = [neighbor]
    count = 0
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        count += 1
        stack.extend(adjacency[u] - seen)
    return count


def centroid_step(state, n):
    mask, root = state
    adjacency = graph_adjacency(mask, n)
    heavy = [v for v in adjacency[root]
             if component_size_across(mask, n, root, v) > n / 2]
    return (mask, heavy[0] if heavy else root)


def tree_eccentricity(mask, n, vertex):
    return max(graph_distances(mask, n, vertex))


def center_step(state, n):
    mask, root = state
    adjacency = graph_adjacency(mask, n)
    current = tree_eccentricity(mask, n, root)
    lower = [v for v in adjacency[root] if tree_eccentricity(mask, n, v) < current]
    return (mask, min(lower) if lower else root)


def parent_tree_instances(max_n=7):
    return [(f"n={n}",
             tuple(rooted_parent(mask, n, 0) for mask in labelled_trees(n)),
             parent_jump)
            for n in range(1, max_n + 1)]


def moving_root_instances(step, max_n=7):
    out = []
    for n in range(1, max_n + 1):
        states = tuple((mask, root) for mask in labelled_trees(n) for root in range(n))
        out.append((f"n={n}", states,
                    lambda state, n=n: step(state, n)))
    return out


# ---------------------------------------------------------------------------
# Ferrers diagrams, polyominoes, and lattice paths


@lru_cache(maxsize=None)
def integer_partitions(n, maximum=None):
    if n == 0:
        return ((),)
    if maximum is None or maximum > n:
        maximum = n
    out = []
    for first in range(maximum, 0, -1):
        for tail in integer_partitions(n - first, min(first, n - first)):
            out.append((first,) + tail)
    return tuple(out)


def column_pair_compress(partition):
    width = partition[0]
    columns = [sum(row > j for row in partition) for j in range(width)]
    merged = [sum(columns[i:i + 2]) for i in range(0, width, 2)]
    height = max(merged)
    return tuple(sum(column > j for column in merged) for j in range(height))


def partition_shape_instances(max_weight=25):
    return [(f"weight={n}", integer_partitions(n), column_pair_compress)
            for n in range(1, max_weight + 1)]


def grid_neighbors(cell, rows, cols):
    r, c = divmod(cell, cols)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = r + dr, c + dc
        if 0 <= rr < rows and 0 <= cc < cols:
            yield rr * cols + cc


def connected_polyomino(mask, rows, cols):
    cells = {i for i in range(rows * cols) if (mask >> i) & 1}
    if not cells:
        return False
    seen = {min(cells)}
    stack = list(seen)
    while stack:
        cell = stack.pop()
        for other in grid_neighbors(cell, rows, cols):
            if other in cells and other not in seen:
                seen.add(other)
                stack.append(other)
    return seen == cells


@lru_cache(maxsize=None)
def polyominoes(rows, cols):
    return tuple(mask for mask in range(1, 1 << (rows * cols))
                 if connected_polyomino(mask, rows, cols))


def row_hull(mask, rows, cols):
    out = mask
    for r in range(rows):
        occupied = [c for c in range(cols) if (mask >> (r * cols + c)) & 1]
        if occupied:
            for c in range(min(occupied), max(occupied) + 1):
                out |= 1 << (r * cols + c)
    return out


def column_hull(mask, rows, cols):
    out = mask
    for c in range(cols):
        occupied = [r for r in range(rows) if (mask >> (r * cols + c)) & 1]
        if occupied:
            for r in range(min(occupied), max(occupied) + 1):
                out |= 1 << (r * cols + c)
    return out


def odd_bounding_box_fill(mask, rows, cols):
    if mask.bit_count() % 2 == 0:
        return mask
    cells = [divmod(i, cols) for i in range(rows * cols) if (mask >> i) & 1]
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    out = mask
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            out |= 1 << (r * cols + c)
    return out


def polyomino_instances(kind):
    out = []
    for rows, cols in ((2, 3), (3, 3), (3, 4)):
        states = polyominoes(rows, cols)
        if kind == "row":
            phi = lambda mask, r=rows, c=cols: row_hull(mask, r, c)
        elif kind == "alternating":
            phi = lambda mask, r=rows, c=cols: column_hull(row_hull(mask, r, c), r, c)
        else:
            phi = lambda mask, r=rows, c=cols: odd_bounding_box_fill(mask, r, c)
        out.append((f"grid={rows}x{cols}", states, phi))
    return out


def lattice_paths(a, b):
    return tuple(tuple(1 if i in north else 0 for i in range(a + b))
                 for north in combinations(range(a + b), b))


def parallel_ne_swap(word):
    out = list(word)
    swaps = [i for i in range(len(word) - 1) if word[i:i + 2] == (1, 0)]
    for i in swaps:
        out[i], out[i + 1] = 0, 1
    return tuple(out)


def path_area(word):
    east_seen = 0
    area = 0
    for step in word:
        if step == 0:
            east_seen += 1
        else:
            area += east_seen
    return area


def gated_path_reverse(word):
    return tuple(reversed(word)) if path_area(word) % 3 == 1 else word


def rotate_initial_north(word):
    return word[1:] + word[:1] if word[0] == 1 else word


def lattice_path_instances(phi, max_side=5):
    return [(f"box={a}x{b}", lattice_paths(a, b), phi)
            for a in range(1, max_side + 1)
            for b in range(1, max_side + 1)]


# ---------------------------------------------------------------------------
# Focused theorem-contract controls


def stirling_first_kind(n, k):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            table[i][j] = table[i - 1][j - 1] + (i - 1) * table[i - 1][j]
    return table[n][k]


def focused_cycle_pairing(max_n=9):
    before = CHECKS.n
    tested = 0
    for n in range(1, max_n + 1):
        depths = Counter()
        terminal_fibres = Counter()
        for p in permutations(range(n)):
            tested += 1
            k = len(canonical_cycles(p))
            expected_depth = 0 if k == 1 else ceil(log2(k))
            cur = p
            depth = 0
            while pair_cycles_concat(cur) != cur:
                cur = pair_cycles_concat(cur)
                depth += 1
            CHECKS.that(depth == expected_depth, (n, p, depth, expected_depth))
            CHECKS.that(len(canonical_cycles(cur)) == 1, (n, p, cur))
            depths[depth] += 1
            terminal_fibres[cur] += 1

        expected = Counter()
        expected[0] = stirling_first_kind(n, 1)
        for k in range(2, n + 1):
            expected[ceil(log2(k))] += stirling_first_kind(n, k)
        CHECKS.that(depths == expected, (n, depths, expected))
        increasing_cycle = cycles_to_permutation((tuple(range(n)),), n)
        CHECKS.that(terminal_fibres[increasing_cycle] == 2 ** (n - 1),
                    (n, terminal_fibres[increasing_cycle]))
        CHECKS.that(max(terminal_fibres.values()) == 2 ** (n - 1),
                    (n, max(terminal_fibres.values())))
        CHECKS.that(sum(value == 2 ** (n - 1) for value in terminal_fibres.values()) == 1,
                    (n, "nonunique maximum terminal fibre"))
        CHECKS.that(sum(terminal_fibres.values()) == factorial(n),
                    (n, sum(terminal_fibres.values())))
    assertions = CHECKS.n - before
    print(
        "FOCUS_PM1 | n<=9 | exact_clock=ceil(log2(number_of_cycles)) | "
        "depth_layers=unsigned_Stirling_dyadic_bands | recurrent=(n-1)! | "
        "unique_max_terminal_fibre=2^(n-1) | "
        f"states={tested} | assertions={assertions}"
    )
    return assertions


def connected_graph_count(n):
    return sum(len(component_sets(mask, n)) == 1
               for mask in range(1 << len(graph_pairs(n))))


def connected_diameter_two_count(n):
    count = 0
    for mask in range(1 << len(graph_pairs(n))):
        if len(component_sets(mask, n)) != 1:
            continue
        diameter = max(max(graph_distances(mask, n, source)) for source in range(n))
        count += diameter <= 2
    return count


def focused_graph_square(max_n=6):
    before = CHECKS.n
    tested = 0
    connected_counts = [1]
    diameter_two_counts = [1]
    for n in range(1, max_n + 1):
        if n > 1:
            connected_counts.append(connected_graph_count(n))
            diameter_two_counts.append(connected_diameter_two_count(n))
        fixed_count = 0
        basin_counts = Counter()
        one_step_fixed_fibres = Counter()
        maximum_depth = 0
        for mask in range(1 << len(graph_pairs(n))):
            tested += 1
            components = component_sets(mask, n)
            endpoint_edges = []
            for component in components:
                endpoint_edges.extend(combinations(component, 2))
            endpoint = graph_mask(endpoint_edges, n)
            cur = mask
            depth = 0
            while graph_power(cur, n, 2) != cur:
                cur = graph_power(cur, n, 2)
                depth += 1
            CHECKS.that(cur == endpoint, (n, mask, cur, endpoint))
            diameters = []
            for component in components:
                if len(component) <= 1:
                    diameters.append(0)
                else:
                    diameters.append(max(
                        graph_distances(mask, n, vertex)[other]
                        for vertex in component for other in component
                    ))
            diameter = max(diameters, default=0)
            expected_depth = 0 if diameter <= 1 else ceil(log2(diameter))
            CHECKS.that(depth == expected_depth, (n, mask, depth, diameter))
            CHECKS.that(graph_power(mask, n, 2 ** depth) == endpoint,
                        (n, mask, depth, "iterate identity"))
            fixed_count += depth == 0
            basin_counts[endpoint] += 1
            if graph_power(mask, n, 2) == endpoint:
                one_step_fixed_fibres[endpoint] += 1
            maximum_depth = max(maximum_depth, depth)

        # Fixed graphs are exactly cluster graphs, one for each set partition.
        CHECKS.that(fixed_count == len(set_partitions_rgs(n)),
                    (n, fixed_count, len(set_partitions_rgs(n))))
        for endpoint, actual in basin_counts.items():
            predicted_basin = 1
            predicted_fibre = 1
            for component in component_sets(endpoint, n):
                predicted_basin *= connected_counts[len(component) - 1]
                predicted_fibre *= diameter_two_counts[len(component) - 1]
            CHECKS.that(actual == predicted_basin,
                        (n, endpoint, actual, predicted_basin, "basin"))
            CHECKS.that(one_step_fixed_fibres[endpoint] == predicted_fibre,
                        (n, endpoint, one_step_fixed_fibres[endpoint],
                         predicted_fibre, "one-step fibre"))
        sharp = 0 if n <= 2 else ceil(log2(n - 1))
        CHECKS.that(maximum_depth == sharp, (n, maximum_depth, sharp))
    assertions = CHECKS.n - before
    print(
        "FOCUS_GR1 | n<=6 | iterate=G^(2^t) | endpoint=component_clique_closure | "
        "clock=ceil(log2(max_component_diameter)) | fixed=Bell(n) | "
        "endpoint_basin=product_connected_graph_counts | "
        "fixed_target_fibre=product_connected_diameter<=2_counts | "
        f"graphs={tested} | assertions={assertions}"
    )
    return assertions


def focused_parent_jump(max_n=8):
    before = CHECKS.n
    tested = 0
    for n in range(1, max_n + 1):
        states = tuple(rooted_parent(mask, n, 0) for mask in labelled_trees(n))
        star = tuple(0 for _ in range(n))
        star_fibre = 0
        maximum_depth = 0
        fixed = 0
        for parent in states:
            tested += 1
            height = max(tree_heights(parent), default=0)
            expected = 0 if height <= 1 else ceil(log2(height))
            cur = parent
            depth = 0
            while parent_jump(cur) != cur:
                cur = parent_jump(cur)
                depth += 1
            CHECKS.that(cur == star, (n, parent, cur, star))
            CHECKS.that(depth == expected, (n, parent, depth, height))
            if parent_jump(parent) == star:
                star_fibre += 1
            fixed += parent == star
            maximum_depth = max(maximum_depth, depth)
        if n == 1:
            predicted_fibre = 1
            total = 1
        else:
            predicted_fibre = sum(comb(n - 1, k) * k ** (n - 1 - k)
                                  for k in range(1, n))
            total = n ** (n - 2)
        CHECKS.that(len(states) == total, (n, len(states), total))
        CHECKS.that(star_fibre == predicted_fibre,
                    (n, star_fibre, predicted_fibre))
        CHECKS.that(fixed == 1, (n, fixed))
        sharp = 0 if n <= 2 else ceil(log2(n - 1))
        CHECKS.that(maximum_depth == sharp, (n, maximum_depth, sharp))
    assertions = CHECKS.n - before
    print(
        "FOCUS_TR1 | n<=8 | parent_t(v)=ancestor_at_2^t | "
        "clock=ceil(log2(height)) | unique_star_attractor | "
        "star_fibre=sum_C(n-1,k)k^(n-1-k) | "
        f"trees={tested} | assertions={assertions}"
    )
    return assertions


def focused_parking(max_n=7):
    before = CHECKS.n
    tested = 0
    for n in range(1, max_n + 1):
        fibres = Counter()
        for state in parking_functions(n):
            tested += 1
            outcome = parking_outcome(state)
            CHECKS.that(tuple(sorted(outcome)) == tuple(range(1, n + 1)),
                        (n, state, outcome))
            CHECKS.that(parking_outcome(outcome) == outcome,
                        (n, outcome, "not fixed"))
            fibres[outcome] += 1
        CHECKS.that(len(fibres) == factorial(n), (n, len(fibres)))
        for outcome in permutations(range(1, n + 1)):
            CHECKS.that(fibres[outcome] == parking_fibre_formula(outcome),
                        (n, outcome, fibres[outcome], parking_fibre_formula(outcome)))
        CHECKS.that(sum(fibres.values()) == (n + 1) ** (n - 1),
                    (n, sum(fibres.values())))
        identity = tuple(range(1, n + 1))
        CHECKS.that(fibres[identity] == factorial(n), (n, fibres[identity]))
        CHECKS.that(sum(value == factorial(n) for value in fibres.values()) == 1,
                    (n, "maximum not unique"))
    assertions = CHECKS.n - before
    print(
        "CONTROL_PK1 | n<=7 | idempotent_outcome_retraction | "
        "target_fibre=product_of_occupied_left_runs | unique_max=n! | "
        f"parking_functions={tested} | assertions={assertions}"
    )
    return assertions


def run():
    rows = []
    rows.append(audit_family("PM1", permutation_instances(pair_cycles_concat)))
    rows.append(audit_family("PM2", permutation_instances(pair_cycles_interleave)))
    rows.append(audit_family("PM3", permutation_instances(canonicalize_cycle_tails)))
    rows.append(audit_family("PM4", permutation_instances(rotate_one_line_to_one)))
    rows.append(audit_family("PM5", permutation_instances(gated_inverse)))
    rows.append(audit_family("PM6", permutation_instances(prefix_max_reversal)))
    rows.append(audit_family("PM7", permutation_instances(reverse_increasing_run_list)))

    rows.append(audit_family("SP1", partition_instances(lambda p: block_batch_merge(p, 2))))
    rows.append(audit_family("SP2", partition_instances(lambda p: block_batch_merge(p, 3))))
    rows.append(audit_family("SP3", partition_instances(lambda p: transfer_block_extrema(p, "left"))))
    rows.append(audit_family("SP4", partition_instances(lambda p: transfer_block_extrema(p, "right"))))
    rows.append(audit_family("SP5", partition_instances(parity_pair_merge)))
    rows.append(audit_family("SP6", partition_instances(gated_partition_reflection)))
    rows.append(audit_family("SP7", partition_instances(balanced_block_split)))

    rows.append(audit_family("PK1", parking_instances()))
    rows.append(audit_family("MT1", matching_instances(rotate_crossing_component_partners)))
    rows.append(audit_family("MT2", matching_instances(first_crossing_uncross)))
    rows.append(audit_family("MT3", matching_instances(first_nesting_flatten)))

    rows.append(audit_family("GR1", graph_instances(lambda g, n: graph_power(g, n, 2))))
    rows.append(audit_family("GR2", graph_instances(lambda g, n: graph_power(g, n, 3))))
    rows.append(audit_family("GR3", graph_instances(lambda g, n: triangle_edge_filter(g, n, False))))
    rows.append(audit_family("GR4", graph_instances(lambda g, n: triangle_edge_filter(g, n, True))))
    rows.append(audit_family("GR5", graph_instances(bridge_delete, max_n=5)))
    rows.append(audit_family("GR6", graph_instances(even_component_complement, max_n=5)))
    rows.append(audit_family("GR7", graph_instances(add_distance_exactly_three)))

    rows.append(audit_family("TR1", parent_tree_instances()))
    rows.append(audit_family("TR2", moving_root_instances(centroid_step)))
    rows.append(audit_family("TR3", moving_root_instances(center_step)))

    rows.append(audit_family("PT1", partition_shape_instances()))
    rows.append(audit_family("PX1", polyomino_instances("row")))
    rows.append(audit_family("PX2", polyomino_instances("alternating")))
    rows.append(audit_family("PX3", polyomino_instances("box")))
    rows.append(audit_family("LP1", lattice_path_instances(parallel_ne_swap)))
    rows.append(audit_family("LP2", lattice_path_instances(gated_path_reverse)))
    rows.append(audit_family("LP3", lattice_path_instances(rotate_initial_north)))

    breadth_assertions = sum(row.assertions for row in rows)
    breadth_states = sum(row.states for row in rows)
    focused_cycle_pairing()
    focused_graph_square()
    focused_parent_jump()
    focused_parking()
    print(
        f"GLOBAL | systems={len(rows)} | parameter_states={breadth_states} | "
        f"breadth_assertions={breadth_assertions} | total_assertions={CHECKS.n} | PASS"
    )


if __name__ == "__main__":
    run()
