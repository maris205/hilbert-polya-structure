#!/usr/bin/env python3
"""Deterministic exact author controls for P166.

The implementation begins with the literal map on (Z/nZ)^n.  It imports
no scout or reviewer code and uses only the Python standard library.
Every literal state is checked for 2 <= n <= 7.  Every target and every
time 0 <= t <= 2n is checked against the n-phase inverse oracle.  Weak
composition checks extend through n=10, and fixed-seed larger-modulus
tests include prime and composite n.
"""

from array import array
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, isqrt
from pathlib import Path
import random


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def histogram(word):
    n = len(word)
    result = [0] * n
    for symbol in word:
        result[symbol] += 1
    return tuple(result)


def encode(word, base):
    result = 0
    for symbol in word:
        result = result * base + symbol
    return result


def literal_step(word):
    n = len(word)
    weight = sum(symbol != 0 for symbol in word)
    return tuple((symbol + weight) % n for symbol in word)


def phase_map(profile):
    n = len(profile)
    return tuple((phase + profile[phase]) % n for phase in range(n))


def tail_period(mapping, start):
    first = {}
    point = start
    while point not in first:
        first[point] = len(first)
        point = mapping[point]
    return first[point], len(first) - first[point]


def graph_cycles(mapping):
    done = set()
    answer = []
    for start in range(len(mapping)):
        if start in done:
            continue
        local = {}
        path = []
        point = start
        while point not in local and point not in done:
            local[point] = len(path)
            path.append(point)
            point = mapping[point]
        if point in local:
            answer.append(tuple(path[local[point] :]))
        done.update(path)
    return answer


def is_gap_profile(profile):
    n = len(profile)
    support = [i for i, value in enumerate(profile) if value]
    if not support:
        return False
    for index, point in enumerate(support):
        successor = support[(index + 1) % len(support)]
        gap = (successor - point) % n or n
        if profile[point] != gap:
            return False
    return True


def stirling(n, k):
    row = [0] * (k + 1)
    row[0] = 1
    for size in range(1, n + 1):
        nxt = [0] * (k + 1)
        for blocks in range(1, min(size, k) + 1):
            nxt[blocks] = row[blocks - 1] + blocks * row[blocks]
        row = nxt
    return row[k]


def period_formula(n):
    answer = {1: 1 + (n - 1) ** n}
    for period in range(2, n + 1):
        answer[period] = factorial(period) * stirling(n, period)
    return answer


def depth_formula(n, depth):
    if depth == 0:
        return (n - 1) ** n + sum(
            factorial(k) * stirling(n, k) for k in range(1, n + 1)
        )
    if depth >= n - 1:
        return 0
    return factorial(depth) * sum(
        comb(n, mass)
        * stirling(mass, depth)
        * (n - depth - 1) ** (n - mass)
        for mass in range(depth, n)
    )


def fibre_formula(word):
    n = len(word)
    profile = histogram(word)
    return (
        int(all(symbol == 0 for symbol in word))
        + int(profile[0] == 0)
        + sum(profile[k] == n - k for k in range(1, n))
    )


def max_fibre_formula(n):
    if n == 2:
        return 1
    return 1 + (isqrt(8 * n + 1) - 1) // 2


def multiply_bivariate(left, right, degree_cap):
    answer = {}
    for (z_left, u_left), coefficient_left in left.items():
        for (z_right, u_right), coefficient_right in right.items():
            degree = z_left + z_right
            if degree <= degree_cap:
                key = (degree, u_left + u_right)
                answer[key] = answer.get(key, Fraction(0)) + (
                    coefficient_left * coefficient_right
                )
    return answer


