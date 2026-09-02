#!/usr/bin/env python3
"""Exact breadth verifier for stochastic replacement pool 2.

Ten literal mechanisms are checked independently with integer/Fraction
arithmetic.  The script is a falsifier and owner-gate companion, not evidence
of novelty.  It intentionally imports no earlier scout verifier.
"""

from collections import defaultdict, deque
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial


ASSERTIONS = 0
SECTION = "setup"
COUNTS = defaultdict(int)
SAMPLES = {}


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    COUNTS[SECTION] += 1
    if not condition:
        raise AssertionError(message)


def equal(left, right, message="exact equality failed"):
    check(left == right, f"{message}: {left!r} != {right!r}")


def solve_linear(matrix, rhs):
    n = len(rhs)
    aug = [[Q(x) for x in matrix[i]] + [Q(rhs[i])] for i in range(n)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col]), None)
        check(pivot is not None, f"singular rational system at {col}")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row == col or not aug[row][col]:
                continue
            factor = aug[row][col]
            aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [aug[i][-1] for i in range(n)]


# ---------------------------------------------------------------------------
# ATF / RNC: convex-polygon diagonals


def edge(a, b):
    return (a, b) if a < b else (b, a)


def boundary_edges(n):
    return {edge(i, (i + 1) % n) for i in range(n)}


def diagonals(n):
    boundary = boundary_edges(n)
    return tuple(e for e in combinations(range(n), 2) if e not in boundary)


def cyclic_between(a, x, b, n):
    return 0 < (x - a) % n < (b - a) % n


def crosses(first, second, n):
    a, b = first
    c, d = second
    if len({a, b, c, d}) < 4:
        return False
    return cyclic_between(a, c, b, n) != cyclic_between(a, d, b, n)


def noncrossing(diagonal_set, n):
    return all(not crosses(a, b, n) for a, b in combinations(diagonal_set, 2))


def triangulations(n):
    return tuple(
        frozenset(ds)
        for ds in combinations(diagonals(n), n - 3)
        if noncrossing(ds, n)
    )


def flip_diagonal(state, chosen, n):
    full_edges = set(state) | boundary_edges(n)
    a, b = chosen
    common = [
        v for v in range(n) if v not in (a, b)
        and edge(a, v) in full_edges and edge(b, v) in full_edges
    ]
    equal(len(common), 2, "triangulation diagonal has two adjacent triangles")
    replacement = edge(common[0], common[1])
    target = frozenset((set(state) - {chosen}) | {replacement})
    check(noncrossing(target, n), "flip preserves noncrossing")
    return target


def verify_atf():
    global SECTION
    SECTION = "ATF associahedron flip"
    catalan = (1, 2, 5, 14, 42, 132)
    sample_return = None
    for n, expected_count in zip(range(3, 9), catalan):
        states = triangulations(n)
        equal(len(states), expected_count, "Catalan triangulation count")
        state_set = set(states)
        incoming = {state: Q(0) for state in states}
        for state in states:
            if n == 3:
                continue
            row = defaultdict(Q)
            for chosen in state:
                target = flip_diagonal(state, chosen, n)
                check(target in state_set, "flip target is triangulation")
                row[target] += Q(1, n - 3)
            equal(sum(row.values()), Q(1), "ATF stochastic row")
            for target, probability in row.items():
                incoming[target] += probability
                # Reversibility with uniform measure is literal symmetry.
                check(state in {flip_diagonal(target, d, n) for d in target},
                      "ATF flip has inverse flip")
            if n == 6 and sample_return is None:
                sample_return = sum(p * p for p in row.values())
        if n > 3:
            for mass in incoming.values():
                equal(mass, Q(1), "ATF uniform stationary column")
    SAMPLES["ATF"] = f"states_n8={len(triangulations(8))};sample_two_step_return={sample_return}"


# ---------------------------------------------------------------------------
# RBF: random Coxeter commutation/braid slot


