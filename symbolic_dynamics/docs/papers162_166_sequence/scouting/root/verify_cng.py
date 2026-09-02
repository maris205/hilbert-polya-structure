#!/usr/bin/env python3
"""Exact scout for cyclic neighbour-GCD dynamics.

The prime-exponent shadow is the finite-chain cellular map

    T(a)_i = min(a_i,a_{i+1})

with cyclic indices.  The verifier exhausts several exponent boxes, checks
the sliding-window iterate, the longest-run depth theorem, the transfer-matrix
depth CDF, the complete one-step image criterion, and every one-step target
fibre.  A two-prime lane checks multiplicative factorisation on divisor tuples.
"""

from __future__ import annotations

from collections import Counter
from itertools import product


CASES = ((1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
         (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
         (3, 3), (3, 4), (3, 5))


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(f"{label} [assertion {self.assertions}]")


A = Audit()


def words(e: int, m: int):
    return tuple(product(range(e + 1), repeat=m))


def step(word):
    m = len(word)
    return tuple(min(word[i], word[(i + 1) % m]) for i in range(m))


def iterate(word, t: int):
    for _ in range(t):
        word = step(word)
    return word


def direct_iterate(word, t: int):
    m = len(word)
    return tuple(min(word[(i + j) % m] for j in range(t + 1)) for i in range(m))


def run_depth(word) -> int:
    minimum = min(word)
    flags = tuple(value > minimum for value in word)
    if not any(flags):
        return 0
    doubled = flags + flags
    longest = current = 0
    for flag in doubled:
        current = current + 1 if flag else 0
        longest = max(longest, current)
    return min(longest, len(word) - 1)


def mat_mul(left, right):
    rows, middle, columns = len(left), len(right), len(right[0])
    answer = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for k in range(middle):
            if left[i][k]:
                for j in range(columns):
                    answer[i][j] += left[i][k] * right[k][j]
    return answer


def mat_pow(matrix, exponent: int):
    size = len(matrix)
    answer = [[int(i == j) for j in range(size)] for i in range(size)]
    while exponent:
        if exponent & 1:
            answer = mat_mul(answer, matrix)
        matrix = mat_mul(matrix, matrix)
        exponent //= 2
    return answer


def trace(matrix) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def run_automaton(t: int, q: int):
    matrix = [[0] * (t + 1) for _ in range(t + 1)]
    for old in range(t + 1):
        matrix[old][0] = 1
        if old < t:
            matrix[old][old + 1] = q
    return matrix


def cdf_formula(e: int, m: int, t: int) -> int:
    return 1 + sum(trace(mat_pow(run_automaton(t, q), m)) for q in range(1, e + 1))


def local_minimum_free(target) -> bool:
    m = len(target)
    return all(not (target[i] < target[(i - 1) % m]
                       and target[i] < target[(i + 1) % m]) for i in range(m))


def canonical_source(target):
    m = len(target)
    return tuple(max(target[(i - 1) % m], target[i]) for i in range(m))


def one_step_transfer_fibre(target, e: int) -> int:
    matrices = []
    for beta in target:
        matrices.append([[int(min(r, s) == beta) for s in range(e + 1)]
                         for r in range(e + 1)])
    product_matrix = [[int(i == j) for j in range(e + 1)] for i in range(e + 1)]
    for matrix in matrices:
        product_matrix = mat_mul(product_matrix, matrix)
    return trace(product_matrix)


def all_time_transfer_fibre(target, e: int, t: int) -> int:
    """Trace of the memory-t de Bruijn transfer for sliding minima."""
    m = len(target)
    if t == 0:
        return 1
    contexts = tuple(product(range(e + 1), repeat=t))
    index = {context: i for i, context in enumerate(contexts)}
    matrices = []
    for beta in target:
        matrix = [[0] * len(contexts) for _ in contexts]
        for context in contexts:
            left = index[context]
            for new in range(e + 1):
                if min(context + (new,)) == beta:
                    shifted = context[1:] + (new,) if t > 1 else (new,)
                    matrix[left][index[shifted]] += 1
        matrices.append(matrix)
    product_matrix = [[int(i == j) for j in range(len(contexts))]
                      for i in range(len(contexts))]
    for matrix in matrices:
        product_matrix = mat_mul(product_matrix, matrix)
    return trace(product_matrix)


def verify_case(e: int, m: int) -> str:
    carrier = words(e, m)
    successor = {word: step(word) for word in carrier}

    for word in carrier:
        for t in range(m + 1):
            A.check(iterate(word, t) == direct_iterate(word, t),
                    f"sliding minimum e={e},m={m},t={t},word={word}")
        depth = run_depth(word)
        A.check(iterate(word, depth) == (min(word),) * m,
                f"depth upper e={e},m={m},word={word}")
        if depth:
            A.check(iterate(word, depth - 1) != (min(word),) * m,
                    f"depth sharp e={e},m={m},word={word}")

    depth_histogram = Counter(run_depth(word) for word in carrier)
    for t in range(m):
        actual_cdf = sum(count for depth, count in depth_histogram.items() if depth <= t)
        A.check(actual_cdf == cdf_formula(e, m, t),
                f"depth CDF e={e},m={m},t={t}")
    A.check(depth_histogram[0] == e + 1, f"fixed count e={e},m={m}")
    A.check(max(depth_histogram) == m - 1, f"global height e={e},m={m}")

    fibres = Counter(successor.values())
    for target in carrier:
        criterion = local_minimum_free(target)
        A.check((fibres[target] > 0) == criterion,
                f"image criterion e={e},m={m},target={target}")
        if criterion:
            A.check(step(canonical_source(target)) == target,
                    f"canonical source e={e},m={m},target={target}")
        A.check(fibres[target] == one_step_transfer_fibre(target, e),
                f"one-step transfer e={e},m={m},target={target}")

    # The memory-t transfer is checked on all targets where its matrix remains
    # modest, and on all t for the smallest boxes.
    if (e + 1) ** (m - 1) <= 128:
        current = {word: word for word in carrier}
        for t in range(m):
            t_fibres = Counter(current.values())
            for target in carrier:
                A.check(t_fibres[target] == all_time_transfer_fibre(target, e, t),
                        f"all-time transfer e={e},m={m},t={t},target={target}")
            current = {word: successor[value] for word, value in current.items()}

    return (f"e={e} m={m} states={len(carrier)} image={len(fibres)} "
            f"height={max(depth_histogram)} fixed={depth_histogram[0]} "
            f"depths={dict(sorted(depth_histogram.items()))}")


def verify_two_prime_factorisation() -> str:
    exponent_caps = (1, 2)
    m = 4
    carriers = [words(e, m) for e in exponent_caps]
    states = tuple(product(*carriers))
    successor = {state: tuple(step(component) for component in state) for state in states}
    fibres = Counter(successor.values())
    for target in states:
        expected = 1
        for component, e in zip(target, exponent_caps):
            expected *= one_step_transfer_fibre(component, e)
        A.check(fibres[target] == expected, f"CRT fibre target={target}")
        expected_depth = max(run_depth(component) for component in target)
        current = target
        A.check(expected_depth <= m - 1, f"CRT depth bound target={target}")
        for _ in range(expected_depth):
            current = tuple(step(component) for component in current)
        A.check(all(len(set(component)) == 1 for component in current),
                f"CRT stabilization target={target}")
    fixed = sum(all(len(set(component)) == 1 for component in state) for state in states)
    A.check(fixed == (exponent_caps[0] + 1) * (exponent_caps[1] + 1), "CRT fixed count")
    return f"caps={exponent_caps} m={m} states={len(states)} image={len(fibres)} fixed={fixed}"


def main() -> None:
    print("CYCLIC_NEIGHBOUR_GCD_EXACT_SCOUT")
    for exponent, length in CASES:
        print(verify_case(exponent, length))
    print("two_prime " + verify_two_prime_factorisation())
    print(f"ASSERTIONS {A.assertions}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
