#!/usr/bin/env python3
"""Second exact scout for genuinely stochastic finite dynamics.

Every probability is a fractions.Fraction.  The program uses no floating
point, sampling, third-party package, network access, seed, or timestamp.
Its deterministic stdout is intended to be frozen byte-for-byte.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


ASSERTIONS = 0
ROWS = []


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def record(handle, carrier, scope, states, signal, disposition, before):
    ROWS.append(
        (handle, carrier, scope, states, ASSERTIONS - before, disposition, signal)
    )


def popcount(value):
    return value.bit_count()


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
    """Exact terminal and clock laws for a strictly descending stochastic rule."""

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
    check(sum((mass for _, mass in terminal_law), Fraction(0)) == 1, (tag, "terminal"))
    check(sum((mass for _, mass in clock_law), Fraction(0)) == 1, (tag, "clock"))
    check(all(mass > 0 for _, mass in terminal_law), (tag, "terminal positive"))
    check(all(mass > 0 for _, mass in clock_law), (tag, "clock positive"))


def convolve(left, right):
    out = Counter()
    for i, a in left.items():
        for j, b in right.items():
            out[i + j] += a * b
    return out


def falling(value, length):
    out = 1
    for offset in range(length):
        out *= value - offset
    return out


def elementary(values, degree):
    coefficients = [1] + [0] * degree
    for value in values:
        for index in range(degree, 0, -1):
            coefficients[index] += value * coefficients[index - 1]
    return coefficients[degree]


# ---------------------------------------------------------------------------
# SF1: edge-first random transversal on a sunflower forest


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
                ((1, 0, selected), Fraction(rates[i] * core_size, denominator))
            )
            next_remaining = remaining & ~(1 << i)
            next_selected = selected | (1 << i)
            next_mode = 2 if next_remaining == 0 else 0
            transitions.append(
                (
                    (next_mode, next_remaining, next_selected),
                    Fraction(rates[i] * petals[i], denominator),
                )
            )
        return transitions

    return successors


def sunflower_clock_formula(petals, core_size):
    m = len(petals)
    ratios = [Fraction(p, core_size + p) for p in petals]
    tails = [Fraction(1)]
    for degree in range(1, m + 1):
        tails.append(elementary(ratios, degree) / comb(m, degree))
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
            probability = Fraction(1)
            for value in r:
                probability *= value
            law[(2, 0, all_mask)] = probability
            continue
        probability = Fraction(1, comb(m, k))
        for i in range(m):
            if selected >> i & 1:
                probability *= r[i]
        probability *= sum(q[i] for i in range(m) if not (selected >> i & 1))
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
            probability = Fraction(1)
            for value in r:
                probability *= value
            law[(2, 0, all_mask)] = probability
            continue
        complement_rate = sum(rates[i] for i in range(m) if not (selected >> i & 1))
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
    check(all(mass > 0 for mass in law.values()), ("SF1 weighted formula positive", petals, core_size, rates))
    check(sum(law.values(), Fraction(0)) == 1, ("SF1 weighted formula mass", petals, core_size, rates))
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
                    ((next_mode, next_remaining, tuple(next_selected), -1), probability)
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
        mark_spaces = [range(petals[i]) if i in selected_indices else (-1,) for i in range(m)]
        if mode == 1:
            multiplicity = core_size * prod_int(petals[i] for i in selected_indices)
            for marks in product(*mark_spaces):
                for core_mark in range(core_size):
                    law[(1, 0, tuple(marks), core_mark)] += aggregate_mass / multiplicity
        else:
            check(selected_mask == all_mask, ("SF1 resolved all petals", endpoint))
            multiplicity = prod_int(petals)
            for marks in product(*mark_spaces):
                law[(2, 0, tuple(marks), -1)] += aggregate_mass / multiplicity
    return law


def sunflower_forest_successors(
    petals_left, core_left, petals_right, core_right,
    rates_left=None, rates_right=None,
):
    rates_left = tuple(1 for _ in petals_left) if rates_left is None else tuple(rates_left)
    rates_right = tuple(1 for _ in petals_right) if rates_right is None else tuple(rates_right)

    def successors(state):
        mode_l, rem_l, sel_l, mode_r, rem_r, sel_r = state
        if mode_l and mode_r:
            return ()
        active_l = [i for i in range(len(petals_left)) if rem_l >> i & 1] if not mode_l else []
        active_r = [i for i in range(len(petals_right)) if rem_r >> i & 1] if not mode_r else []
        total_rate = sum(rates_left[i] for i in active_l) + sum(rates_right[i] for i in active_r)
        transitions = []
        for side, active, petals, core, rates in (
            (0, active_l, petals_left, core_left, rates_left),
            (1, active_r, petals_right, core_right, rates_right),
        ):
            for i in active:
                denominator = total_rate * (core + petals[i])
                if side == 0:
                    transitions.append(
                        (
                            (1, 0, sel_l, mode_r, rem_r, sel_r),
                            Fraction(rates[i] * core, denominator),
                        )
                    )
                    next_rem = rem_l & ~(1 << i)
                    next_mode = 2 if next_rem == 0 else 0
                    transitions.append(
                        (
                            (next_mode, next_rem, sel_l | (1 << i), mode_r, rem_r, sel_r),
                            Fraction(rates[i] * petals[i], denominator),
                        )
                    )
                else:
                    transitions.append(
                        (
                            (mode_l, rem_l, sel_l, 1, 0, sel_r),
                            Fraction(rates[i] * core, denominator),
                        )
                    )
                    next_rem = rem_r & ~(1 << i)
                    next_mode = 2 if next_rem == 0 else 0
                    transitions.append(
                        (
                            (mode_l, rem_l, sel_l, next_mode, next_rem, sel_r | (1 << i)),
                            Fraction(rates[i] * petals[i], denominator),
                        )
                    )
        return transitions

    return successors


def run_sf1():
    before = ASSERTIONS
    states = 0
    max_support = 0
    max_mean = Fraction(0)
    for m in range(1, 6):
        for core_size in range(1, 4):
            for petals in product(range(1, 5), repeat=m):
                analyze = weighted_analyzer(sunflower_successors(petals, core_size))
                initial = (0, (1 << m) - 1, 0)
                terminal_law, clock_law = analyze(initial)
                states += 1
                validate_laws(terminal_law, clock_law, ("SF1", core_size, petals))
                check(dict(terminal_law) == sunflower_terminal_formula(petals, core_size), ("SF1 terminal formula", core_size, petals))
                check(dict(clock_law) == sunflower_clock_formula(petals, core_size), ("SF1 clock formula", core_size, petals))
                mean = sum(steps * mass for steps, mass in clock_law)
                tails = sunflower_clock_formula(petals, core_size)
                check(mean == sum(steps * mass for steps, mass in tails.items()), ("SF1 mean", core_size, petals))
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
        initial = (0, (1 << len(left)) - 1, 0, 0, (1 << len(right)) - 1, 0)
        terminal_law, clock_law = analyze(initial)
        states += 1
        validate_laws(terminal_law, clock_law, ("SF1 forest", left, right))
        local_left = sunflower_terminal_formula(left, core_left)
        local_right = sunflower_terminal_formula(right, core_right)
        predicted_terminal = Counter()
        for endpoint_left, mass_left in local_left.items():
            for endpoint_right, mass_right in local_right.items():
                combined = endpoint_left + endpoint_right
                predicted_terminal[combined] += mass_left * mass_right
        actual_terminal = Counter()
        for endpoint, mass in terminal_law:
            combined = endpoint[:3] + endpoint[3:]
            actual_terminal[combined] += mass
        check(actual_terminal == predicted_terminal, ("SF1 forest terminal factor", left, right))
        predicted_clock = convolve(
            sunflower_clock_formula(left, core_left),
            sunflower_clock_formula(right, core_right),
        )
        check(dict(clock_law) == predicted_clock, ("SF1 forest clock factor", left, right))

    weighted_forest = ((1, 2), 1, (2, 1), 2, (1, 3), (2, 1))
    left, core_left, right, core_right, rates_left, rates_right = weighted_forest
    analyze = weighted_analyzer(
        sunflower_forest_successors(
            left, core_left, right, core_right, rates_left, rates_right
        )
    )
    initial = (0, (1 << len(left)) - 1, 0, 0, (1 << len(right)) - 1, 0)
    terminal_law, clock_law = analyze(initial)
    states += 1
    validate_laws(terminal_law, clock_law, ("SF1 weighted forest", weighted_forest))
    local_left = sunflower_weighted_terminal_formula(left, core_left, rates_left)
    local_right = sunflower_weighted_terminal_formula(right, core_right, rates_right)
    predicted_terminal = Counter()
    for endpoint_left, mass_left in local_left.items():
        for endpoint_right, mass_right in local_right.items():
            predicted_terminal[endpoint_left + endpoint_right] += mass_left * mass_right
    check(dict(terminal_law) == predicted_terminal, ("SF1 weighted forest endpoint", weighted_forest))
    predicted_clock = convolve(
        sunflower_weighted_clock_formula(left, core_left, rates_left),
        sunflower_weighted_clock_formula(right, core_right, rates_right),
    )
    check(dict(clock_law) == predicted_clock, ("SF1 weighted forest clock", weighted_forest))

    for m in range(1, 4):
        for core_size in range(1, 3):
            for petals in product(range(1, 4), repeat=m):
                analyze = weighted_analyzer(
                    sunflower_resolved_successors(petals, core_size)
                )
                initial = (0, (1 << m) - 1, tuple(-1 for _ in petals), -1)
                terminal_law, clock_law = analyze(initial)
                states += 1
                validate_laws(terminal_law, clock_law, ("SF1 resolved", core_size, petals))
                check(
                    dict(terminal_law) == sunflower_resolved_formula(petals, core_size),
                    ("SF1 vertex-resolved law", core_size, petals),
                )
                check(
                    dict(clock_law) == sunflower_clock_formula(petals, core_size),
                    ("SF1 resolved clock", core_size, petals),
                )

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
                    validate_laws(terminal_law, clock_law, ("SF1 weighted", core_size, petals, rates))
                    check(
                        dict(terminal_law)
                        == sunflower_weighted_terminal_formula(petals, core_size, rates),
                        ("SF1 weighted endpoint integral", core_size, petals, rates),
                    )
                    check(
                        dict(clock_law)
                        == sunflower_weighted_clock_formula(petals, core_size, rates),
                        ("SF1 weighted clock", core_size, petals, rates),
                    )

    record(
        "SF1",
        "disjoint sunflower hypergraphs / edge-first random transversal",
        "uniform c=1..3,m=1..5,p_i=1..4; weighted c<=2,m<=3,p_i,lambda_i<=3; three forests; resolved pilot",
        states,
        f"vertex-resolved endpoints, weighted exponential-race integrals, uniform elementary-symmetric clocks, and forest products all match; max aggregate support {max_support}, max mean {max_mean}",
        "PROMOTE_ONE_RESIDUAL_HOSTILE_GATE_REQUIRED",
        before,
    )


# ---------------------------------------------------------------------------
# MS1: repair a red-red and a blue-blue matching edge by a random 2-switch


def ms1_successors(matching, colour_boundary):
    red_edges = [
        index for index, (u, v) in enumerate(matching)
        if u < colour_boundary and v < colour_boundary
    ]
    blue_edges = [
        index for index, (u, v) in enumerate(matching)
        if u >= colour_boundary and v >= colour_boundary
    ]
    check(len(red_edges) == len(blue_edges), ("MS1 balance", matching, colour_boundary))
    if not red_edges:
        return ()
    transitions = []
    probability = Fraction(1, 2 * len(red_edges) * len(blue_edges))
    for red_index in red_edges:
        for blue_index in blue_edges:
            red = matching[red_index]
            blue = matching[blue_index]
            untouched = tuple(
                edge for index, edge in enumerate(matching)
                if index not in (red_index, blue_index)
            )
            for orientation in (0, 1):
                repaired = (
                    tuple(sorted((red[0], blue[orientation]))),
                    tuple(sorted((red[1], blue[1 - orientation]))),
                )
                transitions.append((tuple(sorted(untouched + repaired)), probability))
    return transitions


def run_ms1():
    before = ASSERTIONS
    states = 0
    max_support = 0
    for n in range(1, 7):
        def successors(matching):
            return ms1_successors(matching, n)

        analyze = weighted_analyzer(successors)
        for matching in perfect_matchings(range(2 * n)):
            states += 1
            bad_pairs = sum(u < n and v < n for u, v in matching)
            terminal_law, clock_law = analyze(matching)
            validate_laws(terminal_law, clock_law, ("MS1", n, matching))
            support = factorial(bad_pairs) * 2**bad_pairs
            check(len(terminal_law) == support, ("MS1 support", n, matching))
            check(all(mass == Fraction(1, support) for _, mass in terminal_law), ("MS1 uniform", n, matching))
            check(all(not successors(endpoint) for endpoint, _ in terminal_law), ("MS1 bipartite", n, matching))
            check(dict(clock_law) == {bad_pairs: Fraction(1)}, ("MS1 clock", n, matching))
            max_support = max(max_support, support)
    record(
        "MS1",
        "two-colour perfect matchings / random bad-pair 2-switch repair",
        "every perfect matching on n red and n blue vertices, n=1..6",
        states,
        f"from k red-red/blue-blue pairs the k! 2^k bipartite endpoints are exactly uniform; fixed k clock; max support {max_support}",
        "KILL_SWITCH_CHAIN_FACTORISATION_THIN",
        before,
    )


# ---------------------------------------------------------------------------
# PR1: independent random binary cuts refining a set partition


def set_partitions(n):
    out = []

    def generate(index, labels, maximum):
        if index == n:
            blocks = []
            for label in range(maximum + 1):
                block = sum(1 << i for i, value in enumerate(labels) if value == label)
                blocks.append(block)
            out.append(tuple(sorted(blocks)))
            return
        for label in range(maximum + 2):
            labels.append(label)
            generate(index + 1, labels, max(maximum, label))
            labels.pop()

    if n == 0:
        return ((),)
    generate(1, [0], 0)
    return tuple(out)


def refine_partition(partition, cut, full_mask):
    blocks = []
    for block in partition:
        for piece in (block & cut, block & (full_mask ^ cut)):
            if piece:
                blocks.append(piece)
    return tuple(sorted(blocks))


def partition_refines(target, source):
    return all(any(block & ~outer == 0 for outer in source) for block in target)


def run_pr1():
    before = ASSERTIONS
    states = 0
    kernel_checks = 0
    max_mean_numerator = 0
    for n in range(1, 6):
        partitions = set_partitions(n)
        full_mask = (1 << n) - 1
        discrete = tuple(1 << i for i in range(n))

        @lru_cache(maxsize=None)
        def expected_time(partition):
            if partition == discrete:
                return Fraction(0)
            transitions = Counter(
                refine_partition(partition, cut, full_mask) for cut in range(1 << n)
            )
            hold = transitions.pop(partition, 0)
            return (Fraction(1) + sum(Fraction(count, 1 << n) * expected_time(target) for target, count in transitions.items())) / (1 - Fraction(hold, 1 << n))

        for initial in partitions:
            states += 1
            distribution = Counter({initial: Fraction(1)})
            for time in range(0, 6):
                signatures = 1 << time
                for target in partitions:
                    if not partition_refines(target, initial):
                        continue
                    predicted = Fraction(1)
                    for block in initial:
                        target_blocks = sum(1 for piece in target if piece & ~block == 0)
                        predicted *= Fraction(falling(signatures, target_blocks), signatures ** popcount(block))
                    check(distribution[target] == predicted, ("PR1 kernel", n, initial, target, time))
                    kernel_checks += 1
                absorption = distribution[discrete]
                predicted_absorption = Fraction(1)
                for block in initial:
                    predicted_absorption *= Fraction(falling(signatures, popcount(block)), signatures ** popcount(block))
                check(absorption == predicted_absorption, ("PR1 absorption", n, initial, time))
                next_distribution = Counter()
                for current, mass in distribution.items():
                    for cut in range(1 << n):
                        next_distribution[refine_partition(current, cut, full_mask)] += mass / (1 << n)
                distribution = next_distribution
            mean = expected_time(initial)
            check(mean >= 0, ("PR1 mean", n, initial))
            max_mean_numerator = max(max_mean_numerator, mean.numerator)

    record(
        "PR1",
        "set partitions / simultaneous fair binary refinement",
        "every partition of [n], n=1..5; complete t=0..5 kernels",
        states,
        f"{kernel_checks} target probabilities equal independent signature-collision formula; exact Bellman means computed (max numerator {max_mean_numerator})",
        "KILL_RANDOM_TRIE_HASH_COLLISION_DIRECT",
        before,
    )


# ---------------------------------------------------------------------------
# PK1: random greedy packing in a finite 3-uniform hypergraph


def run_pk1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0
    hypergraphs = (
        (
            (0, 1, 2), (2, 3, 4), (4, 5, 0), (1, 3, 5),
            (0, 3, 4), (1, 4, 5), (2, 3, 5),
        ),
        (
            (0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 4, 0),
            (4, 5, 1), (5, 0, 2), (0, 2, 4), (1, 3, 5),
        ),
        (
            (0, 1, 2), (0, 3, 4), (1, 3, 5), (2, 4, 5),
            (0, 5, 6), (1, 4, 6), (2, 3, 6),
        ),
    )
    for edges in hypergraphs:
        edge_sets = tuple(frozenset(edge) for edge in edges)

        def successors(state):
            remaining, accepted = state
            if remaining == 0:
                return ()
            active = [i for i in range(len(edges)) if remaining >> i & 1]
            transitions = []
            for i in active:
                next_remaining = 0
                for j in active:
                    if edge_sets[i].isdisjoint(edge_sets[j]):
                        next_remaining |= 1 << j
                transitions.append(((next_remaining, accepted | (1 << i)), Fraction(1, len(active))))
            return transitions

        analyze = weighted_analyzer(successors)
        for family in range(1 << len(edges)):
            states += 1
            terminal_law, clock_law = analyze((family, 0))
            validate_laws(terminal_law, clock_law, ("PK1", edges, family))
            for endpoint, _ in terminal_law:
                _, accepted = endpoint
                chosen = [i for i in range(len(edges)) if accepted >> i & 1]
                check(all(edge_sets[i].isdisjoint(edge_sets[j]) for i, j in combinations(chosen, 2)), ("PK1 packing", edges, family, endpoint))
                check(all(any(not edge_sets[i].isdisjoint(edge_sets[j]) for j in chosen) for i in range(len(edges)) if family >> i & 1 and not (accepted >> i & 1)), ("PK1 maximal", edges, family, endpoint))
            multi_terminal += len(terminal_law) > 1
            variable_clock += len(clock_law) > 1
            max_support = max(max_support, len(terminal_law))
    record(
        "PK1",
        "3-uniform hypergraphs / uniform-edge greedy packing",
        "every subhypergraph of three named 7/8-edge 3-graphs",
        states,
        f"{multi_terminal} sources have multiple maximal packings and {variable_clock} have variable clocks; max support {max_support}",
        "KILL_RANDOM_SEQUENTIAL_ADSORPTION_SET_PACKING_OWNER",
        before,
    )


# ---------------------------------------------------------------------------
# TR1: choose a present triangle, then delete one of its edges uniformly


def graph_edges(n):
    return tuple(combinations(range(n), 2))


def run_tr1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0
    for n in (4, 5):
        edges = graph_edges(n)
        edge_index = {edge: i for i, edge in enumerate(edges)}
        triangles = tuple(
            tuple(edge_index[tuple(sorted(edge))] for edge in combinations(vertices, 2))
            for vertices in combinations(range(n), 3)
        )

        def successors(mask):
            active = [triangle for triangle in triangles if all(mask >> edge & 1 for edge in triangle)]
            if not active:
                return ()
            probability = Fraction(1, 3 * len(active))
            return tuple((mask & ~(1 << edge), probability) for triangle in active for edge in triangle)

        analyze = weighted_analyzer(successors)
        for mask in range(1 << len(edges)):
            states += 1
            terminal_law, clock_law = analyze(mask)
            validate_laws(terminal_law, clock_law, ("TR1", n, mask))
            check(all(not successors(endpoint) for endpoint, _ in terminal_law), ("TR1 triangle free", n, mask))
            multi_terminal += len(terminal_law) > 1
            variable_clock += len(clock_law) > 1
            max_support = max(max_support, len(terminal_law))
    record(
        "TR1",
        "simple graphs / random triangle-edge destruction",
        "all labelled graphs on n=4,5",
        states,
        f"{multi_terminal} sources have multiple triangle-free endpoints and {variable_clock} have variable clocks; max support {max_support}",
        "KILL_RANDOM_TRIANGLE_HITTING_NO_CLOSED_ATLAS",
        before,
    )


# ---------------------------------------------------------------------------
# ER1: choose a nonsingleton hyperedge, then erase a random incident vertex


def run_er1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0
    for n in (3, 4):
        edge_types = tuple(range(1, 1 << n))

        def successors(family):
            active = [i for i, edge in enumerate(edge_types) if family >> i & 1 and popcount(edge) >= 2]
            if not active:
                return ()
            transitions = []
            for i in active:
                edge = edge_types[i]
                for vertex in range(n):
                    if edge >> vertex & 1:
                        replacement = edge & ~(1 << vertex)
                        replacement_index = replacement - 1
                        target = (family & ~(1 << i)) | (1 << replacement_index)
                        transitions.append((target, Fraction(1, len(active) * popcount(edge))))
            return transitions

        analyze = weighted_analyzer(successors)
        families = range(1 << len(edge_types)) if n == 3 else (
            family
            for family in range(1 << len(edge_types))
            if popcount(family) <= 4
        )
        for family in families:
            states += 1
            terminal_law, clock_law = analyze(family)
            validate_laws(terminal_law, clock_law, ("ER1", n, family))
            check(all(all(popcount(edge_types[i]) == 1 for i in range(len(edge_types)) if endpoint >> i & 1) for endpoint, _ in terminal_law), ("ER1 singleton terminal", n, family))
            multi_terminal += len(terminal_law) > 1
            variable_clock += len(clock_law) > 1
            max_support = max(max_support, len(terminal_law))
    record(
        "ER1",
        "finite hypergraphs / edge-first random incidence erosion",
        "all families on [3]; all at-most-four-edge families on [4]",
        states,
        f"{multi_terminal} sources have multiple singleton-support endpoints and {variable_clock} have variable clocks; max support {max_support}",
        "KILL_GENERIC_FRAGMENTATION_WITH_MERGERS",
        before,
    )


# ---------------------------------------------------------------------------
# TM1: complete tripartite random greedy matching


def run_tm1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0

    def successors(state):
        a, b, c = state
        weights = ((0, 1, a * b), (0, 2, a * c), (1, 2, b * c))
        total = sum(weight for _, _, weight in weights)
        if total == 0:
            return ()
        transitions = []
        for i, j, weight in weights:
            if weight:
                target = list(state)
                target[i] -= 1
                target[j] -= 1
                transitions.append((tuple(target), Fraction(weight, total)))
        return transitions

    analyze = weighted_analyzer(successors)
    for state in product(range(7), repeat=3):
        states += 1
        terminal_law, clock_law = analyze(state)
        validate_laws(terminal_law, clock_law, ("TM1", state))
        check(all(sum(value > 0 for value in endpoint) <= 1 for endpoint, _ in terminal_law), ("TM1 terminal", state))
        check(all(sum(endpoint) % 2 == sum(state) % 2 for endpoint, _ in terminal_law), ("TM1 parity", state))
        multi_terminal += len(terminal_law) > 1
        variable_clock += len(clock_law) > 1
        max_support = max(max_support, len(terminal_law))
    record(
        "TM1",
        "complete tripartite graphs / uniform-edge greedy matching",
        "all part-count states (a,b,c) in {0,...,6}^3",
        states,
        f"{multi_terminal} sources have multiple residual species and {variable_clock} have variable matching size; max support {max_support}",
        "KILL_MULTISPECIES_ANNIHILATION_RSA_OWNER",
        before,
    )


# ---------------------------------------------------------------------------
# CE1: size-biased winner, uniform opposing loser in a conflict clique


def run_ce1():
    before = ASSERTIONS
    states = 0
    max_denominator = 1
    for n in range(2, 6):
        for weights in product(range(1, 4), repeat=n):
            def successors(active):
                indices = [i for i in range(n) if active >> i & 1]
                if len(indices) <= 1:
                    return ()
                total_weight = sum(weights[i] for i in indices)
                transitions = []
                for winner in indices:
                    for loser in indices:
                        if loser != winner:
                            transitions.append(
                                (
                                    active & ~(1 << loser),
                                    Fraction(weights[winner], total_weight * (len(indices) - 1)),
                                )
                            )
                return transitions

            analyze = weighted_analyzer(successors)
            for active in range(1, 1 << n):
                states += 1
                terminal_law, clock_law = analyze(active)
                validate_laws(terminal_law, clock_law, ("CE1", weights, active))
                total_weight = sum(weights[i] for i in range(n) if active >> i & 1)
                predicted = {
                    1 << i: Fraction(weights[i], total_weight)
                    for i in range(n) if active >> i & 1
                }
                check(dict(terminal_law) == predicted, ("CE1 survivor", weights, active))
                check(dict(clock_law) == {popcount(active) - 1: Fraction(1)}, ("CE1 clock", weights, active))
                max_denominator = max(max_denominator, *(mass.denominator for mass in predicted.values()))
    record(
        "CE1",
        "weighted conflict cliques / size-biased winner elimination",
        "all weights in {1,2,3}^n and all nonempty states, n=2..5",
        states,
        f"survivor i has exact mass w_i/sum(w) for every state; fixed |S|-1 clock; max denominator {max_denominator}",
        "KILL_LUCE_MARTINGALE_ONE_LEMMA_THIN",
        before,
    )


# ---------------------------------------------------------------------------
# CH1: choose an induced chordless cycle, then add a uniform missing chord


def run_ch1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0
    for n in (4, 5):
        edges = graph_edges(n)
        edge_index = {edge: i for i, edge in enumerate(edges)}
        candidate_vertex_sets = tuple(
            sum(1 << vertex for vertex in subset)
            for size in range(4, n + 1)
            for subset in combinations(range(n), size)
        )

        def induced_cycle(graph, vertex_mask):
            vertices = [vertex for vertex in range(n) if vertex_mask >> vertex & 1]
            adjacency = {vertex: set() for vertex in vertices}
            for u, v in combinations(vertices, 2):
                if graph >> edge_index[(u, v)] & 1:
                    adjacency[u].add(v)
                    adjacency[v].add(u)
            if not all(len(adjacency[vertex]) == 2 for vertex in vertices):
                return False
            seen = {vertices[0]}
            stack = [vertices[0]]
            while stack:
                current = stack.pop()
                for neighbor in adjacency[current]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            return len(seen) == len(vertices)

        def successors(graph):
            active = [
                vertex_mask for vertex_mask in candidate_vertex_sets
                if induced_cycle(graph, vertex_mask)
            ]
            if not active:
                return ()
            transitions = []
            for vertex_mask in active:
                vertices = [vertex for vertex in range(n) if vertex_mask >> vertex & 1]
                chords = [
                    edge_index[(u, v)] for u, v in combinations(vertices, 2)
                    if not (graph >> edge_index[(u, v)] & 1)
                ]
                check(chords, ("CH1 chordless cycle has chord", n, graph, vertex_mask))
                for chord in chords:
                    transitions.append(
                        (graph | (1 << chord), Fraction(1, len(active) * len(chords)))
                    )
            return transitions

        analyze = weighted_analyzer(successors)
        for graph in range(1 << len(edges)):
            states += 1
            terminal_law, clock_law = analyze(graph)
            validate_laws(terminal_law, clock_law, ("CH1", n, graph))
            check(all(not successors(endpoint) for endpoint, _ in terminal_law), ("CH1 chordal", n, graph))
            check(all(endpoint | graph == endpoint for endpoint, _ in terminal_law), ("CH1 supergraph", n, graph))
            multi_terminal += len(terminal_law) > 1
            variable_clock += len(clock_law) > 1
            max_support = max(max_support, len(terminal_law))
    record(
        "CH1",
        "simple graphs / random induced-cycle chordal fill",
        "every labelled graph on n=4,5",
        states,
        f"{multi_terminal} sources have multiple chordal completions and {variable_clock} have variable fill clocks; max support {max_support}",
        "KILL_MINIMUM_FILL_HEURISTIC_NO_CLOSED_ATLAS",
        before,
    )


def prod_int(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


# ---------------------------------------------------------------------------
# CT1: random thinning of crossing chords


def perfect_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        return ((),)
    first = vertices[0]
    out = []
    for index in range(1, len(vertices)):
        second = vertices[index]
        remainder = vertices[1:index] + vertices[index + 1:]
        for matching in perfect_matchings(remainder):
            out.append(tuple(sorted(((first, second),) + matching)))
    return tuple(out)


def chords_cross(left, right):
    a, b = left
    c, d = right
    return (a < c < b < d) or (c < a < d < b)


def ct_successors(chords):
    active = [(i, j) for i, j in combinations(range(len(chords)), 2) if chords_cross(chords[i], chords[j])]
    if not active:
        return ()
    probability = Fraction(1, 2 * len(active))
    return tuple(
        (tuple(chord for k, chord in enumerate(chords) if k != deleted), probability)
        for i, j in active for deleted in (i, j)
    )


def run_ct1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0
    analyze = weighted_analyzer(ct_successors)
    for n in range(1, 6):
        for matching in perfect_matchings(range(2 * n)):
            states += 1
            terminal_law, clock_law = analyze(matching)
            validate_laws(terminal_law, clock_law, ("CT1", matching))
            check(all(not ct_successors(endpoint) for endpoint, _ in terminal_law), ("CT1 noncrossing", matching))
            multi_terminal += len(terminal_law) > 1
            variable_clock += len(clock_law) > 1
            max_support = max(max_support, len(terminal_law))
    record(
        "CT1",
        "circle chord matchings / crossing-pair random thinning",
        "every perfect matching on 2n cyclic points, n=1..5",
        states,
        f"{multi_terminal} sources have multiple noncrossing submatchings and {variable_clock} have variable clocks; max support {max_support}",
        "KILL_INTERNAL_P130_COLLISION_AND_NO_LAW",
        before,
    )


# ---------------------------------------------------------------------------
# DC1: random deletion/contraction with every original edge processed once


def canonical_partition(blocks):
    return tuple(sorted(blocks))


def merge_partition(partition, u, v):
    block_u = next(block for block in partition if block >> u & 1)
    block_v = next(block for block in partition if block >> v & 1)
    if block_u == block_v:
        return partition
    return canonical_partition(
        tuple(block for block in partition if block not in (block_u, block_v))
        + (block_u | block_v,)
    )


def component_partition(n, edges, selected):
    blocks = [1 << i for i in range(n)]
    partition = tuple(blocks)
    for index, (u, v) in enumerate(edges):
        if selected >> index & 1:
            partition = merge_partition(partition, u, v)
    return partition


def run_dc1():
    before = ASSERTIONS
    states = 0
    max_support = 0
    for n in (3, 4):
        edges = graph_edges(n)
        singleton_partition = tuple(1 << i for i in range(n))
        for graph in range(1 << len(edges)):
            def successors(state):
                partition, remaining = state
                if remaining == 0:
                    return ()
                active = [i for i in range(len(edges)) if remaining >> i & 1]
                probability = Fraction(1, 2 * len(active))
                transitions = []
                for i in active:
                    next_remaining = remaining & ~(1 << i)
                    transitions.append(((partition, next_remaining), probability))
                    u, v = edges[i]
                    transitions.append(((merge_partition(partition, u, v), next_remaining), probability))
                return transitions

            analyze = weighted_analyzer(successors)
            initial = (singleton_partition, graph)
            terminal_law, clock_law = analyze(initial)
            states += 1
            validate_laws(terminal_law, clock_law, ("DC1", n, graph))
            predicted = Counter()
            edge_indices = [i for i in range(len(edges)) if graph >> i & 1]
            for kept_bits in range(1 << len(edge_indices)):
                kept = sum(1 << edge_indices[j] for j in range(len(edge_indices)) if kept_bits >> j & 1)
                predicted[(component_partition(n, edges, kept), 0)] += Fraction(1, 1 << len(edge_indices))
            check(dict(terminal_law) == predicted, ("DC1 percolation", n, graph))
            check(dict(clock_law) == {popcount(graph): Fraction(1)}, ("DC1 clock", n, graph))
            max_support = max(max_support, len(terminal_law))
    record(
        "DC1",
        "labelled graphs / fair deletion-contraction exposure",
        "every graph on n=3,4 from the singleton partition",
        states,
        f"terminal partition is exactly the component partition of Bernoulli(1/2) bond percolation; fixed edge clock; max support {max_support}",
        "KILL_RANDOM_CLUSTER_TUTTE_DIRECT_OWNER",
        before,
    )


# ---------------------------------------------------------------------------
# CN1: literal-first random short-circuiting of disjoint satisfying clauses


def negative_hypergeometric_clock(false_count, true_count):
    law = Counter()
    total = comb(false_count + true_count, true_count)
    for steps in range(1, false_count + 2):
        law[steps] = Fraction(
            comb(false_count + true_count - steps, true_count - 1), total
        )
    return law


def run_cn1():
    before = ASSERTIONS
    states = 0
    max_clock_support = 0
    clause_types = ((0, 1), (1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (1, 3))
    for number in range(1, 5):
        for clauses in product(clause_types, repeat=number):
            def successors(state):
                total = sum(false_count + true_count for false_count, true_count in state)
                if total == 0:
                    return ()
                transitions = []
                for i, (false_count, true_count) in enumerate(state):
                    if false_count:
                        target = list(state)
                        target[i] = (false_count - 1, true_count)
                        transitions.append((tuple(target), Fraction(false_count, total)))
                    if true_count:
                        target = list(state)
                        target[i] = (0, 0)
                        transitions.append((tuple(target), Fraction(true_count, total)))
                return transitions

            analyze = weighted_analyzer(successors)
            terminal_law, clock_law = analyze(tuple(clauses))
            states += 1
            validate_laws(terminal_law, clock_law, ("CN1", clauses))
            check(len(terminal_law) == 1 and terminal_law[0][0] == tuple((0, 0) for _ in clauses), ("CN1 terminal", clauses))
            predicted = Counter({0: Fraction(1)})
            for false_count, true_count in clauses:
                predicted = convolve(predicted, negative_hypergeometric_clock(false_count, true_count))
            check(dict(clock_law) == predicted, ("CN1 convolution", clauses))
            max_clock_support = max(max_clock_support, len(clock_law))
    record(
        "CN1",
        "read-once monotone CNF / random literal short-circuit",
        "all ordered 1..4-clause formulas from seven (false,true)-types",
        states,
        f"query clock is the convolution of independent negative-hypergeometric first-success laws; max support {max_clock_support}",
        "KILL_RANDOM_EVALUATION_NEGATIVE_HYPERGEOMETRIC_DIRECT",
        before,
    )


# ---------------------------------------------------------------------------
# CR1: delete a uniform clause until the signed CNF first becomes satisfiable


def run_cr1():
    before = ASSERTIONS
    states = 0
    unsatisfiable = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0
    clauses = tuple(vector for vector in product((-1, 0, 1), repeat=2) if any(vector))

    def satisfiable(formula):
        for assignment in product((False, True), repeat=2):
            if all(
                any(
                    sign and assignment[variable] == (sign == 1)
                    for variable, sign in enumerate(clause)
                )
                for clause_index, clause in enumerate(clauses)
                if formula >> clause_index & 1
            ):
                return True
        return False

    def successors(formula):
        if satisfiable(formula):
            return ()
        active = [i for i in range(len(clauses)) if formula >> i & 1]
        return tuple((formula & ~(1 << i), Fraction(1, len(active))) for i in active)

    analyze = weighted_analyzer(successors)
    for formula in range(1 << len(clauses)):
        states += 1
        unsatisfiable += not satisfiable(formula)
        terminal_law, clock_law = analyze(formula)
        validate_laws(terminal_law, clock_law, ("CR1", formula))
        check(all(satisfiable(endpoint) for endpoint, _ in terminal_law), ("CR1 satisfiable", formula))
        multi_terminal += len(terminal_law) > 1
        variable_clock += len(clock_law) > 1
        max_support = max(max_support, len(terminal_law))
    record(
        "CR1",
        "two-variable signed CNFs / uniform clause relaxation",
        "all 256 formulas over the eight non-tautological clause types",
        states,
        f"{unsatisfiable} unsatisfiable starts; {multi_terminal} multi-endpoint and {variable_clock} variable-clock sources; max support {max_support}",
        "KILL_RANDOM_RELAXATION_NO_FACTORISATION",
        before,
    )


# ---------------------------------------------------------------------------
# AP1: choose an augmenting path uniformly and flip it


def matching_masks(n, edges):
    out = []
    for mask in range(1 << len(edges)):
        used = 0
        valid = True
        for i, (u, v) in enumerate(edges):
            if mask >> i & 1:
                if used >> u & 1 or used >> v & 1:
                    valid = False
                    break
                used |= (1 << u) | (1 << v)
        if valid:
            out.append(mask)
    return tuple(out)


def augmenting_paths(n, edges, matching):
    adjacency = [[] for _ in range(n)]
    matched_vertices = 0
    for index, (u, v) in enumerate(edges):
        adjacency[u].append((v, index))
        adjacency[v].append((u, index))
        if matching >> index & 1:
            matched_vertices |= (1 << u) | (1 << v)
    paths = set()

    def explore(vertices, edge_path):
        current = vertices[-1]
        need_matched = len(edge_path) % 2 == 1
        for neighbor, edge_index in adjacency[current]:
            if neighbor in vertices:
                continue
            is_matched = bool(matching >> edge_index & 1)
            if is_matched != need_matched:
                continue
            next_vertices = vertices + (neighbor,)
            next_edges = edge_path + (edge_index,)
            if len(next_edges) % 2 == 1 and not (matched_vertices >> neighbor & 1):
                canonical = min(next_vertices, tuple(reversed(next_vertices)))
                path_mask = sum(1 << edge for edge in next_edges)
                paths.add((canonical, path_mask))
            elif len(next_edges) < n - 1:
                explore(next_vertices, next_edges)

    for start in range(n):
        if not (matched_vertices >> start & 1):
            explore((start,), ())
    return tuple(sorted(path_mask for _, path_mask in paths))


def run_ap1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    max_support = 0
    named_graphs = (
        (5, tuple((u, v) for u in range(2) for v in range(2, 5))),
        (6, tuple(tuple(sorted(edge)) for edge in ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 3), (1, 4)))),
        (4, graph_edges(4)),
    )
    for n, edges in named_graphs:
        edges = tuple(dict.fromkeys(edges))
        matchings = matching_masks(n, edges)
        maximum = max(popcount(mask) for mask in matchings)

        def successors(matching):
            paths = augmenting_paths(n, edges, matching)
            if not paths:
                return ()
            return tuple((matching ^ path, Fraction(1, len(paths))) for path in paths)

        analyze = weighted_analyzer(successors)
        for matching in matchings:
            states += 1
            terminal_law, clock_law = analyze(matching)
            validate_laws(terminal_law, clock_law, ("AP1", n, edges, matching))
            check(all(popcount(endpoint) == maximum for endpoint, _ in terminal_law), ("AP1 maximum", n, matching))
            check(dict(clock_law) == {maximum - popcount(matching): Fraction(1)}, ("AP1 clock", n, matching))
            multi_terminal += len(terminal_law) > 1
            max_support = max(max_support, len(terminal_law))
    record(
        "AP1",
        "finite matchings / uniform augmenting-path flips",
        "every matching of K_2,3, an 8-edge six-vertex graph, and K_4",
        states,
        f"Berge termination and fixed deficiency clock exact; {multi_terminal} sources reach multiple maximum matchings, max support {max_support}",
        "KILL_RANDOMISED_MATCHING_ALGORITHM_DIRECT",
        before,
    )


# ---------------------------------------------------------------------------
# DG1: choose a directed cycle, then delete a uniform arc on it


def directed_arc_data(n):
    arcs = tuple((u, v) for u in range(n) for v in range(n) if u != v)
    index = {arc: i for i, arc in enumerate(arcs)}
    cycles = set()
    for length in range(2, n + 1):
        for vertices in permutations(range(n), length):
            if vertices[0] != min(vertices):
                continue
            mask = 0
            for i in range(length):
                mask |= 1 << index[(vertices[i], vertices[(i + 1) % length])]
            cycles.add((mask, length))
    return arcs, tuple(sorted(cycles))


def run_dg1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0
    for n in (3, 4):
        arcs, cycles = directed_arc_data(n)

        def successors(graph):
            active = [(mask, length) for mask, length in cycles if graph & mask == mask]
            if not active:
                return ()
            transitions = []
            for cycle_mask, length in active:
                for edge in range(len(arcs)):
                    if cycle_mask >> edge & 1:
                        transitions.append((graph & ~(1 << edge), Fraction(1, len(active) * length)))
            return transitions

        analyze = weighted_analyzer(successors)
        if n == 3:
            graphs = tuple(range(1 << len(arcs)))
        else:
            graphs = tuple(
                graph for graph in range(1 << len(arcs)) if popcount(graph) <= 5
            ) + ((1 << len(arcs)) - 1,)
        for graph in graphs:
            states += 1
            terminal_law, clock_law = analyze(graph)
            validate_laws(terminal_law, clock_law, ("DG1", n, graph))
            check(all(not successors(endpoint) for endpoint, _ in terminal_law), ("DG1 acyclic", n, graph))
            multi_terminal += len(terminal_law) > 1
            variable_clock += len(clock_law) > 1
            max_support = max(max_support, len(terminal_law))
    record(
        "DG1",
        "directed graphs / random cycle-arc breaking",
        "all digraphs on n=3; all at-most-five-arc digraphs and the complete digraph on n=4",
        states,
        f"{multi_terminal} starts have multiple DAG endpoints and {variable_clock} have variable clocks; max support {max_support}",
        "KILL_FEEDBACK_ARC_HEURISTIC_NO_EXACT_ATLAS",
        before,
    )


# ---------------------------------------------------------------------------
# SC1: choose an elementary free-face collapse uniformly


def simplicial_complexes(n):
    faces = tuple(range(1, 1 << n))
    out = []
    for complex_mask in range(1 << len(faces)):
        valid = True
        for i, face in enumerate(faces):
            if not (complex_mask >> i & 1):
                continue
            subface = face
            while subface:
                if not (complex_mask >> (subface - 1) & 1):
                    valid = False
                    break
                subface = (subface - 1) & face
            if not valid:
                break
        if valid:
            out.append(complex_mask)
    return tuple(out)


def euler_characteristic(complex_mask):
    return sum(
        (-1) ** (popcount(face) - 1)
        for face in range(1, complex_mask.bit_length() + 1)
        if complex_mask >> (face - 1) & 1
    )


def sc_successors(complex_mask):
    present = [face for face in range(1, complex_mask.bit_length() + 1) if complex_mask >> (face - 1) & 1]
    active = []
    for tau in present:
        if popcount(tau) < 2:
            continue
        for vertex in range(tau.bit_length()):
            if not (tau >> vertex & 1):
                continue
            sigma = tau & ~(1 << vertex)
            cofaces = [face for face in present if face != sigma and face & sigma == sigma]
            if cofaces == [tau]:
                active.append((sigma, tau))
    if not active:
        return ()
    probability = Fraction(1, len(active))
    return tuple((complex_mask & ~(1 << (sigma - 1)) & ~(1 << (tau - 1)), probability) for sigma, tau in active)


def run_sc1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0
    analyze = weighted_analyzer(sc_successors)
    for n in range(1, 5):
        for complex_mask in simplicial_complexes(n):
            states += 1
            terminal_law, clock_law = analyze(complex_mask)
            validate_laws(terminal_law, clock_law, ("SC1", n, complex_mask))
            initial_euler = euler_characteristic(complex_mask)
            check(all(euler_characteristic(endpoint) == initial_euler for endpoint, _ in terminal_law), ("SC1 Euler", n, complex_mask))
            check(all(not sc_successors(endpoint) for endpoint, _ in terminal_law), ("SC1 core", n, complex_mask))
            multi_terminal += len(terminal_law) > 1
            variable_clock += len(clock_law) > 1
            max_support = max(max_support, len(terminal_law))
    record(
        "SC1",
        "finite simplicial complexes / uniform elementary collapse",
        "every labelled complex on n=1..4 vertices",
        states,
        f"Euler characteristic is pathwise invariant; {multi_terminal} multi-core and {variable_clock} variable-clock sources; max support {max_support}",
        "KILL_SIMPLE_HOMOTOPY_OWNER_AND_NO_TERMINAL_LAW",
        before,
    )


# ---------------------------------------------------------------------------
# BF3: choose an essential Boolean variable, then assign a fair bit


def restrict_boolean(mask, variables, chosen, bit):
    remaining = variables - 1
    out = 0
    for assignment in range(1 << remaining):
        low = assignment & ((1 << chosen) - 1)
        high = assignment >> chosen
        original = low | (bit << chosen) | (high << (chosen + 1))
        if mask >> original & 1:
            out |= 1 << assignment
    return out


def bf3_successors(state):
    variables, mask = state
    if mask == 0 or mask == (1 << (1 << variables)) - 1:
        return ()
    essential = [
        variable
        for variable in range(variables)
        if restrict_boolean(mask, variables, variable, 0)
        != restrict_boolean(mask, variables, variable, 1)
    ]
    check(essential, ("BF3 nonconstant essential", state))
    probability = Fraction(1, 2 * len(essential))
    return tuple(
        ((variables - 1, restrict_boolean(mask, variables, variable, bit)), probability)
        for variable in essential for bit in (0, 1)
    )


def run_bf3():
    before = ASSERTIONS
    states = 0
    variable_clock = 0
    max_clock_support = 0
    analyze = weighted_analyzer(bf3_successors)
    for variables in range(0, 5):
        for mask in range(1 << (1 << variables)):
            states += 1
            terminal_law, clock_law = analyze((variables, mask))
            validate_laws(terminal_law, clock_law, ("BF3", variables, mask))
            one_mass = sum(
                mass for endpoint, mass in terminal_law
                if endpoint[1] == (1 << (1 << endpoint[0])) - 1
            )
            check(one_mass == Fraction(popcount(mask), 1 << variables), ("BF3 bias martingale", variables, mask))
            check(all(endpoint[1] in (0, (1 << (1 << endpoint[0])) - 1) for endpoint, _ in terminal_law), ("BF3 constant", variables, mask))
            variable_clock += len(clock_law) > 1
            max_clock_support = max(max_clock_support, len(clock_law))
    record(
        "BF3",
        "Boolean functions / fair restriction of a uniform essential variable",
        "every truth table on n=0..4 variables",
        states,
        f"terminal-one mass equals truth-table bias for every function; {variable_clock} variable-clock functions, max clock support {max_clock_support}",
        "KILL_DECISION_TREE_RESTRICTION_MARTINGALE_THIN",
        before,
    )


# ---------------------------------------------------------------------------
# LM1: choose two crossing sets and delete one uniformly


def sets_cross(left, right):
    return bool(left & right) and bool(left & ~right) and bool(right & ~left)


def run_lm1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0
    for n in (3, 4):
        set_types = tuple(range(1, 1 << n))

        def successors(family):
            active = [(i, j) for i, j in combinations(range(len(set_types)), 2) if family >> i & 1 and family >> j & 1 and sets_cross(set_types[i], set_types[j])]
            if not active:
                return ()
            probability = Fraction(1, 2 * len(active))
            return tuple((family & ~(1 << deleted), probability) for i, j in active for deleted in (i, j))

        analyze = weighted_analyzer(successors)
        families = range(1 << len(set_types)) if n == 3 else (
            family for family in range(1 << len(set_types)) if popcount(family) <= 5
        )
        for family in families:
            states += 1
            terminal_law, clock_law = analyze(family)
            validate_laws(terminal_law, clock_law, ("LM1", n, family))
            check(all(not successors(endpoint) for endpoint, _ in terminal_law), ("LM1 laminar", n, family))
            multi_terminal += len(terminal_law) > 1
            variable_clock += len(clock_law) > 1
            max_support = max(max_support, len(terminal_law))
    record(
        "LM1",
        "set systems / crossing-pair random laminarisation",
        "all families on [3]; all at-most-five-set families on [4]",
        states,
        f"{multi_terminal} sources have multiple laminar endpoints and {variable_clock} have variable clocks; max support {max_support}",
        "KILL_ARBITRARY_LAMINARISATION_NO_FACTORISATION",
        before,
    )


# ---------------------------------------------------------------------------
# GV1: induced-P3 vertex deletion until a cluster graph remains


def run_gv1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0
    n = 5
    edges = graph_edges(n)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    triples = tuple(combinations(range(n), 3))
    for graph in range(1 << len(edges)):
        def induced_p3(vertices):
            count = 0
            for u, v in combinations(vertices, 2):
                count += bool(graph >> edge_index[(u, v)] & 1)
            return count == 2

        def successors(active_vertices):
            active = [triple for triple in triples if all(active_vertices >> vertex & 1 for vertex in triple) and induced_p3(triple)]
            if not active:
                return ()
            probability = Fraction(1, 3 * len(active))
            return tuple((active_vertices & ~(1 << vertex), probability) for triple in active for vertex in triple)

        analyze = weighted_analyzer(successors)
        for active_vertices in range(1 << n):
            states += 1
            terminal_law, clock_law = analyze(active_vertices)
            validate_laws(terminal_law, clock_law, ("GV1", graph, active_vertices))
            check(all(not successors(endpoint) for endpoint, _ in terminal_law), ("GV1 cluster", graph, active_vertices))
            multi_terminal += len(terminal_law) > 1
            variable_clock += len(clock_law) > 1
            max_support = max(max_support, len(terminal_law))
    record(
        "GV1",
        "induced subgraphs / random P3-witness vertex deletion",
        "every induced state of every labelled graph on five vertices",
        states,
        f"{multi_terminal} sources have multiple cluster-graph endpoints and {variable_clock} have variable clocks; max support {max_support}",
        "KILL_CLUSTER_DELETION_HEURISTIC_NO_CLOSED_LAW",
        before,
    )


# ---------------------------------------------------------------------------
# CF1: choose an odd cycle and delete one of its vertices uniformly


def undirected_cycle_data(n):
    edges = graph_edges(n)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    cycles = set()
    for length in range(3, n + 1, 2):
        for vertices in permutations(range(n), length):
            if vertices[0] != min(vertices) or vertices[1] > vertices[-1]:
                continue
            edge_mask = 0
            vertex_mask = 0
            for i in range(length):
                u, v = sorted((vertices[i], vertices[(i + 1) % length]))
                edge_mask |= 1 << edge_index[(u, v)]
                vertex_mask |= 1 << vertices[i]
            cycles.add((vertex_mask, edge_mask, length))
    return edges, tuple(sorted(cycles))


def run_cf1():
    before = ASSERTIONS
    states = 0
    multi_terminal = 0
    variable_clock = 0
    max_support = 0
    n = 5
    edges, cycles = undirected_cycle_data(n)
    for graph in range(1 << len(edges)):
        def successors(active_vertices):
            active = [cycle for cycle in cycles if graph & cycle[1] == cycle[1] and active_vertices & cycle[0] == cycle[0]]
            if not active:
                return ()
            transitions = []
            for vertex_mask, _, length in active:
                for vertex in range(n):
                    if vertex_mask >> vertex & 1:
                        transitions.append((active_vertices & ~(1 << vertex), Fraction(1, len(active) * length)))
            return transitions

        analyze = weighted_analyzer(successors)
        for active_vertices in range(1 << n):
            states += 1
            terminal_law, clock_law = analyze(active_vertices)
            validate_laws(terminal_law, clock_law, ("CF1", graph, active_vertices))
            check(all(not successors(endpoint) for endpoint, _ in terminal_law), ("CF1 bipartite", graph, active_vertices))
            multi_terminal += len(terminal_law) > 1
            variable_clock += len(clock_law) > 1
            max_support = max(max_support, len(terminal_law))
    record(
        "CF1",
        "induced subgraphs / random odd-cycle transversal deletion",
        "every induced state of every labelled graph on five vertices",
        states,
        f"{multi_terminal} sources have multiple bipartite endpoints and {variable_clock} have variable clocks; max support {max_support}",
        "KILL_ODD_CYCLE_TRANSVERSAL_HEURISTIC_NO_CLOSED_LAW",
        before,
    )


def main():
    runners = (
        run_sf1, run_ms1, run_pr1, run_pk1, run_tr1,
        run_er1, run_tm1, run_ce1, run_ch1, run_ct1,
        run_dc1, run_cn1, run_cr1, run_ap1, run_dg1,
        run_sc1, run_bf3, run_lm1, run_gv1, run_cf1,
    )
    for runner in runners:
        runner()
    check(len(ROWS) == 20, "twenty systems")
    check(len({row[0] for row in ROWS}) == 20, "unique handles")
    check(all(row[3] > 0 and row[4] > 0 for row in ROWS), "nonempty rows")

    print("REPLACEMENT_STOCHASTIC_ROUND2_V1")
    for row in ROWS:
        handle, carrier, scope, states, assertions, disposition, signal = row
        print(
            f"{handle}|{carrier}|{scope}|states={states}|assertions={assertions}|"
            f"{disposition}|{signal}"
        )
    print(f"SYSTEMS={len(ROWS)}")
    print(f"ENUMERATED_INPUTS={sum(row[3] for row in ROWS)}")
    print(f"SYSTEM_ASSERTIONS={sum(row[4] for row in ROWS)}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("EXACT_ARITHMETIC=integers+fractions.Fraction")
    print("FLOATING_POINT=none")
    print("SAMPLING=none")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
