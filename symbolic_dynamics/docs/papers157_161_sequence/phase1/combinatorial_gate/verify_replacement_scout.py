#!/usr/bin/env python3
"""Deterministic exact scout for twelve post-gate replacement systems.

No lane imports an earlier portfolio verifier.  The point is counterexample
pressure and signature discovery, not proof by exhaustion.
"""

from __future__ import annotations

from collections import Counter
from functools import cache
from itertools import combinations, permutations, product
from math import comb


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, witness: object = None) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(witness)


A = Audit()


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def cycle_profile(states, update) -> tuple[Counter[int], int, int]:
    states = tuple(states)
    state_set = set(states)
    image = {state: update(state) for state in states}
    A.check(set(image.values()) <= state_set)
    visited = set()
    cycles: Counter[int] = Counter()
    for state in states:
        if state in visited:
            continue
        local = {}
        point = state
        while point not in local and point not in visited:
            local[point] = len(local)
            point = image[point]
        if point in local:
            cycles[len(local) - local[point]] += 1
        visited.update(local)
    max_tail = 0
    max_period = 0
    for state in states:
        local = {}
        point = state
        while point not in local:
            local[point] = len(local)
            point = image[point]
        max_tail = max(max_tail, local[point])
        max_period = max(max_period, len(local) - local[point])
    return cycles, max_tail, max_period


# ---------------------------------------------------------------------------
# TLS: a cyclic Temperley--Lieb generator sweep on link patterns.


@cache
def noncrossing_matchings(points: tuple[int, ...]) -> tuple[tuple, ...]:
    if not points:
        return ((),)
    first = points[0]
    answer = []
    for split in range(1, len(points), 2):
        second = points[split]
        for left in noncrossing_matchings(points[1:split]):
            for right in noncrossing_matchings(points[split + 1 :]):
                answer.append(canonical_matching(((first, second),) + left + right))
    return tuple(answer)


def canonical_matching(edges) -> tuple[tuple[int, int], ...]:
    return tuple(sorted(tuple(sorted(edge)) for edge in edges))


def tl_generator(matching: tuple, index: int, points: int) -> tuple:
    neighbor = (index + 1) % points
    partner = {a: b for edge in matching for a, b in (edge, edge[::-1])}
    if partner[index] == neighbor:
        return matching
    left, right = partner[index], partner[neighbor]
    untouched = [
        edge
        for edge in matching
        if not set(edge) & {index, neighbor, left, right}
    ]
    return canonical_matching(untouched + [(index, neighbor), (left, right)])


def tl_sweep(matching: tuple, points: int) -> tuple:
    for index in range(points):
        matching = tl_generator(matching, index, points)
    return matching


def rotate_matching(matching: tuple, points: int, shift: int) -> tuple:
    return canonical_matching(
        (((left + shift) % points, (right + shift) % points) for left, right in matching)
    )


def strip_boundary(matching: tuple, points: int) -> tuple:
    return canonical_matching(
        (left - 1, right - 1)
        for left, right in matching
        if (left, right) != (0, points - 1)
    )


def dyck_returns(matching: tuple, points: int) -> int:
    openers = {left for left, _ in matching}
    height = 0
    returns = 0
    for position in range(points):
        height += 1 if position in openers else -1
        returns += height == 0
    return returns


