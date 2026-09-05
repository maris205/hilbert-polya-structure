#!/usr/bin/env python3
"""One bounded literal probe, all simple loopless undirected graphs n<=6."""
from collections import Counter, defaultdict
from itertools import combinations


def equality_certificates(n, graph, edge_id, triangles):
    """Target-only full-star/full-K4 certificates; no forward map call."""
    def colour(a, b):
        return (graph >> edge_id[tuple(sorted((a, b)))]) & 1

    def mono(triangle):
        return len({colour(a, b) for a, b in combinations(triangle, 2)}) == 1

    def ordered(*vertices):
        return tuple(sorted(vertices))

    stars = []
    for a, b in combinations(range(n), 2):
        c = colour(a, b)
        outside = [v for v in range(n) if v not in (a, b)]
        if not outside or any(colour(a, v) != c or colour(b, v) != c for v in outside):
            continue
        if any(
            colour(x, y) == c and ordered(a, b, z) > ordered(a, x, y)
            for x, y in combinations(outside, 2) for z in outside if z not in (x, y)
        ):
            continue
        last = ordered(a, b, max(outside))
        if any(mono(t) and t < last for t in combinations(outside, 3)):
            continue
        stars.append((a, b))
    tops = []
    for four in combinations(range(n), 4):
        c = colour(four[0], four[1])
        if any(colour(x, y) != c for x, y in combinations(four, 2)):
            continue
        faces = tuple(combinations(four, 3))
        last = faces[-1]
        if any(len(set(t).intersection(four)) <= 1 and t < last and mono(t) for t in triangles):
            continue
        good = True
        for u in range(n):
            if u in four:
                continue
            for x, y in combinations(four, 2):
                if colour(u, x) != colour(u, y):
                    continue
                p = ordered(u, x, y)
                for q in faces:
                    contains_pair = x in q and y in q
                    forbidden = (colour(u, x) == c and not contains_pair) or (
                        colour(u, x) != c and contains_pair
                    )
                    if forbidden and p < q:
                        good = False
        if good:
            tops.append(four)
    return stars, tops


