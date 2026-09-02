#!/usr/bin/env python3
"""Fresh exact falsifier for the BQC-upgrade and RTI hostile gate.

This program imports neither author verifier.  BQC is checked from literal
edge pushforwards, independent Pruefer enumeration, and a full Laplacian
cofactor.  RTI is checked from literal XOR translations and complete
source/history enumeration.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import comb


class Audit:
    def __init__(self) -> None:
        self.n = 0

    def eq(self, got, want, label: str) -> None:
        self.n += 1
        if got != want:
            raise AssertionError(f"{label}: got {got!r}, want {want!r}")

    def ok(self, value, label: str) -> None:
        self.n += 1
        if not value:
            raise AssertionError(label)


A = Audit()


def det_int(matrix: list[list[int]]) -> int:
    """Fraction-free determinant, independently used on two Laplacians."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [row[:] for row in matrix]
    sign = 1
    denominator = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot_value - a[i][k] * a[k][j]
                A.eq(numerator % denominator, 0, "exact determinant division")
                a[i][j] = numerator // denominator
        for i in range(k + 1, n):
            a[i][k] = 0
        denominator = pivot_value
    return sign * a[-1][-1]


def poly_mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return tuple(out)


def binomial_poly(k: int, omit_top: bool = False) -> tuple[int, ...]:
    end = k if omit_top else k + 1
    return tuple(comb(k, j) for j in range(end))


def poly_power(base: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    out = (1,)
    while exponent:
        if exponent & 1:
            out = poly_mul(out, base)
        base = poly_mul(base, base)
        exponent //= 2
    return out


# ---------------------------------------------------------------------------
# BQC: direct graph dynamics and independent tree-fibre reconstruction.


def pairs(n: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(n), 2))


