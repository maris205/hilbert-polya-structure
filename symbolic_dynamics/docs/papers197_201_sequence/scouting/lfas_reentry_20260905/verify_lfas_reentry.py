#!/usr/bin/env python3
"""LFAS re-entry: independent naive rectangles versus row-support theory."""
from collections import Counter
from itertools import combinations

CHECKS = 0


def check(ok, text):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(text)


def comparable(a, b):
    return a & b == a or a & b == b


def theory_selector(rows):
    for i, k in combinations(range(len(rows)), 2):
        a, b = rows[i] & ~rows[k], rows[k] & ~rows[i]
        if a and b:
            aa, bb = (a & -a).bit_length() - 1, (b & -b).bit_length() - 1
            return i, k, min(aa, bb), max(aa, bb)
    return None


def changed(rows, q):
    i, k, a, b = q
    y = list(rows)
    y[i] ^= (1 << a) | (1 << b)
    y[k] ^= (1 << a) | (1 << b)
    return tuple(y)


def theory_inverse(rows, s):
    q = theory_selector(rows)
    if q is None:
        return {rows}
    i = q[0]
    P = rows[i]
    answer = set()
    for k in range(i + 1, len(rows)):
        D, E = P & ~rows[k], rows[k] & ~P
        if not (D and E):
            continue
        j = ((D | E) & -(D | E)).bit_length() - 1
        same, opposite = (D, E) if D & (1 << j) else (E, D)
        rest = same ^ (1 << j)
        bound = (rest & -rest).bit_length() - 1 if rest else s
        for ell in range(j + 1, bound):
            if not opposite & (1 << ell):
                continue
            newpivot = P ^ (1 << j) ^ (1 << ell)
            if all(comparable(newpivot, rows[h]) for h in range(i + 1, k)):
                answer.add(changed(rows, (i, k, j, ell)))
    return answer


def recurring(rows):
    q = theory_selector(rows)
    if q is None:
        return True
    i, k, a, b = q
    diff = rows[i] ^ rows[k]
    first = diff & -diff
    rest = diff ^ first
    second = rest & -rest
    opposite = bool(rows[i] & first) != bool(rows[i] & second)
    newpivot = rows[i] ^ (1 << a) ^ (1 << b)
    return opposite and all(comparable(newpivot, rows[h]) for h in range(i + 1, k))


def audit(r, s):
    n = 1 << (r * s)
    mask = (1 << s) - 1
    rects = []
    for i, k in combinations(range(r), 2):
        for a, b in combinations(range(s), 2):
            positions = (i * s + a, i * s + b, k * s + a, k * s + b)
            flip = sum(1 << z for z in positions)
            pat1 = (1 << positions[0]) | (1 << positions[3])
            pat2 = flip ^ pat1
            rects.append(((i, k, a, b), flip, pat1, pat2))
    ff, qq = [], []
    for x in range(n):
        q, y = None, x
        for rec, flip, p1, p2 in rects:
            if x & flip in (p1, p2):
                q, y = rec, x ^ flip
                break
        ff.append(y)
        qq.append(q)
    inverse = [[] for _ in range(n)]
    for x, y in enumerate(ff):
        inverse[y].append(x)
    hist, maxf = Counter(), 0
    maxstates = []
    for x in range(n):
        rows = tuple((x >> (i * s)) & mask for i in range(r))
        check(theory_selector(rows) == qq[x], "row-support literal selector")
        got = {tuple((a >> (i * s)) & mask for i in range(r)) for a in inverse[x]}
        check(theory_inverse(rows, s) == got, "explicit full inverse sets")
        seen, at = {}, x
        while at not in seen:
            seen[at] = len(seen)
            at = ff[at]
        tail, period = seen[at], len(seen) - seen[at]
        hist[tail] += 1
        check(period in (1, 2), "full period support")
        check(tail <= 2 * r - 3, "sharp-in-width temporal bound")
        check(recurring(rows) == (tail == 0), "explicit recurrent criterion")
        if qq[x] is not None:
            check(qq[ff[x]][0] == qq[x][0], "invariant pivot row")
            check(qq[ff[x]][1] <= qq[x][1], "descending partner row")
            check(qq[ff[x]][2] <= qq[x][2] and qq[ff[x]][3] <= qq[x][3],
                  "coordinatewise nonincreasing rectangle columns")
        if len(got) > maxf:
            maxf, maxstates = len(got), [rows]
        elif len(got) == maxf:
            maxstates.append(rows)
    expected_max = (r - 1) * (s - 1)
    check(maxf == expected_max, "sharp inverse maximum")
    if (r, s) == (2, 2):
        check(len(maxstates) == 16, "2x2 every state maximizes")
    else:
        stars = {(1,) + (mask ^ 1,) * (r - 1),
                 (mask ^ 1,) + (1,) * (r - 1)}
        check(set(maxstates) == stars, "all maximum-fibre equality states")
    print(f"r={r} s={s} states={n} image={sum(bool(z) for z in inverse)} "
          f"fixed={sum(x==y for x,y in enumerate(ff))} max_tail={max(hist)} "
          f"max_fibre={maxf} maximizers={len(maxstates)}")


def wide_witness(r, s):
    # Unused trailing columns are all zero and do not change the scheduler.
    rows = [1 << r]
    for k in range(1, r):
        rows.append(1 | (1 << k) | sum(1 << j for j in range(k + 2, r + 1)))
    check(s >= r + 1, "witness width")
    rows = tuple(rows)
    path = []
    while not recurring(rows):
        path.append(theory_selector(rows))
        rows = changed(rows, path[-1])
    check(len(path) == 2 * r - 3, "all-r sharp wide witness")
    check(theory_selector(rows) == (0, 1, 0, 1), "witness recurrent rectangle")
    return len(path)


def main():
    print("LFAS conservative re-entry: exact inverse, invariant pivot, sharp-in-width tail")
    boxes = [(2, 2), (2, 3), (3, 2), (2, 5), (5, 2), (3, 3),
             (3, 4), (4, 3), (3, 5), (5, 3), (4, 4)]
    for r, s in boxes:
        audit(r, s)
    for r in range(2, 21):
        for s in (r + 1, r + 4):
            wide_witness(r, s)
    print("wide witnesses: r=2..20, s=r+1 and r+4, tail=2r-3")
    print(f"PASS boxes={len(boxes)} wide_witnesses=38 assertions={CHECKS}")
    print("Exact narrow/square tail formula remains CONJECTURE; external owner gate PENDING")


if __name__ == "__main__":
    main()
