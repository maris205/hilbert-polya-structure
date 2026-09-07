"""Complete theorem checks only in the original FTH n=0,...,5 boxes."""
import collections
import itertools
import json
import math
import os
from pathlib import Path
import sys

CHECKS = 0


def require(condition, detail):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(detail)


def literal(f):
    n = len(f)
    answer = list(f)
    for i in range(n):
        for j in range(i + 1, n):
            if f[i] == f[j]:
                answer[i] = j
                break
    return tuple(answer)


def vertex_cycles(f):
    cycles = set()
    for start in range(len(f)):
        walk = []
        v = start
        while v not in walk:
            walk.append(v)
            v = f[v]
        cycles.add(frozenset(walk[walk.index(v):]))
    return sorted(cycles, key=lambda c: min(c))


def predicted_period(f):
    cycles = vertex_cycles(f)
    cyc = set().union(*cycles) if cycles else set()
    indeg = collections.Counter(f)
    if any(indeg[v] > 1 for v in range(len(f)) if v not in cyc):
        return 0
    if any(indeg[v] > 2 for v in cyc):
        return 0
    active = []
    for c in cycles:
        heads = [a for a in range(len(f)) if a not in cyc and f[a] in c]
        if any(a >= min(c) for a in heads):
            return 0
        if heads:
            active.append(len(c))
    return math.lcm(*active)


def all_images(f):
    image = set(range(len(f)))
    result = [image]
    for _ in range(len(f) + 1):
        image = {f[v] for v in image}
        result.append(image)
    return result


def inverse_codes(g):
    eligible = [i for i, v in enumerate(g) if i < v]
    answer = []
    for bits in range(1 << len(eligible)):
        selected = {i for j, i in enumerate(eligible) if bits >> j & 1}
        selected_heads = [g[i] for i in selected]
        if len(selected_heads) != len(set(selected_heads)):
            continue
        ends = [i for i in range(len(g)) if i not in selected]
        end_values = [g[i] for i in ends]
        if len(end_values) != len(set(end_values)):
            continue
        source = []
        for i in range(len(g)):
            while i in selected:
                i = g[i]
            source.append(g[i])
        answer.append((tuple(sorted(selected)), tuple(source)))
    return answer


def main():
    base = Path(__file__).resolve().parent
    old = {}
    with (base / 'original_pilot.stdout').open(encoding='utf8') as source:
        for line in source:
            row = json.loads(line)
            if row.get('rule') == 'FTH':
                old[row['parameter']] = row
    for n in range(6):
        states = list(itertools.product(range(n), repeat=n))
        index = {s: i for i, s in enumerate(states)}
        outputs = [literal(s) for s in states]
        transition = [index[t] for t in outputs]
        fibres = collections.defaultdict(set)
        for s, t in zip(states, outputs):
            fibres[t].add(s)
        require(transition == old[n]['transition'], ('original_transition', n))
        depths, periods, predictions, inverse_counts = [], [], [], []
        for s, t in zip(states, outputs):
            old_images, new_images = all_images(s), all_images(t)
            require(all(a <= b for a, b in zip(old_images, new_images)), ('images', n, s))
            walk, places = [], {}
            u = s
            while u not in places:
                places[u] = len(walk)
                walk.append(u)
                u = literal(u)
            depth = places[u]
            period = len(walk) - depth
            prediction = predicted_period(s)
            require((prediction > 0) == (depth == 0), ('exact_core', n, s))
            require(not prediction or prediction == period, ('exact_period', n, s))
            if depth == 0:
                require(old_images == new_images, ('frozen_images', n, s))
                cycles = vertex_cycles(s)
                cyc = set().union(*cycles) if cycles else set()
                require(cycles == vertex_cycles(t), ('cycles_unchanged', n, s))
                for a in range(n):
                    if a in cyc or s[a] not in cyc:
                        require(t[a] == s[a], ('retained_arrow', n, s, a))
                    else:
                        predecessor = next(v for v in cyc if s[v] == s[a])
                        require(t[a] == predecessor, ('attachment_rotation', n, s, a))
            codes = inverse_codes(s)
            decoded = [source for _, source in codes]
            require(len(decoded) == len(set(decoded)), ('nonredundant_codes', n, s))
            require(set(decoded) == fibres[s], ('complete_inverse', n, s))
            depths.append(depth)
            periods.append(period)
            predictions.append(prediction)
            inverse_counts.append(len(codes))
        require(depths == old[n]['depths'], ('original_depths', n))
        require(inverse_counts == old[n]['indegrees'], ('original_fibres', n))
        maximizers = [s for s, d in zip(states, inverse_counts) if d == max(inverse_counts)]
        desired = tuple(range(1, n)) + (0,) if n else ()
        require(max(inverse_counts) == (2 ** (n - 1) if n else 1), ('sharp_max', n))
        require(maximizers == [desired], ('unique_maximizer', n))
        print(json.dumps(dict(rule='FTH_PROOF_CHECK', parameter=n, states=len(states),
            transition=transition, depths=depths, periods=periods,
            predicted_recurrent_periods=predictions, inverse_counts=inverse_counts,
            recurrent=sum(p > 0 for p in predictions), max_fibre=max(inverse_counts),
            maximizing_targets=maximizers, checks_cumulative=CHECKS), sort_keys=True), flush=True)
    require(literal((1, 2, 1)) == (2, 2, 1), 'ISPRP separation first step')
    require(literal((2, 2, 1)) == (1, 2, 1), 'ISPRP separation return')
    print(json.dumps(dict(result='PASS', boxes=6, states=3414, checks=CHECKS), sort_keys=True), flush=True)
    modules = {}
    for name, module in sorted(sys.modules.items()):
        modules[name] = dict(origin=getattr(getattr(module, '__spec__', None), 'origin', None),
                             file=getattr(module, '__file__', None))
    with open('/proc/self/maps', encoding='utf8') as source:
        mapped = sorted({line.split()[-1] for line in source if '/' in line and os.path.isfile(line.split()[-1])})
    print(json.dumps(dict(modules=modules, mapped_files=mapped), sort_keys=True), file=sys.stderr)


if __name__ == '__main__':
    main()
