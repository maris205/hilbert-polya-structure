#!/usr/bin/env python3
"""Dependency-free exact scout for the P197--P201 graph/matching lane.

The program uses only the Python standard library.  It does not import any
paper or earlier-scout implementation.  Exhaustion is counterexample pressure
for the theorem contracts and a replay of the stated historical collisions;
it is not evidence of novelty.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import combinations, permutations, product
from math import comb, factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def functional_stats(states, step):
    states = list(states)
    index = {state: i for i, state in enumerate(states)}
    check(len(index) == len(states), "duplicate carrier states")
    nxt = []
    for state in states:
        target = step(state)
        check(target in index, ("closure", state, target))
        nxt.append(index[target])

    indegree = [0] * len(states)
    for target in nxt:
        indegree[target] += 1

    remaining = indegree[:]
    queue = deque(i for i, value in enumerate(remaining) if value == 0)
    peeled = []
    while queue:
        source = queue.popleft()
        peeled.append(source)
        target = nxt[source]
        remaining[target] -= 1
        if remaining[target] == 0:
            queue.append(target)

    periods = [0] * len(states)
    tails = [0] * len(states)
    visited = set()
    cycle_hist = Counter()
    for start, value in enumerate(remaining):
        if not value or start in visited:
            continue
        cycle = []
        current = start
        while current not in visited:
            visited.add(current)
            cycle.append(current)
            current = nxt[current]
        length = len(cycle)
        cycle_hist[length] += 1
        for vertex in cycle:
            periods[vertex] = length

    for source in reversed(peeled):
        target = nxt[source]
        periods[source] = periods[target]
        tails[source] = tails[target] + 1

    maximum_fibre = max(indegree, default=0)
    return {
        "states": states,
        "index": index,
        "nxt": nxt,
        "indegree": indegree,
        "tails": tails,
        "period_array": periods,
        "image": len(set(nxt)),
        "fixed": sum(i == target for i, target in enumerate(nxt)),
        "periods": tuple(sorted(set(periods))),
        "cycles": dict(sorted(cycle_hist.items())),
        "max_tail": max(tails, default=0),
        "depth_hist": dict(sorted(Counter(tails).items())),
        "max_fibre": maximum_fibre,
        "max_fibre_targets": sum(value == maximum_fibre for value in indegree),
    }


def fibonacci(n):
    if n < 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def triangular(n):
    return n * (n + 1) // 2


# ---------------------------------------------------------------------------
# CMM: odd-cycle monomer matching.


def cycle_matchings(n):
    check(n >= 3 and n % 2 == 1, ("CMM rank", n))
    return [
        mask
        for mask in range(1 << n)
        if not (mask & (mask << 1))
        and not ((mask & 1) and ((mask >> (n - 1)) & 1))
    ]


def cycle_monomers(n, mask):
    matched = [False] * n
    for edge in range(n):
        if (mask >> edge) & 1:
            matched[edge] = True
            matched[(edge + 1) % n] = True
    return tuple(i for i, value in enumerate(matched) if not value)


def cmm_step(n, mask):
    holes = cycle_monomers(n, mask)
    a = min(holes)
    if len(holes) == 1:
        return mask ^ (1 << a) ^ (1 << ((a + 1) % n))
    distance = min(t for t in range(1, n) if (a + t) % n in holes)
    arc = 0
    for t in range(distance):
        arc |= 1 << ((a + t) % n)
    return mask ^ arc


def audit_cmm():
    rows = []
    for n in range(3, 22, 2):
        m = (n - 1) // 2
        states = cycle_matchings(n)
        data = functional_stats(states, lambda state, rank=n: cmm_step(rank, state))

        expected_layers = {}
        for depth in range(m + 1):
            size = m - depth
            numerator = n * comb(n - size, size)
            check(numerator % (n - size) == 0, ("CMM integral layer", n, depth))
            expected_layers[depth] = numerator // (n - size)
        check(data["depth_hist"] == expected_layers, ("CMM depth layers", n))
        check(data["max_tail"] == m, ("CMM sharp clock", n))
        check(data["periods"] == (n,), ("CMM period support", n))
        check(data["cycles"] == {n: 1}, ("CMM unique core cycle", n))

        maximum_matchings = []
        for state, tail, indegree in zip(
            data["states"], data["tails"], data["indegree"]
        ):
            holes = cycle_monomers(n, state)
            expected_tail = m - state.bit_count()
            expected_fibre = triangular(holes[0] // 2) + (len(holes) == 1)
            check(tail == expected_tail, ("CMM point clock", n, state))
            check(indegree == expected_fibre, ("CMM every-target fibre", n, state))
            target = cmm_step(n, state)
            if len(holes) == 1:
                maximum_matchings.append(state)
                target_hole = cycle_monomers(n, target)
                check(
                    target_hole == ((holes[0] + 2) % n,),
                    ("CMM core rotor", n, state),
                )
            else:
                check(
                    target.bit_count() == state.bit_count() + 1,
                    ("CMM augmenting step", n, state),
                )

        check(len(maximum_matchings) == n, ("CMM core size", n))
        expected_image = fibonacci(n - 1) + fibonacci(n - 3) + 2
        check(data["image"] == expected_image, ("CMM image", n))
        check(
            data["max_fibre"] == 1 + triangular(m),
            ("CMM fibre maximum", n),
        )
        check(data["max_fibre_targets"] == 1, ("CMM unique fibre maximum", n))
        rows.append(
            (
                n,
                len(states),
                data["image"],
                n,
                data["max_tail"],
                data["periods"],
                data["max_fibre"],
            )
        )
    return rows


# ---------------------------------------------------------------------------
# LAP: path matching, lexicographically first augmenting path.


def path_matchings(n):
    return [
        mask
        for mask in range(1 << max(0, n - 1))
        if not (mask & (mask << 1))
    ]


def path_monomers(n, mask):
    matched = [False] * n
    for edge in range(n - 1):
        if (mask >> edge) & 1:
            matched[edge] = matched[edge + 1] = True
    return tuple(i for i, value in enumerate(matched) if not value)


def lap_step(n, mask):
    holes = path_monomers(n, mask)
    if len(holes) < 2:
        return mask
    a, b = holes[:2]
    return mask ^ (((1 << (b - a)) - 1) << a)


def audit_lap():
    rows = []
    for n in range(1, 19):
        m = n // 2
        states = path_matchings(n)
        data = functional_stats(states, lambda state, rank=n: lap_step(rank, state))
        check(len(states) == fibonacci(n + 1), ("LAP carrier", n))
        expected_depths = {
            m - size: comb(n - size, size) for size in range(m + 1)
        }
        check(data["depth_hist"] == expected_depths, ("LAP layers", n))
        expected_fixed = comb(n - m, m)
        check(data["fixed"] == expected_fixed, ("LAP fixed", n))
        check(data["periods"] == (1,), ("LAP recurrence", n))
        check(data["max_tail"] == m, ("LAP sharp clock", n))
        expected_image = fibonacci(n - 1) + (n % 2)
        check(data["image"] == expected_image, ("LAP image", n))

        for state, tail, indegree in zip(
            data["states"], data["tails"], data["indegree"]
        ):
            holes = path_monomers(n, state)
            if holes:
                prefix_dimers = holes[0] // 2
            else:
                prefix_dimers = m
            expected_fibre = triangular(prefix_dimers) + (state.bit_count() == m)
            check(tail == m - state.bit_count(), ("LAP point clock", n, state))
            check(indegree == expected_fibre, ("LAP target fibre", n, state))
        check(data["max_fibre"] == 1 + triangular(m), ("LAP max fibre", n))
        check(data["max_fibre_targets"] == 1, ("LAP unique max fibre", n))
        rows.append(
            (n, len(states), data["image"], data["fixed"], m, data["max_fibre"])
        )
    return rows


# ---------------------------------------------------------------------------
# Permutation controls: FCM, CASR, and LVR.


def cycles_minimum_first(permutation):
    n = len(permutation)
    seen = [False] * n
    cycles = []
    for start in range(n):
        if seen[start]:
            continue
        word = []
        vertex = start
        while not seen[vertex]:
            seen[vertex] = True
            word.append(vertex)
            vertex = permutation[vertex]
        pivot = min(range(len(word)), key=word.__getitem__)
        cycles.append(word[pivot:] + word[:pivot])
    cycles.sort(key=lambda cycle: cycle[0])
    return cycles


def cycles_to_permutation(cycles, n):
    answer = list(range(n))
    for cycle in cycles:
        for source, target in zip(cycle, cycle[1:] + cycle[:1]):
            answer[source] = target
    return tuple(answer)


def fcm_step(permutation):
    cycles = cycles_minimum_first(permutation)
    if len(cycles) <= 1:
        return permutation
    return cycles_to_permutation([cycles[0] + cycles[1]] + cycles[2:], len(permutation))


def unsigned_stirling_first(n, k):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for size in range(1, n + 1):
        for parts in range(1, size + 1):
            table[size][parts] = table[size - 1][parts - 1] + (size - 1) * table[size - 1][parts]
    return table[n][k]


def cyclic_adjacent_sum_rank(permutation):
    n = len(permutation)
    order = sorted(
        range(n), key=lambda i: (permutation[i] + permutation[(i + 1) % n], i)
    )
    answer = [0] * n
    for rank, position in enumerate(order):
        answer[position] = rank
    return tuple(answer)


def right_lehmer(permutation):
    n = len(permutation)
    return tuple(
        sum(permutation[j] < permutation[i] for j in range(i + 1, n))
        for i in range(n)
    )


def lvr_step(permutation):
    digits = right_lehmer(permutation)
    order = sorted(range(len(permutation)), key=lambda i: (digits[i], i))
    answer = [0] * len(permutation)
    for rank, position in enumerate(order):
        answer[position] = rank
    return tuple(answer)


def strict_earlier_rank(inversion_sequence):
    return tuple(
        sum(inversion_sequence[j] < inversion_sequence[i] for j in range(i))
        for i in range(len(inversion_sequence))
    )


def audit_permutations():
    fcm_rows = []
    casr_expected = {
        1: (1, 1, (1,), 0, 1),
        2: (1, 1, (1,), 1, 2),
        3: (6, 0, (6,), 0, 1),
        4: (8, 0, (8,), 1, 5),
        5: (58, 0, (10,), 5, 8),
        6: (242, 0, (6, 12), 11, 14),
        7: (1551, 0, (14,), 24, 23),
        8: (10083, 0, (8, 16), 33, 54),
    }
    lvr_expected = {
        1: (1, 1, 0, 1),
        2: (2, 2, 0, 1),
        3: (5, 5, 1, 2),
        4: (15, 14, 2, 3),
        5: (53, 42, 3, 7),
        6: (217, 132, 4, 16),
        7: (1014, 429, 5, 35),
        8: (5335, 1430, 6, 83),
    }
    casr_rows, lvr_rows = [], []
    for n in range(1, 9):
        states = list(permutations(range(n)))

        fcm = functional_stats(states, fcm_step)
        expected_depths = {
            depth: unsigned_stirling_first(n, depth + 1) for depth in range(n)
        }
        check(fcm["depth_hist"] == expected_depths, ("FCM Stirling layers", n))
        check(fcm["periods"] == (1,), ("FCM recurrence", n))
        check(fcm["fixed"] == factorial(max(0, n - 1)), ("FCM fixed", n))
        check(fcm["max_tail"] == n - 1, ("FCM clock", n))
        check(fcm["image"] == (1 if n == 1 else factorial(n) // 2), ("FCM image", n))
        check(fcm["max_fibre"] == n, ("FCM max fibre", n))
        check(fcm["max_fibre_targets"] == 1, ("FCM unique max", n))
        fcm_rows.append((n, fcm["image"], fcm["fixed"], fcm["max_tail"], fcm["max_fibre"]))

        casr = functional_stats(states, cyclic_adjacent_sum_rank)
        observed = (
            casr["image"], casr["fixed"], casr["periods"],
            casr["max_tail"], casr["max_fibre"],
        )
        check(observed == casr_expected[n], ("CASR historical replay", n, observed))
        casr_rows.append((n,) + observed)

        lvr = functional_stats(states, lvr_step)
        observed_lvr = (
            lvr["image"], lvr["fixed"], lvr["max_tail"], lvr["max_fibre"]
        )
        check(observed_lvr == lvr_expected[n], ("LVR historical replay", n))
        check(lvr["periods"] == (1,), ("LVR recurrence", n))
        for permutation in states:
            old_code = tuple(reversed(right_lehmer(permutation)))
            new_code = tuple(reversed(right_lehmer(lvr_step(permutation))))
            check(
                new_code == strict_earlier_rank(old_code),
                ("LVR exact S01 conjugacy", n, permutation),
            )
        lvr_rows.append((n,) + observed_lvr)
    return fcm_rows, casr_rows, lvr_rows


# ---------------------------------------------------------------------------
# Graph controls: OTP, OTC, and lexicographic distance-two filling.


def edge_list(n):
    return list(combinations(range(n), 2))


def adjacency(n, mask, edges):
    graph = [set() for _ in range(n)]
    for index, (u, v) in enumerate(edges):
        if (mask >> index) & 1:
            graph[u].add(v)
            graph[v].add(u)
    return graph


def otp_step(n, mask):
    edges = edge_list(n)
    graph = adjacency(n, mask, edges)
    answer = 0
    for index, (u, v) in enumerate(edges):
        if ((mask >> index) & 1) and len(graph[u] & graph[v]) % 2:
            answer |= 1 << index
    return answer


def otc_step(n, mask):
    edges = edge_list(n)
    graph = adjacency(n, mask, edges)
    parity = [0] * n
    for a, b, c in combinations(range(n), 3):
        if b in graph[a] and c in graph[a] and c in graph[b]:
            parity[a] ^= 1
            parity[b] ^= 1
            parity[c] ^= 1
    answer = mask
    for index, (u, v) in enumerate(edges):
        if parity[u] ^ parity[v]:
            answer ^= 1 << index
    return answer


def ldf_step(n, mask):
    edges = edge_list(n)
    graph = adjacency(n, mask, edges)
    for index, (u, v) in enumerate(edges):
        if not ((mask >> index) & 1) and graph[u] & graph[v]:
            return mask | (1 << index)
    return mask


def component_missing_edges(n, mask):
    edges = edge_list(n)
    graph = adjacency(n, mask, edges)
    seen = set()
    total = 0
    for start in range(n):
        if start in seen:
            continue
        queue = [start]
        seen.add(start)
        component = []
        while queue:
            vertex = queue.pop()
            component.append(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append(neighbour)
        edge_count = sum(len(graph[v]) for v in component) // 2
        total += comb(len(component), 2) - edge_count
    return total


def audit_graphs():
    otp_expected = {
        1: (1, 1, 0, 1), 2: (1, 1, 1, 2), 3: (2, 2, 1, 7),
        4: (8, 5, 2, 42), 5: (64, 37, 2, 413), 6: (799, 187, 3, 6560),
    }
    otc_expected = {
        1: (1, 1, (1,), 0, 1), 2: (2, 2, (1,), 0, 1),
        3: (8, 8, (1,), 0, 1), 4: (48, 42, (1,), 2, 5),
        5: (514, 424, (1,), 2, 16), 6: (14676, 7356, (1, 2, 4), 3, 20),
    }
    ldf_expected = {
        1: (1, 1, 0, 1), 2: (2, 2, 0, 1), 3: (5, 5, 1, 4),
        4: (29, 15, 3, 7), 5: (454, 52, 6, 11), 6: (15593, 203, 10, 16),
    }
    otp_rows, otc_rows, ldf_rows = [], [], []
    for n in range(1, 7):
        states = list(range(1 << comb(n, 2)))
        otp = functional_stats(states, lambda state, rank=n: otp_step(rank, state))
        observed_otp = (otp["image"], otp["fixed"], otp["max_tail"], otp["max_fibre"])
        check(observed_otp == otp_expected[n], ("OTP direct replay", n))
        check(otp["periods"] == (1,), ("OTP recurrence", n))
        otp_rows.append((n,) + observed_otp)

        otc = functional_stats(states, lambda state, rank=n: otc_step(rank, state))
        observed_otc = (
            otc["image"], otc["fixed"], otc["periods"],
            otc["max_tail"], otc["max_fibre"],
        )
        check(observed_otc == otc_expected[n], ("OTC direct replay", n))
        otc_rows.append((n,) + observed_otc)

        ldf = functional_stats(states, lambda state, rank=n: ldf_step(rank, state))
        observed_ldf = (ldf["image"], ldf["fixed"], ldf["max_tail"], ldf["max_fibre"])
        check(observed_ldf == ldf_expected[n], ("LDF fingerprint", n))
        check(ldf["periods"] == (1,), ("LDF recurrence", n))
        for state, tail, indegree in zip(ldf["states"], ldf["tails"], ldf["indegree"]):
            check(tail == component_missing_edges(n, state), ("LDF point clock", n, state))
            predicted = int(ldf_step(n, state) == state)
            for edge in range(comb(n, 2)):
                if (state >> edge) & 1:
                    source = state ^ (1 << edge)
                    predicted += ldf_step(n, source) == state
            check(indegree == predicted, ("LDF every-target edge atlas", n, state))
        expected_max = (n - 1) * (n - 2) // 2
        check(ldf["max_tail"] == expected_max, ("LDF sharp clock", n))
        if n >= 3:
            deepest = sum(tail == expected_max for tail in ldf["tails"])
            check(deepest == n ** (n - 2), ("LDF Cayley deepest", n))
        expected_max_targets = 1 if n != 2 else 2
        check(
            ldf["max_fibre_targets"] == expected_max_targets,
            ("LDF maximum-fibre boundary", n),
        )
        ldf_rows.append((n,) + observed_ldf)
    return otp_rows, otc_rows, ldf_rows


# ---------------------------------------------------------------------------
# Rooted labelled tree controls: leaf-grandparent bubbling and subtree lift.


def prufer_trees(n):
    if n == 1:
        return [tuple()]
    if n == 2:
        return [((0, 1),)]
    trees = []
    for code in product(range(n), repeat=n - 2):
        degree = [1] * n
        for value in code:
            degree[value] += 1
        edges = []
        for value in code:
            leaf = next(i for i, d in enumerate(degree) if d == 1)
            edges.append(tuple(sorted((leaf, value))))
            degree[leaf] -= 1
            degree[value] -= 1
        last = [i for i, d in enumerate(degree) if d == 1]
        edges.append(tuple(sorted(last)))
        trees.append(tuple(sorted(edges)))
    return trees


def rooted_data(n, tree):
    graph = [[] for _ in range(n)]
    for u, v in tree:
        graph[u].append(v)
        graph[v].append(u)
    parent = [-1] * n
    depth = [-1] * n
    parent[0] = 0
    depth[0] = 0
    queue = deque([0])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if depth[neighbour] < 0:
                parent[neighbour] = vertex
                depth[neighbour] = depth[vertex] + 1
                queue.append(neighbour)
    return graph, parent, depth


def lgb_step(n, tree):
    graph, parent, depth = rooted_data(n, tree)
    leaves = [
        vertex for vertex in range(1, n)
        if len(graph[vertex]) == 1 and depth[vertex] >= 2
    ]
    if not leaves:
        return tree
    vertex = min(leaves)
    old_parent = parent[vertex]
    grandparent = parent[old_parent]
    edges = set(tree)
    edges.remove(tuple(sorted((vertex, old_parent))))
    edges.add(tuple(sorted((vertex, grandparent))))
    return tuple(sorted(edges))


def lsl_step(n, tree):
    _, parent, depth = rooted_data(n, tree)
    choices = [vertex for vertex in range(1, n) if depth[vertex] >= 2]
    if not choices:
        return tree
    vertex = min(choices)
    old_parent = parent[vertex]
    edges = set(tree)
    edges.remove(tuple(sorted((vertex, old_parent))))
    edges.add((0, vertex))
    return tuple(sorted(edges))


def polynomial_add(left, right):
    answer = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        answer[i] += value
    for i, value in enumerate(right):
        answer[i] += value
    return answer


def polynomial_multiply(left, right):
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def polynomial_shift_scale(poly, shift, scale):
    return [0] * shift + [scale * value for value in poly]


def lgb_layer_polynomials(maximum_n):
    # A_n(q) for trees on [n] rooted at 0, weighted by
    # sum_{v != 0}(depth(v)-1).  Isolate the root branch containing label 1.
    answer = {1: [1]}
    for n in range(2, maximum_n + 1):
        total = [0]
        for size in range(1, n):
            product_poly = polynomial_multiply(answer[size], answer[n - size])
            scale = comb(n - 2, size - 1) * size
            term = polynomial_shift_scale(product_poly, size - 1, scale)
            total = polynomial_add(total, term)
        while len(total) > 1 and total[-1] == 0:
            total.pop()
        answer[n] = total
    return answer


def lgb_predicted_fibre(n, target):
    graph, parent, depth = rooted_data(n, target)
    leaves = [vertex for vertex in range(1, n) if len(graph[vertex]) == 1]
    sources = set()
    if all(depth[vertex] == 1 for vertex in range(1, n)):
        sources.add(target)
    for vertex in leaves:
        common_parent = parent[vertex]
        for sibling in range(1, n):
            if sibling == vertex or parent[sibling] != common_parent:
                continue
            if any(
                other < vertex and other not in (vertex, sibling) and depth[other] >= 2
                for other in leaves
            ):
                continue
            edges = set(target)
            edges.remove(tuple(sorted((vertex, common_parent))))
            edges.add(tuple(sorted((vertex, sibling))))
            source = tuple(sorted(edges))
            check(lgb_step(n, source) == target, ("LGB inverse reconstruction", n, target))
            sources.add(source)
    return len(sources)


def audit_trees():
    layer_polynomials = lgb_layer_polynomials(8)
    lgb_images = (1, 1, 1, 7, 61, 671, 9031, 144495)
    lsl_images = (1, 1, 1, 5, 34, 307, 3506, 48729)
    lgb_rows, lsl_rows = [], []
    for n in range(1, 9):
        states = prufer_trees(n)
        expected_states = 1 if n <= 2 else n ** (n - 2)
        check(len(states) == expected_states, ("tree carrier", n))

        lgb = functional_stats(states, lambda tree, rank=n: lgb_step(rank, tree))
        observed_hist = Counter()
        maximum_clock = (n - 1) * (n - 2) // 2
        for tree, tail, indegree in zip(lgb["states"], lgb["tails"], lgb["indegree"]):
            _, _, depth = rooted_data(n, tree)
            clock = sum(depth[v] - 1 for v in range(1, n))
            observed_hist[clock] += 1
            check(tail == clock, ("LGB exact clock", n, tree))
            target = lgb_step(n, tree)
            if target != tree:
                _, _, target_depth = rooted_data(n, target)
                target_clock = sum(target_depth[v] - 1 for v in range(1, n))
                check(target_clock == clock - 1, ("LGB unit decrement", n, tree))
            check(indegree == lgb_predicted_fibre(n, tree), ("LGB every-target atlas", n, tree))
        expected_hist = {
            exponent: coefficient
            for exponent, coefficient in enumerate(layer_polynomials[n])
            if coefficient
        }
        check(dict(sorted(observed_hist.items())) == expected_hist, ("LGB EGF recurrence", n))
        check(lgb["image"] == lgb_images[n - 1], ("LGB image fingerprint", n))
        check(lgb["fixed"] == 1 and lgb["periods"] == (1,), ("LGB recurrence", n))
        check(lgb["max_tail"] == maximum_clock, ("LGB sharp clock", n))
        deepest = sum(tail == maximum_clock for tail in lgb["tails"])
        check(deepest == factorial(max(0, n - 1)), ("LGB deepest paths", n))
        expected_max_fibre = 1 if n <= 2 else 1 + (n - 1) * (n - 2)
        check(lgb["max_fibre"] == expected_max_fibre, ("LGB max fibre", n))
        check(lgb["max_fibre_targets"] == 1, ("LGB unique max fibre", n))
        lgb_rows.append(
            (n, len(states), lgb["image"], lgb["fixed"], lgb["max_tail"], lgb["max_fibre"])
        )

        lsl = functional_stats(states, lambda tree, rank=n: lsl_step(rank, tree))
        expected_lsl_depth = {}
        for depth in range(max(0, n - 1)):
            expected_lsl_depth[depth] = comb(max(0, n - 2), depth) * (max(0, n - 1) ** depth)
        if n == 1:
            expected_lsl_depth = {0: 1}
        check(lsl["depth_hist"] == expected_lsl_depth, ("LSL Prüfer layers", n))
        for tree, tail in zip(lsl["states"], lsl["tails"]):
            _, _, depth = rooted_data(n, tree)
            root_degree = sum(value == 1 for value in depth)
            check(tail == n - 1 - root_degree, ("LSL point clock", n, tree))
        check(lsl["image"] == lsl_images[n - 1], ("LSL image fingerprint", n))
        check(lsl["fixed"] == 1 and lsl["periods"] == (1,), ("LSL recurrence", n))
        check(lsl["max_tail"] == max(0, n - 2), ("LSL sharp clock", n))
        expected_lsl_max = 1 if n <= 2 else 1 + (n - 1) * (n - 2)
        check(lsl["max_fibre"] == expected_lsl_max, ("LSL max fibre", n))
        check(lsl["max_fibre_targets"] == 1, ("LSL unique max fibre", n))
        lsl_rows.append(
            (n, len(states), lsl["image"], lsl["fixed"], lsl["max_tail"], lsl["max_fibre"])
        )
    return lgb_rows, lsl_rows


def main():
    cmm_rows = audit_cmm()
    lap_rows = audit_lap()
    fcm_rows, casr_rows, lvr_rows = audit_permutations()
    otp_rows, otc_rows, ldf_rows = audit_graphs()
    lgb_rows, lsl_rows = audit_trees()

    print("P197_P201_GRAPH_MATCHING_LANE")
    print("CMM n/states/image/recurrent/max_tail/periods/max_fibre")
    for row in cmm_rows:
        print("CMM", *row)
    print("LAP_LAST", *lap_rows[-1])
    print("FCM_LAST", *fcm_rows[-1])
    print("CASR_LAST", *casr_rows[-1])
    print("LVR_LAST", *lvr_rows[-1])
    print("OTP_LAST", *otp_rows[-1])
    print("OTC_LAST", *otc_rows[-1])
    print("LDF_LAST", *ldf_rows[-1])
    print("LGB_LAST", *lgb_rows[-1])
    print("LSL_LAST", *lsl_rows[-1])
    print("DECISIONS CMM=PROVISIONAL_AMBER_HOSTILE_GATE LGB=RESERVE_ONLY")
    print("KILLS LAP=BEHIND_CMM_AP1_GCM FCM=MCJ_PM1 LVR=S01_CONJUGACY CASR=Q01_ASR")
    print("KILLS OTP=C20_DIRECT OTC=X02_DIRECT LDF=GRAPH_SQUARE_CLOSURE LSL=BASIS_SORT")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
