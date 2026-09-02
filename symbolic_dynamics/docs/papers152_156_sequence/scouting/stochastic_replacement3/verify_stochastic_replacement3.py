#!/usr/bin/env python3
"""Exact falsifier for the stochastic replacement-3 breadth gate.

Eight genuinely different literal mechanisms are checked using only integers
and fractions.Fraction.  Generic finite-state linear algebra is used only as a
falsifier; it is explicitly not counted as a theorem contribution.
"""

from collections import defaultdict, deque
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import prod


ASSERTIONS = 0
SECTION = "setup"
COUNTS = defaultdict(int)
SAMPLES = {}


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    COUNTS[SECTION] += 1
    if not condition:
        raise AssertionError(message)


def equal(left, right, message="exact equality failed"):
    check(left == right, f"{message}: {left!r} != {right!r}")


def solve_linear(matrix, rhs):
    n = len(rhs)
    aug = [[Q(x) for x in matrix[i]] + [Q(rhs[i])] for i in range(n)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col]), None)
        check(pivot is not None, f"singular system at column {col}")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row == col or not aug[row][col]:
                continue
            factor = aug[row][col]
            aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [aug[i][-1] for i in range(n)]


def push(distribution, kernel):
    answer = defaultdict(Q)
    for state, mass in distribution.items():
        for target, probability in kernel(state).items():
            answer[target] += mass * probability
    return dict(answer)


# ---------------------------------------------------------------------------
# DBM: discrete Bak--Sneppen extremal-neighbour refresh


def rotate_tuple(state, shift=1):
    shift %= len(state)
    return state[shift:] + state[:shift]


def dbm_transition(state, alphabet):
    n = len(state)
    minimum = min(state)
    active = [i for i, value in enumerate(state) if value == minimum]
    counts = defaultdict(int)
    denominator = len(active)
    for site in active:
        refreshed = sorted({(site - 1) % n, site, (site + 1) % n})
        denominator_site = alphabet ** len(refreshed)
        for values in product(range(alphabet), repeat=len(refreshed)):
            target = list(state)
            for position, value in zip(refreshed, values):
                target[position] = value
            counts[tuple(target)] += Q(1, len(active) * denominator_site)
    return dict(counts)


def verify_dbm():
    global SECTION
    SECTION = "DBM discrete Bak-Sneppen"
    sample = None
    for n in range(3, 6):
        for alphabet in (2, 3):
            states = tuple(product(range(alphabet), repeat=n))
            state_set = set(states)
            for state in states:
                row = dbm_transition(state, alphabet)
                equal(sum(row.values()), Q(1), "DBM row mass")
                check(set(row) <= state_set, "DBM transition closure")
                rotated_row = {
                    rotate_tuple(target): probability for target, probability in row.items()
                }
                equal(rotated_row, dbm_transition(rotate_tuple(state), alphabet),
                      "DBM rotation equivariance")
            distribution = {tuple([0] * n): Q(1)}
            for _ in range(3):
                distribution = push(distribution, lambda s, a=alphabet: dbm_transition(s, a))
                equal(sum(distribution.values()), Q(1), "DBM time-layer mass")
            if n == 5 and alphabet == 3:
                expected_min = sum(mass * min(state) for state, mass in distribution.items())
                sample = (len(distribution), expected_min)
    SAMPLES["DBM"] = f"n5_q3_support_t3={sample[0]};Emin_t3={sample[1]}"


# ---------------------------------------------------------------------------
# LIT: fixed-rectangle Latin intercalate trades


def is_latin(square):
    n = len(square)
    target = set(range(n))
    return (all(set(row) == target for row in square)
            and all({square[i][j] for i in range(n)} == target for j in range(n)))


def latin_squares(n):
    rows = tuple(permutations(range(n)))
    answer = []

    def visit(chosen):
        if len(chosen) == n:
            answer.append(tuple(chosen))
            return
        for row in rows:
            if all(len({chosen[i][j] for i in range(len(chosen))} | {row[j]})
                   == len(chosen) + 1 for j in range(n)):
                visit(chosen + [row])

    visit([])
    return tuple(answer)


