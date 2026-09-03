#!/usr/bin/env python3
"""Deterministic exact pilots for a fresh nonlinear algebra breadth lane.

Sixteen of the eighteen maps pass the intake exclusions against
valuation/multiplicity erosion, pure power maps, incidence-linear maps, and
order-theoretic closure operators.  Two explicit retractions are retained
only as negative controls and are not counted toward the qualifying breadth.
Enumeration is falsification evidence; theorem and owner decisions live in
the accompanying scout report.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from math import comb


ASSERTIONS = 0
DIGEST = sha256()


def check(condition: bool, message: str = "assertion failed") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def encode(obj) -> bytes:
    return repr(obj).encode("ascii")


def analyze(label: str, states, update):
    states = tuple(states)
    state_set = set(states)
    check(len(state_set) == len(states), f"duplicate states in {label}")
    arrows = {}
    indegree = Counter()
    for state in states:
        target = update(state)
        check(target in state_set, f"non-closed update {label}: {target}")
        arrows[state] = target
        indegree[target] += 1
        DIGEST.update(label.encode("ascii"))
        DIGEST.update(encode(state))
        DIGEST.update(b"->")
        DIGEST.update(encode(target))

    depth = {}
    cycle_hist = Counter()
    for start in states:
        if start in depth:
            continue
        path = []
        local = {}
        current = start
        while current not in depth and current not in local:
            local[current] = len(path)
            path.append(current)
            current = arrows[current]
        if current in local:
            split = local[current]
            cycle = path[split:]
            cycle_hist[len(cycle)] += 1
            for state in cycle:
                depth[state] = 0
            distance = 0
            for state in reversed(path[:split]):
                distance += 1
                depth[state] = distance
        else:
            distance = depth[current]
            for state in reversed(path):
                distance += 1
                depth[state] = distance

    check(len(depth) == len(states), f"depth coverage {label}")
    image_size = len(indegree)
    fixed = sum(arrows[x] == x for x in states)
    fibre_hist = Counter(indegree.values())
    if image_size < len(states):
        fibre_hist[0] = len(states) - image_size
    sig = {
        "states": len(states),
        "image": image_size,
        "fixed": fixed,
        "height": max(depth.values(), default=0),
        "cycles": tuple(sorted(cycle_hist.items())),
        "fibres": tuple(sorted(fibre_hist.items())),
        "depths": tuple(sorted(Counter(depth.values()).items())),
    }
    print(
        f"PILOT {label} S={sig['states']} I={sig['image']} F={sig['fixed']} "
        f"H={sig['height']} C={sig['cycles']} fibres={sig['fibres']} "
        f"depths={sig['depths']}"
    )
    return arrows, indegree, depth, sig


def vectors(q: int, m: int):
    return tuple(product(range(q), repeat=m))


def dot2(u, v) -> int:
    return sum(a & b for a, b in zip(u, v)) & 1


def xor_scaled(u, bit: int, v):
    return tuple(a ^ (bit & b) for a, b in zip(u, v))


def scalar_vec(bit: int, v):
    return tuple(bit & x for x in v)


def verify_v01_bilinear_shift() -> None:
    print("[V01_BSR_bilinear_shift_register]")
    for m in range(1, 8):
        vecs = vectors(2, m)
        states = tuple((u, v) for u in vecs for v in vecs)

        def update(state):
            u, v = state
            return v, scalar_vec(dot2(u, v), v)

        arrows, indegree, depth, sig = analyze(f"V01/m={m}", states, update)
        a = 1 << (m - 1)
        expected_depths = Counter(
            {
                0: 1 + a,
                1: (1 << m) - 1 + a * (a - 1),
                2: ((1 << m) - 1) * a,
                3: (a - 1) * a,
            }
        )
        expected_depths += Counter()  # drop a zero layer when m=1
        check(Counter(depth.values()) == expected_depths, f"V01 depths m={m}")
        check(sig["fixed"] == 1 + a)
        check(sig["height"] == (2 if m == 1 else 3))

        zero = ((0,) * m, (0,) * m)
        check(indegree[zero] == 1 << m)
        for target in states:
            first, second = target
            if second == (0,) * m:
                expected = (1 << m) if first == (0,) * m else a
            elif second == first and first != (0,) * m:
                expected = a
            else:
                expected = 0
            check(indegree.get(target, 0) == expected, f"V01 fibre m={m}")

        # Weight-marked affine-hyperplane fibres.  The coefficient identity
        # is checked for every nonzero target vector and both dot values.
        for target in vecs[1:]:
            weight = sum(target)
            signed = [0] * (m + 1)
            for i in range(weight + 1):
                for j in range(m - weight + 1):
                    signed[i + j] += (-1) ** i * comb(weight, i) * comb(m - weight, j)
            for value in (0, 1):
                actual = Counter(sum(u) for u in vecs if dot2(u, target) == value)
                predicted = {
                    k: (comb(m, k) + (-1) ** value * signed[k]) // 2
                    for k in range(m + 1)
                }
                check(
                    tuple(actual.get(k, 0) for k in range(m + 1))
                    == tuple(predicted[k] for k in range(m + 1)),
                    f"V01 marked fibre m={m} target={target} value={value}",
                )


def verify_v02_cyclic_gram_gate() -> None:
    print("\n[V02_CGG_cyclic_Gram_gate]")
    for m in range(1, 6):
        vecs = vectors(2, m)
        zero = (0,) * m
        states = tuple((u, v, w) for u in vecs for v in vecs for w in vecs)

        def update(state):
            u, v, w = state
            return (
                scalar_vec(dot2(u, v), w),
                scalar_vec(dot2(v, w), u),
                scalar_vec(dot2(w, u), v),
            )

        arrows, indegree, depth, sig = analyze(f"V02/m={m}", states, update)
        q = 1 << m
        recurrent = q**3 // 8
        fixed = 1 + q // 2
        three_cycles = (recurrent - q // 2) // 3
        zero_fibre = q**3 // 8 + 9 * q**2 // 4 - 3 * q // 2
        expected_depths = Counter(
            {
                0: 1 + recurrent,
                1: zero_fibre - 1,
                2: 3 * q * (q - 1) * (q - 2) // 4,
            }
        )
        expected_depths += Counter()
        expected_cycles = Counter({1: fixed, 3: three_cycles})
        expected_cycles += Counter()

        check(sig["fixed"] == fixed, f"V02 fixed m={m}")
        check(Counter(dict(sig["cycles"])) == expected_cycles, f"V02 cycles m={m}")
        check(Counter(depth.values()) == expected_depths, f"V02 depths m={m}")
        check(indegree[(zero, zero, zero)] == zero_fibre, f"V02 zero fibre m={m}")

        for state, image in arrows.items():
            u, v, w = state
            full = dot2(u, v) & dot2(v, w) & dot2(w, u)
            if full:
                check(image == (w, u, v))
                check(arrows[arrows[arrows[state]]] == state)
            else:
                check(arrows[image] == (zero, zero, zero))

        # Exact fibre formula for every target.  It is deliberately checked
        # on the literal targets rather than reconstructed from a histogram.
        for target in states:
            nonzero = [x for x in target if x != zero]
            if not nonzero:
                predicted = zero_fibre
            elif len(nonzero) == 3:
                x, y, z = target
                predicted = int(dot2(x, y) == dot2(y, z) == dot2(z, x) == 1)
            elif len(nonzero) == 2:
                x, y = nonzero
                if dot2(x, y):
                    predicted = 0
                elif x == y:
                    predicted = q // 2
                else:
                    predicted = q // 4
            else:
                (x,) = nonzero
                radical_size = 1 if dot2(x, x) else 2
                # For q=2 the first factor is zero; writing it this way
                # avoids a spurious fractional q/4 intermediate.
                predicted = (q // 2 - radical_size) * q // 4
            check(
                indegree.get(target, 0) == predicted,
                f"V02 target fibre m={m} target={target}",
            )

        check(max(indegree.values()) == zero_fibre, f"V02 maximum fibre m={m}")
        check(
            sum(value == zero_fibre for value in indegree.values()) == 1,
            f"V02 unique maximum fibre m={m}",
        )
        print(
            f"THEOREM V02 m={m} Q={q} recurrent={recurrent} fixed={fixed} "
            f"three_cycles={three_cycles} zero_fibre={zero_fibre} "
            f"depth2={expected_depths.get(2, 0)}"
        )


def verify_v03_dot_transvection() -> None:
    print("\n[V03_DTR_dot_transvection_recurrence]")
    for m in (2, 3, 4):
        vecs = vectors(2, m)
        states = tuple((u, v) for u in vecs for v in vecs)

        def update(state):
            u, v = state
            return v, xor_scaled(u, dot2(u, v), v)

        analyze(f"V03/m={m}", states, update)


def cross(u, v, q: int):
    return (
        (u[1] * v[2] - u[2] * v[1]) % q,
        (u[2] * v[0] - u[0] * v[2]) % q,
        (u[0] * v[1] - u[1] * v[0]) % q,
    )


def verify_v04_cross_fold() -> None:
    print("\n[V04_XCF_cross_product_antisymmetry_fold]")
    for q in (2, 3):
        vecs = vectors(q, 3)
        zero = (0, 0, 0)
        states = tuple((u, v) for u in vecs for v in vecs)

        def update(state):
            u, v = state
            return cross(u, v, q), cross(v, u, q)

        arrows, _, _, sig = analyze(f"V04/q={q}", states, update)
        check(sig["height"] == 2)
        for image in arrows.values():
            check(arrows[image] == (zero, zero))


def matrices(n: int, q: int):
    return tuple(product(range(q), repeat=n * n))


def mat_add(a, b, q: int):
    return tuple((x + y) % q for x, y in zip(a, b))


def mat_scale(c: int, a, q: int):
    return tuple((c * x) % q for x in a)


def mat_transpose(a, n: int):
    return tuple(a[j * n + i] for i in range(n) for j in range(n))


def mat_mul(a, b, n: int, q: int):
    return tuple(
        sum(a[i * n + k] * b[k * n + j] for k in range(n)) % q
        for i in range(n)
        for j in range(n)
    )


def mat_det(a, n: int, q: int) -> int:
    total = 0
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = 1
        for i, j in enumerate(perm):
            term = term * a[i * n + j] % q
        total += (-1 if inversions & 1 else 1) * term
    return total % q


def zero_matrix(n: int):
    return (0,) * (n * n)


def verify_m01_diagonal_commutator() -> None:
    print("\n[M01_DCF_diagonal_feedback_commutator]")
    for n, q in ((2, 2), (2, 3), (3, 2), (3, 3), (4, 2)):
        states = matrices(n, q)
        zero = zero_matrix(n)

        def update(a):
            diagonal = tuple(a[i * n + i] for i in range(n))
            return tuple(
                0 if i == j else ((diagonal[i] - diagonal[j]) * a[i * n + j]) % q
                for i in range(n)
                for j in range(n)
            )

        arrows, indegree, depth, sig = analyze(f"M01/n={n}/q={q}", states, update)
        check(sig["fixed"] == 1)
        check(sig["height"] == 2)
        for a, image in arrows.items():
            check(arrows[image] == zero, f"M01 square zero n={n} q={q}")

        # Exact every-target Potts/chromatic fibre polynomial evaluated at q.
        diagonals = vectors(q, n)
        marked_actual = {}
        for source, target in arrows.items():
            colors = tuple(source[i * n + i] for i in range(n))
            occupation = tuple(colors.count(alpha) for alpha in range(q))
            marked_actual.setdefault(target, Counter())[occupation] += 1
        for target in states:
            if any(target[i * n + i] for i in range(n)):
                predicted = 0
                predicted_marked = Counter()
            else:
                predicted = 0
                predicted_marked = Counter()
                for colors in diagonals:
                    valid = True
                    equal_ordered_pairs = 0
                    for i in range(n):
                        for j in range(n):
                            if i == j:
                                continue
                            if colors[i] == colors[j]:
                                equal_ordered_pairs += 1
                                if target[i * n + j] != 0:
                                    valid = False
                    if valid:
                        contribution = q ** equal_ordered_pairs
                        predicted += contribution
                        occupation = tuple(colors.count(alpha) for alpha in range(q))
                        predicted_marked[occupation] += contribution
            check(indegree.get(target, 0) == predicted, f"M01 fibre n={n} q={q}")
            check(
                marked_actual.get(target, Counter()) == predicted_marked,
                f"M01 occupation-marked fibre n={n} q={q}",
            )
        check(Counter(depth.values())[1] == indegree[zero] - 1)

        # Image census by underlying undirected support graphs.  Each present
        # unordered support edge has q^2-1 possible ordered nonzero pairs.
        undirected_edges = tuple((i, j) for i in range(n) for j in range(i + 1, n))
        predicted_image = 0
        for mask in range(1 << len(undirected_edges)):
            colorable = any(
                all(
                    colors[i] != colors[j]
                    for bit, (i, j) in enumerate(undirected_edges)
                    if (mask >> bit) & 1
                )
                for colors in diagonals
            )
            if colorable:
                predicted_image += (q * q - 1) ** mask.bit_count()
        check(sig["image"] == predicted_image, f"M01 image census n={n} q={q}")
        maximum = max(indegree.values())
        check(maximum == indegree[zero])
        check(sum(value == maximum for value in indegree.values()) == 1)
        print(
            f"THEOREM M01 n={n} q={q} kernel={indegree[zero]} "
            f"image_by_colorable_supports={predicted_image} unique_max_fibre={maximum}"
        )


def verify_m02_hadamard_mutualization() -> None:
    print("\n[M02_HMP_Hadamard_mutualization]")
    for n in (2, 3):
        states = matrices(n, 2)

        def update(a):
            at = mat_transpose(a, n)
            return tuple(x & y for x, y in zip(a, at))

        arrows, indegree, _, _ = analyze(f"M02/n={n}", states, update)
        for a, image in arrows.items():
            check(arrows[image] == image)
            zeros = sum(image[i * n + j] == 0 for i in range(n) for j in range(i + 1, n))
            check(indegree[image] == 3 ** zeros)


def verify_m03_determinant_transpose_blend() -> None:
    print("\n[M03_DTB_determinant_triggered_transpose_blend]")
    for n in (2, 3):
        states = matrices(n, 2)

        def update(a):
            return mat_add(a, mat_scale(mat_det(a, n, 2), mat_transpose(a, n), 2), 2)

        analyze(f"M03/n={n}", states, update)


def verify_m04_alternating_gram_defect() -> None:
    print("\n[M04_AGD_zero_diagonal_Gram_defect]")
    for n in (2, 3):
        states = matrices(n, 2)

        def update(a):
            gram = mat_mul(a, mat_transpose(a, n), n, 2)
            return tuple(0 if i == j else gram[i * n + j] for i in range(n) for j in range(n))

        analyze(f"M04/n={n}", states, update)


def verify_m05_quadratic_diagonal_feedback() -> None:
    print("\n[M05_QDF_square_plus_input_diagonal]")
    for n in (2, 3):
        states = matrices(n, 2)

        def update(a):
            square = mat_mul(a, a, n, 2)
            diagonal = tuple(a[i * n + i] if i == j else 0 for i in range(n) for j in range(n))
            return mat_add(square, diagonal, 2)

        analyze(f"M05/n={n}", states, update)


def verify_m06_mixed_adjoint_factor() -> None:
    print("\n[M06_MAF_square_plus_transpose_left_factor]")
    for n in (2, 3):
        states = matrices(n, 2)

        def update(a):
            return mat_add(mat_mul(a, a, n, 2), mat_mul(mat_transpose(a, n), a, n, 2), 2)

        analyze(f"M06/n={n}", states, update)


def verify_m07_triangular_commutator() -> None:
    print("\n[M07_TLC_strict_triangular_part_commutator]")
    for n, q in ((2, 3), (2, 5), (3, 2)):
        states = matrices(n, q)
        zero = zero_matrix(n)

        def update(a):
            upper = tuple(a[i * n + j] if i < j else 0 for i in range(n) for j in range(n))
            lower = tuple(a[i * n + j] if i > j else 0 for i in range(n) for j in range(n))
            ul = mat_mul(upper, lower, n, q)
            lu = mat_mul(lower, upper, n, q)
            return tuple((x - y) % q for x, y in zip(ul, lu))

        arrows, _, _, _ = analyze(f"M07/n={n}/q={q}", states, update)
        if n == 2:
            for image in arrows.values():
                check(arrows[image] == zero)


def verify_m08_companion_retraction() -> None:
    print("\n[M08_CCR_characteristic_companion_retraction]")
    for q in (2, 3, 5):
        n = 2
        states = matrices(n, q)

        def update(a):
            trace = (a[0] + a[3]) % q
            determinant = mat_det(a, 2, q)
            return (0, (-determinant) % q, 1, trace)

        arrows, _, _, sig = analyze(f"M08/q={q}", states, update)
        check(sig["height"] == 1)
        for image in arrows.values():
            check(arrows[image] == image)


def perm_compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inverse(p):
    out = [0] * len(p)
    for i, value in enumerate(p):
        out[value] = i
    return tuple(out)


def conjugate(x, y):
    return perm_compose(perm_compose(x, y), perm_inverse(x))


def verify_g01_conjugate_inverse_fold() -> None:
    print("\n[G01_CIF_conjugate_inverse_fold]")
    for n in (3, 4):
        group = tuple(permutations(range(n)))
        states = tuple((x, y) for x in group for y in group)

        def update(state):
            x, y = state
            z = conjugate(x, y)
            return z, perm_inverse(z)

        _, indegree, _, sig = analyze(f"G01/S{n}", states, update)
        check(set(indegree.values()) == {len(group)})
        check(sig["height"] == 1)


def verify_g02_mutual_conjugation() -> None:
    print("\n[G02_MCF_mutual_conjugation_feedback]")
    for n in (3, 4):
        group = tuple(permutations(range(n)))
        states = tuple((x, y) for x in group for y in group)

        def update(state):
            x, y = state
            return conjugate(x, y), conjugate(y, x)

        analyze(f"G02/S{n}", states, update)


def verify_g03_hurwitz_pair() -> None:
    print("\n[G03_HUR_Hurwitz_pair_action]")
    for n in (3, 4):
        group = tuple(permutations(range(n)))
        states = tuple((x, y) for x in group for y in group)

        def update(state):
            x, y = state
            return y, conjugate(perm_inverse(y), x)

        arrows, indegree, depth, sig = analyze(f"G03/S{n}", states, update)
        check(sig["height"] == 0)
        check(set(indegree.values()) == {1})
        for (x, y), image in arrows.items():
            check(perm_compose(*image) == perm_compose(x, y))


def verify_g04_product_exchange() -> None:
    print("\n[G04_PXE_product_exchange]")
    for n in (3, 4):
        group = tuple(permutations(range(n)))
        states = tuple((x, y) for x in group for y in group)

        def update(state):
            x, y = state
            return perm_compose(x, y), perm_compose(y, x)

        analyze(f"G04/S{n}", states, update)


def verify_r01_inverse_sum() -> None:
    print("\n[R01_IFS_inverse_sum_rational_feedback]")
    for q in (5, 7, 11, 13, 17, 19):
        states = tuple(range(q))

        def update(x):
            return 0 if x == 0 else (x + pow(x, -1, q)) % q

        analyze(f"R01/q={q}", states, update)


def verify_r02_cyclic_quadratic_plus() -> None:
    print("\n[R02_CQP_cyclic_quadratic_plus]")
    for q in (2, 3, 5, 7):
        states = vectors(q, 3)

        def update(state):
            x, y, z = state
            return ((x * y + z) % q, (y * z + x) % q, (z * x + y) % q)

        analyze(f"R02/q={q}", states, update)


def main() -> None:
    print("FRESH_NONLINEAR_ALGEBRA_GATE")
    print(
        "candidate_count=18 qualifying_nonclosure_count=16 "
        "external=HOLD_EXTERNAL computation=falsification_not_proof"
    )
    verify_v01_bilinear_shift()
    verify_v02_cyclic_gram_gate()
    verify_v03_dot_transvection()
    verify_v04_cross_fold()
    verify_m01_diagonal_commutator()
    verify_m02_hadamard_mutualization()
    verify_m03_determinant_transpose_blend()
    verify_m04_alternating_gram_defect()
    verify_m05_quadratic_diagonal_feedback()
    verify_m06_mixed_adjoint_factor()
    verify_m07_triangular_commutator()
    verify_m08_companion_retraction()
    verify_g01_conjugate_inverse_fold()
    verify_g02_mutual_conjugation()
    verify_g03_hurwitz_pair()
    verify_g04_product_exchange()
    verify_r01_inverse_sum()
    verify_r02_cyclic_quadratic_plus()
    print(f"\nEDGE_DIGEST={DIGEST.hexdigest()}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
