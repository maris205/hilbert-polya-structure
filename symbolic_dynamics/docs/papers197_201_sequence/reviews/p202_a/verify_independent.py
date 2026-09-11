#!/usr/bin/env python3
"""P202 A: new integer/peeling/event-time controls, no author imports."""
from collections import Counter, deque
from functools import lru_cache
from heapq import heappop, heappush
from itertools import permutations, product
from math import gcd
import json

CHECKS = 0
TABLE = (1, 1, 1, 0, 2, 2, 0, 0, 0)
A_EDGES = {(a, b) for a in range(3) for b in range(3) if (b-a) % 3 in (0, 1)}
B_EDGES = {(0, 1), (1, 0), (1, 2), (2, 0)}


def ck(condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(CHECKS)


def encode(x):
    a = 0
    for digit in x:
        a = 3*a + digit
    return a


def step(x):
    return tuple(TABLE[3*a+b] for a, b in zip(x, x[1:]+x[:1]))


def edges(x):
    return tuple(zip(x, x[1:]+x[:1]))


def languages(x):
    ee = edges(x)
    return all(e in A_EDGES for e in ee), all(e in B_EDGES for e in ee)


def graph_from_arrows(f):
    """No orbit-path cycle discovery: Kahn + undirected cycle union-find."""
    size = len(f)
    incoming = [[] for _ in f]
    for x, y in enumerate(f):
        incoming[y].append(x)
    indegree = [len(a) for a in incoming]
    queue = deque(x for x, d in enumerate(indegree) if d == 0)
    peeled = []
    while queue:
        x = queue.popleft()
        peeled.append(x)
        y = f[x]
        indegree[y] -= 1
        if indegree[y] == 0:
            queue.append(y)
    parent = list(range(size))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    core = [x for x, d in enumerate(indegree) if d]
    for x in core:
        a, b = find(x), find(f[x])
        if a != b:
            parent[a] = b
    component_size = Counter(find(x) for x in core)
    depth, period = [0]*size, [0]*size
    for x in core:
        period[x] = component_size[find(x)]
    for x in reversed(peeled):
        depth[x] = depth[f[x]]+1
        period[x] = period[f[x]]
    return incoming, depth, period, Counter(component_size.values())


def runs(x):
    """Cyclic run coordinates, fixed lexicographic block origin for comparison."""
    n = len(x)
    start = next(i for i in range(n) if x[i] == 0 and x[i-1] != 0)
    w = x[start:] + x[:start]
    blocks, i = [], 0
    while i < n:
        cc = aa = bb = 0
        while i < n and w[i] == 0:
            cc += 1; i += 1
        while i < n and w[i] == 1:
            aa += 1; i += 1
        while i < n and w[i] == 2:
            bb += 1; i += 1
        ck(cc > 0 and aa+bb > 0)
        blocks.append((cc, aa, bb))
    return min(tuple(blocks[j:]+blocks[:j]) for j in range(len(blocks)))


@lru_cache(maxsize=None)
def event_clearance(z):
    """Arrival-time batches at slots; no time-step or labelled-particle walk."""
    k = len(z)//3
    occupied = {i for i in range(k) if z[3*i+2]}
    mobile = sum(z)-len(occupied)
    if mobile == 0 or len(occupied) == k:
        return 0
    events = []
    for i in range(k):
        if z[3*i]: heappush(events, (2, i, z[3*i]))
        if z[3*i+1]: heappush(events, (1, i, z[3*i+1]))
        if z[3*i+2] > 1: heappush(events, (3, (i+1)%k, z[3*i+2]-1))
    while events:
        t, i, mass = heappop(events)
        while events and events[0][:2] == (t, i):
            mass += heappop(events)[2]
        if i not in occupied:
            occupied.add(i)
            mobile -= 1
            mass -= 1
        if not mobile or len(occupied) == k:
            return t
        if mass:
            heappush(events, (t+3, (i+1)%k, mass))
    raise AssertionError("Mobile particles without an arrival event")


def bins_step(z):
    k = len(z)//3
    out = [0]*len(z)
    for j in range(k):
        out[3*j] = max(z[3*((j-1)%k)+2]-1, 0)
        out[3*j+1] = z[3*j]
        out[3*j+2] = z[3*j+1] + min(z[3*j+2], 1)
    return tuple(out)


def clear(z):
    occupied = sum(z[i] > 0 for i in range(2, len(z), 3))
    return occupied == len(z)//3 or occupied == sum(z)


def composition(total, length):
    if length == 1:
        yield (total,)
    else:
        for a in range(total+1):
            for tail in composition(total-a, length-1):
                yield (a,)+tail


def parking_boxes():
    count = 0
    for k in range(1, 5):
        for m in range(7):
            best = 0
            for z in composition(m, 3*k):
                count += 1
                q, t = z, 0
                while not clear(q):
                    q = bins_step(q); t += 1
                    ck(t <= 3*max(k, m)+1)
                ck(event_clearance(z) == t)
                best = max(best, t)
            ck(best == (0 if m == 0 else 3*min(k, m)-1))
    print("parking_configurations", count)


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def trace_powers(matrix, cutoff):
    a = [[int(i == j) for j in range(3)] for i in range(3)]
    out = []
    for n in range(cutoff+1):
        out.append(sum(a[i][i] for i in range(3)))
        a = matmul(a, matrix)
    return out


def source_domains(y):
    """One-site admissible domains, with exact right-neighbor consistency."""
    ee = edges(y)
    if (2, 1) in ee:
        return set()
    domains = []
    for a, b in ee:
        domains.append((0,) if a == 1 else (1,) if a == 2 else (1, 2) if b == 1 else (2,))
    return {encode(x) for x in product(*domains)}


def weighted_walk_hist(n):
    ans = Counter()
    for first in range(3):
        paths = {(first, 0): 1}
        for _ in range(n):
            nxt = Counter()
            for (last, weight), count in paths.items():
                for b in range(3):
                    if (last, b) != (2, 1):
                        nxt[b, weight+int((last, b) == (0, 1))] += count
            paths = nxt
        for (last, weight), count in paths.items():
            if last == first:
                ans[weight] += count
    return ans


def all_word_boxes():
    aa = trace_powers([[int((i,j) in A_EDGES) for j in range(3)] for i in range(3)], 180)
    bb = trace_powers([[int((i,j) in B_EDGES) for j in range(3)] for i in range(3)], 180)
    lucas = [2, 1]
    for _ in range(360): lucas.append(lucas[-1]+lucas[-2])
    eps = (2, 1, -1, -2, -1, 1)
    for n in range(1, 181):
        ck(aa[n] == 2**n+eps[n%6])
        if n >= 3: ck(bb[n] == bb[n-2]+bb[n-3])
    total = 0
    for n in range(1, 13):
        states = list(product(range(3), repeat=n))
        total += len(states)
        f = [encode(step(x)) for x in states]
        incoming, depth, period, cycles = graph_from_arrows(f)
        weight_hist = Counter()
        max_targets = set()
        for j, x in enumerate(states):
            literal = tuple((a+1)%3 if a <= b else 0 for a,b in edges(x))
            ck(encode(literal) == f[j])
            a, b = languages(x)
            ck((depth[j] == 0) == (a or b))
            if a:
                ck(step(x) == tuple((u+1)%3 for u in x) and period[j] == 3)
            if b:
                d = next(d for d in range(1, n+1) if n%d == 0 and x == x[:d]*(n//d))
                ck(step(x) == x[1:]+x[:1] and period[j] == d)
            ck(set(incoming[j]) == source_domains(x))
            e = edges(x).count((0,1))
            ck(len(incoming[j]) == (0 if (2,1) in edges(x) else 2**e))
            if incoming[j]: weight_hist[e] += 1
            if len(incoming[j]) == 2**(n//2): max_targets.add(j)
            zword = states[f[f[j]]]
            if len(set(zword)) > 1:
                rr = runs(zword)
                ck(all(c >= 1 and a >= 1 and b >= 0 for c,a,b in rr))
                z = tuple(v for c,a,b in rr for v in (c-1,a-1,b))
                ck(sum(z) == n-2*len(rr))
                newruns = runs(step(zword))
                transformed = [(max(rr[i-1][2],1),c,a-int(b==0)) for i,(c,a,b) in enumerate(rr)]
                expected_runs = min(tuple(transformed[q:]+transformed[:q]) for q in range(len(rr)))
                ck(newruns == expected_runs)
                ck(depth[f[f[j]]] == event_clearance(z))
                ck(depth[j] == (0 if a or b else 1 if depth[f[j]] == 0 else 2+event_clearance(z)))
        ck(sum(weight_hist.values()) == lucas[2*n])
        ck(weight_hist == weighted_walk_hist(n))
        ck(sum(count*2**e for e,count in weight_hist.items()) == 3**n)
        predicted = set()
        if n == 1:
            predicted = set(range(3))
        elif n%2 == 0:
            predicted = {encode(tuple([0,1]*(n//2))), encode(tuple([1,0]*(n//2)))}
        else:
            m = n//2
            for pref in ((0,0,1),(0,1,1),(0,1,2)):
                word = pref+(0,1)*(m-1)
                predicted.update(encode(word[q:]+word[:q]) for q in range(n))
        ck(max_targets == predicted)
        ck(sum(d == 0 for d in depth) == aa[n]+bb[n]-3*int(n%3 == 0))
        for t in range(1, 3*n+7):
            fixed = sum(length*count for length,count in cycles.items() if t%length == 0)
            d = gcd(n,t)
            ck(fixed == int(t%3 == 0)*aa[n]+bb[d]-3*int(d%3 == 0))
        ck(max(depth) == (0 if n == 1 else 2 if n == 2 else 3*(n//3)+1))
        print("word_box", json.dumps({"n":n,"states":len(states),"image":sum(bool(a) for a in incoming),
              "depth":sorted(Counter(depth).items()),"cycles":sorted(cycles.items()),
              "max_fibre":2**(n//2),"max_targets":len(max_targets)}, sort_keys=True,separators=(",",":")))
    print("full_word_states", total)


def sharp_family():
    for n in range(3, 181):
        k, r = divmod(n, 3)
        x = (1,)*(k+r+1)+(2,)+(1,2)*(k-1)
        y = (2,)*(k+r+1)+(0,)+(2,0)*(k-1)
        z = (0,)*(k+r+1)+(1,)+(0,1)*(k-1)
        ck(step(x) == y and step(y) == z)
        t, w = 0, x
        while not any(languages(w)):
            w = step(w); t += 1
            ck(t <= 3*k+1)
        ck(t == 3*k+1)
    print("sharp_witness_lengths", "3..180")


def bounded_owner_controls():
    """Named primary one-sided comparators, not arbitrary block/power codes."""
    comparators = {
        "FCA": lambda a,b: a if (a,b) == (2,1) else (a+1)%3,
        "CCA": lambda a,b: (a+1)%3 if b == (a+1)%3 else a,
        "GHM": lambda a,b: int(b == 1) if a == 0 else (a+1)%3,
        "P196_q3": lambda a,b: 2 if a <= b else b,
        "P164_q3": lambda a,b: int(a == b),
    }
    counts = {}
    for name, rule in comparators.items():
        matches = 0
        for perm in permutations(range(3)):
            for exchange in (False, True):
                match = True
                for a,b in product(range(3), repeat=2):
                    aa,bb = (b,a) if exchange else (a,b)
                    match &= perm[TABLE[3*a+b]] == rule(perm[aa],perm[bb])
                matches += match
        ck(matches == 0)
        words = list(product(range(3), repeat=2))
        f = [encode(tuple(rule(a,b) for a,b in edges(x))) for x in words]
        _,depth,_,cycles = graph_from_arrows(f)
        counts[name] = [sum(d == 0 for d in depth), sorted(cycles.items())]
    ck(counts["FCA"][0] == 3 and counts["CCA"][0] == 3 and counts["GHM"][0] == 1)
    print("owner_local_relabelling_matches", 0)
    print("owner_n2_recurrence", json.dumps(counts,sort_keys=True,separators=(",",":")))


if __name__ == "__main__":
    parking_boxes()
    all_word_boxes()
    sharp_family()
    bounded_owner_controls()
    print("assertions", CHECKS)
    print("status=PASS")
    # Audit census is bound by REVIEW_A.md; this executable cannot prove novelty.
    print("findings=critical:0,major:0,minor:0")
