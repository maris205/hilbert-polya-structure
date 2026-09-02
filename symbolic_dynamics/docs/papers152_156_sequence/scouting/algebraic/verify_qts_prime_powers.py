#!/usr/bin/env python3
"""Independent exact replay of QTS over nonprime odd prime powers.

No finite-field package and no code from verify_algebraic_scout.py is used.
Each quadratic extension F_{q^2} is built as a polynomial quotient over F_p
using the lexicographically first monic irreducible polynomial of degree 2e.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from math import gcd, lcm


class AuditFailure(RuntimeError):
    pass


class Checks:
    def __init__(self) -> None:
        self.count = 0

    def require(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AuditFailure(label)

    def equal(self, left, right, label: str) -> None:
        self.require(left == right, f"{label}: {left!r} != {right!r}")


def digits(value: int, p: int, length: int) -> list[int]:
    out = []
    for _ in range(length):
        out.append(value % p)
        value //= p
    return out


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_remainder(poly: list[int], divisor: list[int], p: int) -> list[int]:
    rem = trim([coefficient % p for coefficient in poly])
    degree = len(divisor) - 1
    while len(rem) - 1 >= degree and rem != [0]:
        shift = len(rem) - 1 - degree
        lead = rem[-1]
        for index, coefficient in enumerate(divisor):
            rem[index + shift] = (rem[index + shift] - lead * coefficient) % p
        trim(rem)
    return rem


def is_irreducible(poly: list[int], p: int) -> bool:
    degree = len(poly) - 1
    if degree <= 0 or poly[-1] % p != 1 or poly[0] % p == 0:
        return False
    for factor_degree in range(1, degree // 2 + 1):
        for code in range(p**factor_degree):
            factor = digits(code, p, factor_degree) + [1]
            if poly_remainder(poly, factor, p) == [0]:
                return False
    return True


def first_irreducible(p: int, degree: int) -> list[int]:
    for code in range(1, p**degree):
        coefficients = digits(code, p, degree)
        if coefficients[0] == 0:
            continue
        candidate = coefficients + [1]
        if is_irreducible(candidate, p):
            return candidate
    raise AuditFailure(f"no irreducible polynomial for p={p}, degree={degree}")


class FiniteField:
    def __init__(self, p: int, degree: int, modulus: list[int]) -> None:
        self.p = p
        self.degree = degree
        self.modulus = modulus
        self.size = p**degree
        self.vectors = [tuple(digits(value, p, degree)) for value in range(self.size)]

    def encode(self, coefficients) -> int:
        value = 0
        place = 1
        for coefficient in coefficients:
            value += (coefficient % self.p) * place
            place *= self.p
        return value

    def scalar(self, value: int) -> int:
        return value % self.p

    def add(self, left: int, right: int) -> int:
        return self.encode(
            (a + b) % self.p for a, b in zip(self.vectors[left], self.vectors[right])
        )

    def neg(self, value: int) -> int:
        return self.encode((-a) % self.p for a in self.vectors[value])

    def sub(self, left: int, right: int) -> int:
        return self.add(left, self.neg(right))

    def mul(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0
        product = [0] * (2 * self.degree - 1)
        for i, a in enumerate(self.vectors[left]):
            for j, b in enumerate(self.vectors[right]):
                product[i + j] = (product[i + j] + a * b) % self.p
        for power in range(len(product) - 1, self.degree - 1, -1):
            lead = product[power] % self.p
            if lead:
                shift = power - self.degree
                for j in range(self.degree):
                    product[shift + j] = (
                        product[shift + j] - lead * self.modulus[j]
                    ) % self.p
        return self.encode(product[: self.degree])

    def pow(self, base: int, exponent: int) -> int:
        if exponent < 0:
            return self.pow(self.inv(base), -exponent)
        result = 1
        while exponent:
            if exponent & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            exponent >>= 1
        return result

    def inv(self, value: int) -> int:
        if value == 0:
            raise ZeroDivisionError("zero has no inverse")
        return self.pow(value, self.size - 2)

    def div(self, numerator: int, denominator: int) -> int:
        return self.mul(numerator, self.inv(denominator))


def multiplicative_order(field: FiniteField, value: int, bound: int) -> int:
    if value == 0:
        raise AuditFailure("multiplicative order requested at zero")
    current = 1
    for order in range(1, bound + 1):
        current = field.mul(current, value)
        if current == 1:
            return order
    raise AuditFailure(f"order of {value} did not divide {bound}")


def quadratic_character(field: FiniteField, value: int, q: int) -> int:
    if value == 0:
        return 0
    powered = field.pow(value, (q - 1) // 2)
    if powered == 1:
        return 1
    if powered == field.neg(1):
        return -1
    raise AuditFailure(f"Euler criterion escaped +/-1 at {value}")


def qts_case(p: int, e: int) -> tuple[list[str], int, int]:
    q = p**e
    extension_degree = 2 * e
    modulus = first_irreducible(p, extension_degree)
    field = FiniteField(p, extension_degree, modulus)
    check = Checks()
    zero, one = 0, 1
    two = field.scalar(2)
    four = field.scalar(4)
    minus_one = field.neg(one)

    check.equal(field.size, q * q, "extension size")
    for value in range(field.size):
        check.equal(field.pow(value, q * q), value, "full-field Frobenius")

    base = [value for value in range(field.size) if field.pow(value, q) == value]
    base_set = set(base)
    check.equal(len(base), q, "fixed subfield size")

    def trace(value: int) -> int:
        return field.add(value, field.pow(value, q))

    def norm(value: int) -> int:
        return field.pow(value, q + 1)

    def qts(value: int) -> int:
        if value == 0:
            return 0
        tr = trace(value)
        return field.div(field.mul(tr, tr), value)

    def polynomial_qts(value: int) -> int:
        return field.add(
            field.add(value, field.mul(two, field.pow(value, q))),
            field.pow(value, 2 * q - 1),
        )

    next_state = []
    for value in range(field.size):
        tr = trace(value)
        nm = norm(value)
        check.require(tr in base_set, "trace outside base field")
        check.require(nm in base_set, "norm outside base field")
        image = qts(value)
        check.equal(image, polynomial_qts(value), "literal polynomial identity")
        next_state.append(image)

    # Generalized-cyclotomic owner hypotheses over the field of size Q=q^2.
    Q = q * q
    index = (Q - 1) // gcd(Q - 1, q - 1, 2 * (q - 1))
    check.equal(index, q + 1, "minimal polynomial index")
    mu = [value for value in range(1, field.size) if field.pow(value, index) == one]
    mu_set = set(mu)
    check.equal(len(mu), index, "root-of-unity section size")
    psi_values = []
    for z in mu:
        h = field.pow(field.add(one, z), 2)
        psi = field.mul(z, field.pow(h, (Q - 1) // index))
        if z == minus_one:
            check.equal(psi, zero, "singular cyclotomic value")
        else:
            check.equal(psi, field.inv(z), "cyclotomic inversion")
            check.require(psi in mu_set, "cyclotomic image outside roots")
            psi_values.append(psi)
    check.equal(len(set(psi_values)), index - 1, "m-nice injectivity")

    trace_zero = [value for value in range(field.size) if trace(value) == zero]
    complement = [value for value in range(field.size) if trace(value) != zero]
    complement_set = set(complement)
    check.equal(len(trace_zero), q, "trace kernel size")
    check.equal(len(complement), q * q - q, "trace complement size")
    for value in trace_zero:
        check.equal(next_state[value], zero, "trace-kernel arrow")
    check.equal(set(next_state[value] for value in complement), complement_set,
                "complement permutation")

    half = field.inv(two)
    quarter = field.inv(four)
    H = [value for value in range(field.size) if trace(value) == one]
    check.equal(len(H), q, "trace-one section size")
    check.require(half in H, "half absent from trace-one section")

    # Coordinate bijection and all iterates through one universal period q-1.
    coordinate_pairs = set()
    order_cache: dict[int, int] = {}
    period_histogram = Counter()
    for value in complement:
        a = trace(value)
        u = field.div(value, a)
        c = norm(u)
        check.require(a in base_set and a != zero, "bad radial coordinate")
        check.require(u in H, "bad trace-one coordinate")
        check.require(c in base_set and c != zero, "bad norm coordinate")
        coordinate_pairs.add((a, u))
        expected_one_step = field.mul(field.div(a, c), field.pow(u, q))
        check.equal(next_state[value], expected_one_step, "skew-product update")

        current = value
        for time in range(q):
            conjugate = u if time % 2 == 0 else field.pow(u, q)
            expected = field.mul(field.mul(a, field.pow(c, -time)), conjugate)
            check.equal(current, expected, "all-iterate coordinate law")
            current = next_state[current]

        if c not in order_cache:
            order_cache[c] = multiplicative_order(field, c, q - 1)
        expected_period = (
            multiplicative_order(field, four, q - 1)
            if u == half
            else lcm(2, order_cache[c])
        )
        current = next_state[value]
        actual_period = 1
        while current != value:
            current = next_state[current]
            actual_period += 1
            check.require(actual_period <= q - 1, "period exceeded q-1")
        check.equal(actual_period, expected_period, "pointwise period")
        period_histogram[actual_period] += 1
    check.equal(len(coordinate_pairs), (q - 1) * q, "coordinate bijection")

    # Every-target fibres and the explicit inverse on the complement.
    fibre_sizes = [0] * field.size
    for image in next_state:
        fibre_sizes[image] += 1
    for target in range(field.size):
        tr = trace(target)
        expected_size = q if target == zero else (0 if tr == zero else 1)
        check.equal(fibre_sizes[target], expected_size, "fibre size")
        if tr != zero:
            b = tr
            v = field.div(target, b)
            c = norm(v)
            source = field.mul(field.mul(b, c), field.pow(v, q))
            check.equal(next_state[source], target, "explicit inverse")

    # Norm-section census (10), including characteristic three.
    norm_counts = Counter(norm(u) for u in H)
    S = []
    for c in base:
        if c == zero:
            continue
        discriminant = field.sub(one, field.mul(four, c))
        if quadratic_character(field, discriminant, q) == -1:
            S.append(c)
    check.equal(len(S), (q - 1) // 2, "nonsquare norm-section size")
    S_set = set(S)
    for c in base:
        expected = 0
        if c == quarter:
            expected = 1
        elif c in S_set:
            expected = 2
        check.equal(norm_counts[c], expected, "norm-section multiplicity")

    # Fixed counts (12), direct cycles (14), and merged zeta factors (15).
    r0 = multiplicative_order(field, four, q - 1)
    fixed_counts = {}
    iterate = list(range(field.size))
    for time in range(1, 2 * (q - 1) + 1):
        iterate = [next_state[value] for value in iterate]
        actual = sum(iterate[value] == value for value in range(field.size))
        expected = 1
        if time % r0 == 0:
            expected += q - 1
        if time % 2 == 0:
            expected += 2 * (q - 1) * sum(
                time % multiplicative_order(field, c, q - 1) == 0 for c in S
            )
        check.equal(actual, expected, "fixed-iterate count")
        fixed_counts[time] = actual

    actual_cycles = Counter()
    visited = set()
    for start in range(field.size):
        if start in visited:
            continue
        path = []
        position = {}
        current = start
        while current not in position and current not in visited:
            position[current] = len(path)
            path.append(current)
            current = next_state[current]
        if current in position:
            cycle_length = len(path) - position[current]
            actual_cycles[cycle_length] += 1
        visited.update(path)

    formula_cycles = Counter({1: 1})
    formula_cycles[r0] += (q - 1) // r0
    S_order_histogram = Counter()
    for c in S:
        order = multiplicative_order(field, c, q - 1)
        cycle_length = lcm(2, order)
        S_order_histogram[order] += 1
        formula_cycles[cycle_length] += 2 * (q - 1) // cycle_length
    formula_cycles = Counter({k: v for k, v in formula_cycles.items() if v})
    check.equal(actual_cycles, formula_cycles, "direct cycle census")
    check.equal(sum(length * count for length, count in actual_cycles.items()),
                q * q - q + 1, "recurrent mass")

    zeta_factors = Counter({1: 1})
    zeta_factors[r0] += (q - 1) // r0
    for c in S:
        cycle_length = lcm(2, multiplicative_order(field, c, q - 1))
        zeta_factors[cycle_length] += 2 * (q - 1) // cycle_length
    zeta_factors = Counter({k: v for k, v in zeta_factors.items() if v})
    check.equal(zeta_factors, actual_cycles, "merged zeta factor exponents")
    if p == 3:
        check.equal(r0, 1, "characteristic-three order of four")
        check.equal(zeta_factors[1], q, "characteristic-three merged (1-z) exponent")

    lines = [
        f"q={q} p={p} e={e} E=F_{p}^{extension_degree} modulus={modulus}",
        f"  states={field.size} base={len(base)} index={index} mu={len(mu)} m_nice=yes",
        f"  fibres={dict(sorted(Counter(fibre_sizes).items()))}",
        f"  periods(points)={dict(sorted(period_histogram.items()))}",
        f"  S_order_hist={dict(sorted(S_order_histogram.items()))} r0={r0}",
        f"  cycles={dict(sorted(actual_cycles.items()))}",
        f"  zeta_factors={dict(sorted(zeta_factors.items()))}",
        "  fixed[1..q-1]="
        + ",".join(f"{time}:{fixed_counts[time]}" for time in range(1, q)),
        f"  assertions={check.count} result=PASS",
    ]
    return lines, check.count, field.size


def main() -> None:
    print("QTS PRIME-POWER EXACT AUDIT")
    print("external_status=HOLD_EXTERNAL")
    print("implementation=independent polynomial-basis finite fields")
    total_assertions = 0
    total_states = 0
    for p, e in ((3, 2), (5, 2), (3, 3), (7, 2)):
        lines, assertions, states = qts_case(p, e)
        print("\n".join(lines))
        total_assertions += assertions
        total_states += states
    print(f"TOTAL cases=4 states={total_states} assertions={total_assertions}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
