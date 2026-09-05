#!/usr/bin/env python3
"""Independent P200 Review A: row-mask tuples and forward orbit paths.

No author/gate imports. Sources use row-exclusive minima; targets use an
ordered difference-word prefix. Complete source SETS, not only fibre counts.
Written before reading the paper author's verifier source.
"""
from collections import Counter, defaultdict
from itertools import product

ASSERTIONS = 0


def check(ok, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not ok:
        raise AssertionError(label)


def comparable(a, b):
    return a & b == a or a & b == b


def lowbit(a):
    return (a & -a).bit_length()-1


def select(rows):
    for i, a in enumerate(rows):
        for k in range(i+1, len(rows)):
            b = rows[k]
            d, e = a & ~b, b & ~a
            if d and e:
                j, ell = sorted((lowbit(d), lowbit(e)))
                return i, k, j, ell
    return None


def flip(rows, q):
    if q is None:
        return rows
    i, k, j, ell = q
    out = list(rows)
    out[i] ^= (1 << j) | (1 << ell)
    out[k] ^= (1 << j) | (1 << ell)
    return tuple(out)


def step(rows):
    return flip(rows, select(rows))


def literal_selector(rows, s):
    # Secondary entrywise scan used on all complete boxes of <=12 cells.
    for i in range(len(rows)):
        for k in range(i+1, len(rows)):
            for a in range(s):
                for b in range(a+1, s):
                    u, v = (rows[i] >> a) & 1, (rows[i] >> b) & 1
                    w, z = (rows[k] >> a) & 1, (rows[k] >> b) & 1
                    if u == z and v == w and u != v:
                        return i, k, a, b
    return None


def inverse(rows, s):
    pivot = next((i for i in range(len(rows))
                  if any(not comparable(rows[i], rows[k])
                         for k in range(i+1, len(rows)))), None)
    if pivot is None:
        return {rows}
    p = rows[pivot]
    answer = set()
    for k in range(pivot+1, len(rows)):
        other = rows[k]
        word = [(j, bool(p & (1 << j))) for j in range(s)
                if (p ^ other) & (1 << j)]
        if not word:
            continue
        j, sign = word[0]
        for ell, kind in word[1:]:
            if kind == sign:
                break
            changed = p ^ (1 << j) ^ (1 << ell)
            if all(comparable(changed, rows[h])
                   for h in range(pivot+1, k)):
                source = flip(rows, (pivot, k, j, ell))
                check(source not in answer, 'distinct reconstructed matrices')
                answer.add(source)
    return answer


def recurrent_criterion(rows, s):
    q = select(rows)
    if q is None:
        return True
    i, k, _, _ = q
    diff = [j for j in range(s) if (rows[i] ^ rows[k]) & (1 << j)]
    j, ell = diff[:2]
    opposite = bool(rows[i] & (1 << j)) != bool(rows[i] & (1 << ell))
    newpivot = rows[i] ^ (1 << j) ^ (1 << ell)
    return opposite and all(comparable(newpivot, rows[h]) for h in range(i+1, k))


def functional_graph(nxt):
    depth, period = {}, {}
    for start in nxt:
        if start in depth:
            continue
        path, index, v = [], {}, start
        while v not in depth and v not in index:
            index[v] = len(path)
            path.append(v)
            v = nxt[v]
        if v not in depth:
            cut = index[v]
            length = len(path)-cut
            for x in path[cut:]:
                depth[x], period[x] = 0, length
            path = path[:cut]
        for x in reversed(path):
            depth[x], period[x] = depth[nxt[x]]+1, period[nxt[x]]
    return depth, period


def maxima(r, s):
    if (r, s) == (2, 2):
        return set(product(range(4), repeat=2))
    full = (1 << s)-1
    first = (1,) + (full ^ 1,)*(r-1)
    return {first, tuple(full ^ a for a in first)}


def main():
    boxes = [(r,s) for r in range(2,9) for s in range(2,9) if r*s <= 16]
    total, image_counts = 0, {}
    for r, s in boxes:
        states = list(product(range(1 << s), repeat=r))
        nxt, pre, selectors = {}, defaultdict(set), {}
        full = (1 << s)-1
        for x in states:
            q = select(x)
            if r*s <= 12:
                check(q == literal_selector(x,s), 'literal rectangle priority')
            y = flip(x,q)
            nxt[x], selectors[x] = y,q
            pre[y].add(x)
            check(tuple(a.bit_count() for a in x) == tuple(a.bit_count() for a in y), 'row margins')
            check(all(sum((a >> j)&1 for a in x) == sum((a >> j)&1 for a in y)
                      for j in range(s)), 'column margins')
            check(step(tuple(full ^ a for a in x)) == tuple(full ^ a for a in y), 'complement conjugacy')
        depth, period = functional_graph(nxt)
        for x in states:
            q = selectors[x]
            check(period[x] in (1,2), 'all periods one or two')
            check((depth[x] == 0) == recurrent_criterion(x,s), 'full recurrent iff')
            check((depth[x] == 0) == (nxt[nxt[x]] == x), 'direct two-step recurrent iff')
            check(depth[x] <= 2*r-3, 'global row tail bound')
            if q is not None:
                qn = selectors[nxt[x]]
                check(qn is not None and qn <= q, 'selector nonincrease and nonfixed closure')
                check(qn[0] == q[0] and qn[1] <= q[1], 'pivot invariance and partner descent')
                partners, cur = [], x
                for _ in range(depth[x]+1):
                    partners.append(selectors[cur][1])
                    cur = nxt[cur]
                check(max(Counter(partners).values()) <= 2, 'every partner at most two visits')
                check(depth[x] <= 2*len(set(partners))-1 <= 2*(r-q[0]-1)-1, 'refined clock')
            check(inverse(x,s) == pre[x], 'every inverse source set including empty')
        actual = {x for x in states if len(pre[x]) == (r-1)*(s-1)}
        check(actual == maxima(r,s), 'complete maximizing equality set')
        check(max(map(len,pre.values())) == (r-1)*(s-1), 'maximum fibre')
        check(sum(map(len,pre.values())) == len(states), 'all-target mass')
        if s >= r+1:
            check(max(depth.values()) == 2*r-3, 'sharp wide box')
        image = sum(bool(pre[x]) for x in states)
        image_counts[r,s] = image
        total += len(states)
        print(f'r={r} s={s} sources={len(states)} targets={len(states)} image={image} fixed={sum(nxt[x]==x for x in states)} tail={max(depth.values())} max_fibre={(r-1)*(s-1)} maximizers={len(actual)}')
    check(image_counts[3,4] == 3292 and image_counts[4,3] == 3290, 'transpose negative control')
    witnesses = 0
    for r in range(2,31):
        for s in (r+1,r+4):
            rows = (1 << r,) + tuple(sum(1 << j for j in {0,k,*range(k+2,r+1)}) for k in range(1,r))
            for complement in (False,True):
                x = tuple(((1 << s)-1) ^ a for a in rows) if complement else rows
                sequence, seen = [], {}
                while x not in seen:
                    seen[x] = len(sequence)
                    sequence.append(x)
                    x = step(x)
                tail = seen[x]
                check(tail == 2*r-3 and len(sequence)-tail == 2, 'entire wide orbit')
                expected = [(0,k,0,j) for k in range(r-1,0,-1) for j in (k+1,k)]
                check([select(a) for a in sequence[:tail+1]] == expected, 'full sharp itinerary')
                check(all(not recurrent_criterion(a,s) for a in sequence[:tail]), 'no premature entry')
                check(all(recurrent_criterion(a,s) for a in sequence[tail:]), 'exact terminal pair')
                witnesses += 1
    print(f'boxes={len(boxes)} full_sources={total} full_targets={total} wide_witnesses={witnesses}')
    print(f'assertions={ASSERTIONS}')
    print('status=PASS')
    print('findings=critical:0,major:0,minor:0')
    print('external_status=OWNER_AMBER/HOLD_EXTERNAL')


if __name__ == '__main__':
    main()
