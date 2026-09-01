#!/usr/bin/env python3
"""Exact falsifier for the P147--P151 replacement algebraic lane.

Eight new literal systems are tested, together with the old DNT re-entry
control.  A sweep over parameters of one update counts as one system.  All
arithmetic is exact and uses only the Python standard library.  Exhaustive
finite enumeration is counterexample pressure, not proof or novelty evidence.
"""

from collections import Counter
from itertools import product
from math import gcd, prod


ASSERTIONS = 0
RESULTS = []


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def compact(value):
    if isinstance(value, dict):
        return "/".join(f"{key}:{value[key]}" for key in sorted(value))
    if isinstance(value, (tuple, list)):
        return "/".join(compact(item) for item in value)
    return str(value).replace(" ", "_")


def record(handle, carrier, scope, start, signal, decision, reason, **metrics):
    RESULTS.append(
        {
            "id": handle,
            "carrier": carrier,
            "scope": scope,
            "assertions": ASSERTIONS - start,
            "signal": signal,
            "decision": decision,
            "reason": reason,
            "metrics": metrics,
        }
    )


def orbit_data(states, step):
    states = tuple(states)
    state_set = set(states)
    check(len(state_set) == len(states), "carrier contains duplicate states")
    nxt = {}
    for state in states:
        image = step(state)
        check(image in state_set, "literal map left its declared carrier")
        nxt[state] = image
    fibres = Counter(nxt.values())
    tails = Counter()
    periods = Counter()
    recurrent = set()
    point_data = {}
    for state in states:
        seen = {}
        order = []
        current = state
        while current not in seen:
            seen[current] = len(order)
            order.append(current)
            current = nxt[current]
        tail = seen[current]
        period = len(order) - tail
        check(period >= 1, "orbit failed to enter a cycle")
        check(nxt[order[-1]] == current, "orbit did not close")
        check(all(item in state_set for item in order), "orbit left carrier")
        tails[tail] += 1
        periods[period] += 1
        recurrent.update(order[tail:])
        point_data[state] = (tail, period)
    return {
        "nxt": nxt,
        "fibres": fibres,
        "point_data": point_data,
        "states": len(states),
        "tails": dict(sorted(tails.items())),
        "periods": dict(sorted(periods.items())),
        "recurrent": len(recurrent),
        "fixed": sum(nxt[state] == state for state in states),
        "image": len(fibres),
        "max_fibre": max(fibres.values(), default=0),
        "max_tail": max(tails, default=0),
        "max_period": max(periods, default=0),
    }


def primes_up_to(bound):
    output = []
    for candidate in range(2, bound + 1):
        if all(candidate % prime for prime in output if prime * prime <= candidate):
            output.append(candidate)
    return output


def valuation(value, prime, cap):
    if value == 0:
        return cap
    exponent = 0
    while exponent < cap and value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def ceil_log_two_ratio(numerator, denominator):
    check(numerator >= denominator >= 1, "invalid logarithmic clock")
    steps = 0
    value = denominator
    while value < numerator:
        value *= 2
        steps += 1
    return steps


# ---------------------------------------------------------------------------
# Small exact finite fields used to pressure-test extension-field uniformity.


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
    """F_p[u]/(modulus), elements encoded by base-p coefficient words."""

    def __init__(self, name, prime, modulus):
        self.name = name
        self.p = prime
        self.modulus = tuple(modulus)
        self.degree = len(self.modulus) - 1
        self.q = prime ** self.degree
        self.zero = 0
        self.one = 1
        check(self.degree in (2, 3), "extension verifier supports degrees two/three")
        check(self.modulus[-1] == 1, "extension modulus is not monic")
        for root in range(prime):
            value = 0
            for coefficient in reversed(self.modulus):
                value = (value * root + coefficient) % prime
            check(value != 0, "declared quadratic/cubic modulus has a base-field root")
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
            check(self.power(value, self.q) == value, "Frobenius field identity failed")
            if value:
                check(self.mul(value, self.inv0(value)) == self.one,
                      "extension-field inverse failed")

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


# ---------------------------------------------------------------------------
# ZTL: zero-totalized Lyness 5-map.


