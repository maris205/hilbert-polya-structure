#!/usr/bin/env python3
"""Deterministic exact pilot for the frozen RX01--RX12 denominator.

Only Python's standard library is used.  Every enumerated carrier is complete
for the displayed bound; random kernels retain scheduler multiplicity.
"""

from collections import Counter, deque
from itertools import combinations, permutations, product
from math import comb
import heapq


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def functional_stats(fmap):
    """Return exact functional-graph data for a list-valued self-map."""
    n = len(fmap)
    indeg = [0] * n
    rev = [[] for _ in range(n)]
    for x, y in enumerate(fmap):
        check(0 <= y < n, "functional image outside carrier")
        indeg[y] += 1
        rev[y].append(x)
    queue = deque(i for i, d in enumerate(indeg) if d == 0)
    recurrent = [True] * n
    while queue:
        x = queue.popleft()
        recurrent[x] = False
        y = fmap[x]
        indeg[y] -= 1
        if indeg[y] == 0:
            queue.append(y)

    cycle_lengths = []
    seen = set()
    recurrent_vertices = [i for i, yes in enumerate(recurrent) if yes]
    for start in recurrent_vertices:
        if start in seen:
            continue
        x = start
        length = 0
        while x not in seen:
            check(recurrent[x], "cycle traversal left recurrent core")
            seen.add(x)
            length += 1
            x = fmap[x]
        cycle_lengths.append(length)

    depth = [-1] * n
    queue = deque(recurrent_vertices)
    for x in recurrent_vertices:
        depth[x] = 0
    while queue:
        y = queue.popleft()
        for x in rev[y]:
            if depth[x] < 0:
                depth[x] = depth[y] + 1
                queue.append(x)
    check(all(d >= 0 for d in depth), "unassigned functional depth")
    return {
        "states": n,
        "image": len(set(fmap)),
        "fixed": sum(fmap[i] == i for i in range(n)),
        "recurrent": len(recurrent_vertices),
        "cycles": tuple(sorted(cycle_lengths)),
        "periods": tuple(sorted(set(cycle_lengths))),
        "max_depth": max(depth, default=0),
    }


def tree_from_prufer(sequence, n):
    if n == 1:
        return ()
    degree = [1] * n
    for x in sequence:
        degree[x] += 1
    leaves = [i for i, d in enumerate(degree) if d == 1]
    heapq.heapify(leaves)
    edges = []
    for x in sequence:
        leaf = heapq.heappop(leaves)
        edges.append(tuple(sorted((leaf, x))))
        degree[leaf] -= 1
        degree[x] -= 1
        if degree[x] == 1:
            heapq.heappush(leaves, x)
    edges.append(tuple(sorted((heapq.heappop(leaves), heapq.heappop(leaves)))))
    return tuple(sorted(edges))


def labelled_trees(n):
    if n == 1:
        yield ()
    elif n == 2:
        yield tree_from_prufer((), n)
    else:
        for sequence in product(range(n), repeat=n - 2):
            yield tree_from_prufer(sequence, n)


