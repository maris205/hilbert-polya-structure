#!/usr/bin/env python3
"""Independent targeted verifier for P168 Hostile Review B.

This audit is deliberately disjoint from both retained implementations:

* states are projective incidence sets, not RREF templates or BFS bases;
* planes are generated as joins of projective points and hyperplanes as
  kernels of normalized coordinate functionals;
* inverses are computed in different quotient-field models;
* trace kernels, scalar orbits, incoming fibres, and the functional graph
  are reconstructed from incidence sets.

The complete carriers are checked for p=2 and p=5.  A separate formula sweep
checks all prime parameters through 97.  This remains bounded falsification,
not a substitute for the manuscript's all-prime proof.
"""

from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json


class Audit:
    def __init__(self):
        self.n = 0

    def check(self, condition, label):
        self.n += 1
        if not condition:
            raise AssertionError(label)

    def equal(self, actual, wanted, label):
        self.n += 1
        if actual != wanted:
            raise AssertionError(f"{label}: actual={actual!r}, wanted={wanted!r}")


AUDIT = Audit()
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


class QuarticField:
    def __init__(self, p, modulus):
        self.p = p
        self.modulus = modulus
        self.elements = tuple(product(range(p), repeat=4))

    def add(self, x, y):
        return tuple((a + b) % self.p for a, b in zip(x, y))

    def scale(self, a, x):
        return tuple((a * z) % self.p for z in x)

    def multiply(self, x, y):
        p = self.p
        work = [0] * 7
        for i, a in enumerate(x):
            for j, b in enumerate(y):
                work[i + j] = (work[i + j] + a * b) % p
        for degree in range(6, 3, -1):
            lead = work[degree]
            if lead:
                for j in range(4):
                    work[degree - 4 + j] = (
                        work[degree - 4 + j] - lead * self.modulus[j]
                    ) % p
        return tuple(work[:4])

    def power(self, x, exponent):
        value = ONE
        while exponent:
            if exponent & 1:
                value = self.multiply(value, x)
            x = self.multiply(x, x)
            exponent >>= 1
        return value

    def inverse(self, x):
        AUDIT.check(x != ZERO, "inverse domain excludes zero")
        y = self.power(x, self.p**4 - 2)
        AUDIT.equal(self.multiply(x, y), ONE, "field inverse identity")
        return y

    def trace(self, x):
        total = ZERO
        y = x
        for _ in range(4):
            total = self.add(total, y)
            y = self.power(y, self.p)
        AUDIT.equal(total[1:], (0, 0, 0), "trace lies in prime field")
        return total[0]


def normalize(v, p):
    if v == ZERO:
        raise ValueError("zero has no projective normalization")
    for x in v:
        if x % p:
            return tuple((z * pow(x, -1, p)) % p for z in v)
    raise AssertionError("nonzero scan failed")


def independent_basis(vectors, p):
    """Incremental echelon basis; no canonical/RREF state representation."""
    pivots = {}
    for original in vectors:
        row = list(original)
        for col in sorted(pivots):
            if row[col]:
                factor = row[col]
                row = [(a - factor * b) % p for a, b in zip(row, pivots[col])]
        pivot = next((j for j, x in enumerate(row) if x), None)
        if pivot is None:
            continue
        inv = pow(row[pivot], -1, p)
        row = [(inv * x) % p for x in row]
        for col in list(pivots):
            if pivots[col][pivot]:
                factor = pivots[col][pivot]
                pivots[col] = tuple(
                    (a - factor * b) % p for a, b in zip(pivots[col], row)
                )
        pivots[pivot] = tuple(row)
    return tuple(pivots[col] for col in sorted(pivots))


def projective_span(vectors, p):
    basis = independent_basis(vectors, p)
    points = set()
    for coefficients in product(range(p), repeat=len(basis)):
        v = tuple(
            sum(c * basis[i][j] for i, c in enumerate(coefficients)) % p
            for j in range(4)
        )
        if v != ZERO:
            points.add(normalize(v, p))
    wanted = (p ** len(basis) - 1) // (p - 1) if basis else 0
    AUDIT.equal(len(points), wanted, "projective span cardinality")
    return frozenset(points)


