#!/usr/bin/env python3
"""Exact controls for bounded Cartier-operator dynamics.

The implementation uses literal polynomial-basis finite fields.  It checks
the coefficient iterate, the coordinate conjugacy to inverse Frobenius times
nilpotent shifts, product-component profiles, every iterated image and fibre,
the complete depth profile, the inverse-Frobenius periodic core and zeta
coefficients, exact lattice-tail stabilization, and recovery of (p,a,n) from
temporal data.  Only the Python standard library is used.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, gcd


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


class FiniteField:
    """A small polynomial-basis field F_p[z]/(modulus)."""

    def __init__(self, p, modulus):
        self.p = p
        self.modulus = tuple(modulus)  # low coefficient first, monic
        self.a = len(self.modulus) - 1
        self.q = p**self.a
        AUDIT.check(self.a >= 1)
        AUDIT.check(self.modulus[-1] == 1)
        self._mul_table = tuple(
            tuple(self._mul_raw(x, y) for y in range(self.q))
            for x in range(self.q)
        )
        self._inverse_frobenius = tuple(
            self.power(x, p ** (self.a - 1)) for x in range(self.q)
        )

    def digits(self, value, length=None):
        if length is None:
            length = self.a
        out = []
        for _ in range(length):
            out.append(value % self.p)
            value //= self.p
        return out

    def encode(self, digits):
        value = 0
        place = 1
        for digit in digits:
            value += (digit % self.p) * place
            place *= self.p
        return value

    def _mul_raw(self, left, right):
        x = self.digits(left)
        y = self.digits(right)
        raw = [0] * (2 * self.a - 1)
        for i, xi in enumerate(x):
            for j, yj in enumerate(y):
                raw[i + j] = (raw[i + j] + xi * yj) % self.p
        for degree in range(len(raw) - 1, self.a - 1, -1):
            coefficient = raw[degree] % self.p
            if coefficient:
                shift = degree - self.a
                for j in range(self.a + 1):
                    raw[shift + j] = (
                        raw[shift + j] - coefficient * self.modulus[j]
                    ) % self.p
        return self.encode(raw[: self.a])

    def mul(self, left, right):
        return self._mul_table[left][right]

    def power(self, value, exponent):
        result = 1
        base = value
        while exponent:
            if exponent & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            exponent //= 2
        return result

    def frobenius_inverse(self, value, times=1):
        if self.a == 1:
            return value
        times %= self.a
        for _ in range(times):
            value = self._inverse_frobenius[value]
        return value

    def frobenius(self, value, times=1):
        """Apply sigma^times, with sigma(value)=value^p."""
        if self.a == 1:
            return value
        return self.power(value, self.p ** (times % self.a))

    def audit_field(self):
        for x in range(self.q):
            AUDIT.check(self.power(x, self.q) == x, "Frobenius identity failed")
            root = self.frobenius_inverse(x)
            AUDIT.check(self.power(root, self.p) == x, "inverse Frobenius failed")
        for x in range(1, self.q):
            AUDIT.check(self.power(x, self.q - 1) == 1, "modulus is not a field")


def cartier(vector, field):
    n = len(vector) - 1
    out = [0] * (n + 1)
    for j in range(n // field.p + 1):
        out[j] = field.frobenius_inverse(vector[field.p * j])
    return tuple(out)


def iterate(vector, field, times):
    vector = tuple(vector)
    for _ in range(times):
        vector = cartier(vector, field)
    return vector


def iterate_formula(vector, field, times):
    n = len(vector) - 1
    scale = field.p**times
    out = [0] * (n + 1)
    for j in range(n // scale + 1):
        out[j] = field.frobenius_inverse(vector[scale * j], times)
    return tuple(out)


def index_chains(n, p):
    """Return the positive-index chains (u, up, ..., up^ell), p not dividing u."""
    chains = []
    for unit in range(1, n + 1):
        if unit % p:
            chain = []
            index = unit
            while index <= n:
                chain.append(index)
                index *= p
            chains.append(tuple(chain))
    return tuple(chains)


def to_product_coordinates(vector, field):
    """Conjugacy d_(u,v)=sigma^(-v)(c_(u p^v))."""
    chains = tuple(
        tuple(field.frobenius_inverse(vector[index], level) for level, index in enumerate(chain))
        for chain in index_chains(len(vector) - 1, field.p)
    )
    return vector[0], chains


def from_product_coordinates(coordinates, field, n):
    constant, chains = coordinates
    vector = [0] * (n + 1)
    vector[0] = constant
    index_data = index_chains(n, field.p)
    AUDIT.check(len(chains) == len(index_data), "chain-count mismatch")
    for chain, values in zip(index_data, chains):
        AUDIT.check(len(chain) == len(values), "chain-length mismatch")
        for level, (index, value) in enumerate(zip(chain, values)):
            vector[index] = field.frobenius(value, level)
    return tuple(vector)


def product_update(coordinates, field):
    """Inverse Frobenius on the constant and a left nilpotent shift per chain."""
    constant, chains = coordinates
    shifted = tuple(chain[1:] + (0,) for chain in chains)
    return field.frobenius_inverse(constant), shifted


def core_cycle_key(value, field):
    orbit = []
    current = value
    while current not in orbit:
        orbit.append(current)
        current = field.frobenius_inverse(current)
    AUDIT.check(current == value, "inverse-Frobenius orbit has a tail")
    return min(orbit), len(orbit)


def direct_entry_time(vector, field):
    current = tuple(vector)
    time = 0
    while any(current[1:]):
        current = cartier(current, field)
        time += 1
        AUDIT.check(time <= len(vector), "orbit did not enter the constant core")
    return time


def valuation(index, p):
    value = 0
    while index % p == 0:
        index //= p
        value += 1
    return value


def predicted_entry_time(vector, p):
    occupied = [j for j, coefficient in enumerate(vector) if j > 0 and coefficient]
    if not occupied:
        return 0
    return 1 + max(valuation(j, p) for j in occupied)


def maximum_depth(n, p):
    if n == 0:
        return 0
    depth = 0
    scale = 1
    while scale <= n:
        depth += 1
        scale *= p
    return depth


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    prime_count = 0
    divisor = 2
    remaining = n
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            prime_count += 1
            if remaining % divisor == 0:
                return 0
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def exact_period_points(field, period):
    return sum(
        mobius(period // d) * field.p**d for d in divisors(period)
    )


def multiply_series(left, right, cutoff):
    out = [0] * (cutoff + 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if i + j <= cutoff:
                out[i + j] += x * y
    return out


def zeta_from_cycles(field, cutoff):
    coefficients = [1] + [0] * cutoff
    for period in divisors(field.a):
        cycles = exact_period_points(field, period) // period
        factor = [0] * (cutoff + 1)
        for repetitions in range(cutoff // period + 1):
            if cycles == 0:
                coefficient = 1 if repetitions == 0 else 0
            else:
                coefficient = comb(cycles + repetitions - 1, repetitions)
            factor[period * repetitions] = coefficient
        coefficients = multiply_series(coefficients, factor, cutoff)
    return coefficients


def zeta_from_fixed(field, cutoff):
    coefficients = [Fraction(0) for _ in range(cutoff + 1)]
    coefficients[0] = Fraction(1)
    for m in range(1, cutoff + 1):
        total = sum(
            field.p ** gcd(field.a, j) * coefficients[m - j]
            for j in range(1, m + 1)
        )
        coefficients[m] = total / m
    return coefficients


def recover_temporal_signature(field, n, fixed_counts, phase_size):
    recovered_p = fixed_counts[1]
    recovered_q = max(fixed_counts[1:])
    recovered_a = next(
        m for m in range(1, len(fixed_counts)) if fixed_counts[m] == recovered_q
    )
    quotient = phase_size
    exponent = 0
    while quotient % recovered_q == 0:
        quotient //= recovered_q
        exponent += 1
    AUDIT.check(quotient == 1, "phase size is not a power of recovered q")
    return recovered_p, recovered_a, exponent - 1


def run_lane(field, n):
    phase = list(product(range(field.q), repeat=n + 1))
    phase_size = len(phase)
    depth_histogram = Counter()
    max_depth = maximum_depth(n, field.p)
    iterate_times = range(0, max_depth + 3)
    fixed_counts = [0] * (2 * field.a + 1)
    entry_profile = Counter()
    component_sizes = Counter()

    chains = index_chains(n, field.p)
    flattened = sorted(index for chain in chains for index in chain)
    AUDIT.check(flattened == list(range(1, n + 1)), "index chains do not partition")

    for vector in phase:
        product_coordinates = to_product_coordinates(vector, field)
        reconstructed = from_product_coordinates(product_coordinates, field, n)
        AUDIT.check(reconstructed == vector, "coordinate conjugacy is not bijective")
        AUDIT.check(
            to_product_coordinates(cartier(vector, field), field)
            == product_update(product_coordinates, field),
            "Cartier/product conjugacy mismatch",
        )

        for t in iterate_times:
            literal = iterate(vector, field, t)
            closed = iterate_formula(vector, field, t)
            AUDIT.check(
                literal == closed,
                f"iterate mismatch q={field.q}, n={n}, t={t}, f={vector}",
            )
            for j in range(n + 1):
                AUDIT.check(literal[j] == closed[j], "coefficient mismatch")

        depth = direct_entry_time(vector, field)
        AUDIT.check(depth == predicted_entry_time(vector, field.p), "depth mismatch")
        AUDIT.check(0 <= depth <= max_depth, "depth outside sharp range")
        depth_histogram[depth] += 1

        endpoint = iterate(vector, field, depth)
        AUDIT.check(not any(endpoint[1:]), "entry point is not constant")
        root = endpoint[0]
        entry_profile[(root, depth)] += 1
        component_key, _ = core_cycle_key(root, field)
        component_sizes[component_key] += 1

        current = vector
        for m in range(1, 2 * field.a + 1):
            current = cartier(current, field)
            if current == vector:
                fixed_counts[m] += 1

    AUDIT.check(sum(depth_histogram.values()) == phase_size)
    AUDIT.check(min(depth_histogram) == 0)
    AUDIT.check(max(depth_histogram) == max_depth)

    for t in iterate_times:
        scale = field.p**t
        retained_degree = n // scale
        literal_cdf = sum(
            count for depth, count in depth_histogram.items() if depth <= t
        )
        formula_cdf = field.q ** (n + 1 - retained_degree)
        AUDIT.check(literal_cdf == formula_cdf, "core-entry CDF mismatch")

        fibres = Counter(iterate(vector, field, t) for vector in phase)
        expected_image = {
            tuple(prefix) + (0,) * (n - retained_degree)
            for prefix in product(range(field.q), repeat=retained_degree + 1)
        }
        AUDIT.check(set(fibres) == expected_image, "iterated image mismatch")
        expected_fibre = field.q ** (n - retained_degree)
        for target in expected_image:
            AUDIT.check(fibres[target] == expected_fibre, "nonuniform fibre")
        AUDIT.check(sum(fibres.values()) == phase_size)
        zero = (0,) * (n + 1)
        AUDIT.check(fibres[zero] == expected_fibre, "kernel-size mismatch")
        if retained_degree < n:
            outside = [0] * (n + 1)
            outside[retained_degree + 1] = 1
            AUDIT.check(fibres[tuple(outside)] == 0, "empty fibre was not empty")

    AUDIT.check(depth_histogram[0] == field.q)
    for t in range(1, max_depth + 1):
        current_cdf = field.q ** (n + 1 - n // (field.p**t))
        previous_cdf = field.q ** (n + 1 - n // (field.p ** (t - 1)))
        AUDIT.check(
            depth_histogram[t] == current_cdf - previous_cdf,
            "depth shell mismatch",
        )
    if n == 0:
        AUDIT.check(max_depth == 0)
        AUDIT.check(depth_histogram[0] == phase_size == field.q)
    else:
        top_chain_count = n // (field.p ** (max_depth - 1))
        deepest = field.q ** (n + 1) - field.q ** (n + 1 - top_chain_count)
        AUDIT.check(depth_histogram[max_depth] == deepest, "deepest shell mismatch")
        AUDIT.check(1 <= top_chain_count < field.p)

    for root in range(field.q):
        AUDIT.check(entry_profile[(root, 0)] == 1, "periodic root multiplicity mismatch")
        for t in range(1, max_depth + 1):
            retained = n // (field.p**t)
            previous = n // (field.p ** (t - 1))
            expected_layer = field.q ** (n - retained) - field.q ** (n - previous)
            AUDIT.check(
                entry_profile[(root, t)] == expected_layer,
                "per-root attached-tree layer mismatch",
            )
        AUDIT.check(
            sum(entry_profile[(root, t)] for t in range(max_depth + 1))
            == field.q**n,
            "attached-tree size mismatch",
        )

    unseen = set(range(field.q))
    cycle_histogram = Counter()
    while unseen:
        start = min(unseen)
        orbit = []
        current = start
        while current not in orbit:
            orbit.append(current)
            current = field.frobenius_inverse(current)
        AUDIT.check(current == start, "constant orbit has a tail")
        for value in orbit:
            AUDIT.check(value in unseen)
            unseen.remove(value)
        cycle_histogram[len(orbit)] += 1

    for period in range(1, field.a + 1):
        if field.a % period == 0:
            points = exact_period_points(field, period)
            AUDIT.check(points % period == 0)
            AUDIT.check(cycle_histogram[period] == points // period)
        else:
            AUDIT.check(cycle_histogram[period] == 0)
    AUDIT.check(
        sum(period * count for period, count in cycle_histogram.items()) == field.q
    )

    AUDIT.check(
        len(component_sizes) == sum(cycle_histogram.values()),
        "weak-component count mismatch",
    )
    component_size_by_period = {}
    for representative, literal_size in component_sizes.items():
        _, period = core_cycle_key(representative, field)
        expected_size = period * field.q**n
        AUDIT.check(literal_size == expected_size, "weak-component size mismatch")
        component_size_by_period[period] = expected_size

    for m in range(1, 2 * field.a + 1):
        AUDIT.check(
            fixed_counts[m] == field.p ** gcd(field.a, m),
            "fixed-count mismatch",
        )
        cycle_fixed = sum(
            period * count
            for period, count in cycle_histogram.items()
            if m % period == 0
        )
        AUDIT.check(cycle_fixed == fixed_counts[m], "cycle/fixed mismatch")

    cutoff = 2 * field.a + 6
    cycle_zeta = zeta_from_cycles(field, cutoff)
    fixed_zeta = zeta_from_fixed(field, cutoff)
    for degree in range(cutoff + 1):
        AUDIT.check(Fraction(cycle_zeta[degree]) == fixed_zeta[degree], "zeta mismatch")

    recovered = recover_temporal_signature(field, n, fixed_counts, phase_size)
    AUDIT.check(recovered == (field.p, field.a, n), "temporal recovery failed")

    if field.a > 1:
        witness = next(x for x in range(field.q) if field.frobenius_inverse(x) != x)
        constant_one = (1,) + (0,) * n
        scaled = (witness,) + (0,) * n
        AUDIT.check(
            cartier(scaled, field)[0]
            != field.mul(witness, cartier(constant_one, field)[0]),
            "false F_q-linearity survived",
        )
        AUDIT.check(any(period > 1 for period in cycle_histogram))
    if n >= field.p + 1:
        low = [0] * (n + 1)
        high = [0] * (n + 1)
        low[field.p + 1] = 1
        high[field.p + 1] = 1
        high[field.p] = 1
        AUDIT.check(predicted_entry_time(low, field.p) == 1)
        AUDIT.check(predicted_entry_time(high, field.p) == 2)
        AUDIT.check(max(i for i, c in enumerate(low) if c) == max(i for i, c in enumerate(high) if c))

    print(
        f"q={field.q}=({field.p}^{field.a}), n={n}: phase={phase_size}, "
        f"D={max_depth}, depths={dict(sorted(depth_histogram.items()))}, "
        f"core_cycles={dict(sorted(cycle_histogram.items()))}, "
        f"component_sizes={dict(sorted(component_size_by_period.items()))}"
    )


def floor_fraction_times_power(alpha, p, exponent):
    return alpha.numerator * p**exponent // alpha.denominator


def audit_lattice_limits():
    cases = {
        2: (Fraction(1), Fraction(3, 2), Fraction(7, 4)),
        3: (Fraction(1), Fraction(4, 3), Fraction(5, 2), Fraction(8, 3)),
        5: (Fraction(1), Fraction(6, 5), Fraction(7, 2), Fraction(24, 5)),
    }
    case_count = 0
    for p, alphas in cases.items():
        for a in (1, 2, 3):
            q = p**a
            for alpha in alphas:
                AUDIT.check(Fraction(1) <= alpha < p)
                previous_exponent = 0
                for k in range(1, 8):
                    exponent = floor_fraction_times_power(alpha, p, k - 1)
                    AUDIT.check(exponent >= previous_exponent)
                    previous_exponent = exponent
                for level in range(0, 10):
                    n = floor_fraction_times_power(alpha, p, level)
                    depth = maximum_depth(n, p)
                    AUDIT.check(p**level <= n < p ** (level + 1))
                    AUDIT.check(depth == level + 1)
                    # The shell probabilities telescope because the final
                    # CDF exponent is n+1.  Keep this audit at exponent level
                    # so large lattice indices never allocate huge integers.
                    cdf_exponents = [n + 1 - n // (p**t) for t in range(depth + 1)]
                    AUDIT.check(cdf_exponents[-1] == n + 1)
                    AUDIT.check(all(x < y for x, y in zip(cdf_exponents, cdf_exponents[1:])))
                    for k in range(1, level + 2):
                        literal_exponent = n // (p ** (level + 1 - k))
                        stable_exponent = floor_fraction_times_power(alpha, p, k - 1)
                        AUDIT.check(literal_exponent == stable_exponent)
                        AUDIT.check(q >= 2 and literal_exponent >= 1)
                case_count += 1
    print(f"lattice stabilization: {case_count} rational (p,a,alpha) lanes through L=9")


def main():
    fields_and_degrees = [
        (FiniteField(2, (0, 1)), 7),
        (FiniteField(3, (0, 1)), 5),
        (FiniteField(2, (1, 1, 1)), 5),
        (FiniteField(2, (1, 1, 0, 1)), 4),
        (FiniteField(3, (1, 0, 1)), 3),
        (FiniteField(2, (1, 1, 0, 0, 1)), 2),
    ]
    for field, degree in fields_and_degrees:
        field.audit_field()
        run_lane(field, 0)
        run_lane(field, degree)
    audit_lattice_limits()
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
