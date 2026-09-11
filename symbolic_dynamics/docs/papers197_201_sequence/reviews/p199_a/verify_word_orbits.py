#!/usr/bin/env python3
"""P199 Round0 Review A: word-only carrier, path orbits, all-gap inverse.

No imports from author/Stage1 code. Enumeration and state identifiers are
words, never child arrays. Tail extraction never uses the proposed clock.
"""
from collections import Counter
from math import comb, factorial

ASSERTIONS = 0


def check(condition):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(ASSERTIONS)


def carrier(n):
    words = [b""]
    for k in range(1, n + 1):
        pair = bytes((k, k))
        words = [w[:i] + pair + w[i:]
                 for w in words for i in range(len(w) + 1)]
    return words


def valid(w, n):
    if len(w) != 2 * n:
        return False
    for j in range(1, n + 1):
        if w.count(j) != 2:
            return False
        a = w.index(j)
        b = w.index(j, a + 1)
        if any(k <= j for k in w[a + 1:b]):
            return False
    return True


def step(w, n):
    if not n:
        return w
    a = w.index(1)
    b = w.index(1, a + 1)
    return (bytes(j - 1 for j in w[:a]) + bytes((n, n))
            + bytes(j - 1 for j in w[a + 1:b] + w[b + 1:]))


def join(w, j):
    a = w.index(j)
    b = w.index(j, a + 1)
    return w[:a + 1] + bytes((j,)) + w[a + 1:b] + w[b + 1:]


def cyclic(w, n, t=1):
    return bytes((j - 1 - t) % n + 1 for j in w) if n else w


def nonadjacent(w, n):
    return frozenset(j for j in range(1, n + 1)
                     if w.index(j, w.index(j) + 1) != w.index(j) + 1)


def closed_gaps(w):
    # Pure word parity signature, no tree reconstruction.
    active = 0
    gaps = [0]
    for i, j in enumerate(w, 1):
        active ^= 1 << j
        if not active:
            gaps.append(i)
    return gaps


def inverse_by_all_gaps(y, n):
    if not n:
        return [b""]
    a = y.index(n)
    check(y[a:a + 2] == bytes((n, n)))
    reduced = bytes(j + 1 for j in y[:a] + y[a + 2:])
    candidates = []
    # Deliberately test EVERY character gap, not just predicted root cuts.
    for b in range(a, len(reduced) + 1):
        x = reduced[:a] + b"\x01" + reduced[a:b] + b"\x01" + reduced[b:]
        if valid(x, n):
            candidates.append(x)
    return candidates


def orbit_paths(successor):
    size = len(successor)
    tail = [-1] * size
    period = [0] * size
    cycles = Counter()
    for start in range(size):
        if tail[start] >= 0:
            continue
        path, position = [], {}
        u = start
        while tail[u] < 0 and u not in position:
            position[u] = len(path)
            path.append(u)
            u = successor[u]
        if tail[u] < 0:
            cut = position[u]
            length = len(path) - cut
            cycles[length] += 1
            for v in path[cut:]:
                tail[v] = 0
                period[v] = length
            path = path[:cut]
        for v in reversed(path):
            tail[v] = tail[successor[v]] + 1
            period[v] = period[successor[v]]
    return tail, period, cycles


def odd_double_factorial(n):
    out = 1
    for j in range(1, n + 1, 2):
        out *= j
    return out


