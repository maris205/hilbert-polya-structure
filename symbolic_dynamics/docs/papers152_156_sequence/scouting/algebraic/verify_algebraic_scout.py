#!/usr/bin/env python3
"""Deterministic exact falsifier for the P152--P156 algebraic scout.

Enumeration is counterexample pressure, not proof.  The two deepest controls
are QTS (a trace-square reciprocal map on F_{p^2}) and PDG (iterated
derivative-gcd on bounded monic polynomials).  Twelve deliberately different
negative controls keep the breadth search honest.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import gcd


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str = "") -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message or f"assertion {self.assertions} failed")


A = Audit()


def primes_upto(n: int) -> list[int]:
    out = []
    for x in range(2, n + 1):
        if all(x % p for p in out if p * p <= x):
            out.append(x)
    return out


def vp(x: int, p: int) -> int:
    if x == 0:
        return 10**9
    ans = 0
    while x % p == 0:
        ans += 1
        x //= p
    return ans


def multiplicative_order(a: int, p: int) -> int:
    a %= p
    if a == 0:
        raise ValueError("zero has no multiplicative order")
    for r in range(1, p):
        if pow(a, r, p) == 1:
            return r
    raise AssertionError("order not found")


def nonsquare(p: int) -> int:
    squares = {x * x % p for x in range(p)}
    return next(x for x in range(2, p) if x not in squares)


class QuadField:
    """F_p[s]/(s^2-d) for an odd prime p and a nonsquare d."""

    def __init__(self, p: int) -> None:
        self.p = p
        self.d = nonsquare(p)
        self.states = [(a, b) for a in range(p) for b in range(p)]

    def add(self, x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
        p = self.p
        return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

    def scale(self, c: int, x: tuple[int, int]) -> tuple[int, int]:
        p = self.p
        return (c * x[0] % p, c * x[1] % p)

    def mul(self, x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
        p, d = self.p, self.d
        return ((x[0] * y[0] + d * x[1] * y[1]) % p,
                (x[0] * y[1] + x[1] * y[0]) % p)

    def trace(self, x: tuple[int, int]) -> int:
        return 2 * x[0] % self.p

    def norm(self, x: tuple[int, int]) -> int:
        return (x[0] * x[0] - self.d * x[1] * x[1]) % self.p

    def conj(self, x: tuple[int, int]) -> tuple[int, int]:
        return (x[0], (-x[1]) % self.p)

    def inv(self, x: tuple[int, int]) -> tuple[int, int]:
        if x == (0, 0):
            return (0, 0)
        return self.scale(pow(self.norm(x), -1, self.p), self.conj(x))


def orbit_data(states, step):
    tails = Counter()
    periods = Counter()
    point = {}
    for x in states:
        seen = {}
        path = []
        y = x
        while y not in seen:
            if y in point:
                tail0, period = point[y]
                for j in range(len(path) - 1, -1, -1):
                    tail0 += 1
                    point[path[j]] = (tail0, period)
                break
            seen[y] = len(path)
            path.append(y)
            y = step(y)
        else:
            start = seen[y]
            period = len(path) - start
            for j in range(start, len(path)):
                point[path[j]] = (0, period)
            tail0 = 0
            for j in range(start - 1, -1, -1):
                tail0 += 1
                point[path[j]] = (tail0, period)
    for x in states:
        t, r = point[x]
        tails[t] += 1
        periods[r] += 1
    return point, tails, periods


def qts_step(K: QuadField, x: tuple[int, int]) -> tuple[int, int]:
    tr = K.trace(x)
    return K.scale(tr * tr, K.inv(x))


def trace_quotient_step(K: QuadField, x: tuple[int, int]) -> tuple[int, int]:
    return K.scale(K.trace(x), K.inv(x))


def normalized_frobenius_step(K: QuadField, x: tuple[int, int]) -> tuple[int, int]:
    tr = K.trace(x)
    if tr == 0:
        return (0, 0)
    return K.scale(pow(tr, -1, K.p), K.conj(x))


def audit_qts() -> tuple[int, int, list[str]]:
    summaries = []
    boxes = 0
    states_seen = 0
    for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
        K = QuadField(p)
        states = K.states
        step = lambda x: qts_step(K, x)
        boxes += 1
        states_seen += len(states)
        fibres = Counter(step(x) for x in states)
        point, tails, periods = orbit_data(states, step)
        A.check(tails == Counter({0: p * p - p + 1, 1: p - 1}), f"QTS tails p={p}")
        A.check(len(fibres) == p * p - p + 1, f"QTS image p={p}")
        for y in states:
            expected = p if y == (0, 0) else (1 if K.trace(y) != 0 else 0)
            A.check(fibres[y] == expected, f"QTS fibre p={p}, y={y}")
        for x in states:
            y = step(x)
            A.check(y in set(states), "QTS closure")
            if K.trace(x) == 0:
                A.check(y == (0, 0), "QTS trace-zero collapse")
                continue
            a = K.trace(x)
            u = K.scale(pow(a, -1, p), x)
            c = K.norm(u)
            expected = K.scale(a * pow(c, -1, p), K.conj(u))
            A.check(y == expected, "QTS skew-product coordinate")
            predicted_period = (multiplicative_order(4, p) if u == (pow(2, -1, p), 0)
                                else __import__("math").lcm(2, multiplicative_order(c, p)))
            A.check(point[x] == (0, predicted_period), f"QTS period p={p}, x={x}")
        # Fixed-iterate formula, which is stronger than comparing cycle maxima.
        for t in range(1, 2 * (p - 1) + 1):
            actual = 0
            for x in states:
                y = x
                for _ in range(t):
                    y = step(y)
                actual += (y == x)
            base = int(pow(4, t, p) == 1)
            conic = 0
            if t % 2 == 0:
                for c in range(1, p):
                    delta = (1 - 4 * c) % p
                    chi = 0 if delta == 0 else (1 if pow(delta, (p - 1) // 2, p) == 1 else -1)
                    if chi == -1 and pow(c, t, p) == 1:
                        conic += 1
            predicted = 1 + (p - 1) * (base + 2 * conic)
            A.check(actual == predicted, f"QTS fixed iterate p={p}, t={t}")
        summaries.append(
            f"p={p}: image={len(fibres)}, tails={dict(sorted(tails.items()))}, "
            f"max_period={max(periods)}"
        )
    return boxes, states_seen, summaries


# ---------- small polynomial arithmetic for PDG ----------

def poly_trim(f: tuple[int, ...], p: int) -> tuple[int, ...]:
    a = list(f)
    while len(a) > 1 and a[-1] % p == 0:
        a.pop()
    return tuple(x % p for x in a)


def poly_degree(f: tuple[int, ...], p: int) -> int:
    f = poly_trim(f, p)
    return -1 if f == (0,) else len(f) - 1


def poly_mul(f: tuple[int, ...], g: tuple[int, ...], p: int) -> tuple[int, ...]:
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i + j] = (out[i + j] + a * b) % p
    return poly_trim(tuple(out), p)


def poly_divmod(f: tuple[int, ...], g: tuple[int, ...], p: int):
    f = list(poly_trim(f, p))
    g = poly_trim(g, p)
    if g == (0,):
        raise ZeroDivisionError
    q = [0] * max(1, len(f) - len(g) + 1)
    invlead = pow(g[-1], -1, p)
    while len(f) >= len(g) and not (len(f) == 1 and f[0] == 0):
        k = len(f) - len(g)
        c = f[-1] * invlead % p
        q[k] = c
        for j in range(len(g)):
            f[k + j] = (f[k + j] - c * g[j]) % p
        while len(f) > 1 and f[-1] == 0:
            f.pop()
    return poly_trim(tuple(q), p), poly_trim(tuple(f), p)


def poly_monic(f: tuple[int, ...], p: int) -> tuple[int, ...]:
    f = poly_trim(f, p)
    if f == (0,):
        return f
    c = pow(f[-1], -1, p)
    return tuple(c * x % p for x in f)


def poly_gcd(f: tuple[int, ...], g: tuple[int, ...], p: int) -> tuple[int, ...]:
    while poly_trim(g, p) != (0,):
        _, r = poly_divmod(f, g, p)
        f, g = g, r
    return poly_monic(f, p)


def poly_derivative(f: tuple[int, ...], p: int) -> tuple[int, ...]:
    if len(f) <= 1:
        return (0,)
    return poly_trim(tuple(i * f[i] % p for i in range(1, len(f))), p)


def monic_polynomials(p: int, N: int):
    yield (1,)
    for d in range(1, N + 1):
        for low in product(range(p), repeat=d):
            yield tuple(low) + (1,)


def irreducibles(p: int, N: int) -> list[tuple[int, ...]]:
    irr = []
    for f in monic_polynomials(p, N):
        d = poly_degree(f, p)
        if d <= 0:
            continue
        reducible = False
        for g in irr:
            if poly_degree(g, p) > d // 2:
                break
            if poly_divmod(f, g, p)[1] == (0,):
                reducible = True
                break
        if not reducible:
            irr.append(f)
    return irr


def factor_monic(f: tuple[int, ...], irr, p: int):
    if f == (1,):
        return ()
    x = f
    fac = []
    for g in irr:
        e = 0
        while poly_divmod(x, g, p)[1] == (0,):
            x = poly_divmod(x, g, p)[0]
            e += 1
        if e:
            fac.append((g, e))
        if x == (1,):
            break
    A.check(x == (1,), f"factorization incomplete: p={p}, f={f}, residue={x}")
    return tuple(fac)


def poly_pow(f: tuple[int, ...], e: int, p: int) -> tuple[int, ...]:
    out = (1,)
    for _ in range(e):
        out = poly_mul(out, f, p)
    return out


def audit_pdg() -> tuple[int, int, list[str]]:
    boxes_spec = [(3, 2), (5, 3), (7, 4), (11, 3), (13, 3), (17, 3)]
    summaries = []
    states_seen = 0
    for p, N in boxes_spec:
        states = list(monic_polynomials(p, N))
        state_set = set(states)
        irr = irreducibles(p, N)
        factors = {f: factor_monic(f, irr, p) for f in states}
        step = lambda f: poly_gcd(f, poly_derivative(f, p), p)
        arrows = {f: step(f) for f in states}
        fibres = Counter(arrows.values())
        states_seen += len(states)
        depths = Counter()
        for f in states:
            g = arrows[f]
            A.check(g in state_set, "PDG closure")
            fac = factors[f]
            predicted = (1,)
            for h, e in fac:
                predicted = poly_mul(predicted, poly_pow(h, e - 1, p), p)
            A.check(g == predicted, f"PDG multiplicity decrement p={p}, f={f}")
            depth = 0 if f == (1,) else max(e for _, e in fac)
            y = f
            for _ in range(depth):
                y = arrows[y]
            A.check(y == (1,), "PDG absorption upper bound")
            if depth:
                z = f
                for _ in range(depth - 1):
                    z = arrows[z]
                A.check(z != (1,), "PDG sharp pointwise depth")
            depths[depth] += 1
        # Every-target image condition and degree-truncated fibre product.
        for g in states:
            facg = factors[g]
            rad_degree = sum(poly_degree(h, p) for h, _ in facg)
            budget = N - poly_degree(g, p) - rad_degree
            predicted_count = 0
            if budget >= 0:
                forbidden = {h for h, _ in facg}
                coeff = [0] * (budget + 1)
                coeff[0] = 1
                for h in irr:
                    d = poly_degree(h, p)
                    if h in forbidden or d > budget:
                        continue
                    for k in range(budget, d - 1, -1):
                        coeff[k] += coeff[k - d]
                predicted_count = sum(coeff)
            A.check(fibres[g] == predicted_count,
                    f"PDG fibre p={p}, N={N}, g={g}, got={fibres[g]}, want={predicted_count}")
        A.check(max(depths) == N, f"PDG global depth p={p}, N={N}")
        A.check(depths[N] == p, f"PDG deepest shell p={p}, N={N}")
        summaries.append(
            f"(p,N)=({p},{N}): states={len(states)}, image={len(fibres)}, "
            f"depths={dict(sorted(depths.items()))}, max_fibre={max(fibres.values())}"
        )
    return len(boxes_spec), states_seen, summaries


def audit_trace_controls() -> tuple[int, int, list[str]]:
    summaries = []
    states_seen = 0
    for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        K = QuadField(p)
        states_seen += 2 * p * p
        for name, step in [
            ("TQI", lambda x: trace_quotient_step(K, x)),
            ("NTF", lambda x: normalized_frobenius_step(K, x)),
        ]:
            fibres = Counter(step(x) for x in K.states)
            point, tails, periods = orbit_data(K.states, step)
            A.check(tails == Counter({0: p + 1, 1: p * p - p - 1}), f"{name} tails p={p}")
            A.check(sorted(fibres.values()) == sorted([p] + [p - 1] * p), f"{name} fibres p={p}")
            A.check(max(periods) <= 2, f"{name} recurrent involution p={p}")
        summaries.append(f"p={p}: each image={p+1}, tails=0:{p+1}/1:{p*p-p-1}, period<=2")
    return 20, states_seen, summaries


def audit_mobius_ideal() -> tuple[int, int, list[str]]:
    summaries = []
    states_seen = 0
    boxes = 0
    for p in [3, 5, 7]:
        for e in range(2, 7):
            mod = p**e
            states = list(range(0, mod, p))
            step = lambda x: x * pow((1 + x) % mod, -1, mod) % mod
            point, tails, periods = orbit_data(states, step)
            A.check(set(tails) == {0}, "MBI is a permutation")
            for x in states:
                a = e if x == 0 else vp(x, p)
                predicted = 1 if x == 0 else p ** max(0, e - 2 * a)
                A.check(point[x] == (0, predicted), "MBI period formula")
            summaries.append(f"p={p},e={e}: states={len(states)}, max_period={max(periods)}")
            states_seen += len(states)
            boxes += 1
    return boxes, states_seen, summaries


def audit_divisor_deficit() -> tuple[int, int, list[str]]:
    summaries = []
    states_seen = 0
    for e in range(2, 81):
        states = list(range(e + 1))
        step = lambda a: max(0, 2 * a - e)
        point, tails, periods = orbit_data(states, step)
        for a in states:
            if a in (0, e):
                A.check(point[a] == (0, 1), "DDE endpoints")
            else:
                b = e - a
                t = 0
                while (1 << t) * b < e:
                    t += 1
                A.check(point[a] == (t, 1), "DDE clock")
        states_seen += len(states)
        if e in (8, 16, 32, 64, 80):
            summaries.append(f"e={e}: tails={dict(sorted(tails.items()))}")
    return 79, states_seen, summaries


def factor_integer(n: int):
    out = Counter()
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] += 1
            n //= d
        d += 1
    if n > 1:
        out[n] += 1
    return out


def euler_phi(n: int) -> int:
    ans = n
    for p in factor_integer(n):
        ans = ans // p * (p - 1)
    return ans


def audit_radical_and_euler() -> tuple[int, int, list[str]]:
    B = 5000
    states = list(range(1, B + 1))
    def radical(n):
        r = 1
        for p in factor_integer(n):
            r *= p
        return r
    rdf = lambda n: n // radical(n)
    depths = Counter()
    for n in states:
        fac = factor_integer(n)
        predicted = max(fac.values(), default=0)
        y, t = n, 0
        while y != 1:
            y = rdf(y)
            t += 1
        A.check(t == predicted, "RDF exponent clock")
        depths[t] += 1
    chain_primes = [2, 3, 7, 43]
    divisors = []
    N = 1
    for p in chain_primes:
        N *= p
    for mask in range(1 << len(chain_primes)):
        n = 1
        for i, p in enumerate(chain_primes):
            if mask >> i & 1:
                n *= p
        divisors.append(n)
    egd = lambda n: gcd(n, euler_phi(n))
    point, tails, periods = orbit_data(divisors, egd)
    A.check(set(periods) == {1}, "EGD absorbs")
    A.check(max(tails) == 4, "EGD Pratt-chain depth")
    return 2, len(states) + len(divisors), [
        f"RDF B={B}: max_depth={max(depths)}, layers={dict(sorted(depths.items()))}",
        f"EGD primes={chain_primes}: tails={dict(sorted(tails.items()))}",
    ]


def delete_fixed_points(pi: tuple[int, ...]) -> tuple[int, ...]:
    keep = [i for i, x in enumerate(pi) if i != x]
    rank = {x: j for j, x in enumerate(keep)}
    return tuple(rank[pi[i]] for i in keep)


def compose(pi, sig):
    return tuple(pi[sig[i]] for i in range(len(pi)))


def perm_power(pi, k):
    out = tuple(range(len(pi)))
    base = pi
    while k:
        if k & 1:
            out = compose(base, out)
        base = compose(base, base)
        k //= 2
    return out


def audit_permutations() -> tuple[int, int, list[str]]:
    fpd_states = 0
    for n in range(1, 9):
        for pi in permutations(range(n)):
            y = delete_fixed_points(pi)
            A.check(delete_fixed_points(y) == y, "FPD must be one-step")
            A.check(all(i != x for i, x in enumerate(y)), "FPD endpoint derangement")
            fpd_states += 1
    dsp_summaries = []
    dsp_states = 0
    for n in range(2, 8):
        states = list(permutations(range(n)))
        state_set = set(states)
        step = lambda pi: perm_power(pi, 1 + sum(pi[i] > pi[i + 1] for i in range(n - 1)))
        for pi in states:
            A.check(step(pi) in state_set, "DSP closure")
        point, tails, periods = orbit_data(states, step)
        dsp_summaries.append(f"DSP n={n}: max_tail={max(tails)}, max_period={max(periods)}")
        dsp_states += len(states)
    return 13, fpd_states + dsp_states, [f"FPD states={fpd_states}: idempotent"] + dsp_summaries


def mat_mul_2(A0, B0, p):
    a, b, c, d = A0
    e, f, g, h = B0
    return ((a*e+b*g)%p, (a*f+b*h)%p, (c*e+d*g)%p, (c*f+d*h)%p)


def audit_matrix_collapse() -> tuple[int, int, list[str]]:
    summaries = []
    states_seen = 0
    for p in [3, 5, 7, 11]:
        states = list(product(range(p), repeat=4))
        def step(M):
            a, b, c, d = M
            det = (a*d-b*c) % p
            return ((-det) % p, 0, 0, (-det) % p)
        fibres = Counter(step(M) for M in states)
        point, tails, periods = orbit_data(states, step)
        for y in states:
            if y[1] or y[2] or y[0] != y[3]:
                A.check(fibres[y] == 0, "MCH nonscalar target")
            else:
                det = (-y[0]) % p
                predicted = (p * (p*p - 1) if det else p**4 - (p*p - 1)*(p*p - p))
                A.check(fibres[y] == predicted, "MCH determinant fibre")
        summaries.append(f"p={p}: image={len(fibres)}, max_tail={max(tails)}, max_period={max(periods)}")
        states_seen += len(states)
    return 4, states_seen, summaries


def is_subspace(S: frozenset[int]) -> bool:
    return 0 in S and all((x ^ y) in S for x in S for y in S)


def dot2(x: int, y: int) -> int:
    return (x & y).bit_count() & 1


def audit_code_hull() -> tuple[int, int, list[str]]:
    summaries = []
    states_seen = 0
    for n in range(1, 5):
        universe = range(1 << n)
        spaces = []
        for mask in range(1 << (1 << n)):
            S = frozenset(x for x in universe if mask >> x & 1)
            if is_subspace(S):
                spaces.append(S)
        def hull(S):
            perp = frozenset(y for y in universe if all(dot2(x, y) == 0 for x in S))
            return S & perp
        for S in spaces:
            H = hull(S)
            A.check(hull(H) == H, "CRH idempotence")
        summaries.append(f"n={n}: subspaces={len(spaces)}, image={len({hull(S) for S in spaces})}")
        states_seen += len(spaces)
    return 4, states_seen, summaries


def audit_dual_and_qrm() -> tuple[int, int, list[str]]:
    summaries = []
    states_seen = 0
    boxes = 0
    for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
        states = list(product(range(p), repeat=2))
        dua = lambda z: (0, (-z[1]) % p)
        point, tails, periods = orbit_data(states, dua)
        A.check(tails == Counter({0: p, 1: p*p-p}), "DUA profile")
        A.check(max(periods) <= 2, "DUA involution core")
        qstates = list(range(p))
        qrm = lambda x: (1 - (0 if x == 0 else pow(x, -1, p))) % p
        fibres = Counter(qrm(x) for x in qstates)
        qpoint, qtails, qperiods = orbit_data(qstates, qrm)
        A.check(set(fibres.values()) == {1} and len(fibres) == p, "QRM permutation")
        A.check(set(qtails) == {0} and max(qperiods) <= 3, "QRM periods")
        summaries.append(
            f"p={p}: DUA tails={dict(sorted(tails.items()))}; "
            f"QRM period_counts={dict(sorted(qperiods.items()))}"
        )
        states_seen += p*p + p
        boxes += 2
    return boxes, states_seen, summaries


def main() -> None:
    handles = ["QTS", "PDG", "TQI", "NTF", "MBI", "DDE", "RDF", "EGD",
               "FPD", "DSP", "MCH", "CRH", "DUA", "QRM"]
    A.check(len(handles) == 14 and len(set(handles)) == 14, "literal-system handle registry")
    start = A.assertions
    qts = audit_qts()
    qts_assertions = A.assertions - start
    start = A.assertions
    pdg = audit_pdg()
    pdg_assertions = A.assertions - start
    rows = []
    for handles, fn in [
        ("TQI+NTF", audit_trace_controls),
        ("MBI", audit_mobius_ideal),
        ("DDE", audit_divisor_deficit),
        ("RDF+EGD", audit_radical_and_euler),
        ("FPD+DSP", audit_permutations),
        ("MCH", audit_matrix_collapse),
        ("CRH", audit_code_hull),
        ("DUA+QRM", audit_dual_and_qrm),
    ]:
        before = A.assertions
        boxes, states, summaries = fn()
        rows.append((handles, boxes, states, A.assertions - before, summaries))

    print("P152--P156 ALGEBRAIC SCOUT: DETERMINISTIC EXACT AUDIT")
    print("external_status=HOLD_EXTERNAL")
    print("scope=14 literal systems; enumeration is falsification, not proof")
    print()
    print("TOP-1 QTS quadratic trace-square reciprocal")
    print(f"boxes={qts[0]} states={qts[1]} assertions={qts_assertions}")
    for line in qts[2]:
        print("  " + line)
    print()
    print("TOP-2 PDG polynomial derivative-gcd peeling")
    print(f"boxes={pdg[0]} states={pdg[1]} assertions={pdg_assertions}")
    for line in pdg[2]:
        print("  " + line)
    print()
    print("BREADTH CONTROLS")
    for handles, boxes, states, assertions, summaries in rows:
        print(f"{handles}: boxes={boxes} states={states} assertions={assertions}")
        for line in summaries:
            print("  " + line)
    print()
    total_boxes = qts[0] + pdg[0] + sum(r[1] for r in rows)
    total_states = qts[1] + pdg[1] + sum(r[2] for r in rows)
    print(f"TOTAL boxes={total_boxes} state_box_incidences={total_states} assertions={A.assertions}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
