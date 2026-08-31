#!/usr/bin/env python3
"""Exact replacement scout for finite stochastic/asynchronous systems.

All controls use Python integers and fractions.Fraction.  There is no
sampling, floating point, network access, third-party package, or timestamp.
The output is a deterministic ledger intended to be byte-frozen.
"""

from collections import Counter, defaultdict, deque
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


def popcount(x):
    return x.bit_count()


def dag_analyzer(successors):
    """Return exact terminal/path/history/mean data for an acyclic rule."""

    @lru_cache(maxsize=None)
    def analyze(state):
        nxt = tuple(successors(state))
        if not nxt:
            return frozenset((state,)), frozenset((0,)), 1, Fraction(0)
        terminals = set()
        lengths = set()
        histories = 0
        mean = Fraction(1)
        for target in nxt:
            child_terminals, child_lengths, child_histories, child_mean = analyze(target)
            terminals.update(child_terminals)
            lengths.update(length + 1 for length in child_lengths)
            histories += child_histories
            mean += child_mean / len(nxt)
        return frozenset(terminals), frozenset(lengths), histories, mean

    return analyze


def terminal_law(successors):
    """Exact terminal law under uniform choice among listed active events."""

    @lru_cache(maxsize=None)
    def law(state):
        nxt = tuple(successors(state))
        if not nxt:
            return ((state, Fraction(1)),)
        out = Counter()
        for target in nxt:
            for terminal, mass in law(target):
                out[terminal] += mass / len(nxt)
        return tuple(sorted(out.items(), key=lambda item: repr(item[0])))

    return law


def polynomial_add(left, right, scale=1, shift=0):
    size = max(len(left), len(right) + shift)
    out = [0] * size
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i + shift] += scale * value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def polynomial_mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return tuple(out)


def binomial_polynomial(power):
    return tuple(comb(power, i) for i in range(power + 1))


# ---------------------------------------------------------------------------
# BR1--BR2: bipartite relations and local rectangle repair


def bipartite_rectangles(a, b):
    return tuple(
        tuple(sorted((i * b + j, i * b + jj, ii * b + j, ii * b + jj)))
        for i, ii in combinations(range(a), 2)
        for j, jj in combinations(range(b), 2)
    )


def bipartite_components(mask, a, b):
    adjacency = [set() for _ in range(a + b)]
    for i in range(a):
        for j in range(b):
            if mask >> (i * b + j) & 1:
                adjacency[i].add(a + j)
                adjacency[a + j].add(i)
    seen = set()
    components = []
    for start in range(a + b):
        if start in seen or not adjacency[start]:
            continue
        queue = [start]
        seen.add(start)
        left = set()
        right = set()
        while queue:
            vertex = queue.pop()
            if vertex < a:
                left.add(vertex)
            else:
                right.add(vertex - a)
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        components.append((tuple(sorted(left)), tuple(sorted(right))))
    return tuple(sorted(components))


def rectangle_closure(mask, a, b):
    out = mask
    for left, right in bipartite_components(mask, a, b):
        for i in left:
            for j in right:
                out |= 1 << (i * b + j)
    return out


@lru_cache(maxsize=None)
def connected_bipartite_edge_poly(a, b):
    """sum connected spanning bipartite graphs x^edges, with a>=1."""
    if b == 0:
        return (1,) if a == 1 else (0,)
    total = binomial_polynomial(a * b)
    answer = total
    for i in range(1, a + 1):
        for j in range(0, b + 1):
            if (i, j) == (a, b):
                continue
            coefficient = comb(a - 1, i - 1) * comb(b, j)
            component = connected_bipartite_edge_poly(i, j)
            remainder = binomial_polynomial((a - i) * (b - j))
            contribution = polynomial_mul(component, remainder)
            answer = polynomial_add(answer, contribution, scale=-coefficient)
    return answer


def target_rectangle_depth_poly(target, a, b):
    answer = (1,)
    for left, right in bipartite_components(target, a, b):
        aa, bb = len(left), len(right)
        edge_poly = connected_bipartite_edge_poly(aa, bb)
        reversed_poly = tuple(reversed(edge_poly))
        answer = polynomial_mul(answer, reversed_poly)
    return answer


def run_br1():
    before = ASSERTIONS
    states = 0
    target_count = 0
    largest_fibre = 0
    max_depth = 0
    for a, b in ((2, 2), (2, 3), (3, 3), (3, 4)):
        rectangles = bipartite_rectangles(a, b)

        def successors(mask):
            out = []
            for rectangle in rectangles:
                present = [edge for edge in rectangle if mask >> edge & 1]
                if len(present) == 3:
                    missing = next(edge for edge in rectangle if not (mask >> edge & 1))
                    out.append(mask | (1 << missing))
            return out

        analyze = dag_analyzer(successors)
        fibres = Counter()
        depth_fibres = defaultdict(Counter)
        for mask in range(1 << (a * b)):
            states += 1
            closure = rectangle_closure(mask, a, b)
            depth = popcount(closure) - popcount(mask)
            terminals, lengths, _, mean = analyze(mask)
            check(terminals == frozenset((closure,)), ("BR1 terminal", a, b, mask))
            check(lengths == frozenset((depth,)), ("BR1 depth", a, b, mask))
            check(mean == depth, ("BR1 mean", a, b, mask))
            check(not successors(closure), ("BR1 closed", a, b, mask))
            fibres[closure] += 1
            depth_fibres[closure][depth] += 1
            max_depth = max(max_depth, depth)
        for target, size in fibres.items():
            target_count += 1
            predicted = target_rectangle_depth_poly(target, a, b)
            actual = tuple(
                depth_fibres[target].get(i, 0) for i in range(len(predicted))
            )
            check(actual == predicted, ("BR1 fibre polynomial", a, b, target))
            check(sum(predicted) == size)
            largest_fibre = max(largest_fibre, size)
    record(
        "BR1", "bipartite relations / asynchronous 3-corner completion",
        "all relations in K_2,2; K_2,3; K_3,3; K_3,4", states,
        f"biclique-component terminal; all {target_count} target depth fibres match connected-bipartite reliability factors; max depth {max_depth}, max fibre {largest_fibre}",
        "RESERVE_COORDINATE_LEMMA_OWNER_HEAVY", before,
    )