def main():
    print("P199_REVIEW_A_WORD_ORBITS_ALL_GAPS")
    total = 0
    previous_root_poly = None
    for n in range(8):
        words = carrier(n)
        index = {w: i for i, w in enumerate(words)}
        check(len(index) == len(words) == odd_double_factorial(2 * n - 1))
        total += len(words)
        successors = []
        predecessors = [[] for _ in words]
        for i, w in enumerate(words):
            check(valid(w, n))
            y = step(w, n)
            check(y in index)
            j = index[y]
            successors.append(j)
            predecessors[j].append(i)
            check(y == (cyclic(join(w, 1), n) if n else w))
            check(nonadjacent(y, n) == frozenset(j - 1 for j in nonadjacent(w, n) if j > 1))
            if n <= 5:
                scheduled = w
                observed = w
                for t in range(1, n + 1):
                    scheduled = join(scheduled, t)
                    observed = step(observed, n)
                    check(observed == cyclic(scheduled, n, t))
                for a in range(1, n + 1):
                    check(join(join(w, a), a) == join(w, a))
                    for b in range(a + 1, n + 1):
                        check(join(join(w, a), b) == join(join(w, b), a))
        tails, periods, cycles = orbit_paths(successors)
        recurrent = 0
        root_poly = Counter()
        image = 0
        fibres = []
        maximizers = []
        for i, y in enumerate(words):
            check(tails[i] == max(nonadjacent(y, n), default=0))
            check((tails[i] == 0) == (not nonadjacent(y, n)))
            check(periods[i] == max(1, n))
            recurrent += tails[i] == 0
            recovered = inverse_by_all_gaps(y, n)
            check(len(set(recovered)) == len(recovered))
            check(sorted(index[x] for x in recovered) == predecessors[i])
            for x in recovered:
                check(step(x, n) == y)
            gaps = closed_gaps(y)
            root_poly[len(gaps)] += 1
            if n:
                a = y.index(n)
                predicted = sum(g > a for g in gaps) if a in gaps else 0
                equals_max = y[:2] == bytes((n, n)) and len(gaps) == n + 1
            else:
                predicted, equals_max = 1, True
            check(len(recovered) == predicted)
            check((len(recovered) == max(1, n)) == equals_max)
            image += bool(recovered)
            fibres.append(len(recovered))
            if equals_max:
                maximizers.append(i)
        depth = Counter(tails)
        check(recurrent == factorial(n))
        check(dict(cycles) == {max(1, n): factorial(max(0, n - 1))})
        check(max(tails) == max(0, n - 1))
        check(sum(fibres) == len(words))
        check(max(fibres) == max(1, n))
        check(len(maximizers) == factorial(max(0, n - 1)))
        check(image == (2 ** (n - 1) * factorial(n - 1) if n else 1))
        if n:
            # Independent ordered prefix/suffix decomposition at the root nn.
            convolution = sum(comb(n - 1, a) * odd_double_factorial(2 * a - 1)
                              * odd_double_factorial(2 * (n - 1 - a) - 1)
                              for a in range(n))
            check(image == convolution)
            for t in range(n):
                cdf = sum(depth[d] for d in range(t + 1))
                check(cdf == factorial(n + t) // (2 ** t * factorial(t)))
                # Delete all high-label leaves simultaneously: order them,
                # then weakly distribute the blocks over 2t+1 old gaps.
                core_and_blocks = (odd_double_factorial(2 * t - 1)
                                   * factorial(n - t) * comb(n + t, 2 * t))
                check(cdf == core_and_blocks)
        if previous_root_poly is not None:
            expected = Counter()
            for e, count in previous_root_poly.items():
                expected[e] += (2 * n - 1 - e) * count
                expected[e + 1] += e * count
            check(+expected == root_poly)
        check(sum(e * count for e, count in root_poly.items()) == 2 ** n * factorial(n))
        previous_root_poly = root_poly
        print(f"n={n} states={len(words)} image={image} recurrent={recurrent} "
              f"max_tail={max(tails)} cycles={dict(sorted(cycles.items()))} "
              f"max_fibre={max(fibres)} maximizers={len(maximizers)} "
              f"depth={tuple(depth[t] for t in range(max(tails) + 1))}")
    check(cyclic(bytes((1, 2, 2, 1)), 2) == bytes((2, 1, 1, 2)))
    check(not valid(cyclic(bytes((1, 2, 2, 1)), 2), 2))
    print(f"sources={total}")
    print(f"targets={total}")
    print(f"assertions={ASSERTIONS}")
    print("status=PASS")
    print("findings=critical:0,major:0,minor:0")


if __name__ == "__main__":
    main()