def marked_egf_formula(n):
    """Coefficient expansion of equation (13), independent of states."""
    polynomial = {(0, 0): Fraction(1)}
    zero_factor = {}
    for degree in range(n + 1):
        zero_factor[(degree, int(degree == 0))] = Fraction(1, factorial(degree))
    polynomial = multiply_bivariate(polynomial, zero_factor, n)
    for required in range(1, n):
        factor = {}
        for degree in range(n + 1):
            factor[(degree, int(degree == required))] = Fraction(
                1, factorial(degree)
            )
        polynomial = multiply_bivariate(polynomial, factor, n)
    answer = Counter()
    for (degree, fibre), coefficient in polynomial.items():
        if degree == n:
            scaled = coefficient * factorial(n)
            check(scaled.denominator == 1, ("EGF integrality", n, fibre, scaled))
            answer[fibre] += int(scaled)
    answer[0] -= 1
    answer[1] += 1
    check(answer[0] >= 0, ("EGF correction", n, answer))
    return dict(sorted((degree, count) for degree, count in answer.items() if count))


def weak_compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for first in range(total + 1):
        yield from weak_compositions(total - first, parts - 1, prefix + (first,))


def composition_audit(n):
    composition_count = 0
    cycle_support_hist = Counter()
    sharp_profiles = 0
    sharp_phase_pairs = 0
    for profile in weak_compositions(n, n):
        composition_count += 1
        mapping = phase_map(profile)
        nontrivial = [cycle for cycle in graph_cycles(mapping) if len(cycle) > 1]
        check(len(nontrivial) <= 1, ("cycle uniqueness", n, profile, nontrivial))
        if nontrivial:
            cycle = nontrivial[0]
            check(sum(profile[j] for j in cycle) == n,
                  ("cycle mass", n, profile, cycle))
            check(set(cycle) == {j for j, value in enumerate(profile) if value},
                  ("cycle support", n, profile, cycle))
            check(is_gap_profile(profile), ("gap cycle", n, profile, cycle))
            cycle_support_hist[len(cycle)] += 1
        elif is_gap_profile(profile):
            check(sum(value > 0 for value in profile) == 1,
                  ("unseen nontrivial gap cycle", n, profile))

        tails = [tail_period(mapping, phase)[0] for phase in range(n)]
        check(max(tails) <= n - 2, ("composition tail cap", n, profile, tails))
        if n >= 3:
            word = tuple(
                symbol
                for symbol, multiplicity in enumerate(profile)
                for _ in range(multiplicity)
            )
            degree = fibre_formula(word)
            maximum = max_fibre_formula(n)
            hits = sum(profile[k] == n - k for k in range(1, n))
            equality = profile[0] == 0 and hits == maximum - 1
            check((degree == maximum) == equality,
                  ("composition max-fibre equality", n, profile, degree, equality))
        if n >= 3:
            zeros = [j for j, value in enumerate(profile) if value == 0]
            doubles = [j for j, value in enumerate(profile) if value == 2]
            equality_shape = (
                len(zeros) == 1
                and len(doubles) == 1
                and all(value in (0, 1, 2) for value in profile)
                and doubles[0] != (zeros[0] - 1) % n
            )
            check((max(tails) == n - 2) == equality_shape,
                  ("sharp shape", n, profile, tails))
            if equality_shape:
                sharp_profiles += 1
                zero = zeros[0]
                double = doubles[0]
                wanted = {(zero + 1) % n}
                if double == (zero + 1) % n:
                    wanted.add((zero + 2) % n)
                observed = {j for j, tail in enumerate(tails) if tail == n - 2}
                check(observed == wanted,
                      ("sharp phases", n, profile, observed, wanted))
                sharp_phase_pairs += len(observed)

    for length in range(2, n + 1):
        check(cycle_support_hist[length] == comb(n, length),
              ("cycle support census", n, length, cycle_support_hist))
    if n >= 3:
        check(sharp_profiles == n * (n - 2),
              ("sharp profile count", n, sharp_profiles))
        check(sharp_phase_pairs == n * (n - 1),
              ("sharp phase-pair count", n, sharp_phase_pairs))
    return composition_count, sharp_profiles, sharp_phase_pairs


