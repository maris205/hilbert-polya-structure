#!/usr/bin/env python3
"""Exact finite falsifiers for the P147--P151 combinatorial breadth scout.

The program audits twelve literal maps.  It is deliberately a falsifier, not
a proof and not a novelty certificate.  Enumeration is used only to test the
stated clocks, endpoint descriptions, fibres, and explicit counterexamples.
All arithmetic and all state spaces below are exact.
"""

from __future__ import annotations

from array import array
from collections import Counter, defaultdict, deque
from functools import lru_cache
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from math import comb, factorial


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def fibonacci(n: int) -> int:
    first, second = 0, 1
    for _ in range(n):
        first, second = second, first + second
    return first


def orbit_to_fixed(state, step):
    seen = set()
    current = state
    tail = 0
    while True:
        check(current not in seen, "unexpected nontrivial cycle")
        seen.add(current)
        nxt = step(current)
        if nxt == current:
            return current, tail
        current = nxt
        tail += 1


# ---------------------------------------------------------------------------
# L01: strict prefix-rank map on inversion sequences (direct-owner kill).


def inversion_sequences(n: int):
    yield from product(*(range(i + 1) for i in range(n)))


def prefix_rank(sequence: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        sum(sequence[j] < sequence[i] for j in range(i))
        for i in range(len(sequence))
    )


def audit_l01() -> list[str]:
    lines = []
    expected_images = {1: 1, 2: 2, 3: 5, 4: 15, 5: 53, 6: 217,
                       7: 1014, 8: 5335, 9: 31240}
    for n in range(1, 10):
        states = tuple(inversion_sequences(n))
        images = set()
        fixed = 0
        maximum = -1
        deepest = []
        for state in states:
            images.add(prefix_rank(state))
            endpoint, tail = orbit_to_fixed(state, prefix_rank)
            check(prefix_rank(endpoint) == endpoint, "L01 endpoint")
            fixed += int(prefix_rank(state) == state)
            if tail > maximum:
                maximum, deepest = tail, [state]
            elif tail == maximum:
                deepest.append(state)
        check(len(states) == factorial(n), "L01 state census")
        check(len(images) == expected_images[n], "L01 image census")
        check(fixed == catalan(n), "L01 Catalan fixed census")
        check(maximum == max(0, n - 2), "L01 sharp tail")
        if n >= 3:
            witness = tuple(range(n - 2)) + (0, 1)
            check(deepest == [witness], "L01 unique deepest source")
        lines.append(
            f"L01 n={n} states={len(states)} image={len(images)} "
            f"fixed={fixed} max_tail={maximum}"
        )
    return lines


# ---------------------------------------------------------------------------
# M01: lexicographic crossing-to-nesting on perfect chord matchings.


Matching = tuple[tuple[int, int], ...]


@lru_cache(maxsize=None)
def perfect_matchings(vertices: tuple[int, ...]) -> tuple[Matching, ...]:
    if not vertices:
        return ((),)
    first = vertices[0]
    answer = []
    for j in range(1, len(vertices)):
        partner = vertices[j]
        rest = vertices[1:j] + vertices[j + 1 :]
        for matching in perfect_matchings(rest):
            answer.append(tuple(sorted(((first, partner),) + matching)))
    return tuple(answer)


def crossing_number(matching: Matching) -> int:
    total = 0
    for first, second in combinations(matching, 2):
        (a, c), (b, d) = sorted((first, second))
        total += int(a < b < c < d)
    return total


def uncross(matching: Matching) -> Matching:
    candidates = []
    for i, j in combinations(range(len(matching)), 2):
        (a, c), (b, d) = sorted((matching[i], matching[j]))
        if a < b < c < d:
            candidates.append(((a, b, c, d), i, j))
    if not candidates:
        return matching
    _, i, j = min(candidates)
    (a, c), (b, d) = sorted((matching[i], matching[j]))
    result = [pair for k, pair in enumerate(matching) if k not in (i, j)]
    result.extend(((a, d), (b, c)))
    return tuple(sorted(result))


def opener_set(matching: Matching) -> frozenset[int]:
    return frozenset(a for a, _ in matching)


