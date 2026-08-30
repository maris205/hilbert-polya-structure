#!/usr/bin/env python3
"""Independent exact verifier for the transpose self-commutator theorem."""

from collections import Counter
from itertools import product


ASSERTIONS = 0


def check(statement, context):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(context)


class Field:
    """Tiny polynomial-basis finite field; modulus is low-to-high and monic."""

    def __init__(self, p, modulus):
        self.p = p
        self.modulus = tuple(modulus)
        self.degree = len(modulus) - 1
        self.q = p ** self.degree

    def digits(self, value, length=None):
        length = self.degree if length is None else length
        out = []
        for _ in range(length):
            out.append(value % self.p)
            value //= self.p
        return out

    def encode(self, coeffs):
        value = 0
        place = 1
        for coeff in coeffs[: self.degree]:
            value += (coeff % self.p) * place
            place *= self.p
        return value

    def add(self, x, y):
        return self.encode(
            [(a + b) % self.p for a, b in zip(self.digits(x), self.digits(y))]
        )

    def neg(self, x):
        return self.encode([(-a) % self.p for a in self.digits(x)])

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        left = self.digits(x)
        right = self.digits(y)
        coeffs = [0] * (2 * self.degree - 1)
        for i, a in enumerate(left):
            for j, b in enumerate(right):
                coeffs[i + j] = (coeffs[i + j] + a * b) % self.p
        for power in range(len(coeffs) - 1, self.degree - 1, -1):
            lead = coeffs[power] % self.p
            if not lead:
                continue
            shift = power - self.degree
            for j in range(self.degree):
                coeffs[shift + j] = (
                    coeffs[shift + j] - lead * self.modulus[j]
                ) % self.p
            coeffs[power] = 0
        return self.encode(coeffs)


def transpose(matrix):
    n = len(matrix)
    return tuple(tuple(matrix[j][i] for j in range(n)) for i in range(n))


def multiply(field, left, right):
    n = len(left)
    return tuple(
        tuple(
            sum_field(field, (field.mul(left[i][k], right[k][j]) for k in range(n)))
            for j in range(n)
        )
        for i in range(n)
    )


def sum_field(field, values):
    total = 0
    for value in values:
        total = field.add(total, value)
    return total


def delta(field, matrix):
    star = transpose(matrix)
    left = multiply(field, matrix, star)
    right = multiply(field, star, matrix)
    n = len(matrix)
    return tuple(
        tuple(field.sub(left[i][j], right[i][j]) for j in range(n))
        for i in range(n)
    )


def matrices(q, n):
    for entries in product(range(q), repeat=n * n):
        yield tuple(tuple(entries[i * n + j] for j in range(n)) for i in range(n))


def audit_two_by_two(field, label):
    q = field.q
    zero = ((0, 0), (0, 0))
    fibres = Counter()
    depth_histogram = Counter()
    for matrix in matrices(q, 2):
        image = delta(field, matrix)
        fibres[image] += 1
        check(delta(field, image) == zero, (label, matrix, "second iterate"))
        check(image == transpose(image), (label, matrix, "self-adjoint image"))
        depth = 0 if matrix == zero else 1 if image == zero else 2
        depth_histogram[depth] += 1
    if field.p == 2:
        expected_image = q * q - q + 1
        expected_zero = q ** 3
        expected_nonzero = q ** 2
        layers = (1, q ** 3 - 1, q ** 4 - q ** 3)
    else:
        expected_image = q * q
        expected_zero = q ** 3 + q * q - q
        expected_nonzero = q * (q - 1)
        layers = (1, q ** 3 + q * q - q - 1, q ** 4 - q ** 3 - q * q + q)
    check(len(fibres) == expected_image, (label, "image", len(fibres)))
    check(fibres[zero] == expected_zero, (label, "zero fibre", fibres[zero]))
    check(
        all(size == expected_nonzero for point, size in fibres.items() if point != zero),
        (label, "nonzero fibres"),
    )
    check(sum(fibres.values()) == q ** 4, (label, "mass"))
    check(tuple(depth_histogram[i] for i in range(3)) == layers, (label, "literal layers", depth_histogram))
    image_set = set(fibres)
    kernel_set = {matrix for matrix in matrices(q, 2) if delta(field, matrix) == zero}
    check(len(kernel_set) == expected_zero, (label, "kernel size"))
    check(image_set <= kernel_set, (label, "image inside kernel"))
    check(len(kernel_set - image_set) == expected_zero - expected_image, (label, "kernel outside image"))
    return expected_image, expected_zero, expected_nonzero, layers


def audit_universal(field, label, n):
    zero = tuple(tuple(0 for _ in range(n)) for _ in range(n))
    count = 0
    for matrix in matrices(field.q, n):
        image = delta(field, matrix)
        check(image == transpose(image), (label, n, "self-adjoint"))
        check(delta(field, image) == zero, (label, n, "square zero"))
        count += 1
    return count


def main():
    fields = (
        ("F2", Field(2, (0, 1))),
        ("F3", Field(3, (0, 1))),
        ("F4", Field(2, (1, 1, 1))),
        ("F5", Field(5, (0, 1))),
        ("F7", Field(7, (0, 1))),
        ("F8", Field(2, (1, 1, 0, 1))),
        ("F9", Field(3, (1, 0, 1))),
    )
    rows = []
    for label, field in fields:
        rows.append((label, field.q, *audit_two_by_two(field, label)))
    universal = []
    for label, field in fields[:2]:
        universal.append((label, 3, audit_universal(field, label, 3)))
    print("transpose self-commutator verifier: PASS")
    print(f"assertions={ASSERTIONS}")
    print("field q image zero_fibre nonzero_fibre depth_layers")
    for row in rows:
        print(*row)
    print("universal_M3", universal)


if __name__ == "__main__":
    main()
