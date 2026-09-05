#!/usr/bin/env python3
"""Independent GM candidate checks; no author-program imports.

The update uses sets and sorted search, the orbit detector walks to a repeat,
and the sharp construction uses symbolic vertex names. The incidence lane
tests the claimed inverse mechanism outside undirected graphs.
"""

from collections import Counter
from itertools import combinations, product
from math import comb
import hashlib
import json


COUNTS = Counter()


def require(statement, label, witness=None):
    COUNTS[label] += 1
    if not statement:
        raise AssertionError((label, witness))


def first_absent(values):
    candidate = 0
    for value in sorted(set(values)):
        if value == candidate:
            candidate += 1
        elif value > candidate:
            break
    return candidate


def step(colors, rows):
    return tuple(first_absent(colors[u] for u in row) for row in rows)


def complete_orbit(start, arrows):
    seen = {}
    current = start
    while current not in seen:
        seen[current] = len(seen)
        current = arrows[current]
    tail = seen[current]
    return tail, len(seen) - tail


def serial_cover_check(path, rows):
    # Part zero stores even times; part one stores odd times.
    cover = [list(path[0]), list(path[1])]
    for v, row in enumerate(rows):
        for u in row:
            require(cover[0][v] != cover[1][u], "cover_initial_proper")
    for time in range(2, len(path)):
        side = time % 2
        for v, row in enumerate(rows):
            old = cover[side][v]
            new = first_absent(cover[1-side][u] for u in row)
            # Guarded moves and unguarded no-ops have the same result.
            if new != old:
                cover[side][v] = new
            require(new <= old, "cover_serial_descent")
            for u in row:
                require(cover[side][v] != cover[1-side][u],
                        "cover_serial_proper")
        require(tuple(cover[side]) == path[time], "cover_exact_adapter")


def graph_lane(digest):
    graphs = sources = 0
    depth_histogram = Counter()
    for n in range(5):
        potential_edges = tuple(combinations(range(n), 2))
        for flags in product((False, True), repeat=len(potential_edges)):
            rows = [set() for _ in range(n)]
            for present, (a, b) in zip(flags, potential_edges):
                if present:
                    rows[a].add(b)
                    rows[b].add(a)
            degree = max(map(len, rows), default=0)
            isolated = sum(not row for row in rows)
            graphs += 1
            for q in (max(3, degree+1), max(3, degree+1)+1):
                states = tuple(product(range(q), repeat=n))
                arrows = {c: step(c, rows) for c in states}
                fibres = Counter(arrows.values())
                maximum = q**isolated * (q-1)**(n-isolated)
                require(sum(fibres.values()) == q**n, "graph_fibre_mass")
                require(max(fibres.values()) == maximum,
                        "graph_max_fibre_value")
                require({y for y, size in fibres.items() if size == maximum}
                        == {(0,)*n}, "graph_max_fibre_unique")
                for c in states:
                    sources += 1
                    h, period = complete_orbit(c, arrows)
                    require(period in (1, 2), "actual_cycle_period")
                    require(h <= max(1, degree), "actual_orbit_tail")
                    depth_histogram[(degree, h)] += 1
                    path = [c]
                    for _ in range(max(1, degree)+3):
                        path.append(arrows[path[-1]])
                    for time in range(len(path)-2):
                        for v, row in enumerate(rows):
                            old, new = path[time][v], path[time+2][v]
                            require(new <= old, "direct_two_step_descent")
                            require(new == old or old >= time+1,
                                    "direct_strict_drop_rank")
                            if time >= max(1, len(row)):
                                require(old == new, "direct_local_deadline")
                    serial_cover_check(path, rows)
                    digest.update(repr((n, flags, q, c, arrows[c], h,
                                        period)).encode("ascii"))
    return {"graphs": graphs, "graph_palette_sources": sources,
            "degree_tail_histogram": [[d, h, count]
                                      for (d, h), count in
                                      sorted(depth_histogram.items())]}


