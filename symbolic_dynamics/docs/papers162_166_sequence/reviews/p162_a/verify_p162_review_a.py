#!/usr/bin/env python3
"""Independent hostile checks for P162.

This program deliberately does not import the paper-local verifier.  It starts
from the literal translation/intersection update and separately evaluates the
closed formula for the source-size/history fibres.
"""

from collections import defaultdict, deque
from fractions import Fraction
from math import comb
import hashlib


ASSERTIONS = 0
ROWS = []


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def erode_vector(source, v, npoints):
    out = 0
    for x in range(npoints):
        if ((source >> x) & 1) and ((source >> (x ^ v)) & 1):
            out |= 1 << x
    return out


def literal_iterate(source, history, npoints):
    state = source
    for v in history:
        state = erode_vector(state, v, npoints)
    return state


def span_set(history):
    span = {0}
    for v in history:
        span |= {h ^ v for h in tuple(span)}
    return frozenset(span)


def erode_span(source, span, npoints):
    out = 0
    for x in range(npoints):
        if all((source >> (x ^ h)) & 1 for h in span):
            out |= 1 << x
    return out


def histories(alphabet_size, length):
    if length == 0:
        yield ()
        return
    digits = [0] * length
    while True:
        yield tuple(digits)
        i = length - 1
        while i >= 0 and digits[i] == alphabet_size - 1:
            digits[i] = 0
            i -= 1
        if i < 0:
            return
        digits[i] += 1


def gaussian2(n, r):
    if r < 0 or r > n:
        return 0
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= 2 ** (n - i) - 1
        denominator *= 2 ** (r - i) - 1
    check(numerator % denominator == 0)
    return numerator // denominator


def spanning_history_count(t, r):
    if r > t:
        return 0
    ans = 1
    for i in range(r):
        ans *= 2**t - 2**i
    return ans


def poly_multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def poly_power(base, exponent):
    out = [1]
    for _ in range(exponent):
        out = poly_multiply(out, base)
    return out


def stabilizer(target, npoints):
    return tuple(
        v
        for v in range(npoints)
        if all(((target >> x) & 1) == ((target >> (x ^ v)) & 1)
               for x in range(npoints))
    )


def predicted_coefficients(d, t, target):
    npoints = 2**d
    b = target.bit_count()
    stab = stabilizer(target, npoints)
    check(len(stab) & (len(stab) - 1) == 0)
    s = len(stab).bit_length() - 1
    out = [0] * (npoints + 1)
    for r in range(s + 1):
        q = 2**r
        outside_cosets = 2 ** (d - r) - b // q
        check(b % q == 0)
        check(outside_cosets >= 0)
        base = [comb(q, k) for k in range(q)]
        local = poly_power(base, outside_cosets)
        history_factor = gaussian2(s, r) * spanning_history_count(t, r)
        for extra, coefficient in enumerate(local):
            out[b + extra] += history_factor * coefficient
    return out, s


def literal_atlas(d, t):
    npoints = 2**d
    phase = 2**npoints
    observed = defaultdict(int)
    history_count = 0
    rank_counts = defaultdict(int)
    for history in histories(npoints, t):
        history_count += 1
        span = span_set(history)
        rank = len(span).bit_length() - 1
        rank_counts[rank] += 1
        for source in range(phase):
            direct = literal_iterate(source, history, npoints)
            compressed = erode_span(source, span, npoints)
            check(direct == compressed, (d, t, source, history))
            observed[(direct, source.bit_count())] += 1
    check(history_count == npoints**t)
    for r in range(d + 1):
        expected_rank = gaussian2(d, r) * spanning_history_count(t, r)
        check(rank_counts[r] == expected_rank,
              ("rank", d, t, r, rank_counts[r], expected_rank))
    for target in range(phase):
        predicted, _ = predicted_coefficients(d, t, target)
        for size in range(npoints + 1):
            check(observed[(target, size)] == predicted[size],
                  ("fibre", d, t, target, size,
                   observed[(target, size)], predicted[size]))
    for size in range(npoints + 1):
        check(sum(observed[(target, size)] for target in range(phase))
              == comb(npoints, size) * npoints**t)
    ROWS.append(
        f"atlas d={d} t={t} histories={history_count} pairs={phase * history_count}"
    )


