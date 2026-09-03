#!/usr/bin/env python3
"""Process-independent hostile verifier for P179.

Set partitions are tuples of disjoint integer bit masks.  This is unrelated
to the restricted-growth-word carrier used by the author.  Literal labelled
histories, an independently coded blockwise missing-set predicate, rational
eigenspace ranks, and the two notions of predecessor are compared exactly.
Only Python's standard library is used and no author module is imported.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb, factorial


ASSERTIONS = 0
ARROW_HASH = sha256()


def check(statement, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(label)


def mask_partitions(n):
    states = {()}
    for label in range(n):
        bit = 1 << label
        next_states = set()
        for state in states:
            next_states.add(tuple(sorted(state + (bit,))))
            for j in range(len(state)):
                blocks = list(state)
                blocks[j] |= bit
                next_states.add(tuple(sorted(blocks)))
        states = next_states
    return tuple(sorted(states))


def isolate(state, label):
    bit = 1 << label
    for j, block in enumerate(state):
        if block & bit:
            if block == bit:
                return state
            blocks = list(state)
            blocks[j] ^= bit
            blocks.append(bit)
            return tuple(sorted(blocks))
    raise AssertionError("label outside partition")


def apply_support(state, support, n):
    result = state
    for label in range(n):
        if support & (1 << label):
            result = isolate(result, label)
    return result


def singleton_count(state):
    return sum(block.bit_count() == 1 for block in state)


def no_singleton_bell(n):
    return sum(singleton_count(state) == 0 for state in mask_partitions(n))


def stirling2(t, r):
    if r < 0 or r > t:
        return 0
    row = [0] * (r + 1)
    row[0] = 1
    for _ in range(t):
        next_row = [0] * (r + 1)
        for k in range(1, r + 1):
            next_row[k] = row[k - 1] + k * row[k]
        row = next_row
    return row[r]


def elementary(values, degree):
    coefficients = [1] + [0] * degree
    for value in values:
        for j in range(degree, 0, -1):
            coefficients[j] += value * coefficients[j - 1]
    return coefficients[degree]


def rank_q(matrix):
    if not matrix:
        return 0
    work = [[Fraction(entry) for entry in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [entry / scale for entry in work[rank]]
        for row in range(len(work)):
            if row != rank and work[row][column]:
                scale = work[row][column]
                work[row] = [
                    x - scale * y for x, y in zip(work[row], work[rank])
                ]
        rank += 1
        if rank == len(work):
            break
    return rank


def is_refinement(target, initial):
    return all(any(block & ~old == 0 for old in initial) for block in target)


def admissible_missing(initial, target, missing):
    """The paper's blockwise cases, coded without applying any E_i map."""
    if not is_refinement(target, initial):
        return False
    for old in initial:
        inside = [block for block in target if block & old]
        if any(block & ~old for block in inside):
            return False
        nonsingletons = [block for block in inside if block.bit_count() >= 2]
        old_missing = old & missing
        if len(nonsingletons) == 1:
            if old_missing != nonsingletons[0]:
                return False
        elif len(nonsingletons) == 0:
            if old_missing.bit_count() > 1:
                return False
        else:
            return False
    return True


def exact_history_endpoints(initial, n, time):
    counts = Counter()
    for history in product(range(n), repeat=time):
        state = initial
        for label in history:
            state = isolate(state, label)
        counts[state] += 1
    return counts


def layer_string(layer):
    return ",".join(f"{s}:{layer[s]}" for s in sorted(layer))


def structural_and_inverse_boxes():
    rows = []
    for n in range(1, 9):
        states = mask_partitions(n)
        incoming_states = defaultdict(set)
        incoming_actions = Counter()
        for state in states:
            for i in range(n):
                once = isolate(state, i)
                ARROW_HASH.update(f"{n}:{state}:{i}>{once}\n".encode("ascii"))
                check(isolate(once, i) == once, f"idempotent n={n} i={i}")
                incoming_states[once].add(state)
                incoming_actions[once] += 1
            for i in range(n):
                for j in range(i + 1, n):
                    check(
                        isolate(isolate(state, i), j)
                        == isolate(isolate(state, j), i),
                        f"commute n={n} i={i} j={j}",
                    )

        layer = Counter(singleton_count(state) for state in states)
        predicted = Counter()
        for s in range(n + 1):
            value = comb(n, s) * no_singleton_bell(n - s)
            if value:
                predicted[s] = value
        check(layer == predicted, f"spectral layer n={n}")
        check(n - 1 not in layer, f"forbidden n-1 layer n={n}")
        check(layer[n] == 1, f"simple absorbing layer n={n}")

        for target in states:
            s = singleton_count(target)
            b = len(target)
            distinct = 0 if s == 0 else 1 + s * (b - s) + comb(s, 2)
            actions = s * b
            check(
                len(incoming_states[target]) == distinct,
                f"distinct predecessors n={n} target={target}",
            )
            check(
                incoming_actions[target] == actions,
                f"labelled predecessor-actions n={n} target={target}",
            )

        # The n=1 boundary simultaneously checks t=0 recurrence and both
        # predecessor conventions.
        if n == 1:
            sole = states[0]
            check(sole == (1,), "n=1 carrier")
            check(isolate(sole, 0) == sole, "n=1 fixed")
            check(len(incoming_states[sole]) == 1, "n=1 predecessor")
            check(incoming_actions[sole] == 1, "n=1 action")

        rows.append((n, len(states), layer, max(map(len, incoming_states.values()))))
    return rows


