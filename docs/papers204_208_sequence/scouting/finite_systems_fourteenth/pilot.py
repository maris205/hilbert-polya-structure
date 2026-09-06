"""Literal fixed-box author scout; no imports of earlier scientific code."""
from collections import Counter, deque
from itertools import combinations, product
import hashlib
import json

CHECKS = 0


def check(condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(CHECKS)


def encode(digits, base):
    value = 0
    for digit in digits:
        value = value * base + digit
    return value


def census(rule, params, mapping, extra=None):
    """Standard functional-graph census adapted from the closed twelfth scout."""
    n = len(mapping)
    check(all(0 <= y < n for y in mapping))
    fibres = Counter(mapping)
    degrees = [fibres[x] for x in range(n)]
    queue = deque(x for x in range(n) if not degrees[x])
    removed = []
    while queue:
        x = queue.popleft()
        removed.append(x)
        y = mapping[x]
        degrees[y] -= 1
        if not degrees[y]:
            queue.append(y)
    core = set(range(n)) - set(removed)
    depth = [0] * n
    for x in reversed(removed):
        depth[x] = depth[mapping[x]] + 1
    unseen = set(core)
    cycles = []
    while unseen:
        start = min(unseen)
        cycle = [start]
        y = mapping[start]
        while y != start:
            check(y in unseen)
            cycle.append(y)
            y = mapping[y]
        unseen.difference_update(cycle)
        cycles.append(cycle)
    check(sum(map(len, cycles)) == len(core))
    check(all(depth[x] == 0 if x in core else depth[x] == depth[mapping[x]] + 1
              for x in range(n)))
    image = set(range(n))
    widths = [n]
    while True:
        nxt = {mapping[x] for x in image}
        if nxt == image:
            break
        widths.append(len(nxt))
        image = nxt
    check(image == core)
    h = max(depth)
    check(len(widths) - 1 == h)
    tail = [depth.index(h)]
    for _ in range(h):
        tail.append(mapping[tail[-1]])
    maximum = max(fibres.values())
    targets = [x for x in sorted(fibres) if fibres[x] == maximum]
    result = dict(rule=rule, params=params, states=n, image=len(fibres),
                  core=len(core), maximum_tail=h, image_widths=widths,
                  cycle_counts=dict(sorted(Counter(map(len, cycles)).items())),
                  longest_cycle=max(cycles, key=len), maximum_tail_orbit=tail,
                  maximum_fibre=maximum, maximum_fibre_target_count=len(targets),
                  first_maximum_fibre_target=targets[0],
                  mapping_sha256=hashlib.sha256(json.dumps(mapping, separators=(",", ":")).encode()).hexdigest())
    if extra:
        result.update(extra)
    return result


def snc_direct(a, rows, cols, p):
    sums = [sum(a[i * cols:(i + 1) * cols]) % p for i in range(rows)]
    if 0 in sums:
        return None
    b = [a[i * cols + j] * cols * pow(sums[i], -1, p) % p
         for i in range(rows) for j in range(cols)]
    columns = [sum(b[i * cols + j] for i in range(rows)) % p for j in range(cols)]
    if 0 in columns:
        return None
    return tuple(b[i * cols + j] * rows * pow(columns[j], -1, p) % p
                 for i in range(rows) for j in range(cols))


def snc_cleared(a, p):
    """Independently clear the two row denominators before column scaling."""
    u = sum(a[:3]) % p
    v = sum(a[3:]) % p
    if u == 0 or v == 0:
        return None
    weighted = tuple((a[j] * v) % p for j in range(3)) + tuple((a[j] * u) % p for j in range(3, 6))
    denominators = [(weighted[j] + weighted[j + 3]) % p for j in range(3)]
    if 0 in denominators:
        return None
    return tuple(2 * weighted[i * 3 + j] * pow(denominators[j], -1, p) % p
                 for i in range(2) for j in range(3))


def snc(p):
    sink = p ** 6
    mapping = []
    for a in product(range(p), repeat=6):
        out = snc_direct(a, 2, 3, p)
        alternative = snc_cleared(a, p)
        check(out == alternative)
        if out is None:
            mapping.append(sink)
            continue
        check(all((out[j] + out[j + 3]) % p == 2 for j in range(3)))
        check(all((x == 0) == (y == 0) for x, y in zip(a, out)))
        for j, k in combinations(range(3), 2):
            check((out[j] * out[3 + k] * a[k] * a[3 + j]
                   - out[k] * out[3 + j] * a[j] * a[3 + k]) % p == 0)
        if sum(out[:3]) % p == 3 and sum(out[3:]) % p == 3:
            check(snc_direct(out, 2, 3, p) == out)
        mapping.append(encode(out, p))
    mapping.append(sink)
    check(snc_direct((1,) * 6, 2, 3, p) == (1,) * 6)
    return census("SNC", dict(rows=2, cols=3, p=p), mapping,
                  dict(sink_encoding=sink, sink_fibre=sum(y == sink for y in mapping)))


def rci(p, dim):
    points = list(product(range(p), repeat=dim))
    v = len(points)
    pair_inversions = {}
    for centre_index, centre in enumerate(points):
        for x, point in enumerate(points):
            delta = tuple((a - b) % p for a, b in zip(point, centre))
            norm = sum(a * a for a in delta) % p
            if norm:
                out = tuple((b + a * pow(norm, -1, p)) % p for a, b in zip(delta, centre))
                expected = encode(out, p)
                solutions = [y for y, q in enumerate(points)
                             if all(norm * (b - c) % p == a for a, b, c in zip(delta, q, centre))]
                check(solutions == [expected])
                pair_inversions[centre_index, x] = expected
            else:
                pair_inversions[centre_index, x] = None
            # All selected forms are anisotropic, including the trivial d=0 carrier.
            check((norm == 0) == (point == centre))
    mapping = []
    for mask in range(1 << v):
        selected = [x for x in range(v) if mask >> x & 1]
        cardinal = len(selected)
        check(cardinal == mask.bit_count())
        if cardinal % p == 0:
            mapping.append(0)
            continue
        total = tuple(sum(points[x][i] for x in selected) % p for i in range(dim))
        centre = tuple(a * pow(cardinal, -1, p) % p for a in total)
        g = encode(centre, p)
        # Independently find the centroid by solving its affine equations.
        centres = [j for j, candidate in enumerate(points)
                   if all(cardinal * b % p == a for a, b in zip(total, candidate))]
        check(centres == [g])
        image = {pair_inversions[g, x] for x in selected if pair_inversions[g, x] is not None}
        out = sum(1 << y for y in image)
        inverse_image = set()
        # Inversion is an involution about this fixed centre, not about a future one.
        for y in range(v):
            x = pair_inversions[g, y]
            if x is not None and mask >> x & 1:
                inverse_image.add(y)
        check(image == inverse_image)
        check(out.bit_count() == cardinal - int(g in selected))
        mapping.append(out)
    for mask in range(1 << v):
        if mask.bit_count() == 1:
            check(mapping[mask] == 0)
        if mask.bit_count() == 2:
            check(mapping[mapping[mask]] == mask)
    return census("RCI", dict(p=p, d=dim), mapping)


def rrm(n):
    if n == 0:
        return census("RRM", dict(n=0), [0])
    mapping = []
    leftoids = 0
    for operation in product(range(n), repeat=n * n):
        out = tuple(operation[operation[x * n + y] * n + x]
                    for x in range(n) for y in range(n))
        # Relational expansion: sum over the unique old multiplication result.
        relational = tuple(sum(operation[z * n + x]
                               for z in range(n) if operation[x * n + y] == z)
                           for x in range(n) for y in range(n))
        check(out == relational)
        if all(operation[x * n + y] == operation[x * n] for x in range(n) for y in range(n)):
            leftoids += 1
            f = [operation[x * n] for x in range(n)]
            check(out == tuple(f[f[x]] for x in range(n) for y in range(n)))
        mapping.append(encode(out, n))
    check(leftoids == n ** n)
    return census("RRM", dict(n=n), mapping, dict(deducted_leftoid_count=leftoids))


def main():
    rows = [snc(p) for p in (5, 7)]
    rows += [rci(p, d) for p, d in ((3, 0), (3, 1), (3, 2), (5, 1), (7, 1), (11, 1))]
    rows += [rrm(n) for n in (0, 1, 2, 3)]
    check(len(rows) == 12)
    check(sum(row["states"] for row in rows) == 155707)
    print(json.dumps(dict(schema="fourteenth-author-pilot-v1", assertions=CHECKS,
                          boxes=rows), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
