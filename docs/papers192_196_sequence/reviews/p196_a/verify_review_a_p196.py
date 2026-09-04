#!/usr/bin/env python3
"""Process-separated exact control for P196 Review A.

This file uses only the Python standard library.  It neither imports nor
executes the author verifier.  Forward states are tuples, characteristic
polynomials are obtained from a Leibniz determinant expansion, and gap
factors are first checked against direct weak-chain enumeration.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import permutations, product
from math import comb, gcd


ASSERTIONS = 0
TRANSITIONS = 0
TARGETS = 0
GAP_CHECKS = 0
FIXED_ITERATE_CHECKS = 0
CHARPOLY_CHECKS = 0


def check(condition: bool, message: object) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def godel(a: int, b: int, top: int) -> int:
    return top if a <= b else b


def update(word: tuple[int, ...], q: int) -> tuple[int, ...]:
    top = q - 1
    m = len(word)
    return tuple(godel(word[i], word[(i + 1) % m], top) for i in range(m))


def shift(word: tuple[int, ...]) -> tuple[int, ...]:
    return word[1:] + word[:1]


def in_core(word: tuple[int, ...], q: int) -> bool:
    top = q - 1
    m = len(word)
    return all(word[(i + 1) % m] == top or word[i] > word[(i + 1) % m]
               for i in range(m))


def gap_formula(top: int, a: int, b: int, distance: int) -> int:
    total = comb(top - a + distance - 1, distance - 1)
    forbidden = comb(b - a + distance - 1, distance - 1) if b >= a else 0
    return total - forbidden


def gap_bruteforce(top: int, a: int, b: int, distance: int) -> int:
    if distance == 1:
        return int(a > b)
    count = 0
    for middle in product(range(a, top + 1), repeat=distance - 1):
        chain = (a,) + middle
        if all(chain[i] <= chain[i + 1] for i in range(len(chain) - 1)) and chain[-1] > b:
            count += 1
    return count


def predicted_fibre(target: tuple[int, ...], q: int) -> int:
    if not in_core(target, q):
        return 0
    top = q - 1
    if all(value == top for value in target):
        return q
    sites = [i for i, value in enumerate(target) if value < top]
    result = 1
    for j, site in enumerate(sites):
        next_site = sites[(j + 1) % len(sites)]
        distance = (next_site - site) % len(target)
        if distance == 0:
            distance = len(target)
        result *= gap_formula(top, target[site], target[next_site], distance)
    return result


def adjacency(q: int) -> list[list[int]]:
    top = q - 1
    return [[int(b == top or a > b) for b in range(q)] for a in range(q)]


def matrix_multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    n = len(left)
    return [[sum(left[i][h] * right[h][j] for h in range(n))
             for j in range(n)] for i in range(n)]


def matrix_power(matrix: list[list[int]], exponent: int) -> list[list[int]]:
    n = len(matrix)
    result = [[int(i == j) for j in range(n)] for i in range(n)]
    base = matrix
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        exponent //= 2
    return result


def trace_power(matrix: list[list[int]], exponent: int) -> int:
    powered = matrix_power(matrix, exponent)
    return sum(powered[i][i] for i in range(len(matrix)))


def poly_add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(perm[i] > perm[j] for i in range(len(perm))
                     for j in range(i + 1, len(perm)))
    return -1 if inversions % 2 else 1


def characteristic_by_leibniz(matrix: list[list[int]]) -> list[int]:
    """Low-to-high coefficients of det(lambda I-A), without row operations."""
    n = len(matrix)
    determinant = [0]
    for perm in permutations(range(n)):
        term = [permutation_sign(perm)]
        for row, column in enumerate(perm):
            if row == column:
                entry = [-matrix[row][column], 1]
            else:
                entry = [-matrix[row][column]]
            term = poly_multiply(term, entry)
        determinant = poly_add(determinant, term)
    determinant += [0] * (n + 1 - len(determinant))
    return determinant


def expected_characteristic(q: int) -> list[int]:
    return [-comb(q - 1, degree) for degree in range(q)] + [1]


def divisors(number: int) -> list[int]:
    return [d for d in range(1, number + 1) if number % d == 0]


def mobius(number: int) -> int:
    primes = 0
    remaining = number
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            remaining //= factor
            primes += 1
            if remaining % factor == 0:
                return 0
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        primes += 1
    return -1 if primes % 2 else 1


def least_shift_period(word: tuple[int, ...]) -> int:
    m = len(word)
    for period in divisors(m):
        if all(word[i] == word[(i + period) % m] for i in range(m)):
            return period
    raise AssertionError("period search failed")


def iterate(transition: dict[tuple[int, ...], tuple[int, ...]],
            state: tuple[int, ...], steps: int) -> tuple[int, ...]:
    current = state
    for _ in range(steps):
        current = transition[current]
    return current


def verify_gap_table(digest) -> None:
    global GAP_CHECKS
    for q in range(2, 8):
        top = q - 1
        for a in range(top):
            for b in range(top):
                for distance in range(1, 8):
                    direct = gap_bruteforce(top, a, b, distance)
                    closed = gap_formula(top, a, b, distance)
                    check(direct == closed, ("gap", q, a, b, distance, direct, closed))
                    if distance == 1:
                        check(closed == int(a > b), ("gap-d1", q, a, b))
                    digest.update(f"G|{q}|{a}|{b}|{distance}|{direct}\n".encode())
                    GAP_CHECKS += 1


def verify_characteristic(digest) -> None:
    global CHARPOLY_CHECKS
    for q in range(2, 9):
        matrix = adjacency(q)
        observed = characteristic_by_leibniz(matrix)
        expected = expected_characteristic(q)
        check(observed == expected, ("charpoly", q, observed, expected))
        traces = [trace_power(matrix, exponent) for exponent in range(3 * q + 1)]
        for exponent in range(q, 3 * q + 1):
            recurrence = sum(comb(q - 1, h) * traces[exponent - q + h]
                             for h in range(q))
            check(traces[exponent] == recurrence,
                  ("trace-recurrence", q, exponent, traces[exponent], recurrence))
        digest.update(f"C|{q}|{tuple(observed)}|{tuple(traces)}\n".encode())
        CHARPOLY_CHECKS += 1


def verify_box(q: int, m: int, digest) -> tuple[int, int, int, int, tuple[int, ...]]:
    global TRANSITIONS, TARGETS, FIXED_ITERATE_CHECKS
    states = [tuple(word) for word in product(range(q), repeat=m)]
    transition = {state: update(state, q) for state in states}
    fibres: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for source in states:
        target = transition[source]
        fibres[target].append(source)
        TRANSITIONS += 1
        check(in_core(target, q), ("image-subset", q, m, source, target))
        if in_core(source, q):
            check(target == shift(source), ("rotation", q, m, source, target))
        else:
            check(target != source, ("outside-fixed", q, m, source))
        digest.update(f"T|{q}|{m}|{source}|{target}\n".encode())

    actual_image = set(fibres)
    predicted_image = {state for state in states if in_core(state, q)}
    check(actual_image == predicted_image, ("image-equality", q, m))
    check(all(update(shift(state), q) == shift(shift(state)) for state in predicted_image),
          ("core-shift-invariance", q, m))

    fixed = [state for state in states if transition[state] == state]
    top_word = (q - 1,) * m
    check(fixed == [top_word], ("unique-fixed", q, m, fixed))
    if m == 1:
        check(predicted_image == {top_word}, ("m1-image", q))
        check(len(fibres[top_word]) == q, ("m1-fibre", q))

    max_fibre = 0
    for target in states:
        actual = len(fibres.get(target, []))
        predicted = predicted_fibre(target, q)
        check(actual == predicted, ("fibre", q, m, target, actual, predicted))
        max_fibre = max(max_fibre, actual)
        TARGETS += 1
        digest.update(f"F|{q}|{m}|{target}|{actual}\n".encode())
    check(sum(len(sources) for sources in fibres.values()) == q ** m,
          ("mass", q, m))

    matrix = adjacency(q)
    for steps in range(1, 2 * m + 1):
        direct = sum(iterate(transition, state, steps) == state for state in states)
        spectral = trace_power(matrix, gcd(m, steps))
        check(direct == spectral, ("iterate-fixed", q, m, steps, direct, spectral))
        FIXED_ITERATE_CHECKS += 1

    direct_periods = Counter(least_shift_period(state) for state in predicted_image)
    for period in divisors(m):
        primitive = sum(mobius(period // e) * trace_power(matrix, e)
                        for e in divisors(period))
        check(direct_periods[period] == primitive,
              ("period-points", q, m, period, direct_periods[period], primitive))
        check(primitive % period == 0, ("cycle-integrality", q, m, period))

    summary = (len(states), len(actual_image), len(fixed), max_fibre,
               tuple(sorted(direct_periods)))
    digest.update(f"B|{q}|{m}|{summary}\n".encode())
    return summary


def main() -> None:
    digest = sha256()
    verify_gap_table(digest)
    verify_characteristic(digest)
    boxes = []
    total_states = 0
    total_core = 0
    for q in range(2, 6):
        for m in range(1, 8):
            summary = verify_box(q, m, digest)
            boxes.append((q, m, summary))
            total_states += summary[0]
            total_core += summary[1]

    last_q, last_m, last = boxes[-1]
    print("P196_HOSTILE_REVIEW_A_EXACT_CONTROL")
    print("REPRESENTATION=tuple_words_direct_gap_chains_leibniz_determinant")
    print("AUTHOR_CODE_IMPORTED=false")
    print("BOXES=q2..5_m1..7")
    print(f"BOX_COUNT={len(boxes)}")
    print(f"STATES={total_states}")
    print(f"CORE_STATES={total_core}")
    print(f"TRANSITIONS={TRANSITIONS}")
    print(f"TARGETS={TARGETS}")
    print(f"GAP_CHECKS={GAP_CHECKS}")
    print(f"FIXED_ITERATE_CHECKS={FIXED_ITERATE_CHECKS}")
    print(f"CHARPOLY_CHECKS={CHARPOLY_CHECKS}")
    print(f"LAST_BOX=q{last_q}_m{last_m}_states{last[0]}_core{last[1]}_fixed{last[2]}_maxfibre{last[3]}_periods{','.join(map(str,last[4]))}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print(f"CONTROL_DIGEST={digest.hexdigest()}")
    print("CRITICAL_FINDINGS=0")
    print("MAJOR_FINDINGS=0")
    print("MINOR_FINDINGS=0")
    print("VERDICT=PROVABLE_AS_STATED")
    print("OWNER_GATE=OWNER_AMBER")
    print("EXTERNAL_STATE=HOLD_EXTERNAL")
    print("FINITE_CONTROL_IS_NOT_PROOF_OR_NOVELTY=true")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
