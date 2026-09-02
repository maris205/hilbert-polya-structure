#!/usr/bin/env python3
"""Independent exact checks for the open P166 algebra/code scout.

The program is intentionally self-contained.  It enumerates the three literal
maps from definitions; it imports no paper or prior-scout implementation.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import reduce
from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb, factorial, gcd, lcm


ASSERTIONS = 0


def check(condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message or f"assertion {ASSERTIONS} failed")


def digest(obj) -> str:
    return sha256(repr(obj).encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# RTCD: reversal-twisted coboundary dynamics on S_n


def p_comp(p, q):
    """Composition p o q."""
    return tuple(p[q[i]] for i in range(len(p)))


def p_inv(p):
    ans = [0] * len(p)
    for i, x in enumerate(p):
        ans[x] = i
    return tuple(ans)


def p_pow(p, exponent: int):
    ans = tuple(range(len(p)))
    base = p
    while exponent:
        if exponent & 1:
            ans = p_comp(ans, base)
        base = p_comp(base, base)
        exponent //= 2
    return ans


def p_order(p) -> int:
    seen = set()
    answer = 1
    for i in range(len(p)):
        if i not in seen:
            j = i
            length = 0
            while j not in seen:
                seen.add(j)
                length += 1
                j = p[j]
            answer = lcm(answer, length)
    return answer


def cycle_type(p):
    seen = set()
    answer = []
    for i in range(len(p)):
        if i not in seen:
            j = i
            length = 0
            while j not in seen:
                seen.add(j)
                length += 1
                j = p[j]
            answer.append(length)
    return tuple(sorted(answer))


def rtcd_map(p):
    w = tuple(reversed(range(len(p))))
    # p^{-1} w p w
    return p_comp(p_comp(p_inv(p), w), p_comp(p, w))


def rtcd_in_image(p) -> bool:
    w = tuple(reversed(range(len(p))))
    # p w must be conjugate to w.
    return cycle_type(p_comp(p, w)) == cycle_type(w)


def v2(number: int) -> int:
    answer = 0
    while number % 2 == 0:
        number //= 2
        answer += 1
    return answer


def multiplicative_order_minus_two(odd_modulus: int) -> int:
    if odd_modulus == 1:
        return 1
    x = -2 % odd_modulus
    answer = 1
    while x != 1:
        x = (-2 * x) % odd_modulus
        answer += 1
    return answer


def orbit_signature(start, transition):
    where = {}
    x = start
    while x not in where:
        where[x] = len(where)
        x = transition(x)
    mu = where[x]
    return mu, len(where) - mu


def integer_partitions(total: int, cap=None):
    if total == 0:
        yield ()
        return
    if cap is None or cap > total:
        cap = total
    for first in range(cap, 0, -1):
        for tail in integer_partitions(total - first, first):
            yield (first,) + tail


def z_partition(partition) -> int:
    counts = Counter(partition)
    answer = 1
    for part, multiplicity in counts.items():
        answer *= (part ** multiplicity) * factorial(multiplicity)
    return answer


def matching_weight(r: int, partition) -> int:
    return (2 ** (r - len(partition))) * factorial(r) // z_partition(partition)


def rtcd_order_census_formula(n: int):
    r = n // 2
    answer = Counter()
    if n % 2 == 0:
        for partition in integer_partitions(r):
            answer[reduce(lcm, partition, 1)] += matching_weight(r, partition)
    else:
        for path_edges in range(r + 1):
            for partition in integer_partitions(r - path_edges):
                order = reduce(lcm, (2 * path_edges + 1,) + partition, 1)
                answer[order] += matching_weight(r, partition)
    return answer


def rtcd_fixed_formula(n: int, iterate: int) -> int:
    r = n // 2
    modulus = abs((-2) ** iterate - 1)
    answer = 0
    if n % 2 == 0:
        for partition in integer_partitions(r):
            if all(modulus % part == 0 for part in partition):
                answer += matching_weight(r, partition)
    else:
        for path_edges in range(r + 1):
            if modulus % (2 * path_edges + 1):
                continue
            for partition in integer_partitions(r - path_edges):
                if all(modulus % part == 0 for part in partition):
                    answer += matching_weight(r, partition)
    return answer


def mobius(number: int) -> int:
    n = number
    primes = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            primes += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        primes += 1
    return -1 if primes % 2 else 1


def divisors(number: int):
    return [d for d in range(1, number + 1) if number % d == 0]


def verify_rtcd():
    rows = []
    fingerprints = []
    for n in range(1, 9):
        states = list(permutations(range(n)))
        w = tuple(reversed(range(n)))
        next_state = {p: rtcd_map(p) for p in states}
        image_fibres = Counter(next_state.values())
        image = set(image_fibres)
        expected_centralizer = (2 ** (n // 2)) * factorial(n // 2)

        check(all(rtcd_in_image(y) for y in image), f"RTCD image support n={n}")
        check(image == {p for p in states if rtcd_in_image(p)}, f"RTCD image equality n={n}")
        check(set(image_fibres.values()) == {expected_centralizer}, f"RTCD fibre n={n}")
        check(len(image) == factorial(n) // expected_centralizer, f"RTCD image size n={n}")

        direct_order_census = Counter(p_order(y) for y in image)
        formula_order_census = rtcd_order_census_formula(n)
        check(direct_order_census == formula_order_census, f"RTCD type census n={n}")

        depths = []
        recurring_periods = Counter()
        signatures = {}
        for p in states:
            y = next_state[p]
            theta_y = p_comp(p_comp(w, y), w)
            check(theta_y == p_inv(y), f"RTCD twisted identity n={n}")
            check(next_state[y] == p_comp(p_inv(y), p_inv(y)), f"RTCD power collapse n={n}")

            actual_depth, actual_period = orbit_signature(p, lambda x: next_state[x])
            signatures[p] = (actual_depth, actual_period)
            if rtcd_in_image(p):
                order_source = p_order(p)
                predicted_depth = v2(order_source)
                predicted_odd_order = order_source >> predicted_depth
            else:
                order_image = p_order(y)
                predicted_depth = 1 + v2(order_image)
                predicted_odd_order = order_image >> v2(order_image)
            predicted_period = multiplicative_order_minus_two(predicted_odd_order)
            check(actual_depth == predicted_depth, f"RTCD depth n={n}")
            check(actual_period == predicted_period, f"RTCD period n={n}")
            depths.append(actual_depth)
            if actual_depth == 0:
                recurring_periods[actual_period] += 1

        if n == 1:
            expected_max_depth = 0
        else:
            expected_max_depth = 1 + (n // 2).bit_length() - 1
        check(max(depths) == expected_max_depth, f"RTCD sharp depth n={n}")

        fixed_values = {}
        for iterate in range(1, 13):
            direct_fixed = 0
            exact_period = 0
            for p in states:
                x = p
                for _ in range(iterate):
                    x = next_state[x]
                direct_fixed += x == p
                mu, period = signatures[p]
                exact_period += mu == 0 and period == iterate
            formula_fixed = rtcd_fixed_formula(n, iterate)
            check(direct_fixed == formula_fixed, f"RTCD fixed formula n={n}, k={iterate}")
            primitive = sum(mobius(iterate // d) * rtcd_fixed_formula(n, d)
                            for d in divisors(iterate))
            check(primitive == exact_period, f"RTCD Mobius n={n}, k={iterate}")
            check(primitive % iterate == 0, f"RTCD cycles integral n={n}, k={iterate}")
            fixed_values[iterate] = formula_fixed

        rows.append((n, len(states), len(image), expected_centralizer,
                     max(depths), sum(recurring_periods.values()),
                     tuple(sorted(recurring_periods.items()))))
        fingerprints.append((n, tuple(sorted(image)), tuple(sorted(fixed_values.items()))))
    return rows, digest(fingerprints)


# ---------------------------------------------------------------------------
# UTAS: A -> A + A^2 on upper triangular binary matrices


def zero_matrix(n):
    return tuple([0] * (n * n))


def matrix_add(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def matrix_mul(a, b):
    n = int(len(a) ** 0.5)
    return tuple(sum(a[n * i + k] * b[n * k + j] for k in range(n)) % 2
                 for i in range(n) for j in range(n))


def matrix_pow(a, exponent: int):
    n = int(len(a) ** 0.5)
    answer = tuple(1 if i == j else 0 for i in range(n) for j in range(n))
    base = a
    while exponent:
        if exponent & 1:
            answer = matrix_mul(answer, base)
        base = matrix_mul(base, base)
        exponent //= 2
    return answer


def triangular_matrices(n, strict=False):
    slots = [(i, j) for i in range(n) for j in range(i + (1 if strict else 0), n)]
    for mask in range(1 << len(slots)):
        entries = [0] * (n * n)
        for bit, (i, j) in enumerate(slots):
            entries[n * i + j] = (mask >> bit) & 1
        yield tuple(entries)


def matrix_phi(a):
    return matrix_add(a, matrix_mul(a, a))


def is_strict(a):
    n = int(len(a) ** 0.5)
    return all(a[n * i + i] == 0 for i in range(n))


def nilpotency_index(a):
    n = int(len(a) ** 0.5)
    power = a
    zero = zero_matrix(n)
    for exponent in range(1, n + 1):
        if power == zero:
            return exponent
        power = matrix_mul(power, a)
    raise AssertionError("strict matrix was not nilpotent")


def artin_schreier_inverse(y):
    n = int(len(y) ** 0.5)
    answer = zero_matrix(n)
    power = y
    while power != zero_matrix(n):
        answer = matrix_add(answer, power)
        power = matrix_mul(power, power)
    return answer


def strict_iterate_formula(a, iterate: int):
    n = int(len(a) ** 0.5)
    answer = zero_matrix(n)
    # (I+F)^t and Lucas: C(t,j) is odd exactly when j is a submask of t.
    for j in range(iterate + 1):
        if j & ~iterate == 0:
            answer = matrix_add(answer, matrix_pow(a, 1 << j))
    return answer


def verify_utas():
    rows = []
    fingerprints = []
    for n in range(1, 6):
        upper = list(triangular_matrices(n))
        strict = list(triangular_matrices(n, strict=True))
        fibres = Counter(matrix_phi(a) for a in upper)
        image = set(fibres)
        check(image == set(strict), f"UTAS image n={n}")

        idempotents = [e for e in upper if matrix_mul(e, e) == e]
        expected_zero_fibre = sum(comb(n, k) * (2 ** (k * (n - k))) for k in range(n + 1))
        check(len(idempotents) == expected_zero_fibre, f"UTAS idempotents n={n}")
        check(fibres[zero_matrix(n)] == expected_zero_fibre, f"UTAS zero fibre n={n}")
        check(fibres[zero_matrix(n)] == max(fibres.values()), f"UTAS extremum n={n}")

        for y in strict:
            inverse = artin_schreier_inverse(y)
            check(matrix_phi(inverse) == y, f"UTAS inverse n={n}")
            commuting_idempotents = 0
            for e in idempotents:
                if matrix_mul(e, y) == matrix_mul(y, e):
                    commuting_idempotents += 1
                    source = matrix_add(inverse, e)
                    check(matrix_phi(source) == y, f"UTAS centralizer lift n={n}")
            check(fibres[y] == commuting_idempotents, f"UTAS target fibre n={n}")

        period_census = Counter()
        square_zero = 0
        for a in strict:
            x = a
            for iterate in range(8):
                check(x == strict_iterate_formula(a, iterate), f"UTAS iterate n={n}")
                x = matrix_phi(x)
            index = nilpotency_index(a)
            r = 0
            while (1 << (1 << r)) < index:
                r += 1
            predicted_period = 1 << r
            actual_depth, actual_period = orbit_signature(a, matrix_phi)
            check(actual_depth == 0, f"UTAS core recurrence n={n}")
            check(actual_period == predicted_period, f"UTAS period n={n}")
            period_census[predicted_period] += 1
            square_zero += matrix_mul(a, a) == zero_matrix(n)

        for a in upper:
            actual_depth, _ = orbit_signature(a, matrix_phi)
            check(actual_depth == (0 if is_strict(a) else 1), f"UTAS tail n={n}")

        regular = [0] * (n * n)
        for i in range(n - 1):
            regular[n * i + i + 1] = 1
        regular = tuple(regular)
        check(fibres[regular] == 2, f"UTAS regular fibre n={n}")
        check(square_zero == period_census[1], f"UTAS fixed census n={n}")

        spectrum = tuple(sorted(Counter(fibres.values()).items()))
        rows.append((n, len(upper), len(image), len(idempotents),
                     tuple(sorted(period_census.items())), spectrum))
        fingerprints.append((n, tuple(sorted(fibres.items()))))
    return rows, digest(fingerprints)


# ---------------------------------------------------------------------------
# SCD: quadratic-subfield core followed by Euclidean duality


# F_4 = F_2[a]/(a^2+a+1), encoded by low/high binary coefficients.
GF4_MUL = (
    (0, 0, 0, 0),
    (0, 1, 2, 3),
    (0, 2, 3, 1),
    (0, 3, 1, 2),
)
GF4_INV = (None, 1, 3, 2)


def f4_add(a, b):
    return a ^ b


def f4_mul(a, b):
    return GF4_MUL[a][b]


def f4_dot(u, v):
    answer = 0
    for x, y in zip(u, v):
        answer = f4_add(answer, f4_mul(x, y))
    return answer


def f4_span(basis, n):
    vectors = set()
    for coefficients in product(range(4), repeat=len(basis)):
        out = [0] * n
        for coefficient, row in zip(coefficients, basis):
            for j in range(n):
                out[j] = f4_add(out[j], f4_mul(coefficient, row[j]))
        vectors.add(tuple(out))
    return frozenset(vectors)


def all_f4_subspaces(n):
    answer = {}
    columns = tuple(range(n))
    for dimension in range(n + 1):
        for pivots in combinations(columns, dimension):
            free = [(row, col) for row, pivot in enumerate(pivots)
                    for col in columns if col not in pivots and col > pivot]
            for values in product(range(4), repeat=len(free)):
                matrix = [[0] * n for _ in range(dimension)]
                for row, pivot in enumerate(pivots):
                    matrix[row][pivot] = 1
                for value, (row, col) in zip(values, free):
                    matrix[row][col] = value
                basis = tuple(tuple(row) for row in matrix)
                key = f4_span(basis, n)
                check(key not in answer, f"duplicate F4 RREF n={n}")
                answer[key] = basis
    return answer


def f2_basis(vectors, n):
    pivots = {}
    for vector in vectors:
        mask = sum((vector[j] & 1) << j for j in range(n))
        original = mask
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in pivots:
                mask ^= pivots[pivot]
            else:
                pivots[pivot] = mask
                break
        if original == 0:
            check(mask == 0)
    return tuple(tuple((mask >> j) & 1 for j in range(n))
                 for _, mask in sorted(pivots.items(), reverse=True))


def scd_interior(space, n):
    rational = [v for v in space if all(x in (0, 1) for x in v)]
    return f4_span(f2_basis(rational, n), n)


def f4_orthogonal(space_basis, n):
    return frozenset(v for v in product(range(4), repeat=n)
                     if all(f4_dot(v, row) == 0 for row in space_basis))


def q_binomial(n: int, k: int, q: int) -> int:
    if k < 0 or k > n:
        return 0
    numerator = denominator = 1
    for i in range(k):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (k - i) - 1
    return numerator // denominator


def grassmann_total(n: int, q: int) -> int:
    return sum(q_binomial(n, k, q) for k in range(n + 1))


def rational_point_free_count(m: int, q: int) -> int:
    # Subspace-lattice Mobius inversion.
    return sum(q_binomial(m, j, q) * ((-1) ** j) *
               (q ** (j * (j - 1) // 2)) * grassmann_total(m - j, q * q)
               for j in range(m + 1))


def verify_scd():
    rows = []
    fingerprints = []
    for n in range(1, 5):
        spaces = all_f4_subspaces(n)
        keys = set(spaces)
        interior = {c: scd_interior(c, n) for c in keys}
        stable = {c for c in keys if interior[c] == c}
        check(len(keys) == grassmann_total(n, 4), f"SCD carrier n={n}")
        check(len(stable) == grassmann_total(n, 2), f"SCD stable count n={n}")

        orthogonal = {c: f4_orthogonal(spaces[c], n) for c in keys}
        transition = {c: orthogonal[interior[c]] for c in keys}
        fibres = Counter(transition.values())
        check(set(fibres) == stable, f"SCD image n={n}")

        for c in keys:
            check(interior[interior[c]] == interior[c], f"SCD interior idempotent n={n}")
            check(transition[transition[c]] == interior[c], f"SCD T2 n={n}")
            check(transition[transition[transition[c]]] == transition[c], f"SCD T3 n={n}")
            depth, period = orbit_signature(c, lambda x: transition[x])
            check(depth == (0 if c in stable else 1), f"SCD depth n={n}")
            check(period in (1, 2), f"SCD period n={n}")

        # The stored canonical RREF has one row per F_4-dimension.
        dimension = {c: len(spaces[c]) for c in keys}
        for target in stable:
            expected = rational_point_free_count(dimension[target], 2)
            check(fibres[target] == expected, f"SCD every-target fibre n={n}")

        mass = sum(q_binomial(n, k, 2) * rational_point_free_count(k, 2)
                   for k in range(n + 1))
        check(mass == len(keys), f"SCD mass n={n}")
        fixed = sum(transition[c] == c for c in keys)
        fibre_by_dimension = tuple((k, rational_point_free_count(k, 2))
                                   for k in range(n + 1))
        rows.append((n, len(keys), len(stable), fixed, fibre_by_dimension))
        fingerprints.append((n, tuple(sorted((tuple(sorted(c)), tuple(sorted(transition[c])))
                                             for c in keys))))
    return rows, digest(fingerprints)


def main():
    rtcd_rows, rtcd_hash = verify_rtcd()
    utas_rows, utas_hash = verify_utas()
    scd_rows, scd_hash = verify_scd()

    print("OPEN_FRESH_P166 INDEPENDENT VERIFIER")
    print("RTCD rows:")
    for row in rtcd_rows:
        print(" ", row)
    print("RTCD fingerprint:", rtcd_hash)
    print("UTAS rows:")
    for row in utas_rows:
        print(" ", row)
    print("UTAS fingerprint:", utas_hash)
    print("SCD rows:")
    for row in scd_rows:
        print(" ", row)
    print("SCD fingerprint:", scd_hash)
    print("assertions:", ASSERTIONS)
    print("decision: KILL_ALL")
    print("external_status: HOLD_EXTERNAL")
    print("status: PASS")


if __name__ == "__main__":
    main()