def stack_matching(openers: frozenset[int], size: int) -> Matching:
    stack = []
    pairs = []
    for vertex in range(size):
        if vertex in openers:
            stack.append(vertex)
        else:
            check(bool(stack), "M01 valid opener word")
            pairs.append((stack.pop(), vertex))
    check(not stack, "M01 balanced opener word")
    return tuple(sorted(pairs))


def multiply_q_integer(poly: list[int], height: int) -> list[int]:
    result = [0] * (len(poly) + height - 1)
    for degree, coefficient in enumerate(poly):
        for shift in range(height):
            result[degree + shift] += coefficient
    return result


def matching_target_polynomial(target: Matching, size: int) -> list[int]:
    openers = opener_set(target)
    height = 0
    polynomial = [1]
    for vertex in range(size):
        if vertex in openers:
            height += 1
        else:
            polynomial = multiply_q_integer(polynomial, height)
            height -= 1
    check(height == 0, "M01 target height")
    return polynomial


def audit_m01() -> list[str]:
    lines = []
    expected_images = {1: 1, 2: 2, 3: 8, 4: 53, 5: 473, 6: 5198}
    for n in range(1, 8):
        states = perfect_matchings(tuple(range(2 * n)))
        images = set()
        basins: dict[Matching, Counter[int]] = defaultdict(Counter)
        fixed = 0
        maximum = -1
        deepest = []
        for state in states:
            nxt = uncross(state)
            images.add(nxt)
            if nxt != state:
                check(
                    crossing_number(nxt) == crossing_number(state) - 1,
                    "M01 one-crossing clock decrement",
                )
                check(opener_set(nxt) == opener_set(state), "M01 opener invariant")
            endpoint, tail = orbit_to_fixed(state, uncross)
            crossings = crossing_number(state)
            check(tail == crossings, "M01 pointwise crossing clock")
            predicted_target = stack_matching(opener_set(state), 2 * n)
            check(endpoint == predicted_target, "M01 stack endpoint")
            basins[endpoint][tail] += 1
            fixed += int(nxt == state)
            if tail > maximum:
                maximum, deepest = tail, [state]
            elif tail == maximum:
                deepest.append(state)
        check(len(states) == factorial(2 * n) // (2**n * factorial(n)),
              "M01 state census")
        check(fixed == catalan(n), "M01 Catalan recurrent census")
        check(maximum == comb(n, 2), "M01 sharp quadratic clock")
        witness = tuple((i, n + i) for i in range(n))
        check(deepest == [witness], "M01 unique deepest source")
        for target, observed in basins.items():
            polynomial = matching_target_polynomial(target, 2 * n)
            expected = Counter(
                {degree: coefficient for degree, coefficient in enumerate(polynomial)
                 if coefficient}
            )
            check(observed == expected, "M01 every-target q-integer fibre")
            check(sum(observed.values()) == sum(polynomial), "M01 basin size")
        if n in expected_images:
            check(len(images) == expected_images[n], "M01 image census")
        lines.append(
            f"M01 n={n} states={len(states)} image={len(images)} "
            f"fixed={fixed} max_tail={maximum} basins={len(basins)}"
        )
    return lines


# ---------------------------------------------------------------------------
# B01: least-hole completion of a partial permutation (portfolio kill).


def partial_permutations(n: int):
    state = [-1] * n

    def rec(i: int, used: set[int]):
        if i == n:
            yield tuple(state)
            return
        state[i] = -1
        yield from rec(i + 1, used)
        for value in range(n):
            if value not in used:
                state[i] = value
                used.add(value)
                yield from rec(i + 1, used)
                used.remove(value)
        state[i] = -1

    yield from rec(0, set())


def complete_least_hole(state: tuple[int, ...]) -> tuple[int, ...]:
    if -1 not in state:
        return state
    result = list(state)
    left = result.index(-1)
    missing_values = sorted(set(range(len(state))) - set(state))
    result[left] = missing_values[0]
    return tuple(result)


