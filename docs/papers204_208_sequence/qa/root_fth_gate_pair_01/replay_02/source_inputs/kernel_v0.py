#!/usr/bin/env python3
"""Independent FTH gate kernel, committed before author proof/code reading.

Source construction: canonical set partitions with injective block destinations.
Only complete original carriers n=0,...,5. No author implementation imports.
"""
import itertools
import json
import math

CHECKS = 0


def require(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def partitions(n):
    """Each set partition once, with blocks ordered by their least element."""
    def extend(i, blocks):
        if i == n:
            yield blocks
            return
        for j in range(len(blocks)):
            yield from extend(i + 1, blocks[:j] + (blocks[j] + (i,),) + blocks[j + 1:])
        yield from extend(i + 1, blocks + ((i,),))
    yield from extend(0, ())


def all_maps_from_partition_destinations(n):
    transitions = {}
    for blocks in partitions(n):
        for destinations in itertools.permutations(range(n), len(blocks)):
            source = [-1] * n
            target = [-1] * n
            for block, destination in zip(blocks, destinations):
                for i in block:
                    source[i] = destination
                for left, right in zip(block, block[1:]):
                    target[left] = right
                target[block[-1]] = destination
            f, g = tuple(source), tuple(target)
            require(f not in transitions, ("duplicate_partition_destination_code", n, f))
            require(all(0 <= x < n for x in f + g), ("carrier", n, f, g))
            transitions[f] = g
    require(len(transitions) == (n ** n if n else 1), ("full_carrier_mass", n))
    return transitions


def coordinate_literal(f):
    return tuple(next((j for j in range(i + 1, len(f)) if f[j] == destination), destination)
                 for i, destination in enumerate(f))


def normalize_cycle(cycle):
    where = min(range(len(cycle)), key=cycle.__getitem__)
    return tuple(cycle[where:] + cycle[:where])


def whole_function_graph(transitions):
    depth, period, representative, cycles = {}, {}, {}, {}
    for start in sorted(transitions):
        if start in depth:
            continue
        path, positions = [], {}
        current = start
        while current not in depth and current not in positions:
            positions[current] = len(path)
            path.append(current)
            current = transitions[current]
        if current in positions:
            split = positions[current]
            cycle = normalize_cycle(path[split:])
            key = cycle[0]
            cycles[key] = cycle
            for vertex in cycle:
                depth[vertex] = 0
                period[vertex] = len(cycle)
                representative[vertex] = key
            prefix = path[:split]
        else:
            prefix = path
        for vertex in reversed(prefix):
            following = transitions[vertex]
            depth[vertex] = depth[following] + 1
            period[vertex] = period[following]
            representative[vertex] = representative[following]
    return depth, period, representative, [cycles[k] for k in sorted(cycles)]


def underlying_cycle_geometry(f):
    n = len(f)
    indegree = [0] * n
    for target in f:
        indegree[target] += 1
    remaining_indegree = indegree[:]
    queue = [i for i in range(n) if remaining_indegree[i] == 0]
    for i in queue:
        remaining_indegree[f[i]] -= 1
        if remaining_indegree[f[i]] == 0:
            queue.append(f[i])
    cycle_vertices = {i for i in range(n) if remaining_indegree[i] > 0}
    unseen = set(cycle_vertices)
    cycles, owner = [], {}
    while unseen:
        head = min(unseen)
        cycle, current = [], head
        while not cycle or current != head:
            cycle.append(current)
            unseen.remove(current)
            current = f[current]
        normalized = normalize_cycle(cycle)
        number = len(cycles)
        cycles.append(normalized)
        for i in normalized:
            owner[i] = number
    attachments = [(i, f[i], owner[f[i]]) for i in range(n)
                   if i not in cycle_vertices and f[i] in cycle_vertices]
    valid = (all(indegree[i] <= 1 for i in range(n) if i not in cycle_vertices)
             and all(indegree[i] <= 2 for i in cycle_vertices)
             and all(i < min(cycles[number]) for i, target, number in attachments))
    predicted_period = math.lcm(*(len(cycles[number]) for i, target, number in attachments))
    rotated = list(f)
    if valid:
        for tail_final, attachment, number in attachments:
            cycle = cycles[number]
            rotated[tail_final] = cycle[(cycle.index(attachment) - 1) % len(cycle)]
    return valid, predicted_period, tuple(rotated), cycles, attachments


def inverse_by_increasing_path_covers(g):
    n = len(g)
    eligible = [i for i in range(n) if i < g[i]]
    require(len(eligible) <= max(0, n - 1), ("eligible_edge_bound", g))
    decoded, codes = [], []
    for bits in range(1 << len(eligible)):
        selected = {eligible[j] for j in range(len(eligible)) if bits >> j & 1}
        incoming = {g[i] for i in selected}
        if len(incoming) != len(selected):
            continue
        paths = []
        covered = set()
        for head in range(n):
            if head in incoming:
                continue
            path, current = [], head
            while True:
                require(current not in covered, ("path_cover_disjoint", g, bits, current))
                covered.add(current)
                path.append(current)
                if current not in selected:
                    break
                current = g[current]
            paths.append(tuple(path))
        require(covered == set(range(n)), ("path_cover_total", g, bits))
        destinations = [g[path[-1]] for path in paths]
        if len(set(destinations)) != len(destinations):
            continue
        source = [-1] * n
        for path, destination in zip(paths, destinations):
            for i in path:
                source[i] = destination
        f = tuple(source)
        require(coordinate_literal(f) == g, ("decoded_literal", g, bits, f))
        decoded.append(f)
        codes.append({"selected_sources": sorted(selected),
                      "paths": [list(path) for path in paths],
                      "destinations": destinations, "source": list(f)})
    require(len(decoded) == len(set(decoded)), ("nonredundant_inverse", g))
    return sorted(decoded), codes


def vertex_image_checks(f, g):
    n = len(f)
    old_image = new_image = set(range(n))
    for k in range(n + 1):
        require(old_image <= new_image, ("iterated_vertex_image_inclusion", f, g, k))
        old_image = {f[i] for i in old_image}
        new_image = {g[i] for i in new_image}
    for source, destination in enumerate(f):
        current = g[source]
        steps = 1
        while current != destination and steps <= n:
            current = g[current]
            steps += 1
        require(current == destination, ("old_arc_path_expansion", f, g, source))


def run():
    rows = []
    for n in range(6):
        transitions = all_maps_from_partition_destinations(n)
        states = sorted(transitions)
        fibres = {target: [] for target in states}
        for source, target in transitions.items():
            require(coordinate_literal(source) == target, ("partition_vs_coordinate", source))
            fibres[target].append(source)
            vertex_image_checks(source, target)
        for target in fibres:
            fibres[target].sort()
        depth, periods, representatives, function_cycles = whole_function_graph(transitions)
        entries = []
        for target in states:
            decoded, codes = inverse_by_increasing_path_covers(target)
            require(decoded == fibres[target], ("complete_target_inverse", target))
            valid, predicted_period, rotated, cycles, attachments = underlying_cycle_geometry(target)
            require(valid == (depth[target] == 0), ("exact_recurrent_carrier", target))
            if valid:
                require(predicted_period == periods[target], ("exact_labelled_period", target))
                require(rotated == transitions[target], ("tail_attachment_rotation", target))
            entries.append({
                "state": list(target), "transition": list(transitions[target]),
                "predecessors": [list(source) for source in decoded],
                "inverse_codes": codes, "entrance_depth": depth[target],
                "eventual_period": periods[target],
                "eventual_cycle_representative": list(representatives[target]),
                "recurrent_geometry": valid,
                "recurrent_predicted_period": predicted_period if valid else None,
                "underlying_directed_cycles": [list(cycle) for cycle in cycles],
                "tail_attachments": [list(item) for item in attachments],
            })
        maximum = max(map(len, fibres.values()))
        maximizers = [target for target in states if len(fibres[target]) == maximum]
        successor = tuple((i + 1) % n for i in range(n))
        expected_maximum = 1 << (n - 1) if n else 1
        require(maximum == expected_maximum, ("sharp_maximum", n, maximum))
        require(maximizers == [successor], ("unique_cyclic_successor_maximizer", n, maximizers))
        require(sum(map(len, fibres.values())) == len(states), ("all_target_mass", n))
        rows.append({
            "n": n, "state_count": len(states),
            "decoded_source_count": sum(map(len, fibres.values())),
            "recurrent_state_count": sum(depth[state] == 0 for state in states),
            "observed_maximum_entrance_depth_not_all_size_theorem": max(depth.values()),
            "maximum_one_step_fibre": maximum,
            "all_maximizers": [list(target) for target in maximizers],
            "complete_whole_function_cycles": [[list(state) for state in cycle]
                                               for cycle in function_cycles],
            "complete_transitions_sources_geometry_and_inverse_codes": entries,
        })
    result = {
        "kind": "INDEPENDENT_FTH_CANDIDATE_GATE_FULL_ORIGINAL_BOXES",
        "source_constructor": "CANONICAL_SET_PARTITIONS_WITH_INJECTIVE_DESTINATION_ASSIGNMENTS",
        "boxes": list(range(6)), "total_states": sum(row["state_count"] for row in rows),
        "total_decoded_sources": sum(row["decoded_source_count"] for row in rows),
        "checks": CHECKS, "excluded_claim": "NO_ALL_SIZE_ENTRANCE_CLOCK_THEOREM",
        "rows": rows,
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    run()
