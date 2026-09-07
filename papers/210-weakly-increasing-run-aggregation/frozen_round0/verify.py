#!/usr/bin/env python3
"""P210 author falsifier: fixed full box N=1..12; no external inputs.

Run with system Python3.10 -I -S -B and a fresh absent -X pycache_prefix.
Complete deterministic JSON goes to stdout. No pilot/old/reviewer imports.
Author representation: cut masks, accumulated OLD-part run sums, interval
endpoints for births, and right-to-left endpoint-partition DP.
"""
import json
from collections import Counter
from functools import lru_cache

MAX_N = 12
CHECKS = Counter()


def check(condition, kind):
    CHECKS[kind] += 1
    if not condition:
        raise AssertionError(kind)


def compositions(n):
    result = []
    for mask in range(1 << (n - 1)):
        ends = [i for i in range(1, n) if mask & (1 << (i - 1))] + [n]
        starts = [0] + ends[:-1]
        result.append(tuple(b - a for a, b in zip(starts, ends)))
    return tuple(sorted(result))


def step(a):
    """Accumulate sums, but compare adjacent original a entries only."""
    result = []
    total = a[0]
    for i in range(1, len(a)):
        if a[i - 1] <= a[i]:
            total += a[i]
        else:
            result.append(total)
            total = a[i]
    return tuple(result + [total])


def cut_step(a):
    """Companion direct cumulative-mass expression, not a sequential sum test."""
    keep = [0]
    total = 0
    for i, mass in enumerate(a):
        total += mass
        if i == len(a) - 1 or mass > a[i + 1]:
            keep.append(total)
    return tuple(b - x for x, b in zip(keep, keep[1:]))


def intervals(a):
    left = 0
    result = []
    for mass in a:
        result.append((left, left + mass))
        left += mass
    return result


def triangular(k):
    return k * (k + 1) // 2


def clock(n):
    h = 0
    while 1 + triangular(h + 1) <= n:
        h += 1
    return h


@lru_cache(None)
def partitions(n, minimum=1):
    """Sorted positive refinements, independently generated from cut masks."""
    if n == 0:
        return ((),)
    return tuple((first,) + rest
                 for first in range(minimum, n + 1)
                 for rest in partitions(n - first, first))


def endpoint_coefficient(n, first, last):
    if first == last:
        return int(n % first == 0)
    remaining = n - first - last
    if remaining < 0:
        return 0
    coeff = [1] + [0] * remaining
    for part in range(first, last + 1):
        for weight in range(part, remaining + 1):
            coeff[weight] += coeff[weight - part]
    return coeff[remaining]


@lru_cache(None)
def endpoint_counts(n):
    found = Counter((p[0], p[-1]) for p in partitions(n))
    rows = {}
    for first in range(1, n + 1):
        for last in range(first, n + 1):
            count = endpoint_coefficient(n, first, last)
            check(count == found[first, last], "partition_coefficient")
            if count:
                rows[first, last] = count
    return rows


@lru_cache(None)
def suffix_dp(s):
    """Count all feasible suffixes by their first part, working right to left."""
    if len(s) == 1:
        v = Counter()
        for (first, last), count in endpoint_counts(s[0]).items():
            v[first] += count
        return dict(v)
    right = suffix_dp(s[1:])
    v = Counter()
    for (first, last), count in endpoint_counts(s[0]).items():
        v[first] += count * sum(amount for c, amount in right.items() if c < last)
    return {first: count for first, count in v.items() if count}


@lru_cache(None)
def refinement_sources(s):
    if len(s) == 1:
        return partitions(s[0])
    return tuple(sorted(p + tail for p in partitions(s[0])
                        for tail in refinement_sources(s[1:]) if p[-1] > tail[0]))


def threshold(s):
    """Full suffix ledger, including unreachable earlier suffixes after failure."""
    r = 1
    rows = [{"index": len(s) - 1, "part": s[-1], "threshold": r,
             "branch": "initial"}]
    for i in range(len(s) - 2, -1, -1):
        if r is None:
            branch = "infeasible_suffix"
        elif s[i] <= r:
            r = None
            branch = "fail"
        elif s[i] == r + 1:
            r = s[i]
            branch = "increment"
        else:
            r = 1
            branch = "reset"
        rows.append({"index": i, "part": s[i], "threshold": r,
                     "branch": branch})
    return list(reversed(rows))


