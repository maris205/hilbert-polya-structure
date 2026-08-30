#!/usr/bin/env python3
"""Exact pilot for complementary-divisor tent dynamics.

The carrier for an exponent profile ``a=(a_1,...,a_r)`` is the product
``prod_i {0,...,a_i}``.  It represents divisors of
``N=prod_i p_i**a_i``.  The literal update

    d -> lcm(d,N/d) / gcd(d,N/d)

acts coordinatewise by ``e -> abs(2*e-a)``.  This file is falsification
evidence only; the all-parameter arguments belong in the proof spike.
"""

from __future__ import annotations

from collections import Counter
from functools import reduce
from itertools import product
from math import gcd, lcm


ASSERTIONS = 0


def check(condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message or f"assertion {ASSERTIONS} failed")


def divisors_from_profile(primes: tuple[int, ...], profile: tuple[int, ...]):
    for exponents in product(*(range(a + 1) for a in profile)):
        value = 1
        for p, e in zip(primes, exponents):
            value *= p**e
        yield exponents, value


def exponent_update(e: int, a: int) -> int:
    return abs(2 * e - a)


def state_update(state: tuple[int, ...], profile: tuple[int, ...]):
    return tuple(exponent_update(e, a) for e, a in zip(state, profile))


def literal_update(d: int, n: int) -> int:
    complement = n // d
    return lcm(d, complement) // gcd(d, complement)


def v2(n: int) -> int:
    check(n > 0)
    answer = 0
    while n % 2 == 0:
        answer += 1
        n //= 2
    return answer


def local_orbit_data(e: int, a: int) -> tuple[int, int]:
    """Return literal preperiod and eventual period."""
    seen: dict[int, int] = {}
    x = e
    while x not in seen:
        seen[x] = len(seen)
        x = exponent_update(x, a)
    start = seen[x]
    period = 1
    y = exponent_update(x, a)
    while y != x:
        period += 1
        y = exponent_update(y, a)
    return start, period


def predicted_local_data(e: int, a: int) -> tuple[int, int]:
    y = a - e
    if y == 0:
        return 0, 1
    modulus = 2 * a // gcd(y, 2 * a)
    alpha = v2(modulus)
    odd = modulus >> alpha
    if odd == 1:
        return alpha, 1
    power = 2 % odd
    period = 1
    while power not in (1, odd - 1):
        power = (2 * power) % odd
        period += 1
    return alpha, period


def fixed_count_local(a: int, iterate: int) -> int:
    return (
        gcd((1 << iterate) - 1, 2 * a)
        + gcd((1 << iterate) + 1, 2 * a)
    ) // 2


def cumulative_depth_local(a: int, depth: int) -> int:
    scale = v2(2 * a)
    if depth >= scale:
        return a + 1
    return a // (1 << (scale - depth)) + 1


def iterated_fibre_local(a: int, target: int, iterate: int) -> int:
    """Predicted size of the fibre of f_a^iterate over target."""
    check(iterate >= 1)
    z = a - target
    scale = v2(2 * a)
    kernel = 1 << min(iterate, scale)
    if z % kernel:
        return 0
    if z == 0:
        return (kernel + 2) // 2
    if z == a:
        return kernel // 2
    return kernel


def orbit_data(state: tuple[int, ...], profile: tuple[int, ...]):
    local = [predicted_local_data(e, a) for e, a in zip(state, profile)]
    return max((tail for tail, _ in local), default=0), reduce(
        lcm, (period for _, period in local), 1
    )


def mobius(n: int) -> int:
    result = 1
    p = 2
    remaining = n
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            result = -result
            if remaining % p == 0:
                return 0
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        result = -result
    return result


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


