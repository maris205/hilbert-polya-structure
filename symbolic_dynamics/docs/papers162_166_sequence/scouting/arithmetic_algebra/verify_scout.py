#!/usr/bin/env python3
"""Exact breadth controls for the P162--P166 arithmetic/algebra scout.

All computations use the Python standard library.  Enumeration is
falsification evidence, never a proof or an ownership certificate.
"""

from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, gcd


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def iterate(step, state, t):
    for _ in range(t):
        state = step(state)
    return state


def inv_mod(a, modulus):
    return pow(a, -1, modulus)


# AA01: unit-pivot Schur stripping over Z/mZ.
def schur_step(matrix, modulus):
    if matrix is None or not matrix:
        return matrix
    n = len(matrix)
    pivot = matrix[0][0]
    if gcd(pivot, modulus) != 1:
        return None
    if n == 1:
        return ()
    inverse = inv_mod(pivot, modulus)
    return tuple(
        tuple(
            (matrix[i][j] - matrix[i][0] * inverse * matrix[0][j]) % modulus
            for j in range(1, n)
        )
        for i in range(1, n)
    )


def matrices(modulus, n):
    for entries in product(range(modulus), repeat=n * n):
        yield tuple(tuple(entries[i * n:(i + 1) * n]) for i in range(n))


def audit_unit_schur():
    signature = []
    for modulus in (3, 4, 5):
        units = sum(gcd(a, modulus) == 1 for a in range(modulus))
        states = list(matrices(modulus, 2))
        survive = []
        for t in (1, 2):
            count = 0
            for matrix in states:
                target = iterate(lambda a: schur_step(a, modulus), matrix, t)
                check(target is None or isinstance(target, tuple),
                      f"AA01 closure m={modulus} t={t}")
                if target is not None:
                    count += 1
            predicted = units ** t * modulus ** (4 - t)
            check(count == predicted,
                  f"AA01 survival m={modulus} t={t}: {count}!={predicted}")
            survive.append(count)

        fibres = Counter(schur_step(matrix, modulus) for matrix in states)
        for target in matrices(modulus, 1):
            check(fibres[target] == units * modulus ** 2,
                  f"AA01 target fibre m={modulus} target={target}")
        check(fibres[()] == 0, f"AA01 wrong one-step dimension m={modulus}")
        empty_two = sum(
            iterate(lambda a: schur_step(a, modulus), matrix, 2) == ()
            for matrix in states
        )
        check(empty_two == units ** 2 * modulus ** 2,
              f"AA01 two-step empty fibre m={modulus}")
        signature.append(f"m{modulus}:states={len(states)},survive={survive},f1={units*modulus**2}")
    return ";".join(signature)


# AA02: adjacent 2x2-minor condensation, audited at its first scalar layer.
def audit_minor_condensation():
    signature = []
    for q in (2, 3, 5):
        counts = Counter()
        for a, b, c, d in product(range(q), repeat=4):
            det = (a * d - b * c) % q
            counts[det] += 1
        zero = q ** 3 + q ** 2 - q
        nonzero = q * (q ** 2 - 1)
        check(counts[0] == zero, f"AA02 zero determinant q={q}")
        for value in range(1, q):
            check(counts[value] == nonzero,
                  f"AA02 nonzero determinant q={q} value={value}")
        check(sum(counts.values()) == q ** 4, f"AA02 mass q={q}")
        signature.append(f"q{q}:fibres=0:{zero},nz:{nonzero}")
    return ";".join(signature)


# AA03: gcd-increment on [1,p^k], reflected to least-valuation erasure.
def digit_sum(n, p):
    total = 0
    while n:
        total += n % p
        n //= p
    return total