def intercalate_scheduler(square):
    n = len(square)
    outcomes = []
    for r1, r2 in combinations(range(n), 2):
        for c1, c2 in combinations(range(n), 2):
            a, b = square[r1][c1], square[r1][c2]
            if a != b and square[r2][c1] == b and square[r2][c2] == a:
                target = [list(row) for row in square]
                target[r1][c1], target[r1][c2] = b, a
                target[r2][c1], target[r2][c2] = a, b
                outcomes.append(tuple(tuple(row) for row in target))
            else:
                outcomes.append(square)
    return outcomes


def verify_lit():
    global SECTION
    SECTION = "LIT Latin intercalate trades"
    samples = []
    for n, expected in ((3, 12), (4, 576)):
        states = latin_squares(n)
        equal(len(states), expected, "Latin-square census")
        state_set = set(states)
        slots = len(tuple(combinations(range(n), 2))) ** 2
        columns = {state: Q(0) for state in states}
        graph = {state: set() for state in states}
        trade_counts = []
        for state in states:
            outcomes = intercalate_scheduler(state)
            equal(len(outcomes), slots, "LIT fixed scheduler size")
            trades = 0
            for target in outcomes:
                check(target in state_set and is_latin(target), "LIT trade preserves Latin")
                columns[target] += Q(1, slots)
                if target != state:
                    trades += 1
                    graph[state].add(target)
                    graph[target].add(state)
            trade_counts.append(trades)
        for mass in columns.values():
            equal(mass, Q(1), "LIT uniform stationary column")
        unseen = set(states)
        component_sizes = []
        while unseen:
            root = next(iter(unseen))
            reached = {root}
            queue = deque([root])
            while queue:
                for target in graph[queue.popleft()]:
                    if target not in reached:
                        reached.add(target)
                        queue.append(target)
            unseen -= reached
            component_sizes.append(len(reached))
        samples.append((n, min(trade_counts), max(trade_counts), tuple(sorted(component_sizes))))
    SAMPLES["LIT"] = ";".join(
        f"n{n}_trades={lo}..{hi}_components={','.join(map(str, comps))}"
        for n, lo, hi, comps in samples
    )


# ---------------------------------------------------------------------------
# PPT: plane-partition add/remove cube toggle chain


def is_plane_partition(state, rows, columns, height):
    if len(state) != rows * columns or any(not 0 <= x <= height for x in state):
        return False
    at = lambda i, j: state[i * columns + j]
    return (all(at(i, j) >= at(i + 1, j)
                for i in range(rows - 1) for j in range(columns))
            and all(at(i, j) >= at(i, j + 1)
                    for i in range(rows) for j in range(columns - 1)))


def plane_partitions(rows, columns, height):
    return tuple(state for state in product(range(height + 1), repeat=rows * columns)
                 if is_plane_partition(state, rows, columns, height))


def ppt_scheduler(state, rows, columns, height):
    outcomes = []
    for position in range(rows * columns):
        for delta in (-1, 1):
            target = list(state)
            target[position] += delta
            target = tuple(target)
            outcomes.append(target if is_plane_partition(target, rows, columns, height) else state)
    return outcomes


def macmahon_count(rows, columns, height):
    value = Q(1)
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            for k in range(1, height + 1):
                value *= Q(i + j + k - 1, i + j + k - 2)
    check(value.denominator == 1, "MacMahon product integral")
    return value.numerator


