#!/usr/bin/env python3
"""Deterministic breadth verifier for matching/incidence replacement maps.

No paper, author, or earlier scout implementation is imported.  Each row is
an exact finite endofunction, not a random sample.  OMD receives additional
all-size-formula checks because it is the strongest (but owner-reduced)
signal in the lane.
"""

from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, product
from math import factorial, gcd, lcm


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, label):
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


A = Audit()


def functional_data(states, update):
    states = tuple(states)
    index = {state: i for i, state in enumerate(states)}
    A.check(len(index) == len(states), "duplicate carrier state")
    nxt = []
    reverse = [[] for _ in states]
    indegree = [0] * len(states)
    for i, state in enumerate(states):
        target = update(state)
        A.check(target in index, ("map left carrier", state, target))
        j = index[target]
        nxt.append(j)
        reverse[j].append(i)
        indegree[j] += 1
    A.check(sum(indegree) == len(states), "indegree mass")

    residual = indegree[:]
    queue = deque(i for i, degree in enumerate(residual) if degree == 0)
    on_cycle = [True] * len(states)
    while queue:
        i = queue.popleft()
        on_cycle[i] = False
        j = nxt[i]
        residual[j] -= 1
        if residual[j] == 0:
            queue.append(j)

    period = [0] * len(states)
    cycle_hist = Counter()
    visited_cycle = set()
    for start in range(len(states)):
        if not on_cycle[start] or start in visited_cycle:
            continue
        cycle = []
        current = start
        while current not in visited_cycle:
            visited_cycle.add(current)
            cycle.append(current)
            current = nxt[current]
        length = len(cycle)
        A.check(current == start, ("cycle traversal", start, current))
        cycle_hist[length] += 1
        for vertex in cycle:
            period[vertex] = length

    depth = [-1] * len(states)
    queue = deque()
    for i in visited_cycle:
        depth[i] = 0
        queue.append(i)
    while queue:
        target = queue.popleft()
        for source in reverse[target]:
            if depth[source] == -1:
                depth[source] = depth[target] + 1
                period[source] = period[target]
                queue.append(source)
    A.check(all(value >= 0 for value in depth), "unclassified depth")
    for i in range(len(states)):
        if depth[i]:
            A.check(depth[nxt[i]] == depth[i] - 1, ("depth descent", i))
            A.check(period[nxt[i]] == period[i], ("eventual period", i))

    fibres = Counter(degree for degree in indegree if degree)
    return {
        "states": len(states),
        "image": sum(degree > 0 for degree in indegree),
        "fibres": tuple(sorted(fibres.items())),
        "cycles": tuple(sorted(cycle_hist.items())),
        "max_depth": max(depth, default=0),
        "depths": tuple(sorted(Counter(depth).items())),
        "next": tuple(nxt),
        "depth": tuple(depth),
        "period": tuple(period),
        "index": index,
    }


def compact(data):
    return (
        data["states"],
        data["image"],
        data["fibres"],
        data["cycles"],
        data["max_depth"],
        data["depths"],
    )


# ---------------------------------------------------------------------------
# Perfect-matching systems


@lru_cache(maxsize=None)
def perfect_matchings(size):
    if size == 0:
        return ((),)

    def rec(vertices):
        if not vertices:
            yield ()
            return
        first = vertices[0]
        for j in range(1, len(vertices)):
            second = vertices[j]
            rest = vertices[1:j] + vertices[j + 1 :]
            for partner_tail in rec(rest):
                partner = [-1] * size
                for i, value in enumerate(partner_tail):
                    if value != -1:
                        partner[i] = value
                partner[first] = second
                partner[second] = first
                yield tuple(partner)

    # The recursive representation above needs a stable sentinel outside the
    # current vertex set.  Build pairs first, then convert once.
    def pairs(vertices):
        if not vertices:
            yield ()
            return
        first = vertices[0]
        for j in range(1, len(vertices)):
            second = vertices[j]
            rest = vertices[1:j] + vertices[j + 1 :]
            for tail in pairs(rest):
                yield ((first, second),) + tail

    answer = []
    for matching in pairs(tuple(range(size))):
        partner = [-1] * size
        for i, j in matching:
            partner[i] = j
            partner[j] = i
        answer.append(tuple(partner))
    return tuple(answer)


