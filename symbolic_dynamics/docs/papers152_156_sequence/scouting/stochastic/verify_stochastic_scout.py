#!/usr/bin/env python3
"""Deterministic exact falsifier for the P152--P156 stochastic Stage-1 scout.

Only Python integers and fractions.Fraction are used.  HTM and BTB receive
the deep all-parameter-interface checks; the remaining ten mechanisms receive
literal small-carrier checks so that the kill ledger is evidence-backed.
"""

from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from itertools import permutations, product
from math import comb, factorial, gcd, prod


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def qstr(x):
    x = Q(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def gauss_solve(a, b):
    """Solve a square rational system without floating point."""
    n = len(b)
    m = [[Q(x) for x in a[i]] + [Q(b[i])] for i in range(n)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if m[i][col]), None)
        if pivot is None:
            raise ArithmeticError("singular exact system")
        m[col], m[pivot] = m[pivot], m[col]
        z = m[col][col]
        m[col] = [x / z for x in m[col]]
        for i in range(n):
            if i != col and m[i][col]:
                z = m[i][col]
                m[i] = [m[i][j] - z * m[col][j] for j in range(n + 1)]
    return [m[i][-1] for i in range(n)]


# ---------------------------------------------------------------------------
# HTM: repeated lowest-common-ancestor / longest-common-prefix meet.


def prefix_products(branching):
    ans = [1]
    for b in branching:
        ans.append(ans[-1] * b)
    return ans


def htm_literal_kernel(branching, depth):
    """Enumerate every sampled leaf; the distinguished leaf is all zeroes."""
    h = len(branching)
    counts = [0] * (h + 1)
    total = prod(branching)
    for leaf in product(*(range(b) for b in branching)):
        lcp = 0
        while lcp < h and leaf[lcp] == 0:
            lcp += 1
        counts[min(depth, lcp)] += 1
    return [Q(c, total) for c in counts]


def htm_formula_kernel(branching, depth):
    bp = prefix_products(branching)
    out = [Q(0) for _ in range(len(branching) + 1)]
    for j in range(depth):
        out[j] = Q(1, bp[j]) - Q(1, bp[j + 1])
    out[depth] = Q(1, bp[depth])
    return out


def htm_step(dist, branching):
    out = [Q(0) for _ in dist]
    for d, mass in enumerate(dist):
        for j, p in enumerate(htm_formula_kernel(branching, d)):
            out[j] += mass * p
    return out


def htm_area_by_bellman(branching):
    """Expected sum of depths, including time zero and excluding no term."""
    g = [Q(0)]
    for d in range(1, len(branching) + 1):
        ker = htm_formula_kernel(branching, d)
        lower = sum(ker[j] * g[j] for j in range(d))
        g.append((Q(d) + lower) / (1 - ker[d]))
    return g[-1]


def htm_area_formula(branching):
    bp = prefix_products(branching)
    return sum((Q(bp[k], bp[k] - 1) for k in range(1, len(bp))), Q(0))


def htm_depth_transform_direct(branching, z, y):
    """Sum_t z^t E[y^D_t] from the literal depth kernel."""
    g = [Q(1, 1 - z)]
    for d in range(1, len(branching) + 1):
        ker = htm_formula_kernel(branching, d)
        lower = sum(ker[j] * g[j] for j in range(d))
        g.append((y ** d + z * lower) / (1 - z * ker[d]))
    return g[-1]


def htm_depth_transform_formula(branching, z, y):
    bp = prefix_products(branching)
    return Q(1, 1 - z) + sum(
        (y ** k - y ** (k - 1)) / (1 - Q(z, bp[k]))
        for k in range(1, len(bp))
    )


