#!/usr/bin/env python3
"""Deterministic standard-library pilots for the P122--P126 algebraic intake.

This is a falsification program, not a proof or novelty certificate.  It
tests twelve literal finite maps selected from a larger paper-free candidate
pool.  All arithmetic is exact and every loop is deterministic.
"""

from collections import Counter, deque
from itertools import product


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def orbit_data(start, step):
    seen = {}
    state = start
    while state not in seen:
        seen[state] = len(seen)
        state = step(state)
    return seen[state], len(seen) - seen[state]


# ---------------------------------------------------------------------------
# C1--C2: transpose self-commutator and anticommutator on M_2(F_q)


def mat2_mul(a, b, q):
    return (
        (a[0] * b[0] + a[1] * b[2]) % q,
        (a[0] * b[1] + a[1] * b[3]) % q,
        (a[2] * b[0] + a[3] * b[2]) % q,
        (a[2] * b[1] + a[3] * b[3]) % q,
    )


def mat2_transpose(a):
    return (a[0], a[2], a[1], a[3])


def mat2_add(a, b, q, sign=1):
    return tuple((x + sign * y) % q for x, y in zip(a, b))


def transpose_commutator(a, q):
    at = mat2_transpose(a)
    return mat2_add(mat2_mul(a, at, q), mat2_mul(at, a, q), q, -1)


def transpose_anticommutator(a, q):
    at = mat2_transpose(a)
    return mat2_add(mat2_mul(a, at, q), mat2_mul(at, a, q), q, 1)


def pilot_transpose_defects():
    lines = []
    zero = (0, 0, 0, 0)
    for q in (2, 3, 5, 7):
        states = tuple(product(range(q), repeat=4))
        fibres = Counter()
        for a in states:
            b = transpose_commutator(a, q)
            fibres[b] += 1
            check(b == mat2_transpose(b), f"C1 image not symmetric q={q}: {a}")
            check((b[0] + b[3]) % q == 0, f"C1 image trace nonzero q={q}: {a}")
            check(transpose_commutator(b, q) == zero, f"C1 square nonzero q={q}: {a}")

        if q % 2:
            check(len(fibres) == q * q, f"C1 odd image size q={q}")
            check(fibres[zero] == q**3 + q**2 - q, f"C1 odd zero fibre q={q}")
            check(
                Counter(size for target, size in fibres.items() if target != zero)
                == Counter({q * (q - 1): q * q - 1}),
                f"C1 odd nonzero fibres q={q}",
            )
        else:
            check(len(fibres) == q * q - q + 1, f"C1 even image size q={q}")
            check(fibres[zero] == q**3, f"C1 even zero fibre q={q}")
            check(
                Counter(size for target, size in fibres.items() if target != zero)
                == Counter({q * q: q * q - q}),
                f"C1 even nonzero fibres q={q}",
            )

        depth_counts = (1, len(fibres) - 1, q**4 - len(fibres))
        check(sum(depth_counts) == q**4, f"C1 depth partition q={q}")
        lines.append(
            f"C1 q={q} image={len(fibres)} zero_fibre={fibres[zero]} "
            f"depths={depth_counts}"
        )

    # In characteristic two C2 is literally C1; in odd characteristic the
    # first symmetric image follows the power recurrence B -> 2 B^2.
    for q in (2, 3, 5):
        states = tuple(product(range(q), repeat=4))
        nonzero_second = 0
        for a in states:
            plus = transpose_anticommutator(a, q)
            if q == 2:
                check(plus == transpose_commutator(a, q), f"C2 char-two collision: {a}")
            else:
                check(plus == mat2_transpose(plus), f"C2 image not symmetric q={q}: {a}")
                second = transpose_anticommutator(plus, q)
                twice_square = tuple((2 * x) % q for x in mat2_mul(plus, plus, q))
                check(second == twice_square, f"C2 symmetric recurrence q={q}: {a}")
                nonzero_second += second != (0, 0, 0, 0)
        lines.append(f"C2 q={q} nonzero_second_iterates={nonzero_second}")
    return lines


# ---------------------------------------------------------------------------
# C3--C5: nonlinear maps on the subspace lattice of F_2^d


