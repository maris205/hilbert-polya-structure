#!/usr/bin/env python3
"""Exact theorem-interface replay for P143; standard library only."""

from collections import Counter
from functools import lru_cache


ASSERTIONS = 0


def check(value, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not value:
        raise AssertionError(message)


def rows(state, n):
    mask = (1 << n) - 1
    return tuple((state >> (n * i)) & mask for i in range(n))


def pack(values, n):
    return sum(value << (n * i) for i, value in enumerate(values))


def transpose(state, n):
    source = rows(state, n)
    target = [0] * n
    for i in range(n):
        for j in range(n):
            if source[i] >> j & 1:
                target[j] |= 1 << i
    return pack(target, n)


def step(state, n):
    source = rows(state, n)
    target = []
    for left in source:
        row = 0
        for j, right in enumerate(source):
            if left & ~right == 0:
                row |= 1 << j
        target.append(row)
    return pack(target, n)


def is_preorder(state, n):
    relation = rows(state, n)
    for i in range(n):
        if not (relation[i] >> i & 1):
            return False
        for j in range(n):
            if relation[i] >> j & 1 and relation[j] & ~relation[i]:
                return False
    return True


def quotient(state, n):
    relation = rows(state, n)
    unused = set(range(n))
    classes = []
    while unused:
        i = min(unused)
        block = tuple(j for j in sorted(unused)
                      if relation[i] >> j & 1 and relation[j] >> i & 1)
        classes.append(block)
        unused.difference_update(block)
    m = len(classes)
    mask = 0
    for a, left in enumerate(classes):
        for b, right in enumerate(classes):
            if relation[left[0]] >> right[0] & 1:
                mask |= 1 << (a * m + b)
    return m, mask


@lru_cache(None)
def closure(relation, m):
    row = [(relation >> (i * m)) & ((1 << m) - 1) for i in range(m)]
    for i in range(m):
        row[i] |= 1 << i
    for k in range(m):
        for i in range(m):
            if row[i] >> k & 1:
                row[i] |= row[k]
    return pack(row, m)


@lru_cache(None)
def upset_count(relation, m):
    relation = closure(relation, m)
    row = rows(relation, m)
    return sum(
        all(not (subset >> i & 1) or row[i] & ~subset == 0 for i in range(m))
        for subset in range(1 << m)
    )


def fibre_formula(target, n):
    if not is_preorder(target, n):
        return 0
    m, base = quotient(target, n)
    missing = [(i, j) for i in range(m) for j in range(m)
               if not (base >> (i * m + j) & 1)]
    answer = 0
    for selected in range(1 << len(missing)):
        relation = base
        for bit, (i, j) in enumerate(missing):
            if selected >> bit & 1:
                relation |= 1 << (i * m + j)
        term = upset_count(closure(relation, m), m) ** n
        answer += -term if selected.bit_count() & 1 else term
    return answer


def verify(n):
    universe = 1 << (n * n)
    image = set()
    fibres = Counter()
    for state in range(universe):
        first = step(state, n)
        second = step(first, n)
        third = step(second, n)
        check(is_preorder(first, n), (n, state, "image"))
        check(second == transpose(first, n), (n, state, "transpose"))
        check(third == first, (n, state, "T3"))
        image.add(first)
        fibres[first] += 1

    fixed = 0
    for target in range(universe):
        preorder = is_preorder(target, n)
        check((target in image) == preorder, (n, target, "surjectivity"))
        if preorder:
            is_fixed = step(target, n) == target
            check(is_fixed == (transpose(target, n) == target),
                  (n, target, "fixed/equivalence"))
            fixed += is_fixed

    for target in image:
        check(fibre_formula(target, n) == fibres[target],
              (n, target, "fibre formula"))
    check(sum(fibres.values()) == universe, (n, "mass"))
    return (universe, len(image), fixed, len(image) - fixed,
            min(fibres.values()), max(fibres.values()))


def main():
    expected = {
        1: (2, 1, 1, 0, 2, 2),
        2: (16, 4, 2, 2, 2, 5),
        3: (512, 29, 5, 24, 8, 24),
        4: (65536, 355, 15, 340, 16, 600),
    }
    print("P143 EXACT CONTROL")
    print("columns=n,states,preorders,fixed_equivalences,strict_2cycle_states,min_fibre,max_fibre")
    for n in range(1, 5):
        result = verify(n)
        check(result == expected[n], (n, result, expected[n]))
        print(n, *result, sep=",")
    print(f"assertions={ASSERTIONS}")
    print("P143_THEOREM_INTERFACES_PASS")


if __name__ == "__main__":
    main()
