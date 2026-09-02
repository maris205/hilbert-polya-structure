#!/usr/bin/env python3
"""Exact finite audit for P160.

Enumeration is bounded counterexample pressure, not a proof or novelty test.
The script is deterministic and uses only the Python standard library.
"""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message=None):
        self.assertions += 1
        if not condition:
            raise AssertionError(message or f"assertion {self.assertions} failed")


A = Audit()


def star(x, y):
    return x if x == y else x ^ y


def step(state):
    a, b, c = state
    return star(b, c), star(c, a), star(a, b)


def kind(state):
    a, b, c = state
    distinct = len({a, b, c})
    if distinct == 1:
        return "diagonal"
    if distinct == 2:
        return "two_equal"
    return "block" if a ^ b ^ c == 0 else "nonblock"


def parameter_sources(target, rank):
    x, y, z = target
    return {(t, t ^ z, t ^ y) for t in range(1 << rank) if t not in (0, y, z)}


def linear_generator(value, rank, mode):
    if mode == "swap01":
        return (value & ~3) | ((value & 1) << 1) | ((value & 2) >> 1)
    if mode == "shear01":
        return value ^ ((value & 1) << 1)
    if mode == "rotate":
        mask = (1 << rank) - 1
        return ((value << 1) & mask) | (value >> (rank - 1))
    raise ValueError(mode)


