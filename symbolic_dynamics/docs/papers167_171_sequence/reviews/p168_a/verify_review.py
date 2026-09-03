#!/usr/bin/env python3
"""Independent hostile verifier for P168.

This implementation deliberately differs from the author verifier:

* field elements are coefficient tuples rather than packed integers;
* the complete subspace lattice is discovered by a breadth-first closure
  under adjoining one vector rather than enumerated from RREF templates;
* fibres and weak components are reconstructed directly from the edge list.

The uniform theorem is proved in the manuscript.  This program is bounded
counterexample pressure for p=2 and p=3.
"""

from __future__ import annotations

from collections import Counter, deque
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json


class Audit:
    def __init__(self) -> None:
        self.n = 0

    def check(self, condition: bool, label: str) -> None:
        self.n += 1
        if not condition:
            raise AssertionError(label)

    def equal(self, left, right, label: str) -> None:
        self.n += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")


A = Audit()
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


class Field:
    def __init__(self, p: int, modulus: tuple[int, int, int, int, int]):
        self.p = p
        self.modulus = modulus
        self.elements = tuple(product(range(p), repeat=4))

    def add(self, x, y):
        return tuple((a + b) % self.p for a, b in zip(x, y))

    def scale(self, c: int, x):
        return tuple(c * a % self.p for a in x)

    def mul(self, x, y):
        p = self.p
        work = [0] * 7
        for i, a in enumerate(x):
            for j, b in enumerate(y):
                work[i + j] = (work[i + j] + a * b) % p
        for degree in range(6, 3, -1):
            lead = work[degree] % p
            if lead:
                for j in range(4):
                    work[degree - 4 + j] = (
                        work[degree - 4 + j] - lead * self.modulus[j]
                    ) % p
                work[degree] = 0
        return tuple(work[:4])

    def power(self, x, exponent: int):
        answer = ONE
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, x)
            x = self.mul(x, x)
            exponent //= 2
        return answer

    def inverse(self, x):
        A.check(x != ZERO, "zero has no inverse")
        answer = self.power(x, self.p**4 - 2)
        A.equal(self.mul(x, answer), ONE, "finite-field inverse")
        return answer


def rref(vectors, p: int):
    rows = [list(v) for v in vectors if v != ZERO]
    rank = 0
    for col in range(4):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col] % p), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, p)
        rows[rank] = [inv * z % p for z in rows[rank]]
        for i in range(len(rows)):
            if i == rank:
                continue
            coefficient = rows[i][col] % p
            if coefficient:
                rows[i] = [
                    (u - coefficient * v) % p
                    for u, v in zip(rows[i], rows[rank])
                ]
        rank += 1
        if rank == len(rows):
            break
    return tuple(tuple(row) for row in rows[:rank])


@lru_cache(maxsize=None)
def points(basis, p: int):
    out = set()
    for coefficients in product(range(p), repeat=len(basis)):
        vector = ZERO
        for coefficient, row in zip(coefficients, basis):
            vector = tuple(
                (x + coefficient * y) % p for x, y in zip(vector, row)
            )
        out.add(vector)
    A.equal(len(out), p ** len(basis), "span cardinality")
    return frozenset(out)


def discover_subspaces(field: Field):
    """Discover the lattice by repeatedly adjoining an outside vector."""
    known = {()}
    queue = deque([()])
    while queue:
        basis = queue.popleft()
        members = points(basis, field.p)
        for vector in field.elements:
            if vector in members:
                continue
            child = rref(basis + (vector,), field.p)
            if child not in known:
                known.add(child)
                queue.append(child)
    return tuple(sorted(known, key=lambda b: (len(b), b)))


def inverse_span(basis, field: Field):
    if not basis:
        return ()
    return rref(
        tuple(field.inverse(x) for x in points(basis, field.p) if x != ZERO),
        field.p,
    )


def scalar_multiple(c, basis, field: Field):
    return rref(tuple(field.mul(c, x) for x in basis), field.p)


def orbit_data(edges):
    tails = []
    periods = []
    cycles = set()
    for start in range(len(edges)):
        seen = {}
        path = []
        x = start
        while x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = edges[x]
        entry = seen[x]
        cycle = tuple(path[entry:])
        canonical = min(tuple(cycle[i:] + cycle[:i]) for i in range(len(cycle)))
        cycles.add(canonical)
        tails.append(entry)
        periods.append(len(cycle))
    return tails, periods, cycles


def weak_component_count(edges):
    neighbors = [set([edges[i]]) for i in range(len(edges))]
    for i, j in enumerate(edges):
        neighbors[j].add(i)
    unseen = set(range(len(edges)))
    count = 0
    while unseen:
        count += 1
        stack = [unseen.pop()]
        while stack:
            for y in neighbors[stack.pop()]:
                if y in unseen:
                    unseen.remove(y)
                    stack.append(y)
    return count


