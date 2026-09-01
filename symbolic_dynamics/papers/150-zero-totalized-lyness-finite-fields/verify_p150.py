#!/usr/bin/env python3
"""Exact paper-local falsifier for P150.

The program constructs the declared finite fields using only the Python
standard library, enumerates every state and target in each finite box, and
checks the literal zero-totalized Lyness map against every theorem formula.
Finite enumeration is counterexample pressure, not proof, novelty, priority,
ownership, or release evidence.
"""

from collections import Counter, defaultdict
from itertools import product


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def primes_up_to(bound):
    primes = []
    for candidate in range(2, bound + 1):
        if all(candidate % prime for prime in primes if prime * prime <= candidate):
            primes.append(candidate)
    return primes


class PrimeField:
    def __init__(self, prime):
        self.name = f"F{prime}"
        self.p = prime
        self.q = prime
        self.zero = 0
        self.one = 1

    def add(self, left, right):
        return (left + right) % self.p

    def neg(self, value):
        return (-value) % self.p

    def sub(self, left, right):
        return (left - right) % self.p

    def mul(self, left, right):
        return left * right % self.p

    def power(self, value, exponent):
        return pow(value, exponent, self.p)

    def inv0(self, value):
        return 0 if value == 0 else pow(value, self.p - 2, self.p)


