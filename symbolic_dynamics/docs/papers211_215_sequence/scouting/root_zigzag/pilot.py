"""One bounded, exact root ZGR scouting pilot; no all-size proof claim."""
import collections
import hashlib
import itertools
import json
import os
from pathlib import Path
import sys


def literal(x):
    out = []
    a = 0
    while a < len(x):
        b = min(a + 2, len(x))
        while b < len(x) and (x[b-2] < x[b-1]) != (x[b-1] < x[b]):
            b += 1
        out.extend(reversed(x[a:b]))
        a = b
    return tuple(out)


def longest_prefix(x):
    if not x:
        return ()
    best = 1
    for b in range(2, len(x) + 1):
        good = all((x[k-1] < x[k]) != (x[k] < x[k+1])
                   for k in range(1, b-1))
        if good:
            best = b
    return x[:best][::-1] + longest_prefix(x[best:])


def emit(tag, data):
    print(tag + ' ' + json.dumps(data, sort_keys=True, separators=(',', ':')),
          flush=True)


checks = 0
total = 0
for n in range(9):
    states = list(itertools.permutations(range(1, n+1)))
    graph = {x: literal(x) for x in states}
    indegree = collections.Counter(graph.values())
    for x, y in graph.items():
        assert y == longest_prefix(x), (x, y)
        assert sorted(y) == list(range(1, n+1))
        checks += 2
    atlas = {}
    cycles = []
    for start in states:
        if start in atlas:
            continue
        path = []
        seen = {}
        x = start
        while x not in atlas and x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = graph[x]
        if x in seen:
            cut = seen[x]
            cycle = path[cut:]
            cycles.append(cycle)
            for c in cycle:
                atlas[c] = (0, len(cycle))
            tail = path[:cut]
        else:
            tail = path
        for x in reversed(tail):
            d, p = atlas[graph[x]]
            atlas[x] = (d + 1, p)
    for x, (d, p) in atlas.items():
        nd, np = atlas[graph[x]]
        assert np == p and nd == max(0, d-1)
        checks += 1
    height = max(d for d, p in atlas.values())
    longest = max(cycles, key=len)
    deepest = next(x for x in states if atlas[x][0] == height)
    max_fibre = max(indegree.values())
    max_target = next(x for x in states if indegree[x] == max_fibre)
    emit('BOX', {'n': n, 'states': len(states), 'height': height,
        'cycle_counts': sorted(collections.Counter(map(len, cycles)).items()),
        'depth_counts': sorted(collections.Counter(d for d,p in atlas.values()).items()),
        'image': len(indegree), 'max_fibre': max_fibre,
        'max_target': max_target, 'deepest': deepest, 'longest_cycle': longest})
    total += len(states)
emit('TOTAL', {'states': total, 'assertions': checks})
paths = {str(Path(__file__).resolve()), str(Path(sys.executable).resolve())}
for module in list(sys.modules.values()):
    name = getattr(module, '__file__', None)
    if name and os.path.isfile(name):
        paths.add(str(Path(name).resolve()))
for line in Path('/proc/self/maps').read_text().splitlines():
    parts = line.split(maxsplit=5)
    if len(parts) == 6 and parts[-1].startswith('/') and os.path.isfile(parts[-1]):
        paths.add(str(Path(parts[-1]).resolve()))
for name in sorted(paths):
    content = Path(name).read_bytes()
    emit('AFTER_PIN', {'path': name, 'bytes': len(content),
                      'sha256': hashlib.sha256(content).hexdigest()})
emit('RUNTIME', {'python': sys.version, 'argv': sys.argv, 'flags': str(sys.flags),
                 'environment': dict(os.environ), 'cwd': os.getcwd()})