def subspaces_f2(d):
    spaces = {1}  # bit 0 represents the zero vector
    queue = deque([1])
    vectors = range(1 << d)
    while queue:
        space = queue.popleft()
        members = [x for x in vectors if (space >> x) & 1]
        for x in vectors:
            if (space >> x) & 1:
                continue
            extended = space
            for u in members:
                extended |= 1 << (u ^ x)
            if extended not in spaces:
                spaces.add(extended)
                queue.append(extended)
    return tuple(sorted(spaces))


def subspace_join(a, b):
    left = [x for x in range(a.bit_length()) if (a >> x) & 1]
    right = [x for x in range(b.bit_length()) if (b >> x) & 1]
    answer = 0
    for x in left:
        for y in right:
            answer |= 1 << (x ^ y)
    return answer


def nilpotent_image(space, d, transpose=False):
    answer = 1
    mask = (1 << d) - 1
    for x in range(1 << d):
        if not ((space >> x) & 1):
            continue
        if transpose:
            image = x >> 1
        else:
            image = (x << 1) & mask
        answer |= 1 << image
    return answer


def nilpotent_preimage(space, d):
    answer = 0
    mask = (1 << d) - 1
    for x in range(1 << d):
        image = (x << 1) & mask
        if (space >> image) & 1:
            answer |= 1 << x
    return answer


def pilot_subspace_maps():
    lines = []
    for d in range(1, 6):
        spaces = subspaces_f2(d)
        joins = {(u, v): subspace_join(u, v) for u in spaces for v in spaces}
        n_images = {u: nilpotent_image(u, d) for u in spaces}

        def step(state):
            u, v = state
            return v, joins[u, n_images[v]]

        depth_hist = Counter()
        cycle_hist = Counter()
        maximum_depth = 0
        for u in spaces:
            for v in spaces:
                # Closed semiring-Fibonacci expression versus literal recurrence.
                sequence = [u, v]
                for _ in range(2 * d + 4):
                    sequence.append(joins[sequence[-2], n_images[sequence[-1]]])
                for t, literal in enumerate(sequence):
                    if t == 0:
                        closed = u
                    elif t == 1:
                        closed = v
                    elif t % 2 == 0:
                        r = t // 2
                        closed = 1
                        term = u
                        for _j in range(r):
                            closed = joins[closed, term]
                            term = n_images[n_images[term]]
                        term = n_images[v]
                        for _j in range(r):
                            closed = joins[closed, term]
                            term = n_images[n_images[term]]
                    else:
                        r = (t - 1) // 2
                        closed = 1
                        term = n_images[u]
                        for _j in range(r):
                            closed = joins[closed, term]
                            term = n_images[n_images[term]]
                        term = v
                        for _j in range(r + 1):
                            closed = joins[closed, term]
                            term = n_images[n_images[term]]
                    check(literal == closed, f"C3 closed iterate d={d}, t={t}, {(u, v)}")

                depth, cycle = orbit_data((u, v), step)
                check(cycle in (1, 2), f"C3 long cycle d={d}: {(u, v)}")
                check(depth <= d, f"C3 depth exceeds d={d}: {(u, v)}")
                depth_hist[depth] += 1
                cycle_hist[cycle] += 1
                maximum_depth = max(maximum_depth, depth)
        check(maximum_depth == (0 if d == 1 else d), f"C3 sharp depth d={d}")
        lines.append(
            f"C3 d={d} subspaces={len(spaces)} max_depth={maximum_depth} "
            f"depth_hist={dict(sorted(depth_hist.items()))} "
            f"eventual_cycle_hist={dict(sorted(cycle_hist.items()))}"
        )

    # C4 is the meet/preimage dual control; it must have the same depth/cycle
    # ceiling as C3, so it is killed as a within-batch dual rather than promoted.
    for d in range(1, 5):
        spaces = subspaces_f2(d)
        preimages = {v: nilpotent_preimage(v, d) for v in spaces}

        def dual_step(state):
            u, v = state
            return v, u & preimages[v]

        maximum_depth = 0
        cycle_lengths = set()
        for u in spaces:
            for v in spaces:
                depth, cycle = orbit_data((u, v), dual_step)
                maximum_depth = max(maximum_depth, depth)
                cycle_lengths.add(cycle)
                check(cycle in (1, 2), f"C4 long cycle d={d}: {(u, v)}")
                check(depth <= d, f"C4 depth exceeds d={d}: {(u, v)}")
        check(maximum_depth == (0 if d == 1 else d), f"C4 sharp depth d={d}")
        lines.append(f"C4 d={d} max_depth={maximum_depth} cycles={sorted(cycle_lengths)}")

    # C5 compares a single bubble pass C12 C23 with the full three-input
    # sorting word C12 C23 C12 on the nondistributive subspace lattice.
    for d in range(1, 5):
        spaces = subspaces_f2(d)
        joins = {(u, v): subspace_join(u, v) for u in spaces for v in spaces}

        def bubble(state):
            u, v, w = state
            low = u & v
            high = joins[u, v]
            return low, high & w, joins[high, w]

        def sort3(state):
            u, v, w = state
            u, v = u & v, joins[u, v]
            v, w = v & w, joins[v, w]
            u, v = u & v, joins[u, v]
            return u, v, w

        bubble_depth = Counter()
        fixed_sort = 0
        for state in product(spaces, repeat=3):
            b1 = bubble(state)
            b2 = bubble(b1)
            b3 = bubble(b2)
            check(b3 == b2, f"C5 bubble not settled by two d={d}: {state}")
            s1 = sort3(state)
            check(sort3(s1) == s1, f"C5 sort word not idempotent d={d}: {state}")
            depth = 0 if b1 == state else 1 if b2 == b1 else 2
            bubble_depth[depth] += 1
            fixed_sort += s1 == state
        lines.append(
            f"C5 d={d} triples={len(spaces)**3} bubble_depth={dict(sorted(bubble_depth.items()))} "
            f"sort_fixed={fixed_sort}"
        )
    return lines


