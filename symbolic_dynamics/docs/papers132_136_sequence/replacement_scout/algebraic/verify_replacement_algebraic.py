#!/usr/bin/env python3
"""Exact breadth verifier for the replacement algebra/arithmetic scout.

The program uses Python integers only.  It performs complete enumeration on
every displayed finite carrier; there is no sampling, floating point, network
access, wall-clock dependence, or third-party package.
"""

from collections import Counter
from dataclasses import dataclass
from math import comb, factorial, gcd


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def factorint(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append((n, 1))
    return out


def divisors(n):
    values = [1]
    for p, e in factorint(n):
        values = [d * p**a for d in values for a in range(e + 1)]
    return sorted(values)


def valuation(n, p):
    if n == 0:
        raise ValueError("ordinary valuation of zero requested")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def clipped_valuation(n, p, e):
    modulus = p**e
    n %= modulus
    if n == 0:
        return e
    return min(e, valuation(n, p))


def v2(n):
    return valuation(n, 2)


def phi(n):
    ans = n
    for p, _ in factorint(n):
        ans = ans // p * (p - 1)
    return ans


def sigma(n):
    ans = 1
    for p, e in factorint(n):
        ans *= (p ** (e + 1) - 1) // (p - 1)
    return ans


def tau(n):
    ans = 1
    for _, e in factorint(n):
        ans *= e + 1
    return ans


def lcm(a, b):
    return a // gcd(a, b) * b


@dataclass(frozen=True)
class Summary:
    states: int
    image: int
    fixed: int
    max_fibre: int
    periods: tuple
    max_tail: int
    recurrent: int


def functional_summary(states, update):
    states = tuple(states)
    universe = set(states)
    AUDIT.check(len(universe) == len(states), "carrier has duplicates")
    nxt = {}
    for x in states:
        y = update(x)
        AUDIT.check(y in universe, (x, y, "not a self-map"))
        nxt[x] = y

    fibres = Counter(nxt.values())
    fixed = sum(nxt[x] == x for x in states)
    periods = set()
    tails = []
    recurrent_points = set()
    for start in states:
        seen = {}
        x = start
        while x not in seen:
            AUDIT.check(x in universe)
            seen[x] = len(seen)
            x = nxt[x]
            AUDIT.check(len(seen) <= len(states) + 1)
        tail = seen[x]
        period = len(seen) - tail
        AUDIT.check(period >= 1)
        y = x
        cycle = []
        for _ in range(period):
            cycle.append(y)
            y = nxt[y]
        AUDIT.check(y == x)
        AUDIT.check(len(set(cycle)) == period)
        periods.add(period)
        tails.append(tail)
        recurrent_points.update(cycle)

    AUDIT.check(sum(fibres.values()) == len(states))
    AUDIT.check(fixed == sum(1 for x in states if x in recurrent_points and nxt[x] == x))
    return Summary(
        states=len(states),
        image=len(fibres),
        fixed=fixed,
        max_fibre=max(fibres.values()),
        periods=tuple(sorted(periods)),
        max_tail=max(tails),
        recurrent=len(recurrent_points),
    )


def summary_line(handle, carrier, params, summaries, decision):
    periods = sorted({r for s in summaries for r in s.periods})
    fixed = [s.fixed for s in summaries]
    images = [s.image for s in summaries]
    recurrent = [s.recurrent for s in summaries]
    return (
        f"{handle}|{carrier}|params={params}|states={sum(s.states for s in summaries)}"
        f"|periods={','.join(map(str, periods))}|max_tail={max(s.max_tail for s in summaries)}"
        f"|fixed={min(fixed)}..{max(fixed)}|recurrent={min(recurrent)}..{max(recurrent)}"
        f"|image={min(images)}..{max(images)}|max_fibre={max(s.max_fibre for s in summaries)}"
        f"|{decision}"
    )


# ---------------------------------------------------------------------------
# Integer divisor and binomial carriers


DIVISOR_PARAMETERS = (3**7, 3**4 * 5**3, 3**3 * 5**2 * 7**2)


def delta(n, d):
    c = n // d
    return lcm(d, c) // gcd(d, c)


DIVISOR_SYSTEMS = (
    (
        "D01",
        "divisors; complementary-factor lcm/gcd disparity",
        lambda n, d: delta(n, d),
        "PROMOTE_INTERNAL_NOVELTY_HOLD",
    ),
    (
        "D02",
        "odd divisors; gcd of n with complementary-factor sum",
        lambda n, d: gcd(n, d + n // d),
        "KILL_COMPLEMENT_MEET_FOLD",
    ),
    (
        "D03",
        "odd divisors; gcd of n with quadratic/complement sum",
        lambda n, d: gcd(n, d * d + n // d),
        "KILL_SHORT_RECURRENT_SIBLING",
    ),
    (
        "D04",
        "odd divisors; gcd of n with quadratic/complement difference",
        lambda n, d: gcd(n, abs(d * d - n // d)),
        "KILL_EXCEPTIONAL_SIBLING",
    ),
    (
        "D05",
        "divisors; cross-totient factor sum",
        lambda n, d: gcd(n, d * phi(n // d) + (n // d) * phi(d)),
        "KILL_PRATT_TOTIENT_ENGINE",
    ),
    (
        "D06",
        "divisors; aligned-totient factor sum",
        lambda n, d: gcd(n, d * phi(d) + (n // d) * phi(n // d)),
        "KILL_PRATT_TOTIENT_ENGINE",
    ),
    (
        "D07",
        "divisors; gcd of complementary totient sum",
        lambda n, d: gcd(n, phi(d) + phi(n // d)),
        "KILL_TOTIENT_VALUE_NO_SPINE",
    ),
    (
        "D08",
        "divisors; gcd of complementary totient difference",
        lambda n, d: gcd(n, abs(phi(d) - phi(n // d))),
        "KILL_TOTIENT_VALUE_NO_SPINE",
    ),
    (
        "D09",
        "divisors; proper-divisor-sum restriction",
        lambda n, d: gcd(n, sigma(d) - d),
        "KILL_ALIQUOT_OWNER_NO_SPINE",
    ),
    (
        "D10",
        "divisors; divisor-count restriction",
        lambda n, d: gcd(n, tau(d)),
        "KILL_DIVISOR_COUNT_COLLAPSE",
    ),
)


def run_divisor_systems():
    lines = []
    total_states = 0
    system_summaries = {}
    for handle, carrier, rule, decision in DIVISOR_SYSTEMS:
        rows = []
        for n in DIVISOR_PARAMETERS:
            ds = divisors(n)
            rows.append(functional_summary(ds, lambda d, n=n, rule=rule: rule(n, d)))
        system_summaries[handle] = rows
        total_states += sum(s.states for s in rows)
        lines.append(summary_line(handle, carrier, len(DIVISOR_PARAMETERS), rows, decision))

    factorial_params = (2**8, 3**5, 5**3)
    rows = []
    for n in factorial_params:
        ds = divisors(n)
        cache = {d: gcd(n, factorial(d)) for d in ds}
        rows.append(functional_summary(ds, cache.__getitem__))
    system_summaries["D11"] = rows
    total_states += sum(s.states for s in rows)
    lines.append(summary_line(
        "D11", "prime-power divisors; factorial restriction", len(factorial_params), rows,
        "KILL_LEGENDRE_THRESHOLD_COROLLARY",
    ))

    section_specs = (
        ("D12", lambda n, k: gcd(n, comb(n, k)), "binomial-section gcd", "KILL_KUMMER_ONE_LINE_COROLLARY"),
        ("D13", lambda n, k: gcd(n, comb(2 * k, k)), "central-binomial gcd", "KILL_KUMMER_CARRY_OWNER"),
        ("D14", lambda n, k: gcd(n, comb(2 * k, k) // (k + 1)), "Catalan-section gcd", "KILL_CATALAN_VALUATION_OWNER"),
    )
    section_params = ((2, 7), (3, 4), (5, 3))
    for handle, rule, carrier, decision in section_specs:
        rows = []
        for p, e in section_params:
            n = p**e
            rows.append(functional_summary(range(n + 1), lambda k, n=n, rule=rule: rule(n, k)))
        system_summaries[handle] = rows
        total_states += sum(s.states for s in rows)
        lines.append(summary_line(handle, carrier, len(section_params), rows, decision))
    return lines, total_states, system_summaries


# ---------------------------------------------------------------------------
# Valuation-controlled maps on finite local rings


LOCAL_PARAMETERS = ((2, 9), (3, 6), (5, 4))


def lowbit_add(p, e, x):
    modulus = p**e
    if x == 0:
        return 0
    return (x + p ** clipped_valuation(x, p, e)) % modulus


def lowbit_subtract(p, e, x):
    modulus = p**e
    if x == 0:
        return 0
    return (x - p ** clipped_valuation(x, p, e)) % modulus


def valuation_reflect(p, e, x):
    modulus = p**e
    if x == 0:
        return 0
    return (p ** clipped_valuation(x, p, e) - x) % modulus


def mirror_kick(p, e, x):
    modulus = p**e
    if x == 0:
        return 0
    a = clipped_valuation(x, p, e)
    return (x + p ** (e - 1 - a)) % modulus


def quadratic_defect_kick(p, e, x):
    modulus = p**e
    a = clipped_valuation(x * x + 1, p, e)
    return (x + p**a) % modulus


def idempotent_defect_kick(p, e, x):
    modulus = p**e
    a = clipped_valuation(x * (x - 1), p, e)
    return (x + p**a) % modulus


LOCAL_SYSTEMS = (
    ("V01", "local ring; add least p-adic place", lowbit_add, "KILL_LOWBIT_FENWICK_AND_P100"),
    ("V02", "local ring; subtract least p-adic place", lowbit_subtract, "KILL_DIGIT_SUM_AND_P100"),
    ("V03", "local ring; reflect about least p-adic place", valuation_reflect, "KILL_GATED_INVOLUTION_THIN"),
    ("V04", "local ring; add mirror valuation place", mirror_kick, "KILL_NO_UNIFORM_THEOREM_SPINE"),
    ("V05", "local ring; quadratic-defect valuation kick", quadratic_defect_kick, "KILL_NO_UNIFORM_THEOREM_SPINE"),
    ("V06", "local ring; idempotent-defect valuation kick", idempotent_defect_kick, "KILL_NO_UNIFORM_THEOREM_SPINE"),
)


def run_local_systems():
    lines = []
    total_states = 0
    system_summaries = {}
    for handle, carrier, rule, decision in LOCAL_SYSTEMS:
        rows = []
        for p, e in LOCAL_PARAMETERS:
            modulus = p**e
            rows.append(functional_summary(
                range(modulus), lambda x, p=p, e=e, rule=rule: rule(p, e, x)
            ))
        system_summaries[handle] = rows
        total_states += sum(s.states for s in rows)
        lines.append(summary_line(handle, carrier, len(LOCAL_PARAMETERS), rows, decision))
    return lines, total_states, system_summaries


# ---------------------------------------------------------------------------
# Polynomial-divisor maps over finite prime fields


ZERO = (0,)
ONE = (1,)


def poly_trim(f):
    f = list(f)
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return tuple(f)


def poly_add(f, g, p):
    n = max(len(f), len(g))
    return poly_trim(tuple(((f[i] if i < len(f) else 0) + (g[i] if i < len(g) else 0)) % p for i in range(n)))


def poly_sub(f, g, p):
    n = max(len(f), len(g))
    return poly_trim(tuple(((f[i] if i < len(f) else 0) - (g[i] if i < len(g) else 0)) % p for i in range(n)))


def poly_mul(f, g, p):
    if f == ZERO or g == ZERO:
        return ZERO
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i + j] = (out[i + j] + a * b) % p
    return poly_trim(tuple(out))


def poly_derivative(f, p):
    if len(f) <= 1:
        return ZERO
    return poly_trim(tuple((i * f[i]) % p for i in range(1, len(f))))


def poly_divmod(f, g, p):
    if g == ZERO:
        raise ZeroDivisionError
    r = list(poly_trim(f))
    q = [0] * max(1, len(r) - len(g) + 1)
    inv = pow(g[-1], -1, p)
    while not (len(r) == 1 and r[0] == 0) and len(r) >= len(g):
        shift = len(r) - len(g)
        c = r[-1] * inv % p
        q[shift] = c
        for i, a in enumerate(g):
            r[i + shift] = (r[i + shift] - c * a) % p
        r = list(poly_trim(tuple(r)))
    return poly_trim(tuple(q)), poly_trim(tuple(r))


def poly_monic(f, p):
    f = poly_trim(f)
    if f == ZERO:
        return ZERO
    inv = pow(f[-1], -1, p)
    return tuple(c * inv % p for c in f)


def poly_gcd(f, g, p):
    while g != ZERO:
        _, r = poly_divmod(f, g, p)
        f, g = g, r
    return poly_monic(f, p)


def polynomial_divisor_carrier(p, root_count):
    factors = [((-a) % p, 1) for a in range(root_count)]
    states = [ONE]
    modulus = ONE
    for h in factors:
        states += [poly_mul(f, h, p) for f in states]
        modulus = poly_mul(modulus, h, p)
    states = sorted(set(states), key=lambda f: (len(f), f))
    AUDIT.check(len(states) == 2**root_count)
    return modulus, states


def exact_poly_quotient(m, f, p):
    q, r = poly_divmod(m, f, p)
    if r != ZERO:
        raise AssertionError("non-divisor in polynomial carrier")
    return q


def polynomial_update(kind, p, modulus, f):
    c = exact_poly_quotient(modulus, f, p)
    df = poly_derivative(f, p)
    dc = poly_derivative(c, p)
    if kind == "F01":
        h = poly_add(df, c, p)
    elif kind == "F02":
        h = poly_add(poly_mul(f, df, p), c, p)
    elif kind == "F03":
        h = poly_sub(poly_mul(df, c, p), poly_mul(f, dc, p), p)
    elif kind == "F04":
        h = poly_add(poly_mul(f, f, p), dc, p)
    else:
        raise ValueError(kind)
    return poly_gcd(modulus, h, p)


POLYNOMIAL_SYSTEMS = (
    ("F01", "split-polynomial divisors; derivative plus complement", "KILL_NO_ALL_PARAMETER_SPINE"),
    ("F02", "split-polynomial divisors; weighted derivative plus complement", "KILL_NO_ALL_PARAMETER_SPINE"),
    ("F03", "split-polynomial divisors; complementary Wronskian gcd", "KILL_DIFFERENTIAL_IDENTITY_DOMINATED"),
    ("F04", "split-polynomial divisors; square plus complement derivative", "KILL_NO_ALL_PARAMETER_SPINE"),
)


def run_polynomial_systems():
    params = ((7, 5), (11, 6), (13, 7))
    carriers = [(p, *polynomial_divisor_carrier(p, r)) for p, r in params]
    lines = []
    total_states = 0
    system_summaries = {}
    for handle, carrier, decision in POLYNOMIAL_SYSTEMS:
        rows = []
        for p, modulus, states in carriers:
            rows.append(functional_summary(
                states,
                lambda f, handle=handle, p=p, modulus=modulus: polynomial_update(handle, p, modulus, f),
            ))
        system_summaries[handle] = rows
        total_states += sum(s.states for s in rows)
        lines.append(summary_line(handle, carrier, len(params), rows, decision))
    return lines, total_states, system_summaries


# ---------------------------------------------------------------------------
# Focused exact theorem checks


def exponent_of_divisor(d, p):
    if d == 1:
        return 0
    return valuation(d, p)


def fold_mod(x, modulus):
    r = x % modulus
    return min(r, modulus - r)


def delta_iterate_formula(n, d, t):
    ans = 1
    for p, e in factorint(n):
        a = exponent_of_divisor(d, p)
        j = e - a
        jt = fold_mod((2**t) * j, 2 * e)
        ans *= p ** (e - jt)
    return ans


def delta_fixed_formula(n, t):
    ans = 1
    for _, e in factorint(n):
        ans *= (gcd(2 * e, 2**t - 1) + gcd(2 * e, 2**t + 1)) // 2
    return ans


def delta_target_fibre_formula(n, target):
    ans = 1
    for p, e in factorint(n):
        b = exponent_of_divisor(target, p)
        if (e - b) % 2:
            return 0
        ans *= 1 if b == 0 else 2
    return ans


def delta_depth_formula(n, d):
    depth = 0
    for p, e in factorint(n):
        a = exponent_of_divisor(d, p)
        j = e - a
        s = v2(2 * e)
        coordinate = 0 if j == 0 else max(0, s - v2(j))
        depth = max(depth, coordinate)
    return depth


def actual_tail_period(start, update, bound):
    seen = {}
    x = start
    while x not in seen:
        seen[x] = len(seen)
        x = update(x)
        AUDIT.check(len(seen) <= bound + 1)
    return seen[x], len(seen) - seen[x]


def focus_delta():
    params = (
        2**12,
        3**9 * 5**6,
        2**8 * 3**7 * 5**5,
        2**5 * 7**4 * 11**3,
    )
    states_total = 0
    max_tail = 0
    recurrent_counts = []
    for n in params:
        ds = divisors(n)
        states_total += len(ds)
        factors = factorint(n)
        for d in ds:
            direct = delta(n, d)
            expected = 1
            for p, e in factors:
                a = exponent_of_divisor(d, p)
                expected *= p ** abs(2 * a - e)
            AUDIT.check(direct == expected)
            x = d
            for t in range(13):
                AUDIT.check(x == delta_iterate_formula(n, d, t))
                x = delta(n, x)
            tail, _ = actual_tail_period(d, lambda z, n=n: delta(n, z), len(ds))
            AUDIT.check(tail == delta_depth_formula(n, d))
            max_tail = max(max_tail, tail)

        fibres = Counter(delta(n, d) for d in ds)
        for target in ds:
            AUDIT.check(fibres.get(target, 0) == delta_target_fibre_formula(n, target))

        for t in range(1, 13):
            actual_fixed = sum(delta_iterate_formula(n, d, t) == d for d in ds)
            AUDIT.check(actual_fixed == delta_fixed_formula(n, t))

        sharp_tail = max(v2(2 * e) for _, e in factors)
        AUDIT.check(max(delta_depth_formula(n, d) for d in ds) == sharp_tail)
        recurrent = 1
        for _, e in factors:
            s = v2(2 * e)
            odd_part = (2 * e) // (2**s)
            recurrent *= (odd_part + 1) // 2
        recurrent_counts.append(recurrent)
        AUDIT.check(sum(delta_depth_formula(n, d) == 0 for d in ds) == recurrent)

        for t in range(sharp_tail + 1):
            actual = sum(delta_depth_formula(n, d) <= t for d in ds)
            expected = 1
            for _, e in factors:
                s = v2(2 * e)
                step = 2 ** max(s - t, 0)
                expected *= e // step + 1
            AUDIT.check(actual == expected)

    return (
        f"FOCUS_D01|params={len(params)}|states={states_total}|all_iterates=t<=12"
        f"|every_target_fibre=checked|fixed_iterates=t<=12|max_tail={max_tail}"
        f"|recurrent_counts={','.join(map(str, recurrent_counts))}|PASS"
    )


def focus_binomial_section():
    params = ((2, 9), (3, 6), (5, 4), (7, 3))
    states_total = 0
    for p, e in params:
        n = p**e
        states_total += n + 1
        update = lambda k, n=n: gcd(n, comb(n, k))
        fibres = Counter(update(k) for k in range(n + 1))
        for k in range(n + 1):
            expected = 1 if k == 0 else p ** (e - valuation(k, p))
            AUDIT.check(update(k) == expected)
        for b in range(e + 1):
            expected_fibre = 2 if b == 0 else p**b - p ** (b - 1)
            AUDIT.check(fibres[p**b] == expected_fibre)
        for a in range(e + 1):
            AUDIT.check(update(p**a) == p ** (e - a))
    return (
        f"FOCUS_D12|params={len(params)}|states={states_total}"
        f"|Kummer_formula=checked|every_target_fibre=checked"
        f"|recurrent_involution_on_prime_powers=checked|KILL_ZERO_RESIDUAL"
    )


def main():
    before = AUDIT.assertions
    divisor_lines, divisor_states, divisor_summaries = run_divisor_systems()
    divisor_assertions = AUDIT.assertions - before

    before = AUDIT.assertions
    local_lines, local_states, local_summaries = run_local_systems()
    local_assertions = AUDIT.assertions - before

    before = AUDIT.assertions
    polynomial_lines, polynomial_states, polynomial_summaries = run_polynomial_systems()
    polynomial_assertions = AUDIT.assertions - before

    before = AUDIT.assertions
    delta_line = focus_delta()
    binomial_line = focus_binomial_section()
    focus_assertions = AUDIT.assertions - before

    all_summaries = {}
    all_summaries.update(divisor_summaries)
    all_summaries.update(local_summaries)
    all_summaries.update(polynomial_summaries)
    AUDIT.check(len(all_summaries) == 24)
    decisions = divisor_lines + local_lines + polynomial_lines
    AUDIT.check(sum("PROMOTE_INTERNAL" in line for line in decisions) == 1)
    AUDIT.check(sum("|KILL_" in line for line in decisions) == 23)

    print("REPLACEMENT_ALGEBRAIC_SCOUT_V1")
    for line in decisions:
        print(line)
    print(delta_line)
    print(binomial_line)
    print(
        f"LEDGER|systems=24|promotions=1|kills=23|enumerated_states="
        f"{divisor_states + local_states + polynomial_states}"
        f"|divisor_assertions={divisor_assertions}|local_assertions={local_assertions}"
        f"|polynomial_assertions={polynomial_assertions}|focus_assertions={focus_assertions}"
        f"|assertions={AUDIT.assertions}|PASS"
    )
    print("EXACT_ARITHMETIC=python_integers")
    print("FLOATING_POINT=none")
    print("SAMPLING=none")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
