#!/usr/bin/env python3
"""Dependency-free exact checks for the P197--P201 replacement breadth lane.

The script deliberately reimplements every literal map in this directory.  It
does not import author, paper, or earlier scouting code.  The output is kept
deterministic so that two fresh-process runs can be compared byte for byte.
"""

from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def orbit_data(update, state):
    seen = {}
    x = state
    while x not in seen:
        seen[x] = len(seen)
        x = update(x)
    return seen[x], len(seen) - seen[x]


def surj(n, k):
    if n == 0:
        return int(k == 0)
    if k == 0 or k > n:
        return 0
    return sum((-1) ** j * comb(k, j) * (k - j) ** n for j in range(k + 1))


def chromatic_krs(r, s, q):
    """Number of proper labelled q-colourings of K_{r,s}, r,s>0."""
    return sum(comb(q, k) * surj(r, k) * (q - k) ** s
               for k in range(1, min(r, q) + 1))


def proper_krs(x, r):
    return set(x[:r]).isdisjoint(x[r:])


def lzk_update_literal(x, r):
    """Least-zero {0,1}-Kempe-component swap, by an actual BFS."""
    if 0 not in x:
        return x
    n = len(x)
    start = x.index(0)
    active = {i for i, a in enumerate(x) if a in (0, 1)}
    component = {start}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u < r:
            neighbours = range(r, n)
        else:
            neighbours = range(r)
        for v in neighbours:
            if v in active and v not in component:
                component.add(v)
                queue.append(v)
    y = list(x)
    for i in component:
        y[i] = 1 - y[i]
    return tuple(y)


def lzk_update_closed(x, r):
    if 0 not in x:
        return x
    z = x.index(0)
    opposite = range(r, len(x)) if z < r else range(r)
    if any(x[i] == 1 for i in opposite):
        return tuple(1 - a if a in (0, 1) else a for a in x)
    y = list(x)
    y[z] = 1
    return tuple(y)


def lzk_class(x, r):
    if 0 not in x:
        return "fixed"
    z = x.index(0)
    opposite = range(r, len(x)) if z < r else range(r)
    return "opposite" if any(x[i] == 1 for i in opposite) else "transient"


def lzk_opposite_count(r, s, q):
    total = 0
    for a in range(q - 1):
        for b in range(q - 1 - a):
            ways = factorial(q - 2) // (
                factorial(a) * factorial(b) * factorial(q - 2 - a - b)
            )
            total += ways * surj(r, a + 1) * surj(s, b + 1)
    return 2 * total


def lzk_transient_depth_count(u, v, q, d):
    """Transient colourings with d zeros on a prescribed side of size u."""
    if d < 1 or d > u:
        return 0
    residual = 0
    for a in range(q - 1):
        for b in range(q - 1 - a):
            ways = factorial(q - 2) // (
                factorial(a) * factorial(b) * factorial(q - 2 - a - b)
            )
            residual += ways * (surj(u - d, a) + surj(u - d, a + 1)) \
                * surj(v, b)
    return comb(u, d) * residual


def lzk_expected_t_fibre(y, r, t):
    kind = lzk_class(y, r)
    if kind == "opposite":
        return 1
    if kind == "fixed":
        ones = y.count(1)
        return sum(comb(ones, j) for j in range(min(t, ones) + 1))
    first_zero = y.index(0)
    same_side = range(r) if first_zero < r else range(r, len(y))
    available = sum(y[i] == 1 and i < first_zero for i in same_side)
    return comb(available, t) if t <= available else 0


