#!/usr/bin/env python3
"""Exact breadth pilot for the P127--P131 combinatorial scouting lane.

Only the Python standard library is used.  The program deliberately mixes
strong and weak candidates: its job is to falsify cheap guesses and record a
deterministic finite-map fingerprint before any theorem promotion.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product


class Checks:
    def __init__(self):
        self.n = 0

    def that(self, condition, payload=None):
        self.n += 1
        if not condition:
            raise AssertionError(payload)


def functional_fingerprint(states, phi, checks):
    states = tuple(states)
    universe = set(states)
    checks.that(len(universe) == len(states), "duplicate states")
    successor = {}
    for state in states:
        image = phi(state)
        checks.that(image in universe, (state, image, "closure"))
        successor[state] = image

    max_tail = 0
    periods = set()
    periodic_nodes = set()
    for start in states:
        seen = {}
        orbit = []
        cur = start
        while cur not in seen:
            checks.that(cur in universe, (start, cur, "orbit closure"))
            seen[cur] = len(orbit)
            orbit.append(cur)
            cur = successor[cur]
            checks.that(len(orbit) <= len(states) + 1, (start, "orbit bound"))
        tail = seen[cur]
        period = len(orbit) - tail
        checks.that(period >= 1, (start, tail, period))
        max_tail = max(max_tail, tail)
        periods.add(period)
        periodic_nodes.update(orbit[tail:])

    image_size = len(set(successor.values()))
    fixed = sum(successor[s] == s for s in states)
    idempotent = all(successor[successor[s]] == successor[s] for s in states)
    involution = all(successor[successor[s]] == s for s in states)
    injective = image_size == len(states)
    return {
        "N": len(states),
        "image": image_size,
        "fixed": fixed,
        "periodic": len(periodic_nodes),
        "tail": max_tail,
        "periods": tuple(sorted(periods)),
        "idempotent": idempotent,
        "involution": involution,
        "injective": injective,
    }


def run_candidate(code, scope, datasets, phi_factory, extra_check=None):
    checks = Checks()
    rows = []
    total_states = 0
    for parameter, states in datasets:
        states = tuple(states)
        phi = phi_factory(parameter)
        row = functional_fingerprint(states, phi, checks)
        if extra_check is not None:
            extra_check(parameter, states, phi, row, checks)
        rows.append((parameter, row))
        total_states += len(states)
    last_parameter, last = rows[-1]
    periods = sorted({p for _, row in rows for p in row["periods"]})
    max_tail = max(row["tail"] for _, row in rows)
    flags = (
        f"idem={int(all(row['idempotent'] for _, row in rows))},"
        f"inv={int(all(row['involution'] for _, row in rows))},"
        f"inj={int(all(row['injective'] for _, row in rows))}"
    )
    print(
        f"{code} | scope={scope} | states={total_states} | "
        f"last={last_parameter}:N{last['N']}/im{last['image']}/fix{last['fixed']} | "
        f"tail={max_tail} | periods={','.join(map(str, periods))} | {flags} | "
        f"assertions={checks.n}"
    )
    return checks.n, rows


# ---------------------------------------------------------------------------
# Posets and order ideals


def transitive_closure(n, covers):
    below = [0] * n
    for a, b in covers:
        below[b] |= 1 << a
    changed = True
    while changed:
        changed = False
        for b in range(n):
            old = below[b]
            x = old
            while x:
                bit = x & -x
                a = bit.bit_length() - 1
                below[b] |= below[a]
                x -= bit
            changed |= below[b] != old
    return tuple(below)


def ideals_of_poset(below):
    n = len(below)
    return tuple(mask for mask in range(1 << n)
                 if all(not (mask >> x & 1) or below[x] & ~mask == 0
                        for x in range(n)))


def fence_poset(n):
    covers = []
    for i in range(n - 1):
        if i % 2 == 0:
            covers.append((i, i + 1))
        else:
            covers.append((i + 1, i))
    return transitive_closure(n, covers)


def grid_poset(a, b):
    covers = []
    idx = lambda i, j: i * b + j
    for i in range(a):
        for j in range(b):
            if i + 1 < a:
                covers.append((idx(i, j), idx(i + 1, j)))
            if j + 1 < b:
                covers.append((idx(i, j), idx(i, j + 1)))
    return transitive_closure(a * b, covers)


def minimal_outside(mask, below):
    n = len(below)
    return [x for x in range(n) if not (mask >> x & 1) and below[x] & ~mask == 0]


def maximal_inside(mask, below):
    n = len(below)
    above = [0] * n
    for y in range(n):
        x = below[y]
        while x:
            bit = x & -x
            above[bit.bit_length() - 1] |= 1 << y
            x -= bit
    return [x for x in range(n) if mask >> x & 1 and above[x] & mask == 0]


def cardinality_boundary_wave(below):
    def phi(mask):
        if mask.bit_count() % 2 == 0:
            for x in minimal_outside(mask, below):
                mask |= 1 << x
        else:
            for x in maximal_inside(mask, below):
                mask &= ~(1 << x)
        return mask
    return phi


def frontier_boundary_wave(below):
    def phi(mask):
        maxima = maximal_inside(mask, below)
        if len(maxima) % 2:
            for x in maxima:
                mask &= ~(1 << x)
        else:
            for x in minimal_outside(mask, below):
                mask |= 1 << x
        return mask
    return phi


def labelled_posets(n):
    pairs = tuple(combinations(range(n), 2))
    out = []
    for choices in product((0, 1, 2), repeat=len(pairs)):
        rel = [0] * n
        for (a, b), choice in zip(pairs, choices):
            if choice == 1:
                rel[a] |= 1 << b
            elif choice == 2:
                rel[b] |= 1 << a
        good = True
        for a in range(n):
            for b in range(n):
                if rel[a] >> b & 1:
                    if rel[b] >> a & 1:
                        good = False
                        break
                    if rel[b] & ~rel[a]:
                        good = False
                        break
            if not good:
                break
        if good:
            out.append(tuple(rel))
    return tuple(out)


def cover_count(rel):
    n = len(rel)
    ans = 0
    for a in range(n):
        for b in range(n):
            if rel[a] >> b & 1:
                middle = rel[a] & sum(1 << k for k in range(n) if rel[k] >> b & 1)
                ans += not middle
    return ans


def dual_poset(rel):
    n = len(rel)
    return tuple(sum((1 << a) for a in range(n) if rel[a] >> b & 1)
                 for b in range(n))


# ---------------------------------------------------------------------------
# Set systems and set partitions


def boolean_antichains(n):
    subsets = tuple(range(1 << n))
    out = []
    for family_mask in range(1 << len(subsets)):
        family = tuple(s for s in subsets if family_mask >> s & 1)
        good = True
        for i, a in enumerate(family):
            for b in family[i + 1:]:
                if a & b == a or a & b == b:
                    good = False
                    break
            if not good:
                break
        if good:
            out.append(family)
    return tuple(out)


def set_partitions(n):
    if n == 0:
        return ((),)
    out = []

    def rec(x, blocks):
        if x == n:
            out.append(tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda b: b[0])))
            return
        for i in range(len(blocks)):
            blocks[i].append(x)
            rec(x + 1, blocks)
            blocks[i].pop()
        blocks.append([x])
        rec(x + 1, blocks)
        blocks.pop()

    rec(0, [])
    return tuple(out)


def rotate_selected_extrema(partition, odd_blocks=True, minima=True, reverse=False):
    blocks = [set(b) for b in partition]
    selected = [i for i, b in enumerate(blocks)
                if (len(b) % 2 == 1) == odd_blocks]
    if len(selected) < 2:
        return partition
    values = [min(blocks[i]) if minima else max(blocks[i]) for i in selected]
    shifted = values[-1:] + values[:-1] if reverse else values[1:] + values[:1]
    for i, old, new in zip(selected, values, shifted):
        blocks[i].remove(old)
        blocks[i].add(new)
    return tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda b: b[0]))


def ordered_set_partitions(n):
    out = []
    for partition in set_partitions(n):
        out.extend(permutations(partition))
    return tuple(out)


# ---------------------------------------------------------------------------
# Young tableaux and plane partitions


def integer_partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


@lru_cache(None)
def tableaux_of_shape(shape):
    n = sum(shape)
    if n == 0:
        return ((),)
    out = []
    for r, length in enumerate(shape):
        if length == 0:
            continue
        if r + 1 < len(shape) and shape[r + 1] == length:
            continue
        smaller = list(shape)
        smaller[r] -= 1
        if smaller[r] == 0:
            smaller.pop(r)
        smaller = tuple(smaller)
        for tab in tableaux_of_shape(smaller):
            rows = [list(row) for row in tab]
            if r == len(rows):
                rows.append([])
            rows[r].append(n)
            out.append(tuple(tuple(row) for row in rows))
    return tuple(out)


def all_tableaux(n):
    return tuple(tab for shape in integer_partitions(n) for tab in tableaux_of_shape(shape))


def transpose_tableau(tab):
    width = len(tab[0]) if tab else 0
    return tuple(tuple(tab[r][c] for r in range(len(tab)) if c < len(tab[r]))
                 for c in range(width))


def descent_count(tab):
    pos = {}
    for r, row in enumerate(tab):
        for c, value in enumerate(row):
            pos[value] = (r, c)
    n = len(pos)
    return sum(pos[i + 1][0] > pos[i][0] for i in range(1, n))


def rectangular_evacuation(tab):
    a = len(tab)
    b = len(tab[0])
    n = a * b
    return tuple(tuple(n + 1 - tab[a - 1 - r][b - 1 - c] for c in range(b))
                 for r in range(a))


def plane_partitions(a, b, c):
    out = []
    cells = [(i, j) for i in range(a) for j in range(b)]
    arr = [[0] * b for _ in range(a)]

    def rec(k):
        if k == len(cells):
            out.append(tuple(tuple(row) for row in arr))
            return
        i, j = cells[k]
        upper = c
        if i:
            upper = min(upper, arr[i - 1][j])
        if j:
            upper = min(upper, arr[i][j - 1])
        for value in range(upper, -1, -1):
            arr[i][j] = value
            rec(k + 1)

    rec(0)
    return tuple(out)


def pp_complement(pp, c):
    a, b = len(pp), len(pp[0])
    return tuple(tuple(c - pp[a - 1 - i][b - 1 - j] for j in range(b))
                 for i in range(a))


def pp_toggle(pp, parity, c):
    a, b = len(pp), len(pp[0])
    out = [list(row) for row in pp]
    for i in range(a):
        for j in range(b):
            if (i + j) % 2 != parity:
                continue
            upper = c
            if i:
                upper = min(upper, pp[i - 1][j])
            if j:
                upper = min(upper, pp[i][j - 1])
            lower = 0
            if i + 1 < a:
                lower = max(lower, pp[i + 1][j])
            if j + 1 < b:
                lower = max(lower, pp[i][j + 1])
            out[i][j] = upper + lower - pp[i][j]
    return tuple(tuple(row) for row in out)


# ---------------------------------------------------------------------------
# Tilings


def weighted_words(n):
    if n == 0:
        return ((),)
    out = []
    if n >= 1:
        out.extend((1,) + w for w in weighted_words(n - 1))
    if n >= 2:
        out.extend((2,) + w for w in weighted_words(n - 2))
    return tuple(out)


def isolated_domino_token_flip(word):
    out = []
    i = 0
    while i < len(word):
        value = word[i]
        j = i
        while j < len(word) and word[j] == value:
            j += 1
        run = j - i
        if value == 1 and run == 2:
            out.append(2)
        elif value == 2 and run >= 2:
            out.extend((1, 1) * run)
        else:
            out.extend(word[i:j])
        i = j
    return tuple(out)


def grid_edges(rows, cols):
    def v(r, c):
        return r * cols + c
    edges = []
    for r in range(rows):
        for c in range(cols):
            if r + 1 < rows:
                edges.append(tuple(sorted((v(r, c), v(r + 1, c)))))
            if c + 1 < cols:
                edges.append(tuple(sorted((v(r, c), v(r, c + 1)))))
    return tuple(edges)


def perfect_matchings_graph(vertex_count, edges):
    adjacency = [[] for _ in range(vertex_count)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)

    @lru_cache(None)
    def rec(mask):
        if mask == 0:
            return ((),)
        bit = mask & -mask
        u = bit.bit_length() - 1
        out = []
        for v in adjacency[u]:
            if mask >> v & 1:
                edge = tuple(sorted((u, v)))
                for rest in rec(mask & ~(1 << u) & ~(1 << v)):
                    out.append(tuple(sorted((edge,) + rest)))
        return tuple(out)

    return rec((1 << vertex_count) - 1)


def static_cell_domino_flip(rows, cols):
    blocks = []
    for r in range(0, rows - 1, 2):
        for c in range(0, cols - 1, 2):
            v = lambda x, y: x * cols + y
            vertical = frozenset((tuple(sorted((v(r, c), v(r + 1, c)))),
                                  tuple(sorted((v(r, c + 1), v(r + 1, c + 1))))))
            horizontal = frozenset((tuple(sorted((v(r, c), v(r, c + 1)))),
                                    tuple(sorted((v(r + 1, c), v(r + 1, c + 1))))))
            blocks.append((vertical, horizontal))

    def phi(matching):
        current = set(matching)
        for vertical, horizontal in blocks:
            if vertical <= current:
                current.difference_update(vertical)
                current.update(horizontal)
            elif horizontal <= current:
                current.difference_update(horizontal)
                current.update(vertical)
        return tuple(sorted(current))
    return phi


# ---------------------------------------------------------------------------
# Uniform hypergraphs and incidence structures


def uniform_hypergraphs(n, r):
    edges = tuple(combinations(range(n), r))
    return edges, tuple(range(1 << len(edges)))


def hypergraph_degrees(mask, edges, n):
    degree = [0] * n
    for i, edge in enumerate(edges):
        if mask >> i & 1:
            for v in edge:
                degree[v] += 1
    return degree


def relabel_hypergraph(mask, edges, permutation):
    edge_index = {edge: i for i, edge in enumerate(edges)}
    out = 0
    for i, edge in enumerate(edges):
        if mask >> i & 1:
            image = tuple(sorted(permutation[v] for v in edge))
            out |= 1 << edge_index[image]
    return out


def odd_degree_rotor(mask, edges, n):
    odd = tuple(v for v, d in enumerate(hypergraph_degrees(mask, edges, n))
                if d % 2)
    if len(odd) <= 1:
        return mask
    position = {v: i for i, v in enumerate(odd)}
    permutation = tuple(
        odd[(position[v] + 1) % len(odd)] if v in position else v
        for v in range(n)
    )
    return relabel_hypergraph(mask, edges, permutation)


def imbalanced_tetra_toggle(mask, edges, n):
    edge_index = {edge: i for i, edge in enumerate(edges)}
    for vertices in combinations(range(n), 4):
        local = [edge_index[e] for e in combinations(vertices, 3)]
        count = sum(mask >> i & 1 for i in local)
        if count in (1, 3):
            for i in local:
                mask ^= 1 << i
            break
    return mask


def transpose_matrix_state(state, n):
    out = 0
    for i in range(n):
        for j in range(n):
            if state >> (i * n + j) & 1:
                out |= 1 << (j * n + i)
    return out


# ---------------------------------------------------------------------------
# Chord matchings and pairs of bipartite matchings


@lru_cache(None)
def chord_matchings(n):
    if n == 0:
        return ((),)
    vertices = tuple(range(2 * n))

    def rec(remaining):
        if not remaining:
            return ((),)
        a = remaining[0]
        out = []
        for j in range(1, len(remaining)):
            b = remaining[j]
            rest_vertices = remaining[1:j] + remaining[j + 1:]
            for rest in rec(rest_vertices):
                out.append(tuple(sorted(((a, b),) + rest)))
        return tuple(out)

    return rec(vertices)


def chords_cross(e, f):
    a, b = e
    c, d = f
    return (a < c < b < d) or (c < a < d < b)


def chords_nest(e, f):
    a, b = e
    c, d = f
    return (a < c < d < b) or (c < a < b < d)


def relation_components(matching, relation):
    n = len(matching)
    adjacency = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if relation(matching[i], matching[j]):
                adjacency[i].append(j)
                adjacency[j].append(i)
    seen = set()
    out = []
    for root in range(n):
        if root in seen:
            continue
        stack = [root]
        seen.add(root)
        component = []
        while stack:
            x = stack.pop()
            component.append(x)
            for y in adjacency[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        out.append(tuple(component))
    return tuple(out)


def isolated_crossing_uncross(matching):
    current = set(matching)
    for component in relation_components(matching, chords_cross):
        if len(component) != 2:
            continue
        e, f = (matching[i] for i in component)
        points = sorted(e + f)
        current.remove(e)
        current.remove(f)
        current.add((points[0], points[1]))
        current.add((points[2], points[3]))
    return tuple(sorted(current))


def component_normalize(matching, relation, rainbow=False):
    current = set(matching)
    for component in relation_components(matching, relation):
        if len(component) < 2:
            continue
        old = [matching[i] for i in component]
        points = sorted(v for edge in old for v in edge)
        current.difference_update(old)
        if rainbow:
            new = [(points[i], points[-1 - i]) for i in range(len(component))]
        else:
            new = [(points[2 * i], points[2 * i + 1]) for i in range(len(component))]
        current.update(tuple(sorted(edge)) for edge in new)
    return tuple(sorted(current))


def alternating_cycle_swap(pair):
    p, q = pair
    n = len(p)
    qinv = [0] * n
    for i, value in enumerate(q):
        qinv[value] = i
    h = tuple(qinv[p[i]] for i in range(n))
    seen = set()
    p2, q2 = list(p), list(q)
    for root in range(n):
        if root in seen:
            continue
        cycle = []
        x = root
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = h[x]
        if len(cycle) % 2 == 1:
            for i in cycle:
                p2[i], q2[i] = q2[i], p2[i]
    return tuple(p2), tuple(q2)


# ---------------------------------------------------------------------------
# Lattice paths, polyominoes, and graphic-matroid bases


def pseudocomplement(mask, below):
    out = 0
    for x in range(len(below)):
        if ((below[x] | (1 << x)) & mask) == 0:
            out |= 1 << x
    return out


def rectangle_paths(a, b):
    return tuple(w for w in product((0, 1), repeat=a + b)
                 if w.count(0) == a and w.count(1) == b)


def path_area(word):
    x = 0
    area = 0
    for step in word:
        if step == 0:
            x += 1
        else:
            area += x
    return area


def connected_subsets(rows, cols):
    n = rows * cols
    out = []
    for mask in range(1, 1 << n):
        start = (mask & -mask).bit_length() - 1
        seen = {start}
        stack = [start]
        while stack:
            v = stack.pop()
            r, c = divmod(v, cols)
            for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= rr < rows and 0 <= cc < cols:
                    w = rr * cols + cc
                    if mask >> w & 1 and w not in seen:
                        seen.add(w)
                        stack.append(w)
        if len(seen) == mask.bit_count():
            out.append(mask)
    return tuple(out)


def polyomino_perimeter(mask, rows, cols):
    ans = 0
    for v in range(rows * cols):
        if not (mask >> v & 1):
            continue
        r, c = divmod(v, cols)
        for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if not (0 <= rr < rows and 0 <= cc < cols) or not (mask >> (rr * cols + cc) & 1):
                ans += 1
    return ans


def reflect_polyomino(mask, rows, cols):
    out = 0
    for v in range(rows * cols):
        if mask >> v & 1:
            r, c = divmod(v, cols)
            out |= 1 << (r * cols + (cols - 1 - c))
    return out


def spanning_trees_complete(n):
    edges = tuple(combinations(range(n), 2))
    out = []
    for chosen in combinations(edges, n - 1):
        adjacency = [[] for _ in range(n)]
        for u, v in chosen:
            adjacency[u].append(v)
            adjacency[v].append(u)
        seen = {0}
        stack = [0]
        while stack:
            x = stack.pop()
            for y in adjacency[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        if len(seen) == n:
            out.append(tuple(chosen))
    return tuple(out)


def basis_exchange_tree(tree, n):
    tree_set = set(tree)
    degree = Counter(v for edge in tree for v in edge)
    if sum(degree[v] == 1 for v in range(n)) % 2 == 0:
        return tree
    all_edges = tuple(combinations(range(n), 2))
    non_tree = [e for e in all_edges if e not in tree_set]
    if not non_tree:
        return tree
    add = non_tree[0]
    adjacency = [[] for _ in range(n)]
    for e in tree:
        u, v = e
        adjacency[u].append((v, e))
        adjacency[v].append((u, e))
    parent = {add[0]: (None, None)}
    queue = deque([add[0]])
    while queue:
        x = queue.popleft()
        if x == add[1]:
            break
        for y, e in adjacency[x]:
            if y not in parent:
                parent[y] = (x, e)
                queue.append(y)
    path_edges = []
    x = add[1]
    while parent[x][0] is not None:
        x, e = parent[x]
        path_edges.append(e)
    remove = max(path_edges)
    tree_set.remove(remove)
    tree_set.add(add)
    return tuple(sorted(tree_set))


def main():
    grand_total = 0
    print("P127-P131 combinatorial breadth exact pilot")
    print("format: code | scope | states | last fingerprint | tail/periods | flags | assertions")

    datasets = [(n, ideals_of_poset(fence_poset(n))) for n in range(1, 13)]
    count, _ = run_candidate("PO1", "fence ideals n=1..12", datasets,
                             lambda n: cardinality_boundary_wave(fence_poset(n)))
    grand_total += count

    datasets = [(m, ideals_of_poset(grid_poset(2, m))) for m in range(1, 8)]
    count, _ = run_candidate("PO2", "ideals of [2]x[m], m=1..7", datasets,
                             lambda m: frontier_boundary_wave(grid_poset(2, m)))
    grand_total += count

    datasets = [(n, labelled_posets(n)) for n in range(1, 5)]
    count, _ = run_candidate(
        "PO3", "all labelled posets n=1..4", datasets,
        lambda n: (lambda rel: dual_poset(rel) if cover_count(rel) % 2 else rel))
    grand_total += count

    datasets = [(n, boolean_antichains(n)) for n in range(1, 5)]
    count, _ = run_candidate(
        "SS1", "all Boolean antichains B_n, n=1..4", datasets,
        lambda n: (lambda fam: tuple(sorted((((1 << n) - 1) ^ s for s in fam)))
                   if sum(s.bit_count() for s in fam) % 2 else fam))
    grand_total += count

    datasets = [(n, set_partitions(n)) for n in range(1, 9)]
    count, _ = run_candidate(
        "SS2", "set partitions n=1..8", datasets,
        lambda n: (lambda p: rotate_selected_extrema(p, True, True, False)))
    grand_total += count

    datasets = [(n, set_partitions(n)) for n in range(1, 9)]
    count, _ = run_candidate(
        "SS3", "set partitions n=1..8", datasets,
        lambda n: (lambda p: rotate_selected_extrema(p, False, False, True)))
    grand_total += count

    datasets = [(n, ordered_set_partitions(n)) for n in range(1, 7)]
    count, _ = run_candidate(
        "SS4", "ordered set partitions n=1..6", datasets,
        lambda n: (lambda p: p[(sum(len(b) % 2 for b in p) % len(p)):] +
                   p[:(sum(len(b) % 2 for b in p) % len(p))]))
    grand_total += count

    datasets = [(n, all_tableaux(n)) for n in range(1, 10)]
    count, _ = run_candidate(
        "TB1", "all SYT n=1..9", datasets,
        lambda n: (lambda tab: transpose_tableau(tab) if descent_count(tab) % 2 else tab))
    grand_total += count

    datasets = []
    for m in range(1, 6):
        shape = (m, m)
        datasets.append((f"2x{m}", tableaux_of_shape(shape)))
    count, _ = run_candidate(
        "TB2", "rectangular SYT 2xm, m=1..5", datasets,
        lambda label: (lambda tab: rectangular_evacuation(tab) if tab[0][-1] % 2 else tab))
    grand_total += count

    datasets = [((2, b, 2), plane_partitions(2, b, 2)) for b in range(1, 5)]
    count, _ = run_candidate(
        "PP1", "plane partitions 2xbx2, b=1..4", datasets,
        lambda abc: (lambda pp: pp_complement(pp, abc[2])
                     if sum(pp[i][i] for i in range(min(len(pp), len(pp[0])))) % 2 else pp))
    grand_total += count

    datasets = [((2, b, 2), plane_partitions(2, b, 2)) for b in range(1, 5)]
    count, _ = run_candidate(
        "PP2", "plane partitions 2xbx2, b=1..4", datasets,
        lambda abc: (lambda pp: pp_toggle(pp, sum(map(sum, pp)) % 2, abc[2])))
    grand_total += count

    datasets = [(n, weighted_words(n)) for n in range(1, 16)]
    count, _ = run_candidate("TL1", "domino tilings of 2xn, n=1..15", datasets,
                             lambda n: (lambda word: isolated_domino_token_flip(word)))
    grand_total += count

    datasets = []
    for cols in (2, 4, 6):
        states = perfect_matchings_graph(4 * cols, grid_edges(4, cols))
        datasets.append((f"4x{cols}", states))
    count, _ = run_candidate("TL2", "domino tilings 4x(2,4,6)", datasets,
                             lambda label: static_cell_domino_flip(4, int(label.split('x')[1])))
    grand_total += count

    edges_53, states_53 = uniform_hypergraphs(5, 3)
    datasets = [("n5r3", states_53)]
    count, _ = run_candidate(
        "HG1", "all 3-graphs on [5]", datasets,
        lambda label: (lambda mask: mask ^ ((1 << len(edges_53)) - 1)
                       if sum(d % 3 == 1 for d in hypergraph_degrees(mask, edges_53, 5)) % 2
                       else mask))
    grand_total += count

    count, _ = run_candidate(
        "HG2", "all 3-graphs on [5]", datasets,
        lambda label: (lambda mask: odd_degree_rotor(mask, edges_53, 5)))
    grand_total += count

    count, _ = run_candidate(
        "HG3", "all 3-graphs on [5]", datasets,
        lambda label: (lambda mask: imbalanced_tetra_toggle(mask, edges_53, 5)))
    grand_total += count

    datasets = [(n, tuple(range(1 << (n * n)))) for n in range(1, 4)]
    count, _ = run_candidate(
        "HG4", "pointed incidence matrices n=1..3", datasets,
        lambda n: (lambda state: transpose_matrix_state(state, n)
                   if sum(((state >> (i * n)) & ((1 << n) - 1)).bit_count() % 2
                          for i in range(n)) % 2 else state))
    grand_total += count

    datasets = [(n, chord_matchings(n)) for n in range(1, 7)]
    count, _ = run_candidate("MT1", "circular perfect matchings, chords n=1..6", datasets,
                             lambda n: (lambda matching: isolated_crossing_uncross(matching)))
    grand_total += count

    count, _ = run_candidate(
        "MT2", "circular perfect matchings, chords n=1..6", datasets,
        lambda n: (lambda matching: component_normalize(matching, chords_cross, False)))
    grand_total += count

    count, _ = run_candidate(
        "MT3", "linear perfect matchings, chords n=1..6", datasets,
        lambda n: (lambda matching: component_normalize(matching, chords_nest, True)))
    grand_total += count

    datasets = []
    for n in range(1, 5):
        perms = tuple(permutations(range(n)))
        datasets.append((n, tuple((p, q) for p in perms for q in perms)))
    count, _ = run_candidate("MT4", "ordered pairs of bipartite matchings n=1..4", datasets,
                             lambda n: (lambda pair: alternating_cycle_swap(pair)))
    grand_total += count

    datasets = [(n, ideals_of_poset(fence_poset(n))) for n in range(1, 13)]
    count, _ = run_candidate("LT1", "fence ideal lattices n=1..12", datasets,
                             lambda n: (lambda mask: pseudocomplement(mask, fence_poset(n))))
    grand_total += count

    datasets = [((a, b), rectangle_paths(a, b)) for a in range(1, 6) for b in range(1, 6)]
    count, _ = run_candidate(
        "LP1", "rectangle paths 1<=a,b<=5", datasets,
        lambda ab: (lambda word: tuple(reversed(word)) if path_area(word) % 3 == 1 else word))
    grand_total += count

    datasets = []
    for cols in range(2, 5):
        datasets.append(((3, cols), connected_subsets(3, cols)))
    count, _ = run_candidate(
        "GE1", "fixed-grid polyominoes 3x2..3x4", datasets,
        lambda rc: (lambda mask: reflect_polyomino(mask, *rc)
                    if polyomino_perimeter(mask, *rc) % 3 == 1 else mask))
    grand_total += count

    datasets = [(n, spanning_trees_complete(n)) for n in range(2, 6)]
    count, _ = run_candidate("MA1", "spanning trees of K_n, n=2..5", datasets,
                             lambda n: (lambda tree: basis_exchange_tree(tree, n)))
    grand_total += count

    print(f"TOTAL | candidates=25 | assertions={grand_total}")
    print("status: finite controls are falsification evidence, not all-size proofs or novelty")


if __name__ == "__main__":
    main()
