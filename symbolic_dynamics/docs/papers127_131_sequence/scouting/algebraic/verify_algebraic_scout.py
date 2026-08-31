#!/usr/bin/env python3
"""Exact breadth pilot for the P127--P131 algebraic scouting lane.

Every system below is a literal finite dynamical map.  The script uses only
the Python standard library, exact integer/finite-field arithmetic, and
deterministic exhaustive enumeration.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import permutations, product
from math import comb, gcd


ASSERTIONS = 0
RESULTS = []


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def record(system_id, family, scope, start, signal, decision, reason, **metrics):
    RESULTS.append({
        "id": system_id,
        "family": family,
        "scope": scope,
        "assertions": ASSERTIONS - start,
        "signal": signal,
        "decision": decision,
        "reason": reason,
        "metrics": metrics,
    })


def orbit_stats(states, step):
    states = tuple(states)
    state_set = set(states)
    nxt = {}
    for state in states:
        image = step(state)
        check(image in state_set, "map left its finite state space")
        nxt[state] = image
    fixed = sum(nxt[state] == state for state in states)
    max_tail = 0
    max_period = 0
    period_hist = {}
    for state in states:
        seen = {}
        current = state
        while current not in seen:
            seen[current] = len(seen)
            current = nxt[current]
        tail = seen[current]
        period = len(seen) - seen[current]
        check(period >= 1, "missing eventual cycle")
        max_tail = max(max_tail, tail)
        max_period = max(max_period, period)
        period_hist[period] = period_hist.get(period, 0) + 1
    return {
        "states": len(states),
        "fixed": fixed,
        "max_tail": max_tail,
        "max_period": max_period,
        "periods": "/".join(f"{k}:{period_hist[k]}" for k in sorted(period_hist)),
    }


# ---------------------------------------------------------------------------
# Finite modules and subspace lattices over F_2


def span_mask(vectors):
    basis = []
    for value in vectors:
        x = value
        for pivot in basis:
            x = min(x, x ^ pivot)
        if x:
            basis.append(x)
            basis.sort(reverse=True)
    values = {0}
    for pivot in basis:
        values |= {x ^ pivot for x in tuple(values)}
    return sum(1 << value for value in values)


@lru_cache(maxsize=None)
def subspaces(dimension):
    vectors = list(range(1, 1 << dimension))
    spaces = set()
    for selector in range(1 << len(vectors)):
        chosen = [vectors[i] for i in range(len(vectors)) if selector >> i & 1]
        spaces.add(span_mask(chosen))
    return tuple(sorted(spaces))


def space_elements(space):
    return [value for value in range(space.bit_length()) if space >> value & 1]


@lru_cache(maxsize=None)
def space_join(left, right):
    return span_mask(space_elements(left) + space_elements(right))


def space_leq(left, right):
    return left & ~right == 0


def space_dim(space):
    size = space.bit_count()
    return size.bit_length() - 1


def tuple_join(values):
    answer = 1
    for value in values:
        answer = space_join(answer, value)
    return answer


def tuple_meet(values):
    answer = values[0]
    for value in values[1:]:
        answer &= value
    return answer


def gaussian_binomial(dimension, rank, prime_power):
    if rank < 0 or rank > dimension:
        return 0
    rank = min(rank, dimension - rank)
    numerator = 1
    denominator = 1
    for index in range(rank):
        numerator *= prime_power ** (dimension - index) - 1
        denominator *= prime_power ** (rank - index) - 1
    check(numerator % denominator == 0, "Gaussian binomial lost integrality")
    return numerator // denominator


@lru_cache(maxsize=None)
def weak_flag_count(dimension, length, prime_power):
    """Number of U_1 <= ... <= U_length in F_q^dimension."""
    if length == 0:
        return 1
    return sum(gaussian_binomial(dimension, rank, prime_power)
               * weak_flag_count(rank, length - 1, prime_power)
               for rank in range(dimension + 1))


def bubble_sweep(values):
    answer = list(values)
    for index in range(len(answer) - 1):
        left, right = answer[index], answer[index + 1]
        answer[index] = left & right
        answer[index + 1] = space_join(left, right)
    return tuple(answer)


def run_m01():
    start = ASSERTIONS
    total_states = 0
    fixed_flags = 0
    max_depth = 0
    sharp = []
    fibre_profiles = []
    for dimension, lengths in ((2, (3, 4, 5)), (3, (3, 4))):
        spaces = subspaces(dimension)
        for length in lengths:
            local_max = 0
            fibres = Counter()
            for state in product(spaces, repeat=length):
                total_states += 1
                initial_meet = tuple_meet(state)
                initial_join = tuple_join(state)
                current = state
                depth = 0
                while bubble_sweep(current) != current:
                    current = bubble_sweep(current)
                    depth += 1
                    check(depth <= length - 1, "bubble clock exceeded r-1")
                is_chain = all(space_leq(current[i], current[i + 1])
                               for i in range(length - 1))
                check(is_chain, "terminal tuple is not a flag")
                check(tuple_meet(current) == initial_meet, "global meet changed")
                check(tuple_join(current) == initial_join, "global join changed")
                check((bubble_sweep(state) == state)
                      == all(space_leq(state[i], state[i + 1])
                             for i in range(length - 1)),
                      "fixed points are not exactly flags")
                local_max = max(local_max, depth)
                if depth == 0:
                    fixed_flags += 1
                fibres[current] += 1
            max_depth = max(max_depth, local_max)
            check(local_max == length - 1, "sharp bubble clock missing")
            check(len(fibres) == weak_flag_count(dimension, length, 2),
                  "terminal image is not the full weak-flag set")
            by_dimension_profile = defaultdict(list)
            for flag, fibre_size in fibres.items():
                profile = tuple(space_dim(space) for space in flag)
                by_dimension_profile[profile].append(fibre_size)
            for counts in by_dimension_profile.values():
                check(len(set(counts)) == 1,
                      "GL-equivariant fibre size changed inside one flag stratum")
            sharp.append(f"d{dimension}r{length}:{local_max}")
            fibre_profiles.append(
                f"d{dimension}r{length}:flags{len(fibres)}:"
                f"fibres{min(fibres.values())}-{max(fibres.values())}:"
                f"profiles{len(by_dimension_profile)}"
            )

    # The three atoms of M_3 separate this order-sensitive projection from
    # Gerlach's symmetric lattice sort.  Here M_3 is L(F_2^2).
    zero = span_mask([])
    top = span_mask([1, 2])
    line_1, line_2, line_3 = (span_mask([1]), span_mask([2]), span_mask([3]))
    witness = (line_1, line_2, line_3)
    terminal = bubble_sweep(bubble_sweep(witness))
    check(terminal == (zero, line_3, top), "M_3 order witness changed")
    permuted_terminal = bubble_sweep(bubble_sweep((line_3, line_2, line_1)))
    check(permuted_terminal == (zero, line_1, top), "M_3 permutation witness changed")
    symmetric_middle = (space_join(line_1, line_2)
                        & space_join(line_1, line_3)
                        & space_join(line_2, line_3))
    check(symmetric_middle == top and symmetric_middle != terminal[1],
          "M_3 witness no longer separates symmetric lattice sorting")
    record(
        "M01", "finite_modules", "F2 subspaces d=2,3; tuple length r=3..5",
        start, "universal depth<=r-1 is sharp; fixed states are weak flags",
        "KILL", "internal meet/join-comparator hard exclusion; GL-equivariant fibre strata are not a subspace-specific residual",
        states=total_states, fixed_flags=fixed_flags, max_depth=max_depth,
        sharp="/".join(sharp), fibre_profiles="/".join(fibre_profiles),
    )


def run_m02():
    start = ASSERTIONS
    spaces = subspaces(3)

    def step(state):
        a, b, c = state
        return (a & space_join(b, c),
                b & space_join(c, a),
                c & space_join(a, b))

    depths = {}
    for state in product(spaces, repeat=3):
        current = state
        depth = 0
        while True:
            image = step(current)
            check(all(space_leq(image[i], current[i]) for i in range(3)),
                  "cyclic meet-sum is not decreasing")
            if image == current:
                break
            check(sum(space_dim(x) for x in image)
                  < sum(space_dim(x) for x in current), "dimension did not fall")
            current = image
            depth += 1
        depths[depth] = depths.get(depth, 0) + 1
    record(
        "M02", "finite_modules", "all 16^3 triples of subspaces of F2^3",
        start, "monotone dimension descent, but only a small-depth closure profile",
        "KILL", "generic subspace closure; weak residual and P109 adjacency",
        states=len(spaces) ** 3, max_depth=max(depths),
        depth_hist="/".join(f"{k}:{depths[k]}" for k in sorted(depths)),
    )


def orthogonal(space, dimension):
    values = space_elements(space)
    good = []
    for vector in range(1 << dimension):
        if all((vector & value).bit_count() % 2 == 0 for value in values):
            good.append(vector)
    return span_mask(good)


def run_m03():
    start = ASSERTIONS
    spaces = subspaces(3)
    line = span_mask([1])
    stats = orbit_stats(spaces, lambda space: space_join(orthogonal(space, 3), line))
    record(
        "M03", "finite_modules", "all subspaces of F2^3; fixed line <e1>",
        start, "orthogonal-plus-line produces short eventual cycles",
        "KILL", "ortholattice/affine closure is mature and census is too small",
        **stats,
    )


def run_m04():
    start = ASSERTIONS
    total_states = 0
    max_depth = 0
    for dimension in range(2, 9):
        states = tuple(range(1 << dimension))
        for vector in states:
            current = vector
            depth = 0
            while current:
                current >>= 1
                depth += 1
            check(depth == vector.bit_length(), "nilpotent projective clock")
            max_depth = max(max_depth, depth)
        total_states += len(states)
    record(
        "M04", "finite_modules", "projective points plus sink for F2 Jordan blocks d=2..8",
        start, "kernel-filtration clock equals highest occupied Jordan coordinate",
        "KILL", "generic nilpotent linear filtration; direct P109 package collision",
        states=total_states, max_depth=max_depth,
    )


def run_m05():
    start = ASSERTIONS
    states = 0
    max_depth = 0
    for exponent in range(2, 13):
        for valuation in range(exponent + 1):
            current = valuation
            depth = 0
            while current:
                current = max(current - 1, 0)
                depth += 1
            check(depth == valuation, "p-saturation valuation clock")
            states += 1
            max_depth = max(max_depth, depth)
    record(
        "M05", "finite_modules", "ideals p^a in Z/p^e for 2<=e<=12",
        start, "exact valuation erosion a->max(a-1,0)",
        "KILL", "one-coordinate saturation is mechanical; P099/P115 firewall",
        states=states, max_depth=max_depth,
    )


# ---------------------------------------------------------------------------
# Finite rings


GF2_MODULI = {2: 0b111, 3: 0b1011, 4: 0b10011, 5: 0b100101}


def gf2_mul(left, right, modulus, degree):
    answer = 0
    a, b = left, right
    while b:
        if b & 1:
            answer ^= a
        b >>= 1
        a <<= 1
        if a >> degree & 1:
            a ^= modulus
    return answer & ((1 << degree) - 1)


def run_r01():
    start = ASSERTIONS
    aggregate = {"states": 0, "fixed": 0, "max_tail": 0, "max_period": 0}
    profiles = []
    for degree, modulus in GF2_MODULI.items():
        states = tuple(range(1 << degree))

        def step(value, mod=modulus, deg=degree):
            return gf2_mul(value, value, mod, deg) ^ value

        for x in states:
            for y in states:
                check(step(x ^ y) == (step(x) ^ step(y)), "Artin-Schreier additivity")
        stats = orbit_stats(states, step)
        for key in aggregate:
            aggregate[key] = (aggregate[key] + stats[key] if key in ("states", "fixed")
                              else max(aggregate[key], stats[key]))
        profiles.append(f"m{degree}:t{stats['max_tail']}p{stats['max_period']}")
    record(
        "R01", "finite_rings", "Artin-Schreier x->x^2+x on F_(2^m), 2<=m<=5",
        start, "linearized map has nontrivial tails but is completely linear-algebraic",
        "KILL", "additive-polynomial/Frobenius theory owns the mechanism",
        profiles="/".join(profiles), **aggregate,
    )


def run_r02():
    start = ASSERTIONS
    profiles = []
    total = 0
    max_tail = 0
    max_period = 0
    for prime in (3, 5, 7):
        states = tuple(product(range(prime), repeat=2))

        def step(value, p=prime):
            a, b = value
            return (a * a % p, 2 * a * b % p)

        stats = orbit_stats(states, step)
        total += stats["states"]
        max_tail = max(max_tail, stats["max_tail"])
        max_period = max(max_period, stats["max_period"])
        profiles.append(f"p{prime}:t{stats['max_tail']}p{stats['max_period']}")
    record(
        "R02", "finite_rings", "squaring on dual numbers F_p[e]/(e^2), p=3,5,7",
        start, "nilpotent coefficient follows the scalar power orbit",
        "KILL", "standard finite-ring power map; no extra fibre theorem signal",
        states=total, max_tail=max_tail, max_period=max_period,
        profiles="/".join(profiles),
    )


def divisors(number):
    return tuple(value for value in range(1, number + 1) if number % value == 0)


def run_r03():
    start = ASSERTIONS
    profiles = []
    total = 0
    max_tail = 0
    max_period = 0
    for modulus in (30, 36, 60, 84, 120):
        states = divisors(modulus)
        step = lambda value, n=modulus: gcd(n, value * value - value)
        stats = orbit_stats(states, step)
        total += stats["states"]
        max_tail = max(max_tail, stats["max_tail"])
        max_period = max(max_period, stats["max_period"])
        profiles.append(f"n{modulus}:t{stats['max_tail']}p{stats['max_period']}")
    record(
        "R03", "finite_rings", "d|n -> gcd(n,d^2-d), n=30,36,60,84,120",
        start, "CRT-prime support stabilizes almost immediately",
        "KILL", "coordinatewise divisor arithmetic is shallow",
        states=total, max_tail=max_tail, max_period=max_period,
        profiles="/".join(profiles),
    )


def run_r04():
    start = ASSERTIONS
    total = 0
    fixed = 0
    for modulus in (8, 12, 15, 16, 21, 25):
        for value in range(modulus):
            image = pow(value, -1, modulus) if gcd(value, modulus) == 1 else 0
            image2 = pow(image, -1, modulus) if gcd(image, modulus) == 1 else 0
            check(image2 == (value if gcd(value, modulus) == 1 else 0),
                  "inverse-or-zero involution")
            fixed += image == value
            total += 1
    record(
        "R04", "finite_rings", "inverse on units and zero otherwise in Z/n",
        start, "all components have tail<=1 and period<=2",
        "KILL", "unit inversion is an immediate involution",
        states=total, fixed=fixed, max_tail=1, max_period=2,
    )


# ---------------------------------------------------------------------------
# Finite semigroups


def transform_compose(left, right):
    return tuple(left[right[index]] for index in range(len(right)))


def run_s01():
    start = ASSERTIONS
    total = 0
    profiles = []
    max_tail = 0
    max_period = 0
    for size in (3, 4):
        states = tuple(product(range(size), repeat=size))
        cycle = tuple((index + 1) % size for index in range(size))

        def step(value, g=cycle):
            return transform_compose(value, transform_compose(g, value))

        for value in states:
            check(len(set(step(value))) <= len(set(value)), "sandwich rank increased")
        stats = orbit_stats(states, step)
        total += stats["states"]
        max_tail = max(max_tail, stats["max_tail"])
        max_period = max(max_period, stats["max_period"])
        profiles.append(f"n{size}:t{stats['max_tail']}p{stats['max_period']}")
    record(
        "S01", "finite_semigroups", "f->f o g o f in full T_n, g an n-cycle, n=3,4",
        start, "rank is Lyapunov but recurrent strata retain mixed periods",
        "KILL", "sandwich semigroup theory is broad; no clean second output",
        states=total, max_tail=max_tail, max_period=max_period,
        profiles="/".join(profiles),
    )


def relation_square(relation, size):
    answer = 0
    for i in range(size):
        for k in range(size):
            if any((relation >> (i * size + j) & 1)
                   and (relation >> (j * size + k) & 1)
                   for j in range(size)):
                answer |= 1 << (i * size + k)
    return answer


def run_s02():
    start = ASSERTIONS
    size = 4
    states = tuple(range(1 << (size * size)))

    def step(relation):
        return relation | relation_square(relation, size)

    for relation in states:
        check(relation & ~step(relation) == 0, "closure map is not increasing")
    stats = orbit_stats(states, step)
    record(
        "S02", "finite_semigroups", "R->R union R^2 on all binary relations on 4 points",
        start, "repeated squaring gives a two-round transitive-closure clock",
        "KILL", "standard Boolean transitive closure/repeated squaring",
        **stats,
    )


def relation_power(relation, exponent, size):
    if exponent == 1:
        return relation
    answer = relation
    for _ in range(exponent - 1):
        composed = 0
        for i in range(size):
            for k in range(size):
                if any((answer >> (i * size + j) & 1)
                       and (relation >> (j * size + k) & 1)
                       for j in range(size)):
                    composed |= 1 << (i * size + k)
        answer = composed
    return answer


def run_s03():
    start = ASSERTIONS
    size = 3
    states = tuple(range(1 << (size * size)))
    step = lambda relation: relation & relation_square(relation, size)
    for relation in states:
        check(step(relation) & ~relation == 0, "relation core is not decreasing")
    stats = orbit_stats(states, step)
    sharp = []
    for size in range(2, 10):
        strict = sum(1 << (i * size + j)
                     for i in range(size) for j in range(i + 1, size))
        current = strict
        time = 0
        while current:
            check(current == relation_power(strict, 1 << time, size),
                  "strict-order power identity")
            current = current & relation_square(current, size)
            time += 1
        sharp.append(f"n{size}:{time}")
    record(
        "S03", "finite_semigroups", "R->R intersect R^2; all 3-point relations and strict orders n<=9",
        start, "strict orders obey R_t=R^(2^t), exposing a logarithmic deletion clock",
        "KILL", "relation powers/transitive reduction are direct semigroup background",
        strict_depths="/".join(sharp), **stats,
    )


def rectangular_product(left, right):
    return (left[0], right[1])


def run_s04():
    start = ASSERTIONS
    band = tuple(product(range(2), repeat=2))
    states = tuple(product(band, repeat=3))

    def step(state):
        a, b, c = state
        return (rectangular_product(a, b),
                rectangular_product(b, c),
                rectangular_product(c, a))

    stats = orbit_stats(states, step)
    record(
        "S04", "finite_semigroups", "(a,b,c)->(ab,bc,ca) in the 2x2 rectangular band",
        start, "literal three-site action is purely periodic after one step",
        "KILL", "coordinate transport in a rectangular band is mechanical",
        **stats,
    )


def perm_compose(left, right):
    return tuple(left[right[index]] for index in range(len(right)))


def run_s05():
    start = ASSERTIONS
    group = tuple(permutations(range(3)))
    states = tuple(product(group, repeat=2))

    def step(state):
        x, y = state
        return perm_compose(x, y), perm_compose(y, x)

    stats = orbit_stats(states, step)
    for x, y in states:
        a, b = step((x, y))
        cycle_type_a = sorted(_perm_cycle_lengths(a))
        cycle_type_b = sorted(_perm_cycle_lengths(b))
        check(cycle_type_a == cycle_type_b, "xy and yx are not conjugate")
    record(
        "S05", "finite_semigroups", "(x,y)->(xy,yx) on S3 x S3",
        start, "conjugate-coordinate constraint coexists with several cycle lengths",
        "KILL", "Nielsen/Hurwitz-style group actions create high owner risk without a closed census",
        **stats,
    )


def _perm_cycle_lengths(value):
    seen = set()
    lengths = []
    for start in range(len(value)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            current = value[current]
            length += 1
        lengths.append(length)
    return lengths


# ---------------------------------------------------------------------------
# Matrix actions


def mat_add(left, right, prime):
    return tuple((a + b) % prime for a, b in zip(left, right))


def mat_sub(left, right, prime):
    return tuple((a - b) % prime for a, b in zip(left, right))


def mat_mul(left, right, size, prime):
    return tuple(sum(left[i * size + k] * right[k * size + j]
                     for k in range(size)) % prime
                 for i in range(size) for j in range(size))


def mat_transpose(value, size):
    return tuple(value[j * size + i] for i in range(size) for j in range(size))


def mat_rank(value, size, prime):
    rows = [list(value[i * size:(i + 1) * size]) for i in range(size)]
    rank = 0
    for column in range(size):
        pivot = next((row for row in range(rank, size) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [entry * inverse % prime for entry in rows[rank]]
        for row in range(size):
            if row != rank and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [(rows[row][j] - factor * rows[rank][j]) % prime
                             for j in range(size)]
        rank += 1
    return rank


def run_x01():
    start = ASSERTIONS
    total = 0
    profiles = []
    max_tail = 0
    max_period = 0
    for size in (2, 3):
        states = tuple(product(range(2), repeat=size * size))

        def step(value, n=size):
            return mat_add(mat_transpose(value, n), mat_mul(value, value, n, 2), 2)

        stats = orbit_stats(states, step)
        total += stats["states"]
        max_tail = max(max_tail, stats["max_tail"])
        max_period = max(max_period, stats["max_period"])
        profiles.append(f"n{size}:t{stats['max_tail']}p{stats['max_period']}")
    record(
        "X01", "matrix_actions", "A->A^T+A^2 over F2, sizes 2 and 3",
        start, "small matrices show mixed cycles but no monotone invariant",
        "KILL", "quadratic matrix iteration is too close to P125 and lacks a proof spine",
        states=total, max_tail=max_tail, max_period=max_period,
        profiles="/".join(profiles),
    )


def run_x02():
    start = ASSERTIONS
    size = 2
    prime = 3
    states = tuple(product(range(prime), repeat=4))
    jordan = (0, 1, 0, 0)

    def step(value):
        commutator = mat_sub(mat_mul(value, jordan, size, prime),
                             mat_mul(jordan, value, size, prime), prime)
        return mat_mul(commutator, commutator, size, prime)

    stats = orbit_stats(states, step)
    record(
        "X02", "matrix_actions", "A->[A,J]^2 in M2(F3), J nilpotent",
        start, "commutator image collapses rapidly to a small recurrent set",
        "KILL", "commutator-polynomial mechanism overlaps P119/P125 controls",
        **stats,
    )


def run_x03():
    start = ASSERTIONS
    states = tuple(product(range(2), repeat=4))
    symplectic = (0, 1, 1, 0)

    def step(value):
        return mat_mul(mat_mul(mat_transpose(value, 2), symplectic, 2, 2), value, 2, 2)

    stats = orbit_stats(states, step)
    for value in states:
        determinant = (value[0] * value[3] - value[1] * value[2]) % 2
        check(step(value) == tuple(determinant * entry for entry in symplectic),
              "2x2 symplectic Gram identity")
    record(
        "X03", "matrix_actions", "A->A^T J A in M2(F2)",
        start, "the entire map is the determinant bit times J",
        "KILL", "one-step determinant collapse is too small and close to quadratic congruence",
        **stats,
    )


def run_x04():
    start = ASSERTIONS
    prime = 3
    states = tuple(product(range(prime), repeat=4))
    identity = (1, 0, 0, 1)

    def adjugate(value):
        a, b, c, d = value
        return d % prime, -b % prime, -c % prime, a % prime

    stats = orbit_stats(states, lambda value: mat_add(adjugate(value), identity, prime))
    record(
        "X04", "matrix_actions", "A->adj(A)+I in M2(F3)",
        start, "affine adjugation has short explicit components",
        "KILL", "direct near-variant of P103 double-adjugate dynamics",
        **stats,
    )


def schur_delete(value, size, prime):
    pivot = next(((i, j) for i in range(size) for j in range(size)
                  if value[i * size + j] % prime), None)
    if pivot is None:
        return size, value
    row, column = pivot
    inverse = pow(value[row * size + column], -1, prime)
    rows = [i for i in range(size) if i != row]
    columns = [j for j in range(size) if j != column]
    answer = []
    for i in rows:
        for j in columns:
            entry = value[i * size + j]
            entry -= value[i * size + column] * inverse * value[row * size + j]
            answer.append(entry % prime)
    return size - 1, tuple(answer)


def run_x05():
    start = ASSERTIONS
    states = tuple(product(range(2), repeat=9))
    max_depth = 0
    rank_hist = {}
    for value in states:
        size = 3
        current = value
        original_rank = mat_rank(value, size, 2)
        rank_hist[original_rank] = rank_hist.get(original_rank, 0) + 1
        depth = 0
        while any(current):
            next_size, image = schur_delete(current, size, 2)
            check(mat_rank(image, next_size, 2) == mat_rank(current, size, 2) - 1,
                  "Schur pivot did not lower rank exactly")
            size, current = next_size, image
            depth += 1
        check(depth == original_rank, "pivot depth is not rank")
        max_depth = max(max_depth, depth)
    record(
        "X05", "matrix_actions", "lexicographic Schur-pivot deletion on all 3x3 F2 matrices",
        start, "termination time is exactly matrix rank",
        "KILL", "Gaussian elimination translation; theorem and fibres are classical/mechanical",
        states=len(states), max_depth=max_depth,
        rank_hist="/".join(f"{k}:{rank_hist[k]}" for k in sorted(rank_hist)),
    )


# ---------------------------------------------------------------------------
# Polynomial transforms over finite prime fields


def poly_trim(value):
    value = list(value)
    while value and value[-1] == 0:
        value.pop()
    return tuple(value)


def poly_add(left, right, prime):
    size = max(len(left), len(right))
    return poly_trim(tuple(((left[i] if i < len(left) else 0)
                            + (right[i] if i < len(right) else 0)) % prime
                           for i in range(size)))


def poly_scale(value, scalar, prime):
    return poly_trim(tuple(scalar * coefficient % prime for coefficient in value))


def poly_mul(left, right, prime):
    if not left or not right:
        return ()
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % prime
    return poly_trim(tuple(answer))


def poly_divmod(dividend, divisor, prime):
    if not divisor:
        raise ZeroDivisionError
    remainder = list(dividend)
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, prime)
    while len(poly_trim(remainder)) >= len(divisor):
        remainder = list(poly_trim(remainder))
        degree = len(remainder) - len(divisor)
        factor = remainder[-1] * inverse % prime
        quotient[degree] = factor
        for index, coefficient in enumerate(divisor):
            remainder[degree + index] = (remainder[degree + index]
                                         - factor * coefficient) % prime
    return poly_trim(tuple(quotient)), poly_trim(tuple(remainder))


def poly_monic(value, prime):
    value = poly_trim(value)
    if not value:
        return ()
    return poly_scale(value, pow(value[-1], -1, prime), prime)


def poly_gcd(left, right, prime):
    a, b = poly_trim(left), poly_trim(right)
    while b:
        _, remainder = poly_divmod(a, b, prime)
        a, b = b, remainder
    return poly_monic(a, prime)


def poly_shift(value, amount, prime):
    answer = ()
    linear = (amount % prime, 1)
    for coefficient in reversed(value):
        answer = poly_add(poly_mul(answer, linear, prime), (coefficient,), prime)
    return answer


def poly_compose(outer, inner, prime):
    answer = ()
    for coefficient in reversed(outer):
        answer = poly_add(poly_mul(answer, inner, prime), (coefficient,), prime)
    return answer


def monic_polynomials(prime, max_degree):
    values = []
    for degree in range(max_degree + 1):
        for lower in product(range(prime), repeat=degree):
            values.append(tuple(lower) + (1,))
    return tuple(values)


def moebius(number):
    answer = 1
    residual = number
    prime = 2
    while prime * prime <= residual:
        if residual % prime == 0:
            residual //= prime
            answer = -answer
            if residual % prime == 0:
                return 0
            while residual % prime == 0:
                residual //= prime
        prime += 1
    if residual > 1:
        answer = -answer
    return answer


@lru_cache(maxsize=None)
def monic_irreducible_count(prime_power, degree):
    return sum(moebius(divisor) * prime_power ** (degree // divisor)
               for divisor in divisors(degree)) // degree


@lru_cache(maxsize=None)
def fixed_translation_irreducible_count(prime_power, characteristic, degree):
    """Irreducibles fixed by x -> x+1 over F_q, via Artin--Schreier trace."""
    if degree % characteristic:
        return 0
    base_degree = degree // characteristic
    prime_part = 1
    coprime_part = base_degree
    while coprime_part % characteristic == 0:
        prime_part *= characteristic
        coprime_part //= characteristic
    numerator = (characteristic - 1) * sum(
        moebius(coprime_part // divisor)
        * prime_power ** (prime_part * divisor)
        for divisor in divisors(coprime_part)
    )
    check(numerator % characteristic == 0,
          "Artin--Schreier nonzero-trace count lost integrality")
    trace_nonzero = numerator // characteristic
    check(trace_nonzero % base_degree == 0,
          "fixed irreducible count lost orbit integrality")
    return trace_nonzero // base_degree


@lru_cache(maxsize=None)
def nonfixed_translation_orbit_count(prime_power, characteristic, degree):
    residual = (monic_irreducible_count(prime_power, degree)
                - fixed_translation_irreducible_count(
                    prime_power, characteristic, degree))
    check(residual % characteristic == 0,
          "nonfixed irreducibles do not split into p-orbits")
    return residual // characteristic


def maximum_cyclic_one_run(mask, length):
    if mask == (1 << length) - 1:
        return length
    answer = 0
    for start in range(length):
        local = 0
        for offset in range(length):
            if mask >> ((start + offset) % length) & 1:
                local += 1
                answer = max(answer, local)
            else:
                break
    return answer


@lru_cache(maxsize=None)
def local_depth_kernel_series(characteristic, time, max_weight):
    """Exponent vectors on one p-orbit, minimum zero and depth <= time."""
    supports = Counter()
    for mask in range(1 << characteristic):
        if maximum_cyclic_one_run(mask, characteristic) <= time:
            supports[mask.bit_count()] += 1
    coefficients = [0] * (max_weight + 1)
    coefficients[0] = supports[0]
    for weight in range(1, max_weight + 1):
        coefficients[weight] = sum(
            count * comb(weight - 1, support_size - 1)
            for support_size, count in supports.items() if support_size
        )
    return tuple(coefficients)


def series_multiply(left, right, max_degree):
    answer = [0] * (max_degree + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= max_degree:
                answer[i + j] += a * b
    return tuple(answer)


def series_power(value, exponent, max_degree):
    answer = (1,) + (0,) * max_degree
    base = value
    while exponent:
        if exponent & 1:
            answer = series_multiply(answer, base, max_degree)
        base = series_multiply(base, base, max_degree)
        exponent >>= 1
    return answer


def translation_depth_cdf_series(prime_power, characteristic, max_degree, time):
    """Exact-degree OGF coefficients for translation-GCD depth <= time."""
    kernel = (1,) + (0,) * max_degree
    for factor_degree in range(1, max_degree + 1):
        orbit_count = nonfixed_translation_orbit_count(
            prime_power, characteristic, factor_degree)
        local = local_depth_kernel_series(
            characteristic, time, max_degree // factor_degree)
        substituted = [0] * (max_degree + 1)
        for index, coefficient in enumerate(local):
            substituted[index * factor_degree] = coefficient
        kernel = series_multiply(
            kernel,
            series_power(tuple(substituted), orbit_count, max_degree),
            max_degree,
        )
    invariant = tuple(
        prime_power ** (degree // characteristic)
        if degree % characteristic == 0 else 0
        for degree in range(max_degree + 1)
    )
    return series_multiply(invariant, kernel, max_degree)


def run_p01():
    start = ASSERTIONS
    profiles = []
    total_states = 0
    max_depth = 0
    final_images = 0
    fibre_profiles = []
    cdf_profiles = []
    for prime, max_degree in ((2, 7), (3, 6), (5, 5)):
        states = monic_polynomials(prime, max_degree)
        state_set = set(states)

        def step(value, p=prime):
            return poly_gcd(value, poly_shift(value, 1, p), p)

        hist = {}
        depth_by_degree = defaultdict(Counter)
        fibres = Counter()
        for value in states:
            current = value
            window = value
            depth = None
            for time in range(prime):
                check(current == window, "translation-GCD window identity")
                image = step(current)
                if depth is None and image == current:
                    depth = time
                window = poly_gcd(window, poly_shift(value, time + 1, prime), prime)
                current = image
            check(depth is not None, "translation-GCD failed to stabilize")
            check(depth <= prime - 1, "translation-GCD exceeded p-1")
            check(poly_shift(current, 1, prime) == current,
                  "terminal polynomial is not translation invariant")
            check(current in state_set, "translation-GCD degree escaped")
            hist[depth] = hist.get(depth, 0) + 1
            depth_by_degree[len(value) - 1][depth] += 1
            fibres[current] += 1

        artin_schreier = tuple([0, -1 % prime] + [0] * (prime - 2) + [1])
        expected_image = {
            poly_compose(outer, artin_schreier, prime)
            for outer in monic_polynomials(prime, max_degree // prime)
        }
        check(set(fibres) == expected_image,
              "terminal image differs from F_p[x^p-x] in the degree box")

        def kernel_exact(degree):
            if degree < prime:
                return prime ** degree
            return prime ** degree - prime ** (degree - prime + 1)

        def kernel_bounded(degree_bound):
            return sum(kernel_exact(degree) for degree in range(degree_bound + 1))

        for target, fibre_size in fibres.items():
            residual_bound = max_degree - (len(target) - 1)
            check(fibre_size == kernel_bounded(residual_bound),
                  "terminal fibre violates the kernel-product formula")

        terminal_degree_cdf = []
        for time in range(prime):
            formula = translation_depth_cdf_series(
                prime, prime, max_degree, time)
            for degree in range(max_degree + 1):
                enumerated = sum(
                    count for local_depth, count
                    in depth_by_degree[degree].items() if local_depth <= time
                )
                check(enumerated == formula[degree],
                      "all-depth translation Euler product mismatch")
            terminal_degree_cdf.append(f"t{time}:{formula[max_degree]}")
        check(max(hist) == prime - 1, "sharp translation clock missing")
        total_states += len(states)
        final_images += len(fibres)
        max_depth = max(max_depth, max(hist))
        profiles.append(f"p{prime}d{max_degree}:states{len(states)}:final{len(fibres)}:depth{max(hist)}")
        fibre_profiles.append(
            f"p{prime}d{max_degree}:kernel{fibres[(1,)]}:"
            f"range{min(fibres.values())}-{max(fibres.values())}"
        )
        cdf_profiles.append(
            f"p{prime}d{max_degree}:" + ".".join(terminal_degree_cdf)
        )
    record(
        "P01", "polynomial_transforms", "monic F_p[x], (p,D)=(2,7),(3,6),(5,5)",
        start, "T^t(f)=gcd(f(x),...,f(x+t)); sharp p-1 clock to F_p[x^p-x]",
        "CONDITIONAL_REENTRY", "old reserve gains an all-depth Euler product and exact terminal quotient/kernel/fibres",
        states=total_states, final_images=final_images, max_depth=max_depth,
        profiles="/".join(profiles), fibre_profiles="/".join(fibre_profiles),
        cdf_profiles="/".join(cdf_profiles),
    )


def run_p02():
    start = ASSERTIONS
    prime = 5
    multiplier = 2
    order = 4
    states = monic_polynomials(prime, 5)

    def dilate(value, scalar):
        return poly_monic(tuple(coefficient * pow(scalar, index, prime) % prime
                                for index, coefficient in enumerate(value)), prime)

    def step(value):
        return poly_gcd(value, dilate(value, multiplier), prime)

    max_depth = 0
    finals = set()
    for value in states:
        current = value
        window = value
        depth = 0
        for time in range(order):
            check(current == window, "dilation-GCD window identity")
            image = step(current)
            if image == current:
                break
            window = poly_gcd(window, dilate(value, pow(multiplier, time + 1, prime)), prime)
            current = image
            depth += 1
        check(depth <= order - 1, "dilation clock exceeded group order")
        check(dilate(current, multiplier) == current, "terminal dilation invariance")
        max_depth = max(max_depth, depth)
        finals.add(current)
    record(
        "P02", "polynomial_transforms", "monic F5[x], degree<=5; dilation x->2x",
        start, "same sliding-minimum theorem with multiplicative orbit length four",
        "KILL", "useful control but not independent of P01 cyclic-automorphism erosion",
        states=len(states), final_images=len(finals), max_depth=max_depth,
    )


def poly_derivative(value, prime):
    return poly_trim(tuple(index * value[index] % prime
                           for index in range(1, len(value))))


def run_p03():
    start = ASSERTIONS
    profiles = []
    total = 0
    max_tail = 0
    for prime, degree in ((2, 8), (3, 6), (5, 5)):
        states = monic_polynomials(prime, degree)

        def step(value, p=prime):
            derivative = poly_derivative(value, p)
            return value if not derivative else poly_gcd(value, derivative, p)

        stats = orbit_stats(states, step)
        check(stats["max_period"] == 1, "derivative gcd should terminate")
        total += stats["states"]
        max_tail = max(max_tail, stats["max_tail"])
        profiles.append(f"p{prime}:t{stats['max_tail']}")
    record(
        "P03", "polynomial_transforms", "f->gcd(f,f') on monic F_p[x] in three boxes",
        start, "multiplicity descent with inseparable fixed points",
        "KILL", "squarefree/inseparable factor extraction is directly classical",
        states=total, max_tail=max_tail, profiles="/".join(profiles),
    )


def run_p04():
    start = ASSERTIONS
    profiles = []
    total = 0
    max_depth = 0
    for prime, degree in ((2, 8), (3, 6), (5, 5)):
        states = ((),) + monic_polynomials(prime, degree)

        def step(value, p=prime):
            if not value:
                return ()
            difference = poly_add(poly_shift(value, 1, p), poly_scale(value, -1, p), p)
            return poly_monic(difference, p)

        stats = orbit_stats(states, step)
        check(stats["fixed"] == 1 and stats["max_period"] == 1,
              "finite difference should end at zero")
        total += stats["states"]
        max_depth = max(max_depth, stats["max_tail"])
        profiles.append(f"p{prime}:t{stats['max_tail']}")
    record(
        "P04", "polynomial_transforms", "monic-normalized Delta f=f(x+1)-f(x), plus zero",
        start, "all orbits terminate, with characteristic-p degree plateaux",
        "KILL", "finite-difference calculus owns the descent; no fibre signal",
        states=total, max_depth=max_depth, profiles="/".join(profiles),
    )


def run_p05():
    start = ASSERTIONS
    profiles = []
    total = 0
    max_tail = 0
    for prime, degree in ((2, 8), (3, 6), (5, 5)):
        states = monic_polynomials(prime, degree)

        def step(value, p=prime):
            reciprocal = poly_monic(tuple(reversed(value)), p)
            return poly_gcd(value, reciprocal, p)

        stats = orbit_stats(states, step)
        total += stats["states"]
        max_tail = max(max_tail, stats["max_tail"])
        profiles.append(f"p{prime}:t{stats['max_tail']}")
    record(
        "P05", "polynomial_transforms", "f->gcd(f,x^deg(f)f(1/x)) on monic polynomials",
        start, "reciprocal-core extraction is idempotent or one-step",
        "KILL", "self-reciprocal factor extraction is mature and dynamically shallow",
        states=total, max_tail=max_tail, profiles="/".join(profiles),
    )


# ---------------------------------------------------------------------------
# Monomial-ideal transforms in a finite exponent box


def point_index(a, b, bound):
    return a * (bound + 1) + b


def box_upward_closure(mask, bound):
    answer = mask
    for a in range(bound + 1):
        for b in range(bound + 1):
            if mask >> point_index(a, b, bound) & 1:
                for c in range(a, bound + 1):
                    for d in range(b, bound + 1):
                        answer |= 1 << point_index(c, d, bound)
    return answer


@lru_cache(maxsize=None)
def monomial_upsets(bound):
    size = (bound + 1) ** 2
    return tuple(mask for mask in range(1 << size)
                 if box_upward_closure(mask, bound) == mask)


def run_i01():
    start = ASSERTIONS
    bound = 3
    states = monomial_upsets(bound)

    def step(mask):
        moved = mask
        for a in range(bound + 1):
            for b in range(1, bound + 1):
                if mask >> point_index(a, b, bound) & 1 and a < bound:
                    moved |= 1 << point_index(a + 1, b - 1, bound)
        return box_upward_closure(moved, bound)

    for state in states:
        check(state & ~step(state) == 0, "Borel closure is not increasing")
    stats = orbit_stats(states, step)
    record(
        "I01", "ideal_transforms", "Borel lowering closure on all monomial upsets in [0,3]^2",
        start, "finite strongly-stable closure has a visible displacement clock",
        "KILL", "Borel closure is standard and monomial-dynamics space is crowded by P124",
        **stats,
    )


def run_i02():
    start = ASSERTIONS
    bound = 3
    states = monomial_upsets(bound)

    def step(mask):
        answer = 0
        for a in range(bound + 1):
            for b in range(bound + 1):
                reflected = point_index(bound - a, bound - b, bound)
                if not (mask >> reflected & 1):
                    answer |= 1 << point_index(a, b, bound)
        return answer

    stats = orbit_stats(states, step)
    for state in states:
        check(step(step(state)) == state, "boxed Alexander dual is not involutive")
    record(
        "I02", "ideal_transforms", "boxed Alexander dual on all monomial upsets in [0,3]^2",
        start, "exact involution with fixed self-dual ideals",
        "KILL", "Alexander duality is directly owned; dynamics is only period two",
        **stats,
    )


def run_i03():
    start = ASSERTIONS
    bound = 3
    states = monomial_upsets(bound)

    def step(mask):
        points = [(a, b) for a in range(bound + 1) for b in range(bound + 1)
                  if mask >> point_index(a, b, bound) & 1]
        answer = 0
        for a, b in points:
            for c, d in points:
                if a + c <= bound and b + d <= bound:
                    answer |= 1 << point_index(a + c, b + d, bound)
        return box_upward_closure(answer, bound)

    for state in states:
        check(step(state) & ~state == 0, "ideal square is not contained in ideal")
    stats = orbit_stats(states, step)
    record(
        "I03", "ideal_transforms", "truncated Minkowski/ideal square on upsets in [0,3]^2",
        start, "powers double exponent thresholds until the box empties",
        "KILL", "direct ideal-power mechanism and P107 collision",
        **stats,
    )


def main():
    runners = (
        run_m01, run_m02, run_m03, run_m04, run_m05,
        run_r01, run_r02, run_r03, run_r04,
        run_s01, run_s02, run_s03, run_s04, run_s05,
        run_x01, run_x02, run_x03, run_x04, run_x05,
        run_p01, run_p02, run_p03, run_p04, run_p05,
        run_i01, run_i02, run_i03,
    )
    for runner in runners:
        runner()
    if sum(result["assertions"] for result in RESULTS) != ASSERTIONS:
        raise AssertionError("per-system assertion accounting mismatch")
    print("algebraic linear breadth scout: PASS")
    print(f"systems={len(RESULTS)} advanced={sum(r['decision'] in ('ADVANCE', 'CONDITIONAL_REENTRY') for r in RESULTS)}")
    for result in RESULTS:
        metric_text = ",".join(f"{key}={value}" for key, value in result["metrics"].items())
        print(
            f"{result['id']} family={result['family']} scope={result['scope']} "
            f"assertions={result['assertions']} metrics={metric_text} "
            f"signal={result['signal']} decision={result['decision']} reason={result['reason']}"
        )
    print(f"TOTAL_ASSERTIONS={ASSERTIONS}")
    print("scope_sentinel=finite enumeration is falsification evidence, never proof or ownership")
    print("novelty_sentinel=bounded owner non-hit is not novelty or priority")


if __name__ == "__main__":
    main()
