#!/usr/bin/env python3
"""Exact controls for involutive norm dynamics on split cyclic group algebras.

The literal lanes use only Python integers.  Prime fields use modular
arithmetic; GF(4) and GF(16) use explicit polynomial-basis arithmetic.  Every
functional graph is built from cyclic coefficient convolution and reversal,
independently of the formulas being tested.
"""

from collections import Counter
from itertools import product
from math import gcd


CHECKS = 0


def check(condition, message):
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    if n == 1:
        return 1
    value = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
            value = -value
            if n % d == 0:
                return 0
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        value = -value
    return value


def valuation_two(n):
    value = 0
    while n % 2 == 0:
        value += 1
        n //= 2
    return value, n


def multiplicative_order_two(m):
    if m == 1:
        return 1
    value = 2 % m
    order = 1
    while value != 1:
        value = (2 * value) % m
        order += 1
        check(order <= m, f"order search failed for m={m}")
    return order


def primitive_root_prime(p):
    factors = []
    residue = p - 1
    d = 2
    while d * d <= residue:
        if residue % d == 0:
            factors.append(d)
            while residue % d == 0:
                residue //= d
        d += 1
    if residue > 1:
        factors.append(residue)
    for candidate in range(1, p):
        if all(pow(candidate, (p - 1) // ell, p) != 1 for ell in factors):
            return candidate
    raise AssertionError(f"no primitive root modulo {p}")


class PrimeField:
    def __init__(self, p):
        self.q = p
        self.name = f"F_{p}"

    def add(self, x, y):
        return (x + y) % self.q

    def mul(self, x, y):
        return (x * y) % self.q

    def power(self, x, exponent):
        return pow(x, exponent, self.q)

    def primitive(self):
        return primitive_root_prime(self.q)


class BinaryField:
    def __init__(self, degree, modulus):
        self.degree = degree
        self.modulus = modulus
        self.q = 1 << degree
        self.name = f"F_{self.q}"

    def add(self, x, y):
        return x ^ y

    def mul(self, x, y):
        out = 0
        a = x
        b = y
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a & self.q:
                a ^= self.modulus
        return out

    def power(self, x, exponent):
        out = 1
        base = x
        while exponent:
            if exponent & 1:
                out = self.mul(out, base)
            base = self.mul(base, base)
            exponent //= 2
        return out

    def primitive(self):
        for candidate in range(2, self.q):
            if all(self.power(candidate, k) != 1 for k in range(1, self.q - 1)):
                return candidate
        raise AssertionError(f"no primitive element in {self.name}")


def star(a):
    n = len(a)
    return tuple(a[(-j) % n] for j in range(n))


def convolution(a, b, field):
    n = len(a)
    out = [0] * n
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            index = (i + j) % n
            out[index] = field.add(out[index], field.mul(x, y))
    return tuple(out)


def norm_map(a, field):
    return convolution(a, star(a), field)


def algebra_power(a, exponent, field):
    identity = (1,) + (0,) * (len(a) - 1)
    out = identity
    base = a
    while exponent:
        if exponent & 1:
            out = convolution(out, base, field)
        base = convolution(base, base, field)
        exponent //= 2
    return out


def dft(a, omega, field):
    n = len(a)
    transformed = []
    for j in range(n):
        value = 0
        for r, coefficient in enumerate(a):
            term = field.mul(coefficient, field.power(omega, j * r))
            value = field.add(value, term)
        transformed.append(value)
    return tuple(transformed)


def fixed_formula(q, n, k):
    orbit_count = (n + gcd(n, 2)) // 2
    return (1 + gcd((1 << k) - 1, q - 1)) ** orbit_count


def functional_graph(states, image):
    visited = set()
    cycles = []
    for initial in states:
        if initial in visited:
            continue
        path = []
        position = {}
        current = initial
        while current not in visited and current not in position:
            position[current] = len(path)
            path.append(current)
            current = image[current]
        if current in position:
            cycles.append(tuple(path[position[current] :]))
        visited.update(path)
    recurrent = {state for cycle in cycles for state in cycle}
    depths = {}
    for state in states:
        current = state
        depth = 0
        while current not in recurrent:
            current = image[current]
            depth += 1
            check(depth <= len(states), "functional graph walk did not terminate")
        depths[state] = depth
    return cycles, recurrent, depths


def recurrent_fourier_test(state, n, m, omega, field):
    values = dft(state, omega, field)
    for j, value in enumerate(values):
        if values[(-j) % n] != value:
            return False
        if value != 0 and field.power(value, m) != 1:
            return False
    return True


def run_literal_lane(field, n):
    q = field.q
    check((q - 1) % n == 0, f"non-split lane {field.name}, n={n}")
    generator = field.primitive()
    check(field.power(generator, q - 1) == 1, "primitive element exponent")
    check(
        all(field.power(generator, k) != 1 for k in range(1, q - 1)),
        "primitive element proper order",
    )
    omega = field.power(generator, (q - 1) // n)
    check(field.power(omega, n) == 1, "Fourier root exponent")
    check(
        all(field.power(omega, k) != 1 for k in range(1, n)),
        "Fourier root proper order",
    )

    states = list(product(range(q), repeat=n))
    image = {}
    for state in states:
        transformed = dft(state, omega, field)
        reversed_transformed = dft(star(state), omega, field)
        expected_reversal = tuple(transformed[(-j) % n] for j in range(n))
        check(reversed_transformed == expected_reversal, "Fourier reversal rule")

        target = norm_map(state, field)
        image[state] = target
        target_transformed = dft(target, omega, field)
        expected_target = tuple(
            field.mul(transformed[j], transformed[(-j) % n]) for j in range(n)
        )
        check(target_transformed == expected_target, "Fourier norm product rule")
        check(star(target) == target, "one-step symmetric collapse")

        current = state
        first_norm = target
        for k in range(1, 6):
            current = image[current] if current in image else norm_map(current, field)
            coefficient_formula = algebra_power(first_norm, 1 << (k - 1), field)
            check(current == coefficient_formula, f"coefficient iterate k={k}")
            transformed_current = dft(current, omega, field)
            fourier_formula = tuple(
                field.power(
                    field.mul(transformed[j], transformed[(-j) % n]),
                    1 << (k - 1),
                )
                for j in range(n)
            )
            check(transformed_current == fourier_formula, f"Fourier iterate k={k}")

    cycles, recurrent, depths = functional_graph(states, image)
    alpha, m = valuation_two(q - 1)
    orbit_count = (n + gcd(n, 2)) // 2
    expected_recurrent = (m + 1) ** orbit_count
    check(len(recurrent) == expected_recurrent, "recurrent-core cardinality")
    for state in states:
        predicted = recurrent_fourier_test(state, n, m, omega, field)
        check((state in recurrent) == predicted, "recurrent-core membership")

    expected_depth = alpha + int(n > gcd(n, 2))
    check(max(depths.values()) == expected_depth, "sharp maximum transient depth")

    fixed = []
    for k in range(1, 13):
        brute = 0
        for state in states:
            current = state
            for _ in range(k):
                current = image[current]
            brute += int(current == state)
        formula = fixed_formula(q, n, k)
        check(brute == formula, f"fixed formula at k={k}")
        fixed.append(brute)

    cycle_inventory = Counter(len(cycle) for cycle in cycles)
    ell = multiplicative_order_two(m)
    for k in range(1, ell + 1):
        least_period_points = sum(
            mobius(k // d) * fixed_formula(q, n, d) for d in divisors(k)
        )
        check(least_period_points % k == 0, "Möbius divisibility")
        expected_cycles = least_period_points // k
        check(cycle_inventory.get(k, 0) == expected_cycles, "cycle inventory")
        if ell % k != 0:
            check(expected_cycles == 0, "period support divides order")
    check(
        all(length > 0 and ell % length == 0 for length in cycle_inventory),
        "all cycle lengths divide the squaring order",
    )
    check(
        sum(length * count for length, count in cycle_inventory.items())
        == len(recurrent),
        "cycle ledger accounts for recurrent core",
    )

    return {
        "q": q,
        "n": n,
        "phase": len(states),
        "fixed": fixed[:8],
        "recurrent": len(recurrent),
        "depth": max(depths.values()),
        "cycles": dict(sorted(cycle_inventory.items())),
    }


def exact_nth_root(value, exponent):
    low, high = 0, value + 1
    while high - low > 1:
        middle = (low + high) // 2
        if middle**exponent <= value:
            low = middle
        else:
            high = middle
    check(low**exponent == value, "expected a perfect power")
    return low


def is_prime_power(value):
    if value < 2:
        return False
    for p in range(2, value + 1):
        if any(p % d == 0 for d in range(2, int(p**0.5) + 1)):
            continue
        residue = value
        while residue % p == 0:
            residue //= p
        if residue == 1:
            return True
    return False


def recover_pair(phase_size, fixed_values, max_depth):
    first = fixed_values[0]
    orbit_count = first.bit_length() - 1
    check(1 << orbit_count == first, "F_1 is a power of two")
    roots = [exact_nth_root(value, orbit_count) for value in fixed_values]
    m = max(roots) - 1
    candidate_lengths = [2 * orbit_count - 1]
    if orbit_count >= 2:
        candidate_lengths.append(2 * orbit_count - 2)
    survivors = []
    for n in candidate_lengths:
        epsilon = int(n > gcd(n, 2))
        exponent = max_depth - epsilon
        if exponent < 0:
            continue
        q = (1 << exponent) * m + 1
        if (
            q**n == phase_size
            and is_prime_power(q)
            and (q - 1) % n == 0
        ):
            survivors.append((q, n))
    check(len(survivors) == 1, f"rigidity survivor count: {survivors}")
    return survivors[0]


def run_rigidity_lanes():
    prime_powers = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 49]
    lanes = 0
    for q in prime_powers:
        alpha, m = valuation_two(q - 1)
        ell = multiplicative_order_two(m)
        for n in divisors(q - 1):
            orbit_count = (n + gcd(n, 2)) // 2
            depth = alpha + int(n > gcd(n, 2))
            fixed_values = [fixed_formula(q, n, k) for k in range(1, ell + 1)]
            recovered = recover_pair(q**n, fixed_values, depth)
            check(recovered == (q, n), f"rigidity failed for {(q, n)}")
            lanes += 1
    return lanes


def main():
    prime_lanes = [
        (PrimeField(3), 1),
        (PrimeField(3), 2),
        (PrimeField(5), 2),
        (PrimeField(5), 4),
        (PrimeField(7), 3),
        (PrimeField(11), 2),
        (PrimeField(13), 3),
    ]
    extension_lanes = [
        (BinaryField(2, 0b111), 3),       # x^2 + x + 1
        (BinaryField(4, 0b10011), 3),     # x^4 + x + 1
    ]

    rows = []
    for field, n in prime_lanes + extension_lanes:
        rows.append(run_literal_lane(field, n))
    rigidity_lanes = run_rigidity_lanes()

    print("cyclic group-algebra involution norm verification: PASS")
    print(f"literal_lanes={len(rows)}")
    print(f"rigidity_lanes={rigidity_lanes}")
    print(f"assertions={CHECKS}")
    for row in rows:
        print(
            "lane"
            f" q={row['q']} n={row['n']} phase={row['phase']}"
            f" fixed_1_8={row['fixed']}"
            f" recurrent={row['recurrent']} depth={row['depth']}"
            f" cycles={row['cycles']}"
        )


if __name__ == "__main__":
    main()