def exact_spectrum_boxes():
    for n in range(1, 6):
        states = mask_partitions(n)
        position = {state: i for i, state in enumerate(states)}
        size = len(states)
        # A=nP has one integer column per source; transposition is irrelevant
        # to eigenspace dimensions but this orientation matches linear action.
        matrix = [[0] * size for _ in range(size)]
        for source in states:
            column = position[source]
            for label in range(n):
                row = position[isolate(source, label)]
                matrix[row][column] += 1
        layers = Counter(singleton_count(state) for state in states)
        total_nullities = 0
        for s, multiplicity in sorted(layers.items()):
            shifted = [
                [
                    matrix[i][j] - (s if i == j else 0)
                    for j in range(size)
                ]
                for i in range(size)
            ]
            nullity = size - rank_q(shifted)
            check(nullity == multiplicity, f"geometric multiplicity n={n} s={s}")
            total_nullities += nullity
        check(total_nullities == size, f"diagonalizability n={n}")


def laws_boxes():
    # Every source/target pair, including time zero, is checked through n=5.
    for n in range(1, 6):
        states = mask_partitions(n)
        universe = (1 << n) - 1
        for initial in states:
            for time in range(0, 6):
                actual = exact_history_endpoints(initial, n, time)
                predicted = Counter()
                for target in states:
                    total = 0
                    for missing in range(1 << n):
                        if admissible_missing(initial, target, missing):
                            support_size = n - missing.bit_count()
                            total += factorial(support_size) * stirling2(
                                time, support_size
                            )
                    predicted[target] = total
                    check(
                        actual[target] == total,
                        f"exact support n={n} t={time} source={initial} target={target}",
                    )
                check(sum(predicted.values()) == n**time, f"kernel mass n={n} t={time}")

                # Independent support endpoint aggregation must agree with the
                # explicit admissibility predicate target by target.
                support_aggregation = Counter()
                for missing in range(1 << n):
                    r = n - missing.bit_count()
                    weight = factorial(r) * stirling2(time, r)
                    if weight:
                        support_aggregation[
                            apply_support(initial, universe ^ missing, n)
                        ] += weight
                check(support_aggregation == +actual, f"support action n={n} t={time}")

                absorbed_actual = actual[tuple(1 << label for label in range(n))]
                sizes = [block.bit_count() for block in initial]
                absorbed_formula = sum(
                    elementary(sizes, missing_count)
                    * factorial(n - missing_count)
                    * stirling2(time, n - missing_count)
                    for missing_count in range(len(sizes) + 1)
                )
                check(
                    absorbed_actual == absorbed_formula,
                    f"absorption CDF numerator n={n} t={time} source={initial}",
                )

    # Push the compressed absorption formula one Bell layer beyond the full
    # every-target box.
    n = 6
    discrete = tuple(1 << label for label in range(n))
    for initial in mask_partitions(n):
        sizes = [block.bit_count() for block in initial]
        for time in range(0, 5):
            actual = exact_history_endpoints(initial, n, time)[discrete]
            formula = sum(
                elementary(sizes, m)
                * factorial(n - m)
                * stirling2(time, n - m)
                for m in range(len(sizes) + 1)
            )
            check(actual == formula, f"absorption extended n=6 t={time}")


def main():
    rows = structural_and_inverse_boxes()
    exact_spectrum_boxes()
    laws_boxes()
    print("P179_REVIEWER_STOCHASTIC")
    for n, bell, layer, max_pred in rows:
        print(
            f"n={n} Bell={bell} singleton_layers={layer_string(layer)} "
            f"max_distinct_pred={max_pred}"
        )
    print("SPECTRUM=rational_geometric_multiplicities n<=5 PASS")
    print("KERNEL=every_source_every_target n<=5 t=0..5 PASS")
    print("ABSORPTION=every_source n<=6 t=0..4 PASS")
    print("PREDECESSORS=distinct_and_labelled n<=8 PASS")
    print(f"ASSERTIONS={ASSERTIONS}")
    print(f"ARROW_SHA256={ARROW_HASH.hexdigest()}")
    print("RESULT=PASS")
    print("RELEASE_SENTINEL=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