def verify_ppt():
    global SECTION
    SECTION = "PPT plane-partition toggles"
    samples = []
    for rows, columns, height in ((1, 2, 3), (2, 2, 2), (2, 3, 2)):
        states = plane_partitions(rows, columns, height)
        equal(len(states), macmahon_count(rows, columns, height), "MacMahon census")
        state_set = set(states)
        slots = 2 * rows * columns
        columns_mass = {state: Q(0) for state in states}
        graph = {state: set() for state in states}
        volume_counts = defaultdict(int)
        for state in states:
            volume_counts[sum(state)] += 1
            outcomes = ppt_scheduler(state, rows, columns, height)
            equal(len(outcomes), slots, "PPT fixed scheduler")
            for target in outcomes:
                check(target in state_set, "PPT toggle closure")
                columns_mass[target] += Q(1, slots)
                if target != state:
                    graph[state].add(target)
                    graph[target].add(state)
        for mass in columns_mass.values():
            equal(mass, Q(1), "PPT uniform stationary column")
        maximum_volume = rows * columns * height
        for volume, count in volume_counts.items():
            equal(count, volume_counts[maximum_volume - volume], "PPT complement symmetry")
        reached = {states[0]}
        queue = deque([states[0]])
        while queue:
            for target in graph[queue.popleft()]:
                if target not in reached:
                    reached.add(target)
                    queue.append(target)
        equal(reached, state_set, "PPT toggle graph connected")
        samples.append((rows, columns, height, len(states), max(volume_counts.values())))
    SAMPLES["PPT"] = ";".join(
        f"{a}x{b}x{c}_states={count}_maxvolcoeff={peak}"
        for a, b, c, count, peak in samples
    )


# ---------------------------------------------------------------------------
# SMB: random blocking-pair paths in two-sided matching


def partial_matchings(n):
    states = []
    for values in product(range(-1, n), repeat=n):
        assigned = [x for x in values if x >= 0]
        if len(assigned) == len(set(assigned)):
            states.append(tuple(values))
    return tuple(states)


def rank_tables(preferences):
    return tuple({value: rank for rank, value in enumerate(row)} for row in preferences)


def blocking_pairs(matching, men_preferences, women_preferences):
    n = len(matching)
    men_rank = rank_tables(men_preferences)
    women_rank = rank_tables(women_preferences)
    husband = [-1] * n
    for man, woman in enumerate(matching):
        if woman >= 0:
            husband[woman] = man
    answer = []
    for man in range(n):
        current_woman = matching[man]
        for woman in range(n):
            if current_woman == woman:
                continue
            man_prefers = (current_woman < 0
                           or men_rank[man][woman] < men_rank[man][current_woman])
            current_man = husband[woman]
            woman_prefers = (current_man < 0
                             or women_rank[woman][man] < women_rank[woman][current_man])
            if man_prefers and woman_prefers:
                answer.append((man, woman))
    return answer


def resolve_blocking_pair(matching, pair):
    man, woman = pair
    target = list(matching)
    old_husband = next((m for m, w in enumerate(target) if w == woman), None)
    if old_husband is not None:
        target[old_husband] = -1
    target[man] = woman
    return tuple(target)


def smb_kernel(matching, men_preferences, women_preferences):
    pairs = blocking_pairs(matching, men_preferences, women_preferences)
    if not pairs:
        return {matching: Q(1)}
    counts = defaultdict(int)
    for pair in pairs:
        counts[resolve_blocking_pair(matching, pair)] += 1
    return {target: Q(count, len(pairs)) for target, count in counts.items()}


def absorption_solution(states, kernel, absorbing):
    transient = [state for state in states if state not in absorbing]
    index = {state: i for i, state in enumerate(transient)}
    size = len(transient)
    matrix = [[Q(0) for _ in range(size)] for _ in range(size)]
    rhs_mean = [Q(1)] * size
    for state in transient:
        i = index[state]
        matrix[i][i] = 1
        for target, probability in kernel(state).items():
            if target in index:
                matrix[i][index[target]] -= probability
    mean = solve_linear(matrix, rhs_mean)
    endpoint = {}
    for terminal in sorted(absorbing):
        rhs = [Q(0)] * size
        for state in transient:
            i = index[state]
            rhs[i] = kernel(state).get(terminal, Q(0))
        solution = solve_linear(matrix, rhs)
        endpoint[terminal] = solution
    return transient, mean, endpoint


