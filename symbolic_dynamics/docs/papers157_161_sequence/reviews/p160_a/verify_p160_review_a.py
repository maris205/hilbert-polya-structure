#!/usr/bin/env python3
"""Independent hostile Review A audit for P160.

This program does not import or execute the author verifier.  It checks the
finite-map claims directly, adds an actual positive-iterate fibre audit, builds
the GL(r,2) x S3 orbits from generators, records the r=2 exponent collision,
and relates the depth-one shell to Pasch configurations.  An affine Steiner
quasigroup of order nine supplies a control against accidental generalization.

Enumeration is bounded counterexample pressure, not an all-rank proof,
ownership certificate, or novelty test.
"""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import permutations, product


class Ledger:
    def __init__(self):
        self.assertions = 0

    def require(self, condition, payload):
        self.assertions += 1
        if not condition:
            raise AssertionError((self.assertions, payload))


L = Ledger()


def sq(x, y):
    """Binary-projective Steiner operation on nonzero bit vectors."""
    return x if x == y else x ^ y


def update(state):
    a, b, c = state
    return sq(b, c), sq(c, a), sq(a, b)


def stratum(state):
    a, b, c = state
    distinct = len(set(state))
    if distinct == 1:
        return "diagonal"
    if distinct == 2:
        return "two_equal"
    return "block" if a ^ b ^ c == 0 else "nonblock"


def iterate(state, exponent):
    for _ in range(exponent):
        state = update(state)
    return state


def block_sources(target, rank):
    x, y, z = target
    return {
        (t, t ^ z, t ^ y)
        for t in range(1 << rank)
        if t not in {0, y, z}
    }


def swap_bits(value, i, j):
    bi, bj = (value >> i) & 1, (value >> j) & 1
    return value ^ ((bi ^ bj) << i) ^ ((bi ^ bj) << j)


def transvection(value, source, target):
    return value ^ ((((value >> source) & 1)) << target)


def state_generators(rank):
    generators = []
    for i in range(rank - 1):
        generators.append(
            lambda s, i=i: tuple(swap_bits(x, i, i + 1) for x in s)
        )
        generators.append(
            lambda s, i=i: tuple(transvection(x, i, i + 1) for x in s)
        )
    generators.extend(
        [
            lambda s: (s[1], s[0], s[2]),
            lambda s: (s[0], s[2], s[1]),
        ]
    )
    return generators


def generated_orbit(seed, rank):
    generators = state_generators(rank)
    orbit = {seed}
    frontier = [seed]
    while frontier:
        state = frontier.pop()
        for generator in generators:
            image = generator(state)
            if image not in orbit:
                orbit.add(image)
                frontier.append(image)
    return orbit


def pasch_configuration(state):
    """Four unordered triples determined by a nonblock input and its sides."""
    a, b, c = state
    x, y, z = update(state)
    return frozenset(
        {
            tuple(sorted((b, c, x))),
            tuple(sorted((c, a, y))),
            tuple(sorted((a, b, z))),
            tuple(sorted((x, y, z))),
        }
    )


