#!/usr/bin/env python3
"""Exact controls for traceless determinant-shear dynamics in characteristic 2.

The carrier for q=2^m is the traceless slice of M_2(F_q), represented by
(a,b,c) for [[a,b],[c,a]].  The literal map is A -> A+det(A)I.  This file
imports no project module; finite enumeration is falsification pressure only.
"""

from collections import Counter
from math import gcd


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


# Monic irreducibles over F_2, including the leading term.
MODULI = {
    1: 0b11,
    2: 0b111,
    3: 0b1011,
    4: 0b10011,
    5: 0b100101,
    6: 0b1000011,
}


class GF2m:
    def __init__(self, degree):
        self.m = degree
        self.q = 1 << degree
        self.modulus = MODULI[degree]
        self.mask = self.q - 1

    def mul(self, x, y):
        answer = 0
        while y:
            if y & 1:
                answer ^= x
            y >>= 1
            x <<= 1
            if x & self.q:
                x ^= self.modulus
        return answer & self.mask

    def square(self, x):
        return self.mul(x, x)

    def power(self, x, exponent):
        answer = 1
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, x)
            x = self.square(x)
            exponent >>= 1
        return answer

    def absolute_trace(self, x):
        answer = 0
        term = x
        for _ in range(self.m):
            answer ^= term
            term = self.square(term)
        check(answer in (0, 1), ("trace not binary", self.m, x, answer))
        return answer

    def D(self, x):
        return self.square(x) ^ x


def poly_degree(f):
    return f.bit_length() - 1


def poly_mod(f, g):
    dg = poly_degree(g)
    while f and poly_degree(f) >= dg:
        f ^= g << (poly_degree(f) - dg)
    return f


def poly_gcd(f, g):
    while g:
        f, g = g, poly_mod(f, g)
    return f


def polynomial_power(base, exponent):
    answer = 1
    while exponent:
        if exponent & 1:
            answer = polynomial_multiply(answer, base)
        base = polynomial_multiply(base, base)
        exponent >>= 1
    return answer


def polynomial_multiply(f, g):
    answer = 0
    while g:
        if g & 1:
            answer ^= f
        f <<= 1
        g >>= 1
    return answer


def chi_D(m):
    # (z+1)^m + 1 in F_2[z].
    return polynomial_power(0b11, m) ^ 1


def R_polynomial(time):
    return (1 << time) - 1 if time else 0


def kappa(m, time):
    if time == 0:
        return m
    return poly_degree(poly_gcd(R_polynomial(time), chi_D(m)))


def two_part(m):
    return m & -m


def determinant(field, state):
    a, b, c = state
    return field.square(a) ^ field.mul(b, c)


def step(field, state):
    a, b, c = state
    return (a ^ determinant(field, state), b, c)


def iterate(field, state, time):
    for _ in range(time):
        state = step(field, state)
    return state


def D_power(field, value, time):
    for _ in range(time):
        value = field.D(value)
    return value


def R_D(field, value, time):
    answer = 0
    term = value
    for _ in range(time):
        answer ^= term
        term = field.D(term)
    return answer


def enumerate_states(field):
    return (
        (a, b, c)
        for b in range(field.q)
        for c in range(field.q)
        for a in range(field.q)
    )


def functional_depths(mapping):
    depth = {}
    recurrent = set()
    for start in mapping:
        if start in depth:
            continue
        trail = []
        place = {}
        state = start
        while state not in depth and state not in place:
            place[state] = len(trail)
            trail.append(state)
            state = mapping[state]
        if state in place:
            begin = place[state]
            for item in trail[begin:]:
                depth[item] = 0
                recurrent.add(item)
            prefix = trail[:begin]
        else:
            prefix = trail
        for item in reversed(prefix):
            depth[item] = depth[mapping[item]] + 1
    return depth, recurrent


