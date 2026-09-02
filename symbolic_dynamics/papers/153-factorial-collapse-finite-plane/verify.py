#!/usr/bin/env python3
"""Deterministic exact verifier for the factorial-collapse skew map.

For every audited odd prime p this script works only with the literal map

    T(x, y) = (x + 1, x*y)  on F_p^2.

It separately checks the closed iterate, the complete functional graph, the
labelled arms, every target fibre at every audited time, and fixed iterates.
No random sampling and no external package is used.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import hashlib


PRIMES = (
    3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
)


@dataclass
class Checks:
    assertions: int = 0

    def equal(self, got, expected, message: str) -> None:
        self.assertions += 1
        if got != expected:
            raise AssertionError(f"{message}: got {got!r}, expected {expected!r}")

    def true(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


def step(state: tuple[int, int], p: int) -> tuple[int, int]:
    """The literal one-step map, kept separate from every theorem formula."""
    x, y = state
    return ((x + 1) % p, (x * y) % p)


def literal_iterate(state: tuple[int, int], t: int, p: int) -> tuple[int, int]:
    out = state
    for _ in range(t):
        out = step(out, p)
    return out


def rising(x: int, t: int, p: int) -> int:
    out = 1
    for j in range(t):
        out = (out * (x + j)) % p
    return out


def iterate_formula(state: tuple[int, int], t: int, p: int) -> tuple[int, int]:
    x, y = state
    return ((x + t) % p, (y * rising(x, t, p)) % p)


def target_coefficient(u: int, t: int, p: int) -> int:
    """Coefficient of the forced source y in a t-step target (u,v)."""
    out = 1
    for r in range(1, t + 1):
        out = (out * (u - r)) % p
    return out


def first_collapse_depth(x: int, p: int) -> int:
    d = (1 - x) % p
    return p if d == 0 else d


def arm_vertex(a: int, depth: int, p: int) -> tuple[int, int]:
    """Depth-t vertex on the arm labelled by its depth-one ordinate a."""
    factorial = 1
    for j in range(1, depth):
        factorial = (factorial * j) % p
    signed_factorial = factorial if (depth - 1) % 2 == 0 else (-factorial) % p
    y = (a * pow(signed_factorial, -1, p)) % p
    return ((1 - depth) % p, y)


def orbit_shape(start: tuple[int, int], p: int) -> tuple[int, int, tuple[tuple[int, int], ...]]:
    seen: dict[tuple[int, int], int] = {}
    path: list[tuple[int, int]] = []
    state = start
    while state not in seen:
        seen[state] = len(path)
        path.append(state)
        state = step(state, p)
    mu = seen[state]
    period = len(path) - mu
    return mu, period, tuple(path[mu:])


def audit_prime(p: int, checks: Checks) -> str:
    states = [(x, y) for x in range(p) for y in range(p)]

    # Lane A: literal time stepping versus the rising-factorial closed iterate.
    # Retain the literal trajectory table so later exhaustive lanes do not
    # restart the same orbit from time zero for every query.
    trajectories: dict[tuple[int, int], list[tuple[int, int]]] = {}
    for state in states:
        current = state
        path = [current]
        x, y = state
        product = 1
        product_anchors = {0, 1, p - 1, p, p + 1, 2 * p, 2 * p + 3}
        for t in range(0, 3 * p + 1):
            if t <= 2 * p + 3:
                expected_closed = ((x + t) % p, (y * product) % p)
                checks.equal(current, expected_closed,
                             f"iterate p={p}, state={state}, t={t}")
                if t in product_anchors:
                    checks.equal(expected_closed, iterate_formula(state, t, p),
                                 f"direct-product anchor p={p}, state={state}, t={t}")
            current = step(current, p)
            path.append(current)
            product = (product * (x + t)) % p
        trajectories[state] = path
        checks.equal(path[p], (state[0], 0),
                     f"p-step collapse p={p}, state={state}")

    # Lane B: graph shape found from first repetitions, not from arm formulas.
    depths: Counter[int] = Counter()
    cycles: set[tuple[tuple[int, int], ...]] = set()
    for state in states:
        mu, period, cycle = orbit_shape(state, p)
        depths[mu] += 1
        checks.equal(period, p, f"eventual period p={p}, state={state}")
        checks.true(all(y == 0 for _, y in cycle),
                    f"cycle escaped y=0 p={p}, state={state}")
        expected_mu = 0 if state[1] == 0 else first_collapse_depth(state[0], p)
        checks.equal(mu, expected_mu, f"depth p={p}, state={state}")
        # Rotate each discovered cycle to a canonical representative.
        rotations = [cycle[k:] + cycle[:k] for k in range(len(cycle))]
        cycles.add(min(rotations))

    expected_depths = Counter({0: p, **{t: p - 1 for t in range(1, p + 1)}})
    checks.equal(depths, expected_depths, f"temporal polynomial p={p}")
    checks.equal(len(cycles), 1, f"cycle count p={p}")
    unique_cycle = next(iter(cycles))
    checks.equal(set(unique_cycle), {(x, 0) for x in range(p)}, f"axis cycle p={p}")

    # Literal indegrees distinguish the common entry and the arm endpoints.
    predecessors: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
    for state in states:
        predecessors[step(state, p)].append(state)
    for u, v in states:
        if (u, v) == (1, 0):
            expected_indegree = p
        elif u == 1 and v != 0:
            expected_indegree = 0
        else:
            expected_indegree = 1
        checks.equal(len(predecessors[(u, v)]), expected_indegree,
                     f"indegree p={p}, target={(u, v)}")

    # Lane C: labelled arms.  The label is y=a at depth one, not at depth p.
    arm_states: set[tuple[int, int]] = set()
    for a in range(1, p):
        checks.equal(arm_vertex(a, 1, p), (0, a), f"arm label p={p}, a={a}")
        checks.equal(arm_vertex(a, p, p), (1, (-a) % p),
                     f"Wilson endpoint p={p}, a={a}")
        for depth in range(1, p + 1):
            vertex = arm_vertex(a, depth, p)
            checks.true(vertex[1] != 0, f"arm hit axis p={p}, a={a}, depth={depth}")
            checks.true(vertex not in arm_states,
                        f"arms intersect p={p}, a={a}, depth={depth}")
            arm_states.add(vertex)
            expected_next = (1, 0) if depth == 1 else arm_vertex(a, depth - 1, p)
            checks.equal(step(vertex, p), expected_next,
                         f"arm arrow p={p}, a={a}, depth={depth}")
    checks.equal(arm_states, {(x, y) for x, y in states if y != 0},
                 f"arms cover all transients p={p}")

    # Lane D: complete target-by-target fibre atlas.  Times beyond p test the
    # saturated all-time clause as well as the requested 0 <= t <= p formula.
    image_sizes: list[int] = []
    coefficients = [1] * p
    for t in range(0, p + 4):
        fibres: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
        for source in states:
            fibres[trajectories[source][t]].append(source)
        literal_image_size = len(fibres)

        r = min(t, p)
        expected_distribution = Counter({
            1: p * (p - r),
            p: r,
            0: r * (p - 1),
        })
        # Counter drops no zero-valued key, whereas equal cardinalities can
        # merge keys only at p=1 (outside the audited odd-prime domain).
        actual_distribution = Counter(len(fibres[target]) for target in states)
        checks.equal(actual_distribution, expected_distribution,
                     f"fibre distribution p={p}, t={t}")
        expected_image = p * (p - r) + r
        checks.equal(literal_image_size, expected_image, f"image size p={p}, t={t}")
        image_sizes.append(literal_image_size)

        collapsed_columns = {u for u in range(p) if coefficients[u] == 0}
        expected_columns = ({r0 % p for r0 in range(1, t + 1)}
                            if t <= p else set(range(p)))
        checks.equal(collapsed_columns, expected_columns,
                     f"collapsed columns p={p}, t={t}")

        if t in {0, 1, p - 1, p, p + 3}:
            for u in range(p):
                checks.equal(coefficients[u], target_coefficient(u, t, p),
                             f"direct target coefficient p={p}, t={t}, u={u}")

        for u, v in states:
            c = coefficients[u]
            source_x = (u - t) % p
            actual = set(fibres[(u, v)])
            if c != 0:
                expected = {(source_x, (v * pow(c, -1, p)) % p)}
            elif v == 0:
                expected = {(source_x, y) for y in range(p)}
            else:
                expected = set()
            checks.equal(actual, expected, f"target fibre p={p}, t={t}, target={(u, v)}")

        # Symbolic integer shadows: target accounting and source mass balance.
        checks.equal(p * (p - r) + r + r * (p - 1), p * p,
                     f"target partition identity p={p}, t={t}")
        checks.equal(p * (p - r) + p * r, p * p,
                     f"source mass identity p={p}, t={t}")

        # c_{t+1}(u)=c_t(u)(u-(t+1)); update only after all t-lane checks.
        coefficients = [(coefficients[u] * (u - (t + 1))) % p for u in range(p)]

    # Lane E: fixed iterates and exact-period/cycle data.
    fixed_shadow: list[int] = []
    for n in range(1, 3 * p + 1):
        fixed = {state for state in states if trajectories[state][n] == state}
        expected = ({(x, 0) for x in range(p)} if n % p == 0 else set())
        checks.equal(fixed, expected, f"fixed iterate p={p}, n={n}")
        fixed_shadow.append(len(fixed))

    temporal_coefficients = [p] + [p - 1] * p
    checks.equal(sum(temporal_coefficients), p * p,
                 f"temporal mass p={p}")

    middle = p // 2
    return (
        f"BOX p={p:3d} states={p*p:5d} cycle_count=1 cycle_length={p:3d} "
        f"arms={p-1:3d} arm_depth={p:3d} "
        f"images[t=0,1,{middle},p,p+3]="
        f"{image_sizes[0]},{image_sizes[1]},{image_sizes[middle]},"
        f"{image_sizes[p]},{image_sizes[p+3]} "
        f"fixed_nonzero_times={[i+1 for i, value in enumerate(fixed_shadow) if value]}"
    )


def main() -> None:
    checks = Checks()
    profile: list[str] = []
    print("FTC_FACTORIAL_COLLAPSE_EXACT_REPLAY_V1")
    print("DOMAIN odd primes p; T(x,y)=(x+1,xy) on F_p^2")
    print("SYMBOLIC ITERATE T^t(x,y)=(x+t, y*PROD[j=0..t-1](x+j))")
    print("SYMBOLIC COLLAPSE T^p(x,y)=(x,0)")
    print("SYMBOLIC TEMPORAL p+(p-1)*(z+...+z^p)")
    print("SYMBOLIC IMAGE 0<=t<=p: p*(p-t)+t; t>=p: p")
    print("SYMBOLIC FIBRES c_t(u)=PROD[r=1..t](u-r): 1 if c!=0; p if c=0,v=0; 0 otherwise")
    print("SYMBOLIC FIX #Fix(T^n)=p*[p|n]; CYCLES one p-cycle; ZETA 1/(1-z^p)")
    for p in PRIMES:
        line = audit_prime(p, checks)
        profile.append(line)
        print(line)
    digest = hashlib.sha256("\n".join(profile).encode("utf-8")).hexdigest()
    print(f"PROFILE_SHA256 {digest}")
    print(f"TOTAL boxes={len(PRIMES)} states={sum(p*p for p in PRIMES)} assertions={checks.assertions}")
    print("VERDICT PASS_EXACT_REPLAY")


if __name__ == "__main__":
    main()