def increasing_subsequence_polynomial(target: tuple[int, ...]) -> Counter[int]:
    polynomial = Counter()
    n = len(target)
    for mask in range(1 << n):
        values = [target[i] for i in range(n) if mask & (1 << i)]
        if all(a < b for a, b in zip(values, values[1:])):
            polynomial[len(values)] += 1
    return polynomial


def audit_b01() -> list[str]:
    lines = []
    for n in range(1, 8):
        states = tuple(partial_permutations(n))
        images = set()
        basins: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
        depth_census = Counter()
        maximum = -1
        deepest = []
        for state in states:
            images.add(complete_least_hole(state))
            endpoint, tail = orbit_to_fixed(state, complete_least_hole)
            missing = state.count(-1)
            check(tail == missing, "B01 missing-pair clock")
            check(sorted(endpoint) == list(range(n)), "B01 permutation endpoint")
            basins[endpoint][tail] += 1
            depth_census[tail] += 1
            if tail > maximum:
                maximum, deepest = tail, [state]
            elif tail == maximum:
                deepest.append(state)
        expected_states = sum(comb(n, k) ** 2 * factorial(k) for k in range(n + 1))
        check(len(states) == expected_states, "B01 state census")
        check(maximum == n, "B01 sharp clock")
        check(deepest == [(-1,) * n], "B01 unique empty deepest source")
        for depth in range(n + 1):
            expected = comb(n, depth) ** 2 * factorial(n - depth)
            check(depth_census[depth] == expected, "B01 temporal census")
        for target in permutations(range(n)):
            expected_by_missing = increasing_subsequence_polynomial(target)
            observed_by_missing = basins[target]
            check(observed_by_missing == expected_by_missing,
                  "B01 every-target increasing-subsequence fibre")
        identity = tuple(range(n))
        reverse = tuple(reversed(range(n)))
        check(sum(basins[identity].values()) == 2**n, "B01 identity basin")
        check(sum(basins[reverse].values()) == n + 1, "B01 reverse basin")
        lines.append(
            f"B01 n={n} states={len(states)} image={len(images)} "
            f"fixed={factorial(n)} max_tail={maximum} "
            f"max_basin={sum(basins[identity].values())}"
        )
    return lines


# ---------------------------------------------------------------------------
# C01: leftmost adjacent-equal cancellation on bounded words (firewall kill).


def cancel_leftmost(word: tuple[int, ...]) -> tuple[int, ...]:
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return word[:i] + word[i + 2 :]
    return word


def freely_reduce(word: tuple[int, ...]) -> tuple[int, ...]:
    stack = []
    for letter in word:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def tree_walk_counts(q: int, bound: int) -> list[list[int]]:
    counts = [[0] * (bound + 2) for _ in range(bound + 1)]
    counts[0][0] = 1
    for steps in range(bound):
        counts[steps + 1][0] = q * counts[steps][1]
        for distance in range(1, bound + 1):
            counts[steps + 1][distance] = (
                counts[steps][distance - 1]
                + (q - 1) * counts[steps][distance + 1]
            )
    return counts


