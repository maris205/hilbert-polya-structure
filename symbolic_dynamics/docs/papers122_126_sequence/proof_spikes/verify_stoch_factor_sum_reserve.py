#!/usr/bin/env python3
"""Exact falsification controls for the A02 factor-sum reserve.

This is intentionally a reserve/kill verifier.  It checks the structural
descent theorem and sharp extremal atom, while also recording the irregular
joint laws on powers of two.  It does not promote the divisor recursion to a
claimed closed form.
"""

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import isqrt, log2


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def factor_pairs(n):
    return tuple((a, n // a) for a in range(2, isqrt(n) + 1) if n % a == 0)


def is_prime(n):
    return n >= 2 and not factor_pairs(n)


@lru_cache(None)
def joint_law(n):
    pairs = factor_pairs(n)
    if not pairs:
        return (((n, 0), Fraction(1)),)
    answer = defaultdict(Fraction)
    for a, b in pairs:
        for (terminal, time), mass in joint_law(a + b - 1):
            answer[(terminal, time + 1)] += mass / len(pairs)
    return tuple(sorted(answer.items()))


@lru_cache(None)
def possible_times(n):
    pairs = factor_pairs(n)
    if not pairs:
        return frozenset((0,))
    return frozenset(
        1 + time
        for a, b in pairs
        for time in possible_times(a + b - 1)
    )


def forward_law(start):
    live = {start: Fraction(1)}
    answer = defaultdict(Fraction)
    time = 0
    while live:
        nxt = defaultdict(Fraction)
        for n, mass in live.items():
            pairs = factor_pairs(n)
            if not pairs:
                answer[(n, time)] += mass
            else:
                for a, b in pairs:
                    nxt[a + b - 1] += mass / len(pairs)
        live = nxt
        time += 1
    return tuple(sorted(answer.items()))


def main():
    # Literal inequality and its equality condition over a broad integer grid.
    factor_edges = 0
    for n in range(4, 20001):
        for a, b in factor_pairs(n):
            child = a + b - 1
            factor_edges += 1
            check(child < n, (n, a, b, "strict descent"))
            check(2 * (child - 2) <= n - 2, (n, a, b, "halving"))
            check((2 * (child - 2) == n - 2) == (a == 2),
                  (n, a, b, "equality"))
            check((child % 2 == 1) == (a % 2 == b % 2),
                  (n, a, b, "parity"))

    # Exact laws, two evaluation routes, terminal theorem, and time bound.
    states = 0
    for n in range(1, 5001):
        law = joint_law(n)
        states += len(law)
        check(sum(mass for _, mass in law) == 1, (n, "mass"))
        check(all(mass > 0 for _, mass in law), (n, "positivity"))
        if n <= 800:
            check(law == forward_law(n), (n, "forward recursion"))
        if factor_pairs(n):
            check(all(terminal >= 3 and terminal % 2 == 1 and is_prime(terminal)
                      for (terminal, _), _mass in law), (n, "odd prime terminal"))
        if n >= 3:
            bound = int(log2(n - 2))
            check(max(time for (terminal, time), mass in law) <= bound,
                  (n, "time bound", bound, law))

    # Sharp family N_r=2+2^r.  Equality forces the unique all-factor-two path.
    sharp_atoms = []
    for r in range(1, 16):
        n = 2 + 2**r
        law = dict(joint_law(n))
        check(max(time for terminal, time in law) == r, (r, n, "sharp depth"))
        product_atom = Fraction(1)
        for j in range(r, 0, -1):
            current = 2 + 2**j
            product_atom /= len(factor_pairs(current))
            check((2, 1 + 2**(j - 1)) in factor_pairs(current),
                  (r, j, current, "factor-two edge"))
        check(law.get((3, r), Fraction(0)) == product_atom,
              (r, n, "unique extremal atom", law.get((3, r)), product_atom))
        sharp_atoms.append((r, n, str(product_atom)))

    # The simplest prime-power lane already depends on factorization of
    # 2^i+2^(k-i)-1; record its exact joint-support sizes rather than fitting.
    power_two_support = []
    for exponent in range(2, 16):
        law = joint_law(2**exponent)
        power_two_support.append((exponent, len(law), max(t for (p, t), q in law)))

    check(dict(joint_law(36)) == {
        (3, 4): Fraction(1, 8),
        (5, 3): Fraction(1, 4),
        (7, 2): Fraction(1, 8),
        (11, 1): Fraction(1, 4),
        (19, 1): Fraction(1, 4),
    }, "n=36 control")

    print("factor-sum descent reserve structural control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"literal_factor_edges={factor_edges}; n=4..20000")
    print(f"exact_start_states=5000; joint_atoms={states}; forward_crosscheck=n<=800")
    print("theorem=odd-prime absorption; T<=floor(log2(n-2)); sharp N_r=2+2^r")
    print("sharp_atoms_r1_to_r15=" + repr(sharp_atoms))
    print("power_two_joint_support_(exponent,size,max_time)=" + repr(power_two_support))
    print("joint_law_n36=" + repr(joint_law(36)))
    print("decision_signal=no_all_size_joint_closed_form_beyond_divisor_DAG")


if __name__ == "__main__":
    main()
