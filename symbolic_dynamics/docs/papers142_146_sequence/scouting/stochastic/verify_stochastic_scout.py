#!/usr/bin/env python3
"""Exact scout for ten distinct finite or absorbing stochastic systems.

Only Python integers and fractions.Fraction are used.  There is no sampling,
floating point arithmetic, third-party import, clock access, or network access.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


class Meter:
    def __init__(self, handle):
        self.handle = handle
        self.inputs = 0
        self.assertions = 0

    def check(self, condition):
        self.assertions += 1
        assert condition


def poly_add(a, b):
    out = [Fraction(0) for _ in range(max(len(a), len(b)))]
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def poly_scale_shift(a, scale=Fraction(1), shift=0):
    return tuple([Fraction(0)] * shift + [scale * value for value in a])


def poly_mul_int(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)


def catalan(m):
    return comb(2 * m, m) // (m + 1)


def compositions(total, parts):
    if parts == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - parts + 2):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def integer_partitions(n, least=1):
    if n == 0:
        yield ()
        return
    for first in range(least, n + 1):
        for tail in integer_partitions(n - first, first):
            yield (first,) + tail


def graph_components(n, edges):
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    seen = set()
    components = []
    for start in range(n):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        component = []
        while stack:
            u = stack.pop()
            component.append(u)
            for v in adjacency[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        components.append(tuple(sorted(component)))
    return tuple(components)


def even_binomial_poly(size):
    values = [comb(size, j) if j % 2 == 0 else 0 for j in range(size + 1)]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def compressed_even_binomial_poly(size):
    return tuple(comb(size, 2 * index) for index in range(size // 2 + 1))


def component_spectrum_poly(sizes):
    answer = (1,)
    for size in sizes:
        answer = poly_mul_int(answer, even_binomial_poly(size))
    return answer


def exact_integer_poly_quotient(numerator, denominator):
    """Return the exact quotient in Z[x], or None when division fails."""
    numerator = list(numerator)
    denominator = list(denominator)
    while len(numerator) > 1 and numerator[-1] == 0:
        numerator.pop()
    while len(denominator) > 1 and denominator[-1] == 0:
        denominator.pop()
    if len(numerator) < len(denominator):
        return None
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    work = numerator[:]
    while len(work) >= len(denominator):
        degree = len(work) - len(denominator)
        if work[-1] % denominator[-1]:
            return None
        coefficient = work[-1] // denominator[-1]
        quotient[degree] = coefficient
        for index, value in enumerate(denominator):
            work[degree + index] -= coefficient * value
        while work and work[-1] == 0:
            work.pop()
    if any(work):
        return None
    while len(quotient) > 1 and quotient[-1] == 0:
        quotient.pop()
    return tuple(quotient)


def reconstruct_component_sizes(total_order, polynomial):
    """Greedily remove the largest even-binomial factor; add isolates last."""
    remaining = tuple(polynomial)
    recovered = []
    for size in range(total_order, 1, -1):
        factor = compressed_even_binomial_poly(size)
        while True:
            quotient = exact_integer_poly_quotient(remaining, factor)
            if quotient is None:
                break
            recovered.append(size)
            remaining = quotient
    if remaining != (1,):
        return None
    isolates = total_order - sum(recovered)
    if isolates < 0:
        return None
    return tuple(sorted(recovered + [1] * isolates))


def system_vs1():
    """Uniform vertex-push chain on orientations of a fixed simple graph."""
    meter = Meter("VS1")
    graph_count = 0
    max_orbit = 0
    for n in range(1, 6):
        possible = tuple(combinations(range(n), 2))
        for graph_mask in range(1 << len(possible)):
            edges = tuple(possible[i] for i in range(len(possible))
                          if (graph_mask >> i) & 1)
            components = graph_components(n, edges)
            sizes = tuple(len(component) for component in components)
            graph_count += 1
            meter.inputs += 1

            coordinate = {}
            generators = [0] * n
            bit = 0
            for component in components:
                root = component[0]
                component_bits = []
                for vertex in component[1:]:
                    coordinate[vertex] = bit
                    component_bits.append(bit)
                    generators[vertex] = 1 << bit
                    bit += 1
                root_mask = 0
                for index in component_bits:
                    root_mask ^= 1 << index
                generators[root] = root_mask
            rank = n - len(components)
            orbit_size = 1 << rank
            max_orbit = max(max_orbit, orbit_size)

            # The cut-incidence image has the predicted rank and no duplicate
            # orientations when one root switch per component is suppressed.
            orientations = set()
            for state in range(orbit_size):
                edge_mask = 0
                for edge_index, (u, v) in enumerate(edges):
                    parity = 0
                    if u in coordinate:
                        parity ^= (state >> coordinate[u]) & 1
                    if v in coordinate:
                        parity ^= (state >> coordinate[v]) & 1
                    if parity:
                        edge_mask |= 1 << edge_index
                orientations.add(edge_mask)
            meter.check(len(orientations) == orbit_size)

            reached = {0}
            queue = deque([0])
            while queue:
                state = queue.popleft()
                for generator in generators:
                    nxt = state ^ generator
                    if nxt not in reached:
                        reached.add(nxt)
                        queue.append(nxt)
            meter.check(len(reached) == orbit_size)

            # Fourier characters give the complete spectrum.
            actual_multiplicity = Counter()
            for character in range(orbit_size):
                negatives = 0
                for generator in generators:
                    negatives += ((character & generator).bit_count() & 1)
                actual_multiplicity[negatives] += 1
            predicted_poly = component_spectrum_poly(sizes)
            predicted_multiplicity = Counter(
                {k: value for k, value in enumerate(predicted_poly) if value}
            )
            meter.check(actual_multiplicity == predicted_multiplicity)
            meter.check(sum(actual_multiplicity.values()) == orbit_size)

            # Independent exact return-walk recursion versus the spectral trace.
            walk_counts = [0] * orbit_size
            walk_counts[0] = 1
            for time in range(6):
                return_probability = Fraction(walk_counts[0], n ** time)
                spectral_return = sum(
                    multiplicity * Fraction(n - 2 * k, n) ** time
                    for k, multiplicity in actual_multiplicity.items()
                ) / orbit_size
                meter.check(return_probability == spectral_return)
                nxt_counts = [0] * orbit_size
                for state, count in enumerate(walk_counts):
                    for generator in generators:
                        nxt_counts[state ^ generator] += count
                walk_counts = nxt_counts

            period_two = all(size % 2 == 0 for size in sizes)
            meter.check((actual_multiplicity.get(n, 0) == 1) == period_two)

    # Exact inverse pressure: spectral multiplicities separate component-size
    # multisets for every integer partition through total order 24.
    partition_count = 0
    for n in range(1, 25):
        seen = {}
        for partition in integer_partitions(n):
            polynomial = component_spectrum_poly(partition)
            inverse_polynomial = tuple(polynomial[index]
                                       for index in range(0, len(polynomial), 2))
            meter.inputs += 1
            partition_count += 1
            meter.check(inverse_polynomial not in seen)
            meter.check(reconstruct_component_sizes(n, inverse_polynomial) == partition)
            seen[inverse_polynomial] = partition
        meter.check(len(seen) == sum(1 for _ in integer_partitions(n)))

    return meter, (
        f"graphs={graph_count} partitions={partition_count} "
        f"max_orbit={max_orbit} inverse_through=24"
    )


def polygon_endpoint(n, deletion_order):
    current = list(range(n))
    diagonals = set()
    for vertex in deletion_order:
        index = current.index(vertex)
        left = current[index - 1]
        right = current[(index + 1) % len(current)]
        diagonals.add(tuple(sorted((left, right))))
        current.pop(index)
    return tuple(sorted(diagonals)), tuple(sorted(current))


def triangulation_faces(n, diagonals):
    edges = {tuple(sorted((i, (i + 1) % n))) for i in range(n)}
    edges.update(diagonals)
    faces = []
    for triple in combinations(range(n), 3):
        if all(tuple(sorted(pair)) in edges for pair in combinations(triple, 2)):
            faces.append(tuple(triple))
    return tuple(faces)


def dual_tree(faces):
    adjacency = [[] for _ in faces]
    for i, j in combinations(range(len(faces)), 2):
        if len(set(faces[i]) & set(faces[j])) == 2:
            adjacency[i].append(j)
            adjacency[j].append(i)
    return adjacency


def rooted_tree_hook_count(adjacency, root):
    parent = {root: -1}
    order = [root]
    for vertex in order:
        for neighbor in adjacency[vertex]:
            if neighbor not in parent:
                parent[neighbor] = vertex
                order.append(neighbor)
    sizes = [1] * len(adjacency)
    for vertex in reversed(order[1:]):
        sizes[parent[vertex]] += sizes[vertex]
    denominator = 1
    for vertex in range(len(adjacency)):
        if vertex != root:
            denominator *= sizes[vertex]
    return factorial(len(adjacency) - 1) // denominator


def system_pe1():
    """Uniform random ear deletion on a labelled convex polygon."""
    meter = Meter("PE1")
    total_histories = 0
    total_endpoints = 0
    profiles = []
    for n in range(3, 10):
        endpoint_counts = Counter()
        rooted_counts = Counter()
        for deletion_order in permutations(range(n), n - 3):
            diagonals, final_face = polygon_endpoint(n, deletion_order)
            endpoint_counts[diagonals] += 1
            rooted_counts[(diagonals, final_face)] += 1
            total_histories += 1
            meter.inputs += 1
        expected_histories = factorial(n) // 6
        meter.check(sum(endpoint_counts.values()) == expected_histories)
        meter.check(len(endpoint_counts) == catalan(n - 2))

        for diagonals, history_count in endpoint_counts.items():
            faces = triangulation_faces(n, diagonals)
            adjacency = dual_tree(faces)
            meter.check(len(faces) == n - 2)
            meter.check(sum(map(len, adjacency)) == 2 * (len(faces) - 1))
            hook_sum = 0
            for root, face in enumerate(faces):
                rooted_hook = rooted_tree_hook_count(adjacency, root)
                hook_sum += rooted_hook
                meter.check(rooted_counts[(diagonals, tuple(sorted(face)))] == rooted_hook)
            meter.check(history_count == hook_sum)
        minimum = min(endpoint_counts.values())
        maximum = max(endpoint_counts.values())
        meter.check(minimum == 2 ** (n - 3))
        meter.check(sum(Fraction(value, expected_histories)
                        for value in endpoint_counts.values()) == 1)
        total_endpoints += len(endpoint_counts)
        profiles.append(f"{n}:{len(endpoint_counts)}/{minimum}/{maximum}")
    return meter, (
        f"histories={total_histories} endpoints={total_endpoints} "
        f"profiles(n:endpoints/minH/maxH)={','.join(profiles)}"
    )


def prufer_tree(n, code):
    degree = [1] * n
    for vertex in code:
        degree[vertex] += 1
    edges = []
    for vertex in code:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append(tuple(sorted((leaf, vertex))))
        degree[leaf] -= 1
        degree[vertex] -= 1
    leaves = [i for i in range(n) if degree[i] == 1]
    edges.append(tuple(sorted(leaves)))
    return tuple(sorted(edges))


def rooted_edge_data(n, edges):
    adjacency = [[] for _ in range(n)]
    edge_index = {edge: i for i, edge in enumerate(edges)}
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    parent = [-1] * n
    parent_edge = [-1] * n
    depth = [0] * n
    order = [0]
    for u in order:
        for v in adjacency[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_edge[v] = edge_index[tuple(sorted((u, v)))]
            depth[v] = depth[u] + 1
            order.append(v)
    children = [[] for _ in range(n)]
    for v in range(1, n):
        children[parent[v]].append(v)
    ancestor_edges = []
    for v in range(1, n):
        chain = []
        u = v
        while u != 0:
            chain.append(parent_edge[u])
            u = parent[u]
        ancestor_edges.append(tuple(chain))
    return children, depth, ancestor_edges


def bipoly_add(a, b):
    answer = defaultdict(Fraction)
    for key, value in a.items():
        answer[key] += value
    for key, value in b.items():
        answer[key] += value
    return {key: value for key, value in answer.items() if value}


def bipoly_mul(a, b):
    answer = defaultdict(Fraction)
    for (ta, za), x in a.items():
        for (tb, zb), y in b.items():
            answer[(ta + tb, za + zb)] += x * y
    return {key: value for key, value in answer.items() if value}


def bipoly_integrate_t(a):
    return {(t + 1, z): value / (t + 1) for (t, z), value in a.items()}


def bipoly_shift(a, dt=0, dz=0, scale=Fraction(1)):
    return {(t + dt, z + dz): scale * value for (t, z), value in a.items()}


def tree_record_pgf(children):
    def visit(vertex):
        result = {(0, 0): Fraction(1)}
        for child in children[vertex]:
            below = visit(child)
            first = bipoly_shift(bipoly_integrate_t(below), dz=1)
            second = bipoly_add(below, bipoly_shift(below, dt=1, scale=-1))
            result = bipoly_mul(result, bipoly_add(first, second))
        return result

    conditional = visit(0)
    answer = defaultdict(Fraction)
    for (_, z_degree), value in conditional.items():
        answer[z_degree] += value  # evaluate the threshold variable at t=1
    top = max(answer, default=0)
    return tuple(answer[i] for i in range(top + 1))


def system_rt1():
    """Uniform edge cutting, always retaining the rooted component."""
    meter = Meter("RT1")
    tree_count = 0
    priority_orders = 0
    extrema = []
    for n in range(2, 7):
        means = []
        codes = product(range(n), repeat=n - 2) if n > 2 else [()]
        for code in codes:
            edges = prufer_tree(n, tuple(code))
            children, depth, ancestor_edges = rooted_edge_data(n, edges)
            tree_count += 1
            meter.inputs += 1
            counts = Counter()
            for priority_order in permutations(range(n - 1)):
                rank = [0] * (n - 1)
                for time, edge in enumerate(priority_order):
                    rank[edge] = time
                records = sum(
                    rank[chain[0]] == min(rank[edge] for edge in chain)
                    for chain in ancestor_edges
                )
                counts[records] += 1
                priority_orders += 1
            empirical = tuple(
                Fraction(counts[k], factorial(n - 1)) for k in range(n)
            )
            while len(empirical) > 1 and empirical[-1] == 0:
                empirical = empirical[:-1]
            formula = tree_record_pgf(children)
            meter.check(empirical == formula)
            meter.check(sum(formula) == 1)
            mean = sum(Fraction(1, depth[v]) for v in range(1, n))
            meter.check(sum(k * value for k, value in enumerate(formula)) == mean)
            means.append(mean)
        harmonic = sum(Fraction(1, k) for k in range(1, n))
        meter.check(min(means) == harmonic)
        meter.check(max(means) == n - 1)
        extrema.append(f"{n}:{harmonic}/{n-1}")
    return meter, (
        f"trees={tree_count} priority_orders={priority_orders} "
        f"mean_extrema(n:min/max)={','.join(extrema)}"
    )


@lru_cache(None)
def deque_endpoint_distribution(labels):
    if len(labels) == 1:
        return {labels[0]: Fraction(1)}
    answer = defaultdict(Fraction)
    for endpoint, mass in deque_endpoint_distribution(labels[1:]).items():
        answer[endpoint] += mass / 2
    for endpoint, mass in deque_endpoint_distribution(labels[:-1]).items():
        answer[endpoint] += mass / 2
    return dict(answer)


def system_dq1():
    """Delete one service quantum from a uniformly chosen end of a workload deque."""
    meter = Meter("DQ1")
    vector_count = 0
    marked_cells = 0
    for total in range(1, 13):
        binomial_cdf = []
        running = 0
        for k in range(total):
            running += comb(total - 1, k)
            binomial_cdf.append(Fraction(running, 2 ** (total - 1)))
        for parts in range(1, total + 1):
            for loads in compositions(total, parts):
                vector_count += 1
                meter.inputs += 1
                labels = tuple(
                    job for job, load in enumerate(loads) for _ in range(load)
                )
                dynamic = deque_endpoint_distribution(labels)
                predicted = {}
                cumulative = 0
                previous = 0
                marked_total = 0
                for job, load in enumerate(loads):
                    cumulative += load
                    count = sum(comb(total - 1, k)
                                for k in range(previous, cumulative))
                    predicted[job] = Fraction(count, 2 ** (total - 1))
                    for k in range(previous, cumulative):
                        meter.check(comb(total - 1, k) > 0)
                        marked_cells += 1
                        marked_total += comb(total - 1, k)
                    previous = cumulative
                meter.check(dynamic == predicted)
                meter.check(sum(predicted.values()) == 1)
                meter.check(marked_total == 2 ** (total - 1))

                # Given total workload, cumulative endpoint masses recover all
                # block boundaries, hence the ordered workload vector.
                reconstructed = []
                cumulative_mass = Fraction(0)
                last_boundary = 0
                for job in range(parts - 1):
                    cumulative_mass += predicted[job]
                    boundary = binomial_cdf.index(cumulative_mass) + 1
                    reconstructed.append(boundary - last_boundary)
                    last_boundary = boundary
                reconstructed.append(total - last_boundary)
                meter.check(tuple(reconstructed) == loads)
    return meter, (
        f"workload_vectors={vector_count} marked_cells={marked_cells} "
        "total_workload_through=12"
    )


def binom_safe(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def system_cs1():
    """A chip descends one or two levels, with a forced last move from level one."""
    meter = Meter("CS1")
    polynomials = [(Fraction(1),), (Fraction(0), Fraction(1))]
    profiles = []
    for height in range(0, 51):
        meter.inputs += 1
        if height >= 2:
            recurrence = poly_add(
                poly_scale_shift(polynomials[height - 1], Fraction(1, 2), 1),
                poly_scale_shift(polynomials[height - 2], Fraction(1, 2), 1),
            )
            polynomials.append(recurrence)
        polynomial = polynomials[height]
        meter.check(sum(polynomial) == 1)
        if height == 0:
            meter.check(polynomial == (Fraction(1),))
            continue
        for time in range(len(polynomial)):
            predicted = Fraction(binom_safe(time - 1, height - time),
                                 2 ** max(time - 1, 0))
            predicted += Fraction(binom_safe(time - 1, height - time - 1),
                                  2 ** time)
            meter.check(polynomial[time] == predicted)
        mean = sum(time * mass for time, mass in enumerate(polynomial))
        closed_mean = (Fraction(2 * height, 3) + Fraction(2, 9)
                       - Fraction(2, 9) * Fraction(-1, 2) ** height)
        meter.check(mean == closed_mean)
        if height in (5, 10, 20, 50):
            profiles.append(f"{height}:{mean}")
    return meter, f"heights=51 mean_profiles={','.join(profiles)}"


def cartesian_shape(rank, left, right):
    if left > right:
        return None
    root = min(range(left, right + 1), key=lambda index: rank[index])
    return (cartesian_shape(rank, left, root - 1),
            cartesian_shape(rank, root + 1, right))


def shape_hook_product(shape):
    if shape is None:
        return 0, 1
    left_size, left_product = shape_hook_product(shape[0])
    right_size, right_product = shape_hook_product(shape[1])
    size = 1 + left_size + right_size
    return size, size * left_product * right_product


def system_if1():
    """Uniformly crack every uncut bond of an interval and record the genealogy."""
    meter = Meter("IF1")
    history_count = 0
    shape_count = 0
    profiles = []
    for gaps in range(1, 9):
        counts = Counter()
        for order in permutations(range(gaps)):
            rank = [0] * gaps
            for time, bond in enumerate(order):
                rank[bond] = time
            counts[cartesian_shape(rank, 0, gaps - 1)] += 1
            history_count += 1
            meter.inputs += 1
        meter.check(sum(counts.values()) == factorial(gaps))
        meter.check(len(counts) == catalan(gaps))
        for shape, count in counts.items():
            size, hook_product = shape_hook_product(shape)
            meter.check(size == gaps)
            meter.check(count == factorial(gaps) // hook_product)
        shape_count += len(counts)
        profiles.append(f"{gaps+1}:{len(counts)}/{max(counts.values())}")
    return meter, (
        f"cut_orders={history_count} shapes={shape_count} "
        f"profiles(sites:shapes/maxH)={','.join(profiles)}"
    )


def system_cb1():
    """Choose a live cactus cycle, then a uniform edge of that cycle, and cut it."""
    meter = Meter("CB1")
    parameter_tuples = 0
    endpoints = 0
    history_terms = 0
    for cycles in range(1, 4):
        for lengths in product(range(3, 7), repeat=cycles):
            parameter_tuples += 1
            meter.inputs += 1
            endpoint_mass = defaultdict(Fraction)
            endpoint_histories = Counter()
            for cycle_order in permutations(range(cycles)):
                for choices in product(*[range(length) for length in lengths]):
                    mass = Fraction(1)
                    remaining = cycles
                    for cycle in cycle_order:
                        mass *= Fraction(1, remaining * lengths[cycle])
                        remaining -= 1
                    endpoint_mass[choices] += mass
                    endpoint_histories[choices] += 1
                    history_terms += 1
            expected_mass = Fraction(1, 1)
            for length in lengths:
                expected_mass /= length
            for endpoint in product(*[range(length) for length in lengths]):
                meter.check(endpoint_mass[endpoint] == expected_mass)
                meter.check(endpoint_histories[endpoint] == factorial(cycles))
                endpoints += 1
            meter.check(sum(endpoint_mass.values()) == 1)
    return meter, (
        f"cacti={parameter_tuples} endpoints={endpoints} "
        f"history_terms={history_terms} cycles_through=3"
    )


def permutation_parity(permutation):
    inversions = sum(permutation[i] > permutation[j]
                     for i in range(len(permutation))
                     for j in range(i + 1, len(permutation)))
    return inversions % 2


def triple_rotations(permutation):
    permutation = tuple(permutation)
    for index in range(len(permutation) - 2):
        a, b, c = permutation[index:index + 3]
        yield permutation[:index] + (b, c, a) + permutation[index + 3:]
        yield permutation[:index] + (c, a, b) + permutation[index + 3:]


def system_ps1():
    """Uniform adjacent three-cycle shuffle on permutations."""
    meter = Meter("PS1")
    state_count = 0
    profiles = []
    for n in range(3, 9):
        states = tuple(permutations(range(n)))
        state_set = set(states)
        indegree = Counter()
        for state in states:
            meter.inputs += 1
            state_count += 1
            successors = tuple(triple_rotations(state))
            meter.check(len(successors) == 2 * (n - 2))
            for successor in successors:
                meter.check(successor in state_set)
                meter.check(permutation_parity(successor) == permutation_parity(state))
                indegree[successor] += 1
        meter.check(all(indegree[state] == 2 * (n - 2) for state in states))

        orbit_sizes = []
        for seed in (tuple(range(n)), (1, 0) + tuple(range(2, n))):
            reached = {seed}
            queue = deque([seed])
            while queue:
                state = queue.popleft()
                for successor in triple_rotations(state):
                    if successor not in reached:
                        reached.add(successor)
                        queue.append(successor)
            orbit_sizes.append(len(reached))
            meter.check(len(reached) == factorial(n) // 2)
        meter.check(sum(orbit_sizes) == factorial(n))

        seed = tuple(range(n))
        one_step = next(triple_rotations(seed))
        meter.check(seed in set(triple_rotations(one_step)))  # a two-step return
        first = next(triple_rotations(seed))
        second = next(triple_rotations(first))
        third = next(triple_rotations(second))
        meter.check(third == seed)  # a three-step return
        profiles.append(f"{n}:{factorial(n)//2}")
    return meter, f"states={state_count} parity_orbits={','.join(profiles)}"


def invert_augmented(matrix, rhs_columns):
    rows = len(matrix)
    width = rows + rhs_columns
    for column in range(rows):
        pivot = next(row for row in range(column, rows)
                     if matrix[row][column] != 0)
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        scale = matrix[column][column]
        matrix[column] = [value / scale for value in matrix[column]]
        for row in range(rows):
            if row == column or matrix[row][column] == 0:
                continue
            scale = matrix[row][column]
            matrix[row] = [matrix[row][j] - scale * matrix[column][j]
                           for j in range(width)]
    return matrix


def resampling_transitions(word, n):
    active = [i for i in range(n - 1)
              if ((word >> i) & 3) == 3]
    if not active:
        return {word: Fraction(1)}
    counts = Counter()
    for index in active:
        cleared = word & ~(3 << index)
        for replacement in range(4):
            counts[cleared | (replacement << index)] += 1
    denominator = 4 * len(active)
    return {target: Fraction(count, denominator)
            for target, count in counts.items()}


def system_mr1():
    """Uniform violated-pair resampling for the bad binary pattern 11."""
    meter = Meter("MR1")
    state_count = 0
    profiles = []
    for n in range(2, 7):
        absorbing = [word for word in range(1 << n)
                     if all(((word >> i) & 3) != 3 for i in range(n - 1))]
        transient = [word for word in range(1 << n) if word not in set(absorbing)]
        transient_index = {word: i for i, word in enumerate(transient)}
        absorbing_index = {word: i for i, word in enumerate(absorbing)}
        t_count = len(transient)
        a_count = len(absorbing)
        matrix = [[Fraction(0) for _ in range(t_count + a_count + 1)]
                  for _ in range(t_count)]
        transition_cache = {}
        for word in transient:
            meter.inputs += 1
            state_count += 1
            row = transient_index[word]
            matrix[row][row] = 1
            transitions = resampling_transitions(word, n)
            transition_cache[word] = transitions
            meter.check(sum(transitions.values()) == 1)
            for target, mass in transitions.items():
                if target in transient_index:
                    matrix[row][transient_index[target]] -= mass
                else:
                    matrix[row][t_count + absorbing_index[target]] += mass
            matrix[row][-1] = 1
        solved = invert_augmented(matrix, a_count + 1)
        maximum_mean = Fraction(0)
        maximum_support = 0
        for word in transient:
            row = transient_index[word]
            probabilities = tuple(solved[row][t_count:t_count + a_count])
            mean = solved[row][-1]
            meter.check(sum(probabilities) == 1)
            meter.check(mean > 0)
            meter.check(all(probability >= 0 for probability in probabilities))
            maximum_mean = max(maximum_mean, mean)
            maximum_support = max(maximum_support,
                                  sum(probability > 0 for probability in probabilities))

            # Replay the Bellman equations independently from the solved table.
            expected_mean = Fraction(1)
            expected_probabilities = [Fraction(0)] * a_count
            for target, mass in transition_cache[word].items():
                if target in transient_index:
                    target_row = transient_index[target]
                    expected_mean += mass * solved[target_row][-1]
                    for index in range(a_count):
                        expected_probabilities[index] += (
                            mass * solved[target_row][t_count + index]
                        )
                else:
                    expected_probabilities[absorbing_index[target]] += mass
            meter.check(mean == expected_mean)
            meter.check(probabilities == tuple(expected_probabilities))
        profiles.append(f"{n}:{t_count}/{a_count}/{maximum_support}/{maximum_mean}")
    return meter, (
        f"transient_states={state_count} "
        f"profiles(n:transient/terminal/maxsupport/maxmean)={','.join(profiles)}"
    )


def interval_events(mask, n):
    events = []
    start = 0
    while start < n:
        if not ((mask >> start) & 1):
            start += 1
            continue
        end = start
        while end < n and ((mask >> end) & 1):
            end += 1
        for left in range(start, end):
            interval_mask = 0
            for right in range(left, end):
                interval_mask |= 1 << right
                events.append(interval_mask)
        start = end
    return tuple(events)


def system_id1():
    """Uniformly erase a nonempty subinterval of the current path components."""
    meter = Meter("ID1")
    polynomials = {(0, 0): (Fraction(1),)}
    state_count = 0
    variable_clock = 0
    profiles = []
    for n in range(1, 11):
        polynomials[(n, 0)] = (Fraction(1),)
        for mask in range(1 << n):
            if mask == 0:
                continue
            meter.inputs += 1
            state_count += 1
            events = interval_events(mask, n)
            total = (Fraction(0),)
            for event in events:
                successor = mask & ~event
                successor_poly = polynomials[(n, successor)]
                total = poly_add(total, successor_poly)
            polynomial = poly_scale_shift(total, Fraction(1, len(events)), 1)
            polynomials[(n, mask)] = polynomial
            meter.check(sum(polynomial) == 1)
            meter.check(polynomial[0] == 0)
            if sum(value > 0 for value in polynomial) > 1:
                variable_clock += 1
        full = polynomials[(n, (1 << n) - 1)]
        mean = sum(time * mass for time, mass in enumerate(full))
        profiles.append(f"{n}:{len(full)-1}/{mean}")
    return meter, (
        f"states={state_count} variable_clock={variable_clock} "
        f"full_interval_profiles(n:maxT/mean)={','.join(profiles)}"
    )


def main():
    systems = [
        system_vs1,
        system_pe1,
        system_rt1,
        system_dq1,
        system_cs1,
        system_if1,
        system_cb1,
        system_ps1,
        system_mr1,
        system_id1,
    ]
    rows = []
    for system in systems:
        meter, summary = system()
        rows.append((meter, summary))

    global_assertions = 0
    global_assertions += 1
    assert len(rows) == 10
    global_assertions += 1
    assert len({meter.handle for meter, _ in rows}) == len(rows)
    global_assertions += 1
    assert all(meter.inputs > 0 and meter.assertions > 0 for meter, _ in rows)

    print("STOCHASTIC_SCOUT_EXACT_V1")
    print("arithmetic=Fraction_and_integer_only")
    print(f"literal_systems={len(rows)}")
    for meter, summary in rows:
        print(f"{meter.handle} inputs={meter.inputs} assertions={meter.assertions} {summary}")
    total_inputs = sum(meter.inputs for meter, _ in rows)
    total_assertions = sum(meter.assertions for meter, _ in rows) + global_assertions
    print(f"TOTAL inputs={total_inputs} assertions={total_assertions} global={global_assertions}")
    print("HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
