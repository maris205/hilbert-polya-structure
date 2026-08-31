#!/usr/bin/env python3
"""Independent extension-field audit for translation--GCD erosion.

This program intentionally does not import either historical prime-field
translation--GCD engine.  It constructs F_4, F_8, and F_9 from explicit
irreducible polynomial bases, implements polynomial shift and Euclidean GCD
from those field tables, and exhaustively compares the literal dynamics with
the proposed orbit, terminal-kernel, fibre, and depth-CDF formulae.

Finite enumeration is a falsification control, not a proof or an ownership
claim.
"""

from collections import Counter, defaultdict
from itertools import product


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


class FiniteField:
    """F_p[u]/(modulus), with elements encoded by base-p coefficient words."""

    def __init__(self, name, characteristic, modulus):
        self.name = name
        self.p = characteristic
        self.modulus = tuple(modulus)
        self.extension_degree = len(self.modulus) - 1
        self.q = self.p ** self.extension_degree
        AUDIT.check(self.extension_degree in (2, 3),
                    f"{name}: unexpected basis degree")
        AUDIT.check(self.modulus[-1] == 1,
                    f"{name}: basis polynomial is not monic")

        # In degrees two and three, absence of a base-field root is exactly
        # irreducibility.  This test is performed before quotient arithmetic.
        for root in range(self.p):
            value = 0
            for coefficient in reversed(self.modulus):
                value = (value * root + coefficient) % self.p
            AUDIT.check(value != 0,
                        f"{name}: declared basis polynomial has a root")

        self._digits = tuple(self._decode(value) for value in range(self.q))
        self.add_table = tuple(
            tuple(self._raw_add(left, right)
                  for right in range(self.q))
            for left in range(self.q)
        )
        self.neg_table = tuple(self._raw_neg(value) for value in range(self.q))
        self.mul_table = tuple(
            tuple(self._raw_mul(left, right)
                  for right in range(self.q))
            for left in range(self.q)
        )
        self.zero = 0
        self.one = 1
        self.alpha = self.p

    def _decode(self, value):
        digits = []
        for _ in range(self.extension_degree):
            digits.append(value % self.p)
            value //= self.p
        return tuple(digits)

    def _encode(self, digits):
        value = 0
        place = 1
        for digit in digits:
            value += (digit % self.p) * place
            place *= self.p
        return value

    def _raw_add(self, left, right):
        return self._encode(
            (a + b) % self.p
            for a, b in zip(self._digits[left], self._digits[right])
        )

    def _raw_neg(self, value):
        return self._encode((-digit) % self.p for digit in self._digits[value])

    def _raw_mul(self, left, right):
        width = self.extension_degree
        coefficients = [0] * (2 * width - 1)
        for i, a in enumerate(self._digits[left]):
            for j, b in enumerate(self._digits[right]):
                coefficients[i + j] = (
                    coefficients[i + j] + a * b
                ) % self.p
        for degree in range(2 * width - 2, width - 1, -1):
            leading = coefficients[degree] % self.p
            if leading:
                for index in range(width):
                    position = degree - width + index
                    coefficients[position] = (
                        coefficients[position]
                        - leading * self.modulus[index]
                    ) % self.p
            coefficients[degree] = 0
        return self._encode(coefficients[:width])

    def add(self, left, right):
        return self.add_table[left][right]

    def neg(self, value):
        return self.neg_table[value]

    def sub(self, left, right):
        return self.add(left, self.neg(right))

    def mul(self, left, right):
        return self.mul_table[left][right]

    def power(self, value, exponent):
        answer = self.one
        base = value
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, base)
            base = self.mul(base, base)
            exponent >>= 1
        return answer

    def inverse(self, value):
        if value == self.zero:
            raise ZeroDivisionError("zero has no inverse")
        return self.power(value, self.q - 2)

    def constant(self, integer):
        return integer % self.p

    def audit_axioms(self):
        start = AUDIT.assertions
        # The quotient basis element must satisfy its displayed modulus.
        basis_value = self.zero
        for coefficient in reversed(self.modulus):
            basis_value = self.add(
                self.mul(basis_value, self.alpha), self.constant(coefficient)
            )
        AUDIT.check(basis_value == self.zero,
                    f"{self.name}: basis relation failed")
        for value in range(self.q):
            AUDIT.check(self.add(value, self.zero) == value,
                        f"{self.name}: additive identity failed")
            AUDIT.check(self.add(value, self.neg(value)) == self.zero,
                        f"{self.name}: additive inverse failed")
            AUDIT.check(self.mul(value, self.one) == value,
                        f"{self.name}: multiplicative identity failed")
            AUDIT.check(self.power(value, self.q) == value,
                        f"{self.name}: Frobenius identity failed")
            if value:
                AUDIT.check(self.mul(value, self.inverse(value)) == self.one,
                            f"{self.name}: multiplicative inverse failed")
        for left in range(self.q):
            for middle in range(self.q):
                AUDIT.check(self.add(left, middle) == self.add(middle, left),
                            f"{self.name}: addition is not commutative")
                AUDIT.check(self.mul(left, middle) == self.mul(middle, left),
                            f"{self.name}: multiplication is not commutative")
                for right in range(self.q):
                    AUDIT.check(
                        self.add(self.add(left, middle), right)
                        == self.add(left, self.add(middle, right)),
                        f"{self.name}: addition is not associative",
                    )
                    AUDIT.check(
                        self.mul(self.mul(left, middle), right)
                        == self.mul(left, self.mul(middle, right)),
                        f"{self.name}: multiplication is not associative",
                    )
                    AUDIT.check(
                        self.mul(left, self.add(middle, right))
                        == self.add(self.mul(left, middle),
                                    self.mul(left, right)),
                        f"{self.name}: distributivity failed",
                    )
        return AUDIT.assertions - start