def adjacency(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    for row in adj:
        row.sort()
    return adj


def all_tree_distances(adj):
    n = len(adj)
    out = []
    for root in range(n):
        distance = [-1] * n
        distance[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if distance[v] < 0:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        check(all(d >= 0 for d in distance), "tree is disconnected")
        out.append(distance)
    return out


def path_vertices(adj, source, target):
    parent = [-1] * len(adj)
    parent[source] = source
    queue = deque([source])
    while queue and parent[target] < 0:
        u = queue.popleft()
        for v in adj[u]:
            if parent[v] < 0:
                parent[v] = u
                queue.append(v)
    path = [target]
    while path[-1] != source:
        path.append(parent[path[-1]])
    return tuple(reversed(path))


def component_after_cut(adj, start, cut_u, cut_v):
    seen = {start}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if {u, v} == {cut_u, cut_v}:
                continue
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return seen


def run_tree_lane():
    rows = []
    for n in range(1, 8):
        tree_count = 0
        root_states = 0
        lar_cycles = 0
        lar_max_depth = 0
        lar_fibres = []
        nlr_fixed = 0
        nlr_max_depth = 0
        agp_periods = set()
        agp_max_depth = 0
        agp_max_period = 0
        for edges in labelled_trees(n):
            tree_count += 1
            check(len(edges) == max(0, n - 1), "wrong tree edge count")
            adj = adjacency(n, edges)
            distance = all_tree_distances(adj)
            eccentricity = [max(row) for row in distance]
            diameter = max(eccentricity)

            lar = [min(v for v in range(n) if distance[r][v] == eccentricity[r])
                   for r in range(n)]
            for r, target in enumerate(lar):
                check(distance[r][target] == eccentricity[r], "RX01 not farthest")
                check(target == min(v for v in range(n)
                                    if distance[r][v] == eccentricity[r]),
                      "RX01 tie rule mismatch")

            if n == 1:
                check(lar == [0], "RX01 singleton boundary")
                stats = functional_stats(lar)
                check(stats["cycles"] == (1,), "RX01 singleton spectrum")
                lar_cycles += 1
            else:
                peripheral = [v for v in range(n) if eccentricity[v] == diameter]
                a = min(peripheral)
                b = min(v for v in range(n) if distance[a][v] == diameter)
                check(a < b, "RX01 canonical endpoint order")
                check(distance[a][b] == diameter, "RX01 pair is not diametral")
                expected = [a if distance[r][a] >= distance[r][b] else b
                            for r in range(n)]
                check(lar == expected, "RX01 two-antipode decoder")
                check(set(lar) == {a, b}, "RX01 image is not canonical pair")
                check(lar[a] == b and lar[b] == a, "RX01 cycle mismatch")
                for r in range(n):
                    x = r
                    for t in range(0, 2 * n + 3):
                        if t == 0:
                            wanted = r
                        else:
                            first = lar[r]
                            wanted = first if t % 2 == 1 else lar[first]
                        check(x == wanted, "RX01 all-time formula mismatch")
                        x = lar[x]

                fibre_a = {r for r in range(n) if lar[r] == a}
                fibre_b = {r for r in range(n) if lar[r] == b}
                for target in range(n):
                    actual = {r for r in range(n) if lar[r] == target}
                    wanted = (fibre_a if target == a else
                              fibre_b if target == b else set())
                    check(actual == wanted, "RX01 every-target fibre mismatch")
                check(fibre_a == {r for r in range(n)
                                  if distance[r][a] >= distance[r][b]},
                      "RX01 weak metric halfspace mismatch")
                check(fibre_b == {r for r in range(n)
                                  if distance[r][a] < distance[r][b]},
                      "RX01 strict metric halfspace mismatch")

                path = path_vertices(adj, a, b)
                check(len(path) == diameter + 1, "RX01 diameter path length")
                if diameter % 2:
                    left = path[diameter // 2]
                    right = path[diameter // 2 + 1]
                    a_side = component_after_cut(adj, a, left, right)
                    b_side = set(range(n)) - a_side
                    check(fibre_b == a_side and fibre_a == b_side,
                          "RX01 odd-centre component formula")
                else:
                    centre = path[diameter // 2]
                    toward_a = path[diameter // 2 - 1]
                    a_branch = component_after_cut(adj, a, centre, toward_a)
                    check(fibre_b == a_branch,
                          "RX01 even-centre strict branch formula")
                    check(fibre_a == set(range(n)) - a_branch,
                          "RX01 even-centre weak branch formula")

                stats = functional_stats(lar)
                check(stats["cycles"] == (2,), "RX01 unique two-cycle")
                check(stats["recurrent"] == 2, "RX01 recurrent multiplicity")
                check(stats["image"] == 2, "RX01 rank/image mismatch")
                check(stats["fixed"] == 0, "RX01 spurious fixed root")
                check(stats["max_depth"] == (0 if n == 2 else 1),
                      "RX01 exact depth")
                # These data imply chi(P_T)=x^(n-2)(x-1)(x+1): rank two,
                # one directed 2-cycle, and all other rows enter it in one step.
                check(sum(lar[r] == r for r in range(n)) == 0,
                      "RX01 trace sentinel")
                check(sum(lar[lar[r]] == r for r in range(n)) == 2,
                      "RX01 trace-square sentinel")
                lar_cycles += 1
                lar_fibres.extend((len(fibre_a), len(fibre_b)))

            lar_max_depth = max(lar_max_depth, stats["max_depth"])

            leaves = [v for v in range(n) if len(adj[v]) <= 1]
            nlr = [min(v for v in leaves
                       if distance[r][v] == min(distance[r][w] for w in leaves))
                   for r in range(n)]
            check(set(nlr) == set(leaves), "RX02 image is not leaf set")
            check(all(nlr[nlr[r]] == nlr[r] for r in range(n)),
                  "RX02 is not idempotent")
            nlr_stats = functional_stats(nlr)
            check(nlr_stats["fixed"] == len(leaves), "RX02 fixed leaf count")
            check(nlr_stats["periods"] == (1,), "RX02 nontrivial period")
            nlr_fixed += nlr_stats["fixed"]
            nlr_max_depth = max(nlr_max_depth, nlr_stats["max_depth"])

            if n == 1:
                agp = [0]
            else:
                agp = []
                for r in range(n):
                    target = lar[r]
                    path = path_vertices(adj, r, target)
                    check(len(path) >= 2, "RX03 empty geodesic move")
                    agp.append(path[1])
                    check(path[1] in adj[r], "RX03 move is not local")
            agp_stats = functional_stats(agp)
            agp_periods.update(agp_stats["periods"])
            agp_max_depth = max(agp_max_depth, agp_stats["max_depth"])
            agp_max_period = max(agp_max_period, max(agp_stats["periods"]))
            root_states += n

        expected_trees = 1 if n <= 2 else n ** (n - 2)
        check(tree_count == expected_trees, "Cayley carrier census")
        check(root_states == n * expected_trees, "rooted-tree state census")
        expected_leaf_pairs = 1 if n == 1 else n * (n - 1) ** (n - 2)
        check(nlr_fixed == expected_leaf_pairs, "RX02 aggregate leaf census")
        fibre_range = ((min(lar_fibres), max(lar_fibres))
                       if lar_fibres else (1, 1))
        rows.append(
            f"RX01/LAR|n={n}|trees={tree_count}|root_states={root_states}"
            f"|cycles={lar_cycles}|max_depth={lar_max_depth}"
            f"|nonempty_fibre_range={fibre_range[0]}..{fibre_range[1]}"
        )
        rows.append(
            f"RX02/NLR|n={n}|root_states={root_states}|fixed={nlr_fixed}"
            f"|max_depth={nlr_max_depth}|identity=F2=F"
        )
        rows.append(
            f"RX03/AGP|n={n}|root_states={root_states}"
            f"|periods={','.join(map(str, sorted(agp_periods)))}"
            f"|max_period={agp_max_period}|max_depth={agp_max_depth}"
        )
    return rows


def directed_positions(n):
    return tuple((i, j) for i in range(n) for j in range(n) if i != j)


def arcs_from_mask(mask, positions):
    return {(i, j) for bit, (i, j) in enumerate(positions) if mask >> bit & 1}


def mask_from_arcs(arcs, positions):
    index = {arc: bit for bit, arc in enumerate(positions)}
    return sum(1 << index[arc] for arc in arcs)


def is_dag(n, arcs):
    indeg = [0] * n
    out = [[] for _ in range(n)]
    for u, v in arcs:
        indeg[v] += 1
        out[u].append(v)
    queue = deque(i for i, d in enumerate(indeg) if d == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in out[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    return visited == n


def is_strict_poset(n, arcs):
    if not is_dag(n, arcs):
        return False
    for i in range(n):
        for j in range(n):
            if (i, j) not in arcs:
                continue
            for k in range(n):
                if (j, k) in arcs and (i, k) not in arcs:
                    return False
    return True


def run_dag_and_poset_lane():
    rows = []
    for n in range(1, 5):
        positions = directed_positions(n)
        dags = []
        posets = []
        for mask in range(1 << len(positions)):
            arcs = arcs_from_mask(mask, positions)
            if is_dag(n, arcs):
                dags.append(mask)
                if is_strict_poset(n, arcs):
                    posets.append(mask)
        dag_index = {mask: i for i, mask in enumerate(dags)}
        dsc_map = []
        for mask in dags:
            arcs = arcs_from_mask(mask, positions)
            indeg = [0] * n
            for _, v in arcs:
                indeg[v] += 1
            source = min(v for v in range(n) if indeg[v] == 0)
            moved = set(arcs)
            outgoing = [(u, v) for u, v in arcs if u == source]
            for u, v in outgoing:
                moved.remove((u, v))
                moved.add((v, u))
            image = mask_from_arcs(moved, positions)
            check(is_dag(n, moved), "RX04 left DAG carrier")
            check(len(moved) == len(arcs), "RX04 changed edge count")
            check(image in dag_index, "RX04 image absent from DAG list")
            dsc_map.append(dag_index[image])
        dsc = functional_stats(dsc_map)
        rows.append(
            f"RX04/DSC|n={n}|DAGs={len(dags)}|fixed={dsc['fixed']}"
            f"|periods={','.join(map(str, dsc['periods']))}"
            f"|max_depth={dsc['max_depth']}"
        )

        poset_index = {mask: i for i, mask in enumerate(posets)}
        pes_map = []
        for mask in posets:
            arcs = arcs_from_mask(mask, positions)
            indeg = [0] * n
            outdeg = [0] * n
            for u, v in arcs:
                indeg[v] += 1
                outdeg[u] += 1
            minima = {v for v in range(n) if indeg[v] == 0}
            maxima = {v for v in range(n) if outdeg[v] == 0}
            image_arcs = {(u, v) for u, v in arcs
                          if u in minima and v in maxima}
            image = mask_from_arcs(image_arcs, positions)
            check(is_strict_poset(n, image_arcs), "RX05 left poset carrier")
            check(image in poset_index, "RX05 image absent from poset list")
            # Recompute to make the idempotence claim literal.
            image_indeg = [0] * n
            image_outdeg = [0] * n
            for u, v in image_arcs:
                image_indeg[v] += 1
                image_outdeg[u] += 1
            image_min = {v for v in range(n) if image_indeg[v] == 0}
            image_max = {v for v in range(n) if image_outdeg[v] == 0}
            twice = {(u, v) for u, v in image_arcs
                     if u in image_min and v in image_max}
            check(twice == image_arcs, "RX05 idempotence mismatch")
            pes_map.append(poset_index[image])
        pes = functional_stats(pes_map)
        check(pes["periods"] == (1,), "RX05 nontrivial period")
        check(pes["max_depth"] <= 1, "RX05 projection depth")
        rows.append(
            f"RX05/PES|n={n}|posets={len(posets)}|image={pes['image']}"
            f"|fixed={pes['fixed']}|max_depth={pes['max_depth']}|identity=F2=F"
        )
    return rows


def relation_exact_one_gram(mask, n):
    out = 0
    for i in range(n):
        for j in range(n):
            witnesses = sum(((mask >> (i * n + k)) & 1) and
                            ((mask >> (j * n + k)) & 1)
                            for k in range(n))
            if witnesses == 1:
                out |= 1 << (i * n + j)
    return out


def relation_exact_two_step(mask, n):
    out = 0
    for i in range(n):
        for j in range(n):
            witnesses = sum(((mask >> (i * n + k)) & 1) and
                            ((mask >> (k * n + j)) & 1)
                            for k in range(n))
            if witnesses == 1:
                out |= 1 << (i * n + j)
    return out


def run_relation_lane():
    rows = []
    for n in range(1, 5):
        total = 1 << (n * n)
        gram_map = []
        two_map = []
        for mask in range(total):
            gram = relation_exact_one_gram(mask, n)
            two = relation_exact_two_step(mask, n)
            check(0 <= gram < total and 0 <= two < total,
                  "relation update left carrier")
            for i in range(n):
                for j in range(n):
                    check(((gram >> (i * n + j)) & 1) ==
                          ((gram >> (j * n + i)) & 1),
                          "RX06 image not symmetric")
            gram_map.append(gram)
            two_map.append(two)
        gram_stats = functional_stats(gram_map)
        two_stats = functional_stats(two_map)
        rows.append(
            f"RX06/EOG|n={n}|states={total}|image={gram_stats['image']}"
            f"|fixed={gram_stats['fixed']}|periods={','.join(map(str, gram_stats['periods']))}"
            f"|max_depth={gram_stats['max_depth']}"
        )
        rows.append(
            f"RX07/E2C|n={n}|states={total}|image={two_stats['image']}"
            f"|fixed={two_stats['fixed']}|periods={','.join(map(str, two_stats['periods']))}"
            f"|max_depth={two_stats['max_depth']}"
        )
    return rows


def hypergraph_maps(n):
    subsets = 1 << n
    family_count = 1 << subsets
    compatibility = []
    containers = []
    for s in range(subsets):
        exact = 0
        contained = 0
        for e in range(subsets):
            if (s & e).bit_count() == 1:
                exact |= 1 << e
            if e & ~s == 0:
                contained |= 1 << e
        compatibility.append(exact)
        containers.append(contained)

    eth = []
    uch = []
    full = family_count - 1
    for family in range(family_count):
        exact_targets = 0
        unique_containers = 0
        for s in range(subsets):
            if family & (full ^ compatibility[s]) == 0:
                exact_targets |= 1 << s
            if (family & containers[s]).bit_count() == 1:
                unique_containers |= 1 << s
        eth.append(exact_targets)
        uch.append(unique_containers)
    return eth, uch


def run_hypergraph_deterministic_lane():
    rows = []
    for n in range(0, 5):
        eth, uch = hypergraph_maps(n)
        family_count = len(eth)
        for family in range(family_count):
            check(0 <= eth[family] < family_count, "RX08 left carrier")
            check(eth[eth[eth[family]]] == eth[family], "RX08 F3=F failure")
            check(0 <= uch[family] < family_count, "RX09 left carrier")
            # Cover-pair antitonicity is an exact polarity sentinel.
            missing = (family_count - 1) ^ family
            while missing:
                bit = missing & -missing
                check(eth[family | bit] & ~eth[family] == 0,
                      "RX08 antitonicity failure")
                missing -= bit
        eth_stats = functional_stats(eth)
        uch_stats = functional_stats(uch)
        check(max(eth_stats["periods"]) <= 2, "RX08 polarity period")
        check(eth_stats["max_depth"] <= 1, "RX08 polarity depth")
        rows.append(
            f"RX08/ETH|n={n}|families={family_count}|image={eth_stats['image']}"
            f"|fixed={eth_stats['fixed']}|periods={','.join(map(str, eth_stats['periods']))}"
            f"|max_depth={eth_stats['max_depth']}|identity=F3=F"
        )
        rows.append(
            f"RX09/UCH|n={n}|families={family_count}|image={uch_stats['image']}"
            f"|fixed={uch_stats['fixed']}|periods={','.join(map(str, uch_stats['periods']))}"
            f"|max_depth={uch_stats['max_depth']}"
        )
    return rows


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]


def undirected_edges(n):
    return tuple(combinations(range(n), 2))


def p3_hinge_action(mask, schedule, edge_index):
    a, b, c = schedule
    bc = 1 << edge_index[tuple(sorted((b, c)))]
    if mask & bc == 0:
        return mask
    ab = 1 << edge_index[tuple(sorted((a, b)))]
    ac = 1 << edge_index[tuple(sorted((a, c)))]
    bit_ab = bool(mask & ab)
    bit_ac = bool(mask & ac)
    if bit_ab != bit_ac:
        mask ^= ab | ac
    return mask


def run_random_graph_lane():
    rows = []
    for n in range(3, 6):
        edges = undirected_edges(n)
        edge_index = {edge: i for i, edge in enumerate(edges)}
        states = 1 << len(edges)
        schedules = tuple(permutations(range(n), 3))
        denominator = n * (n - 1) * (n - 2)
        check(len(schedules) == denominator, "RX10 scheduler denominator")
        transitions = []
        uf = UnionFind(states)
        for mask in range(states):
            counts = Counter()
            for schedule in schedules:
                image = p3_hinge_action(mask, schedule, edge_index)
                check(p3_hinge_action(image, schedule, edge_index) == mask,
                      "RX10 local action not involutive")
                check(image.bit_count() == mask.bit_count(),
                      "RX10 edge count changed")
                counts[image] += 1
                uf.union(mask, image)
            check(sum(counts.values()) == denominator, "RX10 row mass")
            transitions.append(counts)
        for x, counts in enumerate(transitions):
            for y, multiplicity in counts.items():
                check(transitions[y][x] == multiplicity,
                      "RX10 kernel not symmetric")
        components = {}
        for mask in range(states):
            components.setdefault(uf.find(mask), []).append(mask)
        for component in components.values():
            check(len({x.bit_count() for x in component}) == 1,
                  "RX10 action component crosses edge layer")
        rows.append(
            f"RX10/PHS|n={n}|states={states}|D={denominator}"
            f"|components={len(components)}|kernel=symmetric|edge_count=conserved"
        )
    return rows


def run_random_hypergraph_lane():
    rows = []
    for n in range(4, 6):
        triples = tuple(combinations(range(n), 3))
        triple_index = {edge: i for i, edge in enumerate(triples)}
        states = 1 << len(triples)
        schedules = []
        for base in combinations(range(n), 2):
            outside = [v for v in range(n) if v not in base]
            for pair in combinations(outside, 2):
                schedules.append((base, pair))
        schedules = tuple(schedules)
        denominator = comb(n, 2) * comb(n - 2, 2)
        check(len(schedules) == denominator, "RX11 scheduler denominator")

        def action(mask, schedule):
            base, pair = schedule
            first = tuple(sorted(base + (pair[0],)))
            second = tuple(sorted(base + (pair[1],)))
            bit_first = 1 << triple_index[first]
            bit_second = 1 << triple_index[second]
            if bool(mask & bit_first) != bool(mask & bit_second):
                mask ^= bit_first | bit_second
            return mask

        transitions = []
        uf = UnionFind(states)
        for mask in range(states):
            counts = Counter()
            for schedule in schedules:
                image = action(mask, schedule)
                check(action(image, schedule) == mask,
                      "RX11 coordinate exchange not involutive")
                check(image.bit_count() == mask.bit_count(),
                      "RX11 hyperedge count changed")
                counts[image] += 1
                uf.union(mask, image)
            check(sum(counts.values()) == denominator, "RX11 row mass")
            transitions.append(counts)
        for x, counts in enumerate(transitions):
            for y, multiplicity in counts.items():
                check(transitions[y][x] == multiplicity,
                      "RX11 kernel not symmetric")
        components = {}
        for mask in range(states):
            components.setdefault(uf.find(mask), []).append(mask)
        check(len(components) == len(triples) + 1,
              "RX11 exclusion layer component count")
        for component in components.values():
            weights = {x.bit_count() for x in component}
            check(len(weights) == 1, "RX11 component crosses weight layer")
            weight = next(iter(weights))
            check(len(component) == comb(len(triples), weight),
                  "RX11 component is not full fixed-weight layer")
        rows.append(
            f"RX11/HHE|n={n}|states={states}|D={denominator}"
            f"|components={len(components)}|layers=0..{len(triples)}"
            f"|kernel=symmetric"
        )
    return rows


def mutually_eccentric_graph(mask, n, edges, edge_index):
    adj = [[] for _ in range(n)]
    for bit, (u, v) in enumerate(edges):
        if mask >> bit & 1:
            adj[u].append(v)
            adj[v].append(u)
    component = [-1] * n
    components = []
    for start in range(n):
        if component[start] >= 0:
            continue
        cid = len(components)
        vertices = []
        queue = deque([start])
        component[start] = cid
        while queue:
            u = queue.popleft()
            vertices.append(u)
            for v in adj[u]:
                if component[v] < 0:
                    component[v] = cid
                    queue.append(v)
        components.append(vertices)
    distances = [[None] * n for _ in range(n)]
    eccentricity = [0] * n
    for vertices in components:
        if len(vertices) == 1:
            continue
        for root in vertices:
            distances[root][root] = 0
            queue = deque([root])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if distances[root][v] is None:
                        distances[root][v] = distances[root][u] + 1
                        queue.append(v)
            eccentricity[root] = max(distances[root][v] for v in vertices)
    out = 0
    for u, v in edges:
        if component[u] != component[v]:
            continue
        distance = distances[u][v]
        if distance is not None and distance == eccentricity[u] == eccentricity[v]:
            out |= 1 << edge_index[(u, v)]
    return out


def run_eccentric_graph_lane():
    rows = []
    for n in range(1, 6):
        edges = undirected_edges(n)
        edge_index = {edge: i for i, edge in enumerate(edges)}
        states = 1 << len(edges)
        fmap = []
        for mask in range(states):
            image = mutually_eccentric_graph(mask, n, edges, edge_index)
            check(0 <= image < states, "RX12 left graph carrier")
            fmap.append(image)
        stats = functional_stats(fmap)
        rows.append(
            f"RX12/MEG|n={n}|states={states}|image={stats['image']}"
            f"|fixed={stats['fixed']}|periods={','.join(map(str, stats['periods']))}"
            f"|max_depth={stats['max_depth']}"
        )
    return rows


def main():
    rows = []
    rows.extend(run_tree_lane())
    rows.extend(run_dag_and_poset_lane())
    rows.extend(run_relation_lane())
    rows.extend(run_hypergraph_deterministic_lane())
    rows.extend(run_random_graph_lane())
    rows.extend(run_random_hypergraph_lane())
    rows.extend(run_eccentric_graph_lane())
    print("replacement graph-lane exact pilot: PASS")
    print("denominator=12 literal updates; labels are lane-local, no paper allocation")
    for row in rows:
        print(row)
    print(f"assertions_total={ASSERTIONS}")
    print("mechanical_advances=RX01/LAR")
    print("final_survivors=none")
    print("owner_gate=RX01/LAR:KILL_DIRECT_OWNER")
    print("decision=EMPTY/HOLD_EXTERNAL")
    print("finite exhaustion is counterexample pressure, not proof or novelty evidence")


if __name__ == "__main__":
    main()