# ---------------------------------------------------------------------------
# C6--C7: cross-colon maps on rectangular monomial-ideal lattices


def rectangular_monomial_ideals(a, b):
    ideals = []

    def visit(row, previous, thresholds):
        if row == a:
            mask = 0
            for i, lower in enumerate(thresholds):
                for j in range(lower, b):
                    mask |= 1 << (i * b + j)
            ideals.append(mask)
            return
        for lower in range(previous + 1):
            visit(row + 1, lower, thresholds + (lower,))

    visit(0, b, ())
    return tuple(ideals)


def monomial_multiply(ideal, a, b, di, dj):
    answer = 0
    for i in range(a):
        for j in range(b):
            if (ideal >> (i * b + j)) & 1 and i + di < a and j + dj < b:
                answer |= 1 << ((i + di) * b + j + dj)
    return answer


def monomial_colon(ideal, a, b, di, dj):
    answer = 0
    for i in range(a):
        for j in range(b):
            ni, nj = i + di, j + dj
            if ni >= a or nj >= b or (ideal >> (ni * b + nj)) & 1:
                answer |= 1 << (i * b + j)
    return answer


def pilot_monomial_ideals():
    lines = []
    for a in range(2, 9):
        for b in range(2, 9):
            ideals = rectangular_monomial_ideals(a, b)
            ideal_set = set(ideals)

            def cross_product(ideal):
                left = monomial_multiply(monomial_colon(ideal, a, b, 0, 1), a, b, 1, 0)
                right = monomial_multiply(monomial_colon(ideal, a, b, 1, 0), a, b, 0, 1)
                return left | right

            def cross_sum(ideal):
                left = monomial_colon(monomial_multiply(ideal, a, b, 1, 0), a, b, 0, 1)
                right = monomial_colon(monomial_multiply(ideal, a, b, 0, 1), a, b, 1, 0)
                return left | right

            recurrent = 0
            fixed = 0
            two_cycle_states = 0
            maximum_depth = 0
            cross_sum_maximum_depth = 0
            for ideal in ideals:
                check(cross_product(ideal) in ideal_set, f"C6 left ideal lattice {(a, b)}")
                depth, cycle = orbit_data(ideal, cross_product)
                check(cycle in (1, 2), f"C6 long cycle {(a, b)}: {ideal}")
                maximum_depth = max(maximum_depth, depth)
                recurrent += depth == 0
                fixed += cross_product(ideal) == ideal
                two_cycle_states += cross_product(cross_product(ideal)) == ideal and cross_product(ideal) != ideal

                check(cross_sum(ideal) in ideal_set, f"C7 left ideal lattice {(a, b)}")
                sum_depth, sum_cycle = orbit_data(ideal, cross_sum)
                check(sum_cycle in (1, 2), f"C7 long cycle {(a, b)}: {ideal}")
                cross_sum_maximum_depth = max(cross_sum_maximum_depth, sum_depth)

            m = min(a, b)
            predicted_depth = m if a != b else max(1, m - 2)
            check(fixed == m, f"C6 fixed count {(a, b)}")
            check(two_cycle_states == 2 * (m - 1), f"C6 two-cycle count {(a, b)}")
            check(recurrent == 3 * m - 2, f"C6 recurrent count {(a, b)}")
            check(maximum_depth == predicted_depth, f"C6 sharp depth {(a, b)}")
            lines.append(
                f"C6 box={a}x{b} ideals={len(ideals)} fixed={fixed} "
                f"two_cycle_states={two_cycle_states} max_depth={maximum_depth} "
                f"C7_max_depth={cross_sum_maximum_depth}"
            )
    return lines


