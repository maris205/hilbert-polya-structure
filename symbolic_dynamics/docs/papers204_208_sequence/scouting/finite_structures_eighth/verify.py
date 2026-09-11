#!/usr/bin/env python3
"""Separately implemented AUTHOR check; not independent scientific review.

No pilot imports. Reconstructs precisely the 105 intake carriers and checks
every canonical profile field. Uses Kahn deletion, matching subset DP,
explicit path subsets and reverse-reachability closure. Writes stdout only.
"""
from collections import Counter, deque
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math


def partition_table(limit):
    table = [[()] if n == 0 else [] for n in range(limit + 1)]
    for part in range(1, limit + 1):
        for total in range(part, limit + 1):
            table[total].extend((part,) + tail for tail in table[total - part])
    return table


def gaps(a):
    columns = [sum(row >= c for row in a) for c in range(1, max(a, default=0) + 1)]
    return tuple(sorted((height * number for height, number in Counter(columns).items()), reverse=True))


def square(a):
    d = 0
    while d < len(a) and a[d] > d:
        d += 1
    rows = [sum(not (r < d and c < d) for c in range(length))
            for r, length in enumerate(a)]
    return tuple(sorted([v for v in rows if v] + ([d * d] if d else []), reverse=True))


def matching(a, n, rows, columns):
    values = {0: 1}
    for row in rows:
        nxt = {}
        for chosen, count in values.items():
            for index, column in enumerate(columns):
                if not (chosen >> index) & 1 and (a >> (row * n + column)) & 1:
                    key = chosen | (1 << index)
                    nxt[key] = nxt.get(key, 0) + count
        values = nxt
    return values.get((1 << len(columns)) - 1, 0)


def adjugate(a, n, parity=False):
    out = 0
    for row in range(n):
        for column in range(n):
            count = matching(a, n, [r for r in range(n) if r != column],
                             [c for c in range(n) if c != row])
            if (count % 2 == 1) if parity else (count == 1):
                out |= 1 << (row * n + column)
    return out