def literal_audit(n):
    state_count = n ** n
    transition = array("I", [0]) * state_count
    phase_maps = bytearray(state_count * n)
    tails = Counter()
    recurrent_periods = Counter()

    for index, word in enumerate(product(range(n), repeat=n)):
        check(index == encode(word, n), ("lexicographic encoding", n, index, word))
        profile = histogram(word)
        target = literal_step(word)
        expected = tuple((symbol - profile[0]) % n for symbol in word)
        check(target == expected, ("literal phase step", n, word, target, expected))
        transition[index] = encode(target, n)
        mapping = phase_map(profile)
        offset = index * n
        for phase in range(n):
            phase_maps[offset + phase] = mapping[phase]
        tail, period = tail_period(mapping, 0)
        tails[tail] += 1
        if tail == 0:
            recurrent_periods[period] += 1

    check(dict(sorted(recurrent_periods.items())) == period_formula(n),
          ("exact periods", n, recurrent_periods, period_formula(n)))
    for depth in range(0, n + 2):
        check(tails[depth] == depth_formula(n, depth),
              ("exact depths", n, depth, tails[depth], depth_formula(n, depth)))
    check(max(tails) == n - 2, ("sharp depth", n, tails))
    if n >= 3:
        check(tails[n - 2] == (n - 1) * factorial(n) // 2,
              ("last shell", n, tails[n - 2]))

    # One-step every-target fibres and the exact marked enumerator.
    one_step_indegree = array("I", [0]) * state_count
    for target_index in transition:
        one_step_indegree[target_index] += 1
    fibre_distribution = Counter()
    max_fibre = max_fibre_formula(n)
    image_size = 0
    for index, word in enumerate(product(range(n), repeat=n)):
        wanted = fibre_formula(word)
        observed = one_step_indegree[index]
        check(observed == wanted, ("one-step target fibre", n, word, observed, wanted))
        fibre_distribution[observed] += 1
        image_size += observed > 0
        profile = histogram(word)
        if n >= 3:
            hits = sum(profile[k] == n - k for k in range(1, n))
            equality = profile[0] == 0 and hits == max_fibre - 1
            check((observed == max_fibre) == equality,
                  ("max fibre equality", n, word, observed, equality))
    check(dict(sorted(fibre_distribution.items())) == marked_egf_formula(n),
          ("marked EGF", n, fibre_distribution, marked_egf_formula(n)))
    check(max(fibre_distribution) == max_fibre,
          ("sharp max fibre", n, fibre_distribution, max_fibre))

    # All target/time inverse counts, with independent literal powering and
    # phase powering.  The phase arrays keep all n possible target sources.
    literal_power = array("I", range(state_count))
    phase_power = bytearray(state_count * n)
    for index in range(state_count):
        offset = index * n
        for phase in range(n):
            phase_power[offset + phase] = phase
    for time in range(2 * n + 1):
        indegree = array("I", [0]) * state_count
        for target_index in literal_power:
            indegree[target_index] += 1
        for target_index in range(state_count):
            offset = target_index * n
            oracle = phase_power[offset : offset + n].count(0)
            check(indegree[target_index] == oracle,
                  ("all-time target oracle", n, time, target_index,
                   indegree[target_index], oracle))
        if time < 2 * n:
            for source in range(state_count):
                literal_power[source] = transition[literal_power[source]]
            for target_index in range(state_count):
                offset = target_index * n
                for phase in range(n):
                    old = phase_power[offset + phase]
                    phase_power[offset + phase] = phase_maps[offset + old]

    return {
        "states": state_count,
        "image": image_size,
        "tails": dict(sorted(tails.items())),
        "periods": dict(sorted(recurrent_periods.items())),
        "fibres": dict(sorted(fibre_distribution.items())),
        "oracle_times": 2 * n + 1,
    }


