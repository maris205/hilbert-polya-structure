#!/usr/bin/env python3
"""Independent hostile checks for P180 over prime and extension fields.

The author control only used symmetric dot products over prime fields.  This
reviewer builds polynomial-basis finite fields (including characteristic two)
and literal nonsymmetric invertible Gram matrices.  It imports no author or
scouting code and checks t=0 separately from the positive-time formula.
"""

from collections import Counter
from itertools import product
from math import gcd


class Audit:
    def __init__(self):
        self.assertions = 0

    def equal(self, left, right, label=""):
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")

    def true(self, value, label=""):
        self.assertions += 1
        if not value:
            raise AssertionError(label or "assertion failed")


class FiniteField:
    """Small polynomial-basis GF(p^k), with integer-coded elements."""

    def __init__(self, p, modulus, name):
        self.p = p
        self.modulus = tuple(coefficient % p for coefficient in modulus)
        self.k = len(modulus) - 1
        self.q = p**self.k
        self.name = name
        if self.modulus[-1] != 1:
            raise ValueError("modulus must be monic")

    def digits(self, value):
        out = []
        for _ in range(self.k):
            out.append(value % self.p)
            value //= self.p
        return out

    def encode(self, coefficients):
        value = 0
        place = 1
        for coefficient in coefficients[: self.k]:
            value += (coefficient % self.p) * place
            place *= self.p
        return value

    def add(self, left, right):
        return self.encode([a + b for a, b in zip(self.digits(left), self.digits(right))])

    def neg(self, value):
        return self.encode([-a for a in self.digits(value)])

    def mul(self, left, right):
        a = self.digits(left)
        b = self.digits(right)
        raw = [0] * (2 * self.k - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                raw[i + j] = (raw[i + j] + x * y) % self.p
        for degree in range(len(raw) - 1, self.k - 1, -1):
            coefficient = raw[degree] % self.p
            if coefficient:
                shift = degree - self.k
                for j in range(self.k):
                    raw[shift + j] = (raw[shift + j] - coefficient * self.modulus[j]) % self.p
        return self.encode(raw)

    def power(self, base, exponent):
        answer = 1
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, base)
            base = self.mul(base, base)
            exponent >>= 1
        return answer

    def scale_vector(self, scalar, vector):
        return tuple(self.mul(scalar, value) for value in vector)


def vectors(field, m):
    return tuple(product(range(field.q), repeat=m))


def bilinear(field, matrix, u, v):
    answer = 0
    for i in range(len(u)):
        for j in range(len(v)):
            answer = field.add(answer, field.mul(field.mul(u[i], matrix[i][j]), v[j]))
    return answer


def phi(field, matrix, state):
    u, v = state
    c = bilinear(field, matrix, u, v)
    return field.scale_vector(c, u), field.scale_vector(c, v)


def closed_phi(field, matrix, state, t):
    u, v = state
    c = bilinear(field, matrix, u, v)
    scale = field.power(c, (3**t - 1) // 2)
    return field.scale_vector(scale, u), field.scale_vector(scale, v)


def multiplicative_order(field, value):
    if value == 0:
        raise ValueError("zero has no multiplicative order")
    cursor = 1
    for order in range(1, field.q):
        cursor = field.mul(cursor, value)
        if cursor == 1:
            return order
    raise AssertionError("field order not found")


def residue_order(base, modulus):
    cursor = 1
    for order in range(1, modulus + 1):
        cursor = cursor * base % modulus
        if cursor == 1:
            return order
    raise AssertionError("residue order not found")


def orbit_signature(start, transition):
    positions = {}
    state = start
    while state not in positions:
        positions[state] = len(positions)
        state = transition[state]
    return positions[state], len(positions) - positions[state]


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix)))


