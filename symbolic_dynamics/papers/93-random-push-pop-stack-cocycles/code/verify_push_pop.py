#!/usr/bin/env python3
"""Exact controls for random push--pop stack cocycles.

The proof layer uses Python integers and ``fractions.Fraction`` only.  The
final five rescaled values are floating-point diagnostics; they are labelled
separately and never certify an identity or a limit theorem.  No third-party
package is required.

An operation is represented by ``None`` for the left shift D and by an
integer ``a`` for the prefix map C_a.  Operations are listed in chronological
order, so the resulting map is op_n o ... o op_1.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, sqrt, pi


ASSERTIONS = 0
DIAGNOSTIC_CHECKS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def diagnostic_check(condition, message):
    global DIAGNOSTIC_CHECKS
    DIAGNOSTIC_CHECKS += 1
    if not condition:
        raise AssertionError(message)


def normal_form(operations):
    """Return (unmatched prefix, unmatched pops, S, M)."""
    prefix = ()
    unmatched_pops = 0
    walk = 0
    maximum = 0
    for operation in operations:
        if operation is None:
            walk += 1
            maximum = max(maximum, walk)
            if prefix:
                prefix = prefix[1:]
            else:
                unmatched_pops += 1
        else:
            walk -= 1
            prefix = (operation,) + prefix
    return prefix, unmatched_pops, walk, maximum


def apply_to_sequence(operations, sequence):
    """Apply prefix/shift operations directly to a sufficiently long list."""
    answer = list(sequence)
    for operation in operations:
        if operation is None:
            answer = answer[1:]
        else:
            answer = [operation] + answer
    return tuple(answer)


def operations_from_directions(directions, alphabet_size):
    """Use deterministic labels while preserving the supplied directions."""
    operations = []
    for time, is_pop in enumerate(directions):
        operations.append(None if is_pop else time % alphabet_size)
    return tuple(operations)


def check_running_maximum_normal_form(maximum_time=15):
    for time in range(maximum_time + 1):
        for directions in product((0, 1), repeat=time):
            operations = operations_from_directions(directions, 3)
            prefix, pops, walk, maximum = normal_form(operations)
            check(pops == maximum,
                  f"J != M for directions={directions}")
            check(len(prefix) == maximum - walk,
                  f"I != M-S for directions={directions}")
            check(len(prefix) - pops == -walk,
                  f"I-J != -S for directions={directions}")


def check_labeled_maps(alphabet_size=2, maximum_time=9, probe_length=5):
    operation_alphabet = (None,) + tuple(range(alphabet_size))
    for time in range(maximum_time + 1):
        for operations in product(operation_alphabet, repeat=time):
            prefix, pops, walk, maximum = normal_form(operations)
            tail = tuple(("x", index) for index in range(2 * time + probe_length + 1))
            symbolic_operations = tuple(
                None if operation is None else ("a", operation)
                for operation in operations
            )
            direct = apply_to_sequence(symbolic_operations, tail)
            claimed = tuple(("a", letter) for letter in prefix) + tail[pops:]
            check(direct[:len(prefix) + probe_length]
                  == claimed[:len(prefix) + probe_length],
                  f"definition-level map mismatch for {operations}")
            check(pops == maximum and len(prefix) == maximum - walk,
                  f"labeled normal form mismatch for {operations}")


def check_image_and_fibres(alphabet_size, maximum_time, free_tail=2):
    for time in range(maximum_time + 1):
        for directions in product((0, 1), repeat=time):
            operations = operations_from_directions(directions, alphabet_size)
            prefix, pops, _, _ = normal_form(operations)
            outputs = Counter()
            for initial in product(range(alphabet_size),
                                   repeat=pops + free_tail):
                outputs[apply_to_sequence(operations, initial)] += 1
            check(len(outputs) == alphabet_size ** free_tail,
                  f"image-size mismatch for b={alphabet_size}, {directions}")
            check(all(len(output) == len(prefix) + free_tail
                      for output in outputs),
                  f"output-length mismatch for b={alphabet_size}, {directions}")
            check(all(output[:len(prefix)] == prefix for output in outputs),
                  f"cylinder-prefix mismatch for b={alphabet_size}, {directions}")
            check(all(multiplicity == alphabet_size ** pops
                      for multiplicity in outputs.values()),
                  f"fibre-degree mismatch for b={alphabet_size}, {directions}")


def joint_walk_distribution(time, pop_probability):
    push_probability = 1 - pop_probability
    distribution = {(0, 0): Fraction(1)}
    for _ in range(time):
        next_distribution = {}
        for (walk, maximum), mass in distribution.items():
            up = (walk + 1, max(maximum, walk + 1))
            down = (walk - 1, maximum)
            next_distribution[up] = (next_distribution.get(up, Fraction(0))
                                     + mass * pop_probability)
            next_distribution[down] = (next_distribution.get(down, Fraction(0))
                                       + mass * push_probability)
        distribution = next_distribution
    return distribution


def annealed_degree_from_walk(time, pop_probability, alphabet_size):
    distribution = joint_walk_distribution(time, pop_probability)
    return sum(mass * alphabet_size ** maximum
               for (_, maximum), mass in distribution.items())


def expected_maximum(time, pop_probability):
    distribution = joint_walk_distribution(time, pop_probability)
    return sum(mass * maximum
               for (_, maximum), mass in distribution.items())


def ballot_annealed_degree(time, pop_probability, alphabet_size):
    """First-passage expansion from the theorem, evaluated in Q."""
    push_probability = 1 - pop_probability
    answer = Fraction(1)
    for level in range(1, time + 1):
        hit_by_time = Fraction(0)
        for first_time in range(level, time + 1, 2):
            pops = (first_time + level) // 2
            pushes = (first_time - level) // 2
            hit_by_time += (
                Fraction(level, first_time)
                * comb(first_time, pops)
                * pop_probability ** pops
                * push_probability ** pushes
            )
        answer += ((alphabet_size - 1)
                   * alphabet_size ** (level - 1)
                   * hit_by_time)
    return answer


def check_ballot_formula(maximum_time=18):
    for alphabet_size in (2, 3, 5):
        probabilities = (
            Fraction(1, 7),
            Fraction(1, alphabet_size + 1),
            Fraction(2, 5),
            Fraction(1, 2),
            Fraction(5, 7),
        )
        for pop_probability in probabilities:
            for time in range(maximum_time + 1):
                check(
                    annealed_degree_from_walk(time, pop_probability,
                                               alphabet_size)
                    == ballot_annealed_degree(time, pop_probability,
                                               alphabet_size),
                    f"ballot formula failed for b={alphabet_size}, "
                    f"p={pop_probability}, t={time}",
                )


def check_ballot_endpoints(maximum_time=20):
    """Check the direct endpoint laws as well as the finite ballot sum."""
    for alphabet_size in (2, 3, 5):
        for pop_probability in (Fraction(0), Fraction(1)):
            expected = Fraction(1)
            for time in range(maximum_time + 1):
                direct = annealed_degree_from_walk(
                    time, pop_probability, alphabet_size)
                ballot = ballot_annealed_degree(
                    time, pop_probability, alphabet_size)
                check(
                    direct == ballot,
                    f"endpoint ballot formula failed for b={alphabet_size}, "
                    f"p={pop_probability}, t={time}",
                )
                check(
                    direct == expected,
                    f"endpoint degree failed for b={alphabet_size}, "
                    f"p={pop_probability}, t={time}",
                )
                if pop_probability == 1:
                    expected *= alphabet_size


def reflected_moment_sequence(maximum_time, down_probability,
                              alphabet_size):
    """E[b^Y_t] for reflected Y: down toward zero vs. up away from zero."""
    up_probability = 1 - down_probability
    distribution = {0: Fraction(1)}
    moments = []
    for _ in range(maximum_time + 1):
        moments.append(sum(mass * alphabet_size ** state
                           for state, mass in distribution.items()))
        next_distribution = {}
        for state, mass in distribution.items():
            down_state = max(state - 1, 0)
            up_state = state + 1
            next_distribution[down_state] = (
                next_distribution.get(down_state, Fraction(0))
                + mass * down_probability
            )
            next_distribution[up_state] = (
                next_distribution.get(up_state, Fraction(0))
                + mass * up_probability
            )
        distribution = next_distribution
    return moments


def check_critical_tilt(maximum_time=40):
    for alphabet_size in (2, 3, 5):
        pop_probability = Fraction(1, alphabet_size + 1)
        push_probability = 1 - pop_probability
        tilted_pop = push_probability
        for time in range(maximum_time + 1):
            original = annealed_degree_from_walk(
                time, pop_probability, alphabet_size)
            tilted_maximum = expected_maximum(time, tilted_pop)
            claimed = (Fraction(1)
                       + Fraction(alphabet_size - 1, alphabet_size)
                       * tilted_maximum)
            check(original == claimed,
                  f"critical tilt failed for b={alphabet_size}, t={time}")


def check_supercritical_tilt(maximum_time=35):
    cases = (
        (2, Fraction(2, 5)),
        (2, Fraction(3, 5)),
        (3, Fraction(1, 3)),
        (3, Fraction(2, 3)),
        (5, Fraction(1, 4)),
        (5, Fraction(3, 4)),
    )
    for alphabet_size, pop_probability in cases:
        push_probability = 1 - pop_probability
        spectral_base = (alphabet_size * pop_probability
                         + push_probability / alphabet_size)
        check(spectral_base > 1,
              f"case is not supercritical: b={alphabet_size}, p={pop_probability}")
        tilted_pop = alphabet_size * pop_probability / spectral_base
        tilted_moments = reflected_moment_sequence(
            maximum_time, tilted_pop, alphabet_size)
        for time in range(maximum_time + 1):
            original = annealed_degree_from_walk(
                time, pop_probability, alphabet_size)
            check(original == spectral_base ** time * tilted_moments[time],
                  f"supercritical tilt failed for b={alphabet_size}, "
                  f"p={pop_probability}, t={time}")

        rho = push_probability / (pop_probability * alphabet_size ** 2)
        prefactor = (1 - rho) / (1 - alphabet_size * rho)
        check(rho < Fraction(1, alphabet_size),
              f"stationary b-moment diverges for b={alphabet_size}, "
              f"p={pop_probability}")
        check(prefactor * (1 - alphabet_size * rho) == 1 - rho,
              f"prefactor algebra failed for b={alphabet_size}, "
              f"p={pop_probability}")


def check_subcritical_and_threshold_algebra():
    for alphabet_size in (2, 3, 5):
        for pop_probability in (
                Fraction(1, 2 * (alphabet_size + 1)),
                Fraction(1, 3 * (alphabet_size + 1))):
            push_probability = 1 - pop_probability
            ratio = pop_probability / push_probability
            limit = (1 - ratio) / (1 - alphabet_size * ratio)
            spectral_base = (alphabet_size * pop_probability
                             + push_probability / alphabet_size)
            check(spectral_base < 1,
                  f"subcritical threshold failed for b={alphabet_size}")
            check(alphabet_size * ratio < 1,
                  f"terminal maximum moment should be finite for b={alphabet_size}")
            check(limit * (1 - alphabet_size * ratio) == 1 - ratio,
                  f"subcritical limit algebra failed for b={alphabet_size}")

        critical_probability = Fraction(1, alphabet_size + 1)
        critical_base = (alphabet_size * critical_probability
                         + (1 - critical_probability) / alphabet_size)
        coefficient = Fraction((alphabet_size - 1) ** 2,
                               alphabet_size * (alphabet_size + 1))
        tilted_drift = Fraction(alphabet_size - 1, alphabet_size + 1)
        check(critical_base == 1,
              f"critical base failed for b={alphabet_size}")
        check(coefficient
              == Fraction(alphabet_size - 1, alphabet_size) * tilted_drift,
              f"critical slope failed for b={alphabet_size}")


def check_symmetric_critical_distributions(maximum_time=40):
    counts = {(0, 0): 1}
    for time in range(maximum_time + 1):
        prefix_histogram = Counter()
        pop_histogram = Counter()
        for (walk, maximum), count in counts.items():
            prefix_histogram[maximum - walk] += count
            pop_histogram[maximum] += count
        check(prefix_histogram == pop_histogram,
              f"I and J laws differ at symmetric time {time}")
        check(sum(prefix_histogram.values()) == 2 ** time,
              f"symmetric mass mismatch at time {time}")

        next_counts = {}
        for (walk, maximum), count in counts.items():
            up = (walk + 1, max(maximum, walk + 1))
            down = (walk - 1, maximum)
            next_counts[up] = next_counts.get(up, 0) + count
            next_counts[down] = next_counts.get(down, 0) + count
        counts = next_counts


def rescaled_float_diagnostics(alphabet_size=2, maximum_time=400):
    cases = (
        (Fraction(1, 4), "subcritical-limit", 2.0),
        (Fraction(1, 3), "critical-linear-slope", 1.0 / 6.0),
        (Fraction(2, 5), "supercritical-prefactor", 2.5),
        (Fraction(1, 2), "symmetric-prefactor", 1.5),
    )
    rows = []
    for probability, label, target in cases:
        p = float(probability)
        q = 1.0 - p
        spectral_base = alphabet_size * p + q / alphabet_size
        scale = max(1.0, spectral_base)
        weighted = [1.0]
        total = 1.0
        for _ in range(maximum_time):
            next_weighted = [0.0] * (len(weighted) + 1)
            next_weighted[0] += p * alphabet_size * weighted[0] / scale
            for state in range(1, len(weighted)):
                next_weighted[state - 1] += p * weighted[state] / scale
            for state in range(len(weighted)):
                next_weighted[state + 1] += q * weighted[state] / scale
            weighted = next_weighted
            total = sum(weighted)

        value = total
        if label == "critical-linear-slope":
            value = total / maximum_time
        diagnostic_check(abs(value - target) < 0.01,
                         f"floating diagnostic failed for {label}")
        rows.append((label, value, target))

    symmetric_maximum = float(expected_maximum(maximum_time, Fraction(1, 2)))
    scaled_maximum = symmetric_maximum / sqrt(maximum_time)
    gaussian_target = sqrt(2.0 / pi)
    diagnostic_check(abs(scaled_maximum - gaussian_target) < 0.04,
                     "symmetric maximum scale diagnostic failed")
    rows.append(("symmetric-Emax/sqrt(t)", scaled_maximum, gaussian_target))
    return rows


def main():
    print("Random push--pop stack cocycle exact controls")
    check_running_maximum_normal_form()
    check_labeled_maps()
    check_image_and_fibres(alphabet_size=2, maximum_time=10)
    check_image_and_fibres(alphabet_size=3, maximum_time=7)
    check_ballot_formula()
    check_ballot_endpoints()
    check_critical_tilt()
    check_supercritical_tilt()
    check_subcritical_and_threshold_algebra()
    check_symmetric_critical_distributions()
    diagnostics = rescaled_float_diagnostics()

    print("J=M and I=M-S checked for every direction word through t=15")
    print("definition-level labeled maps checked for b=2 through t=9")
    print("image cylinders and constant fibre degrees checked for "
          "(b,t)=(2,10),(3,7)")
    print("ballot first-passage formula checked for b=2,3,5 through t=18")
    print("endpoint laws and ballot sums checked for p=0,1 through t=20")
    print("critical and supercritical change-of-measure identities checked "
          "through t=40 and t=35")
    print("symmetric I and J distributions checked through t=40")
    for label, value, target in diagnostics:
        print(f"diagnostic {label}: value={value:.12f}, target={target:.12f}")
    print(f"ALL DISCRETE EXACT CONTROLS PASSED ({ASSERTIONS:,} assertions; "
          f"{DIAGNOSTIC_CHECKS} floating diagnostics)")


if __name__ == "__main__":
    main()
