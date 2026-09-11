#!/usr/bin/env python3
"""CCI author proof pressure: literal orbits vs weighted all-pairs distances.

No pilot, historical or other author code is imported. This independent
implementation is not an independent reviewer process.
"""

from collections import Counter
from itertools import product
import hashlib
import json

CHECKS = Counter()


def require(condition, label, witness=None):
    CHECKS[label] += 1
    if not condition:
        raise AssertionError((label, witness))


def graph_rows(n):
    locations = tuple((u, v) for u in range(n) for v in range(u+1, n))
    for code in range(1 << len(locations)):
        rows = [0]*n
        for bit, (u, v) in enumerate(locations):
            if code & (1 << bit):
                rows[u] |= 1 << v
                rows[v] |= 1 << u
        yield code, tuple(rows)


def adjacency(rows):
    return tuple(tuple(u for u in range(len(rows)) if row & (1 << u)) for row in rows)


def advance(word, neighbors, q):
    return tuple((color+int(any(word[u] == color for u in neighbors[v]))) % q
                 for v, color in enumerate(word))


def active(word, neighbors):
    return {v for v, color in enumerate(word)
            if any(word[u] == color for u in neighbors[v])}


def arrivals(word, neighbors, q):
    n = len(word)
    infinity = q*n+1
    distance = [[infinity]*n for _ in range(n)]
    for u in range(n):
        distance[u][u] = 0
        for v in neighbors[u]:
            distance[u][v] = (word[v]-word[u]) % q
    for middle in range(n):
        for u in range(n):
            for v in range(n):
                distance[u][v] = min(distance[u][v],
                                      distance[u][middle]+distance[middle][v])
    seeds = active(word, neighbors)
    return tuple(min((distance[u][v] for u in seeds), default=infinity)
                 for v in range(n)), infinity


def exact_masks(target, neighbors, q):
    n = len(target)
    same = tuple(sum(1 << u for u in neighbors[v] if target[u] == target[v])
                 for v in range(n))
    predecessors = tuple(sum(1 << u for u in neighbors[v]
                             if (target[v]-target[u]) % q == 1) for v in range(n))
    result = set()
    all_vertices = (1 << n)-1
    for mask in range(1 << n):
        good = True
        for v in range(n):
            if mask & (1 << v):
                good &= bool(mask & same[v]) and not bool(predecessors[v] & (all_vertices ^ mask))
            else:
                good &= not bool(same[v] & (all_vertices ^ mask))
        if good:
            result.add(tuple((color-int(bool(mask & (1 << v)))) % q
                             for v, color in enumerate(target)))
    return result


def cover_count(rows):
    n = len(rows)
    all_vertices = (1 << n)-1
    answer = 0
    for complement in range(1 << n):
        selected = all_vertices ^ complement
        good = True
        for v, row in enumerate(rows):
            if complement & (1 << v):
                good &= not bool(row & complement)
            else:
                good &= bool(row & selected)
        answer += good
    return answer


def is_star(rows):
    n = len(rows)
    return n >= 3 and sorted(row.bit_count() for row in rows) == [1]*(n-1)+[n-1]


def maximum(n):
    return 1 if n <= 2 else 4 if n == 3 else (1 << (n-1))-1