def run_htm():
    start = ASSERTIONS
    profiles = 0
    for h in range(1, 6):
        for branching in product((2, 3, 4), repeat=h):
            profiles += 1
            bp = prefix_products(branching)
            for d in range(h + 1):
                literal = htm_literal_kernel(branching, d)
                formula = htm_formula_kernel(branching, d)
                check(literal == formula, ("HTM kernel", branching, d))
                check(sum(formula, Q(0)) == 1, ("HTM stochastic", branching, d))

            dist = [Q(0)] * (h + 1)
            dist[h] = Q(1)
            for t in range(1, 8):
                dist = htm_step(dist, branching)
                for k in range(1, h + 1):
                    tail = sum(dist[k:], Q(0))
                    check(tail == Q(1, bp[k] ** t), ("HTM layer", branching, t, k))
                check(dist[0] == 1 - Q(1, branching[0] ** t), "HTM root clock")

            # One observed time-one layer reconstructs every prefix and factor.
            dist1 = htm_step([Q(0)] * h + [Q(1)], branching)
            recovered_prefixes = [1]
            for k in range(1, h + 1):
                tail = sum(dist1[k:], Q(0))
                recovered_prefixes.append(tail.denominator // tail.numerator)
            recovered = tuple(
                recovered_prefixes[k] // recovered_prefixes[k - 1]
                for k in range(1, h + 1)
            )
            check(recovered == branching, ("HTM inverse", branching, recovered))
            check(htm_area_by_bellman(branching) == htm_area_formula(branching),
                  ("HTM area", branching))
            for z, y in ((Q(2, 5), Q(3, 2)), (Q(1, 3), Q(2))):
                check(htm_depth_transform_direct(branching, z, y)
                      == htm_depth_transform_formula(branching, z, y),
                      ("HTM all-time transform", branching, z, y))

    extrema_families = 0
    for h in range(2, 6):
        for multiset in combinations_with_replacement((2, 3, 4, 5), h):
            extrema_families += 1
            vals = {p: htm_area_formula(p) for p in set(permutations(multiset))}
            lo, hi = min(vals.values()), max(vals.values())
            minimizers = sorted(p for p, v in vals.items() if v == lo)
            maximizers = sorted(p for p, v in vals.items() if v == hi)
            check(minimizers == [tuple(sorted(multiset, reverse=True))],
                  ("HTM minimum", multiset, minimizers))
            check(maximizers == [tuple(sorted(multiset))],
                  ("HTM maximum", multiset, maximizers))

    used = ASSERTIONS - start
    return profiles, extrema_families, used


# ---------------------------------------------------------------------------
# BTB: p=1/3 local triad dynamics on a signed r-page book, at update epochs.


def btb_literal_count_kernel(mask, r):
    active = [i for i in range(r) if (mask >> i) & 1]
    if not active:
        return {(0, 0): Q(1)}
    out = {}
    den = 3 * len(active)
    full = (1 << r) - 1
    for i in active:
        private = mask ^ (1 << i)
        out[(private.bit_count(), 0)] = out.get((private.bit_count(), 0), Q(0)) + Q(2, den)
        spine = mask ^ full
        out[(spine.bit_count(), 1)] = out.get((spine.bit_count(), 1), Q(0)) + Q(1, den)
    return out


def btb_direct_transform(r, z, u):
    a = [[Q(i == j) for j in range(r)] for i in range(r)]
    b = [Q(0) for _ in range(r)]
    for k in range(1, r + 1):
        row = k - 1
        targets = ((k - 1, z * Q(2, 3)), (r - k, z * u * Q(1, 3)))
        for target, weight in targets:
            if target == 0:
                b[row] += weight
            else:
                a[row][target - 1] -= weight
    return [Q(1)] + gauss_solve(a, b)


def cheb_u(n, x):
    if n == -1:
        return Q(0)
    if n < -1:
        raise ValueError("Chebyshev index below -1")
    if n == 0:
        return Q(1)
    a, b = Q(1), 2 * x
    if n == 1:
        return b
    for _ in range(1, n):
        a, b = b, 2 * x * b - a
    return b


def btb_cheb_transform(r, z, u):
    if r == 1:
        return [Q(1), z * (2 + u) / 3]
    x = (9 + z * z * (4 - u * u)) / (12 * z)
    f1 = (
        3 * cheb_u(r - 2, x)
        - 2 * z * cheb_u(r - 3, x)
        + z * u
    ) / (
        3 * cheb_u(r - 1, x)
        - 2 * z * cheb_u(r - 2, x)
    )
    return [Q(1)] + [
        cheb_u(k - 1, x) * f1 - cheb_u(k - 2, x)
        for k in range(1, r + 1)
    ]


def btb_direct_mean(r):
    a = [[Q(i == j) for j in range(r)] for i in range(r)]
    b = [Q(1) for _ in range(r)]
    for k in range(1, r + 1):
        for target, weight in ((k - 1, Q(2, 3)), (r - k, Q(1, 3))):
            if target:
                a[k - 1][target - 1] -= weight
    return [Q(0)] + gauss_solve(a, b)


def btb_mean_formula(r, k):
    return Q(k * (r + 2 - k), 2)


def btb_parity_formula(r, k):
    return Q(r + 2 - 2 * k, r + 2)


def run_btb():
    start = ASSERTIONS
    literal_states = 0
    for r in range(1, 10):
        for mask in range(1, 1 << r):
            literal_states += 1
            k = mask.bit_count()
            ker = btb_literal_count_kernel(mask, r)
            check(sum(ker.values(), Q(0)) == 1, ("BTB stochastic", r, mask))
            collapsed = {}
            for (j, spine), p in ker.items():
                collapsed[j] = collapsed.get(j, Q(0)) + p
                if spine:
                    check(j == r - k, ("BTB spine complement", r, mask))
                else:
                    check(j == k - 1, ("BTB private balance", r, mask))
            expected = {}
            expected[k - 1] = expected.get(k - 1, Q(0)) + Q(2, 3)
            expected[r - k] = expected.get(r - k, Q(0)) + Q(1, 3)
            check(collapsed == expected, ("BTB lump", r, mask, collapsed, expected))

    points = ((Q(1, 2), Q(1)), (Q(2, 5), Q(-1)),
              (Q(1, 3), Q(2, 3)), (Q(3, 7), Q(-2, 5)))
    transform_cases = 0
    for r in range(1, 21):
        for z, u in points:
            transform_cases += 1
            direct = btb_direct_transform(r, z, u)
            formula = btb_cheb_transform(r, z, u)
            check(direct == formula, ("BTB transform", r, z, u))
            for k in range(1, r + 1):
                rhs = z * (Q(2, 3) * formula[k - 1] + Q(1, 3) * u * formula[r - k])
                check(formula[k] == rhs, ("BTB Bellman", r, k, z, u))

    for r in range(1, 26):
        direct_mean = btb_direct_mean(r)
        direct_parity = btb_direct_transform(r, Q(1), Q(-1))
        for k in range(1, r + 1):
            check(direct_mean[k] == btb_mean_formula(r, k), ("BTB mean", r, k))
            check(direct_parity[k] == btb_parity_formula(r, k), ("BTB parity", r, k))

    for r in range(1, 201):
        values = {k: btb_mean_formula(r, k) for k in range(1, r + 1)}
        lo, hi = min(values.values()), max(values.values())
        mins = [k for k, v in values.items() if v == lo]
        maxs = [k for k, v in values.items() if v == hi]
        check(mins == [1], ("BTB minimum", r, mins))
        target_maxs = ([1] if r == 1 else
                       ([(r + 2) // 2] if r % 2 == 0
                        else [(r + 1) // 2, (r + 3) // 2]))
        check(maxs == target_maxs, ("BTB maximum", r, maxs, target_maxs))
        check(hi == Q((r + 2) ** 2 // 4, 2), ("BTB max value", r))
        for k in range(1, r + 1):
            odd = Q(k, r + 2)
            mean = values[k]
            recovered_square = Q(2) * mean / (odd * (1 - odd))
            check(recovered_square == (r + 2) ** 2, ("BTB inverse scale", r, k))
            check(odd * (r + 2) == k, ("BTB inverse count", r, k))

    used = ASSERTIONS - start
    return literal_states, transform_cases, used


# ---------------------------------------------------------------------------
# Breadth controls: ten genuinely different literal mechanisms.


def cycle_sinks(word):
    n = len(word)
    return [i for i in range(n) if word[(i - 1) % n] == 1 and word[i] == 0]


def sink_pop_uniform_pilot(n):
    states = list(product((0, 1), repeat=n))
    transient = [s for s in states if cycle_sinks(s)]
    idx = {s: i for i, s in enumerate(transient)}
    a = [[Q(i == j) for j in range(len(transient))] for i in range(len(transient))]
    bm = [Q(1)] * len(transient)
    bp = [Q(0)] * len(transient)
    for s, i in idx.items():
        sinks = cycle_sinks(s)
        for v in sinks:
            for left, right in product((0, 1), repeat=2):
                t = list(s)
                t[(v - 1) % n], t[v] = left, right
                t = tuple(t)
                p = Q(1, 4 * len(sinks))
                if t in idx:
                    a[i][idx[t]] -= p
                elif all(t):
                    bp[i] += p
    means = gauss_solve(a, bm)
    probs = gauss_solve(a, bp)
    em = sum((means[idx[s]] if s in idx else Q(0)) for s in states) / len(states)
    ep = sum((probs[idx[s]] if s in idx else Q(int(all(s)))) for s in states) / len(states)
    return len(transient), em, ep


def split_profile(n):
    counts = {}
    for i, j in combinations(range(n), 2):
        a = j - i
        key = tuple(sorted((a, n - a)))
        counts[key] = counts.get(key, 0) + 1
    return counts


def voter_star_pilot(m):
    # Transient states are (A,k), k<m, and (B,k), k>0.
    states = [(1, k) for k in range(m)] + [(0, k) for k in range(1, m + 1)]
    idx = {s: i for i, s in enumerate(states)}
    a = [[Q(i == j) for j in range(len(states))] for i in range(len(states))]
    bm, bp = [Q(1)] * len(states), [Q(0)] * len(states)
    for s, i in idx.items():
        h, k = s
        targets = ((1, k + 1), (0, k)) if h else ((0, k - 1), (1, k))
        for t in targets:
            if t in idx:
                a[i][idx[t]] -= Q(1, 2)
            elif t == (1, m):
                bp[i] += Q(1, 2)
    mean = gauss_solve(a, bm)[idx[(1, 0)]]
    pa = gauss_solve(a, bp)[idx[(1, 0)]]
    return mean, pa


def prime_support(n):
    ans = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            ans.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ans.append(n)
    return tuple(ans)


def gcd_erosion_step(dist):
    out = {}
    for x, mass in dist.items():
        if x == 1:
            out[1] = out.get(1, Q(0)) + mass
            continue
        for u in range(x):
            y = gcd(x, u)
            out[y] = out.get(y, Q(0)) + mass / x
    return out


def gcd_erosion_mean(n):
    ps = prime_support(n)
    ans = Q(0)
    for size in range(1, len(ps) + 1):
        for subset in combinations(ps, size):
            d = prod(subset)
            ans += (1 if size % 2 else -1) * Q(d, d - 1)
    return ans


@lru_cache(None)
def box_contraction_mean(state):
    if all(x == 1 for x in state):
        return Q(0)
    total = prod(state)
    lower = Q(0)
    for nxt in product(*(range(1, x + 1) for x in state)):
        if nxt != state:
            lower += box_contraction_mean(nxt) / total
    return (1 + lower) / (1 - Q(1, total))


def gf2_rank(rows, ncols):
    rows = list(rows)
    rank = 0
    for col in range(ncols):
        pivot = next((i for i in range(rank, len(rows)) if (rows[i] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> col) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def rank_one_kernel(m, n, k):
    base = [(1 << i) if i < k else 0 for i in range(m)]
    counts = {}
    for u in range(1 << m):
        for v in range(1 << n):
            rows = [base[i] ^ (v if ((u >> i) & 1) else 0) for i in range(m)]
            j = gf2_rank(rows, n)
            counts[j] = counts.get(j, 0) + 1
    return {j: Q(c, 1 << (m + n)) for j, c in sorted(counts.items())}


def rank_count_q2(m, n, k):
    if k == 0:
        return 1
    num, den = 1, 1
    for i in range(k):
        num *= ((1 << m) - (1 << i)) * ((1 << n) - (1 << i))
        den *= (1 << k) - (1 << i)
    check(num % den == 0, ("rank count integer", m, n, k))
    return num // den


def edge_index(n, i, j):
    if i > j:
        i, j = j, i
    z = 0
    for a in range(n):
        for b in range(a + 1, n):
            if (a, b) == (i, j):
                return z
            z += 1
    raise ValueError("bad edge")


def path_mask(n):
    return sum(1 << edge_index(n, i, i + 1) for i in range(n - 1))


def triadic_history_count(n):
    complete = (1 << (n * (n - 1) // 2)) - 1

    def has(mask, i, j):
        return (mask >> edge_index(n, i, j)) & 1

    @lru_cache(None)
    def histories(mask):
        if mask == complete:
            return 1
        eligible = []
        for i, j in combinations(range(n), 2):
            e = edge_index(n, i, j)
            if (mask >> e) & 1:
                continue
            if any(has(mask, i, k) and has(mask, k, j)
                   for k in range(n) if k not in (i, j)):
                eligible.append(e)
        check(bool(eligible), ("triadic closure stuck", n, mask))
        return sum(histories(mask | (1 << e)) for e in eligible)

    return histories(path_mask(n)), histories.cache_info().currsize


def partitions_of(n, cap=None):
    if n == 0:
        yield ()
        return
    cap = n if cap is None else min(cap, n)
    for first in range(cap, 0, -1):
        for rest in partitions_of(n - first, first):
            yield (first,) + rest


def young_removals(shape):
    out = []
    for i, row in enumerate(shape):
        below = shape[i + 1] if i + 1 < len(shape) else 0
        if row > below:
            nxt = list(shape)
            nxt[i] -= 1
            if nxt[-1] == 0:
                nxt.pop()
            out.append(tuple(nxt))
    return out


@lru_cache(None)
def young_histories(shape):
    if not shape:
        return 1
    return sum(young_histories(s) for s in young_removals(shape))


def hook_tableaux(shape):
    n = sum(shape)
    hooks = 1
    for i, row in enumerate(shape):
        for j in range(row):
            below = sum(1 for r in shape[i + 1:] if r > j)
            hooks *= (row - j) + below
    check(factorial(n) % hooks == 0, ("hook integer", shape))
    return factorial(n) // hooks


def chemical_weights(n):
    w = [1]
    for b in range(n // 2):
        a = n - 2 * b
        w.append(w[-1] * comb(a, 2) // (b + 1))
    return w


def move_front(perm, label):
    return (label,) + tuple(x for x in perm if x != label)


def tsetlin_stationary(perm, weights):
    ans = Q(1)
    suffix = sum(weights[x] for x in perm)
    for x in perm:
        ans *= Q(weights[x], suffix)
        suffix -= weights[x]
    return ans


def run_breadth():
    start = ASSERTIONS
    records = {}

    spp = []
    for n in range(3, 7):
        transient, mean, endpoint = sink_pop_uniform_pilot(n)
        check(mean == comb(n, 2), ("sink-pop mean", n, mean))
        check(endpoint == Q(1, 2), ("sink-pop endpoint", n, endpoint))
        spp.append((n, transient, mean))
    records["SPP"] = spp

    pcf = []
    for n in range(3, 11):
        profile = split_profile(n)
        check(sum(profile.values()) == comb(n, 2), ("cycle split total", n))
        for (a, b), count in profile.items():
            expected = n if a != b else n // 2
            check(count == expected, ("cycle split multiplicity", n, a, b, count))
        pcf.append((n, n ** (n - 2)))
    records["PCF"] = pcf

    vos = []
    for m in range(1, 13):
        mean, pa = voter_star_pilot(m)
        check(mean == m, ("voter star clock", m, mean))
        check(pa == Q(1, m + 1), ("voter star endpoint", m, pa))
        vos.append((m, mean, pa))
    records["VOS"] = vos

    rge = []
    for n in (12, 18, 30, 60, 210):
        ps = prime_support(n)
        dist = {n: Q(1)}
        for t in range(1, 7):
            dist = gcd_erosion_step(dist)
            predicted = prod((1 - Q(1, p ** t) for p in ps), start=Q(1))
            check(dist.get(1, Q(0)) == predicted, ("gcd all-time", n, t))
        rge.append((n, ps, gcd_erosion_mean(n)))
    check(rge[2][2] == rge[3][2], "gcd exponents must be invisible")
    records["RGE"] = rge

    bcs = []
    for d in range(1, 9):
        state = (2,) * d
        mean = box_contraction_mean(state)
        formula = sum(((-1) ** (j + 1)) * Q(comb(d, j), 1 - Q(1, 2 ** j))
                      for j in range(1, d + 1))
        check(mean == formula, ("box geometric maximum", d, mean, formula))
        bcs.append((state, mean))
    for state in ((2, 3), (3, 3), (2, 3, 4)):
        bcs.append((state, box_contraction_mean(state)))
    records["BCS"] = bcs

    rro = []
    for m in range(1, 5):
        for n in range(1, 5):
            for k in range(min(m, n) + 1):
                literal = rank_one_kernel(m, n, k)
                up = Q(((1 << m) - (1 << k)) * ((1 << n) - (1 << k)), 1 << (m + n))
                down = Q(0) if k == 0 else Q(((1 << k) - 1) * (1 << (k - 1)), 1 << (m + n))
                formula = {k: 1 - up - down}
                if up:
                    formula[k + 1] = up
                if down:
                    formula[k - 1] = down
                formula = dict(sorted((j, p) for j, p in formula.items() if p))
                check(literal == formula, ("rank-one kernel", m, n, k, literal, formula))
                if k < min(m, n):
                    lhs = rank_count_q2(m, n, k) * up
                    next_down = Q(((1 << (k + 1)) - 1) * (1 << k), 1 << (m + n))
                    rhs = rank_count_q2(m, n, k + 1) * next_down
                    check(lhs == rhs, ("rank detailed balance", m, n, k))
            rro.append((m, n, tuple(rank_one_kernel(m, n, k) for k in range(min(m, n) + 1))))
    records["RRO"] = rro

    tce = []
    expected_histories = {2: 1, 3: 1, 4: 4, 5: 204, 6: 280848, 7: 18163801920}
    for n, expected in expected_histories.items():
        histories, states = triadic_history_count(n)
        check(histories == expected, ("triadic histories", n, histories, expected))
        tce.append((n, histories, states))
    records["TCE"] = tce

    dmf = []
    for n in range(0, 11):
        for shape in partitions_of(n):
            check(young_histories(shape) == hook_tableaux(shape), ("Young history", shape))
    for shape in ((2, 2), (3, 3), (4, 4, 4)):
        dmf.append((shape, hook_tableaux(shape)))
    records["DMF"] = dmf

    cme = []
    for n in range(2, 31):
        w = chemical_weights(n)
        for b in range(len(w) - 1):
            a = n - 2 * b
            check(w[b] * comb(a, 2) == w[b + 1] * (b + 1),
                  ("chemical detailed balance", n, b))
        cme.append((n, tuple(w), sum(w)))
    records["CME"] = cme

    hfw = []
    for n in range(2, 7):
        labels = tuple(range(n))
        weights = tuple(range(1, n + 1))
        perms = list(permutations(labels))
        pi = {p: tsetlin_stationary(p, weights) for p in perms}
        check(sum(pi.values(), Q(0)) == 1, ("Tsetlin normalization", n))
        pushed = {p: Q(0) for p in perms}
        total = sum(weights)
        for p in perms:
            for x in labels:
                pushed[move_front(p, x)] += pi[p] * Q(weights[x], total)
        for p in perms:
            check(pushed[p] == pi[p], ("Tsetlin stationarity", n, p))
        hfw.append((n, pi[tuple(range(n))]))
    equal_two_step = {
        (0, 1, 2): Q(2, 9), (1, 0, 2): Q(2, 9), (2, 0, 1): Q(2, 9),
        (2, 1, 0): Q(1, 9), (0, 2, 1): Q(1, 9), (1, 2, 0): Q(1, 9),
    }
    dist = {(0, 1, 2): Q(1)}
    for _ in range(2):
        nxt = {}
        for p, mass in dist.items():
            for x in range(3):
                y = move_front(p, x)
                nxt[y] = nxt.get(y, Q(0)) + mass / 3
        dist = nxt
    check(dist == equal_two_step, ("Tsetlin two-step", dist))
    records["HFW"] = hfw

    return records, ASSERTIONS - start


def main():
    htm_profiles, htm_extrema, htm_assertions = run_htm()
    btb_states, btb_transforms, btb_assertions = run_btb()
    records, breadth_assertions = run_breadth()

    print("SCOUT|systems=12|selected=2|killed=10|external=HOLD_EXTERNAL")
    print(f"HTM|profiles={htm_profiles}|extrema_families={htm_extrema}|assertions={htm_assertions}"
          f"|sample_area_2x3x4={qstr(htm_area_formula((2,3,4)))}")
    print(f"BTB|literal_bit_states={btb_states}|transform_cases={btb_transforms}"
          f"|assertions={btb_assertions}|sample_r7_means="
          + ",".join(qstr(btb_mean_formula(7, k)) for k in range(1, 8)))
    print("SPP|uniform_means=" + ",".join(f"n{n}:{qstr(mean)}" for n, _, mean in records["SPP"]))
    print("PCF|minimal_histories=" + ",".join(f"n{n}:{h}" for n, h in records["PCF"][:5]))
    print("VOS|A0=" + ",".join(f"m{m}:E{qstr(mean)}/p{qstr(pa)}" for m, mean, pa in records["VOS"][:6]))
    print("RGE|means=" + ",".join(f"n{n}:{qstr(mean)}" for n, _, mean in records["RGE"]))
    print("BCS|means=" + ",".join(f"{state}:{qstr(mean)}" for state, mean in records["BCS"][-3:]))
    r33 = next(kernels for m, n, kernels in records["RRO"] if (m, n) == (3, 3))
    print("RRO|q2_3x3=" + ";".join(
        f"k{k}:" + ",".join(f"{j}->{qstr(p)}" for j, p in ker.items())
        for k, ker in enumerate(r33)))
    print("TCE|path_histories=" + ",".join(f"n{n}:{h}" for n, h, _ in records["TCE"]))
    print("DMF|rectangle_histories=" + ",".join(f"{shape}:{h}" for shape, h in records["DMF"]))
    print("CME|weights_N4=" + ",".join(map(str, records["CME"][2][1]))
          + "|weights_N6=" + ",".join(map(str, records["CME"][4][1])))
    print("HFW|identity_stationary=" + ",".join(f"n{n}:{qstr(p)}" for n, p in records["HFW"]))
    print(f"BREADTH|assertions={breadth_assertions}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
