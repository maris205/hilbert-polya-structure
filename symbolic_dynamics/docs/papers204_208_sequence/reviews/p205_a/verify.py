#!/usr/bin/env python3
"""Independent P205 manuscript Review A pressure; Python standard library only.

Written from the frozen mathematical statements, without opening/importing any
author or earlier gate implementation/canonical. No filesystem/network input.
Arrival uses a priority event queue, recurrence uses whole-functional-graph
leaf removal, and inverse reconstruction enumerates held independent sets.
Finite verification is not a proof of the all-parameter statements.
"""

from collections import Counter, deque
from hashlib import sha256
from heapq import heappop, heappush
from itertools import combinations, product
import json


class Audit:
    def __init__(self):
        self.assertions = 0
        self.digest = sha256()

    def require(self, condition, label):
        self.assertions += 1
        if not condition:
            raise AssertionError(label)

    def record(self, obj):
        self.digest.update(json.dumps(obj, separators=(",", ":")).encode())
        self.digest.update(b"\n")


def graph(n, code):
    pairs = tuple(combinations(range(n), 2))
    edges = tuple(e for i, e in enumerate(pairs) if code & (1 << i))
    neighbors = [[] for _ in range(n)]
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    return edges, tuple(tuple(row) for row in neighbors)


def active_vertices(x, edges):
    vertices = set()
    for u, v in edges:
        if x[u] == x[v]:
            vertices.add(u)
            vertices.add(v)
    return vertices


def literal(x, neighbors, q):
    return tuple((colour + any(x[u] == colour for u in neighbors[v])) % q
                 for v, colour in enumerate(x))


def encode(x, q):
    result = 0
    for digit in x:
        result = q * result + digit
    return result


def arrivals(x, edges, neighbors, q):
    """First-arrival priority queue, not an all-pairs distance matrix."""
    times = [None] * len(x)
    queue = [(0, v) for v in active_vertices(x, edges)]
    # Seed insertion order cannot affect the result, but make it deterministic.
    queue.sort()
    while queue:
        when, v = heappop(queue)
        if times[v] is not None:
            continue
        times[v] = when
        for u in neighbors[v]:
            if times[u] is None:
                heappush(queue, (when + (x[u] - x[v]) % q, u))
    return tuple(times)


def peel(next_state):
    """Exact entrance/period for every state by Kahn removal plus cycle walks."""
    size = len(next_state)
    indegree = [0] * size
    for target in next_state:
        indegree[target] += 1
    queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
    removed = []
    while queue:
        u = queue.popleft()
        removed.append(u)
        v = next_state[u]
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
    height = [0] * size
    period = [0] * size
    for u in range(size):
        if indegree[u] == 0 or period[u]:
            continue
        cycle = [u]
        v = next_state[u]
        while v != u:
            cycle.append(v)
            v = next_state[v]
        for v in cycle:
            period[v] = len(cycle)
    for u in reversed(removed):
        v = next_state[u]
        height[u] = height[v] + 1
        period[u] = period[v]
    return height, period


def components(neighbors):
    unseen = set(range(len(neighbors)))
    result = []
    while unseen:
        first = min(unseen)
        unseen.remove(first)
        component = {first}
        stack = [first]
        while stack:
            u = stack.pop()
            for v in neighbors[u]:
                if v in unseen:
                    unseen.remove(v)
                    component.add(v)
                    stack.append(v)
        result.append(component)
    return result


def held_conditions(held, n, equal_edges, successor):
    # Held vertices form an independent set in the target equality graph.
    independent = all(not (held & (1 << u) and held & (1 << v))
                      for u, v in equal_edges)
    outside = ((1 << n) - 1) ^ held
    supported = 0
    for u, v in equal_edges:
        if outside & (1 << u) and outside & (1 << v):
            supported |= (1 << u) | (1 << v)
    no_outside_isolates = supported == outside
    # The complement of predecessor closure is successor closure of held sets.
    closed = all(not (held & (1 << u)) or (held & (1 << v))
                 for u, v in successor)
    return independent, no_outside_isolates, closed