def randomized_extensions():
    generator = random.Random(0x16648A)
    tests = 0
    for n in (8, 9, 10, 11, 12, 15, 16, 20, 27, 31, 48, 64):
        for _ in range(500):
            profile = [0] * n
            for _ball in range(n):
                profile[generator.randrange(n)] += 1
            profile = tuple(profile)
            mapping = phase_map(profile)
            nontrivial = [cycle for cycle in graph_cycles(mapping) if len(cycle) > 1]
            check(len(nontrivial) <= 1, ("extension cycle uniqueness", n, profile))
            if nontrivial:
                cycle = nontrivial[0]
                check(sum(profile[j] for j in cycle) == n,
                      ("extension cycle mass", n, profile, cycle))
                check(is_gap_profile(profile), ("extension gap cycle", n, profile))
            tails = [tail_period(mapping, phase)[0] for phase in range(n)]
            check(max(tails) <= n - 2, ("extension tail cap", n, profile))
            word = tuple(
                symbol
                for symbol, multiplicity in enumerate(profile)
                for _ in range(multiplicity)
            )
            check(fibre_formula(word) <= max_fibre_formula(n),
                  ("extension fibre cap", n, profile))
            tests += 1
    for n in range(3, 129):
        h = (isqrt(8 * n + 1) - 1) // 2
        profile = [0] * n
        for required in range(1, h + 1):
            profile[n - required] = required
        remainder = n - h * (h + 1) // 2
        if remainder:
            check(n >= 4 and h < n - 1,
                  ("witness nonmarked bin exists", n, h, remainder))
            profile[1] = remainder
            check(profile[1] != n - 1,
                  ("witness nonhit bin", n, h, remainder))
        word = tuple(
            symbol
            for symbol, multiplicity in enumerate(profile)
            for _ in range(multiplicity)
        )
        check(len(word) == n, ("witness size", n, profile))
        check(fibre_formula(word) == 1 + h,
              ("sharp fibre witness", n, profile, fibre_formula(word), 1 + h))
    return tests


def statement_sentinels():
    source = (Path(__file__).resolve().parents[1] / "main.tex").read_text()
    required = (
        "target-local",
        "$n$-phase oracle",
        "exactly the parity-controlled binary complement map",
        "claim of novelty or priority is made",
        "HOLD\\_EXTERNAL",
        "D_{n,n-2}=\\frac{(n-1)n!}{2}",
        "I_n(u)=(u-1)+n![z^n]",
    )
    for token in required:
        check(token in source, ("missing manuscript scope sentinel", token))
    check(source.count("closed global all-time fibre census") >= 1,
          "missing explicit all-time claim ceiling")
    forbidden = ("we prove novelty", "first known")
    for token in forbidden:
        check(token not in source.lower(), ("forbidden priority language", token))


def format_counter(values):
    return ",".join(f"{key}:{values[key]}" for key in sorted(values))


def main():
    print("P166_HWT_AUTHOR_VERIFIER_V1")
    print("literal=T_n(x)=x+wt(x)*1 mod n; integer Hamming weight")
    for n in range(2, 8):
        result = literal_audit(n)
        print(
            f"n={n} states={result['states']} image={result['image']} "
            f"tails={format_counter(result['tails'])} "
            f"periods={format_counter(result['periods'])} "
            f"fibres={format_counter(result['fibres'])} "
            f"oracle_times={result['oracle_times']}"
        )
    for n in range(2, 11):
        count, sharp_profiles, sharp_pairs = composition_audit(n)
        print(
            f"compositions_n={n} count={count} "
            f"sharp_profiles={sharp_profiles} sharp_phase_pairs={sharp_pairs}"
        )
    extension_tests = randomized_extensions()
    statement_sentinels()
    print(
        "extensions=6000 moduli=8,9,10,11,12,15,16,20,27,31,48,64 "
        f"observed={extension_tests}"
    )
    print("BOUNDARIES=n=2;t=0;weights=0,n;zero/full-support targets;composite n")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
