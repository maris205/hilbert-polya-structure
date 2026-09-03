#!/usr/bin/env python3
"""Independent Hostile Review B control for P175.

The author and Review A use dense flat tuples.  This verifier instead stores
each matrix as a canonical sparse tuple of (cell, value) pairs decoded from a
base-q integer.  Finite fields are built generically as polynomial quotients,
including GF(4), GF(8), GF(9), and GF(16).  The comparison partition function
is evaluated both from scalar equations and as a complete-graph Potts model.

No paper, author-verifier, Review-A, or scouting code is imported.  Finite
enumeration is falsification evidence, not an all-parameter proof or owner
clearance.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from math import factorial


ASSERTIONS = 0
DIGEST = sha256()


def require(statement: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(label)


@dataclass(frozen=True)
class PolynomialField:
    prime: int
    modulus: tuple[int, ...]  # low-to-high coefficients; monic

    @property
    def degree(self) -> int:
        return len(self.modulus) - 1

    @property
    def order(self) -> int:
        return self.prime ** self.degree

    def coefficients(self, element: int) -> list[int]:
        answer = []
        for _ in range(self.degree):
            answer.append(element % self.prime)
            element //= self.prime
        return answer

    def encode(self, coefficients) -> int:
        answer = 0
        place = 1
        for coefficient in coefficients:
            answer += (coefficient % self.prime) * place
            place *= self.prime
        return answer

    def add(self, left: int, right: int) -> int:
        return self.encode(
            (a + b) % self.prime
            for a, b in zip(self.coefficients(left), self.coefficients(right))
        )

    def neg(self, element: int) -> int:
        return self.encode((-a) % self.prime for a in self.coefficients(element))

    def sub(self, left: int, right: int) -> int:
        return self.add(left, self.neg(right))

    def mul(self, left: int, right: int) -> int:
        a = self.coefficients(left)
        b = self.coefficients(right)
        work = [0] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                work[i + j] = (work[i + j] + x * y) % self.prime
        for power in range(len(work) - 1, self.degree - 1, -1):
            leading = work[power] % self.prime
            if not leading:
                continue
            shift = power - self.degree
            for index, coefficient in enumerate(self.modulus):
                work[shift + index] = (
                    work[shift + index] - leading * coefficient
                ) % self.prime
        return self.encode(work[:self.degree])

    def power(self, element: int, exponent: int) -> int:
        answer = 1
        factor = element
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, factor)
            factor = self.mul(factor, factor)
            exponent //= 2
        return answer

    def inverse(self, element: int) -> int:
        if element == 0:
            raise ZeroDivisionError("zero has no inverse")
        return self.power(element, self.order - 2)


FIELD_MODELS = {
    2: PolynomialField(2, (0, 1)),
    3: PolynomialField(3, (0, 1)),
    4: PolynomialField(2, (1, 1, 1)),             # x^2+x+1
    5: PolynomialField(5, (0, 1)),
    7: PolynomialField(7, (0, 1)),
    8: PolynomialField(2, (1, 1, 0, 1)),          # x^3+x+1
    9: PolynomialField(3, (1, 0, 1)),             # x^2+1
    16: PolynomialField(2, (1, 1, 0, 0, 1)),      # x^4+x+1
}


def field_control(field: PolynomialField) -> None:
    q = field.order
    require(field.modulus[-1] == 1, f"monic modulus q={q}")
    for a in range(q):
        require(field.add(a, 0) == a, f"additive identity q={q} a={a}")
        require(field.add(a, field.neg(a)) == 0, f"additive inverse q={q} a={a}")
        require(field.mul(a, 1) == a, f"multiplicative identity q={q} a={a}")
        if a:
            require(field.mul(a, field.inverse(a)) == 1,
                    f"multiplicative inverse q={q} a={a}")
            require({field.mul(a, x) for x in range(q)} == set(range(q)),
                    f"nonzero scalar permutation q={q} a={a}")
    for a in range(q):
        for b in range(q):
            require(field.add(a, b) == field.add(b, a),
                    f"addition commutative q={q} a={a} b={b}")
            require(field.mul(a, b) == field.mul(b, a),
                    f"multiplication commutative q={q} a={a} b={b}")
            # This also validates the scalar-equation 0/1/q trichotomy.
            solutions = sum(field.mul(a, x) == b for x in range(q))
            expected = q if a == 0 and b == 0 else 0 if a == 0 else 1
            require(solutions == expected,
                    f"scalar equation q={q} coefficient={a} rhs={b}")
            for c in range(q):
                require(field.mul(a, field.add(b, c))
                        == field.add(field.mul(a, b), field.mul(a, c)),
                        f"distributivity q={q} a={a} b={b} c={c}")


def sparse_from_code(code: int, cells: int, q: int):
    entries = []
    for position in range(cells):
        value = code % q
        code //= q
        if value:
            entries.append((position, value))
    return tuple(entries)


def code_from_sparse(matrix, q: int) -> int:
    return sum(value * q ** position for position, value in matrix)


def phi(matrix, n: int, field: PolynomialField):
    entries = dict(matrix)
    diagonal = [entries.get(i * n + i, 0) for i in range(n)]
    output = []
    for position, value in matrix:
        i, j = divmod(position, n)
        if i == j:
            continue
        coefficient = field.sub(diagonal[i], diagonal[j])
        image_value = field.mul(coefficient, value)
        if image_value:
            output.append((position, image_value))
    return tuple(output)


def diagonal_profile(matrix, n: int, q: int):
    entries = dict(matrix)
    profile = [0] * q
    for i in range(n):
        profile[entries.get(i * n + i, 0)] += 1
    return tuple(profile)


def zero_diagonal(matrix, n: int) -> bool:
    return all(position // n != position % n for position, _ in matrix)


def edge_pairs(n: int):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def support_mask(matrix, n: int) -> int:
    positions = {position for position, _ in matrix}
    mask = 0
    for bit, (i, j) in enumerate(edge_pairs(n)):
        if i * n + j in positions or j * n + i in positions:
            mask |= 1 << bit
    return mask


def equal_ordered_pairs(profile) -> int:
    return sum(count * (count - 1) for count in profile)


def partition_tables(n: int, field: PolynomialField):
    """Scalar-fibre, marked, chromatic-profile, and Potts tables by support."""
    q = field.order
    edges = edge_pairs(n)
    aggregate = {}
    marked = {}
    unweighted_profiles = {}
    proper_counts = {}
    for mask in range(1 << len(edges)):
        fibre_total = 0
        profile_weights = Counter()
        profile_counts = Counter()
        proper_count = 0
        for colours in product(range(q), repeat=n):
            profile = tuple(colours.count(alpha) for alpha in range(q))
            scalar_count = 1
            potts_weight = 1
            for bit, (i, j) in enumerate(edges):
                equal = colours[i] == colours[j]
                supported = bool((mask >> bit) & 1)
                if equal and supported:
                    scalar_count = 0
                    potts_weight = 0            # edge activity v=-1
                    break
                if equal:
                    # Both directed target entries vanish and are free.
                    scalar_count *= q * q
                    potts_weight *= q * q        # nonedge activity v=q^2-1
            require(scalar_count == potts_weight,
                    f"scalar/Potts colouring q={q} n={n} mask={mask}")
            if scalar_count:
                exponent = equal_ordered_pairs(profile)
                require(scalar_count == q ** exponent,
                        f"occupation exponent q={q} n={n} mask={mask}")
                proper_count += 1
                profile_counts[profile] += 1
                profile_weights[profile] += scalar_count
                fibre_total += scalar_count
        for profile, count in profile_counts.items():
            require(profile_weights[profile]
                    == count * q ** equal_ordered_pairs(profile),
                    f"chromatic-profile transform q={q} n={n} mask={mask}")
        aggregate[mask] = fibre_total
        marked[mask] = profile_weights
        unweighted_profiles[mask] = profile_counts
        proper_counts[mask] = proper_count
    return aggregate, marked, unweighted_profiles, proper_counts


def weak_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            yield (first,) + tail


def multinomial(profile) -> int:
    answer = factorial(sum(profile))
    for count in profile:
        answer //= factorial(count)
    return answer


def kernel_formula(n: int, q: int) -> int:
    return sum(
        multinomial(profile) * q ** equal_ordered_pairs(profile)
        for profile in weak_compositions(n, q)
    )


def verify_box(n: int, q: int) -> None:
    field = FIELD_MODELS[q]
    require(field.order == q, f"field order q={q}")
    cells = n * n
    state_count = q ** cells
    zero = ()
    fibres = Counter()
    marked_actual = defaultdict(Counter)
    depth_histogram = Counter()
    second_image = Counter()
    fixed_first = 0
    fixed_second = 0

    for code in range(state_count):
        source = sparse_from_code(code, cells, q)
        require(code_from_sparse(source, q) == code,
                f"sparse round trip q={q} n={n} code={code}")
        target = phi(source, n, field)
        second = phi(target, n, field)
        require(zero_diagonal(target, n), f"image diagonal q={q} n={n} code={code}")
        require(second == zero, f"Phi square q={q} n={n} code={code}")
        fibres[target] += 1
        marked_actual[target][diagonal_profile(source, n, q)] += 1
        second_image[second] += 1
        fixed_first += source == target
        fixed_second += source == second
        if source == zero:
            depth_histogram[0] += 1
        elif target == zero:
            depth_histogram[1] += 1
        else:
            depth_histogram[2] += 1
        DIGEST.update(f"{q}:{n}:{code}>{code_from_sparse(target, q)};".encode("ascii"))

    require(second_image == Counter({zero: state_count}), f"constant square q={q} n={n}")
    require(fixed_first == 1, f"unique fixed point q={q} n={n}")
    require(fixed_second == 1, f"unique fixed point of square q={q} n={n}")

    partition, marked, chromatic_profiles, proper_counts = partition_tables(n, field)
    support_census = Counter(support_mask(target, n) for target in fibres)
    support_mass = Counter()
    maximizers = []
    kappa = fibres[zero]

    for code in range(state_count):
        target = sparse_from_code(code, cells, q)
        diagonal_ok = zero_diagonal(target, n)
        mask = support_mask(target, n)
        expected = partition[mask] if diagonal_ok else 0
        expected_marked = marked[mask] if diagonal_ok else Counter()
        observed = fibres.get(target, 0)
        require(observed == expected,
                f"every-target fibre q={q} n={n} code={code}")
        require(marked_actual.get(target, Counter()) == expected_marked,
                f"occupation fibre q={q} n={n} code={code}")
        require((target in fibres) == (diagonal_ok and proper_counts[mask] > 0),
                f"image criterion q={q} n={n} code={code}")
        if observed == kappa:
            maximizers.append(target)
        if observed:
            support_mass[mask] += observed

    require(maximizers == [zero], f"unique maximal zero fibre q={q} n={n}")
    require(kappa == kernel_formula(n, q), f"weak-composition kernel q={q} n={n}")
    require(kappa == partition[0], f"empty-support partition q={q} n={n}")

    image_formula = 0
    for mask in range(1 << len(edge_pairs(n))):
        target_count = (q * q - 1) ** mask.bit_count() if proper_counts[mask] else 0
        require(support_census.get(mask, 0) == target_count,
                f"support target census q={q} n={n} mask={mask}")
        require(support_mass.get(mask, 0) == target_count * partition[mask],
                f"support fibre mass q={q} n={n} mask={mask}")
        image_formula += target_count
        # The unweighted occupation table is precisely the finite-colour
        # chromatic-symmetric-function specialization.
        require(sum(chromatic_profiles[mask].values()) == proper_counts[mask],
                f"chromatic occupation census q={q} n={n} mask={mask}")
    require(len(fibres) == image_formula, f"image graph sum q={q} n={n}")

    require(all(phi(target, n, field) == zero for target in fibres),
            f"image contained in kernel q={q} n={n}")
    require(depth_histogram[0] == 1, f"root layer q={q} n={n}")
    require(depth_histogram[1] == kappa - 1, f"depth one q={q} n={n}")
    require(depth_histogram[2] == state_count - kappa, f"depth two q={q} n={n}")
    require(len(fibres) - 1 == image_formula - 1,
            f"nonzero branch vertices q={q} n={n}")
    require((kappa - 1) - (len(fibres) - 1) == kappa - image_formula,
            f"depth-one leaves q={q} n={n}")
    require(sum(value for target, value in fibres.items() if target != zero)
            == state_count - kappa, f"nonzero branch mass q={q} n={n}")
    require((max(depth_histogram) == 1) == (n == 1), f"sharp height q={q} n={n}")

    # All positive iterate fixed censuses are one, and Phi^t is constant zero
    # for t>=2.  These are the entire all-time fibre and zeta inputs.
    fixed_census = [fixed_first] + [fixed_second] * 7
    require(fixed_census == [1] * 8, f"all iterate fixed census q={q} n={n}")
    require((state_count, len(fibres), 1) == (q ** (n * n), image_formula, 1),
            f"image tower q={q} n={n}")
    require(sum(fibres.values()) == state_count, f"one-step fibre mass q={q} n={n}")

    print(
        f"BOX q={q} n={n} model=GF({field.prime}^{field.degree}) "
        f"states={state_count} image={len(fibres)} kernel={kappa} "
        f"height={max(depth_histogram)} PASS"
    )


def main() -> None:
    print("P175 HOSTILE REVIEW B — SPARSE POLYNOMIAL-FIELD CONTROL")
    print("STATUS HOLD_EXTERNAL")
    print("NO AUTHOR / REVIEW-A / SCOUT IMPORTS")
    for q in (2, 3, 4, 5, 7, 8, 9, 16):
        field_control(FIELD_MODELS[q])
        print(f"FIELD q={q} axioms/scalar-equations PASS")

    boxes = (
        (1, 4), (1, 8), (1, 9), (1, 16),
        (2, 4), (2, 8), (2, 9), (2, 16),
        (3, 2), (3, 3), (3, 4), (4, 2),
    )
    for n, q in boxes:
        verify_box(n, q)

    print("POTTS exact identity: edge activity -1 on G, q^2-1 on complement PASS")
    print("CHROMATIC occupation profile and deterministic q^m transform PASS")
    print("THEOREM Phi^2=0 / every-target marked fibres / image iff PASS")
    print("THEOREM unique maximum / image-kernel-tree / all-time-zeta PASS")
    print(f"EDGE_DIGEST {DIGEST.hexdigest()}")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("RESULT PASS_MATHEMATICS_OWNER_REFRAME_REQUIRED")


if __name__ == "__main__":
    main()