def base_matching(size):
    return tuple(i + 1 if i % 2 == 0 else i - 1 for i in range(size))


def compose(left, right):
    return tuple(left[right[i]] for i in range(len(left)))


def perm_power(permutation, exponent):
    out = tuple(range(len(permutation)))
    base = permutation
    while exponent:
        if exponent & 1:
            out = compose(out, base)
        base = compose(base, base)
        exponent //= 2
    return out


def overlay_components(matching, fixed):
    size = len(matching)
    unseen = set(range(size))
    components = []
    while unseen:
        root = min(unseen)
        todo = [root]
        vertices = set()
        while todo:
            vertex = todo.pop()
            if vertex in vertices:
                continue
            vertices.add(vertex)
            unseen.discard(vertex)
            todo.append(matching[vertex])
            todo.append(fixed[vertex])
        components.append(tuple(sorted(vertices)))
    return tuple(sorted(components, key=lambda block: block[0]))


def overlay_profile(matching, fixed):
    return tuple(sorted(len(component) // 2 for component in overlay_components(matching, fixed)))


def omd_update(matching, fixed):
    return compose(compose(matching, fixed), matching)


def matching_profile_count(n, profile):
    multiplicities = Counter(profile)
    numerator = factorial(n) * (2 ** (n - len(profile)))
    denominator = 1
    for size, multiplicity in multiplicities.items():
        denominator *= (size**multiplicity) * factorial(multiplicity)
    A.check(numerator % denominator == 0, ("profile integrality", n, profile))
    return numerator // denominator


def pairings(number):
    A.check(number % 2 == 0, ("odd pairing request", number))
    return factorial(number) // (2 ** (number // 2) * factorial(number // 2))


def omd_fibre_formula(profile):
    answer = 1
    for size, multiplicity in Counter(profile).items():
        if size % 2 == 0:
            if multiplicity % 2:
                return 0
            pairs = multiplicity // 2
            answer *= pairings(multiplicity) * (2 * size) ** pairs
        else:
            factor = 0
            for pairs in range(multiplicity // 2 + 1):
                chosen = factorial(multiplicity) // (
                    factorial(multiplicity - 2 * pairs)
                    * 2**pairs
                    * factorial(pairs)
                )
                factor += chosen * (2 * size) ** pairs
            answer *= factor
    return answer


def valuation_two(number):
    answer = 0
    while number % 2 == 0:
        number //= 2
        answer += 1
    return answer, number


def order_two_mod(odd):
    if odd == 1:
        return 1
    power = 2 % odd
    order = 1
    while power != 1:
        power = (2 * power) % odd
        order += 1
        A.check(order <= odd, ("order did not close", odd))
    return order


def integer_partitions(total, minimum=1):
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for tail in integer_partitions(total - first, first):
            yield (first,) + tail


def omd_suite():
    rows = []
    max_fibres = []
    for n in range(1, 8):
        carrier = perfect_matchings(2 * n)
        fixed = base_matching(2 * n)
        update = lambda matching, fixed=fixed: omd_update(matching, fixed)
        data = functional_data(carrier, update)
        observed_fibres = Counter(update(source) for source in carrier)

        profile_seen = Counter(overlay_profile(matching, fixed) for matching in carrier)
        for profile in integer_partitions(n):
            A.check(
                profile_seen[profile] == matching_profile_count(n, profile),
                ("matching profile count", n, profile),
            )
        desired_image = 0
        for target in carrier:
            profile = overlay_profile(target, fixed)
            predicted = omd_fibre_formula(profile)
            A.check(observed_fibres[target] == predicted, ("OMD fibre", n, profile))
            image_test = all(
                multiplicity % 2 == 0
                for size, multiplicity in Counter(profile).items()
                if size % 2 == 0
            )
            A.check((predicted > 0) == image_test, ("OMD image", n, profile))
            desired_depth = max(valuation_two(size)[0] for size in profile)
            desired_period = 1
            for size in profile:
                _, odd = valuation_two(size)
                desired_period = lcm(desired_period, order_two_mod(odd))
            location = data["index"][target]
            A.check(data["depth"][location] == desired_depth, ("OMD depth", n, profile))
            A.check(data["period"][location] == desired_period, ("OMD period", n, profile))
            product_perm = compose(fixed, target)
            iterated = target
            for t in range(0, 2 * n + 2):
                A.check(
                    compose(fixed, iterated) == perm_power(product_perm, 2**t),
                    ("OMD power factor", n, t, profile),
                )
                iterated = update(iterated)

        for profile in integer_partitions(n):
            if all(
                multiplicity % 2 == 0
                for size, multiplicity in Counter(profile).items()
                if size % 2 == 0
            ):
                desired_image += matching_profile_count(n, profile)
        A.check(data["image"] == desired_image, ("OMD image mass", n))
        A.check(sum(observed_fibres.values()) == len(carrier), ("OMD fibre mass", n))
        fixed_counts = [0] * 6
        for matching in carrier:
            current = matching
            for ell in range(1, 7):
                current = update(current)
                fixed_counts[ell - 1] += current == matching
        for ell in range(1, 7):
            desired = sum(
                matching_profile_count(n, profile)
                for profile in integer_partitions(n)
                if all((2**ell - 1) % size == 0 for size in profile)
            )
            A.check(fixed_counts[ell - 1] == desired, ("OMD fixed count", n, ell))
        maximum = max(observed_fibres.values())
        A.check(observed_fibres[fixed] == maximum, ("OMD fixed target max", n))
        max_fibres.append(maximum)
        rows.append((n, compact(data), tuple(fixed_counts)))
    return tuple(rows), tuple(max_fibres)


def hurwitz_system(n=3):
    matchings = perfect_matchings(2 * n)
    states = tuple(product(matchings, repeat=2))

    def update(state):
        left, right = state
        return right, compose(compose(right, left), right)

    return states, update


def component_projection_system(n=6, pointed=False):
    carrier = perfect_matchings(2 * n)
    fixed = base_matching(2 * n)

    def update(matching):
        answer = list(fixed)
        for component in overlay_components(matching, fixed):
            use_matching = (0 in component) if pointed else ((len(component) // 2) % 2 == 1)
            if use_matching:
                for vertex in component:
                    answer[vertex] = matching[vertex]
        return tuple(answer)

    return carrier, update


# ---------------------------------------------------------------------------
# Matrix, relation, and graph incidence maps


def all_bitstates(bits):
    return tuple(range(1 << bits))


def bit(state, position):
    return (state >> position) & 1


def unique_walk_square_system(n=3):
    states = all_bitstates(n * n)

    def update(state):
        out = 0
        for i in range(n):
            for j in range(n):
                witnesses = sum(bit(state, i * n + k) and bit(state, k * n + j) for k in range(n))
                if witnesses == 1:
                    out |= 1 << (i * n + j)
        return out

    return states, update


def simple_graph_system(n, rule):
    edges = tuple(combinations(range(n), 2))
    states = all_bitstates(len(edges))

    def update(state):
        neighbours = [set() for _ in range(n)]
        for position, (i, j) in enumerate(edges):
            if bit(state, position):
                neighbours[i].add(j)
                neighbours[j].add(i)
        out = 0
        for position, (i, j) in enumerate(edges):
            if rule(i, j, neighbours, state, edges):
                out |= 1 << position
        return out

    return states, update


def unique_common_neighbour(i, j, neighbours, _state, _edges):
    return len(neighbours[i] & neighbours[j]) == 1


def unique_rectangle_flip_system(rows=3, columns=3):
    states = all_bitstates(rows * columns)

    def update(state):
        out = state
        for i in range(rows):
            for j in range(columns):
                witnesses = 0
                for other_i in range(rows):
                    if other_i == i:
                        continue
                    for other_j in range(columns):
                        if other_j == j:
                            continue
                        witnesses += (
                            bit(state, i * columns + other_j)
                            and bit(state, other_i * columns + j)
                            and bit(state, other_i * columns + other_j)
                        )
                if witnesses == 1:
                    out ^= 1 << (i * columns + j)
        return out

    return states, update


def degree_offset_matrix_system(rows=3, columns=4):
    states = all_bitstates(rows * columns)

    def update(state):
        row_degree = [sum(bit(state, i * columns + j) for j in range(columns)) for i in range(rows)]
        column_degree = [sum(bit(state, i * columns + j) for i in range(rows)) for j in range(columns)]
        out = 0
        for i in range(rows):
            for j in range(columns):
                if row_degree[i] == column_degree[j] + 1:
                    out |= 1 << (i * columns + j)
        return out

    return states, update


# ---------------------------------------------------------------------------
# Subset maps on incidence/intersection graphs


def subset_neighbour_system(neighbours, selector):
    size = len(neighbours)
    states = all_bitstates(size)

    def update(state):
        counts = [sum(bit(state, j) for j in neighbours[i]) for i in range(size)]
        selected = selector(counts, state)
        out = 0
        for i, keep in enumerate(selected):
            if keep:
                out |= 1 << i
        return out

    return states, update


def exact_selector(value):
    return lambda counts, _state: tuple(count == value for count in counts)


def minimum_positive_selector(counts, _state):
    positive = [count for count in counts if count > 0]
    if not positive:
        return (False,) * len(counts)
    minimum = min(positive)
    return tuple(count == minimum for count in counts)


def kneser_neighbours(base_size, subset_size):
    vertices = tuple(combinations(range(base_size), subset_size))
    return vertices, tuple(
        tuple(j for j, right in enumerate(vertices) if i != j and set(left).isdisjoint(right))
        for i, left in enumerate(vertices)
    )


def johnson_neighbours(base_size, subset_size):
    vertices = tuple(combinations(range(base_size), subset_size))
    return vertices, tuple(
        tuple(j for j, right in enumerate(vertices) if i != j and len(set(left) & set(right)) == subset_size - 1)
        for i, left in enumerate(vertices)
    )


def projective_points(q):
    points = set()
    for vector in product(range(q), repeat=3):
        if not any(vector):
            continue
        first = next(value for value in vector if value)
        inverse = pow(first, q - 2, q)
        points.add(tuple((value * inverse) % q for value in vector))
    return tuple(sorted(points))


def polarity_neighbours(q):
    points = projective_points(q)
    neighbours = tuple(
        tuple(j for j, right in enumerate(points) if sum(a * b for a, b in zip(left, right)) % q == 0)
        for left in points
    )
    return points, neighbours


def rook_neighbours(rows, columns):
    vertices = tuple(product(range(rows), range(columns)))
    neighbours = tuple(
        tuple(j for j, right in enumerate(vertices) if i != j and (left[0] == right[0] or left[1] == right[1]))
        for i, left in enumerate(vertices)
    )
    return vertices, neighbours


def triple_intersection_neighbours(base_size):
    vertices = tuple(combinations(range(base_size), 3))
    neighbours = tuple(
        tuple(j for j, right in enumerate(vertices) if i != j and len(set(left) & set(right)) == 1)
        for i, left in enumerate(vertices)
    )
    return vertices, neighbours


# ---------------------------------------------------------------------------
# Tagged, rank-changing bipartite incidence systems


def tagged_incidence_system(left_size, right_size, incidences, selector):
    left_to_right = [[] for _ in range(left_size)]
    right_to_left = [[] for _ in range(right_size)]
    for left, right in incidences:
        left_to_right[left].append(right)
        right_to_left[right].append(left)
    states = tuple((0, mask) for mask in range(1 << left_size)) + tuple(
        (1, mask) for mask in range(1 << right_size)
    )

    def update(state):
        side, mask = state
        if side == 0:
            counts = [sum(bit(mask, left) for left in right_to_left[right]) for right in range(right_size)]
            keep = selector(counts, mask)
            out = sum((1 << right) for right, flag in enumerate(keep) if flag)
            return 1, out
        counts = [sum(bit(mask, right) for right in left_to_right[left]) for left in range(left_size)]
        keep = selector(counts, mask)
        out = sum((1 << left) for left, flag in enumerate(keep) if flag)
        return 0, out

    return states, update


def maximum_positive_selector(counts, _state):
    maximum = max(counts, default=0)
    if maximum == 0:
        return (False,) * len(counts)
    return tuple(count == maximum for count in counts)


def prime_selector(counts, _state):
    return tuple(count in (2, 3, 5, 7) for count in counts)


def all_but_one_selector(counts, state):
    selected = state.bit_count()
    return tuple(selected > 0 and count == selected - 1 for count in counts)


def incidence_k5_edges():
    edges = tuple(combinations(range(5), 2))
    incidences = tuple((vertex, j) for j, edge in enumerate(edges) for vertex in edge)
    return 5, len(edges), incidences


def incidence_boolean_levels():
    left = tuple(combinations(range(5), 2))
    right = tuple(combinations(range(5), 3))
    incidences = tuple((i, j) for i, a in enumerate(left) for j, b in enumerate(right) if set(a) < set(b))
    return len(left), len(right), incidences


def incidence_fano():
    points, neighbours = polarity_neighbours(2)
    incidences = tuple((i, j) for i, row in enumerate(neighbours) for j in row)
    return len(points), len(points), incidences


def incidence_grid():
    points = tuple(product(range(3), repeat=2))
    lines = tuple((kind, value) for kind in range(2) for value in range(3))
    incidences = tuple(
        (i, j)
        for i, point in enumerate(points)
        for j, (kind, value) in enumerate(lines)
        if point[kind] == value
    )
    return len(points), len(lines), incidences


def incidence_cube_faces():
    vertices = tuple(product(range(2), repeat=3))
    faces = tuple((axis, value) for axis in range(3) for value in range(2))
    incidences = tuple(
        (i, j)
        for i, vertex in enumerate(vertices)
        for j, (axis, value) in enumerate(faces)
        if vertex[axis] == value
    )
    return len(vertices), len(faces), incidences


def incidence_tetrahedron():
    edges = tuple(combinations(range(4), 2))
    faces = tuple(combinations(range(4), 3))
    incidences = tuple((i, j) for i, edge in enumerate(edges) for j, face in enumerate(faces) if set(edge) < set(face))
    return len(edges), len(faces), incidences


# ---------------------------------------------------------------------------
# Ordered set systems (incidence columns evolve independently)


def ordered_family_system(set_count, ground_size, column_update):
    states = all_bitstates(set_count * ground_size)

    def update(state):
        out = 0
        mask_limit = (1 << set_count) - 1
        for element in range(ground_size):
            column = (state >> (element * set_count)) & mask_limit
            new_column = column_update(column, set_count)
            A.check(0 <= new_column <= mask_limit, ("ordered column", column, new_column))
            out |= new_column << (element * set_count)
        return out

    return states, update


def private_column(column, _set_count):
    return column if column.bit_count() == 1 else 0


def compressed_column(column, _set_count):
    return (1 << column.bit_count()) - 1


def sum_owner_column(column, set_count):
    if column == 0:
        return 0
    owner = sum(i for i in range(set_count) if bit(column, i)) % set_count
    return 1 << owner


def rank_interval_column(column, set_count):
    if column == 0:
        return 0
    weight = column.bit_count()
    start = (next(i for i in range(set_count) if bit(column, i)) + weight) % set_count
    return sum(1 << ((start + offset) % set_count) for offset in range(weight))


# ---------------------------------------------------------------------------
# Uniform-hypergraph degree/codegree filters


def uniform_hypergraph_system(base_size, rank, rule):
    edges = tuple(combinations(range(base_size), rank))
    states = all_bitstates(len(edges))

    def update(state):
        degrees = [0] * base_size
        codegrees = Counter()
        for position, edge in enumerate(edges):
            if not bit(state, position):
                continue
            for vertex in edge:
                degrees[vertex] += 1
            for pair in combinations(edge, 2):
                codegrees[pair] += 1
        out = 0
        for position, edge in enumerate(edges):
            if rule(edge, degrees, codegrees):
                out |= 1 << position
        return out

    return states, update


def distinct_degree_rule(edge, degrees, _codegrees):
    values = [degrees[vertex] for vertex in edge]
    return len(set(values)) == len(values)


def distinct_codegree_rule(edge, _degrees, codegrees):
    values = [codegrees[pair] for pair in combinations(edge, 2)]
    return len(set(values)) == len(values)


def main():
    omd_rows, omd_max = omd_suite()

    systems = []
    systems.append(("M02 HUR",) + hurwitz_system())
    systems.append(("M03 OCP",) + component_projection_system(pointed=False))
    systems.append(("M04 OFL",) + component_projection_system(pointed=True))
    systems.append(("R01 UWS",) + unique_walk_square_system())
    systems.append(("R02 UCN",) + simple_graph_system(6, unique_common_neighbour))
    systems.append(("R03 URF",) + unique_rectangle_flip_system())
    systems.append(("R04 DOM",) + degree_offset_matrix_system())

    kneser_vertices, neighbours = kneser_neighbours(5, 2)
    kneser_states, kneser_update = subset_neighbour_system(neighbours, exact_selector(1))
    systems.append(("S01 KUN", kneser_states, kneser_update))
    _, neighbours = johnson_neighbours(5, 2)
    systems.append(("S02 JEX",) + subset_neighbour_system(neighbours, exact_selector(2)))
    _, neighbours = polarity_neighbours(2)
    systems.append(("S03 FTA",) + subset_neighbour_system(neighbours, exact_selector(1)))
    _, neighbours = polarity_neighbours(3)
    systems.append(("S04 PTA",) + subset_neighbour_system(neighbours, exact_selector(1)))
    _, neighbours = rook_neighbours(3, 3)
    systems.append(("S05 RMN",) + subset_neighbour_system(neighbours, minimum_positive_selector))
    triple_vertices, neighbours = triple_intersection_neighbours(5)
    triple_states, triple_update = subset_neighbour_system(neighbours, exact_selector(1))
    systems.append(("S06 TIN", triple_states, triple_update))

    triple_index = {vertex: i for i, vertex in enumerate(triple_vertices)}
    complement_positions = tuple(
        triple_index[tuple(i for i in range(5) if i not in pair)]
        for pair in kneser_vertices
    )

    def complement_state(state):
        return sum(1 << complement_positions[i] for i in range(10) if bit(state, i))

    for state in kneser_states:
        A.check(
            complement_state(kneser_update(state))
            == triple_update(complement_state(state)),
            ("Kneser/triple complement conjugacy", state),
        )

    incidence_specs = (
        ("I01 KVE", incidence_k5_edges(), exact_selector(1)),
        ("I02 BLM", incidence_boolean_levels(), minimum_positive_selector),
        ("I03 FSC", incidence_fano(), exact_selector(2)),
        ("I04 GPM", incidence_grid(), maximum_positive_selector),
        ("I05 CVP", incidence_cube_faces(), prime_selector),
        ("I06 TAB", incidence_tetrahedron(), all_but_one_selector),
    )
    for name, (left, right, incidences), selector in incidence_specs:
        systems.append((name,) + tagged_incidence_system(left, right, incidences, selector))

    systems.append(("O01 PVT",) + ordered_family_system(4, 4, private_column))
    systems.append(("O02 MCC",) + ordered_family_system(4, 4, compressed_column))
    systems.append(("O03 SOR",) + ordered_family_system(4, 4, sum_owner_column))
    systems.append(("O04 RIN",) + ordered_family_system(3, 4, rank_interval_column))

    systems.append(("H01 DDF",) + uniform_hypergraph_system(5, 3, distinct_degree_rule))
    systems.append(("H02 CDF",) + uniform_hypergraph_system(5, 3, distinct_codegree_rule))

    A.check(len(systems) == 25, ("non-OMD system count", len(systems)))
    results = []
    for name, states, update in systems:
        results.append((name, compact(functional_data(states, update))))
    A.check(
        len({signature for _name, signature in results}) == 24,
        "unexpected duplicate functional signatures",
    )

    print("P162-P166 REPLACEMENT MATCHINGS/INCIDENCE SCOUT")
    print("01 M01 OMD n=1..7 rows=" + repr(omd_rows))
    print("01 M01 OMD maximum_fibres=" + repr(omd_max))
    for number, (name, signature) in enumerate(results, start=2):
        print(f"{number:02d} {name} signature={signature}")
    print("DISTINCT_CONJUGACY_CLASSES 25")
    print(f"ASSERTIONS {A.assertions}")
    print("DECISIONS 0_GREEN 0_AMBER 26_KILL")
    print("M01=KILL_GENERIC_PERMUTATION_SQUARE_ROOT_ENGINE")
    print("HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
