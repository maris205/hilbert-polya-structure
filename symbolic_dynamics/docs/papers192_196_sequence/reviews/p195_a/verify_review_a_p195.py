#!/usr/bin/env python3
"""Process-separated Review-A falsifier for P195.

No paper-local module is imported.  Trees are decoded independently, every
root map is rebuilt from edge-deletion searches, and the recurrent EGF is
also checked through a direct weighted-side census.
"""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from heapq import heapify, heappop, heappush
from itertools import product
from math import comb, factorial
from pathlib import Path


CHECKS = 0


def check(statement, message):
    global CHECKS
    CHECKS += 1
    if not statement:
        raise AssertionError(message)


def labelled_trees(n):
    if n == 1:
        yield ((),)
        return
    for code in product(range(n), repeat=n - 2):
        degree = [1] * n
        for value in code:
            degree[value] += 1
        leaves = [v for v in range(n) if degree[v] == 1]
        heapify(leaves)
        edges = []
        for value in code:
            leaf = heappop(leaves)
            edges.append((leaf, value))
            degree[leaf] -= 1
            degree[value] -= 1
            if degree[value] == 1:
                heappush(leaves, value)
        a = heappop(leaves)
        b = heappop(leaves)
        edges.append((a, b))
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        yield tuple(tuple(sorted(row)) for row in graph)


def side_order(graph, blocked, start):
    seen = {blocked}
    stack = [start]
    total = 0
    while stack:
        v = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        total += 1
        stack.extend(graph[v])
    return total


def all_sides(graph):
    return {(u, v): side_order(graph, u, v)
            for u in range(len(graph)) for v in graph[u]}


def map_roots(graph, side):
    out = []
    for u in range(len(graph)):
        eligible = [v for v in graph[u] if side[u, v] % 2]
        out.append(min(eligible) if eligible else u)
    return tuple(out)


def orbit(function, root):
    index = {}
    state = root
    while state not in index:
        index[state] = len(index)
        state = function[state]
    return index[state], len(index) - index[state]


def predicted_indegree(graph, side, target):
    total = int(all(side[target, v] % 2 == 0 for v in graph[target]))
    for source in graph[target]:
        eligible = [v for v in graph[source] if side[source, v] % 2]
        if target in eligible and target == min(eligible):
            total += 1
    return total


