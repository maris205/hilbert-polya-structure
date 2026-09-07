#!/usr/bin/env python3
"""Independent P205 B: time-expanded paths, SCCs, old-conflict edge sets.

Standard library only; no file reads, subprocesses, random draws, or imports
from the author, candidate gate, Review A, or any earlier paper.  Stdout is
the complete deterministic certificate summary, not a preloaded transcript.
"""
from collections import Counter, deque
from hashlib import sha256
from itertools import combinations, product
import json


CHECKS = Counter()


def require(test, kind, witness=None):
    CHECKS[kind] += 1
    if not test:
        raise AssertionError((kind, witness))


def encode(x, q):
    z = 0
    for a in x:
        z = q * z + a
    return z


def literal(x, edges, q):
    """Compute old monochromatic EDGES first, then their endpoints."""
    conflict = 0
    active = 0
    for j, (u, v) in enumerate(edges):
        if x[u] == x[v]:
            conflict |= 1 << j
            active |= (1 << u) | (1 << v)
    return tuple((a + ((active >> v) & 1)) % q
                 for v, a in enumerate(x)), active, conflict


def components(n, edges):
    rows = [[] for _ in range(n)]
    for u, v in edges:
        rows[u].append(v)
        rows[v].append(u)
    seen, result = set(), []
    for root in range(n):
        if root in seen:
            continue
        seen.add(root)
        stack, comp = [root], 0
        while stack:
            u = stack.pop()
            comp |= 1 << u
            for v in rows[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        result.append(comp)
    return result


def path_layers(x, edges, q):
    """Boolean coefficients of ALL seeded walks by total edge weight.

    R[t] = (seed if t=0) union sum_{r>0} R[t-r] A[r],
    closed under A[0]. First nonzero coefficient at a vertex is its
    distance. The horizon uses n-1, not the asserted sharp n-2 bound.
    There is no Floyd update, relaxation queue, or activation simulation.
    """
    n = len(x)
    matrices = [[0] * n for _ in range(q)]
    seeds = 0
    for u, v in edges:
        r = (x[v] - x[u]) % q
        matrices[r][u] |= 1 << v
        matrices[(-r) % q][v] |= 1 << u
        if r == 0:
            seeds |= (1 << u) | (1 << v)

    def multiply(bits, matrix):
        out = 0
        while bits:
            bit = bits & -bits
            bits -= bit
            out |= matrix[bit.bit_length() - 1]
        return out

    layers, distances = [], [None] * n
    for t in range((q - 1) * max(n - 1, 0) + 1):
        current = seeds if t == 0 else 0
        for r in range(1, min(q - 1, t) + 1):
            current |= multiply(layers[t - r], matrices[r])
        while True:
            closed = current | multiply(current, matrices[0])
            if closed == current:
                break
            current = closed
        layers.append(current)
        for v in range(n):
            if distances[v] is None and (current >> v) & 1:
                distances[v] = t
    return tuple(distances), seeds


def scc_clock(successor):
    """Kosaraju SCCs, then reverse BFS from the cyclic SCCs.

    Does not remove zero-indegree states or trace one orbit per source.
    Every singleton SCC is tested for its self-loop explicitly.
    """
    size = len(successor)
    reverse = [[] for _ in range(size)]
    for u, v in enumerate(successor):
        reverse[v].append(u)
    seen, finish = bytearray(size), []
    for root in range(size):
        if seen[root]:
            continue
        seen[root] = 1
        stack = [(root, False)]
        while stack:
            u, closing = stack.pop()
            if closing:
                finish.append(u)
                continue
            stack.append((u, True))
            v = successor[u]
            if not seen[v]:
                seen[v] = 1
                stack.append((v, False))
    assigned = [-1] * size
    groups = []
    for root in reversed(finish):
        if assigned[root] != -1:
            continue
        number = len(groups)
        assigned[root] = number
        stack, group = [root], []
        while stack:
            u = stack.pop()
            group.append(u)
            for v in reverse[u]:
                if assigned[v] == -1:
                    assigned[v] = number
                    stack.append(v)
        groups.append(group)
    depths, periods, queue = [-1] * size, [0] * size, deque()
    cycle_count = 0
    for group in groups:
        if len(group) > 1 or successor[group[0]] == group[0]:
            cycle_count += 1
            for u in group:
                depths[u], periods[u] = 0, len(group)
                queue.append(u)
    while queue:
        u = queue.popleft()
        for v in reverse[u]:
            if depths[v] == -1:
                depths[v], periods[v] = depths[u] + 1, periods[u]
                queue.append(v)
    require(all(d >= 0 for d in depths), "scc_complete")
    return depths, periods, cycle_count


def inverse_edges(y, edges, q):
    """Enumerate subsets C of the target's monochromatic EDGES.

    Only endpoints(C) may have advanced. Validate whether ALL old edges
    have equality exactly on C. Never enumerate selected/held vertex sets.
    """
    mono_positions = [j for j, (u, v) in enumerate(edges) if y[u] == y[v]]
    answers, trials = set(), 0
    for edge_choice in range(1 << len(mono_positions)):
        trials += 1
        chosen_edges, endpoint_bits = 0, 0
        for k, j in enumerate(mono_positions):
            if (edge_choice >> k) & 1:
                chosen_edges |= 1 << j
                u, v = edges[j]
                endpoint_bits |= (1 << u) | (1 << v)
        x = tuple((a - ((endpoint_bits >> v) & 1)) % q
                  for v, a in enumerate(y))
        valid = all((x[u] == x[v]) == bool((chosen_edges >> j) & 1)
                    for j, (u, v) in enumerate(edges))
        if valid:
            code = encode(x, q)
            require(code not in answers, "edge_decoder_injective",
                    (y, edges, chosen_edges))
            answers.add(code)
    return answers, trials


def bound_m(n):
    return 1 if n <= 2 else 4 if n == 3 else (1 << (n - 1)) - 1


def is_star(n, edges):
    if len(edges) != n - 1:
        return False
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    return sorted(degree) == [1] * (n - 1) + [n - 1]


def dynamic_box(n, q):
    possible = list(combinations(range(n), 2))
    states = list(product(range(q), repeat=n))
    transcript = sha256()
    height_hist, period_hist, fibre_hist = Counter(), Counter(), Counter()
    totals = Counter()
    for graph_code in range(1 << len(possible)):
        edges = tuple(e for j, e in enumerate(possible) if (graph_code >> j) & 1)
        comp = components(n, edges)
        outputs = [literal(x, edges, q) for x in states]
        successors = [encode(z, q) for z, _, _ in outputs]
        buckets = [set() for _ in states]
        for u, v in enumerate(successors):
            buckets[v].add(u)
        depths, periods, cycle_count = scc_clock(successors)
        totals["cycles"] += cycle_count
        totals["graphs"] += 1
        edge_seed_classes = {}
        for code, x in enumerate(states):
            distances, seeds = path_layers(x, edges, q)
            finite = [d for d in distances if d is not None]
            h = max(finite, default=0)
            require(depths[code] == h, "exact_entrance", (n, q, graph_code, x))
            require(periods[code] == (q if seeds else 1), "exact_period")
            active = outputs[code][1]
            core = all((active & c) in (0, c) for c in comp)
            require((depths[code] == 0) == core, "component_core")
            require(h <= (q - 1) * max(n - 2, 0), "height_upper")
            actual, first = code, [None] * n
            for t in range(h + 2 * q + 2):
                predicted = tuple((a + max(0, t - distances[v])) % q
                                  if distances[v] is not None else a
                                  for v, a in enumerate(x))
                require(states[actual] == predicted, "all_time_window")
                actual_active = outputs[actual][1]
                threshold = sum(1 << v for v, d in enumerate(distances)
                                if d is not None and t >= d)
                require(actual_active == threshold, "activation_threshold")
                for v in range(n):
                    if first[v] is None and (actual_active >> v) & 1:
                        first[v] = t
                actual = successors[actual]
            require(tuple(first) == distances, "first_conflict")
            decoded, trials = inverse_edges(x, edges, q)
            totals["edge_candidates"] += trials
            require(decoded == buckets[code], "whole_source_set")
            require(len(decoded) <= bound_m(n), "global_fibre_bound")
            if n >= 3:
                expected_max = (len(set(x)) == 1 and
                                (len(edges) == 3 if n == 3 else is_star(n, edges)))
                require((len(decoded) == bound_m(n)) == expected_max,
                        "all_equality_targets")
            height_hist[h] += 1
            period_hist[periods[code]] += 1
            fibre_hist[len(decoded)] += 1
            record = [graph_code, code, successors[code], distances,
                      depths[code], periods[code], sorted(decoded)]
            transcript.update((json.dumps(record, separators=(",", ":")) + "\n").encode())
        require(sum(map(len, buckets)) == len(states), "fibre_mass")
    totals["states_and_targets"] = totals["graphs"] * len(states)
    require(max(height_hist) == (q - 1) * max(n - 2, 0), "global_height_attained")
    require(max(fibre_hist) == bound_m(n), "global_fibre_attained")
    return {"n": n, "q": q, **dict(totals),
            "height_histogram": dict(sorted(height_hist.items())),
            "eventual_period_histogram": dict(sorted(period_hist.items())),
            "fibre_histogram": dict(sorted(fibre_hist.items())),
            "full_state_record_sha256": transcript.hexdigest()}


def static_cases():
    result = []
    for n in range(6):
        all_edges = list(combinations(range(n), 2))
        histogram, digest, candidates = Counter(), sha256(), 0
        for code in range(1 << len(all_edges)):
            edges = tuple(e for j, e in enumerate(all_edges) if (code >> j) & 1)
            decoded, trials = inverse_edges((0,) * n, edges, 3)
            candidates += trials
            number = len(decoded)
            require(number <= bound_m(n), "static_cover_bound")
            if n >= 3:
                expected = len(edges) == 3 if n == 3 else is_star(n, edges)
                require((number == bound_m(n)) == expected, "static_equality_graph")
            histogram[number] += 1
            digest.update(f"{code}:{number}\n".encode())
        result.append({"n": n, "graphs": 1 << len(all_edges),
                       "edge_candidates": candidates,
                       "count_histogram": dict(sorted(histogram.items())),
                       "graph_count_record_sha256": digest.hexdigest()})
    boundary = {
        "star": ((0, 1), (0, 2), (0, 3)),
        "path": ((0, 1), (1, 2), (2, 3)),
        "paw": ((0, 1), (1, 2), (0, 2), (2, 3)),
        "cycle": ((0, 1), (1, 2), (2, 3), (0, 3)),
        "diamond": ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3)),
        "complete": tuple(combinations(range(4), 2)),
    }
    counts = {name: len(inverse_edges((0,) * 4, edges, 3)[0])
              for name, edges in boundary.items()}
    require(counts == dict(zip(boundary, (7, 4, 6, 5, 6, 5))), "four_vertex_boundary")
    p4 = boundary["path"]
    independent = [frozenset(v for v, bit in enumerate(bits) if bit)
                   for bits in product((0, 1), repeat=4)
                   if all(not (bits[u] and bits[v]) for u, v in p4)]
    contain_counts = [sum(v in s for s in independent) for v in range(4)]
    require(len(independent) == 8 and min(contain_counts) == 2,
            "p4_independent_set_bound")
    return {"all_labelled_graphs": result, "connected_four_boundary": counts,
            "p4_independent_sets_containing_vertex": contain_counts}


