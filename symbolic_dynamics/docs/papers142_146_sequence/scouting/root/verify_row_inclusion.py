#!/usr/bin/env python3
"""Exact finite checks for the Boolean row-inclusion preorder dynamics.

For an n x n Boolean matrix A with row supports R_i, define

    T(A)_{ij} = 1  iff  R_i is a subset of R_j.

The script exhausts every matrix through n=4, checks T^3=T, identifies the
periodic set, and independently checks the inclusion--exclusion fibre formula
over the quotient poset of every preorder target.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def unpack_rows(state: int, n: int) -> tuple[int, ...]:
    mask = (1 << n) - 1
    return tuple((state >> (n * i)) & mask for i in range(n))


def pack_rows(rows: tuple[int, ...], n: int) -> int:
    return sum(row << (n * i) for i, row in enumerate(rows))


def transpose(state: int, n: int) -> int:
    rows = unpack_rows(state, n)
    out = [0] * n
    for i in range(n):
        for j in range(n):
            if (rows[i] >> j) & 1:
                out[j] |= 1 << i
    return pack_rows(tuple(out), n)


def row_inclusion(state: int, n: int) -> int:
    rows = unpack_rows(state, n)
    out = []
    for left in rows:
        relation_row = 0
        for j, right in enumerate(rows):
            if left & ~right == 0:
                relation_row |= 1 << j
        out.append(relation_row)
    return pack_rows(tuple(out), n)


def is_preorder(state: int, n: int) -> bool:
    rows = unpack_rows(state, n)
    for i in range(n):
        if not ((rows[i] >> i) & 1):
            return False
        for j in range(n):
            if (rows[i] >> j) & 1 and rows[j] & ~rows[i]:
                return False
    return True


def is_equivalence(state: int, n: int) -> bool:
    return is_preorder(state, n) and transpose(state, n) == state


def quotient_poset(state: int, n: int) -> tuple[int, int]:
    """Return (m, relation mask) for the antisymmetric quotient of a preorder."""
    rows = unpack_rows(state, n)
    unseen = set(range(n))
    classes: list[tuple[int, ...]] = []
    while unseen:
        i = min(unseen)
        cls = tuple(j for j in sorted(unseen) if ((rows[i] >> j) & 1) and ((rows[j] >> i) & 1))
        classes.append(cls)
        unseen.difference_update(cls)
    m = len(classes)
    relation = 0
    for a, ca in enumerate(classes):
        for b, cb in enumerate(classes):
            if (rows[ca[0]] >> cb[0]) & 1:
                relation |= 1 << (a * m + b)
    return m, relation


@lru_cache(maxsize=None)
def transitive_closure(relation: int, m: int) -> int:
    rows = [(relation >> (i * m)) & ((1 << m) - 1) for i in range(m)]
    for i in range(m):
        rows[i] |= 1 << i
    for k in range(m):
        bit = 1 << k
        for i in range(m):
            if rows[i] & bit:
                rows[i] |= rows[k]
    return sum(row << (i * m) for i, row in enumerate(rows))


@lru_cache(maxsize=None)
def number_of_upsets(relation: int, m: int) -> int:
    relation = transitive_closure(relation, m)
    rows = tuple((relation >> (i * m)) & ((1 << m) - 1) for i in range(m))
    count = 0
    for subset in range(1 << m):
        if all(not ((subset >> i) & 1) or rows[i] & ~subset == 0 for i in range(m)):
            count += 1
    return count


def fibre_formula(state: int, n: int) -> int:
    """Count induced order embeddings Q -> B_n by inclusion--exclusion."""
    m, base = quotient_poset(state, n)
    missing = [
        (i, j)
        for i in range(m)
        for j in range(m)
        if not ((base >> (i * m + j)) & 1)
    ]
    total = 0
    # Each selected missing pair enforces the unwanted inclusion f(i) <= f(j).
    for choice in range(1 << len(missing)):
        relation = base
        parity = 0
        for bit, (i, j) in enumerate(missing):
            if (choice >> bit) & 1:
                relation |= 1 << (i * m + j)
                parity ^= 1
        ways = number_of_upsets(transitive_closure(relation, m), m) ** n
        total += -ways if parity else ways
    return total


def bell_number(n: int) -> int:
    # B_{r+1} = sum_{k=0}^r binom(r,k) B_k.
    bells = [1]
    for r in range(n):
        bells.append(sum(combinations_count(r, k) * bells[k] for k in range(r + 1)))
    return bells[n]


def combinations_count(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k > n - k:
        k = n - k
    answer = 1
    for j in range(1, k + 1):
        answer = answer * (n - k + j) // j
    return answer


def verify_size(n: int) -> dict[str, object]:
    universe = 1 << (n * n)
    fibres: Counter[int] = Counter()
    image: set[int] = set()
    fixed = 0
    strict_two_cycle_states = 0
    tail_histogram: Counter[int] = Counter()

    for state in range(universe):
        first = row_inclusion(state, n)
        second = row_inclusion(first, n)
        third = row_inclusion(second, n)
        check(is_preorder(first, n), f"image is not a preorder: n={n}, state={state}")
        check(second == transpose(first, n), f"T(P) != P^op: n={n}, state={state}")
        check(third == first, f"T^3 != T: n={n}, state={state}")
        fibres[first] += 1
        image.add(first)

    for state in range(universe):
        preorder = is_preorder(state, n)
        check((state in image) == preorder, f"image/preorder mismatch: n={n}, state={state}")
        if preorder:
            if row_inclusion(state, n) == state:
                fixed += 1
            else:
                strict_two_cycle_states += 1
            tail_histogram[0] += 1
        else:
            tail_histogram[1] += 1

    check(fixed == bell_number(n), f"fixed/Bell mismatch for n={n}")
    check(strict_two_cycle_states == len(image) - fixed, f"periodic partition mismatch for n={n}")
    check(sum(fibres.values()) == universe, f"fibre mass mismatch for n={n}")

    formula_checks = 0
    for target in sorted(image):
        predicted = fibre_formula(target, n)
        check(predicted == fibres[target], f"fibre formula mismatch: n={n}, target={target}")
        formula_checks += 1

    return {
        "n": n,
        "states": universe,
        "preorders": len(image),
        "equivalences_fixed": fixed,
        "strict_two_cycle_states": strict_two_cycle_states,
        "tail_histogram": dict(sorted(tail_histogram.items())),
        "fibre_formula_targets": formula_checks,
        "fibre_min": min(fibres.values()),
        "fibre_max": max(fibres.values()),
        "fibre_max_multiplicity": sum(value == max(fibres.values()) for value in fibres.values()),
    }


def main() -> None:
    expected_preorders = {1: 1, 2: 4, 3: 29, 4: 355}
    expected_bells = {1: 1, 2: 2, 3: 5, 4: 15}
    print("BOOLEAN ROW-INCLUSION PREORDER DYNAMICS")
    print("map: T(A)_ij = 1 iff row_i(A) subseteq row_j(A)")
    print("scope: exhaustive over every n x n Boolean matrix for 1 <= n <= 4")
    for n in range(1, 5):
        result = verify_size(n)
        check(result["preorders"] == expected_preorders[n], f"known preorder count mismatch at n={n}")
        check(result["equivalences_fixed"] == expected_bells[n], f"known Bell count mismatch at n={n}")
        print(result)
    print(f"assertions={ASSERTIONS}")
    print("THEOREM_CHECKS_PASS")


if __name__ == "__main__":
    main()
