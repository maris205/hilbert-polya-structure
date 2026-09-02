#!/usr/bin/env python3
"""Exact small-carrier probes for the P162--P166 graph/set scout.

This is discovery pressure, not a proof and not novelty evidence.  Every
state space used below is finite and exhaustively traversed; the four named
growth transforms are checked on several seed graphs against their exact
size recurrences.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: str = "") -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label or f"assertion {self.assertions} failed")


A = Audit()


def ceil_log(base: int, n: int) -> int:
    t, power = 0, 1
    while power < n:
        t += 1
        power *= base
    return t


def graph_edges(n: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(n), 2))


def graph_encode(n: int, edge_set) -> int:
    positions = {edge: bit for bit, edge in enumerate(graph_edges(n))}
    code = 0
    for u, v in edge_set:
        if u > v:
            u, v = v, u
        code |= 1 << positions[(u, v)]
    return code


def graph_edge_count(code: int) -> int:
    return code.bit_count()


def graph_push(code: int, n: int, divisor: int, parity: bool = False) -> int:
    positions = {edge: bit for bit, edge in enumerate(graph_edges(n))}
    out = 0
    for bit, (u, v) in enumerate(graph_edges(n)):
        if not (code >> bit) & 1:
            continue
        x, y = u // divisor, v // divisor
        if x == y:
            continue
        edge = (x, y) if x < y else (y, x)
        mask = 1 << positions[edge]
        if parity:
            out ^= mask
        else:
            out |= mask
    return out


def iterate_map(state: int, steps: int, successor) -> int:
    for _ in range(steps):
        state = successor(state)
    return state


def supported_graph_codes(n: int, m: int):
    ambient = graph_edges(n)
    active = [bit for bit, (u, v) in enumerate(ambient) if u < m and v < m]
    for small in range(1 << len(active)):
        code = 0
        for j, bit in enumerate(active):
            if (small >> j) & 1:
                code |= 1 << bit
        yield code


def block_sizes(n: int, divisor: int) -> list[int]:
    m = (n + divisor - 1) // divisor
    return [sum(i // divisor == j for i in range(n)) for j in range(m)]


def bqc_fibre(n: int, divisor: int, target: int) -> int:
    sizes = block_sizes(n, divisor)
    m = len(sizes)
    free = sum(comb(s, 2) for s in sizes)
    answer = 1 << free
    positions = {edge: bit for bit, edge in enumerate(graph_edges(n))}
    for u, v in combinations(range(m), 2):
        if (target >> positions[(u, v)]) & 1:
            answer *= (1 << (sizes[u] * sizes[v])) - 1
    return answer


def probe_bqc() -> str:
    """OR quotient by consecutive binary blocks."""
    start = A.assertions
    n, c = 6, 2
    total = 1 << comb(n, 2)
    counts_by_time = []
    for t in range(1, ceil_log(c, n) + 1):
        direct_divisor = c**t
        counts = Counter()
        for code in range(total):
            iterated = iterate_map(code, t, lambda x: graph_push(x, n, c))
            direct = graph_push(code, n, direct_divisor)
            A.check(iterated == direct, "BQC semigroup law")
            counts[iterated] += 1
        m = (n + direct_divisor - 1) // direct_divisor
        targets = list(supported_graph_codes(n, m))
        A.check(set(counts) == set(targets), "BQC exact image")
        for target in targets:
            A.check(counts[target] == bqc_fibre(n, direct_divisor, target), "BQC fibre")
        counts_by_time.append((len(counts), sorted(Counter(counts.values()).items())))
    h = ceil_log(c, n)
    witness = graph_encode(n, {(0, n - 1)})
    A.check(iterate_map(witness, h - 1, lambda x: graph_push(x, n, c)) != 0, "BQC sharp")
    A.check(iterate_map(witness, h, lambda x: graph_push(x, n, c)) == 0, "BQC clock")
    return (
        f"n=6,c=2,height={h},images={[x[0] for x in counts_by_time]},"
        f"t1_fibres={counts_by_time[0][1]}"
    ) + f"; assertions={A.assertions - start}"


def probe_bpq() -> str:
    """Parity quotient by consecutive binary blocks."""
    start = A.assertions
    n, c = 6, 2
    total = 1 << comb(n, 2)
    image_sizes, spectra = [], []
    for t in range(1, ceil_log(c, n) + 1):
        divisor = c**t
        counts = Counter()
        for code in range(total):
            iterated = iterate_map(code, t, lambda x: graph_push(x, n, c, parity=True))
            direct = graph_push(code, n, divisor, parity=True)
            A.check(iterated == direct, "BPQ semigroup law")
            counts[iterated] += 1
        m = (n + divisor - 1) // divisor
        targets = list(supported_graph_codes(n, m))
        expected = 1 << (comb(n, 2) - comb(m, 2))
        A.check(set(counts) == set(targets), "BPQ exact image")
        for target in targets:
            A.check(counts[target] == expected, "BPQ uniform fibre")
        image_sizes.append(len(counts))
        spectra.append(sorted(Counter(counts.values()).items()))
    return (
        f"n=6,c=2,height={ceil_log(c,n)},images={image_sizes},t1_fibres={spectra[0]}"
        f"; assertions={A.assertions - start}"
    )


def graph_decimate(code: int, n: int, divisor: int) -> int:
    positions = {edge: bit for bit, edge in enumerate(graph_edges(n))}
    out = 0
    for bit, (u, v) in enumerate(graph_edges(n)):
        if (code >> bit) & 1 and u % divisor == 0 and v % divisor == 0:
            out |= 1 << positions[(u // divisor, v // divisor)]
    return out


def probe_evd() -> str:
    """Keep even-labelled vertices, divide labels, and discard every other edge."""
    start = A.assertions
    n, c = 6, 2
    total = 1 << comb(n, 2)
    image_sizes = []
    for t in range(1, ceil_log(c, n) + 1):
        divisor = c**t
        counts = Counter()
        for code in range(total):
            iterated = iterate_map(code, t, lambda x: graph_decimate(x, n, c))
            direct = graph_decimate(code, n, divisor)
            A.check(iterated == direct, "EVD semigroup law")
            counts[iterated] += 1
        m = (n + divisor - 1) // divisor
        targets = list(supported_graph_codes(n, m))
        expected = 1 << (comb(n, 2) - comb(m, 2))
        A.check(set(counts) == set(targets), "EVD exact image")
        for target in targets:
            A.check(counts[target] == expected, "EVD fibre")
        image_sizes.append(len(counts))
    witness = graph_encode(n, {(0, 4)})
    h = ceil_log(c, n)
    A.check(iterate_map(witness, h - 1, lambda x: graph_decimate(x, n, c)) != 0, "EVD sharp")
    A.check(iterate_map(witness, h, lambda x: graph_decimate(x, n, c)) == 0, "EVD clock")
    return f"n=6,c=2,height={h},images={image_sizes}; assertions={A.assertions-start}"


def graph_endpoint_core(code: int, n: int) -> int:
    positions = {edge: bit for bit, edge in enumerate(graph_edges(n))}
    out = 0
    for bit, (u, v) in enumerate(graph_edges(n)):
        if (code >> bit) & 1 and u + 1 < v - 1:
            out |= 1 << positions[(u + 1, v - 1)]
    return out


def graph_endpoint_core_direct(code: int, n: int, t: int) -> int:
    positions = {edge: bit for bit, edge in enumerate(graph_edges(n))}
    out = 0
    for bit, (u, v) in enumerate(graph_edges(n)):
        if (code >> bit) & 1 and u + t < v - t:
            out |= 1 << positions[(u + t, v - t)]
    return out


def probe_ecs() -> str:
    """Strip both endpoints of every ordered chord."""
    start = A.assertions
    n = 6
    total = 1 << comb(n, 2)
    h = (n - 1 + 1) // 2
    images = []
    for t in range(1, h + 1):
        counts = Counter()
        for code in range(total):
            got = iterate_map(code, t, lambda x: graph_endpoint_core(x, n))
            expected = graph_endpoint_core_direct(code, n, t)
            A.check(got == expected, "ECS iterate")
            counts[got] += 1
        active_vertices = max(0, n - 2 * t)
        expected_fibre = 1 << (comb(n, 2) - comb(active_vertices, 2))
        A.check(len(counts) == 1 << comb(active_vertices, 2), "ECS image size")
        for value in counts.values():
            A.check(value == expected_fibre, "ECS uniform fibre")
        images.append(len(counts))
    witness = graph_encode(n, {(0, n - 1)})
    A.check(iterate_map(witness, h - 1, lambda x: graph_endpoint_core(x, n)) != 0, "ECS sharp")
    A.check(iterate_map(witness, h, lambda x: graph_endpoint_core(x, n)) == 0, "ECS clock")
    return f"n=6,height={h},images={images}; assertions={A.assertions-start}"


def graph_right_slide(code: int, n: int) -> int:
    positions = {edge: bit for bit, edge in enumerate(graph_edges(n))}
    out = 0
    for bit, (u, v) in enumerate(graph_edges(n)):
        if (code >> bit) & 1 and v - u >= 2:
            out |= 1 << positions[(u, v - 1)]
    return out


def graph_right_slide_direct(code: int, n: int, t: int) -> int:
    positions = {edge: bit for bit, edge in enumerate(graph_edges(n))}
    out = 0
    for bit, (u, v) in enumerate(graph_edges(n)):
        if (code >> bit) & 1 and v - u > t:
            out |= 1 << positions[(u, v - t)]
    return out


def probe_els() -> str:
    """Slide the right endpoint of each edge left until collision."""
    start = A.assertions
    n, h = 6, 5
    total = 1 << comb(n, 2)
    images = []
    for t in range(1, h + 1):
        counts = Counter()
        for code in range(total):
            got = iterate_map(code, t, lambda x: graph_right_slide(x, n))
            expected = graph_right_slide_direct(code, n, t)
            A.check(got == expected, "ELS iterate")
            counts[got] += 1
        active_vertices = n - t
        expected_image = 1 << comb(active_vertices, 2)
        expected_fibre = 1 << (comb(n, 2) - comb(active_vertices, 2))
        A.check(len(counts) == expected_image, "ELS image")
        for value in counts.values():
            A.check(value == expected_fibre, "ELS fibre")
        images.append(len(counts))
    return f"n=6,height=5,images={images}; assertions={A.assertions-start}"


def subset_quotient(mask: int, n: int, divisor: int) -> int:
    out = 0
    for i in range(n):
        if (mask >> i) & 1:
            out |= 1 << (i // divisor)
    return out


def family_push(code: int, n: int, subset_map, parity: bool = False) -> int:
    out = 0
    for subset in range(1 << n):
        if not (code >> subset) & 1:
            continue
        image = subset_map(subset)
        if parity:
            out ^= 1 << image
        else:
            out |= 1 << image
    return out


def family_targets(m: int):
    yield from range(1 << (1 << m))


def sfc_lift_count(n: int, divisor: int, target_subset: int) -> int:
    sizes = block_sizes(n, divisor)
    result = 1
    for j, size in enumerate(sizes):
        if (target_subset >> j) & 1:
            result *= (1 << size) - 1
    return result


def sfc_fibre(n: int, divisor: int, target_family: int) -> int:
    m = (n + divisor - 1) // divisor
    result = 1
    for target_subset in range(1 << m):
        if (target_family >> target_subset) & 1:
            lifts = sfc_lift_count(n, divisor, target_subset)
            result *= (1 << lifts) - 1
    return result


def probe_sfc() -> str:
    """Direct image of an arbitrary set family under binary label coalescence."""
    start = A.assertions
    n, c = 4, 2
    total = 1 << (1 << n)
    images, first_spectrum = [], None
    for t in range(1, ceil_log(c, n) + 1):
        divisor = c**t
        counts = Counter()
        for family in range(total):
            one = lambda x: family_push(x, n, lambda s: subset_quotient(s, n, c))
            iterated = iterate_map(family, t, one)
            direct = family_push(family, n, lambda s: subset_quotient(s, n, divisor))
            A.check(iterated == direct, "SFC semigroup law")
            counts[iterated] += 1
        m = (n + divisor - 1) // divisor
        targets = list(family_targets(m))
        A.check(set(counts) == set(targets), "SFC image")
        for target in targets:
            A.check(counts[target] == sfc_fibre(n, divisor, target), "SFC fibre")
        images.append(len(counts))
        if t == 1:
            first_spectrum = sorted(Counter(counts.values()).items())
    witness = 1 << (1 << (n - 1))
    h = ceil_log(c, n)
    before = iterate_map(witness, h - 1, lambda x: family_push(x, n, lambda s: subset_quotient(s, n, c)))
    at = iterate_map(witness, h, lambda x: family_push(x, n, lambda s: subset_quotient(s, n, c)))
    after = family_push(at, n, lambda s: subset_quotient(s, n, c))
    A.check(before != at and at == after, "SFC sharp stabilization")
    return f"n=4,c=2,height={h},images={images},t1_fibres={first_spectrum}; assertions={A.assertions-start}"


def subset_shift(mask: int, n: int, t: int = 1) -> int:
    out = 0
    for i in range(t, n):
        if (mask >> i) & 1:
            out |= 1 << (i - t)
    return out


def probe_stp() -> str:
    """Delete the first coordinate from every member, relabel, and deduplicate."""
    start = A.assertions
    n = 4
    total = 1 << (1 << n)
    images = []
    for t in range(1, n + 1):
        counts = Counter()
        for family in range(total):
            one = lambda x: family_push(x, n, lambda s: subset_shift(s, n, 1))
            iterated = iterate_map(family, t, one)
            direct = family_push(family, n, lambda s: subset_shift(s, n, t))
            A.check(iterated == direct, "STP trace iterate")
            counts[iterated] += 1
        m = n - t
        targets = list(family_targets(m))
        A.check(set(counts) == set(targets), "STP image")
        expected_base = (1 << (1 << t)) - 1
        for target in targets:
            expected = expected_base ** target.bit_count()
            A.check(counts[target] == expected, "STP fibre")
        images.append(len(counts))
    witness = 1 << (1 << (n - 1))
    before = iterate_map(witness, n - 1, lambda x: family_push(x, n, lambda s: subset_shift(s, n)))
    at = iterate_map(witness, n, lambda x: family_push(x, n, lambda s: subset_shift(s, n)))
    after = family_push(at, n, lambda s: subset_shift(s, n))
    A.check(before != at and at == after, "STP sharp")
    return f"n=4,height=4,images={images}; assertions={A.assertions-start}"


def probe_spp() -> str:
    """Parity pushforward of a set family under the same coordinate deletion."""
    start = A.assertions
    n = 4
    total = 1 << (1 << n)
    images = []
    for t in range(1, n + 1):
        counts = Counter()
        for family in range(total):
            one = lambda x: family_push(x, n, lambda s: subset_shift(s, n), parity=True)
            iterated = iterate_map(family, t, one)
            direct = family_push(family, n, lambda s: subset_shift(s, n, t), parity=True)
            A.check(iterated == direct, "SPP linear iterate")
            counts[iterated] += 1
        m = n - t
        targets = list(family_targets(m))
        expected = 1 << ((1 << n) - (1 << m))
        A.check(set(counts) == set(targets), "SPP image")
        for target in targets:
            A.check(counts[target] == expected, "SPP fibre")
        images.append(len(counts))
    return f"n=4,height=4,images={images},terminal_fibre={1<<15}; assertions={A.assertions-start}"


def ksets(n: int, k: int) -> tuple[tuple[int, ...], ...]:
    return tuple(combinations(range(n), k))


def uniform_push(code: int, n: int, k: int, divisor: int) -> int:
    source_faces = ksets(n, k)
    positions = {face: bit for bit, face in enumerate(source_faces)}
    out = 0
    for bit, face in enumerate(source_faces):
        if not (code >> bit) & 1:
            continue
        image = tuple(sorted({i // divisor for i in face}))
        if len(image) == k:
            out |= 1 << positions[image]
    return out


def hbc_fibre(n: int, k: int, divisor: int, target: int) -> int:
    sizes = block_sizes(n, divisor)
    m = len(sizes)
    positions = {face: bit for bit, face in enumerate(ksets(n, k))}
    target_faces = ksets(m, k)
    live = 0
    answer = 1
    for face in target_faces:
        lifts = 1
        for j in face:
            lifts *= sizes[j]
        live += lifts
        if (target >> positions[face]) & 1:
            answer *= (1 << lifts) - 1
    answer *= 1 << (comb(n, k) - live)
    return answer


def probe_hbc() -> str:
    """OR quotient of a 3-uniform hypergraph, discarding collapsed triples."""
    start = A.assertions
    n, k, c = 5, 3, 2
    total = 1 << comb(n, k)
    h = 0
    while (n + c**h - 1) // c**h >= k:
        h += 1
    image_sizes, spectra = [], []
    for t in range(1, h + 1):
        divisor = c**t
        counts = Counter()
        for state in range(total):
            iterated = iterate_map(state, t, lambda x: uniform_push(x, n, k, c))
            direct = uniform_push(state, n, k, divisor)
            A.check(iterated == direct, "HBC semigroup law")
            counts[iterated] += 1
        m = (n + divisor - 1) // divisor
        targets = []
        target_faces = ksets(m, k)
        ambient_positions = {face: bit for bit, face in enumerate(ksets(n, k))}
        for small in range(1 << len(target_faces)):
            target = 0
            for j, face in enumerate(target_faces):
                if (small >> j) & 1:
                    target |= 1 << ambient_positions[face]
            targets.append(target)
        A.check(set(counts) == set(targets), "HBC image")
        for target in targets:
            A.check(counts[target] == hbc_fibre(n, k, divisor, target), "HBC fibre")
        image_sizes.append(len(counts))
        spectra.append(sorted(Counter(counts.values()).items()))
    return f"n=5,k=3,c=2,height={h},images={image_sizes},t1_fibres={spectra[0]}; assertions={A.assertions-start}"


def is_clutter(family: int, n: int) -> bool:
    members = [s for s in range(1 << n) if (family >> s) & 1]
    return all(not (a != b and (a & b) == a) for a in members for b in members)


def clutter_blocker(family: int, n: int) -> int:
    edges = [s for s in range(1 << n) if (family >> s) & 1]
    hitting = []
    for candidate in range(1 << n):
        if all(candidate & edge for edge in edges):
            hitting.append(candidate)
    minimal = [h for h in hitting if not any(g != h and (g & h) == g for g in hitting)]
    return sum(1 << h for h in minimal)


def probe_cbl() -> str:
    """Blocker duality on labelled clutters."""
    start = A.assertions
    n = 4
    clutters = [family for family in range(1 << (1 << n)) if is_clutter(family, n)]
    A.check(len(clutters) == 168, "CBL Dedekind census")
    fixed = 0
    for family in clutters:
        blocked = clutter_blocker(family, n)
        A.check(is_clutter(blocked, n), "CBL closure")
        A.check(clutter_blocker(blocked, n) == family, "CBL involution")
        fixed += blocked == family
    return f"n=4,clutters=168,fixed={fixed},two_cycle_states={168-fixed}; assertions={A.assertions-start}"


def relation_transpose(code: int, rows: int, cols: int) -> int:
    out = 0
    for i in range(rows):
        for j in range(cols):
            if (code >> (i * cols + j)) & 1:
                out |= 1 << (j * rows + i)
    return out


def probe_bim() -> str:
    """Transpose a labelled rectangular bipartite incidence relation."""
    start = A.assertions
    rows, cols = 2, 3
    images = set()
    for code in range(1 << (rows * cols)):
        image = relation_transpose(code, rows, cols)
        images.add(image)
        A.check(relation_transpose(image, cols, rows) == code, "BIM involution")
    A.check(len(images) == 64, "BIM bijection")
    return f"shape=2x3,states=64,image=64,period_divides=2; assertions={A.assertions-start}"


def tournament_beats(code: int, n: int, u: int, v: int) -> bool:
    if u == v:
        raise ValueError("loop")
    edge = (u, v) if u < v else (v, u)
    bit = graph_edges(n).index(edge)
    low_beats_high = bool((code >> bit) & 1)
    return low_beats_high if u < v else not low_beats_high


def tournament_triangle_flip(code: int, n: int) -> int:
    positions = {edge: bit for bit, edge in enumerate(graph_edges(n))}
    toggles = 0
    for a, b, c in combinations(range(n), 3):
        cyclic = (
            tournament_beats(code, n, a, b)
            and tournament_beats(code, n, b, c)
            and tournament_beats(code, n, c, a)
        ) or (
            tournament_beats(code, n, b, a)
            and tournament_beats(code, n, c, b)
            and tournament_beats(code, n, a, c)
        )
        if cyclic:
            for edge in ((a, b), (a, c), (b, c)):
                toggles ^= 1 << positions[edge]
    return code ^ toggles


def functional_signature(states, successor):
    succ = {s: successor(s) for s in states}
    tail_hist, cycle_hist = Counter(), Counter()
    for start in states:
        seen = {}
        path = []
        cur = start
        while cur not in seen:
            seen[cur] = len(path)
            path.append(cur)
            cur = succ[cur]
        tail = seen[cur]
        cycle = len(path) - seen[cur]
        tail_hist[tail] += 1
        cycle_hist[cycle] += 1
    return tail_hist, cycle_hist, len(set(succ.values()))


def probe_ttr() -> str:
    """Simultaneously reverse arcs with odd cyclic-triangle incidence."""
    start = A.assertions
    n = 5
    states = range(1 << comb(n, 2))
    for code in states:
        image = tournament_triangle_flip(code, n)
        A.check(0 <= image < (1 << comb(n, 2)), "TTR closure")
    tails, cycles, image = functional_signature(states, lambda x: tournament_triangle_flip(x, n))
    return f"n=5,states=1024,image={image},tails={sorted(tails.items())},cycles={sorted(cycles.items())}; assertions={A.assertions-start}"


def decode_graph(code: int, n: int) -> set[tuple[int, int]]:
    return {edge for bit, edge in enumerate(graph_edges(n)) if (code >> bit) & 1}


def mycielski(n: int, edges: set[tuple[int, int]]):
    out = set(edges)
    for u, v in edges:
        out.add(tuple(sorted((u, n + v))))
        out.add(tuple(sorted((v, n + u))))
    apex = 2 * n
    for v in range(n):
        out.add((n + v, apex))
    return 2 * n + 1, out


def prism(n: int, edges: set[tuple[int, int]]):
    out = set(edges)
    out.update((u + n, v + n) for u, v in edges)
    out.update((v, v + n) for v in range(n))
    return 2 * n, out


def corona_leaf(n: int, edges: set[tuple[int, int]]):
    out = set(edges)
    out.update((v, n + v) for v in range(n))
    return 2 * n, out


def bipartite_double_cover(n: int, edges: set[tuple[int, int]]):
    out = set()
    for u, v in edges:
        out.add((u, n + v))
        out.add((v, n + u))
    return 2 * n, out


def growth_probe(name: str, transform, vertex_rule, edge_rule) -> str:
    start = A.assertions
    seeds = [
        (1, set()),
        (2, {(0, 1)}),
        (3, {(0, 1), (1, 2)}),
        (3, {(0, 1), (0, 2), (1, 2)}),
    ]
    triangle_sequence = None
    for seed_n, seed_edges in seeds:
        n, edges = seed_n, set(seed_edges)
        sequence = [(n, len(edges))]
        for _ in range(3):
            old_n, old_m = n, len(edges)
            n, edges = transform(n, edges)
            A.check(n == vertex_rule(old_n), f"{name} vertex recurrence")
            A.check(len(edges) == edge_rule(old_n, old_m), f"{name} edge recurrence")
            A.check(all(0 <= u < v < n for u, v in edges), f"{name} labelled closure")
            sequence.append((n, len(edges)))
        if seed_n == 3 and len(seed_edges) == 3:
            triangle_sequence = sequence
    return f"K3_sequence={triangle_sequence}; assertions={A.assertions-start}"


def emit(handle: str, description: str, signature: str, decision: str) -> None:
    print(f"[{handle}] PASS | {description} | {signature} | decision={decision}")


def main() -> None:
    print("P162-P166 graph/hypergraph/set breadth scout -- exact transcript")
    print("HOLD_EXTERNAL; exhaustive small probes are not proofs or novelty evidence")
    emit("BQC", "binary-block OR quotient of labelled graphs", probe_bqc(), "FOCUSED_AMBER")
    emit("BPQ", "binary-block parity quotient of labelled graphs", probe_bpq(), "KILL_GENERIC_LINEAR")
    emit("EVD", "even-vertex decimation with label division", probe_evd(), "KILL_SELECTOR_VALUATION_TRANSFER")
    emit("ECS", "two-end chord contraction", probe_ecs(), "KILL_P149_P160_COORDINATE_TRANSFER")
    emit("ELS", "right-end edge slide", probe_els(), "KILL_ENDPOINT_SHIFT_THIN")
    emit("SFC", "set-family direct image under block coalescence", probe_sfc(), "KILL_BQC_P97_DIRECT_IMAGE_ENGINE")
    emit("STP", "set-family trace with relabelling", probe_stp(), "KILL_DIRECT_TRACE_OWNER_THIN")
    emit("SPP", "parity trace of set families", probe_spp(), "KILL_GENERIC_LINEAR")
    emit("HBC", "3-uniform hypergraph block quotient", probe_hbc(), "KILL_BQC_ENGINE_DUPLICATE")
    emit("CBL", "clutter blocker duality", probe_cbl(), "KILL_DIRECT_BLOCKER_OWNER")
    emit("BIM", "bipartite incidence transpose", probe_bim(), "KILL_P127_TRANSPOSE_THIN")
    emit("TTR", "odd cyclic-triangle tournament reversal", probe_ttr(), "KILL_UNSTABLE_SMALL_SIGNATURE")
    emit(
        "MYC",
        "Mycielski graph growth",
        growth_probe("MYC", mycielski, lambda n: 2 * n + 1, lambda n, m: 3 * m + n),
        "KILL_DIRECT_NAMED_OWNER_THIN_INVERSE",
    )
    emit(
        "PRM",
        "Cartesian prism lift",
        growth_probe("PRM", prism, lambda n: 2 * n, lambda n, m: 2 * m + n),
        "KILL_DIRECT_GRAPH_PRODUCT_OWNER",
    )
    emit(
        "COR",
        "one-leaf corona growth",
        growth_probe("COR", corona_leaf, lambda n: 2 * n, lambda n, m: m + n),
        "KILL_DIRECT_CORONA_OWNER_THIN",
    )
    emit(
        "BDC",
        "canonical bipartite double cover",
        growth_probe("BDC", bipartite_double_cover, lambda n: 2 * n, lambda n, m: 2 * m),
        "KILL_DIRECT_PRODUCT_OWNER_THIN",
    )
    A.check(True, "terminal sentinel")
    print(f"TOTAL systems=16 assertions={A.assertions} status=PASS HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
