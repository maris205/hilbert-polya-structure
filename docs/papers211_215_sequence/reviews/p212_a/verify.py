#!/usr/bin/env python3
"""P212 Review A: standalone SOURCE preparation, not executed at preparation.

No imports, file reads, canonical reads, environment reads, or subprocesses.
Fixed carriers only. Root must accept this complete source and separately bind
an actual invocation. Numeric state indices are little-endian, zero-based.
Observed side: two slot swaps. Expected side: cyclic visit words reconstructed
by most-recent arrivals, plus an independent edge-orientation feasibility census.
"""

PARAMETERS = {
    "schema": "P212_A_PARAMETERS_V1",
    "carrier_sizes": [1, 2, 3, 4],
    "label_base": 0,
    "state_order": "little_endian_base_n_u_v_f0_through_f_n_minus_1",
    "core_sizes": [1, 2, 3, 4],
    "coefficient_scale": 24,
    "unexercised_first_sizes": [5, 6, 5],
    "imports": [],
    "data_inputs": [],
}


def wire(value):
    if type(value) is bool:
        return "true" if value else "false"
    if type(value) is int:
        return str(value)
    if type(value) is str:
        if any(ord(c) < 32 or ord(c) > 126 for c in value):
            raise ValueError("wire strings must be printable ASCII")
        return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'
    if type(value) in (list, tuple):
        return "[" + ",".join(wire(v) for v in value) + "]"
    if type(value) is dict and all(type(k) is str for k in value):
        return "{" + ",".join(wire(k) + ":" + wire(value[k]) for k in sorted(value)) + "}"
    raise TypeError("unsupported deterministic wire value")


def need(condition, message):
    if not condition:
        raise ValueError(message)


class Ledger:
    def __init__(self):
        self.rows = []

    def check(self, name, scope, observed, expected):
        passed = wire(observed) == wire(expected)
        self.rows.append([name, scope, observed, expected, passed])
        return passed


def factorial(n):
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def permutations(values):
    if not values:
        yield ()
    for i, first in enumerate(values):
        for tail in permutations(values[:i] + values[i + 1:]):
            yield (first,) + tail