def audit_tls() -> tuple[list[int], list[int], list[int], list[int]]:
    state_counts, image_counts, max_periods, max_fibres = [], [], [], []
    for n in range(1, 10):
        points = 2 * n
        states = noncrossing_matchings(tuple(range(points)))
        fibres = Counter(tl_sweep(state, points) for state in states)
        state_counts.append(len(states))
        image_counts.append(len(fibres))
        max_fibres.append(max(fibres.values()))
        A.check(len(states) == catalan(n))
        A.check(len(fibres) == catalan(n - 1))
        for target, indegree in fibres.items():
            A.check((0, points - 1) in target)
            interior = strip_boundary(target, points)
            rotated = rotate_matching(interior, points - 2, 1)
            A.check(indegree == 1 + dyck_returns(rotated, points - 2))
        if n == 1:
            max_periods.append(1)
            continue
        embedded = [
            canonical_matching(
                ((0, points - 1),)
                + tuple((left + 1, right + 1) for left, right in inner)
            )
            for inner in noncrossing_matchings(tuple(range(points - 2)))
        ]
        for state in embedded:
            after = tl_sweep(state, points)
            A.check(
                strip_boundary(after, points)
                == rotate_matching(strip_boundary(state, points), points - 2, -2)
            )
        _, tail, period = cycle_profile(states, lambda state: tl_sweep(state, points))
        A.check(tail <= 1)
        max_periods.append(period)
        k = n - 1
        distribution = Counter(fibres.values())
        for r in range(1, k + 1):
            ballot = r * comb(2 * k - r - 1, k - 1) // k
            A.check(distribution[r + 1] == ballot, (n, r, distribution))
    return state_counts, image_counts, max_periods, max_fibres


# ---------------------------------------------------------------------------
# DFG: alternating face flips of 2-by-n domino tilings.


def independent_sets(path_vertices: int) -> tuple[int, ...]:
    return tuple(
        mask
        for mask in range(1 << path_vertices)
        if not (mask & (mask << 1))
    )


def toggle_parity(mask: int, path_vertices: int, parity: int) -> int:
    old = mask
    answer = mask
    for vertex in range(1, path_vertices + 1):
        if vertex % 2 != parity:
            continue
        bit = 1 << (vertex - 1)
        if old & bit:
            answer ^= bit
            continue
        neighbors = 0
        if vertex > 1:
            neighbors |= 1 << (vertex - 2)
        if vertex < path_vertices:
            neighbors |= 1 << vertex
        if not old & neighbors:
            answer ^= bit
    return answer


def domino_gyration(mask: int, path_vertices: int) -> int:
    return toggle_parity(toggle_parity(mask, path_vertices, 0), path_vertices, 1)


def audit_dfg() -> list[int]:
    maxima = []
    for width in range(1, 21):
        states = independent_sets(width - 1)
        images = {domino_gyration(state, width - 1) for state in states}
        A.check(len(images) == len(states))
        _, tail, period = cycle_profile(
            states, lambda state: domino_gyration(state, width - 1)
        )
        A.check(tail == 0)
        maxima.append(period)
        if width >= 5:
            A.check(period == 3 * width - 10, (width, period))
    return maxima


# ---------------------------------------------------------------------------
# MVT: Markoff-surface Vieta rotor over finite prime fields.


def audit_mvt() -> tuple[list[int], list[int]]:
    counts, maxima = [], []
    for prime in (3, 5, 7, 11, 13, 17, 19):
        states = tuple(
            (x, y, z)
            for x in range(prime)
            for y in range(prime)
            for z in range(prime)
            if (x * x + y * y + z * z - 3 * x * y * z) % prime == 0
        )

        def update(state):
            x, y, z = state
            return y, z, (3 * y * z - x) % prime

        for state in states:
            x, y, z = update(state)
            A.check((x * x + y * y + z * z - 3 * x * y * z) % prime == 0)
        A.check(len({update(state) for state in states}) == len(states))
        _, tail, period = cycle_profile(states, update)
        A.check(tail == 0)
        counts.append(len(states))
        maxima.append(period)
    return counts, maxima


# ---------------------------------------------------------------------------
# NFR: Nielsen--Fibonacci map (x,y) -> (y,xy) on symmetric groups.


def permutation_product(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[i]] for i in range(len(left)))


def audit_nfr() -> tuple[list[int], list[int]]:
    counts, maxima = [], []
    for degree in range(1, 5):
        group = tuple(permutations(range(degree)))
        states = tuple(product(group, repeat=2))

        def update(state):
            left, right = state
            return right, permutation_product(left, right)

        A.check(len({update(state) for state in states}) == len(states))
        _, tail, period = cycle_profile(states, update)
        A.check(tail == 0)
        counts.append(len(states))
        maxima.append(period)
    return counts, maxima


# ---------------------------------------------------------------------------
# HWT: a full Hurwitz sweep on reduced transposition factorizations.