def reduced_words_longest(n):
    target = tuple(range(n - 1, -1, -1))
    words = []

    def visit(permutation, word):
        if permutation == target:
            words.append(tuple(word))
            return
        for i in range(n - 1):
            if permutation[i] < permutation[i + 1]:
                nxt = list(permutation)
                nxt[i], nxt[i + 1] = nxt[i + 1], nxt[i]
                visit(tuple(nxt), word + [i])

    visit(tuple(range(n)), [])
    return tuple(words)


def coxeter_slot_moves(word):
    """Fixed scheduler: all L-1 pair slots and all L-2 triple slots."""
    length = len(word)
    outcomes = []
    for i in range(length - 1):
        if abs(word[i] - word[i + 1]) > 1:
            target = list(word)
            target[i], target[i + 1] = target[i + 1], target[i]
            outcomes.append(tuple(target))
        else:
            outcomes.append(word)
    for i in range(length - 2):
        a, b, c = word[i:i + 3]
        if a == c and abs(a - b) == 1:
            target = list(word)
            target[i:i + 3] = (b, a, b)
            outcomes.append(tuple(target))
        else:
            outcomes.append(word)
    return outcomes


def verify_rbf():
    global SECTION
    SECTION = "RBF reduced-word braid walk"
    expected = {2: 1, 3: 2, 4: 16, 5: 768}
    for n in range(2, 6):
        words = reduced_words_longest(n)
        equal(len(words), expected[n], "number of reduced words for w0")
        word_set = set(words)
        if n == 2:
            continue
        slots = 2 * len(words[0]) - 3
        columns = {word: Q(0) for word in words}
        graph = {word: set() for word in words}
        for word in words:
            outcomes = coxeter_slot_moves(word)
            equal(len(outcomes), slots, "fixed Coxeter scheduler size")
            for target in outcomes:
                check(target in word_set, "Coxeter move preserves reduced-word set")
                columns[target] += Q(1, slots)
                if target != word:
                    graph[word].add(target)
                    graph[target].add(word)
            equal(sum(Q(1, slots) for _ in outcomes), Q(1), "RBF stochastic row")
        for mass in columns.values():
            equal(mass, Q(1), "RBF uniform stationary column")
        reached = {words[0]}
        queue = deque([words[0]])
        while queue:
            for target in graph[queue.popleft()]:
                if target not in reached:
                    reached.add(target)
                    queue.append(target)
        equal(len(reached), len(words), "Matsumoto graph connected in pilot")
    SAMPLES["RBF"] = "reduced_words_n5=768"


# ---------------------------------------------------------------------------
# RAN: random Apollonian face subdivision / ordered ternary leaf expansion


LEAF = None


def leaf_paths(tree, prefix=()):
    if tree is LEAF:
        return [prefix]
    ans = []
    for i, child in enumerate(tree):
        ans.extend(leaf_paths(child, prefix + (i,)))
    return ans


def replace_at_path(tree, path, replacement):
    if not path:
        return replacement
    children = list(tree)
    children[path[0]] = replace_at_path(children[path[0]], path[1:], replacement)
    return tuple(children)


def internal_size_product(tree):
    if tree is LEAF:
        return 0, 1
    child_data = [internal_size_product(child) for child in tree]
    size = 1 + sum(item[0] for item in child_data)
    product_sizes = size
    for _, child_product in child_data:
        product_sizes *= child_product
    return size, product_sizes


def external_path_length(tree, depth=0):
    if tree is LEAF:
        return depth
    return sum(external_path_length(child, depth + 1) for child in tree)