def incidence_lane(digest):
    systems = sources = 0
    for n in range(4):
        subsets = [tuple(i for i in range(n) if (mask >> i) & 1)
                   for mask in range(1 << n)]
        for rows in product(subsets, repeat=n):
            systems += 1
            max_arity = max(map(len, rows), default=0)
            unused = sum(all(u not in row for row in rows) for u in range(n))
            q = max(3, max_arity+1)
            fibres = Counter()
            for c in product(range(q), repeat=n):
                sources += 1
                fibres[step(c, rows)] += 1
            bound = q**unused * (q-1)**(n-unused)
            require(sum(fibres.values()) == q**n, "incidence_mass")
            require(max(fibres.values()) == bound, "incidence_max_value")
            require({y for y, size in fibres.items() if size == bound}
                    == {(0,)*n}, "incidence_unique_max")
            digest.update(repr((rows, q, sorted(fibres.items()))).encode("ascii"))
    return {"incidence_systems": systems, "incidence_sources": sources}


def symbolic_sharp(d):
    rows = {}
    initial = {}

    def vertex(name, color):
        rows[name] = set()
        initial[name] = color

    def edge(a, b):
        rows[a].add(b)
        rows[b].add(a)

    for k in range(1, d+1):
        vertex(("chain", k), k)
    vertex(("u",), 0)
    vertex(("w",), 0)
    for k in range(1, d):
        edge(("chain", k), ("chain", k+1))
    edge(("chain", 1), ("u",))
    edge(("u",), ("w",))
    for k in range(2, d+1):
        for j in range(k-1):
            clique = [("anchor", k, j, color) for color in range(j+1)]
            for node in clique:
                vertex(node, node[-1])
            for a, b in combinations(clique, 2):
                edge(a, b)
            edge(clique[-1], ("chain", k))
    return rows, initial


def sharp_lane(digest):
    records = []
    for d in range(2, 17):
        rows, initial = symbolic_sharp(d)
        require(len(rows) == d+2+comb(d+1, 3), "sharp_vertex_count")
        require(max(map(len, rows.values())) == d, "sharp_max_degree")
        colors = initial
        seen = {}
        for time in range(2*d+6):
            expected = dict(initial)
            for k in range(1, d+1):
                drop = time >= k+1 and time % 2 == (k+1) % 2
                expected[("chain", k)] = k-int(drop)
            expected[("w",)] = time % 2
            expected[("u",)] = 0 if time % 2 == 0 else (2 if time == 1 else 1)
            require(colors == expected, "sharp_all_coordinates_all_times",
                    (d, time))
            seen[time] = colors
            colors = {v: first_absent(colors[u] for u in row)
                      for v, row in rows.items()}
        require(seen[d-1] != seen[d+1], "sharp_lower_bound")
        require(seen[d] == seen[d+2], "sharp_exact_entrance")
        record = {"degree": d, "vertices": len(rows), "entrance": d}
        records.append(record)
        digest.update(repr(record).encode("ascii"))
    return records


def main():
    digest = hashlib.sha256()
    graph = graph_lane(digest)
    incidence = incidence_lane(digest)
    witnesses = sharp_lane(digest)
    require(step((0, 2), ((1,), (0,))) == (0, 1), "degree_one_witness")
    binary = Counter(step(c, ((1,), (0,))) for c in product(range(2), repeat=2))
    require(len(binary) == 4 and set(binary.values()) == {1},
            "q_two_uniqueness_counterexample")
    print(json.dumps({"scope": "INDEPENDENT_GM_CANDIDATE_GATE_NOT_PAPER_REVIEW",
                      **graph, **incidence, "sharp_witnesses": witnesses,
                      "checks": dict(sorted(COUNTS.items())),
                      "total_checks": sum(COUNTS.values()),
                      "enumeration_sha256": digest.hexdigest(),
                      "result": "PASS_BOUNDED_MATH_AND_ADAPTER_ONLY",
                      "value_gate": "NOT_INFERRED_FROM_COMPUTATION",
                      "external_status": "HOLD_EXTERNAL"},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
