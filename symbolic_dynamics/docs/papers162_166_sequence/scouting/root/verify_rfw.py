#!/usr/bin/env python3
"""Exact scout for the reciprocal Fibonacci window.

For an odd prime p, totalize inversion by inv0(0)=0 and iterate

    H_p(x,y) = (y, x*y*inv0(x+y)).

The program exhausts every state for the declared primes.  It checks the
projective Fibonacci classification, the complete temporal histogram, every
one-step fibre, every t-step fibre through saturation, and the recurrent
cycle inventory obtained from fixed-point/Mobius inversion.  It is a finite
falsifier and consistency certificate, not a substitute for proof.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from math import isqrt


PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(f"{label} [assertion {self.assertions}]")


A = Audit()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def inv0(x: int, p: int) -> int:
    return 0 if x % p == 0 else pow(x, p - 2, p)


def step(state: tuple[int, int], p: int) -> tuple[int, int]:
    x, y = state
    return y, x * y * inv0(x + y, p) % p


def iterate(state: tuple[int, int], t: int, p: int) -> tuple[int, int]:
    for _ in range(t):
        state = step(state, p)
    return state


def fib_rank(p: int) -> int:
    previous, current = 0, 1
    for index in range(1, 2 * p + 3):
        previous, current = current, (previous + current) % p
        if previous == 0:
            return index
    raise AssertionError(f"rank search bound failed for p={p}")


def mat_mul(left, right, p: int):
    return (
        ((left[0] * right[0] + left[1] * right[2]) % p,
         (left[0] * right[1] + left[1] * right[3]) % p,
         (left[2] * right[0] + left[3] * right[2]) % p,
         (left[2] * right[1] + left[3] * right[3]) % p)
    )


def mat_pow(matrix, exponent: int, p: int):
    answer = (1, 0, 0, 1)
    while exponent:
        if exponent & 1:
            answer = mat_mul(answer, matrix, p)
        matrix = mat_mul(matrix, matrix, p)
        exponent //= 2
    return answer


def mat_vec(matrix, vector, p: int):
    return ((matrix[0] * vector[0] + matrix[1] * vector[1]) % p,
            (matrix[2] * vector[0] + matrix[3] * vector[1]) % p)


def matrix_order(matrix, p: int) -> int:
    power = (1, 0, 0, 1)
    for exponent in range(1, 6 * (p * p - 1) + 1):
        power = mat_mul(power, matrix, p)
        if power == (1, 0, 0, 1):
            return exponent
    raise AssertionError(f"matrix order bound failed for p={p}")


def projective(vector: tuple[int, int], p: int) -> tuple[int, int]:
    u, v = vector
    if u:
        return 1, v * inv0(u, p) % p
    return 0, 1


def bad_orbit(p: int, z: int) -> tuple[tuple[int, int], ...]:
    matrix = (0, 1, 1, 1)
    vector = (1, 0)
    orbit = []
    for _ in range(z):
        orbit.append(projective(vector, p))
        vector = mat_vec(matrix, vector, p)
    return tuple(orbit)


def predicted_depth(state: tuple[int, int], p: int, orbit) -> int:
    x, y = state
    if state == (0, 0):
        return 0
    if y == 0:
        return 1
    if x == 0:
        return 2
    line = projective((inv0(x, p), inv0(y, p)), p)
    if line not in orbit:
        return 0
    index = orbit.index(line)
    A.check(index >= 2, f"torus state on coordinate line p={p}, state={state}")
    return len(orbit) + 1 - index


def actual_depths(states, successor):
    depth = {}
    recurrent = set()
    for start in states:
        if start in depth:
            continue
        path = []
        where = {}
        cursor = start
        while cursor not in depth and cursor not in where:
            where[cursor] = len(path)
            path.append(cursor)
            cursor = successor[cursor]
        if cursor in where:
            cut = where[cursor]
            cycle = path[cut:]
            for point in cycle:
                depth[point] = 0
                recurrent.add(point)
            tail = path[:cut]
        else:
            tail = path
        for point in reversed(tail):
            depth[point] = depth[successor[point]] + 1
    return depth, recurrent


def nullity_two(matrix, p: int) -> int:
    a, b, c, d = matrix
    if (a, b, c, d) == (0, 0, 0, 0):
        return 2
    return 1 if (a * d - b * c) % p == 0 else 0


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    primes = 0
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            primes += 1
            if n % divisor == 0:
                return 0
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    if n > 1:
        primes += 1
    return -1 if primes % 2 else 1


def predicted_one_fibre(target: tuple[int, int], p: int) -> int:
    a, b = target
    if a == 0:
        return p if b == 0 else 0
    if b == 0:
        return 2
    return 0 if a == b else 1


def predicted_sink_fibre(t: int, p: int, z: int) -> int:
    if t == 0:
        return 1
    if t == 1:
        return p
    return 1 + min(t + 1, z) * (p - 1)


def predicted_all_time_fibre(target, t: int, p: int, z: int, orbit) -> int:
    if t == 0:
        return 1
    if target == (0, 0):
        return predicted_sink_fibre(t, p, z)
    depth = predicted_depth(target, p, orbit)
    if depth == 0:
        return 1
    x, y = target
    if x == 0:
        return 0
    if y == 0:
        if t == 1:
            return 2
        return int(2 <= t <= z - 2)
    return int(t <= z - 1 - depth)


def verify_prime(p: int) -> str:
    A.check(is_prime(p) and p % 2 == 1, f"declared odd prime p={p}")
    states = tuple((x, y) for x in range(p) for y in range(p))
    successor = {state: step(state, p) for state in states}
    z = fib_rank(p)
    orbit = bad_orbit(p, z)
    A.check(len(set(orbit)) == z, f"projective rank orbit p={p}")
    A.check(orbit[0] == (1, 0) and orbit[1] == (0, 1), f"axis order p={p}")
    A.check(mat_pow((0, 1, 1, 1), z, p)[1:3] == (0, 0), f"scalar return p={p}")

    depths, recurrent = actual_depths(states, successor)
    for state in states:
        A.check(depths[state] == predicted_depth(state, p, orbit),
                f"depth classification p={p}, state={state}")
    expected_histogram = Counter({0: p * p - z * (p - 1), 1: p - 1})
    expected_histogram[2] += 2 * (p - 1)
    for depth in range(3, z):
        expected_histogram[depth] += p - 1
    A.check(Counter(depths.values()) == expected_histogram, f"depth histogram p={p}")
    A.check(max(depths.values()) == z - 1, f"sharp height p={p}")

    one_fibres = Counter(successor.values())
    for target in states:
        A.check(one_fibres[target] == predicted_one_fibre(target, p),
                f"one-step fibre p={p}, target={target}")
    A.check(len(one_fibres) == p * p - 2 * p + 2, f"one-step image p={p}")

    current = {state: state for state in states}
    for t in range(0, z + 2):
        fibres = Counter(current.values())
        for target in states:
            A.check(fibres[target] == predicted_all_time_fibre(target, t, p, z, orbit),
                    f"all-time fibre p={p}, t={t}, target={target}")
        current = {state: successor[value] for state, value in current.items()}

    matrix = (0, 1, 1, 1)
    order = matrix_order(matrix, p)
    cycle_histogram = Counter()
    unseen = set(recurrent)
    while unseen:
        start = next(iter(unseen))
        cycle = []
        cursor = start
        while cursor not in cycle:
            cycle.append(cursor)
            cursor = successor[cursor]
        A.check(cursor == start, f"recurrent component is cycle p={p}")
        for point in cycle:
            unseen.remove(point)
        cycle_histogram[len(cycle)] += 1

    for k in range(1, order + 1):
        power = mat_pow(matrix, k, p)
        difference = ((power[0] - 1) % p, power[1], power[2], (power[3] - 1) % p)
        fixed_formula = p ** nullity_two(difference, p)
        if power == (1, 0, 0, 1):
            fixed_formula -= z * (p - 1)
        fixed_actual = sum(iterate(state, k, p) == state for state in states)
        A.check(fixed_actual == fixed_formula, f"fixed formula p={p}, k={k}")
        exact_points = sum(mobius(k // d) * (
            p ** nullity_two((
                (mat_pow(matrix, d, p)[0] - 1) % p,
                mat_pow(matrix, d, p)[1],
                mat_pow(matrix, d, p)[2],
                (mat_pow(matrix, d, p)[3] - 1) % p,
            ), p)
            - (z * (p - 1) if mat_pow(matrix, d, p) == (1, 0, 0, 1) else 0)
        ) for d in divisors(k))
        A.check(exact_points % k == 0, f"Mobius divisibility p={p}, k={k}")
        A.check(exact_points // k == cycle_histogram[k], f"cycle formula p={p}, k={k}")

    return (
        f"p={p} z={z} matrix_order={order} recurrent={len(recurrent)} "
        f"max_depth={max(depths.values())} image={len(one_fibres)} "
        f"cycles={dict(sorted(cycle_histogram.items()))}"
    )


def main() -> None:
    print("RECIPROCAL_FIBONACCI_WINDOW_EXACT_SCOUT")
    for prime in PRIMES:
        print(verify_prime(prime))
    print(f"ASSERTIONS {A.assertions}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
