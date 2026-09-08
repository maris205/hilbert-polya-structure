"""Single bounded WFS census. No historical mathematical imports."""
import collections
import hashlib
import itertools
import json
import os
import sys


def literal(f, p):
    out = [0] * p
    for x, y in enumerate(f):
        out[y] = (out[y] + x) % p
    return tuple(out)


def emit(obj):
    print(json.dumps(obj, sort_keys=True, separators=(",", ":")))


for prime in (3, 5):
    states = list(itertools.product(range(prime), repeat=prime))
    index = {f: i for i, f in enumerate(states)}
    succ = [index[literal(f, prime)] for f in states]
    pre = [[] for _ in states]
    for i, j in enumerate(succ):
        pre[j].append(i)
    indeg = [len(v) for v in pre]
    rem = indeg[:]
    queue = collections.deque(i for i, d in enumerate(rem) if not d)
    deleted = []
    while queue:
        i = queue.popleft()
        deleted.append(i)
        j = succ[i]
        rem[j] -= 1
        if not rem[j]:
            queue.append(j)
    depth = [None] * len(states)
    period = [None] * len(states)
    cycles = []
    for i in range(len(states)):
        if rem[i] and depth[i] is None:
            cyc, j = [], i
            while depth[j] is None:
                depth[j] = 0
                cyc.append(j)
                j = succ[j]
            assert j == i
            for j in cyc:
                period[j] = len(cyc)
            cycles.append(cyc)
    for i in reversed(deleted):
        depth[i] = depth[succ[i]] + 1
        period[i] = period[succ[i]]
    assert sum(indeg) == prime ** prime
    assert all(sum(states[succ[i]]) % prime == 0 for i in range(len(states)))
    for f in itertools.permutations(range(prime)):
        inv = tuple(f.index(y) for y in range(prime))
        assert literal(f, prime) == inv
    for a in range(1, prime):
        for b in range(prime):
            f = tuple((a * x + b) % prime for x in range(prime))
            assert literal(literal(f, prime), prime) == f
    for c in range(prime):
        assert literal((c,) * prime, prime) == (0,) * prime
    for i, f in enumerate(states):
        emit({"kind": "state", "p": prime, "id": i, "f": f,
              "successor": succ[i], "depth": depth[i],
              "period": period[i], "predecessors": pre[i]})
    maxf = max(indeg)
    h = max(depth)
    emit({"kind": "summary", "p": prime, "states": len(states),
          "image": sum(d > 0 for d in indeg),
          "core": sum(d == 0 for d in depth), "height": h,
          "depth_histogram": sorted(collections.Counter(depth).items()),
          "cycle_histogram": sorted(collections.Counter(map(len, cycles)).items()),
          "fibre_histogram": sorted(collections.Counter(indeg).items()),
          "max_fibre": maxf,
          "max_fibre_targets": [i for i, d in enumerate(indeg) if d == maxf],
          "deepest_states": [i for i, d in enumerate(depth) if d == h],
          "cycles": cycles})

module_pins = []
for name, module in sorted(sys.modules.items()):
    file = getattr(module, "__file__", None)
    if file and os.path.isfile(file):
        actual = os.path.realpath(file)
        with open(actual, "rb") as stream:
            raw = stream.read()
        module_pins.append({"module": name, "path": actual, "bytes": len(raw),
                            "sha256": hashlib.sha256(raw).hexdigest()})
emit({"kind": "child_runtime", "python_version": sys.version,
      "executable": os.path.realpath(sys.executable), "sys_path": sys.path,
      "flags": repr(sys.flags), "loaded_module_pins": module_pins,
      "limit": "Loaded-module pins do not inventory the dynamic loader and its complete configuration."})
