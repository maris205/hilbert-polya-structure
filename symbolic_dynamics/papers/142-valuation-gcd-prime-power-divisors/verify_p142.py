#!/usr/bin/env python3
"""Exact falsification controls for P142.

The verifier uses only Python integers and the standard-library gcd.  It
recomputes the literal divisor map, constructs every bounded functional graph,
and compares it with each formula frozen in the theorem contract.  Finite
enumeration is not a proof of the all-parameter statements and is not novelty
or ownership evidence.
"""

from collections import Counter
from math import gcd


ASSERTIONS = 0
ODD_PRIMES = (3, 5, 7, 11)
MIN_EXPONENT = 2
MAX_EXPONENT = 128
FIXED_ITERATES = 12
BINARY_MAX_EXPONENT = 48


def check(condition, message):
    """Count and enforce one Boolean assertion."""
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def valuation(value, prime):
    """Return v_prime(value) for a positive integer value."""
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def ceil_div(numerator, denominator):
    return (numerator + denominator - 1) // denominator


def ceil_log_ratio(numerator, denominator):
    """Least j >= 0 with 2**j * denominator >= numerator."""
    exponent = 0
    scaled = denominator
    while scaled < numerator:
        scaled *= 2
        exponent += 1
    return exponent


def exponent_step(exponent, state):
    return min(2 * state, exponent - state)


def predicted_entry_time(exponent, state):
    lower = ceil_div(exponent, 3)
    upper = (2 * exponent) // 3
    if state == 0 or lower <= state <= upper:
        return 0
    if 1 <= state < lower:
        return ceil_log_ratio(lower, state)
    if state == exponent:
        return 1
    return 1 + ceil_log_ratio(lower, exponent - state)