class PolynomialRing:
    """Dense polynomials over one of the explicit extension fields."""

    def __init__(self, field):
        self.field = field
        self.zero = ()
        self.one = (field.one,)
        self.x = (field.zero, field.one)

    def trim(self, coefficients):
        value = list(coefficients)
        while value and value[-1] == self.field.zero:
            value.pop()
        return tuple(value)

    def degree(self, value):
        return len(value) - 1

    def add(self, left, right):
        width = max(len(left), len(right))
        coefficients = [self.field.zero] * width
        for index in range(width):
            a = left[index] if index < len(left) else self.field.zero
            b = right[index] if index < len(right) else self.field.zero
            coefficients[index] = self.field.add(a, b)
        return self.trim(coefficients)

    def sub(self, left, right):
        width = max(len(left), len(right))
        coefficients = [self.field.zero] * width
        for index in range(width):
            a = left[index] if index < len(left) else self.field.zero
            b = right[index] if index < len(right) else self.field.zero
            coefficients[index] = self.field.sub(a, b)
        return self.trim(coefficients)

    def scale(self, value, scalar):
        return self.trim(self.field.mul(coefficient, scalar)
                         for coefficient in value)

    def multiply(self, left, right):
        if not left or not right:
            return self.zero
        coefficients = [self.field.zero] * (len(left) + len(right) - 1)
        for i, a in enumerate(left):
            for j, b in enumerate(right):
                coefficients[i + j] = self.field.add(
                    coefficients[i + j], self.field.mul(a, b)
                )
        return self.trim(coefficients)

    def divmod(self, dividend, divisor):
        divisor = self.trim(divisor)
        if not divisor:
            raise ZeroDivisionError("polynomial division by zero")
        remainder = list(self.trim(dividend))
        if len(remainder) < len(divisor):
            return self.zero, tuple(remainder)
        quotient = [self.field.zero] * (len(remainder) - len(divisor) + 1)
        inverse_lead = self.field.inverse(divisor[-1])
        while remainder and len(remainder) >= len(divisor):
            shift = len(remainder) - len(divisor)
            factor = self.field.mul(remainder[-1], inverse_lead)
            quotient[shift] = self.field.add(quotient[shift], factor)
            for index, coefficient in enumerate(divisor):
                position = shift + index
                remainder[position] = self.field.sub(
                    remainder[position], self.field.mul(factor, coefficient)
                )
            remainder = list(self.trim(remainder))
        return self.trim(quotient), tuple(remainder)

    def monic(self, value):
        value = self.trim(value)
        if not value:
            return value
        return self.scale(value, self.field.inverse(value[-1]))

    def gcd(self, left, right):
        a, b = self.trim(left), self.trim(right)
        while b:
            _, remainder = self.divmod(a, b)
            a, b = b, remainder
        return self.monic(a)

    def shift_constant(self, value, constant):
        """Return f(x+constant) by Horner evaluation."""
        answer = self.zero
        linear = (constant, self.field.one)
        for coefficient in reversed(value):
            answer = self.add(self.multiply(answer, linear), (coefficient,))
        return answer

    def shift_one(self, value):
        return self.shift_constant(value, self.field.one)

    def compose(self, outer, inner):
        answer = self.zero
        for coefficient in reversed(outer):
            answer = self.add(self.multiply(answer, inner), (coefficient,))
        return answer

    def monics_exact(self, degree):
        for lower in product(range(self.field.q), repeat=degree):
            yield tuple(lower) + (self.field.one,)

    def monics_bounded(self, maximum_degree):
        for degree in range(maximum_degree + 1):
            yield from self.monics_exact(degree)