def audit_binary_rank(rank):
    points = range(1, 1 << rank)
    states = tuple(product(points, repeat=3))
    state_set = set(states)
    n = len(tuple(points))
    by_kind = defaultdict(set)
    successor = {}
    predecessors = defaultdict(set)

    for state in states:
        image = update(state)
        L.require(image in state_set, ("closure", rank, state, image))
        successor[state] = image
        predecessors[image].add(state)
        by_kind[stratum(state)].add(state)

    expected_sizes = {
        "diagonal": n,
        "two_equal": 3 * n * (n - 1),
        "block": n * (n - 1),
        "nonblock": n * (n - 1) * (n - 3),
    }
    for name, expected in expected_sizes.items():
        L.require(len(by_kind[name]) == expected, ("class", rank, name))

    strict_cycles = set()
    fixed_states = set()
    for state in states:
        image = successor[state]
        kind = stratum(state)
        if kind in {"diagonal", "block"}:
            L.require(image == state, ("fixed", rank, state))
            fixed_states.add(state)
        elif kind == "two_equal":
            orbit = (state, iterate(state, 1), iterate(state, 2))
            L.require(len(set(orbit)) == 3, ("strict-three", rank, state))
            L.require(iterate(state, 3) == state, ("return-three", rank, state))
            L.require(all(stratum(x) == "two_equal" for x in orbit),
                      ("three-stratum", rank, state))
            strict_cycles.add(frozenset(orbit))
        else:
            L.require(stratum(image) == "block" and successor[image] == image,
                      ("one-step-collapse", rank, state, image))

    L.require(len(fixed_states) == n * n, ("fixed-count", rank))
    L.require(len(strict_cycles) == n * (n - 1), ("cycle-count", rank))
    L.require(sum(map(len, strict_cycles)) == 3 * n * (n - 1),
              ("cycle-states", rank))

    expected_fibre = {
        "diagonal": 1,
        "two_equal": 1,
        "block": n - 2,
        "nonblock": 0,
    }
    for target in states:
        fibre = predecessors[target]
        L.require(len(fibre) == expected_fibre[stratum(target)],
                  ("one-step-fibre", rank, target))
        if stratum(target) == "block":
            direct = block_sources(target, rank)
            L.require(fibre == direct, ("parameter-fibre", rank, target))
            L.require(target in direct, ("block-self-source", rank, target))
            L.require(sum(stratum(x) == "nonblock" for x in direct) == n - 3,
                      ("block-leaves", rank, target))

    # This check is deliberately stronger than the author's fixed-iterate loop:
    # calculate every S^k fibre, not merely which states are fixed by S^k.
    for exponent in range(1, 9):
        iterate_predecessors = Counter(iterate(state, exponent) for state in states)
        for target in states:
            L.require(iterate_predecessors[target] == expected_fibre[stratum(target)],
                      ("positive-iterate-fibre", rank, exponent, target))
        actual_fix = sum(iterate(state, exponent) == state for state in states)
        predicted_fix = 4 * n * n - 3 * n if exponent % 3 == 0 else n * n
        L.require(actual_fix == predicted_fix,
                  ("fixed-iterate", rank, exponent, actual_fix, predicted_fix))

    fibre_histogram = Counter(len(predecessors[target]) for target in states)
    predicted_histogram = Counter()
    predicted_histogram[0] += n * (n - 1) * (n - 3)
    predicted_histogram[1] += 3 * n * n - 2 * n
    predicted_histogram[n - 2] += n * (n - 1)
    predicted_histogram = +predicted_histogram
    L.require(fibre_histogram == predicted_histogram,
              ("fibre-histogram", rank, fibre_histogram, predicted_histogram))
    for moment in range(1, 7):
        actual = sum(size ** moment * multiplicity
                     for size, multiplicity in fibre_histogram.items())
        expected = 3 * n * n - 2 * n + n * (n - 1) * (n - 2) ** moment
        L.require(actual == expected, ("moment", rank, moment))

    maximum = max(fibre_histogram)
    L.require(maximum == n - 2, ("maximum-fibre", rank, maximum))
    L.require(maximum + 3 == (1 << rank), ("rank-recovery", rank, maximum))

    # Build weak components directly from the map's undirected shadow.
    unseen = set(states)
    component_sizes = []
    while unseen:
        seed = unseen.pop()
        component = {seed}
        frontier = [seed]
        while frontier:
            state = frontier.pop()
            for neighbour in predecessors[state] | {successor[state]}:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    component.add(neighbour)
                    frontier.append(neighbour)
        component_sizes.append(len(component))
    L.require(len(component_sizes) == 2 * n * n - n,
              ("component-count", rank))
    predicted_components = Counter({1: n + n * (n - 1), 3: n * (n - 1)})
    # For n=3, a zero-leaf block star is also a singleton; otherwise stars
    # have n-2 vertices (center plus n-3 leaves).
    if n > 3:
        predicted_components = Counter({1: n, 3: n * (n - 1), n - 2: n * (n - 1)})
    L.require(Counter(component_sizes) == predicted_components,
              ("component-shapes", rank, Counter(component_sizes), predicted_components))

    # Direct generator orbits for GL(r,2) x S3 (bounded to keep the reviewer
    # verifier independent and inexpensive).
    if rank <= 5:
        representatives = {
            "diagonal": (1, 1, 1),
            "two_equal": (1, 1, 2),
            "block": (1, 2, 3),
        }
        if rank >= 3:
            representatives["nonblock"] = (1, 2, 4)
        for name, representative in representatives.items():
            orbit = generated_orbit(representative, rank)
            L.require(orbit == by_kind[name],
                      ("GLxS3-orbit", rank, name, len(orbit), len(by_kind[name])))
        L.require((not by_kind["nonblock"]) == (rank == 2),
                  ("empty-orbit-boundary", rank))

    # The projective collapse is the maximal-Pasch property in ordered form.
    pasch_counts = Counter(pasch_configuration(s) for s in by_kind["nonblock"])
    L.require(all(len(configuration) == 4 for configuration in pasch_counts),
              ("pasch-four-blocks", rank))
    L.require(set(pasch_counts.values()) <= {24}, ("pasch-multiplicity", rank))
    expected_pasch = n * (n - 1) * (n - 3) // 24
    L.require(len(pasch_counts) == expected_pasch,
              ("pasch-count", rank, len(pasch_counts), expected_pasch))

    if rank == 2:
        L.require(fibre_histogram == Counter({1: 27}), ("r2-fibre-collision",))
        uncombined = Counter({1: 3 * n * n - 2 * n})
        uncombined[n - 2] += n * (n - 1)
        L.require(uncombined == Counter({1: 27}), ("r2-polynomial-collision",))
        L.require(4 / n - 3 / (n * n) == 1, ("r2-image-probability",))

    edge_digest = sha256(
        "\n".join(f"{state!r}->{successor[state]!r}" for state in states).encode()
    ).hexdigest()[:16]
    return (
        f"BINARY r={rank} N={n} states={len(states)} fixed_states={len(fixed_states)} "
        f"strict_3_cycles={len(strict_cycles)} strict_3_states={sum(map(len, strict_cycles))} "
        f"depth1={len(by_kind['nonblock'])} components={len(component_sizes)} "
        f"pasch={len(pasch_counts)} fibre_values={','.join(map(str, sorted(fibre_histogram)))} "
        f"edge_sha16={edge_digest}"
    )