def all_subspaces(d):
    npoints = 2**d
    zero = frozenset({0})
    seen = {zero}
    queue = deque([zero])
    while queue:
        space = queue.popleft()
        for v in range(npoints):
            if v in space:
                continue
            enlarged = frozenset(space | {h ^ v for h in space})
            if enlarged not in seen:
                seen.add(enlarged)
                queue.append(enlarged)
    return seen


def witness_and_fixed_checks():
    for d in range(7):
        npoints = 2**d
        full = (1 << npoints) - 1
        witness = full ^ 1
        spaces = all_subspaces(d)
        for space in spaces:
            got = erode_span(witness, space, npoints)
            expected = full
            for x in space:
                expected &= ~(1 << x)
            check(got == expected, ("witness", d, space))
        ROWS.append(f"witness d={d} subspaces={len(spaces)}")

    for d in range(4):
        npoints = 2**d
        phase = 2**npoints
        fixed = []
        for source in range(phase):
            universal = True
            for v in range(npoints):
                universal &= erode_vector(source, v, npoints) == source
                check(isinstance(universal, bool))
            if universal:
                fixed.append(source)
        check(fixed == [0, phase - 1], ("fixed", d, fixed))
        ROWS.append(f"universal-fixed d={d} count={len(fixed)}")


def clock_and_recovery_checks():
    for d in range(7):
        displayed_mean = sum(
            (Fraction(2**d, 2**d - 2**r) for r in range(d)),
            Fraction(0),
        )
        # Solve the finite rank-chain hitting-time equations backwards,
        # independently of the displayed summation.
        rank_chain_mean = Fraction(0)
        for r in reversed(range(d)):
            stay = Fraction(2**r, 2**d)
            rank_chain_mean = (1 + (1 - stay) * rank_chain_mean) / (1 - stay)
        check(rank_chain_mean == displayed_mean)
        if d == 0:
            check(displayed_mean == 0)
        for t in range(0, d + 5):
            full_rank_count = 0 if t < d else spanning_history_count(t, d)
            product_numerator = 0
            if t >= d:
                product_numerator = 1
                for i in range(d):
                    product_numerator *= 2**t - 2**i
            check(full_rank_count == product_numerator)
        ROWS.append(f"clock d={d} mean={displayed_mean}")

    odd_trivial = 0
    for d in range(5):
        npoints = 2**d
        phase = 2**npoints
        by_size = defaultdict(dict)
        for target in range(phase):
            coefficients, s = predicted_coefficients(d, 1, target)
            mass = sum(coefficients)
            b = target.bit_count()
            if s == 0:
                check(mass == 1)
                if b % 2:
                    odd_trivial += 1
            else:
                check(b % (2**s) == 0)
                check(mass == 1 + (2**s - 1) * 3 ** (2 ** (d - 1) - b // 2))
            previous = by_size[b].get(s)
            if previous is not None:
                check(previous == mass)
            by_size[b][s] = mass
        for b, cells in by_size.items():
            ordered = sorted(cells.items())
            for (s0, m0), (s1, m1) in zip(ordered, ordered[1:]):
                check(s0 < s1 and m0 < m1, ("recovery", d, b, ordered))
        ROWS.append(f"recovery d={d} targets={phase} sizes={len(by_size)}")
    check(odd_trivial > 0)
    ROWS.append(f"odd-trivial-targets={odd_trivial}")


def main():
    print("P162 HOSTILE REVIEW A INDEPENDENT CHECK V1")
    for d, maximum_t in ((0, 5), (1, 6), (2, 5), (3, 4)):
        for t in range(maximum_t + 1):
            literal_atlas(d, t)
    witness_and_fixed_checks()
    clock_and_recovery_checks()
    for row in ROWS:
        print(row)
    digest = hashlib.sha256("\n".join(ROWS).encode()).hexdigest()
    print(f"ASSERTIONS {ASSERTIONS}")
    print(f"ROW_SHA256 {digest}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
