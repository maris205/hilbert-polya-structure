#!/usr/bin/env python3
"""Deterministic exact controls for the uniform vertex-push chain.

Only Python integers and fractions.Fraction are used.  The program performs
exhaustive finite checks; the all-parameter statements in the paper are
proved in main.tex and are not inferred from this computation.
"""

from collections import Counter, deque
from fractions import Fraction
from itertools import combinations
from math import comb


class Checks:
    def __init__(self):
        self.assertions = 0

    def equal(self, left, right, label):
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")

    def true(self, condition, label):
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


CHECK = Checks()
RECOVERY_DIVISION_ATTEMPTS = 0
RECOVERY_SUCCESSFUL_PEELS = 0


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def poly_mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def poly_derivative(poly):
    if len(poly) == 1:
        return (Fraction(0),)
    return trim(Fraction(i) * poly[i] for i in range(1, len(poly)))


def poly_divmod_fraction(dividend, divisor):
    dividend = list(map(Fraction, trim(dividend)))
    divisor = list(map(Fraction, trim(divisor)))
    if divisor == [0]:
        raise ZeroDivisionError("zero polynomial")
    if len(dividend) < len(divisor):
        return (Fraction(0),), trim(dividend)
    quotient = [Fraction(0)] * (len(dividend) - len(divisor) + 1)
    while len(dividend) >= len(divisor) and any(dividend):
        shift = len(dividend) - len(divisor)
        scale = dividend[-1] / divisor[-1]
        quotient[shift] += scale
        for i, coefficient in enumerate(divisor):
            dividend[i + shift] -= scale * coefficient
        dividend = list(trim(dividend))
    return trim(quotient), trim(dividend)


def poly_gcd(left, right):
    left = trim(map(Fraction, left))
    right = trim(map(Fraction, right))
    while right != (Fraction(0),):
        _, remainder = poly_divmod_fraction(left, right)
        left, right = right, remainder
    lead = left[-1]
    return trim(value / lead for value in left)


def try_divide_exact_integer(dividend, divisor):
    """Return the integral quotient, or None when exact division fails."""
    quotient, remainder = poly_divmod_fraction(dividend, divisor)
    if remainder != (Fraction(0),):
        return None
    if not all(value.denominator == 1 for value in quotient):
        return None
    return trim(value.numerator for value in quotient)