# ---------------------------------------------------------------------------
# C8, C10--C13: polynomial, group, matrix-pair, and radical controls


def pilot_vieta():
    lines = []
    for q in (2, 3, 5, 7, 11, 13, 17, 19):
        def step(state):
            a, b = state
            return (a + b) % q, (a * b) % q

        fibres = Counter(step(state) for state in product(range(q), repeat=2))
        check(sum(fibres.values()) == q * q, f"C8 fibre partition q={q}")
        if q % 2:
            check(Counter(fibres.values())[1] == q, f"C8 ramified fibres q={q}")
            check(Counter(fibres.values())[2] == q * (q - 1) // 2, f"C8 split fibres q={q}")
            check(len(fibres) == q * (q + 1) // 2, f"C8 image size q={q}")
        fixed = 0
        maximum_depth = 0
        maximum_cycle = 0
        for state in product(range(q), repeat=2):
            depth, cycle = orbit_data(state, step)
            maximum_depth = max(maximum_depth, depth)
            maximum_cycle = max(maximum_cycle, cycle)
            fixed += step(state) == state
        check(fixed == q, f"C8 fixed axis q={q}")
        lines.append(
            f"C8 q={q} image={len(fibres)} fixed={fixed} "
            f"max_depth={maximum_depth} max_cycle={maximum_cycle}"
        )
    return lines


def heisenberg_multiply(x, y, p):
    a, b, c = x
    d, e, f = y
    return (a + d) % p, (b + e) % p, (c + f + a * e) % p


def heisenberg_inverse(x, p):
    a, b, c = x
    return (-a) % p, (-b) % p, (-c + a * b) % p


def pilot_heisenberg_pair_maps():
    lines = []
    expected_nielsen = {
        2: {1: 1, 3: 9, 6: 6},
        3: {1: 1, 8: 91},
        5: {1: 1, 4: 31, 20: 775},
        7: {1: 1, 16: 7353},
    }
    for p in (2, 3, 5, 7):
        elements = tuple(product(range(p), repeat=3))

        def nielsen(state):
            x, y = state
            return y, heisenberg_multiply(x, y, p)

        visited = set()
        cycles = Counter()
        for state in product(elements, repeat=2):
            image = nielsen(state)
            # Explicit inverse: (u,v) -> (v u^{-1},u).
            recovered = (heisenberg_multiply(image[1], heisenberg_inverse(image[0], p), p), image[0])
            check(recovered == state, f"C10 inverse failed p={p}: {state}")
            if state in visited:
                continue
            orbit = []
            position = {}
            current = state
            while current not in position:
                position[current] = len(orbit)
                orbit.append(current)
                visited.add(current)
                current = nielsen(current)
            check(position[current] == 0, f"C10 transient in bijection p={p}")
            cycles[len(orbit)] += 1
        check(dict(cycles) == expected_nielsen[p], f"C10 cycle census p={p}")
        lines.append(f"C10 p={p} cycles={dict(sorted(cycles.items()))}")

    # Direct Hurwitz owner control, restricted to smaller lanes.
    for p in (2, 3, 5):
        elements = tuple(product(range(p), repeat=3))
        identity = (0, 0, 0)

        def conjugate_by(x, y):
            return heisenberg_multiply(
                heisenberg_multiply(heisenberg_inverse(y, p), x, p), y, p
            )

        def hurwitz(state):
            x, y = state
            return y, conjugate_by(x, y)

        maximum_cycle = 0
        for state in product(elements, repeat=2):
            x, y = state
            product_xy = heisenberg_multiply(x, y, p)
            image = hurwitz(state)
            check(heisenberg_multiply(*image, p) == product_xy, f"C11 product failed p={p}")
            second = hurwitz(image)
            check(second[0] == conjugate_by(x, product_xy), f"C11 square conjugacy p={p}")
            depth, cycle = orbit_data(state, hurwitz)
            check(depth == 0, f"C11 nonbijective orbit p={p}")
            check((2 * p) % cycle == 0, f"C11 cycle does not divide 2p p={p}")
            maximum_cycle = max(maximum_cycle, cycle)
        lines.append(f"C11 p={p} max_cycle={maximum_cycle} divisor_bound={2*p}")
    return lines


def mat2_rank(a, q):
    if a == (0, 0, 0, 0):
        return 0
    return 2 if (a[0] * a[3] - a[1] * a[2]) % q else 1


def pilot_matrix_pair_product():
    lines = []
    for q in (2, 3):
        matrices = tuple(product(range(q), repeat=4))

        def step(state):
            a, b = state
            return mat2_mul(a, b, q), mat2_mul(b, a, q)

        maximum_depth = 0
        maximum_cycle = 0
        for state in product(matrices, repeat=2):
            image = step(state)
            check(mat2_rank(image[0], q) <= min(mat2_rank(state[0], q), mat2_rank(state[1], q)), "C12 rank")
            check(mat2_rank(image[1], q) <= min(mat2_rank(state[0], q), mat2_rank(state[1], q)), "C12 rank")
            depth, cycle = orbit_data(state, step)
            maximum_depth = max(maximum_depth, depth)
            maximum_cycle = max(maximum_cycle, cycle)
        lines.append(
            f"C12 q={q} states={len(matrices)**2} max_depth={maximum_depth} "
            f"max_cycle={maximum_cycle}"
        )
    return lines


def upper_positions(n):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def tuple_to_matrix(values, n):
    matrix = [[0] * n for _ in range(n)]
    for value, (i, j) in zip(values, upper_positions(n)):
        matrix[i][j] = value
    return matrix


def matrix_multiply(a, b, q):
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) % q for j in range(n)]
        for i in range(n)
    ]


