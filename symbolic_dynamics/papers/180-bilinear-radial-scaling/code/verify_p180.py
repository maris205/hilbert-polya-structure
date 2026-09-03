#!/usr/bin/env python3
"""Exact prime-field regression control for P180.

The literal pair map is enumerated independently from the closed formulas.
The finite boxes are counterexample pressure only; the manuscript proof is
uniform over every finite field and every nondegenerate bilinear form.
"""

from collections import Counter
from itertools import product
from math import gcd


def vectors(q, m):
    return list(product(range(q), repeat=m))


def dot(state, q):
    u, v = state
    return sum(x * y for x, y in zip(u, v)) % q


def radial(state, q):
    c = dot(state, q)
    return (tuple(c * x % q for x in state[0]),
            tuple(c * x % q for x in state[1]))


def iterate(state, q, t):
    for _ in range(t):
        state = radial(state, q)
    return state


def closed_iterate(state, q, t):
    if t == 0:
        return state
    c = dot(state, q)
    exponent = (3**t - 1) // 2
    scale = pow(c, exponent, q)
    return (tuple(scale * x % q for x in state[0]),
            tuple(scale * x % q for x in state[1]))


def orbit_data(states, transition):
    tail = {}
    period = {}
    for start in states:
        seen = {}
        state = start
        while state not in seen:
            seen[state] = len(seen)
            state = transition[state]
        tail[start] = seen[state]
        period[start] = len(seen) - seen[state]
    return tail, period


def field_order(c, q):
    value = 1
    for order in range(1, q):
        value = value * c % q
        if value == 1:
            return order
    raise AssertionError("multiplicative order missing")


def residue_order(a, modulus):
    value = 1
    for order in range(1, modulus + 1):
        value = value * a % modulus
        if value == 1:
            return order
    raise AssertionError("residue order missing")


def main():
    assertions = 0
    rows = []
    for q in (2, 3, 5, 7, 11, 13):
        for m in (1, 2):
            vecs = vectors(q, m)
            states = [(u, v) for u in vecs for v in vecs]
            zero = ((0,) * m, (0,) * m)
            Q = q ** (m - 1) * (q**m - 1)
            Z = q ** (2 * m - 1) + q**m - q ** (m - 1)

            levels = Counter(dot(state, q) for state in states)
            assert levels[0] == Z
            assert all(levels[c] == Q for c in range(1, q))
            assertions += q

            for state in states:
                for t in range(5):
                    assert iterate(state, q, t) == closed_iterate(state, q, t)
                    expected_dot = pow(dot(state, q), 3**t, q)
                    assert dot(iterate(state, q, t), q) == expected_dot
                    assertions += 2

            transition = {state: radial(state, q) for state in states}
            tail, period = orbit_data(states, transition)
            A = 0
            h = q - 1
            while h % 3 == 0:
                A += 1
                h //= 3

            predicted_tail = Counter({0: 1 + h * Q, 1: Z - 1})
            for a in range(1, A + 1):
                predicted_tail[a] += 2 * 3 ** (a - 1) * h * Q
            assert Counter(tail.values()) == +predicted_tail
            assertions += len(states)

            for state in states:
                c = dot(state, q)
                if state == zero:
                    assert (tail[state], period[state]) == (0, 1)
                elif c == 0:
                    assert (tail[state], period[state]) == (1, 1)
                else:
                    order = field_order(c, q)
                    a = 0
                    while order % 3 == 0:
                        a += 1
                        order //= 3
                    assert tail[state] == a
                    assert period[state] == residue_order(3, 2 * order)
                assertions += 1

            zero_time_fibres = Counter(iterate(state, q, 0)
                                       for state in states)
            for target in states:
                assert zero_time_fibres[target] == 1
                assertions += 1

            for t in range(1, 4):
                fibres = Counter(iterate(state, q, t) for state in states)
                root_count = gcd(3**t, q - 1)
                for target in states:
                    d = dot(target, q)
                    if target == zero:
                        expected = Z
                    elif d == 0:
                        expected = 0
                    elif pow(d, (q - 1) // root_count, q) == 1:
                        expected = root_count
                    else:
                        expected = 0
                    assert fibres[target] == expected
                    assertions += 1

            one_step = Counter(transition.values())
            cube_kernel = gcd(3, q - 1)
            assert len(one_step) == 1 + (q - 1) * Q // cube_kernel
            assert one_step[zero] == Z
            assert all(value == cube_kernel
                       for target, value in one_step.items() if target != zero)
            assert max(one_step.values()) == Z
            assert [target for target, value in one_step.items() if value == Z] == [zero]
            assertions += len(one_step) + 4

            rows.append((q, m, len(states), Z, Q,
                         tuple(sorted(predicted_tail.items())),
                         len(one_step)))

    print("P180_BILINEAR_RADIAL_SCALING")
    for q, m, size, Z, Q, tails, image in rows:
        print(f"q={q} m={m} states={size} Z={Z} Q={Q} tails={tails} image={image}")
    print(f"ASSERTIONS={assertions}")
    print("BOXES=prime q in {2,3,5,7,11,13}; m in {1,2}; iterates t<=4; fibres t<=3")
    print("TIME_ZERO_FIBRES=IDENTITY_PASS")
    print("RESULT=PASS")
    print("RELEASE_SENTINEL=THEOREM_CONTROL_ONLY/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
