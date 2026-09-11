#!/usr/bin/env python3
"""Independent OR gate: bitplanes, path/cycle graphs, source-edge walks.

No author imports. Deterministic stdout; graph construction does not assume
the asserted core or height. Labelled parking tokens independently check the
run-factor statement, including physical cyclic origin only modulo rotation.
"""
from collections import Counter
from itertools import permutations
from math import gcd
import argparse

ASSERTIONS = 0


def check(ok, context):
    global ASSERTIONS
    ASSERTIONS += 1
    if not ok:
        raise AssertionError(context)


TABLE = ((1, 1, 1), (0, 2, 2), (0, 0, 0))
EDGES = tuple(tuple(tuple(b for b in range(3) if TABLE[a][b] == y)
                    for a in range(3)) for y in range(3))


def digits(code, n):
    ans = []
    for _ in range(n):
        code, d = divmod(code, 3)
        ans.append(d)
    return tuple(ans)


def encode(word):
    return sum(a * 3**i for i, a in enumerate(word))


def literal(word):
    return tuple((a + 1) % 3 if a <= word[(i + 1) % len(word)] else 0
                 for i, a in enumerate(word))


def cyclic_normal(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def graph(n):
    size, mask = 3**n, (1 << n) - 1
    weights = [0] * (1 << n)
    for b in range(1, 1 << n):
        low = b & -b
        weights[b] = weights[b ^ low] + 3**(low.bit_length() - 1)
    one, two, succ = [0] * size, [0] * size, [0] * size
    for s in range(size):
        p, d = divmod(s, 3)
        one[s] = (one[p] << 1) | (d == 1)
        two[s] = (two[p] << 1) | (d == 2)
        z = mask ^ (one[s] | two[s])
        right_z = (z >> 1) | ((z & 1) << (n - 1))
        succ[s] = weights[z] + 2 * weights[one[s] & ~right_z]
    pred = [[] for _ in range(size)]
    for s, t in enumerate(succ):
        pred[t].append(s)
    depth, period = [-1] * size, [0] * size
    cycles = Counter()
    for start in range(size):
        if depth[start] >= 0:
            continue
        path, pos, s = [], {}, start
        while depth[s] < 0 and s not in pos:
            pos[s] = len(path)
            path.append(s)
            s = succ[s]
        if depth[s] < 0:
            begin = pos[s]
            length = len(path) - begin
            cycles[length] += 1
            for u in path[begin:]:
                depth[u], period[u] = 0, length
            path = path[:begin]
        for u in reversed(path):
            depth[u], period[u] = depth[succ[u]] + 1, period[succ[u]]
    return succ, pred, depth, period, cycles


def sources_by_edge_walk(y):
    n = len(y)
    out = []
    powers = [3**i for i in range(n)]

    def extend(first, last, pos, code):
        if pos == n - 1:
            if first in EDGES[y[pos]][last]:
                out.append(code)
            return
        for nxt in EDGES[y[pos]][last]:
            extend(first, nxt, pos + 1, code + powers[pos + 1] * nxt)

    for a in range(3):
        extend(a, a, 0, a)
    return sorted(out)


def run_data(w):
    n = len(w)
    cuts = [i for i in range(n) if w[i] == 0 and w[i - 1] != 0]
    if not cuts:
        return None
    c, a, b = [], [], []
    for j, start in enumerate(cuts):
        stop = cuts[(j + 1) % len(cuts)]
        length = (stop - start) % n or n
        block = tuple(w[(start + v) % n] for v in range(length))
        cc, aa, bb = block.count(0), block.count(1), block.count(2)
        check(block == (0,) * cc + (1,) * aa + (2,) * bb,
              ("nonmonotone image block", w, block))
        c.append(cc); a.append(aa); b.append(bb)
    return tuple(c), tuple(a), tuple(b)


def tokens_from_runs(run):
    c, a, b = run
    parked, free = set(), []
    for i in range(len(c)):
        free.extend([3 * i] * (c[i] - 1))
        free.extend([3 * i + 1] * (a[i] - 1))
        if b[i]:
            parked.add(3 * i + 2)
            free.extend([3 * i + 2] * (b[i] - 1))
    return parked, free


def token_step(parked, free, k):
    new_parked, new_free = set(parked), []
    for p in free:
        q = (p + 1) % (3 * k)
        if q % 3 == 2 and q not in new_parked:
            new_parked.add(q)
        else:
            new_free.append(q)
    return new_parked, new_free


def count_tokens(parked, free, k):
    counts = [0] * (3 * k)
    for p in parked:
        counts[p] += 1
    for p in free:
        counts[p] += 1
    return tuple(counts)


def counts_word(counts):
    w = ()
    for j in range(0, len(counts), 3):
        w += (0,) * (counts[j] + 1)
        w += (1,) * (counts[j + 1] + 1)
        w += (2,) * counts[j + 2]
    return w


def token_clock(parked, free, k):
    t = 0
    while free and len(parked) < k:
        parked, free = token_step(parked, free, k)
        t += 1
        if t > 3 * k:
            raise AssertionError(("parking clock overflow", k, parked, free))
    return t


def rotations(word):
    return {encode(word[i:] + word[:i]) for i in range(len(word))}


def matrix_mul(a, b):
    return tuple(tuple(sum(a[i][h] * b[h][j] for h in range(3))
                       for j in range(3)) for i in range(3))


def traces(matrix, n):
    p = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    out = [3]
    for _ in range(n):
        p = matrix_mul(p, matrix)
        out.append(sum(p[j][j] for j in range(3)))
    return out


def fibre_polynomial(n):
    # Transfer walks retaining the complete exponent, not evaluations only.
    coefficients = Counter()
    for start in range(3):
        paths = {(start, 0): 1}
        for _ in range(n):
            nxt = Counter()
            for (a, e), count in paths.items():
                for b in range(3):
                    if (a, b) != (2, 1):
                        nxt[b, e + ((a, b) == (0, 1))] += count
            paths = nxt
        for (last, e), count in paths.items():
            if last == start:
                coefficients[e] += count
    return coefficients


def exact_box(n):
    succ, pred, depth, period, cycles = graph(n)
    maximum = 2**(n // 2)
    if n == 1:
        expected_max = {0, 1, 2}
    elif n % 2 == 0:
        expected_max = rotations((0, 1) * (n // 2))
    else:
        m = n // 2
        expected_max = set().union(*(rotations(prefix + (0, 1) * (m - 1))
                                    for prefix in ((0, 0, 1), (0, 1, 1), (0, 1, 2))))
    actual_max, recurrent, a_count, b_count, intersection = set(), 0, 0, 0, 0
    fibre_hist = Counter()
    for s in range(3**n):
        w = digits(s, n)
        pairs = tuple((w[i], w[(i + 1) % n]) for i in range(n))
        is_a = all((b - a) % 3 in (0, 1) for a, b in pairs)
        is_b = all(p in ((0, 1), (1, 0), (1, 2), (2, 0)) for p in pairs)
        legal = (2, 1) not in pairs
        e = pairs.count((0, 1))
        check(succ[s] == encode(literal(w)), ("bitplane", n, s))
        check(depth[s] == 0 if is_a or is_b else depth[s] > 0,
              ("exhaustive core", n, s, depth[s]))
        if is_a:
            check(succ[s] == encode(tuple((v + 1) % 3 for v in w)) and period[s] == 3,
                  ("colour core", n, s))
        if is_b:
            spatial_period = next(t for t in range(1, n + 1) if w[t:] + w[:t] == w)
            check(succ[s] == encode(w[1:] + w[:1]) and period[s] == spatial_period,
                  ("rotation core", n, s))
        check(len(pred[s]) == (2**e if legal else 0), ("fibre", n, s))
        check(pred[s] == sources_by_edge_walk(w), ("full source set", n, s))
        if pred[s]:
            fibre_hist[e] += 1
        if len(pred[s]) == maximum:
            actual_max.add(s)
        recurrent += depth[s] == 0
        a_count += is_a; b_count += is_b; intersection += is_a and is_b
        if legal and len(set(w)) > 1:
            c, a, b = run_data(w)
            w_next = ()
            for i in range(len(c)):
                w_next += (0,) * max(b[i - 1], 1)
                w_next += (1,) * c[i]
                w_next += (2,) * (a[i] - (b[i] == 0))
            check(cyclic_normal(literal(w)) == cyclic_normal(w_next),
                  ("run evolution including zero ones", n, s))
            if min(a) >= 1:
                parked, free = tokens_from_runs((c, a, b))
                check(depth[s] == token_clock(parked, free, len(c)),
                      ("exact point clock", n, s))
    ta = traces(((1, 1, 0), (0, 1, 1), (1, 0, 1)), n)
    tb = traces(((0, 1, 0), (1, 0, 1), (1, 0, 0)), n)
    image = sum(bool(p) for p in pred)
    ti = traces(((1, 1, 1), (1, 1, 1), (1, 0, 1)), n)[n]
    luc = [2, 1]
    for _ in range(2, 2 * n + 1):
        luc.append(luc[-1] + luc[-2])
    check(image == ti == luc[2 * n], ("image census", n))
    check((a_count, b_count, intersection) == (ta[n], tb[n], 3 * (n % 3 == 0)),
          ("split recurrent census", n))
    check(recurrent == ta[n] + tb[n] - intersection, ("union census", n))
    check(ta[n] == 2**n + (2, 1, -1, -2, -1, 1)[n % 6], ("A formula", n))
    if n >= 3:
        check(tb[n] == tb[n - 2] + tb[n - 3], ("B recursion", n))
    for t in range(1, 6 * n + 1):
        actual = sum(p * count for p, count in cycles.items() if t % p == 0)
        d = gcd(n, t)
        claimed = (t % 3 == 0) * ta[n] + tb[d] - 3 * (d % 3 == 0)
        check(actual == claimed, ("fixed iterate census", n, t, actual, claimed))
    for u in (0, 1, 2, 3, 5):
        weighted = traces(((1, u, 1), (1, 1, 1), (1, 0, 1)), n)[n]
        check(weighted == sum(count * u**e for e, count in fibre_hist.items()),
              ("weighted fibre polynomial evaluations", n, u))
    check(fibre_hist == fibre_polynomial(n), ("all fibre polynomial coefficients", n))
    expected_h = 0 if n == 1 else 2 if n == 2 else 3 * (n // 3) + 1
    check(max(depth) == expected_h, ("sharp height", n, max(depth)))
    check(actual_max == expected_max, ("all maximum targets", n))
    check(sum(len(p) for p in pred) == 3**n, ("inverse mass", n))
    print(f"n={n} states={3**n} image={image} recurrent={recurrent} height={max(depth)} "
          f"max_fibre={maximum} maximizers={len(actual_max)} cycles={sorted(cycles.items())}")


def compositions(m, length):
    if length == 1:
        yield (m,)
    else:
        for v in range(m + 1):
            for tail in compositions(m - v, length - 1):
                yield (v,) + tail


def independent_parking_boxes():
    total = 0
    for k, max_m in ((1, 12), (2, 8), (3, 5), (4, 4)):
        for m in range(max_m + 1):
            maximum = 0
            for counts in compositions(m, 3 * k):
                total += 1
                c, a, b = counts[0::3], counts[1::3], counts[2::3]
                parked, free = tokens_from_runs((tuple(v + 1 for v in c),
                                                tuple(v + 1 for v in a), b))
                check(count_tokens(parked, free, k) == counts, ("token conversion", counts))
                pp, ff = token_step(parked, free, k)
                w = counts_word(counts)
                next_w = counts_word(count_tokens(pp, ff, k))
                check(cyclic_normal(literal(w)) == cyclic_normal(next_w),
                      ("labelled token lift", counts))
                t = token_clock(parked, free, k)
                maximum = max(maximum, t)
                check(t <= (3 * min(k, m) - 1 if m else 0), ("parking bound", counts))
            check(maximum == (3 * min(k, m) - 1 if m else 0), ("parking sharp box", k, m))
    for n in range(3, 151):
        k, r = divmod(n, 3)
        w = (1,) * (k + r + 1) + (2,) + (1, 2) * (k - 1)
        w1 = (2,) * (k + r + 1) + (0,) + (2, 0) * (k - 1)
        w2 = (0,) * (k + r + 1) + (1,) + (0, 1) * (k - 1)
        check(literal(w) == w1 and literal(w1) == w2, ("sharp prefix", n))
        parked, free = tokens_from_runs(run_data(w2))
        check(token_clock(parked, free, k) == 3 * k - 1, ("sharp witness", n))
    print(f"parking_complete_configurations={total} sharp_witness_lengths=3..150")


def owner_controls():
    # Global colour conjugacies, with optional spatial reflection. Reflection
    # only chooses the other directed neighbour; it cannot alter the 2-input
    # local identity. Test central and exchanged-input orientations explicitly.
    families = {
        "CCA": lambda a, b: b if b == (a + 1) % 3 else a,
        "GHM": lambda a, b: (int(b == 1) if a == 0 else (a + 1) % 3),
        "FCA": lambda a, b: a if a == 2 and b == 1 else (a + 1) % 3,
    }
    for name, rule in families.items():
        for perm in permutations(range(3)):
            for reverse_inputs in (False, True):
                identity = all(perm[TABLE[a][b]] == rule(perm[b], perm[a])
                               if reverse_inputs else
                               perm[TABLE[a][b]] == rule(perm[a], perm[b])
                               for a in range(3) for b in range(3))
                check(not identity, ("exact local owner found", name, perm, reverse_inputs))
    for a in range(3):
        for b in range(3):
            check(TABLE[a][b] == (a + 1 + (a == 1 and b == 0)) % 3,
                  ("colour moving frame", a, b))
    check(TABLE[1][0] == 0 and TABLE[2][1] == 0,
          "OR skips at10; it does not hold at21 like FCA")
    # Beyond letter conjugacies: different cycle spectra already exclude an
    # arbitrary same-length full-carrier conjugacy to these three families.
    check(all(families["CCA"](a, a) == a for a in range(3)), "CCA n1 fixed")
    check(families["GHM"](0, 0) == 0, "GHM n1 fixed")
    def fca_pair(w):
        return (families["FCA"](w[0], w[1]), families["FCA"](w[1], w[0]))
    check(not any(fca_pair((a, b)) != (a, b) and
                  fca_pair(fca_pair((a, b))) == (a, b)
                  for a in range(3) for b in range(3)), "FCA n2 has no 2cycle")
    check(literal((0, 1)) == (1, 0) and literal((1, 0)) == (0, 1), "OR n2 has 2cycle")
    m = ((1, 1, 1), (1, 1, 1), (1, 0, 1))
    m2, m3 = matrix_mul(m, m), matrix_mul(matrix_mul(m, m), m)
    check(all(m3[i][j] - 3*m2[i][j] + m[i][j] == 0
              for i in range(3) for j in range(3)), "image matrix polynomial")
    check(sum(m[i][i] for i in range(3)) == 3 and
          sum(m[i][i]*m[j][j] - m[i][j]*m[j][i]
              for i in range(3) for j in range(i+1, 3)) == 1 and
          m[0] == m[1], "image characteristic coefficients")
    print("owner_controls=36_local_relabelling_nonidentities+9_moving_frame_entries")
    print("additional_controls=CCA_GHM_n1_and_FCA_n2_cycle_obstructions+image_characteristic")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=12)
    args = parser.parse_args()
    print("OR_INDEPENDENT_BITPLANE_PATH_GATE_V1")
    print("author_imports=none; graph=orbit_path_cycle_discovery; inverse=local_edge_walk")
    owner_controls()
    for n in range(1, args.max_n + 1):
        exact_box(n)
    independent_parking_boxes()
    print(f"assertions={ASSERTIONS}")
    print("status=PASS")
    print("findings=critical:0,major:0,minor:0")


if __name__ == "__main__":
    main()
