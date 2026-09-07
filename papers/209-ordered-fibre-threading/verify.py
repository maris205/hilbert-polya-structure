#!/usr/bin/env python3
"""Fresh P209 author checker. Fixed original boxes n=0,...,5; no local imports.

The literal tuple-product transition, brute whole-function orbit, graph
predicate, and target subset decoder are separately computed. Complete JSON
stdout is the canonical payload; this program never reads a canonical file.
Runtime observation belongs to the separately pinned execution bootstrap.
"""

from itertools import product
from math import lcm
import json


CHECKS = 0


def require(test, label, *witness):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError((label, witness))


def thread(f):
    """Simultaneous old-fibre replacement; no theorem used."""
    g = list(f)
    for value in range(len(f)):
        members = [i for i, v in enumerate(f) if v == value]
        for left, right in zip(members, members[1:]):
            g[left] = right
        if members:
            g[members[-1]] = value
    return tuple(g)


def images(f):
    current = set(range(len(f)))
    result = [tuple(sorted(current))]
    for unused in range(len(f) + 1):
        current = {f[i] for i in current}
        result.append(tuple(sorted(current)))
    return result


def components(f):
    remaining = set(range(len(f)))
    answer = []
    while remaining:
        found = {min(remaining)}
        frontier = list(found)
        while frontier:
            i = frontier.pop()
            neighbours = {f[i]} | {j for j, v in enumerate(f) if v == i}
            for j in neighbours - found:
                found.add(j)
                frontier.append(j)
        remaining -= found
        answer.append(tuple(sorted(found)))
    return tuple(sorted(answer))


def graph_data(f):
    n = len(f)
    indegree = [f.count(i) for i in range(n)]
    residual = indegree[:]
    pending = [i for i in range(n) if residual[i] == 0]
    stripped = set()
    while pending:
        i = pending.pop()
        stripped.add(i)
        residual[f[i]] -= 1
        if residual[f[i]] == 0:
            pending.append(f[i])
    cycle_vertices = set(range(n)) - stripped
    cycles = []
    unvisited = set(cycle_vertices)
    while unvisited:
        start = min(unvisited)
        cyc, i = [start], f[start]
        while i != start:
            cyc.append(i)
            i = f[i]
        unvisited -= set(cyc)
        cycles.append(tuple(cyc))
    cycle_index = {v: k for k, cyc in enumerate(cycles) for v in cyc}
    finals = [i for i in stripped if f[i] in cycle_vertices]
    valid = all(indegree[i] <= 1 for i in stripped)
    valid = valid and all(indegree[i] <= 2 for i in cycle_vertices)
    valid = valid and all(i < min(cycles[cycle_index[f[i]]]) for i in finals)
    attached = sorted({cycle_index[f[i]] for i in finals})
    predicted_period = lcm(*(len(cycles[k]) for k in attached)) if valid else None
    paths = []
    if valid:
        for start in sorted(i for i in stripped if indegree[i] == 0):
            path, i = [], start
            while i not in cycle_vertices:
                path.append(i)
                i = f[i]
            paths.append({"vertices": path, "attachment": i})
        require(sum(len(p["vertices"]) for p in paths) == len(stripped),
                "geometry_paths_cover_noncycle", f)
    return {"cycles": cycles, "cycle_vertices": sorted(cycle_vertices),
            "indegree": indegree, "paths": paths, "finals": sorted(finals),
            "recurrent_predicate": valid, "predicted_period": predicted_period}


def whole_orbit(f, transition):
    seen, orbit = {}, []
    current = f
    while current not in seen:
        seen[current] = len(orbit)
        orbit.append(current)
        current = transition[current]
    mu = seen[current]
    return mu, len(orbit) - mu, orbit


def decode(g):
    eligible = [i for i, v in enumerate(g) if i < v]
    codes = []
    for mask in range(1 << len(eligible)):
        selected = {i for bit, i in enumerate(eligible) if mask & (1 << bit)}
        heads = [g[i] for i in selected]
        endpoints = [i for i in range(len(g)) if i not in selected]
        targets = [g[i] for i in endpoints]
        if len(heads) != len(set(heads)) or len(targets) != len(set(targets)):
            continue
        source, end_for_vertex = [], []
        for i in range(len(g)):
            end = i
            while end in selected:
                require(g[end] > end, "decoder_increasing", g, mask, end)
                end = g[end]
            end_for_vertex.append(end)
            source.append(g[end])
        source = tuple(source)
        recovered = {i for i in range(len(g))
                     if any(j > i and source[j] == source[i] for j in range(len(g)))}
        require(recovered == selected, "code_recovery", g, mask, source)
        require(thread(source) == g, "decoded_literal_transition", g, mask, source)
        codes.append({"selected": sorted(selected), "endpoints": end_for_vertex,
                      "source": source})
    return eligible, codes


