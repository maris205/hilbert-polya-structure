#!/usr/bin/env python3
"""Independent theorem-level controls for the three coordinator spikes.

Enumeration is used only as finite counterexample pressure.  Each assertion
compares the literal dynamics with a separately coded closed formula.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial, gcd


def first_descent_map(p):
    for j in range(len(p) - 1):
        if p[j] > p[j + 1]:
            return p[j + 1 :: -1] + p[j + 2 :]
    return p


def orbit_coordinates(states, nxt):
    tail = {}
    period = {}
    for x in states:
        order = {}
        y = x
        while y not in order:
            order[y] = len(order)
            y = nxt[y]
        mu = order[y]
        lam = len(order) - mu
        tail[x] = mu
        period[x] = lam
    return tail, period


def decreasing_run_from_second(p):
    r = 1
    while r + 1 < len(p) and p[r] > p[r + 1]:
        r += 1
    return r


def check_fdr():
    assertions = 0
    rows = []
    for n in range(3, 9):
        states = list(permutations(range(1, n + 1)))
        nxt = {p: first_descent_map(p) for p in states}
        image = set(nxt.values())
        predicted_image = {p for p in states if p[0] < p[1]}
        assert image == predicted_image
        assertions += len(states) + 1

        recurrent = {tuple(range(1, n + 1))}
        recurrent |= {p for p in states if p[0] < p[1] > p[2]}
        tail, period = orbit_coordinates(states, nxt)
        actual_recurrent = {p for p in states if tail[p] == 0}
        assert actual_recurrent == recurrent
        assert all(period[p] == (1 if p == tuple(range(1, n + 1)) else 2)
                   for p in recurrent)
        expected_tail = Counter({0: factorial(n) // 3 + 1,
                                 1: factorial(n) // 2,
                                 2: factorial(n) // 6 - 1})
        assert Counter(tail.values()) == +expected_tail
        assertions += len(states) + 3

        incoming = defaultdict(set)
        for p, q in nxt.items():
            incoming[q].add(p)
        ident = tuple(range(1, n + 1))
        for q in states:
            expected = 0
            if q in predicted_image:
                expected = decreasing_run_from_second(q) + int(q == ident)
            assert len(incoming[q]) == expected
            assertions += 1
        max_fibre = max(map(len, incoming.values()))
        expected_max_targets = {
            q for q in states
            if q[0] < q[1] and q[1] == n
            and all(q[j] > q[j + 1] for j in range(1, n - 1))
        }
        if n == 3:
            expected_max_targets.add(ident)
        assert max_fibre == n - 1
        assert {q for q in states if len(incoming[q]) == max_fibre} == expected_max_targets
        assertions += len(states) + 2
        rows.append((n, len(states), len(image), dict(sorted(expected_tail.items())), max_fibre))
    return assertions, rows


def partitions(n):
    if n == 0:
        yield ()
        return
    def extend(word, top):
        if len(word) == n:
            yield tuple(word)
            return
        for a in range(top + 2):
            yield from extend(word + [a], max(top, a))
    yield from extend([0], 0)


def blocks(p):
    out = defaultdict(list)
    for i, a in enumerate(p):
        out[a].append(i)
    return list(out.values())


def canonical(block_list, n):
    block_list = sorted((sorted(b) for b in block_list if b), key=lambda b: b[0])
    out = [0] * n
    for a, block in enumerate(block_list):
        for i in block:
            out[i] = a
    return tuple(out)


def isolate(p, i):
    old = blocks(p)
    for j, b in enumerate(old):
        if i in b and len(b) > 1:
            old[j] = [x for x in b if x != i]
            old.append([i])
            return canonical(old, len(p))
    return p


def singleton_number(p):
    return sum(len(b) == 1 for b in blocks(p))


def associated_bell(m):
    return sum(1 for p in partitions(m) if singleton_number(p) == 0)


def stirling2(t, k):
    table = [[0] * (k + 1) for _ in range(t + 1)]
    table[0][0] = 1
    for a in range(1, t + 1):
        for b in range(1, min(a, k) + 1):
            table[a][b] = table[a - 1][b - 1] + b * table[a - 1][b]
    return table[t][k] if k <= t else 0


def elementary(values, degree):
    e = [0] * (degree + 1)
    e[0] = 1
    for v in values:
        for j in range(degree, 0, -1):
            e[j] += v * e[j - 1]
    return e[degree]


def mat_rank(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    rank = 0
    for col in range(len(a[0]) if a else 0):
        pivot = next((r for r in range(rank, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        z = a[rank][col]
        a[rank] = [x / z for x in a[rank]]
        for r in range(len(a)):
            if r != rank and a[r][col]:
                z = a[r][col]
                a[r] = [x - z * y for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


def check_rsi():
    assertions = 0
    rows = []
    for n in range(1, 9):
        states = list(partitions(n))
        index = {p: j for j, p in enumerate(states)}
        incoming_states = defaultdict(set)
        incoming_actions = Counter()
        for p in states:
            for i in range(n):
                q = isolate(p, i)
                incoming_states[q].add(p)
                incoming_actions[q] += 1
        for q in states:
            s = singleton_number(q)
            b = len(blocks(q))
            expected_states = 0 if s == 0 else 1 + s * (b - s) + comb(s, 2)
            assert len(incoming_states[q]) == expected_states
            assert incoming_actions[q] == s * b
            assertions += 2

        layer = Counter(map(singleton_number, states))
        predicted = {s: comb(n, s) * associated_bell(n - s) for s in range(max(0, n - 1))}
        predicted[n] = 1
        assert dict(layer) == {s: v for s, v in predicted.items() if v}
        assertions += len(states)

        # Directly test the absorption CDF against all label histories for n <= 6.
        if n <= 6:
            for p in states:
                sizes = [len(b) for b in blocks(p)]
                for t in range(0, 5):
                    good = 0
                    for history in product(range(n), repeat=t):
                        q = p
                        for i in history:
                            q = isolate(q, i)
                        good += singleton_number(q) == n
                    formula = sum(
                        elementary(sizes, m) * factorial(n - m) * stirling2(t, n - m)
                        for m in range(len(sizes) + 1)
                    )
                    assert good == formula
                    assertions += 1

        # For n <= 5, verify eigenspace dimensions directly over Q.  Since
        # nP is integral, the eigenvalue s/n becomes the integer s here.
        if n <= 5:
            N = len(states)
            nP = [[0] * N for _ in range(N)]
            for p in states:
                r = index[p]
                for i in range(n):
                    nP[r][index[isolate(p, i)]] += 1
            for s, multiplicity in layer.items():
                shifted = [[nP[r][c] - (s if r == c else 0)
                            for c in range(N)] for r in range(N)]
                nullity = N - mat_rank(shifted)
                assert nullity == multiplicity
                assertions += N
        rows.append((n, len(states), dict(sorted(layer.items())), max(map(len, incoming_states.values()))))
    return assertions, rows


def dot(pair, q):
    u, v = pair
    return sum(a * b for a, b in zip(u, v)) % q


def radial(pair, q):
    c = dot(pair, q)
    return (tuple(c * x % q for x in pair[0]),
            tuple(c * x % q for x in pair[1]))


def power(pair, q, t):
    for _ in range(t):
        pair = radial(pair, q)
    return pair


def multiplicative_order(a, modulus):
    x = 1
    for k in range(1, modulus + 1):
        x = x * a % modulus
        if x == 1:
            return k
    raise AssertionError("order not found")


def order_in_field(c, q):
    x = 1
    for k in range(1, q):
        x = x * c % q
        if x == 1:
            return k
    raise AssertionError("field order not found")


def check_brs():
    assertions = 0
    rows = []
    for q in (2, 3, 5, 7, 11, 13):
        for m in (1, 2):
            vecs = list(product(range(q), repeat=m))
            states = [(u, v) for u in vecs for v in vecs]
            zero = ((0,) * m, (0,) * m)
            Q = q ** (m - 1) * (q**m - 1)
            Z = q ** (2 * m - 1) + q**m - q ** (m - 1)
            levels = Counter(map(lambda z: dot(z, q), states))
            assert levels[0] == Z
            assert all(levels[c] == Q for c in range(1, q))
            assertions += q

            nxt = {z: radial(z, q) for z in states}
            tail, period = orbit_coordinates(states, nxt)
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
            for z in states:
                c = dot(z, q)
                if z == zero:
                    assert tail[z] == 0 and period[z] == 1
                elif c == 0:
                    assert tail[z] == 1 and period[z] == 1
                else:
                    r = order_in_field(c, q)
                    a = 0
                    while r % 3 == 0:
                        a += 1
                        r //= 3
                    assert tail[z] == a
                    assert period[z] == multiplicative_order(3, 2 * r)
                assertions += 1

            for t in range(1, 4):
                fibres = Counter(power(z, q, t) for z in states)
                g = gcd(3**t, q - 1)
                assert fibres[zero] == Z
                for target in states:
                    d = dot(target, q)
                    if target == zero:
                        expected = Z
                    elif d == 0:
                        expected = 0
                    else:
                        expected = g if pow(d, (q - 1) // g, q) == 1 else 0
                    assert fibres[target] == expected
                    assertions += 1
            g = gcd(3, q - 1)
            assert len(set(nxt.values())) == 1 + (q - 1) * Q // g
            assert max(Counter(nxt.values()).values()) == Z
            assertions += 2
            rows.append((q, m, len(states), Z, Q, dict(sorted(predicted_tail.items()))))
    return assertions, rows


def main():
    total = 0
    for name, check in (("FDR", check_fdr), ("RSI", check_rsi), ("BRS", check_brs)):
        count, rows = check()
        total += count
        print(name, "assertions", count)
        for row in rows:
            print(" ", row)
    print("TOTAL_ASSERTIONS", total)
    print("release_sentinel=THEOREM_CONTROLS_ONLY/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
