#!/usr/bin/env python3
"""Independent LFAS gate: column-major carrier, graph peeling, prefix inverse.

No imports from the author package. The literal graph checks four matrix
entries; the inverse uses the target difference word, not source scheduling.
"""
from collections import Counter, deque
from itertools import combinations

CHECKS = 0


def require(value, label):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(label)


def decode(x, r, s):
    return tuple(tuple((x >> (c*r+i)) & 1 for c in range(s)) for i in range(r))


def encode(rows):
    return sum(v << (c*len(rows)+i) for i, row in enumerate(rows)
               for c, v in enumerate(row))


def comparable(a, b):
    types = {u-v for u, v in zip(a, b)}
    return not (-1 in types and 1 in types)


def reverse_rectangle(rows, q):
    i, k, a, b = q
    return tuple(tuple(1-v if j in (i, k) and c in (a, b) else v
                       for c, v in enumerate(row)) for j, row in enumerate(rows))


def literal(rows):
    r, s = len(rows), len(rows[0])
    for i, k in combinations(range(r), 2):
        for a, b in combinations(range(s), 2):
            v = (rows[i][a], rows[i][b], rows[k][a], rows[k][b])
            if v in ((1, 0, 0, 1), (0, 1, 1, 0)):
                q = (i, k, a, b)
                return reverse_rectangle(rows, q), q
    return rows, None


def target_pivot(rows):
    for i, k in combinations(range(len(rows)), 2):
        if not comparable(rows[i], rows[k]):
            return i, k
    return None


def inverse_by_prefix(rows):
    p = target_pivot(rows)
    if p is None:
        return {encode(rows)}
    i = p[0]
    answer = set()
    for k in range(i+1, len(rows)):
        differences = [c for c in range(len(rows[0])) if rows[i][c] != rows[k][c]]
        if not differences:
            continue
        a = differences[0]
        # The first target difference followed by its initial opposite run.
        for b in differences[1:]:
            if rows[i][b] == rows[i][a]:
                break
            pivot = tuple(1-v if c in (a, b) else v for c, v in enumerate(rows[i]))
            if all(comparable(pivot, rows[h]) for h in range(i+1, k)):
                answer.add(encode(reverse_rectangle(rows, (i, k, a, b))))
    return answer


def recurrent_criterion(rows):
    p = target_pivot(rows)
    if p is None:
        return True
    i, k = p
    a, b = [c for c in range(len(rows[0])) if rows[i][c] != rows[k][c]][:2]
    if rows[i][a] == rows[i][b]:
        return False
    pivot = tuple(1-v if c in (a, b) else v for c, v in enumerate(rows[i]))
    return all(comparable(pivot, rows[h]) for h in range(i+1, k))


def graph_data(forward):
    n = len(forward)
    inverse = [set() for _ in range(n)]
    for x, y in enumerate(forward):
        inverse[y].add(x)
    degree = [len(z) for z in inverse]
    queue = deque(x for x in range(n) if degree[x] == 0)
    removed = []
    while queue:
        x = queue.popleft()
        removed.append(x)
        y = forward[x]
        degree[y] -= 1
        if degree[y] == 0:
            queue.append(y)
    depth, period = [0]*n, [0]*n
    for x in range(n):
        if degree[x] and not period[x]:
            orbit, at = [x], forward[x]
            while at != x:
                orbit.append(at)
                at = forward[at]
            for y in orbit:
                period[y] = len(orbit)
    for x in reversed(removed):
        depth[x] = depth[forward[x]]+1
        period[x] = period[forward[x]]
    return inverse, depth, period


