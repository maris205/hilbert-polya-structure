#!/usr/bin/env python3
"""Bounded ninth-lane author scout; no repository imports or input reads."""
from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import isqrt, prod
import json


ASSERTIONS = Counter()


def check(value, section):
    ASSERTIONS[section] += 1
    if not value:
        raise AssertionError(section)


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def graph_record(tag, parameters, states, update, extra=None):
    index = {x: i for i, x in enumerate(states)}
    check(len(index) == len(states), tag + ":unique")
    targets = []
    for x in states:
        y = update(x)
        check(y in index, tag + ":closure")
        targets.append(index[y])
    incoming = [0] * len(states)
    for j in targets:
        incoming[j] += 1
    remaining = incoming[:]
    queue = deque(i for i, count in enumerate(remaining) if not count)
    peeled = []
    while queue:
        i = queue.popleft()
        peeled.append(i)
        j = targets[i]
        remaining[j] -= 1
        if not remaining[j]:
            queue.append(j)
    height = [0] * len(states)
    for i in reversed(peeled):
        height[i] = height[targets[i]] + 1
    cycles = Counter()
    seen = set()
    for i in range(len(states)):
        if not remaining[i] or i in seen:
            continue
        j = i
        length = 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = targets[j]
        check(j == i, tag + ":cycle_partition")
        cycles[length] += 1
    check(len(seen) + len(peeled) == len(states), tag + ":partition")
    maximum_height = max(height)
    first_deepest = height.index(maximum_height)
    orbit = []
    j = first_deepest
    until = set()
    while j not in until:
        until.add(j)
        orbit.append(states[j])
        j = targets[j]
    check(len(orbit) > maximum_height, tag + ":deep_orbit")
    maximum_fibre = max(incoming)
    record = {
        "tag": tag, "parameters": parameters, "states": len(states),
        "image": sum(v > 0 for v in incoming), "height": maximum_height,
        "height_histogram": sorted(Counter(height).items()),
        "cycles_by_length": sorted(cycles.items()), "core": len(seen),
        "maximum_fibre": maximum_fibre,
        "all_maximizing_targets": [states[i] for i, v in enumerate(incoming)
                                   if v == maximum_fibre],
        "maximum_height_witness_orbit": orbit,
        "witness_cycle_entry": states[j],
        "transition_table_sha256": sha256(encoded(targets).encode()).hexdigest(),
        "fibre_histogram": sorted(Counter(incoming).items()),
    }
    if extra:
        record["controls"] = extra(states, targets, height, incoming, index)
    return record


def eld(f, p):
    m = len(f)
    inverse = [1] + [0] * (m - 1)
    for k in range(1, m):
        inverse[k] = -sum(f[i] * inverse[k-i] for i in range(1, k+1)) % p
    return tuple([1] + [sum(i*f[i]*inverse[k-i] for i in range(1, k+1)) % p
                        for k in range(1, m)])


