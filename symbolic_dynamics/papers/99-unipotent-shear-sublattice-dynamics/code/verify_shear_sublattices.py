#!/usr/bin/env python3
"""Exact controls for unipotent shear on index-N sublattices of Z^2.

The program uses only the Python standard library.  It independently
constructs HNF states, canonicalizes the sheared bases, enumerates cycles,
counts fixed states, performs Mobius inversion, and checks the prime-power
valuation formulas.  Every assertion is exact integer arithmetic.
"""

from __future__ import annotations

from collections import Counter
from math import gcd, isqrt


CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def divisors(n: int) -> list[int]:
    low: list[int] = []
    high: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            low.append(d)
            if d * d != n:
                high.append(n // d)
    return low + high[::-1]


def hnf_states(n: int) -> list[tuple[int, int, int]]:
    return [(a, b, n // a) for a in divisors(n) for b in range(a)]


def sigma1(n: int) -> int:
    return sum(divisors(n))


def canonicalize_upper_basis(a: int, d: int, c: int) -> tuple[int, int, int]:
    """Canonical HNF for columns (a,0),(d,c), with a,c positive."""
    return (a, d % a, c)


def shear_via_basis(state: tuple[int, int, int]) -> tuple[int, int, int]:
    a, b, c = state
    # U(a,0)=(a,0) and U(b,c)=(b+c,c), followed by HNF reduction.
    return canonicalize_upper_basis(a, b + c, c)


def closed_action(state: tuple[int, int, int]) -> tuple[int, int, int]:
    a, b, c = state
    return (a, (b + c) % a, c)


def in_upper_lattice(
    vector: tuple[int, int], basis: tuple[int, int, int]
) -> bool:
    """Membership in span_Z{(a,0),(d,c)} without canonicality assumptions."""
    x, y = vector
    a, d, c = basis
    if y % c:
        return False
    k = y // c
    return (x - k * d) % a == 0


def same_upper_lattice(
    first: tuple[int, int, int], second: tuple[int, int, int]
) -> bool:
    a1, d1, c1 = first
    a2, d2, c2 = second
    first_generators = ((a1, 0), (d1, c1))
    second_generators = ((a2, 0), (d2, c2))
    return all(in_upper_lattice(v, second) for v in first_generators) and all(
        in_upper_lattice(v, first) for v in second_generators
    )


def formula_cycle_inventory(n: int) -> Counter[int]:
    answer: Counter[int] = Counter()
    for a in divisors(n):
        c = n // a
        g = gcd(a, c)
        answer[a // g] += g
    return answer


def direct_cycle_inventory(n: int) -> Counter[int]:
    states = set(hnf_states(n))
    unseen = set(states)
    answer: Counter[int] = Counter()
    while unseen:
        start = min(unseen)
        current = start
        orbit: list[tuple[int, int, int]] = []
        while current not in orbit:
            check(current in states, f"action left phase at N={n}, state={current}")
            orbit.append(current)
            current = shear_via_basis(current)
        check(current == start, f"non-cycle encountered at N={n}, start={start}")
        for state in orbit:
            unseen.remove(state)
        answer[len(orbit)] += 1
    return answer


def direct_fixed_count(n: int, time: int) -> int:
    count = 0
    for a, b, c in hnf_states(n):
        # Direct phase-space test for the time-th translated residue; this
        # enumerates b and does not use the layer divisibility count below.
        count += (b + time * c) % a == b
    return count


def formula_fixed_count(n: int, time: int) -> int:
    return sum(a for a in divisors(n) if (time * (n // a)) % a == 0)


def mobius(n: int) -> int:
    remaining = n
    prime_count = 0
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            if remaining % p == 0:
                return 0
            prime_count += 1
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def mobius_cycle_count(n: int, period: int) -> int:
    numerator = sum(
        mobius(period // d) * formula_fixed_count(n, d)
        for d in divisors(period)
    )
    check(numerator % period == 0, f"nonintegral inversion at N={n}, m={period}")
    return numerator // period


def vp(n: int, p: int) -> int:
    result = 0
    while n % p == 0:
        result += 1
        n //= p
    return result


def prime_layer_inventory(p: int, r: int) -> Counter[int]:
    result: Counter[int] = Counter()
    for j in range(r + 1):
        result[p ** (j - min(j, r - j))] += p ** min(j, r - j)
    return result


def prime_closed_inventory(p: int, r: int) -> Counter[int]:
    result: Counter[int] = Counter()
    result[1] = sum(p**j for j in range(r // 2 + 1))
    for j in range(r // 2 + 1, r + 1):
        result[p ** (2 * j - r)] += p ** (r - j)
    return result


def prime_layer_fixed(p: int, r: int, time: int) -> int:
    return sum(
        p**j
        for j in range(r + 1)
        if (time * p ** (r - j)) % p**j == 0
    )


def prime_staircase_fixed(p: int, r: int, time: int) -> int:
    j_max = min(r, (r + vp(time, p)) // 2)
    return (p ** (j_max + 1) - 1) // (p - 1)


def run_hnf_lane() -> None:
    state_total = 0
    for n in range(1, 121):
        states = hnf_states(n)
        state_total += len(states)
        check(len(states) == len(set(states)), f"duplicate HNF state at N={n}")
        check(len(states) == sigma1(n), f"state count mismatch at N={n}")
        for a, b, c in states:
            check(a * c == n and 0 <= b < a, f"invalid HNF state at N={n}")
            raw_image = (a, b + c, c)
            canonical_image = shear_via_basis((a, b, c))
            check(
                canonical_image == closed_action((a, b, c)),
                f"action formula mismatch at N={n}, state={(a, b, c)}",
            )
            check(
                same_upper_lattice(raw_image, canonical_image),
                f"HNF reduction changed lattice at N={n}, state={(a, b, c)}",
            )
    print(f"HNF/action lane: N=1..120, {state_total} canonical states checked")


def run_general_dynamics_lane() -> None:
    fixed_cases = 0
    mobius_cases = 0
    for n in range(1, 121):
        formula = formula_cycle_inventory(n)
        direct = direct_cycle_inventory(n)
        check(direct == formula, f"cycle inventory mismatch at N={n}")
        check(
            sum(period * count for period, count in formula.items()) == sigma1(n),
            f"cycle accounting mismatch at N={n}",
        )
        check(max(formula) == n, f"maximal period does not recover N={n}")
        check(formula[n] == 1, f"maximal cycle is not unique at N={n}")
        for time in range(1, 2 * n + 1):
            fixed_cases += 1
            check(
                direct_fixed_count(n, time) == formula_fixed_count(n, time),
                f"fixed count mismatch at N={n}, time={time}",
            )
            orbit_fixed = sum(
                period * count
                for period, count in formula.items()
                if time % period == 0
            )
            check(
                orbit_fixed == formula_fixed_count(n, time),
                f"orbit/fixed identity mismatch at N={n}, time={time}",
            )
        for period in range(1, n + 1):
            mobius_cases += 1
            check(
                mobius_cycle_count(n, period) == formula.get(period, 0),
                f"Mobius reconstruction mismatch at N={n}, m={period}",
            )
    print(
        "general dynamics lane: 120 cycle censuses, "
        f"{fixed_cases} fixed-time cases, {mobius_cases} Mobius cases"
    )


def run_prime_power_lane() -> None:
    cases = 0
    valuation_cases = 0
    for p in (2, 3, 5, 7):
        for r in range(1, 11):
            cases += 1
            layered = prime_layer_inventory(p, r)
            closed = prime_closed_inventory(p, r)
            check(layered == closed, f"prime inventory mismatch at p={p}, r={r}")
            check(
                sum(period * count for period, count in closed.items())
                == (p ** (r + 1) - 1) // (p - 1),
                f"prime state accounting mismatch at p={p}, r={r}",
            )
            check(max(closed) == p**r, f"prime recovery mismatch at p={p}, r={r}")
            check(closed[p**r] == 1, f"prime maximal cycle mismatch p={p}, r={r}")
            for s in range(r + 3):
                # Multiplying by a p-coprime unit checks that only v_p(time) matters.
                for unit in (1, p + 1):
                    time = unit * p**s
                    valuation_cases += 1
                    check(
                        prime_layer_fixed(p, r, time)
                        == prime_staircase_fixed(p, r, time),
                        f"staircase mismatch at p={p}, r={r}, time={time}",
                    )
    print(
        f"prime-power lane: {cases} pairs (p,r), "
        f"{valuation_cases} valuation/unit cases"
    )


def run_regression_lane() -> None:
    expected = {
        1: {1: 1},
        8: {1: 3, 2: 2, 8: 1},
        9: {1: 4, 9: 1},
        12: {1: 3, 3: 3, 4: 1, 12: 1},
        16: {1: 7, 4: 2, 16: 1},
        25: {1: 6, 25: 1},
    }
    for n, inventory in expected.items():
        check(
            formula_cycle_inventory(n) == Counter(inventory),
            f"regression inventory mismatch at N={n}",
        )
    check(
        [formula_fixed_count(8, n) for n in range(1, 9)]
        == [3, 7, 3, 7, 3, 7, 3, 15],
        "N=8 fixed sequence regression failed",
    )
    print("regression lane: six inventories and the N=8 fixed sequence checked")


def main() -> None:
    print("Exact verification: unipotent shear on fixed-index sublattices")
    run_hnf_lane()
    run_general_dynamics_lane()
    run_prime_power_lane()
    run_regression_lane()
    print(f"PASS: {CHECKS:,} exact assertions")


if __name__ == "__main__":
    main()
