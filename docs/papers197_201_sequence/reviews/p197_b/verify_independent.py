#!/usr/bin/env python3
"""Review B: radix-3 truth table, binary-lift graph, extremal-level inverse.

No author or Review-A source code is read, copied, or imported. Characteristic
polynomial uses SCC factorization and exact Bareiss evaluations, not Newton
or Berkowitz. All operations use the Python standard library.
"""
from array import array
from collections import Counter
from itertools import product
from math import comb, gcd

CHECKS = 0
# Entry indexed by lower-place digit plus three times the next digit.
PAIR = (1, 0, 0, 2, 1, 0, 2, 2, 1)


def check(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)


def word(code, n):
    out = []
    for _ in range(n):
        code, digit = divmod(code, 3)
        out.append(digit - 1)
    return out


def encode(w):
    return sum((v + 1) * 3 ** i for i, v in enumerate(w))


def step(code, n):
    first, current, place, answer = code % 3, code, 1, 0
    for i in range(n):
        current, a = divmod(current, 3)
        b = current % 3 if i + 1 < n else first
        answer += PAIR[a + 3 * b] * place
        place *= 3
    return answer


def shift(code, n, distance=2):
    distance %= n
    scale = 3 ** distance
    return code // scale + (code % scale) * 3 ** (n - distance)


def open_output(w):
    # Comparison sorting, not the radix-3 local lookup.
    w = list(w)
    while len(w) > 1:
        w = [0 if a == b else (1 if sorted((a, b))[0] == a else -1)
             for a, b in zip(w, w[1:])]
    return w[0]