def permutation_inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(permutation.index(i) for i in range(len(permutation)))


def conjugate(conjugator: tuple[int, ...], element: tuple[int, ...]) -> tuple[int, ...]:
    return permutation_product(
        permutation_product(permutation_inverse(conjugator), element), conjugator
    )


def transposition(degree: int, left: int, right: int) -> tuple[int, ...]:
    answer = list(range(degree))
    answer[left], answer[right] = answer[right], answer[left]
    return tuple(answer)


def factorization_product(word: tuple[tuple[int, ...], ...], degree: int) -> tuple[int, ...]:
    answer = tuple(range(degree))
    for factor in word:
        answer = permutation_product(answer, factor)
    return answer


def hurwitz_sweep(word: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    answer = list(word)
    for index in range(len(answer) - 1):
        left, right = answer[index], answer[index + 1]
        answer[index], answer[index + 1] = right, conjugate(right, left)
    return tuple(answer)


def audit_hwt() -> tuple[list[int], list[int]]:
    counts, maxima = [], []
    for degree in range(2, 7):
        factors = tuple(
            transposition(degree, i, j)
            for i in range(degree)
            for j in range(i + 1, degree)
        )
        long_cycle = tuple(range(1, degree)) + (0,)
        states = tuple(
            word
            for word in product(factors, repeat=degree - 1)
            if factorization_product(word, degree) == long_cycle
        )
        A.check(len(states) == degree ** (degree - 2))
        for state in states:
            A.check(factorization_product(hurwitz_sweep(state), degree) == long_cycle)
        A.check(len({hurwitz_sweep(state) for state in states}) == len(states))
        _, tail, period = cycle_profile(states, hurwitz_sweep)
        A.check(tail == 0)
        counts.append(len(states))
        maxima.append(period)
    return counts, maxima


# ---------------------------------------------------------------------------
# BWT: the Burrows--Wheeler last-column map on distinct-letter words.


def bwt(permutation: tuple[int, ...]) -> tuple[int, ...]:
    if not permutation:
        return ()
    rotations = sorted(
        permutation[index:] + permutation[:index] for index in range(len(permutation))
    )
    return tuple(rotation[-1] for rotation in rotations)


def audit_bwt() -> tuple[list[int], list[int], list[int]]:
    image_counts, tails, periods = [], [], []
    for n in range(1, 9):
        states = tuple(permutations(range(n)))
        fibres = Counter(bwt(state) for state in states)
        A.check(set(fibres.values()) == {n})
        A.check(len(fibres) == (len(states) // n))
        _, tail, period = cycle_profile(states, bwt)
        image_counts.append(len(fibres))
        tails.append(tail)
        periods.append(period)
    return image_counts, tails, periods


# ---------------------------------------------------------------------------
# RAC: fixed-width reverse-and-add with carries modulo the base power.


def reverse_digits(value: int, base: int, width: int) -> int:
    answer = 0
    for _ in range(width):
        answer = base * answer + value % base
        value //= base
    return answer


def audit_rac() -> tuple[list[int], list[int], list[int]]:
    images, tails, periods = [], [], []
    base = 3
    for width in range(1, 9):
        modulus = base**width

        def update(value):
            return (value + reverse_digits(value, base, width)) % modulus

        states = tuple(range(modulus))
        profile, tail, period = cycle_profile(states, update)
        A.check(profile[1] >= 1)
        images.append(len({update(value) for value in states}))
        tails.append(tail)
        periods.append(period)
    return images, tails, periods


# ---------------------------------------------------------------------------
# CRW: greedy lex-decreasing Coxeter-relation rewrite on w0 reduced words.


@cache
def reduced_words_w0(degree: int, permutation: tuple[int, ...] | None = None):
    if permutation is None:
        permutation = tuple(range(1, degree + 1))
    target = tuple(range(degree, 0, -1))
    if permutation == target:
        return ((),)
    answer = []
    for index in range(degree - 1):
        if permutation[index] < permutation[index + 1]:
            successor = (
                permutation[:index]
                + (permutation[index + 1], permutation[index])
                + permutation[index + 2 :]
            )
            for suffix in reduced_words_w0(degree, successor):
                answer.append((index + 1,) + suffix)
    return tuple(answer)


def coxeter_rewrite(word: tuple[int, ...]) -> tuple[int, ...]:
    candidates = []
    for index in range(len(word) - 1):
        left, right = word[index : index + 2]
        if abs(left - right) > 1 and right < left:
            candidates.append((index, word[:index] + (right, left) + word[index + 2 :]))
    for index in range(len(word) - 2):
        left, middle, right = word[index : index + 3]
        if left == right and abs(left - middle) == 1:
            replacement = (middle, left, middle)
            if replacement < (left, middle, right):
                candidates.append((index, word[:index] + replacement + word[index + 3 :]))
    if not candidates:
        return word
    return min(candidates, key=lambda item: (item[0], item[1]))[1]


def audit_crw() -> tuple[list[int], list[int], list[int]]:
    counts, fixed, maxima = [], [], []
    for degree in range(2, 6):
        states = reduced_words_w0(degree)
        state_set = set(states)
        tails = []
        terminal = set()
        for state in states:
            point = state
            time = 0
            while True:
                successor = coxeter_rewrite(point)
                A.check(successor in state_set)
                if successor == point:
                    terminal.add(point)
                    break
                A.check(successor < point)
                point = successor
                time += 1
            tails.append(time)
        counts.append(len(states))
        fixed.append(len(terminal))
        maxima.append(max(tails))
    return counts, fixed, maxima


# ---------------------------------------------------------------------------
# PPR: rowmotion on order ideals of small three-chain products.


def product_poset_ideals(box: tuple[int, int, int]):
    elements = tuple(product(*(range(side) for side in box)))
    lower = tuple(
        sum(
            1 << j
            for j, candidate in enumerate(elements)
            if all(candidate[d] <= element[d] for d in range(3))
        )
        for element in elements
    )
    ideals = tuple(
        mask
        for mask in range(1 << len(elements))
        if all(not (mask >> i & 1) or not (lower[i] & ~mask) for i in range(len(elements)))
    )
    return lower, ideals


def rowmotion(mask: int, lower: tuple[int, ...]) -> int:
    minimal_complement = [
        i
        for i, downset in enumerate(lower)
        if not (mask >> i & 1) and not ((downset & ~(1 << i)) & ~mask)
    ]
    answer = 0
    for index in minimal_complement:
        answer |= lower[index]
    return answer


def audit_ppr() -> tuple[list[int], list[int]]:
    counts, periods = [], []
    for box in ((2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 2), (3, 3, 1)):
        lower, states = product_poset_ideals(box)
        A.check(len({rowmotion(state, lower) for state in states}) == len(states))
        _, tail, period = cycle_profile(states, lambda state: rowmotion(state, lower))
        A.check(tail == 0)
        counts.append(len(states))
        periods.append(period)
    return counts, periods


# ---------------------------------------------------------------------------
# LPS: row/symbol parastrophe on Latin squares.


def latin_squares(order: int) -> tuple[tuple[tuple[int, ...], ...], ...]:
    rows = tuple(permutations(range(order)))
    answer = []

    def extend(prefix: list[tuple[int, ...]]) -> None:
        if len(prefix) == order:
            answer.append(tuple(prefix))
            return
        for row in rows:
            if all(row[column] not in {old[column] for old in prefix} for column in range(order)):
                prefix.append(row)
                extend(prefix)
                prefix.pop()

    extend([])
    return tuple(answer)


def latin_parastrophe(square: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    order = len(square)
    answer = [[0] * order for _ in range(order)]
    for row in range(order):
        for column in range(order):
            answer[square[row][column]][column] = row
    return tuple(tuple(row) for row in answer)


def audit_lps() -> tuple[list[int], list[int]]:
    counts, fixed = [], []
    for order in range(1, 5):
        states = latin_squares(order)
        for state in states:
            A.check(latin_parastrophe(latin_parastrophe(state)) == state)
        counts.append(len(states))
        fixed.append(sum(latin_parastrophe(state) == state for state in states))
    return counts, fixed


# ---------------------------------------------------------------------------
# FPG: swap point and line under the standard projective polarity.


def projective_points(prime: int) -> tuple[tuple[int, int, int], ...]:
    answer = set()
    for vector in product(range(prime), repeat=3):
        if vector == (0, 0, 0):
            continue
        pivot = next(value for value in vector if value)
        inverse = pow(pivot, -1, prime)
        answer.add(tuple(value * inverse % prime for value in vector))
    return tuple(sorted(answer))


def audit_fpg() -> tuple[list[int], list[int]]:
    counts, fixed = [], []
    for prime in (2, 3, 5):
        points = projective_points(prime)
        flags = tuple(
            (point, line)
            for point in points
            for line in points
            if sum(x * y for x, y in zip(point, line)) % prime == 0
        )
        A.check(len(flags) == (prime * prime + prime + 1) * (prime + 1))
        A.check(all((line, point) in set(flags) for point, line in flags))
        counts.append(len(flags))
        fixed.append(sum(point == line for point, line in flags))
    return counts, fixed


# ---------------------------------------------------------------------------
# PTR: rotate convex-polygon triangulations.


@cache
def interval_triangulations(left: int, right: int) -> tuple[frozenset, ...]:
    if right - left < 2:
        return (frozenset(),)
    answer = []
    for middle in range(left + 1, right):
        for first in interval_triangulations(left, middle):
            for second in interval_triangulations(middle, right):
                diagonals = set(first) | set(second)
                if middle - left > 1:
                    diagonals.add((left, middle))
                if right - middle > 1:
                    diagonals.add((middle, right))
                answer.append(frozenset(diagonals))
    return tuple(answer)


def rotate_triangulation(triangulation: frozenset, vertices: int) -> frozenset:
    return frozenset(
        tuple(sorted(((left + 1) % vertices, (right + 1) % vertices)))
        for left, right in triangulation
    )


def audit_ptr() -> tuple[list[int], list[int]]:
    counts, periods = [], []
    for vertices in range(3, 13):
        states = interval_triangulations(0, vertices - 1)
        A.check(len(states) == catalan(vertices - 2))
        A.check(len({rotate_triangulation(state, vertices) for state in states}) == len(states))
        _, tail, period = cycle_profile(
            states, lambda state: rotate_triangulation(state, vertices)
        )
        A.check(tail == 0)
        counts.append(len(states))
        periods.append(period)
    return counts, periods


def main() -> None:
    tls = audit_tls()
    dfg = audit_dfg()
    mvt = audit_mvt()
    nfr = audit_nfr()
    hwt = audit_hwt()
    bwt_data = audit_bwt()
    rac = audit_rac()
    crw = audit_crw()
    ppr = audit_ppr()
    lps = audit_lps()
    fpg = audit_fpg()
    ptr = audit_ptr()
    print("COMBINATORIAL_GATE_REPLACEMENT_SCOUT v1")
    print(f"TLS states/images/max-period/max-fibre n=1..9: {tls}")
    print(f"DFG max periods width=1..20: {dfg}")
    print(f"MVT states/max-period p=3,5,7,11,13,17,19: {mvt}")
    print(f"NFR states/max-period S_1..S_4: {nfr}")
    print(f"HWT states/max-period degree=2..6: {hwt}")
    print(f"BWT images/max-tail/max-period n=1..8: {bwt_data}")
    print(f"RAC images/max-tail/max-period base=3 width=1..8: {rac}")
    print(f"CRW states/fixed/max-tail degree=2..5: {crw}")
    print(f"PPR states/max-period boxes: {ppr}")
    print(f"LPS states/fixed order=1..4: {lps}")
    print(f"FPG states/fixed q=2,3,5: {fpg}")
    print(f"PTR states/max-period vertices=3..12: {ptr}")
    print("STRONGEST TLS: image retraction + rotation core + target fibre law")
    print("OWNER_KILL DFG: exact path-independent-set Coxeter toggle action")
    print("REPLACEMENT_SYSTEMS 12")
    print(f"ASSERTIONS {A.assertions}")
    print("PASS")


if __name__ == "__main__":
    main()