def audit_field(field):
    q, m = field.q, field.m
    # Field and Frobenius sentinels.
    for x in range(1, q):
        check(field.power(x, q - 1) == 1, ("field", m, x))
    for x in range(q):
        check(field.power(x, q) == x, ("Frobenius", m, x))
        check(field.absolute_trace(field.D(x)) == 0, ("AS image", m, x))

    states = tuple(enumerate_states(field))
    mapping = {state: step(field, state) for state in states}
    det_counts = Counter(determinant(field, state) for state in states)
    check(set(det_counts.values()) == {q * q}, ("det fibres", m, det_counts))

    # Literal determinant semiconjugacy and pointwise iterate.
    horizon = max(2 * m + 2, two_part(m) + 2)
    for state in states:
        d = determinant(field, state)
        nxt = mapping[state]
        check(determinant(field, nxt) == field.D(d), ("det update", m, state))
        scalar = 0
        term = d
        for time in range(horizon + 1):
            predicted = (state[0] ^ scalar, state[1], state[2])
            check(iterate(field, state, time) == predicted, ("iterate", m, state, time))
            scalar ^= term
            term = field.D(term)

    depths, recurrent = functional_depths(mapping)
    s = two_part(m)
    observed_depth = Counter(depths.values())
    predicted_cumulative = {
        time: q * q * (1 << (m - s + min(time, s)))
        for time in range(s + 1)
    }
    for time, predicted in predicted_cumulative.items():
        observed = sum(value <= time for value in depths.values())
        check(observed == predicted, ("depth CDF", m, time, observed, predicted))
    check(max(depths.values()) == s, ("sharp tail", m, max(depths.values()), s))
    check(len(recurrent) == q * q * (1 << (m - s)), ("core", m, len(recurrent)))

    # Every time image and every target fibre.  Full targetwise checks are
    # retained through q=32; q=64 keeps all aggregate and fixed-point checks.
    image_rows = []
    target_times = range(1, s + 3)
    for time in target_times:
        counts = Counter(iterate(field, state, time) for state in states)
        fibre = 1 << min(time, s)
        predicted_image = q * q * (1 << (m - min(time, s)))
        check(len(counts) == predicted_image, ("image", m, time, len(counts)))
        check(set(counts.values()) == {fibre}, ("uniform fibre", m, time))
        if q <= 32:
            for target in states:
                e = determinant(field, target)
                rhs = R_D(field, e, time)
                feasible = any(D_power(field, x, time) == rhs for x in range(q))
                check((counts[target] == fibre) == feasible,
                      ("target criterion", m, time, target, counts[target], rhs))
        image_rows.append((time, len(counts), fibre))

    # One-step target criterion evaluates to the absolute trace of det.
    first = Counter(mapping.values())
    for target in states:
        feasible = field.absolute_trace(determinant(field, target)) == 0
        check((first[target] == 2) == feasible, ("one-step criterion", m, target))

    # Periodic points.  Determinant has q^2 lifts, and the displacement after
    # k steps is R_k(D)d.  Cyclicity of D gives the polynomial-gcd dimension.
    fixed_rows = []
    for time in range(1, 2 * m + 3):
        observed = sum(iterate(field, state, time) == state for state in states)
        predicted = q * q * (1 << kappa(m, time))
        check(observed == predicted, ("fixed", m, time, observed, predicted, kappa(m, time)))
        fixed_rows.append((time, observed, kappa(m, time)))

    # Exact source counts over one recurrent target expose the common binary
    # in-tree: cumulative 2^t until the nilpotent cap.
    recurrent_target = min(recurrent)
    ancestry = []
    for time in range(s + 2):
        observed = sum(iterate(field, state, time) == recurrent_target for state in states)
        predicted = 1 << min(time, s)
        check(observed == predicted, ("recurrent target", m, time, observed, predicted))
        ancestry.append(observed)

    print(
        "BOX",
        f"m={m}",
        f"q={q}",
        f"states={len(states)}",
        f"core={len(recurrent)}",
        f"sharp_tail={max(depths.values())}",
        f"depths={sorted(observed_depth.items())}",
        f"images={image_rows}",
        f"fixed={fixed_rows}",
        f"ancestry={ancestry}",
    )
    return len(states), sum(observed_depth.values())


def audit_symbolic_boundaries():
    for m in range(1, 129):
        s = two_part(m)
        polynomial = chi_D(m)
        check(poly_degree(polynomial) == m, ("chi degree", m))
        # The zero root of chi_D has exact multiplicity 2^v2(m).
        check((polynomial & ((1 << s) - 1)) == 0, ("zero multiplicity low", m, s))
        check((polynomial >> s) & 1, ("zero multiplicity exact", m, s))
        for time in range(1, 2 * m + 3):
            value = kappa(m, time)
            check(0 <= value <= m, ("kappa range", m, time, value))
    print("SYMBOLIC m=1..128 zero-primary/gcd/fixed-count boundaries PASS")


def main():
    total_states = 0
    total_depth_states = 0
    for m in range(1, 7):
        states, depth_states = audit_field(GF2m(m))
        total_states += states
        total_depth_states += depth_states
    audit_symbolic_boundaries()
    print("SUMMARY")
    print(f"literal_states={total_states}")
    print(f"depth_states={total_depth_states}")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("THEOREM iterate/core/sharp-tail/all-time-target-fibres/fixed-atlas PASS")
    print("DECISION GREEN_PENDING_INDEPENDENT_OWNER_COLLISION_GATE")
    print("EXTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