def matrix_tuple(a):
    return tuple(value for row in a for value in row)


def pilot_radical_sandwich():
    lines = []
    for n in range(2, 7):
        positions = upper_positions(n)
        regular_shift = [[0] * n for _ in range(n)]
        for i in range(n - 1):
            regular_shift[i][i + 1] = 1

        def step(state):
            a = [list(state[i * n : (i + 1) * n]) for i in range(n)]
            return matrix_tuple(matrix_multiply(matrix_multiply(a, regular_shift, 2), a, 2))

        maximum_depth = 0
        for values in product(range(2), repeat=len(positions)):
            start = matrix_tuple(tuple_to_matrix(values, n))
            depth, cycle = orbit_data(start, step)
            check(cycle == 1 and step((0,) * (n * n)) == (0,) * (n * n), f"C13 recurrence n={n}")
            maximum_depth = max(maximum_depth, depth)
        predicted = 0
        exponent = 1
        while exponent < n:
            exponent = 2 * exponent + 1
            predicted += 1
        check(maximum_depth == predicted, f"C13 sharp logarithmic depth n={n}")
        lines.append(
            f"C13 n={n} states={2**len(positions)} max_depth={maximum_depth} "
            f"predicted={predicted}"
        )
    return lines


def main():
    sections = []
    sections.extend(pilot_transpose_defects())
    sections.extend(pilot_subspace_maps())
    sections.extend(pilot_monomial_ideals())
    sections.extend(pilot_vieta())
    sections.extend(pilot_heisenberg_pair_maps())
    sections.extend(pilot_matrix_pair_product())
    sections.extend(pilot_radical_sandwich())

    print("P122--P126 ALGEBRAIC INTAKE PILOTS: PASS")
    print(f"assertions={ASSERTIONS}")
    print("coded_candidates=C1,C2,C3,C4,C5,C6,C7,C8,C10,C11,C12,C13")
    for line in sections:
        print(line)


if __name__ == "__main__":
    main()