def target_data(y, edges, q):
    equal_edges = tuple((u, v) for u, v in edges if y[u] == y[v])
    successor = []
    for u, v in edges:
        if (y[v] - y[u]) % q == 1:
            successor.append((u, v))
        if (y[u] - y[v]) % q == 1:
            successor.append((v, u))
    return equal_edges, tuple(successor)


def held_decode(y, edges, q):
    equal_edges, successor = target_data(y, edges, q)
    result = set()
    for held in range(1 << len(y)):
        if all(held_conditions(held, len(y), equal_edges, successor)):
            result.add(encode(tuple(value if held & (1 << v) else (value - 1) % q
                                    for v, value in enumerate(y)), q))
    return result


def total_covers(n, edges):
    return sum(all(held_conditions(held, n, edges, ()))
               for held in range(1 << n))


def is_star(neighbors):
    n = len(neighbors)
    return n >= 3 and sorted(map(len, neighbors)) == [1] * (n - 1) + [n - 1]


def extremal_size(n):
    return 1 if n <= 2 else 4 if n == 3 else (1 << (n - 1)) - 1


def dynamic_box(n, q, audit):
    before = audit.assertions
    states = tuple(product(range(q), repeat=n))
    total_graphs = 1 << (n * (n - 1) // 2)
    height_histogram = Counter()
    period_histogram = Counter()
    maximum_locations = 0
    reached_maximum = 0
    checked_times = 0
    for graph_code in range(total_graphs):
        edges, neighbors = graph(n, graph_code)
        next_state = [encode(literal(x, neighbors, q), q) for x in states]
        incoming = [set() for _ in states]
        for source, target in enumerate(next_state):
            incoming[target].add(source)
        heights, periods = peel(next_state)
        component_list = components(neighbors)
        for source, x in enumerate(states):
            arrival = arrivals(x, edges, neighbors, q)
            finite = [time for time in arrival if time is not None]
            predicted_height = max(finite, default=0)
            audit.require(heights[source] == predicted_height,
                          ("entrance", n, q, graph_code, x))
            active = active_vertices(x, edges)
            immediate_core = all(not (active & c) or c <= active
                                 for c in component_list)
            audit.require((heights[source] == 0) == immediate_core,
                          ("componentwise-core", n, q, graph_code, x))
            audit.require(periods[source] == (q if active else 1),
                          ("exact-period", n, q, graph_code, x))
            uniform_height = (q - 1) * max(0, n - 2)
            audit.require(heights[source] <= uniform_height,
                          ("uniform-height", n, q, graph_code, x))
            first_seen = [None] * n
            current_index = source
            previous_active = set()
            previous_conflicts = set()
            for time in range(heights[source] + 2 * q + 1):
                current = states[current_index]
                predicted = tuple(value if arrival[v] is None else
                                  (value + max(0, time - arrival[v])) % q
                                  for v, value in enumerate(x))
                audit.require(current == predicted,
                              ("all-time-coordinate", n, q, graph_code, x, time))
                now_active = active_vertices(current, edges)
                conflicts = {(u, v) for u, v in edges if current[u] == current[v]}
                audit.require(previous_active <= now_active,
                              ("active-monotonicity", n, q, graph_code, x, time))
                audit.require(previous_conflicts <= conflicts,
                              ("permanent-edge", n, q, graph_code, x, time))
                for v in now_active:
                    if first_seen[v] is None:
                        first_seen[v] = time
                previous_active = now_active
                previous_conflicts = conflicts
                current_index = next_state[current_index]
                checked_times += 1
            audit.require(tuple(first_seen) == arrival,
                          ("actual-first-conflict", n, q, graph_code, x))
            decoded = held_decode(x, edges, q)
            audit.require(decoded == incoming[source],
                          ("full-predecessor-set", n, q, graph_code, x))
            size = len(incoming[source])
            audit.require(size <= extremal_size(n),
                          ("uniform-fibre", n, q, graph_code, x))
            if n >= 3:
                claimed_extremizer = (len(set(x)) == 1 and
                                      (len(edges) == 3 if n == 3 else is_star(neighbors)))
                audit.require((size == extremal_size(n)) == claimed_extremizer,
                              ("all-graph-target-equality", n, q, graph_code, x))
            maximum_locations += size == extremal_size(n)
            reached_maximum = max(reached_maximum, size)
            height_histogram[heights[source]] += 1
            period_histogram[periods[source]] += 1
            audit.record(["dynamic", n, q, graph_code, source,
                          arrival, heights[source], periods[source], size])
    audit.require(reached_maximum == extremal_size(n), ("attained-fibre", n, q))
    audit.require(max(height_histogram) == (q - 1) * max(0, n - 2),
                  ("attained-height", n, q))
    if n >= 3:
        audit.require(maximum_locations == (q if n == 3 else n * q),
                      ("labelled-extremizer-count", n, q))
    return {"n": n, "q": q, "graphs": total_graphs,
            "states_and_targets": total_graphs * len(states),
            "checked_orbit_times": checked_times,
            "height_histogram": dict(sorted(height_histogram.items())),
            "period_histogram": dict(sorted(period_histogram.items())),
            "maximum_fibre": reached_maximum,
            "maximum_graph_target_pairs": maximum_locations,
            "assertions": audit.assertions - before}


def static_box(n, audit):
    before = audit.assertions
    census = Counter()
    maximizers = []
    number_of_graphs = 1 << (n * (n - 1) // 2)
    for code in range(number_of_graphs):
        edges, neighbors = graph(n, code)
        count = total_covers(n, edges)
        audit.require(count <= extremal_size(n), ("static-bound", n, code))
        if n >= 3:
            claimed = len(edges) == 3 if n == 3 else is_star(neighbors)
            audit.require((count == extremal_size(n)) == claimed,
                          ("static-all-maximizers", n, code))
        if count == extremal_size(n):
            maximizers.append(code)
        census[count] += 1
        audit.record(["static", n, code, count])
    return {"n": n, "graphs": number_of_graphs,
            "cover_count_histogram": dict(sorted(census.items())),
            "maximizer_graph_codes": maximizers,
            "assertions": audit.assertions - before}


def boundary_cases(audit):
    representatives = {
        "star": ((0, 1), (0, 2), (0, 3)),
        "path": ((0, 1), (1, 2), (2, 3)),
        "paw": ((0, 1), (1, 2), (0, 2), (2, 3)),
        "four_cycle": ((0, 1), (1, 2), (2, 3), (0, 3)),
        "diamond": ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3)),
        "complete": tuple(combinations(range(4), 2)),
    }
    expected = {"star": 7, "path": 4, "paw": 6,
                "four_cycle": 5, "diamond": 6, "complete": 5}
    actual = {name: total_covers(4, edges) for name, edges in representatives.items()}
    audit.require(actual == expected, "six-connected-order-four-values")
    p4_independent = [held for held in range(16)
                      if held_conditions(held, 4, representatives["path"], ())[0]]
    incidences = [sum(bool(held & (1 << u)) for held in p4_independent) for u in range(4)]
    audit.require(len(p4_independent) == 8 and min(incidences) == 2,
                  "four-path-independent-exclusion")
    result = {"connected_order_four": actual,
              "path_independent_sets": p4_independent,
              "path_vertex_incidences": incidences}
    audit.record(["boundary", result])
    return result