def main() -> None:
    # Literal arithmetic agrees with the exponent tent map.
    profiles = [
        ((2,), (13,)),
        ((2, 3), (7, 5)),
        ((2, 3, 5), (4, 3, 2)),
        ((2, 3, 5), (3, 2, 1)),
    ]
    literal_states = 0
    for primes, profile in profiles:
        n = reduce(lambda x, pa: x * pa[0] ** pa[1], zip(primes, profile), 1)
        lookup = {d: state for state, d in divisors_from_profile(primes, profile)}
        for state, d in divisors_from_profile(primes, profile):
            image = literal_update(d, n)
            check(image in lookup)
            check(lookup[image] == state_update(state, profile))
            literal_states += 1

    # The folding coordinate y=a-e is the quotient of doubling modulo 2a.
    local_states = 0
    for a in range(1, 129):
        for e in range(a + 1):
            y = a - e
            folded_double = min((2 * y) % (2 * a), (-2 * y) % (2 * a))
            check(a - exponent_update(e, a) == folded_double)
            check(local_orbit_data(e, a) == predicted_local_data(e, a))
            local_states += 1

        for iterate in range(1, 19):
            literal_fixed = 0
            for e in range(a + 1):
                x = e
                for _ in range(iterate):
                    x = exponent_update(x, a)
                literal_fixed += x == e
            check(literal_fixed == fixed_count_local(a, iterate))

        depths = Counter(local_orbit_data(e, a)[0] for e in range(a + 1))
        for depth in range(v2(2 * a) + 1):
            literal_cumulative = sum(count for t, count in depths.items() if t <= depth)
            check(literal_cumulative == cumulative_depth_local(a, depth))
        check(max(depths) == v2(2 * a))

        for iterate in range(1, v2(2 * a) + 4):
            fibres = Counter()
            for e in range(a + 1):
                x = e
                for _ in range(iterate):
                    x = exponent_update(x, a)
                fibres[x] += 1
            for target in range(a + 1):
                check(fibres[target] == iterated_fibre_local(a, target, iterate))
            check(sum(fibres.values()) == a + 1)

    # Product formulas: pointwise max/lcm, fixed products, and depth products.
    product_profiles = []
    for rank in (1, 2, 3):
        for profile in product(range(1, 7), repeat=rank):
            if reduce(lambda x, y: x * (y + 1), profile, 1) <= 180:
                product_profiles.append(profile)

    product_states = 0
    for profile in product_profiles:
        states = list(product(*(range(a + 1) for a in profile)))
        for state in states:
            seen: dict[tuple[int, ...], int] = {}
            x = state
            while x not in seen:
                seen[x] = len(seen)
                x = state_update(x, profile)
            literal_tail = seen[x]
            literal_period = 1
            y = state_update(x, profile)
            while y != x:
                literal_period += 1
                y = state_update(y, profile)
            check((literal_tail, literal_period) == orbit_data(state, profile))
            product_states += 1

        for iterate in range(1, 11):
            literal_fixed = 0
            for state in states:
                x = state
                for _ in range(iterate):
                    x = state_update(x, profile)
                literal_fixed += x == state
            predicted = reduce(
                lambda x, y: x * y,
                (fixed_count_local(a, iterate) for a in profile),
                1,
            )
            check(literal_fixed == predicted)

        maximum = max(v2(2 * a) for a in profile)
        for depth in range(maximum + 1):
            literal = sum(orbit_data(state, profile)[0] <= depth for state in states)
            predicted = reduce(
                lambda x, y: x * y,
                (cumulative_depth_local(a, depth) for a in profile),
                1,
            )
            check(literal == predicted)

        # Exact-period counts obtained from fixed counts are nonnegative and
        # reconstruct every recurrent state.
        fixed = {
            n: reduce(
                lambda x, y: x * y,
                (fixed_count_local(a, n) for a in profile),
                1,
            )
            for n in range(1, 25)
        }
        exact = {}
        for n in range(1, 25):
            exact[n] = sum(mobius(n // d) * fixed[d] for d in divisors(n))
            check(exact[n] >= 0)
            check(exact[n] % n == 0)
            check(sum(exact[d] for d in divisors(n)) == fixed[n])

    # Falsification sentinels: neither universal absorption nor an unsigned
    # order formula survives.
    check(local_orbit_data(1, 5) == (0, 2))
    check(local_orbit_data(1, 7) == (0, 3))
    check(local_orbit_data(1, 3) == (0, 1))
    check(predicted_local_data(1, 5)[1] < 4)  # order_5(2)=4, sign quotient=2.

    print("complementary-divisor tent pilot: PASS")
    print(f"literal_states={literal_states}")
    print(f"local_states={local_states}")
    print(f"product_profiles={len(product_profiles)}")
    print(f"product_states={product_states}")
    print(f"assertions={ASSERTIONS}")
    print("sentinel_a5_e1=tail0_period2")
    print("sentinel_a7_e1=tail0_period3")


if __name__ == "__main__":
    main()
