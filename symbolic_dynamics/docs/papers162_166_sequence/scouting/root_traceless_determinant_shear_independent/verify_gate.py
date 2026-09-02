#!/usr/bin/env python3
"""Independent hostile gate for traceless determinant shear.

No author/scout module is imported.  Finite fields GF(2^m) are constructed
from irreducible polynomials discovered at runtime.  The program tests the
literal matrix map as well as the determinant-coordinate conjugacy.
"""

from collections import Counter
from hashlib import sha256
from itertools import product
from math import prod


ASSERTIONS = 0


def check(statement, label=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(label)


def pdeg(poly):
    return poly.bit_length() - 1


def pmul(left, right):
    answer = 0
    while right:
        if right & 1:
            answer ^= left
        left <<= 1
        right >>= 1
    return answer


def pmod(dividend, divisor):
    d = pdeg(divisor)
    while dividend and pdeg(dividend) >= d:
        dividend ^= divisor << (pdeg(dividend) - d)
    return dividend


def pgcd(left, right):
    while right:
        left, right = right, pmod(left, right)
    return left


def irreducible(poly, degree):
    if pdeg(poly) != degree or not (poly & 1):
        return False
    for d in range(1, degree // 2 + 1):
        for tail in range(1 << d):
            divisor = (1 << d) | tail
            if pmod(poly, divisor) == 0:
                return False
    return True


def first_irreducible(degree):
    for tail in range(1 << degree):
        candidate = (1 << degree) | tail
        if irreducible(candidate, degree):
            return candidate
    raise RuntimeError(("no irreducible", degree))


class BinaryExtension:
    def __init__(self, degree):
        self.m = degree
        self.q = 1 << degree
        self.modulus = first_irreducible(degree)
        self.mask = self.q - 1

    def multiply(self, left, right):
        return pmod(pmul(left, right), self.modulus) & self.mask

    def square(self, value):
        return self.multiply(value, value)

    def power(self, value, exponent):
        answer = 1
        while exponent:
            if exponent & 1:
                answer = self.multiply(answer, value)
            value = self.square(value)
            exponent >>= 1
        return answer

    def square_root(self, value):
        return self.power(value, 1 << (self.m - 1))

    def trace(self, value):
        answer = 0
        term = value
        for _ in range(self.m):
            answer ^= term
            term = self.square(term)
        check(answer in (0, 1), ("trace", self.m, value, answer))
        return answer

    def artin_schreier(self, value):
        return self.square(value) ^ value


def determinant(field, matrix):
    a, b, c = matrix
    return field.square(a) ^ field.multiply(b, c)


def phi(field, matrix):
    a, b, c = matrix
    return (a ^ determinant(field, matrix), b, c)


def phi_power(field, matrix, time):
    for _ in range(time):
        matrix = phi(field, matrix)
    return matrix


def D_power(field, value, time):
    for _ in range(time):
        value = field.artin_schreier(value)
    return value


def R_action(field, value, time):
    answer = 0
    term = value
    for _ in range(time):
        answer ^= term
        term = field.artin_schreier(term)
    return answer


def conjugacy(field, matrix):
    _, b, c = matrix
    return (b, c, determinant(field, matrix))


def inverse_conjugacy(field, triple):
    b, c, det = triple
    a = field.square_root(det ^ field.multiply(b, c))
    return (a, b, c)


def two_primary_size(integer):
    return integer & -integer


def chi_D(degree):
    # Characteristic/minimal polynomial of D=F+I on GF(2^m):
    # chi_D(z)=(z+1)^m+1.
    answer = 1
    for _ in range(degree):
        answer = pmul(answer, 0b11)
    return answer ^ 1


def R_poly(time):
    return (1 << time) - 1


def fixed_kernel_dimension(degree, time):
    if time == 0:
        return degree
    return pdeg(pgcd(R_poly(time), chi_D(degree)))


def divisors(integer):
    return tuple(d for d in range(1, integer + 1) if integer % d == 0)


def mobius(integer):
    primes = 0
    residual = integer
    factor = 2
    while factor * factor <= residual:
        if residual % factor == 0:
            residual //= factor
            primes += 1
            if residual % factor == 0:
                return 0
            while residual % factor == 0:
                residual //= factor
        factor += 1
    if residual > 1:
        primes += 1
    return -1 if primes % 2 else 1


def scalar_period(field, value):
    if value == 0:
        return 1
    current = field.artin_schreier(value)
    period = 1
    while current != value:
        current = field.artin_schreier(current)
        period += 1
        check(period <= field.q, ("period cap", field.m, value))
    return period


def audit_field(m):
    field = BinaryExtension(m)
    q = field.q
    s = two_primary_size(m)
    elements = tuple(range(q))
    states = tuple(product(elements, repeat=3))

    # Runtime-discovered true field and Frobenius checks.
    check(irreducible(field.modulus, m), ("modulus", m))
    for x in elements:
        check(field.power(x, q) == x, ("Frobenius", m, x))
        check(field.square(field.square_root(x)) == x, ("sqrt", m, x))
        if x:
            check(field.power(x, q - 1) == 1, ("multiplicative", m, x))
    for x, y, z in product(elements, repeat=3):
        check(field.multiply(x, y ^ z) == field.multiply(x, y) ^ field.multiply(x, z),
              ("distributive", m, x, y, z))
    for x in elements:
        check(field.trace(field.artin_schreier(x)) == 0, ("AS trace", m, x))

    # The decisive coordinate bijection and literal conjugacy.
    coordinate_digest = []
    for state in states:
        encoded = conjugacy(field, state)
        check(inverse_conjugacy(field, encoded) == state, ("H inverse", m, state))
        left = conjugacy(field, phi(field, state))
        b, c, det = encoded
        right = (b, c, field.artin_schreier(det))
        check(left == right, ("full conjugacy", m, state, left, right))
        coordinate_digest.append((state, encoded, left))
    check(len({conjugacy(field, state) for state in states}) == q ** 3,
          ("H bijection", m))

    stable_image = {D_power(field, x, s) for x in elements}
    check(len(stable_image) == 1 << (m - s), ("stable image", m, stable_image))

    # Literal iterate, semiconjugacy, depth, image, and all-target fibres.
    depth_counts = Counter()
    for state in states:
        d = determinant(field, state)
        depth = next(t for t in range(s + 1) if D_power(field, d, t) in stable_image)
        depth_counts[depth] += 1
        for t in range(s + 3):
            predicted = (state[0] ^ R_action(field, d, t), state[1], state[2])
            actual = phi_power(field, state, t)
            check(actual == predicted, ("matrix iterate", m, state, t))
            check(determinant(field, actual) == D_power(field, d, t),
                  ("det iterate", m, state, t))

    expected_depths = Counter({0: q * q * (1 << (m - s))})
    for depth in range(1, s + 1):
        expected_depths[depth] = q * q * (1 << (m - s + depth - 1))
    check(depth_counts == expected_depths, ("depth histogram", m, depth_counts, expected_depths))
    check(max(depth_counts) == s, ("sharp tail", m))

    image_rows = []
    time_fibres = {}
    for t in range(s + 3):
        fibre_counts = Counter(phi_power(field, source, t) for source in states)
        time_fibres[t] = fibre_counts
        image_determinants = {D_power(field, x, t) for x in elements}
        expected_fibre = 1 << min(t, s)
        check(len(fibre_counts) == q * q * (1 << (m - min(t, s))),
              ("image count", m, t))
        check(set(fibre_counts.values()) == {expected_fibre},
              ("uniform nonempty fibre", m, t))
        for target in states:
            e = determinant(field, target)
            direct = e in image_determinants
            claimed = R_action(field, e, t) in image_determinants
            check(direct == claimed, ("criterion equivalence", m, t, target))
            check((fibre_counts[target] == expected_fibre) == direct,
                  ("all-target fibre", m, t, target))
            if t == 1:
                check(direct == (field.trace(e) == 0), ("trace criterion", m, target))
        image_rows.append((t, len(fibre_counts), expected_fibre))

    # Fixed points, gcd formula, exact periods, and Möbius inversion.
    recurrent_determinants = tuple(sorted(stable_image))
    period_scalar = Counter(scalar_period(field, d) for d in recurrent_determinants)
    maximum_period = max(period_scalar)
    fixed_rows = []
    for k in range(1, maximum_period + 1):
        literal_fixed = sum(phi_power(field, state, k) == state for state in states)
        gcd_fixed = q * q * (1 << fixed_kernel_dimension(m, k))
        direct_fixed = q * q * sum(D_power(field, d, k) == d for d in elements)
        check(literal_fixed == gcd_fixed == direct_fixed, ("fixed formula", m, k))
        exact_mobius = sum(
            mobius(k // divisor)
            * q * q * (1 << fixed_kernel_dimension(m, divisor))
            for divisor in divisors(k)
        )
        exact_observed = q * q * period_scalar[k]
        check(exact_mobius == exact_observed, ("Mobius periods", m, k))
        check(exact_mobius % k == 0, ("cycle integrality", m, k))
        fixed_rows.append((k, literal_fixed, exact_observed, exact_observed // k))

    # Exact t-step fibres over every recurrent target are uniform.  Literal
    # cumulative unions are tested separately because they are not generally
    # equal to a single t-step fibre for a nonfixed cyclic target.
    recurrent_states = tuple(
        state for state in states if determinant(field, state) in stable_image
    )
    for target in recurrent_states:
        for t in range(s + 2):
            check(time_fibres[t][target] == 1 << min(t, s),
                  ("recurrent exact ancestry", m, target, t))

    ancestry_sentinel = None
    if m == 3:
        nonfixed_det = next(d for d in stable_image if field.artin_schreier(d) != d)
        target = inverse_conjugacy(field, (0, 0, nonfixed_det))
        exact_one = {source for source in states if phi_power(field, source, 1) == target}
        cumulative_one = {
            source for source in states
            if source == target or phi_power(field, source, 1) == target
        }
        check(len(exact_one) == 2, "m=3 exact ancestry sentinel")
        check(len(cumulative_one) == 3, "m=3 cumulative ancestry sentinel")
        ancestry_sentinel = (
            "period", scalar_period(field, nonfixed_det),
            "exact_t1", len(exact_one),
            "union_t0_t1", len(cumulative_one),
        )

    digest = sha256(repr(coordinate_digest).encode()).hexdigest()
    row = (
        m,
        q,
        field.modulus,
        len(states),
        s,
        tuple(sorted(depth_counts.items())),
        tuple(image_rows),
        tuple(fixed_rows),
        ancestry_sentinel,
        digest,
    )
    return row


def symbolic_boundary_audit():
    rows = []
    for m in range(1, 257):
        s = two_primary_size(m)
        chi = chi_D(m)
        check(pdeg(chi) == m, ("chi degree", m))
        # Exact z-adic order s.
        check(chi & ((1 << s) - 1) == 0, ("z^s divides", m, s))
        check((chi >> s) & 1, ("z^(s+1) does not divide", m, s))
        for k in range(1, 2 * m + 2):
            dimension = fixed_kernel_dimension(m, k)
            check(0 <= dimension <= m, ("gcd dimension", m, k, dimension))
        rows.append((m, s, pdeg(chi)))
    return sha256(repr(rows).encode()).hexdigest()


def main():
    rows = [audit_field(m) for m in range(1, 7)]
    symbolic_digest = symbolic_boundary_audit()
    print("P166 TRACELESS DETERMINANT SHEAR — INDEPENDENT HOSTILE GATE")
    print("lifecycle=HOLD_EXTERNAL")
    print("implementation=runtime_irreducible_fields_no_author_import")
    print("DECISIVE_CONJUGACY H(A)=(b,c,det(A)); H Phi=(id,id,D) H")
    print("D(x)=x^2+x")
    print("columns=m,q,modulus,states,s,depths,images,fixed_period_rows,ancestry_sentinel,digest")
    for row in rows:
        print("BOX", row)
    print("symbolic_m_1_256_sha256=" + symbolic_digest)
    print("assertions=" + str(ASSERTIONS))
    print("FORMULAS_PASS iterate/depth/image/fibre/trace/fixed/Mobius")
    print("CUMULATIVE_WARNING nonfixed recurrent target union differs from exact t-fibre")
    print("DECISION KILL_CONJUGATE_TO_CLASSICAL_ARTIN_SCHREIER_LINEAR_MAP")
    print("EXTERNAL HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