def run_br2():
    before = ASSERTIONS
    states = 0
    nonconfluent = 0
    variable_clock = 0
    max_terminals = 0
    for a, b in ((2, 3), (3, 3)):
        rectangles = bipartite_rectangles(a, b)

        def successors(mask):
            out = []
            for rectangle in rectangles:
                missing = [edge for edge in rectangle if not (mask >> edge & 1)]
                if len(missing) == 1:
                    rows = sorted({edge // b for edge in rectangle})
                    cols = sorted({edge % b for edge in rectangle})
                    mr, mc = divmod(missing[0], b)
                    opposite = next(
                        edge for edge in rectangle
                        if edge // b != mr and edge % b != mc
                    )
                    out.append(mask ^ (1 << opposite))
            return out

        analyze = dag_analyzer(successors)
        law = terminal_law(successors)
        for mask in range(1 << (a * b)):
            states += 1
            terminals, lengths, _, mean = analyze(mask)
            check(all(not successors(target) for target in terminals))
            check(mean >= min(lengths) and mean <= max(lengths))
            masses = dict(law(mask))
            check(sum(masses.values(), Fraction()) == 1)
            check(set(masses) == set(terminals))
            nonconfluent += len(terminals) > 1
            variable_clock += len(lengths) > 1
            max_terminals = max(max_terminals, len(terminals))
    record(
        "BR2", "bipartite relations / stochastic 3-corner erosion",
        "all relations in K_2,3 and K_3,3", states,
        f"{nonconfluent} nonconfluent and {variable_clock} variable-clock sources; at most {max_terminals} terminals",
        "KILL_NONCONFLUENT_RECTANGLE_REPAIR", before,
    )


# ---------------------------------------------------------------------------
# FG1--FG4: finite affine/projective geometry processes


def xor_basis(vectors):
    basis = {}
    for value in vectors:
        x = value
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                for other in tuple(basis):
                    if other != pivot and (basis[other] >> pivot) & 1:
                        basis[other] ^= x
                break
    return tuple(basis[pivot] for pivot in sorted(basis, reverse=True))


def linear_span_mask(vectors):
    basis = xor_basis(vectors)
    values = {0}
    for vector in basis:
        values.update(value ^ vector for value in tuple(values))
    return sum(1 << value for value in values)


def affine_closure_mask(mask, d):
    if mask == 0:
        return 0
    points = [point for point in range(1 << d) if mask >> point & 1]
    origin = points[0]
    differences = [point ^ origin for point in points[1:]]
    linear = linear_span_mask(differences)
    return sum(1 << (origin ^ value) for value in range(1 << d) if linear >> value & 1)


def gaussian_two(n, k):
    if k < 0 or k > n:
        return 0
    numerator = denominator = 1
    for i in range(k):
        numerator *= (1 << (n - i)) - 1
        denominator *= (1 << (k - i)) - 1
    return numerator // denominator


def affine_spanning_depth_poly(rank):
    if rank == 0:
        return (1,)
    size = 1 << rank
    # Include exponent ``size`` temporarily for the empty subset.  For
    # positive rank its coefficient cancels under affine-flat Moebius
    # inversion, after which the trailing zero is removed below.
    out = [0] * (size + 1)
    for subrank in range(rank + 1):
        codim = rank - subrank
        number = (1 << codim) * gaussian_two(rank, subrank)
        mu = (-1) ** codim * (1 << (codim * (codim - 1) // 2))
        # The empty set has no affine hull and must be removed before
        # Moebius inversion on the nonempty affine-flat lattice.
        for subset_size in range(1, (1 << subrank) + 1):
            out[size - subset_size] += number * mu * comb(1 << subrank, subset_size)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def run_fg1():
    before = ASSERTIONS
    states = 0
    target_count = 0
    max_fibre = 0
    for d in (1, 2, 3):
        points = tuple(range(1 << d))
        triples = tuple(combinations(points, 3))

        def successors(mask):
            out = []
            for x, y, z in triples:
                if all(mask >> point & 1 for point in (x, y, z)):
                    fourth = x ^ y ^ z
                    if not (mask >> fourth & 1):
                        out.append(mask | (1 << fourth))
            return out

        analyze = dag_analyzer(successors)
        fibres = Counter()
        depth_fibres = defaultdict(Counter)
        for mask in range(1 << (1 << d)):
            states += 1
            closure = affine_closure_mask(mask, d)
            depth = popcount(closure) - popcount(mask)
            terminals, lengths, _, mean = analyze(mask)
            check(terminals == frozenset((closure,)))
            check(lengths == frozenset((depth,)))
            check(mean == depth)
            fibres[closure] += 1
            depth_fibres[closure][depth] += 1
        for target, size in fibres.items():
            target_count += 1
            if target == 0:
                predicted = (1,)
            else:
                rank = popcount(target).bit_length() - 1
                predicted = affine_spanning_depth_poly(rank)
            actual = tuple(depth_fibres[target].get(i, 0) for i in range(len(predicted)))
            check(actual == predicted, ("FG1 affine fibre", d, target, actual, predicted))
            check(sum(predicted) == size)
            max_fibre = max(max_fibre, size)
    record(
        "FG1", "subsets of binary affine space / parallelogram completion",
        "all subsets of AG(d,2), d=1,2,3", states,
        f"terminal is affine span; every one of {target_count} fibres has the affine-lattice Moebius depth polynomial; max fibre {max_fibre}",
        "RESERVE_CLASSICAL_AFFINE_CLOSURE", before,
    )


def affine_planes(d):
    planes = set()
    points = range(1 << d)
    for x, y, z in combinations(points, 3):
        fourth = x ^ y ^ z
        if fourth not in (x, y, z):
            planes.add(tuple(sorted((x, y, z, fourth))))
    return tuple(sorted(planes))


def run_fg2():
    before = ASSERTIONS
    d = 3
    planes = affine_planes(d)

    def successors(mask):
        out = []
        for plane in planes:
            if all(mask >> point & 1 for point in plane):
                for point in plane:
                    out.append(mask ^ (1 << point))
        return out

    analyze = dag_analyzer(successors)
    law = terminal_law(successors)
    states = nonconfluent = variable_clock = max_terminals = 0
    for mask in range(1 << (1 << d)):
        states += 1
        terminals, lengths, _, mean = analyze(mask)
        masses = dict(law(mask))
        check(sum(masses.values(), Fraction()) == 1)
        check(set(masses) == set(terminals))
        check(all(not successors(target) for target in terminals))
        check(mean >= min(lengths) and mean <= max(lengths))
        nonconfluent += len(terminals) > 1
        variable_clock += len(lengths) > 1
        max_terminals = max(max_terminals, len(terminals))
    record(
        "FG2", "subsets of AG(3,2) / random full-parallelogram thinning",
        "all 256 subsets; uniform active plane-and-point deletion", states,
        f"{nonconfluent} nonconfluent sources, {variable_clock} variable clocks, at most {max_terminals} cap-set terminals",
        "KILL_CAP_SET_THINNING_NO_CLOSED_LAW", before,
    )


def fano_lines():
    lines = set()
    for x, y in combinations(range(1, 8), 2):
        lines.add(tuple(sorted((x, y, x ^ y))))
    return tuple(sorted(lines))


def vector_span_nonzero(mask):
    vectors = [point for point in range(1, 8) if mask >> (point - 1) & 1]
    linear = linear_span_mask(vectors)
    return sum(1 << (point - 1) for point in range(1, 8) if linear >> point & 1)


def projective_spanning_depth_poly(rank):
    if rank == 0:
        return (1,)
    target_size = (1 << rank) - 1
    out = [0] * (target_size + 1)
    for subrank in range(rank + 1):
        codim = rank - subrank
        number = gaussian_two(rank, subrank)
        mu = (-1) ** codim * (1 << (codim * (codim - 1) // 2))
        subsize = (1 << subrank) - 1
        for subset_size in range(subsize + 1):
            out[target_size - subset_size] += number * mu * comb(subsize, subset_size)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def run_fg3():
    before = ASSERTIONS
    lines = fano_lines()

    def successors(mask):
        out = []
        for line in lines:
            present = [point for point in line if mask >> (point - 1) & 1]
            if len(present) == 2:
                missing = next(point for point in line if not (mask >> (point - 1) & 1))
                out.append(mask | (1 << (missing - 1)))
        return out

    analyze = dag_analyzer(successors)
    fibres = Counter()
    depth_fibres = defaultdict(Counter)
    max_depth = 0
    for mask in range(128):
        closure = vector_span_nonzero(mask)
        depth = popcount(closure) - popcount(mask)
        terminals, lengths, _, mean = analyze(mask)
        check(terminals == frozenset((closure,)))
        check(lengths == frozenset((depth,)))
        check(mean == depth)
        fibres[closure] += 1
        depth_fibres[closure][depth] += 1
        max_depth = max(max_depth, depth)
    for target, size in fibres.items():
        rank = 0 if target == 0 else (popcount(target) + 1).bit_length() - 1
        predicted = projective_spanning_depth_poly(rank)
        actual = tuple(depth_fibres[target].get(i, 0) for i in range(len(predicted)))
        check(actual == predicted)
        check(sum(predicted) == size)
    record(
        "FG3", "Fano-plane point sets / two-points-complete-a-line",
        "all 128 point subsets", 128,
        f"terminal is projective span; {len(fibres)} target fibres match subspace-Moebius polynomials; max depth {max_depth}",
        "KILL_MATROID_CLOSURE_DIRECT", before,
    )


def binary_rank(points):
    return len(xor_basis(points))


def fano_circuits():
    universe = tuple(range(1, 8))
    circuits = []
    for size in range(3, 5):
        for subset in combinations(universe, size):
            if binary_rank(subset) == size:
                continue
            if all(binary_rank(subset[:i] + subset[i + 1 :]) == size - 1 for i in range(size)):
                circuits.append(subset)
    return tuple(circuits)


def run_fg4():
    before = ASSERTIONS
    circuits = fano_circuits()

    def successors(mask):
        out = []
        for circuit in circuits:
            if all(mask >> (point - 1) & 1 for point in circuit):
                for point in circuit:
                    out.append(mask ^ (1 << (point - 1)))
        return out

    analyze = dag_analyzer(successors)
    law = terminal_law(successors)
    multi = max_terminals = 0
    for mask in range(128):
        vectors = tuple(point for point in range(1, 8) if mask >> (point - 1) & 1)
        rank = binary_rank(vectors)
        span = vector_span_nonzero(mask)
        terminals, lengths, _, mean = analyze(mask)
        check(lengths == frozenset((popcount(mask) - rank,)))
        check(mean == popcount(mask) - rank)
        for terminal in terminals:
            terminal_vectors = tuple(
                point for point in range(1, 8) if terminal >> (point - 1) & 1
            )
            check(len(terminal_vectors) == binary_rank(terminal_vectors) == rank)
            check(vector_span_nonzero(terminal) == span)
        masses = dict(law(mask))
        check(sum(masses.values(), Fraction()) == 1)
        check(set(masses) == set(terminals))
        multi += len(terminals) > 1
        max_terminals = max(max_terminals, len(terminals))
    record(
        "FG4", "Fano matroid subsets / uniform active-circuit deletion",
        "all 128 subsets; every contained circuit and deleted circuit element", 128,
        f"rank and span are invariant, clock is nullity; {multi} multi-basis sources and at most {max_terminals} terminals",
        "KILL_RANDOM_MATROID_BASIS_REDUCTION", before,
    )


# ---------------------------------------------------------------------------
# HG1--HG5: hypergraph and set-family rewrites


def triple_universe(n):
    triples = tuple(combinations(range(n), 3))
    index = {triple: i for i, triple in enumerate(triples)}
    boundaries = tuple(
        tuple(index[face] for face in combinations(four, 3))
        for four in combinations(range(n), 4)
    )
    return triples, boundaries


def simplicial_matroid_closure(mask, n, triples):
    """Closure of triangles in the binary boundary-vector matroid."""
    edges = tuple(combinations(range(n), 2))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    vectors = []
    for triple in triples:
        vector = 0
        for edge in combinations(triple, 2):
            vector |= 1 << edge_index[edge]
        vectors.append(vector)
    selected = tuple(vectors[i] for i in range(len(triples)) if mask >> i & 1)
    basis = xor_basis(selected)
    rank = len(basis)
    return sum(
        1 << i for i, vector in enumerate(vectors)
        if len(xor_basis(basis + (vector,))) == rank
    )


def run_hg1():
    before = ASSERTIONS
    states = closed_targets = max_depth = max_fibre = 0
    for n in (4, 5):
        triples, boundaries = triple_universe(n)

        def successors(mask):
            out = []
            for boundary in boundaries:
                missing = [face for face in boundary if not (mask >> face & 1)]
                if len(missing) == 1:
                    out.append(mask | (1 << missing[0]))
            return out

        analyze = dag_analyzer(successors)
        fibres = Counter()
        for mask in range(1 << len(triples)):
            states += 1
            terminals, lengths, _, mean = analyze(mask)
            check(len(terminals) == 1)
            terminal = next(iter(terminals))
            depth = popcount(terminal) - popcount(mask)
            check(lengths == frozenset((depth,)))
            check(mean == depth)
            check(not successors(terminal))
            check(
                terminal == simplicial_matroid_closure(mask, n, triples),
                ("HG1 simplicial-matroid closure", n, mask, terminal),
            )
            fibres[terminal] += 1
            max_depth = max(max_depth, depth)
        closed_targets += len(fibres)
        max_fibre = max(max_fibre, max(fibres.values()))

    # The equality above is a low-dimensional coincidence, not an all-n
    # theorem.  At n=6 this seven-face set is already Horn-closed although
    # the boundary vector of (3,4,5) lies in its binary linear span.
    n = 6
    triples, boundaries = triple_universe(n)
    triple_index = {triple: i for i, triple in enumerate(triples)}
    witness_faces = (
        (0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4),
        (1, 2, 5), (1, 3, 5), (2, 4, 5),
    )
    witness = sum(1 << triple_index[face] for face in witness_faces)
    linear_closure = simplicial_matroid_closure(witness, n, triples)
    forced_face = 1 << triple_index[(3, 4, 5)]
    check(all(
        sum((witness >> face) & 1 for face in boundary) != 3
        for boundary in boundaries
    ))
    check(not (witness & forced_face) and linear_closure & forced_face)
    states += 1
    record(
        "HG1", "3-uniform hypergraphs / tetrahedron-boundary completion",
        "all 3-graphs on n=4,5; one exact n=6 separation witness", states,
        f"n=4,5 mimic simplicial-matroid closure ({closed_targets} flats), but a 7-face n=6 absorbing state omits a linearly forced face; max audited depth {max_depth}, fibre {max_fibre}",
        "KILL_LOW_DIMENSION_MATROID_MIRAGE_NO_ATLAS", before,
    )


def run_hg2():
    before = ASSERTIONS
    states = nonconfluent = variable_clock = max_terminals = 0
    for n in (4, 5):
        triples, boundaries = triple_universe(n)

        def successors(mask):
            out = []
            for boundary in boundaries:
                if all(mask >> face & 1 for face in boundary):
                    for face in boundary:
                        out.append(mask ^ (1 << face))
            return out

        analyze = dag_analyzer(successors)
        law = terminal_law(successors)
        for mask in range(1 << len(triples)):
            states += 1
            terminals, lengths, _, mean = analyze(mask)
            masses = dict(law(mask))
            check(sum(masses.values(), Fraction()) == 1)
            check(set(masses) == set(terminals))
            check(all(not successors(target) for target in terminals))
            check(mean >= min(lengths) and mean <= max(lengths))
            nonconfluent += len(terminals) > 1
            variable_clock += len(lengths) > 1
            max_terminals = max(max_terminals, len(terminals))
    record(
        "HG2", "3-uniform hypergraphs / random tetrahedron-face erosion",
        "all 3-graphs on n=4,5", states,
        f"{nonconfluent} nonconfluent and {variable_clock} variable-clock sources; at most {max_terminals} terminals",
        "KILL_NONCONFLUENT_TETRAHEDRON_EROSION", before,
    )


def nonempty_subsets(n):
    return tuple(mask for mask in range(1, 1 << n))


def run_hg3():
    before = ASSERTIONS
    ground = nonempty_subsets(3)

    def successors(family):
        out = []
        for i, small in enumerate(ground):
            if not (family >> i & 1):
                continue
            for j, large in enumerate(ground):
                if i != j and family >> j & 1 and small & large == small:
                    out.append(family ^ (1 << j))
        return out

    analyze = dag_analyzer(successors)
    max_depth = max_histories = 0
    for family in range(1 << len(ground)):
        minimal = 0
        for i, edge in enumerate(ground):
            if family >> i & 1 and not any(
                family >> j & 1 and other != edge and other & edge == other
                for j, other in enumerate(ground)
            ):
                minimal |= 1 << i
        depth = popcount(family) - popcount(minimal)
        terminals, lengths, histories, mean = analyze(family)
        check(terminals == frozenset((minimal,)))
        check(lengths == frozenset((depth,)))
        check(mean == depth)
        max_depth = max(max_depth, depth)
        max_histories = max(max_histories, histories)
    record(
        "HG3", "finite set families / asynchronous dominated-edge deletion",
        "all 128 families of nonempty subsets of [3]", 128,
        f"unique Sperner kernel, fixed deletion clock; max depth {max_depth}, max witness-labelled histories {max_histories}",
        "KILL_SPERNERIZATION_TRIVIAL", before,
    )


def run_hg4():
    before = ASSERTIONS
    ground = tuple(range(8))

    def successors(family):
        out = []
        present = [i for i in ground if family >> i & 1]
        for a, b in combinations(present, 2):
            union = a | b
            if not (family >> union & 1):
                out.append(family | (1 << union))
        return out

    analyze = dag_analyzer(successors)
    targets = set()
    max_depth = 0
    for family in range(256):
        terminals, lengths, _, mean = analyze(family)
        check(len(terminals) == 1)
        terminal = next(iter(terminals))
        depth = popcount(terminal) - popcount(family)
        check(lengths == frozenset((depth,)))
        check(mean == depth)
        check(not successors(terminal))
        targets.add(terminal)
        max_depth = max(max_depth, depth)
    record(
        "HG4", "set families / asynchronous union-closure completion",
        "all 256 families on 2^[3]", 256,
        f"generic semilattice closure; {len(targets)} targets and max depth {max_depth}",
        "KILL_GENERIC_SEMILATTICE_CLOSURE", before,
    )


def run_hg5():
    before = ASSERTIONS
    ground = nonempty_subsets(3)

    def successors(family):
        out = []
        present = [i for i in range(len(ground)) if family >> i & 1]
        for i, j in combinations(present, 2):
            a, b = ground[i], ground[j]
            if a & b in (a, b):
                continue
            if popcount(a) < popcount(b):
                out.append(family ^ (1 << j))
            elif popcount(b) < popcount(a):
                out.append(family ^ (1 << i))
            else:
                out.append(family ^ (1 << i))
                out.append(family ^ (1 << j))
        return out

    analyze = dag_analyzer(successors)
    law = terminal_law(successors)
    nonconfluent = variable_clock = max_terminals = 0
    for family in range(1 << len(ground)):
        terminals, lengths, _, mean = analyze(family)
        masses = dict(law(family))
        check(sum(masses.values(), Fraction()) == 1)
        check(set(masses) == set(terminals))
        check(all(not successors(target) for target in terminals))
        check(mean >= min(lengths) and mean <= max(lengths))
        nonconfluent += len(terminals) > 1
        variable_clock += len(lengths) > 1
        max_terminals = max(max_terminals, len(terminals))
    record(
        "HG5", "set families / random incomparability thinning",
        "all 128 families of nonempty subsets of [3]", 128,
        f"{nonconfluent} nonconfluent and {variable_clock} variable-clock sources; at most {max_terminals} chain terminals",
        "KILL_ARBITRARY_CHAIN_THINNING", before,
    )


# ---------------------------------------------------------------------------
# MT1--MT3: weighted matching, matroidal deletion, and lozenge/ideal flips


def run_mt1():
    before = ASSERTIONS
    states = nonconfluent = variable_clock = max_terminals = 0
    for edge_count in (3, 4, 5):
        for order in permutations(range(edge_count)):
            weight = {edge: order[edge] for edge in range(edge_count)}

            def successors(mask):
                out = []
                for edge in range(edge_count - 1):
                    if mask >> edge & 1 and mask >> (edge + 1) & 1:
                        loser = edge if weight[edge] < weight[edge + 1] else edge + 1
                        out.append(mask ^ (1 << loser))
                return out

            analyze = dag_analyzer(successors)
            law = terminal_law(successors)
            for mask in range(1 << edge_count):
                states += 1
                terminals, lengths, _, mean = analyze(mask)
                masses = dict(law(mask))
                check(sum(masses.values(), Fraction()) == 1)
                check(set(masses) == set(terminals))
                check(all(target & (target << 1) == 0 for target in terminals))
                check(mean >= min(lengths) and mean <= max(lengths))
                nonconfluent += len(terminals) > 1
                variable_clock += len(lengths) > 1
                max_terminals = max(max_terminals, len(terminals))
    record(
        "MT1", "distinctly weighted path edges / pairwise conflict elimination",
        "all weight orders and active subsets for 3,4,5 path edges", states,
        f"{nonconfluent} nonconfluent and {variable_clock} variable-clock weighted instances; at most {max_terminals} matchings",
        "KILL_ASYNCHRONOUS_MATCHING_HEURISTIC", before,
    )


def graph_components(mask, n, edges):
    adjacency = [set() for _ in range(n)]
    for index, (u, v) in enumerate(edges):
        if mask >> index & 1:
            adjacency[u].add(v)
            adjacency[v].add(u)
    seen = set()
    components = []
    for start in range(n):
        if start in seen:
            continue
        queue = [start]
        seen.add(start)
        comp = []
        while queue:
            u = queue.pop()
            comp.append(u)
            for v in adjacency[u]:
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
        components.append(tuple(sorted(comp)))
    return tuple(sorted(components))


def run_mt2():
    before = ASSERTIONS
    states = multi = max_terminals = 0
    for n in (4, 5):
        edges = tuple(combinations(range(n), 2))

        def successors(mask):
            base = graph_components(mask, n, edges)
            out = []
            for edge in range(len(edges)):
                if mask >> edge & 1:
                    target = mask ^ (1 << edge)
                    if graph_components(target, n, edges) == base:
                        out.append(target)
            return out

        analyze = dag_analyzer(successors)
        law = terminal_law(successors)
        for mask in range(1 << len(edges)):
            states += 1
            components = graph_components(mask, n, edges)
            rank = n - len(components)
            depth = popcount(mask) - rank
            terminals, lengths, _, mean = analyze(mask)
            check(lengths == frozenset((depth,)))
            check(mean == depth)
            for terminal in terminals:
                check(popcount(terminal) == rank)
                check(graph_components(terminal, n, edges) == components)
            masses = dict(law(mask))
            check(sum(masses.values(), Fraction()) == 1)
            check(set(masses) == set(terminals))
            multi += len(terminals) > 1
            max_terminals = max(max_terminals, len(terminals))
    record(
        "MT2", "labelled graphs / uniform cycle-edge reverse deletion",
        "all graphs on n=4,5", states,
        f"graphic-matroid rank clock; {multi} multi-forest sources and at most {max_terminals} spanning-forest terminals",
        "KILL_RANDOM_SPANNING_FOREST_CLASSICAL", before,
    )


def poset_box(a, b, c):
    elements = tuple(product(range(a), range(b), range(c)))
    index = {element: i for i, element in enumerate(elements)}
    lower_masks = []
    upper_masks = []
    for x, y, z in elements:
        lower = 0
        upper = 0
        for xx, yy, zz in elements:
            if xx <= x and yy <= y and zz <= z and (xx, yy, zz) != (x, y, z):
                lower |= 1 << index[(xx, yy, zz)]
            if xx >= x and yy >= y and zz >= z and (xx, yy, zz) != (x, y, z):
                upper |= 1 << index[(xx, yy, zz)]
        lower_masks.append(lower)
        upper_masks.append(upper)
    return elements, tuple(lower_masks), tuple(upper_masks)


def run_mt3():
    before = ASSERTIONS
    states = max_histories = max_depth = 0
    for a, b, c in ((2, 2, 2), (2, 2, 3), (2, 2, 4)):
        elements, lower, upper = poset_box(a, b, c)
        ideals = tuple(
            mask for mask in range(1 << len(elements))
            if all(not (mask >> i & 1) or lower[i] & ~mask == 0 for i in range(len(elements)))
        )

        def successors(mask):
            return [
                mask ^ (1 << i) for i in range(len(elements))
                if mask >> i & 1 and upper[i] & mask == 0
            ]

        analyze = dag_analyzer(successors)
        for mask in ideals:
            states += 1
            depth = popcount(mask)
            terminals, lengths, histories, mean = analyze(mask)
            check(terminals == frozenset((0,)))
            check(lengths == frozenset((depth,)))
            check(mean == depth)
            max_histories = max(max_histories, histories)
            max_depth = max(max_depth, depth)
    record(
        "MT3", "boxed plane partitions / random removable-cube flips",
        "all ideals in 2x2x2, 2x2x3, 2x2x4 boxes", states,
        f"volume clock and linear-extension histories; max depth {max_depth}, max histories {max_histories}",
        "KILL_DISTRIBUTIVE_LATTICE_LINEAR_EXTENSIONS", before,
    )


# ---------------------------------------------------------------------------
# W01--W04: non-transport local word and associahedral rewrites


def all_words(alphabet, maximum_length):
    for length in range(maximum_length + 1):
        yield from product(alphabet, repeat=length)


def audit_word_rule(handle, description, alphabet, maximum_length, successor_builder, disposition):
    before = ASSERTIONS
    analyze = dag_analyzer(successor_builder)
    law = terminal_law(successor_builder)
    states = nonconfluent = variable_clock = max_terminals = max_depth = 0
    for word in all_words(alphabet, maximum_length):
        states += 1
        terminals, lengths, _, mean = analyze(word)
        masses = dict(law(word))
        check(sum(masses.values(), Fraction()) == 1)
        check(set(masses) == set(terminals))
        check(all(not successor_builder(target) for target in terminals))
        check(mean >= min(lengths) and mean <= max(lengths))
        nonconfluent += len(terminals) > 1
        variable_clock += len(lengths) > 1
        max_terminals = max(max_terminals, len(terminals))
        max_depth = max(max_depth, max(lengths))
    record(
        handle, description,
        f"all {len(alphabet)}-ary words of lengths 0..{maximum_length}", states,
        f"{nonconfluent} nonconfluent, {variable_clock} variable-clock; max terminals {max_terminals}, max depth {max_depth}",
        disposition, before,
    )


def run_w01():
    def successors(word):
        return [
            word[:i] + (word[i],) + word[i + 3 :]
            for i in range(len(word) - 2) if word[i] == word[i + 2]
        ]

    audit_word_rule(
        "W01", "ternary words / local loop erasure aba -> a", (0, 1, 2), 9,
        successors, "KILL_FREE_BAND_LOOP_ERASURE_OWNER",
    )


def run_w02():
    def successors(word):
        return [
            word[:i] + word[i : i + 2] + word[i + 4 :]
            for i in range(len(word) - 3)
            if word[i : i + 2] == word[i + 2 : i + 4]
        ]

    audit_word_rule(
        "W02", "binary words / adjacent length-two square contraction", (0, 1), 14,
        successors, "KILL_WORD_EQUATION_SQUARE_REDUCTION",
    )


def run_w03():
    def successors(word):
        return [
            word[:i] + (word[i], word[i + 3]) + word[i + 4 :]
            for i in range(len(word) - 3)
            if word[i] == word[i + 3] and word[i + 1] == word[i + 2]
        ]

    audit_word_rule(
        "W03", "ternary words / doubled-palindrome interior collapse abba -> aa",
        (0, 1, 2), 9, successors, "KILL_LOCAL_REDUCTION_NO_UNIFORM_NORMAL_FORM",
    )


def full_binary_trees(leaves):
    @lru_cache(maxsize=None)
    def build(n):
        if n == 1:
            return ("x",)
        out = []
        for left_size in range(1, n):
            for left in build(left_size):
                for right in build(n - left_size):
                    out.append((left, right))
        return tuple(out)

    return build(leaves)


def tamari_successors(tree):
    if tree == "x":
        return []
    left, right = tree
    out = []
    if left != "x":
        a, b = left
        out.append((a, (b, right)))
    for new_left in tamari_successors(left):
        out.append((new_left, right))
    for new_right in tamari_successors(right):
        out.append((left, new_right))
    return out


def right_comb(leaves):
    tree = "x"
    for _ in range(leaves - 1):
        tree = ("x", tree)
    return tree


def run_w04():
    before = ASSERTIONS
    analyze = dag_analyzer(tamari_successors)
    states = variable_clock = max_depth = max_histories = 0
    for leaves in range(1, 9):
        target = right_comb(leaves)
        for tree in full_binary_trees(leaves):
            states += 1
            terminals, lengths, histories, mean = analyze(tree)
            check(terminals == frozenset((target,)))
            check(mean >= min(lengths) and mean <= max(lengths))
            variable_clock += len(lengths) > 1
            max_depth = max(max_depth, max(lengths))
            max_histories = max(max_histories, histories)
    record(
        "W04", "binary bracketings / asynchronous right Tamari rotations",
        "all full binary trees with 1..8 leaves", states,
        f"unique right comb but {variable_clock} variable-clock states; max depth {max_depth}, max histories {max_histories}",
        "KILL_TAMARI_LATTICE_DIRECT_OWNER", before,
    )


# ---------------------------------------------------------------------------
# BF1--BF2: finite signed-CNF simplification processes


def clauses_for_variables(n):
    clauses = []
    for choices in product((0, 1, -1), repeat=n):
        if all(choice == 0 for choice in choices):
            continue
        positive = sum(1 << i for i, choice in enumerate(choices) if choice == 1)
        negative = sum(1 << i for i, choice in enumerate(choices) if choice == -1)
        clauses.append((positive, negative))
    return tuple(clauses)


def formula_family(n):
    clauses = clauses_for_variables(n)
    if n == 2:
        return clauses, tuple(
            frozenset(clauses[i] for i in range(len(clauses)) if mask >> i & 1)
            for mask in range(1 << len(clauses))
        )
    formulas = {frozenset()}
    for size in range(1, 5):
        formulas.update(frozenset(choice) for choice in combinations(clauses, size))
    return clauses, tuple(sorted(formulas, key=lambda f: (len(f), repr(sorted(f)))))


def run_bf1():
    before = ASSERTIONS
    states = nonconfluent = variable_clock = max_terminals = 0
    for n in (2, 3):
        _, formulas = formula_family(n)

        def successors(formula):
            if (0, 0) in formula:
                return []
            positive_all = 0
            negative_all = 0
            for positive, negative in formula:
                positive_all |= positive
                negative_all |= negative
            out = []
            for variable in range(n):
                bit = 1 << variable
                if positive_all & bit and not negative_all & bit:
                    out.append(frozenset(
                        clause for clause in formula if not clause[0] & bit
                    ))
                if negative_all & bit and not positive_all & bit:
                    out.append(frozenset(
                        clause for clause in formula if not clause[1] & bit
                    ))
            return out

        analyze = dag_analyzer(successors)
        law = terminal_law(successors)
        for formula in formulas:
            states += 1
            terminals, lengths, _, mean = analyze(formula)
            masses = dict(law(formula))
            check(sum(masses.values(), Fraction()) == 1)
            check(set(masses) == set(terminals))
            check(all(not successors(target) for target in terminals))
            check(mean >= min(lengths) and mean <= max(lengths))
            nonconfluent += len(terminals) > 1
            variable_clock += len(lengths) > 1
            max_terminals = max(max_terminals, len(terminals))
    record(
        "BF1", "signed CNF formulas / asynchronous pure-literal elimination",
        "all two-variable formulas; all three-variable formulas with <=4 clauses", states,
        f"{nonconfluent} nonconfluent and {variable_clock} variable-clock formulas; at most {max_terminals} residual cores",
        "KILL_PURE_LITERAL_ALGORITHM_CLASSICAL", before,
    )


def run_bf2():
    before = ASSERTIONS
    states = nonconfluent = variable_clock = conflicts = max_terminals = 0
    for n in (2, 3):
        _, formulas = formula_family(n)

        def successors(formula):
            if (0, 0) in formula:
                return []
            units = set()
            for positive, negative in formula:
                if popcount(positive) + popcount(negative) == 1:
                    if positive:
                        units.add((positive.bit_length() - 1, True))
                    else:
                        units.add((negative.bit_length() - 1, False))
            out = []
            for variable, value in sorted(units):
                bit = 1 << variable
                reduced = set()
                for positive, negative in formula:
                    if (value and positive & bit) or ((not value) and negative & bit):
                        continue
                    if value:
                        negative &= ~bit
                    else:
                        positive &= ~bit
                    reduced.add((positive, negative))
                out.append(frozenset(reduced))
            return out

        analyze = dag_analyzer(successors)
        law = terminal_law(successors)
        for formula in formulas:
            states += 1
            terminals, lengths, _, mean = analyze(formula)
            masses = dict(law(formula))
            check(sum(masses.values(), Fraction()) == 1)
            check(set(masses) == set(terminals))
            check(all(not successors(target) for target in terminals))
            check(mean >= min(lengths) and mean <= max(lengths))
            nonconfluent += len(terminals) > 1
            variable_clock += len(lengths) > 1
            conflicts += any((0, 0) in target for target in terminals)
            max_terminals = max(max_terminals, len(terminals))
    record(
        "BF2", "signed CNF formulas / asynchronous unit propagation",
        "all two-variable formulas; all three-variable formulas with <=4 clauses", states,
        f"{conflicts} formulas reach contradiction; {nonconfluent} nonconfluent and {variable_clock} variable-clock cases; max terminals {max_terminals}",
        "KILL_UNIT_PROPAGATION_CLASSICAL", before,
    )


def main():
    runners = (
        run_br1, run_br2,
        run_fg1, run_fg2, run_fg3, run_fg4,
        run_hg1, run_hg2, run_hg3, run_hg4, run_hg5,
        run_mt1, run_mt2, run_mt3,
        run_w01, run_w02, run_w03, run_w04,
        run_bf1, run_bf2,
    )
    for runner in runners:
        runner()
    check(len(ROWS) == 20, "system-count sentinel")
    check(len({row[0] for row in ROWS}) == 20, "unique-handle sentinel")
    check(all(row[3] > 0 and row[4] > 0 for row in ROWS), "nonempty-ledger sentinel")
    print("REPLACEMENT_STOCHASTIC_SCOUT_V1")
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