def verify_ran():
    global SECTION
    SECTION = "RAN Apollonian face growth"
    distribution = {LEAF: Q(1)}
    denominator = 1
    state_counts = []
    for internal_nodes in range(1, 7):
        previous_leaf_count = 2 * (internal_nodes - 1) + 1
        denominator *= previous_leaf_count
        nxt = defaultdict(Q)
        for tree, mass in distribution.items():
            paths = leaf_paths(tree)
            equal(len(paths), previous_leaf_count, "ternary face count")
            for path in paths:
                target = replace_at_path(tree, path, (LEAF, LEAF, LEAF))
                nxt[target] += mass / previous_leaf_count
        distribution = dict(nxt)
        equal(sum(distribution.values()), Q(1), "RAN layer mass")
        state_counts.append(len(distribution))
        for tree, mass in distribution.items():
            size, product_sizes = internal_size_product(tree)
            equal(size, internal_nodes, "RAN internal size")
            histories = factorial(size) // product_sizes
            equal(mass, Q(histories, denominator), "RAN increasing-tree hook probability")
    min_area = min(external_path_length(tree) for tree in distribution)
    max_area = max(external_path_length(tree) for tree in distribution)
    SAMPLES["RAN"] = f"states_m1..6={','.join(map(str,state_counts))};area_range_m6={min_area}..{max_area}"


# ---------------------------------------------------------------------------
# GRS: global Gilbert-Shannon-Reeds inverse riffle


def apply_inverse_a_shuffle(deck, labels):
    return tuple(deck[i] for i in sorted(range(len(deck)), key=lambda i: (labels[i], i)))


def a_shuffle_distribution(n, a):
    counts = defaultdict(int)
    identity = tuple(range(n))
    for labels in product(range(a), repeat=n):
        counts[apply_inverse_a_shuffle(identity, labels)] += 1
    return {deck: Q(count, a**n) for deck, count in counts.items()}


def rising_sequences(deck):
    return 1 + sum(deck[i] > deck[i + 1] for i in range(len(deck) - 1))


def verify_grs():
    global SECTION
    SECTION = "GRS global riffle shuffle"
    sample_support = None
    for n in range(1, 7):
        for a in (2, 3, 4):
            dist = a_shuffle_distribution(n, a)
            equal(sum(dist.values()), Q(1), "a-shuffle mass")
            for deck, mass in dist.items():
                runs = rising_sequences(deck)
                expected = Q(comb(a + n - runs, n), a**n) if runs <= a else Q(0)
                equal(mass, expected, "Bayer-Diaconis rising-sequence law")
        # Two independent binary inverse shuffles equal one 4-shuffle.
        first = a_shuffle_distribution(n, 2)
        composed = defaultdict(Q)
        for deck, mass in first.items():
            for labels in product(range(2), repeat=n):
                composed[apply_inverse_a_shuffle(deck, labels)] += mass / (2**n)
        equal(dict(composed), a_shuffle_distribution(n, 4), "riffle semigroup law")
        if n == 6:
            sample_support = len(first)
    SAMPLES["GRS"] = f"binary_support_n6={sample_support}"


# ---------------------------------------------------------------------------
# SBS: pile-wise stochastic Bulgarian solitaire


def integer_partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def bulgarian_transition(partition):
    piles = len(partition)
    counts = defaultdict(int)
    for mask in range(1 << piles):
        chosen = mask.bit_count()
        new_parts = []
        for i, size in enumerate(partition):
            remaining = size - bool(mask & (1 << i))
            if remaining:
                new_parts.append(remaining)
        if chosen:
            new_parts.append(chosen)
        counts[tuple(sorted(new_parts, reverse=True))] += 1
    return {state: Q(count, 1 << piles) for state, count in counts.items()}


def stationary_distribution(states, transition):
    n = len(states)
    index = {state: i for i, state in enumerate(states)}
    matrix = [[Q(0) for _ in range(n)] for _ in range(n)]
    rhs = [Q(0)] * n
    for row in range(n - 1):
        for source in states:
            matrix[row][index[source]] = transition[source].get(states[row], Q(0))
        matrix[row][row] -= 1
    matrix[-1] = [Q(1)] * n
    rhs[-1] = Q(1)
    return solve_linear(matrix, rhs)


