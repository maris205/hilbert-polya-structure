#!/usr/bin/env python3
"""Independent exact controls for P166 open discovery Round 8.

The six maps are implemented directly from the literal definitions in the
Round-8 scout.  No earlier scout or author module is imported.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import comb, factorial


ASSERTIONS = 0


def check(condition: bool, message: str = "assertion failed") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def functional_stats(states, update):
    indegree = Counter(update(x) for x in states)
    tails = Counter()
    periods = Counter()
    for x in states:
        seen = {}
        y = x
        step = 0
        while y not in seen:
            seen[y] = step
            y = update(y)
            step += 1
        tails[seen[y]] += 1
        periods[step - seen[y]] += 1
    return {
        "states": len(states),
        "image": len(indegree),
        "max_tail": max(tails),
        "max_period": max(periods),
        "tail_hist": tuple(sorted(tails.items())),
        "period_hist": tuple(sorted(periods.items())),
        "max_fibre": max(indegree.values()),
        "indegree": indegree,
    }


# ---------------------------------------------------------------------------
# BFR: cyclic Tits refinement on faces of the braid arrangement


def ordered_partitions(n: int):
    out = []
    for k in range(1, n + 1):
        out.extend(
            word
            for word in product(range(k), repeat=n)
            if set(word) == set(range(k))
        )
    return out


def rotate_labels(face, power=1):
    n = len(face)
    power %= n
    out = [0] * n
    for i, block in enumerate(face):
        out[(i + power) % n] = block
    return tuple(out)


def tits_product(left, right):
    pairs = list(zip(left, right))
    ranks = {pair: i for i, pair in enumerate(sorted(set(pairs)))}
    return tuple(ranks[pair] for pair in pairs)


def bfr(face):
    return tits_product(face, rotate_labels(face))


def bfr_closed(face, time):
    out = face
    for j in range(1, time + 1):
        out = tits_product(out, rotate_labels(face, j))
    return out


def run_bfr():
    rows = []
    for n in range(2, 8):
        states = ordered_partitions(n)
        for face in states:
            y = face
            for time in range(0, n + 2):
                check(y == bfr_closed(face, time), f"BFR iterate n={n} t={time}")
                y = bfr(y)
        stats = functional_stats(states, bfr)
        expected_fixed = sum(factorial(d) for d in range(1, n + 1) if n % d == 0)
        fixed = sum(bfr(x) == x for x in states)
        check(fixed == expected_fixed, f"BFR fixed count n={n}")
        check(stats["max_tail"] == n - 2, f"BFR sharp tail n={n}")
        check(stats["max_period"] == 1, f"BFR recurrent core n={n}")
        for face in states:
            check(bfr_closed(face, n - 2) == bfr_closed(face, n - 1))
        rows.append(
            (n, len(states), stats["image"], fixed, stats["max_tail"], stats["max_fibre"])
        )
    return rows


# ---------------------------------------------------------------------------
# QDP: delete every arrow of an ordered DAG admitting an alternate path


def dag_edges(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def adjacency(mask, n):
    adj = [[False] * n for _ in range(n)]
    for bit, (i, j) in enumerate(dag_edges(n)):
        adj[i][j] = bool((mask >> bit) & 1)
    return adj


def closure_of(mask, n):
    reach = adjacency(mask, n)
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return reach


def qdp(mask, n):
    edges = dag_edges(n)
    adj = adjacency(mask, n)
    reach = closure_of(mask, n)
    out = mask
    for bit, (i, j) in enumerate(edges):
        if adj[i][j] and any(adj[i][k] and reach[k][j] for k in range(n)):
            out &= ~(1 << bit)
    return out


def matrix_key(matrix):
    return tuple(tuple(int(x) for x in row) for row in matrix)


def run_qdp():
    rows = []
    for n in range(2, 7):
        states = list(range(1 << (n * (n - 1) // 2)))
        indegree = Counter()
        for mask in states:
            target = qdp(mask, n)
            indegree[target] += 1
            check(qdp(target, n) == target, f"QDP idempotence n={n}")
            check(
                matrix_key(closure_of(mask, n)) == matrix_key(closure_of(target, n)),
                f"QDP reachability n={n}",
            )
        for target, count in indegree.items():
            reach = closure_of(target, n)
            closure_edges = sum(reach[i][j] for i in range(n) for j in range(i + 1, n))
            edge_count = target.bit_count()
            check(count == 2 ** (closure_edges - edge_count), f"QDP fibre n={n}")
        check(sum(indegree.values()) == len(states), f"QDP mass n={n}")
        rows.append(
            (
                n,
                len(states),
                len(indegree),
                max(indegree.values()),
                tuple(sorted(Counter(indegree.values()).items())),
            )
        )
    return rows


# ---------------------------------------------------------------------------
# QTF: toggle an arrow iff it has exactly one two-arrow factorization


def qtf(mask, n):
    edges = dag_edges(n)
    positions = {edge: bit for bit, edge in enumerate(edges)}
    out = mask
    for bit, (i, j) in enumerate(edges):
        factorizations = sum(
            bool((mask >> positions[i, k]) & 1) and bool((mask >> positions[k, j]) & 1)
            for k in range(i + 1, j)
        )
        if factorizations == 1:
            out ^= 1 << bit
    return out


def run_qtf():
    rows = []
    expected_period = {2: 1, 3: 2, 4: 2, 5: 4, 6: 8}
    for n in range(2, 7):
        states = list(range(1 << (n * (n - 1) // 2)))
        stats = functional_stats(states, lambda mask: qtf(mask, n))
        check(stats["image"] == len(states), f"QTF bijection n={n}")
        check(stats["max_tail"] == 0, f"QTF no transient n={n}")
        check(stats["max_period"] == expected_period[n], f"QTF pilot period n={n}")
        for mask in states:
            target = qtf(mask, n)
            # Every edge of span one is frozen; the map is triangular by span.
            for bit, (i, j) in enumerate(dag_edges(n)):
                if j == i + 1:
                    check(((mask ^ target) >> bit) & 1 == 0, f"QTF atom edge n={n}")
        rows.append(
            (
                n,
                len(states),
                stats["max_period"],
                stats["period_hist"],
            )
        )
    return rows


# ---------------------------------------------------------------------------
# BLM: clockwise transfer from every strict cyclic local maximum in a bargraph


def weak_compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for first in range(total + 1):
        yield from weak_compositions(total - first, parts - 1, prefix + (first,))


def blm(heights):
    m = len(heights)
    delta = [0] * m
    for i in range(m):
        if heights[i] > heights[i - 1] and heights[i] > heights[(i + 1) % m]:
            delta[i] -= 1
            delta[(i + 1) % m] += 1
    return tuple(heights[i] + delta[i] for i in range(m))


def run_blm():
    rows = []
    for m in range(3, 7):
        for total in (m, 2 * m, 3 * m):
            states = list(weak_compositions(total, m))
            for heights in states:
                target = blm(heights)
                check(sum(target) == total, f"BLM mass m={m} N={total}")
                check(min(target) >= 0, f"BLM positivity m={m} N={total}")
                check(sum(x * x for x in target) <= sum(x * x for x in heights), "BLM energy")
                no_strict_peak = all(
                    not (heights[i] > heights[i - 1] and heights[i] > heights[(i + 1) % m])
                    for i in range(m)
                )
                check((target == heights) == no_strict_peak, "BLM fixed criterion")
            stats = functional_stats(states, blm)
            check(stats["max_period"] == 1, f"BLM pilot recurrence m={m} N={total}")
            rows.append(
                (
                    m,
                    total,
                    len(states),
                    stats["image"],
                    stats["tail_hist"][0][1],
                    stats["max_tail"],
                    stats["max_fibre"],
                )
            )
    return rows


# ---------------------------------------------------------------------------
# DWS: span of the codewords whose Hamming weight is divisible by three


def binary_span(generators):
    result = {0}
    for generator in generators:
        old = list(result)
        result.update(x ^ generator for x in old)
    return frozenset(result)


def binary_subspaces(n):
    seen = {frozenset({0})}
    todo = [frozenset({0})]
    while todo:
        space = todo.pop()
        for vector in range(1 << n):
            if vector not in space:
                extension = binary_span(tuple(space) + (vector,))
                if extension not in seen:
                    seen.add(extension)
                    todo.append(extension)
    return sorted(seen, key=lambda space: (len(space), tuple(sorted(space))))


def dws(code):
    return binary_span(x for x in code if x.bit_count() % 3 == 0)


def run_dws():
    rows = []
    for n in range(1, 7):
        states = binary_subspaces(n)
        indegree = Counter()
        for code in states:
            target = dws(code)
            indegree[target] += 1
            check(target <= code, f"DWS descent n={n}")
            check(dws(target) == target, f"DWS projection n={n}")
            selected = [x for x in code if x.bit_count() % 3 == 0]
            check(binary_span(selected) == target, f"DWS literal n={n}")
        fixed = sum(dws(code) == code for code in states)
        check(fixed == len(indegree), f"DWS image=fixed n={n}")
        rows.append((n, len(states), fixed, max(indegree.values())))
    return rows


# ---------------------------------------------------------------------------
# MIP: each symbol points to its least preimage, with itself as empty default


def mip(function):
    n = len(function)
    preimages = [[] for _ in range(n)]
    for position, value in enumerate(function):
        preimages[value].append(position)
    return tuple(min(preimages[value]) if preimages[value] else value for value in range(n))


def mip_target_fibre_formula(target):
    """Count words with the prescribed first-occurrence/default vector."""
    n = len(target)
    moving = {symbol for symbol in range(n) if target[symbol] != symbol}
    forced_positions = [target[symbol] for symbol in moving]
    if len(set(forced_positions)) != len(forced_positions):
        return 0
    fixed_available = [
        symbol
        for symbol in range(n)
        if target[symbol] == symbol and symbol not in forced_positions
    ]
    total = 0
    # A fixed coordinate can mean either first occurrence at itself or absence.
    for choose_mask in range(1 << len(fixed_available)):
        present_fixed = {
            fixed_available[j]
            for j in range(len(fixed_available))
            if (choose_mask >> j) & 1
        }
        first = {symbol: target[symbol] for symbol in moving}
        first.update({symbol: symbol for symbol in present_fixed})
        if len(set(first.values())) != len(first):
            continue
        contribution = 1
        occupied = set(first.values())
        for position in range(n):
            if position in occupied:
                continue
            available = sum(first_position < position for first_position in first.values())
            contribution *= available
        total += contribution
    return total


def involution_count(n):
    values = [1, 1]
    for size in range(2, n + 1):
        values.append(values[-1] + (size - 1) * values[-2])
    return values[n]


def bell_count(n):
    values = [1]
    for size in range(n):
        values.append(sum(comb(size, k) * values[k] for k in range(size + 1)))
    return values[n]


def mip_recurrent_count(n):
    """Labelled SET recurrence from cycles and admissible rooted paths."""
    values = [1]
    for size in range(1, n + 1):
        total = 0
        for component_size in range(1, size + 1):
            if component_size == 1:
                components = 1
            elif component_size == 2:
                components = 1  # the directed 2-cycle
            elif component_size == 3:
                components = factorial(2) + 2
            else:
                components = factorial(component_size - 1) + factorial(component_size) // 4
            total += comb(size - 1, component_size - 1) * components * values[size - component_size]
        values.append(total)
    return values[n]


def run_mip():
    rows = []
    for n in range(1, 8):
        states = list(product(range(n), repeat=n))
        stats = functional_stats(states, mip)
        for target in stats["indegree"]:
            moving_values = [target[i] for i in range(n) if target[i] != i]
            check(len(moving_values) == len(set(moving_values)), f"MIP image structure n={n}")
        for target, count in stats["indegree"].items():
            check(count == mip_target_fibre_formula(target), f"MIP fibre n={n}")
        if n <= 6:
            for target in states:
                check(
                    stats["indegree"].get(target, 0) == mip_target_fibre_formula(target),
                    f"MIP unsupported target n={n}",
                )
        check(sum(stats["indegree"].values()) == n ** n, f"MIP mass n={n}")
        check(stats["max_tail"] == 2 * n - 2, f"MIP pilot sharp tail n={n}")
        check(stats["max_period"] <= 2, f"MIP pilot period n={n}")
        recurrent = stats["tail_hist"][0][1]
        fixed = sum(mip(state) == state for state in states)
        check(recurrent == mip_recurrent_count(n), f"MIP recurrent EGF n={n}")
        check(fixed == involution_count(n), f"MIP fixed/involutions n={n}")
        identity = tuple(range(n))
        check(stats["indegree"][identity] == mip_target_fibre_formula(identity), "MIP identity fibre")
        check(stats["indegree"][identity] == bell_count(n), "MIP Bell sentinel")
        witness = tuple(range(1, n)) + ((1,) if n >= 2 else (0,))
        y = witness
        for _ in range(2 * n - 2):
            y = mip(y)
        check(mip(mip(y)) == y, f"MIP explicit deepest witness n={n}")
        rows.append(
            (
                n,
                len(states),
                stats["image"],
                recurrent,
                fixed,
                stats["max_tail"],
                stats["max_period"],
                stats["max_fibre"],
            )
        )
    return rows


def main():
    bfr_rows = run_bfr()
    qdp_rows = run_qdp()
    qtf_rows = run_qtf()
    blm_rows = run_blm()
    dws_rows = run_dws()
    mip_rows = run_mip()

    print("ROUND8_INDEPENDENT_EXACT_SCOUT")
    print("BFR rows (n,states,image,fixed,max_tail,max_fibre)")
    for row in bfr_rows:
        print("BFR", *row)
    print("QDP rows (n,states,image,max_fibre,fibre_spectrum)")
    for row in qdp_rows:
        print("QDP", *row)
    print("QTF rows (n,states,max_period,period_hist)")
    for row in qtf_rows:
        print("QTF", *row)
    print("BLM rows (m,N,states,image,fixed,max_tail,max_fibre)")
    for row in blm_rows:
        print("BLM", *row)
    print("DWS rows (n,states,fixed,max_fibre)")
    for row in dws_rows:
        print("DWS", *row)
    print("MIP rows (n,states,image,recurrent,fixed,max_tail,max_period,max_fibre)")
    for row in mip_rows:
        print("MIP", *row)
    print("ASSERTIONS", ASSERTIONS)
    print("VERDICT GREEN_OWNER_THIN_MIP")
    print("LIFECYCLE HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