def sharp_families():
    digest, cases, maximum = sha256(), 0, 0
    for n in range(2, 41):
        edges = tuple((u, u + 1) for u in range(n - 1))
        for q in range(3, 12):
            x = (0, 0) + tuple(-(i - 1) % q for i in range(2, n))
            distances, _ = path_layers(x, edges, q)
            expected = (0, 0) + tuple((q - 1) * (i - 1) for i in range(2, n))
            require(distances == expected, "sharp_path_distances")
            z = x
            for t in range(expected[-1] + q + 1):
                active = literal(z, edges, q)[1]
                require(active == sum(1 << v for v, d in enumerate(expected) if d <= t),
                        "sharp_path_literal_activation")
                z = literal(z, edges, q)[0]
            digest.update((json.dumps([n, q, distances], separators=(",", ":")) + "\n").encode())
            maximum = max(maximum, expected[-1])
            cases += 1
    stars = []
    for n in range(3, 15):
        edges = tuple((0, v) for v in range(1, n))
        count = len(inverse_edges((0,) * n, edges, 3)[0])
        require(count == (1 << (n - 1)) - 1, "larger_star_fibres")
        stars.append([n, count])
    return {"path_n": [2, 40], "path_q": [3, 11], "path_cases": cases,
            "largest_checked_entrance": maximum,
            "path_record_sha256": digest.hexdigest(), "constant_star_fibres": stars}