def main():
    audit = Audit()
    fields = {
        "F2": FiniteField(2, (0, 1), "F2"),
        "F3": FiniteField(3, (0, 1), "F3"),
        "F4": FiniteField(2, (1, 1, 1), "F4"),
        "F5": FiniteField(5, (0, 1), "F5"),
        "F7": FiniteField(7, (0, 1), "F7"),
        "F8": FiniteField(2, (1, 1, 0, 1), "F8"),
        "F9": FiniteField(3, (1, 0, 1), "F9"),
        "F19": FiniteField(19, (0, 1), "F19"),
    }

    # alpha is integer p in this encoding.  Upper triangular matrices with
    # diagonal one are invertible and are nonsymmetric when alpha != 0.
    cases = [
        ("F2", ((1,),)),
        ("F2", ((1, 1), (0, 1))),
        ("F3", ((1,),)),
        ("F3", ((1, 1), (0, 1))),
        ("F4", ((1,),)),
        ("F4", ((1, 2), (0, 1))),
        ("F5", ((1, 1), (0, 1))),
        ("F7", ((1,),)),
        ("F8", ((1,),)),
        ("F8", ((1, 2), (0, 1))),
        ("F9", ((1,),)),
        ("F9", ((1, 3), (0, 1))),
        ("F19", ((1,),)),
    ]

    # Field axioms most relevant to the formulas, including extension fields.
    for field in fields.values():
        for value in range(field.q):
            audit.equal(field.add(value, 0), value, f"additive identity {field.name}")
            audit.equal(field.add(value, field.neg(value)), 0, f"additive inverse {field.name}")
            audit.equal(field.mul(value, 1), value, f"multiplicative identity {field.name}")
            if value:
                audit.equal(field.mul(value, field.power(value, field.q - 2)), 1,
                            f"field inverse {field.name}")

    rows = []
    saw_nonsymmetric = False
    saw_characteristic_two = False
    saw_extension = False
    saw_A_zero = False
    saw_A_two = False

    for field_name, matrix in cases:
        field = fields[field_name]
        m = len(matrix)
        vecs = vectors(field, m)
        states = tuple((u, v) for u in vecs for v in vecs)
        zero_vector = (0,) * m
        zero = (zero_vector, zero_vector)
        nonsymmetric = matrix != transpose(matrix)
        saw_nonsymmetric |= nonsymmetric
        saw_characteristic_two |= field.p == 2
        saw_extension |= field.k > 1

        # Two-sided nondegeneracy is checked literally; this makes no symmetry
        # assumption and guards the exact hypothesis used by the level proof.
        for u in vecs:
            if u != zero_vector:
                audit.true(any(bilinear(field, matrix, u, v) != 0 for v in vecs),
                           f"left nondegenerate {field.name},m={m}")
        for v in vecs:
            if v != zero_vector:
                audit.true(any(bilinear(field, matrix, u, v) != 0 for u in vecs),
                           f"right nondegenerate {field.name},m={m}")

        q = field.q
        Q = q ** (m - 1) * (q**m - 1)
        Z = q ** (2 * m - 1) + q**m - q ** (m - 1)
        levels = Counter(bilinear(field, matrix, u, v) for u, v in states)
        audit.equal(levels[0], Z, f"null cone {field.name},m={m}")
        for c in range(1, q):
            audit.equal(levels[c], Q, f"nonzero level {field.name},m={m},c={c}")

        images = [list(states)]
        for _ in range(5):
            images.append([phi(field, matrix, state) for state in images[-1]])

        for t in range(0, 6):
            for state, observed in zip(states, images[t]):
                audit.equal(observed, closed_phi(field, matrix, state, t),
                            f"closed iterate {field.name},m={m},t={t}")
                c = bilinear(field, matrix, state[0], state[1])
                audit.equal(bilinear(field, matrix, observed[0], observed[1]),
                            field.power(c, 3**t),
                            f"scalar cube {field.name},m={m},t={t}")

        transition = {state: images[1][i] for i, state in enumerate(states)}
        tails = Counter()
        for state in states:
            tail, period = orbit_signature(state, transition)
            c = bilinear(field, matrix, state[0], state[1])
            if state == zero:
                expected = (0, 1)
            elif c == 0:
                expected = (1, 1)
            else:
                order = multiplicative_order(field, c)
                a = 0
                s = order
                while s % 3 == 0:
                    a += 1
                    s //= 3
                expected = (a, residue_order(3, 2 * s))
            audit.equal((tail, period), expected,
                        f"tail/period {field.name},m={m},state={state}")
            tails[tail] += 1

        A = 0
        h = q - 1
        while h % 3 == 0:
            A += 1
            h //= 3
        saw_A_zero |= A == 0
        saw_A_two |= A >= 2
        predicted_tails = Counter({0: 1 + h * Q, 1: Z - 1})
        for a in range(1, A + 1):
            predicted_tails[a] += 2 * 3 ** (a - 1) * h * Q
        audit.equal(tails, +predicted_tails, f"tail census {field.name},m={m}")
        audit.equal(max(tails), max(1, A), f"sharp tail {field.name},m={m}")

        # t=0 is the identity fibre and is intentionally separate from the
        # manuscript's positive-time Z/g_t formula.
        fibres_zero = Counter(images[0])
        audit.equal(len(fibres_zero), len(states), f"t=0 image {field.name},m={m}")
        for target in states:
            audit.equal(fibres_zero[target], 1, f"t=0 singleton fibre {field.name},m={m}")

        for t in range(1, 6):
            fibres = Counter(images[t])
            g_t = gcd(3**t, q - 1)
            for target in states:
                d = bilinear(field, matrix, target[0], target[1])
                if target == zero:
                    expected = Z
                elif d == 0:
                    expected = 0
                elif field.power(d, (q - 1) // g_t) == 1:
                    expected = g_t
                else:
                    expected = 0
                audit.equal(fibres[target], expected,
                            f"all-target fibre {field.name},m={m},t={t}")
            audit.equal(len(fibres), 1 + (q - 1) * Q // g_t,
                        f"time image size {field.name},m={m},t={t}")
            audit.equal(fibres[zero], Z, f"zero fibre {field.name},m={m},t={t}")
            audit.true(Z > g_t, f"strict maximum inequality {field.name},m={m},t={t}")
            audit.equal({target for target, size in fibres.items() if size == max(fibres.values())},
                        {zero}, f"unique maximum {field.name},m={m},t={t}")

        g = gcd(3, q - 1)
        one_step = Counter(images[1])
        audit.equal(len(one_step), 1 + (q - 1) * Q // g,
                    f"one-step image {field.name},m={m}")
        for target, size in one_step.items():
            audit.equal(size, Z if target == zero else g,
                        f"one-step fibre uniformity {field.name},m={m}")

        rows.append((field.name, q, m, "nonsym" if nonsymmetric else "sym",
                     field.p, A, Z, Q, tuple(sorted(tails.items())), len(one_step)))

    audit.true(saw_nonsymmetric, "nonsymmetric form coverage")
    audit.true(saw_characteristic_two, "characteristic-two coverage")
    audit.true(saw_extension, "nonprime field coverage")
    audit.true(saw_A_zero, "A=0 coverage")
    audit.true(saw_A_two, "A>=2 coverage")

    print("P180_REVIEW_A_EXTENSION_FIELD_NONSYMMETRIC_AUDIT")
    for name, q, m, symmetry, characteristic, A, Z, Q, tails, image_size in rows:
        print(f"field={name} q={q} char={characteristic} m={m} form={symmetry} A={A} Z={Z} Q={Q} tails={tails} image={image_size}")
    print("FORM_SCOPE=nonsymmetric_two_sided_nondegenerate_PASS")
    print("BOUNDARIES=t0_identity;A0;A_ge_2;characteristic_2;extension_fields_PASS")
    print("POSITIVE_TIME_FIBRES=t1..5_PASS;zero_unique_max_each_time_PASS")
    print(f"ASSERTIONS={audit.assertions}")
    print("RESULT=PASS")
    print("EXTERNAL_STATUS=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
