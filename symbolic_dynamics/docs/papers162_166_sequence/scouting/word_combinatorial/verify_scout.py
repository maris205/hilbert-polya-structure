#!/usr/bin/env python3
"""Independent exact breadth probes for the P162--P166 word/combinatorial lane.

Every check is deterministic and uses only the Python standard library.  The
script is deliberately self-contained: it does not import any paper verifier.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def eq(self, got, want, label: str = "") -> None:
        self.assertions += 1
        if got != want:
            raise AssertionError(f"{label}: got {got!r}, want {want!r}")

    def ok(self, value: bool, label: str = "") -> None:
        self.assertions += 1
        if not value:
            raise AssertionError(label or "assertion failed")


A = Audit()


def poly_mul(p: Counter[int], q: Counter[int]) -> Counter[int]:
    out: Counter[int] = Counter()
    for i, x in p.items():
        for j, y in q.items():
            out[i + j] += x * y
    return out


def functional_signature(states, fn):
    states = tuple(states)
    image = {fn(x) for x in states}
    fibres = Counter(fn(x) for x in states)
    cycles = set()
    max_tail = 0
    for start in states:
        order = {}
        path = []
        x = start
        while x not in order:
            order[x] = len(path)
            path.append(x)
            x = fn(x)
        mu = order[x]
        cycles.add(frozenset(path[mu:]))
        max_tail = max(max_tail, mu)
    cycle_lengths = Counter(map(len, cycles))
    return len(image), tuple(sorted(Counter(fibres.values()).items())), tuple(sorted(cycle_lengths.items())), max_tail


# 1--2. Lehmer-coordinate systems.
def lehmer(p):
    return tuple(sum(p[j] < p[i] for j in range(i + 1, len(p))) for i in range(len(p)))


def lehmer_decode(code):
    pool = list(range(len(code)))
    out = []
    for digit in code:
        out.append(pool.pop(digit))
    return tuple(out)


def lcd_step(p):
    return lehmer_decode(tuple(max(x - 1, 0) for x in lehmer(p)))


def lhf_step(p):
    return lehmer_decode(tuple(x // 2 for x in lehmer(p)))


def lcd_formula_poly(target_code, t):
    out = Counter({0: 1})
    n = len(target_code)
    for i, b in enumerate(target_code):
        cap = n - i - 1
        if b:
            if b + t > cap:
                return Counter()
            factor = Counter({b + t: 1})
        else:
            factor = Counter({x: 1 for x in range(min(t, cap) + 1)})
        out = poly_mul(out, factor)
    return out


def lhf_formula_poly(target_code, t):
    out = Counter({0: 1})
    scale = 1 << t
    n = len(target_code)
    for i, b in enumerate(target_code):
        cap = n - i - 1
        lo = scale * b
        hi = min(scale * (b + 1) - 1, cap)
        if lo > hi:
            return Counter()
        out = poly_mul(out, Counter({x: 1 for x in range(lo, hi + 1)}))
    return out


def probe_lehmer():
    n = 8
    states = tuple(permutations(range(n)))
    lcd_images = []
    lcd_spectra = []
    current = {p: p for p in states}
    for t in range(n):
        fibres = defaultdict(Counter)
        for p in states:
            y = current[p]
            direct = lehmer_decode(tuple(max(x - t, 0) for x in lehmer(p)))
            A.eq(y, direct, "LCD iterate")
            fibres[y][sum(lehmer(p))] += 1
            if t == 0:
                A.eq(max(lehmer(p), default=0), next((k for k in range(n) if lehmer_decode(tuple(max(x-k, 0) for x in lehmer(p))) == tuple(range(n))), n - 1), "LCD clock")
        for y, actual in fibres.items():
            A.eq(actual, lcd_formula_poly(lehmer(y), t), "LCD target fibre polynomial")
        lcd_images.append(len(fibres))
        ordinary = [sum(poly.values()) for poly in fibres.values()]
        lcd_spectra.append((min(ordinary), max(ordinary)))
        current = {p: lcd_step(y) for p, y in current.items()}
    A.eq(lcd_images, [factorial(k) for k in range(n, 0, -1)], "LCD image factorials")
    A.eq(lcd_spectra[2], (factorial(3), factorial(2) * 3 ** 6), "LCD t=2 extrema")

    lhf_images = []
    current = {p: p for p in states}
    for t in range(4):
        fibres = defaultdict(Counter)
        for p in states:
            y = current[p]
            direct = lehmer_decode(tuple(x // (1 << t) for x in lehmer(p)))
            A.eq(y, direct, "LHF iterate")
            fibres[y][sum(lehmer(p))] += 1
        for y, actual in fibres.items():
            A.eq(actual, lhf_formula_poly(lehmer(y), t), "LHF target fibre polynomial")
        lhf_images.append(len(fibres))
        current = {p: lhf_step(y) for p, y in current.items()}
    A.eq(lhf_images, [40320, 576, 16, 1], "LHF image sizes")
    return f"LCD n=8 images={lcd_images}; t2 fibre-range={lcd_spectra[2]}", f"LHF n=8 images={lhf_images}"


# 3. Dyck area-sequence erosion.
def area_sequences(n):
    if n == 0:
        return ((),)
    out = []

    def rec(a):
        if len(a) == n:
            out.append(tuple(a))
            return
        for x in range(a[-1] + 2):
            a.append(x)
            rec(a)
            a.pop()

    rec([0])
    return tuple(out)


def erosion(x):
    return tuple(max(a - 1, 0) for a in x)


def dae_fibre_poly(target, t):
    n = len(target)
    allowed = []
    for i, b in enumerate(target):
        cap = i
        vals = (b + t,) if b else tuple(range(min(t, cap) + 1))
        allowed.append(tuple(x for x in vals if x <= cap))
    dp = {(0, 0): 1} if 0 in allowed[0] else {}
    for i in range(1, n):
        ndp = defaultdict(int)
        for (prev, weight), count in dp.items():
            for x in allowed[i]:
                if x <= prev + 1:
                    ndp[(x, weight + x)] += count
        dp = ndp
    out = Counter()
    for (_, weight), count in dp.items():
        out[weight] += count
    return out


def probe_dae():
    n = 9
    states = area_sequences(n)
    A.eq(len(states), 4862, "Catalan(9)")
    current = {x: x for x in states}
    image_sizes = []
    for t in range(n):
        fibres = defaultdict(Counter)
        for x in states:
            y = current[x]
            A.eq(y, tuple(max(a - t, 0) for a in x), "DAE iterate")
            fibres[y][sum(x)] += 1
            if t == 0:
                A.eq(max(x, default=0), next((k for k in range(n) if tuple(max(a-k, 0) for a in x) == (0,) * n), n - 1), "DAE clock")
        for y, actual in fibres.items():
            A.eq(actual, dae_fibre_poly(y, t), "DAE area fibre")
            A.eq(y[: min(t + 1, n)], (0,) * min(t + 1, n), "DAE image prefix")
        m = n - t
        expected = comb(2 * m, m) // (m + 1)
        A.eq(len(fibres), expected, "DAE image formula")
        image_sizes.append(len(fibres))
        current = {x: erosion(y) for x, y in current.items()}
    A.eq(image_sizes, [4862, 1430, 429, 132, 42, 14, 5, 2, 1], "DAE images")
    return f"DAE n=9 images={image_sizes}; sharp-height={n-1}"


# 4. Motzkin height erosion (deliberate proof-engine collision control).
def motzkin_profiles(n):
    out = []

    def rec(a):
        if len(a) == n:
            if abs(a[-1]) <= 1:
                out.append(tuple(a + [0]))
            return
        for x in range(max(0, a[-1] - 1), a[-1] + 2):
            a.append(x)
            rec(a)
            a.pop()

    rec([0])
    return tuple(out)


def mhe_fibre_poly(target, t):
    allowed = []
    for b in target:
        allowed.append((b + t,) if b else tuple(range(t + 1)))
    dp = {(0, 0): 1}
    for i in range(1, len(target)):
        ndp = defaultdict(int)
        for (prev, weight), count in dp.items():
            for x in allowed[i]:
                if abs(x - prev) <= 1:
                    ndp[(x, weight + x)] += count
        dp = ndp
    out = Counter()
    for (last, weight), count in dp.items():
        if last == 0:
            out[weight] += count
    return out


def probe_mhe():
    n = 10
    states = motzkin_profiles(n)
    A.eq(len(states), 2188, "Motzkin(10)")
    current = {x: x for x in states}
    images = []
    for t in range(6):
        fibres = defaultdict(Counter)
        for x in states:
            y = current[x]
            A.eq(y, tuple(max(a - t, 0) for a in x), "MHE iterate")
            fibres[y][sum(x)] += 1
        for y, actual in fibres.items():
            A.eq(actual, mhe_fibre_poly(y, t), "MHE fibre DP")
        images.append(len(fibres))
        current = {x: erosion(y) for x, y in current.items()}
    return f"MHE length=10 images(t=0..5)={images}"


# 5. Deterministic stack sorting.
def stack_sort(p):
    if not p:
        return ()
    m = max(p)
    i = p.index(m)
    return stack_sort(p[:i]) + stack_sort(p[i + 1 :]) + (m,)


def probe_stack_sort():
    n = 8
    states = tuple(permutations(range(n)))
    tails = Counter()
    fibres = Counter(stack_sort(p) for p in states)
    for p in states:
        x = p
        k = 0
        while x != tuple(range(n)):
            x = stack_sort(x)
            k += 1
            A.ok(k <= n - 1, "stack-sort bound")
        tails[k] += 1
    return f"SST n=8 image={len(fibres)}, fibre-range=({min(fibres.values())},{max(fibres.values())}), tail-hist={sorted(tails.items())}"


# 6--18. Named/bijective/idempotent collision controls.
def ducci(x):
    return tuple(abs(x[(i + 1) % len(x)] - x[i]) for i in range(len(x)))


def parikh_mod(x, q):
    c = Counter(x)
    return tuple(c[i] % q for i in range(q))


def vervaat(x):
    s = 0
    prefix = [0]
    for bit in x:
        s += 1 if bit else -1
        prefix.append(s)
    cut = min(range(len(x)), key=lambda i: prefix[i])
    return x[cut:] + x[:cut]


def ideals_grid(r, c):
    cells = tuple(product(range(r), range(c)))
    out = []
    for mask in range(1 << len(cells)):
        I = frozenset(cells[i] for i in range(len(cells)) if mask >> i & 1)
        if all((u, v) in I for i, j in I for u in range(i + 1) for v in range(j + 1)):
            out.append(I)
    return tuple(out)


def rowmotion(I, r=2, c=3):
    comp = {(i, j) for i in range(r) for j in range(c)} - set(I)
    mins = {x for x in comp if not any(y != x and y[0] <= x[0] and y[1] <= x[1] for y in comp)}
    return frozenset((u, v) for i, j in mins for u in range(i + 1) for v in range(j + 1))


def cyclic_predecessor(p):
    out = [None] * len(p)
    for i, x in enumerate(p):
        out[x] = p[i - 1]
    return tuple(out)


def is_single_cycle(p):
    seen = set()
    x = 0
    for _ in range(len(p)):
        seen.add(x)
        x = p[x]
    return x == 0 and len(seen) == len(p)


def foata(p):
    n = len(p)
    seen = set()
    cycles = []
    for start in range(n):
        if start in seen:
            continue
        cyc = []
        x = start
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = p[x]
        m = max(cyc)
        k = cyc.index(m)
        cyc = cyc[k:] + cyc[:k]
        cycles.append(tuple(cyc))
    cycles.sort(key=lambda z: z[0])
    return tuple(x for cyc in cycles for x in cyc)


def inverse_perm(p):
    out = [0] * len(p)
    for i, x in enumerate(p):
        out[x] = i
    return tuple(out)


def toggle_sweep(mask, n):
    for i in range(n):
        if mask >> i & 1:
            mask ^= 1 << i
        elif (i == 0 or not (mask >> (i - 1) & 1)) and (i + 1 == n or not (mask >> (i + 1) & 1)):
            mask ^= 1 << i
    return mask


def parking_normalize(w):
    n = len(w)
    good = []
    for k in range(n + 1):
        v = tuple((x + k) % (n + 1) for x in w)
        if all(x <= i for i, x in enumerate(sorted(v))):
            good.append(v)
    A.eq(len(good), 1, "Pollak unique representative")
    return good[0]


def gray(x):
    return x ^ (x >> 1)


def invgray(g):
    x = 0
    while g:
        x ^= g
        g >>= 1
    return x


def standard_tableaux(r, c):
    cells = tuple(product(range(r), range(c)))
    out = []
    for order in permutations(cells):
        placed = set()
        tab = [[None] * c for _ in range(r)]
        good = True
        for label, (i, j) in enumerate(order, 1):
            if (i and (i - 1, j) not in placed) or (j and (i, j - 1) not in placed):
                good = False
                break
            placed.add((i, j))
            tab[i][j] = label
        if good:
            out.append(tuple(tuple(row) for row in tab))
    return tuple(out)


def tableau_promotion(tab):
    a = [list(row) for row in tab]
    r, c = len(a), len(a[0])
    i = j = 0
    a[0][0] = None
    while True:
        choices = []
        if i + 1 < r:
            choices.append((a[i + 1][j], i + 1, j))
        if j + 1 < c:
            choices.append((a[i][j + 1], i, j + 1))
        if not choices:
            break
        _, u, v = min(choices)
        a[i][j] = a[u][v]
        a[u][v] = None
        i, j = u, v
    size = r * c
    for u in range(r):
        for v in range(c):
            if a[u][v] is not None:
                a[u][v] -= 1
    a[i][j] = size
    return tuple(tuple(row) for row in a)


def insertion_tableau(p):
    rows = []
    for value in p:
        x = value
        i = 0
        while True:
            if i == len(rows):
                rows.append([x])
                break
            row = rows[i]
            j = next((j for j, y in enumerate(row) if y > x), None)
            if j is None:
                row.append(x)
                break
            row[j], x = x, row[j]
            i += 1
    return tuple(tuple(row) for row in rows)


def rsk_row_canonical(p):
    tab = insertion_tableau(p)
    return tuple(x for row in reversed(tab) for x in row)


def probe_controls():
    lines = []

    states = tuple(product(range(3), repeat=5))
    sig = functional_signature(states, ducci)
    lines.append(f"DUC q=3,n=5 signature={sig}")

    states = tuple(product(range(4), repeat=4))
    sig = functional_signature(states, lambda x: parikh_mod(x, 4))
    lines.append(f"PHM q=4,n=4 signature={sig}")

    states = tuple(x for x in product((0, 1), repeat=10) if sum(x) == 5)
    image = {vervaat(x) for x in states}
    A.eq(len(image), 42, "Vervaat Catalan image")
    A.ok(all(vervaat(y) == y for y in image), "Vervaat idempotence")
    fibres = Counter(vervaat(x) for x in states)
    lines.append(f"VVT semilength=5 image=42, fibre-spectrum={sorted(Counter(fibres.values()).items())}")

    states = ideals_grid(2, 3)
    A.eq(len(states), 10, "2x3 ideals")
    sig = functional_signature(states, rowmotion)
    A.eq(sig[0], len(states), "rowmotion bijection")
    lines.append(f"ROW grid=2x3 signature={sig}")

    states = tuple(permutations(range(7)))
    fibres = Counter(cyclic_predecessor(p) for p in states)
    A.eq(len(fibres), factorial(6), "cyclic predecessor image")
    A.ok(all(v == 7 for v in fibres.values()), "cyclic predecessor uniform fibres")
    A.ok(all(is_single_cycle(y) for y in fibres), "predecessors are 7-cycles")
    sig = functional_signature(states, cyclic_predecessor)
    lines.append(f"CPD n=7 signature={sig}")

    image = {foata(p) for p in states}
    A.eq(len(image), len(states), "Foata bijection")
    sig = functional_signature(states, foata)
    lines.append(f"FTF n=7 signature={sig}")

    rank = {p: i for i, p in enumerate(states)}
    lexsucc = lambda p: states[(rank[p] + 1) % len(states)]
    sig = functional_signature(states, lexsucc)
    A.eq(sig[2], ((factorial(7), 1),), "lex successor full cycle")
    lines.append(f"LXS n=7 signature={sig}")

    sig = functional_signature(states, inverse_perm)
    A.eq(sig[2], ((1, 232), (2, 2404)), "permutation inverse cycles")
    lines.append(f"PIN n=7 signature={sig}")

    n = 8
    istates = tuple(mask for mask in range(1 << n) if not (mask & (mask << 1)))
    A.eq(len(istates), 55, "path independent sets")
    sig = functional_signature(istates, lambda x: toggle_sweep(x, n))
    A.eq(sig[0], len(istates), "toggle sweep bijection")
    lines.append(f"ITS path=8 signature={sig}")

    n = 4
    pstates = tuple(product(range(n + 1), repeat=n))
    fibres = Counter(parking_normalize(x) for x in pstates)
    A.eq(len(fibres), (n + 1) ** (n - 1), "parking count")
    A.ok(all(v == n + 1 for v in fibres.values()), "parking uniform fibre")
    A.ok(all(parking_normalize(y) == y for y in fibres), "parking idempotent")
    lines.append(f"PFN n=4 image={len(fibres)}, uniform-fibre={n+1}")

    n = 8
    gstates = tuple(range(1 << n))
    gsucc = lambda g: gray((invgray(g) + 1) % (1 << n))
    sig = functional_signature(gstates, gsucc)
    A.eq(sig[2], ((1 << n, 1),), "Gray successor full cycle")
    lines.append(f"BRG n=8 signature={sig}")

    tabs = standard_tableaux(2, 3)
    A.eq(len(tabs), 5, "hook-length tableaux count")
    sig = functional_signature(tabs, tableau_promotion)
    A.eq(sig[0], len(tabs), "tableau promotion bijection")
    lines.append(f"SPR shape=2x3 signature={sig}")

    states = tuple(permutations(range(7)))
    fibres = Counter(rsk_row_canonical(p) for p in states)
    A.eq(len(fibres), 232, "RSK canonical image/involutions count")
    A.ok(all(rsk_row_canonical(y) == y for y in fibres), "RSK row canonical idempotent")
    lines.append(f"RKC n=7 image={len(fibres)}, fibre-spectrum={sorted(Counter(fibres.values()).items())}")
    return lines


def main():
    lines = []
    lines.extend(probe_lehmer())
    lines.append(probe_dae())
    lines.append(probe_mhe())
    lines.append(probe_stack_sort())
    lines.extend(probe_controls())
    A.eq(len(lines), 18, "eighteen literal systems")
    print("P162--P166 WORD/COMBINATORIAL BREADTH SCOUT")
    for i, line in enumerate(lines, 1):
        print(f"{i:02d} {line}")
    print(f"ASSERTIONS {A.assertions}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
