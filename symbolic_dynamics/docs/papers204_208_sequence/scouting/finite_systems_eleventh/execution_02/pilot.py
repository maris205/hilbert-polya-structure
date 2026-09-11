#!/usr/bin/env python3
"""Exact author-only original-box pilot; standard library, no old imports."""
from collections import Counter
from itertools import permutations, product
import hashlib
import json

CHECKS = 0


def check(condition):
    global CHECKS
    CHECKS += 1
    assert condition


def atlas(label, states, outputs, extra):
    index = {x: i for i, x in enumerate(states)}
    nxt = [index[y] for y in outputs]
    check(len(index) == len(states))
    fibres = Counter(nxt)
    check(sum(fibres.values()) == len(states))
    depth = [-1] * len(states)
    period = [0] * len(states)
    cycles = []
    for start in range(len(states)):
        if depth[start] >= 0:
            continue
        path, pos = [], {}
        x = start
        while depth[x] < 0 and x not in pos:
            pos[x] = len(path)
            path.append(x)
            x = nxt[x]
        if x in pos:
            cyc = path[pos[x]:]
            k = cyc.index(min(cyc))
            cyc = cyc[k:] + cyc[:k]
            cycles.append(cyc)
            for y in cyc:
                depth[y], period[y] = 0, len(cyc)
            path = path[:pos[x]]
        for y in reversed(path):
            depth[y] = depth[nxt[y]] + 1
            period[y] = period[nxt[y]]
    for x, y in enumerate(nxt):
        check(period[x] == period[y])
        check(depth[x] == (depth[y] + 1 if depth[x] else 0))
    maxh = max(depth)
    hsource = depth.index(maxh)
    hpath, x = [], hsource
    for _ in range(maxh + period[hsource] + 1):
        hpath.append(states[x])
        x = nxt[x]
    longest = min(cycles, key=lambda c: (-len(c), c))
    maxf = max(fibres.values())
    maxtargets = sorted(y for y, size in fibres.items() if size == maxf)
    row = dict(label=label, states=len(states), images=len(fibres),
               fixed=sum(x == y for x, y in enumerate(nxt)),
               cycle_census=sorted(Counter(map(len, cycles)).items()),
               maximum_tail=maxh,
               height_census=sorted(Counter(depth).items()),
               target_fibre_histogram=sorted(Counter(
                   fibres.get(x, 0) for x in range(len(states))).items()),
               maximum_fibre=maxf, maximum_fibre_target_count=len(maxtargets),
               maximum_fibre_first_target=states[maxtargets[0]],
               longest_cycle=[states[y] for y in longest],
               maximum_height_orbit=hpath,
               transition_index_sha256=hashlib.sha256(
                   json.dumps(nxt, separators=(",", ":")).encode()).hexdigest(),
               extra=extra)
    print(json.dumps(row, sort_keys=True, separators=(",", ":")))
    return fibres, index


def wzs(d):
    n = 1 << d
    characters = [sum(((xi & x).bit_count() % 2) << x for x in range(n))
                  for xi in range(n)]
    states = list(range(1 << n))
    outputs = []
    odd_failures = []
    for state in states:
        coeff = [1 - 2 * ((state >> x) & 1) for x in range(n)]
        stride = 1
        while stride < n:
            for start in range(0, n, 2 * stride):
                for j in range(stride):
                    a, b = coeff[start+j], coeff[start+j+stride]
                    coeff[start+j], coeff[start+j+stride] = a+b, a-b
            stride *= 2
        direct = [n - 2 * (state ^ c).bit_count() for c in characters]
        check(coeff == direct)
        check(sum(x*x for x in coeff) == n*n)
        target = sum((c == 0) << i for i, c in enumerate(coeff))
        outputs.append(target)
        if d >= 2 and state.bit_count() % 2 and target:
            odd_failures.append(state)
    full = (1 << n) - 1
    for state in states:
        check(outputs[state] == outputs[state ^ full])
    atlas(f"WZS_d{d}", states, outputs,
          dict(odd_weight_nonempty_output_failures=odd_failures,
               empty_output=outputs[0], full_output=outputs[-1]))


def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % p
    return trim(out)


def rem(a, h, p):
    a = list(a)
    trim(a)
    while len(a) >= len(h):
        shift, lead = len(a) - len(h), a[-1]
        for j, c in enumerate(h):
            a[shift+j] = (a[shift+j] - lead*c) % p
        trim(a)
    return a


def value(a, x, p):
    out = 0
    for c in reversed(a):
        out = (out*x + c) % p
    return out


def determinant(matrix, p):
    a = [row[:] for row in matrix]
    det = 1
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i] % p), None)
        if pivot is None:
            return 0
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            det = -det
        z = a[i][i] % p
        det = det*z % p
        for j in range(i+1, len(a)):
            factor = a[j][i]*pow(z, -1, p) % p
            for k in range(i, len(a)):
                a[j][k] = (a[j][k] - factor*a[i][k]) % p
    return det % p


def acp_map(state, p):
    r = len(state)
    f = list(state) + [1]
    h = [(j*f[j]*pow(r, -1, p)) % p for j in range(1, r+1)]
    m = r - 1
    matrix = [[0]*m for _ in range(m)]
    for j in range(m):
        col = rem([0]*j + f, h, p)
        for i, c in enumerate(col):
            matrix[i][j] = c
    char = [0]*(m+1)
    for perm in permutations(range(m)):
        inv = sum(perm[i] > perm[j] for i in range(m) for j in range(i+1, m))
        term = [(-1)**inv % p]
        for i, j in enumerate(perm):
            term = mul(term, [(-matrix[i][j]) % p, 1] if i == j
                       else [(-matrix[i][j]) % p], p)
        for k, c in enumerate(term):
            char[k] = (char[k] + c) % p
    check(char[-1] == 1)
    for y in range(r):
        test = [[((y if i == j else 0) - matrix[i][j]) % p
                 for j in range(m)] for i in range(m)]
        check(value(char, y, p) == determinant(test, p))
    out = mul([(-state[0]) % p, 1], char, p)
    check(len(out) == r+1 and out[-1] == 1)
    check(value(out, state[0], p) == 0)
    if r == 2:
        b, a = state
        z = a*a*pow(4, -1, p) % p
        check(out == [(b*b-b*z) % p, (z-2*b) % p, 1])
    return tuple(out[:-1])


def acp(r, p):
    states = list(product(range(p), repeat=r))
    outputs = [acp_map(state, p) for state in states]
    fibres, index = atlas(f"ACP_r{r}_p{p}", states, outputs,
                          dict(coefficient_order="ascending constant first"))
    if r == 2:
        for target in states:
            v, u = target
            decoded = sum(1 for b in range(p) if (b*b+u*b+v) % p == 0
                          for a in range(p) if (a*a-4*(u+2*b)) % p == 0)
            check(decoded == fibres.get(index[target], 0))


def main():
    for d in range(5):
        wzs(d)
    for r, p in ((2,3),(2,5),(2,7),(2,11),(3,5),(3,7),(4,5)):
        acp(r, p)
    print(json.dumps(dict(status="PASS", assertions=CHECKS,
                          literal_count=2, full_boxes=12), sort_keys=True))


if __name__ == "__main__":
    main()