def run_box(n):
    initial_checks = CHECKS
    states = list(product(range(n), repeat=n))
    transition = {f: thread(f) for f in states}
    preimages = {f: [] for f in states}
    for f, g in transition.items():
        require(g in transition, "carrier", n, f, g)
        preimages[g].append(f)
    rows = []
    recurrent_count = 0
    period_census = {}
    fibre_census = {}
    maxima = []
    maximum = max(len(v) for v in preimages.values())
    for f in states:
        g = transition[f]
        graph = graph_data(f)
        old_images, new_images = images(f), images(g)
        for depth, (old, new) in enumerate(zip(old_images, new_images)):
            require(set(old) <= set(new), "all_images_monotone", f, depth)
        require(components(f) == components(g), "weak_components_preserved", f)
        for j in range(n):
            fibre = [i for i in range(n) if f[i] == f[j]]
            formula = int(j in f) + int(j != min(fibre))
            require(g.count(j) == formula, "indegree_identity", f, j)
        for i in range(n):
            require(g[i] == f[i] or g[i] > i, "changed_arrows_increase", f, i)
        mu, period, orbit = whole_orbit(f, transition)
        is_recurrent = mu == 0
        require(is_recurrent == graph["recurrent_predicate"], "exact_recurrent_set", f)
        if is_recurrent:
            recurrent_count += 1
            period_census[period] = period_census.get(period, 0) + 1
            require(period == graph["predicted_period"], "exact_labelled_period", f)
            cyc = set(graph["cycle_vertices"])
            cyc_previous = {f[i]: i for i in cyc}
            for state in orbit:
                require(images(state) == old_images, "all_images_frozen", f, state)
            for i in range(n):
                expected = cyc_previous[f[i]] if i not in cyc and f[i] in cyc else f[i]
                require(g[i] == expected, "attachment_rotation_only", f, i)
            for value in range(n):
                fibre = [i for i in range(n) if f[i] == value]
                for i in fibre[1:]:
                    require(i in cyc, "nonfirst_fibre_member_on_cycle", f, value, i)
        eligible, codes = decode(f)
        decoded_sources = sorted(tuple(c["source"]) for c in codes)
        require(decoded_sources == preimages[f], "complete_target_source_set", f)
        require(len(decoded_sources) == len(set(decoded_sources)), "nonredundancy", f)
        size = len(preimages[f])
        require(size <= (1 << max(n - 1, 0)), "global_bound", f)
        fibre_census[size] = fibre_census.get(size, 0) + 1
        if size == maximum:
            maxima.append(f)
        rows.append({"state": f, "image": g, "vertex_images": old_images,
                     "graph": graph, "entrance_steps_observed": mu,
                     "whole_function_period": period, "whole_orbit": orbit,
                     "eligible": eligible, "inverse_codes": codes,
                     "literal_predecessors": preimages[f], "fibre_size": size})
    successor = tuple(range(1, n)) + ((0,) if n else ())
    require(maximum == (1 << max(n - 1, 0)), "sharp_maximum", n)
    require(maxima == [successor], "unique_maximizer", n, maxima)
    require(sum(len(v) for v in preimages.values()) == len(states), "fibre_mass", n)
    return {"n": n, "state_count": len(states), "checks": CHECKS - initial_checks,
            "recurrent_count": recurrent_count,
            "recurrent_period_census": sorted(period_census.items()),
            "fibre_census": sorted(fibre_census.items()), "maximum_fibre": maximum,
            "maximizing_targets": maxima, "rows": rows}


def main():
    require(thread((1, 2, 1)) == (2, 2, 1), "ring_distance_witness_first")
    require(thread((2, 2, 1)) == (1, 2, 1), "ring_distance_witness_return")
    require(thread((0, 0)) == (1, 0) and thread((1, 1)) == (1, 1),
            "same_kernel_different_images")
    require(thread((2, 2, 2)) == (1, 2, 2), "new_sibling_edge_forward_orbit_witness")
    boxes = [run_box(n) for n in range(6)]
    result = {"schema": "p209-author-v1", "status": "PASS", "checks": CHECKS,
              "boxes": boxes, "total_states": sum(b["state_count"] for b in boxes),
              "scope": "Exhaustive n=0,...,5 only; finite pressure, not all-size proof.",
              "entrance_field_scope": "Observed orbit index only; no all-size clock claim."}
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