def eld_control(p, m):
    def control(states, targets, heights, incoming, index):
        expected = {x for x in states
                    if all(x[p*k] == x[k] for k in range(1, (m-1)//p+1))}
        actual = {states[j] for j in targets}
        check(expected == actual, "ELD:ghost_image")
        weight = p**((m-1)//p)
        for i, x in enumerate(states):
            check(incoming[i] == (weight if x in expected else 0), "ELD:ghost_fibre")
            check(heights[i] <= 1, "ELD:height_one")
        check(len({eld(x, p) for x in expected}) == len(expected), "ELD:image_permutation")
        return {"ghost_image_size": len(expected), "uniform_nonzero_fibre": weight}
    return control


def vdf(x, p):
    return tuple(prod(a-b for j, b in enumerate(x) if j != i) % p
                 for i, a in enumerate(x))


def vdf_control(p, n):
    def control(states, targets, heights, incoming, index):
        for x in states:
            y = vdf(x, p)
            for i in range(n):
                for j in range(i+1, n):
                    if x[i] == x[j]:
                        check(y[i] == y[j] == 0, "VDF:duplicate_zero")
            if x.count(0) >= 2:
                check(all(y[i] == 0 for i, a in enumerate(x) if a == 0), "VDF:zero_lock")
            if n == 2:
                check(vdf(y, p) == tuple(2*a % p for a in y), "VDF:linear_two_slice")
        return {"n2_scalar_adapter": n == 2, "general_clock": "unproved"}
    return control


def compositions(total, n):
    if n == 1:
        yield (total,)
        return
    for a in range(1, total-n+2):
        for rest in compositions(total-a, n-1):
            yield (a,) + rest


def rha(x):
    k = sum(x) - len(x)
    weights = [Fraction(1, a) for a in x]
    weight_sum = sum(weights)
    quotas = [k*w/weight_sum for w in weights]
    floor = [q.numerator//q.denominator for q in quotas]
    left = k-sum(floor)
    order = sorted(range(len(x)), key=lambda i: (-(quotas[i]-floor[i]), i))
    for i in order[:left]:
        floor[i] += 1
    return tuple(a+1 for a in floor)


def matchings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for i in range(1, len(vertices)):
        for rest in matchings(vertices[1:i] + vertices[i+1:]):
            yield ((first, vertices[i]),) + rest


def normalize(edges):
    return tuple(sorted(tuple(sorted(e)) for e in edges))


def epn(matching):
    length = {v: b-a for a, b in matching for v in (a, b)}
    order = sorted(length, key=lambda v: (length[v], v))
    return normalize(zip(order[::2], order[1::2]))


def old_edr(matching):
    length = {v: b-a for a, b in matching for v in (a, b)}
    order = sorted(length, key=lambda v: (length[v], v))
    rank = {v: i for i, v in enumerate(order)}
    return normalize((rank[a], rank[b]) for a, b in matching)


def old_lew(matching):
    ordered = sorted(matching, key=lambda e: (e[1]-e[0], e[0], e[1]))
    flat = [a for a, b in ordered] + [b for a, b in reversed(ordered)]
    return normalize(zip(flat[::2], flat[1::2]))


def epn_control(n):
    def control(states, targets, heights, incoming, index):
        differences = {"EDR": None, "LEW": None}
        for m in states:
            y = epn(m)
            before = sum(b-a for a, b in m)
            after = sum(b-a for a, b in y)
            check((y == m and before == after) or after <= before-2, "EPN:strict_potential")
            check((before-n) % 2 == 0 and n <= before <= n*n, "EPN:potential_range")
            check(heights[index[m]] <= n*(n-1)//2, "EPN:generic_height_bound")
            for label, old in (("EDR", old_edr), ("LEW", old_lew)):
                if differences[label] is None and y != old(m):
                    differences[label] = {"source": m, "EPN": y, "old": old(m)}
        return {"literal_difference_witnesses": differences,
                "generic_length_bound": n*(n-1)//2}
    return control


def qrm(x):
    if len(x) == 1:
        return x
    squares = sum(a*a for a in x)
    return tuple(isqrt((squares-a*a)//(len(x)-1)) for a in x)


def qrm_control(n, m):
    def control(states, targets, heights, incoming, index):
        for x in states:
            y = qrm(x)
            check(min(x) <= min(y) <= max(y) <= max(x), "QRM:range")
            if n == 1:
                check(y == x, "QRM:n1_identity")
            elif n == 2:
                check(y == x[::-1], "QRM:n2_swap")
            else:
                if len(set(x)) > 1:
                    check(max(qrm(y)) < max(x), "QRM:two_step_max")
                check((y == x) == (len(set(x)) == 1), "QRM:fixed")
                check(heights[index[x]] <= 2*(max(x)-min(x)), "QRM:generic_height_bound")
        return {"n_ge_3_bound": 2*m if n >= 3 else None,
                "separate_valued_inverse": "unproved"}
    return control


def qef(x, p):
    a, b, c = x
    return ((a+b*c) % p, (b+a*c) % p, (c+a*b) % p)


def qef_control(p):
    def control(states, targets, heights, incoming, index):
        old_difference = None
        for x in states:
            y = qef(x, p)
            check((y == x) == (sum(a != 0 for a in x) <= 1), "QEF:fixed_axes")
            a, b, c = x
            check((y[0]-y[1]) % p == ((a-b)*(1-c)) % p, "QEF:difference_factor")
            old = tuple(x[i]*(1+x[(i+1)%3]-x[(i-1)%3]) % p for i in range(3))
            if old_difference is None and old != y:
                old_difference = {"source": x, "QEF": y, "old_LV": old}
        return {"fixed_count": 3*p-2, "old_LV_difference": old_difference,
                "general_clock": "unproved"}
    return control


def main():
    records = []
    for p in (2, 3, 5):
        for m in range(2, 7):
            states = [(1,) + x for x in product(range(p), repeat=m-1)]
            records.append(graph_record("ELD", {"p": p, "m": m}, states,
                                        lambda x: eld(x, p), eld_control(p, m)))
    for p in (2, 3, 5, 7):
        for n in range(1, 5):
            states = list(product(range(p), repeat=n))
            records.append(graph_record("VDF", {"p": p, "n": n}, states,
                                        lambda x: vdf(x, p), vdf_control(p, n)))
    for n in range(1, 5):
        for total in range(n, 19):
            states = list(compositions(total, n))
            records.append(graph_record("RHA", {"n": n, "N": total}, states, rha))
    for n in range(1, 7):
        states = list(matchings(tuple(range(2*n))))
        records.append(graph_record("EPN", {"n": n}, states, epn, epn_control(n)))
    for n in range(1, 6):
        for m in range(5):
            states = list(product(range(m+1), repeat=n))
            records.append(graph_record("QRM", {"n": n, "M": m}, states, qrm, qrm_control(n, m)))
    for p in (2, 3, 5, 7, 11, 13):
        states = list(product(range(p), repeat=3))
        records.append(graph_record("QEF", {"p": p}, states,
                                    lambda x: qef(x, p), qef_control(p)))
    check(len(records) == 134, "declared_boxes")
    output = {"schema": "finite-algebra-ninth-author-scout-v1",
              "boxes": len(records), "states": sum(r["states"] for r in records),
              "assertions": sum(ASSERTIONS.values()), "assertions_by_section": dict(ASSERTIONS),
              "records_sha256": sha256(encoded(records).encode()).hexdigest(),
              "records": records, "status": "BOUNDED_OBSERVATIONS_AND_WEAK_PROOF_CONTROLS_ONLY"}
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