def even_factor(size):
    """E_size(y) = sum_r binom(size,2r)y^r."""
    return tuple(comb(size, 2 * r) for r in range(size // 2 + 1))


def sign_factor(size):
    """B_size(x) = sum_{j even} binom(size,j)x^j."""
    return tuple(comb(size, j) if j % 2 == 0 else 0
                 for j in range(size + 1))


def component_product(sizes, compressed=False):
    out = (1,)
    for size in sizes:
        out = poly_mul(out, even_factor(size) if compressed
                       else sign_factor(size))
    return out


def recover_component_orders(total, compressed):
    """Recover component orders using only the known total and Q_G.

    Candidate sizes are tested from total down to two by exact polynomial
    divisibility.  The all-parameter proof that this scan cannot accept a
    spurious size is the nearest-root separation argument in main.tex.
    Isolates are then the residual of the known total because E_1=1.
    """
    global RECOVERY_DIVISION_ATTEMPTS, RECOVERY_SUCCESSFUL_PEELS

    if total < 1:
        raise ValueError("the known vertex total must be positive")
    remainder = trim(compressed)
    if not remainder or remainder[0] != 1:
        raise ValueError("Q_G must have constant coefficient one")

    recovered = []
    for size in range(total, 1, -1):
        factor = even_factor(size)
        while len(remainder) >= len(factor):
            RECOVERY_DIVISION_ATTEMPTS += 1
            quotient = try_divide_exact_integer(remainder, factor)
            if quotient is None:
                break
            RECOVERY_SUCCESSFUL_PEELS += 1
            recovered.append(size)
            remainder = quotient

    if remainder != (1,):
        raise ValueError(f"unresolved compressed factor: {remainder!r}")
    isolates = total - sum(recovered)
    if isolates < 0:
        raise ValueError("recovered non-isolated orders exceed known total")
    return tuple(sorted((1,) * isolates + tuple(recovered)))


def partitions(total, minimum=1):
    """Yield nondecreasing positive integer partitions of total."""
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def edge_pairs(order):
    return list(combinations(range(order), 2))


def components(order, edges):
    neighbors = [set() for _ in range(order)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    unseen = set(range(order))
    answer = []
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        queue = [root]
        block = []
        while queue:
            vertex = queue.pop()
            block.append(vertex)
            for nxt in neighbors[vertex]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    queue.append(nxt)
        answer.append(tuple(sorted(block)))
    return tuple(answer)


def gf2_rank(vectors):
    basis = {}
    for value in vectors:
        while value:
            pivot = value.bit_length() - 1
            if pivot in basis:
                value ^= basis[pivot]
            else:
                basis[pivot] = value
                break
    return len(basis)


def cut_generators(order, edges):
    """Return the labelled vertex-push translations in edge coordinates."""
    generators = []
    for vertex in range(order):
        cut = 0
        for edge_index, (u, v) in enumerate(edges):
            if vertex == u or vertex == v:
                cut ^= 1 << edge_index
        generators.append(cut)
    return tuple(generators)


def generated_orbit(generators):
    orbit = {0}
    queue = deque([0])
    while queue:
        state = queue.popleft()
        for generator in generators:
            nxt = state ^ generator
            if nxt not in orbit:
                orbit.add(nxt)
                queue.append(nxt)
    return tuple(sorted(orbit))


def matrix_multiply(left, right):
    rows = len(left)
    inner = len(right)
    columns = len(right[0])
    out = [[Fraction(0) for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for k in range(inner):
            if left[i][k] == 0:
                continue
            for j in range(columns):
                out[i][j] += left[i][k] * right[k][j]
    return out


def characteristic_polynomial(matrix):
    """Exact coefficients of det(xI-A), highest degree first."""
    dimension = len(matrix)
    power = [[Fraction(int(i == j)) for j in range(dimension)]
             for i in range(dimension)]
    traces = [Fraction(dimension)]
    for _ in range(1, dimension + 1):
        power = matrix_multiply(power, matrix)
        traces.append(sum(power[i][i] for i in range(dimension)))

    # Newton/Faddeev--LeVerrier recurrence for
    # x^d+c_1 x^(d-1)+...+c_d.
    coefficients = [Fraction(1)]
    for degree in range(1, dimension + 1):
        value = -sum(coefficients[degree - index] * traces[index]
                     for index in range(1, degree + 1)) / degree
        coefficients.append(value)
    return tuple(coefficients)


def labelled_transition_characteristic(order, edges):
    """Build the literal labelled-generator kernel and return its charpoly."""
    generators = cut_generators(order, edges)
    orbit = generated_orbit(generators)
    index = {state: position for position, state in enumerate(orbit)}
    matrix = [[Fraction(0) for _ in orbit] for _ in orbit]
    for state in orbit:
        row = index[state]
        for generator in generators:
            matrix[row][index[state ^ generator]] += Fraction(1, order)
    for row in matrix:
        CHECK.equal(sum(row), Fraction(1), "literal transition row sum")
    return characteristic_polynomial(matrix)


def graph_controls(max_order=5, max_time=6):
    graph_count = 0
    orbit_state_count = 0
    history_cells = 0
    for order in range(1, max_order + 1):
        possible = edge_pairs(order)
        for graph_mask in range(1 << len(possible)):
            graph_count += 1
            edges = [edge for index, edge in enumerate(possible)
                     if (graph_mask >> index) & 1]
            blocks = components(order, edges)
            block_masks = [sum(1 << vertex for vertex in block)
                           for block in blocks]
            component_sizes = tuple(sorted(map(len, blocks)))
            component_count = len(blocks)

            generators = cut_generators(order, edges)

            CHECK.equal(gf2_rank(generators), order - component_count,
                        "cut-space rank")

            image_counts = Counter()
            actual_kernel = set()
            for push_mask in range(1 << order):
                state = 0
                for vertex in range(order):
                    if (push_mask >> vertex) & 1:
                        state ^= generators[vertex]
                image_counts[state] += 1
                if state == 0:
                    actual_kernel.add(push_mask)

            expected_kernel = set()
            for choice in range(1 << component_count):
                relation = 0
                for index, block_mask in enumerate(block_masks):
                    if (choice >> index) & 1:
                        relation |= block_mask
                expected_kernel.add(relation)
            CHECK.equal(actual_kernel, expected_kernel,
                        "all and only component relations")
            CHECK.equal(len(image_counts), 1 << (order - component_count),
                        "orbit cardinality")
            for multiplicity in image_counts.values():
                CHECK.equal(multiplicity, 1 << component_count,
                            "constant relation-fibre size")

            orbit = set(generated_orbit(generators))
            CHECK.equal(orbit, set(image_counts), "irreducible push orbit")
            orbit_state_count += len(orbit)
            for state in orbit:
                CHECK.true(all((state ^ generator) in orbit
                               for generator in generators),
                           "transition closure")
                CHECK.true(all(((state ^ generator) ^ generator) == state
                               for generator in generators),
                           "transition symmetry")

            weight_multiplicity = Counter()
            for negative_mask in range(1 << order):
                legal = all((negative_mask & block_mask).bit_count() % 2 == 0
                            for block_mask in block_masks)
                if legal:
                    weight_multiplicity[negative_mask.bit_count()] += 1
            expected_polynomial = component_product(component_sizes)
            observed_polynomial = tuple(weight_multiplicity.get(k, 0)
                                        for k in range(order + 1))
            CHECK.equal(trim(observed_polynomial), trim(expected_polynomial),
                        "character weight polynomial")
            CHECK.equal(sum(weight_multiplicity.values()), len(orbit),
                        "complete character count")

            eigenvalues = Counter()
            for weight, multiplicity in weight_multiplicity.items():
                eigenvalues[Fraction(order - 2 * weight, order)] += multiplicity
            reconstructed = [0] * (order + 1)
            for eigenvalue, multiplicity in eigenvalues.items():
                weight = Fraction(order) * (1 - eigenvalue) / 2
                CHECK.equal(weight.denominator, 1,
                            "spectral index is integral when n is known")
                reconstructed[weight.numerator] = multiplicity
            CHECK.equal(trim(reconstructed), trim(expected_polynomial),
                        "spectrum reconstructs M_G")

            counts = {0: 1}
            for time in range(max_time + 1):
                direct = Fraction(counts.get(0, 0), order ** time)
                spectral = sum(
                    Fraction(multiplicity, len(orbit))
                    * Fraction(order - 2 * weight, order) ** time
                    for weight, multiplicity in weight_multiplicity.items()
                )
                CHECK.equal(direct, spectral, "exact return law")
                history_cells += len(counts)
                if time < max_time:
                    updated = Counter()
                    for state, count in counts.items():
                        for generator in generators:
                            updated[state ^ generator] += count
                    CHECK.equal(sum(updated.values()), order ** (time + 1),
                                "complete labelled history count")
                    counts = dict(updated)

            all_even = all(size % 2 == 0 for size in component_sizes)
            has_odd_relation = any(mask.bit_count() % 2 == 1
                                   for mask in actual_kernel)
            CHECK.equal(has_odd_relation, not all_even,
                        "odd component relation criterion")
            CHECK.equal(eigenvalues.get(Fraction(-1), 0),
                        1 if all_even else 0,
                        "minus-one eigenvalue criterion")

    return graph_count, orbit_state_count, history_cells


def inverse_controls(max_total=30):
    partition_count = 0
    signatures = 0
    for total in range(1, max_total + 1):
        seen = {}
        for part in partitions(total):
            partition_count += 1
            compressed = component_product(part, compressed=True)
            uncompressed = component_product(part, compressed=False)
            expanded = [0] * (2 * len(compressed) - 1)
            for degree, coefficient in enumerate(compressed):
                expanded[2 * degree] = coefficient
            CHECK.equal(trim(expanded), trim(uncompressed), "M_G(x)=Q_G(x^2)")

            CHECK.true(compressed not in seen,
                       "fixed-total component signature is injective")
            seen[compressed] = part

            # The recovery routine sees only (total, compressed).  The true
            # partition is used only after recovery, as an expected answer.
            recovered = recover_component_orders(total, compressed)
            CHECK.equal(recovered, part, "input-only component recovery")
        signatures += len(seen)
        CHECK.equal(len(seen), sum(1 for _ in partitions(total)),
                    "all fixed-total signatures distinct")
    return partition_count, signatures


def algebraic_factor_controls(max_size=30):
    squarefree_factors = 0
    for size in range(2, max_size + 1):
        factor = tuple(map(Fraction, even_factor(size)))
        CHECK.equal(len(factor) - 1, size // 2, "E_s degree")
        CHECK.equal(poly_gcd(factor, poly_derivative(factor)),
                    (Fraction(1),), "E_s has only simple roots")
        squarefree_factors += 1
    return squarefree_factors


def folded_quotient_controls(max_size=12):
    """Check the pivot-coordinate quotient generators, including s=1,2."""
    sizes = 0
    for size in range(1, max_size + 1):
        dimension = size - 1
        all_ones = (1 << dimension) - 1
        # Coordinates are a_v+a_pivot.  The pivot push maps to all ones;
        # every other labelled push maps to its coordinate vector.
        images = tuple(1 << index for index in range(dimension)) + (all_ones,)
        CHECK.equal(len(images), size, "one quotient generator per label")
        if size == 1:
            CHECK.equal(images, (0,), "isolated push is the identity")
        elif size == 2:
            CHECK.equal(images, (1, 1),
                        "two labelled pushes give the same FQ1 translation")
        else:
            CHECK.equal(set(images),
                        {1 << index for index in range(dimension)} | {all_ones},
                        "folded-hypercube Cayley generator set")
            CHECK.equal(len(set(images)), size,
                        "nondegenerate folded generators are distinct")
        sizes += 1
    return sizes


def boundary_controls():
    # Build P4 and K4 from genuinely different edge sets, construct their
    # literal labelled-generator kernels, and compare exact characteristic
    # polynomials rather than calling the component formula twice.
    order = 4
    path_edges = ((0, 1), (1, 2), (2, 3))
    complete_edges = tuple(edge_pairs(order))
    CHECK.true(path_edges != complete_edges, "P4 and K4 edge sets differ")
    CHECK.equal(len(path_edges), 3, "P4 edge count")
    CHECK.equal(len(complete_edges), 6, "K4 edge count")
    path_characteristic = labelled_transition_characteristic(order, path_edges)
    complete_characteristic = labelled_transition_characteristic(
        order, complete_edges
    )
    CHECK.equal(path_characteristic, complete_characteristic,
                "constructed P4 and K4 transition spectra agree")

    # K4 has distinct affine cut-space cosets.  Translating one orbit to
    # another conjugates every push transition, so the starting orientation
    # (and even its push-equivalence class) is invisible to the chain matrix.
    edges = edge_pairs(order)
    generators = cut_generators(order, edges)
    orbit = set()
    for mask in range(1 << order):
        state = 0
        for vertex in range(order):
            if (mask >> vertex) & 1:
                state ^= generators[vertex]
        orbit.add(state)
    shift = next(state for state in range(1 << len(edges)) if state not in orbit)
    shifted = {state ^ shift for state in orbit}
    CHECK.true(orbit.isdisjoint(shifted), "distinct starting push orbits")
    for state in orbit:
        for generator in generators:
            CHECK.equal((state ^ generator) ^ shift,
                        (state ^ shift) ^ generator,
                        "affine-orbit transition conjugacy")

    # Without the ambient order, every positive-order edgeless graph gives
    # the same one-state identity kernel and spectrum {1}.
    edgeless_characteristics = []
    for edgeless_order in range(1, 7):
        edgeless_characteristics.append(
            labelled_transition_characteristic(edgeless_order, ())
        )
    CHECK.true(len(set(edgeless_characteristics)) == 1,
               "known n is necessary: all edgeless spectra coincide")
    CHECK.equal(edgeless_characteristics[0],
                (Fraction(1), Fraction(-1)),
                "one-state identity characteristic polynomial")

    return {
        "constructed_adjacency_witnesses": 1,
        "affine_orbit_witnesses": 1,
        "unknown_n_edgeless_orders": len(edgeless_characteristics),
    }


def main():
    graph_count, orbit_states, history_cells = graph_controls()
    partition_count, signature_count = inverse_controls()
    squarefree_factors = algebraic_factor_controls()
    quotient_sizes = folded_quotient_controls()
    boundary = boundary_controls()

    CHECK.equal(graph_count, 1099, "literal labelled graph total")
    CHECK.true(CHECK.assertions > 0, "nonempty exact assertion ledger")

    print("P145_EXACT_CONTROL_V2")
    print("arithmetic=integer_and_Fraction_only")
    print("sampling=none")
    print(f"labelled_graphs_n_le_5={graph_count}")
    print(f"orbit_states_visited={orbit_states}")
    print(f"return_recurrence_state_cells_t_le_6={history_cells}")
    print(f"component_partitions_total_n_le_30={partition_count}")
    print(f"distinct_fixed_total_signatures={signature_count}")
    print(f"input_only_recovery_cases={partition_count}")
    print(f"recovery_division_attempts={RECOVERY_DIVISION_ATTEMPTS}")
    print(f"successful_input_only_factor_peels={RECOVERY_SUCCESSFUL_PEELS}")
    print(f"squarefree_even_binomial_factors={squarefree_factors}")
    print(f"folded_quotient_sizes_checked={quotient_sizes}")
    print("constructed_P4_K4_adjacency_witnesses="
          f"{boundary['constructed_adjacency_witnesses']}")
    print(f"affine_orbit_witnesses={boundary['affine_orbit_witnesses']}")
    print("unknown_n_edgeless_orders_checked="
          f"{boundary['unknown_n_edgeless_orders']}")
    print(f"exact_assertions={CHECK.assertions}")
    print("status=PASS")
    print("external_status=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
