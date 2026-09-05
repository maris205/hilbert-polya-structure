#!/usr/bin/env python3
"""P204 Review A: independently written graph/recursive-word audit.

No imports from author, candidate, old-paper, or other-review code.
No file, environment, random, network, or third-party data dependencies.
The classical descent adapter is a value-gate test, not an author repair.
"""
from collections import Counter, deque
from functools import cache
from itertools import permutations
from math import comb, factorial
import json


CHECKS = Counter()


def require(condition, tag, witness=None):
    CHECKS[tag] += 1
    if not condition:
        raise AssertionError((tag, witness))


def words(n, prefix=()):
    if len(prefix) == n:
        yield prefix
    else:
        for value in range(len(prefix) + 1):
            yield from words(n, prefix + (value,))


def literal(word, weak=False):
    # Enumerate the complete earlier-index comparison relation; no stack
    # or backwards scan from the author's implementation is reused.
    return tuple(min((i - h for h in range(i)
                      if (word[h] <= word[i] if weak else word[h] < word[i])),
                     default=0) for i in range(len(word)))


def graph(arrows):
    indegree = [0] * len(arrows)
    for target in arrows:
        indegree[target] += 1
    queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
    peeled = []
    while queue:
        vertex = queue.popleft()
        peeled.append(vertex)
        target = arrows[vertex]
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
    tails = [0] * len(arrows)
    periods = [0] * len(arrows)
    cycles = []
    for start, degree in enumerate(indegree):
        if degree and periods[start] == 0:
            cycle = []
            vertex = start
            while not cycle or vertex != start:
                cycle.append(vertex)
                vertex = arrows[vertex]
            cycles.append(tuple(cycle))
            for vertex in cycle:
                periods[vertex] = len(cycle)
    for vertex in reversed(peeled):
        tails[vertex] = tails[arrows[vertex]] + 1
        periods[vertex] = periods[arrows[vertex]]
    return tails, periods, cycles


def intervals(word):
    barriers = [i for i, value in enumerate(word) if value == 0]
    barriers.append(len(word))
    return tuple((left, right - left - 1)
                 for left, right in zip(barriers, barriers[1:])
                 if right > left + 1)


def in_core(word):
    return all(word[r + j] in {1, j}
               for r, m in intervals(word) for j in range(1, m + 1))


def generated_core(n):
    def extend(prefix, run):
        if len(prefix) == n:
            yield prefix
            return
        yield from extend(prefix + (0,), 0)
        yield from extend(prefix + (1,), run + 1)
        if run:
            yield from extend(prefix + (run + 1,), run + 1)
    return set(extend((0,), 0))


def predicted_second(word):
    output = []
    run = 0
    for i, value in enumerate(word):
        if value == 0:
            run = 0
            output.append(0)
        else:
            run += 1
            output.append(run if run > 1 and word[i - 1] < value else 1)
    return tuple(output)


def exchange(word):
    output = list(word)
    for r, m in intervals(word):
        for j in range(2, m + 1):
            output[r + j] = j if word[r + j] == 1 else 1
    return tuple(output)


def ascent_mask(word):
    return sum(1 << i for i in range(len(word) - 1)
               if word[i] < word[i + 1])


def target_mask(target, r, m, time):
    return sum(1 << (j - 2) for j in range(2, m + 1)
               if target[r + j] == (j if time % 2 == 0 else 1))


@cache
def recursive_source_count(r, m, mask):
    # Condition a suffix by its first value, then recurse right-to-left.
    # Every transition appends an actual legal source letter. It does not
    # cut the word into monotone runs and uses no inclusion-exclusion.
    @cache
    def prefix_count(position, following):
        if position == 0:
            return 1
        total = 0
        for value in range(1, r + position + 1):
            if position < m:
                required_rise = bool(mask & (1 << (position - 1)))
                if (value < following) != required_rise:
                    continue
            total += prefix_count(position - 1, value)
        return total
    return prefix_count(m, 0)


@cache
def signed_cut(r, m, mask):
    result = 0
    submask = mask
    while True:
        start = 1
        term = 1
        for position in range(2, m + 2):
            if position == m + 1 or submask & (1 << (position - 2)):
                term *= comb(r + position - 1, position - start)
                start = position
        result += (-1) ** (mask.bit_count() - submask.bit_count()) * term
        if submask == 0:
            return result
        submask = (submask - 1) & mask


