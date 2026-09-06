#!/usr/bin/env python3
"""MNC nonauthor candidate audit; stdlib only, no runtime input files.

Independent representations: full functional-graph peeling, direct triple
constraint propagation, equality-edge masks, and a colored binary-tail lift.
No author/scout/historical verifier, data, or canonical is imported or read.
Full cyclic boxes remain n=3..9. Larger n tests are explicit witnesses and
scalar identities only, not an enlarged full-state pilot.
"""
from collections import Counter, defaultdict, deque
from hashlib import sha256
from itertools import product
import json


ASSERTIONS = 0


def check(ok, context):
    global ASSERTIONS
    ASSERTIONS += 1
    if not ok:
        raise AssertionError(context)


def dump(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def digest(obj):
    return sha256(dump(obj).encode()).hexdigest()


def literal(x):
    n = len(x)
    return tuple(min(abs(x[i] - x[i-1]), abs(x[i] - x[(i+1) % n]))
                 for i in range(n))


def table(a, b, c):
    if a == b or b == c:
        return 0
    if b != 1 and a == c == 2-b:
        return 2
    return 1


def tabulated(x):
    n = len(x)
    return tuple(table(x[i-1], x[i], x[(i+1) % n]) for i in range(n))


def binary(x):
    n = len(x)
    return tuple((x[i-1] ^ x[i]) & (x[i] ^ x[(i+1) % n])
                 for i in range(n))


def paired_zeros(x):
    n = len(x)
    return all(v or x[i-1] == 0 or x[(i+1) % n] == 0
               for i, v in enumerate(x))


def pulses(x):
    n = len(x)
    return paired_zeros(x) and all(not v or
        (x[i-1] == 0 and x[(i+1) % n] == 0) for i, v in enumerate(x))


def colored_class(x):
    n = len(x)
    return paired_zeros(x) and all(v != 2 or
        (x[i-1] == 0 and x[(i+1) % n] == 0) for i, v in enumerate(x))


def lift_tail(x):
    p = tuple(int(v > 0) for v in x)
    d = tuple(int(v == 2) for v in x)
    gp = binary(p)
    return tuple(gp[i] + d[i] for i in range(len(x)))


def source_sets(target):
    """Cyclic local-CSP backtracking, not distance-word reconstruction."""
    n = len(target)
    found = set()
    for first, second in product(range(3), repeat=2):
        stack = [(first, second)]
        while stack:
            x = stack.pop()
            if len(x) == n:
                if (table(x[-2], x[-1], first) == target[-1] and
                        table(x[-1], first, second) == target[0]):
                    found.add(x)
                continue
            target_index = len(x)-1
            for nxt in range(3):
                if table(x[-2], x[-1], nxt) == target[target_index]:
                    stack.append(x + (nxt,))
    return found


def overlap_count(target):
    """Nine-overlap endpoint DP; cyclic trace via remembered starting pair."""
    answer = 0
    for a0, b0 in product(range(3), repeat=2):
        counts = {(a0, b0): 1}
        for output in target:
            nxt_counts = defaultdict(int)
            for (a, b), multiplicity in counts.items():
                for c in range(3):
                    if table(a, b, c) == output:
                        nxt_counts[b, c] += multiplicity
            counts = nxt_counts
        answer += counts.get((a0, b0), 0)
    return answer


def edge_word(x):
    return tuple(abs(x[i] - x[(i+1) % len(x)]) for i in range(len(x)))


def edge_formula(d):
    w = tuple(v for v in d if v)
    ones = w.count(1)
    twos = len(w)-ones
    if not w:
        return 3
    if not ones:
        return 1 + (-1)**twos
    if ones % 2:
        return 0
    if not twos:
        return 2**(ones//2+1)
    start = w.index(2)
    rotated = w[start+1:] + w[:start+1]
    gap = 0
    for v in rotated:
        if v == 1:
            gap += 1
        else:
            if gap % 2:
                return 0
            gap = 0
    return 2**(ones//2)


def support_of_edges(e):
    return tuple(e[i-1] & e[i] for i in range(len(e)))


def mixed_runs(mask):
    """Lengths of each labeled cyclic zero block, starting after a one."""
    n = len(mask)
    lengths = []
    for i in range(n):
        if mask[i] == 0 and mask[i-1] == 1:
            ell = 0
            while mask[(i+ell) % n] == 0:
                ell += 1
            lengths.append(ell)
    return lengths


def periodic_c(n):
    return (2, 1, -1, -2, -1, 1)[n % 6]


def zero_formula(n):
    return 2**n + (-1)**n + 2*periodic_c(n)


def relaxed_formula(mask):
    n = len(mask)
    k = sum(mask)
    if not k:
        return zero_formula(n)
    if k == n:
        return 2**n + 2*(-1)**n
    lengths = mixed_runs(mask)
    if 1 in lengths:
        return 0
    leading = 2**(k+len(lengths))
    correction = 2*(-1)**(k+len(lengths))
    for ell in lengths:
        leading *= (2**(ell-1) + (-1)**ell)//3
        correction *= (1, 1, 0, -1, -1, 0)[(ell-2) % 6]
    return leading + correction


def graph_heights(states, successors):
    """Kahn peeling detects all cycles without assuming stabilization."""
    indeg = {x: 0 for x in states}
    for y in successors.values():
        indeg[y] += 1
    queue = deque(x for x in states if indeg[x] == 0)
    order = []
    while queue:
        x = queue.popleft()
        order.append(x)
        y = successors[x]
        indeg[y] -= 1
        if indeg[y] == 0:
            queue.append(y)
    recurrent = {x for x in states if indeg[x]}
    cycles = []
    visited = set()
    for x in sorted(recurrent):
        if x in visited:
            continue
        orbit = []
        z = x
        while z not in visited:
            visited.add(z)
            orbit.append(z)
            z = successors[z]
        cycles.append(orbit)
    depth = {x: 0 for x in recurrent}
    for x in reversed(order):
        depth[x] = depth[successors[x]] + 1
    return depth, cycles


def full_box(n):
    states = list(product(range(3), repeat=n))
    successors = {x: literal(x) for x in states}
    fibre_sets = defaultdict(set)
    edge_counts = Counter()
    singleton_counts = Counter()
    class_count = 0
    for x in states:
        y = successors[x]
        fibre_sets[y].add(x)
        edge_counts[edge_word(x)] += 1
        singleton_counts[tuple(int(v > 0) for v in y)] += 1
        check(y == tabulated(x), ["literal-table", n, x])
        check(paired_zeros(y), ["paired-first-image", n, x])
        z = successors[y]
        check(colored_class(z), ["second-image-color-class", n, x])
        check((y == x) == pulses(x), ["full-fixed-language", n, x])
        if colored_class(x):
            class_count += 1
            check(y == lift_tail(x), ["exact-colored-ECA36-lift", n, x])
            check(successors[y] == y, ["class-idempotence", n, x])
    depths, cycles = graph_heights(states, successors)
    check(all(len(c) == 1 for c in cycles), ["nontrivial-cycle", n])
    check(max(depths.values()) == (2 if n <= 4 else 3), ["sharp-height", n])
    fibre_vector = []
    relaxed_by_edges = Counter()
    for e in product(range(2), repeat=n):
        k = sum(e)
        relaxed_by_edges[support_of_edges(e)] += 2**k + 2*(-1)**k
    relaxed_rows = []
    for mask in product(range(2), repeat=n):
        val = singleton_counts[mask]
        check(val == relaxed_by_edges[mask], ["colored-equality-edge-adapter", n, mask])
        check(val == relaxed_formula(mask), ["all-mask-closed-form", n, mask])
        if 0 < sum(mask) < n:
            check(val <= 2**(n-1)+2, ["mixed-relaxation-bound", n, mask])
        relaxed_rows.append(val)
    for d in states:
        check(edge_counts[d] == edge_formula(d), ["all-edge-weight-formula", n, d])
    inverse_by_distance = Counter()
    for d in states:
        b = tuple(min(d[i-1], d[i]) for i in range(n))
        inverse_by_distance[b] += edge_formula(d)
    csp_set_hashes = []
    for b in states:
        observed = len(fibre_sets[b])
        check(overlap_count(b) == observed, ["all-target-overlap-DP", n, b])
        check(inverse_by_distance[b] == observed, ["all-target-distance-decoder", n, b])
        if n <= 7:
            generated = source_sets(b)
            check(generated == fibre_sets[b], ["complete-CSP-source-set", n, b])
            csp_set_hashes.append(digest(sorted(generated)))
        if any(b) and not all(b):
            check(observed <= relaxed_formula(tuple(int(v > 0) for v in b)),
                  ["magnitude-forgetting-inclusion", n, b])
        if n >= 4:
            if any(b):
                check(observed < zero_formula(n), ["strict-all-nonzero", n, b])
            else:
                check(observed == zero_formula(n), ["zero-extremizer", n])
            if all(b) and 2 in b:
                check(observed <= 2**(n-2), ["positive-two-bound", n, b])
        fibre_vector.append(observed)
    maximum = max(fibre_vector)
    maximizers = [list(b) for b, v in zip(states, fibre_vector) if v == maximum]
    check(maximizers == [[1]*n] if n == 3 else maximizers == [[0]*n],
          ["unique-maximizer", n])
    if n == 3:
        check(fibre_sets[(1, 1, 1)] == {x for x in states if len(set(x)) == 3},
              ["exception-all-six-sources"])
    return {"n": n, "states": len(states), "height": max(depths.values()),
            "depth_histogram": sorted(Counter(depths.values()).items()),
            "cycle_length_histogram": sorted(Counter(map(len, cycles)).items()),
            "fixed_count": len(cycles), "colored_class_count": class_count,
            "fibre_histogram": sorted(Counter(fibre_vector).items()),
            "maximum_fibre": maximum, "maximizers": maximizers,
            "zero_fibre": fibre_vector[0], "all_one_fibre": len(fibre_sets[(1,)*n]),
            "labeled_fibre_vector_sha256": digest(fibre_vector),
            "all_mask_relaxed_vector_sha256": digest(relaxed_rows),
            "CSP_source_set_hash_vector_sha256": digest(csp_set_hashes) if n <= 7 else None}


def shrink(x, alphabet):
    rule = table if alphabet == 3 else lambda a, b, c: (a ^ b) & (b ^ c)
    return tuple(rule(x[i-1], x[i], x[i+1]) for i in range(1, len(x)-1))


def local_identities():
    checked = Counter()
    for x in product(range(3), repeat=9):
        trajectory = [x]
        for _ in range(4):
            trajectory.append(shrink(trajectory[-1], 3))
        check(trajectory[4][0] == trajectory[3][1], ["radius-four-identity", x])
        checked["ternary_width9"] += 1
    for x in product(range(2), repeat=7):
        trajectory = [x]
        for _ in range(3):
            trajectory.append(shrink(trajectory[-1], 2))
        check(trajectory[3][0] == trajectory[2][1], ["deducted-ECA36-identity", x])
        checked["binary_width7"] += 1
    code = 0
    for a, b, c in product(range(3), repeat=3):
        v = min(abs(a-b), abs(b-c))
        check(table(a, b, c) == v, ["local-triple-rule", a, b, c])
        code += v * 3**(9*a+3*b+c)
    binary_code = sum(((a ^ b) & (b ^ c))*2**(4*a+2*b+c)
                      for a, b, c in product(range(2), repeat=3))
    check(binary_code == 36, ["binary-rule-code"])
    return dict(checked, ternary_code=code, binary_code=binary_code)


def large_scalar_and_witness_checks():
    all_one = [3, 0, 4]
    for n in range(3, 65):
        all_one.append(2*all_one[n-2]+2*all_one[n-3])
    rows = []
    for n in range(3, 65):
        check(overlap_count((1,)*n) == all_one[n], ["all-one-DP-vs-recurrence", n])
        check(overlap_count((0,)*n) == zero_formula(n), ["zero-DP-vs-matching", n])
        if n == 3:
            x = (0, 1, 2)
        elif n == 4:
            x = (0, 0, 1, 2)
        elif n == 5:
            x = (0, 1, 1, 0, 2)
        else:
            x = (0,)*(n-4) + (1, 1, 0, 2)
        orbit = [x]
        while literal(orbit[-1]) != orbit[-1] and len(orbit) <= 5:
            orbit.append(literal(orbit[-1]))
        check(len(orbit)-1 == (2 if n <= 4 else 3), ["explicit-all-length-witness", n])
        check(literal(orbit[-1]) == orbit[-1], ["witness-terminal", n])
        if n >= 4:
            check(2**(n-1)+2 < 2**n-5 <= zero_formula(n), ["mixed-strict-scalar", n])
            check(2**(n-2) < zero_formula(n), ["two-strict-scalar", n])
            check(4*all_one[n] <= 3*2**n, ["all-one-scalar-majorant", n])
            check(all_one[n] < zero_formula(n), ["all-one-strict-scalar", n])
        rows.append({"n": n, "zero_count": zero_formula(n), "all_one_count": all_one[n],
                     "witness_height": len(orbit)-1, "witness_orbit_sha256": digest(orbit)})
    return rows


def main():
    output = {"schema": "MNC-independent-candidate-audit/1",
              "scope": "n=3..9 full cyclic boxes; CSP sets n=3..7; no input files",
              "local_identity_pressure": local_identities(),
              "boxes": [full_box(n) for n in range(3, 10)],
              "scalar_and_explicit_witness_only": large_scalar_and_witness_checks()}
    output["assertions"] = ASSERTIONS
    output["record_sha256"] = digest(output)
    output["status"] = "PASS"
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
