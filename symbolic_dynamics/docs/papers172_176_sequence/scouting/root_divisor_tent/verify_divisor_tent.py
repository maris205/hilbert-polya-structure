#!/usr/bin/env python3
"""Exact kill-gate for common-factor cancellation on divisor pairs."""

from __future__ import annotations

import hashlib
import itertools
import json
import math


CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def v2(value: int) -> int:
    if value == 0:
        return 10**9
    answer = 0
    while value % 2 == 0:
        value //= 2
        answer += 1
    return answer


def step(exponent: int, state: int) -> int:
    return abs(exponent - 2 * state)


def iterate(exponent: int, state: int, time: int) -> int:
    for _ in range(time):
        state = step(exponent, state)
    return state


def triangle_distance(exponent: int, value: int) -> int:
    residue = value % (2 * exponent)
    return abs(exponent - residue)


def predicted_depth(exponent: int, state: int) -> int:
    scale = v2(exponent)
    if state > 0 and v2(state) == scale:
        return 0
    if state == 0 or v2(state) > scale:
        return 1
    return scale - v2(state) + 1


def orbit_data(exponent: int, state: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    time = 0
    while state not in seen:
        seen[state] = time
        state = step(exponent, state)
        time += 1
    return seen[state], time - seen[state]


def predicted_fixed(exponent: int, time: int) -> int:
    odd_part = exponent >> v2(exponent)
    return (
        math.gcd(odd_part, (1 << time) - 1)
        + math.gcd(odd_part, (1 << time) + 1)
    ) // 2


def congruence_fibre(exponent: int, time: int, target: int) -> set[int]:
    if time == 0:
        return {target} if 0 <= target <= exponent else set()
    modulus = 2 * exponent
    residues = {(exponent - target) % modulus, (exponent + target) % modulus}
    return {
        source
        for source in range(exponent + 1)
        if (pow(2, time, modulus) * source) % modulus in residues
    }


def divisors(primes: tuple[int, ...], exponents: tuple[int, ...]):
    for vector in itertools.product(*(range(e + 1) for e in exponents)):
        value = math.prod(p**a for p, a in zip(primes, vector))
        yield vector, value


def literal_step(modulus: int, divisor: int) -> int:
    common = math.gcd(divisor, modulus // divisor)
    return modulus // (common * common)


def run() -> None:
    scalar_profiles = {}
    for exponent in range(1, 161):
        recurrent = []
        depths = []
        for state in range(exponent + 1):
            depth, period = orbit_data(exponent, state)
            depths.append(depth)
            if depth == 0:
                recurrent.append(state)
            check(depth == predicted_depth(exponent, state),
                  f"depth e={exponent} a={state}")
            for time in range(1, 13):
                check(
                    iterate(exponent, state, time)
                    == triangle_distance(exponent, (1 << time) * state),
                    f"triangle iterate e={exponent} a={state} t={time}",
                )
                check(
                    (iterate(exponent, state, time) == state)
                    == (depth == 0 and time % period == 0),
                    f"period gate e={exponent} a={state} t={time}",
                )
        scale = v2(exponent)
        odd_part = exponent >> scale
        check(max(depths) == scale + 1, f"sharp depth e={exponent}")
        check(
            recurrent
            == [a for a in range(1, exponent + 1) if v2(a) == scale],
            f"recurrent set e={exponent}",
        )
        check(len(recurrent) == (odd_part + 1) // 2,
              f"recurrent count e={exponent}")
        for time in range(1, 13):
            fixed = sum(iterate(exponent, a, time) == a
                        for a in range(exponent + 1))
            check(fixed == predicted_fixed(exponent, time),
                  f"fixed e={exponent} t={time}")
        for time in range(0, min(10, scale + 5)):
            for target in range(exponent + 1):
                direct = {
                    source
                    for source in range(exponent + 1)
                    if iterate(exponent, source, time) == target
                }
                check(
                    direct == congruence_fibre(exponent, time, target),
                    f"fibre e={exponent} t={time} b={target}",
                )
        if exponent in {1, 2, 3, 4, 6, 8, 10, 12, 16, 24, 32, 64, 96, 128, 160}:
            period_census = {}
            for a in recurrent:
                _, period = orbit_data(exponent, a)
                period_census[period] = period_census.get(period, 0) + 1
            scalar_profiles[str(exponent)] = {
                "height": max(depths),
                "recurrent": len(recurrent),
                "period_points": period_census,
            }

    product_profiles = []
    boxes = [
        (2, 3), (3, 4), (4, 5), (5, 6), (6, 8), (7, 10),
        (8, 12), (3, 4, 5), (4, 6, 8), (5, 8, 9), (6, 10, 12),
    ]
    primes = (2, 3, 5)
    for exponents in boxes:
        used_primes = primes[:len(exponents)]
        modulus = math.prod(p**e for p, e in zip(used_primes, exponents))
        states = list(itertools.product(*(range(e + 1) for e in exponents)))
        recurrent_count = 1
        height = 0
        for e in exponents:
            odd_part = e >> v2(e)
            recurrent_count *= (odd_part + 1) // 2
            height = max(height, v2(e) + 1)
        direct_depths = []
        for vector in states:
            component_data = [orbit_data(e, a) for e, a in zip(exponents, vector)]
            direct_depths.append(max(depth for depth, _ in component_data))
        check(max(direct_depths) == height, f"product height {exponents}")
        check(sum(d == 0 for d in direct_depths) == recurrent_count,
              f"product recurrent {exponents}")
        for time in range(1, 9):
            fixed = sum(
                all(iterate(e, a, time) == a for e, a in zip(exponents, vector))
                for vector in states
            )
            check(
                fixed == math.prod(predicted_fixed(e, time) for e in exponents),
                f"product fixed {exponents} t={time}",
            )
        for vector, divisor in divisors(used_primes, exponents):
            literal = literal_step(modulus, divisor)
            predicted_vector = tuple(step(e, a) for e, a in zip(exponents, vector))
            predicted_literal = math.prod(
                p**a for p, a in zip(used_primes, predicted_vector)
            )
            check(literal == predicted_literal, f"literal {exponents} {vector}")
        product_profiles.append({
            "exponents": exponents,
            "states": len(states),
            "height": height,
            "recurrent": recurrent_count,
        })

    payload = {
        "decision": "KILL_INTERNAL_COLLISION_P142",
        "literal": "d -> N/gcd(d,N/d)^2",
        "scalar_rule": "a -> abs(e-2a)",
        "scalar_profiles": scalar_profiles,
        "product_profiles": product_profiles,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print("DIVISOR_TENT_KILL_GATE_PASS")
    print(f"assertions={CHECKS}")
    print(f"payload_sha256={hashlib.sha256(canonical.encode()).hexdigest()}")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    run()
