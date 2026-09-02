#!/usr/bin/env python3
"""Exact Stage-1 pressure tests for combinatorial replacement scout 2.

The program is intentionally deterministic.  Literal enumeration is used to
look for counterexamples and to replay finite profiles; it is not presented as
an all-parameter proof or as evidence of novelty/priority.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial


class Audit:
    def __init__(self):
        self.assertions = 0
        self.boxes = 0

    def check(self, condition, message=""):
        self.assertions += 1
        if not condition:
            raise AssertionError(message or f"assertion {self.assertions} failed")

    def box(self):
        self.boxes += 1


A = Audit()


def standardize(values):
    values = tuple(values)
    rank = {v: i + 1 for i, v in enumerate(sorted(values))}
    return tuple(rank[v] for v in values)


def identity(n):
    return tuple(range(1, n + 1))


def permutation_iter(n):
    return permutations(range(1, n + 1))


# ---------------------------------------------------------------------------
# CME: cycle-maximum extraction


def cycle_supports(p):
    seen = set()
    blocks = []
    for start in range(1, len(p) + 1):
        if start in seen:
            continue
        block = []
        x = start
        while x not in seen:
            seen.add(x)
            block.append(x)
            x = p[x - 1]
        blocks.append(tuple(sorted(block)))
    blocks.sort(key=lambda b: b[0])
    return tuple(blocks)


def cme(p):
    return standardize(max(block) for block in cycle_supports(p))


@lru_cache(None)
def cme_tail(p):
    q = cme(p)
    if q == p:
        A.check(p == identity(len(p)), ("CME nonidentity fixed point", p))
        return 0
    return 1 + cme_tail(q)


def direct_sum(p, q):
    return tuple(p) + tuple(len(p) + x for x in q)


def right_to_left_minima(sigma):
    minimum = len(sigma) + 1
    count = 0
    for value in reversed(sigma):
        if value < minimum:
            minimum = value
            count += 1
    return count


@lru_cache(None)
def cme_schedule_dp(sigma):
    """Independently find the shortest O/C/S endpoint schedule."""
    m = len(sigma)
    inv = [0] * m
    for i, value in enumerate(sigma):
        inv[value - 1] = i

    @lru_cache(None)
    def dp(i, j):
        # i openers and j closers have already appeared.
        if i == m and j == m:
            return 0
        choices = []
        if i < m:  # opener only
            choices.append(1 + dp(i + 1, j))
        if j < m and inv[j] < i:  # closer of an already open block
            choices.append(1 + dp(i, j + 1))
        if i < m and j < m and inv[j] == i:  # singleton opener/closer
            choices.append(1 + dp(i + 1, j + 1))
        return min(choices)

    return dp(0, 0)


def cme_min_source_rank(sigma):
    """Closed image threshold: 2m minus the RTL-minimum count."""
    return 2 * len(sigma) - right_to_left_minima(sigma)


def rgs_words(n):
    if n == 0:
        yield ()
        return

    def rec(prefix, maximum):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for value in range(maximum + 2):
            prefix.append(value)
            yield from rec(prefix, max(maximum, value))
            prefix.pop()

    yield from rec([0], 0)


def blocks_from_rgs(word):
    blocks = [[] for _ in range(max(word, default=-1) + 1)]
    for value, block in enumerate(word, 1):
        blocks[block].append(value)
    return tuple(tuple(block) for block in blocks)


def cme_support_formula(n):
    """All target fibres via ordered supports and prod (|B|-1)! weights."""
    answer = Counter()
    support_terms = 0
    for word in rgs_words(n):
        blocks = blocks_from_rgs(word)  # RGS order is increasing block minimum.
        target = standardize(max(block) for block in blocks)
        weight = 1
        for block in blocks:
            weight *= factorial(len(block) - 1)
        answer[target] += weight
        support_terms += 1
    return answer, support_terms


def reverse_permutation(n):
    return tuple(range(n, 0, -1))


def reverse_preimage(m):
    """The involution (1,2m-1)(2,2m-2)...(m), a source of reverse_m."""
    n = 2 * m - 1
    p = list(range(1, n + 1))
    for i in range(1, m):
        j = n + 1 - i
        p[i - 1] = j
        p[j - 1] = i
    return tuple(p)


def audit_cme():
    maxima = []
    censuses = []
    images = []
    fixed = []
    literal_images = {}
    literal_fibres = {}
    min_rank_by_tail = {}
    states = 0

    for n in range(1, 11):
        A.box()
        fibres = Counter()
        census = Counter()
        fixed_here = 0
        for p in permutation_iter(n):
            states += 1
            q = cme(p)
            A.check(1 <= len(q) <= n, ("CME closure", p, q))
            A.check(sorted(q) == list(range(1, len(q) + 1)))
            A.check(len(q) == len(cycle_supports(p)))
            t = cme_tail(p)
            census[t] += 1
            fibres[q] += 1
            min_rank_by_tail.setdefault(t, n)
            if q == p:
                fixed_here += 1
                A.check(p == identity(n))
        maxima.append(max(census))
        censuses.append(dict(sorted(census.items())))
        images.append(len(fibres))
        fixed.append(fixed_here)
        literal_images[n] = set(fibres)
        if n <= 8:
            literal_fibres[n] = fibres

    A.check(maxima == [0, 1, 2, 2, 3, 3, 3, 3, 4, 4])
    A.check(fixed == [1] * 10)
    A.check({t: min_rank_by_tail[t] for t in range(5)} ==
            {0: 1, 1: 2, 2: 3, 3: 5, 4: 9})

    # Exact all-rank image threshold in the tested boxes.
    schedule_checks = 0
    for m in range(1, 9):
        for sigma in permutation_iter(m):
            r = cme_min_source_rank(sigma)
            A.check(cme_schedule_dp(sigma) == r,
                    ("CME schedule closed form", sigma, cme_schedule_dp(sigma), r))
            A.check(m <= r <= 2 * m - 1)
            for n in range(m, 11):
                A.check((sigma in literal_images[n]) == (n >= r),
                        ("CME image", sigma, n, r))
                schedule_checks += 1
            t = cme_tail(sigma)
            if t == 0:
                A.check(r >= 1)
            else:
                # Finite pressure only: this is the unproved global clock gate.
                A.check(r >= 2 ** t + 1, ("CME power gate", sigma, r, t))

    # Every-target support formula, including targets with zero fibres.
    fibre_checks = 0
    support_terms = 0
    for n in range(1, 9):
        formula, terms = cme_support_formula(n)
        support_terms += terms
        A.check(sum(formula.values()) == factorial(n))
        A.check(formula == literal_fibres[n], ("CME fibre dictionary", n))
        for m in range(1, n + 1):
            for sigma in permutation_iter(m):
                A.check(formula.get(sigma, 0) == literal_fibres[n].get(sigma, 0))
                fibre_checks += 1

    # Direct-sum firewall and the exact reverse witnesses.
    sum_checks = 0
    small = {n: tuple(permutation_iter(n)) for n in range(1, 5)}
    for a in range(1, 5):
        for b in range(1, 5):
            for p in small[a]:
                for q in small[b]:
                    A.check(cme(direct_sum(p, q)) == direct_sum(cme(p), cme(q)))
                    A.check(cme_tail(direct_sum(p, q)) == max(cme_tail(p), cme_tail(q)))
                    sum_checks += 1

    witnesses = []
    for t in range(0, 6):
        rank = 1 if t == 0 else 2 ** (t - 1) + 1
        w = reverse_permutation(rank)
        A.check(cme_tail(w) == t, ("CME reverse witness", t, w))
        if t:
            source = reverse_preimage(rank)
            A.check(len(source) == 2 ** t + 1)
            A.check(cme(source) == w)
        witnesses.append((t, rank))

    return {
        "states": states,
        "max_tail": maxima,
        "tail_census": censuses,
        "image_counts": images,
        "min_rank_by_tail": {t: min_rank_by_tail[t] for t in range(5)},
        "schedule_checks": schedule_checks,
        "fibre_checks": fibre_checks,
        "support_terms": support_terms,
        "sum_checks": sum_checks,
        "witnesses": witnesses,
    }


# ---------------------------------------------------------------------------
# PMT: partition-multiplicity transform


@lru_cache(None)
def integer_partitions(n, maximum=None):
    if n == 0:
        return ((),)
    if maximum is None or maximum > n:
        maximum = n
    answer = []
    for first in range(maximum, 0, -1):
        for rest in integer_partitions(n - first, first):
            answer.append((first,) + rest)
    return tuple(answer)


def pmt(part):
    return tuple(sorted(Counter(part).values(), reverse=True))


@lru_cache(None)
def pmt_tail(part):
    q = pmt(part)
    if q == part:
        A.check(part == (1,))
        return 0
    return 1 + pmt_tail(q)


def pmt_min_source_rank(mu):
    return sum((i + 1) * value for i, value in enumerate(mu))


def pmt_section(mu):
    values = []
    for part_value, multiplicity in enumerate(mu, 1):
        values.extend([part_value] * multiplicity)
    return tuple(sorted(values, reverse=True))


@lru_cache(None)
def unique_permutations(values):
    """Multiset permutations without first materializing k! duplicates."""
    values = tuple(values)
    if not values:
        return ((),)
    answer = []
    for value in sorted(set(values)):
        remaining = list(values)
        remaining.remove(value)
        for suffix in unique_permutations(tuple(remaining)):
            answer.append((value,) + suffix)
    return tuple(answer)


def pmt_fibre_formula(mu, n):
    k = len(mu)
    total = 0
    for distinct_parts in combinations(range(1, n + 1), k):
        for assignment in unique_permutations(mu):
            if sum(a * multiplicity for a, multiplicity in zip(distinct_parts, assignment)) == n:
                total += 1
    return total


def audit_pmt():
    maxima, images, censuses = [], [], []
    min_rank_by_tail = {}
    literal_fibres = {}
    states = 0
    for n in range(1, 31):
        A.box()
        fibres = Counter()
        census = Counter()
        for part in integer_partitions(n):
            states += 1
            q = pmt(part)
            t = pmt_tail(part)
            fibres[q] += 1
            census[t] += 1
            min_rank_by_tail.setdefault(t, n)
            A.check(sum(q) == len(part))
            A.check(n >= pmt_min_source_rank(q), ("PMT rank", part, q))
        maxima.append(max(census))
        images.append(len(fibres))
        censuses.append(dict(sorted(census.items())))
        if n <= 16:
            literal_fibres[n] = fibres

    A.check(maxima[:14] == [0, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6])
    A.check({t: min_rank_by_tail[t] for t in range(7)} ==
            {0: 1, 1: 2, 2: 2, 3: 3, 4: 4, 5: 7, 6: 14})

    section_checks = 0
    fibre_checks = 0
    for m in range(1, 13):
        for mu in integer_partitions(m):
            source = pmt_section(mu)
            A.check(pmt(source) == mu)
            A.check(sum(source) == pmt_min_source_rank(mu))
            section_checks += 1
            for n in range(m, 17):
                formula = pmt_fibre_formula(mu, n)
                literal = literal_fibres[n].get(mu, 0)
                A.check(formula == literal, ("PMT fibre", mu, n, formula, literal))
                A.check((literal > 0) == (n >= pmt_min_source_rank(mu))
                        if n == pmt_min_source_rank(mu) else True)
                fibre_checks += 1

    return {
        "states": states,
        "max_tail_1_to_30": maxima,
        "image_counts_1_to_16": images[:16],
        "min_rank_by_tail": {t: min_rank_by_tail[t] for t in range(7)},
        "section_checks": section_checks,
        "fibre_checks": fibre_checks,
    }


# ---------------------------------------------------------------------------
# FOT: Foata's first fundamental transformation, iterated as a bijection


def ordered_cycles_with_max_first(p):
    cycles = []
    seen = set()
    for start in range(1, len(p) + 1):
        if start in seen:
            continue
        cycle = []
        x = start
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = p[x - 1]
        j = cycle.index(max(cycle))
        cycle = cycle[j:] + cycle[:j]
        cycles.append(tuple(cycle))
    return tuple(sorted(cycles, key=lambda c: c[0]))


def foata(p):
    return tuple(x for cycle in ordered_cycles_with_max_first(p) for x in cycle)


def audit_foata():
    maxima = []
    cycle_censuses = []
    expected = [1, 1, 3, 7, 25, 216, 963, 23435]
    for n in range(1, 9):
        A.box()
        states = tuple(permutation_iter(n))
        images = {foata(p) for p in states}
        A.check(len(images) == factorial(n))
        seen = set()
        census = Counter()
        for p in states:
            if p in seen:
                continue
            orbit = []
            q = p
            while q not in seen:
                seen.add(q)
                orbit.append(q)
                q = foata(q)
            A.check(q in orbit)
            census[len(orbit)] += 1
        A.check(sum(length * count for length, count in census.items()) == factorial(n))
        maxima.append(max(census))
        cycle_censuses.append(dict(sorted(census.items())))
    A.check(maxima == expected)
    return {"max_period": maxima, "cycle_census_n8": cycle_censuses[-1]}


# ---------------------------------------------------------------------------
# LGT: iterated line graph on graph isomorphism classes


@lru_cache(None)
def canonical_graph(n, edges):
    edges = tuple(sorted(tuple(sorted(e)) for e in edges))
    if n <= 1:
        return (n, ())
    best = None
    for perm in permutations(range(n)):
        moved = tuple(sorted(tuple(sorted((perm[u], perm[v]))) for u, v in edges))
        if best is None or moved < best:
            best = moved
    return (n, best)


def graph(n, edges):
    return canonical_graph(n, tuple(edges))


def line_graph(g):
    _, edges = g
    new_edges = []
    for i, e in enumerate(edges):
        for j in range(i + 1, len(edges)):
            if set(e) & set(edges[j]):
                new_edges.append((i, j))
    return graph(len(edges), new_edges)


def path_graph(n):
    return graph(n, ((i, i + 1) for i in range(n - 1)))


def cycle_graph(n):
    return graph(n, ((i, (i + 1) % n) for i in range(n)))


def star_graph(leaves):
    return graph(leaves + 1, ((0, i) for i in range(1, leaves + 1)))


def complete_graph(n):
    return graph(n, combinations(range(n), 2))


def audit_line_graph():
    A.box()
    path_tails = []
    empty = path_graph(0)
    for n in range(0, 9):
        p = path_graph(n)
        q = p
        tail = 0
        while q != empty:
            q = line_graph(q)
            tail += 1
            A.check(tail <= n + 1)
        A.check(tail == n)
        path_tails.append(tail)
    for n in range(3, 9):
        c = cycle_graph(n)
        A.check(line_graph(c) == c)
    A.check(line_graph(star_graph(3)) == complete_graph(3))
    A.check(line_graph(complete_graph(3)) == complete_graph(3))
    k4_line = line_graph(complete_graph(4))
    A.check(k4_line[0] == 6 and len(k4_line[1]) == 12)
    return {"path_tail_n0_to_8": path_tails, "K4_line": (k4_line[0], len(k4_line[1]))}


# ---------------------------------------------------------------------------
# POD: order dual plus label reversal on naturally labelled finite posets


def is_transitive_relation(n, relation):
    R = set(relation)
    for i, j in R:
        for j2, k in R:
            if j == j2 and (i, k) not in R:
                return False
    return True


def naturally_labelled_posets(n):
    pairs = tuple(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        relation = tuple(pairs[i] for i in range(len(pairs)) if mask & (1 << i))
        if is_transitive_relation(n, relation):
            yield relation


def poset_dual_relabel(n, relation):
    return tuple(sorted((n - 1 - j, n - 1 - i) for i, j in relation))


def audit_poset_dual():
    counts, fixed = [], []
    for n in range(1, 7):
        A.box()
        states = tuple(naturally_labelled_posets(n))
        images = set()
        fixed_here = 0
        for relation in states:
            q = poset_dual_relabel(n, relation)
            A.check(is_transitive_relation(n, q))
            A.check(poset_dual_relabel(n, q) == relation)
            images.add(q)
            fixed_here += q == relation
        A.check(len(images) == len(states))
        counts.append(len(states))
        fixed.append(fixed_here)
    A.check(counts == [1, 2, 7, 40, 357, 4824])
    return {"states_n1_to_6": counts, "fixed_n1_to_6": fixed}


# ---------------------------------------------------------------------------
# HBL: blocker duality on nonempty clutters


def clutters(n):
    subsets = tuple(range(1, 1 << n))
    for mask in range(1, 1 << len(subsets)):
        family = tuple(subsets[i] for i in range(len(subsets)) if mask & (1 << i))
        if all(not (a != b and a & b == a) for a in family for b in family):
            yield tuple(sorted(family))


def blocker(n, clutter):
    hitting = []
    for candidate in range(1, 1 << n):
        if all(candidate & edge for edge in clutter):
            hitting.append(candidate)
    minimal = [candidate for candidate in hitting
               if not any(other != candidate and other & candidate == other for other in hitting)]
    return tuple(sorted(minimal))


def audit_blocker():
    counts, fixed = [], []
    for n in range(1, 5):
        A.box()
        states = tuple(clutters(n))
        images = set()
        fixed_here = 0
        for clutter in states:
            q = blocker(n, clutter)
            A.check(blocker(n, q) == clutter, ("blocker involution", n, clutter, q))
            images.add(q)
            fixed_here += q == clutter
        A.check(len(images) == len(states))
        counts.append(len(states))
        fixed.append(fixed_here)
    return {"clutters_n1_to_4": counts, "self_blocking_n1_to_4": fixed}


# ---------------------------------------------------------------------------
# SYT: tableau transpose on the disjoint union of all shapes of rank n


@lru_cache(None)
def all_syt(n):
    if n == 1:
        return (((1,),),)
    answer = set()
    for tableau in all_syt(n - 1):
        rows = [list(row) for row in tableau]
        for r in range(len(rows) + 1):
            if r == len(rows):
                candidate = rows + [[n]]
            else:
                new_length = len(rows[r]) + 1
                if r > 0 and new_length > len(rows[r - 1]):
                    continue
                candidate = [row[:] for row in rows]
                candidate[r].append(n)
            answer.add(tuple(tuple(row) for row in candidate))
    return tuple(sorted(answer))


def tableau_transpose(tableau):
    width = len(tableau[0])
    return tuple(tuple(tableau[r][c] for r in range(len(tableau)) if c < len(tableau[r]))
                 for c in range(width))


def audit_tableau_transpose():
    counts, fixed = [], []
    for n in range(1, 10):
        A.box()
        states = all_syt(n)
        images = set()
        fixed_here = 0
        for tableau in states:
            q = tableau_transpose(tableau)
            A.check(tableau_transpose(q) == tableau)
            images.add(q)
            fixed_here += q == tableau
        A.check(len(images) == len(states))
        counts.append(len(states))
        fixed.append(fixed_here)
    A.check(counts == [1, 2, 4, 10, 26, 76, 232, 764, 2620])
    A.check(fixed == [1] + [0] * 8)
    return {"states_n1_to_9": counts, "fixed_n1_to_9": fixed}


# ---------------------------------------------------------------------------
# SPR: set-partition reversal on restricted-growth words


def reverse_set_partition(word):
    n = len(word)
    blocks = blocks_from_rgs(word)
    moved = [tuple(sorted(n + 1 - x for x in block)) for block in blocks]
    moved.sort(key=lambda block: block[0])
    owner = {}
    for index, block in enumerate(moved):
        for x in block:
            owner[x] = index
    return tuple(owner[x] for x in range(1, n + 1))


def audit_set_partition_reversal():
    counts, fixed = [], []
    for n in range(1, 10):
        A.box()
        states = tuple(rgs_words(n))
        images = set()
        fixed_here = 0
        for word in states:
            q = reverse_set_partition(word)
            A.check(reverse_set_partition(q) == word)
            images.add(q)
            fixed_here += q == word
        A.check(len(images) == len(states))
        counts.append(len(states))
        fixed.append(fixed_here)
    A.check(counts == [1, 2, 5, 15, 52, 203, 877, 4140, 21147])
    return {"Bell_n1_to_9": counts, "fixed_n1_to_9": fixed}


# ---------------------------------------------------------------------------
# NBR: reflection on binary necklaces


def rotations(word):
    return tuple(word[i:] + word[:i] for i in range(len(word)))


def necklace_canonical(word):
    return min(rotations(tuple(word)))


def binary_necklaces(n):
    states = set()
    for mask in range(1 << n):
        word = tuple((mask >> i) & 1 for i in range(n))
        states.add(necklace_canonical(word))
    return tuple(sorted(states))


def necklace_reflect(word):
    return necklace_canonical(tuple(reversed(word)))


def audit_necklace_reflection():
    counts, fixed = [], []
    for n in range(1, 17):
        A.box()
        states = binary_necklaces(n)
        images = set()
        fixed_here = 0
        for word in states:
            q = necklace_reflect(word)
            A.check(necklace_reflect(q) == word)
            images.add(q)
            fixed_here += q == word
        A.check(len(images) == len(states))
        counts.append(len(states))
        fixed.append(fixed_here)
    return {"necklaces_n1_to_16": counts, "reflection_fixed_n1_to_16": fixed}


# ---------------------------------------------------------------------------
# SOC: orthogonal-complement involution on F_2 subspaces


@lru_cache(None)
def binary_subspaces(d):
    spaces = {frozenset({0})}
    frontier = [frozenset({0})]
    while frontier:
        space = frontier.pop()
        for v in range(1 << d):
            if v in space:
                continue
            enlarged = frozenset(set(space) | {x ^ v for x in space})
            if enlarged not in spaces:
                spaces.add(enlarged)
                frontier.append(enlarged)
    return tuple(sorted(spaces, key=lambda s: (len(s), tuple(sorted(s)))))


def parity(x):
    return x.bit_count() & 1


def orthogonal_complement(d, space):
    return frozenset(v for v in range(1 << d)
                     if all(parity(v & x) == 0 for x in space))


def audit_subspace_orthocomplement():
    counts, fixed = [], []
    for d in range(1, 6):
        A.box()
        states = binary_subspaces(d)
        images = set()
        fixed_here = 0
        for space in states:
            q = orthogonal_complement(d, space)
            A.check(q in states)
            A.check(orthogonal_complement(d, q) == space)
            A.check(len(space) * len(q) == 2 ** d)
            images.add(q)
            fixed_here += q == space
        A.check(len(images) == len(states))
        counts.append(len(states))
        fixed.append(fixed_here)
    A.check(counts == [2, 5, 16, 67, 374])
    return {"subspaces_d1_to_5": counts, "self_dual_d1_to_5": fixed}


def main():
    cme_data = audit_cme()
    pmt_data = audit_pmt()
    foata_data = audit_foata()
    line_data = audit_line_graph()
    poset_data = audit_poset_dual()
    blocker_data = audit_blocker()
    tableau_data = audit_tableau_transpose()
    set_partition_data = audit_set_partition_reversal()
    necklace_data = audit_necklace_reflection()
    subspace_data = audit_subspace_orthocomplement()

    print("COMBINATORIAL_REPLACEMENT2_EXACT_AUDIT")
    print("external_status=HOLD_EXTERNAL")
    print("systems_tested=10")
    print(f"CME_states={cme_data['states']}")
    print(f"CME_max_tail_n1_to_10={cme_data['max_tail']}")
    print(f"CME_tail_census_n1_to_10={cme_data['tail_census']}")
    print(f"CME_image_counts_n1_to_10={cme_data['image_counts']}")
    print(f"CME_min_rank_by_tail={cme_data['min_rank_by_tail']}")
    print(f"CME_schedule_checks={cme_data['schedule_checks']}")
    print(f"CME_fibre_checks={cme_data['fibre_checks']}")
    print(f"CME_support_terms={cme_data['support_terms']}")
    print(f"CME_direct_sum_checks={cme_data['sum_checks']}")
    print(f"CME_reverse_witnesses={cme_data['witnesses']}")
    print(f"PMT_states={pmt_data['states']}")
    print(f"PMT_max_tail_n1_to_30={pmt_data['max_tail_1_to_30']}")
    print(f"PMT_image_counts_n1_to_16={pmt_data['image_counts_1_to_16']}")
    print(f"PMT_min_rank_by_tail={pmt_data['min_rank_by_tail']}")
    print(f"PMT_section_checks={pmt_data['section_checks']}")
    print(f"PMT_fibre_checks={pmt_data['fibre_checks']}")
    print(f"FOT_max_period_n1_to_8={foata_data['max_period']}")
    print(f"FOT_cycle_census_n8={foata_data['cycle_census_n8']}")
    print(f"LGT_profile={line_data}")
    print(f"POD_profile={poset_data}")
    print(f"HBL_profile={blocker_data}")
    print(f"SYT_profile={tableau_data}")
    print(f"SPR_profile={set_partition_data}")
    print(f"NBR_profile={necklace_data}")
    print(f"SOC_profile={subspace_data}")
    print("CME_power_clock=UNFALSIFIED_PROOF_GATE")
    print("CME_image_and_fibres=PASS_EXACT")
    print("second_survivor=NONE")
    print(f"boxes={A.boxes}")
    print(f"assertions={A.assertions}")
    print("status=PASS_EXPECTED_PROFILES")


if __name__ == "__main__":
    main()