def fib(k):
    # Count monomer-dimer tilings, independent of a Fibonacci update loop.
    if k == 0:
        return 0
    return sum(comb(k - 1 - j, j) for j in range((k - 1) // 2 + 1))


def lucas(k):
    return 2 if k == 0 else fib(k - 1) + fib(k + 1)


def gap_prediction(w):
    skeleton = [v for v in w if v]
    r = len(skeleton)
    if r == 0:
        return 3
    if min(skeleton) == max(skeleton):
        return 0
    cut = next(i for i in range(r) if skeleton[i] != skeleton[i - 1])
    s = skeleton[cut:] + skeleton[:cut]
    runs, previous = [], None
    for v in s:
        if v == previous:
            runs[-1] += 1
        else:
            runs.append(1)
        previous = v
    if max(runs) >= 3:
        return 0
    double = [i for i, length in enumerate(runs) if length == 2]
    if not double:
        return lucas(r)
    check((len(double) - r) % 2 == 0, "gap parity")
    value = 1
    for a, b in zip(double, double[1:] + [double[0] + len(runs)]):
        value *= fib(b - a)
    return value


def level_inverse(target):
    """Equality quotient; low levels among sources, high among sinks.

    All remaining vertices have middle level and must be edge-independent.
    This reconstructs labelled sources, without transfer matrices or traces.
    """
    n = len(target)
    parent = list(range(n))

    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for i, s in enumerate(target):
        if s == 0:
            parent[root(i)] = root((i + 1) % n)
    labels = sorted({root(i) for i in range(n)})
    quotient = [labels.index(root(i)) for i in range(n)]
    m = len(labels)
    edges = set()
    for i, s in enumerate(target):
        if s:
            a, b = quotient[i], quotient[(i + 1) % n]
            if a == b:
                return set()
            edges.add((a, b) if s == 1 else (b, a))
    sources = [i for i in range(m) if all(b != i for a, b in edges)]
    sinks = [i for i in range(m) if all(a != i for a, b in edges)]
    result = set()
    for low_bits in range(1 << len(sources)):
        low = {v for j, v in enumerate(sources) if low_bits >> j & 1}
        available = [v for v in sinks if v not in low]
        for high_bits in range(1 << len(available)):
            high = {v for j, v in enumerate(available) if high_bits >> j & 1}
            middle = set(range(m)) - low - high
            if any(a in middle and b in middle for a, b in edges):
                continue
            values = [-1 if i in low else (1 if i in high else 0)
                      for i in range(m)]
            result.add(encode([values[i] for i in quotient]))
    return result


def lift_apply(powers, vertex, exponent):
    bit = 0
    while exponent:
        if exponent & 1:
            vertex = powers[bit][vertex]
        exponent >>= 1
        bit += 1
    return vertex


def run_length(w):
    if min(w) == max(w):
        return len(w)
    best = current = 1
    for a, b in zip(w + w, (w + w)[1:]):
        current = current + 1 if a == b else 1
        best = max(best, current)
    return min(len(w), best)


def desired_maximizers(n):
    if n == 1:
        return {1}
    output = set()
    for s in (-1, 1):
        if n % 2 == 0:
            output.add(encode([s * (-1) ** i for i in range(n)]))
        else:
            for zero in range(n):
                out, j = [], 0
                for i in range(n):
                    if i == zero:
                        out.append(0)
                    else:
                        out.append(s * (-1) ** j)
                        j += 1
                output.add(encode(out))
    if n in (2, 3):
        output.add((3 ** n - 1) // 2)
    return output


def graph_box(n):
    size = 3 ** n
    successor = array('I', (step(i, n) for i in range(size)))
    powers = [successor]
    for _ in range(max(size, 4 * n).bit_length()):
        old = powers[-1]
        powers.append(array('I', (old[old[i]] for i in range(size))))
    # For ANY size-state map, its size-th image is exactly its periodic set.
    recurrent = {lift_apply(powers, i, size) for i in range(size)}
    check({successor[i] for i in recurrent} == recurrent, "stable eventual image")
    depth = array('H', [0]) * size
    for i in range(size):
        if i in recurrent:
            continue
        at, distance = i, 0
        for j in range(len(powers) - 1, -1, -1):
            after = powers[j][at]
            if after not in recurrent:
                at, distance = after, distance + (1 << j)
        check(successor[at] in recurrent, "first entrance after lifted prefix")
        depth[i] = distance + 1
    fibres = array('I', [0]) * size
    incoming = {} if n <= 6 else None
    for source, target in enumerate(successor):
        fibres[target] += 1
        if incoming is not None:
            incoming.setdefault(target, set()).add(source)
    period_bound = 4 * n // gcd(n, 2)
    divisors = [d for d in range(1, period_bound + 1) if period_bound % d == 0]
    period_count = Counter()
    for i in recurrent:
        check(lift_apply(powers, i, period_bound) == i, "period divisibility bound")
        p = next(d for d in divisors if lift_apply(powers, i, d) == i)
        period_count[p] += 1
    check(all(count % p == 0 for p, count in period_count.items()), "cycle census integrality")
    for i in range(size):
        w = word(i, n)
        check((i in recurrent) == (powers[2][i] == shift(i, n)), "fourth root core iff")
        check(depth[i] == 0 or depth[successor[i]] == depth[i] - 1, "pointwise first entrance")
        if min(w) != max(w):
            check(depth[i] <= run_length(w), "constant-interval bound")
        else:
            check(depth[i] <= 1, "constant boundary")
        check(fibres[i] == gap_prediction(w), "every target including zero fibre")
        if incoming is not None:
            check(level_inverse(w) == incoming.get(i, set()), "exact low-middle-high inverse sources")
    greatest = max(fibres)
    maximizers = {i for i, value in enumerate(fibres) if value == greatest}
    check(greatest == (3 if n == 1 else lucas(2 * (n // 2))), "sharp Lucas maximum")
    check(maximizers == desired_maximizers(n), "all equality targets")
    expected_tail = 1 if n == 1 else n - 1 if n % 2 == 0 else n - 2
    check(max(depth) == expected_tail, "parity sharp global tail")
    check(sum(fibres) == size, "mass all targets")
    print(f"n={n} sources={size} targets={size} image={sum(bool(a) for a in fibres)} "
          f"recurrent={len(recurrent)} max_tail={max(depth)} max_fibre={greatest} "
          f"maximizers={len(maximizers)} depths={sorted(Counter(depth).items())} "
          f"cycles={[(p, c // p) for p, c in sorted(period_count.items())]}")
    return Counter(depth), period_count


def local_certificates():
    totals = []
    for length, cap in ((6, 1), (7, 2)):
        count = 0
        for w in product((-1, 0, 1), repeat=length):
            if any(len(set(w[i:i + cap + 1])) == 1 for i in range(length - cap)):
                continue
            check(open_output(w) == open_output(w[2:length - 2]), "complete local certificate")
            count += 1
        totals.append(count)
    check(totals == [96, 1344], "local domain sizes")
    table = [((-1,-1,0),4,48,1),((-1,-1,1),4,48,1),
             ((-1,0,-1),2,64,-1),((-1,0,0),4,48,-1),
             ((-1,0,1),2,64,0),((-1,1,-1),2,64,-1),
             ((-1,1,0),4,64,-1),((0,-1,0),2,64,1)]
    cover = set()
    for middle, orbit_size, extensions, result in table:
        orbit = {middle, tuple(reversed(middle)), tuple(-v for v in middle),
                 tuple(-v for v in reversed(middle))}
        check(len(orbit) == orbit_size and not (orbit & cover), "certificate symmetry orbit")
        cover |= orbit
        count = 0
        for outer in product((-1,0,1), repeat=4):
            w = outer[:2] + middle + outer[2:]
            if any(w[i] == w[i+1] == w[i+2] for i in range(5)):
                continue
            check(open_output(w) == result, "table row result")
            count += 1
        check(count == extensions, "table row extensions")
    check(len(cover) == 24, "all nonconstant middle triples")
    print("local_certificates=96,1344 full_unreduced_domains_and_eight_table_rows PASS")


def overlap_graph(length, constraint):
    size = 3 ** length
    adjacency = [[] for _ in range(size)]
    for i in range(size):
        w = word(i, length)
        for v in (-1, 0, 1):
            if constraint(w + [v]):
                adjacency[i].append(i // 3 + (v + 1) * 3 ** (length - 1))
    return adjacency


def trace_powers(adjacency, limit):
    matrix = [{i: 1} for i in range(len(adjacency))]
    traces = []
    for _ in range(limit):
        next_matrix = []
        for row in matrix:
            out = {}
            for i, value in row.items():
                for j in adjacency[i]:
                    out[j] = out.get(j, 0) + value
            next_matrix.append(out)
        matrix = next_matrix
        traces.append(sum(row.get(i, 0) for i, row in enumerate(matrix)))
    return traces


def bareiss(matrix):
    a = [list(row) for row in matrix]
    size, previous, parity = len(a), 1, 1
    for k in range(size - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, size) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            parity = -parity
        pivot = a[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                value, remainder = divmod(numerator, previous)
                check(remainder == 0, "Bareiss exact division")
                a[i][j] = value
            a[i][k] = 0
        previous = pivot
    return parity * a[-1][-1]


def determinant_certificate(adjacency):
    size = len(adjacency)
    reach = [{i} | set(row) for i, row in enumerate(adjacency)]
    for k in range(size):
        for i in range(size):
            if k in reach[i]:
                reach[i] |= reach[k]
    remaining, components = set(range(size)), []
    while remaining:
        i = min(remaining)
        component = sorted(j for j in remaining if j in reach[i] and i in reach[j])
        components.append(component)
        remaining -= set(component)
    giant = [c for c in components if len(c) > 1]
    check(len(giant) == 1 and len(giant[0]) == 38, "SCC nontrivial factor")
    singles = [c[0] for c in components if len(c) == 1]
    check(len(singles) == 43 and sum(i in adjacency[i] for i in singles) == 1,
          "42 zero factors and one z-1 factor")
    vertices = giant[0]
    for z in range(39):
        matrix = [[(z if i == j else 0) - int(j in adjacency[i])
                   for j in vertices] for i in vertices]
        expected = z ** 32 * (z ** 3 - z*z - 2*z - 1) * (z ** 3 + z*z + 2*z + 1)
        check(bareiss(matrix) == expected, "39-point exact degree-38 identity")
    check(sum(map(len, components)) == 81 and sum(map(len, adjacency)) == 165,
          "full matrix dimension and edge count")
    print("A0_charpoly=SCC_42_transient_singletons+one_loop+38_block; "
          "Bareiss_at_39_distinct_integers PASS_FULL_DEGREE_81_IDENTITY")


def traces_and_witnesses(boxes):
    for t in range(3):
        adjacency = overlap_graph(t + 4, lambda w, t=t:
                                  open_output(w) == open_output(w[2:t+3]))
        traces = trace_powers(adjacency, 6)
        for n, value in enumerate(traces, 1):
            check(value == sum(c for depth, c in boxes[n][0].items() if depth <= t),
                  "de Bruijn CDF trace, including repeated windows")
        if t == 0:
            determinant_certificate(adjacency)
        print(f"CDF_trace_t={t} n=1..6 values={traces}")
    for p in range(1, 5):
        adjacency = overlap_graph(p, lambda w: open_output(w) == w[0])
        traces = trace_powers(adjacency, 8)
        for n, value in enumerate(traces, 1):
            check(value == sum(c for period, c in boxes[n][1].items() if p % period == 0),
                  "iterate-fixed trace")
        print(f"fixed_trace_p={p} n=1..8 values={traces}")
    witnesses = 0
    for n in range(2, 81):
        current = encode([0] * (n - 1) + [1])
        tail = 0
        while True:
            fourth = current
            for _ in range(4):
                fourth = step(fourth, n)
            if fourth == shift(current, n):
                break
            current = step(current, n)
            tail += 1
            check(tail <= n, "witness enters bounded core")
        check(tail == (n - 1 if n % 2 == 0 else n - 2), "large sharp witness")
        witnesses += 1
    print(f"sharp_witnesses={witnesses} n=2..80 integer_local_map PASS")


def main():
    print("P197_REVIEW_B_RADIX3_BINARY_LIFT_EXTREMAL_LEVEL_INVERSE_BAREISS")
    print("author_and_A_code_read_or_imported=none; full_graph_n<=12; full_inverse_sets_n<=6")
    local_certificates()
    boxes = {n: graph_box(n) for n in range(1, 13)}
    traces_and_witnesses(boxes)
    print(f"assertions={CHECKS}")
    print("PASS_BOUNDED_INDEPENDENT_REVIEW_B; NO_NOVELTY_CERTIFICATION")


if __name__ == '__main__':
    main()
