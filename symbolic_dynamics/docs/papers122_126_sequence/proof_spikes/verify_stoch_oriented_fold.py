#!/usr/bin/env python3
"""Exact falsification controls for S01 oriented adjacent-fold.

The controls deliberately separate four statements which can otherwise be
confused: the literal Markov chain, the static edge-priority realization, the
permutation MNA statistic, and the unrelated forgetting process.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def poly_add(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def poly_mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def poly_scale(a, scalar):
    return tuple(scalar * x for x in a)


def fold_by_priority(n, edge_order):
    alive = set(range(1, n + 1))
    for edge in edge_order:
        if edge in alive and edge + 1 in alive:
            alive.remove(edge + 1)
    return frozenset(alive)


def fold_by_automaton(n, edge_order):
    if n == 0:
        return frozenset()
    if n == 1:
        return frozenset((1,))
    rank = {edge: time for time, edge in enumerate(edge_order)}
    survivor = [False] * (n + 1)
    survivor[1] = True
    survivor[2] = False
    for vertex in range(3, n + 1):
        survivor[vertex] = (
            not survivor[vertex - 1]
            and rank[vertex - 2] < rank[vertex - 1]
        )
    return frozenset(i for i in range(1, n + 1) if survivor[i])


def mna(edge_order):
    """MNA of the edge-priority word, by left greedy scan."""
    rank = {edge: time for time, edge in enumerate(edge_order)}
    priority_word = tuple(rank[edge] for edge in range(1, len(edge_order) + 1))
    chosen = 0
    i = 0
    while i + 1 < len(priority_word):
        if priority_word[i] < priority_word[i + 1]:
            chosen += 1
            i += 2
        else:
            i += 1
    return chosen


@lru_cache(None)
def literal_terminal_law(n, mask):
    legal = [
        i for i in range(n - 1)
        if (mask & (1 << i)) and (mask & (1 << (i + 1)))
    ]
    if not legal:
        return ((mask, Fraction(1)),)
    answer = defaultdict(Fraction)
    for i in legal:
        child = mask & ~(1 << (i + 1))
        for terminal, mass in literal_terminal_law(n, child):
            answer[terminal] += mass / len(legal)
    return tuple(sorted(answer.items()))


def mask_of(vertices):
    return sum(1 << (v - 1) for v in vertices)


def independent_support(n):
    answer = []
    for size in range(n + 1):
        for subset in combinations(range(1, n + 1), size):
            subset = frozenset(subset)
            if 1 in subset and all(i + 1 not in subset for i in subset):
                answer.append(subset)
    return frozenset(answer)


def block_lengths(m, cuts):
    if m == 0:
        return ()
    points = (0,) + tuple(sorted(cuts)) + (m,)
    return tuple(points[i + 1] - points[i] for i in range(len(points) - 1))


def subsets(values):
    values = tuple(sorted(values))
    for r in range(len(values) + 1):
        yield from combinations(values, r)


@lru_cache(None)
def descent_set_count(m, descents_tuple):
    """Number beta_m(B) of permutations with exact descent set B."""
    descents = frozenset(descents_tuple)
    total = 0
    for allowed_tuple in subsets(descents):
        lengths = block_lengths(m, allowed_tuple)
        alpha = factorial(m)
        for length in lengths:
            alpha //= factorial(length)
        total += (-1) ** (len(descents) - len(allowed_tuple)) * alpha
    return total


def point_fibre_formula(n, terminal):
    if n <= 1:
        return int(terminal == frozenset(range(1, n + 1)))
    if terminal not in independent_support(n):
        return 0
    m = n - 1
    required_up = frozenset(
        vertex - 2 for vertex in terminal if vertex >= 3
    )
    required_down = frozenset(
        vertex - 2
        for vertex in range(3, n + 1)
        if vertex not in terminal and vertex - 1 not in terminal
    )
    free_descent_places = frozenset(range(1, m)) - required_up
    answer = 0
    optional = free_descent_places - required_down
    for extra in subsets(optional):
        descents = tuple(sorted(required_down | frozenset(extra)))
        answer += descent_set_count(m, descents)
    return answer


def forgetting_size(order):
    memory = {0}
    for value in order:
        old_minimum = min(memory)
        memory.add(value)
        if value > old_minimum:
            memory.remove(old_minimum)
    return len(memory)


def series_mul(a, b, degree):
    out = [Fraction(0)] * (degree + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= degree:
                out[i + j] += x * y
    return out


def main():
    # Exhaustive literal/priority/automaton/MNA and point-fibre controls.
    permutation_cases = 0
    fibre_tables = {}
    count_laws = {}
    for n in range(1, 11):
        fibres = Counter()
        count_law = Counter()
        for edge_order in permutations(range(1, n)):
            terminal = fold_by_priority(n, edge_order)
            automaton_terminal = fold_by_automaton(n, edge_order)
            permutation_cases += 1
            check(terminal == automaton_terminal,
                  (n, edge_order, terminal, automaton_terminal))
            check(len(terminal) == 1 + mna(edge_order),
                  (n, edge_order, terminal, mna(edge_order)))
            fibres[terminal] += 1
            count_law[len(terminal)] += 1

        support = independent_support(n)
        check(frozenset(fibres) == support, (n, "support", fibres, support))
        for terminal in support:
            check(fibres[terminal] == point_fibre_formula(n, terminal),
                  (n, terminal, fibres[terminal], point_fibre_formula(n, terminal)))

        literal = dict(literal_terminal_law(n, (1 << n) - 1))
        priority = {
            mask_of(terminal): Fraction(count, factorial(max(0, n - 1)))
            for terminal, count in fibres.items()
        }
        check(literal == priority, (n, "literal versus priorities", literal, priority))
        fibre_tables[n] = fibres
        count_laws[n] = count_law

    # First-event recurrence for probability polynomials through n=40.
    probabilities = [(Fraction(1),), (Fraction(0), Fraction(1))]
    for n in range(2, 41):
        numerator = (Fraction(0),)
        for i in range(1, n):
            numerator = poly_add(numerator, poly_mul(probabilities[i], probabilities[n - i - 1]))
        probabilities.append(poly_scale(numerator, Fraction(1, n - 1)))
        check(sum(probabilities[n]) == 1, (n, "PGF mass"))

    for n, counts in count_laws.items():
        expected = tuple(Fraction(counts[k], factorial(max(0, n - 1)))
                         for k in range(max(counts) + 1))
        check(probabilities[n] == expected, (n, "recurrence versus MNA", probabilities[n], expected))

    # Closed OGF: D(z,u)(F(z,u)-1)=u z, coefficientwise.
    # D_0=1, D_1=-1, D_k=(1-u)(-1)^k/k! for k>=2.
    denominator = [(Fraction(1),), (Fraction(-1),)]
    for k in range(2, 41):
        c = Fraction((-1) ** k, factorial(k))
        denominator.append((c, -c))
    q = [(Fraction(0),)] + probabilities[1:]
    for n in range(41):
        coefficient = (Fraction(0),)
        for k in range(n + 1):
            coefficient = poly_add(coefficient, poly_mul(denominator[k], q[n - k]))
        target = (Fraction(0), Fraction(1)) if n == 1 else (Fraction(0),)
        check(coefficient == target, (n, "closed OGF", coefficient, target))

    # Factorial moment GFs, checked against the exact PGFs.
    degree = 40
    exp_minus = [Fraction((-1) ** k, factorial(k)) for k in range(degree + 1)]
    one_minus_z = [Fraction(1), Fraction(-1)] + [Fraction(0)] * (degree - 1)
    inv2 = [Fraction(n + 1) for n in range(degree + 1)]
    inv3 = [Fraction((n + 1) * (n + 2), 2) for n in range(degree + 1)]
    z_exp = [Fraction(0)] + exp_minus[:-1]
    mean_series = series_mul(z_exp, inv2, degree)
    exp_minus_minus_b = [exp_minus[k] - one_minus_z[k] for k in range(degree + 1)]
    fac2_num = series_mul(z_exp, exp_minus_minus_b, degree)
    fac2_series = [2 * x for x in series_mul(fac2_num, inv3, degree)]
    for n in range(1, degree + 1):
        mean = sum(Fraction(k) * mass for k, mass in enumerate(probabilities[n]))
        fac2 = sum(Fraction(k * (k - 1)) * mass for k, mass in enumerate(probabilities[n]))
        check(mean == mean_series[n], (n, "mean GF", mean, mean_series[n]))
        check(fac2 == fac2_series[n], (n, "factorial GF", fac2, fac2_series[n]))

    # Exact finite-distribution separation from the forgetting process.
    forgetting_laws = {}
    mismatch_sizes = []
    for m in range(1, 9):
        memory_counts = Counter(forgetting_size(order) for order in permutations(range(1, m + 1)))
        forgetting_laws[m] = memory_counts
        fold_counts = count_laws[m + 1]
        if memory_counts != fold_counts:
            mismatch_sizes.append(m)
    check(forgetting_laws[1] == count_laws[2], "m=1 collision")
    check(forgetting_laws[2] == count_laws[3], "m=2 collision")
    check(forgetting_laws[3] == Counter({2: 4, 1: 1, 3: 1}), "forgetting m=3")
    check(count_laws[4] == Counter({2: 5, 1: 1}), "fold n=4")
    check(mismatch_sizes == list(range(3, 9)), ("mismatch sizes", mismatch_sizes))

    print("oriented adjacent-fold exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"exhaustive_edge_priority_permutations={permutation_cases}; n=1..10")
    print("literal_Markov_vs_priority=n<=10; automaton_and_MNA=n<=10")
    print("pointwise_descent_interval_fibres=all_terminal_sets_n<=10")
    print("PGF_recurrence_and_closed_OGF=n<=40; factorial_moments=n<=40")
    print("support=all independent subsets containing vertex 1")
    print("fold_count_law_n4=" + repr(count_laws[4]))
    print("forgetting_size_law_m3=" + repr(forgetting_laws[3]))
    print("forgetting_distribution_mismatch_m=" + repr(mismatch_sizes))
    print("owner_collision=survivor_count_minus_one_is_MNA_on_S_(n-1)")


if __name__ == "__main__":
    main()
