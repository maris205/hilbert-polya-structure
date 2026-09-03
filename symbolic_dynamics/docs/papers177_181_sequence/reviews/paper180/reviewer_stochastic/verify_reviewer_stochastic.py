#!/usr/bin/env python3
"""Independent hostile verifier for P180 over genuine extension fields.

Finite fields are built here as polynomial quotients.  Bilinear forms use
several invertible matrices, including nonsymmetric shears.  Functional-graph
tails are recovered by indegree peeling and reverse propagation rather than
the author's per-start orbit walk.  No project code or third-party package is
imported.  The finite boxes are exact falsification pressure, not proof.
"""

from collections import Counter, defaultdict, deque
from hashlib import sha256
from itertools import product
from math import gcd


ASSERTIONS = 0
ARROW_HASH = sha256()


def check(statement, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(label)


class QuotientField:
    """F_p[x]/(modulus), elements encoded by base-p coefficient digits."""

    def __init__(self, p, modulus, name):
        self.p = p
        self.modulus = tuple(coefficient % p for coefficient in modulus)
        self.degree = len(self.modulus) - 1
        self.q = p**self.degree
        self.name = name
        check(self.modulus[-1] == 1, f"{name} modulus monic")
        self._digits = tuple(self._decode_raw(value) for value in range(self.q))
        self.add_table = tuple(
            tuple(self._add_raw(a, b) for b in range(self.q))
            for a in range(self.q)
        )
        self.mul_table = tuple(
            tuple(self._mul_raw(a, b) for b in range(self.q))
            for a in range(self.q)
        )
        # These identities certify that the chosen quotient really is a field
        # in every declared box, instead of assuming irreducibility silently.
        for a in range(1, self.q):
            check(self.pow(a, self.q - 1) == 1, f"{name} Fermat a={a}")
            check(any(self.mul(a, b) == 1 for b in range(1, self.q)), f"{name} inverse a={a}")
        check(
            max(self.multiplicative_order(a) for a in range(1, self.q))
            == self.q - 1,
            f"{name} cyclic multiplicative group",
        )

    def _decode_raw(self, value):
        digits = []
        for _ in range(self.degree):
            digits.append(value % self.p)
            value //= self.p
        return tuple(digits)

    def _encode_raw(self, digits):
        value = 0
        place = 1
        for digit in digits:
            value += (digit % self.p) * place
            place *= self.p
        return value

    def _add_raw(self, a, b):
        return self._encode_raw(
            [(x + y) % self.p for x, y in zip(self._digits[a], self._digits[b])]
        )

    def _mul_raw(self, a, b):
        left = self._digits[a]
        right = self._digits[b]
        work = [0] * (2 * self.degree - 1)
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                work[i + j] = (work[i + j] + x * y) % self.p
        for power in range(len(work) - 1, self.degree - 1, -1):
            leading = work[power] % self.p
            if leading:
                offset = power - self.degree
                for j in range(self.degree):
                    work[offset + j] = (
                        work[offset + j] - leading * self.modulus[j]
                    ) % self.p
                work[power] = 0
        return self._encode_raw(work[: self.degree])

    def add(self, a, b):
        return self.add_table[a][b]

    def neg(self, a):
        return self._encode_raw([(-x) % self.p for x in self._digits[a]])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        return self.mul_table[a][b]

    def pow(self, base, exponent):
        answer = 1
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, base)
            base = self.mul(base, base)
            exponent //= 2
        return answer

    def multiplicative_order(self, element):
        check(element != 0, f"{self.name} order of zero")
        value = 1
        for order in range(1, self.q):
            value = self.mul(value, element)
            if value == 1:
                return order
        raise AssertionError(f"{self.name} missing multiplicative order")


def vectors(field, dimension):
    return tuple(product(range(field.q), repeat=dimension))


def determinant_2(field, matrix):
    return field.sub(
        field.mul(matrix[0][0], matrix[1][1]),
        field.mul(matrix[0][1], matrix[1][0]),
    )


def forms(field, dimension):
    if dimension == 1:
        return (("unit", ((1,),)),)
    zero, one = 0, 1
    alpha = field.p if field.degree > 1 else one
    identity = ((one, zero), (zero, one))
    shear = ((one, alpha), (zero, one))
    alternating = ((zero, one), (field.neg(one), zero))
    answer = (("identity", identity), ("shear", shear), ("alternating", alternating))
    for name, matrix in answer:
        check(determinant_2(field, matrix) != 0, f"{field.name} {name} nondegenerate")
    check(shear != tuple(zip(*shear)), f"{field.name} shear nonsymmetric")
    return answer