def attained_witness(s):
    """Construct a refinement attaining each successfully propagated minimum."""
    tail = (1,) * s[-1]
    r = 1
    for part in reversed(s[:-1]):
        if part <= r:
            return None
        if part == r + 1:
            prefix = (part,)
            r = part
        else:
            prefix = (1, part - 1)
            r = 1
        tail = prefix + tail
    return tail


def encode(s):
    emitted = [1] * (s[-1] - 1)
    r = 1
    for part in reversed(s[:-1]):
        if part <= r:
            raise ValueError("not in image")
        if part == r + 1:
            r += 1
        else:
            emitted.append(triangular(r + 1))
            emitted.extend([1] * (part - r - 2))
            r = 1
    emitted.append(triangular(r))
    return tuple(emitted)


def triangle_index(value):
    k = 1
    while triangular(k) < value:
        k += 1
    if triangular(k) != value:
        raise ValueError("not a triangular part")
    return k


def decode(parts):
    terminal = triangle_index(parts[-1])
    prefix = parts[:-1]
    i = 0
    while i < len(prefix) and prefix[i] == 1:
        i += 1
    read_list = [i + 1]
    while i < len(prefix):
        j = triangle_index(prefix[i]) - 1
        check(j >= 1, "inverse_reset_atom")
        i += 1
        u = 0
        while i < len(prefix) and prefix[i] == 1:
            u += 1
            i += 1
        read_list.extend(range(2, j + 1))
        read_list.append(j + 2 + u)
    read_list.extend(range(2, terminal + 1))
    return tuple(reversed(read_list))


@lru_cache(None)
def triangular_compositions(n):
    if n == 0:
        return ((),)
    result = []
    k = 1
    while triangular(k) <= n:
        part = triangular(k)
        result.extend((part,) + tail for tail in triangular_compositions(n - part))
        k += 1
    return tuple(sorted(result))


def orbit_records(source):
    state = source
    orbit = [state]
    born = {block: 0 for block in intervals(state)}
    rounds = []
    t = 0
    while step(state) != state:
        t += 1
        old_intervals = intervals(state)
        output = step(state)
        check(output == cut_step(state), "two_literal_expressions")
        old_set = set(old_intervals)
        new_intervals = intervals(output)
        cuts = []
        for i in range(len(state) - 1):
            if state[i] <= state[i + 1]:
                check(state[i] >= t, "deleted_cut_left_mass")
                if t >= 2:
                    check(born[old_intervals[i + 1]] == t - 1, "delayed_right_birth")
                cuts.append({"cut": old_intervals[i][1], "left_mass": state[i],
                             "right_mass": state[i + 1], "right_birth": born[old_intervals[i + 1]]})
        new = []
        for block in new_intervals:
            if block not in old_set:
                mass = block[1] - block[0]
                check(mass >= 1 + triangular(t), "new_block_mass")
                parents = [p for p in old_intervals if block[0] <= p[0] and p[1] <= block[1]]
                check(len(parents) >= 2 and sum(q - p for p, q in parents) == mass,
                      "new_block_parent_partition")
                born[block] = t
                new.append({"interval": block, "mass": mass, "parents": parents})
        check(sum(output) == sum(source), "mass_preserved")
        check(len(output) < len(state), "length_strictly_decreases")
        check(set(new_intervals).issubset(set(born)), "birth_identity_defined")
        rounds.append({"round": t, "old": state, "new": output,
                       "deleted_cuts": cuts, "new_blocks": new})
        state = output
        check(state not in orbit, "no_nontrivial_cycle")
        orbit.append(state)
    check(all(x > y for x, y in zip(state, state[1:])), "endpoint_strict_descent")
    return orbit, rounds


