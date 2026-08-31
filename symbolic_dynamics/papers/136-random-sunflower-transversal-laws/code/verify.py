#!/usr/bin/env python3
"""Exact controls for P136.

The program is self-contained.  It uses integers and fractions.Fraction only:
no floating point, sampling, seed, network access, timestamp, or third-party
package.  Its stdout is frozen byte-for-byte in verification_output.txt.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def popcount(value):
    return value.bit_count()


def prod_int(values):
    result = 1
    for value in values:
        result *= value
    return result


def add_mass(counter, key, value):
    counter[key] += value
    if counter[key] == 0:
        del counter[key]


def aggregate(transitions):
    out = Counter()
    for target, probability in transitions:
        add_mass(out, target, probability)
    check(sum(out.values(), Fraction(0)) == 1, ("transition mass", transitions))
    return tuple(sorted(out.items(), key=lambda item: repr(item[0])))


def weighted_analyzer(successors):
    """Return exact terminal and discrete step-count laws."""

    @lru_cache(maxsize=None)
    def analyze(state):
        transitions = tuple(successors(state))
        if not transitions:
            return ((state, Fraction(1)),), ((0, Fraction(1)),)
        transitions = aggregate(transitions)
        terminal = Counter()
        clock = Counter()
        for target, probability in transitions:
            terminal_law, clock_law = analyze(target)
            for endpoint, mass in terminal_law:
                add_mass(terminal, endpoint, probability * mass)
            for steps, mass in clock_law:
                add_mass(clock, steps + 1, probability * mass)
        return (
            tuple(sorted(terminal.items(), key=lambda item: repr(item[0]))),
            tuple(sorted(clock.items())),
        )

    return analyze


def validate_laws(terminal_law, clock_law, tag):
    check(sum((mass for _, mass in terminal_law), Fraction(0)) == 1,
          (tag, "terminal"))
    check(sum((mass for _, mass in clock_law), Fraction(0)) == 1,
          (tag, "step count"))
    check(all(mass > 0 for _, mass in terminal_law),
          (tag, "terminal positive"))
    check(all(mass > 0 for _, mass in clock_law),
          (tag, "step count positive"))


def convolve(left, right):
    out = Counter()
    for i, a in left.items():
        for j, b in right.items():
            out[i + j] += a * b
    return out


def elementary(values, degree):
    coefficients = [Fraction(1)] + [Fraction(0)] * degree
    for value in values:
        for index in range(degree, 0, -1):
            coefficients[index] += value * coefficients[index - 1]
    return coefficients[degree]


def sunflower_successors(petals, core_size, rates=None):
    rates = tuple(1 for _ in petals) if rates is None else tuple(rates)

    def successors(state):
        mode, remaining, selected = state
        if mode:
            return ()
        if remaining == 0:
            return (((2, 0, selected), Fraction(1)),)
        active = [i for i in range(len(petals)) if remaining >> i & 1]
        total_rate = sum(rates[i] for i in active)
        transitions = []
        for i in active:
            denominator = total_rate * (core_size + petals[i])
            transitions.append(
                ((1, 0, selected),
                 Fraction(rates[i] * core_size, denominator))
            )
            next_remaining = remaining & ~(1 << i)
            next_selected = selected | (1 << i)
            next_mode = 2 if next_remaining == 0 else 0
            transitions.append(
                ((next_mode, next_remaining, next_selected),
                 Fraction(rates[i] * petals[i], denominator))
            )
        return transitions

    return successors


def stopping_tails(petals, core_size):
    m = len(petals)
    ratios = [Fraction(p, core_size + p) for p in petals]
    return [elementary(ratios, degree) / comb(m, degree)
            for degree in range(m + 1)]


def sunflower_clock_formula(petals, core_size):
    m = len(petals)
    tails = stopping_tails(petals, core_size)
    law = Counter()
    for steps in range(1, m):
        law[steps] = tails[steps - 1] - tails[steps]
    law[m] = tails[m - 1]
    return law


def sunflower_terminal_formula(petals, core_size):
    m = len(petals)
    all_mask = (1 << m) - 1
    r = [Fraction(p, core_size + p) for p in petals]
    q = [Fraction(core_size, core_size + p) for p in petals]
    law = Counter()
    for selected in range(1 << m):
        k = popcount(selected)
        if k == m:
            law[(2, 0, all_mask)] = prod_int(r)
            continue
        probability = Fraction(1, comb(m, k))
        for i in range(m):
            if selected >> i & 1:
                probability *= r[i]
        probability *= sum(q[i] for i in range(m)
                           if not (selected >> i & 1))
        probability /= m - k
        law[(1, 0, selected)] = probability
    return law


def sunflower_weighted_terminal_formula(petals, core_size, rates):
    m = len(petals)
    all_mask = (1 << m) - 1
    r = [Fraction(p, core_size + p) for p in petals]
    q = [Fraction(core_size, core_size + p) for p in petals]
    law = Counter()
    for selected in range(1 << m):
        if selected == all_mask:
            law[(2, 0, all_mask)] = prod_int(r)
            continue
        complement_rate = sum(
            rates[i] for i in range(m) if not (selected >> i & 1)
        )
        integral = Fraction(0)
        submask = selected
        while True:
            denominator = complement_rate + sum(
                rates[i] for i in range(m) if submask >> i & 1
            )
            integral += Fraction((-1) ** popcount(submask), denominator)
            if submask == 0:
                break
            submask = (submask - 1) & selected
        probability = integral
        for i in range(m):
            if selected >> i & 1:
                probability *= r[i]
        probability *= sum(
            q[j] * rates[j]
            for j in range(m) if not (selected >> j & 1)
        )
        law[(1, 0, selected)] = probability
    check(all(mass > 0 for mass in law.values()),
          ("weighted formula positive", petals, core_size, rates))
    check(sum(law.values(), Fraction(0)) == 1,
          ("weighted formula mass", petals, core_size, rates))
    return law


def sunflower_weighted_clock_formula(petals, core_size, rates):
    terminal = sunflower_weighted_terminal_formula(petals, core_size, rates)
    m = len(petals)
    clock = Counter()
    for endpoint, mass in terminal.items():
        mode, _, selected = endpoint
        steps = m if mode == 2 else popcount(selected) + 1
        clock[steps] += mass
    return clock


def sunflower_resolved_successors(petals, core_size):
    def successors(state):
        mode, remaining, selected, core_mark = state
        if mode:
            return ()
        if remaining == 0:
            return (((2, 0, selected, -1), Fraction(1)),)
        active = [i for i in range(len(petals)) if remaining >> i & 1]
        transitions = []
        for i in active:
            probability = Fraction(1, len(active) * (core_size + petals[i]))
            for mark in range(core_size):
                transitions.append(((1, 0, selected, mark), probability))
            for mark in range(petals[i]):
                next_selected = list(selected)
                next_selected[i] = mark
                next_remaining = remaining & ~(1 << i)
                next_mode = 2 if next_remaining == 0 else 0
                transitions.append(
                    ((next_mode, next_remaining, tuple(next_selected), -1),
                     probability)
                )
        return transitions

    return successors


def sunflower_resolved_formula(petals, core_size):
    aggregate_law = sunflower_terminal_formula(petals, core_size)
    m = len(petals)
    all_mask = (1 << m) - 1
    law = Counter()
    for endpoint, aggregate_mass in aggregate_law.items():
        mode, _, selected_mask = endpoint
        selected_indices = [i for i in range(m) if selected_mask >> i & 1]
        mark_spaces = [
            range(petals[i]) if i in selected_indices else (-1,)
            for i in range(m)
        ]
        if mode == 1:
            multiplicity = core_size * prod_int(
                petals[i] for i in selected_indices
            )
            for marks in product(*mark_spaces):
                for core_mark in range(core_size):
                    law[(1, 0, tuple(marks), core_mark)] += (
                        aggregate_mass / multiplicity
                    )
        else:
            check(selected_mask == all_mask,
                  ("resolved all petals", endpoint))
            multiplicity = prod_int(petals)
            for marks in product(*mark_spaces):
                law[(2, 0, tuple(marks), -1)] += (
                    aggregate_mass / multiplicity
                )
    return law


def sunflower_forest_successors(
    petals_left, core_left, petals_right, core_right,
    rates_left=None, rates_right=None,
):
    rates_left = (tuple(1 for _ in petals_left) if rates_left is None
                  else tuple(rates_left))
    rates_right = (tuple(1 for _ in petals_right) if rates_right is None
                   else tuple(rates_right))

    def successors(state):
        mode_l, rem_l, sel_l, mode_r, rem_r, sel_r = state
        if mode_l and mode_r:
            return ()
        active_l = ([i for i in range(len(petals_left)) if rem_l >> i & 1]
                    if not mode_l else [])
        active_r = ([i for i in range(len(petals_right)) if rem_r >> i & 1]
                    if not mode_r else [])
        total_rate = (sum(rates_left[i] for i in active_l)
                      + sum(rates_right[i] for i in active_r))
        transitions = []
        for side, active, petals, core, rates in (
            (0, active_l, petals_left, core_left, rates_left),
            (1, active_r, petals_right, core_right, rates_right),
        ):
            for i in active:
                denominator = total_rate * (core + petals[i])
                if side == 0:
                    transitions.append(
                        ((1, 0, sel_l, mode_r, rem_r, sel_r),
                         Fraction(rates[i] * core, denominator))
                    )
                    next_rem = rem_l & ~(1 << i)
                    next_mode = 2 if next_rem == 0 else 0
                    transitions.append(
                        ((next_mode, next_rem, sel_l | (1 << i),
                          mode_r, rem_r, sel_r),
                         Fraction(rates[i] * petals[i], denominator))
                    )
                else:
                    transitions.append(
                        ((mode_l, rem_l, sel_l, 1, 0, sel_r),
                         Fraction(rates[i] * core, denominator))
                    )
                    next_rem = rem_r & ~(1 << i)
                    next_mode = 2 if next_rem == 0 else 0
                    transitions.append(
                        ((mode_l, rem_l, sel_l, next_mode, next_rem,
                          sel_r | (1 << i)),
                         Fraction(rates[i] * petals[i], denominator))
                    )
        return transitions

    return successors


def run_controls():
    states = 0
    max_support = 0
    max_mean = Fraction(0)

    for m in range(1, 6):
        for core_size in range(1, 4):
            for petals in product(range(1, 5), repeat=m):
                analyze = weighted_analyzer(
                    sunflower_successors(petals, core_size)
                )
                initial = (0, (1 << m) - 1, 0)
                terminal_law, clock_law = analyze(initial)
                states += 1
                validate_laws(terminal_law, clock_law,
                              ("unit", core_size, petals))
                check(dict(terminal_law)
                      == sunflower_terminal_formula(petals, core_size),
                      ("unit endpoint", core_size, petals))
                check(dict(clock_law)
                      == sunflower_clock_formula(petals, core_size),
                      ("unit step count", core_size, petals))

                tails = stopping_tails(petals, core_size)
                mean = sum(steps * mass for steps, mass in clock_law)
                second = sum(steps * steps * mass
                             for steps, mass in clock_law)
                check(mean == sum(tails[:-1]),
                      ("tail mean", core_size, petals))
                check(second == sum((2 * t + 1) * tails[t]
                                    for t in range(m)),
                      ("tail second moment", core_size, petals))
                r = [Fraction(p, core_size + p) for p in petals]
                q = [Fraction(core_size, core_size + p) for p in petals]
                top_split = prod_int(r) + Fraction(1, m) * sum(
                    q[j] * prod_int(r[i] for i in range(m) if i != j)
                    for j in range(m)
                )
                check(top_split == dict(clock_law)[m]
                      == elementary(r, m - 1) / m,
                      ("top atom", core_size, petals))
                max_mean = max(max_mean, mean)
                max_support = max(max_support, len(terminal_law))

    forest_parameters = (
        ((1, 2), 1, (2, 3), 2),
        ((1, 3, 2), 2, (2, 1), 1),
        ((2, 4, 1), 3, (3, 2, 1), 2),
    )
    for left, core_left, right, core_right in forest_parameters:
        analyze = weighted_analyzer(
            sunflower_forest_successors(left, core_left, right, core_right)
        )
        initial = (0, (1 << len(left)) - 1, 0,
                   0, (1 << len(right)) - 1, 0)
        terminal_law, clock_law = analyze(initial)
        states += 1
        validate_laws(terminal_law, clock_law,
                      ("forest", left, right))
        local_left = sunflower_terminal_formula(left, core_left)
        local_right = sunflower_terminal_formula(right, core_right)
        predicted_terminal = Counter()
        for endpoint_left, mass_left in local_left.items():
            for endpoint_right, mass_right in local_right.items():
                predicted_terminal[endpoint_left + endpoint_right] += (
                    mass_left * mass_right
                )
        check(dict(terminal_law) == predicted_terminal,
              ("forest endpoint", left, right))
        predicted_clock = convolve(
            sunflower_clock_formula(left, core_left),
            sunflower_clock_formula(right, core_right),
        )
        check(dict(clock_law) == predicted_clock,
              ("forest step count", left, right))

    weighted_forest = ((1, 2), 1, (2, 1), 2, (1, 3), (2, 1))
    left, core_left, right, core_right, rates_left, rates_right = (
        weighted_forest
    )
    analyze = weighted_analyzer(
        sunflower_forest_successors(
            left, core_left, right, core_right, rates_left, rates_right
        )
    )
    initial = (0, (1 << len(left)) - 1, 0,
               0, (1 << len(right)) - 1, 0)
    terminal_law, clock_law = analyze(initial)
    states += 1
    validate_laws(terminal_law, clock_law,
                  ("weighted forest", weighted_forest))
    local_left = sunflower_weighted_terminal_formula(
        left, core_left, rates_left
    )
    local_right = sunflower_weighted_terminal_formula(
        right, core_right, rates_right
    )
    predicted_terminal = Counter()
    for endpoint_left, mass_left in local_left.items():
        for endpoint_right, mass_right in local_right.items():
            predicted_terminal[endpoint_left + endpoint_right] += (
                mass_left * mass_right
            )
    check(dict(terminal_law) == predicted_terminal,
          ("weighted forest endpoint", weighted_forest))
    predicted_clock = convolve(
        sunflower_weighted_clock_formula(left, core_left, rates_left),
        sunflower_weighted_clock_formula(right, core_right, rates_right),
    )
    check(dict(clock_law) == predicted_clock,
          ("weighted forest step count", weighted_forest))

    for m in range(1, 4):
        for core_size in range(1, 3):
            for petals in product(range(1, 4), repeat=m):
                analyze = weighted_analyzer(
                    sunflower_resolved_successors(petals, core_size)
                )
                initial = (0, (1 << m) - 1,
                           tuple(-1 for _ in petals), -1)
                terminal_law, clock_law = analyze(initial)
                states += 1
                validate_laws(terminal_law, clock_law,
                              ("resolved", core_size, petals))
                check(dict(terminal_law)
                      == sunflower_resolved_formula(petals, core_size),
                      ("actual vertices", core_size, petals))
                check(dict(clock_law)
                      == sunflower_clock_formula(petals, core_size),
                      ("resolved step count", core_size, petals))

    for m in range(1, 4):
        for core_size in range(1, 3):
            for petals in product(range(1, 4), repeat=m):
                for rates in product(range(1, 4), repeat=m):
                    analyze = weighted_analyzer(
                        sunflower_successors(petals, core_size, rates)
                    )
                    initial = (0, (1 << m) - 1, 0)
                    terminal_law, clock_law = analyze(initial)
                    states += 1
                    validate_laws(
                        terminal_law, clock_law,
                        ("weighted", core_size, petals, rates),
                    )
                    check(dict(terminal_law)
                          == sunflower_weighted_terminal_formula(
                              petals, core_size, rates
                          ),
                          ("weighted endpoint", core_size, petals, rates))
                    check(dict(clock_law)
                          == sunflower_weighted_clock_formula(
                              petals, core_size, rates
                          ),
                          ("weighted step count", core_size, petals, rates))

    return states, max_support, max_mean


def main():
    states, max_support, max_mean = run_controls()
    if states != 5812:
        raise AssertionError(("frozen input count", states))
    print("P136_RANDOM_SUNFLOWER_TRANSVERSAL_LAWS")
    print("arithmetic=fractions.Fraction; sampling=none; third_party=none")
    print(f"parameter_inputs={states}")
    print(f"exact_assertions={ASSERTIONS}")
    print("lanes=unit_aggregate:4092,weighted_aggregate:1638,"
          "unit_actual_vertices:78,two_component_forests:4")
    print(f"max_aggregate_support={max_support}")
    print(f"max_unit_mean={max_mean}")
    print("checks=weighted_endpoint,actual_vertices,uniform_step_count,top_atom,"
          "mean,second_moment,forest_endpoint,forest_step_count")
    print("status=PASS")


if __name__ == "__main__":
    main()
