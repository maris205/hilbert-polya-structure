#!/usr/bin/env python3
"""Independent exact pilots for P166 replacement discovery round 3.

The verifier imports no project code.  It builds five carriers literally:
permutations, residues, complete deterministic automata, plane full binary
trees, and perfect matchings with a stochastic repair kernel.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb, factorial, gcd


ASSERTIONS = 0


def claim(value: bool, note: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not value:
        raise AssertionError(note)


def digest(rows) -> str:
    return sha256("\n".join(map(str, rows)).encode()).hexdigest()


# ---------------------------------------------------------------------------
# PLP: simultaneously prune cyclic local maxima from permutation cycles.


def permutation_cycles(p):
    seen = set()
    answer = []
    for start in range(len(p)):
        if start in seen:
            continue
        cycle = []
        x = start
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = p[x]
        answer.append(tuple(cycle))
    return tuple(answer)


def plp_step(p):
    q = list(range(len(p)))
    for cycle in permutation_cycles(p):
        m = len(cycle)
        if m == 1:
            continue
        if m == 2:
            peaks = {max(cycle)}
        else:
            peaks = {
                x for i, x in enumerate(cycle)
                if x > cycle[i - 1] and x > cycle[(i + 1) % m]
            }
        claim(bool(peaks), "a nontrivial cyclic word has a local maximum")
        survivors = [x for x in cycle if x not in peaks]
        for x in peaks:
            q[x] = x
        if len(survivors) == 1:
            q[survivors[0]] = survivors[0]
        else:
            for a, b in zip(survivors, survivors[1:] + survivors[:1]):
                q[a] = b
    return tuple(q)


@lru_cache(None)
def bounded_cartesian_permutations(k: int, height: int) -> int:
    """Permutations of k labels whose min-Cartesian tree has <=height levels."""
    if k == 0:
        return 1
    if height == 0:
        return 0
    return sum(
        comb(k - 1, left)
        * bounded_cartesian_permutations(left, height - 1)
        * bounded_cartesian_permutations(k - 1 - left, height - 1)
        for left in range(k)
    )


@lru_cache(None)
def plp_cdf(n: int, t: int) -> int:
    """Number of n-permutations absorbed by time t, by labelled cycles."""
    if n == 0:
        return 1
    answer = 0
    for cycle_size in range(1, n + 1):
        allowed_cycles = bounded_cartesian_permutations(cycle_size - 1, t)
        answer += comb(n - 1, cycle_size - 1) * allowed_cycles * plp_cdf(n - cycle_size, t)
    return answer


def absorption_depth(step, state, fixed):
    depth = 0
    while not fixed(state):
        state = step(state)
        depth += 1
        claim(depth < 100)
    return depth


def verify_plp():
    summary = []
    transition_rows = []
    for n in range(9):
        states = list(permutations(range(n)))
        fibres = Counter()
        depths = Counter()
        identity = tuple(range(n))
        for p in states:
            target = plp_step(p)
            claim(tuple(sorted(target)) == identity)
            fibres[target] += 1
            d = absorption_depth(plp_step, p, lambda x: x == identity)
            depths[d] += 1
            transition_rows.append((n, p, target, d))
        for t in range(n + 1):
            claim(sum(v for d, v in depths.items() if d <= t) == plp_cdf(n, t))
        max_depth = max(depths, default=0)
        claim(max_depth == max(0, n - 1))
        deepest = depths[max_depth]
        claim(deepest == (1 if n <= 1 else 1 << (n - 2)))
        claim(set(plp_step(p) for p in states if p == plp_step(p)) == {identity})
        summary.append((n, len(states), len(fibres), max(fibres.values()), tuple(sorted(depths.items()))))
    return summary, digest(transition_rows)


# ---------------------------------------------------------------------------
# UZD: step left at units and right at zero divisors/nonunits modulo m.


def is_unit(x: int, modulus: int) -> bool:
    return gcd(x, modulus) == 1


def uzd_step(x: int, modulus: int) -> int:
    return (x - 1) % modulus if is_unit(x, modulus) else (x + 1) % modulus


def uzd_coordinates(modulus: int):
    unit = [is_unit(x, modulus) for x in range(modulus)]
    boundaries = [z for z in range(modulus) if not unit[z] and unit[(z + 1) % modulus]]
    claim(bool(boundaries))
    coordinates = {}
    runs = []
    for z in boundaries:
        alpha = 1
        while alpha < modulus and not unit[(z - alpha) % modulus]:
            alpha += 1
        one = (z + 1) % modulus
        beta = 1
        while beta < modulus and unit[(one + beta) % modulus]:
            beta += 1
        runs.append((z, alpha, beta))
        for j in range(alpha):
            x = (z - j) % modulus
            claim(x not in coordinates)
            coordinates[x] = (z, 0, j)
        for j in range(beta):
            x = (one + j) % modulus
            claim(x not in coordinates)
            coordinates[x] = (z, 1, j)
    claim(len(coordinates) == modulus)
    return coordinates, tuple(runs)


def uzd_formula(x: int, t: int, modulus: int, coordinates) -> int:
    z, side, distance = coordinates[x]
    one = (z + 1) % modulus
    if t <= distance:
        if side == 0:
            return (z - (distance - t)) % modulus
        return (one + (distance - t)) % modulus
    remainder = t - distance
    if side == 0:
        return one if remainder % 2 else z
    return z if remainder % 2 else one


def verify_uzd():
    displayed = []
    orbit_rows = []
    for modulus in range(2, 81):
        coordinates, runs = uzd_coordinates(modulus)
        depths = Counter(value[2] for value in coordinates.values())
        recurrent = {x for x, value in coordinates.items() if value[2] == 0}
        claim(len(recurrent) == 2 * len(runs))
        claim(all(uzd_step(uzd_step(x, modulus), modulus) == x for x in recurrent))
        for x in range(modulus):
            literal = x
            for t in range(2 * modulus + 1):
                claim(literal == uzd_formula(x, t, modulus, coordinates))
                literal = uzd_step(literal, modulus)
        for t in range(2 * modulus + 1):
            literal_fibres = Counter()
            formula_fibres = Counter()
            for x in range(modulus):
                y = x
                for _ in range(t):
                    y = uzd_step(y, modulus)
                literal_fibres[y] += 1
                formula_fibres[uzd_formula(x, t, modulus, coordinates)] += 1
            claim(literal_fibres == formula_fibres)
        maximum = max(depths)
        claim(maximum == max(max(a, b) - 1 for z, a, b in runs))
        orbit_rows.append((modulus, runs, tuple(sorted(depths.items()))))
        if modulus <= 20:
            displayed.append((modulus, len(runs), maximum, tuple((a, b) for z, a, b in runs)))
    return displayed, digest(orbit_rows)


# ---------------------------------------------------------------------------
# SCQ: quotient an automaton by the least transition congruence generated by
# all one-letter collision pairs, and repeat.


def scq_step(partition, transitions):
    m = len(partition)
    parent = list(range(m))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x == y:
            return False
        if x > y:
            x, y = y, x
        parent[y] = x
        return True

    for letter in transitions:
        seen = {}
        for state, target in enumerate(letter):
            if target in seen:
                union(state, seen[target])
            else:
                seen[target] = state

    changed = True
    while changed:
        changed = False
        for p in range(m):
            for q in range(p):
                if find(p) == find(q):
                    for letter in transitions:
                        changed |= union(letter[p], letter[q])

    groups = defaultdict(list)
    for state in range(m):
        groups[find(state)].append(state)
    groups = sorted(groups.values(), key=lambda I: min(x for i in I for x in partition[i]))
    new_partition = tuple(
        tuple(sorted(x for i in I for x in partition[i])) for I in groups
    )
    old_to_new = {i: j for j, I in enumerate(groups) for i in I}
    new_transitions = []
    for letter in transitions:
        induced = []
        for I in groups:
            images = {old_to_new[letter[i]] for i in I}
            claim(len(images) == 1, "transition congruence must induce a quotient map")
            induced.append(images.pop())
        new_transitions.append(tuple(induced))
    return new_partition, tuple(new_transitions)


def scq_depth(n: int, transitions):
    partition = tuple((i,) for i in range(n))
    rows = []
    while True:
        rows.append((partition, transitions))
        new = scq_step(partition, transitions)
        if new == (partition, transitions):
            break
        claim(len(new[0]) < len(partition))
        partition, transitions = new
    return len(rows) - 1, rows[-1], tuple(rows)


def verify_scq():
    summary = []
    trajectory_rows = []
    for n in range(1, 5):
        depths = Counter()
        endpoints = Counter()
        total = n ** (2 * n)
        for flat in product(range(n), repeat=2 * n):
            transitions = (tuple(flat[:n]), tuple(flat[n:]))
            depth, endpoint, trajectory = scq_depth(n, transitions)
            partition, terminal_maps = endpoint
            claim(all(len(set(letter)) == len(letter) for letter in terminal_maps))
            claim(depth <= n - 1)
            depths[depth] += 1
            endpoints[len(partition)] += 1
            trajectory_rows.append((n, transitions, depth, endpoint))
        claim(sum(depths.values()) == total)
        claim(max(depths) == n - 1)
        summary.append((n, total, tuple(sorted(depths.items())), tuple(sorted(endpoints.items()))))
    return summary, digest(trajectory_rows)


# ---------------------------------------------------------------------------
# RHR: rotate the root of a plane full binary tree toward a child whose size
# exceeds the other child by at least two.


@lru_cache(None)
def plane_trees(internal_nodes: int):
    if internal_nodes == 0:
        return (None,)
    return tuple(
        (left, right)
        for left_size in range(internal_nodes)
        for left in plane_trees(left_size)
        for right in plane_trees(internal_nodes - 1 - left_size)
    )


@lru_cache(None)
def tree_size(tree) -> int:
    return 0 if tree is None else 1 + tree_size(tree[0]) + tree_size(tree[1])


def rhr_step(tree):
    if tree is None:
        return None
    left, right = tree
    a, b = tree_size(left), tree_size(right)
    if a > b + 1:
        A, B = left
        return A, (B, right)
    if b > a + 1:
        B, C = right
        return (left, B), C
    return tree


def rhr_predecessors(target):
    if target is None:
        return {None}
    left, right = target
    answer = set()
    if abs(tree_size(left) - tree_size(right)) <= 1:
        answer.add(target)
    if right is not None:
        B, C = right
        candidate = ((left, B), C)
        if rhr_step(candidate) == target:
            answer.add(candidate)
    if left is not None:
        A, B = left
        candidate = (A, (B, right))
        if rhr_step(candidate) == target:
            answer.add(candidate)
    return answer


def functional_shape(step, state):
    seen = {}
    while state not in seen:
        seen[state] = len(seen)
        state = step(state)
    return seen[state], len(seen) - seen[state]


def verify_rhr():
    summary = []
    transition_rows = []
    for n in range(12):
        states = plane_trees(n)
        state_set = set(states)
        fibres = Counter(rhr_step(tree) for tree in states)
        shapes = Counter()
        for tree in states:
            target = rhr_step(tree)
            claim(target in state_set)
            shape = functional_shape(rhr_step, tree)
            claim(shape[1] in (1, 2))
            shapes[shape] += 1
            transition_rows.append((n, tree, target, shape))
        for target in states:
            roots = rhr_predecessors(target)
            claim(roots.issubset(state_set))
            claim(fibres[target] == len(roots))
            claim(len(roots) <= 3)
        max_tail = max(t for t, p in shapes)
        claim(max_tail == max(0, (n - 1) // 2))
        summary.append(
            (n, len(states), len(fibres), max(fibres.values()), max_tail,
             max(p for t, p in shapes), tuple(sorted(shapes.items())))
        )
    return summary, digest(transition_rows)


# ---------------------------------------------------------------------------
# RMR: choose a reference pair uniformly and repair it in a perfect matching.


@lru_cache(None)
def matching_pairs(vertices):
    vertices = tuple(vertices)
    if not vertices:
        return ((),)
    first = vertices[0]
    answer = []
    for i in range(1, len(vertices)):
        second = vertices[i]
        rest = vertices[1:i] + vertices[i + 1:]
        for tail in matching_pairs(rest):
            answer.append(tuple(sorted(((first, second),) + tail)))
    return tuple(answer)


def partner_form(pair_count: int, pairs):
    p = list(range(2 * pair_count))
    for a, b in pairs:
        p[a], p[b] = b, a
    return tuple(p)


def rmr_repair(matching, reference_index: int):
    a, b = 2 * reference_index, 2 * reference_index + 1
    if matching[a] == b:
        return matching
    x, y = matching[a], matching[b]
    result = list(matching)
    for u, v in ((a, b), (x, y)):
        result[u], result[v] = v, u
    return tuple(result)


def matching_profile(matching):
    m = len(matching) // 2
    graph = [set() for _ in range(m)]
    for a in range(2 * m):
        b = matching[a]
        if a < b:
            i, j = a // 2, b // 2
            graph[i].add(j)
            graph[j].add(i)
    remaining = set(range(m))
    parts = []
    while remaining:
        start = min(remaining)
        component = {start}
        stack = [start]
        while stack:
            x = stack.pop()
            for y in graph[x]:
                if y not in component:
                    component.add(y)
                    stack.append(y)
        remaining.difference_update(component)
        parts.append(len(component))
    return tuple(sorted(parts))


def profile_successor(profile, part: int):
    values = list(profile)
    values.remove(part)
    values.extend((1, part - 1))
    return tuple(sorted(values))


@lru_cache(None)
def rmr_expected(profile):
    m = sum(profile)
    if all(k == 1 for k in profile):
        return Fraction(0)
    multiplicity = Counter(profile)
    fixed = multiplicity[1]
    future = Fraction(0)
    for k, number in multiplicity.items():
        if k >= 2:
            future += k * number * rmr_expected(profile_successor(profile, k))
    return (m + future) / (m - fixed)


def odd_double_factorial(m: int) -> int:
    answer = 1
    for k in range(1, m + 1):
        answer *= 2 * k - 1
    return answer


def onto_words(time: int, used_labels: int) -> int:
    return sum(
        (-1) ** j * comb(used_labels, j) * (used_labels - j) ** time
        for j in range(used_labels + 1)
    )


def rmr_cdf_formula(profile, time: int) -> Fraction:
    choices = Counter({0: 1})
    for part in profile:
        new = Counter()
        for used, count in choices.items():
            new[used + part] += count
            new[used + part - 1] += count * part
        choices = new
    words = sum(count * onto_words(time, used) for used, count in choices.items())
    return Fraction(words, sum(profile) ** time)


@lru_cache(None)
def rmr_cdf_recursion(profile, time: int) -> Fraction:
    if all(part == 1 for part in profile):
        return Fraction(1)
    if time == 0:
        return Fraction(0)
    m = sum(profile)
    multiplicity = Counter(profile)
    answer = Fraction(multiplicity[1], m) * rmr_cdf_recursion(profile, time - 1)
    for part, number in multiplicity.items():
        if part >= 2:
            answer += Fraction(part * number, m) * rmr_cdf_recursion(
                profile_successor(profile, part), time - 1
            )
    return answer


def verify_rmr():
    summary = []
    transition_rows = []
    for m in range(1, 7):
        states = [partner_form(m, pairs) for pairs in matching_pairs(tuple(range(2 * m)))]
        claim(len(states) == odd_double_factorial(m))
        state_set = set(states)
        roots = defaultdict(set)
        marked = Counter()
        profile_counts = Counter()
        deepest = 0
        for matching in states:
            profile = matching_profile(matching)
            profile_counts[profile] += 1
            accepted_distance = m - len(profile)
            deepest = max(deepest, accepted_distance)
            literal_profile_kernel = Counter()
            for reference_index in range(m):
                target = rmr_repair(matching, reference_index)
                claim(target in state_set)
                target_profile = matching_profile(target)
                literal_profile_kernel[target_profile] += 1
                roots[target].add(matching)
                marked[target] += 1
                if target != matching:
                    claim(m - len(target_profile) == accepted_distance - 1)
                transition_rows.append((m, matching, reference_index, target))
            expected_kernel = Counter()
            multiplicity = Counter(profile)
            expected_kernel[profile] += multiplicity[1]
            for k, number in multiplicity.items():
                if k >= 2:
                    expected_kernel[profile_successor(profile, k)] += k * number
            claim(literal_profile_kernel == expected_kernel)
        claim(deepest == m - 1)
        deepest_count = sum(number for profile, number in profile_counts.items() if len(profile) == 1)
        claim(deepest_count == (1 << (m - 1)) * factorial(m - 1))
        image_count = 0
        for target in states:
            fixed = sum(target[2 * i] == 2 * i + 1 for i in range(m))
            wanted_roots = 0 if fixed == 0 else 1 + fixed * (2 * m - fixed - 1)
            wanted_marked = fixed * (2 * m - 1)
            claim(len(roots[target]) == wanted_roots)
            claim(marked[target] == wanted_marked)
            if fixed:
                image_count += 1
        inclusion_exclusion_image = sum(
            (-1) ** (j + 1) * comb(m, j) * odd_double_factorial(m - j)
            for j in range(1, m + 1)
        )
        claim(image_count == inclusion_exclusion_image)
        for profile in profile_counts:
            for time in range(2 * m + 4):
                claim(rmr_cdf_formula(profile, time) == rmr_cdf_recursion(profile, time))
        harmonic_tail = sum((Fraction(m, k) for k in range(2, m + 1)), Fraction(0))
        claim(rmr_expected((m,)) == harmonic_tail)
        max_expectation = max(rmr_expected(profile) for profile in profile_counts)
        summary.append(
            (m, len(states), len(profile_counts), image_count, deepest,
             deepest_count, str(rmr_expected((m,))), str(max_expectation))
        )
    return summary, digest(transition_rows)


# ---------------------------------------------------------------------------
# OST: contract every nonroot vertex having odd fringe-subtree size; surviving
# descendants are promoted, in plane order, to the nearest surviving ancestor.


@lru_cache(None)
def positive_compositions(total: int):
    if total == 0:
        return ((),)
    answer = []
    for first in range(1, total + 1):
        for rest in positive_compositions(total - first):
            answer.append((first,) + rest)
    return tuple(answer)


@lru_cache(None)
def rooted_plane_trees(vertices: int):
    if vertices == 1:
        return ((),)
    answer = []
    for sizes in positive_compositions(vertices - 1):
        families = [rooted_plane_trees(size) for size in sizes]
        for children in product(*families):
            answer.append(tuple(children))
    return tuple(answer)


@lru_cache(None)
def rooted_size(tree) -> int:
    return 1 + sum(rooted_size(child) for child in tree)


def ost_forest(tree, force_root=False):
    promoted = tuple(
        descendant
        for child in tree
        for descendant in ost_forest(child, False)
    )
    if force_root or rooted_size(tree) % 2 == 0:
        return (promoted,)
    return promoted


def ost_step(tree):
    result = ost_forest(tree, True)
    claim(len(result) == 1)
    return result[0]


def ost_iterate(tree, time: int):
    for _ in range(time):
        tree = ost_step(tree)
    return tree


def ost_depth(tree):
    root = ()
    return absorption_depth(ost_step, tree, lambda x: x == root)


def c_constant(time: int) -> int:
    answer = 1
    for j in range(1, time + 1):
        answer *= (2 ** j - 1) ** (2 ** (time - j))
    return answer


def ost_minimal_fibre(time: int, target) -> int:
    exponent = 2 ** (time + 1) - 2
    c = c_constant(time)
    answer = c ** (rooted_size(target) - 1)
    stack = list(target)
    while stack:
        vertex = stack.pop()
        answer *= comb(len(vertex) + exponent, exponent)
        stack.extend(vertex)
    return answer


def ost_local_factor(time: int, degree: int) -> int:
    exponent = 2 ** (time + 1) - 2
    return c_constant(time) * comb(degree + exponent, exponent)


def ost_aggregate_minimal_fibre(time: int, target_size: int) -> int:
    if target_size == 1:
        return 1
    c = c_constant(time)
    return (
        c ** (target_size - 1)
        * comb(2 ** (time + 1) * (target_size - 1), target_size - 2)
        // (target_size - 1)
    )


def verify_ost():
    maximum_size = 11
    states_by_size = {
        n: rooted_plane_trees(n) for n in range(1, maximum_size + 1)
    }
    summary = []
    transition_rows = []
    minimal_fibres = Counter()
    for n, states in states_by_size.items():
        depths = Counter()
        for tree in states:
            target = ost_step(tree)
            claim(rooted_size(target) <= n)
            depth = ost_depth(tree)
            depths[depth] += 1
            transition_rows.append((n, tree, target, depth))
            for time in range(4):
                image = ost_iterate(tree, time)
                m = rooted_size(image)
                claim(n >= 1 + 2 ** time * (m - 1))
                if n == 1 + 2 ** time * (m - 1):
                    minimal_fibres[(time, image)] += 1
        wanted_maximum = 0 if n == 1 else (n - 1).bit_length()
        claim(max(depths) == wanted_maximum)
        summary.append((n, len(states), tuple(sorted(depths.items()))))

    checked_targets = 0
    for time in range(1, 6):
        for degree in range(21):
            recurrence = sum(
                (degree - split + 1)
                * ost_local_factor(time - 1, degree - split + 1)
                * ost_local_factor(time - 1, split)
                for split in range(degree + 1)
            )
            claim(recurrence == ost_local_factor(time, degree))
    for time in range(4):
        aggregate_by_size = Counter()
        for m, targets in states_by_size.items():
            source_size = 1 + 2 ** time * (m - 1)
            if source_size > maximum_size:
                continue
            for target in targets:
                observed = minimal_fibres[(time, target)]
                wanted = ost_minimal_fibre(time, target)
                claim(observed == wanted)
                claim(observed > 0)
                aggregate_by_size[m] += observed
                checked_targets += 1
            claim(aggregate_by_size[m] == ost_aggregate_minimal_fibre(time, m))

    sharp = []
    for height in range(1, 5):
        minimum_size = 1 + 2 ** (height - 1)
        observed = sum(
            ost_depth(tree) == height
            for tree in states_by_size[minimum_size]
        )
        wanted = c_constant(height - 1)
        claim(observed == wanted)
        sharp.append((height, minimum_size, observed))
    return summary, tuple(sharp), checked_targets, digest(transition_rows)


def main():
    plp, plp_hash = verify_plp()
    uzd, uzd_hash = verify_uzd()
    scq, scq_hash = verify_scq()
    rhr, rhr_hash = verify_rhr()
    rmr, rmr_hash = verify_rmr()
    ost, ost_sharp, ost_targets, ost_hash = verify_ost()
    print("P166 REPLACEMENT DISCOVERY ROUND 3 — INDEPENDENT EXACT VERIFIER")
    print("lifecycle=HOLD_EXTERNAL")
    print("PLP rows: n,states,image,max_fibre,depth_hist")
    for row in plp:
        print("PLP", row)
    print("PLP transition_sha256=" + plp_hash)
    print("UZD displayed rows: modulus,cycles,max_depth,(zero_run,unit_run)")
    for row in uzd:
        print("UZD", row)
    print("UZD orbit_sha256=" + uzd_hash)
    print("SCQ rows: n,automata,depth_hist,endpoint_block_hist")
    for row in scq:
        print("SCQ", row)
    print("SCQ trajectory_sha256=" + scq_hash)
    print("RHR rows: n,trees,image,max_fibre,max_tail,max_period,shape_hist")
    for row in rhr:
        print("RHR", row)
    print("RHR transition_sha256=" + rhr_hash)
    print("RMR rows: pairs,matchings,profiles,image,max_accepted,deepest_count,E_one_cycle,max_E")
    for row in rmr:
        print("RMR", row)
    print("RMR marked_transition_sha256=" + rmr_hash)
    print("OST rows: vertices,trees,depth_hist")
    for row in ost:
        print("OST", row)
    print("OST sharp rows: height,minimal_vertices,minimal_sources")
    for row in ost_sharp:
        print("OST_SHARP", row)
    print("OST checked_minimal_targets=" + str(ost_targets))
    print("OST transition_sha256=" + ost_hash)
    print("assertions=" + str(ASSERTIONS))


if __name__ == "__main__":
    main()