def main():
    masses = []
    recurrence = [1]
    total_states = total_image = total_witnesses = 0
    for n in range(1, MAX_N + 1):
        states = compositions(n)
        check(len(states) == 1 << (n - 1), "complete_carrier_cardinality")
        check(len(set(states)) == len(states), "carrier_unique")
        edges = {a: step(a) for a in states}
        fibres = {s: [] for s in states}
        for a, s in edges.items():
            check(s in fibres and sum(s) == n, "edge_closed")
            check(s == cut_step(a), "literal_whole_graph")
            fibres[s].append(a)
        row_by_state = {}
        depths = Counter()
        fixed = []
        for a in states:
            orbit, births = orbit_records(a)
            depth = len(orbit) - 1
            check(depth <= clock(n), "pointwise_upper_clock")
            check((depth == 0) == all(x > y for x, y in zip(a, a[1:])),
                  "fixed_point_iff")
            if depth == 0:
                fixed.append(a)
            depths[depth] += 1
            row_by_state[a] = {"state": a, "edge": edges[a], "depth": depth,
                               "fixed_endpoint": orbit[-1], "orbit": orbit, "birth_rounds": births}
        check(max(depths) == clock(n), "sharp_global_clock")
        image = sorted(s for s in states if fibres[s])
        target_rows = []
        for s in states:
            sources = tuple(sorted(fibres[s]))
            direct = refinement_sources(s)
            dp = suffix_dp(s)
            check(direct == sources, "full_fibre_source_equality")
            check(sum(dp.values()) == len(sources), "endpoint_dp_fibre")
            thresholds = threshold(s)
            for i, row in enumerate(thresholds):
                actual_sources = refinement_sources(s[i:])
                first_counts = Counter(a[0] for a in actual_sources)
                check(dict(first_counts) == suffix_dp(s[i:]), "all_suffix_endpoint_counts")
                attainable = sorted(first_counts)
                minimum = min(attainable) if attainable else None
                check(row["threshold"] == minimum, "attained_suffix_minimum")
                witness = attained_witness(s[i:])
                check((witness is not None) == bool(actual_sources), "constructive_suffix_iff")
                if witness is not None:
                    check(witness in actual_sources and witness[0] == minimum,
                          "constructive_minimum_attainment")
                    check(step(witness) == s[i:], "constructive_suffix_literal")
                row.update({"attainable_first_parts": attainable,
                            "first_part_counts": sorted(first_counts.items()),
                            "attaining_preimage": witness})
            in_image = bool(sources)
            check((thresholds[0]["threshold"] is not None) == in_image, "image_iff")
            code = encode(s) if in_image else None
            if code is not None:
                check(sum(code) == n, "forward_weight")
                check(code in triangular_compositions(n), "forward_triangular_member")
                check(decode(code) == s, "image_roundtrip")
            target_rows.append({"target": s, "fibre": len(sources), "sources": sources,
                                "suffixes": thresholds, "image": in_image, "code": code})
        triangular_rows = []
        triangles = triangular_compositions(n)
        for parts in triangles:
            target = decode(parts)
            check(target in image, "inverse_image_member")
            check(sum(target) == n, "inverse_weight")
            check(encode(target) == parts, "triangular_roundtrip")
            triangular_rows.append({"parts": parts, "decoded_target": target})
        check(len({encode(s) for s in image}) == len(image) == len(triangles),
              "bijection_complete_cardinality")
        count = sum(recurrence[n - triangular(k)] for k in range(1, n + 1)
                    if triangular(k) <= n)
        recurrence.append(count)
        check(count == len(image), "known_triangular_recurrence")
        witnesses = []
        for h in range(1, clock(n) + 1):
            r = n - 1 - triangular(h)
            a = tuple(range(h, 0, -1)) + (1 + r,)
            actual = row_by_state[a]["orbit"]
            expected = [a] + [tuple(range(h, j, -1)) + (r + 1 + triangular(j),)
                              for j in range(1, h + 1)]
            check(actual == expected, "all_surplus_witness_orbit")
            check(row_by_state[a]["depth"] == h, "all_surplus_witness_depth")
            witnesses.append({"h": h, "surplus": r, "state": a, "orbit": actual})
        endpoint_table = [[a, b, endpoint_coefficient(n, a, b)]
                          for a in range(1, n + 1) for b in range(a, n + 1)]
        masses.append({"N": n, "states": [row_by_state[a] for a in states],
                       "targets": target_rows, "fixed_points": fixed,
                       "triangular_objects": triangular_rows, "witnesses": witnesses,
                       "endpoint_partition_coefficients": endpoint_table,
                       "summary": {"states": len(states), "fixed": len(fixed),
                                   "depth_histogram": sorted(depths.items()),
                                   "max_depth": max(depths), "H": clock(n),
                                   "image": len(image), "triangular_count": len(triangles),
                                   "witness_count": len(witnesses)}})
        total_states += len(states)
        total_image += len(image)
        total_witnesses += len(witnesses)
    check(total_states == 4095, "original_box_total")
    result = {"schema": "P210_AUTHOR_FULL_CANONICAL_V1", "mass_box": [1, MAX_N],
              "parameters": {"positive_parts": True, "old_part_synchronous": True,
                             "external_data": False},
              "masses": masses,
              "totals": {"states": total_states, "edges": total_states,
                         "targets": total_states, "image_objects": total_image,
                         "triangular_objects": total_image, "surplus_witnesses": total_witnesses},
              "checks_by_kind": dict(sorted(CHECKS.items())), "checks": sum(CHECKS.values())}
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
