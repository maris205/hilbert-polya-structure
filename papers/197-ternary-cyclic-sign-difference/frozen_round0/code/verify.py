#!/usr/bin/env python3
"""P197 author verifier. Exact finite checks; no imported scouting modules.

Full cyclic carriers and every target n=1..12. Tuple literals, direct orbit
paths, comparison matrices, and a sparse Newton-identity certificate.
"""
from collections import Counter
from itertools import product
from math import gcd

ALPHABET = (-1, 0, 1)
ASSERTIONS = 0


def check(value, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not value:
        raise AssertionError(label)


def difference(x, cyclic=True):
    return tuple((x[(i+1) % len(x)] > x[i]) -
                 (x[(i+1) % len(x)] < x[i])
                 for i in range(len(x) if cyclic else len(x)-1))


def delta(w):
    while len(w) > 1:
        w = difference(w, False)
    return w[0]


def encode(x):
    out = 0
    for a in x:
        out = 3*out + a+1
    return out


def fib(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a+b
    return a


def lucas(k):
    return 2 if k == 0 else fib(k-1)+fib(k+1)


def cyclic_runs(w):
    if len(set(w)) == 1:
        return [len(w)]
    start = next(i for i in range(len(w)) if w[i] != w[i-1])
    runs = []
    for j in range(len(w)):
        i = (start+j) % len(w)
        if j == 0 or w[i] != w[i-1]:
            runs.append(1)
        else:
            runs[-1] += 1
    return runs


def gap_fibre(y):
    w = tuple(a for a in y if a)
    if not w:
        return 3
    if len(set(w)) == 1:
        return 0
    runs = cyclic_runs(w)
    if max(runs) > 2:
        return 0
    marked = [j for j, r in enumerate(runs) if r == 2]
    if not marked:
        return lucas(len(w))
    out = 1
    for a, b in zip(marked, marked[1:]+[marked[0]+len(runs)]):
        out *= fib(b-a)
    return out


def trace_fibre(y):
    acc = [[int(i == j) for j in range(3)] for i in range(3)]
    for sign in y:
        acc = [[sum(acc[a][b] for b in range(3)
                    if (c > b)-(c < b) == sign)
                for c in range(3)] for a in range(3)]
    return sum(acc[a][a] for a in range(3))


def graph_depth_period(nxt):
    depth = [-1]*len(nxt)
    period = [0]*len(nxt)
    for start in range(len(nxt)):
        if depth[start] >= 0:
            continue
        path, pos, v = [], {}, start
        while depth[v] < 0 and v not in pos:
            pos[v] = len(path)
            path.append(v)
            v = nxt[v]
        if depth[v] < 0:
            entry = pos[v]
            length = len(path)-entry
            for u in path[entry:]:
                depth[u], period[u] = 0, length
            path = path[:entry]
        for u in reversed(path):
            depth[u], period[u] = depth[nxt[u]]+1, period[nxt[u]]
    return depth, period


def certificates():
    local6 = local7 = 0
    for w in product(ALPHABET, repeat=6):
        if all(w[i] != w[i+1] for i in range(5)):
            check(delta(w) == delta(w[2:4]), 'length-six identity')
            local6 += 1
    for w in product(ALPHABET, repeat=7):
        if all(not w[i] == w[i+1] == w[i+2] for i in range(5)):
            check(delta(w) == delta(w[2:5]), 'length-seven identity')
            local7 += 1
    check((local6, local7) == (96, 1344), 'complete local coverage')
    middle = [((-1,-1,0),4,48,1),((-1,-1,1),4,48,1),
              ((-1,0,-1),2,64,-1),((-1,0,0),4,48,-1),
              ((-1,0,1),2,64,0),((-1,1,-1),2,64,-1),
              ((-1,1,0),4,64,-1),((0,-1,0),2,64,1)]
    for centre, orbit, size, value in middle:
        found = 0
        for outer in product(ALPHABET, repeat=4):
            w = outer[:2]+centre+outer[2:]
            if all(not w[i] == w[i+1] == w[i+2] for i in range(5)):
                found += 1
                check(delta(w) == value, 'representative local output')
        orbit_set = {centre, centre[::-1], tuple(-a for a in centre),
                     tuple(-a for a in centre[::-1])}
        check((found, len(orbit_set)) == (size, orbit), 'table row counts')
    print(f'local_certificate words6={local6} words7={local7} status=PASS')

    # Compute every characteristic coefficient of the explicitly defined A0.
    verts = list(product(ALPHABET, repeat=4))
    edges = [[] for _ in verts]
    for w in product(ALPHABET, repeat=5):
        if delta(w) == w[2]:
            edges[encode(w[:4])].append(encode(w[1:]))
    check(sum(map(len, edges)) == 165, 'A0 exact edge count')
    size = len(verts)
    power = [[int(i == j) for j in range(size)] for i in range(size)]
    traces = [size]
    coefficients = [1]
    for k in range(1, size+1):
        new = [[0]*size for _ in range(size)]
        for i, row in enumerate(power):
            for j, value in enumerate(row):
                if value:
                    for dest in edges[j]:
                        new[i][dest] += value
        power = new
        traces.append(sum(power[i][i] for i in range(size)))
        value = -sum(coefficients[k-i]*traces[i] for i in range(1,k+1))
        check(value % k == 0, 'Newton exact integer division')
        coefficients.append(value//k)
    expected = [1,-1,-1,-3,-2,2,3,1]+[0]*74
    check(coefficients == expected, 'full degree81 characteristic polynomial')
    check(traces[1:8] == [1,3,13,27,41,93,225], 'initial recurrent traces')
    print('A0 vertices=81 edges=165 charpoly=z^74*(z-1)*(z^3-z^2-2z-1)*(z^3+z^2+2z+1) status=PASS')
    return traces


def expected_maximizers(y):
    n = len(y)
    if not any(y):
        return n <= 3
    w = [a for a in y if a]
    if len(w) != 2*(n//2):
        return False
    return all(w[i] != w[i-1] for i in range(len(w)))


def main():
    traces = certificates()
    total = 0
    for n in range(1,13):
        states = list(product(ALPHABET, repeat=n))
        nxt = [encode(difference(x)) for x in states]
        fibres = Counter(nxt)
        depth, period = graph_depth_period(nxt)
        total += len(states)
        for i, x in enumerate(states):
            four = nxt[nxt[nxt[nxt[i]]]]
            core = four == encode(x[2:]+x[:2]) if n >= 2 else four == i
            check(core == (depth[i] == 0), 'core iff recurrence')
            check((4*n//gcd(n,2)) % period[i] == 0, 'period divisibility')
            check(gap_fibre(x) == fibres[i], 'every target exact gap fibre')
            if n <= 8:
                check(trace_fibre(x) == fibres[i], 'every target comparison trace')
            if len(set(x)) > 1:
                check(depth[i] <= max(cyclic_runs(x)), 'pointwise run tail')
            check((fibres[i] == max_fibre(n)) == expected_maximizers(x),
                  'all maximum equality targets')
        height = 1 if n == 1 else n-1 if n % 2 == 0 else n-2
        check(max(depth) == height, 'parity sharp maximum')
        check(sum(d == 0 for d in depth) == traces[n], 'core trace census')
        check(sum(fibres.values()) == 3**n, 'full target mass')
        witness = encode((0,)*(n-1)+(1,))
        check(depth[witness] == height, 'explicit sharp witness including n1')
        print(f'n={n} states={len(states)} image={len(fibres)} recurrent={sum(d==0 for d in depth)} tail={height} max_fibre={max(fibres.values())} periods={sorted(set(period))}')
    for r in range(0,12):
        for length in range(2,15):
            for s in (-1,1):
                z = (0,)*r+tuple(s*(-1)**i for i in range(length))
                if r:
                    check(difference(z) == (0,)*(r-1)+tuple(s*(-1)**i for i in range(length+1)), 'unrotated junction identity')
                value = z
                for _ in range(4):
                    value = difference(value)
                core = value == z[2:]+z[:2]
                check(core == (r == 0 or (r == 1 and length % 2 == 0)), 'qualified witness core iff')
    print(f'full_sources={total} full_targets={total} assertions={ASSERTIONS}')
    print('status=PASS')
    print('external_status=OWNER_AMBER/HOLD_EXTERNAL')


def max_fibre(n):
    return 3 if n == 1 else lucas(2*(n//2))


if __name__ == '__main__':
    main()
