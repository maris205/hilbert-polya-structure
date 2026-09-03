#!/usr/bin/env python3
"""Independent exact verifier for P174 minimum-pivot Mobius feedback.

The point ``p`` represents infinity in P^1(F_p).  This standard-library-only
program reconstructs the literal map, every complete carrier in the declared
prime boxes, the functional graph, and every target fibre.  It imports no
scouting or manuscript code.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path


PRIMES = (2, 3, 5, 7, 11, 13, 17, 19)


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)

    def equal(self, left, right, label: str) -> None:
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")


A = Audit()


def choose(n: int, r: int) -> int:
    if r < 0 or n < 0 or r > n:
        return 0
    return comb(n, r)


def is_prime(p: int) -> bool:
    return p >= 2 and all(p % d for d in range(2, int(p**0.5) + 1))


def inverse_nonzero(x: int, p: int) -> int:
    A.check(0 < x < p, f"inverse domain p={p}, x={x}")
    y = pow(x, p - 2, p)
    A.equal((x * y) % p, 1, f"F_p inverse p={p}, x={x}")
    return y


def pivot(state: tuple[int, ...], p: int) -> int:
    finite = [x for x in state if x != p]
    A.check(bool(finite), f"finite pivot exists p={p}, state={state}")
    return min(finite)


def mobius_feedback(state: tuple[int, ...], p: int) -> tuple[int, ...]:
    """Apply x -> 1/(x-a), where a is the least finite point."""
    a = pivot(state, p)
    target = []
    for x in state:
        if x == a:
            y = p
        elif x == p:
            y = 0
        else:
            y = inverse_nonzero((x - a) % p, p)
        target.append(y)
    return tuple(sorted(target))


def forced_source(target: tuple[int, ...], a: int, p: int) -> tuple[int, ...]:
    """Inverse of x -> 1/(x-a), before checking that a is the pivot."""
    source = []
    for y in target:
        if y == p:
            x = a
        elif y == 0:
            x = p
        else:
            x = (a + inverse_nonzero(y, p)) % p
        source.append(x)
    return tuple(sorted(source))


def inversion_on_core(state: tuple[int, ...], p: int) -> tuple[int, ...]:
    answer = []
    for x in state:
        if x == 0:
            answer.append(p)
        elif x == p:
            answer.append(0)
        else:
            answer.append(inverse_nonzero(x, p))
    return tuple(sorted(answer))


def fibre_height(target: tuple[int, ...], p: int) -> int:
    if p not in target:
        return 0
    inverse_labels = [inverse_nonzero(y, p) for y in target if 0 < y < p]
    return p - max(inverse_labels, default=0)


def fixed_formula(p: int, r: int) -> int:
    if p == 2:
        return choose(1, r)
    pairs = (p - 3) // 2
    total = 0
    for singles in range(3):
        remaining = r - singles
        if remaining >= 0 and remaining % 2 == 0:
            total += choose(2, singles) * choose(pairs, remaining // 2)
    return total


def tail_period(
    state: tuple[int, ...],
    successor: dict[tuple[int, ...], tuple[int, ...]],
) -> tuple[int, int]:
    seen: dict[tuple[int, ...], int] = {}
    point = state
    while point not in seen:
        seen[point] = len(seen)
        point = successor[point]
    return seen[point], len(seen) - seen[point]


def edge_digest(
    states: tuple[tuple[int, ...], ...],
    successor: dict[tuple[int, ...], tuple[int, ...]],
) -> str:
    digest = sha256()
    for state in states:
        digest.update(bytes(state))
        digest.update(b">")
        digest.update(bytes(successor[state]))
        digest.update(b";")
    return digest.hexdigest()


def audit_box(p: int, k: int) -> dict[str, object]:
    infinity = p
    states = tuple(combinations(range(p + 1), k))
    state_set = set(states)
    successor: dict[tuple[int, ...], tuple[int, ...]] = {}
    fibres: Counter[tuple[int, ...]] = Counter()
    pivot_masks: defaultdict[tuple[int, ...], int] = defaultdict(int)
    image_one: set[tuple[int, ...]] = set()
    image_two: set[tuple[int, ...]] = set()

    for state in states:
        a = pivot(state, p)
        target = mobius_feedback(state, p)
        A.equal(len(target), k, f"target size p={p}, k={k}")
        A.equal(len(set(target)), k, f"projectivity is injective p={p}, k={k}")
        A.check(target in state_set, f"carrier closure p={p}, k={k}")
        A.check(infinity in target, f"first image contains infinity p={p}, k={k}")
        A.equal(
            forced_source(target, a, p),
            state,
            f"pivot-labelled inverse reconstructs source p={p}, k={k}",
        )
        bit = 1 << a
        A.check(
            pivot_masks[target] & bit == 0,
            f"one source per target and pivot p={p}, k={k}",
        )
        pivot_masks[target] |= bit
        successor[state] = target
        fibres[target] += 1
        image_one.add(target)

    depths: Counter[int] = Counter()
    recurrent_periods: Counter[int] = Counter()
    fixed = 0
    for state in states:
        m1 = successor[state]
        m2 = successor[m1]
        m4 = successor[successor[m2]]
        image_two.add(m2)
        A.check(
            0 in m2 and infinity in m2,
            f"second image is in recurrent core p={p}, k={k}",
        )
        A.equal(m4, m2, f"M^4=M^2 pointwise p={p}, k={k}")
        actual_tail, actual_period = tail_period(state, successor)
        expected_tail = 0 if 0 in state and infinity in state else (
            1 if infinity in state else 2
        )
        A.equal(actual_tail, expected_tail, f"pointwise tail p={p}, k={k}")
        A.check(actual_period in (1, 2), f"period bound p={p}, k={k}")
        depths[actual_tail] += 1
        if actual_tail == 0:
            A.equal(
                m1,
                inversion_on_core(state, p),
                f"core action is inversion p={p}, k={k}",
            )
            recurrent_periods[actual_period] += 1
        fixed += m1 == state

    expected_z = {state for state in states if infinity in state}
    expected_y = {state for state in states if 0 in state and infinity in state}
    A.equal(image_one, expected_z, f"im(M)=Z p={p}, k={k}")
    A.equal(image_two, expected_y, f"im(M^2)=Y p={p}, k={k}")

    for target in states:
        h = fibre_height(target, p)
        A.equal(fibres[target], h, f"every-target fibre p={p}, k={k}")
        expected_mask = 0 if h == 0 else (1 << h) - 1
        A.equal(
            pivot_masks[target],
            expected_mask,
            f"pivot-marked fibre polynomial p={p}, k={k}",
        )
        for a in range(h):
            source = forced_source(target, a, p)
            A.check(source in state_set, f"forced source in carrier p={p}, k={k}")
            A.equal(pivot(source, p), a, f"forced pivot valid p={p}, k={k}")
            A.equal(
                mobius_feedback(source, p),
                target,
                f"forced source maps back p={p}, k={k}",
            )

    recurrent = choose(p - 1, k - 2)
    depth_one = choose(p - 1, k - 1)
    depth_two = choose(p, k)
    fixed_expected = fixed_formula(p, k - 2)
    A.equal(
        dict(sorted(depths.items())),
        {0: recurrent, 1: depth_one, 2: depth_two},
        f"exact depth layers p={p}, k={k}",
    )
    A.equal(fixed, fixed_expected, f"fixed coefficient p={p}, k={k}")
    A.equal(recurrent_periods[1], fixed_expected, f"fixed core points p={p}, k={k}")
    A.equal(
        recurrent_periods[2],
        recurrent - fixed_expected,
        f"two-periodic core points p={p}, k={k}",
    )
    A.equal(len(image_one), choose(p, k - 1), f"first-image size p={p}, k={k}")
    A.equal(len(image_two), recurrent, f"second-image size p={p}, k={k}")
    A.equal(sum(fibres.values()), len(states), f"fibre mass p={p}, k={k}")

    fibre_distribution = Counter(fibres[target] for target in states)
    A.equal(
        fibre_distribution[0], choose(p, k), f"zero-fibre targets p={p}, k={k}"
    )
    for h in range(1, p + 1):
        A.equal(
            fibre_distribution[h],
            choose(p - h, k - 2),
            f"positive fibre distribution p={p}, k={k}, h={h}",
        )
    maximum_fibre = max(fibres.values())
    A.equal(maximum_fibre, p - k + 2, f"maximum fibre p={p}, k={k}")
    A.equal(
        sum(h * choose(p - h, k - 2) for h in range(1, p + 1)),
        choose(p + 1, k),
        f"target-fibre mass identity p={p}, k={k}",
    )

    return {
        "p": p,
        "k": k,
        "states": len(states),
        "image_M": len(image_one),
        "image_M2": len(image_two),
        "depths": {str(d): depths[d] for d in sorted(depths)},
        "fixed": fixed,
        "two_cycles": (recurrent - fixed) // 2,
        "maximum_fibre": maximum_fibre,
        "edge_sha256": edge_digest(states, successor),
    }


def main() -> None:
    for p in PRIMES:
        A.check(is_prime(p), f"declared parameter is prime p={p}")

    boxes = []
    for p in PRIMES:
        for k in range(2, p + 1):
            boxes.append(audit_box(p, k))

    p = 2
    boundary_states = ((0, 2), (1, 2), (0, 1))
    boundary_edges = {state: mobius_feedback(state, p) for state in boundary_states}
    A.equal(boundary_edges[(0, 2)], (0, 2), "binary boundary fixed core")
    A.equal(boundary_edges[(1, 2)], (0, 2), "binary boundary depth one")
    A.equal(boundary_edges[(0, 1)], (1, 2), "binary boundary depth two")

    result = {
        "decision": "AUTHOR_ROUND0_PASS",
        "external_status": "PROVISIONAL_AMBER / HOLD_EXTERNAL",
        "literal_map": "M(S)={1/(x-a(S)):x in S}, a(S)=least finite point",
        "prime_boxes": list(PRIMES),
        "complete_parameter_boxes": len(boxes),
        "boxes": boxes,
        "boundary_p2_k2": {
            "states_in_orbit_order": [[0, 1], [1, 2], [0, 2]],
            "depths": [2, 1, 0],
            "fixed_core": [0, 2],
        },
        "assertions": A.assertions,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(result, indent=2, sort_keys=True, separators=(",", ": ")))


if __name__ == "__main__":
    main()
