#!/usr/bin/env python3
"""The sole frozen MCA pilot; exhaustive 30 boxes / 5,704 allocations."""
from collections import Counter
from functools import reduce
from itertools import product
import json
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent


def forward(f, m):
    loads = Counter(f)
    return tuple((i + loads[i]) % m for i in f)


def orbit(f, arrows):
    seen = {}
    x = f
    while x not in seen:
        seen[x] = len(seen)
        x = arrows[x]
    return seen[x], len(seen) - seen[x]


def recurrence(f, m):
    piles = sorted(Counter(f).items())
    return all((j - i) % gcd(m, u - v) != 0
               for a, (i, u) in enumerate(piles)
               for j, v in piles[a + 1:])


def partitions(n):
    """Canonical restricted-growth construction, independent of forward()."""
    if n == 0:
        yield ()
        return
    for old in partitions(n - 1):
        for i in range(len(old)):
            yield old[:i] + (old[i] + (n - 1,),) + old[i + 1:]
        yield old + ((n - 1,),)


def decode(g, m, blocks_list):
    count = 0
    for blocks in blocks_list:
        used = set()
        valid = True
        for block in blocks:
            j = g[block[0]]
            if any(g[a] != j for a in block):
                valid = False
                break
            i = (j - len(block)) % m
            if i in used:
                valid = False
                break
            used.add(i)
        count += valid
    return count


def main():
    summary_path = HERE / 'evidence01' / 'pilot_summary.json'
    if summary_path.exists():
        raise RuntimeError('refusing scientific rerun / output overwrite')
    boxes = []
    checks = 0
    visited = 0
    max_counterexamples = []
    for m in range(1, 6):
        for n in range(0, 6):
            states = list(product(range(m), repeat=n))
            arrows = {f: forward(f, m) for f in states}
            fibres = Counter(arrows.values())
            block_list = tuple(partitions(n))
            maximum = max(fibres.values())
            constant = fibres[(0,) * n]
            maximizers = [list(g) for g in states if fibres[g] == maximum]
            max_height = 0
            recurrence_count = 0
            periods = set()
            for f in states:
                tail, period = orbit(f, arrows)
                recurrent = recurrence(f, m)
                inverse = decode(f, m, block_list)
                bound = 0 if n == 0 else (min(n, m) - 1) * (m - 1)
                assert recurrent == (tail == 0), ('recurrence', m, n, f)
                assert tail <= bound, ('height', m, n, f, tail, bound)
                assert inverse == fibres[f], ('inverse', m, n, f)
                checks += 3
                if recurrent:
                    exact = 1 if n == 0 else m // reduce(gcd, Counter(f).values(), m)
                    assert period == exact, ('period', m, n, f, period, exact)
                    checks += 1
                    recurrence_count += 1
                    periods.add(period)
                if m == 2:
                    expected = (1 if n % 2 == 0 else
                                (2 ** (n - 1) if len(set(f)) == 1 else 0))
                    assert fibres[f] == expected, ('m2_control', n, f)
                    checks += 1
                if fibres[f] > constant:
                    max_counterexamples.append({'m': m, 'N': n, 'target': f,
                                                'fibre': fibres[f], 'constant': constant})
                max_height = max(max_height, tail)
                visited += 1
                print(json.dumps({'kind': 'state', 'm': m, 'N': n, 'state': f,
                                  'next': arrows[f], 'tail': tail, 'period': period,
                                  'recurrent_predicate': recurrent,
                                  'fibre': fibres[f], 'decoder': inverse}, sort_keys=True))
            boxes.append({'m': m, 'N': n, 'states': len(states),
                          'max_height': max_height, 'recurrent': recurrence_count,
                          'recurrent_periods': sorted(periods),
                          'maximum_fibre': maximum, 'constant_fibre': constant,
                          'maximizers': maximizers})
    assert visited == 5704 and len(boxes) == 30
    result = {'status': 'FINITE_CHECKS_ONLY', 'boxes': boxes,
              'state_count': visited, 'deductive_assertions': checks,
              'constant_max_counterexamples': max_counterexamples,
              'constant_max_proved_all_parameters': False,
              'scientific_executions_in_this_lane': 1}
    summary_path.write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')
    print(json.dumps({'kind': 'summary', **result}, sort_keys=True))


if __name__ == '__main__':
    main()
