#!/usr/bin/env python3
"""Exact integer/rational scouting for stochastic and local-rewrite systems.

Every transition is constructed literally.  Probabilities are represented by
fractions.Fraction whenever a probability is evaluated.  No randomness,
floating point, third-party package, network access, or timestamp is used.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial, gcd
import sys


sys.setrecursionlimit(1_000_000)

ASSERTIONS = 0
RESULTS = []


def check(condition, message="exact check failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def finish(code, family, range_text, states, decision, signal, before):
    RESULTS.append(
        {
            "code": code,
            "family": family,
            "range": range_text,
            "states": states,
            "assertions": ASSERTIONS - before,
            "decision": decision,
            "signal": signal,
        }
    )


def tarjan_scc(nodes, adjacency):
    """Return exact SCCs of a finite directed graph."""
    index = 0
    stack = []
    on_stack = set()
    indices = {}
    low = {}
    components = []

    def visit(v):
        nonlocal index
        indices[v] = index
        low[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)
        for w in adjacency[v]:
            if w not in indices:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            component = set()
            while True:
                w = stack.pop()
                on_stack.remove(w)
                component.add(w)
                if w == v:
                    break
            components.append(component)

    for node in nodes:
        if node not in indices:
            visit(node)
    return components


def closed_components(components, adjacency):
    out = []
    for component in components:
        if all(target in component for state in component for target in adjacency[state]):
            out.append(component)
    return out


def bitcount(x):
    return x.bit_count()


def inversion_count_bits(mask, n):
    return sum(
        1
        for i in range(n)
        for j in range(i + 1, n)
        if ((mask >> i) & 1) and not ((mask >> j) & 1)
    )


# ---------------------------------------------------------------------------
# S01: ternary cyclic-dominance deletion


def predator(a, b):
    check(a != b)
    return a if (a - b) % 3 == 1 else b


def predator_successors(word):
    out = []
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            winner = predator(word[i], word[i + 1])
            out.append(word[:i] + (winner,) + word[i + 2 :])
    return out


@lru_cache(None)
def predator_expected_terminal_size(word):
    successors = predator_successors(word)
    if not successors:
        return Fraction(len(word))
    return sum(
        (predator_expected_terminal_size(target) for target in successors),
        Fraction(),
    ) / len(successors)


@lru_cache(None)
def predator_terminal_size_distribution(word):
    successors = predator_successors(word)
    if not successors:
        return ((len(word), Fraction(1)),)
    total = defaultdict(Fraction)
    for target in successors:
        for terminal_size, probability in predator_terminal_size_distribution(target):
            total[terminal_size] += probability / len(successors)
    return tuple(sorted(total.items()))


def rising_factorial(value, order):
    answer = 1
    for offset in range(order):
        answer *= value + offset
    return answer


def pilot_s01():
    before = ASSERTIONS
    explicit_states = 0
    for n in range(1, 10):
        for word in product(range(3), repeat=n):
            explicit_states += 1
            successors = predator_successors(word)
            check(bool(successors) == (len(set(word)) > 1))
            if successors:
                check(sum((Fraction(1, len(successors)) for _ in successors), Fraction()) == 1)
            for target in successors:
                check(len(target) == n - 1)
                check(all(letter in (0, 1, 2) for letter in target))
            value = predator_expected_terminal_size(word)
            check(Fraction(1) <= value <= n)

    periodic_values = []
    periodic_distributions = []
    for n in range(1, 20):
        word = tuple(i % 3 for i in range(n))
        value = predator_expected_terminal_size(word)
        distribution = dict(predator_terminal_size_distribution(word))
        check(sum(distribution.values(), Fraction()) == 1)
        check(sum(size * probability for size, probability in distribution.items()) == value)
        k = (n - 1) // 3
        predicted = Fraction(1)
        for j in range(1, k + 1):
            predicted *= Fraction(3 * j + 1, 3 * j)
        check(value == predicted)
        periodic_values.append(value)
        periodic_distributions.append(distribution)

    check(periodic_values[0] == periodic_values[1] == periodic_values[2] == 1)
    for k in range(7):
        first = 3 * k
        available = periodic_distributions[first : min(first + 3, 19)]
        check(all(distribution == available[0] for distribution in available))

    # The observed full law is the block-count chain of PD(1/3,0).  This
    # verifies the identity but deliberately does not promote it to a theorem:
    # a literal reduction/coupling proof is still missing.
    for k in range(6):
        old = periodic_distributions[3 * k]
        new = periodic_distributions[3 * (k + 1)]
        denominator = 3 * (k + 1)
        for terminal_size in range(1, k + 3):
            predicted_probability = old.get(terminal_size, Fraction()) * Fraction(
                denominator - terminal_size, denominator
            )
            predicted_probability += old.get(terminal_size - 1, Fraction()) * Fraction(
                terminal_size - 1, denominator
            )
            check(new.get(terminal_size, Fraction()) == predicted_probability)

    for k in range(7):
        distribution = periodic_distributions[3 * k]
        for order in range(1, 6):
            actual = sum(
                rising_factorial(size, order) * probability
                for size, probability in distribution.items()
            )
            predicted = Fraction(factorial(order))
            for j in range(1, k + 1):
                predicted *= Fraction(3 * j + order, 3 * j)
            check(actual == predicted)

    finish(
        "S01",
        "variable ternary words / active-boundary deletion",
        "all words length 1..9; periodic full terminal-size law length 1..19",
        max(
            predator_expected_terminal_size.cache_info().currsize,
            predator_terminal_size_distribution.cache_info().currsize,
        ),
        "STOP_UNPROVED_OWNER_COLLISION",
        "Full periodic terminal-size PGF follows the PD(1/3,0) block-count recurrence through n=19, but no literal reduction proof was obtained and the target law is directly owned.",
        before,
    )


# ---------------------------------------------------------------------------
# S02: rootward occupied-set coalescence on a path


def rootward_successors(mask, n):
    out = []
    for v in range(1, n):
        if (mask >> v) & 1:
            out.append((mask & ~(1 << v)) | (1 << (v - 1)))
    return out


@lru_cache(None)
def rootward_distribution(n, mask):
    if mask == 1:
        return ((0, Fraction(1)),)
    successors = rootward_successors(mask, n)
    total = defaultdict(Fraction)
    for target in successors:
        for time, probability in rootward_distribution(n, target):
            total[time + 1] += probability / len(successors)
    return tuple(sorted(total.items()))


@lru_cache(None)
def rootward_expected_steps(n, mask):
    if mask == 1:
        return Fraction(0)
    successors = rootward_successors(mask, n)
    return Fraction(1) + sum(
        (rootward_expected_steps(n, target) for target in successors),
        Fraction(),
    ) / len(successors)


@lru_cache(None)
def pure_death_pair_meeting_mean(lower, upper):
    """Continuous-time meeting mean for ordered rate-one pure-death walks."""
    check(0 <= lower <= upper)
    if lower == upper:
        return Fraction(0)
    if lower == 0:
        return Fraction(upper)
    return Fraction(1, 2) + (
        pure_death_pair_meeting_mean(lower - 1, upper)
        + pure_death_pair_meeting_mean(lower, upper - 1)
    ) / 2


def double_factorial(n):
    value = 1
    while n > 1:
        value *= n
        n -= 2
    return value


def pilot_s02():
    before = ASSERTIONS
    states = 0
    rooted_states = 0
    for n in range(1, 13):
        for mask in range(1, 1 << n):
            states += 1
            successors = rootward_successors(mask, n)
            check(bool(successors) == (mask != 1))
            potential = sum(v for v in range(n) if (mask >> v) & 1)
            if successors:
                check(sum((Fraction(1, len(successors)) for _ in successors), Fraction()) == 1)
            for target in successors:
                check(0 < target < (1 << n))
                target_potential = sum(v for v in range(n) if (target >> v) & 1)
                check(target_potential < potential)

            if mask & 1:
                rooted_states += 1
                positions = [v for v in range(n) if (mask >> v) & 1]
                interface_sum = sum(
                    (
                        pure_death_pair_meeting_mean(left, right)
                        for left, right in zip(positions, positions[1:])
                    ),
                    Fraction(),
                )
                check(rootward_expected_steps(n, mask) == interface_sum)

    check(rooted_states == sum(1 << (n - 1) for n in range(1, 13)))
    for upper in range(1, 13):
        check(
            pure_death_pair_meeting_mean(upper - 1, upper)
            == Fraction(
                double_factorial(2 * upper - 1),
                double_factorial(2 * upper - 2),
            )
        )

    for n in range(1, 11):
        distribution = dict(rootward_distribution(n, (1 << n) - 1))
        check(sum(distribution.values(), Fraction()) == 1)
        expected = sum((time * probability for time, probability in distribution.items()), Fraction())
        predicted = sum(
            (
                Fraction(double_factorial(2 * j - 3), double_factorial(2 * j - 4))
                for j in range(2, n + 1)
            ),
            Fraction(),
        )
        check(expected == predicted)
        if n == 1:
            check(distribution == {0: Fraction(1)})
        else:
            check(set(distribution) == set(range(n - 1, comb(n, 2) + 1)))
            check(min(distribution) == n - 1)
            check(max(distribution) == comb(n, 2))
            check(distribution[n - 1] == Fraction(1, factorial(n - 1)))
            check(distribution[comb(n, 2)] == Fraction(1, 2 ** comb(n - 1, 2)))

    finish(
        "S02",
        "occupied subsets of a rooted path / active-pile rootward coalescence",
        "all nonempty subsets n=1..12; full-start law n=1..10",
        states,
        "PROMOTE",
        "General rooted-state mean is the sum of adjacent pure-death interface meeting means; full-start PGF has contiguous support, exact endpoint masses, and the double-factorial mean.",
        before,
    )


# ---------------------------------------------------------------------------
# S03: asynchronous pointer squaring from a directed cycle


def pointer_active(function):
    return [v for v in range(len(function)) if function[function[v]] != function[v]]


def pointer_update(function, v):
    target = list(function)
    target[v] = function[function[v]]
    return tuple(target)


def pointer_reachable_cycle(n, store_edges):
    initial = tuple((i + 1) % n for i in range(n))
    queue = deque([initial])
    seen = {initial}
    adjacency = {} if store_edges else None
    while queue:
        function = queue.popleft()
        targets = tuple(pointer_update(function, v) for v in pointer_active(function))
        if adjacency is not None:
            adjacency[function] = targets
        for target in targets:
            check(len(target) == n)
            check(all(0 <= x < n for x in target))
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return seen, adjacency


def pilot_s03():
    before = ASSERTIONS
    states = 0
    reach_counts = []
    for n in range(1, 8):
        seen, adjacency = pointer_reachable_cycle(n, store_edges=(n <= 6))
        states += len(seen)
        predicted = (n + 1) ** (n - 1)
        check(len(seen) == predicted)
        absorbing = {
            function for function in seen if not pointer_active(function)
        }
        constants = {tuple(root for _ in range(n)) for root in range(n)}
        check(absorbing == constants)
        reach_counts.append(len(seen))
        if adjacency is not None:
            components = tarjan_scc(seen, adjacency)
            closed = closed_components(components, adjacency)
            check(len(closed) == n)
            check({next(iter(component)) for component in closed} == constants)
            check(all(len(component) == 1 for component in closed))

    finish(
        "S03",
        "endofunctions / asynchronous local pointer squaring",
        "directed-cycle start n=1..7; closed-SCC audit n=1..6",
        states,
        "KILL_INTERNAL",
        "Negative evidence: reachable census is (n+1)^(n-1) and closed classes are constants, but pointer doubling is an explicit P117 historical hard exclusion (and earlier C10).",
        before,
    )


# ---------------------------------------------------------------------------
# S04: stochastic adjacent-pair annihilation


def pilot_s04():
    before = ASSERTIONS
    states = 0
    absorbing_counts = []
    fib = [0, 1]
    for _ in range(20):
        fib.append(fib[-1] + fib[-2])
    for n in range(1, 13):
        absorbing = 0
        for mask in range(1 << n):
            states += 1
            active = 0
            for i in range(n - 1):
                target = mask
                if ((mask >> i) & 3) == 3:
                    target = mask & ~(3 << i)
                    active += 1
                    check(bitcount(target) == bitcount(mask) - 2)
                    check(bitcount(target) % 2 == bitcount(mask) % 2)
                check(0 <= target < (1 << n))
            if active == 0:
                absorbing += 1
            if n > 1:
                check(sum((Fraction(1, n - 1) for _ in range(n - 1)), Fraction()) == 1)
        check(absorbing == fib[n + 2])
        absorbing_counts.append(absorbing)
    finish(
        "S04",
        "binary particles on a line / random-edge 11->00 annihilation",
        "all words n=1..12",
        states,
        "KILL_OWNER_CLASSICAL",
        "Absorbers are Fibonacci independent sets and particle parity is invariant; standard annihilating/RSA boundary dominates.",
        before,
    )


# ---------------------------------------------------------------------------
# S05: asynchronous isolated-spin majority


def disagreement_edges(mask, n):
    return sum(((mask >> i) & 1) != ((mask >> (i + 1)) & 1) for i in range(n - 1))


def pilot_s05():
    before = ASSERTIONS
    states = 0
    absorbing_counts = []
    for n in range(1, 11):
        absorbing = 0
        for mask in range(1 << n):
            states += 1
            active = []
            for i in range(1, n - 1):
                left = (mask >> (i - 1)) & 1
                center = (mask >> i) & 1
                right = (mask >> (i + 1)) & 1
                majority = 1 if left + center + right >= 2 else 0
                target = (mask & ~(1 << i)) | (majority << i)
                check(0 <= target < (1 << n))
                if target != mask:
                    active.append(target)
                    check(disagreement_edges(target, n) == disagreement_edges(mask, n) - 2)
            if not active:
                absorbing += 1
        absorbing_counts.append(absorbing)
        check(absorbing >= 2)
    finish(
        "S05",
        "binary spin lines / random-site strict majority",
        "all words n=1..10",
        states,
        "KILL_OWNER_CLASSICAL",
        "Every effective update removes exactly two domain walls; this is the zero-temperature one-dimensional Glauber/majority core.",
        before,
    )


# ---------------------------------------------------------------------------
# S06: reversible parity triple rewrite


def pilot_s06():
    before = ASSERTIONS
    states = 0
    effective_edges = 0
    for n in range(1, 10):
        for mask in range(1 << n):
            states += 1
            for i in range(max(0, n - 2)):
                pattern = (mask >> i) & 7
                target = mask
                if pattern == 2:
                    target = (mask & ~(7 << i)) | (7 << i)
                elif pattern == 7:
                    target = (mask & ~(7 << i)) | (2 << i)
                if target != mask:
                    effective_edges += 1
                    check(bitcount(target) % 2 == bitcount(mask) % 2)
                    check(((target >> i) & 7) in (2, 7))
                    inverse = (target & ~(7 << i)) | (pattern << i)
                    check(inverse == mask)
                check(0 <= target < (1 << n))
    check(effective_edges % 2 == 0)
    finish(
        "S06",
        "binary words / symmetric 010<->111 triple rewrite",
        "all words n=1..9",
        states,
        "KILL_TRIVIAL_REVERSIBILITY",
        "Parity sectors are invariant and every effective edge is an involutive reverse edge, so uniform component stationarity is immediate.",
        before,
    )


# ---------------------------------------------------------------------------
# S07: hard-core heat-bath chain


def independent_masks_path(n):
    return [mask for mask in range(1 << n) if not (mask & (mask << 1))]


def pilot_s07():
    before = ASSERTIONS
    states = 0
    for n in range(1, 13):
        masks = independent_masks_path(n)
        states += len(masks)
        kernels = {}
        for mask in masks:
            counts = Counter()
            for v in range(n):
                cleared = mask & ~(1 << v)
                counts[cleared] += 1
                neighbors_free = (
                    (v == 0 or not ((mask >> (v - 1)) & 1))
                    and (v == n - 1 or not ((mask >> (v + 1)) & 1))
                )
                occupied = cleared | ((1 << v) if neighbors_free else 0)
                counts[occupied] += 1
            check(sum(counts.values()) == 2 * n)
            check(all(target in masks for target in counts))
            kernels[mask] = counts
        for source in masks:
            for target, weight in kernels[source].items():
                if source != target:
                    check(weight == kernels[target][source])
    finish(
        "S07",
        "independent sets of a path / single-site hard-core heat bath",
        "all independent sets n=1..12",
        states,
        "KILL_OWNER_CLASSICAL",
        "Exact detailed balance gives the uniform hard-core measure at activity one; no residual beyond standard Glauber dynamics.",
        before,
    )


# ---------------------------------------------------------------------------
# S08: monomer-dimer edge flip


def pilot_s08():
    before = ASSERTIONS
    states = 0
    for n in range(2, 14):
        edge_count = n - 1
        matchings = [
            mask for mask in range(1 << edge_count) if not (mask & (mask << 1))
        ]
        states += len(matchings)
        kernels = {}
        for mask in matchings:
            counts = Counter()
            for edge in range(edge_count):
                if (mask >> edge) & 1:
                    target = mask & ~(1 << edge)
                else:
                    left_free = edge == 0 or not ((mask >> (edge - 1)) & 1)
                    right_free = edge == edge_count - 1 or not ((mask >> (edge + 1)) & 1)
                    target = mask | (1 << edge) if left_free and right_free else mask
                counts[target] += 1
                check(target in matchings)
            check(sum(counts.values()) == edge_count)
            kernels[mask] = counts
        for source in matchings:
            for target, weight in kernels[source].items():
                if source != target:
                    check(weight == kernels[target][source])
    finish(
        "S08",
        "path matchings / random-edge monomer-dimer toggle",
        "all matchings on paths with 2..13 vertices",
        states,
        "KILL_OWNER_CLASSICAL",
        "Symmetric edge toggles give uniform matching stationarity; standard monomer-dimer Glauber chain.",
        before,
    )


# ---------------------------------------------------------------------------
# S09: cyclic facilitated exclusion


def pilot_s09():
    before = ASSERTIONS
    states = 0
    closed_summary = []
    for n in range(4, 10):
        nodes = list(range(1 << n))
        states += len(nodes)
        adjacency = {}
        for mask in nodes:
            targets = []
            for i in range(n):
                positions = (i, (i + 1) % n, (i + 2) % n)
                bits = tuple((mask >> p) & 1 for p in positions)
                if bits == (1, 1, 0):
                    target = mask & ~(1 << positions[1])
                    target |= 1 << positions[2]
                    targets.append(target)
                    check(bitcount(target) == bitcount(mask))
            adjacency[mask] = tuple(targets) if targets else (mask,)
        components = tarjan_scc(nodes, adjacency)
        closed = closed_components(components, adjacency)
        check(bool(closed))
        closed_summary.append((n, len(closed), max(map(len, closed))))
    finish(
        "S09",
        "conserved binary particles on a cycle / 110->101 facilitated hop",
        "all cyclic words n=4..9",
        states,
        "KILL_OWNER_CLASSICAL",
        "Multiple recurrent sectors occur, but the kernel is a standard facilitated exclusion/TASEP specialization.",
        before,
    )


# ---------------------------------------------------------------------------
# S10: voter copying on a path


def pilot_s10():
    before = ASSERTIONS
    states = 0
    for n in range(2, 10):
        events = [(i, i + 1) for i in range(n - 1)] + [
            (i + 1, i) for i in range(n - 1)
        ]
        for mask in range(1 << n):
            states += 1
            drift = 0
            for receiver, donor in events:
                donor_bit = (mask >> donor) & 1
                old_bit = (mask >> receiver) & 1
                target = (mask & ~(1 << receiver)) | (donor_bit << receiver)
                drift += bitcount(target) - bitcount(mask)
                check(0 <= target < (1 << n))
                check(bitcount(target) - bitcount(mask) == donor_bit - old_bit)
            check(drift == 0)
            check(sum((Fraction(1, len(events)) for _ in events), Fraction()) == 1)
    finish(
        "S10",
        "binary opinions on a path / oriented-edge voter copying",
        "all words n=2..9",
        states,
        "KILL_OWNER_CLASSICAL",
        "Particle count is an exact martingale, yielding consensus probability k/n; this is the classical voter model.",
        before,
    )


# ---------------------------------------------------------------------------
# S11: coalescing random walks on a star


def star_neighbors(vertex, leaves):
    return tuple(range(1, leaves + 1)) if vertex == 0 else (0,)


def pilot_s11():
    before = ASSERTIONS
    states = 0
    for leaves in range(1, 9):
        vertex_count = leaves + 1
        nodes = list(range(1, 1 << vertex_count))
        states += len(nodes)
        adjacency = {}
        for mask in nodes:
            probabilities = defaultdict(Fraction)
            occupied = [v for v in range(vertex_count) if (mask >> v) & 1]
            for v in occupied:
                neighbors = star_neighbors(v, leaves)
                for w in neighbors:
                    target = (mask & ~(1 << v)) | (1 << w)
                    probabilities[target] += Fraction(1, len(occupied) * len(neighbors))
                    check(bitcount(target) <= bitcount(mask))
            check(sum(probabilities.values(), Fraction()) == 1)
            adjacency[mask] = tuple(probabilities)
        components = tarjan_scc(nodes, adjacency)
        closed = closed_components(components, adjacency)
        singleton_masks = {1 << v for v in range(vertex_count)}
        check(len(closed) == 1)
        check(closed[0] == singleton_masks)
    finish(
        "S11",
        "unlabelled particles on stars / random-walk coalescence",
        "all nonempty occupancies on stars with 1..8 leaves",
        states,
        "KILL_OWNER_CLASSICAL",
        "The sole closed class is the singleton random-walk class; standard coalescing-walk ownership is direct.",
        before,
    )


# ---------------------------------------------------------------------------
# S12: annihilating random walks on a cycle


def pilot_s12():
    before = ASSERTIONS
    states = 0
    closed_signatures = []
    for n in range(3, 10):
        nodes = list(range(1 << n))
        states += len(nodes)
        adjacency = {}
        for mask in nodes:
            if mask == 0:
                adjacency[mask] = (0,)
                continue
            probabilities = defaultdict(Fraction)
            occupied = [v for v in range(n) if (mask >> v) & 1]
            for v in occupied:
                for step in (-1, 1):
                    w = (v + step) % n
                    if (mask >> w) & 1:
                        target = mask & ~(1 << v) & ~(1 << w)
                    else:
                        target = (mask & ~(1 << v)) | (1 << w)
                    probabilities[target] += Fraction(1, 2 * len(occupied))
                    check(bitcount(target) % 2 == bitcount(mask) % 2)
            check(sum(probabilities.values(), Fraction()) == 1)
            adjacency[mask] = tuple(probabilities)
        components = tarjan_scc(nodes, adjacency)
        closed = closed_components(components, adjacency)
        check(any(component == {0} for component in closed))
        check(any(all(bitcount(mask) == 1 for mask in component) for component in closed))
        check(len(closed) == 2)
        closed_signatures.append(tuple(sorted(len(component) for component in closed)))
    finish(
        "S12",
        "binary particles on cycles / nearest-neighbor annihilating walks",
        "all occupancies n=3..9",
        states,
        "KILL_OWNER_CLASSICAL",
        "Even and odd parity terminate in the empty and singleton recurrent sectors; classical annihilating random walks.",
        before,
    )


# ---------------------------------------------------------------------------
# S13: subtractive Euclidean dynamics


def euclid_step(state):
    a, b = state
    if a == b:
        return state
    return (a - b, b) if a > b else (a, b - a)


def pilot_s13():
    before = ASSERTIONS
    states = 0
    maximum_depth = 0
    for a in range(1, 21):
        for b in range(1, 21):
            states += 1
            initial_gcd = gcd(a, b)
            state = (a, b)
            depth = 0
            while state[0] != state[1]:
                target = euclid_step(state)
                check(sum(target) < sum(state))
                check(gcd(*target) == initial_gcd)
                state = target
                depth += 1
            check(state == (initial_gcd, initial_gcd))
            maximum_depth = max(maximum_depth, depth)
    check(maximum_depth == 19)
    finish(
        "S13",
        "positive integer pairs / subtract-larger Euclidean rewrite",
        "all pairs 1<=a,b<=20",
        states,
        "KILL_OWNER_CLASSICAL",
        "Exact gcd absorption and depth 19 on the box are the classical subtractive Euclidean algorithm.",
        before,
    )


# ---------------------------------------------------------------------------
# S14: asynchronous binary carries


def carry_successors(state):
    out = []
    for i in range(len(state) - 1):
        if state[i] >= 2:
            target = list(state)
            target[i] -= 2
            target[i + 1] += 1
            out.append(tuple(target))
    return out


def pilot_s14():
    before = ASSERTIONS
    all_states = set()
    length = 6
    for value in range(32):
        initial = (value,) + (0,) * (length - 1)
        queue = deque([initial])
        seen = {initial}
        terminals = set()
        while queue:
            state = queue.popleft()
            all_states.add(state)
            successors = carry_successors(state)
            if not successors:
                terminals.add(state)
            for target in successors:
                check(sum((1 << i) * x for i, x in enumerate(target)) == value)
                check(sum(target) == sum(state) - 1)
                if target not in seen:
                    seen.add(target)
                    queue.append(target)
        binary = tuple((value >> i) & 1 for i in range(length))
        check(terminals == {binary})
        check(all(sum(state) - bitcount(value) >= 0 for state in seen))
    finish(
        "S14",
        "finite digit-count vectors / active-site binary carrying",
        "all values N=0..31 in six digit positions",
        len(all_states),
        "KILL_OWNER_CLASSICAL",
        "Every schedule reaches the binary expansion and uses N-popcount(N) carries; abelian carry network.",
        before,
    )


# ---------------------------------------------------------------------------
# S15: path sandpile with two sinks


def sandpile_successors(state):
    length = len(state)
    out = []
    for i, chips in enumerate(state):
        if chips >= 2:
            target = list(state)
            target[i] -= 2
            if i > 0:
                target[i - 1] += 1
            if i + 1 < length:
                target[i + 1] += 1
            out.append(tuple(target))
    return out


def sandpile_weight(state):
    length = len(state)
    return sum((i + 1) * (length - i) * chips for i, chips in enumerate(state))


def pilot_s15():
    before = ASSERTIONS
    visited_total = 0
    for length in range(1, 6):
        @lru_cache(None)
        def endpoints(state):
            successors = sandpile_successors(state)
            if not successors:
                return frozenset((state,))
            answer = set()
            for target in successors:
                check(sandpile_weight(target) == sandpile_weight(state) - 2)
                answer.update(endpoints(target))
            return frozenset(answer)

        for state in product(range(4), repeat=length):
            result = endpoints(state)
            check(len(result) == 1)
            check(all(chips < 2 for chips in next(iter(result))))
        visited_total += endpoints.cache_info().currsize
    finish(
        "S15",
        "chip configurations on sinked paths / asynchronous threshold firing",
        "initial heights 0..3 on path lengths 1..5",
        visited_total,
        "KILL_OWNER_CLASSICAL",
        "A quadratic Green weight drops by two and all schedules stabilize identically; standard abelian sandpile.",
        before,
    )


# ---------------------------------------------------------------------------
# S16: random-to-front scheduling


def move_to_front(permutation_state, position):
    return (
        (permutation_state[position],)
        + permutation_state[:position]
        + permutation_state[position + 1 :]
    )


def pilot_s16():
    before = ASSERTIONS
    states = 0
    for n in range(1, 9):
        perms = list(permutations(range(n)))
        states += len(perms)
        incoming = Counter()
        for state in perms:
            targets = [move_to_front(state, position) for position in range(n)]
            check(all(sorted(target) == list(range(n)) for target in targets))
            for target in targets:
                incoming[target] += 1
        check(set(incoming) == set(perms))
        check(all(incoming[state] == n for state in perms))
    finish(
        "S16",
        "permutations / uniformly selected item moved to front",
        "all permutations n=1..8",
        states,
        "KILL_OWNER_CLASSICAL",
        "The transition matrix is doubly stochastic here; this is the uniform Tsetlin/random-to-front chain.",
        before,
    )


# ---------------------------------------------------------------------------
# S17: lazy adjacent-descent sorting


def permutation_inversions(state):
    return sum(state[i] > state[j] for i in range(len(state)) for j in range(i + 1, len(state)))


def pilot_s17():
    before = ASSERTIONS
    states = 0
    for n in range(1, 9):
        identity = tuple(range(n))
        absorbers = 0
        for state in permutations(range(n)):
            states += 1
            active = 0
            for i in range(n - 1):
                target = state
                if state[i] > state[i + 1]:
                    target_list = list(state)
                    target_list[i], target_list[i + 1] = target_list[i + 1], target_list[i]
                    target = tuple(target_list)
                    active += 1
                    check(permutation_inversions(target) == permutation_inversions(state) - 1)
                check(sorted(target) == list(range(n)))
            if active == 0:
                absorbers += 1
                check(state == identity)
        check(absorbers == 1)
    finish(
        "S17",
        "permutations / random-bond adjacent descent swap",
        "all permutations n=1..8",
        states,
        "KILL_OWNER_CLASSICAL",
        "Inversion number drops one per effective move and identity is unique; 0-Hecke/bubble-sort exclusion boundary is direct.",
        before,
    )


# ---------------------------------------------------------------------------
# S18: random-transposition coagulation/fragmentation


def permutation_cycle_count(state):
    seen = set()
    cycles = 0
    for start in range(len(state)):
        if start not in seen:
            cycles += 1
            v = start
            while v not in seen:
                seen.add(v)
                v = state[v]
    return cycles


def transpose_positions(state, i, j):
    target = list(state)
    target[i], target[j] = target[j], target[i]
    return tuple(target)


def pilot_s18():
    before = ASSERTIONS
    states = 0
    for n in range(2, 8):
        for state in permutations(range(n)):
            states += 1
            cycles = permutation_cycle_count(state)
            for i, j in combinations(range(n), 2):
                target = transpose_positions(state, i, j)
                check(transpose_positions(target, i, j) == state)
                check(abs(permutation_cycle_count(target) - cycles) == 1)
    finish(
        "S18",
        "permutations / random-transposition cycle split-merge",
        "all permutations n=2..7",
        states,
        "KILL_OWNER_CLASSICAL",
        "Every step splits or merges one cycle and the kernel is symmetric; classical random-transposition coagulation-fragmentation.",
        before,
    )


# ---------------------------------------------------------------------------
# S19: meet-join comparators on tuples of subsets


def set_comparator_inversions(rows, q):
    total = 0
    for element in range(q):
        word = sum(((row >> element) & 1) << i for i, row in enumerate(rows))
        total += inversion_count_bits(word, len(rows))
    return total


def set_comparator_terminal(rows, q):
    m = len(rows)
    terminal = [0] * m
    for element in range(q):
        count = sum((row >> element) & 1 for row in rows)
        for i in range(m - count, m):
            terminal[i] |= 1 << element
    return tuple(terminal)


def pilot_s19():
    before = ASSERTIONS
    states = 0
    for m in range(2, 6):
        for q in range(1, 4):
            basin_counts = Counter()
            for rows in product(range(1 << q), repeat=m):
                states += 1
                terminal = set_comparator_terminal(rows, q)
                basin_counts[terminal] += 1
                active = []
                for i in range(m - 1):
                    left, right = rows[i], rows[i + 1]
                    if left & ~right:
                        target = list(rows)
                        target[i] = left & right
                        target[i + 1] = left | right
                        target = tuple(target)
                        active.append(target)
                        check(set_comparator_inversions(target, q) < set_comparator_inversions(rows, q))
                        check(set_comparator_terminal(target, q) == terminal)
                if not active:
                    check(rows == terminal)
            for terminal, count in basin_counts.items():
                predicted = 1
                for element in range(q):
                    multiplicity = sum((row >> element) & 1 for row in terminal)
                    predicted *= comb(m, multiplicity)
                check(count == predicted)
    finish(
        "S19",
        "tuples in a Boolean lattice / adjacent meet-join comparator",
        "all m-tuples for m=2..5 and ground size q=1..3",
        states,
        "KILL_DECOMPOSES_TO_CLASSICAL",
        "Unique nested endpoint and basin product prod C(m,k_e), but the map decomposes elementwise into coupled 0-Hecke binary sorts.",
        before,
    )


# ---------------------------------------------------------------------------
# S20: random peak deletion in Dyck words


def dyck_words(n):
    out = []

    def rec(prefix, opened, closed):
        if opened == n and closed == n:
            out.append(prefix)
            return
        if opened < n:
            rec(prefix + "(", opened + 1, closed)
        if closed < opened:
            rec(prefix + ")", opened, closed + 1)

    rec("", 0, 0)
    return out


def is_dyck(word):
    height = 0
    for letter in word:
        height += 1 if letter == "(" else -1
        if height < 0:
            return False
    return height == 0


def pilot_s20():
    before = ASSERTIONS
    states = 0
    for n in range(0, 11):
        words = dyck_words(n)
        states += len(words)
        check(len(words) == comb(2 * n, n) // (n + 1))
        for word in words:
            peaks = [i for i in range(len(word) - 1) if word[i : i + 2] == "()"]
            check(bool(peaks) == (n > 0))
            for i in peaks:
                target = word[:i] + word[i + 2 :]
                check(is_dyck(target))
                check(len(target) == len(word) - 2)
    finish(
        "S20",
        "Dyck words / uniformly selected peak deletion",
        "all Dyck words of semilength 0..10",
        states,
        "KILL_SCHEDULE_ONLY",
        "Absorption time is deterministically the semilength; residual scheduling histories reduce to classical tree/poset deletion orders.",
        before,
    )


# ---------------------------------------------------------------------------
# S21: free equal-pair cancellation


def free_reduce(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def pilot_s21():
    before = ASSERTIONS
    states = 0
    for n in range(0, 17):
        for word in product((0, 1), repeat=n):
            states += 1
            normal = free_reduce(word)
            check(all(normal[i] != normal[i + 1] for i in range(len(normal) - 1)))
            for i in range(n - 1):
                if word[i] == word[i + 1]:
                    target = word[:i] + word[i + 2 :]
                    check(free_reduce(target) == normal)
    finish(
        "S21",
        "binary words of variable length / equal-neighbor pair cancellation",
        "all source words length 0..16",
        states,
        "KILL_STANDARD_NORMAL_FORM",
        "Every schedule has the same alternating normal form; this is free-product reduction/confluence, not a new stochastic law.",
        before,
    )


# ---------------------------------------------------------------------------
# S22: sink flips on cyclic orientations


def pilot_s22():
    before = ASSERTIONS
    states = 0
    recurrent_summary = []
    for n in range(3, 11):
        nodes = list(range(1 << n))
        states += len(nodes)
        adjacency = {}
        for mask in nodes:
            targets = []
            for v in range(n):
                left_edge = (v - 1) % n
                right_edge = v
                left_points_in = (mask >> left_edge) & 1
                right_points_in = not ((mask >> right_edge) & 1)
                if left_points_in and right_points_in:
                    target = mask ^ (1 << left_edge) ^ (1 << right_edge)
                    targets.append(target)
                    check(0 <= target < (1 << n))
            adjacency[mask] = tuple(targets) if targets else (mask,)
        components = tarjan_scc(nodes, adjacency)
        closed = closed_components(components, adjacency)
        check(bool(closed))
        recurrent_summary.append((n, len(closed), max(map(len, closed))))
    finish(
        "S22",
        "acyclic/cyclic orientations of a cycle / asynchronous sink-to-source flip",
        "all orientations for cycle lengths 3..10",
        states,
        "KILL_OWNER_CLASSICAL",
        "Nontrivial recurrent classes appear, but sink firing is the standard chip-firing/acyclic-orientation action.",
        before,
    )


# ---------------------------------------------------------------------------
# S23: local-minimum triple rotation


def pilot_s23():
    before = ASSERTIONS
    states = 0
    nontrivial_closed = 0
    for n in range(3, 9):
        nodes = list(permutations(range(n)))
        states += len(nodes)
        adjacency = {}
        for state in nodes:
            targets = []
            for i in range(1, n - 1):
                if state[i] < state[i - 1] and state[i] < state[i + 1]:
                    target = (
                        state[: i - 1]
                        + (state[i], state[i + 1], state[i - 1])
                        + state[i + 2 :]
                    )
                    targets.append(target)
                    check(sorted(target) == list(range(n)))
            adjacency[state] = tuple(targets) if targets else (state,)
        components = tarjan_scc(nodes, adjacency)
        closed = closed_components(components, adjacency)
        nontrivial_closed += sum(len(component) > 1 for component in closed)
        check(bool(closed))
    finish(
        "S23",
        "permutations / active local-minimum triple rotation",
        "all permutations n=3..8",
        states,
        "KILL_WEAK_STRUCTURE",
        f"Exact SCC scan has {nontrivial_closed} nontrivial closed classes through n=8; no monotone clock or compact recurrent contract.",
        before,
    )


# ---------------------------------------------------------------------------
# S24: oriented 101->010 rewrite


def braid_successors(mask, n):
    out = []
    for i in range(n - 2):
        if ((mask >> i) & 7) == 5:
            out.append((mask & ~(7 << i)) | (2 << i))
    return out


def pilot_s24():
    before = ASSERTIONS
    states = 0
    nonconfluent = 0
    max_endpoints = 1
    for n in range(1, 16):
        @lru_cache(None)
        def endpoints(mask):
            successors = braid_successors(mask, n)
            if not successors:
                return frozenset((mask,))
            answer = set()
            for target in successors:
                answer.update(endpoints(target))
            return frozenset(answer)

        for mask in range(1 << n):
            states += 1
            successors = braid_successors(mask, n)
            for target in successors:
                check(bitcount(target) == bitcount(mask) - 1)
                check(target < mask)
            if n <= 12:
                endpoint_set = endpoints(mask)
                if len(endpoint_set) > 1:
                    nonconfluent += 1
                max_endpoints = max(max_endpoints, len(endpoint_set))
    check(nonconfluent > 0)
    check(max_endpoints >= 9)
    finish(
        "S24",
        "fixed-length binary words / oriented 101->010 local rewrite",
        "all words n=1..15; endpoint sets n=1..12",
        states,
        "KILL_NONCONFLUENT_COMPLEXITY",
        f"Termination is immediate, but {nonconfluent} states through n=12 have multiple normal forms (maximum {max_endpoints}); no compact basin signal.",
        before,
    )


# ---------------------------------------------------------------------------
# S25: fair binary active-boundary deletion (replacement attempt; owner kill)


def fair_boundary_successors(word):
    events = []
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            events.append(word[:i] + word[i + 1 :])
            events.append(word[: i + 1] + word[i + 2 :])
    return events


@lru_cache(None)
def fair_boundary_terminal_size_distribution(word):
    events = fair_boundary_successors(word)
    if not events:
        return ((len(word), Fraction(1)),)
    total = defaultdict(Fraction)
    for target in events:
        for terminal_size, probability in fair_boundary_terminal_size_distribution(target):
            total[terminal_size] += probability / len(events)
    return tuple(sorted(total.items()))


def pilot_s25():
    before = ASSERTIONS
    for n in range(1, 11):
        for word in product((0, 1), repeat=n):
            events = fair_boundary_successors(word)
            active = sum(word[i] != word[i + 1] for i in range(n - 1))
            check(len(events) == 2 * active)
            for target in events:
                check(len(target) == n - 1)
                check(all(letter in (0, 1) for letter in target))

    alternating = []
    for n in range(1, 18):
        word = tuple(i % 2 for i in range(n))
        distribution = dict(fair_boundary_terminal_size_distribution(word))
        check(sum(distribution.values(), Fraction()) == 1)
        alternating.append(distribution)

    for k in range(1, 9):
        check(alternating[2 * k - 2] == alternating[2 * k - 1])

    for k in range(1, 8):
        old = alternating[2 * k - 2]
        new = alternating[2 * (k + 1) - 2]
        denominator = 2 * k
        for terminal_size in range(1, k + 2):
            predicted = old.get(terminal_size, Fraction()) * Fraction(
                denominator - terminal_size, denominator
            )
            predicted += old.get(terminal_size - 1, Fraction()) * Fraction(
                terminal_size - 1, denominator
            )
            check(new.get(terminal_size, Fraction()) == predicted)

    for k in range(1, 9):
        distribution = alternating[2 * k - 2]
        for order in range(1, 6):
            actual = sum(
                rising_factorial(size, order) * probability
                for size, probability in distribution.items()
            )
            predicted = Fraction(factorial(order))
            for j in range(1, k):
                predicted *= Fraction(2 * j + order, 2 * j)
            check(actual == predicted)

    finish(
        "S25",
        "variable binary words / fair active-boundary endpoint deletion",
        "all words length 1..10; alternating full terminal-size law length 1..17",
        fair_boundary_terminal_size_distribution.cache_info().currsize,
        "KILL_OWNER_INTERNAL",
        "Paired alternating lengths obey exactly the PD(1/2,0) block-count PGF recurrence; this is an owned Pitman-Yor law behind another adjacent-coalescence wrapper.",
        before,
    )


# ---------------------------------------------------------------------------
# S26: random greedy matching on complete rooted binary trees


def complete_binary_tree_edges(height):
    internal = (1 << height) - 1
    edges = []
    for vertex in range(internal):
        edges.append((vertex, 2 * vertex + 1))
        edges.append((vertex, 2 * vertex + 2))
    return tuple(edges)


def pilot_s26():
    before = ASSERTIONS
    state_total = 0
    last_size_law = None
    last_root_probability = None
    for height in range(0, 4):
        vertex_count = (1 << (height + 1)) - 1
        edges = complete_binary_tree_edges(height)

        @lru_cache(None)
        def greedy_law(remaining):
            available = tuple(
                (u, v)
                for u, v in edges
                if ((remaining >> u) & 1) and ((remaining >> v) & 1)
            )
            if not available:
                check(
                    all(
                        not (((remaining >> u) & 1) and ((remaining >> v) & 1))
                        for u, v in edges
                    )
                )
                return (((0, False), Fraction(1)),)
            total = defaultdict(Fraction)
            for u, v in available:
                target = remaining & ~(1 << u) & ~(1 << v)
                check(bitcount(target) == bitcount(remaining) - 2)
                for (size, root_matched), probability in greedy_law(target):
                    total[(size + 1, root_matched or u == 0 or v == 0)] += (
                        probability / len(available)
                    )
            check(sum(total.values(), Fraction()) == 1)
            return tuple(sorted(total.items()))

        initial = (1 << vertex_count) - 1
        joint = dict(greedy_law(initial))
        check(sum(joint.values(), Fraction()) == 1)
        size_law = defaultdict(Fraction)
        for (size, root_matched), probability in joint.items():
            size_law[size] += probability
        check(sum(size_law.values(), Fraction()) == 1)
        root_probability = sum(
            probability
            for (size, root_matched), probability in joint.items()
            if root_matched
        )
        check(Fraction(0) <= root_probability <= 1)
        state_total += greedy_law.cache_info().currsize
        last_size_law = dict(size_law)
        last_root_probability = root_probability

    check(last_size_law == {4: Fraction(9, 49), 5: Fraction(40, 49)})
    check(last_root_probability == Fraction(40, 49))
    finish(
        "S26",
        "complete rooted binary trees / uniformly random greedy edge matching",
        "heights 0..3; complete reachable remaining-vertex recursion",
        state_total,
        "KILL_OWNER_NO_ALL_PARAMETER_RESIDUAL",
        "At height 3 the size law is {4:9/49,5:40/49} and root-match probability is 40/49, but no new all-height closure survives generic random-greedy-matching/RSA ownership.",
        before,
    )


def main():
    pilots = [
        pilot_s01,
        pilot_s02,
        pilot_s03,
        pilot_s04,
        pilot_s05,
        pilot_s06,
        pilot_s07,
        pilot_s08,
        pilot_s09,
        pilot_s10,
        pilot_s11,
        pilot_s12,
        pilot_s13,
        pilot_s14,
        pilot_s15,
        pilot_s16,
        pilot_s17,
        pilot_s18,
        pilot_s19,
        pilot_s20,
        pilot_s21,
        pilot_s22,
        pilot_s23,
        pilot_s24,
        pilot_s25,
        pilot_s26,
    ]
    for pilot in pilots:
        pilot()

    check(len(RESULTS) == 26)
    check(sum(result["decision"] == "PROMOTE" for result in RESULTS) == 1)
    check(all(result["states"] > 0 for result in RESULTS))
    check(all(result["assertions"] > 0 for result in RESULTS))

    print("stochastic/local-rewrite exact scouting: PASS")
    print("systems=26; promoted=1; arithmetic=integer+Fraction; randomness=none")
    for result in RESULTS:
        print(
            "{code}|family={family}|range={range}|states={states}|assertions={assertions}|"
            "decision={decision}|signal={signal}".format(**result)
        )
    print(f"exact_assertions={ASSERTIONS}")
    print("promoted=S02")
    print("internal_firewall=P90,P101,P114,P117,P121,P126")
    print("bounded_nonhit_is_not_novelty=YES")


if __name__ == "__main__":
    main()