class ExtensionField:
    """F_p[u]/(modulus), with elements encoded by base-p coefficient words."""

    def __init__(self, name, prime, modulus):
        self.name = name
        self.p = prime
        self.modulus = tuple(modulus)
        self.degree = len(self.modulus) - 1
        self.q = prime ** self.degree
        self.zero = 0
        self.one = 1
        check(self.degree in (2, 3), "only quadratic/cubic extensions are declared")
        check(self.modulus[-1] == 1, "extension modulus is not monic")
        # For degree two or three, absence of a base-field root is equivalent
        # to irreducibility.
        for root in range(prime):
            value = 0
            for coefficient in reversed(self.modulus):
                value = (value * root + coefficient) % prime
            check(value != 0, "declared extension polynomial is reducible")
        self.digits = tuple(self._decode(value) for value in range(self.q))
        self.add_table = tuple(
            tuple(self._raw_add(left, right) for right in range(self.q))
            for left in range(self.q)
        )
        self.neg_table = tuple(self._raw_neg(value) for value in range(self.q))
        self.mul_table = tuple(
            tuple(self._raw_mul(left, right) for right in range(self.q))
            for left in range(self.q)
        )
        for value in range(self.q):
            check(self.power(value, self.q) == value, "Frobenius identity failed")
            if value:
                check(self.mul(value, self.inv0(value)) == self.one,
                      "extension inverse failed")

    def _decode(self, value):
        digits = []
        for _ in range(self.degree):
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
            (a + b) % self.p for a, b in zip(self.digits[left], self.digits[right])
        )

    def _raw_neg(self, value):
        return self._encode((-digit) % self.p for digit in self.digits[value])

    def _raw_mul(self, left, right):
        width = self.degree
        coefficients = [0] * (2 * width - 1)
        for i, a in enumerate(self.digits[left]):
            for j, b in enumerate(self.digits[right]):
                coefficients[i + j] = (coefficients[i + j] + a * b) % self.p
        for degree in range(2 * width - 2, width - 1, -1):
            leading = coefficients[degree] % self.p
            if leading:
                for index in range(width):
                    position = degree - width + index
                    coefficients[position] = (
                        coefficients[position] - leading * self.modulus[index]
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

    def inv0(self, value):
        return self.zero if value == self.zero else self.power(value, self.q - 2)


def orbit_signature(state, step):
    seen = {}
    order = []
    current = state
    while current not in seen:
        seen[current] = len(order)
        order.append(current)
        current = step(current)
        check(len(order) <= 9, "orbit exceeded the proved tail-plus-period bound")
    tail = seen[current]
    period = len(order) - tail
    check(period >= 1, "orbit did not close")
    check(step(order[-1]) == current, "last orbit arrow is inconsistent")
    return tail, period


def canonical_cycle(state, step):
    cycle = [state]
    current = step(state)
    while current != state:
        cycle.append(current)
        current = step(current)
        check(len(cycle) <= 5, "recurrent cycle exceeded the theorem ceiling")
    pivot = min(range(len(cycle)), key=cycle.__getitem__)
    return tuple(cycle[pivot:] + cycle[:pivot])


def run_field(field):
    q = field.q
    zero, one = field.zero, field.one
    minus_one = field.neg(one)
    check(q % 2 == 1 and one != minus_one, "P150 requires odd characteristic")
    states = tuple(product(range(q), repeat=2))
    state_set = set(states)

    def add3(a, b, c):
        return field.add(field.add(a, b), c)

    def step(state):
        x, y = state
        return (y, field.mul(field.add(one, y), field.inv0(x)))

    generic = {
        (x, y) for x, y in states
        if x != zero and y != zero
        and field.add(one, x) != zero
        and field.add(one, y) != zero
        and add3(one, x, y) != zero
    }
    axes = {(zero, a) for a in range(q)} | {(a, zero) for a in range(q)}
    e1 = {(a, minus_one) for a in range(q) if a != zero}
    parameters = tuple(a for a in range(q) if a not in (zero, minus_one))
    e2 = {(field.neg(field.add(one, a)), a) for a in parameters}
    e3 = {(minus_one, field.neg(field.add(one, a))) for a in parameters}
    strata = (generic, axes, e1, e2, e3)

    check(len(generic) == (q - 2) * (q - 3), "generic-locus size failed")
    check(len(axes) == 2 * q - 1, "axis size failed")
    check(len(e1) == q - 1 and len(e2) == len(e3) == q - 2,
          "exceptional-layer size failed")
    for index, left in enumerate(strata):
        for right in strata[index + 1:]:
            check(left.isdisjoint(right), "declared strata overlap")
    check(set().union(*strata) == state_set, "declared strata do not cover plane")
    check(sum(map(len, strata)) == q * q, "stratum cardinalities have wrong sum")

    images = {}
    predecessors = defaultdict(set)
    tail_histogram = Counter()
    recurrent_period_points = Counter()
    signatures = {}
    for state in states:
        memberships = tuple(state in stratum for stratum in strata)
        check(sum(memberships) == 1, "point does not have unique stratum")
        image = step(state)
        check(image in state_set, "literal update left affine carrier")
        images[state] = image
        predecessors[image].add(state)
        tail, period = orbit_signature(state, step)
        signatures[state] = (tail, period)
        tail_histogram[tail] += 1
        if tail == 0:
            recurrent_period_points[period] += 1

        x, y = state
        if state in generic:
            fixed = x == y and field.sub(field.sub(field.mul(x, x), x), one) == zero
            expected = (0, 1 if fixed else 5)
        elif state in axes:
            if state == (zero, zero):
                expected = (0, 1)
            else:
                a = y if x == zero else x
                expected = (0, 2 if field.mul(a, a) == one else 4)
        elif state in e1:
            expected = (1, 2)
        elif state in e2:
            expected = (2, 2)
        else:
            expected = (3, 2)
        check((tail, period) == expected, "pointwise tail/period classification failed")

    # Pressure-test the five displayed rational iterates, not merely L^5=id.
    for x, y in generic:
        z = field.mul(field.add(one, y), field.inv0(x))
        w = field.mul(add3(one, x, y), field.inv0(field.mul(x, y)))
        t = field.mul(field.add(one, x), field.inv0(y))
        expected_orbit = ((y, z), (z, w), (w, t), (t, x), (x, y))
        current = (x, y)
        for expected in expected_orbit:
            current = step(current)
            check(current == expected, "generic five-iterate formula failed")

    # Literal exceptional arrows and their exact predecessor boundaries.
    check(step((minus_one, minus_one)) == (minus_one, zero),
          "exceptional leaf arrow failed")
    check(step((minus_one, zero)) == (zero, minus_one)
          and step((zero, minus_one)) == (minus_one, zero),
          "distinguished two-cycle failed")
    for a in parameters:
        level3 = (minus_one, field.neg(field.add(one, a)))
        level2 = (field.neg(field.add(one, a)), a)
        level1 = (a, minus_one)
        check(step(level3) == level2 and step(level2) == level1
              and step(level1) == (minus_one, zero),
              "exceptional length-three chain failed")

    roots = sum(
        field.sub(field.sub(field.mul(a, a), a), one) == zero
        for a in range(q)
    )
    check(roots in (0, 1, 2), "quadratic root count exceeded degree")
    expected_tails = {
        0: q * q - 3 * q + 5,
        1: q - 1,
        2: q - 2,
        3: q - 2,
    }
    check(dict(sorted(tail_histogram.items())) == expected_tails,
          "temporal polynomial failed")
    expected_recurrent_periods = {
        1: 1 + roots,
        2: 4,
        4: 2 * (q - 3),
        5: (q - 2) * (q - 3) - roots,
    }
    expected_recurrent_periods = {
        period: count for period, count in expected_recurrent_periods.items() if count
    }
    check(dict(sorted(recurrent_period_points.items())) == expected_recurrent_periods,
          "recurrent point-period census failed")
    check(((q - 2) * (q - 3) - roots) % 5 == 0,
          "exact-period-five points do not divide into cycles")

    cycles = set()
    for state, (tail, _period) in signatures.items():
        if tail == 0:
            cycles.add(canonical_cycle(state, step))
    cycle_counts = Counter(map(len, cycles))
    expected_cycle_counts = {
        1: 1 + roots,
        2: 2,
        4: (q - 3) // 2,
        5: ((q - 2) * (q - 3) - roots) // 5,
    }
    expected_cycle_counts = {
        period: count for period, count in expected_cycle_counts.items() if count
    }
    check(dict(sorted(cycle_counts.items())) == expected_cycle_counts,
          "literal cycle extraction failed")
    for iterate in range(1, 21):
        literal_fixed = sum(
            tail == 0 and iterate % period == 0
            for tail, period in signatures.values()
        )
        expected_fixed = (
            1 + roots
            + (4 if iterate % 2 == 0 else 0)
            + (2 * (q - 3) if iterate % 4 == 0 else 0)
            + (((q - 2) * (q - 3) - roots) if iterate % 5 == 0 else 0)
        )
        check(literal_fixed == expected_fixed, "zeta fixed-iterate shadow failed")

    # Every-target fibres and image.
    for target in states:
        u, v = target
        if u == minus_one and v == zero:
            expected_fibre = q
        elif u == minus_one:
            expected_fibre = 0
        else:
            expected_fibre = 1
        check(len(predecessors[target]) == expected_fibre,
              "every-target fibre law failed")
    image = set(images.values())
    check(len(image) == q * q - q + 1, "image size failed")
    check(max(map(len, predecessors.values())) == q, "maximum fibre failed")
    max_targets = {target for target in states if len(predecessors[target]) == q}
    check(max_targets == {(minus_one, zero)}, "maximum fibre is not unique")

    expected_root_predecessors = {(x, minus_one) for x in range(q)}
    check(predecessors[(minus_one, zero)] == expected_root_predecessors,
          "distinguished q-fibre has wrong predecessor set")
    check(predecessors[(zero, minus_one)] == {(minus_one, zero)},
          "cycle predecessor set failed")
    check(not predecessors[(minus_one, minus_one)], "exceptional leaf has a predecessor")
    for a in parameters:
        level3 = (minus_one, field.neg(field.add(one, a)))
        level2 = (field.neg(field.add(one, a)), a)
        level1 = (a, minus_one)
        check(predecessors[level1] == {level2}, "level-one predecessor failed")
        check(predecessors[level2] == {level3}, "level-two predecessor failed")
        check(not predecessors[level3], "level-three point is not a leaf")

    return {
        "name": field.name,
        "q": q,
        "states": q * q,
        "recurrent": q * q - 3 * q + 5,
        "image": q * q - q + 1,
        "roots": roots,
        "cycles": expected_cycle_counts,
    }


def main():
    fields = [PrimeField(prime) for prime in primes_up_to(101) if prime % 2]
    fields += [
        ExtensionField("F9", 3, (1, 0, 1)),
        ExtensionField("F25", 5, (2, 0, 1)),
        ExtensionField("F27", 3, (1, 2, 0, 1)),
        ExtensionField("F49", 7, (1, 0, 1)),
        ExtensionField("F121", 11, (1, 0, 1)),
        ExtensionField("F125", 5, (1, 1, 0, 1)),
    ]
    profiles = [run_field(field) for field in fields]
    total_cells = sum(profile["states"] for profile in profiles)
    check(len(fields) == 31, "field-box count changed")
    check(total_cells == 110095, "state/target-cell count changed")

    print("P150_ZERO_TOTALIZED_LYNESS_EXACT_CONTROL")
    print("SCOPE=all_odd_prime_fields_through_F101_plus_F9_F25_F27_F49_F121_F125")
    for profile in profiles:
        cycles = "/".join(
            f"C{period}:{profile['cycles'][period]}" for period in sorted(profile["cycles"])
        )
        print(
            f"FIELD|name={profile['name']}|q={profile['q']}|states={profile['states']}|"
            f"recurrent={profile['recurrent']}|image={profile['image']}|"
            f"roots={profile['roots']}|cycles={cycles}"
        )
    print(f"TOTAL_FIELDS={len(fields)}")
    print(f"TOTAL_STATE_TARGET_CELLS={total_cells}")
    print(f"TOTAL_ASSERTIONS={ASSERTIONS}")
    print("ENUMERATION_IS_NOT_PROOF=1")
    print("HOLD_EXTERNAL=1")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
