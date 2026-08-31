#!/usr/bin/env python3
"""Exact replacement pilot for the P132--P136 combinatorial lane.

The script exhausts twenty literal finite maps on underused carriers.  It is
falsification evidence, not a novelty certificate.  In addition to a complete
functional-graph scan, the two finite-map finalists receive independent
pointwise basin checks and several killed controls receive formula checks.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


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
        last_image, last_fixed = len(image_set), len(fixed)
        CHECKS.that(fixed <= image_set, (ident, label, "fixed/image"))
        for start in states:
            seen = {}
            cur = start
            while cur not in seen:
                seen[cur] = len(seen)
                cur = nxt[cur]
            tail = seen[cur]
            period = len(seen) - tail
            CHECKS.that(period >= 1, (ident, label, start, period))
            witness = cur
            for _ in range(period):
                witness = nxt[witness]
            CHECKS.that(witness == cur, (ident, label, start, tail, period))
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


def iterate_to_fixed(state, phi):
    depth = 0
    while phi(state) != state:
        state = phi(state)
        depth += 1
    return state, depth


# ---------------------------------------------------------------------------
# Endofunctions


def functional_cycles(f):
    n = len(f)
    done = set()
    out = []
    for seed in range(n):
        if seed in done:
            continue
        path = []
        position = {}
        cur = seed
        while cur not in done and cur not in position:
            position[cur] = len(path)
            path.append(cur)
            cur = f[cur]
        if cur in position:
            cycle = path[position[cur]:]
            pivot = cycle.index(min(cycle))
            out.append(tuple(cycle[pivot:] + cycle[:pivot]))
        done.update(path)
    return tuple(sorted(out, key=lambda cycle: cycle[0]))


def cyclic_vertices(f):
    return {v for cycle in functional_cycles(f) for v in cycle}


def weak_components(f):
    n = len(f)
    adj = [set() for _ in range(n)]
    for v, w in enumerate(f):
        adj[v].add(w)
        adj[w].add(v)
    unseen = set(range(n))
    out = []
    while unseen:
        seed = min(unseen)
        comp = {seed}
        queue = [seed]
        unseen.remove(seed)
        while queue:
            v = queue.pop()
            for w in adj[v]:
                if w in unseen:
                    unseen.remove(w)
                    comp.add(w)
                    queue.append(w)
        out.append(frozenset(comp))
    return tuple(out)


def fm_cycle_open(f):
    active = [cycle for cycle in functional_cycles(f) if len(cycle) > 1]
    if not active:
        return f
    pivot = min(v for cycle in active for v in cycle)
    out = list(f)
    out[pivot] = pivot
    return tuple(out)


def fm_leaf_loop(f):
    indegree = [0] * len(f)
    for image in f:
        indegree[image] += 1
    leaves = [v for v, degree in enumerate(indegree) if degree == 0]
    if not leaves:
        return f
    pivot = min(leaves)
    out = list(f)
    out[pivot] = pivot
    return tuple(out)


def fm_cycle_excision(f):
    active = [cycle for cycle in functional_cycles(f) if len(cycle) > 1]
    if not active:
        return f
    cycle = min(active, key=lambda c: min(c))
    pivot = min(cycle)
    j = cycle.index(pivot)
    cycle = cycle[j:] + cycle[:j]
    successor, predecessor = cycle[1], cycle[-1]
    out = list(f)
    out[pivot] = pivot
    out[predecessor] = predecessor if len(cycle) == 2 else successor
    return tuple(out)


def fm_component_min_root(f):
    out = list(f)
    for component in weak_components(f):
        pivot = min(component)
        out[pivot] = pivot
    return tuple(out)


def endofunction_instances(phi, max_n):
    return [
        (f"n={n}", tuple(product(range(n), repeat=n)), phi)
        for n in range(1, max_n + 1)
    ]


def component_root_of_forest(g, v):
    while g[v] != v:
        v = g[v]
    return v


def convolve(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def integer_break(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n % 3 == 0:
        return 3 ** (n // 3)
    if n % 3 == 1:
        return 4 * 3 ** ((n - 4) // 3)
    return 2 * 3 ** ((n - 2) // 3)


def focused_cycle_open(max_n=6):
    before = CHECKS.n
    last_max = 0
    for n in range(1, max_n + 1):
        states = tuple(product(range(n), repeat=n))
        actual = defaultdict(Counter)
        layers = Counter()
        for f in states:
            target, depth = iterate_to_fixed(f, fm_cycle_open)
            expected_depth = sum(len(cycle) > 1 for cycle in functional_cycles(f))
            CHECKS.that(depth == expected_depth, ("FM1-depth", n, f, depth))
            CHECKS.that(all(len(c) == 1 for c in functional_cycles(target)),
                        ("FM1-target", n, f, target))
            actual[target][depth] += 1
            layers[depth] += 1

        for target, observed in actual.items():
            roots = [cycle[0] for cycle in functional_cycles(target)]
            polynomial = [1]
            for root in roots:
                admissible = 0
                for v in range(n):
                    if v == root or component_root_of_forest(target, v) != root:
                        continue
                    cur = v
                    good = True
                    while cur != root:
                        if cur < root:
                            good = False
                        cur = target[cur]
                    admissible += good
                polynomial = convolve(polynomial, [1, admissible])
            expected = Counter({k: value for k, value in enumerate(polynomial) if value})
            CHECKS.that(observed == expected,
                        ("FM1-fibre", n, target, observed, expected))

        permutation_nontrivial = defaultdict(Counter)
        for r in range(1, n + 1):
            for p in permutations(range(r)):
                k = sum(len(cycle) > 1 for cycle in functional_cycles(p))
                permutation_nontrivial[r][k] += 1
        expected_layers = Counter()
        for r in range(1, n + 1):
            forest_count = 1 if r == n else r * n ** (n - r - 1)
            for k, count in permutation_nontrivial[r].items():
                expected_layers[k] += comb(n, r) * count * forest_count
        CHECKS.that(layers == expected_layers, ("FM1-layers", n, layers, expected_layers))
        CHECKS.that(len(actual) == (n + 1) ** (n - 1), ("FM1-fixed", n, len(actual)))
        CHECKS.that(max(layers) == n // 2, ("FM1-max-depth", n, layers))
        last_max = max(sum(counter.values()) for counter in actual.values())
        CHECKS.that(last_max == integer_break(n), ("FM1-max-fibre", n, last_max))
    assertions = CHECKS.n - before
    print(f"FOCUS FM1 | n<=6 | pointwise_depth_fibres=PASS | last_max_fibre={last_max} | assertions={assertions}")
    return assertions


def focused_leaf_loop(max_n=6):
    before = CHECKS.n
    last_max = 0
    for n in range(1, max_n + 1):
        states = tuple(product(range(n), repeat=n))
        actual = defaultdict(Counter)
        layers = Counter()
        for f in states:
            target, depth = iterate_to_fixed(f, fm_leaf_loop)
            expected_depth = n - len(cyclic_vertices(f))
            CHECKS.that(depth == expected_depth, ("FM2-depth", n, f, depth))
            CHECKS.that(len(set(target)) == n, ("FM2-permutation", n, f, target))
            actual[target][depth] += 1
            layers[depth] += 1
        CHECKS.that(len(actual) == factorial(n), ("FM2-fixed", n, len(actual)))
        for target, observed in actual.items():
            m = sum(target[v] == v for v in range(n))
            expected = Counter({0: 1})
            for k in range(1, m + 1):
                value = comb(m, k) * (n - k) * n ** (k - 1)
                if value:
                    expected[k] = value
            CHECKS.that(observed == expected,
                        ("FM2-fibre", n, target, observed, expected))
            total_formula = 1 if m == 0 else (n + 1 - m) * (n + 1) ** (m - 1)
            CHECKS.that(sum(observed.values()) == total_formula,
                        ("FM2-total", n, target, observed, total_formula))
        expected_layers = Counter({0: factorial(n)})
        for k in range(1, n):
            r = n - k
            expected_layers[k] = comb(n, r) * factorial(r) * r * n ** (k - 1)
        CHECKS.that(layers == expected_layers, ("FM2-layers", n, layers, expected_layers))
        fibres = {target: sum(counter.values()) for target, counter in actual.items()}
        identity = tuple(range(n))
        last_max = max(fibres.values())
        CHECKS.that(fibres[identity] == (n + 1) ** (n - 1),
                    ("FM2-identity", n, fibres[identity]))
        CHECKS.that([target for target, size in fibres.items() if size == last_max] == [identity],
                    ("FM2-unique-max", n, last_max))
    assertions = CHECKS.n - before
    print(f"FOCUS FM2 | n<=6 | permutation_basin_polynomials=PASS | last_max_fibre={last_max} | assertions={assertions}")
    return assertions


def focused_cycle_excision(max_n=6):
    before = CHECKS.n
    for n in range(1, max_n + 1):
        fixed = 0
        for f in product(range(n), repeat=n):
            target, depth = iterate_to_fixed(f, fm_cycle_excision)
            excess = sum(len(cycle) - 1 for cycle in functional_cycles(f))
            CHECKS.that(depth == excess, ("FM3-depth", n, f, depth, excess))
            CHECKS.that(all(len(c) == 1 for c in functional_cycles(target)),
                        ("FM3-target", n, f, target))
            fixed += depth == 0
        CHECKS.that(fixed == (n + 1) ** (n - 1), ("FM3-fixed", n, fixed))
    assertions = CHECKS.n - before
    print(f"FOCUS FM3 | n<=6 | cyclic_excess_clock=PASS | assertions={assertions}")
    return assertions


# ---------------------------------------------------------------------------
# Hypergraphs, simplicial complexes, and clutters


def family_edges(mask):
    bit = 0
    while mask:
        if mask & 1:
            yield bit
        bit += 1
        mask >>= 1


def edges_family(edges):
    mask = 0
    for edge in edges:
        mask |= 1 << edge
    return mask


def delete_max_edge(edge):
    return 0 if edge == 0 else edge ^ (1 << (edge.bit_length() - 1))


def hf_max_delete(mask, n):
    return edges_family(delete_max_edge(edge) for edge in family_edges(mask))


def degrees(mask, n):
    out = [0] * n
    for edge in family_edges(mask):
        for v in range(n):
            out[v] += (edge >> v) & 1
    return out


def hf_degree_delete(mask, n):
    degree = degrees(mask, n)
    out = []
    for edge in family_edges(mask):
        if edge == 0:
            out.append(0)
            continue
        vertices = [v for v in range(n) if edge >> v & 1]
        pivot = min(vertices, key=lambda v: (degree[v], v))
        out.append(edge ^ (1 << pivot))
    return edges_family(out)


def hf_pair_intersections(mask, n):
    edges = sorted(family_edges(mask))
    out = []
    for j in range(0, len(edges), 2):
        out.append(edges[j] if j + 1 == len(edges) else edges[j] & edges[j + 1])
    return edges_family(out)


def hf_incidence_leaf_strip(mask, n):
    degree = degrees(mask, n)
    leaves = sum((degree[v] == 1) << v for v in range(n))
    return edges_family(edge & ~leaves for edge in family_edges(mask))


def all_hypergraphs(n):
    return range(1 << (1 << n))


def is_complex(mask, n):
    for edge in family_edges(mask):
        subset = edge
        while True:
            if not (mask >> subset) & 1:
                return False
            if subset == 0:
                break
            subset = (subset - 1) & edge
    return True


def is_clutter(mask, n):
    edges = tuple(family_edges(mask))
    return all(not (a != b and a & b == a) for a in edges for b in edges)


@lru_cache(maxsize=None)
def complexes(n):
    return tuple(mask for mask in all_hypergraphs(n) if is_complex(mask, n))


@lru_cache(maxsize=None)
def clutters(n):
    return tuple(mask for mask in all_hypergraphs(n) if is_clutter(mask, n))


def sc_prefix_delete(mask, n):
    return hf_max_delete(mask, n)


def inclusion_minimalize(edges):
    unique = set(edges)
    return edges_family(edge for edge in unique
                        if not any(other != edge and other & edge == other for other in unique))


def cl_degree_delete(mask, n):
    degree = degrees(mask, n)
    out = []
    for edge in family_edges(mask):
        if edge == 0:
            out.append(0)
        else:
            vertices = [v for v in range(n) if edge >> v & 1]
            pivot = min(vertices, key=lambda v: (degree[v], v))
            out.append(edge ^ (1 << pivot))
    return inclusion_minimalize(out)


def family_max_rank(mask):
    return max((edge.bit_count() for edge in family_edges(mask)), default=0)


def focused_hf_max_delete(max_n=4):
    before = CHECKS.n
    last_iterated_image = 0
    for n in range(1, max_n + 1):
        states = tuple(all_hypergraphs(n))
        for mask in states:
            _, depth = iterate_to_fixed(mask, lambda x, n=n: hf_max_delete(x, n))
            expected = 0 if mask in (0, 1) else family_max_rank(mask)
            CHECKS.that(depth == expected, ("HF1-depth", n, mask, depth, expected))
        for t in range(n + 1):
            fibres = Counter()
            for source in states:
                target = source
                for _ in range(t):
                    target = hf_max_delete(target, n)
                fibres[target] += 1
            expected_types = 1 << (1 << (n - t))
            CHECKS.that(len(fibres) == expected_types,
                        ("HF1-image", n, t, len(fibres), expected_types))
            last_iterated_image = len(fibres)
            for target, observed in fibres.items():
                expected = 1
                for edge in family_edges(target):
                    if edge == 0:
                        parents = sum(comb(n, j) for j in range(min(t, n) + 1))
                    else:
                        larger = n - edge.bit_length()
                        parents = comb(larger, t) if larger >= t else 0
                    expected *= (1 << parents) - 1
                CHECKS.that(observed == expected,
                            ("HF1-fibre", n, t, target, observed, expected))
    assertions = CHECKS.n - before
    print(f"FOCUS HF1 | n<=4 | all_iterate_fibres=PASS | last_iterated_image={last_iterated_image} | assertions={assertions}")
    return assertions


def focused_rank_clocks(max_n=4):
    before = CHECKS.n
    for n in range(1, max_n + 1):
        for mask in all_hypergraphs(n):
            _, depth = iterate_to_fixed(mask, lambda x, n=n: hf_degree_delete(x, n))
            expected = 0 if mask in (0, 1) else family_max_rank(mask)
            CHECKS.that(depth == expected, ("HF2-depth", n, mask, depth, expected))
        for mask in complexes(n):
            _, depth = iterate_to_fixed(mask, lambda x, n=n: sc_prefix_delete(x, n))
            expected = 0 if mask in (0, 1) else family_max_rank(mask)
            CHECKS.that(depth == expected, ("SC1-depth", n, mask, depth, expected))
    assertions = CHECKS.n - before
    print(f"FOCUS RANK | n<=4 | hypergraph_and_complex_clocks=PASS | assertions={assertions}")
    return assertions


# ---------------------------------------------------------------------------
# Order ideals, antichains, and labelled posets


def crown_predecessors(m):
    preds = [0] * (2 * m)
    for i in range(m):
        preds[m + i] = (1 << i) | (1 << ((i + 1) % m))
    return tuple(preds)


def ideals(preds):
    n = len(preds)
    return tuple(mask for mask in range(1 << n)
                 if all(not (mask >> v & 1) or preds[v] & ~mask == 0 for v in range(n)))


def ideal_maxima(mask, preds):
    return [v for v in range(len(preds)) if mask >> v & 1
            and not any(mask >> w & 1 and (preds[w] >> v) & 1 for w in range(len(preds)))]


def oi_pivot_exchange(mask, preds):
    maxima = ideal_maxima(mask, preds)
    if not maxima:
        return mask
    pivot = max(maxima)
    reduced = mask ^ (1 << pivot)
    available = [v for v in range(len(preds)) if not (reduced >> v) & 1
                 and v != pivot and preds[v] & ~reduced == 0]
    return reduced | (1 << min(available)) if available else mask


def oi_principal_parity(mask, preds):
    remove = [v for v in ideal_maxima(mask, preds)
              if (preds[v].bit_count() + 1) % 2 == 1]
    reduced = mask
    for v in remove:
        reduced &= ~(1 << v)
    add = [v for v in range(len(preds)) if not (reduced >> v) & 1
           and preds[v] & ~reduced == 0
           and (preds[v].bit_count() + 1) % 2 == 0]
    for v in add:
        reduced |= 1 << v
    return reduced


def binary_tree_predecessors(height):
    n = 2 ** (height + 1) - 1
    preds = []
    for v in range(n):
        mask = 0
        cur = v
        while cur:
            cur = (cur - 1) // 2
            mask |= 1 << cur
        preds.append(mask)
    return tuple(preds)


def antichains(preds):
    n = len(preds)
    return tuple(mask for mask in range(1 << n)
                 if all(not (mask >> a & 1 and mask >> b & 1)
                        or not ((preds[a] >> b) & 1 or (preds[b] >> a) & 1)
                        for a in range(n) for b in range(a)))


def ac_parent_contract(mask, preds):
    selected = set()
    for v in range(len(preds)):
        if mask >> v & 1:
            selected.add(0 if v == 0 else (v - 1) // 2)
    maximal = [v for v in selected
               if not any(v != w and (preds[w] >> v) & 1 for w in selected)]
    return sum(1 << v for v in maximal)


@lru_cache(maxsize=None)
def natural_posets(n):
    pairs = tuple((i, j) for i in range(n) for j in range(i + 1, n))
    found = set()
    for edge_mask in range(1 << len(pairs)):
        reach = [0] * n
        for bit, (i, j) in enumerate(pairs):
            if edge_mask >> bit & 1:
                reach[i] |= 1 << j
        for k in range(n):
            for i in range(n):
                if reach[i] >> k & 1:
                    reach[i] |= reach[k]
        preds = [0] * n
        for i in range(n):
            for j in range(n):
                if reach[i] >> j & 1:
                    preds[j] |= 1 << i
        found.add(tuple(preds))
    return tuple(sorted(found))


def delete_least_maximal_poset(state):
    n, preds = state
    if n == 0:
        return state
    maxima = [v for v in range(n)
              if not any((preds[w] >> v) & 1 for w in range(n))]
    deleted = min(maxima)
    old = [v for v in range(n) if v != deleted]
    relabel = {v: j for j, v in enumerate(old)}
    new_preds = []
    for v in old:
        mask = 0
        for u in old:
            if preds[v] >> u & 1:
                mask |= 1 << relabel[u]
        new_preds.append(mask)
    return n - 1, tuple(new_preds)


def focused_poset_reductions():
    before = CHECKS.n
    for height in range(4):
        preds = binary_tree_predecessors(height)
        for antichain in antichains(preds):
            _, depth = iterate_to_fixed(antichain, lambda x, p=preds: ac_parent_contract(x, p))
            expected = max(((v + 1).bit_length() - 1 for v in range(len(preds))
                            if antichain >> v & 1), default=0)
            CHECKS.that(depth == expected, ("AC1-depth", height, antichain, depth, expected))
    all_states = tuple((n, preds) for n in range(6) for preds in natural_posets(n))
    for state in all_states:
        _, depth = iterate_to_fixed(state, delete_least_maximal_poset)
        CHECKS.that(depth == state[0], ("PO1-depth", state, depth))
    assertions = CHECKS.n - before
    print(f"FOCUS POSET | parent_and_branching_clocks=PASS | assertions={assertions}")
    return assertions


# ---------------------------------------------------------------------------
# Standard Young tableaux


def addable_rows(shape):
    rows = [r for r in range(len(shape)) if r == 0 or shape[r] < shape[r - 1]]
    rows.append(len(shape))
    return tuple(rows)


def tableau_add(tableau, value, row):
    rows = [list(r) for r in tableau]
    if row == len(rows):
        rows.append([value])
    else:
        rows[row].append(value)
    return tuple(tuple(r) for r in rows)


@lru_cache(maxsize=None)
def tableaux(n):
    states = {()}
    for value in range(n):
        nxt = set()
        for tableau in states:
            shape = tuple(map(len, tableau))
            for row in addable_rows(shape):
                nxt.add(tableau_add(tableau, value, row))
        states = nxt
    return tuple(sorted(states))


def tableau_delete_max(tableau):
    if not tableau:
        return tableau
    value = sum(map(len, tableau)) - 1
    rows = [list(row) for row in tableau]
    for r, row in enumerate(rows):
        if row and row[-1] == value:
            row.pop()
            if not row:
                rows.pop(r)
            return tuple(tuple(x) for x in rows)
    raise AssertionError(("max not corner", tableau))


def tableau_relocate_max_first_row(tableau):
    if not tableau:
        return tableau
    value = sum(map(len, tableau)) - 1
    base = tableau_delete_max(tableau)
    return tableau_add(base, value, 0)


def focused_tableaux(max_n=8):
    before = CHECKS.n
    all_states = tuple(tableau for n in range(max_n + 1) for tableau in tableaux(n))
    for tableau in all_states:
        _, depth = iterate_to_fixed(tableau, tableau_delete_max)
        CHECKS.that(depth == sum(map(len, tableau)), ("YT1-depth", tableau, depth))
    for n in range(1, max_n + 1):
        fibres = Counter(tableau_relocate_max_first_row(t) for t in tableaux(n))
        for target, observed in fibres.items():
            base = tableau_delete_max(target)
            expected = len(addable_rows(tuple(map(len, base))))
            CHECKS.that(observed == expected, ("YT2-fibre", n, target, observed, expected))
    assertions = CHECKS.n - before
    print(f"FOCUS TABLEAUX | n<=8 | Young_branching_fibres=PASS | assertions={assertions}")
    return assertions


# ---------------------------------------------------------------------------
# Plane partitions and lattice animals


def plane_partitions(a, b, h):
    out = []
    for values in product(range(h + 1), repeat=a * b):
        good = True
        for i in range(a):
            for j in range(b):
                x = values[i * b + j]
                if i + 1 < a and x < values[(i + 1) * b + j]:
                    good = False
                if j + 1 < b and x < values[i * b + j + 1]:
                    good = False
        if good:
            out.append(values)
    return tuple(out)


def pp_removable(values, a, b):
    out = []
    for i in range(a):
        for j in range(b):
            x = values[i * b + j]
            down = values[(i + 1) * b + j] if i + 1 < a else 0
            right = values[i * b + j + 1] if j + 1 < b else 0
            if x > max(down, right):
                out.append(i * b + j)
    return out


def pp_corner_wave(values, a, b):
    out = list(values)
    for index in pp_removable(values, a, b):
        out[index] -= 1
    return tuple(out)


def pp_parity_corner(values, a, b):
    removable = pp_removable(values, a, b)
    if not removable:
        return values
    volume = sum(values)
    selected = [index for index in removable
                if ((index // b) + (index % b) + volume) % 2 == 0]
    if not selected:
        selected = [min(removable)]
    out = list(values)
    for index in selected:
        out[index] -= 1
    return tuple(out)


def directed_animals(width, height):
    out = [0]
    cells = width * height
    for mask in range(1, 1 << cells):
        if not mask & 1:
            continue
        reached = {0}
        queue = [0]
        while queue:
            cell = queue.pop()
            x, y = cell % width, cell // width
            for nxt in ((cell + 1) if x + 1 < width else -1,
                        (cell + width) if y + 1 < height else -1):
                if nxt >= 0 and mask >> nxt & 1 and nxt not in reached:
                    reached.add(nxt)
                    queue.append(nxt)
        if len(reached) == mask.bit_count():
            out.append(mask)
    return tuple(out)


def animal_delete_sink(mask, width, height):
    if mask == 0 or mask == 1:
        return mask
    sinks = []
    for cell in range(width * height):
        if not (mask >> cell) & 1 or cell == 0:
            continue
        x, y = cell % width, cell // width
        east = x + 1 < width and (mask >> (cell + 1)) & 1
        north = y + 1 < height and (mask >> (cell + width)) & 1
        if not east and not north:
            sinks.append(cell)
    CHECKS.that(bool(sinks), ("animal-no-sink", mask, width, height))
    return mask ^ (1 << max(sinks))


def gravity(mask, width, height):
    moving = []
    for cell in range(width, width * height):
        if mask >> cell & 1 and not (mask >> (cell - width)) & 1:
            moving.append(cell)
    out = mask
    for cell in moving:
        out ^= 1 << cell
        out ^= 1 << (cell - width)
    return out


def packed_columns(mask, width, height):
    out = 0
    for x in range(width):
        count = sum((mask >> (y * width + x)) & 1 for y in range(height))
        for y in range(count):
            out |= 1 << (y * width + x)
    return out


def focused_lattice():
    before = CHECKS.n
    for width, height in ((2, 2), (3, 2), (3, 3), (4, 3)):
        for animal in directed_animals(width, height):
            target, depth = iterate_to_fixed(
                animal, lambda x, w=width, h=height: animal_delete_sink(x, w, h))
            expected = max(0, animal.bit_count() - 1)
            CHECKS.that(depth == expected, ("DA1-depth", width, height, animal, depth))
            CHECKS.that(target in (0, 1), ("DA1-target", width, height, animal, target))
    for width, height in ((2, 3), (3, 3), (3, 4)):
        for mask in range(1 << (width * height)):
            target, _ = iterate_to_fixed(mask, lambda x, w=width, h=height: gravity(x, w, h))
            CHECKS.that(target == packed_columns(mask, width, height),
                        ("LA1-target", width, height, mask, target))
    assertions = CHECKS.n - before
    print(f"FOCUS LATTICE | directed_animal_clock_and_gravity_endpoint=PASS | assertions={assertions}")
    return assertions


def main():
    rows = []
    rows.append(scan_family("FM1_CYCLE_OPEN", endofunction_instances(fm_cycle_open, 6)))
    rows.append(scan_family("FM2_LEAF_LOOP", endofunction_instances(fm_leaf_loop, 6)))
    rows.append(scan_family("FM3_CYCLE_EXCISE", endofunction_instances(fm_cycle_excision, 6)))
    rows.append(scan_family("FM4_COMPONENT_MIN", endofunction_instances(fm_component_min_root, 5)))

    for ident, phi in (
        ("HF1_MAX_DELETE", hf_max_delete),
        ("HF2_DEGREE_DELETE", hf_degree_delete),
        ("HF3_PAIR_INTERSECT", hf_pair_intersections),
        ("HF4_LEAF_STRIP", hf_incidence_leaf_strip),
    ):
        rows.append(scan_family(
            ident,
            [(f"n={n}", tuple(all_hypergraphs(n)), lambda x, n=n, p=phi: p(x, n))
             for n in range(1, 5)],
        ))
    rows.append(scan_family(
        "SC1_PREFIX_DELETE",
        [(f"n={n}", complexes(n), lambda x, n=n: sc_prefix_delete(x, n))
         for n in range(1, 5)],
    ))
    rows.append(scan_family(
        "CL1_DEGREE_DELETE",
        [(f"n={n}", clutters(n), lambda x, n=n: cl_degree_delete(x, n))
         for n in range(1, 5)],
    ))

    rows.append(scan_family(
        "OI1_PIVOT_EXCHANGE",
        [(f"crown={m}", ideals(crown_predecessors(m)),
          lambda x, p=crown_predecessors(m): oi_pivot_exchange(x, p))
         for m in range(3, 7)],
    ))
    rows.append(scan_family(
        "OI2_PRINCIPAL_PARITY",
        [(f"crown={m}", ideals(crown_predecessors(m)),
          lambda x, p=crown_predecessors(m): oi_principal_parity(x, p))
         for m in range(3, 7)],
    ))
    rows.append(scan_family(
        "AC1_PARENT_CONTRACT",
        [(f"height={h}", antichains(binary_tree_predecessors(h)),
          lambda x, p=binary_tree_predecessors(h): ac_parent_contract(x, p))
         for h in range(4)],
    ))
    poset_states = tuple((n, preds) for n in range(6) for preds in natural_posets(n))
    rows.append(scan_family("PO1_DELETE_MAXIMAL", [("n<=5", poset_states, delete_least_maximal_poset)]))

    tableau_states = tuple(tableau for n in range(9) for tableau in tableaux(n))
    rows.append(scan_family("YT1_DELETE_MAX", [("n<=8", tableau_states, tableau_delete_max)]))
    rows.append(scan_family(
        "YT2_RELOCATE_MAX",
        [(f"n={n}", tableaux(n), tableau_relocate_max_first_row) for n in range(1, 9)],
    ))

    pp_instances = []
    for a, b, h in ((2, 1, 3), (2, 2, 3), (2, 3, 2)):
        states = plane_partitions(a, b, h)
        pp_instances.append((f"{a}x{b}x{h}", states,
                             lambda x, a=a, b=b: pp_corner_wave(x, a, b)))
    rows.append(scan_family("PP1_CORNER_WAVE", pp_instances))
    pp_instances = []
    for a, b, h in ((2, 1, 3), (2, 2, 3), (2, 3, 2)):
        states = plane_partitions(a, b, h)
        pp_instances.append((f"{a}x{b}x{h}", states,
                             lambda x, a=a, b=b: pp_parity_corner(x, a, b)))
    rows.append(scan_family("PP2_PARITY_CORNER", pp_instances))

    animal_instances = []
    for width, height in ((2, 2), (3, 2), (3, 3), (4, 3)):
        animal_instances.append((
            f"{width}x{height}", directed_animals(width, height),
            lambda x, w=width, h=height: animal_delete_sink(x, w, h),
        ))
    rows.append(scan_family("DA1_DELETE_SINK", animal_instances))
    rows.append(scan_family(
        "LA1_SOUTH_GRAVITY",
        [(f"{w}x{h}", tuple(range(1 << (w * h))),
          lambda x, w=w, h=h: gravity(x, w, h))
         for w, h in ((2, 3), (3, 3), (3, 4))],
    ))

    CHECKS.that(len(rows) == 20, ("literal-system-count", len(rows)))
    focused_cycle_open()
    focused_leaf_loop()
    focused_cycle_excision()
    focused_hf_max_delete()
    focused_rank_clocks()
    focused_poset_reductions()
    focused_tableaux()
    focused_lattice()

    state_total = sum(row.states for row in rows)
    print(f"SUMMARY | literal_systems={len(rows)} | parameter_states={state_total} | assertions={CHECKS.n} | PASS")


if __name__ == "__main__":
    main()
