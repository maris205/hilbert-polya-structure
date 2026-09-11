#!/usr/bin/env python3
"""P198 Review A: vertex-partner carrier and direct orbit paths.

Written by root, not the P198 paper author. No author/scout imports.
Inverse source SETS are reconstructed from endpoint pairs, not counted
only by the triangular expression. Exhaustive odd n<=23.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb

ASSERTIONS = 0


def check(ok, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not ok:
        raise AssertionError(label)


@lru_cache(None)
def path_matchings(vertices):
    if not vertices:
        return ((),)
    out = list(path_matchings(vertices[1:]))
    if len(vertices) > 1:
        pair = (vertices[0], vertices[1])
        out += [(pair,)+rest for rest in path_matchings(vertices[2:])]
    return tuple(out)


def partner_vector(n, edges):
    p = [-1]*n
    for a,b in edges:
        assert p[a] == p[b] == -1
        p[a],p[b] = b,a
    return tuple(p)


def carrier(n):
    states = [partner_vector(n,e) for e in path_matchings(tuple(range(n)))]
    states += [partner_vector(n,((0,n-1),)+e)
               for e in path_matchings(tuple(range(1,n-1)))]
    return states


def edges(p):
    return frozenset((i,j) for i,j in enumerate(p) if i < j)


def flip_arc(p, a, distance):
    n = len(p)
    chosen = set(edges(p))
    for h in range(distance):
        i,j = (a+h)%n,(a+h+1)%n
        pair = tuple(sorted((i,j)))
        if pair in chosen:
            chosen.remove(pair)
        else:
            chosen.add(pair)
    return partner_vector(n,chosen)


def step(p):
    monomers = [i for i,j in enumerate(p) if j < 0]
    a = monomers[0]
    distance = 2 if len(monomers) == 1 else monomers[1]-a
    return flip_arc(p,a,distance)


def inverse(p):
    n = len(p)
    holes = [i for i,j in enumerate(p) if j < 0]
    u = holes[0]
    sources = set()
    # All candidate endpoint pairs before u with target dimers at both ends.
    for a in range(u):
        for b in range(a+1,u):
            if (b-a)%2 == 0:
                continue
            if all(p[a+h] == a+h+1 and p[a+h+1] == a+h
                   for h in range(0,b-a,2)):
                q = flip_arc(p,a,b-a)
                check(q not in sources, 'distinct endpoint inverse sources')
                sources.add(q)
    if len(holes) == 1:
        a = (u-2)%n
        q = flip_arc(p,a,2)
        check(q not in sources, 'core predecessor disjoint from transient')
        sources.add(q)
    return sources


def graph(nxt):
    depth, period = {}, {}
    for start in nxt:
        if start in depth:
            continue
        path, pos, v = [], {}, start
        while v not in depth and v not in pos:
            pos[v] = len(path)
            path.append(v)
            v = nxt[v]
        if v not in depth:
            t = pos[v]
            length = len(path)-t
            for a in path[t:]:
                depth[a],period[a] = 0,length
            path = path[:t]
        for a in reversed(path):
            depth[a],period[a] = depth[nxt[a]]+1,period[nxt[a]]
    return depth,period


def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return a


def main():
    total = 0
    for n in range(3,24,2):
        m = n//2
        states = carrier(n)
        universe = set(states)
        check(len(states) == len(universe), 'carrier unique')
        check(len(states) == fib(n-1)+fib(n+1), 'complete carrier census')
        nxt, pre = {}, defaultdict(set)
        for p in states:
            q = step(p)
            check(q in universe, 'closure')
            nxt[p] = q
            pre[q].add(p)
        depth,period = graph(nxt)
        histogram = Counter()
        maximal = []
        for p in states:
            holes = [i for i,j in enumerate(p) if j < 0]
            size = (n-len(holes))//2
            histogram[depth[p]] += 1
            check(depth[p] == m-size, 'exact deficiency tail')
            check(period[p] == n, 'single allowed period')
            check((depth[p] == 0) == (len(holes) == 1), 'complete recurrent iff')
            if len(holes) == 1:
                check(nxt[p].index(-1) == (holes[0]+2)%n, 'clockwise core orientation')
            sources = inverse(p)
            check(sources == pre[p], 'every complete inverse source set')
            r = holes[0]//2
            check(len(pre[p]) == r*(r+1)//2+int(len(holes)==1), 'all triangular counts')
            check(bool(pre[p]) == (len(holes)==1 or holes[0]>=2), 'all image iff')
            if len(pre[p]) == 1+m*(m+1)//2:
                maximal.append(p)
        for r in range(m+1):
            expected = n*comb(n-r,r)//(n-r)
            check(histogram[m-r] == expected, 'every depth coefficient')
        check(sum(depth[p] == 0 for p in states) == n, 'one full recurrent cycle')
        check(max(depth.values()) == m, 'sharp global clock')
        check([p for p in states if depth[p] == m] == [(-1,)*n], 'unique deepest empty')
        check(max(map(len,pre.values())) == 1+m*(m+1)//2, 'maximum fibre')
        check(len(maximal) == 1 and maximal[0].index(-1) == n-1, 'unique maximum equality')
        image = sum(bool(pre[p]) for p in states)
        check(image == fib(n-1)+fib(n-3)+2, 'image census incl n3')
        check(sum(map(len,pre.values())) == len(states), 'full target mass')
        total += len(states)
        print(f'n={n} sources={len(states)} targets={len(states)} image={image} recurrent={n} tail={m} max_fibre={1+m*(m+1)//2}')
        path_matchings.cache_clear()
    print(f'full_sources={total}')
    print(f'full_targets={total}')
    print(f'assertions={ASSERTIONS}')
    print('findings=critical:0,major:0,minor:0')
    print('status=PASS')
    print('external_status=OWNER_AMBER/HOLD_EXTERNAL')


if __name__ == '__main__':
    main()
