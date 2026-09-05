#!/usr/bin/env python3
"""P202 B: byte words, composition powers, sparse patches, cumulative flux.

No author/A module imports; no Kahn pruning, path-cycle discovery, labelled
particle simulation, event heap or source-domain/edge-walk reconstruction.
The full frozen manuscript, not empirical output, supplies the claims.
"""
from array import array
from collections import Counter
from itertools import product
from math import gcd

CHECKS = 0


def check(ok, where):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(where)


def forward(w):
    return bytes((a + 1 + (a == 1 and b == 0)) % 3
                 for a, b in zip(w, w[1:] + w[:1]))


def rank(w):
    v = 0
    for a in w:
        v = 3 * v + a
    return v


def flags(w):
    pairs = tuple(zip(w, w[1:] + w[:1]))
    return (all((b-a) % 3 <= 1 for a, b in pairs),
            all((a, b) in ((0, 1), (1, 0), (1, 2), (2, 0))
                for a, b in pairs))


def rotations(w):
    return {w[i:] + w[:i] for i in range(len(w))}


def run_surplus(w):
    """Parse a nonconstant twice-image using a zero-run boundary."""
    n = len(w)
    cut = next(i for i in range(n) if w[i] == 0 and w[i-1] != 0)
    v = w[cut:] + w[:cut]
    z = []
    i = 0
    while i < n:
        counts = []
        for letter in range(3):
            begin = i
            while i < n and v[i] == letter:
                i += 1
            counts.append(i-begin)
        c, a, b = counts
        check(c >= 1 and a >= 1 and b >= 0, ("run domain", w))
        z.extend((c-1, a-1, b))
    check(sum(z) == n-2*(len(z)//3), "surplus mass")
    return tuple(z)


def flux_clearance(z, verify_steps=False):
    """U_i(t+1)=(z_i+U_(i-1)(t)-capacity_i)_+, U(0)=0."""
    size = len(z)
    cap = tuple(int(i % 3 == 2) for i in range(size))
    total = sum(z)
    cumulative = (0,) * size
    previous = z
    for t in range(3*size + 1):
        state = tuple(z[i]+cumulative[i-1]-cumulative[i]
                      for i in range(size))
        if verify_steps:
            check(sum(state) == total and min(state) >= 0, "flux conservation")
            if t:
                local = tuple((min(previous[i], 1) if cap[i] else 0)
                              + previous[i-1] - (min(previous[i-1], 1)
                                                   if cap[i-1] else 0)
                              for i in range(size))
                check(local == state, "cumulative/local recurrence")
        occupied = sum(state[i] > 0 for i in range(2, size, 3))
        if occupied == size//3 or occupied == total:
            return t
        previous = state
        cumulative = tuple(max(z[i]+cumulative[i-1]-cap[i], 0)
                           for i in range(size))
    raise AssertionError(("uncleared flux", z))


def compositions(total, slots, prefix=()):
    if slots == 1:
        yield prefix+(total,)
    else:
        for first in range(total+1):
            yield from compositions(total-first, slots-1, prefix+(first,))


def parking_checks():
    boxes = 0
    for k in range(1, 5):
        for mass in range(6):
            expected = 0 if mass == 0 else 3*min(k, mass)-1
            maximum = 0
            for z in compositions(mass, 3*k):
                t = flux_clearance(z, True)
                check(t <= expected, "all parking upper")
                maximum = max(maximum, t)
                boxes += 1
            check(maximum == expected, "all parking sharp")
            check(flux_clearance((mass,)+(0,)*(3*k-1), True) == expected,
                  "single-c-bin equality")
    print("parking_configurations="+str(boxes), flush=True)


def polynomial_trace(n):
    # Dynamic closed walks with an integer coefficient vector, no interpolation.
    result = Counter()
    for initial in range(3):
        layer = {(initial, 0): 1}
        for _ in range(n):
            following = Counter()
            for (last, degree), count in layer.items():
                for nxt in range(3):
                    if (last, nxt) != (2, 1):
                        following[nxt, degree+int((last, nxt) == (0, 1))] += count
            layer = following
        for (last, degree), count in layer.items():
            if last == initial:
                result[degree] += count
    return result


def int_trace(matrix, n):
    acc = [[int(i == j) for j in range(3)] for i in range(3)]
    for _ in range(n):
        acc = [[sum(acc[i][k]*matrix[k][j] for k in range(3))
                for j in range(3)] for i in range(3)]
    return sum(acc[i][i] for i in range(3))


def exact_box(n, lucas, bseq):
    words = [bytes(w) for w in product(range(3), repeat=n)]
    size = len(words)
    successor = array('I', (rank(forward(w)) for w in words))
    incoming = [[] for _ in words]
    for source, target in enumerate(successor):
        incoming[target].append(source)
    jumps = [successor]
    while 1 << len(jumps) <= 6*n+6:
        last = jumps[-1]
        jumps.append(array('I', (last[last[x]] for x in range(size))))

    def advance(x, t):
        bit = 0
        while t:
            if t & 1:
                x = jumps[bit][x]
            bit += 1
            t >>= 1
        return x

    # This idempotence proves in the finite box that EVERY actual cycle
    # has period dividing 3n. The fixed set is then the true recurrent set.
    projection = array('I', (advance(x, 3*n) for x in range(size)))
    check(all(projection[projection[x]] == projection[x] for x in range(size)),
          "semigroup idempotent power")
    core = bytearray(projection[x] == x for x in range(size))
    depths = Counter()
    maximum_targets = set()
    maximum = max(map(len, incoming))
    observed_poly = Counter()
    actual_core = []
    for x, w in enumerate(words):
        aflag, bflag = flags(w)
        check(bool(core[x]) == (aflag or bflag), "entire original-word core")
        if aflag:
            check(words[successor[x]] == bytes((a+1) % 3 for a in w), "C action")
        if bflag:
            check(words[successor[x]] == w[1:]+w[:1], "R action")
        if core[x]:
            depth = 0
            actual_core.append(x)
        else:
            cursor, depth = x, 0
            for bit in reversed(range(len(jumps))):
                candidate = jumps[bit][cursor]
                if not core[candidate]:
                    cursor = candidate
                    depth += 1 << bit
            check(core[successor[cursor]], "first true core entry")
            depth += 1
        depths[depth] += 1
        if depth <= 1:
            check((0 if aflag or bflag else 1) == depth, "prehistory boundary")
        else:
            twice = words[successor[successor[x]]]
            check(len(set(twice)) > 1, "no nonconstant-to-constant")
            check(2+flux_clearance(run_surplus(twice)) == depth, "exact flux entry")

        pairs = tuple(zip(w, w[1:]+w[:1]))
        allowed = (2, 1) not in pairs
        check(bool(incoming[x]) == allowed, "image iff")
        if allowed:
            # Sparse patches at exceptional coordinates, added as base-3
            # rank decrements. This constructs actual sources, not domains.
            base = rank(bytes((a-1) % 3 for a in w))
            patches = [3**(n-1-i) for i, pair in enumerate(pairs) if pair == (0, 1)]
            sources = [base]
            for decrement in patches:
                sources += [v-decrement for v in sources]
            check(len(set(sources)) == len(sources), "distinct sparse patches")
            check(set(sources) == set(incoming[x]), "full inverse source SET")
            observed_poly[len(patches)] += 1
        else:
            check(incoming[x] == [], "empty fibre")
        if len(incoming[x]) == maximum:
            maximum_targets.add(w)

    check(max(depths) == (0 if n == 1 else 2 if n == 2 else 3*(n//3)+1), "sharp H")
    check(sum(bool(v) for v in incoming) == lucas[2*n], "Lucas image")
    check(observed_poly == polynomial_trace(n), "entire weighted polynomial")
    check(sum(count * 2**degree for degree, count in observed_poly.items()) == size,
          "weighted fibre sum")
    check(maximum == 2**(n//2), "maximum fibre")
    if n == 1:
        expected_targets = {bytes([a]) for a in range(3)}
    elif n % 2 == 0:
        expected_targets = rotations(bytes([0, 1]*(n//2)))
    else:
        expected_targets = set()
        for middle in (0, 1, 2):
            initial = bytes([0, 0, 1] if middle == 0 else
                            [0, 1, 1] if middle == 1 else [0, 1, 2])
            expected_targets |= rotations(initial+bytes([0, 1]*((n-3)//2)))
    check(maximum_targets == expected_targets, "all equality targets")
    acount = 2**n+(2, 1, -1, -2, -1, 1)[n % 6]
    check(len(actual_core) == acount+bseq[n]-3*int(n % 3 == 0), "recurrent census")
    for t in range(1, 6*n+1):
        fixed = sum(advance(x, t) == x for x in actual_core)
        d = gcd(n, t)
        check(fixed == (acount if t % 3 == 0 else 0)+bseq[d]-3*int(d % 3 == 0),
              ("fixed iterate", n, t))
    print(f"n={n} states={size} image={sum(bool(v) for v in incoming)} "
          f"recurrent={len(actual_core)} H={max(depths)} max_fibre={maximum} "
          f"max_targets={len(maximum_targets)} depth_hist={sorted(depths.items())}", flush=True)
    return size


def sharp_words():
    for n in range(3, 211):
        k, r = divmod(n, 3)
        w = bytes([1]*(k+r+1)+[2]+[1, 2]*(k-1))
        expected1 = bytes([2]*(k+r+1)+[0]+[2, 0]*(k-1))
        expected2 = bytes([0]*(k+r+1)+[1]+[0, 1]*(k-1))
        check(forward(w) == expected1 and forward(expected1) == expected2,
              "uniform two-step prehistory")
        t = 0
        while not any(flags(w)):
            w = forward(w)
            t += 1
            check(t <= 3*k+1, "sharp family termination")
        check(t == 3*k+1, "sharp family first entry")
    print("sharp_witness_lengths=3..210", flush=True)


def main():
    print("P202_REVIEW_B / BYTE_WORDS_COMPOSITION_POWERS_CUMULATIVE_FLUX", flush=True)
    parking_checks()
    lucas = [2, 1]
    for _ in range(420):
        lucas.append(lucas[-1]+lucas[-2])
    bseq = [3, 0, 2]
    for j in range(3, 211):
        bseq.append(bseq[j-2]+bseq[j-3])
    for n in range(1, 61):
        check(int_trace([[0, 1, 0], [1, 0, 1], [1, 0, 0]], n) == bseq[n],
              "Q exact integer trace")
        check(int_trace([[1, 1, 0], [0, 1, 1], [1, 0, 1]], n)
              == 2**n+(2, 1, -1, -2, -1, 1)[n % 6], "A exact integer trace")
    total = sum(exact_box(n, lucas, bseq) for n in range(1, 13))
    sharp_words()
    print(f"full_word_states={total}")
    print(f"assertions={CHECKS}")
    print("status=PASS")
    print("scope=BOUNDED_INDEPENDENT_CONTROL_NOT_NOVELTY_CERTIFICATION")
    print("external_status=HOLD_EXTERNAL")


if __name__ == '__main__':
    main()