def box(n):
    edges = tuple(combinations(range(n), 2))
    edge_id = {e: i for i, e in enumerate(edges)}
    triangles = tuple(combinations(range(n), 3))
    masks = tuple(sum(1 << edge_id[e] for e in combinations(t, 2)) for t in triangles)
    states = range(1 << len(edges))
    selected = []
    transitions = []
    for graph in states:
        index = next((i for i, m in enumerate(masks) if graph & m in (0, m)), None)
        matrix = [[0] * n for _ in range(n)]
        for (a, b), e in edge_id.items():
            matrix[a][b] = matrix[b][a] = (graph >> e) & 1
        direct = next((k for k, (a, b, c) in enumerate(triangles)
                       if matrix[a][b] == matrix[a][c] == matrix[b][c]), None)
        assert index == direct
        selected.append(index)
        transitions.append(graph if index is None else graph ^ masks[index])
    predecessors = defaultdict(set)
    for graph, target in enumerate(transitions):
        predecessors[target].add(graph)
    tails, periods = Counter(), Counter()
    max_tail, tail_witness = -1, None
    assertions = len(states)
    for graph in states:
        seen, state = {}, graph
        active_trace = []
        while state not in seen:
            seen[state] = len(seen)
            if selected[state] is not None:
                active_trace.append(triangles[selected[state]])
            state = transitions[state]
        tail, period = seen[state], len(seen) - seen[state]
        tails[tail] += 1
        periods[period] += 1
        if tail > max_tail:
            max_tail, tail_witness = tail, graph
        assert period in (1, 2)
        assertions += 1
        if len(active_trace) > 1:
            anchor = min(active_trace[1])
            assert all(min(t) == anchor for t in active_trace[1:])
            assertions += 1
        used = set(active_trace[0]) if active_trace else set()
        for old, new in zip(active_trace[:tail], active_trace[1:tail + 1]):
            added = set(new).difference(old)
            assert len(added) == 1 and not added.intersection(used)
            assertions += 1
            used.update(added)
        inverse = {graph} if selected[graph] is None else set()
        for k, mask in enumerate(masks):
            if graph & mask not in (0, mask):
                continue
            source = graph ^ mask
            if all(source & earlier not in (0, earlier) for earlier in masks[:k]):
                inverse.add(source)
        assert inverse == predecessors[graph]
        assertions += 1
        monochromatic = [k for k, m in enumerate(masks) if graph & m in (0, m)]
        local_inverse = {graph} if not monochromatic else set()
        for k in monochromatic:
            q = set(triangles[k])
            c = int(graph & masks[k] != 0)
            destroys_earlier = all(len(q.intersection(triangles[j])) == 2
                                  for j in monochromatic if j < k)
            creates_none = all(
                not all(((graph >> edge_id[tuple(sorted((u, v)))]) & 1) == 1 - c
                        for v in (a, b))
                for a, b in combinations(sorted(q), 2) for u in range(n)
                if u not in q and tuple(sorted((u, a, b))) < triangles[k]
            )
            if destroys_earlier and creates_none:
                local_inverse.add(graph ^ masks[k])
            if k == selected[graph]:
                assert creates_none == (tail == 0)
                assertions += 1
        assert local_inverse == inverse
        assertions += 1
        for p, q in combinations((triangles[selected[s]] for s in inverse if s != graph), 2):
            assert len(set(p).intersection(q)) == 2
            assertions += 1
        if n >= 4:
            stars, tops = equality_certificates(n, graph, edge_id, triangles)
            maximum_certificate = bool(tops) if n <= 5 else (
                bool(stars or tops) if n == 6 else bool(stars)
            )
            assert (len(inverse) == max(4, n - 2)) == maximum_certificate
            assertions += 1
            for a, b in stars:
                assert all(
                    graph ^ masks[triangles.index(tuple(sorted((a, b, v))))] in inverse
                    for v in range(n) if v not in (a, b)
                )
                assertions += 1
            for four in tops:
                assert all(graph ^ masks[triangles.index(q)] in inverse for q in combinations(four, 3))
                assertions += 1
        if selected[graph] is not None:
            first = set(triangles[selected[graph]])
            for source in inverse:
                k = selected[source]
                assert k >= selected[graph]
                assert len(first.intersection(triangles[k])) >= 2
                assertions += 2
            assert len(inverse) <= 3 * (n - 3) + 1
            assertions += 1
        else:
            assert inverse == {graph}
            assertions += 1
    maximum = max(map(len, predecessors.values()))
    assert maximum == (1 if n <= 3 else max(4, n - 2))
    assertions += 1
    assert max_tail == max(0, n - 3)
    assertions += 1
    if n >= 3:
        order = list(reversed(range(1, n)))
        colours = [0, 0] + [(i - 1) % 2 for i in range(2, n - 1)]
        witness = 0
        for i, v in enumerate(order):
            if colours[i]:
                witness |= 1 << edge_id[(0, v)]
        for i, j in combinations(range(n - 1), 2):
            c = i % 2 if j == i + 1 else (
                1 - colours[i] if colours[i] == colours[j] else colours[i]
            )
            if c:
                witness |= 1 << edge_id[tuple(sorted((order[i], order[j])))]
        for t in range(n - 2):
            assert triangles[selected[witness]] == tuple(sorted((0, order[t], order[t + 1])))
            assertions += 1
            witness = transitions[witness]
        assert transitions[transitions[witness]] == witness
        assertions += 1
    maximizers = [g for g in states if len(predecessors[g]) == maximum]
    trace = []
    g = tail_witness
    for _ in range(max_tail + 2):
        trace.append((g, None if selected[g] is None else triangles[selected[g]]))
        g = transitions[g]
    print(f"n={n} states={len(states)} image={sum(bool(predecessors[g]) for g in states)} "
          f"fixed={sum(transitions[g] == g for g in states)} "
          f"max_tail={max_tail} max_fibre={maximum} maximizers={len(maximizers)}")
    print("tail_hist=" + repr(sorted(tails.items())))
    print("period_state_hist=" + repr(sorted(periods.items())))
    print("fibre_hist=" + repr(sorted(Counter(len(predecessors[g]) for g in states).items())))
    print("deepest_trace=" + repr(trace))
    print("first_maximizers=" + repr(maximizers[:20]))
    print(f"assertions={assertions}")
    return assertions


if __name__ == "__main__":
    print("MONOCHROMATIC_TRIANGLE_PROBE_V1 / NO_NUMBER / HOLD_EXTERNAL")
    count = sum(box(n) for n in range(7))
    print(f"TOTAL_ASSERTIONS={count}")
    print("PASS_BOUNDED_ONLY / NO_ALL_N_SHARP_CLAIM")