def literal_step(prime, exponent, state):
    modulus = prime**exponent
    divisor = prime**state
    output = gcd(modulus, divisor * divisor + modulus // divisor)
    return output, valuation(output, prime)


def orbit_record(images, start):
    seen = {}
    order = []
    state = start
    while state not in seen:
        seen[state] = len(order)
        order.append(state)
        state = images[state]
    tail = seen[state]
    period = len(order) - tail
    return tail, period, tuple(order[tail:])


def run_odd_prime_controls():
    profiles = []
    total_states = 0
    total_fibre_targets = 0
    total_orbits = 0

    for prime in ODD_PRIMES:
        for exponent in range(MIN_EXPONENT, MAX_EXPONENT + 1):
            lower = ceil_div(exponent, 3)
            upper = (2 * exponent) // 3
            recurrent = {0, *range(lower, upper + 1)}
            recurrent_count = upper - lower + 2
            fixed_count = 1 + (exponent % 2 == 0)

            check(exponent - upper == lower,
                  "complement-band lower endpoint identity failed")
            check(exponent - lower == upper,
                  "complement-band upper endpoint identity failed")
            check(len(recurrent) == recurrent_count,
                  "recurrent-set cardinality formula failed")

            images = []
            for state in range(exponent + 1):
                literal, output_exponent = literal_step(prime, exponent, state)
                predicted = exponent_step(exponent, state)
                check(literal == prime**output_exponent,
                      "literal gcd was not a pure power of the carrier prime")
                check(output_exponent == predicted,
                      "literal valuation conjugacy failed")
                check(0 <= output_exponent <= exponent,
                      "literal map left the exponent carrier")
                if 3 * state == exponent:
                    check((literal // (prime ** (2 * state))) == 1,
                          "odd equal-valuation branch acquired an extra factor")
                images.append(output_exponent)

            check(tuple(images) == tuple(exponent_step(exponent, state)
                                          for state in range(exponent + 1)),
                  "literal and predicted transition tables differ")

            observed_recurrent = set()
            depth_histogram = Counter()
            for state in range(exponent + 1):
                tail, period, cycle = orbit_record(images, state)
                predicted_tail = predicted_entry_time(exponent, state)
                check(tail == predicted_tail,
                      "pointwise entry-time formula failed")
                check(period in (1, 2),
                      "functional graph acquired a cycle longer than two")
                entry_state = cycle[0]
                predicted_period = (1 if entry_state == 0
                                    or 2 * entry_state == exponent else 2)
                check(period == predicted_period,
                      "fixed/complement-cycle classification failed")
                check(all(member in recurrent for member in cycle),
                      "direct orbit closed outside the predicted recurrent set")
                if tail == 0:
                    check(state in recurrent,
                          "zero-tail state lies outside the recurrent set")
                else:
                    check(state not in recurrent,
                          "positive-tail state lies inside the recurrent set")
                observed_recurrent.update(cycle)
                depth_histogram[tail] += 1
                total_orbits += 1

            check(observed_recurrent == recurrent,
                  "complete recurrent exponent set failed")
            check(sum(images[state] == state for state in range(exponent + 1))
                  == fixed_count,
                  "fixed-state count failed")

            for iterate in range(1, FIXED_ITERATES + 1):
                fixed_iterate = 0
                for state in range(exponent + 1):
                    current = state
                    for _ in range(iterate):
                        current = images[current]
                    fixed_iterate += current == state
                predicted_fixed_iterate = (fixed_count if iterate % 2
                                             else recurrent_count)
                check(fixed_iterate == predicted_fixed_iterate,
                      "fixed-iterate parity formula failed")

            maximum_tail = 1 + ceil_log_ratio(lower, 1)
            deepest = [state for state in range(exponent + 1)
                       if predicted_entry_time(exponent, state) == maximum_tail]
            check(max(depth_histogram) == maximum_tail,
                  "sharp maximum entry time failed")
            if exponent >= 4:
                check(deepest == [exponent - 1],
                      "unique deepest exponent failed")
            else:
                check(deepest == [exponent],
                      "small-exponent unique deepest boundary failed")

            m = ceil_log_ratio(lower, 1)
            predicted_histogram = Counter({0: recurrent_count, 1: 1})
            c_values = []
            for depth in range(1, m + 1):
                c_depth = (ceil_div(lower, 1 << (depth - 1))
                           - ceil_div(lower, 1 << depth))
                check(c_depth > 0,
                      "temporal coefficient should be positive in its range")
                predicted_histogram[depth] += c_depth
                predicted_histogram[depth + 1] += c_depth
                c_values.append(c_depth)
            check(predicted_histogram == depth_histogram,
                  "complete temporal polynomial failed")
            check(sum(predicted_histogram.values()) == exponent + 1,
                  "temporal polynomial does not enumerate the carrier")

            actual_fibres = {target: set() for target in range(exponent + 1)}
            for source, target in enumerate(images):
                actual_fibres[target].add(source)
            for target in range(exponent + 1):
                expected_fibre = set()
                if target <= upper:
                    expected_fibre.add(exponent - target)
                    if target % 2 == 0:
                        expected_fibre.add(target // 2)
                check(actual_fibres[target] == expected_fibre,
                      "every-target inverse formula failed")
                if (target <= upper and target % 2 == 0
                        and 3 * target == 2 * exponent):
                    check(len(expected_fibre) == 1,
                          "coincident inverse branches were double counted")
                total_fibre_targets += 1
            check({images[state] for state in range(exponent + 1)}
                  == set(range(upper + 1)),
                  "image interval formula failed")
            check(max(len(fibre) for fibre in actual_fibres.values()) == 2,
                  "maximum one-step fibre should equal two")

            total_states += exponent + 1
            if prime == 3 and exponent in (2, 3, 4, 8, 16, 32, 64, 128):
                temporal = "/".join(
                    f"{depth}:{depth_histogram[depth]}"
                    for depth in sorted(depth_histogram)
                )
                profiles.append(
                    f"e={exponent},L={lower},U={upper},R={recurrent_count},"
                    f"A={fixed_count},M={maximum_tail},deep={deepest[0]},"
                    f"D={temporal},c={','.join(map(str, c_values)) or '-'}"
                )

    return {
        "boxes": len(ODD_PRIMES) * (MAX_EXPONENT - MIN_EXPONENT + 1),
        "states": total_states,
        "orbits": total_orbits,
        "fibre_targets": total_fibre_targets,
        "profiles": profiles,
    }


def run_binary_boundary_controls():
    states = 0
    equal_cases = 0
    smallest_witness = None
    for exponent in range(MIN_EXPONENT, BINARY_MAX_EXPONENT + 1):
        modulus = 1 << exponent
        for state in range(exponent + 1):
            divisor = 1 << state
            literal = gcd(modulus, divisor * divisor + modulus // divisor)
            literal_exponent = valuation(literal, 2)
            baseline = min(2 * state, exponent - state)
            predicted = baseline + (1 if 3 * state == exponent else 0)
            predicted = min(exponent, predicted)
            check(literal == 1 << literal_exponent,
                  "binary gcd was not a power of two")
            check(literal_exponent == predicted,
                  "binary boundary valuation formula failed")
            if 3 * state == exponent:
                equal_cases += 1
                check(literal_exponent == 2 * state + 1,
                      "binary equal-valuation branch missed its extra factor")
                check(literal_exponent != baseline,
                      "binary case incorrectly obeyed the odd-prime rule")
                if smallest_witness is None:
                    smallest_witness = (exponent, state, literal_exponent)
            states += 1
    check(equal_cases == BINARY_MAX_EXPONENT // 3,
          "binary equal-valuation case count failed")
    check(smallest_witness == (3, 1, 3),
          "smallest binary boundary witness failed")
    return {
        "boxes": BINARY_MAX_EXPONENT - MIN_EXPONENT + 1,
        "states": states,
        "equal_cases": equal_cases,
        "smallest_witness": smallest_witness,
    }


def main():
    odd = run_odd_prime_controls()
    binary = run_binary_boundary_controls()
    print("P142_VALUATION_GCD_EXACT_CONTROL")
    print("arithmetic=exact_python_integers;sampling=none;floating_point=none")
    print("odd_primes=" + ",".join(map(str, ODD_PRIMES)))
    print(f"odd_exponents={MIN_EXPONENT}..{MAX_EXPONENT}")
    print(f"odd_boxes={odd['boxes']}")
    print(f"odd_states={odd['states']}")
    print(f"odd_orbits={odd['orbits']}")
    print(f"odd_fibre_targets={odd['fibre_targets']}")
    print(f"fixed_iterates_checked=1..{FIXED_ITERATES}")
    print(f"binary_exponents={MIN_EXPONENT}..{BINARY_MAX_EXPONENT}")
    print(f"binary_boxes={binary['boxes']}")
    print(f"binary_states={binary['states']}")
    print(f"binary_equal_cases={binary['equal_cases']}")
    exponent, state, value = binary["smallest_witness"]
    print(f"binary_smallest_witness=e{exponent},a{state},valuation{value}")
    for profile in odd["profiles"]:
        print("PROFILE " + profile)
    print(f"TOTAL_ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
