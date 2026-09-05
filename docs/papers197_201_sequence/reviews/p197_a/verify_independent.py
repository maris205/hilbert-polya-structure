#!/usr/bin/env python3
"""P197 Review A. No author imports. Bitplanes/Kahn/level assignments.

Bitplane and local-window helpers extend this reviewer's disclosed pre-Round0
preparation. Full graph peeling, target level-assignment and graph determinant
checks are new Round0 work. SymPy is used only for exact Berkowitz determinant.
"""
from array import array
from collections import Counter, deque
from itertools import product, permutations
from math import gcd
import sympy as sp

ASSERTIONS = 0


def check(test, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not test:
        raise AssertionError((label, ASSERTIONS))


def rot(a, n, k=1):
    k %= n
    return ((a >> k) | (a << (n-k))) & ((1 << n)-1)


def update(lo, hi, n):
    mask = (1 << n)-1
    z = mask ^ (lo | hi)
    ln, hn = rot(lo, n), rot(hi, n)
    return (hi & (mask ^ hn)) | (z & ln), (lo & (mask ^ ln)) | (z & hn)


def word(lo, hi, n):
    return tuple(-1 if lo >> i & 1 else 1 if hi >> i & 1 else 0 for i in range(n))


def local(w):
    w = list(w)
    while len(w) > 1:
        w = [(b > a)-(b < a) for a, b in zip(w, w[1:])]
    return w[0]


def fib(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a+b
    return a


def maxf(n):
    k = 2*(n//2)
    return 3 if n == 1 else fib(k-1)+fib(k+1)


def longest_run(w):
    if len(set(w)) == 1:
        return len(w)
    lengths, run = [], 0
    start = next(i for i in range(len(w)) if w[i] != w[i-1])
    for j in range(len(w)):
        i = (start+j) % len(w)
        if j and w[i] != w[i-1]:
            lengths.append(run)
            run = 0
        run += 1
    return max(lengths+[run])


def level_assignments(y):
    # Collapse equal edges, then explicitly assign successive levels 0,1,2.
    # No transfer matrices and no Fibonacci formula enter this count.
    signs = tuple(s for s in y if s)
    if not signs:
        return 3
    count = 0
    def visit(i, previous, first):
        nonlocal count
        if i == len(signs)-1:
            count += ((first > previous)-(first < previous) == signs[i])
            return
        choices = range(previous+1, 3) if signs[i] > 0 else range(previous)
        for value in choices:
            visit(i+1, value, first)
    for first in range(3):
        visit(0, first, first)
    return count


def gap_formula(y):
    s = tuple(a for a in y if a)
    if not s:
        return 3
    if len(set(s)) == 1:
        return 0
    start = next(i for i in range(len(s)) if s[i] != s[i-1])
    s = s[start:]+s[:start]
    runs = [1]
    for a, b in zip(s, s[1:]):
        if a == b:
            runs[-1] += 1
        else:
            runs.append(1)
    if max(runs) > 2:
        return 0
    marked = [i for i, r in enumerate(runs) if r == 2]
    if not marked:
        return fib(len(s)-1)+fib(len(s)+1)
    answer = 1
    for a, b in zip(marked, marked[1:]+[marked[0]+len(runs)]):
        answer *= fib(b-a)
    return answer


def expected_max(y):
    if not any(y):
        return len(y) <= 3
    s = tuple(a for a in y if a)
    return len(s) == 2*(len(y)//2) and all(s[i] != s[i-1] for i in range(len(s)))


def graph(n):
    size = 3**n
    low, high = array('I', [0])*size, array('I', [0])*size
    for i in range(1, size):
        q, r = divmod(i, 3)
        low[i] = (low[q] << 1) | (r == 1)
        high[i] = (high[q] << 1) | (r == 2)
    ids = {(low[i], high[i]): i for i in range(size)}
    nxt = array('I', (ids[update(low[i], high[i], n)] for i in range(size)))
    indegree = array('I', [0])*size
    for j in nxt:
        indegree[j] += 1
    remaining = array('I', indegree)
    queue = deque(i for i, d in enumerate(remaining) if not d)
    removed = array('I')
    while queue:
        i = queue.popleft()
        removed.append(i)
        j = nxt[i]
        remaining[j] -= 1
        if not remaining[j]:
            queue.append(j)
    depths = array('I', [0])*size
    periods = array('I', [0])*size
    cycle_census = Counter()
    for i in range(size):
        if remaining[i] and not periods[i]:
            cycle, j = [i], nxt[i]
            while j != i:
                cycle.append(j)
                j = nxt[j]
            for j in cycle:
                periods[j] = len(cycle)
            cycle_census[len(cycle)] += 1
    for i in reversed(removed):
        depths[i] = depths[nxt[i]]+1
        periods[i] = periods[nxt[i]]
    return low, high, ids, nxt, indegree, depths, periods, cycle_census


def overlap(width, predicate):
    vertices = list(product((-1, 0, 1), repeat=width))
    ids = {w: i for i, w in enumerate(vertices)}
    edges = [[] for _ in vertices]
    for i, w in enumerate(vertices):
        for a in (-1, 0, 1):
            v = w+(a,)
            if predicate(v):
                edges[i].append(ids[v[1:]])
    return vertices, edges


def walk_traces(edges, upto):
    traces = [0]*(upto+1)
    for start in range(len(edges)):
        active = {start: 1}
        for length in range(1, upto+1):
            following = {}
            for u, count in active.items():
                for v in edges[u]:
                    following[v] = following.get(v, 0)+count
            active = following
            traces[length] += active.get(start, 0)
    return traces


def local_and_polynomial():
    counts = []
    for width, forbidden in ((6, 2), (7, 3)):
        count = 0
        for w in product((-1, 0, 1), repeat=width):
            if any(len(set(w[i:i+forbidden])) == 1 for i in range(width-forbidden+1)):
                continue
            check(local(w) == local(w[2:forbidden+2]), 'all local windows')
            count += 1
        counts.append(count)
    check(counts == [96, 1344], 'local coverage')
    rows = [((-1,-1,0),4,48,1),((-1,-1,1),4,48,1),((-1,0,-1),2,64,-1),
            ((-1,0,0),4,48,-1),((-1,0,1),2,64,0),((-1,1,-1),2,64,-1),
            ((-1,1,0),4,64,-1),((0,-1,0),2,64,1)]
    covered = set()
    for middle, orbit_size, number, value in rows:
        orbit = {middle, middle[::-1], tuple(-a for a in middle), tuple(-a for a in middle[::-1])}
        check(not covered.intersection(orbit), 'disjoint middle triple orbits')
        covered.update(orbit)
        actual = 0
        for outer in product((-1, 0, 1), repeat=4):
            w = outer[:2]+middle+outer[2:]
            if not any(w[i] == w[i+1] == w[i+2] for i in range(5)):
                check(local(w) == value, 'table output')
                actual += 1
        check((len(orbit), actual) == (orbit_size, number), 'table counts')
    check(len(covered) == 24, 'all nonconstant middle triples')
    vertices, edges = overlap(4, lambda w: local(w) == w[2])
    check((len(vertices), sum(map(len, edges))) == (81, 165), 'A0 size')
    matrix = sp.zeros(81)
    for i, row in enumerate(edges):
        for j in row:
            matrix[i,j] += 1
    # Samuelson-Berkowitz coefficients, not trace/Newton recovery.
    coefficients = tuple(map(int, matrix.berkowitz_charpoly().all_coeffs()))
    check(coefficients == (1,-1,-1,-3,-2,2,3,1)+(0,)*74, 'full determinant')
    z = sp.Symbol('z')
    product_poly = sp.Poly(z**74*(z-1)*(z**3-z**2-2*z-1)*(z**3+z**2+2*z+1), z)
    check(tuple(map(int, product_poly.all_coeffs())) == coefficients, 'factorization')
    traces = walk_traces(edges, 12)
    check(traces[1:8] == [1,3,13,27,41,93,225], 'core initial conditions')
    for n in range(8,13):
        check(traces[n] == sum(a*traces[n-j] for j,a in enumerate((1,1,3,2,-2,-3,-1),1)), 'recurrence')
    print('local_windows=96,1344 table_orbits=24 charpoly_method=Berkowitz coefficients=82 status=PASS')
    return traces


def main():
    traces = local_and_polynomial()
    junctions = 0
    for r in range(1,25):
        for length in range(2,25):
            for sign in (-1,1):
                n = r+length
                w = (0,)*r+tuple(sign*(-1)**i for i in range(length))
                lo = sum(1 << i for i,a in enumerate(w) if a < 0)
                hi = sum(1 << i for i,a in enumerate(w) if a > 0)
                a,b = update(lo,hi,n)
                expected = (0,)*(r-1)+tuple(sign*(-1)**i for i in range(length+1))
                check(word(a,b,n) == expected, 'unrotated witness junction')
                for _ in range(3):
                    a,b = update(a,b,n)
                core = (a,b) == (rot(lo,n,2),rot(hi,n,2))
                check(core == (r == 1 and length % 2 == 0), 'all earlier junctions noncore')
                index = r-4 if r >= 4 else 0 if r == 3 else n-2
                if not core:
                    check(word(a,b,n)[index] != word(rot(lo,n,2),rot(hi,n,2),n)[index], 'explicit noncore discrepancy')
                junctions += 1
    print(f'junctions={junctions} zero_runs=1..24 strict_lengths=2..24 status=PASS')
    small = {}
    total = 0
    for n in range(1,13):
        low, high, ids, nxt, indegree, depth, period, cycles = graph(n)
        maximum = maxf(n)
        for i in range(3**n):
            y = word(low[i], high[i], n)
            four = nxt[nxt[nxt[nxt[i]]]]
            core = low[four] == rot(low[i], n, 2) and high[four] == rot(high[i], n, 2)
            check(core == (depth[i] == 0), 'core iff peeled recurrent')
            check((4*n//gcd(n,2)) % period[i] == 0, 'period bound')
            check(indegree[i] == level_assignments(y), 'every target level assignment')
            check(indegree[i] == gap_formula(y), 'every target gap')
            check((indegree[i] == maximum) == expected_max(y), 'all maximizing targets')
            if len(set(y)) > 1:
                check(depth[i] <= longest_run(y), 'run clock')
            if core:
                third = nxt[nxt[nxt[i]]]
                inverse = ids[(rot(low[third], n, -2),rot(high[third], n, -2))]
                check(nxt[inverse] == i and depth[inverse] == 0, 'core two-sided inverse')
            # For small carriers, explicitly check local equations at all depths,
            # not only eventual recurrence or a maximum-tail summary.
            if n <= 6:
                j = i
                for t in range(n+2):
                    d4 = nxt[nxt[nxt[nxt[j]]]]
                    condition = low[d4] == rot(low[j], n, 2) and high[d4] == rot(high[j], n, 2)
                    check(condition == (depth[i] <= t), 'pointwise first-entry equation')
                    j = nxt[j]
        height = 1 if n == 1 else n-1-n % 2
        check(max(depth) == height, 'sharp height')
        check(depth[ids[(0, 1 << (n-1))]] == height, '0...01 sharp witness')
        check(sum(indegree) == 3**n, 'mass identity')
        check(sum(d == 0 for d in depth) == traces[n], 'recurrent trace')
        check(sum(p*c for p,c in cycles.items()) == traces[n], 'cycle mass')
        if n <= 6:
            small[n] = (Counter(depth), cycles)
        if n >= 2:
            for a,b in permutations((-1,0,1),2):
                w = (a,)*(n-1)+(b,)
                lo = sum(1 << j for j,s in enumerate(w) if s < 0)
                hi = sum(1 << j for j,s in enumerate(w) if s > 0)
                expected = int(abs(a-b) == 1) if n <= 3 else height
                check(depth[ids[(lo,hi)]] == expected, 'all one-exception small boundaries')
        print(f'n={n} sources={3**n} targets={3**n} image={sum(d>0 for d in indegree)} recurrent={traces[n]} max_tail={height} max_fibre={max(indegree)} maximizers={sum(d==maximum for d in indegree)} cycles={sorted(cycles.items())}')
        total += 3**n
    for t in range(4):
        _, edges = overlap(t+4, lambda w: local(w) == local(w[2:t+3]))
        cdf = walk_traces(edges, 6)
        for n in range(1,7):
            check(cdf[n] == sum(c for d,c in small[n][0].items() if d <= t), 'At trace repeated windows')
        print(f'depth_trace t={t} n=1..6 status=PASS')
    fixed = {}
    for p in range(1,7):
        _, edges = overlap(p, lambda w: local(w) == w[0])
        fixed[p] = walk_traces(edges, 6)
        for n in range(1,7):
            expected = sum(q*c for q,c in small[n][1].items() if p % q == 0)
            check(fixed[p][n] == expected, 'Cp trace repeated windows')
            mobius_sum = sum(int(sp.mobius(p//d))*fixed[d][n] for d in range(1,p+1) if p % d == 0)
            check(mobius_sum == p*small[n][1][p], 'Mobius exact least cycles')
        print(f'period_trace p={p} n=1..6 status=PASS')
    check(gap_formula((1,1,-1,-1)) == 1, 'non-strict Fibonacci merge control')
    print(f'full_sources={total}')
    print(f'full_targets={total}')
    print(f'assertions={ASSERTIONS}')
    print('status=PASS')
    print('findings=critical:0,major:0,minor:0')
    print('external_status=OWNER_AMBER/HOLD_EXTERNAL')


if __name__ == '__main__':
    main()