def audit_gcd_increment():
    signature = []
    for p, k in ((2, 5), (3, 4), (5, 3)):
        modulus = p ** k

        def step(x):
            return modulus if x == modulus else x + gcd(x, modulus)

        fibres = Counter(step(x) for x in range(1, modulus + 1))
        max_clock = 0
        for x in range(1, modulus + 1):
            y = modulus - x
            reflected = modulus - step(x)
            erased = 0 if y == 0 else y - gcd(y, modulus)
            check(reflected == erased, f"AA03 reflection p={p} k={k} x={x}")
            clock = 0
            z = x
            while z != modulus:
                z = step(z)
                clock += 1
                check(clock <= (p - 1) * k, f"AA03 termination p={p} k={k}")
            check(clock == digit_sum(y, p), f"AA03 digit clock p={p} k={k} x={x}")
            max_clock = max(max_clock, clock)

        for target in range(1, modulus + 1):
            predicted = int(target == modulus)
            for divisor in range(1, modulus + 1):
                if modulus % divisor or target % divisor:
                    continue
                source = target - divisor
                if source >= 1 and gcd(source, modulus) == divisor:
                    predicted += 1
            check(fibres[target] == predicted,
                  f"AA03 divisor fibre p={p} k={k} y={target}")
        check(max_clock == (p - 1) * k, f"AA03 sharp clock p={p} k={k}")
        signature.append(f"p{p}k{k}:states={modulus},height={max_clock},maxfib={max(fibres.values())}")
    return ";".join(signature)


# AA04: Lucas digit truncation on binomial-index pairs.
def binomial_pairs(p, k):
    bound = p ** k
    return [(a, b) for a in range(bound) for b in range(a + 1)]