def run_ztl():
    start = ASSERTIONS
    fields = [PrimeField(prime) for prime in primes_up_to(43) if prime % 2]
    fields += [
        ExtensionField("F9", 3, (1, 0, 1)),
        ExtensionField("F25", 5, (2, 0, 1)),
        ExtensionField("F27", 3, (1, 2, 0, 1)),
        ExtensionField("F49", 7, (1, 0, 1)),
    ]
    total_states = 0
    profiles = []
    for field in fields:
        q = field.q
        zero, one = field.zero, field.one
        minus_one = field.neg(one)
        states = tuple(product(range(q), repeat=2))

        def step(state):
            x, y = state
            return (y, field.mul(field.add(one, y), field.inv0(x)))

        data = orbit_data(states, step)
        axes = {(zero, a) for a in range(q)} | {(a, zero) for a in range(q)}
        generic = {
            (x, y) for x, y in states
            if x != zero and y != zero
            and field.add(x, one) != zero
            and field.add(y, one) != zero
            and field.add(field.add(x, y), one) != zero
        }
        tail_one = {(a, minus_one) for a in range(q) if a != zero}
        parameters = tuple(a for a in range(q) if a not in (zero, minus_one))
        tail_two = {
            (field.neg(field.add(one, a)), a) for a in parameters
        }
        tail_three = {
            (minus_one, field.neg(field.add(one, a))) for a in parameters
        }
        check(len(generic) == (q - 2) * (q - 3), "ZTL generic-locus count failed")
        check(len(axes) == 2 * q - 1, "ZTL axis count failed")
        check(len(tail_one) == q - 1 and len(tail_two) == len(tail_three) == q - 2,
              "ZTL exceptional-tree layer count failed")
        pieces = [generic, axes, tail_one, tail_two, tail_three]
        check(sum(len(piece) for piece in pieces) == q * q,
              "ZTL displayed strata have wrong total size")
        for i, left in enumerate(pieces):
            for right in pieces[i + 1:]:
                check(left.isdisjoint(right), "ZTL displayed strata overlap")
        check(set().union(*pieces) == set(states), "ZTL strata do not cover the plane")

        for state in generic:
            current = state
            for _ in range(5):
                current = step(current)
            check(current == state, "ZTL lost Lyness five-periodicity on the open locus")
        for a in parameters:
            t1 = (a, minus_one)
            t2 = (field.neg(field.add(one, a)), a)
            t3 = (minus_one, field.neg(field.add(one, a)))
            check(step(t3) == t2 and step(t2) == t1 and step(t1) == (minus_one, zero),
                  "ZTL exceptional length-three chain failed")
        check(step((minus_one, minus_one)) == (minus_one, zero),
              "ZTL exceptional length-one leaf failed")
        check(step((minus_one, zero)) == (zero, minus_one)
              and step((zero, minus_one)) == (minus_one, zero),
              "ZTL exceptional two-cycle failed")

        roots = sum(
            field.sub(field.sub(field.mul(a, a), a), one) == zero
            for a in range(q)
        )
        expected_tails = {0: q * q - 3 * q + 5, 1: q - 1, 2: q - 2, 3: q - 2}
        expected_periods = {
            1: 1 + roots,
            2: 3 * q - 1,
            4: 2 * q - 6,
            5: (q - 2) * (q - 3) - roots,
        }
        expected_periods = {key: value for key, value in expected_periods.items() if value}
        check(data["tails"] == expected_tails, "ZTL temporal polynomial failed")
        check(data["periods"] == expected_periods, "ZTL point-period census failed")
        check(data["fixed"] == 1 + roots, "ZTL fixed-point census failed")
        check(data["recurrent"] == q * q - 3 * q + 5,
              "ZTL recurrent-point census failed")
        check(data["max_tail"] == 3 and data["max_period"] <= 5,
              "ZTL sharp clock or period bound failed")
        check(((q - 2) * (q - 3) - roots) % 5 == 0,
              "ZTL exact-five points do not form cycles")

        for target in states:
            u, v = target
            if u == minus_one and v == zero:
                expected_fibre = q
            elif u == minus_one:
                expected_fibre = 0
            else:
                expected_fibre = 1
            check(data["fibres"].get(target, 0) == expected_fibre,
                  "ZTL every-target fibre law failed")
        check(data["image"] == q * q - q + 1 and data["max_fibre"] == q,
              "ZTL image or maximum fibre failed")
        for state in states:
            if state in generic or state in axes:
                expected_tail = 0
            elif state in tail_one:
                expected_tail = 1
            elif state in tail_two:
                expected_tail = 2
            else:
                expected_tail = 3
            check(data["point_data"][state][0] == expected_tail,
                  "ZTL pointwise tail classification failed")

        total_states += q * q
        profiles.append(
            f"{field.name}:S{q*q}:R{data['recurrent']}:I{data['image']}:"
            f"F{data['fixed']}:C4{(q-3)//2}:C5{((q-2)*(q-3)-roots)//5}"
        )
    record(
        "ZTL", "affine_planes_over_odd_finite_fields",
        "13 odd prime fields through F43 plus F9/F25/F27/F49; (x,y)->(y,(1+y)inv0(x))",
        start,
        "complete graph decomposition, sharp three-step exceptional tree, periods 1/2/4/5, zeta-ready cycle census, and every-target fibres 0/1/q",
        "SELECT_REPLACEMENT_OWNER_PENDING",
        "classical Lyness five-periodicity is zero credit; the surviving all-affine singular-boundary graph package is paper-sized if the bounded owner miss survives specialist review",
        boxes=len(fields), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# RIC: zero-totalized reciprocal increment x -> x + inv0(x).


def run_ric():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    for prime in (p for p in primes_up_to(97) if p % 2):
        states = tuple(range(prime))

        def inverse_zero(value):
            return 0 if value == 0 else pow(value, prime - 2, prime)

        def step(value):
            return (value + inverse_zero(value)) % prime

        data = orbit_data(states, step)
        check(data["fixed"] == 1 and data["nxt"][0] == 0,
              "RIC zero should be the unique fixed point")
        for target in states:
            discriminant = (target * target - 4) % prime
            if discriminant == 0:
                quadratic_roots = 1
            elif pow(discriminant, (prime - 1) // 2, prime) == 1:
                quadratic_roots = 2
            else:
                quadratic_roots = 0
            expected = quadratic_roots + (1 if target == 0 else 0)
            check(data["fibres"].get(target, 0) == expected,
                  "RIC discriminant fibre law failed")
        check(data["max_fibre"] <= 3, "RIC acquired a fibre larger than three")
        total_states += prime
        if prime in (3, 5, 7, 13, 23, 43, 97):
            profiles.append(
                f"p{prime}:I{data['image']}:T{data['max_tail']}:P{data['max_period']}:"
                f"D{compact(data['tails'])}"
            )
    record(
        "RIC", "odd_prime_fields",
        "all odd primes p<=97; x->x+inv0(x)", start,
        "exact quadratic-discriminant inverse atlas but strongly field-dependent tails and cycles",
        "KILL_DIRECT_OWNER",
        "the same rational family x+x^{-1} already has direct finite-field functional-graph owners; changing the projective boundary to inv0(0)=0 leaves only a trivial boundary splice",
        boxes=len(tuple(p for p in primes_up_to(97) if p % 2)), states=total_states,
        profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# NID: Newton idempotent lifting on the two Hensel residue balls.


def run_nid():
    start = ASSERTIONS
    boxes = (
        tuple((5, exponent) for exponent in range(2, 7))
        + tuple((7, exponent) for exponent in range(2, 6))
        + tuple((11, exponent) for exponent in range(2, 5))
        + tuple((13, exponent) for exponent in range(2, 5))
    )
    total_states = 0
    profiles = []
    for prime, exponent in boxes:
        modulus = prime ** exponent
        states = tuple(value for value in range(modulus) if value % prime in (0, 1))

        def step(value):
            return (3 * value * value - 2 * value * value * value) % modulus

        data = orbit_data(states, step)
        expected_depths = Counter({0: 2})
        for a in range(1, exponent):
            depth = ceil_log_two_ratio(exponent, a)
            expected_depths[depth] += 2 * (prime - 1) * prime ** (exponent - a - 1)
        check(data["tails"] == dict(sorted(expected_depths.items())),
              "NID temporal polynomial failed")
        check(data["fixed"] == data["recurrent"] == 2,
              "NID should absorb at exactly 0 and 1")
        check(data["max_period"] == 1,
              "NID acquired a nontrivial recurrent cycle")
        check(data["max_tail"] == ceil_log_two_ratio(exponent, 1),
              "NID sharp logarithmic clock failed")
        for value in states:
            if value in (0, 1):
                expected_tail = 0
            else:
                error = value if value % prime == 0 else (1 - value) % modulus
                a = valuation(error, prime, exponent)
                expected_tail = ceil_log_two_ratio(exponent, a)
                image = step(value)
                image_error = image if image % prime == 0 else (1 - image) % modulus
                check(valuation(image_error, prime, exponent) == min(exponent, 2 * a),
                      "NID failed to double the idempotent-error valuation")
            check(data["point_data"][value] == (expected_tail, 1),
                  "NID pointwise absorption time failed")
        total_states += len(states)
        profiles.append(
            f"p{prime}e{exponent}:S{len(states)}:T{data['max_tail']}:"
            f"D{compact(data['tails'])}"
        )
    record(
        "NID", "two_idempotent_residue_balls_in_Z_mod_p^e",
        "p in {5,7,11,13}, displayed exponents 2..6; x->3x^2-2x^3", start,
        "exact valuation-doubling clock with sharp ceil(log_2 e) absorption at 0/1",
        "KILL_DIRECT_ALGORITHM_OWNER",
        "this polynomial is the standard Newton/idempotent-lifting iteration and precision doubling is its classical purpose",
        boxes=len(boxes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# RDC: radical complement on the full divisor set of N.


def run_rdc():
    start = ASSERTIONS
    exponent_boxes = (
        (1,), (2,), (3,), (4,), (1, 1), (1, 2), (2, 2), (1, 3),
        (2, 3), (1, 2, 4), (2, 3, 4), (1, 1, 2, 3), (1, 2, 3, 4),
    )
    primes = (2, 3, 5, 7, 11)
    total_states = 0
    profiles = []
    for exponents in exponent_boxes:
        local_primes = primes[:len(exponents)]
        states = tuple(product(*(range(exponent + 1) for exponent in exponents)))
        modulus = prod(prime ** exponent for prime, exponent in zip(local_primes, exponents))

        def encode(state):
            return prod(prime ** a for prime, a in zip(local_primes, state))

        def step(state):
            return tuple(exponent if a == 0 else exponent - 1
                         for a, exponent in zip(state, exponents))

        data = orbit_data(states, step)
        for state in states:
            divisor = encode(state)
            radical = prod(prime for prime, a in zip(local_primes, state) if a > 0)
            check(encode(step(state)) == modulus // radical,
                  "RDC exponent update is not the literal N/rad(d) map")
        squarefree_coordinates = sum(exponent == 1 for exponent in exponents)
        thick = tuple(exponent for exponent in exponents if exponent >= 2)
        recurrent = 2 ** squarefree_coordinates
        if thick:
            expected_tails = {
                0: recurrent,
                1: recurrent * (prod(thick) - 1),
                2: recurrent * (prod(exponent + 1 for exponent in thick) - prod(thick)),
            }
            expected_tails = {key: value for key, value in expected_tails.items() if value}
            expected_max_tail = 2
        else:
            expected_tails = {0: recurrent}
            expected_max_tail = 0
        check(data["tails"] == expected_tails, "RDC temporal polynomial failed")
        check(data["recurrent"] == recurrent and data["max_tail"] == expected_max_tail,
              "RDC recurrent census or sharp clock failed")
        if squarefree_coordinates:
            check(data["fixed"] == 0 and data["max_period"] == 2,
                  "RDC squarefree coordinates should force two-cycles")
        else:
            check(data["fixed"] == 1 and data["max_period"] == 1,
                  "RDC thick coordinates should have one fixed point")
        for target in states:
            expected_fibre = 1
            admissible = True
            for b, exponent in zip(target, exponents):
                if b == exponent:
                    factor = 1
                elif b == exponent - 1:
                    factor = exponent
                else:
                    admissible = False
                    factor = 0
                expected_fibre *= factor
            if not admissible:
                expected_fibre = 0
            check(data["fibres"].get(target, 0) == expected_fibre,
                  "RDC every-target product fibre failed")
        check(data["image"] == 2 ** len(exponents),
              "RDC Boolean-corner image failed")
        check(data["max_fibre"] == prod(exponents),
              "RDC maximum fibre failed")
        total_states += len(states)
        profiles.append(
            f"e{compact(exponents)}:S{len(states)}:R{recurrent}:I{data['image']}:"
            f"T{data['max_tail']}:MF{data['max_fibre']}"
        )
    record(
        "RDC", "positive_divisors_of_fixed_integers",
        "13 prime-exponent boxes; d->N/rad(d) on d|N", start,
        "exact fixed/two-cycle product, two-step temporal polynomial, Boolean-corner image, and every-target multiplicative fibres",
        "KILL_THEOREM_THIN",
        "the coordinate theorem is complete but definition-level and has clock at most two; it cannot carry a paper after radical/squarefree-kernel background is subtracted",
        boxes=len(exponent_boxes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# DLV: conservative quadratic Lotka--Volterra Euler map.


def run_dlv():
    start = ASSERTIONS
    tested_primes = tuple(p for p in primes_up_to(43) if p % 2)
    total_states = 0
    profiles = []
    nontrivial_cycle_seen = False
    for prime in tested_primes:
        states = tuple(product(range(prime), repeat=2))

        def step(state):
            x, y = state
            return (x * (1 + y) % prime, y * (1 - x) % prime)

        data = orbit_data(states, step)
        check(data["fixed"] == 2 * prime - 1,
              "DLV coordinate-axis fixed census failed")
        check(data["image"] == prime * (prime + 1) // 2,
              "DLV quadratic image size failed")
        check(data["max_fibre"] == 2, "DLV fibre exceeded quadratic degree")
        for state in states:
            image = step(state)
            check(sum(state) % prime == sum(image) % prime,
                  "DLV failed to preserve x+y")
            x, y = state
            total = (x + y) % prime
            check(image[0] == x * (1 + total - x) % prime,
                  "DLV invariant-line quadratic reduction failed")
        for target in states:
            u, v = target
            total = (u + v) % prime
            discriminant = ((1 + total) ** 2 - 4 * u) % prime
            if discriminant == 0:
                expected = 1
            elif pow(discriminant, (prime - 1) // 2, prime) == 1:
                expected = 2
            else:
                expected = 0
            check(data["fibres"].get(target, 0) == expected,
                  "DLV every-target discriminant fibre failed")
        nontrivial_cycle_seen |= data["max_period"] > 1
        total_states += prime * prime
        profiles.append(
            f"p{prime}:R{data['recurrent']}:I{data['image']}:"
            f"T{data['max_tail']}:P{data['max_period']}"
        )
    check(nontrivial_cycle_seen, "DLV scout never produced a nontrivial cycle")
    record(
        "DLV", "affine_planes_over_odd_prime_fields",
        "all odd primes p<=43; (x,y)->(x(1+y),y(1-x))", start,
        "conserved x+y, exact discriminant inverse atlas, coordinate-axis fixed set, and field-dependent nontrivial cycles",
        "KILL_GENERIC_QUADRATIC_FOLIATION",
        "on each invariant line the map is the one-variable quadratic x->x(1+s-x); a uniform graph theorem would solve an owner-dense parameter family rather than exploit a new finite-system mechanism",
        boxes=len(tested_primes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# OTL: zero-totalized third-order Lyness map (a same-root negative control).


def run_otl():
    start = ASSERTIONS
    fields = [PrimeField(prime) for prime in primes_up_to(31) if prime % 2]
    fields += [
        ExtensionField("F9", 3, (1, 0, 1)),
        ExtensionField("F25", 5, (2, 0, 1)),
    ]
    total_states = 0
    profiles = []
    for field in fields:
        q = field.q
        zero, one = field.zero, field.one
        states = tuple(product(range(q), repeat=3))

        def step(state):
            x, y, z = state
            return (y, z, field.mul(field.add(one, field.add(y, z)),
                                    field.inv0(x)))

        def lyness(state):
            x, y = state
            return (y, field.mul(field.add(one, y), field.inv0(x)))

        data = orbit_data(states, step)
        generic = set()
        for x, y, z in states:
            a = field.add(one, field.add(y, z))
            b = field.add(field.add(field.mul(x, z), x),
                          field.add(field.add(y, z), one))
            c = field.add(one, field.add(x, y))
            if all(value != zero for value in (x, y, z, a, b, c)):
                generic.add((x, y, z))
        check(len(generic) == q ** 3 - 6 * q * q + 14 * q - 11,
              "OTL generic-locus count failed")
        for state in generic:
            current = state
            for _ in range(8):
                current = step(current)
            check(current == state and data["point_data"][state][0] == 0,
                  "OTL open locus lost eight-periodicity")
        expected_tails = {
            0: q ** 3 - 3 * q * q + 2 * q + 5,
            1: 2 * q - 2,
            2: 2 * q - 3,
            3: (q - 2) * (q + 1),
            4: q * (q - 2),
            5: (q - 2) * (q - 1),
        }
        check(data["tails"] == expected_tails, "OTL temporal polynomial failed")
        check(data["max_tail"] == 5 and data["recurrent"] == expected_tails[0],
              "OTL sharp clock or recurrent census failed")
        check(set(data["periods"]) <= {1, 2, 3, 4, 6, 8, 15},
              "OTL acquired an unclassified recurrent period")
        exact_eight = (q - 1) * (q - 2) * (q - 3)
        check(data["periods"].get(8, 0) == exact_eight,
              "OTL exact-eight census failed")
        for a, b in product(range(q), repeat=2):
            current = (a, b, zero)
            for _ in range(3):
                current = step(current)
            lower = lyness(lyness((a, b)))
            check(current == (lower[0], lower[1], zero),
                  "OTL zero slice did not reduce to two Lyness steps")
        for target in states:
            u, v, w = target
            coefficient = field.add(one, field.add(u, v))
            if coefficient == zero and w == zero:
                expected_fibre = q
            elif coefficient != zero:
                expected_fibre = 1
            else:
                expected_fibre = 0
            check(data["fibres"].get(target, 0) == expected_fibre,
                  "OTL every-target fibre law failed")
        check(data["image"] == q ** 3 - q * (q - 1)
              and data["max_fibre"] == q,
              "OTL image or maximum fibre failed")
        total_states += q ** 3
        profiles.append(
            f"{field.name}:S{q**3}:R{data['recurrent']}:I{data['image']}:"
            f"T{data['max_tail']}:P{data['max_period']}:C8{exact_eight//8}"
        )
    record(
        "OTL", "affine_three_spaces_over_odd_finite_fields",
        "odd prime fields through F31 plus F9/F25; (x,y,z)->(y,z,(1+y+z)inv0(x))",
        start,
        "sharp depth five, periods among 1/2/3/4/6/8/15, exact period-eight open locus, and 0/1/q inverse atlas",
        "KILL_INTERNAL_ZTL_ROOT_COLLISION",
        "the invariant zero slice satisfies T^3(a,b,0)=(L^2(a,b),0) for the selected ZTL map L, so the striking period-15 boundary is literally the same Lyness root rather than a second system",
        boxes=len(fields), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# GAE: gcd addition, a literal conjugate of P100 digit erasure.


def run_gae():
    start = ASSERTIONS
    boxes = (
        tuple((2, exponent) for exponent in range(1, 11))
        + tuple((3, exponent) for exponent in range(1, 8))
        + tuple((5, exponent) for exponent in range(1, 6))
        + tuple((7, exponent) for exponent in range(1, 5))
    )
    total_states = 0
    profiles = []
    for prime, exponent in boxes:
        modulus = prime ** exponent
        states = tuple(range(modulus))

        def step(value):
            return 0 if value == 0 else (value + gcd(value, modulus)) % modulus

        data = orbit_data(states, step)
        expected_depths = Counter()
        for value in states:
            conjugate = (-value) % modulus
            digits = []
            work = conjugate
            for _ in range(exponent):
                digits.append(work % prime)
                work //= prime
            expected_tail = sum(digits)
            expected_depths[expected_tail] += 1
            check(data["point_data"][value] == (expected_tail, 1),
                  "GAE digit-sum clock failed")
            image_conjugate = (-step(value)) % modulus
            if conjugate:
                check(image_conjugate == conjugate - prime ** valuation(
                    conjugate, prime, exponent),
                    "GAE failed its explicit conjugacy to P100 erasure")
        check(data["tails"] == dict(sorted(expected_depths.items())),
              "GAE temporal polynomial failed")
        check(data["max_tail"] == exponent * (prime - 1),
              "GAE sharp digit-sum clock failed")
        for target in states:
            y = (-target) % modulus
            if y == 0:
                expected_fibre = exponent + 1
            else:
                b = valuation(y, prime, exponent)
                digit = (y // (prime ** b)) % prime
                expected_fibre = b + (digit < prime - 1)
            check(data["fibres"].get(target, 0) == expected_fibre,
                  "GAE every-target fibre law failed")
        check(data["image"] == modulus - prime ** (exponent - 1)
              and data["max_fibre"] == exponent + 1,
              "GAE image or maximum fibre failed")
        total_states += modulus
        if (prime, exponent) in ((2, 10), (3, 7), (5, 5), (7, 4)):
            profiles.append(
                f"p{prime}e{exponent}:S{modulus}:I{data['image']}:"
                f"T{data['max_tail']}:MF{data['max_fibre']}"
            )
    record(
        "GAE", "prime_power_residue_rings",
        "p=2,3,5,7 through exponents 10,7,5,4; x->x+gcd(x,p^e) mod p^e",
        start,
        "digit-sum absorption, full temporal polynomial, image size, and every-target fibres",
        "KILL_EXACT_CONJUGACY_P100",
        "negation x->-x conjugates the literal map exactly to P100's least-valuation digit erasure y->y-p^v_p(y); all quantitative axes transfer",
        boxes=len(boxes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# QNC: quadratic collapse on the nilradical of Z/p^e Z.


def square_root_count_prime_power(delta, prime, exponent):
    if exponent == 0:
        return 1
    modulus = prime ** exponent
    delta %= modulus
    order = valuation(delta, prime, exponent)
    if order == exponent:
        return prime ** (exponent // 2)
    if order % 2:
        return 0
    half = order // 2
    unit = delta // (prime ** order)
    if pow(unit % prime, (prime - 1) // 2, prime) != 1:
        return 0
    return 2 * prime ** half


def run_qnc():
    start = ASSERTIONS
    boxes = (
        tuple((3, exponent) for exponent in range(2, 9))
        + tuple((5, exponent) for exponent in range(2, 7))
        + tuple((7, exponent) for exponent in range(2, 6))
        + tuple((11, exponent) for exponent in range(2, 5))
        + tuple((13, exponent) for exponent in range(2, 5))
    )
    total_states = 0
    profiles = []
    for prime, exponent in boxes:
        modulus = prime ** exponent
        states = tuple(range(0, modulus, prime))

        def step(value):
            return value * (value + prime) % modulus

        data = orbit_data(states, step)
        if exponent == 2:
            expected_tails = {0: 1, 1: prime - 1}
        else:
            expected_tails = {0: 1, 1: 2 * prime - 1}
            for depth in range(2, exponent - 1):
                expected_tails[depth] = 2 * (prime - 1) * prime ** (depth - 1)
            expected_tails[exponent - 1] = (prime - 2) * prime ** (exponent - 2)
        check(data["tails"] == expected_tails,
              "QNC temporal polynomial failed")
        check(data["fixed"] == data["recurrent"] == 1
              and data["max_tail"] == exponent - 1,
              "QNC unique absorber or sharp clock failed")
        for value in states:
            if value == 0:
                expected_tail = 0
            else:
                a = valuation(value, prime, exponent)
                if a >= 2:
                    expected_tail = exponent - a
                    check(valuation(step(value), prime, exponent)
                          == min(exponent, a + 1),
                          "QNC high-valuation increment failed")
                else:
                    unit = value // prime
                    b = valuation(unit + 1, prime, exponent - 2)
                    expected_tail = exponent - 1 - b
            check(data["point_data"][value] == (expected_tail, 1),
                  "QNC pointwise absorption clock failed")
        root_exponent = exponent - 2
        root_modulus = prime ** root_exponent
        for target in states:
            if target % (prime * prime):
                expected_fibre = 0
            else:
                w = (target // (prime * prime)) % root_modulus
                delta = (1 + 4 * w) % root_modulus
                expected_fibre = prime * square_root_count_prime_power(
                    delta, prime, root_exponent)
            check(data["fibres"].get(target, 0) == expected_fibre,
                  "QNC every-target square-root fibre law failed")
        square_images = 1 + (prime - 1) * sum(
            prime ** (root_exponent - 2 * r - 1)
            for r in range((root_exponent - 1) // 2 + 1)
        ) // 2 if root_exponent else 1
        check(data["image"] == square_images, "QNC square-image census failed")
        if root_exponent % 2 == 0:
            expected_max = prime ** (root_exponent // 2 + 1)
        else:
            expected_max = 2 * prime ** ((root_exponent - 1) // 2 + 1)
        check(data["max_fibre"] == expected_max,
              "QNC sharp maximum fibre failed")
        total_states += len(states)
        profiles.append(
            f"p{prime}e{exponent}:S{len(states)}:I{data['image']}:"
            f"T{data['max_tail']}:MF{data['max_fibre']}"
        )
    record(
        "QNC", "nilradicals_pZ_mod_p^e_of_odd_prime_power_rings",
        "p in {3,5,7,11,13}, exponents through 8; x->x(x+p) mod p^e",
        start,
        "sharp (e-1)-step absorption with full depth polynomial plus a discriminant/square-root every-target fibre atlas and parity-sensitive maximum fibre",
        "RESERVE_SECOND_PAPER_SIZED_OWNER_PENDING",
        "the valuation clock and singular quadratic-congruence inverse axis are independent and no exact-map owner was found in the bounded primary-source search; specialist local-ring dynamics audit remains mandatory",
        boxes=len(boxes), states=total_states, profiles=";".join(profiles),
    )


# ---------------------------------------------------------------------------
# DNT re-entry control: H -> N_G(H) on all subgroups of a dihedral 2-group.


def dihedral_mul(left, right, order):
    a, b = left
    c, d = right
    return ((a + (c if b == 0 else -c)) % order, (b + d) % 2)


def dihedral_inv(element, order):
    a, b = element
    return ((-a) % order, 0) if b == 0 else (a, 1)


def dihedral_conjugate(g, h, order):
    return dihedral_mul(dihedral_mul(g, h, order), dihedral_inv(g, order), order)


def dihedral_subgroups(power):
    order = 1 << power
    entries = []
    for k in range(power + 1):
        step = 1 << k
        rotations = frozenset((value, 0) for value in range(0, order, step))
        entries.append((("R", k, 0), rotations))
    for k in range(power + 1):
        step = 1 << k
        for shift in range(step):
            rotations = {(value, 0) for value in range(0, order, step)}
            reflections = {((shift + value) % order, 1)
                           for value in range(0, order, step)}
            entries.append((("H", k, shift), frozenset(rotations | reflections)))
    return entries


def run_dnt():
    start = ASSERTIONS
    total_states = 0
    profiles = []
    for power in range(1, 9):
        order = 1 << power
        group = tuple((a, b) for b in (0, 1) for a in range(order))
        entries = dihedral_subgroups(power)
        key_to_group = dict(entries)
        group_to_key = {value: key for key, value in entries}
        check(len(key_to_group) == len(group_to_key) == 2 * order + power,
              "DNT subgroup classifier has duplicates or omissions")
        full_key = ("H", 0, 0)
        literal_next = {}
        for key, subgroup in entries:
            normalizer = frozenset(
                element for element in group
                if all(dihedral_conjugate(element, h, order) in subgroup for h in subgroup)
            )
            check(normalizer in group_to_key, "DNT normalizer left classified carrier")
            literal_next[key] = group_to_key[normalizer]
            kind, k, shift = key
            predicted = full_key if kind == "R" or k == 0 else (
                "H", k - 1, shift % (1 << (k - 1))
            )
            check(literal_next[key] == predicted,
                  "DNT normalizer-halving formula failed")
            check(subgroup <= normalizer, "DNT update is not inflationary")
        data = orbit_data(key_to_group, literal_next.__getitem__)
        expected_depths = Counter({0: 1, 1: power + 1})
        for k in range(1, power + 1):
            expected_depths[k] += 1 << k
        check(data["tails"] == dict(sorted(expected_depths.items())),
              "DNT temporal polynomial failed")
        check(data["fixed"] == data["recurrent"] == 1,
              "DNT should have the full group as unique recurrent point")
        check(data["max_tail"] == power and data["max_period"] == 1,
              "DNT sharp clock failed")
        for target in key_to_group:
            kind, k, _ = target
            if target == full_key:
                expected = power + 4
            elif kind == "H" and 1 <= k <= power - 1:
                expected = 2
            else:
                expected = 0
            check(data["fibres"].get(target, 0) == expected,
                  "DNT every-target fibre law failed")
        check(data["image"] == order - 1, "DNT image census failed")
        total_states += len(entries)
        profiles.append(
            f"m{power}:S{len(entries)}:I{data['image']}:T{data['max_tail']}:"
            f"FG{data['fibres'][full_key]}"
        )
    record(
        "DNT", "all_subgroups_of_dihedral_2_groups",
        "1<=m<=8; H->N_G(H) in D_(2^(m+1))", start,
        "replayed sharp m-step normalizer tower, temporal polynomial, image, and every-target fibres",
        "KILL_REENTRY_DIRECT_OWNER",
        "re-entry value is low: successive normalizers are the literal classical problem and the exact theorem is a mechanical join of the owned dihedral subgroup classifier with an elementary conjugation calculation",
        boxes=8, states=total_states, profiles=";".join(profiles),
    )


def main():
    run_ztl()
    run_ric()
    run_nid()
    run_rdc()
    run_dlv()
    run_otl()
    run_gae()
    run_qnc()
    run_dnt()
    check(len(RESULTS) == 9, "audit did not emit eight new systems plus DNT")
    check({row["id"] for row in RESULTS} == {
        "ZTL", "RIC", "NID", "RDC", "DLV", "OTL", "GAE", "QNC", "DNT"
    },
          "audit handle set changed")
    check(sum(row["id"] != "DNT" for row in RESULTS) == 8,
          "new-system count is not eight")
    print("ALGEBRAIC_REPLACEMENT_EXACT_AUDIT")
    for row in RESULTS:
        fields = [
            "SYSTEM",
            f"id={row['id']}",
            f"carrier={row['carrier']}",
            f"assertions={row['assertions']}",
            f"scope={compact(row['scope'])}",
            f"signal={compact(row['signal'])}",
            f"decision={row['decision']}",
            f"reason={compact(row['reason'])}",
        ]
        fields.extend(f"{key}={compact(value)}" for key, value in row["metrics"].items())
        print("|".join(fields))
    print(f"TOTAL_ASSERTIONS={ASSERTIONS}")
    print("NEW_LITERAL_SYSTEMS=8")
    print("REENTRY_CONTROLS=1")
    print("ENUMERATION_IS_NOT_PROOF=1")
    print("HOLD_EXTERNAL=1")


if __name__ == "__main__":
    main()