def bilinear(field, matrix, u, v):
    total = 0
    for i in range(len(u)):
        for j in range(len(v)):
            total = field.add(total, field.mul(field.mul(u[i], matrix[i][j]), v[j]))
    return total


def scale_pair(field, scalar, state):
    u, v = state
    return (
        tuple(field.mul(scalar, coordinate) for coordinate in u),
        tuple(field.mul(scalar, coordinate) for coordinate in v),
    )


def transition(field, matrix, state):
    return scale_pair(field, bilinear(field, matrix, *state), state)


def graph_tail_period(states, arrows):
    """Functional graph classification by Kahn peeling, then reverse DP."""
    indegree = Counter(arrows.values())
    queue = deque(state for state in states if indegree[state] == 0)
    peeled = []
    while queue:
        state = queue.popleft()
        peeled.append(state)
        target = arrows[state]
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)

    tail = {}
    period = {}
    remaining = {state for state in states if indegree[state] > 0}
    while remaining:
        start = next(iter(remaining))
        cycle = []
        state = start
        while True:
            cycle.append(state)
            state = arrows[state]
            if state == start:
                break
        length = len(cycle)
        for state in cycle:
            remaining.remove(state)
            tail[state] = 0
            period[state] = length

    for state in reversed(peeled):
        target = arrows[state]
        tail[state] = tail[target] + 1
        period[state] = period[target]
    check(len(tail) == len(states), "functional graph classification total")
    return tail, period


def integer_order(base, modulus):
    check(gcd(base, modulus) == 1, f"integer order undefined mod {modulus}")
    value = 1
    for order in range(1, 2 * modulus + 1):
        value = value * base % modulus
        if value == 1:
            return order
    raise AssertionError(f"integer order missing mod {modulus}")


def valuation_three(value):
    exponent = 0
    while value % 3 == 0:
        exponent += 1
        value //= 3
    return exponent, value


