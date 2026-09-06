#!/usr/bin/env python3
"""Six fifth-lane full-carrier pilots, fixed bounds in INTAKE.md."""
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
import json

checks = 0
digest = sha256()


def require(statement):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(checks)


def analyze(tag, parameter, states, update, audit=None, fibre_size=None):
    states = list(states)
    index = {state: i for i, state in enumerate(states)}
    require(len(index) == len(states))
    targets = [update(state) for state in states]
    require(all(target in index for target in targets))
    forward = [index[target] for target in targets]
    indegree = Counter(forward)
    tail, period = [-1] * len(states), [-1] * len(states)
    cycles = Counter()
    for start in range(len(states)):
        if tail[start] >= 0:
            continue
        path, seen = [], {}
        current = start
        while tail[current] < 0 and current not in seen:
            seen[current] = len(path)
            path.append(current)
            current = forward[current]
        if tail[current] < 0:
            cut = seen[current]
            cycle = path[cut:]
            cycles[len(cycle)] += 1
            for vertex in cycle:
                tail[vertex], period[vertex] = 0, len(cycle)
            path = path[:cut]
        for vertex in reversed(path):
            tail[vertex], period[vertex] = tail[forward[vertex]] + 1, period[forward[vertex]]
    for i, target in enumerate(targets):
        require(period[i] == period[forward[i]])
        require(tail[i] == 0 or tail[i] == tail[forward[i]] + 1)
        if audit is not None:
            require(audit(states[i], target))
        if fibre_size is not None:
            require(indegree[i] == fibre_size(states[i]))
        digest.update(json.dumps([tag, parameter, states[i], target, tail[i], period[i]],
                                 separators=(",", ":"), sort_keys=True).encode())
        digest.update(b"\n")
    maximum = max(indegree.values())
    maximizing = [states[i] for i in range(len(states)) if indegree[i] == maximum]
    height = max(tail)
    return {"rule": tag, "parameter": parameter, "states": len(states),
            "image": len(indegree), "recurrent": sum(t == 0 for t in tail),
            "cycles_by_length": dict(sorted(cycles.items())), "height": height,
            "depth_counts": dict(sorted(Counter(tail).items())),
            "deepest_witness": states[tail.index(height)],
            "maximum_fibre": maximum, "maximizer_count": len(maximizing),
            "maximizer_witness": maximizing[0],
            "nonempty_fibre_histogram": dict(sorted(Counter(indegree.values()).items()))}


def permutation_group(d, alternating=False):
    elements = [g for g in permutations(range(d))
                if not alternating or sum(g[i] > g[j] for i in range(d)
                                          for j in range(i + 1, d)) % 2 == 0]
    locations = {g: i for i, g in enumerate(elements)}
    table = [[locations[tuple(g[h[i]] for i in range(d))] for h in elements] for g in elements]
    identity = locations[tuple(range(d))]
    inverse = [next(j for j in range(len(elements)) if table[i][j] == identity)
               for i in range(len(elements))]
    require(all(table[i][inverse[i]] == table[inverse[i]][i] == identity
                for i in range(len(elements))))
    return table, inverse


def cyclic_group(n):
    return [[(a + b) % n for b in range(n)] for a in range(n)]


def dihedral_eight():
    elements = list(product(range(4), range(2)))
    locations = {g: i for i, g in enumerate(elements)}
    return [[locations[((a + (-1) ** e * b) % 4, (e + f) % 2)]
             for b, f in elements] for a, e in elements]