def divisors(number):
    return tuple(value for value in range(1, number + 1)
                 if number % value == 0)


def moebius(number):
    value = number
    sign = 1
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            value //= factor
            sign = -sign
            if value % factor == 0:
                return 0
            while value % factor == 0:
                value //= factor
        factor += 1
    if value > 1:
        sign = -sign
    return sign


def irreducible_count(prime_power, degree):
    numerator = sum(moebius(divisor)
                    * prime_power ** (degree // divisor)
                    for divisor in divisors(degree))
    AUDIT.check(numerator % degree == 0,
                "monic irreducible count lost integrality")
    return numerator // degree


def fixed_irreducible_count(prime_power, characteristic, degree):
    if degree % characteristic:
        return 0
    base_degree = degree // characteristic
    coprime_part = base_degree
    prime_power_part = 1
    while coprime_part % characteristic == 0:
        coprime_part //= characteristic
        prime_power_part *= characteristic
    trace_sum = sum(
        moebius(coprime_part // divisor)
        * prime_power ** (prime_power_part * divisor)
        for divisor in divisors(coprime_part)
    )
    numerator = (characteristic - 1) * trace_sum
    denominator = characteristic * base_degree
    AUDIT.check(numerator % denominator == 0,
                "fixed irreducible trace count lost integrality")
    return numerator // denominator


def is_irreducible(ring, polynomial, monics_by_degree):
    degree = ring.degree(polynomial)
    if degree <= 0:
        return False
    if degree == 1:
        return True
    for divisor_degree in range(1, degree // 2 + 1):
        for candidate in monics_by_degree[divisor_degree]:
            _, remainder = ring.divmod(polynomial, candidate)
            if not remainder:
                return False
    return True


def multiply_series(left, right, maximum_degree):
    answer = [0] * (maximum_degree + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            if i + j > maximum_degree:
                break
            if b:
                answer[i + j] += a * b
    return tuple(answer)


def power_series(series, exponent, maximum_degree):
    answer = (1,) + (0,) * maximum_degree
    base = tuple(series)
    while exponent:
        if exponent & 1:
            answer = multiply_series(answer, base, maximum_degree)
        exponent >>= 1
        if exponent:
            base = multiply_series(base, base, maximum_degree)
    return answer


def longest_positive_cyclic_run(vector):
    length = len(vector)
    support = tuple(value > 0 for value in vector)
    if all(support):
        return length
    answer = 0
    for start in range(length):
        local = 0
        for offset in range(length):
            if support[(start + offset) % length]:
                local += 1
                answer = max(answer, local)
            else:
                break
    return answer


def residual_vector_series(characteristic, depth_bound, maximum_weight):
    """Direct exponent-vector enumeration; no transfer matrix is reused."""
    coefficients = [0] * (maximum_weight + 1)
    for vector in product(range(maximum_weight + 1),
                          repeat=characteristic):
        weight = sum(vector)
        if (weight <= maximum_weight
                and min(vector) == 0
                and longest_positive_cyclic_run(vector) <= depth_bound):
            coefficients[weight] += 1
    return tuple(coefficients)


def depth_cdf_formula(prime_power, characteristic, maximum_degree, depth_bound):
    # All invariant factors, collectively: 1/(1-q z^p).
    answer = tuple(
        prime_power ** (degree // characteristic)
        if degree % characteristic == 0 else 0
        for degree in range(maximum_degree + 1)
    )
    for factor_degree in range(1, maximum_degree + 1):
        total_irreducibles = irreducible_count(prime_power, factor_degree)
        fixed_irreducibles = fixed_irreducible_count(
            prime_power, characteristic, factor_degree
        )
        residual = total_irreducibles - fixed_irreducibles
        AUDIT.check(residual % characteristic == 0,
                    "nonfixed irreducibles do not form p-cycles")
        orbit_count = residual // characteristic
        maximum_weight = maximum_degree // factor_degree
        local = residual_vector_series(
            characteristic, depth_bound, maximum_weight
        )
        substituted = [0] * (maximum_degree + 1)
        for weight, coefficient in enumerate(local):
            substituted[weight * factor_degree] = coefficient
        answer = multiply_series(
            answer,
            power_series(tuple(substituted), orbit_count, maximum_degree),
            maximum_degree,
        )
    return answer


def translation_step(ring, polynomial):
    return ring.gcd(polynomial, ring.shift_one(polynomial))


def terminal_projection(ring, polynomial, characteristic):
    answer = polynomial
    for _ in range(characteristic - 1):
        answer = translation_step(ring, answer)
    return answer


def kernel_exact(prime_power, characteristic, degree):
    if degree < 0:
        return 0
    if degree < characteristic:
        return prime_power ** degree
    return (prime_power ** degree
            - prime_power ** (degree - characteristic + 1))


def audit_lane(field, maximum_degree):
    lane_start = AUDIT.assertions
    field_assertions = field.audit_axioms()
    ring = PolynomialRing(field)
    characteristic = field.p
    prime_power = field.q
    states = tuple(ring.monics_bounded(maximum_degree))
    state_set = set(states)

    depth_by_degree = defaultdict(Counter)
    terminal_by_state = {}
    exact_fibres = Counter()
    bounded_fibres = Counter()
    fixed_states = set()

    for polynomial in states:
        current = polynomial
        window = polynomial
        depth = None
        terminal = None
        for time in range(characteristic):
            AUDIT.check(current == window,
                        f"{field.name}: literal/window iterate mismatch")
            image = translation_step(ring, current)
            if depth is None and image == current:
                depth = time
            if time == characteristic - 1:
                terminal = current
            else:
                translated_input = ring.shift_constant(
                    polynomial, field.constant(time + 1)
                )
                window = ring.gcd(window, translated_input)
            current = image
        AUDIT.check(depth is not None and depth <= characteristic - 1,
                    f"{field.name}: terminal clock failed")
        AUDIT.check(translation_step(ring, terminal) == terminal,
                    f"{field.name}: terminal image is not fixed")
        AUDIT.check(ring.shift_one(terminal) == terminal,
                    f"{field.name}: terminal image is not invariant")
        AUDIT.check(terminal in state_set,
                    f"{field.name}: terminal image left degree phase")

        quotient, remainder = ring.divmod(polynomial, terminal)
        AUDIT.check(not remainder,
                    f"{field.name}: terminal image does not divide input")
        AUDIT.check(ring.multiply(terminal, quotient) == polynomial,
                    f"{field.name}: quotient reconstruction failed")
        AUDIT.check(terminal_projection(ring, quotient, characteristic)
                    == ring.one,
                    f"{field.name}: residual quotient is outside kernel")

        degree = ring.degree(polynomial)
        depth_by_degree[degree][depth] += 1
        terminal_by_state[polynomial] = terminal
        exact_fibres[(terminal, degree)] += 1
        bounded_fibres[terminal] += 1
        if depth == 0:
            fixed_states.add(polynomial)

    # Build F_q[x^p-x] independently by composition.
    artin_schreier_coefficients = [field.zero] * (characteristic + 1)
    artin_schreier_coefficients[1] = field.neg(field.one)
    artin_schreier_coefficients[characteristic] = field.one
    artin_schreier = tuple(artin_schreier_coefficients)
    expected_invariants = set()
    for outer_degree in range(maximum_degree // characteristic + 1):
        for outer in ring.monics_exact(outer_degree):
            expected_invariants.add(ring.compose(outer, artin_schreier))
    observed_image = set(terminal_by_state.values())
    AUDIT.check(observed_image == expected_invariants,
                f"{field.name}: terminal image is not the invariant ring slice")
    AUDIT.check(fixed_states == expected_invariants,
                f"{field.name}: fixed set is not the invariant ring slice")
    for invariant in expected_invariants:
        AUDIT.check(ring.shift_one(invariant) == invariant,
                    f"{field.name}: constructed invariant is not fixed")
    for degree in range(maximum_degree + 1):
        fixed_in_degree = sum(ring.degree(value) == degree
                              for value in fixed_states)
        expected_fixed = (prime_power ** (degree // characteristic)
                          if degree % characteristic == 0 else 0)
        AUDIT.check(fixed_in_degree == expected_fixed,
                    f"{field.name}: fixed exact-degree count failed")

    # Hostile terminology control: Q^{-1}(1) is a fibre, not the kernel of
    # a monoid homomorphism.  Split x^p-x into one linear factor and its
    # complementary orbit product.  Both pieces project to 1, while their
    # product is invariant and projects to itself.
    complement, complement_remainder = ring.divmod(artin_schreier, ring.x)
    AUDIT.check(not complement_remainder,
                f"{field.name}: Artin--Schreier complement division failed")
    AUDIT.check(terminal_projection(ring, ring.x, characteristic) == ring.one,
                f"{field.name}: first nonmultiplicativity factor left fibre")
    AUDIT.check(terminal_projection(ring, complement, characteristic)
                == ring.one,
                f"{field.name}: complementary factor left fibre")
    AUDIT.check(terminal_projection(
                    ring, ring.multiply(ring.x, complement), characteristic)
                == artin_schreier != ring.one,
                f"{field.name}: projection unexpectedly multiplicative")

    # Exact kernel and all exact/bounded target fibres.
    for degree in range(maximum_degree + 1):
        enumerated_kernel = exact_fibres[(ring.one, degree)]
        AUDIT.check(enumerated_kernel
                    == kernel_exact(prime_power, characteristic, degree),
                    f"{field.name}: kernel coefficient failed")
    for target in expected_invariants:
        target_degree = ring.degree(target)
        bounded_expected = 0
        for input_degree in range(maximum_degree + 1):
            residual_degree = input_degree - target_degree
            expected = kernel_exact(
                prime_power, characteristic, residual_degree
            )
            AUDIT.check(exact_fibres[(target, input_degree)] == expected,
                        f"{field.name}: exact target fibre failed")
            bounded_expected += expected
        AUDIT.check(bounded_fibres[target] == bounded_expected,
                    f"{field.name}: bounded target fibre failed")

    # Naive irreducibility testing and literal translation orbits.
    monics_by_degree = {
        degree: tuple(ring.monics_exact(degree))
        for degree in range(1, maximum_degree + 1)
    }
    irreducibles_by_degree = {}
    irreducible_profile = []
    for degree in range(1, maximum_degree + 1):
        irreducibles = {
            polynomial for polynomial in monics_by_degree[degree]
            if is_irreducible(ring, polynomial, monics_by_degree)
        }
        irreducibles_by_degree[degree] = irreducibles
        expected_total = irreducible_count(prime_power, degree)
        AUDIT.check(len(irreducibles) == expected_total,
                    f"{field.name}: irreducible count failed")
        for polynomial in irreducibles:
            AUDIT.check(ring.shift_one(polynomial) in irreducibles,
                        f"{field.name}: shift did not preserve irreducibility")

        remaining = set(irreducibles)
        orbit_lengths = Counter()
        fixed_count = 0
        while remaining:
            seed = min(remaining)
            orbit = []
            current = seed
            while current not in orbit:
                orbit.append(current)
                current = ring.shift_one(current)
            AUDIT.check(current == seed,
                        f"{field.name}: irreducible orbit did not close at seed")
            AUDIT.check(len(orbit) in (1, characteristic),
                        f"{field.name}: impossible translation orbit length")
            AUDIT.check(all(value in remaining for value in orbit),
                        f"{field.name}: orbit partition overlap")
            remaining.difference_update(orbit)
            orbit_lengths[len(orbit)] += 1
            if len(orbit) == 1:
                fixed_count += 1

        expected_fixed_irreducibles = fixed_irreducible_count(
            prime_power, characteristic, degree
        )
        AUDIT.check(fixed_count == expected_fixed_irreducibles,
                    f"{field.name}: fixed irreducible trace formula failed")
        expected_nonfixed_orbits = (
            expected_total - expected_fixed_irreducibles
        ) // characteristic
        AUDIT.check(orbit_lengths[characteristic]
                    == expected_nonfixed_orbits,
                    f"{field.name}: nonfixed irreducible orbit count failed")
        AUDIT.check(orbit_lengths[1] == expected_fixed_irreducibles,
                    f"{field.name}: fixed irreducible orbit count failed")
        irreducible_profile.append(
            f"d{degree}:N{expected_total}:b{fixed_count}:"
            f"a{expected_nonfixed_orbits}"
        )

    # Independent residual-exponent enumeration checks every CDF cell.
    cdf_top_degree = []
    for depth_bound in range(characteristic):
        formula = depth_cdf_formula(
            prime_power, characteristic, maximum_degree, depth_bound
        )
        for degree in range(maximum_degree + 1):
            enumerated = sum(
                multiplicity
                for local_depth, multiplicity in depth_by_degree[degree].items()
                if local_depth <= depth_bound
            )
            AUDIT.check(enumerated == formula[degree],
                        f"{field.name}: depth CDF Euler product failed")
        cdf_top_degree.append(f"t{depth_bound}:{formula[maximum_degree]}")
    AUDIT.check(max(max(counter) for counter in depth_by_degree.values())
                == characteristic - 1,
                f"{field.name}: sharp terminal depth absent")
    terminal_formula = depth_cdf_formula(
        prime_power, characteristic, maximum_degree, characteristic - 1
    )
    for degree, coefficient in enumerate(terminal_formula):
        AUDIT.check(coefficient == prime_power ** degree,
                    f"{field.name}: terminal CDF boundary failed")

    kernel_profile = ",".join(
        f"K{degree}={kernel_exact(prime_power, characteristic, degree)}"
        for degree in range(maximum_degree + 1)
    )
    fibre_sizes = tuple(bounded_fibres.values())
    lane_assertions = AUDIT.assertions - lane_start
    modulus_text = "+".join(
        f"{coefficient}u^{degree}"
        for degree, coefficient in enumerate(field.modulus)
        if coefficient
    )
    print(
        f"FIELD={field.name} q={prime_power} p={characteristic} "
        f"basis={modulus_text} D={maximum_degree} states={len(states)} "
        f"images={len(expected_invariants)} depth={characteristic - 1}"
    )
    print(f"  field_axiom_assertions={field_assertions}")
    print(f"  irreducibles={'/'.join(irreducible_profile)}")
    print(f"  top_degree_cdf={','.join(cdf_top_degree)}")
    print(f"  kernel={kernel_profile}")
    print(
        f"  bounded_fibres=min{min(fibre_sizes)}:max{max(fibre_sizes)}:"
        f"kernel{bounded_fibres[ring.one]}"
    )
    print("  terminology_control=Q_inverse_1_is_a_fibre_not_a_monoid_kernel")
    print(f"  lane_assertions={lane_assertions}")


def main():
    print("INDEPENDENT_EXTENSION_TRANSLATION_GCD_AUDIT")
    print("engine=explicit quotient fields + Horner shift + Euclidean GCD + naive irreducibility")
    lanes = (
        (FiniteField("F4", 2, (1, 1, 1)), 6),
        (FiniteField("F8", 2, (1, 1, 0, 1)), 4),
        (FiniteField("F9", 3, (1, 0, 1)), 4),
    )
    for field, maximum_degree in lanes:
        audit_lane(field, maximum_degree)
    print(f"TOTAL_ASSERTIONS={AUDIT.assertions}")
    print("scope_sentinel=finite extension-field enumeration is falsification evidence, never proof")
    print("credit_sentinel=old window/clock/fixed/depth results remain zero credit")
    print("release_sentinel=bounded owner non-hit is not novelty or priority; external HOLD")


if __name__ == "__main__":
    main()