def add3(x, y):
    return (x[0] + y[0]) % 3, (x[1] + y[1]) % 3


def neg3(x):
    return (-x[0]) % 3, (-x[1]) % 3


def affine_steiner(x, y):
    # -x-y is idempotent in characteristic three and is the third point on
    # the affine line through distinct x,y.
    return neg3(add3(x, y))


def affine_update(state):
    a, b, c = state
    return affine_steiner(b, c), affine_steiner(c, a), affine_steiner(a, b)


def affine_block(state):
    a, b, c = state
    return len(set(state)) == 3 and add3(add3(a, b), c) == (0, 0)


def audit_general_steiner_control():
    points = tuple(product(range(3), repeat=2))
    states = tuple(product(points, repeat=3))
    for x in points:
        L.require(affine_steiner(x, x) == x, ("affine-idempotent", x))
    for x in points:
        for y in points:
            L.require(affine_steiner(x, y) == affine_steiner(y, x),
                      ("affine-commutative", x, y))
            L.require(affine_steiner(x, affine_steiner(x, y)) == y,
                      ("affine-steiner-law", x, y))

    witness = ((0, 0), (1, 0), (0, 1))
    image = affine_update(witness)
    L.require(len(set(witness)) == 3 and not affine_block(witness),
              ("control-source-nonblock", witness))
    L.require(len(set(image)) == 3 and not affine_block(image),
              ("control-image-nonblock", witness, image))
    L.require(affine_update(affine_update(affine_update(witness))) == witness,
              ("control-three-period", witness))

    # Universal Steiner strata survive: diagonals and blocks are fixed;
    # two-equal states have exact period three.  The nonblock collapse does not.
    for state in states:
        image_state = affine_update(state)
        distinct = len(set(state))
        if distinct == 1 or affine_block(state):
            L.require(image_state == state, ("universal-fixed-strata", state))
        elif distinct == 2:
            L.require(affine_update(affine_update(image_state)) == state,
                      ("universal-two-equal-return", state))
            L.require(image_state != state and affine_update(image_state) != state,
                      ("universal-two-equal-strict", state))

    return (
        "GENERAL_STEINER_CONTROL carrier=AG(2,3) order=9 "
        f"nonblock_witness={witness!r} image={image!r} image_is_block=NO period=3"
    )


def main():
    print("P160 INDEPENDENT HOSTILE REVIEW A EXACT AUDIT")
    print("INDEPENDENCE author_verifier_imported=NO author_verifier_executed=NO")
    print("ROLE bounded counterexample pressure; proof/owner/novelty/release=NO")
    for rank in range(2, 7):
        print(audit_binary_rank(rank))
    print(audit_general_steiner_control())
    print(f"ASSERTIONS={L.assertions}")
    print("STATUS=PASS")
    print("EXTERNAL_STATUS=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