def audit_c01() -> list[str]:
    lines = []
    for q, bound in ((2, 12), (3, 8)):
        states = tuple(
            word
            for length in range(bound + 1)
            for word in product(range(q), repeat=length)
        )
        images = set()
        basins: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
        fixed = 0
        maximum = 0
        for word in states:
            nxt = cancel_leftmost(word)
            images.add(nxt)
            endpoint, tail = orbit_to_fixed(word, cancel_leftmost)
            reduced = freely_reduce(word)
            check(endpoint == reduced, "C01 free-product normal form")
            check(tail == (len(word) - len(reduced)) // 2,
                  "C01 cancellation clock")
            basins[endpoint][tail] += 1
            fixed += int(nxt == word)
            maximum = max(maximum, tail)
        expected_fixed = 1 + sum(q * (q - 1) ** (length - 1)
                                 for length in range(1, bound + 1))
        check(fixed == expected_fixed, "C01 fixed-word census")
        check(maximum == bound // 2, "C01 sharp cancellation clock")
        walk_counts = tree_walk_counts(q, bound)
        for target, observed in basins.items():
            distance = len(target)
            expected = Counter()
            for length in range(distance, bound + 1, 2):
                coefficient = walk_counts[length][distance]
                if coefficient:
                    expected[(length - distance) // 2] += coefficient
            check(observed == expected, "C01 every-target regular-tree fibre")
        lines.append(
            f"C01 q={q} N={bound} states={len(states)} image={len(images)} "
            f"fixed={fixed} max_tail={maximum} basins={len(basins)}"
        )
    return lines


# ---------------------------------------------------------------------------
# T01: rooted-tree walk toward a heavy component/centroid (classical kill).


def labelled_trees(n: int):
    if n == 1:
        yield ((),)
        return
    for code in product(range(n), repeat=max(0, n - 2)):
        degree = [1] * n
        for vertex in code:
            degree[vertex] += 1
        leaves = [vertex for vertex in range(n) if degree[vertex] == 1]
        heapify(leaves)
        adjacency = [[] for _ in range(n)]
        for vertex in code:
            leaf = heappop(leaves)
            adjacency[leaf].append(vertex)
            adjacency[vertex].append(leaf)
            degree[leaf] -= 1
            degree[vertex] -= 1
            if degree[vertex] == 1:
                heappush(leaves, vertex)
        first = heappop(leaves)
        second = heappop(leaves)
        adjacency[first].append(second)
        adjacency[second].append(first)
        yield tuple(tuple(sorted(neighbors)) for neighbors in adjacency)


def tree_centroid_dynamics(adjacency: tuple[tuple[int, ...], ...]):
    n = len(adjacency)
    parent = [-1] * n
    order = [0]
    for vertex in order:
        for neighbor in adjacency[vertex]:
            if neighbor != parent[vertex]:
                parent[neighbor] = vertex
                order.append(neighbor)
    subtree = [1] * n
    for vertex in reversed(order[1:]):
        subtree[parent[vertex]] += subtree[vertex]

    def side_size(vertex: int, neighbor: int) -> int:
        if parent[neighbor] == vertex:
            return subtree[neighbor]
        check(parent[vertex] == neighbor, "T01 tree parent relation")
        return n - subtree[vertex]

    successor = []
    for vertex in range(n):
        heavy = [neighbor for neighbor in adjacency[vertex]
                 if 2 * side_size(vertex, neighbor) > n]
        check(len(heavy) <= 1, "T01 unique heavy component")
        successor.append(heavy[0] if heavy else vertex)
    centroids = tuple(v for v in range(n) if successor[v] == v)
    check(len(centroids) in (1, 2), "T01 one or two centroids")

    distance = [-1] * n
    queue = deque(centroids)
    for vertex in centroids:
        distance[vertex] = 0
    while queue:
        vertex = queue.popleft()
        for neighbor in adjacency[vertex]:
            if distance[neighbor] < 0:
                distance[neighbor] = distance[vertex] + 1
                queue.append(neighbor)
    return tuple(successor), centroids, tuple(distance)


def audit_t01() -> list[str]:
    lines = []
    for n in range(1, 9):
        tree_count = 0
        rooted_states = 0
        image_states = 0
        fixed_states = 0
        maximum = 0
        for adjacency in labelled_trees(n):
            tree_count += 1
            successor, centroids, distance = tree_centroid_dynamics(adjacency)
            rooted_states += n
            image_states += len(set(successor))
            fixed_states += len(centroids)
            basin = Counter()
            for root in range(n):
                current = root
                tail = 0
                while successor[current] != current:
                    check(distance[successor[current]] == distance[current] - 1,
                          "T01 centroid-distance decrement")
                    current = successor[current]
                    tail += 1
                check(tail == distance[root], "T01 pointwise distance clock")
                check(current in centroids, "T01 centroid endpoint")
                basin[current] += 1
                maximum = max(maximum, tail)
            if len(centroids) == 1:
                check(tuple(basin.values()) == (n,), "T01 unique-centroid basin")
            else:
                check(n % 2 == 0, "T01 bicentroid parity")
                check(sorted(basin.values()) == [n // 2, n // 2],
                      "T01 bicentroid equal basins")
        expected_trees = 1 if n == 1 else n ** (n - 2)
        check(tree_count == expected_trees, "T01 Cayley tree census")
        check(rooted_states == (1 if n == 1 else n ** (n - 1)),
              "T01 rooted-tree state census")
        check(maximum == (n - 1) // 2, "T01 sharp centroid clock")
        lines.append(
            f"T01 n={n} trees={tree_count} rooted={rooted_states} "
            f"image={image_states} fixed={fixed_states} max_tail={maximum}"
        )
    return lines


# ---------------------------------------------------------------------------
# G01: fixed-order graph elimination fill-in (direct-owner kill).


def graph_pairs(n: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(n), 2))


def elimination_fill(n: int, graph: int) -> int:
    pairs = graph_pairs(n)
    index = {edge: i for i, edge in enumerate(pairs)}

    def edge(a: int, b: int) -> bool:
        if a > b:
            a, b = b, a
        return bool(graph & (1 << index[a, b]))

    for vertex in range(n):
        higher = [u for u in range(vertex + 1, n) if edge(vertex, u)]
        missing = [(a, b) for a, b in combinations(higher, 2) if not edge(a, b)]
        if missing:
            result = graph
            for pair in missing:
                result |= 1 << index[pair]
            return result
    return graph


def audit_g01() -> list[str]:
    lines = []
    for n in range(1, 7):
        states = range(1 << comb(n, 2))
        images = set()
        fixed = 0
        maximum = 0
        for graph in states:
            nxt = elimination_fill(n, graph)
            images.add(nxt)
            if nxt != graph:
                check(nxt | graph == nxt, "G01 only adds fill edges")
            endpoint, tail = orbit_to_fixed(
                graph, lambda state, order=n: elimination_fill(order, state)
            )
            check(elimination_fill(n, endpoint) == endpoint, "G01 PEO endpoint")
            fixed += int(nxt == graph)
            maximum = max(maximum, tail)
        check(maximum == max(0, n - 2), "G01 sharp elimination clock")
        lines.append(
            f"G01 n={n} states={1 << comb(n, 2)} image={len(images)} "
            f"fixed={fixed} max_tail={maximum}"
        )
    return lines


# ---------------------------------------------------------------------------
# S01: lexicographically scheduled ij-compression of uniform set families.


def shifted_family(n: int, subsets: tuple[int, ...], family: int,
                   i: int, j: int) -> int:
    position = {subset: p for p, subset in enumerate(subsets)}
    result = family
    for p, subset in enumerate(subsets):
        if not (family & (1 << p)):
            continue
        if (subset & (1 << j)) and not (subset & (1 << i)):
            replacement = (subset ^ (1 << j)) | (1 << i)
            q = position[replacement]
            if not (family & (1 << q)):
                result &= ~(1 << p)
                result |= 1 << q
    return result


def family_potential(subsets: tuple[int, ...], family: int) -> int:
    return sum(
        sum(i for i in range(max((subset.bit_length(), 1))) if subset & (1 << i))
        for p, subset in enumerate(subsets)
        if family & (1 << p)
    )


def compression_step(n: int, k: int, family: int) -> int:
    subsets = tuple(mask for mask in range(1 << n) if mask.bit_count() == k)
    for i, j in combinations(range(n), 2):
        shifted = shifted_family(n, subsets, family, i, j)
        if shifted != family:
            return shifted
    return family


def audit_s01() -> list[str]:
    lines = []
    for n in range(1, 6):
        for k in range(n + 1):
            subsets = tuple(mask for mask in range(1 << n) if mask.bit_count() == k)
            number = 1 << len(subsets)
            images = set()
            fixed = 0
            maximum = 0
            for family in range(number):
                step = lambda state, nn=n, kk=k: compression_step(nn, kk, state)
                nxt = step(family)
                images.add(nxt)
                if nxt != family:
                    check(family_potential(subsets, nxt)
                          < family_potential(subsets, family),
                          "S01 strict compression potential")
                endpoint, tail = orbit_to_fixed(family, step)
                check(step(endpoint) == endpoint, "S01 shifted endpoint")
                fixed += int(nxt == family)
                maximum = max(maximum, tail)
            lines.append(
                f"S01 n={n} k={k} states={number} image={len(images)} "
                f"fixed={fixed} max_tail={maximum}"
            )
    return lines


# ---------------------------------------------------------------------------
# F01: indegree-ranked conjugation of endofunctions (relabeling kill).


def indegree_canonicalize(state: tuple[int, ...]) -> tuple[int, ...]:
    n = len(state)
    indegree = [0] * n
    for image in state:
        indegree[image] += 1
    order = sorted(range(n), key=lambda vertex: (indegree[vertex], vertex))
    rank = {vertex: i for i, vertex in enumerate(order)}
    result = [0] * n
    for vertex in range(n):
        result[rank[vertex]] = rank[state[vertex]]
    return tuple(result)


def audit_f01() -> list[str]:
    lines = []
    for n in range(1, 7):
        states = product(range(n), repeat=n)
        images = set()
        fixed = 0
        maximum = 0
        count = 0
        for state in states:
            count += 1
            nxt = indegree_canonicalize(state)
            images.add(nxt)
            check(indegree_canonicalize(nxt) == nxt, "F01 idempotence")
            tail = int(nxt != state)
            fixed += int(tail == 0)
            maximum = max(maximum, tail)
        check(count == n**n, "F01 endofunction census")
        check(fixed == len(images), "F01 fixed equals image")
        lines.append(
            f"F01 n={n} states={count} image={len(images)} "
            f"fixed={fixed} max_tail={maximum}"
        )
    return lines


# ---------------------------------------------------------------------------
# O01: rowmotion on order ideals of a fence poset (direct-owner kill).


def fence_lower_sets(n: int) -> tuple[int, ...]:
    lower = [1 << vertex for vertex in range(n)]
    for i in range(n - 1):
        if i % 2 == 0:
            low, high = i, i + 1
        else:
            low, high = i + 1, i
        lower[high] |= 1 << low
    changed = True
    while changed:
        changed = False
        for vertex in range(n):
            closure = lower[vertex]
            for lower_vertex in range(n):
                if closure & (1 << lower_vertex):
                    closure |= lower[lower_vertex]
            if closure != lower[vertex]:
                lower[vertex] = closure
                changed = True
    return tuple(lower)


def fence_ideals(n: int) -> tuple[int, ...]:
    lower = fence_lower_sets(n)
    return tuple(
        mask for mask in range(1 << n)
        if all(not (mask & (1 << vertex)) or lower[vertex] & ~mask == 0
               for vertex in range(n))
    )


def fence_rowmotion(n: int, ideal: int) -> int:
    lower = fence_lower_sets(n)
    minimal_complement = [
        vertex for vertex in range(n)
        if not (ideal & (1 << vertex))
        and (lower[vertex] & ~(1 << vertex) & ~ideal) == 0
    ]
    result = 0
    for vertex in minimal_complement:
        result |= lower[vertex]
    return result


def audit_o01() -> list[str]:
    lines = []
    for n in range(1, 16):
        ideals = fence_ideals(n)
        ideal_set = set(ideals)
        images = {fence_rowmotion(n, ideal) for ideal in ideals}
        check(images == ideal_set, "O01 rowmotion bijection")
        period_census = Counter()
        for ideal in ideals:
            current = fence_rowmotion(n, ideal)
            period = 1
            while current != ideal:
                check(current in ideal_set, "O01 carrier closure")
                current = fence_rowmotion(n, current)
                period += 1
                check(period <= len(ideals), "O01 finite orbit bound")
            period_census[period] += 1
        expected_ideals = fibonacci(n + 2)
        check(len(ideals) == expected_ideals, "O01 Fibonacci ideal census")
        profile = ",".join(f"{period}:{count}" for period, count
                           in sorted(period_census.items()))
        lines.append(
            f"O01 n={n} states={len(ideals)} image={len(images)} "
            f"fixed={period_census[1]} periods={profile}"
        )
    return lines


# ---------------------------------------------------------------------------
# U01: least-pair union closure on a family of subsets (generic-closure kill).


def union_step(n: int, family: int) -> int:
    members = [subset for subset in range(1 << n) if family & (1 << subset)]
    for first, second in combinations(members, 2):
        union = first | second
        if not (family & (1 << union)):
            return family | (1 << union)
    return family


def union_closure(n: int, family: int) -> int:
    current = family
    while True:
        nxt = union_step(n, current)
        if nxt == current:
            return current
        current = nxt


def audit_u01() -> list[str]:
    lines = []
    for n in range(1, 5):
        number = 1 << (1 << n)
        images = set()
        fixed_families = []
        basin_by_size: dict[int, Counter[int]] = defaultdict(Counter)
        fixed = 0
        maximum = 0
        for family in range(number):
            nxt = union_step(n, family)
            images.add(nxt)
            endpoint, tail = orbit_to_fixed(
                family, lambda state, nn=n: union_step(nn, state)
            )
            closure = union_closure(n, family)
            check(endpoint == closure, "U01 scheduler-independent union closure")
            check(tail == endpoint.bit_count() - family.bit_count(),
                  "U01 closure-deficit clock")
            basin_by_size[endpoint][family.bit_count()] += 1
            fixed += int(nxt == family)
            maximum = max(maximum, tail)
        fixed_families = sorted(basin_by_size)
        check(fixed == len(fixed_families), "U01 fixed union-closed census")

        # This identity is the zeta-transform statement whose inversion gives
        # G_U(z)=sum_{V<=U} mu(V,U)(1+z)^|V| for every union-closed target U.
        for target in fixed_families:
            accumulated = Counter()
            for subtarget in fixed_families:
                if subtarget & ~target == 0:
                    accumulated.update(basin_by_size[subtarget])
            for size in range(target.bit_count() + 1):
                check(accumulated[size] == comb(target.bit_count(), size),
                      "U01 every-target zeta/Mobius fibre identity")
        lines.append(
            f"U01 n={n} states={number} image={len(images)} "
            f"fixed={fixed} max_tail={maximum}"
        )
    return lines


# ---------------------------------------------------------------------------
# Q01: lexicographic cyclic-triangle reversal in a tournament (cycle kill).


@lru_cache(maxsize=None)
def tournament_rules(n: int):
    pairs = graph_pairs(n)
    index = {edge: i for i, edge in enumerate(pairs)}
    rules = []
    for triple in combinations(range(n), 3):
        a, b, c = triple
        positions = (index[a, b], index[a, c], index[b, c])
        mask = sum(1 << position for position in positions)
        rules.append((positions, mask))
    return tuple(rules)


def tournament_step(n: int, state: int) -> int:
    for (i, j, k), mask in tournament_rules(n):
        pattern = (
            ((state >> i) & 1)
            | (((state >> j) & 1) << 1)
            | (((state >> k) & 1) << 2)
        )
        if pattern in (0b010, 0b101):
            return state ^ mask
    return state


def functional_orbit(state: int, successor: list[int]) -> tuple[int, int]:
    seen = {}
    current = state
    while current not in seen:
        seen[current] = len(seen)
        current = successor[current]
    tail = seen[current]
    period = len(seen) - seen[current]
    return tail, period


def audit_q01() -> list[str]:
    lines = []
    for n in range(1, 8):
        number = 1 << comb(n, 2)
        successor = array(
            "I", (tournament_step(n, state) for state in range(number))
        )
        image_marks = bytearray(number)
        for target in successor:
            image_marks[target] = 1
        image_count = sum(image_marks)
        fixed = sum(state == successor[state] for state in range(number))
        check(fixed == factorial(n), "Q01 transitive fixed tournaments")
        tail_max = 0
        period_census = Counter()
        for state in range(number):
            tail, period = functional_orbit(state, successor)
            tail_max = max(tail_max, tail)
            period_census[period] += 1
            check(period in (1, 2), "Q01 bounded cycle-period falsifier")
        if n >= 3:
            index = {edge: i for i, edge in enumerate(graph_pairs(n))}
            triangle_mask = sum(1 << index[pair]
                                for pair in combinations((0, 1, 2), 2))
            witness = 1 << index[0, 2]
            check(successor[witness] == (witness ^ triangle_mask),
                  "Q01 explicit triangle reversal")
            check(successor[witness ^ triangle_mask] == witness,
                  "Q01 explicit 2-cycle")
        profile = ",".join(f"{period}:{count}" for period, count
                           in sorted(period_census.items()))
        lines.append(
            f"Q01 n={n} states={number} image={image_count} fixed={fixed} "
            f"max_tail={tail_max} period_states={profile}"
        )
    return lines


# ---------------------------------------------------------------------------
# D01: least-unstable chip firing on a path with two sinks (classical kill).


def weak_compositions_at_most(parts: int, total_bound: int):
    state = [0] * parts

    def rec(i: int, remaining: int):
        if i == parts:
            yield tuple(state)
            return
        for value in range(remaining + 1):
            state[i] = value
            yield from rec(i + 1, remaining - value)
        state[i] = 0

    yield from rec(0, total_bound)


def chip_step(state: tuple[int, ...], reverse: bool = False) -> tuple[int, ...]:
    indices = range(len(state) - 1, -1, -1) if reverse else range(len(state))
    for i in indices:
        if state[i] >= 2:
            result = list(state)
            result[i] -= 2
            if i > 0:
                result[i - 1] += 1
            if i + 1 < len(state):
                result[i + 1] += 1
            return tuple(result)
    return state


def chip_potential(state: tuple[int, ...]) -> int:
    m = len(state)
    return sum((i + 1) * (m - i) * chips for i, chips in enumerate(state))


def stabilize_chips(state: tuple[int, ...], reverse: bool = False):
    current = state
    steps = 0
    while True:
        nxt = chip_step(current, reverse=reverse)
        if nxt == current:
            return current, steps
        check(chip_potential(nxt) == chip_potential(current) - 2,
              "D01 exact potential decrement")
        current = nxt
        steps += 1


def audit_d01() -> list[str]:
    lines = []
    total_bound = 8
    for m in range(1, 7):
        states = tuple(weak_compositions_at_most(m, total_bound))
        images = set()
        fixed = 0
        maximum = 0
        for state in states:
            nxt = chip_step(state)
            images.add(nxt)
            endpoint, tail = stabilize_chips(state)
            reverse_endpoint, reverse_tail = stabilize_chips(state, reverse=True)
            check(endpoint == reverse_endpoint, "D01 abelian endpoint")
            check(tail == reverse_tail, "D01 odometer firing count")
            check(all(chips <= 1 for chips in endpoint), "D01 stable endpoint")
            check(2 * tail == chip_potential(state) - chip_potential(endpoint),
                  "D01 potential-gap clock")
            fixed += int(nxt == state)
            maximum = max(maximum, tail)
        check(len(states) == comb(total_bound + m, m), "D01 carrier census")
        check(fixed == 2**m, "D01 stable binary census")
        lines.append(
            f"D01 m={m} N={total_bound} states={len(states)} image={len(images)} "
            f"fixed={fixed} max_tail={maximum}"
        )
    return lines


def main() -> None:
    sections = [
        ("L01_PREFIX_RANK", audit_l01),
        ("M01_CHORD_UNCROSS", audit_m01),
        ("B01_PARTIAL_PERMUTATION", audit_b01),
        ("C01_WORD_CANCELLATION", audit_c01),
        ("T01_TREE_CENTROID", audit_t01),
        ("G01_ELIMINATION_FILL", audit_g01),
        ("S01_SET_COMPRESSION", audit_s01),
        ("F01_FUNCTION_CANONICALIZE", audit_f01),
        ("O01_FENCE_ROWMOTION", audit_o01),
        ("U01_UNION_CLOSURE", audit_u01),
        ("Q01_TOURNAMENT_TRIANGLE", audit_q01),
        ("D01_PATH_CHIP_FIRING", audit_d01),
    ]
    print("P147-P151 COMBINATORIAL SCOUT")
    for name, audit in sections:
        print(f"[{name}]")
        for line in audit():
            print(line)
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