def projective_carrier(field):
    p = field.p
    points = tuple(sorted({normalize(v, p) for v in field.elements if v != ZERO}))
    L = p**3 + p**2 + p + 1
    AUDIT.equal(len(points), L, "projective point count")

    zero = frozenset()
    lines = {frozenset((x,)) for x in points}
    planes = {projective_span((x, y), p) for x, y in combinations(points, 2)}
    hyperplanes = set()
    for normal in points:
        hyperplanes.add(frozenset(
            x for x in points
            if sum(a * b for a, b in zip(normal, x)) % p == 0
        ))
    full = frozenset(points)
    spaces = {zero, full} | lines | planes | hyperplanes
    dimension = {}
    for space in spaces:
        size = len(space)
        d = next(d for d in range(5) if (p**d - 1) // (p - 1) == size)
        dimension[space] = d
    P = (p**2 + 1) * (p**2 + p + 1)
    AUDIT.equal(len(planes), P, "projective plane count")
    AUDIT.equal(len(hyperplanes), L, "kernel hyperplane count")
    AUDIT.equal(
        Counter(dimension.values()),
        Counter({0: 1, 1: L, 2: P, 3: L, 4: 1}),
        "incidence carrier rank census",
    )
    ordered = tuple(sorted(spaces, key=lambda s: (dimension[s], tuple(sorted(s)))))
    return points, ordered, dimension, hyperplanes


def map_state(space, field):
    if not space:
        return frozenset()
    inverse_points = [normalize(field.inverse(x), field.p) for x in space]
    return projective_span(inverse_points, field.p)


def scalar_state(c, space, field):
    if not space:
        return frozenset()
    return frozenset(normalize(field.multiply(c, x), field.p) for x in space)


def graph_orbits(edges):
    tails = []
    periods = []
    cycles = set()
    for start in range(len(edges)):
        seen = {}
        walk = []
        x = start
        while x not in seen:
            seen[x] = len(walk)
            walk.append(x)
            x = edges[x]
        entry = seen[x]
        cycle = walk[entry:]
        canonical = min(tuple(cycle[k:] + cycle[:k]) for k in range(len(cycle)))
        cycles.add(canonical)
        tails.append(entry)
        periods.append(len(cycle))
    return tails, periods, cycles


def weak_components(edges):
    adjacency = [set((edges[i],)) for i in range(len(edges))]
    for i, j in enumerate(edges):
        adjacency[j].add(i)
    unseen = set(range(len(edges)))
    components = []
    while unseen:
        component = {unseen.pop()}
        frontier = list(component)
        while frontier:
            x = frontier.pop()
            for y in adjacency[x]:
                if y in unseen:
                    unseen.remove(y)
                    component.add(y)
                    frontier.append(y)
        components.append(component)
    return components


def verify_prime(p, modulus):
    before = AUDIT.n
    field = QuarticField(p, modulus)

    # This certifies the chosen quotient model is a field without importing
    # the author's irreducibility finder.
    inverse = {}
    for x in field.elements:
        if x != ZERO:
            inverse[x] = field.inverse(x)
    AUDIT.equal(len(inverse), p**4 - 1, "all nonzero elements invert")

    points, spaces, dimension, hyperplanes = projective_carrier(field)
    index = {space: i for i, space in enumerate(spaces)}
    L = p**3 + p**2 + p + 1
    P = (p**2 + 1) * (p**2 + p + 1)
    Q = p**2 + 1
    S = 2 + 2 * L + P
    R = 2 + L + Q
    F = 4 if p == 2 else 6
    AUDIT.equal(len(spaces), S, "Gaussian carrier total")

    edges = []
    for space in spaces:
        target = map_state(space, field)
        AUDIT.check(target in index, "inverse span is in incidence carrier")
        AUDIT.check(dimension[target] >= dimension[space], "rank monotonicity")
        edges.append(index[target])

    tails, periods, cycles = graph_orbits(edges)
    recurrent = {i for i, d in enumerate(tails) if d == 0}
    fixed = {i for i, j in enumerate(edges) if i == j}
    AUDIT.equal(len(recurrent), R, "recurrent count")
    AUDIT.equal(len(fixed), F, "fixed count")
    AUDIT.equal(
        Counter(map(len, cycles)), Counter({1: F, 2: (R - F)//2}),
        "cycle census",
    )
    AUDIT.check(all(periods[i] <= 2 for i in recurrent), "recurrent periods <= 2")

    # Rebuild the scalar quadratic-subfield orbit from Frobenius fixed points.
    quadratic_vectors = [x for x in field.elements if field.power(x, p**2) == x]
    quadratic = projective_span(quadratic_vectors, p)
    AUDIT.equal(dimension[quadratic], 2, "quadratic subfield plane")
    scalar_quadratics = {scalar_state(c, quadratic, field) for c in points}
    AUDIT.equal(len(scalar_quadratics), Q, "scalar quadratic plane count")
    expected_recurrent = {
        i for i, space in enumerate(spaces)
        if dimension[space] in (0, 1, 4) or space in scalar_quadratics
    }
    AUDIT.equal(recurrent, expected_recurrent, "recurrent set classification")

    transitions = Counter()
    for i, space in enumerate(spaces):
        ds, dt = dimension[space], dimension[spaces[edges[i]]]
        transitions[(ds, dt, i in recurrent)] += 1
        if i in recurrent:
            AUDIT.equal(edges[edges[i]], i, "recurrent involution")
        elif ds == 2:
            AUDIT.equal(dt, 3 if p == 2 else 4, "transient plane rank")
        elif ds == 3:
            AUDIT.equal(dt, 4, "hyperplane rank")

    wanted_depths = (
        Counter({0: R, 1: L, 2: P-Q}) if p == 2
        else Counter({0: R, 1: S-R})
    )
    AUDIT.equal(Counter(tails), wanted_depths, "depth enumerator")

    # Every-target fibres are reconstructed from graph powers, not formulas.
    powers = []
    current = list(range(S))
    for _ in range(6):
        current = [edges[i] for i in current]
        powers.append(Counter(current))
    full = next(i for i, s in enumerate(spaces) if dimension[s] == 4)
    for t, fibres in enumerate(powers, 1):
        for i, space in enumerate(spaces):
            if i in recurrent and i != full:
                wanted = 1
            elif i == full:
                wanted = 1 + L if p == 2 and t == 1 else 1 + L + P - Q
            elif p == 2 and t == 1 and dimension[space] == 3:
                wanted = 2
            else:
                wanted = 0
            AUDIT.equal(fibres[i], wanted, "positive-time target fibre")

    # Independently reconstruct the trace parametrization of hyperplanes.
    trace_hyperplanes = {
        frozenset(x for x in points if field.trace(field.multiply(c, x)) == 0)
        for c in points
    }
    AUDIT.equal(trace_hyperplanes, hyperplanes, "trace kernels are all hyperplanes")
    seed_hyperplane = next(iter(hyperplanes))
    scalar_orbit = {scalar_state(c, seed_hyperplane, field) for c in points}
    AUDIT.equal(scalar_orbit, hyperplanes, "scalar action transitive on hyperplanes")

    incoming_planes = Counter()
    for i, space in enumerate(spaces):
        if dimension[space] == 2 and i not in recurrent:
            incoming_planes[spaces[edges[i]]] += 1
    if p == 2:
        AUDIT.equal(set(incoming_planes), hyperplanes, "binary hyperplane image support")
        AUDIT.check(all(incoming_planes[h] == 2 for h in hyperplanes),
                    "binary two-to-one plane fibres")
    else:
        AUDIT.equal(set(incoming_planes), {spaces[full]}, "odd plane image support")
        AUDIT.equal(incoming_planes[spaces[full]], P-Q, "odd plane fibre mass")

    components = weak_components(edges)
    AUDIT.equal(len(components), (R+F)//2, "weak component count")
    full_component = next(c for c in components if full in c)
    AUDIT.equal(len(full_component), 1 + L + P-Q, "full transient basin size")

    # Twisted equivariance is checked across the complete binary carrier and
    # a deterministic incidence cross-section at p=5.
    chosen_scalars = points if p == 2 else points[::11]
    chosen_states = spaces if p == 2 else spaces[::7]
    for c in chosen_scalars:
        cinv = field.inverse(c)
        for space in chosen_states:
            lhs_state = scalar_state(c, space, field)
            rhs_state = scalar_state(cinv, spaces[edges[index[space]]], field)
            AUDIT.equal(spaces[edges[index[lhs_state]]], rhs_state,
                        "twisted scalar equivariance")

    serial = [
        [dimension[space], sorted(space), dimension[spaces[edges[i]]], sorted(spaces[edges[i]])]
        for i, space in enumerate(spaces)
    ]
    return {
        "p": p,
        "modulus": modulus,
        "checks": AUDIT.n-before,
        "states": S,
        "image": len(set(edges)),
        "recurrent": len(recurrent),
        "fixed": len(fixed),
        "height": max(tails),
        "depths": dict(sorted(Counter(tails).items())),
        "cycles": dict(sorted(Counter(map(len, cycles)).items())),
        "full_fibres_t1_to_t6": [row[full] for row in powers],
        "transitions": {str(k): v for k, v in sorted(transitions.items())},
        "incidence_edge_sha256": sha256(
            json.dumps(serial, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
    }


def primes_through(n):
    return [p for p in range(2, n+1) if all(p % d for d in range(2, int(p**0.5)+1))]


def formula_sweep():
    rows = []
    for p in primes_through(97):
        L = p**3+p**2+p+1
        P = (p**2+1)*(p**2+p+1)
        Q = p**2+1
        S = 2+2*L+P
        R = 2+L+Q
        F = 2 + __import__("math").gcd(2, L) + __import__("math").gcd(2, Q)
        AUDIT.equal(S-R, L+P-Q, f"stratum partition p={p}")
        AUDIT.check(P-Q > 0, f"sharp transient planes exist p={p}")
        AUDIT.equal(F, 4 if p == 2 else 6, f"fixed parity p={p}")
        AUDIT.equal(1+L+P-Q, S-R+1, f"full basin fibre p={p}")
        AUDIT.check((R-F) % 2 == 0, f"two-cycle parity p={p}")
        if p == 2:
            AUDIT.equal((P-Q)//L, 2, "binary plane/hyperplane quotient")
        rows.append((p, S, R, F))
    return rows


def main():
    rows = [
        verify_prime(2, (1, 1, 1, 1, 1)),
        verify_prime(5, (1, 0, 4, 3, 1)),
    ]
    sweep = formula_sweep()
    report = {
        "decision": "HOSTILE_REVIEW_B_TARGETED_PASS",
        "implementation": "projective-incidence carrier / join-kernel enumeration",
        "scope": "complete p=2,p=5; formula sweep primes<=97",
        "rows": rows,
        "formula_sweep_rows": len(sweep),
        "total_checks": AUDIT.n,
    }
    payload = json.dumps(report, sort_keys=True, separators=(",", ":"))
    report["payload_sha256"] = sha256(payload.encode()).hexdigest()
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