def audit_lzk():
    boxes = [(2, 1, 1), (2, 2, 3), (3, 1, 1), (3, 2, 3),
             (3, 3, 4), (4, 3, 4), (5, 3, 4)]
    rows = []
    for q, r, s in boxes:
        states = [x for x in product(range(q), repeat=r + s)
                  if proper_krs(x, r)]
        check(len(states) == chromatic_krs(r, s, q), "LZK state census")
        state_set = set(states)
        update = lambda x: lzk_update_literal(x, r)
        images = []
        for x in states:
            y = update(x)
            check(y in state_set, "LZK closure")
            check(y == lzk_update_closed(x, r), "LZK closed form")
            depth, period = orbit_data(update, x)
            kind = lzk_class(x, r)
            if kind == "fixed":
                check((depth, period) == (0, 1), "LZK fixed orbit")
            elif kind == "opposite":
                check((depth, period) == (0, 2), "LZK opposite orbit")
            else:
                check((depth, period) == (x.count(0), 1), "LZK zero clock")
            images.append(y)

        fixed = sum(lzk_class(x, r) == "fixed" for x in states)
        opposite = sum(lzk_class(x, r) == "opposite" for x in states)
        check(fixed == chromatic_krs(r, s, q - 1), "LZK fixed census")
        check(opposite == lzk_opposite_count(r, s, q), "LZK two-cycle census")
        check(opposite % 2 == 0, "LZK oriented/two-cycle division")

        current = {x: x for x in states}
        for t in range(r + s + 2):
            fibre = Counter(current.values())
            for y in states:
                expected = lzk_expected_t_fibre(y, r, t)
                check(fibre[y] == expected,
                      "LZK all-time target fibre q,r,s,t,y="
                      f"{q,r,s,t,y}: {fibre[y]} != {expected}")
            current = {x: update(current[x]) for x in states}

        indegree = Counter(images)
        depths = Counter(orbit_data(update, x)[0] for x in states)
        periods = sorted({orbit_data(update, x)[1] for x in states})
        for d in range(1, max(r, s) + 1):
            expected_layer = lzk_transient_depth_count(r, s, q, d) \
                + lzk_transient_depth_count(s, r, q, d)
            check(depths[d] == expected_layer, "LZK exact depth census")
        if q == 2:
            check(len(states) == 2 and periods == [2], "LZK q=2 boundary")
            check(max(depths) == 0 and max(indegree.values()) == 1,
                  "LZK q=2 no transient boundary")
        else:
            check(max(depths) == max(r, s), "LZK sharp tail")
            check(max(indegree.values()) == max(r, s) + 1,
                  "LZK sharp one-step fibre")
        rows.append((q, r, s, len(states), len(indegree), fixed + opposite,
                     max(depths), max(indegree.values()), fixed,
                     opposite // 2))

    print("LZK least-zero Kempe on proper K_rs colourings")
    for row in rows:
        print("  q=%d r=%d s=%d states=%d image=%d recurrent=%d "
              "max_tail=%d max_fibre=%d fixed=%d two_cycles=%d" % row)


def proper_path_word(x):
    return all(a != b for a, b in zip(x, x[1:]))


def pzk_update(x):
    if 0 not in x:
        return x
    i = x.index(0)
    lo = i
    hi = i
    while lo and x[lo - 1] in (0, 1):
        lo -= 1
    while hi + 1 < len(x) and x[hi + 1] in (0, 1):
        hi += 1
    y = list(x)
    for j in range(lo, hi + 1):
        y[j] = 1 - y[j]
    return tuple(y)


def pzk_expected_orbit(x):
    depth = 0
    i = 0
    while i < len(x):
        if x[i] >= 2:
            i += 1
            continue
        j = i
        while j < len(x) and x[j] in (0, 1):
            j += 1
        block = x[i:j]
        if 0 in block:
            if len(block) >= 2:
                return depth, 2
            depth += 1
        i = j
    return depth, 1


def audit_pzk():
    rows = []
    for q, n in [(3, 6), (3, 10), (4, 8), (4, 10)]:
        states = [x for x in product(range(q), repeat=n) if proper_path_word(x)]
        check(len(states) == q * (q - 1) ** (n - 1), "PZK state count")
        image = Counter()
        depth_hist = Counter()
        periods = set()
        for x in states:
            y = pzk_update(x)
            check(proper_path_word(y), "PZK closure")
            got = orbit_data(pzk_update, x)
            check(got == pzk_expected_orbit(x), "PZK block clock")
            depth_hist[got[0]] += 1
            periods.add(got[1])
            image[y] += 1
        fixed = (q - 1) * (q - 2) ** (n - 1)
        check(sum(pzk_update(x) == x for x in states) == fixed, "PZK fixed census")
        check(max(depth_hist) == (n + 1) // 2, "PZK sharp tail")
        check(periods == {1, 2}, "PZK period support")
        check(max(image.values()) == (n + 1) // 2 + 1, "PZK max fibre")
        recurrent = sum(orbit_data(pzk_update, x)[0] == 0 for x in states)
        rows.append((q, n, len(states), len(image), recurrent,
                     max(depth_hist), max(image.values())))
    print("PZK least-zero Kempe on properly edge-coloured paths")
    for row in rows:
        print("  q=%d n=%d states=%d image=%d recurrent=%d "
              "max_tail=%d max_fibre=%d" % row)


def rectangle_list(r, s):
    return [(i, k, j, ell) for i, k in combinations(range(r), 2)
            for j, ell in combinations(range(s), 2)]


def alternating_rectangle(mask, rect, s):
    i, k, j, ell = rect
    bits = tuple((mask >> (a * s + b)) & 1
                 for a, b in ((i, j), (i, ell), (k, j), (k, ell)))
    return bits in ((1, 0, 0, 1), (0, 1, 1, 0))


def lfas_setup(r, s):
    rects = rectangle_list(r, s)
    flips = []
    for i, k, j, ell in rects:
        flips.append(sum(1 << (a * s + b)
                         for a, b in ((i, j), (i, ell), (k, j), (k, ell))))

    def selector(mask):
        for idx, rect in enumerate(rects):
            if alternating_rectangle(mask, rect, s):
                return idx
        return -1

    def update(mask):
        idx = selector(mask)
        return mask if idx < 0 else mask ^ flips[idx]

    return rects, flips, selector, update


@lru_cache(maxsize=None)
def stirling2(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)


def lonesum_count(r, s):
    return sum(factorial(k) ** 2 * stirling2(r + 1, k + 1)
               * stirling2(s + 1, k + 1)
               for k in range(min(r, s) + 1))


def audit_lfas():
    rows = []
    for r, s in [(2, 2), (2, 4), (3, 3), (3, 4), (4, 4)]:
        rects, flips, selector, update = lfas_setup(r, s)
        states = range(1 << (r * s))
        image = Counter(update(x) for x in states)
        fixed = 0
        depth_hist = Counter()
        periods = set()
        for x in states:
            q = selector(x)
            y = update(x)
            q2 = selector(y)
            if q < 0:
                fixed += 1
                check(y == x, "LFAS fixed update")
            else:
                check(q2 <= q, "LFAS selector monotonicity")
                # Every alternating switch preserves all row and column sums.
                for i in range(r):
                    check(sum((x >> (i * s + j)) & 1 for j in range(s)) ==
                          sum((y >> (i * s + j)) & 1 for j in range(s)),
                          "LFAS row margin")
                for j in range(s):
                    check(sum((x >> (i * s + j)) & 1 for i in range(r)) ==
                          sum((y >> (i * s + j)) & 1 for i in range(r)),
                          "LFAS column margin")
                if q2 == q:
                    check(update(y) == x, "LFAS equality gives two-cycle")
            d, p = orbit_data(update, x)
            check(p in (1, 2), "LFAS period classification")
            check(d <= max(0, len(rects) - 1), "LFAS scheduler bound")
            depth_hist[d] += 1
            periods.add(p)

        check(fixed == lonesum_count(r, s), "LFAS lonesum census")
        for target in states:
            atlas = int(selector(target) < 0)
            for idx, rect in enumerate(rects):
                if alternating_rectangle(target, rect, s):
                    source = target ^ flips[idx]
                    atlas += int(selector(source) == idx)
            check(image[target] == atlas, "LFAS every-target atlas")
        rows.append((r, s, 1 << (r * s), len(image), fixed,
                     max(depth_hist), max(image.values()), tuple(sorted(periods))))
    print("LFAS least alternating-rectangle switch")
    for row in rows:
        print("  r=%d s=%d states=%d image=%d fixed=%d max_tail=%d "
              "max_fibre=%d periods=%s" % row)


def tournament_setup(n):
    edges = list(combinations(range(n), 2))
    edge_index = {e: i for i, e in enumerate(edges)}
    triangles = list(combinations(range(n), 3))
    flips = [sum(1 << edge_index[e] for e in combinations(t, 2))
             for t in triangles]

    def arrow(mask, u, v):
        if u < v:
            return (mask >> edge_index[u, v]) & 1
        return 1 - ((mask >> edge_index[v, u]) & 1)

    def cyclic(mask, tri):
        i, j, k = tri
        return (arrow(mask, i, j), arrow(mask, j, k), arrow(mask, i, k)) \
            in ((1, 1, 0), (0, 0, 1))

    def selector(mask):
        for idx, tri in enumerate(triangles):
            if cyclic(mask, tri):
                return idx
        return -1

    def update(mask):
        idx = selector(mask)
        return mask if idx < 0 else mask ^ flips[idx]

    def scores(mask):
        return tuple(sum(arrow(mask, i, j) for j in range(n) if j != i)
                     for i in range(n))

    return triangles, flips, cyclic, selector, update, scores


def audit_lfctr():
    rows = []
    for n in range(3, 7):
        triangles, flips, cyclic, selector, update, scores = tournament_setup(n)
        states = range(1 << comb(n, 2))
        image = Counter(update(x) for x in states)
        fixed = 0
        depths = Counter()
        periods = set()
        for x in states:
            q = selector(x)
            y = update(x)
            if q < 0:
                fixed += 1
            else:
                check(scores(y) == scores(x), "LFCTR score preservation")
                check(selector(y) <= q, "LFCTR selector monotonicity")
            d, p = orbit_data(update, x)
            check(p in (1, 2), "LFCTR period classification")
            depths[d] += 1
            periods.add(p)
        check(fixed == factorial(n), "LFCTR transitive fixed census")
        for target in states:
            atlas = int(selector(target) < 0)
            for idx, tri in enumerate(triangles):
                if cyclic(target, tri):
                    atlas += int(selector(target ^ flips[idx]) == idx)
            check(image[target] == atlas, "LFCTR target atlas")
        rows.append((n, 1 << comb(n, 2), len(image), fixed, max(depths),
                     max(image.values()), tuple(sorted(periods))))
    print("LFCTR lex-first cyclic-triangle reversal (pilot-only sharp rows)")
    for row in rows:
        print("  n=%d states=%d image=%d fixed=%d max_tail=%d "
              "max_fibre=%d periods=%s" % row)


def graph_setup(n):
    edges = list(combinations(range(n), 2))
    edge_index = {e: i for i, e in enumerate(edges)}

    def components(mask):
        unseen = set(range(n))
        out = []
        while unseen:
            root = min(unseen)
            block = {root}
            stack = [root]
            unseen.remove(root)
            while stack:
                u = stack.pop()
                for v in list(unseen):
                    e = (u, v) if u < v else (v, u)
                    if (mask >> edge_index[e]) & 1:
                        unseen.remove(v)
                        block.add(v)
                        stack.append(v)
            out.append(tuple(sorted(block)))
        return out

    def bridges(mask):
        base_components = len(components(mask))
        out = 0
        for idx, edge in enumerate(edges):
            if (mask >> idx) & 1 and len(components(mask ^ (1 << idx))) > base_components:
                out |= 1 << idx
        return out

    def update(mask):
        return mask & ~bridges(mask)

    return edges, components, bridges, update


def is_forest_on_vertices(c, chosen_edges):
    parent = list(range(c))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for i, j in chosen_edges:
        a, b = find(i), find(j)
        if a == b:
            return False
        parent[a] = b
    return True


def weighted_component_forest_count(sizes):
    c = len(sizes)
    pairs = list(combinations(range(c), 2))
    total = 0
    for bits in range(1 << len(pairs)):
        selected = [pairs[i] for i in range(len(pairs)) if (bits >> i) & 1]
        if is_forest_on_vertices(c, selected):
            weight = 1
            for i, j in selected:
                weight *= sizes[i] * sizes[j]
            total += weight
    return total


def audit_bridge_deletion():
    rows = []
    for n in range(1, 6):
        edges, components, bridges, update = graph_setup(n)
        states = range(1 << len(edges))
        image = Counter(update(x) for x in states)
        fixed = 0
        for x in states:
            y = update(x)
            check(update(y) == y, "BDC idempotence")
            fixed += y == x
        for target in states:
            if bridges(target):
                expected = 0
            else:
                expected = weighted_component_forest_count(
                    tuple(len(c) for c in components(target)))
            check(image[target] == expected, "BDC weighted-forest fibre")
        rows.append((n, 1 << len(edges), len(image), fixed, max(image.values())))
    print("BDC simultaneous bridge deletion")
    for row in rows:
        print("  n=%d states=%d image=fixed=%d fixed_check=%d max_fibre=%d" % row)


def matching_masks(n):
    edges = list(combinations(range(n), 2))
    edge_index = {e: i for i, e in enumerate(edges)}
    out = []

    def rec(available, mask):
        if not available:
            out.append(mask)
            return
        a = min(available)
        rest = set(available)
        rest.remove(a)
        rec(rest, mask)
        for b in sorted(rest):
            nxt = set(rest)
            nxt.remove(b)
            rec(nxt, mask | (1 << edge_index[a, b]))

    rec(set(range(n)), 0)
    return edges, edge_index, out


def audit_gmp():
    rows = []
    for n in range(1, 11):
        edges, edge_index, states = matching_masks(n)

        def monomers(mask):
            used = set()
            for idx, (a, b) in enumerate(edges):
                if (mask >> idx) & 1:
                    used.update((a, b))
            return tuple(i for i in range(n) if i not in used)

        def update(mask):
            u = monomers(mask)
            if len(u) < 2:
                return mask
            return mask | (1 << edge_index[u[0], u[1]])

        image = Counter(update(x) for x in states)
        depth_hist = Counter()
        for x in states:
            d, p = orbit_data(update, x)
            check(p == 1 and d == len(monomers(x)) // 2, "GMP deficiency clock")
            depth_hist[d] += 1
        for target in states:
            u = monomers(target)
            cutoff = min(u) if u else n
            expected = int(len(u) <= 1)
            for idx, (a, b) in enumerate(edges):
                if (target >> idx) & 1 and b < cutoff:
                    expected += 1
            check(image[target] == expected, "GMP target fibre")
        rows.append((n, len(states), len(image), max(depth_hist), max(image.values())))
    print("GMP greedy least-monomer pairing")
    for row in rows:
        print("  n=%d states=%d image=%d max_tail=%d max_fibre=%d" % row)


def oriented_decode(n, code):
    edges = list(combinations(range(n), 2))
    arcs = [set() for _ in range(n)]
    z = code
    for a, b in edges:
        digit = z % 3
        z //= 3
        if digit == 1:
            arcs[a].add(b)
        elif digit == 2:
            arcs[b].add(a)
    return edges, arcs


def oriented_encode(n, arcs):
    value = 0
    place = 1
    for a, b in combinations(range(n), 2):
        digit = 1 if b in arcs[a] else 2 if a in arcs[b] else 0
        value += place * digit
        place *= 3
    return value


def scc_partition(arcs):
    n = len(arcs)
    reach = []
    for root in range(n):
        seen = {root}
        stack = [root]
        while stack:
            u = stack.pop()
            for v in arcs[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        reach.append(seen)
    unseen = set(range(n))
    blocks = []
    while unseen:
        a = min(unseen)
        block = {b for b in unseen if b in reach[a] and a in reach[b]}
        unseen -= block
        blocks.append(tuple(sorted(block)))
    return tuple(blocks)


def scr_update(n, code):
    _, arcs = oriented_decode(n, code)
    blocks = scc_partition(arcs)
    block_of = {v: i for i, block in enumerate(blocks) for v in block}
    out = [set() for _ in range(n)]
    for u in range(n):
        for v in arcs[u]:
            if block_of[u] == block_of[v]:
                out[v].add(u)
            else:
                out[u].add(v)
    return oriented_encode(n, out)


def audit_scr():
    dag_counts = [1, 1, 3, 25, 543, 29281]
    rows = []
    for n in range(1, 6):
        total = 3 ** comb(n, 2)
        fixed = 0
        for x in range(total):
            _, arcs = oriented_decode(n, x)
            y = scr_update(n, x)
            _, arcs_y = oriented_decode(n, y)
            check(scc_partition(arcs) == scc_partition(arcs_y), "SCR SCC invariant")
            check(scr_update(n, y) == x, "SCR involution")
            is_dag = all(len(block) == 1 for block in scc_partition(arcs))
            check((y == x) == is_dag, "SCR fixed iff DAG")
            fixed += y == x
        check(fixed == dag_counts[n], "SCR DAG census")
        rows.append((n, total, fixed, (total - fixed) // 2))
    print("SCR reverse every strongly connected component")
    for row in rows:
        print("  n=%d states=%d fixed_DAG=%d two_cycles=%d" % row)


def audit_hci():
    rows = []
    for n, k in [(4, 3), (5, 3)]:
        hedges = list(combinations(range(n), k))
        conflict = [[False] * len(hedges) for _ in hedges]
        for i, e in enumerate(hedges):
            for j, f in enumerate(hedges):
                conflict[i][j] = i != j and len(set(e) & set(f)) >= 2

        def update(mask):
            out = 0
            for i in range(len(hedges)):
                if not ((mask >> i) & 1):
                    continue
                if not any((mask >> j) & 1 and conflict[i][j]
                           for j in range(len(hedges))):
                    out |= 1 << i
            return out

        states = range(1 << len(hedges))
        image = Counter(update(x) for x in states)
        fixed = 0
        for x in states:
            y = update(x)
            check(update(y) == y, "HCI idempotence")
            fixed += x == y
        for target in states:
            if update(target) != target:
                expected = 0
            else:
                pool = [i for i in range(len(hedges))
                        if not ((target >> i) & 1)
                        and not any((target >> j) & 1 and conflict[i][j]
                                    for j in range(len(hedges)))]
                expected = 0
                for bits in range(1 << len(pool)):
                    chosen = [pool[a] for a in range(len(pool)) if (bits >> a) & 1]
                    if all(any(conflict[i][j] for j in chosen if j != i)
                           for i in chosen):
                        expected += 1
            check(image[target] == expected, "HCI conflict-graph fibre")
        rows.append((n, k, 1 << len(hedges), len(image), fixed, max(image.values())))
    print("HCI isolate linear edges of a uniform hypergraph")
    for row in rows:
        print("  n=%d k=%d states=%d image=fixed=%d fixed_check=%d max_fibre=%d" % row)


def permutation_cycles(p):
    n = len(p)
    seen = set()
    cycles = []
    for a in range(n):
        if a in seen:
            continue
        cyc = []
        x = a
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = p[x]
        cycles.append(tuple(cyc))
    return cycles


def oci_update(p):
    out = list(p)
    for cyc in permutation_cycles(p):
        if len(cyc) % 2 == 1:
            for a in cyc:
                out[p[a]] = a
    return tuple(out)


def oci_fixed_count(n):
    # EGF exp(x)/sqrt(1-x^2): odd cycles of length >=3 are forbidden.
    total = 0
    for pairs in range(n // 2 + 1):
        even_support = 2 * pairs
        # Number of permutations on the chosen support with only even cycles.
        even_cycle_perms = 0
        for p in permutations(range(even_support)):
            if all(len(c) % 2 == 0 for c in permutation_cycles(p)):
                even_cycle_perms += 1
        total += comb(n, even_support) * even_cycle_perms
    return total


def audit_oci():
    rows = []
    for n in range(1, 9):
        states = list(permutations(range(n)))
        fixed = 0
        for p in states:
            y = oci_update(p)
            check(oci_update(y) == p, "OCI involution")
            criterion = all(len(c) == 1 or len(c) % 2 == 0
                            for c in permutation_cycles(p))
            check((y == p) == criterion, "OCI fixed cycle criterion")
            fixed += y == p
        check(fixed == oci_fixed_count(n), "OCI EGF census")
        rows.append((n, len(states), fixed, (len(states) - fixed) // 2))
    print("OCI invert every odd permutation cycle")
    for row in rows:
        print("  n=%d states=%d fixed=%d two_cycles=%d" % row)


def main():
    audit_lzk()
    audit_pzk()
    audit_lfas()
    audit_lfctr()
    audit_bridge_deletion()
    audit_gmp()
    audit_scr()
    audit_hci()
    audit_oci()
    print(f"TOTAL_ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