def tail_string(counter):
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def audit_box(field, dimension, form_name, matrix):
    vecs = vectors(field, dimension)
    states = tuple((u, v) for u in vecs for v in vecs)
    zero_vector = (0,) * dimension
    zero = (zero_vector, zero_vector)
    q = field.q
    Q = q ** (dimension - 1) * (q**dimension - 1)
    Z = q ** (2 * dimension - 1) + q**dimension - q ** (dimension - 1)

    levels = Counter(bilinear(field, matrix, *state) for state in states)
    check(levels[0] == Z, f"{field.name} m={dimension} {form_name} null cone")
    for value in range(1, q):
        check(levels[value] == Q, f"{field.name} m={dimension} level={value}")

    arrows = {}
    for state in states:
        target = transition(field, matrix, state)
        arrows[state] = target
        ARROW_HASH.update(
            f"{field.name}|{dimension}|{form_name}|{state}>{target}\n".encode("ascii")
        )
        check(target in states, f"{field.name} closure")

    # Literal forward iteration versus the radial closed form.  The exponent
    # is an ordinary integer even in characteristic two.
    endpoints = {state: state for state in states}
    fibre_profiles = []
    for time in range(0, 5):
        exponent = (3**time - 1) // 2
        for state in states:
            c = bilinear(field, matrix, *state)
            predicted = scale_pair(field, field.pow(c, exponent), state)
            actual = endpoints[state]
            check(actual == predicted, f"{field.name} closed iterate t={time}")
            check(
                bilinear(field, matrix, *actual) == field.pow(c, 3**time),
                f"{field.name} scalar cube t={time}",
            )
        if time == 0:
            fibres = Counter(endpoints.values())
            for target in states:
                check(fibres[target] == 1, f"{field.name} identity fibre target={target}")
            check(sum(fibres.values()) == len(states), f"{field.name} identity fibre mass")
        else:
            fibres = Counter(endpoints.values())
            g_t = gcd(3**time, q - 1)
            for target in states:
                d = bilinear(field, matrix, *target)
                if target == zero:
                    expected = Z
                elif d == 0:
                    expected = 0
                elif field.pow(d, (q - 1) // g_t) == 1:
                    expected = g_t
                else:
                    expected = 0
                check(
                    fibres[target] == expected,
                    f"{field.name} fibre m={dimension} t={time} target={target}",
                )
            check(sum(fibres.values()) == len(states), f"{field.name} fibre mass t={time}")
            fibre_profiles.append(len(fibres))
        if time < 4:
            endpoints = {source: arrows[target] for source, target in endpoints.items()}

    tail, period = graph_tail_period(states, arrows)
    order_cache = {
        c: field.multiplicative_order(c) for c in range(1, q)
    }
    for state in states:
        c = bilinear(field, matrix, *state)
        if state == zero:
            expected = (0, 1)
        elif c == 0:
            expected = (1, 1)
        else:
            a, s = valuation_three(order_cache[c])
            expected = (a, integer_order(3, 2 * s))
            if field.p == 2 and s > 1:
                check(
                    integer_order(3, 2 * s) == integer_order(3, s),
                    f"{field.name} characteristic-two order interpretation",
                )
        check(
            (tail[state], period[state]) == expected,
            f"{field.name} orbit m={dimension} {form_name} state={state}",
        )

    A, h = valuation_three(q - 1)
    predicted_tails = Counter({0: 1 + h * Q, 1: Z - 1})
    for a in range(1, A + 1):
        predicted_tails[a] += 2 * 3 ** (a - 1) * h * Q
    observed_tails = Counter(tail.values())
    check(observed_tails == +predicted_tails, f"{field.name} tail census")
    check(sum(observed_tails.values()) == q ** (2 * dimension), f"{field.name} tail mass")
    check(max(observed_tails) == max(1, A), f"{field.name} maximum tail")
    if A == 0:
        check(observed_tails[0] == 1 + (q - 1) * Q, f"{field.name} A=0 recurrent")
        check(observed_tails[1] == Z - 1, f"{field.name} A=0 null tail")

    one_step = Counter(arrows.values())
    g = gcd(3, q - 1)
    expected_image = 1 + (q - 1) * Q // g
    check(len(one_step) == expected_image, f"{field.name} image size")
    check(one_step[zero] == Z, f"{field.name} zero fibre")
    for target, count in one_step.items():
        if target != zero:
            check(count == g, f"{field.name} uniform nonzero fibre")
    maximum_targets = [target for target, count in one_step.items() if count == max(one_step.values())]
    check(maximum_targets == [zero], f"{field.name} unique maximum fibre")
    check(Z > q - 1 >= g, f"{field.name} strict maximum inequality")

    return len(states), Z, Q, A, observed_tails, tuple(fibre_profiles)


def main():
    specifications = (
        (2, (0, 1), "GF2", (1, 2)),
        (3, (0, 1), "GF3", (1, 2)),
        (5, (0, 1), "GF5", (1, 2)),
        (7, (0, 1), "GF7", (1, 2)),
        (2, (1, 1, 1), "GF4", (1, 2)),
        (2, (1, 1, 0, 1), "GF8", (1, 2)),
        (3, (1, 0, 1), "GF9", (1, 2)),
        (2, (1, 1, 0, 0, 1), "GF16", (1,)),
        (5, (2, 0, 1), "GF25", (1,)),
        (2, (1, 1, 0, 0, 0, 0, 1), "GF64", (1,)),
        (19, (0, 1), "GF19", (1,)),
        (109, (0, 1), "GF109", (1,)),
    )
    rows = []
    for p, modulus, name, dimensions in specifications:
        field = QuotientField(p, modulus, name)
        for dimension in dimensions:
            for form_name, matrix in forms(field, dimension):
                result = audit_box(field, dimension, form_name, matrix)
                rows.append((name, dimension, form_name) + result)

    print("P180_REVIEWER_STOCHASTIC")
    for name, dimension, form_name, states, Z, Q, A, tails, image_profiles in rows:
        print(
            f"field={name} m={dimension} form={form_name} states={states} "
            f"Z={Z} Q={Q} A={A} tails={tail_string(tails)} "
            f"images_t1..4={'/'.join(map(str, image_profiles))}"
        )
    print("FIBRES=every_target t=0..4; t0_identity=PASS")
    print("FIELDS=prime_and_extension; char2={GF2,GF4,GF8,GF16,GF64}; Amax=3")
    print("FORMS=unit/identity/nonsymmetric_shear/alternating")
    print("GRAPH_METHOD=indegree_peeling_plus_reverse_dynamic_programming")
    print(f"ASSERTIONS={ASSERTIONS}")
    print(f"ARROW_SHA256={ARROW_HASH.hexdigest()}")
    print("RESULT=PASS")
    print("RELEASE_SENTINEL=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
