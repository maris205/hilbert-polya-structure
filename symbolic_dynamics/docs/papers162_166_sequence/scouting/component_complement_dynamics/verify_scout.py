#!/usr/bin/env python3
"""Independent exhaustive verifier for component-complement dynamics.

No paper, scout, or repository code is imported.  Labelled simple graphs are
bit masks.  The program constructs connected components literally, builds the
complete multipartite image, and checks the functional graph, every depth
polynomial, every one-step target fibre, its extremal coefficients, and the
full weighted time-t kernel through t=6.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from math import comb


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def edge_list(n):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


@lru_cache(maxsize=None)
def partitions(n):
    """Set partitions as restricted-growth strings."""
    if n == 0:
        return ((),)
    out = []

    def visit(prefix, maximum):
        if len(prefix) == n:
            out.append(tuple(prefix))
            return
        for value in range(maximum + 2):
            prefix.append(value)
            visit(prefix, max(maximum, value))
            prefix.pop()

    visit([0], 0)
    return tuple(out)


def block_sizes(pi):
    counts = Counter(pi)
    return tuple(counts[i] for i in range(len(counts)))


def edge_count(mask):
    return mask.bit_count()


def component_partition(n, mask):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for bit, (i, j) in enumerate(edge_list(n)):
        if mask >> bit & 1:
            union(i, j)
    names = {}
    answer = []
    for vertex in range(n):
        root = find(vertex)
        if root not in names:
            names[root] = len(names)
        answer.append(names[root])
    return tuple(answer)


def complete_multipartite_mask(n, pi):
    mask = 0
    for bit, (i, j) in enumerate(edge_list(n)):
        if pi[i] != pi[j]:
            mask |= 1 << bit
    return mask


def update_literal(n, mask):
    return complete_multipartite_mask(n, component_partition(n, mask))


def connected(n, mask):
    return len(set(component_partition(n, mask))) == 1


def add_poly(left, right, scale=1):
    out = Counter(left)
    for degree, coefficient in right.items():
        out[degree] += scale * coefficient
        if out[degree] == 0:
            del out[degree]
    return +out


def mul_poly(left, right):
    out = Counter()
    for a, ca in left.items():
        for b, cb in right.items():
            out[a + b] += ca * cb
    return +out


def all_graph_poly(n):
    N = len(edge_list(n))
    return Counter({e: comb(N, e) for e in range(N + 1)})


def tree_count(s):
    return 1 if s == 1 else s ** (s - 2)


def format_poly(poly):
    if not poly:
        return "0"
    return ",".join(f"{degree}:{poly[degree]}" for degree in sorted(poly))


def expected_fibre(pi, connected_polys):
    answer = Counter({0: 1})
    for size in block_sizes(pi):
        answer = mul_poly(answer, connected_polys[size])
    return answer


def graph_box(n, connected_polys):
    edges = edge_list(n)
    N = len(edges)
    graph_count = 1 << N
    full = graph_count - 1
    masks = range(graph_count)

    components = [component_partition(n, mask) for mask in masks]
    updates = [complete_multipartite_mask(n, pi) for pi in components]
    is_connected = [len(set(pi)) == 1 for pi in components]

    conn_poly = Counter(edge_count(mask) for mask in masks
                        if is_connected[mask])
    connected_polys[n] = conn_poly
    A = all_graph_poly(n)

    # Independent connected-graph recurrence: expose the component of 0.
    recurrence = Counter(A)
    for size in range(1, n):
        term = mul_poly(connected_polys[size], all_graph_poly(n - size))
        recurrence = add_poly(recurrence, term,
                              scale=-comb(n - 1, size - 1))
    check(recurrence == conn_poly, f"connected recurrence n={n}")

    target_masks = {complete_multipartite_mask(n, pi)
                    for pi in partitions(n)}
    image = set(updates)
    check(image == target_masks, f"exact image n={n}")
    check(len(image) == len(partitions(n)), f"Bell image n={n}")

    actual_fibres = defaultdict(Counter)
    for source in masks:
        actual_fibres[updates[source]][edge_count(source)] += 1

    expected_fibres = {}
    for pi in partitions(n):
        target = complete_multipartite_mask(n, pi)
        expected = expected_fibre(pi, connected_polys)
        expected_fibres[target] = expected
        check(actual_fibres[target] == expected,
              f"one-step fibre n={n} pi={pi}")

        sizes = block_sizes(pi)
        minimum = n - len(sizes)
        minimum_coefficient = 1
        for size in sizes:
            minimum_coefficient *= tree_count(size)
        maximum = sum(comb(size, 2) for size in sizes)
        check(min(expected) == minimum,
              f"minimum degree n={n} pi={pi}")
        check(expected[minimum] == minimum_coefficient,
              f"forest coefficient n={n} pi={pi}")
        check(max(expected) == maximum,
              f"maximum degree n={n} pi={pi}")
        check(expected[maximum] == 1,
              f"clique coefficient n={n} pi={pi}")

    for target in masks:
        expected = expected_fibres.get(target, Counter())
        check(actual_fibres.get(target, Counter()) == expected,
              f"all-target zero/nonzero n={n} target={target}")

    fibre_mass = Counter()
    for poly in actual_fibres.values():
        fibre_mass = add_poly(fibre_mass, poly)
    check(fibre_mass == A, f"one-step fibre mass n={n}")

    if n == 1:
        check(updates == [0], "n=1 fixed boundary")
        depths = [0]
        expected_depth = {0: Counter({0: 1}), 1: Counter(), 2: Counter()}
        core_size = 1
    else:
        check(updates[0] == full and updates[full] == 0,
              f"core two-cycle n={n}")
        depths = []
        for source in masks:
            if source in (0, full):
                depth = 0
            elif is_connected[source]:
                depth = 1
                check(updates[source] == 0,
                      f"connected tail n={n} source={source}")
            else:
                depth = 2
                first = updates[source]
                check(source != 0, f"empty excluded n={n}")
                check(is_connected[first],
                      f"disconnected first image connected n={n}")
                check(first not in (0, full),
                      f"disconnected first image noncore n={n}")
                check(updates[first] == 0,
                      f"disconnected second image empty n={n}")
            depths.append(depth)
        expected_depth = {
            0: Counter({0: 1, N: 1}),
            1: add_poly(conn_poly, Counter({N: 1}), scale=-1),
            2: add_poly(add_poly(A, conn_poly, scale=-1),
                        Counter({0: 1}), scale=-1),
        }
        core_size = 2

    actual_depth = {d: Counter() for d in range(3)}
    for mask, depth in enumerate(depths):
        actual_depth[depth][edge_count(mask)] += 1
    for depth in range(3):
        check(actual_depth[depth] == expected_depth[depth],
              f"depth polynomial n={n} depth={depth}")

    if n == 2:
        check(max(depths) == 0, "n=2 height zero")
    if n >= 3:
        check(max(depths) == 2, f"sharp height n={n}")
        witness = 1  # the edge (0,1), all remaining vertices isolated
        check(depths[witness] == 2, f"depth-two witness n={n}")

    # Every weighted time-t fibre through t=6.
    for t in range(1, 7):
        actual = defaultdict(Counter)
        for source in masks:
            target = source
            for _ in range(t):
                target = updates[target]
            actual[target][edge_count(source)] += 1

        if t == 1:
            check(dict(actual) == dict(actual_fibres),
                  f"time-one kernel n={n}")
            continue

        if n == 1:
            expected = {0: Counter({0: 1})}
        else:
            disconnected_poly = add_poly(A, conn_poly, scale=-1)
            if t % 2 == 0:
                expected = {0: disconnected_poly, full: conn_poly}
            else:
                expected = {0: conn_poly, full: disconnected_poly}
        check(dict(actual) == expected, f"time kernel n={n} t={t}")
        check(set(actual) == set(expected), f"time support n={n} t={t}")

    # Every source obeys the class/parity endpoint rule at larger times.
    for source in masks:
        for t in range(2, 7):
            target = source
            for _ in range(t):
                target = updates[target]
            if n == 1:
                expected_target = 0
            elif is_connected[source]:
                expected_target = full if t % 2 == 0 else 0
            else:
                expected_target = 0 if t % 2 == 0 else full
            check(target == expected_target,
                  f"class parity n={n} source={source} t={t}")

    depth_sizes = tuple(sum(actual_depth[d].values()) for d in range(3))
    return (f"BOX n={n} graphs={graph_count} image={len(image)} "
            f"Bell={len(partitions(n))} core={core_size} "
            f"depths={depth_sizes[0]}/{depth_sizes[1]}/{depth_sizes[2]} "
            f"Conn={format_poly(conn_poly)}")


def main():
    print("CCD INDEPENDENT EXACT AUDIT")
    print("domain labelled simple graphs n>=1; HOLD_EXTERNAL")
    connected_polys = {0: Counter({0: 1})}
    for n in range(1, 7):
        print(graph_box(n, connected_polys))
    print("BOUNDARY n=1 empty=K1 and is fixed")
    print("BOUNDARY n=2 only empty/K2 two-cycle; height=0")
    print("SHARP n>=3 height=2")
    print("TIME t>=2 support={empty,K_n}; parity formulas checked t=2..6")
    print(f"graphs_exhausted={sum(1 << comb(n,2) for n in range(1,7))}")
    print(f"assertions={ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
