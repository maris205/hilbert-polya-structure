#!/usr/bin/env python3
"""Exact Stage-1 falsifier for the P147--P151 stochastic scouting lane.

All arithmetic is integral or Fraction arithmetic.  The program deliberately
contains both labelled-state recursions and compressed/formula engines where a
candidate is being considered for promotion.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial, gcd


ASSERTIONS = 0
LANE_ASSERTIONS: dict[str, int] = defaultdict(int)


def check(lane: str, condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    LANE_ASSERTIONS[lane] += 1
    if not condition:
        raise AssertionError(f"{lane}: {message}")


def add_dist(target: dict, source: dict, weight: Fraction = Fraction(1)) -> None:
    for key, value in source.items():
        target[key] += weight * value


def poly_add(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    n = max(len(a), len(b))
    return tuple((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n))


def poly_mul(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)


def poly_scale(a: tuple[Fraction, ...], scalar: Fraction | int) -> tuple[Fraction, ...]:
    return tuple(scalar * coefficient for coefficient in a)


def poly_shift(a: tuple[Fraction, ...], amount: int) -> tuple[Fraction, ...]:
    return (Fraction(0),) * amount + a


def poly_derivative_at_one(a: tuple[Fraction, ...], order: int = 0) -> Fraction:
    if order == 0:
        return sum(a, Fraction(0))
    if order == 1:
        return sum(Fraction(i) * coefficient for i, coefficient in enumerate(a))
    if order == 2:
        return sum(Fraction(i * (i - 1)) * coefficient for i, coefficient in enumerate(a))
    raise ValueError("only derivative orders zero, one, and two are used")


# S01 -----------------------------------------------------------------------
# Delete a uniformly chosen non-isolated vertex.  On a path this is exactly
# the peak-set/local-maximum statistic of a uniform vertex ordering.


def simulate_active_vertex_path(order: tuple[int, ...], n: int) -> frozenset[int]:
    alive = set(range(n))
    for v in order:
        if v not in alive:
            continue
        if (v - 1 in alive) or (v + 1 in alive):
            alive.remove(v)
    return frozenset(alive)


def path_local_maxima(order: tuple[int, ...]) -> frozenset[int]:
    rank = {v: i for i, v in enumerate(order)}
    n = len(order)
    return frozenset(
        v
        for v in range(n)
        if (v == 0 or rank[v] > rank[v - 1]) and (v == n - 1 or rank[v] > rank[v + 1])
    )


def verify_graph_peak_transfer() -> None:
    lane = "S01_graph_peaks_KILL"
    f: list[tuple[Fraction, ...]] = [(Fraction(1),), (Fraction(0), Fraction(1))]
    for n in range(2, 10):
        total = defaultdict(int)
        for order in permutations(range(n)):
            endpoint = simulate_active_vertex_path(order, n)
            peaks = path_local_maxima(order)
            check(lane, endpoint == peaks, f"path peak transfer n={n}, order={order}")
            total[len(endpoint)] += 1
        empirical = tuple(Fraction(total[k], factorial(n)) for k in range(max(total) + 1))
        convolution = (Fraction(0),)
        for a in range(n):
            convolution = poly_add(convolution, poly_mul(f[a], f[n - 1 - a]))
        predicted = tuple(x / n for x in convolution)
        check(lane, empirical == predicted, f"Riccati recurrence n={n}")
        expected = sum(Fraction(k) * p for k, p in enumerate(empirical))
        check(lane, expected == Fraction(n + 1, 3), f"mean n={n}")
        f.append(predicted)


# S02 -----------------------------------------------------------------------
# Uniform nonbridge-edge deletion.  On a banana graph this is reverse Kruskal
# with a uniform edge order; hence the random-MST owner is direct.


def banana_graph(lengths: tuple[int, ...]):
    u, v = 0, 1
    next_vertex = 2
    paths = []
    edges = []
    for length in lengths:
        internal = list(range(next_vertex, next_vertex + length - 1))
        next_vertex += length - 1
        vertices = [u, *internal, v]
        path_edges = []
        for a, b in zip(vertices, vertices[1:]):
            edge = tuple(sorted((a, b)))
            edges.append(edge)
            path_edges.append(edge)
        paths.append(tuple(path_edges))
    return next_vertex, tuple(edges), tuple(paths)


def connected(n: int, edges: frozenset[tuple[int, int]]) -> bool:
    if n == 0:
        return True
    seen = {0}
    stack = [0]
    adjacency = [[] for _ in range(n)]
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    while stack:
        a = stack.pop()
        for b in adjacency[a]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return len(seen) == n


def reverse_delete_endpoint(n: int, edges: tuple[tuple[int, int], ...], order: tuple[tuple[int, int], ...]):
    state = frozenset(edges)
    for edge in order:
        trial = state - {edge}
        if connected(n, trial):
            state = trial
    return state


def last_exponential_probability(lengths: tuple[int, ...], i: int) -> Fraction:
    others = [j for j in range(len(lengths)) if j != i]
    ans = Fraction(0)
    for mask in range(1 << len(others)):
        denom = lengths[i]
        parity = 0
        for k, j in enumerate(others):
            if mask >> k & 1:
                denom += lengths[j]
                parity ^= 1
        ans += Fraction((-1) ** parity * lengths[i], denom)
    return ans


def verify_reverse_kruskal_owner() -> None:
    lane = "S02_reverse_Kruskal_KILL"
    for lengths in ((2, 2, 2), (2, 2, 3), (2, 3, 3)):
        n, edges, paths = banana_graph(lengths)
        counts = defaultdict(int)
        for order in permutations(edges):
            endpoint = reverse_delete_endpoint(n, edges, order)
            check(lane, len(endpoint) == n - 1 and connected(n, endpoint), "reverse-delete tree")
            counts[endpoint] += 1
        distribution = {tree: Fraction(count, factorial(len(edges))) for tree, count in counts.items()}
        check(lane, sum(distribution.values()) == 1, "banana mass")
        for survivor, path in enumerate(paths):
            expected_survivor = last_exponential_probability(lengths, survivor)
            observed_survivor = sum(
                p for tree, p in distribution.items() if set(path).issubset(tree)
            )
            check(lane, observed_survivor == expected_survivor, f"PL last path {lengths}, {survivor}")
            per_tree = expected_survivor
            for j, length in enumerate(lengths):
                if j != survivor:
                    per_tree /= length
            for tree, probability in distribution.items():
                if set(path).issubset(tree):
                    check(lane, probability == per_tree, "every-tree banana law")


# S03 -----------------------------------------------------------------------
# Select an induced P3 uniformly and delete its centre.  K_{a,b} projects
# exactly to the OK-Corral cross-death urn.


def p3_center_count_transition(a: int, b: int) -> dict[tuple[int, int], Fraction]:
    total = a * comb(b, 2) + b * comb(a, 2)
    if total == 0:
        return {(a, b): Fraction(1)}
    out = defaultdict(Fraction)
    if a * comb(b, 2):
        out[(a - 1, b)] += Fraction(a * comb(b, 2), total)
    if b * comb(a, 2):
        out[(a, b - 1)] += Fraction(b * comb(a, 2), total)
    return dict(out)


@lru_cache(None)
def p3_center_terminal(a: int, b: int) -> dict[tuple[int, int], Fraction]:
    transitions = p3_center_count_transition(a, b)
    if transitions == {(a, b): Fraction(1)}:
        return transitions
    out = defaultdict(Fraction)
    for state, weight in transitions.items():
        add_dist(out, p3_center_terminal(*state), weight)
    return dict(out)


def verify_ok_corral_transfer() -> None:
    lane = "S03_OK_Corral_KILL"
    for a in range(1, 9):
        for b in range(1, 9):
            transitions = p3_center_count_transition(a, b)
            check(lane, sum(transitions.values()) == 1, "P3 transition mass")
            if a + b > 2:
                denom = a + b - 2
                check(
                    lane,
                    transitions.get((a - 1, b), Fraction(0)) == Fraction(b - 1, denom),
                    f"OK-Corral A-death {a,b}",
                )
                check(
                    lane,
                    transitions.get((a, b - 1), Fraction(0)) == Fraction(a - 1, denom),
                    f"OK-Corral B-death {a,b}",
                )
            terminal = p3_center_terminal(a, b)
            check(lane, sum(terminal.values()) == 1, "OK-Corral terminal mass")
            check(lane, all(x == 0 or y == 0 or (x, y) == (1, 1) for x, y in terminal), "absorbers")


# S04 -----------------------------------------------------------------------
# Uniform source deletion in a DAG.  Its possible histories are precisely the
# linear extensions/topological orders, a direct classical owner.


def is_topological(order: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> bool:
    rank = {v: i for i, v in enumerate(order)}
    return all(rank[a] < rank[b] for a, b in edges)


@lru_cache(None)
def source_histories(vertices: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> int:
    if not vertices:
        return 1
    incoming = {v: 0 for v in vertices}
    for a, b in edges:
        if a in incoming and b in incoming:
            incoming[b] += 1
    sources = [v for v in vertices if incoming[v] == 0]
    total = 0
    for source in sources:
        new_vertices = tuple(v for v in vertices if v != source)
        new_edges = tuple(e for e in edges if source not in e)
        total += source_histories(new_vertices, new_edges)
    return total


def verify_source_linear_extension_owner() -> None:
    lane = "S04_linear_extensions_KILL"
    for n in range(1, 6):
        potential = tuple(combinations(range(n), 2))
        for mask in range(1 << len(potential)):
            edges = tuple(potential[i] for i in range(len(potential)) if mask >> i & 1)
            brute = 0
            for order in permutations(range(n)):
                valid = is_topological(order, edges)
                brute += valid
                check(lane, valid == all(order.index(a) < order.index(b) for a, b in edges), "topological support")
            check(lane, brute == source_histories(tuple(range(n)), edges), "linear-extension recurrence")


# S05 -----------------------------------------------------------------------
# Uniform Young-diagram corner deletion: history support/count is standard
# tableaux, and the hook-length formula owns the count.


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def corners(shape: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(i for i, row in enumerate(shape) if i == len(shape) - 1 or shape[i + 1] < row)


def remove_corner(shape: tuple[int, ...], row: int) -> tuple[int, ...]:
    out = list(shape)
    out[row] -= 1
    if out[row] == 0:
        out.pop(row)
    return tuple(out)


@lru_cache(None)
def corner_histories(shape: tuple[int, ...]) -> int:
    if not shape:
        return 1
    return sum(corner_histories(remove_corner(shape, row)) for row in corners(shape))


def hook_tableau_count(shape: tuple[int, ...]) -> int:
    n = sum(shape)
    product = 1
    for i, row in enumerate(shape):
        for j in range(row):
            below = sum(1 for lower in shape[i + 1 :] if lower > j)
            product *= row - j + below
    return factorial(n) // product


def verify_young_hook_owner() -> None:
    lane = "S05_hook_length_KILL"
    for n in range(13):
        for shape in partitions(n):
            check(lane, corner_histories(shape) == hook_tableau_count(shape), f"hook owner {shape}")
            for row in corners(shape):
                child = remove_corner(shape, row)
                check(lane, sum(child) == n - 1, "corner decrement")


# S06 -----------------------------------------------------------------------
# Cycle erosion: delete a uniform active element from a nontrivial permutation
# cycle and shortcut it.  The endpoint is independent uniform survivors, so the
# residual is only a random-order/exponential-race wrapper.


@lru_cache(None)
def cycle_erosion_terminal(cycles: tuple[tuple[int, ...], ...]):
    active = [v for cycle in cycles if len(cycle) > 1 for v in cycle]
    if not active:
        return {tuple(cycle[0] for cycle in cycles): Fraction(1)}
    out = defaultdict(Fraction)
    for v in active:
        new_cycles = []
        for cycle in cycles:
            if v in cycle:
                new_cycles.append(tuple(x for x in cycle if x != v))
            else:
                new_cycles.append(cycle)
        add_dist(out, cycle_erosion_terminal(tuple(new_cycles)), Fraction(1, len(active)))
    return dict(out)


def verify_cycle_erosion_wrapper() -> None:
    lane = "S06_cycle_erosion_KILL"
    for lengths in ((2,), (3,), (2, 2), (2, 3), (3, 3), (2, 3, 4)):
        cycles = []
        label = 0
        for length in lengths:
            cycles.append(tuple(range(label, label + length)))
            label += length
        distribution = cycle_erosion_terminal(tuple(cycles))
        expected_mass = Fraction(1)
        for length in lengths:
            expected_mass /= length
        check(lane, sum(distribution.values()) == 1, "cycle terminal mass")
        check(lane, len(distribution) == __import__("math").prod(lengths), "cycle endpoint count")
        for probability in distribution.values():
            check(lane, probability == expected_mass, "independent uniform survivor")


# S07 -----------------------------------------------------------------------
# Select a comparable lower/upper pair in a complete height-two poset and
# fair-delete one endpoint: a negative-binomial stopping law.


@lru_cache(None)
def fair_pair_terminal(a: int, b: int):
    if a == 0 or b == 0:
        return {(a, b): Fraction(1)}
    out = defaultdict(Fraction)
    add_dist(out, fair_pair_terminal(a - 1, b), Fraction(1, 2))
    add_dist(out, fair_pair_terminal(a, b - 1), Fraction(1, 2))
    return dict(out)


def verify_negative_binomial_wrapper() -> None:
    lane = "S07_negative_binomial_KILL"
    for a in range(1, 10):
        for b in range(1, 10):
            distribution = fair_pair_terminal(a, b)
            check(lane, sum(distribution.values()) == 1, "pair-elimination mass")
            for s in range(1, a + 1):
                length = b + (a - s)
                expected = Fraction(comb(length - 1, b - 1), 2**length)
                check(lane, distribution.get((s, 0), 0) == expected, "lower survivor law")
            for s in range(1, b + 1):
                length = a + (b - s)
                expected = Fraction(comb(length - 1, a - 1), 2**length)
                check(lane, distribution.get((0, s), 0) == expected, "upper survivor law")


# S08 -----------------------------------------------------------------------
# Choose a conflicting pair of edges uniformly and fair-delete one edge.  On
# K_{2,n}, reachable states lump to (x,y,z): double columns, A-only columns,
# B-only columns.  This is a surviving candidate.


def edge_conflicts(state: frozenset[tuple[int, int]]):
    return tuple((a, b) for a, b in combinations(sorted(state), 2) if a[0] == b[0] or a[1] == b[1])


@lru_cache(None)
def conflict_terminal(state: frozenset[tuple[int, int]]):
    conflicts = edge_conflicts(state)
    if not conflicts:
        return {state: Fraction(1)}
    out = defaultdict(Fraction)
    weight = Fraction(1, 2 * len(conflicts))
    for e, f in conflicts:
        add_dist(out, conflict_terminal(state - {e}), weight)
        add_dist(out, conflict_terminal(state - {f}), weight)
    return dict(out)


@lru_cache(None)
def conflict_size_two_probability(x: int, y: int, z: int) -> Fraction:
    conflicts = comb(x + y, 2) + comb(x + z, 2) + x
    if conflicts == 0:
        return Fraction(int(y + z == 2))
    denom = 2 * conflicts
    ans = Fraction(0)
    if x:
        ans += Fraction(x * (x + y), denom) * conflict_size_two_probability(x - 1, y, z + 1)
        ans += Fraction(x * (x + z), denom) * conflict_size_two_probability(x - 1, y + 1, z)
    if y and x + y - 1:
        ans += Fraction(y * (x + y - 1), denom) * conflict_size_two_probability(x, y - 1, z)
    if z and x + z - 1:
        ans += Fraction(z * (x + z - 1), denom) * conflict_size_two_probability(x, y, z - 1)
    return ans


def representative_conflict_state(x: int, y: int, z: int) -> frozenset[tuple[int, int]]:
    edges = set()
    column = 0
    for _ in range(x):
        edges.add((0, column))
        edges.add((1, column))
        column += 1
    for _ in range(y):
        edges.add((0, column))
        column += 1
    for _ in range(z):
        edges.add((1, column))
        column += 1
    return frozenset(edges)


def conflict_overlap_potential(a: int, b: int, x: int) -> Fraction:
    """Intersection density for the two occupied rows of L(K_{2,n})."""
    return Fraction(x, a * b)


def conflict_overlap_drift(a: int, b: int, x: int) -> Fraction:
    """One-step drift before either row has reached size one."""
    denominator = a * (a - 1) + b * (b - 1) + 2 * x
    current = conflict_overlap_potential(a, b, x)
    future = Fraction(0)
    if x:
        future += Fraction(x * a, denominator) * conflict_overlap_potential(a - 1, b, x - 1)
        future += Fraction(x * b, denominator) * conflict_overlap_potential(a, b - 1, x - 1)
    if a > x:
        future += Fraction((a - x) * (a - 1), denominator) * conflict_overlap_potential(a - 1, b, x)
    if b > x:
        future += Fraction((b - x) * (b - 1), denominator) * conflict_overlap_potential(a, b - 1, x)
    return future - current


@lru_cache(None)
def conflict_singleton_boundary_failure(b: int) -> Fraction:
    """Failure probability from one overlapping singleton versus a b-set."""
    if b == 1:
        return Fraction(1)
    denominator = b * (b - 1) + 2
    return (
        1 + (b - 1) ** 2 * conflict_singleton_boundary_failure(b - 1)
    ) / denominator


def verify_conflict_candidate() -> None:
    lane = "S08_annihilation_DIRECT_OWNER_KILL"
    for columns in range(1, 7):
        for x in range(columns + 1):
            for y in range(columns - x + 1):
                for z in range(columns - x - y + 1):
                    state = representative_conflict_state(x, y, z)
                    distribution = conflict_terminal(state)
                    observed = sum(p for endpoint, p in distribution.items() if len(endpoint) == 2)
                    expected = conflict_size_two_probability(x, y, z)
                    check(lane, sum(distribution.values()) == 1, "conflict terminal mass")
                    check(lane, observed == expected, f"strong lumping {(x,y,z)}")
                    check(lane, all(len(endpoint) <= 2 for endpoint in distribution), "matching absorber")
        start = frozenset((row, column) for row in (0, 1) for column in range(columns))
        distribution = conflict_terminal(start)
        p2 = conflict_size_two_probability(columns, 0, 0)
        check(lane, sum(p for endpoint, p in distribution.items() if len(endpoint) == 2) == p2, "p_n")
        size_two = [endpoint for endpoint in distribution if len(endpoint) == 2]
        size_one = [endpoint for endpoint in distribution if len(endpoint) == 1]
        check(lane, len(size_two) == columns * (columns - 1), "size-two support")
        check(lane, len(size_one) == 2 * columns, "size-one support")
        for endpoint in size_two:
            check(lane, distribution[endpoint] == p2 / (columns * (columns - 1)), "uniform 2-matching")
        for endpoint in size_one:
            check(lane, distribution[endpoint] == (1 - p2) / (2 * columns), "uniform 1-matching")

    # The overlap density x/(ab) is a supermartingale until the first row
    # becomes a singleton.  This is the analytic input for q_n <= H_n/n.
    for a in range(2, 31):
        for b in range(2, 31):
            for x in range(min(a, b) + 1):
                drift = conflict_overlap_drift(a, b, x)
                check(lane, drift <= 0, f"overlap supermartingale {(a,b,x)}")

    harmonic = Fraction(1)
    previous_r = Fraction(1)
    for b in range(2, 121):
        harmonic += Fraction(1, b)
        boundary = conflict_singleton_boundary_failure(b)
        r_value = b * boundary
        check(
            lane,
            r_value == previous_r + Fraction(b - 2 * previous_r, b * (b - 1) + 2),
            f"singleton transformed recurrence b={b}",
        )
        check(lane, r_value <= harmonic, f"singleton harmonic upper bound b={b}")
        previous_r = r_value

    harmonic = Fraction(0)
    for columns in range(1, 21):
        harmonic += Fraction(1, columns)
        failure = 1 - conflict_size_two_probability(columns, 0, 0)
        check(lane, failure <= harmonic / columns, f"q_n harmonic bound n={columns}")
        # e < 3 turns the proved e^{-6}/n lower bound into an exact rational
        # regression inequality.
        check(lane, failure >= Fraction(1, 729 * columns), f"q_n rational lower bound n={columns}")


# S09 -----------------------------------------------------------------------
# Select a triangle uniformly and one of its three edges uniformly, then delete
# that edge.  The book graph has a shared-spine catastrophe and an exact full
# endpoint/clock law.  This is the strongest surviving candidate.


def graph_triangles(state: frozenset[tuple[int, int]]):
    vertices = sorted({v for edge in state for v in edge})
    out = []
    for triple in combinations(vertices, 3):
        edges = tuple(tuple(sorted(edge)) for edge in combinations(triple, 2))
        if all(edge in state for edge in edges):
            out.append(edges)
    return tuple(out)


@lru_cache(None)
def triangle_edge_terminal(state: frozenset[tuple[int, int]]):
    triangles = graph_triangles(state)
    if not triangles:
        return {(state, 0): Fraction(1)}
    out = defaultdict(Fraction)
    weight = Fraction(1, 3 * len(triangles))
    for triangle in triangles:
        for edge in triangle:
            for (endpoint, clock), probability in triangle_edge_terminal(state - {edge}).items():
                out[(endpoint, clock + 1)] += weight * probability
    return dict(out)


def book_edges(r: int):
    spine = (0, 1)
    pages = []
    edges = {spine}
    for i in range(r):
        a = (0, i + 2)
        b = (1, i + 2)
        pages.append((a, b))
        edges.update((a, b))
    return spine, tuple(pages), frozenset(edges)


def expected_book_endpoint(r: int):
    spine, pages, start = book_edges(r)
    out = {}
    # Spine deleted after exactly s already resolved pages.
    for s in range(r):
        for resolved in combinations(range(r), s):
            for side_bits in range(1 << s):
                deleted = {spine}
                for j, page_index in enumerate(resolved):
                    deleted.add(pages[page_index][side_bits >> j & 1])
                out[start - deleted] = Fraction(1, 3 ** (s + 1) * comb(r, s))
    # Spine retained; every page has exactly one side deleted.
    for side_bits in range(1 << r):
        deleted = {pages[i][side_bits >> i & 1] for i in range(r)}
        out[start - deleted] = Fraction(1, 3**r)
    return out


def verify_triangle_book_candidate() -> None:
    lane = "S09_triangle_book_INTERNAL_P136_KILL"
    for r in range(1, 8):
        _spine, _pages, start = book_edges(r)
        joint = triangle_edge_terminal(start)
        endpoint = defaultdict(Fraction)
        clock = defaultdict(Fraction)
        for (state, steps), probability in joint.items():
            endpoint[state] += probability
            clock[steps] += probability
        expected = expected_book_endpoint(r)
        check(lane, sum(endpoint.values()) == 1, "book endpoint mass")
        check(lane, sum(clock.values()) == 1, "book clock mass")
        check(lane, len(endpoint) == 3**r, "book endpoint count")
        check(lane, endpoint == expected, f"every-target book law r={r}")
        for state, probability in expected.items():
            check(lane, endpoint[state] == probability, "book target probability")
        for t in range(1, r):
            check(lane, clock[t] == Fraction(2, 3) ** (t - 1) / 3, "truncated geometric interior")
        check(lane, clock[r] == Fraction(2, 3) ** (r - 1), "truncated geometric endpoint")


# S10 -----------------------------------------------------------------------
# Uniform simplicial-vertex deletion on a windmill of clique blocks.  The
# process is exactly the terminal monochromatic run of a uniform permutation,
# leaving only an owner-thin PEO/random-scan wrapper.


@lru_cache(None)
def windmill_terminal(blocks: tuple[tuple[int, ...], ...]):
    active = [block for block in blocks if block]
    if len(active) <= 1:
        endpoint = active[0] if active else ()
        return {endpoint: Fraction(1)}
    vertices = [v for block in blocks for v in block]
    out = defaultdict(Fraction)
    for v in vertices:
        new_blocks = tuple(tuple(x for x in block if x != v) for block in blocks)
        add_dist(out, windmill_terminal(new_blocks), Fraction(1, len(vertices)))
    return dict(out)


def verify_simplicial_wrapper() -> None:
    lane = "S10_simplicial_PEO_KILL"
    for sizes in ((1, 1), (2, 1), (2, 2), (3, 2), (2, 3, 1), (3, 3, 2)):
        blocks = []
        label = 0
        for size in sizes:
            blocks.append(tuple(range(label, label + size)))
            label += size
        distribution = windmill_terminal(tuple(blocks))
        total = sum(sizes)
        check(lane, sum(distribution.values()) == 1, "windmill mass")
        for i, block in enumerate(blocks):
            other = total - len(block)
            for s in range(1, len(block) + 1):
                for subset in combinations(block, s):
                    expected = Fraction(factorial(s) * factorial(total - s - 1) * other, factorial(total))
                    check(lane, distribution.get(tuple(subset), 0) == expected, "terminal-run target")
            winner = sum(p for endpoint, p in distribution.items() if endpoint and endpoint[0] in block)
            check(lane, winner == Fraction(len(block), total), "winner identifies block size")


# R11 -----------------------------------------------------------------------
# Simple random walk from the centre of a finite spider, with all leaves
# absorbing.  Unequal arm lengths produce a leaf-marked Chebyshev transform,
# exact moments, sharp fixed-mass extrema, and a parameter inverse.


@lru_cache(None)
def spider_continuant(length: int) -> tuple[Fraction, ...]:
    """P_l(z)=z^(l-1) U_(l-1)(1/z), with P_0=0."""
    if length == 0:
        return (Fraction(0),)
    if length == 1:
        return (Fraction(1),)
    if length == 2:
        return (Fraction(2),)
    return poly_add(
        poly_scale(spider_continuant(length - 1), 2),
        poly_scale(poly_shift(spider_continuant(length - 2), 2), -1),
    )


def spider_transform(arms: tuple[int, ...]):
    factors = tuple(spider_continuant(length) for length in arms)
    full_product = (Fraction(1),)
    for factor in factors:
        full_product = poly_mul(full_product, factor)
    denominator = poly_scale(full_product, len(arms))
    numerators = []
    for i, length in enumerate(arms):
        other_product = (Fraction(1),)
        for j, factor in enumerate(factors):
            if i != j:
                other_product = poly_mul(other_product, factor)
        numerators.append(poly_shift(other_product, length))
        failed_excursion = poly_shift(
            poly_mul(spider_continuant(length - 1), other_product), 2
        )
        denominator = poly_add(denominator, poly_scale(failed_excursion, -1))
    return denominator, tuple(numerators)


def rational_series(
    numerator: tuple[Fraction, ...], denominator: tuple[Fraction, ...], horizon: int
) -> tuple[Fraction, ...]:
    out = []
    for degree in range(horizon + 1):
        residual = numerator[degree] if degree < len(numerator) else Fraction(0)
        for j in range(1, min(degree, len(denominator) - 1) + 1):
            residual -= denominator[j] * out[degree - j]
        out.append(residual / denominator[0])
    return tuple(out)


def spider_first_passage_dp(arms: tuple[int, ...], horizon: int):
    transient = {(-1, 0): Fraction(1)}
    endpoint = [[Fraction(0)] * (horizon + 1) for _ in arms]
    for time in range(1, horizon + 1):
        new_transient = defaultdict(Fraction)
        for (arm, position), probability in transient.items():
            if arm == -1:
                for i, length in enumerate(arms):
                    step_probability = probability / len(arms)
                    if length == 1:
                        endpoint[i][time] += step_probability
                    else:
                        new_transient[i, 1] += step_probability
                continue
            length = arms[arm]
            if position == 1:
                new_transient[-1, 0] += probability / 2
            else:
                new_transient[arm, position - 1] += probability / 2
            if position + 1 == length:
                endpoint[arm][time] += probability / 2
            else:
                new_transient[arm, position + 1] += probability / 2
        transient = dict(new_transient)
    return tuple(tuple(row) for row in endpoint)


def verify_spider_absorption_replacement() -> None:
    lane = "R11_finite_spider_absorption_PASS_OWNER_THIN"
    for number_of_arms in range(1, 5):
        for arms in product(range(1, 5), repeat=number_of_arms):
            horizon = 2 * sum(arms) + 12
            denominator, numerators = spider_transform(arms)
            dynamic = spider_first_passage_dp(arms, horizon)
            formula = tuple(rational_series(numerator, denominator, horizon) for numerator in numerators)
            for i, length in enumerate(arms):
                for time in range(horizon + 1):
                    check(lane, dynamic[i][time] == formula[i][time], f"spider PGF {arms}, arm={i}, t={time}")
                    if (time - length) % 2:
                        check(lane, formula[i][time] == 0, f"spider parity {arms}, arm={i}, t={time}")
                check(
                    lane,
                    formula[i][length] == Fraction(1, number_of_arms * 2 ** (length - 1)),
                    f"spider first atom {arms}, arm={i}",
                )

            total_numerator = (Fraction(0),)
            for numerator in numerators:
                total_numerator = poly_add(total_numerator, numerator)
            d0 = poly_derivative_at_one(denominator, 0)
            d1 = poly_derivative_at_one(denominator, 1)
            d2 = poly_derivative_at_one(denominator, 2)
            n0 = poly_derivative_at_one(total_numerator, 0)
            n1 = poly_derivative_at_one(total_numerator, 1)
            n2 = poly_derivative_at_one(total_numerator, 2)
            total_mass = n0 / d0
            mean_from_transform = (n1 - d1 * total_mass) / d0
            factorial_second = (n2 - 2 * d1 * mean_from_transform - d2 * total_mass) / d0
            variance_from_transform = factorial_second + mean_from_transform - mean_from_transform**2

            conductance = sum((Fraction(1, length) for length in arms), Fraction(0))
            total_length = sum(arms)
            cubic_sum = sum(length**3 for length in arms)
            mean_formula = Fraction(total_length) / conductance
            variance_formula = (
                Fraction(cubic_sum - 2 * total_length, 3) / conductance
                + Fraction(total_length**2, 3) / conductance**2
            )
            check(lane, total_mass == 1, f"spider transform normalization {arms}")
            check(lane, mean_from_transform == mean_formula, f"spider mean {arms}")
            check(lane, variance_from_transform == variance_formula, f"spider variance {arms}")

            endpoint_probabilities = tuple(Fraction(1, length) / conductance for length in arms)
            for i, probability in enumerate(endpoint_probabilities):
                check(
                    lane,
                    poly_derivative_at_one(numerators[i], 0) / d0 == probability,
                    f"spider harmonic endpoint {arms}, arm={i}",
                )

            common_divisor = 0
            for length in arms:
                common_divisor = gcd(common_divisor, length)
            primitive = tuple(length // common_divisor for length in arms)
            inverse_products = tuple(
                endpoint_probabilities[i] * primitive[i] for i in range(number_of_arms)
            )
            check(lane, len(set(inverse_products)) == 1, f"endpoint ratio inverse {arms}")
            primitive_conductance = sum((Fraction(1, length) for length in primitive), Fraction(0))
            primitive_mean = Fraction(sum(primitive)) / primitive_conductance
            check(
                lane,
                mean_formula / primitive_mean == common_divisor**2,
                f"endpoint plus mean scale inverse {arms}",
            )

            quotient, remainder = divmod(total_length, number_of_arms)
            maximum_conductance = Fraction(number_of_arms - 1) + Fraction(
                1, total_length - number_of_arms + 1
            )
            minimum_conductance = Fraction(number_of_arms - remainder, quotient)
            if remainder:
                minimum_conductance += Fraction(remainder, quotient + 1)
            lower_mean = Fraction(total_length) / maximum_conductance
            upper_mean = Fraction(total_length) / minimum_conductance
            is_extreme = sorted(arms) == [1] * (number_of_arms - 1) + [
                total_length - number_of_arms + 1
            ]
            is_balanced = max(arms) - min(arms) <= 1
            check(lane, mean_formula >= lower_mean, f"spider sharp lower mean {arms}")
            check(lane, (mean_formula == lower_mean) == is_extreme, f"spider lower equality {arms}")
            check(lane, mean_formula <= upper_mean, f"spider sharp upper mean {arms}")
            check(lane, (mean_formula == upper_mean) == is_balanced, f"spider upper equality {arms}")


# R12 -----------------------------------------------------------------------
# Choose an inversion of a permutation uniformly and swap its two entries.
# The exact clock is interesting but the process is a random-sorting control.


def inversion_pairs(permutation: tuple[int, ...]):
    return tuple(
        (i, j)
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
        if permutation[i] > permutation[j]
    )


@lru_cache(None)
def inversion_swap_clock(permutation: tuple[int, ...]):
    inversions = inversion_pairs(permutation)
    if not inversions:
        return {0: Fraction(1)}
    out = defaultdict(Fraction)
    for i, j in inversions:
        successor = list(permutation)
        successor[i], successor[j] = successor[j], successor[i]
        for clock, probability in inversion_swap_clock(tuple(successor)).items():
            out[clock + 1] += probability / len(inversions)
    return dict(out)


def permutation_cycle_count(permutation: tuple[int, ...]) -> int:
    seen = set()
    cycles = 0
    for start in range(len(permutation)):
        if start in seen:
            continue
        cycles += 1
        vertex = start
        while vertex not in seen:
            seen.add(vertex)
            vertex = permutation[vertex]
    return cycles


def verify_random_inversion_sort_control() -> None:
    lane = "R12_random_inversion_sort_FIREWALL_KILL"
    for n in range(1, 8):
        for permutation in permutations(range(n)):
            inversions = inversion_pairs(permutation)
            distribution = inversion_swap_clock(permutation)
            check(lane, sum(distribution.values()) == 1, f"inversion clock mass {permutation}")
            check(
                lane,
                min(distribution) == n - permutation_cycle_count(permutation),
                f"inversion minimum clock {permutation}",
            )
            check(lane, max(distribution) == len(inversions), f"inversion maximum clock {permutation}")
            for i, j in inversions:
                successor = list(permutation)
                successor[i], successor[j] = successor[j], successor[i]
                decrement = len(inversions) - len(inversion_pairs(tuple(successor)))
                check(lane, decrement > 0 and decrement % 2 == 1, "odd strict inversion descent")


# R13 -----------------------------------------------------------------------
# Swap a uniform occupied/unoccupied label in a k-subset.  This is exactly the
# Bernoulli--Laplace/Johnson walk and is retained only as a direct-owner control.


def verify_bernoulli_laplace_control() -> None:
    lane = "R13_Bernoulli_Laplace_DIRECT_OWNER_KILL"
    for n in range(2, 12):
        for k in range(1, n // 2 + 1):
            states = tuple(combinations(range(n), k))
            start = states[0]
            probabilities = {start: Fraction(1)}
            degree = k * (n - k)
            for time in range(7):
                spectral_return = Fraction(0)
                for j in range(min(k, n - k) + 1):
                    multiplicity = comb(n, j) - (comb(n, j - 1) if j else 0)
                    eigenvalue = 1 - Fraction(j * (n - j + 1), degree)
                    spectral_return += multiplicity * eigenvalue**time
                spectral_return /= comb(n, k)
                check(
                    lane,
                    probabilities.get(start, 0) == spectral_return,
                    f"Johnson return n={n}, k={k}, t={time}",
                )
                check(lane, sum(probabilities.values()) == 1, "Johnson mass")
                if time == 6:
                    break
                next_probabilities = defaultdict(Fraction)
                for state, probability in probabilities.items():
                    occupied = set(state)
                    for leaving in state:
                        for entering in range(n):
                            if entering in occupied:
                                continue
                            successor = tuple(sorted((occupied - {leaving}) | {entering}))
                            next_probabilities[successor] += probability / degree
                probabilities = dict(next_probabilities)

            multiplicity_sum = sum(
                comb(n, j) - (comb(n, j - 1) if j else 0)
                for j in range(min(k, n - k) + 1)
            )
            check(lane, multiplicity_sum == comb(n, k), "Johnson spectral multiplicities")


# R14 -----------------------------------------------------------------------
# Fair randomized halving: an even integer is halved; an odd integer is sent
# equiprobably to its two integer halves.  Stop at one.  The exact clock has
# only the two atoms bracketing log_2(n).  This attractive identity is retained
# as a negative control because it is a one-scalar digit-contraction law, too
# close in mechanism/proof to the occupied digit-erasure/synchronization lane.


def trim_polynomial(a: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    a = tuple(a)
    while len(a) > 1 and a[-1] == 0:
        a = a[:-1]
    return a


@lru_cache(None)
def fair_halving_clock(n: int) -> tuple[Fraction, ...]:
    if n == 1:
        return (Fraction(1),)
    if n % 2 == 0:
        return trim_polynomial(poly_shift(fair_halving_clock(n // 2), 1))
    lower = fair_halving_clock(n // 2)
    upper = fair_halving_clock(n // 2 + 1)
    return trim_polynomial(poly_shift(poly_scale(poly_add(lower, upper), Fraction(1, 2)), 1))


def verify_fair_halving_control() -> None:
    lane = "R14_fair_halving_INTERNAL_DIGIT_KILL"
    seen: dict[tuple[Fraction, ...], int] = {}
    for n in range(1, 1 << 16):
        distribution = fair_halving_clock(n)
        check(lane, sum(distribution, Fraction(0)) == 1, f"halving mass n={n}")
        if n == 1:
            predicted = (Fraction(1),)
            mean = Fraction(0)
            variance = Fraction(0)
        else:
            k = n.bit_length() - 1
            upper_probability = Fraction(n - (1 << k), 1 << k)
            predicted_list = [Fraction(0)] * (k + 2)
            predicted_list[k] = 1 - upper_probability
            predicted_list[k + 1] = upper_probability
            predicted = trim_polynomial(tuple(predicted_list))
            mean = Fraction(k) + upper_probability
            variance = upper_probability * (1 - upper_probability)
        check(lane, distribution == predicted, f"two-atom halving law n={n}")
        first_moment = poly_derivative_at_one(distribution, 1)
        second_factorial = poly_derivative_at_one(distribution, 2)
        check(lane, first_moment == mean, f"halving mean n={n}")
        check(
            lane,
            second_factorial + first_moment - first_moment**2 == variance,
            f"halving variance n={n}",
        )
        check(lane, distribution not in seen, f"halving inverse collision n={n}")
        seen[distribution] = n


# R15 -----------------------------------------------------------------------
# From n>1 choose phi(n) or n/rad(n) with equal probability.  Both branches
# strictly descend, but the complete clock is non-identifying already on the
# infinite family p and 2p (p odd prime).  The literal arithmetic recursion is
# kept as a no-inverse/no-second-axis negative control.


@lru_cache(None)
def prime_factorization(n: int) -> tuple[tuple[int, int], ...]:
    factors = []
    divisor = 2
    remaining = n
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 1
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def euler_phi(n: int) -> int:
    value = n
    for prime, _ in prime_factorization(n):
        value = value // prime * (prime - 1)
    return value


def radical(n: int) -> int:
    value = 1
    for prime, _ in prime_factorization(n):
        value *= prime
    return value


@lru_cache(None)
def totient_radical_clock(n: int) -> tuple[Fraction, ...]:
    if n == 1:
        return (Fraction(1),)
    left = totient_radical_clock(euler_phi(n))
    right = totient_radical_clock(n // radical(n))
    return trim_polynomial(poly_shift(poly_scale(poly_add(left, right), Fraction(1, 2)), 1))


def verify_totient_radical_control() -> None:
    lane = "R15_totient_radical_NO_INVERSE_KILL"
    collisions = 0
    seen: dict[tuple[Fraction, ...], int] = {}
    for n in range(1, 5001):
        distribution = totient_radical_clock(n)
        check(lane, sum(distribution, Fraction(0)) == 1, f"totient-radical mass n={n}")
        if n > 1:
            check(lane, 1 <= euler_phi(n) < n, f"totient descent n={n}")
            check(lane, 1 <= n // radical(n) < n, f"radical quotient descent n={n}")
        if distribution in seen:
            collisions += 1
        else:
            seen[distribution] = n
        factors = prime_factorization(n)
        if n > 2 and len(factors) == 1 and factors[0][1] == 1:
            check(
                lane,
                totient_radical_clock(n) == totient_radical_clock(2 * n),
                f"prime doubling blindness p={n}",
            )
    check(lane, collisions >= 2500, "totient-radical collision pressure")


# R16 -----------------------------------------------------------------------
# For a characteristic-zero polynomial with fixed labelled irreducible roots,
# encode multiplicities by e.  Choose gcd(f,f') (e -> (e-1)_+) or the
# squarefree kernel (positive e -> 1) fairly, and stop at 1.  The law depends
# only on max(e), so the polynomial carrier supplies no useful inverse axis.


def derivative_gcd_exponents(state: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(max(0, exponent - 1) for exponent in state)


def squarefree_exponents(state: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(1 if exponent else 0 for exponent in state)


def multiplicity_mean(maximum: int) -> Fraction:
    if maximum == 0:
        return Fraction(0)
    return Fraction(4) - Fraction(4, 1 << maximum)


def verify_random_squarefree_control() -> None:
    lane = "R16_random_squarefree_MAX_ONLY_KILL"
    for number_of_factors in range(1, 5):
        for state in product(range(1, 7), repeat=number_of_factors):
            maximum = max(state)
            expected = multiplicity_mean(maximum)
            left = derivative_gcd_exponents(state)
            right = squarefree_exponents(state)
            bellman = 1 + Fraction(1, 2) * multiplicity_mean(max(left)) + Fraction(
                1, 2
            ) * multiplicity_mean(max(right))
            check(lane, expected == bellman, f"multiplicity mean Bellman {state}")

            actual = {state: Fraction(1)}
            scalar = {maximum: Fraction(1)}
            for time in range(17):
                actual_maxima = defaultdict(Fraction)
                for profile, probability in actual.items():
                    actual_maxima[max(profile)] += probability
                check(lane, dict(actual_maxima) == scalar, f"max-only law {state}, t={time}")
                check(lane, sum(actual.values(), Fraction(0)) == 1, "multiplicity mass")
                next_actual = defaultdict(Fraction)
                for profile, probability in actual.items():
                    if max(profile) == 0:
                        next_actual[profile] += probability
                    else:
                        next_actual[derivative_gcd_exponents(profile)] += probability / 2
                        next_actual[squarefree_exponents(profile)] += probability / 2
                next_scalar = defaultdict(Fraction)
                for value, probability in scalar.items():
                    if value == 0:
                        next_scalar[0] += probability
                    else:
                        next_scalar[value - 1] += probability / 2
                        next_scalar[1] += probability / 2
                actual = dict(next_actual)
                scalar = dict(next_scalar)


# R17 -----------------------------------------------------------------------
# Resolve every crossing of the closed positive two-braid independently by
# the two Temperley--Lieb smoothings.  Sequentially choosing unresolved
# crossings is only a random-order presentation of the Kauffman state sum.


def two_braid_smoothing_loops(resolutions: tuple[int, ...]) -> int:
    diagram = 0  # 0 is the identity tangle, 1 is the cup-cap generator.
    internal_loops = 0
    for resolution in resolutions:
        if resolution == 0:
            continue
        if diagram == 0:
            diagram = 1
        else:
            internal_loops += 1
    closure_loops = 2 if diagram == 0 else 1
    return internal_loops + closure_loops


def verify_random_kauffman_control() -> None:
    lane = "R17_random_Kauffman_state_sum_DIRECT_KILL"
    for crossings in range(1, 17):
        counts = defaultdict(int)
        for resolutions in product((0, 1), repeat=crossings):
            loops = two_braid_smoothing_loops(resolutions)
            number_of_one_smoothings = sum(resolutions)
            predicted_loops = 2 if number_of_one_smoothings == 0 else number_of_one_smoothings
            check(lane, loops == predicted_loops, f"TL2 loops n={crossings}, state={resolutions}")
            counts[loops] += 1
        check(lane, sum(counts.values()) == 1 << crossings, f"Kauffman state mass n={crossings}")
        for loops, count in counts.items():
            predicted_count = comb(crossings, loops)
            if loops == 2:
                predicted_count += 1
            check(lane, count == predicted_count, f"Kauffman loop law n={crossings}, L={loops}")
        expected_loops = sum(Fraction(loops * count, 1 << crossings) for loops, count in counts.items())
        check(
            lane,
            expected_loops == Fraction(crossings, 2) + Fraction(2, 1 << crossings),
            f"Kauffman mean loops n={crossings}",
        )


def main() -> None:
    verify_graph_peak_transfer()
    verify_reverse_kruskal_owner()
    verify_ok_corral_transfer()
    verify_source_linear_extension_owner()
    verify_young_hook_owner()
    verify_cycle_erosion_wrapper()
    verify_negative_binomial_wrapper()
    verify_conflict_candidate()
    verify_triangle_book_candidate()
    verify_simplicial_wrapper()
    verify_spider_absorption_replacement()
    verify_random_inversion_sort_control()
    verify_bernoulli_laplace_control()
    verify_fair_halving_control()
    verify_totient_radical_control()
    verify_random_squarefree_control()
    verify_random_kauffman_control()
    print("P147-P151 stochastic Stage-1 exact scout")
    print("literal_systems=17")
    for lane in sorted(LANE_ASSERTIONS):
        print(f"{lane}={LANE_ASSERTIONS[lane]}")
    print(f"exact_assertions={ASSERTIONS}")
    print("selected_signal=R11_finite_spider_absorption")
    print("second_pool_selection=NONE_VALUE_GATE_ENFORCED")
    print("killed_replacements=S08_K2n_annihilation,S09_triangle_book")
    print("external_status=HOLD_EXTERNAL")
    print("PASS")


if __name__ == "__main__":
    main()