def controls():
    path = ((0, 1), (1, 2))
    x1, x2 = (0, 0, 1), (0, 0, 2)
    d1, s1 = path_layers(x1, path, 3)
    d2, s2 = path_layers(x2, path, 3)
    require(s1 == s2 and d1 != d2, "control_seed_mask_not_clock")
    require(d1 == (0, 0, 1) and d2 == (0, 0, 2), "control_weight_orientation")
    require(literal(x1, path, 3)[0] == (1, 1, 1), "control_first_conflict_not_increment")
    require(literal((1, 1, 1), path, 3)[0] == (2, 2, 2), "control_increment_next_step")
    mutants = [
        ("omit_cover", ((0, 1),), (0, 0), frozenset()),
        ("omit_internal_neighbour", ((0, 1),), (0, 0), frozenset((0,))),
        ("omit_predecessor_closure", path, (0, 1, 1), frozenset((1, 2))),
    ]
    mutant_records = []
    for label, edges, target, selected in mutants:
        source = tuple((a - (v in selected)) % 3 for v, a in enumerate(target))
        actual = literal(source, edges, 3)[0]
        require(actual != target, "negative_" + label)
        mutant_records.append({"omission": label, "edges": edges, "target": target,
                               "selected": sorted(selected), "false_source": source,
                               "actual_image": actual})
    # Same H, different directed target relation changes the whole fibre.
    y1, y2 = (0, 1, 1), (0, 2, 2)
    f1, f2 = inverse_edges(y1, path, 3)[0], inverse_edges(y2, path, 3)[0]
    require(len(f1) != len(f2), "control_total_cover_only_not_decoder")
    # Ordinary CCA on the same constant K2 holds; CCI has a q-cycle.
    require(literal((0, 0), ((0, 1),), 3)[0] == (1, 1), "control_cca_separator")
    # P202 has a non-power-of-three period; CCI has only 1 or q.
    # The P205 star size-seven fibre also blocks a permutation conjugacy
    # to P202's same-length power-of-two-only one-step fibre census.
    require(len(inverse_edges((0,) * 4, ((0, 1), (0, 2), (0, 3)), 3)[0]) == 7,
            "control_nonbinary_product_fibre")
    return {"same_seed_different_distances": [list(d1), list(d2)],
            "same_H_targets": [y1, y2], "same_H_fibre_sizes": [len(f1), len(f2)],
            "omitted_condition_counterexamples": mutant_records,
            "cca_constant_edge": {"source": [0, 0], "CCI": [1, 1], "CCA": [0, 0]}}


def main():
    boxes = [dynamic_box(n, q) for n in range(5) for q in (3, 5, 6)]
    boxes.append(dynamic_box(5, 3))
    static = static_cases()
    sharp = sharp_families()
    negative = controls()
    output = {"review": "P205 manuscript B / frozen_round1",
              "status": "PASS_FINITE_CHECKS_NOT_ALL_PARAMETER_PROOF",
              "methods": ["Boolean total-weight walk layers", "Kosaraju SCC and reverse BFS",
                          "old conflict EDGE subset source reconstruction"],
              "complete_dynamic_boxes": boxes, "static_audit": static,
              "sharp_witness_families": sharp, "negative_and_adapter_controls": negative,
              "assertion_counts": dict(sorted(CHECKS.items())),
              "total_assertions": sum(CHECKS.values()),
              "scope": "All listed labelled graphs, all their states and target SOURCE SETS; no all-size inference from cutoffs."}
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