def audit(r, s):
    size = 1 << (r*s)
    matrices = [decode(x, r, s) for x in range(size)]
    forward, selectors = [], []
    for rows in matrices:
        y, q = literal(rows)
        forward.append(encode(y))
        selectors.append(q)
    inverse, depth, periods = graph_data(forward)
    for x, rows in enumerate(matrices):
        y, q = forward[x], selectors[x]
        require(inverse_by_prefix(rows) == inverse[x], "complete inverse SOURCE SET")
        require(recurrent_criterion(rows) == (depth[x] == 0), "recurrent iff graph")
        require(periods[x] in (1, 2), "period support")
        require(depth[x] <= 2*r-3, "all-state row tail bound")
        require(sum(map(sum, rows)) == sum(map(sum, matrices[y])), "total mass")
        require(tuple(map(sum, rows)) == tuple(map(sum, matrices[y])), "row margins")
        require(tuple(map(sum, zip(*rows))) == tuple(map(sum, zip(*matrices[y]))), "column margins")
        require(forward[x ^ (size-1)] == (y ^ (size-1)), "complement commutation")
        if q is not None:
            next_q = selectors[y]
            require(next_q is not None, "no switch reaches fixed")
            require(next_q[0] == q[0], "invariant first pivot")
            require(next_q[1] <= q[1], "nonincreasing partner")
            require(next_q <= q, "selector cannot increase")
            at, visits = x, Counter()
            for _ in range(depth[x]+1):
                visits[selectors[at][1]] += 1
                at = forward[at]
            require(max(visits.values()) <= 2, "at most two selector states per partner")
            require(depth[x] <= 2*len(visits)-1, "refined partner bound")
        else:
            require(inverse[x] == {x}, "fixed isolated source")
    maximum = max(map(len, inverse))
    maximizers = {x for x in range(size) if len(inverse[x]) == maximum}
    require(maximum == (r-1)*(s-1), "sharp fibre maximum")
    star = encode(((1,)+(0,)*(s-1),)+((0,)+(1,)*(s-1),)*(r-1))
    expected = set(range(16)) if (r, s) == (2, 2) else {star, star ^ (size-1)}
    require(maximizers == expected, "ALL equality targets")
    require(sum(map(len, inverse)) == size, "full fibre mass")
    if s >= r+1:
        require(max(depth) == 2*r-3, "wide sharpness exhaustively")
    print(f"r={r} s={s} states={size} image={sum(bool(z) for z in inverse)} "
          f"fixed={sum(x==y for x,y in enumerate(forward))} "
          f"depths={sorted(Counter(depth).items())} max_fibre={maximum} "
          f"maximizers={len(maximizers)}")


def witness(r, s):
    supports = [{r}] + [{0, k} | set(range(k+2, r+1)) for k in range(1, r)]
    rows = tuple(tuple(int(c in support) for c in range(s)) for support in supports)
    seen, itinerary = {}, []
    while rows not in seen:
        seen[rows] = len(seen)
        rows, q = literal(rows)
        itinerary.append(q)
    tail = seen[rows]
    expected = [q for k in range(r-1, 0, -1)
                for q in ((0, k, 0, k+1), (0, k, 0, k))]
    require(tail == 2*r-3, "wide orbit exact tail")
    require(len(seen)-tail == 2, "wide orbit period")
    require(itinerary[:tail+1] == expected, "wide complete selector itinerary")


def main():
    print("LFAS_INDEPENDENT_STAGE1_COLUMN_MAJOR_GRAPH_CONTROL")
    boxes = [(2, 2), (2, 3), (3, 2), (3, 3), (2, 5), (5, 2),
             (3, 4), (4, 3), (3, 5), (5, 3), (4, 4), (2, 8), (8, 2)]
    for r, s in boxes:
        audit(r, s)
    for r in range(2, 21):
        for s in (r+1, r+5):
            witness(r, s)
    print("wide_witnesses=38 r=2..20 widths=r+1,r+5 exact_selector_itineraries=PASS")
    print(f"boxes={len(boxes)} source_states={sum(1 << (r*s) for r,s in boxes)} assertions={CHECKS}")
    print("PASS_BOUNDED_CONTROL_NOT_EXTERNAL_NOVELTY_CLEARANCE")


if __name__ == "__main__":
    main()