def path_transform(a, n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    edge = {pair: (a >> index) & 1 for index, pair in enumerate(pairs)}
    out = 0
    for index, (i, j) in enumerate(pairs):
        number = 0
        for size in range(j - i):
            for middle in combinations(range(i + 1, j), size):
                walk = (i,) + middle + (j,)
                number += all(edge[u, v] for u, v in zip(walk, walk[1:]))
        if number % 3 == 1:
            out |= 1 << index
    return out


def backward(f):
    n = len(f)
    reachable = [[i == j or f[i] == j + 1 for j in range(n)] for i in range(n)]
    for middle in range(n):
        for source in range(n):
            if reachable[source][middle]:
                for target in range(n):
                    reachable[source][target] |= reachable[middle][target]
    return tuple(sum(reachable[j][i] for j in range(n)) for i in range(n))


def fit(a, capacity, detail=False):
    bins = []
    assignment = []
    for item in a:
        where = 0
        while where < len(bins) and sum(bins[where]) + item > capacity:
            where += 1
        if where == len(bins):
            bins.append([])
        bins[where].append(item)
        assignment.append(where)
    residuals = [capacity - sum(b) for b in bins]
    result = tuple(residuals[where] for where in assignment)
    return (result, residuals) if detail else result


def freeze(x):
    return tuple(freeze(y) for y in x) if isinstance(x, list) else x


def verify_profile(row, states, operation):
    states = sorted(states)
    assert len(states) == len(set(states))
    arrows = {state: operation(state) for state in states}
    assert set(arrows.values()) <= set(states)
    fibre = Counter(arrows.values())
    indegree = {state: fibre[state] for state in states}
    queue = deque(state for state in states if not indegree[state])
    deleted = []
    while queue:
        state = queue.popleft()
        deleted.append(state)
        child = arrows[state]
        indegree[child] -= 1
        if not indegree[child]:
            queue.append(child)
    cyclic = {state for state in states if indegree[state]}
    cycles = []
    pending = set(cyclic)
    period = {}
    while pending:
        start = min(pending)
        cycle = [start]
        state = arrows[start]
        while state != start:
            cycle.append(state)
            state = arrows[state]
        pending.difference_update(cycle)
        cycles.append(tuple(cycle))
        for state in cycle:
            period[state] = len(cycle)
    height = {state: 0 for state in cyclic}
    for state in reversed(deleted):
        height[state] = height[arrows[state]] + 1
        period[state] = period[arrows[state]]
    max_height = max(height.values())
    witness = min(state for state in states if height[state] == max_height)
    orbit = [witness]
    for _ in range(max_height + period[witness]):
        orbit.append(arrows[orbit[-1]])
    histogram = Counter(map(len, cycles))
    observed = {
        'states': len(states), 'image': len(fibre), 'recurrent': len(cyclic),
        'fixed': histogram[1], 'cycles': {str(k): v for k, v in sorted(histogram.items())},
        'height': max_height, 'height_witness_orbit': tuple(orbit),
        'max_fibre': max(fibre.values()),
        'max_fibre_targets': tuple(sorted(a for a, count in fibre.items() if count == max(fibre.values()))),
        'longest_cycle': max(cycles, key=lambda a: (len(a), a)),
        'transition_sha256': hashlib.sha256(json.dumps(sorted(arrows.items()), separators=(',', ':')).encode()).hexdigest(),
    }
    for field, value in observed.items():
        assert value == freeze(row[field]), (row['literal'], row['parameters'], field, value, row[field])
    assert sum(fibre.values()) == len(states)
    assert len(cyclic) == sum(k * v for k, v in histogram.items())
    return states, arrows, fibre


def main():
    rows = [json.loads(line) for line in Path(__file__).with_name('PILOT_CANONICAL.jsonl').read_text().splitlines()]
    partitions = partition_table(24)
    expected = ([('WGP', {'N': n}) for n in range(25)] + [('DSR', {'N': n}) for n in range(25)]
                + [('UPA', {'n': n}) for n in range(5)] + [('DP3', {'n': n}) for n in range(7)]
                + [('BRF', {'n': n}) for n in range(7)]
                + [('FFR', {'M': m, 'k': k}) for m in range(6) for k in range(6)])
    assert [(row['literal'], row['parameters']) for row in rows] == expected
    total = 0
    nonparity = None
    matching_branch_count = 0
    for row in rows:
        name, p = row['literal'], row['parameters']
        if name in ('WGP', 'DSR'):
            states, operation = partitions[p['N']], gaps if name == 'WGP' else square
        elif name == 'UPA':
            n = p['n']
            states, operation = range(1 << (n * n)), lambda a: adjugate(a, n)
        elif name == 'DP3':
            n = p['n']
            states, operation = range(1 << (n * (n - 1) // 2)), lambda a: path_transform(a, n)
        elif name == 'BRF':
            n = p['n']
            states, operation = product(range(1, n + 1), repeat=n), backward
        else:
            m, k = p['M'], p['k']
            states, operation = product(range(m + 1), repeat=k), lambda a: fit(a, m)
        states, arrows, fibre = verify_profile(row, states, operation)
        total += len(states)
        extra = {}
        if name == 'DSR':
            predicted = []
            for a in states:
                d = sum(value >= i for i, value in enumerate(a, 1))
                staircase = tuple(d * j for j in range(d, 0, -1))
                formula = a[:d] == staircase and all(value <= d for value in a[d:])
                assert formula == (arrows[a] == a)
                if formula:
                    predicted.append(a)
            static_count = int(p['N'] == 0)
            for d in range(1, math.isqrt(p['N']) + 1):
                residue = p['N'] - d * d * (d + 1) // 2
                if residue >= 0:
                    static_count += sum(not a or a[0] <= d for a in partitions[residue])
            assert static_count == len(predicted) == row['fixed']
            extra['fixed_characterization_checked'] = len(states)
        if name == 'UPA':
            if n <= 3:
                assert all(arrows[a] == adjugate(a, n, True) for a in states)
            for a in states:
                if matching(a, n, list(range(n)), list(range(n))) == 1:
                    twice = arrows[arrows[a]]
                    assert arrows[arrows[twice]] == twice
                    matching_branch_count += 1
                if n == 4 and nonparity is None and arrows[a] != adjugate(a, n, True):
                    nonparity = {'n': n, 'matrix_bits': a, 'unique_bits': arrows[a], 'parity_bits': adjugate(a, n, True)}
            extra['unique_matching_branch_U4_U2'] = 'PASS'
        if name == 'DP3':
            bound = 1 if n < 2 else 2 ** (n - 2)
            assert all(bound % int(length) == 0 for length in row['cycles'])
            assert row['height'] <= max(0, bound - 1)
            extra['generic_period_divisor'] = bound
        if name == 'BRF' and n:
            assert fibre[(n,) * n] == math.factorial(n - 1)
            for i in range(n):
                target = tuple(1 if j == i else n for j in range(n))
                assert fibre[target] == math.factorial(n - 1)
            extra['named_fibres'] = math.factorial(n - 1)
        if name == 'FFR':
            for a in states:
                _, residuals = fit(a, m, True)
                assert all(x + y < m for x, y in combinations(residuals, 2))
            extra['pairwise_bin_residual_control'] = len(states)
        print(json.dumps({'literal': name, 'parameters': p, 'states_checked': len(states),
                          'status': 'PASS_SEPARATE_AUTHOR_CHECK', **extra}, sort_keys=True, separators=(',', ':')), flush=True)
    assert gaps((4, 2, 1)) == (3, 2, 2)
    assert square((2, 2)) == (4,)
    assert square((10, 10)) == (8, 8, 4)
    orbit = [(1, 1)]
    for _ in range(3):
        orbit.append(fit(orbit[-1], 5))
    assert orbit == [(1, 1), (3, 3), (2, 2), (1, 1)]
    assert nonparity is not None
    print(json.dumps({'status': 'PASS_AUTHOR_CONTROLS', 'boxes': len(rows), 'state_map_pairs': total,
                      'UPA_first_nonparity_sentinel': nonparity,
                      'UPA_unique_matching_states_checked': matching_branch_count,
                      'FFR_three_cycle_M5_k2': orbit,
                      'WGP_gap_vs_copies_input': [4, 2, 1],
                      'DSR_increasing_Durfee_input': [10, 10], 'DSR_increasing_Durfee_output': [8, 8, 4]},
                     sort_keys=True, separators=(',', ':')), flush=True)


if __name__ == '__main__':
    main()
