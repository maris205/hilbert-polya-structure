#!/usr/bin/env python3
"""Exact breadth audit for fresh deterministic finite dynamics.

The program is dependency-free and intentionally uses only small complete
carriers.  Enumeration is falsification pressure, not an all-parameter proof
or a novelty claim.  The accompanying notes separate proved formulas from
finite observations and apply the P1--P171 collision firewall.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def finite_stats(states, step):
    states = tuple(states)
    state_set = set(states)
    successor = {}
    fibres = Counter()
    for state in states:
        target = step(state)
        check(target in state_set, "carrier closure")
        successor[state] = target
        fibres[target] += 1

    orbit = {}
    cycles = Counter()
    for start in states:
        if start in orbit:
            continue
        path = []
        position = {}
        point = start
        while point not in orbit and point not in position:
            position[point] = len(path)
            path.append(point)
            point = successor[point]
        if point in position:
            cycle_start = position[point]
            period = len(path) - cycle_start
            cycles[period] += 1
            for state in path[cycle_start:]:
                orbit[state] = (0, period)
            path = path[:cycle_start]
        for state in reversed(path):
            tail, period = orbit[successor[state]]
            orbit[state] = (tail + 1, period)
    check(len(orbit) == len(states), "functional graph coverage")
    return {
        "states": len(states),
        "image": len(fibres),
        "fixed": sum(successor[x] == x for x in states),
        "tail": max(tail for tail, _ in orbit.values()),
        "cycles": dict(sorted(cycles.items())),
        "depths": dict(sorted(Counter(tail for tail, _ in orbit.values()).items())),
        "period_states": dict(sorted(Counter(period for _, period in orbit.values()).items())),
        "max_fibre": max(fibres.values()),
    }, successor, fibres, orbit


def emit(handle: str, box: str, stats: dict) -> None:
    print(
        f"{handle} {box} states={stats['states']} image={stats['image']} "
        f"fixed={stats['fixed']} tail={stats['tail']} cycles={stats['cycles']} "
        f"depths={stats['depths']} periods={stats['period_states']} "
        f"max_fibre={stats['max_fibre']}"
    )


def falling(n: int, k: int) -> int:
    answer = 1
    for j in range(k):
        answer *= n - j
    return answer


def canonical_rgs(word):
    rename = {}
    answer = []
    for letter in word:
        if letter not in rename:
            rename[letter] = len(rename)
        answer.append(rename[letter])
    return tuple(answer)


@lru_cache(maxsize=None)
def set_partitions(n: int):
    if n == 0:
        return ((),)
    answer = [(0,)]
    for _ in range(1, n):
        next_answer = []
        for word in answer:
            for letter in range(max(word) + 2):
                next_answer.append(word + (letter,))
        answer = next_answer
    return tuple(answer)


def blocks_of_rgs(word):
    if not word:
        return ()
    blocks = [[] for _ in range(max(word) + 1)]
    for element, block in enumerate(word, 1):
        blocks[block].append(element)
    return tuple(tuple(block) for block in blocks)


def involution_number(n: int) -> int:
    a, b = 1, 1
    if n == 0:
        return a
    for m in range(2, n + 1):
        a, b = b, b + (m - 1) * a
    return b


# D01: occurrence-rank transpose on set partitions -------------------------


def occurrence_rank_transpose(word):
    seen = Counter()
    ranks = []
    for block in word:
        ranks.append(seen[block])
        seen[block] += 1
    return canonical_rgs(ranks)


def tableau_image(blocks) -> bool:
    return all(
        len(blocks[j]) >= len(blocks[j + 1])
        and all(x < y for x, y in zip(blocks[j], blocks[j + 1]))
        for j in range(len(blocks) - 1)
    )


def ort_fibre_formula(blocks) -> int:
    if not tableau_image(blocks):
        return 0
    answer = 1
    for upper, lower in zip(blocks, blocks[1:]):
        for index, x in enumerate(lower):
            eligible = sum(y < x for y in upper)
            answer *= eligible - index
    return answer


def poly_mul(a, b):
    answer = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            answer[i + j] += x * y
    return tuple(answer)


def injection_gap_poly(upper, lower):
    counts = Counter()

    def visit(index, used, gap):
        if index == len(lower):
            counts[gap] += 1
            return
        x = lower[index]
        for y in upper:
            if y < x and y not in used:
                visit(index + 1, used | {y}, gap + x - y)

    visit(0, set(), 0)
    if not counts:
        return (0,)
    return tuple(counts.get(degree, 0) for degree in range(max(counts) + 1))


def ort_gap_poly(blocks):
    if not tableau_image(blocks):
        return (0,)
    answer = (1,)
    for upper, lower in zip(blocks, blocks[1:]):
        answer = poly_mul(answer, injection_gap_poly(upper, lower))
    return answer


def source_chain_gap(word) -> int:
    return sum(block[-1] - block[0] for block in blocks_of_rgs(word))


def audit_ort():
    for n in range(1, 10):
        states = set_partitions(n)
        stats, successor, fibres, _ = finite_stats(states, occurrence_rank_transpose)
        emit("D01_ORT", f"n={n}", stats)
        image_expected = involution_number(n)
        check(stats["image"] == image_expected, "ORT involution/SYT image count")
        check(all(occurrence_rank_transpose(occurrence_rank_transpose(occurrence_rank_transpose(x)))
                  == occurrence_rank_transpose(x) for x in states), "ORT T^3=T")
        if n == 1:
            check(stats["fixed"] == 1 and stats["tail"] == 0, "ORT n=1 boundary")
        else:
            check(stats["fixed"] == 0, "ORT no fixed state for n>=2")
            check(stats["cycles"] == {2: image_expected // 2}, "ORT image transposition cycles")
            check(stats["tail"] == (0 if n == 2 else 1), "ORT sharp tail boundary")
        for target in states:
            blocks = blocks_of_rgs(target)
            check((target in fibres) == tableau_image(blocks), "ORT image criterion")
            check(fibres[target] == ort_fibre_formula(blocks), "ORT every-target fibre")

        if n <= 8:
            marked = defaultdict(Counter)
            for source, target in successor.items():
                marked[target][source_chain_gap(source)] += 1
            for target in states:
                predicted = ort_gap_poly(blocks_of_rgs(target))
                actual = tuple(
                    marked[target].get(degree, 0)
                    for degree in range(max(marked[target], default=0) + 1)
                )
                while len(actual) > 1 and actual[-1] == 0:
                    actual = actual[:-1]
                while len(predicted) > 1 and predicted[-1] == 0:
                    predicted = predicted[:-1]
                check(actual == predicted, "ORT gap-marked fibre polynomial")


# D02: minimum-pivot Mobius feedback on P^1(F_p) --------------------------


def mobius_feedback(state, p: int):
    pivot = min(x for x in state if x != p)
    answer = []
    for x in state:
        if x == pivot:
            y = p
        elif x == p:
            y = 0
        else:
            y = pow((x - pivot) % p, p - 2, p)
        answer.append(y)
    return tuple(sorted(answer))


def mobius_fibre_height(target, p: int) -> int:
    if p not in target:
        return 0
    inverses = [pow(y, p - 2, p) for y in target if y not in (0, p)]
    return p - max(inverses, default=0)


def inversion_fixed_subsets(p: int, r: int) -> int:
    if p == 2:
        return comb(p - 1, r)
    answer = 0
    pairs = (p - 3) // 2
    for singles in range(3):
        remainder = r - singles
        if remainder >= 0 and remainder % 2 == 0 and remainder // 2 <= pairs:
            answer += comb(2, singles) * comb(pairs, remainder // 2)
    return answer


def audit_mobius_feedback():
    for p in (2, 3, 5, 7, 11, 13):
        maximum_k = p if p <= 7 else 5
        for k in range(2, maximum_k + 1):
            states = tuple(combinations(range(p + 1), k))
            step = lambda state, prime=p: mobius_feedback(state, prime)
            stats, successor, fibres, orbit = finite_stats(states, step)
            emit("D02_MPM", f"p={p},k={k}", stats)
            recurrent = comb(p - 1, k - 2)
            depth_one = comb(p - 1, k - 1)
            depth_two = comb(p, k)
            fixed = inversion_fixed_subsets(p, k - 2)
            check(stats["image"] == comb(p, k - 1), "MPM image count")
            check(stats["depths"] == {0: recurrent, 1: depth_one, 2: depth_two},
                  "MPM exact depth layers")
            expected_cycles = {1: fixed}
            if recurrent > fixed:
                expected_cycles[2] = (recurrent - fixed) // 2
            check(stats["cycles"] == expected_cycles, "MPM recurrent involution atlas")
            for state, (tail, period) in orbit.items():
                expected_tail = 0 if 0 in state and p in state else (1 if p in state else 2)
                check(tail == expected_tail, "MPM pointwise tail criterion")
                if expected_tail == 0:
                    check(period in (1, 2), "MPM core inversion period")
            pivot_sets = defaultdict(set)
            for source, target in successor.items():
                pivot_sets[target].add(min(x for x in source if x != p))
            for target in states:
                height = mobius_fibre_height(target, p)
                check(fibres[target] == height, "MPM every-target fibre")
                check(pivot_sets[target] == set(range(height)), "MPM pivot-marked geometric fibre")


# D03: fibre-successor collapse on endofunctions ---------------------------


def permutation_cycles(mapping):
    n = len(mapping)
    seen = set()
    cycles = []
    for start in range(n):
        if start in seen:
            continue
        cycle = []
        point = start
        while point not in seen:
            seen.add(point)
            cycle.append(point)
            point = mapping[point]
        cycles.append(tuple(cycle))
    return tuple(cycles)


def canonical_cycle_permutation(blocks, n):
    answer = [None] * n
    for block in blocks:
        ordered = sorted(block)
        for x, y in zip(ordered, ordered[1:] + ordered[:1]):
            answer[x] = y
    return tuple(answer)


def fibre_successor(function):
    blocks = defaultdict(list)
    for x, image in enumerate(function):
        blocks[image].append(x)
    return canonical_cycle_permutation(tuple(blocks.values()), len(function))


def fsp_fixedpoint_poly(sizes, n):
    k = len(sizes)
    elementary = [0] * (k + 1)
    elementary[0] = 1
    for size in sizes:
        for degree in range(k, 0, -1):
            elementary[degree] += size * elementary[degree - 1]
    result = [0] * (k + 1)
    for selected in range(k + 1):
        coefficient = elementary[selected] * falling(n - selected, k - selected)
        for j in range(selected + 1):
            result[j] += coefficient * comb(selected, j) * ((-1) ** (selected - j))
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def audit_fsp():
    for n in range(1, 7):
        states = tuple(product(range(n), repeat=n))
        stats, successor, fibres, _ = finite_stats(states, fibre_successor)
        emit("D03_FSP", f"n={n}", stats)
        check(stats["image"] == len(set_partitions(n)), "FSP Bell image")
        check(stats["fixed"] == 1 and stats["cycles"] == {1: 1}, "FSP unique fixed identity")
        check(stats["depths"].get(0) == 1, "FSP depth-zero boundary")
        if n >= 2:
            check(stats["depths"].get(1) == factorial(n) - 1, "FSP bijection layer")
            check(stats["depths"].get(2) == n ** n - factorial(n), "FSP nonbijection layer")
        marked = defaultdict(Counter)
        for source, target in successor.items():
            marked[target][sum(source[i] == i for i in range(n))] += 1
        for target in states:
            count = fibres[target]
            if count:
                cycles = permutation_cycles(target)
                check(target == canonical_cycle_permutation(cycles, n), "FSP canonical cycle target")
                check(count == falling(n, len(cycles)), "FSP every-target fibre")
                if n <= 5:
                    actual = tuple(marked[target].get(j, 0) for j in range(max(marked[target]) + 1))
                    check(actual == fsp_fixedpoint_poly(tuple(map(len, cycles)), n),
                          "FSP fixed-point-marked fibre")


# D04: stable word standardisation -----------------------------------------


def stable_standardise(word):
    order = sorted(range(len(word)), key=lambda i: (word[i], i))
    rank = [0] * len(word)
    for value, index in enumerate(order):
        rank[index] = value
    return tuple(rank)


def inverse_descent_count(permutation):
    position = [0] * len(permutation)
    for index, value in enumerate(permutation):
        position[value] = index
    return sum(position[value] > position[value + 1] for value in range(len(permutation) - 1))


def audit_standardisation():
    for n in range(1, 7):
        states = tuple(product(range(n), repeat=n))
        stats, _, fibres, _ = finite_stats(states, stable_standardise)
        emit("D04_STW", f"q=n={n}", stats)
        check(stats["image"] == factorial(n) and stats["fixed"] == factorial(n),
              "STW permutation retraction")
        check(stats["tail"] == (0 if n == 1 else 1), "STW sharp one-step clock")
        for target in permutations(range(n)):
            d = inverse_descent_count(target)
            check(fibres[target] == comb(2 * n - d - 1, n), "STW P-partition fibre")


# D05: circular parking assignment -----------------------------------------


def circular_parking(preferences):
    n = len(preferences)
    occupied = [False] * n
    assignment = []
    for preference in preferences:
        spot = preference
        while occupied[spot]:
            spot = (spot + 1) % n
        occupied[spot] = True
        assignment.append(spot)
    return tuple(assignment)


def parking_fibre_poly(assignment):
    n = len(assignment)
    occupied = set()
    answer = (1,)
    for spot in assignment:
        run = 0
        point = (spot - 1) % n
        while point in occupied:
            run += 1
            point = (point - 1) % n
        answer = poly_mul(answer, tuple(1 for _ in range(run + 1)))
        occupied.add(spot)
    return answer


def parking_displacement(preferences, assignment):
    n = len(preferences)
    return sum((assignment[i] - preferences[i]) % n for i in range(n))


def audit_parking():
    for n in range(1, 7):
        states = tuple(product(range(n), repeat=n))
        stats, successor, fibres, _ = finite_stats(states, circular_parking)
        emit("D05_CPA", f"n={n}", stats)
        check(stats["image"] == factorial(n) and stats["fixed"] == factorial(n),
              "CPA assignment-permutation retraction")
        marked = defaultdict(Counter)
        for source, target in successor.items():
            marked[target][parking_displacement(source, target)] += 1
        for target in permutations(range(n)):
            polynomial = parking_fibre_poly(target)
            check(fibres[target] == sum(polynomial), "CPA every-outcome fibre")
            actual = tuple(marked[target].get(j, 0) for j in range(max(marked[target]) + 1))
            check(actual == polynomial, "CPA displacement-marked fibre")


# D06: cross-ratio normalisation on ordered projective quadruples ----------


def pgl_matrices(p: int):
    matrices = set()
    for a, b, c, d in product(range(p), repeat=4):
        if (a * d - b * c) % p == 0:
            continue
        entries = (a, b, c, d)
        first = next(x for x in entries if x)
        inverse = pow(first, p - 2, p)
        matrices.add(tuple((x * inverse) % p for x in entries))
    return tuple(sorted(matrices))


def pgl_apply(matrix, point, p: int):
    a, b, c, d = matrix
    if point == p:
        numerator, denominator = a, c
    else:
        numerator = (a * point + b) % p
        denominator = (c * point + d) % p
    if denominator == 0:
        return p
    return numerator * pow(denominator, p - 2, p) % p


@lru_cache(maxsize=None)
def triple_normalisers(p: int):
    answer = {}
    matrices = pgl_matrices(p)
    points = range(p + 1)
    for triple in permutations(points, 3):
        matches = [
            matrix for matrix in matrices
            if tuple(pgl_apply(matrix, x, p) for x in triple) == (p, 0, 1)
        ]
        check(len(matches) == 1, "sharp three-transitivity of PGL2")
        answer[triple] = matches[0]
    return answer


def cross_ratio_normalise(state, p: int):
    matrix = triple_normalisers(p)[state[:3]]
    return (p, 0, 1, pgl_apply(matrix, state[3], p))


def audit_cross_ratio():
    for p in (3, 5, 7):
        states = tuple(permutations(range(p + 1), 4))
        step = lambda state, prime=p: cross_ratio_normalise(state, prime)
        stats, _, fibres, _ = finite_stats(states, step)
        emit("D06_CRN", f"q={p}", stats)
        group_size = p * (p * p - 1)
        check(stats["image"] == p - 2 and stats["fixed"] == p - 2,
              "CRN cross-ratio image")
        check(stats["tail"] == 1, "CRN one-step clock")
        for target, count in fibres.items():
            check(target[:3] == (p, 0, 1), "CRN canonical triple")
            check(count == group_size, "CRN PGL2 orbit fibre")


# D07: Schubert-pivot retraction on binary Grassmannians -------------------


def rref_subspaces(n: int, k: int):
    answer = []
    for pivots in combinations(range(n), k):
        positions = [
            (row, column)
            for row, pivot in enumerate(pivots)
            for column in range(pivot + 1, n)
            if column not in pivots
        ]
        for bits in product((0, 1), repeat=len(positions)):
            rows = [1 << pivot for pivot in pivots]
            for bit, (row, column) in zip(bits, positions):
                if bit:
                    rows[row] |= 1 << column
            answer.append(tuple(rows))
    return tuple(answer)


def pivot_columns(rows):
    return tuple((row & -row).bit_length() - 1 for row in rows)


def schubert_retract(rows):
    return tuple(1 << pivot for pivot in pivot_columns(rows))


def schubert_dimension(n, pivots):
    k = len(pivots)
    return sum(n - k + row - pivot for row, pivot in enumerate(pivots))


def audit_schubert():
    for n in range(1, 7):
        for k in range(n + 1):
            states = rref_subspaces(n, k)
            stats, _, fibres, _ = finite_stats(states, schubert_retract)
            emit("D07_SPR", f"F2,n={n},k={k}", stats)
            check(stats["image"] == comb(n, k) and stats["fixed"] == comb(n, k),
                  "SPR coordinate-subspace image")
            for pivots in combinations(range(n), k):
                target = tuple(1 << pivot for pivot in pivots)
                check(fibres[target] == 2 ** schubert_dimension(n, pivots),
                      "SPR Schubert-cell fibre")


# D08: queue projection of perfect matchings -------------------------------


@lru_cache(maxsize=None)
def perfect_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        return ((),)
    first = vertices[0]
    answer = []
    for partner_index in range(1, len(vertices)):
        partner = vertices[partner_index]
        remaining = vertices[1:partner_index] + vertices[partner_index + 1:]
        for rest in perfect_matchings(remaining):
            answer.append(tuple(sorted(((first, partner),) + rest)))
    return tuple(answer)


def matching_openers(matching):
    return tuple(sorted(min(edge) for edge in matching))


def matching_queue_project(matching):
    vertices = set(x for edge in matching for x in edge)
    openers = matching_openers(matching)
    closers = tuple(sorted(vertices - set(openers)))
    return tuple(sorted(zip(openers, closers)))


def matching_signature_fibre(matching):
    openers = set(matching_openers(matching))
    height = 0
    answer = 1
    for vertex in range(2 * len(matching)):
        if vertex in openers:
            height += 1
        else:
            answer *= height
            height -= 1
    return answer


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def audit_matching_queue():
    for pairs in range(1, 7):
        states = perfect_matchings(tuple(range(2 * pairs)))
        stats, _, fibres, _ = finite_stats(states, matching_queue_project)
        emit("D08_MQP", f"pairs={pairs}", stats)
        check(stats["image"] == catalan(pairs) and stats["fixed"] == catalan(pairs),
              "MQP Catalan image")
        for target, count in fibres.items():
            check(count == matching_signature_fibre(target), "MQP every-signature fibre")


# D09: increasing-cycle canonicalisation of permutations -------------------


def increasing_cycle_canonical(permutation):
    return canonical_cycle_permutation(permutation_cycles(permutation), len(permutation))


def audit_increasing_cycles():
    for n in range(1, 9):
        states = tuple(permutations(range(n)))
        stats, _, fibres, _ = finite_stats(states, increasing_cycle_canonical)
        emit("D09_ICC", f"n={n}", stats)
        check(stats["image"] == len(set_partitions(n)) and stats["fixed"] == len(set_partitions(n)),
              "ICC Bell image")
        for target, count in fibres.items():
            expected = 1
            for cycle in permutation_cycles(target):
                expected *= factorial(len(cycle) - 1)
            check(count == expected, "ICC cycle-support fibre")


# D10: BFS canonicalisation of accessible binary automata ------------------


def reachable_automaton(state):
    n = len(state) // 2
    seen = {0}
    queue = deque([0])
    while queue:
        vertex = queue.popleft()
        for letter in range(2):
            target = state[2 * vertex + letter]
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return len(seen) == n


def bfs_canonical_automaton(state):
    n = len(state) // 2
    order = [0]
    old_to_new = {0: 0}
    cursor = 0
    while cursor < n:
        old = order[cursor]
        for letter in range(2):
            target = state[2 * old + letter]
            if target not in old_to_new:
                old_to_new[target] = len(order)
                order.append(target)
        cursor += 1
    return tuple(
        old_to_new[state[2 * old + letter]]
        for old in order
        for letter in range(2)
    )


def audit_automata():
    for n in range(1, 5):
        states = tuple(state for state in product(range(n), repeat=2 * n) if reachable_automaton(state))
        stats, _, fibres, _ = finite_stats(states, bfs_canonical_automaton)
        emit("D10_BCA", f"binary,n={n}", stats)
        orbit_size = factorial(n - 1)
        check(stats["fixed"] == stats["image"], "BCA retraction")
        check(all(count == orbit_size for count in fibres.values()), "BCA free relabelling fibres")


# D11: alternating double-lex binary-matrix sort ---------------------------


def mask_to_matrix(mask, rows, columns):
    return tuple(tuple((mask >> (i * columns + j)) & 1 for j in range(columns)) for i in range(rows))


def double_lex_step(matrix):
    rows = tuple(sorted(matrix))
    columns = sorted(tuple(row[j] for row in rows) for j in range(len(rows[0])))
    return tuple(tuple(columns[j][i] for j in range(len(columns))) for i in range(len(rows)))


def audit_double_lex():
    for rows, columns in ((2, 2), (2, 3), (3, 3), (3, 4), (4, 4)):
        states = tuple(mask_to_matrix(mask, rows, columns) for mask in range(1 << (rows * columns)))
        stats, _, _, _ = finite_stats(states, double_lex_step)
        emit("D11_DLX", f"{rows}x{columns}", stats)
        check(set(stats["cycles"]) == {1}, "DLX tested recurrence is fixed")


# D12: degree-rank inversion-graph feedback --------------------------------


def graph_step(mask: int, n: int) -> int:
    degrees = [0] * n
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (mask >> bit) & 1:
                degrees[i] += 1
                degrees[j] += 1
            bit += 1
    order = sorted(range(n), key=lambda vertex: (degrees[vertex], vertex))
    rank = [0] * n
    for value, vertex in enumerate(order):
        rank[vertex] = value
    answer = 0
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if rank[i] > rank[j]:
                answer |= 1 << bit
            bit += 1
    return answer


def audit_degree_inversion():
    for n in range(1, 7):
        states = tuple(range(1 << (n * (n - 1) // 2)))
        step = lambda mask, order=n: graph_step(mask, order)
        stats, _, _, _ = finite_stats(states, step)
        emit("D12_DRI", f"n={n}", stats)
        check(set(stats["cycles"]).issubset({1, 2}), "DRI tested periods divide two")


# D13: sorting a tree's Pruefer code ---------------------------------------


def pruefer_sort(code):
    return tuple(sorted(code))


def audit_pruefer_sort():
    for n in range(2, 9):
        states = tuple(product(range(n), repeat=max(0, n - 2)))
        stats, _, fibres, _ = finite_stats(states, pruefer_sort)
        emit("D13_PCS", f"trees,n={n}", stats)
        check(stats["image"] == comb(2 * n - 3, n - 2), "PCS multiset-code image")
        for target, count in fibres.items():
            multiplicities = Counter(target)
            expected = factorial(n - 2)
            for value in multiplicities.values():
                expected //= factorial(value)
            check(count == expected, "PCS multinomial tree fibre")


# D14: RSK diagonal projection from permutations to involutions ------------


def rsk(permutation):
    insertion = []
    recording = []
    for time, value in enumerate(permutation, 1):
        x = value
        row = 0
        while True:
            if row == len(insertion):
                insertion.append([x])
                recording.append([time])
                break
            position = next((j for j, y in enumerate(insertion[row]) if y > x), None)
            if position is None:
                insertion[row].append(x)
                recording[row].append(time)
                break
            insertion[row][position], x = x, insertion[row][position]
            row += 1
    return tuple(map(tuple, insertion)), tuple(map(tuple, recording))


def inverse_rsk(insertion, recording):
    p = [list(row) for row in insertion]
    q = [list(row) for row in recording]
    n = sum(map(len, q))
    word = [None] * n
    for time in range(n, 0, -1):
        row = next(i for i, values in enumerate(q) if time in values)
        column = q[row].index(time)
        q[row].pop(column)
        x = p[row].pop(column)
        if not q[row]:
            q.pop(row)
            p.pop(row)
        for upper in range(row - 1, -1, -1):
            position = max(j for j, y in enumerate(p[upper]) if y < x)
            p[upper][position], x = x, p[upper][position]
        word[time - 1] = x
    return tuple(word)


def rsk_diagonal(permutation):
    _, recording = rsk(permutation)
    return inverse_rsk(recording, recording)


def tableau_count(shape):
    n = sum(shape)
    hooks = 1
    for row, length in enumerate(shape):
        for column in range(length):
            below = sum(other > column for other in shape[row + 1:])
            hooks *= length - column + below
    return factorial(n) // hooks


def audit_rsk_diagonal():
    for n in range(1, 9):
        states = tuple(permutations(range(1, n + 1)))
        for state in states:
            check(inverse_rsk(*rsk(state)) == state, "RSK inverse regression")
        stats, _, fibres, _ = finite_stats(states, rsk_diagonal)
        emit("D14_RDP", f"n={n}", stats)
        check(stats["image"] == involution_number(n) and stats["fixed"] == involution_number(n),
              "RDP involution image")
        for target, count in fibres.items():
            insertion, recording = rsk(target)
            check(insertion == recording, "RDP target is involution tableau pair")
            check(count == tableau_count(tuple(map(len, recording))), "RDP every-involution fibre")


# D15: lexicographically least linear-extension projection -----------------


def labelled_posets(n: int):
    pairs = tuple(combinations(range(n), 2))
    answer = []
    for choices in product(range(3), repeat=len(pairs)):
        rows = [0] * n
        for choice, (i, j) in zip(choices, pairs):
            if choice == 1:
                rows[i] |= 1 << j
            elif choice == 2:
                rows[j] |= 1 << i
        transitive = True
        for i in range(n):
            if (rows[i] >> i) & 1:
                transitive = False
                break
            for j in range(n):
                if (rows[i] >> j) & 1 and rows[j] & ~rows[i]:
                    transitive = False
                    break
            if not transitive:
                break
        if transitive:
            answer.append(tuple(rows))
    return tuple(answer)


def lex_extension_project(rows):
    n = len(rows)
    remaining = set(range(n))
    order = []
    while remaining:
        available = [
            vertex for vertex in remaining
            if not any((rows[other] >> vertex) & 1 for other in remaining)
        ]
        vertex = min(available)
        order.append(vertex)
        remaining.remove(vertex)
    output = [0] * n
    for i, x in enumerate(order):
        for y in order[i + 1:]:
            output[x] |= 1 << y
    return tuple(output)


def audit_poset_extension():
    for n in range(1, 6):
        states = labelled_posets(n)
        stats, _, fibres, _ = finite_stats(states, lex_extension_project)
        emit("D15_LXP", f"n={n}", stats)
        check(stats["image"] == factorial(n) and stats["fixed"] == factorial(n),
              "LXP total-order image")
        check(sum(fibres.values()) == len(states), "LXP full fibre census")


# D16: centroid rerooting of labelled trees --------------------------------


def pruefer_edges(code, n):
    if n == 1:
        return ()
    degree = [1] * n
    for x in code:
        degree[x] += 1
    edges = []
    for x in code:
        leaf = min(i for i in range(n) if degree[i] == 1)
        edges.append((min(leaf, x), max(leaf, x)))
        degree[leaf] -= 1
        degree[x] -= 1
    leaves = [i for i in range(n) if degree[i] == 1]
    edges.append(tuple(sorted(leaves)))
    return tuple(sorted(edges))


def tree_centroid(code, n):
    adjacency = [set() for _ in range(n)]
    for x, y in pruefer_edges(code, n):
        adjacency[x].add(y)
        adjacency[y].add(x)
    eccentric_component = []
    for removed in range(n):
        sizes = []
        seen = {removed}
        for neighbour in adjacency[removed]:
            if neighbour in seen:
                continue
            stack = [neighbour]
            seen.add(neighbour)
            size = 0
            while stack:
                point = stack.pop()
                size += 1
                for other in adjacency[point]:
                    if other not in seen:
                        seen.add(other)
                        stack.append(other)
            sizes.append(size)
        eccentric_component.append(max(sizes, default=0))
    optimum = min(eccentric_component)
    return min(i for i, value in enumerate(eccentric_component) if value == optimum)


def audit_centroid_reroot():
    for n in range(1, 8):
        codes = tuple(product(range(n), repeat=max(0, n - 2))) if n >= 2 else ((),)
        states = tuple((code, root) for code in codes for root in range(n))
        step = lambda state, order=n: (state[0], tree_centroid(state[0], order))
        stats, _, fibres, _ = finite_stats(states, step)
        emit("D16_CRR", f"n={n}", stats)
        check(stats["image"] == len(codes) and stats["fixed"] == len(codes),
              "CRR one canonical root per tree")
        check(all(count == n for count in fibres.values()), "CRR uniform root fibre")


# D17: binary matrix rank-normal-form retraction ---------------------------


def binary_rank(rows, n):
    rows = list(rows)
    rank = 0
    for column in range(n):
        pivot = next((i for i in range(rank, n) if (rows[i] >> column) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(n):
            if i != rank and ((rows[i] >> column) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def rank_normal_retract(rows):
    n = len(rows)
    rank = binary_rank(rows, n)
    return tuple((1 << i) if i < rank else 0 for i in range(n))


def rank_matrix_count(n, rank):
    numerator = 1
    denominator = 1
    for i in range(rank):
        numerator *= (2 ** n - 2 ** i) ** 2
        denominator *= 2 ** rank - 2 ** i
    return numerator // denominator


def audit_rank_normal():
    for n in range(1, 5):
        states = tuple(
            tuple((mask >> (i * n)) & ((1 << n) - 1) for i in range(n))
            for mask in range(1 << (n * n))
        )
        stats, _, fibres, _ = finite_stats(states, rank_normal_retract)
        emit("D17_RNR", f"F2,{n}x{n}", stats)
        check(stats["image"] == n + 1 and stats["fixed"] == n + 1, "RNR rank images")
        for rank in range(n + 1):
            target = tuple((1 << i) if i < rank else 0 for i in range(n))
            check(fibres[target] == rank_matrix_count(n, rank), "RNR rank-stratum fibre")


# D18: Ferrers-conjugate intervalisation of set partitions -----------------


def conjugate_partition(parts):
    return tuple(sum(part >= column for part in parts) for column in range(1, max(parts, default=0) + 1))


def interval_partition(parts):
    word = []
    for block, size in enumerate(parts):
        word.extend([block] * size)
    return tuple(word)


def ferrers_intervalise(word):
    sizes = tuple(sorted(map(len, blocks_of_rgs(word)), reverse=True))
    return interval_partition(conjugate_partition(sizes))


def partition_type_fibre(parts):
    n = sum(parts)
    answer = factorial(n)
    for size in parts:
        answer //= factorial(size)
    for multiplicity in Counter(parts).values():
        answer //= factorial(multiplicity)
    return answer


def integer_partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def audit_ferrers_interval():
    for n in range(1, 10):
        states = set_partitions(n)
        stats, _, fibres, _ = finite_stats(states, ferrers_intervalise)
        emit("D18_FCI", f"n={n}", stats)
        types = tuple(integer_partitions(n))
        self_conjugate = sum(conjugate_partition(parts) == parts for parts in types)
        expected_cycles = {}
        if self_conjugate:
            expected_cycles[1] = self_conjugate
        if len(types) > self_conjugate:
            expected_cycles[2] = (len(types) - self_conjugate) // 2
        check(stats["image"] == len(types) and stats["cycles"] == expected_cycles,
              "FCI partition-conjugation atlas")
        for target in states:
            count = fibres[target]
            blocks = blocks_of_rgs(target)
            if count:
                target_type = tuple(map(len, blocks))
                source_type = conjugate_partition(target_type)
                check(count == partition_type_fibre(source_type), "FCI every-target type fibre")


def main() -> None:
    print("Fresh finite geometry / automata / relation breadth")
    print("STATUS HOLD_EXTERNAL")
    audit_ort()
    audit_mobius_feedback()
    audit_fsp()
    audit_standardisation()
    audit_parking()
    audit_cross_ratio()
    audit_schubert()
    audit_matching_queue()
    audit_increasing_cycles()
    audit_automata()
    audit_double_lex()
    audit_degree_inversion()
    audit_pruefer_sort()
    audit_rsk_diagonal()
    audit_poset_extension()
    audit_centroid_reroot()
    audit_rank_normal()
    audit_ferrers_interval()
    print("SYSTEMS 18")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("RESULT PASS")


if __name__ == "__main__":
    main()
