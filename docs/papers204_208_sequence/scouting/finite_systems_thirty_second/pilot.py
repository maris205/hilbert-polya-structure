#!/usr/bin/env python3
"""Original ONI graph pilot; exactly n=0,...,5, full original-state output."""
import itertools
import json

checks = 0

def require(statement):
    global checks
    checks += 1
    assert statement

def step(n, mask, pairs):
    nei = [set() for _ in range(n)]
    for k, (u, v) in enumerate(pairs):
        if mask >> k & 1:
            nei[u].add(v)
            nei[v].add(u)
    out = 0
    for k, (u, v) in enumerate(pairs):
        if not nei[u] <= nei[v] and not nei[v] <= nei[u]:
            out |= 1 << k
    return out

def fixed_forbidden(n, mask, pairs):
    edges = {p for k, p in enumerate(pairs) if mask >> k & 1}
    for vertices in itertools.combinations(range(n), 4):
        subedges = [p for p in itertools.combinations(vertices, 2) if p in edges]
        deg = {v: 0 for v in vertices}
        for u, v in subedges:
            deg[u] += 1
            deg[v] += 1
        if len(subedges) == 2 and sorted(deg.values()) == [1, 1, 1, 1]:
            return False
        if len(subedges) == 3 and sorted(deg.values()) == [1, 1, 2, 2]:
            return False
    return True

total = 0
for n in range(6):
    pairs = list(itertools.combinations(range(n), 2))
    size = 1 << len(pairs)
    transitions = [step(n, mask, pairs) for mask in range(size)]
    indegree = [0] * size
    for source, target in enumerate(transitions):
        require(0 <= target < size)
        require(source & target == source)
        indegree[target] += 1
        require((target == source) == fixed_forbidden(n, source, pairs))
    tails = []
    cycles = []
    trajectories = []
    for source in range(size):
        seen = {}
        orbit = []
        state = source
        while state not in seen:
            seen[state] = len(orbit)
            orbit.append(state)
            state = transitions[state]
        tail = seen[state]
        period = len(orbit) - tail
        require(period == 1)
        require(tail <= len(pairs) - source.bit_count())
        tails.append(tail)
        cycles.append(period)
        trajectories.append(orbit + [state])
        print(json.dumps(dict(kind='state', n=n, source=source,
                              target=transitions[source], tail=tail,
                              period=period, indegree=indegree[source]), sort_keys=True))
    maximum_tail = max(tails)
    maximum_fibre = max(indegree)
    witness = tails.index(maximum_tail)
    print(json.dumps(dict(kind='summary', n=n, states=size, image=sum(x > 0 for x in indegree),
                          fixed=sum(transitions[x] == x for x in range(size)),
                          max_tail=maximum_tail, max_fibre=maximum_fibre,
                          fibre_extremizers=[x for x in range(size) if indegree[x] == maximum_fibre],
                          tail_witness=trajectories[witness], pairs=pairs), sort_keys=True))
    total += size
print(json.dumps(dict(kind='end', total_states=total, checks=checks,
                      status='bounded scouting only; no all-parameter inference'), sort_keys=True))