def verify_sbs():
    global SECTION
    SECTION = "SBS stochastic Bulgarian solitaire"
    sample_stationary = None
    for cards in range(1, 9):
        states = tuple(integer_partitions(cards))
        state_set = set(states)
        transition = {}
        for state in states:
            row = bulgarian_transition(state)
            equal(sum(row.values()), Q(1), "SBS stochastic row")
            check(set(row) <= state_set, "SBS conserves card mass")
            transition[state] = row
        stationary = stationary_distribution(states, transition)
        equal(sum(stationary), Q(1), "SBS stationary mass")
        for target in states:
            incoming = sum(stationary[i] * transition[source].get(target, Q(0))
                           for i, source in enumerate(states))
            equal(incoming, stationary[states.index(target)], "SBS stationary equation")
        # Positive self-loops plus reachability certify the finite pilot class.
        for state in states:
            check(transition[state].get(state, Q(0)) > 0, "SBS aperiodic self-loop")
        reached = {states[0]}
        queue = deque([states[0]])
        while queue:
            source = queue.popleft()
            for target, probability in transition[source].items():
                if probability and target not in reached:
                    reached.add(target)
                    queue.append(target)
        equal(reached, state_set, "SBS irreducible pilot")
        if cards == 8:
            sample_stationary = max(stationary)
    SAMPLES["SBS"] = f"partitions_N8={len(tuple(integer_partitions(8)))};max_stationary_N8={sample_stationary}"


# ---------------------------------------------------------------------------
# RSK: iid-word row-insertion shape growth


def row_insert(tableau, value):
    rows = [list(row) for row in tableau]
    carry = value
    row_index = 0
    while True:
        if row_index == len(rows):
            rows.append([carry])
            break
        position = next((j for j, entry in enumerate(rows[row_index]) if entry > carry), None)
        if position is None:
            rows[row_index].append(carry)
            break
        rows[row_index][position], carry = carry, rows[row_index][position]
        row_index += 1
    return tuple(tuple(row) for row in rows)


def tableau_shape(tableau):
    return tuple(len(row) for row in tableau)


def hook_product(shape):
    answer = 1
    for i, length in enumerate(shape):
        for j in range(length):
            answer *= length - j + sum(other > j for other in shape[i + 1:])
    return answer


def standard_tableaux_count(shape):
    return factorial(sum(shape)) // hook_product(shape)


def schur_ones(shape, alphabet):
    value = Q(1)
    for i, length in enumerate(shape):
        for j in range(length):
            hook = length - j + sum(other > j for other in shape[i + 1:])
            value *= Q(alphabet + j - i, hook)
    check(value.denominator == 1, "hook-content value integral")
    return value.numerator


def addable_shapes(shape, alphabet):
    ans = []
    for row in range(len(shape) + 1):
        if row == len(shape):
            if len(shape) < alphabet:
                ans.append(shape + (1,))
        elif row == 0 or shape[row - 1] > shape[row]:
            target = list(shape)
            target[row] += 1
            ans.append(tuple(target))
    return ans


def verify_rsk():
    global SECTION
    SECTION = "RSK iid-word shape growth"
    sample_shapes = None
    for alphabet in range(2, 5):
        previous = {(): Q(1)}
        for length in range(1, 8):
            counts = defaultdict(int)
            for word in product(range(alphabet), repeat=length):
                tableau = ()
                for letter in word:
                    tableau = row_insert(tableau, letter)
                counts[tableau_shape(tableau)] += 1
            distribution = {shape: Q(count, alphabet**length) for shape, count in counts.items()}
            equal(sum(distribution.values()), Q(1), "RSK shape mass")
            for shape, count in counts.items():
                expected_count = standard_tableaux_count(shape) * schur_ones(shape, alphabet)
                equal(count, expected_count, "RSK hook-content endpoint law")
            pushed = defaultdict(Q)
            for shape, mass in previous.items():
                denominator = alphabet * schur_ones(shape, alphabet) if shape else alphabet
                for target in addable_shapes(shape, alphabet):
                    probability = Q(schur_ones(target, alphabet), denominator)
                    pushed[target] += mass * probability
                equal(sum(Q(schur_ones(target, alphabet), denominator)
                          for target in addable_shapes(shape, alphabet)), Q(1),
                      "RSK Schur transition row")
            equal(dict(pushed), distribution, "RSK shape Markov kernel")
            previous = distribution
            if alphabet == 4 and length == 7:
                sample_shapes = len(distribution)
    SAMPLES["RSK"] = f"shapes_m4_t7={sample_shapes}"


