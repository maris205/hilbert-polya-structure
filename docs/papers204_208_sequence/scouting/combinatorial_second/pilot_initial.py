#!/usr/bin/env python3
"""Second combinatorial lane: cheap exact initial candidates, no theorem oracle."""
from collections import Counter, deque
from functools import lru_cache
from itertools import product
import json


def analyze(states, update):
    ids = {w:i for i,w in enumerate(states)}
    assert len(ids) == len(states)
    arrows = [ids[update(w)] for w in states]
    fibres = Counter(arrows)
    indeg = [fibres[i] for i in range(len(states))]
    queue = deque(i for i,d in enumerate(indeg) if d == 0)
    peeled = []
    while queue:
        i = queue.popleft()
        peeled.append(i)
        j = arrows[i]
        indeg[j] -= 1
        if indeg[j] == 0:
            queue.append(j)
    depth = [0]*len(states)
    for i in reversed(peeled):
        depth[i] = depth[arrows[i]]+1
    seen = set()
    cycles = Counter()
    for i,d in enumerate(indeg):
        if not d or i in seen:
            continue
        j, length = i, 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = arrows[j]
        cycles[length] += 1
    assert sum(fibres.values()) == len(states)
    assert sum(k*v for k,v in cycles.items()) == len(seen)
    return {"states":len(states),"image":len(fibres),"recurrent":len(seen),
        "height":max(depth),"cycles":dict(sorted(cycles.items())),
        "max_fibre":max(fibres.values()),
        "height_witness":states[depth.index(max(depth))]}


def predecessor_reverse(f):
    pred = [[] for _ in f]
    for i,j in enumerate(f):
        pred[j].append(i)
    return tuple(min(p) if p else f[i] for i,p in enumerate(pred))


def zero_pair_reaction(w):
    n = len(w)
    v = list(w)
    if n >= 3:
        for i in range(n):
            if (w[i],w[(i+1)%n],w[(i+2)%n]) == (0,0,1):
                v[i],v[(i+1)%n],v[(i+2)%n] = 1,1,0
    return tuple(v)


@lru_cache(None)
def partitions(n, largest=None):
    if n == 0:
        return ((),)
    if largest is None or largest > n:
        largest = n
    return tuple((a,)+tail for a in range(largest,0,-1)
                 for tail in partitions(n-a,a))


def balanced_split_transpose(w):
    if not w:
        return ()
    pieces = [p for a in w for p in (a//2,(a+1)//2) if p]
    return tuple(sum(p >= h for p in pieces) for h in range(1,max(pieces)+1))


def ballistic_annihilation(w):
    n = len(w)
    if not n:
        return w
    killed = set()
    for i in range(n):
        if w[i] == 1 and w[(i+1)%n] == -1:
            killed.update((i,(i+1)%n))
    landing = [0]*n
    for i,a in enumerate(w):
        if a and i not in killed:
            landing[(i+a)%n] += a
    assert all(a in (-1,0,1) for a in landing)
    return tuple(landing)


def main():
    specs = (
        ("PR", range(1,7), lambda n:list(product(range(n),repeat=n)), predecessor_reverse),
        ("ZR", range(1,15), lambda n:list(product((0,1),repeat=n)), zero_pair_reaction),
        ("BS", range(1,31), lambda n:list(partitions(n)), balanced_split_transpose),
        ("BA", range(1,10), lambda n:list(product((-1,0,1),repeat=n)), ballistic_annihilation),
    )
    for label, sizes, carrier, update in specs:
        for n in sizes:
            print(json.dumps({"candidate":label,"n":n,**analyze(carrier(n),update)},
                sort_keys=True,separators=(",",":")),flush=True)


if __name__ == "__main__":
    main()
