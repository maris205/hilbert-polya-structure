#!/usr/bin/env python3
"""Independent exact breadth checks for the replacement cross-class lane.

No randomness, floating point, network access, third-party package, or earlier
project code is used.  Enumeration is falsification pressure, not proof.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, gcd, lcm


ASSERTIONS = 0


def check(condition):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(f"assertion {ASSERTIONS} failed")


def orbit(step, state):
    seen = {}
    x = state
    while x not in seen:
        seen[x] = len(seen)
        x = step(x)
    return seen[x], len(seen) - seen[x]


def bits_weight(x):
    return x.bit_count()


def falling(a, k):
    ans = 1
    for j in range(k):
        ans *= a - j
    return ans


def stirling2(n, k):
    tab = [[0] * (k + 1) for _ in range(n + 1)]
    tab[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            tab[i][j] = tab[i - 1][j - 1] + j * tab[i - 1][j]
    return tab[n][k]


# A01: row-majority normalization.
def rmn_row(x, n):
    return x ^ ((1 << n) - 1) if 2 * bits_weight(x) > n else x


rmn_last = None
for n in range(1, 9):
    fibres = Counter(rmn_row(x, n) for x in range(1 << n))
    expected_image = sum(comb(n, j) for j in range(n // 2 + 1))
    check(len(fibres) == expected_image)
    for x in range(1 << n):
        y = rmn_row(x, n)
        check(rmn_row(y, n) == y)
    for y, f in fibres.items():
        w = bits_weight(y)
        check(f == (1 if n % 2 == 0 and 2 * w == n else 2))
    rmn_last = (n, len(fibres), Counter(fibres.values()))
print(f"A01 RMN PASS n={rmn_last[0]} image={rmn_last[1]} fibre_hist={dict(sorted(rmn_last[2].items()))}")


# A02: support biclique hull.
def bch(x, h, w):
    rows = [any((x >> (i * w + j)) & 1 for j in range(w)) for i in range(h)]
    cols = [any((x >> (i * w + j)) & 1 for i in range(h)) for j in range(w)]
    y = 0
    for i in range(h):
        for j in range(w):
            if rows[i] and cols[j]:
                y |= 1 << (i * w + j)
    return y


def no_zero_margin_count(r, s):
    return sum(
        (-1) ** (i + j) * comb(r, i) * comb(s, j) * 2 ** ((r - i) * (s - j))
        for i in range(r + 1)
        for j in range(s + 1)
    )


bch_last = None
for h in range(1, 4):
    for w in range(1, 4):
        fibres = Counter(bch(x, h, w) for x in range(1 << (h * w)))
        check(len(fibres) == 1 + (2**h - 1) * (2**w - 1))
        for x in range(1 << (h * w)):
            y = bch(x, h, w)
            check(bch(y, h, w) == y)
        for y, f in fibres.items():
            if y == 0:
                check(f == 1)
                continue
            rr = sum(any((y >> (i * w + j)) & 1 for j in range(w)) for i in range(h))
            ss = sum(any((y >> (i * w + j)) & 1 for i in range(h)) for j in range(w))
            check(f == no_zero_margin_count(rr, ss))
        bch_last = (h, w, len(fibres), Counter(fibres.values()))
print(f"A02 SBH PASS shape={bch_last[0]}x{bch_last[1]} image={bch_last[2]} fibre_hist={dict(sorted(bch_last[3].items()))}")


# A03: row-column degree equality matrix.
def rce(x, n):
    rows = [sum((x >> (i * n + j)) & 1 for j in range(n)) for i in range(n)]
    cols = [sum((x >> (i * n + j)) & 1 for i in range(n)) for j in range(n)]
    y = 0
    for i in range(n):
        for j in range(n):
            if rows[i] == cols[j]:
                y |= 1 << (i * n + j)
    return y


rce_expected = {
    1: (1, 1, 1, 1),
    2: (4, 1, 2, 1),
    3: (41, 10, 3, 2),
    4: (1100, 17, 4, 2),
}
for n in range(1, 5):
    image = set()
    fixed = 0
    max_tail = 0
    periods = set()
    for x in range(1 << (n * n)):
        y = rce(x, n)
        image.add(y)
        fixed += y == x
        mu, per = orbit(lambda z: rce(z, n), x)
        max_tail = max(max_tail, mu)
        periods.add(per)
        # Independent check of the mutual-histogram factor after one step.
        rd = [sum((x >> (i * n + j)) & 1 for j in range(n)) for i in range(n)]
        cd = [sum((x >> (i * n + j)) & 1 for i in range(n)) for j in range(n)]
        yr = [sum((y >> (i * n + j)) & 1 for j in range(n)) for i in range(n)]
        yc = [sum((y >> (i * n + j)) & 1 for i in range(n)) for j in range(n)]
        check(yr == [cd.count(v) for v in rd])
        check(yc == [rd.count(v) for v in cd])
    got = (len(image), fixed, max_tail, max(periods))
    check(got == rce_expected[n])
    check(periods <= {1, 2})
print("A03 RCE PASS signatures=" + ",".join(f"n{n}:{rce_expected[n]}" for n in sorted(rce_expected)))


# A04: corner-controlled simultaneous row/column crop.
SINK = (0, 0, ())


def ccc(state):
    h, w, a = state
    if h == 0 or w == 0:
        return SINK
    nh, nw = h - 1, w - 1
    if nh == 0 or nw == 0:
        return SINK
    if a[0] != 0:
        b = tuple(a[i * w + j] for i in range(1, h) for j in range(1, w))
    else:
        b = tuple(a[i * w + j] for i in range(h - 1) for j in range(w - 1))
    return nh, nw, b


ccc_last = None
for q in (2, 3):
    for h in range(1, 4):
        for w in range(1, 4):
            sources = [(h, w, a) for a in product(range(q), repeat=h * w)]
            fibres = Counter(ccc(s) for s in sources)
            for s in sources:
                x, d = s, 0
                while x != SINK:
                    x = ccc(x)
                    d += 1
                check(d == min(h, w))
            if h == 1 or w == 1:
                check(fibres == Counter({SINK: q ** (h * w)}))
            else:
                for target, f in fibres.items():
                    top = (q - 1) * q ** (h + w - 2)
                    bottom = q ** (h + w - 1) if target[2][0] == 0 else 0
                    check(f == top + bottom)
            ccc_last = (q, h, w, Counter(fibres.values()))
print(f"A04 CCC PASS q={ccc_last[0]} shape={ccc_last[1]}x{ccc_last[2]} fibre_hist={dict(sorted(ccc_last[3].items()))}")


# L01: median clamp on a Boolean lattice.
def lmc(s, a, b, mask):
    return (s & (a | b)) | (a & b)


lmc_last = None
for n in range(1, 6):
    mask = (1 << n) - 1
    for a in range(1 << n):
        for b in range(1 << n):
            fibres = Counter(lmc(s, a, b, mask) for s in range(1 << n))
            d = bits_weight(a ^ b)
            check(len(fibres) == 2**d)
            check(set(fibres.values()) == {2 ** (n - d)})
            for s in range(1 << n):
                y = lmc(s, a, b, mask)
                check(lmc(y, a, b, mask) == y)
    lmc_last = (n, 3**n)
print(f"L01 LMC PASS n={lmc_last[0]} anchor_intervals={lmc_last[1]}")


# L02: lattice comparator (meet, join).
def lcp(pair):
    x, y = pair
    return x & y, x | y


lcp_last = None
for n in range(1, 9):
    fibres = Counter(lcp((x, y)) for x in range(1 << n) for y in range(1 << n))
    check(len(fibres) == 3**n)
    for target, f in fibres.items():
        lo, hi = target
        check((lo & ~hi) == 0)
        check(f == 2 ** bits_weight(lo ^ hi))
        check(lcp(target) == target)
    lcp_last = (n, len(fibres), max(fibres.values()))
print(f"L02 LCP PASS n={lcp_last[0]} image={lcp_last[1]} max_fibre={lcp_last[2]}")


def fence_order(n):
    le = [[i == j for j in range(n)] for i in range(n)]
    for i in range(n - 1):
        if i % 2 == 0:
            le[i][i + 1] = True
        else:
            le[i + 1][i] = True
    return le


def is_ideal(s, le):
    n = len(le)
    return all(
        not ((s >> x) & 1) or all(not le[y][x] or ((s >> y) & 1) for y in range(n))
        for x in range(n)
    )


def ideals(le):
    return [s for s in range(1 << len(le)) if is_ideal(s, le)]


# L03: odd-principal-ideal hull on fence ideals.
def oih(s, le):
    n = len(le)
    seeds = [
        x
        for x in range(n)
        if sum(bool(le[y][x] and ((s >> y) & 1)) for y in range(n)) % 2
    ]
    out = 0
    for x in seeds:
        for y in range(n):
            if le[y][x]:
                out |= 1 << y
    return out


oih_sig = []
for n in range(1, 15):
    le = fence_order(n)
    states = ideals(le)
    max_tail, max_period, fixed = 0, 0, 0
    cycles = {}
    for s in states:
        y = oih(s, le)
        check(is_ideal(y, le))
        # The minimal-element bits evolve by radius-one binary dilation.
        evens = [((s >> (2 * i)) & 1) for i in range((n + 1) // 2)]
        got = [((y >> (2 * i)) & 1) for i in range((n + 1) // 2)]
        pred = [int(evens[i] or (i and evens[i - 1]) or (i + 1 < len(evens) and evens[i + 1])) for i in range(len(evens))]
        check(got == pred)
        mu, per = orbit(lambda z: oih(z, le), s)
        max_tail, max_period = max(max_tail, mu), max(max_period, per)
        fixed += y == s
        path, loc, z = [], {}, s
        while z not in loc:
            loc[z] = len(path)
            path.append(z)
            z = oih(z, le)
        cyc = path[loc[z]:]
        rotations = [tuple(cyc[i:] + cyc[:i]) for i in range(len(cyc))]
        cycles[min(rotations)] = len(cyc)
    check(max_tail == (n - 1) // 2)
    if n % 2:
        check(max_period == 1)
        check(fixed == 2 ** ((n - 1) // 2) + 1)
        check(Counter(cycles.values()) == Counter({1: fixed}))
    else:
        check(max_period == 2)
        check(fixed == 1)
        check(Counter(cycles.values()) == Counter({1: 1, 2: 2 ** (n // 2 - 1)}))
    oih_sig.append((n, len(states), max_tail, max_period, fixed))
print("L03 OIH PASS last=" + str(oih_sig[-1]) + " exact_binary_dilation_factor=yes")


# L04: meet/symmetric-difference pair map in a Boolean lattice.
def msd(pair):
    x, y = pair
    return x & y, x ^ y


msd_last = None
for n in range(1, 9):
    fibres = Counter(msd((x, y)) for x in range(1 << n) for y in range(1 << n))
    check(len(fibres) == 3**n)
    fixed = 0
    maxtail = 0
    for x in range(1 << n):
        for y in range(1 << n):
            mu, per = orbit(msd, (x, y))
            check(per == 1)
            maxtail = max(maxtail, mu)
            fixed += msd((x, y)) == (x, y)
    check(fixed == 2**n)
    check(maxtail == 2)
    for (u, v), f in fibres.items():
        check((u & v) == 0)
        check(f == 2 ** bits_weight(v))
    msd_last = (n, len(fibres), fixed, maxtail)
print(f"L04 MSD PASS n={msd_last[0]} image={msd_last[1]} fixed={msd_last[2]} max_tail={msd_last[3]}")


# F01: kernel-representative retraction on endofunctions.
def krr(f):
    mins = {}
    for i, y in enumerate(f):
        mins[y] = min(i, mins.get(y, i))
    return tuple(mins[y] for y in f)


krr_last = None
for n in range(1, 6):
    fibres = Counter(krr(f) for f in product(range(n), repeat=n))
    for f in product(range(n), repeat=n):
        y = krr(f)
        check(krr(y) == y)
    for target, f in fibres.items():
        k = len(set(target))
        check(f == falling(n, k))
    krr_last = (n, len(fibres), Counter(fibres.values()))
print(f"F01 KRR PASS n={krr_last[0]} image={krr_last[1]} fibre_hist={dict(sorted(krr_last[2].items()))}")


# F02: row-equality relation.
def rem(x, n):
    rows = [(x >> (i * n)) & ((1 << n) - 1) for i in range(n)]
    y = 0
    for i in range(n):
        for j in range(n):
            if rows[i] == rows[j]:
                y |= 1 << (i * n + j)
    return y


rem_last = None
for n in range(1, 5):
    fibres = Counter(rem(x, n) for x in range(1 << (n * n)))
    for target, f in fibres.items():
        rows = [(target >> (i * n)) & ((1 << n) - 1) for i in range(n)]
        k = len(set(rows))
        check(f == falling(2**n, k))
        check(rem(target, n) == target)
    rem_last = (n, len(fibres), Counter(fibres.values()))
print(f"F02 REM PASS n={rem_last[0]} image={rem_last[1]} fibre_hist={dict(sorted(rem_last[2].items()))}")


# F03: squaring in the full transformation monoid.
def fsq(f):
    return tuple(f[f[i]] for i in range(len(f)))


def transformation_profile(f):
    n = len(f)
    height = 0
    cycles = set()
    for start in range(n):
        loc, path, x = {}, [], start
        while x not in loc:
            loc[x] = len(path)
            path.append(x)
            x = f[x]
        height = max(height, loc[x])
        cyc = path[loc[x]:]
        cycles.add(frozenset(cyc))
    L = 1
    for cyc in cycles:
        L = lcm(L, len(cyc))
    return height, L


def ceil_log2(x):
    t, p = 0, 1
    while p < x:
        p *= 2
        t += 1
    return t


def vtwo(x):
    a = 0
    while x % 2 == 0:
        a += 1
        x //= 2
    return a


def order_two(modulus):
    if modulus == 1:
        return 1
    x, t = 2 % modulus, 1
    while x != 1:
        x = (2 * x) % modulus
        t += 1
    return t


def permutation_cycles(p):
    seen = set()
    lengths = []
    for i in range(len(p)):
        if i in seen:
            continue
        x, ell = i, 0
        while x not in seen:
            seen.add(x)
            ell += 1
            x = p[x]
        lengths.append(ell)
    return lengths


def allowed_permutation_count(c, divisor):
    return sum(all(divisor % ell == 0 for ell in permutation_cycles(p)) for p in permutations(range(c)))


fsq_last = None
for n in range(1, 6):
    states = list(product(range(n), repeat=n))
    for f in states:
        h, L = transformation_profile(f)
        mu, per = orbit(fsq, f)
        a = vtwo(L)
        check(mu == max(ceil_log2(h), a))
        check(per == order_two(L // (2**a)))
    fixed_counts = []
    for t in range(1, 4):
        divisor = 2**t - 1
        observed = 0
        for f in states:
            y = f
            for _ in range(t):
                y = fsq(y)
            observed += y == f
        formula = 0
        for c in range(1, n + 1):
            formula += comb(n, c) * allowed_permutation_count(c, divisor) * c ** (n - c)
        check(observed == formula)
        fixed_counts.append(observed)
    fsq_last = (n, len(states), tuple(fixed_counts))
print(f"F03 FSQ PASS n={fsq_last[0]} states={fsq_last[1]} fixed_t123={fsq_last[2]}")


# F04: symmetric core of a binary relation.
def rsc(x, n):
    y = 0
    for i in range(n):
        for j in range(n):
            if ((x >> (i * n + j)) & 1) and ((x >> (j * n + i)) & 1):
                y |= 1 << (i * n + j)
    return y


rsc_last = None
for n in range(1, 5):
    fibres = Counter(rsc(x, n) for x in range(1 << (n * n)))
    check(len(fibres) == 2 ** (n * (n + 1) // 2))
    for target, f in fibres.items():
        absent = 0
        for i in range(n):
            for j in range(i + 1, n):
                check(((target >> (i * n + j)) & 1) == ((target >> (j * n + i)) & 1))
                absent += not ((target >> (i * n + j)) & 1)
        check(f == 3**absent)
        check(rsc(target, n) == target)
    rsc_last = (n, len(fibres), max(fibres.values()))
print(f"F04 RSC PASS n={rsc_last[0]} image={rsc_last[1]} max_fibre={rsc_last[2]}")


# C01: adjacent-coprime run consolidation on compositions.
def compositions(n):
    if n == 0:
        yield ()
        return
    for cuts in range(1 << (n - 1)):
        out, part = [], 1
        for i in range(n - 1):
            if (cuts >> i) & 1:
                out.append(part)
                part = 1
            else:
                part += 1
        out.append(part)
        yield tuple(out)


def crg(a):
    if not a:
        return a
    out, total = [], a[0]
    for x, y in zip(a, a[1:]):
        if gcd(x, y) > 1:
            total += y
        else:
            out.append(total)
            total = y
    out.append(total)
    return tuple(out)


crg_depths = []
crg_fixed = []
for n in range(1, 17):
    md, nf = 0, 0
    for a in compositions(n):
        b = crg(a)
        check(sum(a) == sum(b))
        check(len(b) <= len(a))
        check((b == a) == all(gcd(x, y) == 1 for x, y in zip(a, a[1:])))
        mu, per = orbit(crg, a)
        check(per == 1)
        check(mu <= len(a) - 1)
        md = max(md, mu)
        nf += b == a
    crg_depths.append(md)
    crg_fixed.append(nf)
check(crg((2, 3, 4)) == (2, 3, 4))
print(f"C01 CRG PASS max_depths={tuple(crg_depths)} fixed_n16={crg_fixed[-1]}")


# C02: directed-relation row-degree quotient.
def dqc(state):
    n, x = state
    if n <= 1:
        return state
    deg = [sum((x >> (i * n + j)) & 1 for j in range(n)) for i in range(n)]
    vals = sorted(set(deg))
    cls = [[i for i in range(n) if deg[i] == v] for v in vals]
    r, y = len(cls), 0
    for a, ca in enumerate(cls):
        for b, cb in enumerate(cls):
            if any((x >> (i * n + j)) & 1 for i in ca for j in cb):
                y |= 1 << (a * r + b)
    return r, y


dqc_sig = []
for n in range(1, 5):
    max_tail, max_period, fixed, image = 0, 0, 0, set()
    for x in range(1 << (n * n)):
        s = (n, x)
        y = dqc(s)
        image.add(y)
        mu, per = orbit(dqc, s)
        max_tail, max_period = max(max_tail, mu), max(max_period, per)
        fixed += y == s
        check(per == 1)
        check(y[0] <= n)
        check(mu <= n)
    dqc_sig.append((n, len(image), fixed, max_tail, max_period))
print(f"C02 DQC PASS signatures={tuple(dqc_sig)}")


# C03: duplicate-column contraction.
def twc(columns):
    return tuple(sorted(set(columns)))


twc_last = None
for h in range(1, 4):
    alphabet = 1 << h
    for w in range(1, 6):
        fibres = Counter(twc(cols) for cols in product(range(alphabet), repeat=w))
        for target, f in fibres.items():
            r = len(target)
            check(f == falling(r, r) * stirling2(w, r))
            check(twc(target) == target)
        check(len(fibres) == sum(comb(alphabet, r) for r in range(1, min(w, alphabet) + 1)))
        twc_last = (h, w, len(fibres), max(fibres.values()))
print(f"C03 TWC PASS h={twc_last[0]} w={twc_last[1]} image={twc_last[2]} max_fibre={twc_last[3]}")


# C04: sibling-equicardinal quotient of rooted unordered trees.
def tree_size(t):
    return 1 + sum(tree_size(c) for c in t)


def tree_step(t):
    stepped = [tree_step(c) for c in t]
    groups = defaultdict(list)
    for original, new in zip(t, stepped):
        groups[tree_size(original)].append(new)
    merged = []
    for size_key in sorted(groups):
        children = []
        for root in groups[size_key]:
            children.extend(root)
        merged.append(tuple(sorted(children)))
    return tuple(sorted(merged))


trees_by_size = {1: {()}}
for n in range(2, 11):
    universe = sorted(
        (t for size in range(1, n) for t in trees_by_size[size]),
        key=lambda t: (tree_size(t), t),
    )
    made = set()

    def choose(start, remaining, chosen):
        if remaining == 0:
            made.add(tuple(sorted(chosen)))
            return
        for idx in range(start, len(universe)):
            t = universe[idx]
            s = tree_size(t)
            if s > remaining:
                break
            choose(idx, remaining - s, chosen + [t])

    choose(0, n - 1, [])
    trees_by_size[n] = made

seq_sig = []
for n in range(1, 11):
    md, fixed = 0, 0
    for t in trees_by_size[n]:
        y = tree_step(t)
        check(tree_size(y) <= tree_size(t))
        mu, per = orbit(tree_step, t)
        check(per == 1)
        check(mu <= n - 1)
        md = max(md, mu)
        fixed += y == t
    seq_sig.append((n, len(trees_by_size[n]), md, fixed))
print(f"C04 SEQ PASS signatures={tuple(seq_sig)}")


# M01: complement-pivot subset kernel.
def cps_next(s, i, n):
    return (((1 << n) - 1) ^ s) | (1 << i)


cps_last = None
for n in range(2, 8):
    for s in range(1, 1 << n):
        members = [i for i in range(n) if (s >> i) & 1]
        row = Counter(cps_next(s, i, n) for i in members)
        check(sum(Fraction(v, len(members)) for v in row.values()) == 1)
        for u, mult in row.items():
            check(bits_weight(u) == n - bits_weight(s) + 1)
            check(mult >= 1)
        # Exact square: lazy Johnson/Bernoulli--Laplace kernel.
        two = defaultdict(Fraction)
        for i in members:
            u = cps_next(s, i, n)
            um = [j for j in range(n) if (u >> j) & 1]
            for j in um:
                two[cps_next(u, j, n)] += Fraction(1, len(members) * len(um))
        k = len(members)
        check(two[s] == Fraction(1, n - k + 1))
        for i in members:
            for j in range(n):
                if not ((s >> j) & 1):
                    target = (s ^ (1 << i)) | (1 << j)
                    check(two[target] == Fraction(1, k * (n - k + 1)))
        check(sum(two.values()) == 1)
    cps_last = (n, (1 << n) - 1)
print(f"M01 CPS PASS n={cps_last[0]} nonempty_states={cps_last[1]} square=lazy_Johnson")


# M02: maximum-fibre load migration on endofunctions.
def flm_successors(f):
    n = len(f)
    counts = Counter(f)
    if len(counts) == n:
        return Counter({f: 1})
    maxload = max(counts.values())
    heavy = sorted(y for y, c in counts.items() if c == maxload)
    empty = min(set(range(n)) - set(f))
    out = Counter()
    for y in heavy:
        i = min(j for j, z in enumerate(f) if z == y)
        g = list(f)
        g[i] = empty
        out[tuple(g)] += 1
    return out


flm_supports = []
flm_example = None
for n in range(1, 6):
    @lru_cache(None)
    def flm_law(f):
        if len(set(f)) == n:
            return {(0, f): Fraction(1)}
        succ = flm_successors(f)
        out = defaultdict(Fraction)
        for g, mult in succ.items():
            check(len(set(g)) == len(set(f)) + 1)
            for (t, z), p in flm_law(g).items():
                out[(t + 1, z)] += Fraction(mult, sum(succ.values())) * p
        return dict(out)

    maxsupport = 0
    for f in product(range(n), repeat=n):
        law = flm_law(f)
        check(sum(law.values()) == 1)
        check({t for t, _ in law} == {n - len(set(f))})
        for (t, z), p in law.items():
            check(p > 0)
            check(len(set(z)) == n)
        if len(law) > maxsupport:
            maxsupport = len(law)
            flm_example = (f, law)
    flm_supports.append(maxsupport)
print(f"M02 FLM PASS max_terminal_supports={tuple(flm_supports)} last_example_support={len(flm_example[1])}")


# M03: degree-discrepancy row-complement kernel on square binary arrays.
def drc_successors(x, n):
    rows = [sum((x >> (i * n + j)) & 1 for j in range(n)) for i in range(n)]
    cols = [sum((x >> (i * n + j)) & 1 for i in range(n)) for j in range(n)]
    active = [i for i in range(n) if rows[i] != cols[i]]
    if not active:
        return (x,)
    rowmask = (1 << n) - 1
    return tuple(x ^ (rowmask << (i * n)) for i in active)


def strongly_connected_components(graph):
    index = 0
    stack = []
    onstack = set()
    indices = {}
    low = {}
    answer = []

    def visit(v):
        nonlocal index
        indices[v] = low[v] = index
        index += 1
        stack.append(v)
        onstack.add(v)
        for w in graph[v]:
            if w not in indices:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in onstack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack.remove(w)
                comp.append(w)
                if w == v:
                    break
            answer.append(tuple(sorted(comp)))

    for v in graph:
        if v not in indices:
            visit(v)
    return answer


drc_sig = []
for n in range(1, 4):
    graph = {x: drc_successors(x, n) for x in range(1 << (n * n))}
    for x, succ in graph.items():
        check(len(succ) >= 1)
        check(sum(Fraction(1, len(succ)) for _ in succ) == 1)
    comps = strongly_connected_components(graph)
    owner = {x: idx for idx, c in enumerate(comps) for x in c}
    closed = [
        c for idx, c in enumerate(comps)
        if all(owner[y] == idx for x in c for y in graph[x])
    ]
    absorbing = sum(graph[x] == (x,) for x in graph)
    drc_sig.append((n, len(comps), len(closed), max(map(len, closed)), absorbing))
print(f"M03 DRC PASS scc_signatures={tuple(drc_sig)}")


# M04: random odd-principal generator growth on fence ideals.
def opg_active(s, le):
    n = len(le)
    return [
        x
        for x in range(n)
        if not ((s >> x) & 1)
        and sum(bool(le[y][x] and ((s >> y) & 1)) for y in range(n)) % 2
    ]


def add_principal(s, x, le):
    return s | sum((1 << y) for y in range(len(le)) if le[y][x])


opg_max_support = []
for n in range(1, 10):
    le = fence_order(n)

    @lru_cache(None)
    def law(s):
        active = opg_active(s, le)
        if not active:
            return {s: Fraction(1)}
        out = defaultdict(Fraction)
        for x in active:
            y = add_principal(s, x, le)
            check(is_ideal(y, le))
            check((y | s) == y and y != s)
            for z, p in law(y).items():
                out[z] += p / len(active)
        return dict(out)

    support = 0
    for s in ideals(le):
        dist = law(s)
        check(sum(dist.values()) == 1)
        support = max(support, len(dist))
        for z, p in dist.items():
            check(p > 0)
            check(not opg_active(z, le))
    opg_max_support.append(support)
le5 = fence_order(5)

@lru_cache(None)
def law5(s):
    aa = opg_active(s, le5)
    if not aa:
        return {s: Fraction(1)}
    out = defaultdict(Fraction)
    for x in aa:
        for z, p in law5(add_principal(s, x, le5)).items():
            out[z] += p / len(aa)
    return dict(out)

check(law5(17) == {23: Fraction(1, 2), 29: Fraction(1, 2)})
print(f"M04 OPG PASS max_terminal_supports={tuple(opg_max_support)} n5_state17=23/29_half")


print(f"ASSERTIONS {ASSERTIONS}")
print("STATUS PASS")