def predicted_fibre(target, time, counter):
    if not in_core(target):
        return 0
    answer = 1
    for r, m in intervals(target):
        answer *= counter(r, m, target_mask(target, r, m, time))
    return answer


def fibonacci(index):
    values = [0, 1]
    for _ in range(2, index + 1):
        values.append(values[-2] + values[-1])
    return values[index]


def permutation_descent_mask(permutation):
    return sum(1 << i for i in range(len(permutation) - 1)
               if permutation[i] > permutation[i + 1])


def permutation_ie(m, mask):
    total = 0
    submask = mask
    while True:
        previous = 0
        denominator = 1
        for i in range(1, m + 1):
            if i == m or submask & (1 << (i - 1)):
                denominator *= factorial(i - previous)
                previous = i
        total += (-1) ** (mask.bit_count() - submask.bit_count()) * (
            factorial(m) // denominator)
        if submask == 0:
            return total
        submask = (submask - 1) & mask


def enumerate_positive(r, m):
    census = Counter()
    def grow(prefix, mask):
        if len(prefix) == m:
            census[mask] += 1
            return
        position = len(prefix) + 1
        for value in range(1, r + position + 1):
            new_mask = mask
            if prefix and prefix[-1] < value:
                new_mask |= 1 << (position - 2)
            grow(prefix + (value,), new_mask)
    grow((), 0)
    return census


def main():
    graph_reports = []
    times = (2, 3, 4, 5, 8, 9)
    for n in range(1, 9):
        carrier = list(words(n))
        index = {word: i for i, word in enumerate(carrier)}
        arrows = [index[literal(word)] for word in carrier]
        tails, periods, cycles = graph(arrows)
        generated = generated_core(n)
        graph_core = {carrier[i] for i, tail in enumerate(tails) if tail == 0}
        require(graph_core == generated, 'graph_recurrence_equals_generated_core', n)
        require({carrier[arrows[arrows[i]]] for i in range(len(carrier))} == generated,
                'second_image_surjectivity', n)
        require(len(graph_core) == fibonacci(2 * n - 1), 'recurrent_fibonacci', n)
        require(sum(len(cycle) == 1 for cycle in cycles) == fibonacci(n + 1),
                'fixed_fibonacci', n)
        require(all(len(cycle) in (1, 2) for cycle in cycles), 'exact_period_support', n)
        require(max(tails) == (0 if n < 3 else 1 if n == 3 else 2), 'sharp_graph_tail', n)
        for i, source in enumerate(carrier):
            first = carrier[arrows[i]]
            second = carrier[arrows[arrows[i]]]
            require(tuple(value == 0 for value in source) ==
                    tuple(value == 0 for value in first), 'zero_positions', source)
            require(second == predicted_second(source), 'pointwise_second', source)
            require((tails[i] == 0) == in_core(source), 'core_predicate_vs_graph', source)
            if tails[i] == 0:
                require(first == exchange(source), 'core_involution', source)
            for r, m in intervals(first):
                require(first[r + 1] == 1, 'first_block_start', source)
                for j in range(2, m + 1):
                    require(first[r + j] == 1 or first[r + j] > first[r + j - 1],
                            'first_image_inequality', source)
        for time in times:
            census = Counter()
            for i, source in enumerate(carrier):
                target_index = i
                for _ in range(time):
                    target_index = arrows[target_index]
                target = carrier[target_index]
                census[target] += 1
                require(intervals(source) == intervals(target), 'time_barrier_blocks', (time, source))
                for r, m in intervals(source):
                    require(ascent_mask(source[r + 1:r + m + 1]) ==
                            target_mask(target, r, m, time),
                            'pointwise_phase_mask', (time, source, target))
            for target in carrier:
                recursive = predicted_fibre(target, time, recursive_source_count)
                require(census[target] == recursive, 'all_target_graph_vs_recursive', (time, target))
                require(recursive == predicted_fibre(target, time, signed_cut),
                        'all_target_recursive_vs_cut', (time, target))
            require(sum(census.values()) == factorial(n), 'all_target_mass', (n, time))
        graph_reports.append(dict(n=n, states=len(carrier),
                                  tails=dict(sorted(Counter(tails).items())),
                                  cycles_by_length=dict(sorted(Counter(map(len, cycles)).items()))))

    permutation_censuses = {}
    adapter_rows = []
    for m in range(1, 9):
        census = Counter(permutation_descent_mask(p) for p in permutations(range(m)))
        permutation_censuses[m] = census
        for mask in range(1 << (m - 1)):
            require(census[mask] == permutation_ie(m, mask), 'classical_macmahon_formula', (m, mask))
        for r in range(7):
            for mask in range(1 << (m - 1)):
                actual = recursive_source_count(r, m, mask)
                require(actual == signed_cut(r, m, mask), 'isolated_recursive_vs_cut', (r, m, mask))
                require(actual == comb(r + m, m) * census[mask],
                        'factorized_descent_owner_adapter', (r, m, mask))
                require(actual == recursive_source_count(r, m, ((1 << (m - 1)) - 1) ^ mask),
                        'complementary_masks_equal_count', (r, m, mask))
            if r in (0, 1, 3, 6) and m in (1, 2, 4, 8):
                adapter_rows.append(dict(r=r, m=m, factor=comb(r + m, m),
                                         block_source_mass=factorial(r + m) // factorial(r),
                                         masks=1 << (m - 1)))
    for r in range(4):
        for m in range(1, 6):
            actual = enumerate_positive(r, m)
            for mask in range(1 << (m - 1)):
                require(actual[mask] == recursive_source_count(r, m, mask),
                        'literal_positive_words_vs_recursive', (r, m, mask))

    # Verify the adapter's actual inversion-code map and prefix multiplicity,
    # not only the final counting identity. No old inverse-code code is used.
    for length in range(1, 8):
        suffix_frequencies = {r: Counter() for r in range(length)}
        for p in permutations(range(length)):
            code = tuple(sum(p[h] > p[i] for h in range(i)) for i in range(length))
            require(ascent_mask(code) == permutation_descent_mask(p),
                    'classical_theta_ascent_descent', (p, code))
            require(tuple(i for i, value in enumerate(code) if value == 0) ==
                    tuple(i for i in range(length) if all(p[i] > p[h] for h in range(i))),
                    'classical_theta_zero_record', (p, code))
            for r in range(length):
                block = tuple(value + 1 for value in code[r:])
                suffix_frequencies[r][block] += 1
                require(ascent_mask(block) == permutation_descent_mask(p[r:]),
                        'suffix_adapter_preserves_actual_set', (p, r))
        for r, census in suffix_frequencies.items():
            require(len(census) == factorial(length) // factorial(r),
                    'suffix_adapter_full_support', (length, r))
            for block, count in census.items():
                require(count == factorial(r), 'suffix_adapter_prefix_multiplicity', (length, r, block))

    strict_tie = literal((0, 1, 1))
    weak_tie = literal((0, 1, 1), weak=True)
    require(strict_tie == (0, 1, 2) and weak_tie == (0, 1, 1), 'strict_weak_tie_control')
    require(literal((0, 0, 0), weak=True) == (0, 1, 1), 'weak_rule_breaks_zero_barriers')
    for n in range(4, 33):
        source = (0,) * (n - 4) + (0, 1, 2, 2)
        require(not in_core(literal(source)) and in_core(literal(literal(source))),
                'zero_prepended_sharp_witness', n)
    require(recursive_source_count(0, 2, 1) == 1 and
            recursive_source_count(1, 2, 1) == 3, 'flag_offset_example')
    require(literal(literal((0, 1, 1))) == (0, 1, 1) and
            literal(literal(literal((0, 1, 1)))) == (0, 1, 2), 'phase_target_direction_control')
    print(json.dumps(dict(audit='P204_REVIEW_A_V1',
                          method='comparison-relation arrows / Kahn graph / backwards source-word recursion',
                          times=list(times), graphs=graph_reports,
                          owner_adapter='D(r,m,A) = binom(r+m,m) * beta_m(A-1)',
                          adapter_rows=adapter_rows,
                          checks=dict(sorted(CHECKS.items())), total_checks=sum(CHECKS.values()),
                          mathematical_checks='PASS', paper_value_verdict='KILL_VALUE_INVERSE_AXIS_MACMAHON_ADAPTER'),
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