def verify_prime(p: int, modulus):
    before = A.n
    field = Field(p, modulus)

    # Independently validate that the chosen quotient is a field.
    inverses = {}
    for x in field.elements:
        if x != ZERO:
            inverses[x] = field.inverse(x)
    A.equal(len(inverses), p**4 - 1, "all nonzero elements invert")

    spaces = discover_subspaces(field)
    index = {space: i for i, space in enumerate(spaces)}
    L = p**3 + p**2 + p + 1
    P = (p**2 + 1) * (p**2 + p + 1)
    Q = p**2 + 1
    S = 2 + 2 * L + P
    R = 2 + L + Q
    F = 4 if p == 2 else 6
    A.equal(len(spaces), S, "Gaussian total")
    A.equal(Counter(map(len, spaces)), Counter({0: 1, 1: L, 2: P, 3: L, 4: 1}),
            "rank census")

    edges = []
    for space in spaces:
        target = inverse_span(space, field)
        A.check(target in index, "image is a discovered subspace")
        A.check(len(target) >= len(space), "rank monotonicity")
        edges.append(index[target])

    tails, periods, cycles = orbit_data(edges)
    recurrent = {i for i, tail in enumerate(tails) if tail == 0}
    fixed = {i for i, target in enumerate(edges) if i == target}
    A.equal(len(recurrent), R, "recurrent census")
    A.equal(len(fixed), F, "fixed census")
    A.equal(Counter(len(cycle) for cycle in cycles), Counter({1: F, 2: (R - F) // 2}),
            "cycle census")
    A.check(all(periods[i] in (1, 2) for i in recurrent), "periods divide two")

    # Construct the quadratic subfield by Frobenius, then all scalar copies.
    subfield_points = tuple(x for x in field.elements if field.power(x, p**2) == x)
    subfield = rref(subfield_points, p)
    A.equal(len(subfield), 2, "quadratic-subfield dimension")
    quadratic_copies = {
        scalar_multiple(c, subfield, field)
        for c in field.elements if c != ZERO
    }
    A.equal(len(quadratic_copies), Q, "quadratic scalar-copy census")
    expected_recurrent = {
        i for i, space in enumerate(spaces)
        if len(space) in (0, 1, 4) or space in quadratic_copies
    }
    A.equal(recurrent, expected_recurrent, "recurrent-state classification")

    # Rank transition and the characteristic-two jump.
    transition_ranks = Counter()
    for i, space in enumerate(spaces):
        target = spaces[edges[i]]
        transition_ranks[(len(space), len(target), i in recurrent)] += 1
        if i in recurrent:
            A.equal(edges[edges[i]], i, "recurrent involution")
        elif len(space) == 2:
            A.equal(len(target), 3 if p == 2 else 4, "non-subfield plane rank")
        elif len(space) == 3:
            A.equal(len(target), 4, "hyperplane rank")

    expected_depths = (
        Counter({0: R, 1: L, 2: P - Q})
        if p == 2 else Counter({0: R, 1: S - R})
    )
    A.equal(Counter(tails), expected_depths, "depth histogram")
    A.equal(max(tails), 2 if p == 2 else 1, "sharp height")

    # Direct positive-time fibre atlas through time four.
    powers = []
    current = list(range(S))
    for _ in range(4):
        current = [edges[x] for x in current]
        powers.append(Counter(current))
    full = next(i for i, space in enumerate(spaces) if len(space) == 4)
    for i, space in enumerate(spaces):
        for t, fibres in enumerate(powers, 1):
            if i in recurrent and i != full:
                wanted = 1
            elif i == full:
                wanted = (
                    1 + L if p == 2 and t == 1
                    else 1 + L + P - Q
                )
            elif p == 2 and len(space) == 3 and t == 1:
                wanted = 2
            else:
                wanted = 0
            A.equal(fibres[i], wanted, "all-target positive-time fibre")

    A.equal(len(set(edges)), R + L if p == 2 else R, "first-image size")
    A.equal(weak_component_count(edges), (R + F) // 2, "weak-component count")

    # Exhaustive scalar equivariance at p=2; deterministic spread at p=3.
    scalars = [x for x in field.elements if x != ZERO]
    tested_scalars = scalars if p == 2 else scalars[::4]
    tested_spaces = spaces if p == 2 else spaces[::3]
    for scalar in tested_scalars:
        inverse_scalar = inverses[scalar]
        for space in tested_spaces:
            lhs = inverse_span(scalar_multiple(scalar, space, field), field)
            rhs = scalar_multiple(inverse_scalar, inverse_span(space, field), field)
            A.equal(lhs, rhs, "twisted scalar equivariance")

    serial = [
        f"{p}:{space!r}>{spaces[edges[i]]!r}"
        for i, space in enumerate(spaces)
    ]
    return {
        "p": p,
        "checks": A.n - before,
        "states": S,
        "image": len(set(edges)),
        "recurrent": R,
        "fixed": F,
        "height": max(tails),
        "depths": dict(sorted(Counter(tails).items())),
        "cycle_lengths": dict(sorted(Counter(len(c) for c in cycles).items())),
        "full_fibres_t1_to_t4": [powers[t][full] for t in range(4)],
        "edge_sha256": sha256("\n".join(serial).encode()).hexdigest(),
        "transition_ranks": {
            str(key): value for key, value in sorted(transition_ranks.items())
        },
    }


def main() -> None:
    # x^4+x+1 and x^4+x^3+x^2+1 are irreducible over F_2 and F_3.
    rows = [
        verify_prime(2, (1, 1, 0, 0, 1)),
        verify_prime(3, (1, 0, 1, 1, 1)),
    ]
    report = {
        "decision": "HOSTILE_REVIEW_A_PASS",
        "external_status": "HOLD_EXTERNAL",
        "implementation": "tuple-field/subspace-BFS independent reconstruction",
        "rows": rows,
        "total_checks": A.n,
    }
    payload = json.dumps(report, sort_keys=True, separators=(",", ":"))
    report["payload_sha256"] = sha256(payload.encode()).hexdigest()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