def graph_push(mask: int, n: int, width: int) -> int:
    edge_list = pairs(n)
    edge_index = {edge: j for j, edge in enumerate(edge_list)}
    out = 0
    for j, (u, v) in enumerate(edge_list):
        if mask >> j & 1:
            x, y = sorted((u // width, v // width))
            if x != y:
                out |= 1 << edge_index[(x, y)]
    return out


def graph_iterate(mask: int, n: int, c: int, t: int) -> int:
    for _ in range(t):
        mask = graph_push(mask, n, c)
    return mask


def blocks(n: int, width: int) -> tuple[int, ...]:
    return tuple(min(width, n - start) for start in range(0, n, width))


def bqc_source_poly(target: int, n: int, width: int) -> tuple[int, ...]:
    sizes = blocks(n, width)
    m = len(sizes)
    all_edges = pairs(n)
    for j, (u, v) in enumerate(all_edges):
        if target >> j & 1 and (u >= m or v >= m):
            return ()
    exponent = sum(comb(s, 2) for s in sizes)
    out = binomial_poly(exponent)
    small_index = {edge: j for j, edge in enumerate(all_edges)}
    for i, j in pairs(m):
        if target >> small_index[(i, j)] & 1:
            out = poly_mul(out, tuple([0] + list(binomial_poly(sizes[i] * sizes[j]))[1:]))
    return out


def check_bqc_graph_atlas() -> tuple[int, str]:
    boxes = 0
    rows: list[str] = []
    for n in range(1, 7):
        edge_count = comb(n, 2)
        phase = 1 << edge_count
        c_values = range(2, n + 3) if n <= 5 else (2, 3, 4, 6, 7)
        for c in c_values:  # includes a c>n collision boundary
            height = 0
            power = 1
            while power < n:
                height += 1
                power *= c
            for t in range(height + 2):
                width = c**t
                actual: dict[int, Counter[int]] = defaultdict(Counter)
                for source in range(phase):
                    literal = graph_iterate(source, n, c, t)
                    direct = graph_push(source, n, width)
                    A.eq(literal, direct, "BQC semigroup law")
                    actual[literal][source.bit_count()] += 1
                m = len(blocks(n, width))
                small_edges = pairs(m)
                ambient_index = {edge: j for j, edge in enumerate(pairs(n))}
                supported = []
                for small_mask in range(1 << len(small_edges)):
                    target = sum(
                        1 << ambient_index[edge]
                        for j, edge in enumerate(small_edges)
                        if small_mask >> j & 1
                    )
                    supported.append(target)
                    expected = bqc_source_poly(target, n, width)
                    got = +actual[target]
                    expected_counter = Counter({k: value for k, value in enumerate(expected) if value})
                    A.eq(got, expected_counter, "BQC weighted every-target fibre")
                A.eq(set(actual), set(supported), "BQC complete image")
                A.eq(len(actual), 1 << comb(m, 2), "BQC image size")
                A.eq(sum(sum(v.values()) for v in actual.values()), phase, "BQC fibre mass")
                if m < n:
                    unsupported = 1 << ambient_index[(0, m)]
                    A.eq(bqc_source_poly(unsupported, n, width), (), "BQC unsupported target")
                    A.eq(actual[unsupported], Counter(), "BQC unsupported literal fibre")
                boxes += 1
                rows.append(f"{n}:{c}:{t}:{len(actual)}")

    for n in range(2, 25):
        for c in range(2, n + 3):
            height = 0
            power = 1
            while power < n:
                height += 1
                power *= c
            for u, v in pairs(n):
                clock = 0
                x, y = u, v
                while x != y:
                    x //= c
                    y //= c
                    clock += 1
                A.eq(graph_iterate(1 << pairs(n).index((u, v)), n, c, clock), 0, "BQC edge dies")
                if clock:
                    A.ok(graph_iterate(1 << pairs(n).index((u, v)), n, c, clock - 1) != 0, "BQC edge sharp")
            extreme = 1 << pairs(n).index((0, n - 1))
            A.ok(graph_iterate(extreme, n, c, height - 1) != 0, "BQC global sharp witness")
            A.eq(graph_iterate(extreme, n, c, height), 0, "BQC global height")

    # The advertised inverse works only after normalizing the parameter range.
    strict_boxes = 0
    collision_boxes = 0
    for n in range(2, 2049):
        values = [sum(comb(s, 2) for s in blocks(n, c)) for c in range(1, n + 1)]
        A.ok(all(x < y for x, y in zip(values, values[1:])), "BQC I(n,c) strict on 1..n")
        A.eq(values[-1], sum(comb(s, 2) for s in blocks(n, n + 1)), "BQC c>n collision")
        strict_boxes += 1
        collision_boxes += 1
    digest = sha256("\n".join(rows).encode()).hexdigest()
    return boxes + strict_boxes + collision_boxes, digest


def prufer_edges(n: int, word: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    if n == 1:
        return ()
    degree = [1] * n
    for x in word:
        degree[x] += 1
    edges = []
    for x in word:
        leaf = next(i for i, d in enumerate(degree) if d == 1)
        edges.append(tuple(sorted((leaf, x))))
        degree[leaf] -= 1
        degree[x] -= 1
    remaining = [i for i, d in enumerate(degree) if d == 1]
    edges.append(tuple(sorted(remaining)))
    return tuple(sorted(edges))


def tree_masks(n: int) -> tuple[int, ...]:
    edge_index = {edge: j for j, edge in enumerate(pairs(n))}
    words = [()] if n == 1 else product(range(n), repeat=n - 2)
    out = []
    for word in words:
        edge_set = prufer_edges(n, tuple(word))
        mask = sum(1 << edge_index[e] for e in edge_set)
        out.append(mask)
    A.eq(len(set(out)), 1 if n == 1 else n ** (n - 2), "independent Pruefer bijection")
    return tuple(out)


def full_blowup_tree_count(sizes: tuple[int, ...], base_mask: int) -> int:
    offsets = [0]
    for s in sizes:
        offsets.append(offsets[-1] + s)
    n = offsets[-1]
    adjacency = [[0] * n for _ in range(n)]
    for i, s in enumerate(sizes):
        for u, v in combinations(range(offsets[i], offsets[i + 1]), 2):
            adjacency[u][v] = adjacency[v][u] = 1
    for k, (i, j) in enumerate(pairs(len(sizes))):
        if base_mask >> k & 1:
            for u in range(offsets[i], offsets[i + 1]):
                for v in range(offsets[j], offsets[j + 1]):
                    adjacency[u][v] = adjacency[v][u] = 1
    lap = [[0] * n for _ in range(n)]
    for i in range(n):
        lap[i][i] = sum(adjacency[i])
        for j in range(n):
            if i != j:
                lap[i][j] = -adjacency[i][j]
    return det_int([row[:-1] for row in lap[:-1]])


def reduced_blowup_tree_count(sizes: tuple[int, ...], base_mask: int, root: int) -> int:
    m = len(sizes)
    adjacent = [[False] * m for _ in range(m)]
    for k, (i, j) in enumerate(pairs(m)):
        if base_mask >> k & 1:
            adjacent[i][j] = adjacent[j][i] = True
    D = [sum(sizes[j] for j in range(m) if adjacent[i][j]) for i in range(m)]
    Q = [[D[i] if i == j else (-sizes[j] if adjacent[i][j] else 0) for j in range(m)] for i in range(m)]
    cofactor = det_int([[Q[i][j] for j in range(m) if j != root] for i in range(m) if i != root])
    numerator = cofactor
    for i in range(m):
        numerator *= (sizes[i] + D[i]) ** (sizes[i] - 1)
    A.eq(numerator % sizes[root], 0, "BQC reduced determinant integral")
    return numerator // sizes[root]


def prescribed_tree_count(sizes: tuple[int, ...], target: int) -> int:
    total = 0
    sub = target
    while True:
        total += (-1) ** ((target ^ sub).bit_count()) * full_blowup_tree_count(sizes, sub)
        if sub == 0:
            return total
        sub = (sub - 1) & target


def check_bqc_tree_atlas() -> tuple[int, str]:
    rows = []
    boxes = 0
    for n in range(1, 8):
        trees = tree_masks(n)
        cayley = 1 if n == 1 else n ** (n - 2)
        for width in sorted({1, n, n + 1} | set(range(2, n + 1))):
            sizes = blocks(n, width)
            m = len(sizes)
            actual = Counter(graph_push(tree, n, width) for tree in trees)
            A.eq(sum(actual.values()), cayley, "BQC tree total Cayley mass")
            edge_index = {edge: j for j, edge in enumerate(pairs(n))}
            path = sum(1 << edge_index[(i, i + 1)] for i in range(n - 1))
            cycle = path | (1 << edge_index[(0, n - 1)]) if n > 2 else path
            disconnected = sum(1 << edge_index[(i, i + 1)] for i in range(0, n - 1, 2))
            # Verify the reduced formula against a full n-by-n Matrix--Tree
            # cofactor.  The large width-one boundary uses a deterministic
            # sample; all smaller base graphs are traversed.
            if m <= 4:
                formula_bases = range(1 << comb(m, 2))
            else:
                formula_bases = sorted(set(sorted(actual)[:80] + [0, path, cycle, disconnected]))
            for base in formula_bases:
                full = full_blowup_tree_count(sizes, base)
                for root in range(m):
                    A.eq(reduced_blowup_tree_count(sizes, base, root), full, "BQC reduced blow-up formula")
            if m <= 4:
                ambient_index = {edge: j for j, edge in enumerate(pairs(n))}
                target_pairs = []
                for small in range(1 << comb(m, 2)):
                    ambient = sum(
                        1 << ambient_index[edge]
                        for j, edge in enumerate(pairs(m))
                        if small >> j & 1
                    )
                    target_pairs.append((ambient, small))
            else:
                sample = sorted(actual)[:80]
                target_pairs = [(target, target) for target in sorted(set(sample + [0, path, cycle, disconnected]))]
            formula_mass = 0
            for target, packed_target in target_pairs:
                expected = prescribed_tree_count(sizes, packed_target)
                A.ok(expected >= 0, "BQC tree inversion nonnegative")
                A.eq(actual[target], expected, "BQC every-target tree fibre")
                if m <= 4:
                    formula_mass += expected
            if m <= 4:
                A.eq(formula_mass, cayley, "BQC tree-fibre partition")
            if width >= n:
                A.eq(actual, Counter({0: cayley}), "BQC one-block tree boundary")
            rows.append(f"{n}:{width}:{sizes}:{len(actual)}")
            boxes += 1
    return boxes, sha256("\n".join(rows).encode()).hexdigest()


# ---------------------------------------------------------------------------
# RTI: literal random translations, rank clock, and inverse atlas.


def translate_subset(mask: int, v: int, d: int) -> int:
    out = 0
    for x in range(1 << d):
        if mask >> x & 1:
            out |= 1 << (x ^ v)
    return out


def rti_step(mask: int, v: int, d: int) -> int:
    return mask & translate_subset(mask, v, d)


def span_mask(vectors: tuple[int, ...]) -> int:
    span = {0}
    for v in vectors:
        span.update(tuple(x ^ v for x in span))
    return sum(1 << x for x in span)


def erosion(mask: int, subspace: int, d: int) -> int:
    out = (1 << (1 << d)) - 1
    for h in range(1 << d):
        if subspace >> h & 1:
            out &= translate_subset(mask, h, d)
    return out


def rti_run(mask: int, history: tuple[int, ...], d: int) -> int:
    for v in history:
        mask = rti_step(mask, v, d)
    return mask


def subspaces(d: int) -> tuple[int, ...]:
    known = {1}
    frontier = [1]
    while frontier:
        H = frontier.pop()
        elements = tuple(x for x in range(1 << d) if H >> x & 1)
        for v in range(1 << d):
            K = span_mask(elements + (v,))
            if K not in known:
                known.add(K)
                frontier.append(K)
    return tuple(sorted(known))


def dimension(H: int) -> int:
    size = H.bit_count()
    A.ok(size > 0 and size & (size - 1) == 0, "RTI subspace size")
    return size.bit_length() - 1


def stabilizer(mask: int, d: int) -> int:
    return sum(1 << v for v in range(1 << d) if translate_subset(mask, v, d) == mask)


def gaussian(s: int, r: int) -> int:
    if r < 0 or r > s:
        return 0
    numerator = denominator = 1
    for i in range(r):
        numerator *= (1 << (s - i)) - 1
        denominator *= (1 << (r - i)) - 1
    A.eq(numerator % denominator, 0, "Gaussian binomial integral")
    return numerator // denominator


def spanning_histories(t: int, r: int) -> int:
    out = 1
    for i in range(r):
        out *= (1 << t) - (1 << i)
    return out


def rti_formula(target: int, d: int, t: int) -> Counter[int]:
    b = target.bit_count()
    s = dimension(stabilizer(target, d))
    out: Counter[int] = Counter()
    for r in range(s + 1):
        histories = spanning_histories(t, r)
        if histories == 0:
            continue
        h = 1 << r
        A.eq(b % h, 0, "RTI stabilized target coset divisibility")
        outside = (1 << (d - r)) - b // h
        free = poly_power(binomial_poly(h, omit_top=True), outside)
        multiplier = gaussian(s, r) * histories
        for extra, coefficient in enumerate(free):
            out[b + extra] += multiplier * coefficient
    return +out


def check_rti_atlas() -> tuple[int, str]:
    boxes = 0
    rows = []
    for d, max_t in ((0, 4), (1, 5), (2, 4), (3, 4)):
        N = 1 << d
        phase = 1 << N
        step_table = [[rti_step(source, v, d) for source in range(phase)] for v in range(N)]
        spaces = subspaces(d)
        eroded = {H: [erosion(source, H, d) for source in range(phase)] for H in spaces}
        for t in range(max_t + 1):
            actual: dict[int, Counter[int]] = defaultdict(Counter)
            history_counts: Counter[int] = Counter()
            for history in product(range(N), repeat=t):
                H = span_mask(tuple(history))
                history_counts[H] += 1
                sources_to_check = range(phase) if d <= 2 else range(0, phase, 5)
                for source in sources_to_check:
                    literal = source
                    for v in history:
                        literal = step_table[v][literal]
                    A.eq(literal, eroded[H][source], "RTI history-span identity")
            for H, multiplicity in history_counts.items():
                for source, target in enumerate(eroded[H]):
                    actual[target][source.bit_count()] += multiplicity
            mass = 0
            for target in range(phase):
                expected = rti_formula(target, d, t)
                A.eq(actual[target], expected, "RTI every-target weighted fibre")
                mass += sum(expected.values())
            A.eq(mass, phase * N**t, "RTI source-history mass")
            rows.append(f"{d}:{t}:{phase}:{mass}")
            boxes += 1
    return boxes, sha256("\n".join(rows).encode()).hexdigest()


def check_rti_temporal_and_recovery() -> tuple[int, int, str]:
    rows = []
    boxes = 0
    odd_boundary_targets = 0
    for d in range(0, 7):
        N = 1 << d
        spaces = subspaces(d)
        # Fixed-subspace history counts and full-rank CDF.
        for t in range(0, d + 5):
            if (d <= 3 and t <= 5) or (d == 4 and t <= 4):
                counts = Counter(span_mask(tuple(h)) for h in product(range(N), repeat=t))
                for H in spaces:
                    A.eq(counts[H], spanning_histories(t, dimension(H)), "RTI fixed-span history count")
            full = spanning_histories(t, d)
            if t < d:
                A.eq(full, 0, "RTI rank lower boundary")
            else:
                numerator = 1
                for i in range(d):
                    numerator *= (1 << t) - (1 << i)
                A.eq(full, numerator, "RTI full-rank product")

        expected_time = sum((Fraction(1 << d, (1 << d) - (1 << r)) for r in range(d)), Fraction(0))
        recurrence_time = Fraction(0)
        for r in reversed(range(d)):
            recurrence_time += Fraction(1 << d, (1 << d) - (1 << r))
        A.eq(expected_time, recurrence_time, "RTI exact mean clock")

        phase = 1 << N
        full_set = phase - 1
        absorbing = []
        if d <= 3:
            for state in range(phase):
                fixed_all = all(rti_step(state, v, d) == state for v in range(N))
                if fixed_all:
                    absorbing.append(state)
            A.eq(absorbing, [0, full_set], "RTI only absorbing states")
        for H in spaces:
            for state in (range(phase) if d <= 3 else (0, full_set, 1, full_set ^ 1)):
                if dimension(H) == d:
                    A.eq(erosion(state, H, d), full_set if state == full_set else 0, "RTI full-span absorption")
        witness = full_set ^ 1
        for H in spaces:
            A.eq(erosion(witness, H, d), full_set ^ H, "RTI sharp witness identity")
            A.eq(erosion(witness, H, d) == 0, dimension(H) == d, "RTI sharp clock")

        if d <= 3:
            values_by_size: dict[int, dict[int, int]] = defaultdict(dict)
            for target in range(phase):
                b = target.bit_count()
                s = dimension(stabilizer(target, d))
                literal = sum(rti_formula(target, d, 1).values())
                if s == 0:
                    corrected = 1
                else:
                    A.eq(b % 2, 0, "RTI nontrivial stabilizer forces even target")
                    corrected = 1 + ((1 << s) - 1) * 3 ** ((1 << (d - 1)) - b // 2)
                A.eq(literal, corrected, "RTI corrected one-step recovery formula")
                old = values_by_size[b].setdefault(s, literal)
                A.eq(old, literal, "RTI fibre depends on size and stabilizer")
                if b % 2:
                    A.eq(s, 0, "RTI odd target has trivial translation stabilizer")
                    odd_boundary_targets += 1
            for b, values in values_by_size.items():
                ordered = sorted(values.items())
                A.ok(all(x[1] < y[1] for x, y in zip(ordered, ordered[1:])), f"RTI stabilizer recovery b={b}")
        rows.append(f"{d}:{len(spaces)}:{expected_time}:{odd_boundary_targets}")
        boxes += 1
    return boxes, odd_boundary_targets, sha256("\n".join(rows).encode()).hexdigest()


def main() -> None:
    bqc_graph_boxes, bqc_graph_digest = check_bqc_graph_atlas()
    bqc_tree_boxes, bqc_tree_digest = check_bqc_tree_atlas()
    rti_atlas_boxes, rti_atlas_digest = check_rti_atlas()
    rti_temporal_boxes, odd_boundary_targets, rti_temporal_digest = check_rti_temporal_and_recovery()
    print("P162--P166 REPLACEMENT HOSTILE GATE 1")
    print(f"BQC graph_boxes={bqc_graph_boxes} digest={bqc_graph_digest}")
    print(f"BQC tree_boxes={bqc_tree_boxes} digest={bqc_tree_digest}")
    print("BQC parameter_collision=c=n_equals_every_c_greater_than_n")
    print(f"RTI atlas_boxes={rti_atlas_boxes} digest={rti_atlas_digest}")
    print(f"RTI temporal_boxes={rti_temporal_boxes} odd_formula7_boundaries={odd_boundary_targets} digest={rti_temporal_digest}")
    print(f"ASSERTIONS {A.n}")
    print("STATUS PASS_WITH_TWO_STATEMENT_REPAIRS")


if __name__ == "__main__":
    main()