def audit_rank(rank):
    points = tuple(range(1, 1 << rank))
    states = tuple(product(points, repeat=3))
    state_set = set(states)
    successor = {}
    indegree = Counter()
    predecessors = defaultdict(set)
    class_count = Counter()

    for state in states:
        target = step(state)
        A.check(target in state_set, ("closure", rank, state, target))
        successor[state] = target
        indegree[target] += 1
        predecessors[target].add(state)
        class_count[kind(state)] += 1

    npoints = len(points)
    expected_classes = {
        "diagonal": npoints,
        "two_equal": 3 * npoints * (npoints - 1),
        "block": npoints * (npoints - 1),
        "nonblock": npoints * (npoints - 1) * (npoints - 3),
    }
    A.check(dict(class_count) == {k: v for k, v in expected_classes.items() if v},
            (rank, class_count, expected_classes))

    fixed = 0
    periodic = 0
    image = set(successor.values())
    edge_payload = []
    fixed_iterate_counts = Counter()
    for state in states:
        target = successor[state]
        state_kind = kind(state)
        edge_payload.append(f"{state!r}->{target!r}")
        if state_kind in ("diagonal", "block"):
            A.check(target == state, ("fixed", rank, state))
            expected_period, expected_depth = 1, 0
            fixed += 1
            periodic += 1
        elif state_kind == "two_equal":
            A.check(step(step(step(state))) == state, ("third iterate", rank, state))
            A.check(target != state and step(target) != state, ("strict period", rank, state))
            expected_period, expected_depth = 3, 0
            periodic += 1
        else:
            A.check(kind(target) == "block", ("collapse", rank, state, target))
            A.check(successor[target] == target, ("depth one", rank, state))
            expected_period, expected_depth = 1, 1

        cursor = state
        first_seen = {}
        path = []
        while cursor not in first_seen:
            first_seen[cursor] = len(path)
            path.append(cursor)
            cursor = successor[cursor]
        depth = first_seen[cursor]
        period = len(path) - depth
        A.check((period, depth) == (expected_period, expected_depth),
                ("orbit", rank, state, period, depth))

        expected_fibre = npoints - 2 if state_kind == "block" else (
            0 if state_kind == "nonblock" else 1)
        A.check(indegree[state] == expected_fibre,
                ("fibre", rank, state, indegree[state], expected_fibre))

        for permutation in ((1, 0, 2), (1, 2, 0)):
            permuted = tuple(state[index] for index in permutation)
            expected = tuple(target[index] for index in permutation)
            A.check(step(permuted) == expected,
                    ("coordinate equivariance", rank, state, permutation))
        for mode in ("swap01", "shear01", "rotate"):
            transformed = tuple(linear_generator(value, rank, mode) for value in state)
            transformed_target = tuple(linear_generator(value, rank, mode) for value in target)
            A.check(step(transformed) == transformed_target,
                    ("linear equivariance", rank, state, mode))

        for exponent in range(1, 8):
            iterate = state
            for _ in range(exponent):
                iterate = successor[iterate]
            should_fix = state_kind in ("diagonal", "block") or (
                state_kind == "two_equal" and exponent % 3 == 0)
            A.check((iterate == state) == should_fix,
                    ("fixed iterate", rank, state, exponent))
            fixed_iterate_counts[exponent] += iterate == state

    A.check(fixed == npoints ** 2)
    A.check(periodic == 4 * npoints ** 2 - 3 * npoints)
    A.check(len(image) == periodic)

    unseen = set(states)
    components = 0
    while unseen:
        components += 1
        stack = [unseen.pop()]
        while stack:
            state = stack.pop()
            neighbours = predecessors[state] | {successor[state]}
            fresh = neighbours & unseen
            unseen.difference_update(fresh)
            stack.extend(fresh)
    A.check(components == 2 * npoints ** 2 - npoints)

    for exponent in range(1, 6):
        actual_moment = sum(indegree[state] ** exponent for state in states)
        predicted_moment = (
            3 * npoints ** 2 - 2 * npoints
            + npoints * (npoints - 1) * (npoints - 2) ** exponent
        )
        A.check(actual_moment == predicted_moment,
                ("fibre moment", rank, exponent, actual_moment, predicted_moment))
    A.check(sum(indegree[state] == 0 for state in states)
            == npoints * (npoints - 1) * (npoints - 3))
    actual_fibre_histogram = Counter(indegree[state] for state in states)
    predicted_fibre_histogram = Counter()
    predicted_fibre_histogram[0] += npoints * (npoints - 1) * (npoints - 3)
    predicted_fibre_histogram[1] += 3 * npoints ** 2 - 2 * npoints
    predicted_fibre_histogram[npoints - 2] += npoints * (npoints - 1)
    predicted_fibre_histogram += Counter()
    A.check(actual_fibre_histogram == predicted_fibre_histogram,
            ("fibre histogram", rank, actual_fibre_histogram, predicted_fibre_histogram))
    A.check((max(actual_fibre_histogram) + 3).bit_length() - 1 == rank
            and 1 << rank == max(actual_fibre_histogram) + 3,
            ("rank recovery", rank, actual_fibre_histogram))

    for target in states:
        if kind(target) != "block":
            continue
        sources = predecessors[target]
        parametrized = parameter_sources(target, rank)
        A.check(sources == parametrized, ("parameter set", rank, target))
        A.check(len(sources) == npoints - 2)
        A.check(target in sources)
        A.check(sum(kind(source) == "nonblock" for source in sources) == npoints - 3)

    expected_fixed_iterates = {
        exponent: (4 * npoints ** 2 - 3 * npoints if exponent % 3 == 0 else npoints ** 2)
        for exponent in range(1, 8)
    }
    A.check(dict(fixed_iterate_counts) == expected_fixed_iterates)

    signature = sha256("\n".join(edge_payload).encode()).hexdigest()[:16]
    cycles3 = npoints * (npoints - 1)
    transient = npoints * (npoints - 1) * (npoints - 3)
    return (
        f"RANK r={rank} N={npoints} states={len(states)} fixed={fixed} "
        f"cycles3={cycles3} periodic={periodic} depth1={transient} "
        f"components={components} fibres=0,1,{npoints - 2} edge_sha16={signature}"
    )


def main():
    print("P160 BINARY-PROJECTIVE STEINER TRIANGLE COLLAPSE EXACT AUDIT")
    print("ROLE bounded counterexample pressure; proof/owner/novelty/release=NO")
    for rank in range(2, 7):
        print(audit_rank(rank))
    print(f"ASSERTIONS={A.assertions}")
    print("STATUS=PASS")
    print("EXTERNAL_STATUS=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