def verify_smb():
    global SECTION
    SECTION = "SMB blocking-pair matching"
    profiles = [
        (
            ((0, 1, 2), (1, 2, 0), (2, 0, 1)),
            ((1, 0, 2), (2, 1, 0), (0, 2, 1)),
        ),
        (
            ((0, 1, 2), (0, 2, 1), (1, 0, 2)),
            ((2, 1, 0), (1, 0, 2), (0, 2, 1)),
        ),
    ]
    samples = []
    states = partial_matchings(3)
    equal(len(states), 34, "number of partial matchings n=3")
    for profile_id, (men, women) in enumerate(profiles):
        kernel = lambda s, m=men, w=women: smb_kernel(s, m, w)
        state_set = set(states)
        stable = {state for state in states if not blocking_pairs(state, men, women)}
        check(stable, "SMB has stable states")
        for state in states:
            row = kernel(state)
            equal(sum(row.values()), Q(1), "SMB row mass")
            check(set(row) <= state_set, "SMB closure")
        # Every state has a directed route to stability in the finite pilot.
        reverse = {state: set() for state in states}
        for state in states:
            for target, probability in kernel(state).items():
                if probability and target != state:
                    reverse[target].add(state)
        can_absorb = set(stable)
        queue = deque(stable)
        while queue:
            for source in reverse[queue.popleft()]:
                if source not in can_absorb:
                    can_absorb.add(source)
                    queue.append(source)
        equal(can_absorb, state_set, "SMB every state can reach stability")
        transient, mean, endpoint = absorption_solution(states, kernel, stable)
        initial = (-1, -1, -1)
        initial_index = transient.index(initial)
        endpoint_law = {terminal: values[initial_index]
                        for terminal, values in endpoint.items()
                        if values[initial_index]}
        equal(sum(endpoint_law.values()), Q(1), "SMB endpoint mass")
        samples.append((profile_id, len(stable), mean[initial_index], len(endpoint_law)))
    SAMPLES["SMB"] = ";".join(
        f"profile{i}_stable={stable}_Eempty={mean}_endpoints={support}"
        for i, stable, mean, support in samples
    )


# ---------------------------------------------------------------------------
# AIM: capped additive-increase/multiplicative-decrease