def dynamic_checks(digest):
    output = []
    for n in range(5):
        for q in (3, 4, 5):
            height = largest_fibre = count = equality_count = 0
            periods = set()
            for graph, rows in graph_rows(n):
                neighbors = adjacency(rows)
                words = tuple(product(range(q), repeat=n))
                arrows = {word: advance(word, neighbors, q) for word in words}
                fibres = {word: set() for word in words}
                for word in words:
                    count += 1
                    fibres[arrows[word]].add(word)
                    tau, infinity = arrivals(word, neighbors, q)
                    expected_height = max((d for d in tau if d < infinity), default=0)
                    visited, x = {}, word
                    observed_tau = [infinity]*n
                    old_active = set()
                    time = 0
                    while x not in visited:
                        visited[x] = time
                        now = active(x, neighbors)
                        require(old_active <= now, "permanent_activation")
                        for v in now:
                            observed_tau[v] = min(observed_tau[v], time)
                        require(x == tuple((word[v]+max(0, time-tau[v])) % q
                                           if tau[v] < infinity else word[v]
                                           for v in range(n)), "all_time_arrival_formula")
                        old_active = now
                        x = arrows[x]
                        time += 1
                    actual_height = visited[x]
                    period = time-actual_height
                    require(actual_height == expected_height, "exact_entrance")
                    require(tuple(observed_tau) == tau, "first_conflict_is_shortest_arrival")
                    require(period == (q if any(d < infinity for d in tau) else 1),
                            "exact_period")
                    require(actual_height <= max(0, (q-1)*(n-2)), "uniform_clock_upper")
                    height = max(height, actual_height)
                    periods.add(period)
                    digest.update(repr((n, q, graph, word, tau, actual_height, period)).encode("ascii"))
                for target in words:
                    predicted = exact_masks(target, neighbors, q)
                    require(predicted == fibres[target], "every_target_exact_source_set")
                    size = len(predicted)
                    largest_fibre = max(largest_fibre, size)
                    require(size <= maximum(n), "uniform_fibre_upper")
                    if n >= 3:
                        predicted_equality = (is_star(rows) if n >= 4 else all(row.bit_count() == 2 for row in rows)) and len(set(target)) == 1
                        require((size == maximum(n)) == predicted_equality,
                                "all_fibre_equality_cases")
                    equality_count += size == maximum(n)
            require(height == max(0, (q-1)*(n-2)), "sharp_global_clock_small")
            require(largest_fibre == maximum(n), "sharp_global_fibre_small")
            output.append({"n": n, "q": q, "sources": count, "height": height,
                           "periods": sorted(periods), "max_fibre": largest_fibre,
                           "extremal_graph_target_pairs": equality_count})
    return output


def static_checks(digest):
    output = []
    for n in range(7):
        largest = 0
        equalities = []
        graph_count = 0
        for code, rows in graph_rows(n):
            graph_count += 1
            value = cover_count(rows)
            require(value <= maximum(n), "static_total_cover_upper")
            if n >= 3:
                predicted = is_star(rows) if n >= 4 else all(row.bit_count() == 2 for row in rows)
                require((value == maximum(n)) == predicted, "static_total_cover_equality")
            largest = max(largest, value)
            if value == maximum(n):
                equalities.append(code)
            digest.update(repr((n, code, value)).encode("ascii"))
        output.append({"n": n, "graphs": graph_count, "max_total_covers": largest,
                       "extremal_graphs": len(equalities)})
    return output


def sharp_family_checks():
    cases = 0
    for n in range(2, 21):
        neighbors = tuple(tuple(u for u in (v-1, v+1) if 0 <= u < n) for v in range(n))
        for q in range(3, 10):
            cases += 1
            word = (0,)+tuple(-(v-1) % q for v in range(1, n))
            endpoint = (q-1)*(n-2)
            tau, infinity = arrivals(word, neighbors, q)
            require(max(tau) == endpoint, "sharp_path_shortest_distance")
            x = word
            for time in range(endpoint+q+1):
                expected = tuple((word[v]+max(0, time-tau[v])) % q for v in range(n))
                require(x == expected, "sharp_path_literal_trajectory")
                x = advance(x, neighbors, q)
    return cases


def main():
    digest = hashlib.sha256()
    dynamics = dynamic_checks(digest)
    static = static_checks(digest)
    paths = sharp_family_checks()
    print(json.dumps({"status": "PASS_BOUNDED_AUTHOR_PROOF_PRESSURE_NOT_INDEPENDENT_REVIEW",
                      "dynamics": dynamics, "total_cover_extrema": static,
                      "sharp_path_cases": paths, "checks": dict(sorted(CHECKS.items())),
                      "total_checks": sum(CHECKS.values()),
                      "enumeration_sha256": digest.hexdigest(),
                      "external_status": "HOLD_EXTERNAL"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