def cuts(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in cuts(total - first, parts - 1):
                yield (first,) + tail


def digits(n, length, number):
    result = []
    for _ in range(length):
        result.append(number % n)
        number //= n
    need(number == 0, "out of range state rank")
    return tuple(result)


def rank(n, word):
    result, place = 0, 1
    for x in word:
        need(type(x) is int and 0 <= x < n, "invalid label")
        result += place * x
        place *= n
    return result


def successor(word):
    slots = list(word)
    memory_slot = 2 + slots[1]
    slots[0], slots[memory_slot] = slots[memory_slot], slots[0]
    slots[0], slots[1] = slots[1], slots[0]
    return tuple(slots)


def predecessor(word):
    slots = list(word)
    slots[0], slots[1] = slots[1], slots[0]
    memory_slot = 2 + slots[1]
    slots[0], slots[memory_slot] = slots[memory_slot], slots[0]
    return tuple(slots)


def edge(a, b):
    return (min(a, b), max(a, b))


def edges_from_paths(paths):
    return tuple(sorted(edge(a, b) for path in paths for a, b in zip(path, path[1:])))


def edges_from_state(word):
    return tuple(sorted([edge(word[0], word[1])] +
                        [edge(x, y) for x, y in enumerate(word[2:])]))


def vertices(mask, n):
    return tuple(x for x in range(n) if mask & (1 << x))


def inside(edges, mask):
    return tuple((a, b) for a, b in edges if mask & (1 << a) and mask & (1 << b))


def degree(edges, x):
    return sum((a == x) + (b == x) for a, b in edges)


def structural(word):
    n = len(word) - 2
    edges = edges_from_state(word)
    active = 1 << word[0]
    while True:
        enlarged = active
        for a, b in edges:
            if active & ((1 << a) | (1 << b)):
                enlarged |= (1 << a) | (1 << b)
        if enlarged == active:
            break
        active = enlarged
    # Different from leaf pruning: union every induced minimum-degree-two subset.
    admissible = []
    core = 0
    for mask in range(1 << n):
        if mask & active != mask:
            continue
        induced = inside(edges, mask)
        if all(degree(induced, x) >= 2 for x in vertices(mask, n)):
            admissible.append(mask)
            core |= mask
    need(core in admissible and core != 0, "two-core maximum not admissible")
    labels = vertices(core, n)
    core_edges = inside(edges, core)
    outside = tuple((x, word[x + 2]) for x in range(n) if x not in labels)
    return (labels, core_edges, outside), active, admissible


def primitive_necklace(word):
    word = tuple(word)
    need(bool(word), "empty closed visit word")
    for d in range(1, len(word) + 1):
        if len(word) % d == 0 and all(word[j] == word[j % d] for j in range(len(word))):
            word = word[:d]
            break
    return min(word[i:] + word[:i] for i in range(len(word)))


def concatenate_closed(paths):
    walk = [paths[0][0]]
    for path in paths:
        need(walk[-1] == path[0], "macro path endpoints do not meet")
        walk.extend(path[1:])
    need(walk[0] == walk[-1], "macro walk not closed")
    return primitive_necklace(walk[:-1])


def reconstruct(visit_word, phase, n, frozen):
    """Recover each core pointer from the last arrival at its source vertex."""
    memory = dict(frozen)
    length = len(visit_word)
    for x in set(visit_word):
        for age in range(length):
            j = (phase - age) % length
            if visit_word[j] == x:
                memory[x] = visit_word[(j - 1) % length]
                break
    need(sorted(memory) == list(range(n)), "visit reconstruction misses a label")
    return (visit_word[phase], visit_word[(phase + 1) % length],
            *(memory[x] for x in range(n)))


def cycle_words(family, paths):
    words = set()
    if family == 0:
        a, b = paths
        for aa in set((a, a[::-1])):
            for bb in set((b, b[::-1])):
                words.add(concatenate_closed((aa, bb, aa[::-1], bb[::-1])))
    elif family == 1:
        a, b, bridge = paths
        for aa in set((a, a[::-1])):
            for bb in set((b, b[::-1])):
                words.add(concatenate_closed((bridge, bb, bridge[::-1], aa,
                                               bridge, bb[::-1], bridge[::-1], aa[::-1])))
    else:
        for i, j, k in set(permutations(paths)):
            words.add(concatenate_closed((i, k[::-1], j, i[::-1], k, j[::-1])))
    return tuple(sorted(words))


def period_row(family, lengths):
    if family == 0:
        a, b = lengths
        if a == b == 1:
            return 0, 1, 1
        if max(a, b) <= 2:
            return 1, a + b, 1
        return 2, 2 * (a + b), 2 if min(a, b) >= 3 else 1
    if family == 1:
        a, b, c = lengths
        if max(a, b) <= 2:
            return 3, a + b + 2 * c, 1
        return 4, 2 * (a + b + 2 * c), 2 if min(a, b) >= 3 else 1
    direct = lengths.count(1)
    return (5, 2, 1) if direct == 3 else (6, 2 * sum(lengths), 1 if direct >= 2 else 2)


def incidence_assignments(s, edges):
    """Orient edge occurrences, then forget occurrence IDs in the actual state."""
    feasible = {}
    for extra, (a, b) in enumerate(edges):
        for u, v in sorted(set(((a, b), (b, a)))):
            stored = edges[:extra] + edges[extra + 1:]

            def assign(j, memory):
                if j == len(stored):
                    if sorted(memory) == list(range(s)):
                        state = (u, v, *(memory[x] for x in range(s)))
                        feasible[state] = feasible.get(state, 0) + 1
                    return
                aa, bb = stored[j]
                for tail, head in sorted(set(((aa, bb), (bb, aa)))):
                    if tail not in memory:
                        memory[tail] = head
                        assign(j + 1, memory)
                        del memory[tail]

            assign(0, {})
    return feasible


def make_catalogue(s, ledger):
    records = {}

    def receive(family, paths):
        paths = tuple(tuple(p) for p in paths)
        key = edges_from_paths(paths)
        descriptor = (family, paths)
        if key in records:
            need(records[key] == descriptor, "inconsistent canonical path presentation")
        records[key] = descriptor

    labels = tuple(range(s))
    for branch in labels:
        rest = tuple(x for x in labels if x != branch)
        for order in permutations(rest):
            for i in range(s):
                a = (branch,) + order[:i] + (branch,)
                b = (branch,) + order[i:] + (branch,)
                receive(0, sorted((min(a, a[::-1]), min(b, b[::-1]))))
    for a in labels:
        for b in labels:
            if a >= b:
                continue
            rest = tuple(x for x in labels if x not in (a, b))
            for order in permutations(rest):
                for i, j, k in cuts(s - 2, 3):
                    aa = (a,) + order[:i] + (a,)
                    bb = (b,) + order[i:i + j] + (b,)
                    bridge = (a,) + order[i + j:] + (b,)
                    receive(1, (min(aa, aa[::-1]), min(bb, bb[::-1]), bridge))
                    paths = ((a,) + order[:i] + (b,),
                             (a,) + order[i:i + j] + (b,),
                             (a,) + order[i + j:] + (b,))
                    receive(2, sorted(paths))
    result = []
    for edges, (family, paths) in sorted(records.items()):
        identifier = len(result)
        scope = [s, identifier]
        lengths = tuple(len(p) - 1 for p in paths)
        row, period, decorations = period_row(family, lengths)
        words = cycle_words(family, paths)
        feasibility = incidence_assignments(s, edges)
        word_states = []
        for visit in words:
            orbit = [reconstruct(visit, t, s, ()) for t in range(len(visit))]
            ledger.check("word_primitive_state_period", scope, len(set(orbit)), len(visit))
            ledger.check("word_swap_successors", scope,
                         [successor(w) for w in orbit], orbit[1:] + orbit[:1])
            ledger.check("word_exact_edges", scope,
                         sorted(set(edges_from_state(w) for w in orbit)), [edges])
            word_states.extend(orbit)
        ledger.check("word_incidence_exhaustion", scope, sorted(word_states), sorted(feasibility))
        ledger.check("word_decoration_count", scope, len(words), decorations)
        ledger.check("word_period_table", scope, [len(w) for w in words], [period] * decorations)
        result.append({"id": identifier, "edges": edges, "family": family,
                       "paths": paths, "lengths": lengths, "row": row,
                       "period": period, "decorations": decorations,
                       "visit_words": words,
                       "incidence_states": [[w, feasibility[w]] for w in sorted(feasibility)]})
    return result


def add_count(counts, key, amount=1):
    counts[key] = counts.get(key, 0) + amount


def polynomial(counts):
    return [[p, value] for p, value in sorted(counts.items()) if value]


def coefficient24(s):
    """Integer-scaled length sums, not Fraction/sparse rational-function code."""
    pieces = [{}, {}, {}]
    for a in range(1, s + 1):
        b = s + 1 - a
        if a == b == 1:
            p, weight = 1, 24
        elif max(a, b) <= 2:
            p, weight = a + b, 12
        else:
            p, weight = 2 * (a + b), 6
        add_count(pieces[0], p, weight)
    for a in range(1, s):
        for b in range(1, s + 1 - a):
            c = s + 1 - a - b
            p = a + b + 2 * c
            weight = 12 if max(a, b) <= 2 else 6
            if weight == 6:
                p *= 2
            add_count(pieces[1], p, weight)
    if s == 2:
        add_count(pieces[2], 2, 12)
    if s >= 3:
        for k, weight in ((1, 12), (2, 12), (3, 4)):
            if s - 2 >= k:
                for _ in cuts(s - 2 - k, k):
                    add_count(pieces[2], 2 * s + 2, weight)
    return pieces


def orbit_normal_form(ids):
    ids = tuple(ids)
    smallest = ids.index(min(ids))
    return ids[smallest:] + ids[:smallest]


def check_carrier(n, catalogues, ledger):
    states = [digits(n, n + 2, i) for i in range(n ** (n + 2))]
    arrows = [rank(n, successor(w)) for w in states]
    backwards = [rank(n, predecessor(w)) for w in states]
    incoming = [[] for _ in states]
    for i, target in enumerate(arrows):
        incoming[target].append(i)
    decomposed = [structural(w) for w in states]
    keys = sorted(set(item[0] for item in decomposed))
    key_id = {key: i for i, key in enumerate(keys)}
    expected = {}
    for mask in range(1, 1 << n):
        labels = vertices(mask, n)
        outside = tuple(x for x in range(n) if x not in labels)
        for entry in catalogues[len(labels)]:
            edges = tuple(sorted(edge(labels[a], labels[b]) for a, b in entry["edges"]))
            for code in range(n ** len(outside)):
                targets = digits(n, len(outside), code)
                frozen = tuple(zip(outside, targets))
                key = (labels, edges, frozen)
                need(key not in expected, "duplicate expected full group")
                expected[key] = entry
    ledger.check("complete_core_complement_groups", n, keys, sorted(expected))
    need(set(keys) == set(expected), "group mismatch prevents continued decoding")
    orbit_for = [-1] * len(states)
    orbits = []
    for seed in range(len(states)):
        if orbit_for[seed] != -1:
            continue
        route, local = [], set()
        current = seed
        while current not in local and orbit_for[current] == -1:
            local.add(current)
            route.append(current)
            current = arrows[current]
        ledger.check("first_repetition_is_seed", [n, len(orbits)], current, seed)
        need(current == seed, "literal graph has a transient")
        for i in route:
            orbit_for[i] = len(orbits)
        orbits.append(tuple(route))
    ledger.check("orbit_partition", n, sorted(i for route in orbits for i in route), list(range(len(states))))
    state_rows = []
    members = [[] for _ in keys]
    for i, word in enumerate(states):
        key, active, admissible = decomposed[i]
        labels, core_edges, frozen = key
        gid = key_id[key]
        members[gid].append(i)
        scope = [n, i]
        ledger.check("unit_predecessor", scope, incoming[i], [backwards[i]])
        ledger.check("inverse_both_directions", scope, [arrows[backwards[i]], backwards[arrows[i]]], [i, i])
        ledger.check("full_augmented_edges", scope, edges_from_state(states[arrows[i]]), edges_from_state(word))
        ledger.check("frozen_core_key", scope, decomposed[arrows[i]][0], key)
        ledger.check("register_membership", scope, [word[0] in labels, word[1] in labels], [True, True])
        ledger.check("active_excess", scope, len(inside(edges_from_state(word), active)), len(vertices(active, n)) + 1)
        ledger.check("core_excess_and_degrees", scope,
                     [len(core_edges) == len(labels) + 1, all(degree(core_edges, x) >= 2 for x in labels)],
                     [True, True])
        state_rows.append([i, word, arrows[i], backwards[i], gid, orbit_for[i], active, admissible])
    groups = []
    row_counts = [[0, 0, 0] for _ in range(7)]
    for gid, key in enumerate(keys):
        labels, edges, frozen = key
        entry = expected[key]
        expected_cycles = []
        for visit in entry["visit_words"]:
            relabelled = tuple(labels[x] for x in visit)
            ids = [rank(n, reconstruct(relabelled, t, n, frozen)) for t in range(len(visit))]
            expected_cycles.append(orbit_normal_form(ids))
        observed_ids = sorted(set(orbit_for[i] for i in members[gid]))
        actual_cycles = sorted(orbit_normal_form(orbits[j]) for j in observed_ids)
        ledger.check("complete_decorated_orbit_partition", [n, gid], actual_cycles, sorted(expected_cycles))
        ledger.check("exact_periods_for_group", [n, gid], [len(orbits[j]) for j in observed_ids],
                     [entry["period"]] * entry["decorations"])
        row = entry["row"]
        row_counts[row][0] += 1
        row_counts[row][1] += len(observed_ids)
        row_counts[row][2] += len(members[gid])
        groups.append([gid, key, len(labels), entry["id"], observed_ids, sorted(expected_cycles)])
    counts = {}
    for route in orbits:
        add_count(counts, len(route))
    predicted24 = {}
    contributions = []
    for s in range(1, n + 1):
        multiplier = factorial(n) // factorial(n - s) * n ** (n - s)
        core = {}
        for piece in coefficient24(s):
            for p, value in piece.items():
                add_count(core, p, value)
                add_count(predicted24, p, multiplier * value)
        contributions.append([s, multiplier, polynomial(core)])
    ledger.check("full_period_census_scaled24", n, polynomial({p: 24 * c for p, c in counts.items()}),
                 polynomial(predicted24))
    period_set = [1] if n == 1 else list(range(1, 2 * n + 1)) + list(range(2 * n + 2, 4 * n - 3, 2))
    ledger.check("attained_period_set", n, sorted(counts), period_set)
    ledger.check("sharp_maximum", n, max(counts), 1 if n == 1 else 4 * n - 4)
    ledger.check("fixed_states", n, sum(i == arrows[i] for i in range(len(states))), n ** n)
    ledger.check("weighted_full_mass", n, sum(p * c for p, c in counts.items()), n ** (n + 2))
    ledger.check("seven_row_presence", n, [r[0] > 0 for r in row_counts],
                 [n >= first for first in (1, 2, 3, 2, 4, 2, 3)])
    limits = [[], [], []]
    for gid, key in enumerate(keys):
        entry = expected[key]
        family, lengths = entry["family"], entry["lengths"]
        if family == 0 and min(lengths) >= 3:
            limits[0].append(gid)
        if family == 1 and min(lengths[:2]) >= 3:
            limits[1].append(gid)
        if family == 2 and min(lengths) >= 2:
            limits[2].append(gid)
    ledger.check("unexercised_first_size_families", n, limits, [[], [], []])
    return {"n": n, "states": state_rows, "orbits": orbits, "groups": groups,
            "row_counts": row_counts, "period_counts": polynomial(counts),
            "extension_terms_scaled24": contributions, "unexercised_group_ids": limits}


def main():
    ledger = Ledger()
    catalogues = {s: make_catalogue(s, ledger) for s in PARAMETERS["core_sizes"]}
    coefficient_rows = []
    for s in PARAMETERS["core_sizes"]:
        observed = [{}, {}, {}]
        for entry in catalogues[s]:
            for word in entry["visit_words"]:
                add_count(observed[entry["family"]], len(word), 24)
        pieces = coefficient24(s)
        for family in range(3):
            ledger.check("labelled_core_series_scaled24", [s, family], polynomial(observed[family]),
                         polynomial({p: factorial(s) * c for p, c in pieces[family].items()}))
        total = sum(sum(piece.values()) for piece in pieces)
        weighted = sum(p * c for piece in pieces for p, c in piece.items())
        ledger.check("closed_core_coefficient_scaled24", s, total,
                     24 if s == 1 else 48 if s == 2 else 5 * s * s + s + 24)
        ledger.check("weighted_core_coefficient_scaled24", s, weighted, 12 * s * s * (s + 1))
        coefficient_rows.append([s, [polynomial(piece) for piece in pieces], total, weighted])
    carriers = [check_carrier(n, catalogues, ledger) for n in PARAMETERS["carrier_sizes"]]
    ledger.check("complete_fixed_carrier_total", "all", sum(len(c["states"]) for c in carriers), 4356)
    failures = [i for i, row in enumerate(ledger.rows) if not row[4]]
    names = sorted(set(row[0] for row in ledger.rows))
    census = [[name, sum(row[0] == name for row in ledger.rows),
               sum(row[0] == name and not row[4] for row in ledger.rows)] for name in names]
    output = {"schema": "P212_A_FULL_OUTPUT_V1", "role": "independent_review_A_finite_checks_only",
              "parameters": PARAMETERS,
              "method": "two_slot_swaps_vs_visit_word_last_arrival_and_incidence_quotient",
              "catalogues": [[s, catalogues[s]] for s in PARAMETERS["core_sizes"]],
              "coefficients_scaled24": coefficient_rows, "carriers": carriers,
              "checks": ledger.rows, "check_census": census, "failure_ids": failures,
              "finite_passed": not failures,
              "limits": ["no_all_size_proof_from_finite_checks", "no_first_size_5_6_5_execution",
                         "no_external_certification", "no_final_manuscript_or_build_verdict"]}
    print(wire(output))
    if failures:
        raise RuntimeError("P212 A finite predicates failed; complete output retained")


if __name__ == "__main__":
    main()