def audit_lucas_truncation():
    signature = []
    for p, k in ((2, 5), (3, 4)):
        states = binomial_pairs(p, k)
        check(len(states) == p ** k * (p ** k + 1) // 2,
              f"AA04 carrier p={p} k={k}")
        for t in range(1, k + 1):
            scale = p ** t
            targets = binomial_pairs(p, k - t)
            counts = Counter((a // scale, b // scale) for a, b in states)
            for A, B in targets:
                predicted = scale ** 2 if A > B else scale * (scale + 1) // 2
                check(counts[(A, B)] == predicted,
                      f"AA04 fibre p={p} k={k} t={t} target={(A,B)}")
        signature.append(f"p{p}k{k}:states={len(states)},terminalfib={len(states)}")
    return ";".join(signature)


# AA05: reciprocal-GCD retraction in factor-exponent coordinates.
def reciprocal_meet(state):
    return tuple(min(state[i], state[-1 - i]) for i in range(len(state)))


def audit_reciprocal_gcd():
    signature = []
    for length, cap in ((3, 2), (4, 2), (5, 3)):
        states = list(product(range(cap + 1), repeat=length))
        fibres = Counter(reciprocal_meet(state) for state in states)
        fixed = []
        for state in states:
            target = reciprocal_meet(state)
            check(reciprocal_meet(target) == target,
                  f"AA05 idempotence m={length} c={cap}")
            if target == state:
                fixed.append(state)
        predicted_fixed = (cap + 1) ** ((length + 1) // 2)
        check(len(fixed) == predicted_fixed, f"AA05 fixed m={length} c={cap}")
        for target in states:
            if reciprocal_meet(target) != target:
                check(fibres[target] == 0, f"AA05 nonimage target={target}")
                continue
            predicted = 1
            for i in range(length // 2):
                a = target[i]
                check(a == target[-1 - i], f"AA05 fixed symmetry target={target}")
                predicted *= 2 * (cap - a) + 1
            check(fibres[target] == predicted, f"AA05 fibre target={target}")
        signature.append(f"m{length}c{cap}:states={len(states)},fixed={len(fixed)},maxfib={max(fibres.values())}")
    return ";".join(signature)


# AA06: syzygy on indecomposables over k[x]/(x^n).
def audit_nakayama_syzygy():
    signature = []
    for n in range(2, 13):
        def step(length):
            if length in (0, n):
                return 0
            return n - length

        fibres = Counter(step(length) for length in range(n + 1))
        check(step(0) == 0 and step(n) == 0, f"AA06 endpoints n={n}")
        for length in range(1, n):
            check(iterate(step, length, 2) == length, f"AA06 period n={n} l={length}")
            check(fibres[length] == 1, f"AA06 singleton fibre n={n} l={length}")
        check(fibres[0] == 2 and fibres[n] == 0, f"AA06 boundary fibres n={n}")
        recurrent = n  # zero plus n-1 nonprojective lengths
        fixed = 1 + int(n % 2 == 0)
        signature.append(f"n{n}:rec={recurrent},fixed={fixed},depth1=1")
    return ";".join(signature[-3:])


# AA07: a Coxeter element on positive roots of type A_n, killed at negativity.
def audit_coxeter_escape():
    signature = []
    for n in range(1, 11):
        sink = None
        roots = [(a, b) for a in range(1, n + 1) for b in range(a + 1, n + 2)]

        def step(root):
            if root is None:
                return None
            a, b = root
            aa = 1 if a == n + 1 else a + 1
            bb = 1 if b == n + 1 else b + 1
            return (aa, bb) if aa < bb else sink

        fibres = Counter(step(root) for root in roots + [sink])
        depth_hist = Counter()
        for a, b in roots:
            clock = 0
            state = (a, b)
            while state is not sink:
                state = step(state)
                clock += 1
            predicted = n + 2 - b
            check(clock == predicted, f"AA07 clock n={n} root={(a,b)}")
            depth_hist[clock] += 1
        for t in range(1, n + 1):
            check(depth_hist[t] == n + 1 - t, f"AA07 shell n={n} t={t}")
        check(fibres[sink] == n + 1, f"AA07 sink fibre n={n}")
        for root in roots:
            predicted = int(root[0] > 1)
            check(fibres[root] == predicted, f"AA07 root fibre n={n} root={root}")
        signature.append(f"A{n}:roots={len(roots)},height={n},sinkfib={n+1}")
    return ";".join(signature[-3:])


# AA08: function-field continued-fraction Gauss shift in quotient-word form.
def all_words(alphabet_size, max_length):
    words = [()]
    for length in range(1, max_length + 1):
        words.extend(product(range(alphabet_size), repeat=length))
    return words


def audit_continued_fraction_shift():
    signature = []
    for alphabet_size, max_length in ((2, 6), (3, 5)):
        states = all_words(alphabet_size, max_length)

        def step(word):
            return word[1:] if word else ()

        for word in states:
            check(iterate(step, word, len(word)) == (), f"AA08 clock word={word}")
            if word:
                check(iterate(step, word, len(word) - 1) != (), f"AA08 sharp word={word}")
        for t in range(1, max_length + 1):
            counts = Counter(iterate(step, word, t) for word in states)
            terminal = sum(alphabet_size ** j for j in range(t + 1))
            check(counts[()] == terminal, f"AA08 terminal fibre a={alphabet_size} t={t}")
            for target in states:
                if not target or len(target) + t > max_length:
                    continue
                check(counts[target] == alphabet_size ** t,
                      f"AA08 target fibre a={alphabet_size} t={t} target={target}")
        signature.append(f"a{alphabet_size}n{max_length}:states={len(states)},height={max_length}")
    return ";".join(signature)


# AA09: divide a divisor by its least active prime.
def prime_peel(state):
    state = list(state)
    for i, exponent in enumerate(state):
        if exponent:
            state[i] -= 1
            break
    return tuple(state)


def audit_prime_exponent_peeling():
    signature = []
    for caps in ((2, 1, 3), (1, 2, 2, 1), (3, 2, 1, 2)):
        states = list(product(*(range(cap + 1) for cap in caps)))
        fibres = Counter(prime_peel(state) for state in states)
        for state in states:
            clock = sum(state)
            check(iterate(prime_peel, state, clock) == tuple(0 for _ in caps),
                  f"AA09 clock state={state}")
            if clock:
                check(iterate(prime_peel, state, clock - 1) != tuple(0 for _ in caps),
                      f"AA09 sharp state={state}")
        for target in states:
            if not any(target):
                predicted = 1 + len(caps)
            else:
                first = next(i for i, exponent in enumerate(target) if exponent)
                predicted = first + int(target[first] < caps[first])
            check(fibres[target] == predicted, f"AA09 fibre caps={caps} target={target}")
        histogram = Counter(map(sum, states))
        polynomial = [1]
        for cap in caps:
            new = [0] * (len(polynomial) + cap)
            for i, value in enumerate(polynomial):
                for j in range(cap + 1):
                    new[i + j] += value
            polynomial = new
        check([histogram[i] for i in range(len(polynomial))] == polynomial,
              f"AA09 shell product caps={caps}")
        signature.append(f"caps={caps}:states={len(states)},height={sum(caps)},maxfib={max(fibres.values())}")
    return ";".join(signature)


# AA10: repeatedly remove one copy of the least F_q-rational root.
def poly_eval(poly, a, q):
    value = 0
    for coefficient in reversed(poly):
        value = (value * a + coefficient) % q
    return value


def divide_linear(poly, a, q):
    # Synthetic division for low-to-high coefficient tuples and a monic input.
    high = list(reversed(poly))
    quotient_high = [high[0]]
    for coefficient in high[1:-1]:
        quotient_high.append((coefficient + a * quotient_high[-1]) % q)
    remainder = (high[-1] + a * quotient_high[-1]) % q
    check(remainder == 0, f"AA10 nonroot division a={a} poly={poly}")
    return tuple(reversed(quotient_high))


def monic_polynomials(q, max_degree):
    result = []
    for degree in range(max_degree + 1):
        if degree == 0:
            result.append((1,))
        else:
            for lower in product(range(q), repeat=degree):
                result.append(tuple(lower) + (1,))
    return result


def least_root(poly, q):
    for a in range(q):
        if poly_eval(poly, a, q) == 0:
            return a
    return None


def audit_least_root_deflation():
    signature = []
    for q, cap in ((2, 6), (3, 4), (5, 3)):
        states = monic_polynomials(q, cap)

        def step(poly):
            root = least_root(poly, q)
            return poly if root is None else divide_linear(poly, root, q)

        fibres = Counter(step(poly) for poly in states)
        fixed_by_degree = Counter()
        terminals = []
        for poly in states:
            degree = len(poly) - 1
            multiplicity = 0
            work = poly
            for a in range(q):
                while poly_eval(work, a, q) == 0:
                    work = divide_linear(work, a, q)
                    multiplicity += 1
            clock = 0
            orbit = poly
            while step(orbit) != orbit:
                orbit = step(orbit)
                clock += 1
            check(clock == multiplicity, f"AA10 clock q={q} poly={poly}")
            check(least_root(orbit, q) is None, f"AA10 terminal q={q} poly={poly}")
            root = least_root(poly, q)
            if root is None:
                terminals.append(poly)
                fixed_by_degree[degree] += 1
                predicted = 1 if degree == cap else q + 1
            else:
                predicted = 0 if degree == cap else root + 1
            check(fibres[poly] == predicted, f"AA10 one-step fibre q={q} poly={poly}")

        for degree in range(cap + 1):
            predicted = sum(
                (-1) ** j * comb(q, j) * q ** (degree - j)
                for j in range(min(q, degree) + 1)
            )
            check(fixed_by_degree[degree] == predicted,
                  f"AA10 fixed degree q={q} d={degree}")

        for t in range(cap + 1):
            counts = Counter(iterate(step, poly, t) for poly in states)
            for target in terminals:
                room = min(t, cap - (len(target) - 1))
                predicted = comb(room + q, q)
                check(counts[target] == predicted,
                      f"AA10 terminal fibre q={q} t={t} target={target}")
        signature.append(f"q{q}N{cap}:states={len(states)},fixed={len(terminals)},height={cap}")
    return ";".join(signature)


# AA11: a Chinese-remainder tower dropping the least active prime coordinate.
def crt_states(primes):
    result = []
    r = len(primes)
    for mask in range(1 << r):
        indices = tuple(i for i in range(r) if mask & (1 << i))
        modulus = 1
        for i in indices:
            modulus *= primes[i]
        result.extend((indices, residue) for residue in range(modulus))
    return result


def elementary_weight(primes, degree):
    return sum(
        product_value(indices)
        for indices in combinations(primes, degree)
    )


def product_value(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


def audit_crt_forgetting():
    signature = []
    for primes in ((2, 3, 5), (2, 3, 5, 7)):
        states = crt_states(primes)

        def step(state):
            indices, residue = state
            if not indices:
                return state
            remaining = indices[1:]
            modulus = product_value(primes[i] for i in remaining)
            return (remaining, residue % modulus)

        terminal = ((), 0)
        for state in states:
            check(iterate(step, state, len(state[0])) == terminal,
                  f"AA11 clock primes={primes} state={state}")
        for t in range(1, len(primes) + 1):
            counts = Counter(iterate(step, state, t) for state in states)
            predicted_terminal = sum(elementary_weight(primes, j) for j in range(t + 1))
            check(counts[terminal] == predicted_terminal,
                  f"AA11 terminal fibre primes={primes} t={t}")
            for target in states:
                indices, _ = target
                if not indices:
                    continue
                eligible = primes[:indices[0]]
                predicted = elementary_weight(eligible, t) if t <= len(eligible) else 0
                check(counts[target] == predicted,
                      f"AA11 target fibre primes={primes} t={t} target={target}")
        check(len(states) == product_value(p + 1 for p in primes),
              f"AA11 carrier mass primes={primes}")
        signature.append(f"p={primes}:states={len(states)},height={len(primes)}")
    return ";".join(signature)


# AA12: strict chain-prefix summation, a regular nilpotent linear control.
def prefix_step(vector, q):
    running = 0
    answer = []
    for coordinate in vector:
        answer.append(running)
        running = (running + coordinate) % q
    return tuple(answer)


def audit_prefix_nilpotent():
    signature = []
    for q, n in ((2, 8), (3, 6), (5, 5)):
        states = list(product(range(q), repeat=n))
        zero = (0,) * n
        for t in range(n + 1):
            images = Counter(iterate(lambda x: prefix_step(x, q), state, t) for state in states)
            kernel = images[zero]
            check(kernel == q ** t, f"AA12 kernel q={q} n={n} t={t}")
            nonempty_fibres = set(images.values())
            check(nonempty_fibres == {q ** t}, f"AA12 uniform fibre q={q} n={n} t={t}")
            check(len(images) == q ** (n - t), f"AA12 image q={q} n={n} t={t}")
        check(all(iterate(lambda x: prefix_step(x, q), state, n) == zero for state in states),
              f"AA12 nilpotence q={q} n={n}")
        check(any(iterate(lambda x: prefix_step(x, q), state, n - 1) != zero for state in states),
              f"AA12 sharp height q={q} n={n}")
        signature.append(f"q{q}n{n}:states={len(states)},height={n},lastkernel={q**n}")
    return ";".join(signature)


def main():
    rows = [
        ("AA01_USP", audit_unit_schur()),
        ("AA02_DMC", audit_minor_condensation()),
        ("AA03_GIO", audit_gcd_increment()),
        ("AA04_LDT", audit_lucas_truncation()),
        ("AA05_RGM", audit_reciprocal_gcd()),
        ("AA06_NAK", audit_nakayama_syzygy()),
        ("AA07_COX", audit_coxeter_escape()),
        ("AA08_FCG", audit_continued_fraction_shift()),
        ("AA09_PEP", audit_prime_exponent_peeling()),
        ("AA10_LRD", audit_least_root_deflation()),
        ("AA11_CRT", audit_crt_forgetting()),
        ("AA12_PFX", audit_prefix_nilpotent()),
    ]
    check(len(rows) == 12, "registry must contain twelve literal systems")
    check(len({name for name, _ in rows}) == len(rows), "handles must be distinct")
    print("P162_P166_ARITHMETIC_ALGEBRA_SCOUT v1")
    print("external_status=HOLD_EXTERNAL")
    for name, signature in rows:
        print(f"{name} {signature}")
    print(f"systems={len(rows)}")
    print(f"assertions={ASSERTIONS}")
    print("status=PASS")


if __name__ == "__main__":
    main()