def negative_controls(audit):
    missing = {}
    for n in range(1, 4):
        for code in range(1 << (n * (n - 1) // 2)):
            edges, neighbors = graph(n, code)
            for y in product(range(3), repeat=n):
                equal, successor = target_data(y, edges, 3)
                for held in range(1 << n):
                    flags = held_conditions(held, n, equal, successor)
                    for omitted in range(3):
                        if omitted in missing or flags[omitted]:
                            continue
                        if all(flags[j] for j in range(3) if j != omitted):
                            source = tuple(value if held & (1 << v) else (value - 1) % 3
                                           for v, value in enumerate(y))
                            image = literal(source, neighbors, 3)
                            audit.require(image != y, ("negative-control", omitted))
                            missing[omitted] = {"n": n, "graph_code": code,
                                                "target": y, "held_mask": held,
                                                "source": source, "actual_image": image}
    audit.require(len(missing) == 3, "all-three-conditions-necessary")
    edges = ((0, 1), (1, 2))
    neighbors = ((1,), (0, 2), (1,))
    x = (0, 0, 2)
    timeline = [x]
    for _ in range(3):
        timeline.append(literal(timeline[-1], neighbors, 3))
    audit.require(timeline == [(0, 0, 2), (1, 1, 2), (2, 2, 2), (0, 0, 0)],
                  "activation-versus-first-increment-shift")
    audit.require(arrivals(x, edges, neighbors, 3) == (0, 0, 2),
                  "directed-residue-not-reversed")
    audit.require(active_vertices((0, 0, 1), edges) == active_vertices(x, edges) and
                  active_vertices(literal((0, 0, 1), neighbors, 3), edges) !=
                  active_vertices(literal(x, neighbors, 3), edges),
                  "initial-active-mask-not-autonomous-flood")
    result = {"omitted_held_conditions": missing, "q3_path_timeline": timeline}
    audit.record(["negative", result])
    return result


def sharp_paths(audit):
    rows = []
    for n in range(2, 31):
        edges = tuple((v, v + 1) for v in range(n - 1))
        neighbors = tuple(tuple(u for u in (v - 1, v + 1) if 0 <= u < n)
                          for v in range(n))
        for q in range(3, 14):
            x = tuple(0 if v <= 1 else (1 - v) % q for v in range(n))
            expected = (q - 1) * (n - 2)
            arrival = arrivals(x, edges, neighbors, q)
            audit.require(max(arrival) == expected, ("sharp-path-queue", n, q))
            current = x
            first_all_active = None
            for time in range(expected + q + 1):
                prediction = tuple((value + max(0, time - arrival[v])) % q
                                   for v, value in enumerate(x))
                audit.require(current == prediction, ("sharp-path-literal", n, q, time))
                if len(active_vertices(current, edges)) == n and first_all_active is None:
                    first_all_active = time
                current = literal(current, neighbors, q)
            audit.require(first_all_active == expected, ("sharp-path-last-arrival", n, q))
            rows.append([n, q, expected])
            audit.record(["sharp-path", n, q, expected])
    return {"n_range_inclusive": [2, 30], "q_range_inclusive": [3, 13],
            "cases": len(rows), "height_sum": sum(row[2] for row in rows)}


def main():
    audit = Audit()
    dynamics = [dynamic_box(n, q, audit)
                for q, largest_n in ((3, 5), (4, 4), (5, 4), (7, 3))
                for n in range(largest_n + 1)]
    statics = [static_box(n, audit) for n in range(7)]
    boundary = boundary_cases(audit)
    negative = negative_controls(audit)
    paths = sharp_paths(audit)
    print(json.dumps({"status": "PASS", "review": "P205_A_ROUND0",
                      "representation": "event_queue__functional_graph_peeling__held_sets",
                      "external_inputs": [], "randomness": "none",
                      "dynamic_boxes": dynamics, "static_boxes": statics,
                      "boundary": boundary, "negative_controls": negative,
                      "sharp_paths": paths, "assertions": audit.assertions,
                      "dynamic_states": sum(row["states_and_targets"] for row in dynamics),
                      "literal_orbit_times": sum(row["checked_orbit_times"] for row in dynamics),
                      "static_graphs": sum(row["graphs"] for row in statics),
                      "record_sha256": audit.digest.hexdigest(),
                      "scope_limit": "finite proof pressure; not all-parameter or priority proof"},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
