#!/usr/bin/env python3
"""Inspect original recorded rows; never evaluates/imports the ONI map."""
import itertools
import json
import math
import pathlib

OWN = pathlib.Path(__file__).resolve().parent
raw_a = (OWN / 'commands/08_oni_pilot_a/stdout.raw').read_bytes()
raw_b = (OWN / 'commands/09_oni_pilot_b/stdout.raw').read_bytes()
assert raw_a == raw_b
records = [json.loads(s) for s in raw_a.splitlines()]
checks = 1

def need(x):
    global checks
    checks += 1
    assert x

def neighbourhoods(n, mask):
    result = [set() for _ in range(n)]
    for bit, (u, v) in enumerate(itertools.combinations(range(n), 2)):
        if mask >> bit & 1:
            result[u].add(v)
            result[v].add(u)
    return result

def stirling(a, k):
    if a == 0:
        return int(k == 0)
    if k == 0:
        return 0
    return stirling(a - 1, k - 1) + k * stirling(a - 1, k)

total_targets = 0
for n in range(6):
    states = {r['source']: r for r in records if r['kind'] == 'state' and r['n'] == n}
    need(len(states) == 1 << (n * (n - 1) // 2))
    predecessors = {target: [] for target in states}
    for source, row in states.items():
        predecessors[row['target']].append(source)
        src_nei = neighbourhoods(n, source)
        dst_nei = neighbourhoods(n, row['target'])
        need([bool(s) for s in src_nei] == [bool(s) for s in dst_nei])
    for target, row in states.items():
        nei = neighbourhoods(n, target)
        support = {u for u in range(n) if nei[u]}
        need(len(predecessors[target]) == row['indegree'])
        if not support:
            need(predecessors[target] == [0])
            print(json.dumps(dict(n=n, target=target, parts=[], count=1, predecessors=[0]), sort_keys=True))
            total_targets += 1
            continue
        first = min(support)
        part_b = nei[first]
        part_a = support - part_b
        if any(nei[u] != part_b for u in part_a) or any(nei[v] != part_a for v in part_b):
            continue
        a, b = len(part_a), len(part_b)
        formula = sum(math.factorial(k)**2 * stirling(a, k) * stirling(b, k)
                      for k in range(1, min(a, b) + 1))
        need(formula == len(predecessors[target]))
        for source in predecessors[target]:
            src = neighbourhoods(n, source)
            need(all(src[u] and src[u] <= part_b for u in part_a))
            need(all(src[v] and src[v] <= part_a for v in part_b))
            need(all(src[u] <= src[v] or src[v] <= src[u]
                     for u in part_a for v in part_a))
        print(json.dumps(dict(n=n, target=target, parts=[sorted(part_a),sorted(part_b)],
                              count=formula, predecessors=predecessors[target]), sort_keys=True))
        total_targets += 1
print(json.dumps(dict(status='PASS same recorded data only', checks=checks,
                      complete_bipartite_or_empty_targets=total_targets), sort_keys=True))
