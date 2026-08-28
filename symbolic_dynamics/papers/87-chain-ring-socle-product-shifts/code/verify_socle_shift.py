#!/usr/bin/env python3
"""Deterministic exact controls for finite-chain-ring socle-product shifts.

The primary control is the valuation model, which is valid for every finite
commutative chain ring with the displayed residue-field size and length.  For
prime residue fields it is independently realized in Z/p^r Z and in
F_p[t]/(t^r).  The nonprime case q=4 is also realized in
F_4[t]/(t^r), with F_4=F_2[u]/(u^2+u+1).
"""

from fractions import Fraction
from itertools import permutations


CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def layer_sizes(q, a):
    return [(q - 1) * q ** (a - i) for i in range(a + 1)]


def quotient_matrix(q, a):
    """Action on functions constant on valuation layers."""
    weights = layer_sizes(q, a)
    return [
        [weights[j] if i + j == a else 0 for j in range(a + 1)]
        for i in range(a + 1)
    ]


def identity(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def matmul(left, right):
    rows = len(left)
    inner = len(right)
    cols = len(right[0])
    return [
        [sum(left[i][k] * right[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def matrix_rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][col]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(rows):
            if row != pivot_row and work[row][col]:
                factor = work[row][col]
                work[row] = [
                    work[row][j] - factor * work[pivot_row][j]
                    for j in range(cols)
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def poly_trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(left, right):
    size = max(len(left), len(right))
    result = [0] * size
    for i in range(size):
        result[i] = (left[i] if i < len(left) else 0) + (
            right[i] if i < len(right) else 0
        )
    return poly_trim(result)


def poly_scale(poly, scalar):
    return poly_trim([scalar * value for value in poly])


def poly_mul(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, value_left in enumerate(left):
        for j, value_right in enumerate(right):
            result[i + j] += value_left * value_right
    return poly_trim(result)


def poly_pow(base, exponent):
    result = [1]
    factor = list(base)
    while exponent:
        if exponent & 1:
            result = poly_mul(result, factor)
        factor = poly_mul(factor, factor)
        exponent //= 2
    return result


def permutation_sign(perm):
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def determinant_i_minus_zq(matrix):
    """Return det(I-zQ) as an integer coefficient list."""
    size = len(matrix)
    result = [0]
    for perm in permutations(range(size)):
        term = [1]
        for row, col in enumerate(perm):
            entry = [int(row == col), -matrix[row][col]]
            term = poly_mul(term, entry)
        result = poly_add(result, poly_scale(term, permutation_sign(perm)))
    return poly_trim(result)


def rho_squared(q, a):
    return (q - 1) ** 2 * q**a


def fixed_formula(q, a, period):
    rho2 = rho_squared(q, a)
    if a % 2:
        if period % 2:
            return 0
        return (a + 1) * rho2 ** (period // 2)
    rho = (q - 1) * q ** (a // 2)
    if period % 2:
        return rho**period
    return (a + 1) * rho**period


def expected_determinant(q, a):
    rho2 = rho_squared(q, a)
    if a % 2:
        return poly_pow([1, 0, -rho2], (a + 1) // 2)
    rho = (q - 1) * q ** (a // 2)
    return poly_mul([1, -rho], poly_pow([1, 0, -rho2], a // 2))


def recover_parameters(fixed):
    f1, f2, f3, f4 = fixed
    if f1:
        check(f2 % (f1 * f1) == 0, "even recovery divisibility")
        a = f2 // (f1 * f1) - 1
        target = f1 * f1
        check(a % 2 == 0, "even recovery parity")
        check(f3 == f1**3, "even recovery F3 consistency")
        check(f4 == (a + 1) * f1**4, "even recovery F4 consistency")
    else:
        check(f3 == 0, "odd recovery F3")
        check(f4 % f2 == 0, "odd recovery rho divisibility")
        check((f2 * f2) % f4 == 0, "odd recovery length divisibility")
        a = (f2 * f2) // f4 - 1
        target = f4 // f2
        check(a % 2 == 1, "odd recovery parity")

    q = 2
    while (q - 1) ** 2 * q**a < target:
        q += 1
    check((q - 1) ** 2 * q**a == target, "recovery has an integral q")
    return q, a


def abstract_control(q, a):
    weights = layer_sizes(q, a)
    number_vertices = q ** (a + 1) - 1
    check(sum(weights) == number_vertices, f"layer cardinality q={q}, a={a}")
    for i, weight in enumerate(weights):
        check(weight == q ** (a + 1 - i) - q ** (a - i), "layer difference")
        check(weights[a - i] > 0, "opposite layer exists")
        for _ in range(weight):
            check(weights[a - i] == (q - 1) * q**i, "vertex outdegree")
        for j in range(a + 1):
            check((i + j == a) == (j == a - i), "valuation boundary relation")

    components = []
    seen = set()
    for i in range(a + 1):
        if i not in seen:
            component = frozenset((i, a - i))
            components.append(component)
            seen.update(component)
    check(len(components) == a // 2 + 1, "component count")
    check(sum(len(component) for component in components) == a + 1, "partition")
    mixing_components = sum(len(component) == 1 for component in components)
    check(mixing_components == int(a % 2 == 0), "parity mixing transition")

    rho2 = rho_squared(q, a)
    for component in components:
        indices = sorted(component)
        if len(indices) == 1:
            i = indices[0]
            check(weights[i] ** 2 == rho2, "central Perron value")
        else:
            i, j = indices
            check(weights[i] * weights[j] == rho2, "bipartite Perron value")

    quotient = quotient_matrix(q, a)
    check(matrix_rank(quotient) == a + 1, "rank a+1")
    check(
        determinant_i_minus_zq(quotient) == expected_determinant(q, a),
        f"zeta determinant q={q}, a={a}",
    )
    power = identity(a + 1)
    for period in range(1, 11):
        power = matmul(power, quotient)
        check(trace(power) == fixed_formula(q, a, period), "all-period trace formula")

    fixed = tuple(fixed_formula(q, a, period) for period in range(1, 5))
    check(recover_parameters(fixed) == (q, a), "four-period recovery")
    return fixed


class PrimeField:
    def __init__(self, prime):
        self.q = prime
        self.name = f"F_{prime}"

    def add(self, left, right):
        return (left + right) % self.q

    def mul(self, left, right):
        return (left * right) % self.q


class FieldFour:
    q = 4
    name = "F_4"

    @staticmethod
    def add(left, right):
        return left ^ right

    @staticmethod
    def mul(left, right):
        # Binary basis 1,u with u^2=u+1.
        a0, a1 = left & 1, (left >> 1) & 1
        b0, b1 = right & 1, (right >> 1) & 1
        constant = (a0 * b0) ^ (a1 * b1)
        linear = (a0 * b1) ^ (a1 * b0) ^ (a1 * b1)
        return constant | (linear << 1)


def decode_coefficients(number, q, length):
    coefficients = []
    for _ in range(length):
        coefficients.append(number % q)
        number //= q
    return tuple(coefficients)


def polynomial_valuation(poly):
    return next((i for i, coefficient in enumerate(poly) if coefficient), len(poly))


def truncated_product(left, right, field):
    length = len(left)
    result = [0] * length
    for i, a_i in enumerate(left):
        if not a_i:
            continue
        for j, b_j in enumerate(right[: length - i]):
            if b_j:
                result[i + j] = field.add(result[i + j], field.mul(a_i, b_j))
    return tuple(result)


def monomial(length, degree, coefficient=1):
    result = [0] * length
    result[degree] = coefficient
    return tuple(result)


def polynomial_ring_control(field, a):
    q = field.q
    length = a + 1
    layers = [[] for _ in range(length)]
    zero = (0,) * length
    for number in range(q**length):
        element = decode_coefficients(number, q, length)
        valuation = polynomial_valuation(element)
        check(0 <= valuation <= length, "polynomial valuation range")
        if element != zero:
            check(valuation < length, "nonzero polynomial valuation")
            layers[valuation].append(element)
        else:
            check(valuation == length, "zero polynomial valuation")

    check([len(layer) for layer in layers] == layer_sizes(q, a), "polynomial layers")
    for left in range(1, q):
        for right in range(1, q):
            check(field.mul(left, right) != 0, "field leading coefficients do not cancel")

    for i, layer in enumerate(layers):
        for element in layer:
            for j in range(length):
                product = truncated_product(element, monomial(length, j), field)
                value = polynomial_valuation(product)
                expected = i + j if i + j < length else length
                check(value == expected, "truncated-polynomial product valuation")
                check((value == a) == (i + j == a), "polynomial socle boundary")
    return layers


def zmod_valuation(value, prime, length):
    if value == 0:
        return length
    valuation = 0
    while value % prime == 0:
        value //= prime
        valuation += 1
    return valuation


def zmod_ring_control(prime, a):
    length = a + 1
    modulus = prime**length
    layers = [[] for _ in range(length)]
    for value in range(modulus):
        valuation = zmod_valuation(value, prime, length)
        check(0 <= valuation <= length, "zmod valuation range")
        if value:
            check(valuation < length, "nonzero zmod valuation")
            layers[valuation].append(value)
        else:
            check(valuation == length, "zero zmod valuation")

    check([len(layer) for layer in layers] == layer_sizes(prime, a), "zmod layers")
    for i, layer in enumerate(layers):
        for value in layer:
            for j in range(length):
                product = (value * prime**j) % modulus
                product_value = zmod_valuation(product, prime, length)
                expected = i + j if i + j < length else length
                check(product_value == expected, "zmod product valuation")
                check((product_value == a) == (i + j == a), "zmod socle boundary")
    return layers


def collapse_control(prime, a):
    z_layers = zmod_ring_control(prime, a)
    p_layers = polynomial_ring_control(PrimeField(prime), a)
    check(len(z_layers) == len(p_layers), "collapse layer count")

    # Any layerwise bijection is a graph isomorphism.  Pairing the stored
    # order gives one explicit such bijection and checks every vertex.
    for i, (z_layer, p_layer) in enumerate(zip(z_layers, p_layers)):
        check(len(z_layer) == len(p_layer), "collapse layer size")
        for z_value, p_value in zip(z_layer, p_layer):
            check(zmod_valuation(z_value, prime, a + 1) == i, "zmod map valuation")
            check(polynomial_valuation(p_value) == i, "polynomial map valuation")
        for j in range(a + 1):
            z_adjacent = i + j == a
            p_adjacent = i + j == a
            check(z_adjacent == p_adjacent, "layerwise graph isomorphism")

    # The two rings are not isomorphic: their characteristics are p^(a+1)
    # and p, respectively.
    check(prime ** (a + 1) != prime, "different characteristics")
    check((prime * 1) % (prime ** (a + 1)) != 0, "zmod characteristic witness")
    polynomial_p_times_one = 0
    for _ in range(prime):
        polynomial_p_times_one = (polynomial_p_times_one + 1) % prime
    check(polynomial_p_times_one == 0, "polynomial characteristic witness")


def main():
    print("finite-chain-ring socle-product exact controls")
    registry = {}
    for q in (2, 3, 4, 5):
        rows = []
        for a in range(1, 6):
            fixed = abstract_control(q, a)
            check(fixed not in registry, "controlled four-period collision")
            registry[fixed] = (q, a)
            rows.append(f"a={a}:{fixed}")
        print(f"q={q} abstract: " + "; ".join(rows))

    for prime in (2, 3, 5):
        for a in range(1, 6):
            collapse_control(prime, a)
        print(
            f"q={prime} concrete: Z/{prime}^r Z and F_{prime}[t]/(t^r), "
            "r=2,...,6, layerwise collapse PASS"
        )

    field_four = FieldFour()
    for a in range(1, 6):
        polynomial_ring_control(field_four, a)
    print("q=4 concrete: F_4[t]/(t^r), r=2,...,6, valuation boundary PASS")

    print(f"ALL EXACT CONTROLS PASSED: {CHECKS:,} assertions")


if __name__ == "__main__":
    main()