def poly_multiply(a, b, limit):
    out = [Fraction(0) for _ in range(limit + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= limit:
                out[i + j] += x * y
    return out


def poly_exp(f, limit):
    out = [Fraction(0) for _ in range(limit + 1)]
    out[0] = Fraction(1)
    for n in range(1, limit + 1):
        out[n] = sum(k * f[k] * out[n - k] for k in range(1, n + 1)) / n
    return out


def theoretical_series(limit):
    rooted = [Fraction(0) for _ in range(limit + 1)]
    for n in range(1, limit + 1):
        rooted[n] = Fraction(n ** (n - 1), factorial(n))
    odd = [rooted[n] if n % 2 else Fraction(0) for n in range(limit + 1)]
    even = [rooted[n] if n % 2 == 0 else Fraction(0) for n in range(limit + 1)]
    exp_even = poly_exp(even, limit)

    weighted_odd_sets = [Fraction(0) for _ in range(limit + 1)]
    power = [Fraction(0) for _ in range(limit + 1)]
    power[0] = Fraction(1)
    for k in range(limit + 1):
        for j in range(limit + 1):
            weighted_odd_sets[j] += power[j] / factorial(k + 1)
        power = poly_multiply(power, odd, limit)
    base = poly_multiply(exp_even, weighted_odd_sets, limit)
    w = [Fraction(0)] + base[:-1]
    fixed = [Fraction(0)] + exp_even[:-1]
    w_odd = [w[n] if n % 2 else Fraction(0) for n in range(limit + 1)]
    recurrent = poly_multiply(w_odd, w_odd, limit)
    return fixed, w, recurrent


def h_components(graph, side):
    h = [tuple(v for v in graph[u] if side[u, v] % 2) for u in range(len(graph))]
    comps = []
    unseen = set(range(len(graph)))
    while unseen:
        start = min(unseen)
        stack = [start]
        comp = set()
        while stack:
            u = stack.pop()
            if u in comp:
                continue
            comp.add(u)
            unseen.discard(u)
            stack.extend(h[u])
        comps.append((comp, h))
    return comps


def edge_text(graph):
    return ",".join(f"{u + 1}-{v + 1}" for u, row in enumerate(graph)
                    for v in row if u < v)


def main():
    limit = 8
    workspace = Path(__file__).resolve().parents[4]
    paper = workspace / "papers/195-odd-side-least-neighbor-trees"
    manuscript = (paper / "main.tex").read_text(encoding="utf-8")
    source_ledger = (paper / "SOURCE_VERIFICATION.md").read_text(encoding="utf-8")
    check("P123" in manuscript and "P159" in manuscript,
          "P195-A1 manuscript subtraction missing")
    check("P123" in source_ledger and "P159" in source_ledger,
          "P195-A1 source-ledger subtraction missing")
    check("zeta conversion" in manuscript and "no separation" in manuscript,
          "P195-A1 zero-credit boundary missing")
    check(manuscript.count("OWNER\\_AMBER/HOLD\\_EXTERNAL") >= 2,
          "P195-A2 dual release gate missing")
    fixed_series, w_series, recurrent_series = theoretical_series(limit)
    records = []
    digest = sha256()
    transitions = 0
    weighted_side_totals = [Fraction(0) for _ in range(limit + 1)]
    first_multi = None

    for n in range(1, limit + 1):
        trees = 0
        depths = Counter()
        periods = Counter()
        recurrent = 0
        fixed = 0
        maximum_fibre = 0
        for graph in labelled_trees(n):
            trees += 1
            side = all_sides(graph)
            function = map_roots(graph, side)
            direct_fibres = Counter(function)
            transitions += n
            digest.update(f"{n}:{edge_text(graph)}:{function}\n".encode("ascii"))

            for u in range(n):
                odd_branches = sum(side[u, v] % 2 for v in graph[u])
                weighted_side_totals[n] += Fraction(1, odd_branches + 1)
                if n % 2 == 0:
                    check(odd_branches % 2 == 1, "even-order H degree is not odd")
                    expected = min(v for v in graph[u] if side[u, v] % 2)
                    check(function[u] == expected, "not the least H-neighbour")
                else:
                    check(all((side[u, v] % 2) != (side[v, u] % 2)
                              for v in graph[u]), "odd-order edge orientation failure")

                depth, period = orbit(function, u)
                depths[depth] += 1
                periods[period] += 1
                recurrent += depth == 0
                fixed += function[u] == u
                check(direct_fibres[u] == predicted_indegree(graph, side, u),
                      "local inverse atlas failure")
                maximum_fibre = max(maximum_fibre, direct_fibres[u])

            if n % 2 == 0:
                for comp, h in h_components(graph, side):
                    mutual = [(u, function[u]) for u in sorted(comp)
                              if u < function[u] and function[function[u]] == u]
                    if len(mutual) >= 2 and first_multi is None:
                        first_multi = (n, edge_text(graph),
                                       tuple((u + 1, v + 1) for u, v in mutual))

        check(trees == (1 if n == 1 else n ** (n - 2)), "Cayley census failure")
        check(max(depths) == (n - 1) // 2, "sharp tail failure")
        check(set(periods) == ({1} if n % 2 else {2}), "period support failure")
        predicted_fixed = fixed_series[n] * factorial(n)
        predicted_recurrent = recurrent_series[n] * factorial(n)
        if n % 2:
            check(fixed == recurrent == predicted_fixed, "odd fixed EGF failure")
            check(maximum_fibre == (n + 1) // 2, "odd max fibre failure")
        else:
            check(fixed == 0, "even fixed point exists")
            check(recurrent == predicted_recurrent, "even recurrent EGF failure")
            check(maximum_fibre == n - 1, "even max fibre failure")
        expected_weight = w_series[n] * factorial(n)
        check(weighted_side_totals[n] == expected_weight,
              "integrated odd-branch weight failure")
        hist = ",".join(f"{d}:{depths[d]}" for d in sorted(depths))
        records.append((n, trees, sum(depths.values()), recurrent,
                        max(depths), maximum_fibre, hist))

    check(first_multi is not None and first_multi[0] == 6,
          "minimal same-H-component multiple-attractor witness is not order six")

    print("P195 hostile Review-A independent control")
    for n, trees, states, recurrent, mt, mf, hist in records:
        print(f"n={n} trees={trees} states={states} recurrent={recurrent} "
              f"max_tail={mt} max_fibre={mf} depth_hist={hist}")
    print(f"transitions={transitions}")
    print(f"checks={CHECKS}")
    print(f"record_digest={digest.hexdigest()}")
    print(f"first_multi_H_component={first_multi}")
    print("imports_author_code=false")
    print("owner_state=OWNER_AMBER/HOLD_EXTERNAL")
    print("historical_findings_closed=P195-A1,P195-A2")
    print("open_findings=critical:0,major:0,minor:0")
    print("review_decision=PASS")
    print("status=PASS")


if __name__ == "__main__":
    main()