# ---------------------------------------------------------------------------
# MCA: random digit-position addition modulo b^h


def modular_add_distribution(base, height, weights, steps):
    modulus = base**height
    dist = {0: Q(1)}
    increments = [base**i for i in range(height)]
    for _ in range(steps):
        nxt = defaultdict(Q)
        for state, mass in dist.items():
            for increment, weight in zip(increments, weights):
                nxt[(state + increment) % modulus] += mass * weight
        dist = dict(nxt)
    return dist


def carry_count(value, base, height, position):
    count = 0
    for i in range(position, height):
        digit = (value // (base**i)) % base
        if digit != base - 1:
            break
        count += 1
    return count


def verify_mca():
    global SECTION
    SECTION = "MCA modular carry addition"
    for base in range(2, 6):
        for height in range(1, 5):
            denominator = height * (height + 1) // 2
            weights = [Q(i + 1, denominator) for i in range(height)]
            one_step = modular_add_distribution(base, height, weights, 1)
            for i, weight in enumerate(weights):
                equal(one_step[base**i], weight, "MCA one-layer weight inverse")
            for steps in range(1, 6):
                direct = defaultdict(int)
                for choices in product(range(height), repeat=steps):
                    value = sum(base**i for i in choices) % (base**height)
                    multiplicity_weight = Q(1)
                    for i in choices:
                        multiplicity_weight *= weights[i]
                    direct[value] += multiplicity_weight
                equal(dict(direct), modular_add_distribution(base, height, weights, steps),
                      "MCA sequence/convolution agreement")
            modulus = base**height
            for position in range(height):
                for ell in range(1, height - position + 1):
                    count = sum(carry_count(value, base, height, position) >= ell
                                for value in range(modulus))
                    equal(Q(count, modulus), Q(1, base**ell), "MCA stationary carry tail")
    SAMPLES["MCA"] = "weighted_one_layer_recovers_increment_weights"


# ---------------------------------------------------------------------------
# RGE: uniformly random nonzero Schur pivot over F_2


def matrix_rank_f2(matrix):
    if not matrix:
        return 0
    rows = [sum(bit << j for j, bit in enumerate(row)) for row in matrix]
    rank = 0
    columns = len(matrix[0])
    for col in range(columns):
        pivot = next((i for i in range(rank, len(rows)) if rows[i] & (1 << col)), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i] & (1 << col):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def schur_pivot_f2(matrix, pivot_row, pivot_col):
    row_indices = [i for i in range(len(matrix)) if i != pivot_row]
    col_indices = [j for j in range(len(matrix[0])) if j != pivot_col]
    return tuple(
        tuple(matrix[i][j] ^ (matrix[i][pivot_col] & matrix[pivot_row][j])
              for j in col_indices)
        for i in row_indices
    )


@lru_cache(maxsize=None)
def pivot_histories(matrix):
    pivots = [(i, j) for i, row in enumerate(matrix) for j, bit in enumerate(row) if bit]
    if not pivots:
        return 1
    return sum(pivot_histories(schur_pivot_f2(matrix, i, j)) for i, j in pivots)


def matrix_from_mask(n, mask):
    return tuple(tuple((mask >> (i * n + j)) & 1 for j in range(n)) for i in range(n))


def verify_rge():
    global SECTION
    SECTION = "RGE random Schur pivot elimination"
    history_values_rank3 = set()
    for n in range(1, 4):
        for mask in range(1 << (n * n)):
            matrix = matrix_from_mask(n, mask)
            rank = matrix_rank_f2(matrix)
            pivots = [(i, j) for i, row in enumerate(matrix) for j, bit in enumerate(row) if bit]
            for i, j in pivots:
                residual = schur_pivot_f2(matrix, i, j)
                equal(matrix_rank_f2(residual), rank - 1, "Schur pivot lowers rank by one")
            histories = pivot_histories(matrix)
            check(histories >= 1, "pivot history count positive")
            if n == 3 and rank == 3:
                history_values_rank3.add(histories)
    check(len(history_values_rank3) > 1, "RGE history law not rank-only")
    SAMPLES["RGE"] = "rank3_history_values=" + ",".join(map(str, sorted(history_values_rank3)))


# ---------------------------------------------------------------------------
# RNC: random compatible-diagonal insertion


def compatible_extensions(state, n):
    return [d for d in diagonals(n) if d not in state and all(not crosses(d, e, n) for e in state)]


def verify_rnc():
    global SECTION
    SECTION = "RNC noncrossing chord insertion"
    endpoint_ranges = []
    for n in range(4, 8):
        distribution = {frozenset(): Q(1)}
        for _ in range(n - 3):
            nxt = defaultdict(Q)
            for state, mass in distribution.items():
                choices = compatible_extensions(state, n)
                check(choices, "RNC nonmaximal state has extension")
                for chosen in choices:
                    target = frozenset(set(state) | {chosen})
                    check(noncrossing(target, n), "RNC update stays noncrossing")
                    nxt[target] += mass / len(choices)
            distribution = dict(nxt)
            equal(sum(distribution.values()), Q(1), "RNC layer mass")
        endpoints = set(triangulations(n))
        equal(set(distribution), endpoints, "RNC reaches every triangulation")
        masses = list(distribution.values())
        endpoint_ranges.append((min(masses), max(masses)))
        # The pentagon is still uniform; the first asymmetry occurs for the
        # hexagon, which is an important boundary case for this candidate.
        if n >= 6:
            check(min(masses) < max(masses), "RNC endpoint law nonuniform")
    SAMPLES["RNC"] = "mass_ranges_n4..7=" + ";".join(f"{lo}..{hi}" for lo, hi in endpoint_ranges)


# ---------------------------------------------------------------------------
# RMI: orbit of a uniformly random mapping


def orbit_tail_cycle(mapping):
    seen = {}
    path = []
    state = 0
    while state not in seen:
        seen[state] = len(path)
        path.append(state)
        state = mapping[state]
    tail = seen[state]
    cycle = len(path) - tail
    return tail, cycle


def falling(n, k):
    answer = 1
    for i in range(k):
        answer *= n - i
    return answer


def verify_rmi():
    global SECTION
    SECTION = "RMI random-mapping orbit"
    sample_joint = None
    for n in range(1, 7):
        counts = defaultdict(int)
        for mapping in product(range(n), repeat=n):
            counts[orbit_tail_cycle(mapping)] += 1
        equal(sum(counts.values()), n**n, "RMI mapping census")
        for tail in range(n):
            for cycle in range(1, n - tail + 1):
                r = tail + cycle
                expected = falling(n - 1, r - 1) * n ** (n - r)
                equal(counts[(tail, cycle)], expected, "RMI exact tail-cycle law")
        if n == 6:
            sample_joint = counts[(2, 2)]
    SAMPLES["RMI"] = f"n6_count_tail2_cycle2={sample_joint}/46656"


def main():
    verify_atf()
    verify_rbf()
    verify_ran()
    verify_grs()
    verify_sbs()
    verify_rsk()
    verify_mca()
    verify_rge()
    verify_rnc()
    verify_rmi()
    for name in sorted(COUNTS):
        print(f"{name}: assertions={COUNTS[name]} sample={SAMPLES.get(name.split()[0], '-')}")
    print(f"PASS systems=10 selected=0 assertions={ASSERTIONS}")


if __name__ == "__main__":
    main()
