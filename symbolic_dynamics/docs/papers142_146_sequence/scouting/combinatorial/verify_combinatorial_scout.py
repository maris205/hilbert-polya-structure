#!/usr/bin/env python3
"""Exact Route-A combinatorial breadth scout for the next anonymous batch.

The program exhausts thirteen genuinely different literal finite maps.  It is
counterexample pressure and a reproducible fingerprint, never a novelty
certificate.  The three strongest mathematical signals receive independent
formula checks; known conjugacies and standard-owner controls are deliberately
kept in the transcript as permanent negative evidence.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial
import heapq


class Checks:
    def __init__(self) -> None:
        self.n = 0

    def that(self, condition: bool, payload=None) -> None:
        self.n += 1
        if not condition:
            raise AssertionError(payload)


CHECKS = Checks()


@dataclass(frozen=True)
class Row:
    ident: str
    parameters: int
    states: int
    periods: tuple[int, ...]
    max_tail: int
    last_image: int
    last_fixed: int
    assertions: int


def scan_family(ident, instances):
    before = CHECKS.n
    periods = set()
    max_tail = 0
    state_total = 0
    last_image = last_fixed = 0
    parameter_count = 0
    for label, raw_states, phi in instances:
        parameter_count += 1
        states = tuple(raw_states)
        universe = set(states)
        CHECKS.that(bool(states), (ident, label, "empty"))
        CHECKS.that(len(states) == len(universe), (ident, label, "duplicates"))
        state_total += len(states)
        nxt = {}
        for state in states:
            image = phi(state)
            CHECKS.that(image in universe, (ident, label, state, image, "closure"))
            nxt[state] = image
        CHECKS.that(len(nxt) == len(states), (ident, label, "coverage"))
        image_set = set(nxt.values())
        fixed = {state for state in states if nxt[state] == state}
        CHECKS.that(fixed <= image_set, (ident, label, "fixed/image"))
        last_image, last_fixed = len(image_set), len(fixed)
        for start in states:
            seen = {}
            cur = start
            while cur not in seen:
                seen[cur] = len(seen)
                cur = nxt[cur]
            tail = seen[cur]
            period = len(seen) - tail
            CHECKS.that(period >= 1, (ident, label, start, tail, period))
            witness = cur
            for _ in range(period):
                witness = nxt[witness]
            CHECKS.that(witness == cur, (ident, label, start, "cycle"))
            periods.add(period)
            max_tail = max(max_tail, tail)
    row = Row(
        ident, parameter_count, state_total, tuple(sorted(periods)), max_tail,
        last_image, last_fixed, CHECKS.n - before,
    )
    print(
        f"{row.ident} | params={row.parameters} | states={row.states} | "
        f"periods={','.join(map(str, row.periods))} | max_tail={row.max_tail} | "
        f"last_image={row.last_image} | last_fixed={row.last_fixed} | "
        f"assertions={row.assertions}"
    )
    return row


def endpoint_depth(state, phi):
    seen = set()
    depth = 0
    while phi(state) != state:
        CHECKS.that(state not in seen, ("endpoint-cycle", state))
        seen.add(state)
        state = phi(state)
        depth += 1
    return state, depth


def catalan(n):
    return comb(2 * n, n) // (n + 1)


# ---------------------------------------------------------------------------
# T01: sibling-min cascade on rooted labelled trees


def prufer_parent(code, n):
    if n == 1:
        return (0,)
    degree = [1] * n
    for x in code:
        degree[x] += 1
    leaves = [v for v, d in enumerate(degree) if d == 1]
    heapq.heapify(leaves)
    edges = []
    for x in code:
        leaf = heapq.heappop(leaves)
        edges.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
        if degree[x] == 1:
            heapq.heappush(leaves, x)
    if n > 1:
        edges.append((heapq.heappop(leaves), heapq.heappop(leaves)))
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    parent = [-1] * n
    parent[0] = 0
    queue = [0]
    for u in queue:
        for v in adjacency[u]:
            if parent[v] < 0:
                parent[v] = u
                queue.append(v)
    return tuple(parent)


def rooted_trees(n):
    if n == 1:
        yield (0,)
        return
    for code in product(range(n), repeat=n - 2):
        yield prufer_parent(code, n)


def tree_children(parent):
    children = [[] for _ in parent]
    for v in range(1, len(parent)):
        children[parent[v]].append(v)
    return children


def sibling_min_cascade(parent):
    children = tree_children(parent)
    out = list(parent)
    for siblings in children:
        if siblings:
            least = min(siblings)
            for v in siblings:
                if v != least:
                    out[v] = least
    return tuple(out)


def least_frontier_order(parent):
    children = tree_children(parent)
    frontier = list(children[0])
    heapq.heapify(frontier)
    order = [0]
    while frontier:
        v = heapq.heappop(frontier)
        order.append(v)
        for child in children[v]:
            heapq.heappush(frontier, child)
    return tuple(order)


def path_order(parent):
    children = tree_children(parent)
    order = [0]
    while children[order[-1]]:
        CHECKS.that(len(children[order[-1]]) == 1, ("not-path", parent))
        order.append(children[order[-1]][0])
    return tuple(order)


def tree_basin_formula(order):
    value = 1
    for k in range(1, len(order)):
        last_greater = 0
        for j in range(1, k):
            if order[j] > order[k]:
                last_greater = j
        value *= k - last_greater
    return value


def tree_instances(max_n=8):
    for n in range(1, max_n + 1):
        yield f"n={n}", rooted_trees(n), sibling_min_cascade


def focus_tree(max_n=8):
    before = CHECKS.n
    last_max = 0
    for n in range(1, max_n + 1):
        basins = Counter()
        depths = Counter()
        for parent in rooted_trees(n):
            greedy = least_frontier_order(parent)
            image = sibling_min_cascade(parent)
            CHECKS.that(least_frontier_order(image) == greedy,
                        ("T01-order-invariant", n, parent))
            target, depth = endpoint_depth(parent, sibling_min_cascade)
            CHECKS.that(path_order(target) == greedy,
                        ("T01-endpoint", n, parent, target, greedy))
            CHECKS.that(depth <= max(0, n - 2),
                        ("T01-clock", n, parent, depth))
            basins[greedy] += 1
            depths[depth] += 1
        expected_orders = set(permutations(range(1, n)))
        CHECKS.that({order[1:] for order in basins} == expected_orders,
                    ("T01-support", n))
        for order, observed in basins.items():
            CHECKS.that(observed == tree_basin_formula(order),
                        ("T01-fibre", n, order, observed,
                         tree_basin_formula(order)))
        increasing = tuple(range(n))
        last_max = max(basins.values())
        CHECKS.that(basins[increasing] == factorial(max(0, n - 1)),
                    ("T01-increasing", n, basins[increasing]))
        CHECKS.that([order for order, size in basins.items() if size == last_max]
                    == [increasing], ("T01-unique-max", n, last_max))
        CHECKS.that(max(depths) == max(0, n - 2),
                    ("T01-sharp-clock", n, depths))
        star = tuple([0] * n)
        _, star_depth = endpoint_depth(star, sibling_min_cascade)
        CHECKS.that(star_depth == max(0, n - 2),
                    ("T01-star", n, star_depth))
    assertions = CHECKS.n - before
    print(
        f"FOCUS T01 | n<=8 | order_invariant=PASS | terminal_fibres=PASS | "
        f"sharp_clock=PASS | last_max_fibre={last_max} | assertions={assertions}"
    )
    return assertions


# ---------------------------------------------------------------------------
# D01: first-two-component reassociation on Dyck paths


def dyck_paths(n):
    def rec(word, up, down):
        if up == n and down == n:
            yield tuple(word)
            return
        if up < n:
            word.append(1)
            yield from rec(word, up + 1, down)
            word.pop()
        if down < up:
            word.append(-1)
            yield from rec(word, up, down + 1)
            word.pop()
    yield from rec([], 0, 0)


def dyck_returns(path):
    height = 0
    out = []
    for i, step in enumerate(path):
        height += step
        if height == 0:
            out.append(i + 1)
    return tuple(out)


def dyck_reassociate(path):
    returns = dyck_returns(path)
    if len(returns) <= 1:
        return path
    first, second = returns[:2]
    return path[:first - 1] + path[first:second] + (path[first - 1],) + path[second:]


def dyck_endpoint(path):
    first = dyck_returns(path)[0]
    return path[:first - 1] + path[first:] + (path[first - 1],)


def dyck_instances(max_n=11):
    for n in range(1, max_n + 1):
        yield f"n={n}", dyck_paths(n), dyck_reassociate


def focus_dyck(max_n=11):
    before = CHECKS.n
    last_max = 0
    for n in range(1, max_n + 1):
        basins = defaultdict(Counter)
        depth_layers = Counter()
        deepest = []
        for path in dyck_paths(n):
            components = len(dyck_returns(path))
            target, depth = endpoint_depth(path, dyck_reassociate)
            CHECKS.that(depth == components - 1,
                        ("D01-depth", n, path, depth, components))
            CHECKS.that(target == dyck_endpoint(path),
                        ("D01-endpoint", n, path, target, dyck_endpoint(path)))
            basins[target][depth] += 1
            depth_layers[depth] += 1
            if depth == n - 1:
                deepest.append(path)
        for target, observed in basins.items():
            interior = target[1:-1]
            r = len(dyck_returns(interior)) if interior else 0
            expected = Counter({d: 1 for d in range(r + 1)})
            CHECKS.that(observed == expected,
                        ("D01-target-polynomial", n, target, observed, expected))
        for k in range(1, n + 1):
            expected = k * comb(2 * n - k, n) // (2 * n - k)
            CHECKS.that(depth_layers[k - 1] == expected,
                        ("D01-layer", n, k, depth_layers[k - 1], expected))
        CHECKS.that(len(basins) == catalan(n - 1),
                    ("D01-fixed", n, len(basins)))
        deepest_source = tuple(step for _ in range(n) for step in (1, -1))
        CHECKS.that(deepest == [deepest_source],
                    ("D01-unique-deepest", n, deepest))
        fibre_sizes = {target: sum(poly.values()) for target, poly in basins.items()}
        last_max = max(fibre_sizes.values())
        max_target = (1,) + tuple(step for _ in range(n - 1) for step in (1, -1)) + (-1,)
        CHECKS.that(last_max == n and fibre_sizes[max_target] == n,
                    ("D01-max-fibre", n, last_max, max_target))
        CHECKS.that([target for target, size in fibre_sizes.items() if size == last_max]
                    == [max_target], ("D01-unique-max-target", n))
    assertions = CHECKS.n - before
    print(
        f"FOCUS D01 | n<=11 | temporal_census=PASS | pointwise_depth_fibres=PASS | "
        f"unique_deepest=PASS | last_max_fibre={last_max} | assertions={assertions}"
    )
    return assertions


# ---------------------------------------------------------------------------
# P01: Cartesian-min preorder; exact conjugacy kill with stack sorting


def cartesian_preorder(word):
    if not word:
        return ()
    pivot = word.index(min(word))
    return ((word[pivot],) + cartesian_preorder(word[:pivot])
            + cartesian_preorder(word[pivot + 1:]))


def stack_sort(word):
    if not word:
        return ()
    pivot = word.index(max(word))
    return stack_sort(word[:pivot]) + stack_sort(word[pivot + 1:]) + (word[pivot],)


def reverse_complement(word):
    n = len(word)
    return tuple(n + 1 - x for x in reversed(word))


@lru_cache(maxsize=None)
def cartesian_fibre(word):
    if not word:
        return 1
    if word[0] != min(word):
        return 0
    total = 0
    for cut in range(1, len(word) + 1):
        total += cartesian_fibre(word[1:cut]) * cartesian_fibre(word[cut:])
    return total


def permutation_instances(phi, max_n):
    for n in range(1, max_n + 1):
        yield f"n={n}", permutations(range(1, n + 1)), phi


def focus_cartesian(max_n=9):
    before = CHECKS.n
    last_max = 0
    for n in range(1, max_n + 1):
        fibres = Counter()
        depth_sources = Counter()
        max_sources = []
        for perm in permutations(range(1, n + 1)):
            conjugate = reverse_complement(
                cartesian_preorder(reverse_complement(perm)))
            CHECKS.that(conjugate == stack_sort(perm),
                        ("P01-stack-conjugacy", n, perm, conjugate, stack_sort(perm)))
            target, depth = endpoint_depth(perm, cartesian_preorder)
            CHECKS.that(target == tuple(range(1, n + 1)),
                        ("P01-terminal", n, perm, target))
            CHECKS.that(depth <= n - 1, ("P01-clock", n, perm, depth))
            image = cartesian_preorder(perm)
            fibres[image] += 1
            depth_sources[depth] += 1
            if depth == n - 1:
                max_sources.append(perm)
        for target, observed in fibres.items():
            CHECKS.that(observed == cartesian_fibre(target),
                        ("P01-fibre", n, target, observed, cartesian_fibre(target)))
        identity = tuple(range(1, n + 1))
        last_max = max(fibres.values())
        CHECKS.that(last_max == catalan(n) and fibres[identity] == catalan(n),
                    ("P01-Catalan-max", n, last_max))
        CHECKS.that([target for target, size in fibres.items() if size == last_max]
                    == [identity], ("P01-unique-max", n))
        if n == 1:
            expected_sources = [(1,)]
        elif n == 2:
            expected_sources = [(2, 1)]
        else:
            expected_sources = [
                (n, 1) + tail for tail in permutations(range(2, n))
            ]
        CHECKS.that(max_sources == expected_sources,
                    ("P01-sharp-sources", n, max_sources, expected_sources))
    assertions = CHECKS.n - before
    print(
        f"FOCUS P01 | n<=9 | stack_conjugacy=EXACT | target_fibres=PASS | "
        f"sharp_clock=PASS | last_max_fibre={last_max} | assertions={assertions}"
    )
    return assertions


# ---------------------------------------------------------------------------
# O01: ordered-set-partition minimum extraction


def ordered_partitions(n):
    states = [((0,),)]
    for x in range(1, n):
        new = []
        for state in states:
            for i in range(len(state)):
                blocks = list(state)
                blocks[i] = blocks[i] + (x,)
                new.append(tuple(blocks))
            for i in range(len(state) + 1):
                new.append(state[:i] + ((x,),) + state[i:])
        states = new
    return tuple(states)


def ordered_partition_extract(state):
    out = []
    for block in state:
        if len(block) == 1:
            out.append(block)
        else:
            out.append((block[0],))
            out.append(block[1:])
    return tuple(out)


def ordered_partition_endpoint(state):
    return tuple(x for block in state for x in block)


def ordered_partition_instances(max_n=7):
    for n in range(1, max_n + 1):
        yield f"n={n}", ordered_partitions(n), ordered_partition_extract


def focus_ordered_partitions(max_n=7):
    before = CHECKS.n
    last_max = 0
    for n in range(1, max_n + 1):
        basins = Counter()
        for state in ordered_partitions(n):
            target, depth = endpoint_depth(state, ordered_partition_extract)
            word = tuple(block[0] for block in target)
            CHECKS.that(word == ordered_partition_endpoint(state),
                        ("O01-endpoint", n, state, word))
            CHECKS.that(depth == max(len(block) for block in state) - 1,
                        ("O01-depth", n, state, depth))
            basins[word] += 1
        for word, observed in basins.items():
            ascents = sum(word[i] < word[i + 1] for i in range(n - 1))
            CHECKS.that(observed == 2 ** ascents,
                        ("O01-fibre", n, word, observed, ascents))
        identity = tuple(range(n))
        last_max = max(basins.values())
        CHECKS.that(last_max == 2 ** (n - 1) and basins[identity] == last_max,
                    ("O01-max", n, last_max))
        CHECKS.that([word for word, size in basins.items() if size == last_max]
                    == [identity], ("O01-unique-max", n))
    assertions = CHECKS.n - before
    print(
        f"FOCUS O01 | n<=7 | segmentation_fibres=PASS | refinement_clock=PASS | "
        f"last_max_fibre={last_max} | assertions={assertions}"
    )
    return assertions


# ---------------------------------------------------------------------------
# S01/S02: set-family union closure and clutter blocker


def family_members(mask):
    bit = 0
    while mask:
        if mask & 1:
            yield bit
        bit += 1
        mask >>= 1


def family_mask(members):
    out = 0
    for member in members:
        out |= 1 << member
    return out


def union_square(mask):
    members = tuple(family_members(mask))
    return mask | family_mask(a | b for a in members for b in members)


def set_family_instances(max_n=4):
    for n in range(1, max_n + 1):
        yield f"n={n}", range(1 << (1 << n)), union_square


def is_antichain(mask):
    members = tuple(family_members(mask))
    return all(not (a != b and (a & b) == a) for a in members for b in members)


def clutters(n):
    return tuple(mask for mask in range(1 << (1 << n)) if is_antichain(mask))


def blocker(mask, n):
    edges = tuple(family_members(mask))
    hitting = [x for x in range(1 << n) if all(x & edge for edge in edges)]
    minimal = []
    for x in hitting:
        if not any(y != x and (y & x) == y for y in hitting):
            minimal.append(x)
    return family_mask(minimal)


def clutter_instances(max_n=4):
    for n in range(1, max_n + 1):
        yield f"n={n}", clutters(n), lambda state, n=n: blocker(state, n)


def focus_blocker(max_n=4):
    before = CHECKS.n
    for n in range(1, max_n + 1):
        for state in clutters(n):
            CHECKS.that(blocker(blocker(state, n), n) == state,
                        ("S02-involution", n, state))
    assertions = CHECKS.n - before
    print(f"FOCUS S02 | n<=4 | blocker_involution=PASS | assertions={assertions}")
    return assertions


# ---------------------------------------------------------------------------
# R01: directed-relation path doubling


def relation_has(mask, n, u, v):
    return bool(mask & (1 << (u * n + v)))


def relation_path_double(mask, n):
    out = mask
    for u in range(n):
        for v in range(n):
            if relation_has(mask, n, u, v):
                for w in range(n):
                    if relation_has(mask, n, v, w):
                        out |= 1 << (u * n + w)
    return out


def relation_closure(mask, n):
    out = mask
    for k in range(n):
        for i in range(n):
            if relation_has(out, n, i, k):
                for j in range(n):
                    if relation_has(out, n, k, j):
                        out |= 1 << (i * n + j)
    return out


def relation_diameter(mask, n):
    # Positive path distance is required: a directed cycle can create a
    # previously absent diagonal pair even when every distinct reachable pair
    # is already an edge.  Thus the diagonal starts at infinity unless a loop
    # is literally present, rather than at the usual zero.
    infinity = n * n + 1
    dist = [
        [1 if relation_has(mask, n, u, v) else infinity for v in range(n)]
        for u in range(n)
    ]
    for k in range(n):
        old = [row[:] for row in dist]
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(old[i][j], old[i][k] + old[k][j])
    finite = [dist[i][j] for i in range(n) for j in range(n) if dist[i][j] < infinity]
    return max(finite, default=0)


def ceil_log2(x):
    value = 0
    power = 1
    while power < x:
        value += 1
        power *= 2
    return value


def relation_instances(max_n=4):
    for n in range(1, max_n + 1):
        yield f"n={n}", range(1 << (n * n)), lambda state, n=n: relation_path_double(state, n)


def focus_relations(max_n=4):
    before = CHECKS.n
    for n in range(1, max_n + 1):
        phi = lambda state, n=n: relation_path_double(state, n)
        for state in range(1 << (n * n)):
            target, depth = endpoint_depth(state, phi)
            diameter = relation_diameter(state, n)
            CHECKS.that(target == relation_closure(state, n),
                        ("R01-closure", n, state, target))
            CHECKS.that(depth == ceil_log2(max(1, diameter)),
                        ("R01-clock", n, state, depth, diameter))
    assertions = CHECKS.n - before
    print(f"FOCUS R01 | n<=4 | exact_powers=PASS | diameter_clock=PASS | assertions={assertions}")
    return assertions


# ---------------------------------------------------------------------------
# Q01/Q02: two poset neighborhood/support transforms


@lru_cache(maxsize=None)
def labelled_posets(n):
    pairs = tuple(combinations(range(n), 2))
    out = []
    for choices in product((-1, 0, 1), repeat=len(pairs)):
        rows = [1 << i for i in range(n)]
        for (i, j), choice in zip(pairs, choices):
            if choice < 0:
                rows[j] |= 1 << i
            elif choice > 0:
                rows[i] |= 1 << j
        transitive = True
        for i in range(n):
            for k in range(n):
                if rows[i] >> k & 1 and rows[k] & ~rows[i]:
                    transitive = False
                    break
            if not transitive:
                break
        if transitive:
            out.append(tuple(rows))
    return tuple(out)


def strict_subset(a, b):
    return a != b and (a & b) == a


def open_downset_inclusion(poset):
    n = len(poset)
    down = []
    for x in range(n):
        down.append(sum((bool(poset[u] >> x & 1) and u != x) << u for u in range(n)))
    rows = []
    for x in range(n):
        row = 1 << x
        for y in range(n):
            if strict_subset(down[x], down[y]):
                row |= 1 << y
        rows.append(row)
    return tuple(rows)


def atom_support_inclusion(poset):
    n = len(poset)
    minima = [x for x in range(n) if not any(u != x and poset[u] >> x & 1 for u in range(n))]
    supports = []
    for x in range(n):
        supports.append(sum((poset[m] >> x & 1) << m for m in minima))
    rows = []
    for x in range(n):
        row = 1 << x
        for y in range(n):
            if strict_subset(supports[x], supports[y]):
                row |= 1 << y
        rows.append(row)
    return tuple(rows)


def poset_instances(phi, max_n=5):
    for n in range(1, max_n + 1):
        yield f"n={n}", labelled_posets(n), phi


def focus_atom_support(max_n=5):
    before = CHECKS.n
    for n in range(1, max_n + 1):
        for state in labelled_posets(n):
            image = atom_support_inclusion(state)
            CHECKS.that(atom_support_inclusion(image) == image,
                        ("Q02-idempotent", n, state, image))
    assertions = CHECKS.n - before
    print(f"FOCUS Q02 | n<=5 | support_retraction=PASS | assertions={assertions}")
    return assertions


# ---------------------------------------------------------------------------
# C01: parallel rightward relaxation of fixed-length compositions


def compositions(n):
    if n == 0:
        yield ()
        return
    for cuts in range(1 << (n - 1)):
        part = 1
        out = []
        for i in range(n - 1):
            if cuts >> i & 1:
                out.append(part)
                part = 1
            else:
                part += 1
        out.append(part)
        yield tuple(out)


def composition_relax(state):
    out = list(state)
    active = [i for i in range(len(state) - 1) if state[i] >= state[i + 1] + 2]
    for i in active:
        out[i] -= 1
        out[i + 1] += 1
    return tuple(out)


def composition_instances(max_n=12):
    for n in range(1, max_n + 1):
        yield f"weight={n}", compositions(n), composition_relax


def focus_compositions(max_n=12):
    before = CHECKS.n
    for n in range(1, max_n + 1):
        for state in compositions(n):
            image = composition_relax(state)
            old_moment = sum(i * value for i, value in enumerate(state))
            new_moment = sum(i * value for i, value in enumerate(image))
            active = sum(state[i] >= state[i + 1] + 2 for i in range(len(state) - 1))
            CHECKS.that(new_moment - old_moment == active,
                        ("C01-potential", n, state, image))
    assertions = CHECKS.n - before
    print(f"FOCUS C01 | weight<=12 | strict_moment_potential=PASS | assertions={assertions}")
    return assertions


# ---------------------------------------------------------------------------
# N01: Kreweras complement on noncrossing set partitions


def set_partitions(n):
    def rec(x, blocks):
        if x == n:
            yield tuple(tuple(block) for block in blocks)
            return
        for i in range(len(blocks)):
            blocks[i].append(x)
            yield from rec(x + 1, blocks)
            blocks[i].pop()
        blocks.append([x])
        yield from rec(x + 1, blocks)
        blocks.pop()
    if n == 0:
        yield ()
    else:
        yield from rec(1, [[0]])


def noncrossing(partition):
    for i, left in enumerate(partition):
        for right in partition[i + 1:]:
            for a, c in combinations(left, 2):
                for b, d in combinations(right, 2):
                    b, d = sorted((b, d))
                    if (a < b < c < d) or (b < a < d < c):
                        return False
    return True


@lru_cache(maxsize=None)
def noncrossing_partitions(n):
    return tuple(partition for partition in set_partitions(n) if noncrossing(partition))


def cycles_to_partition(perm):
    unseen = set(range(len(perm)))
    blocks = []
    while unseen:
        start = min(unseen)
        cycle = []
        cur = start
        while cur in unseen:
            unseen.remove(cur)
            cycle.append(cur)
            cur = perm[cur]
        blocks.append(tuple(sorted(cycle)))
    return tuple(sorted(blocks, key=lambda block: block[0]))


def kreweras(partition):
    n = sum(map(len, partition))
    perm = list(range(n))
    for block in partition:
        for i, x in enumerate(block):
            perm[x] = block[(i + 1) % len(block)]
    inverse = [0] * n
    for i, image in enumerate(perm):
        inverse[image] = i
    complement_perm = tuple(inverse[(i + 1) % n] for i in range(n))
    return cycles_to_partition(complement_perm)


def noncrossing_instances(max_n=8):
    for n in range(1, max_n + 1):
        yield f"n={n}", noncrossing_partitions(n), kreweras


def focus_kreweras(max_n=8):
    before = CHECKS.n
    for n in range(1, max_n + 1):
        for state in noncrossing_partitions(n):
            cur = state
            for _ in range(2 * n):
                cur = kreweras(cur)
            CHECKS.that(cur == state, ("N01-order", n, state, cur))
    assertions = CHECKS.n - before
    print(f"FOCUS N01 | n<=8 | order_divides_2n=PASS | assertions={assertions}")
    return assertions


# ---------------------------------------------------------------------------
# P02: RSK insertion-tableau row-word projection


def insertion_tableau(word):
    rows = []
    for value in word:
        carry = value
        row_index = 0
        while True:
            if row_index == len(rows):
                rows.append([carry])
                break
            row = rows[row_index]
            position = next((i for i, x in enumerate(row) if x > carry), None)
            if position is None:
                row.append(carry)
                break
            row[position], carry = carry, row[position]
            row_index += 1
    return tuple(tuple(row) for row in rows)


def tableau_row_word(tableau):
    return tuple(value for row in reversed(tableau) for value in row)


def rsk_projection(word):
    return tableau_row_word(insertion_tableau(word))


def hook_tableaux(shape):
    n = sum(shape)
    hooks = 1
    for i, row_length in enumerate(shape):
        for j in range(row_length):
            below = sum(j < shape[k] for k in range(i + 1, len(shape)))
            hooks *= row_length - j + below
    return factorial(n) // hooks


def focus_rsk(max_n=8):
    before = CHECKS.n
    for n in range(1, max_n + 1):
        fibres = Counter()
        for word in permutations(range(n)):
            image = rsk_projection(word)
            CHECKS.that(rsk_projection(image) == image,
                        ("P02-idempotent", n, word, image))
            fibres[image] += 1
        for target, observed in fibres.items():
            shape = tuple(map(len, insertion_tableau(target)))
            CHECKS.that(observed == hook_tableaux(shape),
                        ("P02-RSK-fibre", n, target, observed, shape))
    assertions = CHECKS.n - before
    print(f"FOCUS P02 | n<=8 | RSK_fibres=PASS | idempotent=PASS | assertions={assertions}")
    return assertions


# ---------------------------------------------------------------------------
# L01: unilateral shift on Catalan area sequences


def area_sequences(n):
    if n == 1:
        yield (0,)
        return
    def rec(seq):
        if len(seq) == n:
            yield tuple(seq)
            return
        for value in range(seq[-1] + 2):
            seq.append(value)
            yield from rec(seq)
            seq.pop()
    yield from rec([0])


def area_shift(state):
    if len(state) == 1:
        return state
    return (0,) + tuple(value + 1 for value in state[:-1])


def area_instances(max_n=11):
    for n in range(1, max_n + 1):
        yield f"n={n}", area_sequences(n), area_shift


def focus_area(max_n=11):
    before = CHECKS.n
    last_max = 0
    for n in range(1, max_n + 1):
        fibres = Counter()
        for state in area_sequences(n):
            target, depth = endpoint_depth(state, area_shift)
            staircase = tuple(range(n))
            CHECKS.that(target == staircase, ("L01-terminal", n, state, target))
            prefix = 0
            for i, value in enumerate(state):
                if value == i:
                    prefix += 1
                else:
                    break
            CHECKS.that(depth == n - prefix,
                        ("L01-clock", n, state, depth, prefix))
            fibres[area_shift(state)] += 1
        for target, observed in fibres.items():
            CHECKS.that(observed == target[-1] + 1,
                        ("L01-fibre", n, target, observed))
        last_max = max(fibres.values())
    assertions = CHECKS.n - before
    print(
        f"FOCUS L01 | n<=11 | prefix_clock=PASS | one_step_fibres=PASS | "
        f"last_max_fibre={last_max} | assertions={assertions}"
    )
    return assertions


def main():
    rows = []
    rows.append(scan_family("T01", tree_instances()))
    rows.append(scan_family("D01", dyck_instances()))
    rows.append(scan_family("P01", permutation_instances(cartesian_preorder, 9)))
    rows.append(scan_family("O01", ordered_partition_instances()))
    rows.append(scan_family("S01", set_family_instances()))
    rows.append(scan_family("S02", clutter_instances()))
    rows.append(scan_family("R01", relation_instances()))
    rows.append(scan_family("Q01", poset_instances(open_downset_inclusion)))
    rows.append(scan_family("Q02", poset_instances(atom_support_inclusion)))
    rows.append(scan_family("C01", composition_instances()))
    rows.append(scan_family("N01", noncrossing_instances()))
    rows.append(scan_family("P02", permutation_instances(rsk_projection, 8)))
    rows.append(scan_family("L01", area_instances()))

    focus_tree()
    focus_dyck()
    focus_cartesian()
    focus_ordered_partitions()
    focus_blocker()
    focus_relations()
    focus_atom_support()
    focus_compositions()
    focus_kreweras()
    focus_rsk()
    focus_area()

    CHECKS.that(len(rows) == 13, ("literal-system-count", len(rows)))
    total_states = sum(row.states for row in rows)
    print(
        f"SUMMARY | literal_systems={len(rows)} | parameter_states={total_states} | "
        f"assertions={CHECKS.n} | PASS"
    )


if __name__ == "__main__":
    main()
