#!/usr/bin/env python3
"""Exact root controls for the P147--P151 breadth gate.

The program checks two literal systems.  It is a falsifier, not a proof or an
owner certificate.  All arithmetic is exact.
"""

from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb, factorial, log2


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


# ---------------------------------------------------------------------------
# XPF: codimension-one exterior-power dynamics on abelian p-group types.


def types_of_rank(r: int, e: int):
    for ascending in combinations_with_replacement(range(1, e + 1), r):
        yield tuple(reversed(ascending))


def exterior_codim_one(group_type: tuple[int, ...]) -> tuple[int, ...]:
    r = len(group_type)
    check(r >= 3, "XPF is scoped to rank at least three")
    return (group_type[-2],) + (group_type[-1],) * (r - 1)


def xpf_tail(group_type: tuple[int, ...]) -> int:
    first = exterior_codim_one(group_type)
    if first == group_type:
        return 0
    return 1 if exterior_codim_one(first) == first else 2


def audit_xpf() -> tuple[int, int, int]:
    state_total = 0
    box_total = 0
    largest_fibre = 0
    for r in range(3, 9):
        for e in range(1, 13):
            box_total += 1
            states = tuple(types_of_rank(r, e))
            state_total += len(states)
            check(len(states) == comb(e + r - 1, r), "XPF state census")

            incoming = defaultdict(int)
            terminal = defaultdict(int)
            tails = defaultdict(int)
            images = set()
            for lam in states:
                first = exterior_codim_one(lam)
                second = exterior_codim_one(first)
                third = exterior_codim_one(second)
                incoming[first] += 1
                terminal[second] += 1
                images.add(first)
                tail = xpf_tail(lam)
                tails[tail] += 1
                check(second == third, "XPF square is fixed")
                check(tail in (0, 1, 2), "XPF tail range")
                check((tail == 0) == (len(set(lam)) == 1), "XPF fixed types")
                check((tail <= 1) == (lam[-2] == lam[-1]), "XPF tail-one gate")

            check(len(images) == e * (e + 1) // 2, "XPF image census")
            check(tails[0] == e, "XPF fixed census")
            check(
                tails[1] == comb(e + r - 2, r - 1) - e,
                "XPF depth-one census",
            )
            check(tails[2] == comb(e + r - 2, r), "XPF depth-two census")

            for target in states:
                a = target[-1]
                b = target[0]
                image_shape = target[1:] == (a,) * (r - 1) and b >= a
                expected = comb(e - b + r - 2, r - 2) if image_shape else 0
                check(incoming[target] == expected, "XPF every-target fibre")
                largest_fibre = max(largest_fibre, incoming[target])

                terminal_shape = target == (a,) * r
                terminal_expected = (
                    comb(e - a + r - 1, r - 1) if terminal_shape else 0
                )
                check(
                    terminal[target] == terminal_expected,
                    "XPF terminal every-target fibre",
                )
    return box_total, state_total, largest_fibre


# ---------------------------------------------------------------------------
# EQC: coarsen a labelled set partition by equal block cardinality.


Partition = tuple[tuple[int, ...], ...]


def canonical_partition(blocks) -> Partition:
    normalized = [tuple(sorted(block)) for block in blocks if block]
    normalized.sort(key=lambda block: block[0])
    return tuple(normalized)


def set_partitions(n: int):
    if n == 0:
        yield ()
        return

    def extend(i: int, blocks: list[list[int]]):
        if i == n:
            yield canonical_partition(blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from extend(i + 1, blocks)
            blocks[j].pop()
        blocks.append([i])
        yield from extend(i + 1, blocks)
        blocks.pop()

    yield from extend(1, [[0]])


def equal_cardinality_coarsening(partition: Partition) -> Partition:
    by_size: dict[int, list[int]] = defaultdict(list)
    for block in partition:
        by_size[len(block)].extend(block)
    return canonical_partition(by_size.values())


def eqc_tail(partition: Partition) -> int:
    seen = set()
    current = partition
    tail = 0
    while True:
        check(current not in seen, "EQC has no nontrivial cycle")
        seen.add(current)
        nxt = equal_cardinality_coarsening(current)
        if nxt == current:
            return tail
        check(len(nxt) < len(current), "EQC strict block descent")
        current = nxt
        tail += 1


@lru_cache(maxsize=None)
def divisors(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def equipartitions(block_size: int, part_size: int) -> int:
    multiplicity = block_size // part_size
    return factorial(block_size) // (
        factorial(part_size) ** multiplicity * factorial(multiplicity)
    )


def predicted_eqc_fibre(target: Partition) -> int:
    sizes = tuple(len(block) for block in target)

    def rec(i: int, used: frozenset[int]) -> int:
        if i == len(sizes):
            return 1
        total = 0
        b = sizes[i]
        for s in divisors(b):
            if s not in used:
                total += equipartitions(b, s) * rec(i + 1, used | {s})
        return total

    return rec(0, frozenset())


def fixed_partition_count(n: int) -> int:
    # Choose a set of distinct block sizes summing to n; labels are then
    # distributed among the uniquely sized blocks.
    total = 0

    def rec(next_size: int, remaining: int, denominator: int) -> None:
        nonlocal total
        if remaining == 0:
            total += factorial(n) // denominator
            return
        for size in range(next_size, remaining + 1):
            rec(size + 1, remaining - size, denominator * factorial(size))

    rec(1, n, 1)
    return total


def binary_cascade_partition(t: int) -> Partition:
    sizes = [2**j for j in range(t - 1, 0, -1)] + [1, 1]
    blocks = []
    cursor = 0
    for size in sizes:
        blocks.append(tuple(range(cursor, cursor + size)))
        cursor += size
    check(cursor == 2**t, "EQC cascade size")
    return canonical_partition(blocks)


def audit_eqc() -> tuple[int, int, int, int]:
    state_total = 0
    image_total = 0
    largest_fibre = 0
    maximum_tail = 0
    for n in range(1, 10):
        states = tuple(set_partitions(n))
        state_total += len(states)
        incoming = defaultdict(int)
        fixed = 0
        for partition in states:
            target = equal_cardinality_coarsening(partition)
            incoming[target] += 1
            tail = eqc_tail(partition)
            maximum_tail = max(maximum_tail, tail)
            sizes = tuple(map(len, partition))
            is_fixed = len(set(sizes)) == len(sizes)
            fixed += int(is_fixed)
            check((target == partition) == is_fixed, "EQC fixed criterion")
            check(tail <= int(log2(n)), "EQC logarithmic clock")
        check(fixed == fixed_partition_count(n), "EQC fixed EGF coefficient")

        for target in states:
            predicted = predicted_eqc_fibre(target)
            check(incoming[target] == predicted, "EQC every-target fibre")
            check((incoming[target] > 0) == (predicted > 0), "EQC image gate")
            image_total += int(incoming[target] > 0)
            largest_fibre = max(largest_fibre, incoming[target])

    for t in range(1, 10):
        witness = binary_cascade_partition(t)
        check(eqc_tail(witness) == t, "EQC sharp binary cascade")

    return state_total, image_total, maximum_tail, largest_fibre


def main() -> None:
    xpf_boxes, xpf_states, xpf_max_fibre = audit_xpf()
    eqc_states, eqc_images, eqc_max_tail, eqc_max_fibre = audit_eqc()
    print("P147-P151 ROOT SCOUT")
    print(
        "XPF "
        f"boxes={xpf_boxes} states={xpf_states} max_one_step_fibre={xpf_max_fibre} "
        "status=CONDITIONAL_REENTRY_OWNER_HEAVY"
    )
    print(
        "EQC "
        f"labelled_states={eqc_states} image_targets={eqc_images} "
        f"small_box_max_tail={eqc_max_tail} max_one_step_fibre={eqc_max_fibre} "
        "status=STRONG_OWNER_SEARCH_REQUIRED"
    )
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
