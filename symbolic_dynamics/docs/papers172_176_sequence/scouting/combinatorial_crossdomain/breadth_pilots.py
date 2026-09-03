#!/usr/bin/env python3
"""Exact breadth pilots for the P172--P176 combinatorial cross-domain lane.

This file intentionally uses only the Python standard library.  Exhaustive
boxes are counterexample pressure, not proofs or ownership evidence.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def finite_map_stats(states, step):
    states = tuple(states)
    state_set = set(states)
    successor = {}
    image = set()
    fixed = 0
    period_states = Counter()
    max_tail = 0
    max_fibre = 0
    fibres = Counter()
    for state in states:
        target = step(state)
        check(target in state_set, "finite-map closure")
        successor[state] = target
        image.add(target)
        fibres[target] += 1
        fixed += target == state
    if fibres:
        max_fibre = max(fibres.values())
    for state in states:
        seen = {}
        point = state
        while point not in seen:
            seen[point] = len(seen)
            point = successor[point]
        tail = seen[point]
        period = len(seen) - tail
        check(period >= 1, "positive period")
        max_tail = max(max_tail, tail)
        period_states[period] += 1
    return {
        "states": len(states),
        "image": len(image),
        "fixed": fixed,
        "tail": max_tail,
        "period_states": dict(sorted(period_states.items())),
        "max_fibre": max_fibre,
    }, successor, fibres


def print_row(label: str, parameter: str, stats: dict) -> None:
    print(
        f"{label} {parameter} states={stats['states']} image={stats['image']} "
        f"fixed={stats['fixed']} tail={stats['tail']} "
        f"period_states={stats['period_states']} max_fibre={stats['max_fibre']}"
    )


# ---------------------------------------------------------------------------
# Posets: a strict order is represented by one outgoing bit row per vertex.


@lru_cache(maxsize=None)
def labelled_posets(n: int):
    pairs = tuple(combinations(range(n), 2))
    answer = []
    for choices in product(range(3), repeat=len(pairs)):
        rows = [0] * n
        for (left, right), choice in zip(pairs, choices):
            if choice == 1:
                rows[left] |= 1 << right
            elif choice == 2:
                rows[right] |= 1 << left
        transitive = True
        for left in range(n):
            for middle in range(n):
                if rows[left] & (1 << middle):
                    if rows[middle] & ~rows[left]:
                        transitive = False
                        break
            if not transitive:
                break
        if transitive:
            answer.append(tuple(rows))
    return tuple(answer)


def poset_predecessor_counts(poset):
    n = len(poset)
    return tuple(1 + sum(bool(poset[y] & (1 << x)) for y in range(n)) for x in range(n))


def poset_successor_counts(poset):
    return tuple(1 + row.bit_count() for row in poset)


def principal_cardinality_dominance(poset):
    n = len(poset)
    down = poset_predecessor_counts(poset)
    up = poset_successor_counts(poset)
    return tuple(
        sum(1 << y for y in range(n) if down[x] < down[y] and up[x] > up[y])
        for x in range(n)
    )


def extremal_skeleton(poset):
    n = len(poset)
    minimal = [not any(poset[y] & (1 << x) for y in range(n)) for x in range(n)]
    maximal = [poset[x] == 0 for x in range(n)]
    return tuple(
        sum(1 << y for y in range(n) if minimal[x] and maximal[y] and poset[x] & (1 << y))
        for x in range(n)
    )


def poset_ranks(poset):
    n = len(poset)

    @lru_cache(maxsize=None)
    def rank(vertex):
        predecessors = [u for u in range(n) if poset[u] & (1 << vertex)]
        return 0 if not predecessors else 1 + max(rank(u) for u in predecessors)

    return tuple(rank(v) for v in range(n))


def rank_layer_completion(poset):
    ranks = poset_ranks(poset)
    n = len(poset)
    return tuple(sum(1 << y for y in range(n) if ranks[x] < ranks[y]) for x in range(n))


def audit_posets():
    for n in range(1, 6):
        states = labelled_posets(n)
        check(len(states) == (1, 3, 19, 219, 4231)[n - 1], "labelled-poset census")
        for label, step in (
            ("P01_PCD", principal_cardinality_dominance),
            ("P02_ESK", extremal_skeleton),
            ("P03_RLC", rank_layer_completion),
        ):
            stats, successor, _ = finite_map_stats(states, step)
            print_row(label, f"n={n}", stats)
            for state in states:
                target = successor[state]
                if label == "P01_PCD":
                    for row, new_row in zip(state, target):
                        check(row & ~new_row == 0, "PCD is extensive")
                    down = poset_predecessor_counts(state)
                    up = poset_successor_counts(state)
                    fixed_criterion = all(
                        bool(state[x] & (1 << y))
                        == (down[x] < down[y] and up[x] > up[y])
                        for x in range(n)
                        for y in range(n)
                        if x != y
                    )
                    check((target == state) == fixed_criterion, "PCD fixed criterion")
                elif label in {"P02_ESK", "P03_RLC"}:
                    check(step(target) == target, f"{label} is a retraction")


# ---------------------------------------------------------------------------
# Simple labelled graphs.


@lru_cache(maxsize=None)
def graph_edges(n: int):
    return tuple(combinations(range(n), 2))


def graph_adjacency(mask: int, n: int):
    adjacency = [0] * n
    for bit, (left, right) in enumerate(graph_edges(n)):
        if mask & (1 << bit):
            adjacency[left] |= 1 << right
            adjacency[right] |= 1 << left
    return tuple(adjacency)


@lru_cache(maxsize=None)
def matching_masks(n: int):
    edges = graph_edges(n)
    result = []
    for mask in range(1 << len(edges)):
        used = 0
        valid = True
        for bit, (left, right) in enumerate(edges):
            if mask & (1 << bit):
                endpoints = (1 << left) | (1 << right)
                if used & endpoints:
                    valid = False
                    break
                used |= endpoints
        if valid:
            result.append(mask)
    return tuple(result)


def maximum_matching_support(mask: int, n: int) -> int:
    feasible = [candidate for candidate in matching_masks(n) if candidate & ~mask == 0]
    maximum = max(candidate.bit_count() for candidate in feasible)
    support = 0
    for candidate in feasible:
        if candidate.bit_count() == maximum:
            support |= candidate
    return support


def maximum_matching_delete(mask: int, n: int) -> int:
    return mask & ~maximum_matching_support(mask, n)


def dominating_edge_core(mask: int, n: int) -> int:
    adjacency = graph_adjacency(mask, n)
    full = (1 << n) - 1
    output = 0
    for bit, (left, right) in enumerate(graph_edges(n)):
        if mask & (1 << bit):
            closed = adjacency[left] | adjacency[right] | (1 << left) | (1 << right)
            if closed == full:
                output |= 1 << bit
    return output


def true_twin_edge_core(mask: int, n: int) -> int:
    adjacency = graph_adjacency(mask, n)
    closed = tuple(adjacency[v] | (1 << v) for v in range(n))
    output = 0
    for bit, (left, right) in enumerate(graph_edges(n)):
        if mask & (1 << bit) and closed[left] == closed[right]:
            output |= 1 << bit
    return output


def eccentricity_class_completion(mask: int, n: int) -> int:
    adjacency = graph_adjacency(mask, n)
    component = [-1] * n
    eccentricity = [0] * n
    component_id = 0
    for start in range(n):
        if component[start] != -1:
            continue
        queue = deque([start])
        component[start] = component_id
        vertices = [start]
        while queue:
            vertex = queue.popleft()
            for neighbour in range(n):
                if adjacency[vertex] & (1 << neighbour) and component[neighbour] == -1:
                    component[neighbour] = component_id
                    vertices.append(neighbour)
                    queue.append(neighbour)
        for source in vertices:
            distance = {source: 0}
            inner = deque([source])
            while inner:
                vertex = inner.popleft()
                for neighbour in vertices:
                    if adjacency[vertex] & (1 << neighbour) and neighbour not in distance:
                        distance[neighbour] = distance[vertex] + 1
                        inner.append(neighbour)
            eccentricity[source] = max(distance.values())
        component_id += 1
    output = 0
    for bit, (left, right) in enumerate(graph_edges(n)):
        if component[left] == component[right] and eccentricity[left] == eccentricity[right]:
            output |= 1 << bit
    return output


def audit_graphs():
    for n in range(1, 6):
        states = tuple(range(1 << len(graph_edges(n))))
        maps = (
            ("G01_MMS", lambda state, n=n: maximum_matching_support(state, n)),
            ("G02_MMD", lambda state, n=n: maximum_matching_delete(state, n)),
            ("G03_DEC", lambda state, n=n: dominating_edge_core(state, n)),
            ("G04_TTC", lambda state, n=n: true_twin_edge_core(state, n)),
            ("G05_ECC", lambda state, n=n: eccentricity_class_completion(state, n)),
        )
        for label, step in maps:
            stats, successor, _ = finite_map_stats(states, step)
            print_row(label, f"n={n}", stats)
            for state in states:
                target = successor[state]
                if label in {"G01_MMS", "G04_TTC", "G05_ECC"}:
                    check(step(target) == target, f"{label} retraction")
                if label in {"G01_MMS", "G02_MMD", "G03_DEC", "G04_TTC"}:
                    check(target & ~state == 0, f"{label} only deletes edges")


# ---------------------------------------------------------------------------
# Tournaments.


def tournament_arc(mask: int, n: int, left: int, right: int) -> bool:
    if left == right:
        return False
    if left < right:
        bit = graph_edges(n).index((left, right))
        return bool(mask & (1 << bit))
    return not tournament_arc(mask, n, right, left)


def unique_triangle_reversal(mask: int, n: int) -> int:
    output = mask
    for bit, (left, right) in enumerate(graph_edges(n)):
        tail, head = (left, right) if mask & (1 << bit) else (right, left)
        count = sum(
            tournament_arc(mask, n, head, third)
            and tournament_arc(mask, n, third, tail)
            for third in range(n)
            if third not in (left, right)
        )
        if count == 1:
            output ^= 1 << bit
    return output


def tournament_sccs(mask: int, n: int):
    reach = [[tournament_arc(mask, n, left, right) for right in range(n)] for left in range(n)]
    for vertex in range(n):
        reach[vertex][vertex] = True
    for middle in range(n):
        for left in range(n):
            if reach[left][middle]:
                for right in range(n):
                    reach[left][right] = reach[left][right] or reach[middle][right]
    unused = set(range(n))
    classes = []
    while unused:
        start = min(unused)
        block = tuple(vertex for vertex in sorted(unused) if reach[start][vertex] and reach[vertex][start])
        classes.append(block)
        unused.difference_update(block)
    return tuple(classes)


def condensation_reversal(mask: int, n: int) -> int:
    classes = tournament_sccs(mask, n)
    owner = {}
    for index, block in enumerate(classes):
        for vertex in block:
            owner[vertex] = index
    output = mask
    for bit, (left, right) in enumerate(graph_edges(n)):
        if owner[left] != owner[right]:
            output ^= 1 << bit
    return output


def audit_tournaments():
    for n in range(1, 7):
        states = tuple(range(1 << len(graph_edges(n))))
        for label, step in (
            ("T01_UTR", lambda state, n=n: unique_triangle_reversal(state, n)),
            ("T02_CDR", lambda state, n=n: condensation_reversal(state, n)),
        ):
            stats, successor, _ = finite_map_stats(states, step)
            print_row(label, f"n={n}", stats)
            if label == "T02_CDR":
                for state in states:
                    check(step(successor[state]) == state, "condensation reversal involution")


# ---------------------------------------------------------------------------
# Three-uniform hypergraphs.


@lru_cache(maxsize=None)
def triples(n: int):
    return tuple(combinations(range(n), 3))


def pair_codegrees(mask: int, n: int):
    counts = Counter()
    for bit, edge in enumerate(triples(n)):
        if mask & (1 << bit):
            for pair in combinations(edge, 2):
                counts[pair] += 1
    return counts


def shadow_clique_completion(mask: int, n: int) -> int:
    codegree = pair_codegrees(mask, n)
    output = 0
    for bit, edge in enumerate(triples(n)):
        if all(codegree[pair] > 0 for pair in combinations(edge, 2)):
            output |= 1 << bit
    return output


def pair_core_pruning(mask: int, n: int) -> int:
    codegree = pair_codegrees(mask, n)
    output = 0
    for bit, edge in enumerate(triples(n)):
        if mask & (1 << bit) and all(codegree[pair] >= 2 for pair in combinations(edge, 2)):
            output |= 1 << bit
    return output


def odd_codegree_feedback(mask: int, n: int) -> int:
    codegree = pair_codegrees(mask, n)
    output = 0
    for bit, edge in enumerate(triples(n)):
        if sum(codegree[pair] for pair in combinations(edge, 2)) % 2:
            output |= 1 << bit
    return output


def audit_hypergraphs():
    for n in range(3, 6):
        states = tuple(range(1 << len(triples(n))))
        for label, step in (
            ("H01_SCC", lambda state, n=n: shadow_clique_completion(state, n)),
            ("H02_PCP", lambda state, n=n: pair_core_pruning(state, n)),
            ("H03_OCF", lambda state, n=n: odd_codegree_feedback(state, n)),
        ):
            stats, successor, _ = finite_map_stats(states, step)
            print_row(label, f"n={n}", stats)
            if label == "H01_SCC":
                for state in states:
                    check(step(successor[state]) == successor[state], "shadow completion retraction")
            if label == "H02_PCP":
                for state in states:
                    check(successor[state] & ~state == 0, "pair core only deletes")


# ---------------------------------------------------------------------------
# Families of subsets of [n].


def maximal_members(family: int, n: int):
    members = [subset for subset in range(1 << n) if family & (1 << subset)]
    return tuple(
        subset
        for subset in members
        if not any(subset != other and subset & ~other == 0 for other in members)
    )


def maximal_complement_antichain(family: int, n: int) -> int:
    full = (1 << n) - 1
    return sum(1 << (full ^ subset) for subset in maximal_members(family, n))


def boolean_interval_hull(family: int, n: int) -> int:
    members = [subset for subset in range(1 << n) if family & (1 << subset)]
    output = family
    for lower in members:
        for upper in members:
            if lower & ~upper:
                continue
            free = upper ^ lower
            sub = free
            while True:
                output |= 1 << (lower | sub)
                if sub == 0:
                    break
                sub = (sub - 1) & free
    return output


def left_exchange_generation(family: int, n: int) -> int:
    output = family
    for subset in range(1 << n):
        if not family & (1 << subset):
            continue
        for high in range(n):
            if not subset & (1 << high):
                continue
            for low in range(high):
                if not subset & (1 << low):
                    target = (subset ^ (1 << high)) | (1 << low)
                    output |= 1 << target
    return output


def is_antichain_family(family: int, n: int) -> bool:
    members = [subset for subset in range(1 << n) if family & (1 << subset)]
    return all(
        left == right or (left & ~right and right & ~left)
        for left in members
        for right in members
    )


def max_complement_fibre_formula(target: int, n: int) -> int:
    if not is_antichain_family(target, n):
        return 0
    full = (1 << n) - 1
    maxima = [full ^ subset for subset in range(1 << n) if target & (1 << subset)]
    downset = set()
    for maximum in maxima:
        sub = maximum
        while True:
            downset.add(sub)
            if sub == 0:
                break
            sub = (sub - 1) & maximum
    return 1 << (len(downset) - len(maxima))


def audit_set_families():
    for n in range(1, 5):
        states = tuple(range(1 << (1 << n)))
        for label, step in (
            ("F01_MCA", lambda state, n=n: maximal_complement_antichain(state, n)),
            ("F02_BIH", lambda state, n=n: boolean_interval_hull(state, n)),
            ("F03_LEG", lambda state, n=n: left_exchange_generation(state, n)),
        ):
            stats, successor, fibres = finite_map_stats(states, step)
            print_row(label, f"n={n}", stats)
            for state in states:
                target = successor[state]
                if label == "F01_MCA":
                    check(is_antichain_family(target, n), "MCA image antichain")
                    check(step(step(target)) == target, "MCA image is recurrent")
                else:
                    check(state & ~target == 0, f"{label} extensive")
            if label == "F01_MCA":
                for target in states:
                    check(
                        fibres.get(target, 0) == max_complement_fibre_formula(target, n),
                        "MCA every-target fibre formula",
                    )


# ---------------------------------------------------------------------------
# Permutations.


def adjacent_sum_rerank(permutation):
    n = len(permutation)
    scores = tuple(permutation[i] + permutation[(i + 1) % n] for i in range(n))
    order = sorted(range(n), key=lambda i: (scores[i], i))
    rank = [0] * n
    for value, position in enumerate(order, 1):
        rank[position] = value
    return tuple(rank)


def cartesian_breadth_first(permutation):
    if not permutation:
        return permutation
    n = len(permutation)
    left_child = [-1] * n
    right_child = [-1] * n

    def build(low, high):
        if low >= high:
            return -1
        root = min(range(low, high), key=lambda i: permutation[i])
        left_child[root] = build(low, root)
        right_child[root] = build(root + 1, high)
        return root

    root = build(0, n)
    queue = deque([root])
    output = []
    while queue:
        vertex = queue.popleft()
        output.append(permutation[vertex])
        if left_child[vertex] != -1:
            queue.append(left_child[vertex])
        if right_child[vertex] != -1:
            queue.append(right_child[vertex])
    return tuple(output)


def audit_permutations():
    for n in range(1, 8):
        states = tuple(permutations(range(1, n + 1)))
        for label, step in (
            ("Q01_ASR", adjacent_sum_rerank),
            ("Q02_CBF", cartesian_breadth_first),
        ):
            stats, _, _ = finite_map_stats(states, step)
            print_row(label, f"n={n}", stats)


# ---------------------------------------------------------------------------
# Binary/ternary words.


def bracket_matching_support(word: int, n: int) -> int:
    stack = []
    output = 0
    for position in range(n):
        bit_position = n - 1 - position
        if word & (1 << bit_position):
            stack.append(bit_position)
        elif stack:
            opening = stack.pop()
            output |= (1 << opening) | (1 << bit_position)
    return output


def one_runs(word: int, n: int):
    bits = format(word, f"0{n}b")
    runs = []
    index = 0
    while index < n:
        if bits[index] == "0":
            index += 1
            continue
        end = index
        while end < n and bits[end] == "1":
            end += 1
        runs.append(end - index)
        index = end
    return tuple(runs)


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def bracket_fibre_formula(target: int, n: int) -> int:
    runs = one_runs(target, n)
    if any(length % 2 for length in runs):
        return 0
    zeros = n - target.bit_count()
    answer = zeros + 1
    for length in runs:
        answer *= catalan(length // 2)
    return answer


def lz78_phrase_start_mask(word: int, n: int) -> int:
    text = format(word, f"0{n}b")
    dictionary = {""}
    position = 0
    output = 0
    while position < n:
        prefix = max((item for item in dictionary if text.startswith(item, position)), key=len)
        if position + len(prefix) < n:
            phrase = text[position : position + len(prefix) + 1]
            dictionary.add(phrase)
            length = len(prefix) + 1
        else:
            length = len(prefix)
        if length == 0:
            length = 1
            dictionary.add(text[position : position + 1])
        output |= 1 << (n - 1 - position)
        position += length
    return output


def move_to_front_encode(word, alphabet_size: int):
    order = list(range(alphabet_size))
    output = []
    for letter in word:
        index = order.index(letter)
        output.append(index)
        order.pop(index)
        order.insert(0, letter)
    return tuple(output)


def audit_words():
    matching_heights = []
    for n in range(1, 16):
        states = tuple(range(1 << n))
        step = lambda state, n=n: bracket_matching_support(state, n)
        stats, successor, fibres = finite_map_stats(states, step)
        print_row("W01_BMS", f"n={n}", stats)
        matching_heights.append(stats["tail"])
        check(stats["image"] == (1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987)[n - 1], "BMS Fibonacci image")
        check(stats["fixed"] == 1, "BMS unique fixed point")
        for target in states:
            check(fibres.get(target, 0) == bracket_fibre_formula(target, n), "BMS every-target fibre")
            if target in fibres:
                check(all(length % 2 == 0 for length in one_runs(target, n)), "BMS image run criterion")
        for state in states:
            point = state
            for _ in range(1 + n * n):
                if point == 0:
                    break
                point = successor[point]
            check(point == 0, "BMS bounded convergence witness")
    print(f"W01_BMS_HEIGHTS n=1..15 values={matching_heights}")

    for n in range(1, 15):
        states = tuple(range(1 << n))
        stats, _, _ = finite_map_stats(states, lambda state, n=n: lz78_phrase_start_mask(state, n))
        print_row("W02_LZP", f"n={n}", stats)

    for alphabet_size, maximum_length in ((2, 8), (3, 6), (4, 5)):
        for n in range(1, maximum_length + 1):
            states = tuple(product(range(alphabet_size), repeat=n))
            step = lambda state, q=alphabet_size: move_to_front_encode(state, q)
            stats, _, fibres = finite_map_stats(states, step)
            print_row("W03_MTF", f"q={alphabet_size},n={n}", stats)
            check(stats["image"] == stats["states"], "MTF encoder bijective")
            check(all(value == 1 for value in fibres.values()), "MTF singleton fibres")


# ---------------------------------------------------------------------------
# Latin squares and row/column normalization.


@lru_cache(maxsize=None)
def latin_squares(n: int):
    cells = [-1] * (n * n)
    row_used = [0] * n
    col_used = [0] * n
    result = []

    def search(position: int) -> None:
        if position == n * n:
            result.append(tuple(tuple(cells[r * n : (r + 1) * n]) for r in range(n)))
            return
        row, column = divmod(position, n)
        forbidden = row_used[row] | col_used[column]
        for symbol in range(n):
            flag = 1 << symbol
            if forbidden & flag:
                continue
            cells[position] = symbol
            row_used[row] |= flag
            col_used[column] |= flag
            search(position + 1)
            row_used[row] ^= flag
            col_used[column] ^= flag

    search(0)
    return tuple(result)


def normalize_latin(square):
    n = len(square)
    column_for_symbol = [0] * n
    for column, symbol in enumerate(square[0]):
        column_for_symbol[symbol] = column
    first = tuple(tuple(square[row][column_for_symbol[symbol]] for symbol in range(n)) for row in range(n))
    row_for_symbol = [0] * n
    for row in range(n):
        row_for_symbol[first[row][0]] = row
    return tuple(first[row_for_symbol[symbol]] for symbol in range(n))


def audit_latin():
    known = {1: 1, 2: 2, 3: 12, 4: 576}
    for n in range(1, 5):
        states = latin_squares(n)
        check(len(states) == known[n], "Latin-square census")
        stats, successor, fibres = finite_map_stats(states, normalize_latin)
        print_row("L01_RCN", f"n={n}", stats)
        for state in states:
            check(normalize_latin(successor[state]) == successor[state], "Latin normalization retraction")
        expected = 1
        for factor in range(2, n + 1):
            expected *= factor
        expected *= 1 if n <= 1 else expected // n
        check(all(value == expected for value in fibres.values()), "uniform Latin normalization fibres")


def main() -> None:
    print("P172--P176 combinatorial cross-domain breadth pilots")
    print("STATUS HOLD_EXTERNAL")
    audit_posets()
    audit_graphs()
    audit_tournaments()
    audit_hypergraphs()
    audit_set_families()
    audit_permutations()
    audit_words()
    audit_latin()
    print(f"ASSERTIONS {ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