def aim_kernel(state, cap, loss_probability):
    decrease = max(1, state // 2)
    increase = min(cap, state + 1)
    row = defaultdict(Q)
    row[decrease] += loss_probability
    row[increase] += 1 - loss_probability
    return dict(row)


def finite_stationary(states, kernel):
    size = len(states)
    index = {state: i for i, state in enumerate(states)}
    matrix = [[Q(0) for _ in range(size)] for _ in range(size)]
    rhs = [Q(0)] * size
    for equation, target in enumerate(states[:-1]):
        for source in states:
            matrix[equation][index[source]] = kernel(source).get(target, Q(0))
        matrix[equation][index[target]] -= 1
    matrix[-1] = [Q(1)] * size
    rhs[-1] = Q(1)
    return solve_linear(matrix, rhs)


def verify_aim():
    global SECTION
    SECTION = "AIM capped AIMD"
    samples = []
    for cap in range(4, 13):
        for probability in (Q(1, 3), Q(2, 5)):
            states = tuple(range(1, cap + 1))
            kernel = lambda s, c=cap, p=probability: aim_kernel(s, c, p)
            for state in states:
                row = kernel(state)
                equal(sum(row.values()), Q(1), "AIM row mass")
                check(set(row) <= set(states), "AIM closure")
                if 1 < state < cap and state // 2 != state + 1:
                    equal(row[max(1, state // 2)], probability, "AIM one-row loss inverse")
            stationary = finite_stationary(states, kernel)
            equal(sum(stationary), Q(1), "AIM stationary mass")
            for target in states:
                incoming = sum(stationary[i] * kernel(source).get(target, Q(0))
                               for i, source in enumerate(states))
                equal(incoming, stationary[target - 1], "AIM stationary equation")
            # Compare literal Bernoulli words with iterative layers.
            distribution = {1: Q(1)}
            for steps in range(1, 7):
                distribution = push(distribution, kernel)
                direct = defaultdict(Q)
                for losses in product((0, 1), repeat=steps):
                    state = 1
                    mass = Q(1)
                    for loss in losses:
                        mass *= probability if loss else 1 - probability
                        state = max(1, state // 2) if loss else min(cap, state + 1)
                    direct[state] += mass
                equal(distribution, dict(direct), "AIM word/layer agreement")
            if cap == 12:
                mean = sum(stationary[i] * state for i, state in enumerate(states))
                samples.append((probability, mean))
    SAMPLES["AIM"] = ";".join(f"cap12_p{p}_mean={m}" for p, m in samples)


# ---------------------------------------------------------------------------
# RSP: random-edge descent on a Gray-ranked cube orientation


def gray(index):
    return index ^ (index >> 1)


def gray_rank(value):
    answer = 0
    while value:
        answer ^= value
        value >>= 1
    return answer


def rsp_outgoing(vertex, dimension):
    rank = gray_rank(vertex)
    return tuple(target for bit in range(dimension)
                 for target in (vertex ^ (1 << bit),)
                 if gray_rank(target) < rank)


def shifted_mixture(distributions):
    answer = defaultdict(Q)
    count = len(distributions)
    for distribution in distributions:
        for time, mass in distribution.items():
            answer[time + 1] += mass / count
    return dict(answer)


def verify_rsp():
    global SECTION
    SECTION = "RSP random-edge Gray cube"
    samples = []
    for dimension in range(2, 8):
        vertices = tuple(range(1 << dimension))
        ranks = [gray_rank(vertex) for vertex in vertices]
        equal(set(ranks), set(range(1 << dimension)), "Gray rank permutation")
        # Check the unique-sink property on every face.  A face is specified by
        # its free-coordinate mask and an assignment on the complementary
        # fixed coordinates.
        full_mask = (1 << dimension) - 1
        for free_mask in range(1 << dimension):
            fixed_mask = full_mask ^ free_mask
            fixed = fixed_mask
            while True:
                face = []
                free = free_mask
                while True:
                    face.append(fixed | free)
                    if free == 0:
                        break
                    free = (free - 1) & free_mask
                sinks = [
                    vertex for vertex in face
                    if not any(
                        gray_rank(vertex ^ (1 << bit)) < gray_rank(vertex)
                        for bit in range(dimension) if free_mask & (1 << bit)
                    )
                ]
                equal(len(sinks), 1, "RSP unique sink on every cube face")
                if fixed == 0:
                    break
                fixed = (fixed - 1) & fixed_mask
        time_laws = {gray(0): {0: Q(1)}}
        for rank in range(1, 1 << dimension):
            vertex = gray(rank)
            outgoing = rsp_outgoing(vertex, dimension)
            check(outgoing, "RSP nonsink has outgoing edge")
            for target in outgoing:
                check(gray_rank(target) < rank, "RSP strict rank descent")
                check(bin(vertex ^ target).count("1") == 1, "RSP cube edge")
            law = shifted_mixture([time_laws[target] for target in outgoing])
            equal(sum(law.values()), Q(1), "RSP clock-law mass")
            time_laws[vertex] = law
        top = gray((1 << dimension) - 1)
        mean = sum(time * mass for time, mass in time_laws[top].items())
        samples.append((dimension, len(time_laws[top]), mean))
    SAMPLES["RSP"] = ";".join(
        f"d{d}_clock_support={support}_Etop={mean}" for d, support, mean in samples
    )


# ---------------------------------------------------------------------------
# R2O: uniformly choose a strict 2-opt improvement of a Euclidean tour


def canonical_tour(tour):
    check(tour[0] == 0, "tour anchored at zero")
    reverse = (0,) + tuple(reversed(tour[1:]))
    return min(tuple(tour), reverse)


def tours(n):
    return tuple(sorted({canonical_tour((0,) + order)
                         for order in permutations(range(1, n))}))


def squared_distance(first, second):
    return (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2


def tour_length(tour, points):
    return sum(squared_distance(points[tour[i]], points[tour[(i + 1) % len(tour)]])
               for i in range(len(tour)))


def two_opt_neighbors(tour):
    n = len(tour)
    answer = set()
    for first in range(1, n - 1):
        for last in range(first + 1, n):
            if first == 1 and last == n - 1:
                continue
            candidate = canonical_tour(tour[:first] + tuple(reversed(tour[first:last + 1]))
                                       + tour[last + 1:])
            if candidate != tour:
                answer.add(candidate)
    return tuple(sorted(answer))


def verify_r2o():
    global SECTION
    SECTION = "R2O strict 2-opt descent"
    point_families = {
        6: ((0, 0), (1, 4), (3, 1), (5, 5), (7, 0), (9, 3)),
        7: ((0, 0), (1, 5), (3, 1), (4, 6), (6, 2), (8, 7), (10, 0)),
    }
    samples = []
    for n, points in point_families.items():
        states = tours(n)
        # (n-1)!/2, written without importing factorial.
        expected = prod(range(1, n)) // 2
        equal(len(states), expected, "undirected anchored tour census")
        state_set = set(states)
        lengths = {tour: tour_length(tour, points) for tour in states}
        improving = {}
        for tour in states:
            neighbours = two_opt_neighbors(tour)
            check(set(neighbours) <= state_set, "2-opt closure")
            improving[tour] = tuple(target for target in neighbours
                                    if lengths[target] < lengths[tour])
            for target in improving[tour]:
                check(lengths[target] < lengths[tour], "strict 2-opt descent")
        ordered = sorted(states, key=lambda tour: (lengths[tour], tour))
        endpoint_laws = {}
        clock_laws = {}
        local_optima = []
        for tour in ordered:
            targets = improving[tour]
            if not targets:
                local_optima.append(tour)
                endpoint_laws[tour] = {tour: Q(1)}
                clock_laws[tour] = {0: Q(1)}
            else:
                endpoint = defaultdict(Q)
                for target in targets:
                    for terminal, mass in endpoint_laws[target].items():
                        endpoint[terminal] += mass / len(targets)
                endpoint_laws[tour] = dict(endpoint)
                clock_laws[tour] = shifted_mixture([clock_laws[target] for target in targets])
            equal(sum(endpoint_laws[tour].values()), Q(1), "R2O endpoint mass")
            equal(sum(clock_laws[tour].values()), Q(1), "R2O clock mass")
        start = max(states, key=lambda tour: (lengths[tour], tour))
        samples.append((n, len(states), len(local_optima),
                        len(endpoint_laws[start]), len(clock_laws[start])))
    SAMPLES["R2O"] = ";".join(
        f"n{n}_tours={count}_local={local}_start_endpoints={ends}_clock={clock}"
        for n, count, local, ends, clock in samples
    )


# ---------------------------------------------------------------------------
# RDA: asynchronous deferred acceptance


def rda_step(state, proposer, proposer_preferences, receiver_preferences):
    partners, next_choices = state
    n = len(partners)
    check(partners[proposer] < 0 and next_choices[proposer] < n,
          "RDA proposer eligible")
    receiver = proposer_preferences[proposer][next_choices[proposer]]
    new_next = list(next_choices)
    new_next[proposer] += 1
    new_partners = list(partners)
    current = next((man for man, woman in enumerate(partners) if woman == receiver), None)
    receiver_rank = rank_tables(receiver_preferences)[receiver]
    if current is None or receiver_rank[proposer] < receiver_rank[current]:
        if current is not None:
            new_partners[current] = -1
        new_partners[proposer] = receiver
    return tuple(new_partners), tuple(new_next)


def rda_kernel(state, proposer_preferences, receiver_preferences):
    partners, next_choices = state
    n = len(partners)
    eligible = [man for man in range(n) if partners[man] < 0 and next_choices[man] < n]
    if not eligible:
        return {state: Q(1)}
    counts = defaultdict(int)
    for proposer in eligible:
        counts[rda_step(state, proposer, proposer_preferences, receiver_preferences)] += 1
    return {target: Q(count, len(eligible)) for target, count in counts.items()}


def rda_terminal_distribution(proposer_preferences, receiver_preferences):
    n = len(proposer_preferences)
    initial = (tuple([-1] * n), tuple([0] * n))
    distributions = {initial: {0: Q(1)}}
    queue = deque([initial])
    terminal = defaultdict(Q)
    seen = {initial}
    while queue:
        state = queue.popleft()
        partners, next_choices = state
        row = rda_kernel(state, proposer_preferences, receiver_preferences)
        eligible = [man for man in range(n)
                    if partners[man] < 0 and next_choices[man] < n]
        if not eligible:
            continue
        for target in row:
            check(sum(target[1]) == sum(next_choices) + 1, "RDA proposal rank increases")
            if target not in seen:
                seen.add(target)
                queue.append(target)
    # Dynamic programming by total proposal count.
    layer = {initial: Q(1)}
    for time in range(n * n + 1):
        nxt = defaultdict(Q)
        for state, mass in layer.items():
            partners, next_choices = state
            eligible = [man for man in range(n)
                        if partners[man] < 0 and next_choices[man] < n]
            if not eligible:
                terminal[(partners, time)] += mass
            else:
                for target, probability in rda_kernel(
                        state, proposer_preferences, receiver_preferences).items():
                    nxt[target] += mass * probability
        layer = dict(nxt)
        if not layer:
            break
    equal(sum(terminal.values()), Q(1), "RDA terminal mass")
    return seen, dict(terminal)


def verify_rda():
    global SECTION
    SECTION = "RDA asynchronous deferred acceptance"
    profiles = [
        (
            ((0, 1, 2), (0, 1, 2), (0, 1, 2)),
            ((2, 1, 0), (1, 2, 0), (0, 2, 1)),
        ),
        (
            ((0, 1, 2, 3), (1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2)),
            ((1, 0, 3, 2), (2, 1, 0, 3), (3, 2, 1, 0), (0, 3, 2, 1)),
        ),
    ]
    samples = []
    for profile_id, (proposers, receivers) in enumerate(profiles):
        seen, terminal = rda_terminal_distribution(proposers, receivers)
        matchings = {partners for (partners, _), mass in terminal.items() if mass}
        clocks = {time for (_, time), mass in terminal.items() if mass}
        equal(len(matchings), 1, "RDA order-independent proposer-optimal matching")
        equal(len(clocks), 1, "RDA total proposals deterministic")
        matching = next(iter(matchings))
        check(-1 not in matching and len(set(matching)) == len(matching),
              "RDA terminal perfect matching")
        # The clock is the sum of the final partners' ranks plus one.
        expected_clock = sum(proposers[man].index(woman) + 1
                             for man, woman in enumerate(matching))
        equal(next(iter(clocks)), expected_clock, "RDA proposal-count identity")
        samples.append((profile_id, len(seen), next(iter(clocks)), matching))
    SAMPLES["RDA"] = ";".join(
        f"profile{i}_states={states}_clock={clock}_matching={','.join(map(str, matching))}"
        for i, states, clock, matching in samples
    )


def main():
    verify_dbm()
    verify_lit()
    verify_ppt()
    verify_smb()
    verify_aim()
    verify_rsp()
    verify_r2o()
    verify_rda()
    for name in sorted(COUNTS):
        key = name.split()[0]
        print(f"{name}: assertions={COUNTS[name]} sample={SAMPLES.get(key, '-')}")
    print(f"PASS systems=8 selected=0 assertions={ASSERTIONS}")


if __name__ == "__main__":
    main()