def quaternion_eight():
    # index=2*unit+sign, units 1,i,j,k; sign=1 denotes a negative.
    units = (((0, 0), (1, 0), (2, 0), (3, 0)),
             ((1, 0), (0, 1), (3, 0), (2, 1)),
             ((2, 0), (3, 1), (0, 1), (1, 0)),
             ((3, 0), (2, 0), (1, 1), (0, 1)))
    return [[2 * units[a // 2][b // 2][0] +
             ((a % 2 + b % 2 + units[a // 2][b // 2][1]) % 2)
             for b in range(8)] for a in range(8)]


def unique_ordered_products(subset, table):
    occupied = [i for i in range(len(table)) if subset >> i & 1]
    counts = Counter(table[a][b] for a in occupied for b in occupied)
    return sum(1 << value for value, count in counts.items() if count == 1)


def cross_table(p):
    vectors = list(product(range(p), repeat=3))
    index = {v: i for i, v in enumerate(vectors)}
    def cross(u, v):
        return ((u[1] * v[2] - u[2] * v[1]) % p,
                (u[2] * v[0] - u[0] * v[2]) % p,
                (u[0] * v[1] - u[1] * v[0]) % p)
    return [[index[cross(u, v)] for v in vectors] for u in vectors]


def cross_cycle_audit(p, cross):
    vectors = list(product(range(p), repeat=3))
    index = {v: i for i, v in enumerate(vectors)}
    determinant = [[[sum(x * y for x, y in zip(vectors[cross[a][b]], vectors[c])) % p
                    for c in range(len(vectors))] for b in range(len(vectors))]
                   for a in range(len(vectors))]
    scaled = [[index[tuple(k * x % p for x in v)] for v in vectors] for k in range(p)]
    def audit(state, target):
        dets = [determinant[state[i]][state[(i + 1) % 4]][state[(i + 2) % 4]]
                for i in range(4)]
        return all(cross[target[i]][target[(i + 1) % 4]] == scaled[dets[i]][state[(i + 1) % 4]]
                   and determinant[target[i]][target[(i + 1) % 4]][target[(i + 2) % 4]]
                   == dets[i] * dets[(i + 1) % 4] % p for i in range(4))
    return audit


def evaluate(coefficients, x, p):
    answer = 0
    for a in reversed(coefficients):
        answer = (answer * x + a) % p
    return answer


def derivative_composition_data(p):
    states = list(product(range(p), repeat=p))
    values = {tuple(evaluate(f, x, p) for x in range(p)): f for f in states}
    require(len(values) == p ** p)
    def update(f):
        derivative = tuple((i * f[i]) % p for i in range(1, p))
        return values[tuple(evaluate(derivative, evaluate(f, x, p), p) for x in range(p))]
    return states, update


def wronskian_product_data(p):
    polynomials = list(product(range(p), repeat=p))
    index = {f: i for i, f in enumerate(polynomials)}
    def multiply(f, g):
        return tuple(sum(f[i] * g[k - i] for i in range(k + 1)) % p for k in range(p))
    multiplication = [[index[multiply(f, g)] for g in polynomials] for f in polynomials]
    derivatives = [index[tuple(((k + 1) * f[k + 1]) % p for k in range(p - 1)) + (0,)]
                   for f in polynomials]
    def update(pair):
        f, g = pair
        left = polynomials[multiplication[derivatives[f]][g]]
        right = polynomials[multiplication[f][derivatives[g]]]
        wronskian = index[tuple((a - b) % p for a, b in zip(left, right))]
        return wronskian, multiplication[f][g]
    return list(product(range(len(polynomials)), repeat=2)), update


def main():
    rows = []
    for d in (2, 3, 4, 5):
        table, inverse = permutation_group(d)
        root_counts = Counter(table[g][g] for g in range(len(table)))
        carrier = list(product(range(len(table)), repeat=2))
        rows.append(analyze("GHD", {"group": "S", "degree": d}, carrier,
                            lambda pair: (table[pair[0]][pair[1]], table[inverse[pair[0]]][pair[1]]),
                            fibre_size=lambda target: root_counts[table[target[0]][inverse[target[1]]]]))
        rows.append(analyze("TQP", {"group": "S", "degree": d}, carrier,
                            lambda pair: (table[table[pair[0]][pair[0]]][pair[1]],
                                          table[pair[0]][table[pair[1]][pair[1]]]),
                            audit=lambda pair, target:
                            table[target[0]][inverse[target[1]]]
                            == table[table[pair[0]][table[pair[0]][inverse[pair[1]]]]][inverse[pair[0]]]))
    for p in (2, 3):
        cross = cross_table(p)
        rows.append(analyze("XCY", {"prime": p, "vectors": 4, "dimension": 3},
                            product(range(p ** 3), repeat=4),
                            lambda state: tuple(cross[state[i]][state[(i + 1) % 4]] for i in range(4)),
                            audit=cross_cycle_audit(p, cross)))
    for p in (2, 3, 5):
        states, update = derivative_composition_data(p)
        rows.append(analyze("DCP", {"prime": p, "degree_less_than": p}, states, update))
    for name, table in (("C3", cyclic_group(3)), ("C4", cyclic_group(4)),
                        ("S3", permutation_group(3)[0]), ("D8", dihedral_eight()),
                        ("Q8", quaternion_eight()), ("A4", permutation_group(4, True)[0])):
        size = len(table)
        require(all(table[table[a][b]][c] == table[a][table[b][c]]
                    for a in range(size) for b in range(size) for c in range(size)))
        rows.append(analyze("UOP", {"group": name, "order": size}, range(1 << size),
                            lambda subset: unique_ordered_products(subset, table)))
    for p in (2, 3):
        states, update = wronskian_product_data(p)
        rows.append(analyze("WPP", {"prime": p, "truncation": p}, states, update))
    print(json.dumps({"status": "PILOT_COMPLETE_NOT_THEOREM", "literal_maps": 6,
                      "boxes": len(rows), "states_across_boxes": sum(row["states"] for row in rows),
                      "assertions": checks, "enumeration_sha256": digest.hexdigest(),
                      "profiles": rows}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
