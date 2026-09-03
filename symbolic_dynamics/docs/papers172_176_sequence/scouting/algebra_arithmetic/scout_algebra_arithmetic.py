#!/usr/bin/env python3
"""Exact finite pilots for the P172--P176 algebra/arithmetic scout lane.

The script is intentionally standard-library only.  It enumerates twenty
literal finite maps.  Small cases are evidence and counterexample pressure,
not proofs and not novelty certificates.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial, gcd, prod


ASSERTIONS = 0


def check(condition: bool, message: str = "assertion failed") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def gaussian_binomial(n: int, k: int, q: int) -> int:
    if not 0 <= k <= n:
        return 0
    numerator = prod(q**n - q**i for i in range(k))
    denominator = prod(q**k - q**i for i in range(k))
    return numerator // denominator


def gaussian_subspace_total(n: int, q: int) -> int:
    return sum(gaussian_binomial(n, k, q) for k in range(n + 1))


def subspace_interval_mobius(rank: int, q: int) -> int:
    return (-1) ** rank * q ** (rank * (rank - 1) // 2)


def radical(n: int) -> int:
    ans = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            ans *= p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ans *= n
    return ans


def functional_stats(states, update):
    """Return exact functional-graph statistics on an explicitly listed set."""
    states = list(states)
    state_set = set(states)
    nxt = {}
    indeg = Counter()
    for x in states:
        y = update(x)
        check(y in state_set, f"map not closed at {x!r} -> {y!r}")
        nxt[x] = y
        indeg[y] += 1

    depth = {}
    cycle_lengths = []
    seen_global = set()
    for start in states:
        if start in seen_global:
            continue
        path = []
        pos = {}
        x = start
        while x not in pos and x not in depth:
            pos[x] = len(path)
            path.append(x)
            x = nxt[x]
        if x in pos:
            j = pos[x]
            cyc = path[j:]
            cycle_lengths.append(len(cyc))
            for z in cyc:
                depth[z] = 0
            for z in reversed(path[:j]):
                depth[z] = depth[nxt[z]] + 1
        else:
            for z in reversed(path):
                depth[z] = depth[nxt[z]] + 1
        seen_global.update(path)
    check(len(depth) == len(states))
    for x in states:
        check(depth[nxt[x]] == max(depth[x] - 1, 0) or depth[x] == 0)
    return {
        "states": len(states),
        "image": len(set(nxt.values())),
        "fixed": sum(nxt[x] == x for x in states),
        "cycles": len(cycle_lengths),
        "cycle_lengths": tuple(sorted(Counter(cycle_lengths).items())),
        "max_tail": max(depth.values(), default=0),
        "max_fibre": max(indeg.values(), default=0),
        "zero_fibres": len(states) - len(indeg),
        "depth_hist": tuple(sorted(Counter(depth.values()).items())),
    }, nxt, depth, indeg


def fmt_stats(s) -> str:
    return (
        f"states={s['states']} image={s['image']} fixed={s['fixed']} "
        f"cycles={s['cycles']} cycle_lengths={s['cycle_lengths']} "
        f"max_tail={s['max_tail']} max_fibre={s['max_fibre']} "
        f"zero_fibres={s['zero_fibres']} depth_hist={s['depth_hist']}"
    )


# ---------- Binary subspaces ----------


def mask_elements(space_mask: int):
    x = space_mask
    while x:
        bit = x & -x
        yield bit.bit_length() - 1
        x -= bit


@lru_cache(None)
def binary_subspaces(m: int) -> tuple[int, ...]:
    """All F_2-subspaces of F_2^m, encoded as masks of their vectors."""
    zero = 1  # vector 0 only
    found = {zero}
    queue = deque([zero])
    ambient = 1 << m
    while queue:
        space = queue.popleft()
        members = tuple(mask_elements(space))
        for v in range(1, ambient):
            if (space >> v) & 1:
                continue
            new_space = space
            for u in members:
                new_space |= 1 << (u ^ v)
            if new_space not in found:
                found.add(new_space)
                queue.append(new_space)
    ans = tuple(sorted(found))
    gaussian_total = 0
    for k in range(m + 1):
        num = prod((2**m - 2**i) for i in range(k))
        den = prod((2**k - 2**i) for i in range(k))
        gaussian_total += num // den
    check(len(ans) == gaussian_total)
    for s in ans:
        size = s.bit_count()
        check(size & (size - 1) == 0)
    return ans


def binary_span(vectors, m: int) -> int:
    space = 1
    for v in vectors:
        if (space >> v) & 1:
            continue
        members = tuple(mask_elements(space))
        for u in members:
            space |= 1 << (u ^ v)
    check(space in set(binary_subspaces(m)))
    return space


def binary_image(space: int, linear_map) -> int:
    return sum((1 << linear_map(v)) for v in mask_elements(space))


def binary_sum(a: int, b: int, m: int) -> int:
    return binary_span(tuple(mask_elements(a)) + tuple(mask_elements(b)), m)


def binary_dim(space: int) -> int:
    return space.bit_count().bit_length() - 1


def binary_backward_orbit_span(space: int, m: int, t: int) -> int:
    out = 1
    for i in range(t + 1):
        preimage = binary_image(
            space, lambda v, ii=i, mm=m: rotate_left_n(v, mm, -ii)
        )
        out = binary_sum(out, preimage, m)
    return out


def rotate_left(v: int, m: int) -> int:
    return ((v << 1) & ((1 << m) - 1)) | (v >> (m - 1))


def vector_add(x: int, y: int, p: int, m: int) -> int:
    a = digits(x, p, m)
    b = digits(y, p, m)
    return undigits(tuple((u + v) % p for u, v in zip(a, b)), p)


def vector_scale(c: int, x: int, p: int, m: int) -> int:
    return undigits(tuple(c * u % p for u in digits(x, p, m)), p)


@lru_cache(None)
def prime_subspaces(p: int, m: int):
    """All subspaces of F_p^m for small odd-prime control cases."""
    zero = frozenset((0,))
    found = {zero}
    queue = deque([zero])
    for_space = p**m
    while queue:
        space = queue.popleft()
        for v in range(1, for_space):
            if v in space:
                continue
            new_space = frozenset(
                vector_add(u, vector_scale(c, v, p, m), p, m)
                for u in space for c in range(p)
            )
            if new_space not in found:
                found.add(new_space)
                queue.append(new_space)
    ans = tuple(sorted(found, key=lambda s: (len(s), tuple(sorted(s)))))
    gaussian_total = 0
    for k in range(m + 1):
        num = prod((p**m - p**i) for i in range(k))
        den = prod((p**k - p**i) for i in range(k))
        gaussian_total += num // den
    check(len(ans) == gaussian_total)
    return ans


def rotate_prime_vector(x: int, p: int, m: int, t: int = 1) -> int:
    a = digits(x, p, m)
    t %= m
    return undigits(tuple(a[(i - t) % m] for i in range(m)), p)


def prime_sum(a, b, p: int, m: int):
    return frozenset(vector_add(x, y, p, m) for x in a for y in b)


def prime_dim(space, p: int) -> int:
    size = len(space)
    dimension = 0
    while size > 1:
        check(size % p == 0)
        size //= p
        dimension += 1
    return dimension


def prime_backward_orbit_span(space, p: int, m: int, t: int):
    out = frozenset((0,))
    for i in range(t + 1):
        preimage = frozenset(rotate_prime_vector(x, p, m, -i) for x in space)
        out = prime_sum(out, preimage, p, m)
    return out


IRREDUCIBLE_GF2 = {
    2: 0b111,       # x^2+x+1
    3: 0b1011,      # x^3+x+1
    4: 0b10011,     # x^4+x+1
    5: 0b100101,    # x^5+x^2+1
    6: 0b1000011,   # x^6+x+1
}


def gf2_mul(a: int, b: int, m: int) -> int:
    modulus = IRREDUCIBLE_GF2[m]
    out = 0
    x = a
    y = b
    while y:
        if y & 1:
            out ^= x
        y >>= 1
        x <<= 1
        if x & (1 << m):
            x ^= modulus
    return out & ((1 << m) - 1)


def test_fields() -> None:
    for m in IRREDUCIBLE_GF2:
        n = 1 << m
        for a in range(1, n):
            check(len({gf2_mul(a, b, m) for b in range(n)}) == n)


# ---------- Polynomials over F_p ----------


def poly_trim(f, p):
    f = tuple(x % p for x in f)
    i = len(f) - 1
    while i > 0 and f[i] == 0:
        i -= 1
    return f[: i + 1]


def poly_divmod(f, g, p):
    f = list(poly_trim(f, p))
    g = poly_trim(g, p)
    check(g != (0,))
    if len(f) < len(g):
        return (0,), tuple(f)
    q = [0] * (len(f) - len(g) + 1)
    inv = pow(g[-1], -1, p)
    while len(f) >= len(g) and any(f):
        c = f[-1] * inv % p
        j = len(f) - len(g)
        q[j] = c
        for i, gi in enumerate(g):
            f[i + j] = (f[i + j] - c * gi) % p
        f = list(poly_trim(f, p))
    return poly_trim(q, p), poly_trim(f, p)


def poly_monic(f, p):
    f = poly_trim(f, p)
    if f == (0,):
        return f
    inv = pow(f[-1], -1, p)
    return tuple(x * inv % p for x in f)


def poly_gcd(f, g, p):
    f = poly_trim(f, p)
    g = poly_trim(g, p)
    while g != (0,):
        _, r = poly_divmod(f, g, p)
        f, g = g, r
    return poly_monic(f, p)


def poly_derivative(f, p):
    if len(f) <= 1:
        return (0,)
    return poly_trim(tuple(i * f[i] % p for i in range(1, len(f))), p)


@lru_cache(None)
def monic_polynomials(p: int, max_degree: int) -> tuple[tuple[int, ...], ...]:
    ans = [(1,)]
    for d in range(1, max_degree + 1):
        for low in product(range(p), repeat=d):
            ans.append(tuple(low) + (1,))
    return tuple(ans)


@lru_cache(None)
def irreducibles(p: int, max_degree: int):
    ans = []
    for f in monic_polynomials(p, max_degree):
        d = len(f) - 1
        if d == 0:
            continue
        reducible = False
        for g in monic_polynomials(p, d // 2):
            if len(g) == 1:
                continue
            _, r = poly_divmod(f, g, p)
            if r == (0,):
                reducible = True
                break
        if not reducible:
            ans.append(f)
    return tuple(ans)


@lru_cache(None)
def poly_factor(f, p):
    f = poly_monic(f, p)
    out = []
    for g in irreducibles(p, len(f) - 1):
        e = 0
        while len(f) >= len(g):
            q, r = poly_divmod(f, g, p)
            if r != (0,):
                break
            f = q
            e += 1
        if e:
            out.append((g, e))
        if f == (1,):
            break
    check(f == (1,))
    return tuple(out)


def derivative_gcd(f, p):
    return poly_gcd(f, poly_derivative(f, p), p)


def convolve_truncated(a, b, limit: int):
    out = [0] * (limit + 1)
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if i + j > limit:
                break
            if y:
                out[i + j] += x * y
    return out


def derivative_gcd_fibre_gf_count(target, p: int, n: int, t: int) -> int:
    """Coefficient sum of the exact factor-degree fibre Euler product."""
    target_factor = dict(poly_factor(target, p))
    coeff = [1] + [0] * n
    for irr in irreducibles(p, n):
        d = len(irr) - 1
        b = target_factor.get(irr, 0)
        local = [0] * (n + 1)
        for e in range(n // d + 1):
            if e - min(t, e % p) == b:
                local[e * d] = 1
        coeff = convolve_truncated(coeff, local, n)
        if not any(coeff):
            return 0
    return sum(coeff)


def derivative_gcd_depth_gf_count(p: int, n: int, r: int) -> int:
    """Count depth <= r from the truncated irreducible-factor Euler product."""
    coeff = [1] + [0] * n
    for irr in irreducibles(p, n):
        d = len(irr) - 1
        local = [0] * (n + 1)
        for e in range(n // d + 1):
            if e % p <= r:
                local[e * d] = 1
        coeff = convolve_truncated(coeff, local, n)
    return sum(coeff)


def reciprocal_monic(f, p):
    f = poly_trim(f, p)
    check(f[0] != 0)
    return poly_monic(tuple(reversed(f)), p)


# ---------- Base-p vectors ----------


def digits(x: int, p: int, m: int) -> tuple[int, ...]:
    ans = []
    for _ in range(m):
        ans.append(x % p)
        x //= p
    return tuple(ans)


def undigits(a, p: int) -> int:
    out = 0
    mul = 1
    for x in a:
        out += x * mul
        mul *= p
    return out


def cyclic_difference(x: int, p: int, m: int) -> int:
    a = digits(x, p, m)
    b = tuple((a[(i - 1) % m] - a[i]) % p for i in range(m))
    return undigits(b, p)


def finite_difference_poly(x: int, p: int, degree: int) -> int:
    a = digits(x, p, degree + 1)
    b = []
    for j in range(degree + 1):
        b.append(sum(a[k] * comb(k, j) for k in range(j + 1, degree + 1)) % p)
    return undigits(tuple(b), p)


# ---------- Matrices, permutations, forms ----------


def strict_ut_positions(n: int):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def strict_ut_square(code: int, n: int) -> int:
    pos = strict_ut_positions(n)
    a = [[0] * n for _ in range(n)]
    for k, (i, j) in enumerate(pos):
        a[i][j] = (code >> k) & 1
    b = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            b[i][j] = sum(a[i][k] * a[k][j] for k in range(n)) % 2
    out = 0
    for k, (i, j) in enumerate(pos):
        out |= b[i][j] << k
    return out


def perm_compose(a, b):
    """a after b."""
    return tuple(a[b[i]] for i in range(len(a)))


def perm_inverse(a):
    inv = [0] * len(a)
    for i, x in enumerate(a):
        inv[x] = i
    return tuple(inv)


def commutator_with_transposition(g):
    n = len(g)
    a = tuple([1, 0] + list(range(2, n)))
    return perm_compose(perm_compose(perm_compose(perm_inverse(g), a), g), a)


def permutation_fixed_points(g) -> int:
    return sum(i == x for i, x in enumerate(g))


def polynomial_multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)


def partial_rencontres_polynomial(size: int, diagonal_slots: int):
    """Sum u^fix over bijections between two size-N sets sharing s labels."""
    check(0 <= diagonal_slots <= size)
    out = [0] * (diagonal_slots + 1)
    for j in range(diagonal_slots + 1):
        scale = comb(diagonal_slots, j) * factorial(size - j)
        for k in range(j + 1):
            out[k] += scale * comb(j, k) * (-1) ** (j - k)
    check(sum(out) == factorial(size))
    check(all(x >= 0 for x in out))
    return tuple(out)


def transposition_conjugator_polynomial(n: int, overlap: int):
    """Marked fibre polynomial for g^{-1}(12)g=b, |supp(b) cap {1,2}|=r."""
    check(overlap in (0, 1, 2))
    common_complement = n - 4 + overlap
    check(common_complement >= 0)
    orientation = {
        0: (2,),
        1: (1, 1),
        2: (1, 0, 1),
    }[overlap]
    ans = polynomial_multiply(
        orientation,
        partial_rencontres_polynomial(n - 2, common_complement),
    )
    check(sum(ans) == 2 * factorial(n - 2))
    return ans


def ut4_multiply_vector(x: int, y: int) -> int:
    n = 4
    pos = strict_ut_positions(n)
    index = {ij: k for k, ij in enumerate(pos)}
    out = 0
    for i in range(n):
        for j in range(i + 1, n):
            bit = 0
            for k in range(i + 1, j):
                bit ^= ((x >> index[(i, k)]) & 1) & ((y >> index[(k, j)]) & 1)
            out |= bit << index[(i, j)]
    return out


def lie_hull(space: int) -> int:
    vecs = tuple(mask_elements(space))
    brackets = []
    for x in vecs:
        for y in vecs:
            brackets.append(ut4_multiply_vector(x, y) ^ ut4_multiply_vector(y, x))
    return binary_span(vecs + tuple(brackets), 6)


def symplectic_pair(x: int, y: int, m: int) -> int:
    out = 0
    for i in range(0, m, 2):
        out ^= ((x >> i) & 1) & ((y >> (i + 1)) & 1)
        out ^= ((x >> (i + 1)) & 1) & ((y >> i) & 1)
    return out


def symplectic_radical(space: int, m: int) -> int:
    orth = 0
    vecs = tuple(mask_elements(space))
    for x in range(1 << m):
        if all(symplectic_pair(x, y, m) == 0 for y in vecs):
            orth |= 1 << x
    check(orth in set(binary_subspaces(m)))
    return space & orth


def subset_shift(mask: int, h: int, n: int) -> int:
    out = 0
    for x in range(n):
        if (mask >> x) & 1:
            out |= 1 << ((x + h) % n)
    return out


def translation_stabilizer(mask: int, n: int) -> int:
    return sum(1 << h for h in range(n) if subset_shift(mask, h, n) == mask)


def cyclic_generated_subgroup(mask: int, n: int) -> int:
    g = n
    for x in range(n):
        if (mask >> x) & 1:
            g = gcd(g, x)
    return sum(1 << x for x in range(n) if x % g == 0)


def schur_square(space: int, m: int) -> int:
    vecs = tuple(mask_elements(space))
    products = tuple(x & y for x in vecs for y in vecs)
    return binary_span(products, m)


def nilpotent_hull(space: int, m: int) -> int:
    image = binary_image(space, lambda x: x >> 1)
    return binary_sum(space, image, m)


def print_case(system: str, params: str, stats) -> None:
    print(f"{system} {params} {fmt_stats(stats)}")


def run() -> None:
    print("P172-P176 ALGEBRA/ARITHMETIC EXACT SCOUT")
    print("schema=literal-map pilots; standard-library; HOLD_EXTERNAL")
    test_fields()

    # A01. U -> U intersect F(U), F a Frobenius cycle in a normal basis.
    print("\n[A01] frobenius_meet_subspaces")
    for m in range(3, 7):
        states = binary_subspaces(m)
        shift = lambda v, mm=m: rotate_left(v, mm)
        update = lambda u, sh=shift: u & binary_image(u, sh)
        s, nxt, depth, indeg = functional_stats(states, update)
        for u in states:
            acc = u
            x = u
            for t in range(m + 1):
                if t:
                    acc &= binary_image(u, lambda v, tt=t, mm=m: rotate_left_n(v, mm, tt))
                    x = nxt[x]
                check(x == acc)
            check(nxt[u] == u if binary_image(u, shift) == u else True)
        invariant = sum(binary_image(u, shift) == u for u in states)
        check(s["fixed"] == invariant)
        xm_minus_one = (1,) + (0,) * (m - 1) + (1,)
        invariant_formula = prod(e + 1 for _, e in poly_factor(xm_minus_one, 2))
        check(invariant == invariant_formula)
        terminal = Counter()
        for u in states:
            x = u
            while nxt[x] != x:
                x = nxt[x]
            terminal[x] += 1
        fixed_spaces = tuple(u for u in states if nxt[u] == u)
        for w in fixed_spaces:
            containing = sum((w & ~u) == 0 for u in states)
            cumulative_basins = sum(c for k, c in terminal.items() if (w & ~k) == 0)
            check(containing == cumulative_basins)
        fibre_times = "not_run"
        if m <= 5:
            for t in range(m):
                actual = Counter()
                for u in states:
                    x = u
                    for _ in range(t):
                        x = nxt[x]
                    actual[x] += 1
                upper_counts = {
                    k: gaussian_subspace_total(
                        m - binary_dim(binary_backward_orbit_span(k, m, t)), 2
                    )
                    for k in states
                }
                for w in states:
                    dw = binary_dim(w)
                    predicted = sum(
                        subspace_interval_mobius(binary_dim(k) - dw, 2) * upper_counts[k]
                        for k in states if (w & ~k) == 0
                    )
                    check(predicted == actual.get(w, 0))
            fibre_times = f"0..{m - 1}"
        check(s["max_tail"] == m - 1)
        print_case(
            "A01",
            f"q=2 m={m} invariant={invariant} fixed_formula={invariant_formula} "
            f"mobius_fibre_times={fibre_times}",
            s,
        )
    for p, m in ((3, 3), (3, 4), (5, 3)):
        states = prime_subspaces(p, m)
        update = lambda u, pp=p, mm=m: u & frozenset(rotate_prime_vector(x, pp, mm) for x in u)
        s, nxt, _, _ = functional_stats(states, update)
        for u in states:
            x = u
            acc = u
            for t in range(1, m + 1):
                acc &= frozenset(rotate_prime_vector(v, p, m, t) for v in u)
                x = nxt[x]
                check(x == acc)
        invariant = sum(frozenset(rotate_prime_vector(x, p, m) for x in u) == u for u in states)
        check(s["fixed"] == invariant)
        xm_minus_one = ((-1) % p,) + (0,) * (m - 1) + (1,)
        invariant_formula = prod(e + 1 for _, e in poly_factor(xm_minus_one, p))
        check(invariant == invariant_formula)
        check(s["max_tail"] == m - 1)
        terminal = Counter()
        for u in states:
            x = u
            while nxt[x] != x:
                x = nxt[x]
            terminal[x] += 1
        for w in (u for u in states if nxt[u] == u):
            containing = sum(w <= u for u in states)
            cumulative_basins = sum(c for k, c in terminal.items() if w <= k)
            check(containing == cumulative_basins)
        for t in range(m):
            actual = Counter()
            for u in states:
                x = u
                for _ in range(t):
                    x = nxt[x]
                actual[x] += 1
            upper_counts = {
                k: gaussian_subspace_total(
                    m - prime_dim(prime_backward_orbit_span(k, p, m, t), p),
                    p,
                )
                for k in states
            }
            for w in states:
                dw = prime_dim(w, p)
                predicted = sum(
                    subspace_interval_mobius(prime_dim(k, p) - dw, p)
                    * upper_counts[k]
                    for k in states if w <= k
                )
                check(predicted == actual.get(w, 0))
        print_case(
            "A01",
            f"q={p} m={m} invariant={invariant} fixed_formula={invariant_formula} "
            f"mobius_fibre_times=0..{m - 1}",
            s,
        )

    # A02. Multiplicative span closure on field subspaces containing 1.
    print("\n[A02] field_product_span_closure")
    for m in range(2, 7):
        states = tuple(u for u in binary_subspaces(m) if (u >> 1) & 1)
        def update(u, mm=m):
            vv = tuple(mask_elements(u))
            return binary_span(tuple(gf2_mul(x, y, mm) for x in vv for y in vv), mm)
        s, nxt, depth, indeg = functional_stats(states, update)
        fixed_dims = Counter((u.bit_count().bit_length() - 1) for u in states if nxt[u] == u)
        check(s["fixed"] == len(divisors(m)))
        check(tuple(sorted(fixed_dims)) == tuple(divisors(m)))
        basin_dims = Counter()
        for u in states:
            x = u
            while nxt[x] != x:
                x = nxt[x]
            basin_dims[x.bit_count().bit_length() - 1] += 1
        print_case("A02", f"q=2 m={m} fixed_dims={tuple(sorted(fixed_dims.items()))} basin_by_terminal_dim={tuple(sorted(basin_dims.items()))}", s)

    # A03. f -> gcd(f,f') on monic polynomials of bounded degree.
    print("\n[A03] derivative_gcd_polynomials")
    for p, n in ((2, 8), (3, 6), (5, 4)):
        states = monic_polynomials(p, n)
        update = lambda f, pp=p: derivative_gcd(f, pp)
        s, nxt, depth, indeg = functional_stats(states, update)
        for f in states:
            factors = poly_factor(f, p)
            check(depth[f] == max((e % p for _, e in factors), default=0))
            x = f
            for t in range(p + 1):
                xf = dict(poly_factor(x, p))
                for g, e in factors:
                    check(xf.get(g, 0) == e - min(t, e % p))
                x = nxt[x]
            check(poly_derivative(x, p) == (0,))
        print_case("A03", f"p={p} degree_le={n}", s)
        for r in range(p):
            actual_cdf = sum(d <= r for d in depth.values())
            gf_cdf = derivative_gcd_depth_gf_count(p, n, r)
            check(actual_cdf == gf_cdf)
            print(f"A03 p={p} depth_le={r} factor_degree_gf={gf_cdf}")
        for t in range(1, p):
            counts = Counter()
            for f in states:
                x = f
                for _ in range(t):
                    x = nxt[x]
                counts[x] += 1
            for g in states:
                predicted = derivative_gcd_fibre_gf_count(g, p, n, t)
                check(predicted == counts.get(g, 0))
            print(f"A03 p={p} t={t} image={len(counts)} max_time_t_fibre={max(counts.values())}")

    # A04. Artin--Schreier/Frobenius difference in a normal basis.
    print("\n[A04] artin_schreier_difference")
    for p, m in ((2, 5), (2, 8), (3, 4), (3, 6)):
        states = range(p**m)
        update = lambda x, pp=p, mm=m: cyclic_difference(x, pp, mm)
        s, _, _, _ = functional_stats(states, update)
        print_case("A04", f"p={p} m={m}", s)

    # A05. Finite difference Delta f=f(x+1)-f(x).
    print("\n[A05] finite_difference_polynomials")
    for p, d in ((2, 7), (3, 5), (5, 3)):
        states = range(p ** (d + 1))
        update = lambda x, pp=p, dd=d: finite_difference_poly(x, pp, dd)
        s, nxt, _, _ = functional_stats(states, update)
        for x in states:
            y = x
            for _ in range(p):
                y = nxt[y]
            check(y == 0)
        print_case("A05", f"p={p} degree_le={d}", s)

    # A06. Trace/linear-functional scaling x -> Tr(x)x.
    print("\n[A06] trace_scaling")
    for p, m in ((3, 4), (5, 3), (7, 2)):
        states = range(p**m)
        def update(x, pp=p, mm=m):
            a = digits(x, pp, mm)
            tr = sum(a) % pp
            return undigits(tuple(tr * z % pp for z in a), pp)
        s, _, _, _ = functional_stats(states, update)
        print_case("A06", f"p={p} m={m}", s)

    # A07. Norm scaling reduces exactly to a fixed power map on F_(q^m)^*.
    print("\n[A07] norm_scaling")
    for q, m in ((3, 3), (4, 3), (5, 2)):
        n = q**m - 1
        norm_exp = n // (q - 1)
        states = range(n + 1)  # exponent 0..n-1 plus distinguished zero n
        update = lambda j, nn=n, ee=norm_exp: nn if j == nn else ((ee + 1) * j) % nn
        s, _, _, _ = functional_stats(states, update)
        print_case("A07", f"q={q} m={m} power={norm_exp+1}", s)

    # A08. State-dependent radical-of-order erosion on a cyclic group.
    print("\n[A08] order_radical_erosion")
    for n in (60, 72, 120, 180):
        states = range(n)
        def update(j, nn=n):
            order = nn // gcd(nn, j)
            return j * radical(order) % nn
        s, nxt, depth, _ = functional_stats(states, update)
        expected = max((max_prime_exp(n),), default=0)
        check(s["fixed"] == 1)
        check(s["max_tail"] <= expected)
        print_case("A08", f"N={n} max_prime_exp={expected}", s)

    # A09. I -> I+Ann(I) on ideals of Z/NZ (prime-exponent model).
    print("\n[A09] annihilator_sum_ideals")
    for exponents in ((3, 4, 2), (6, 5), (7, 3, 2)):
        states = tuple(product(*(range(e + 1) for e in exponents)))
        update = lambda a, ee=exponents: tuple(min(x, e - x) for x, e in zip(a, ee))
        s, nxt, _, _ = functional_stats(states, update)
        check(all(nxt[nxt[x]] == nxt[x] for x in states))
        print_case("A09", f"exponents={exponents}", s)

    # A10. Squaring on the residue ring Z/p^k Z.
    print("\n[A10] modular_squaring")
    for p, k in ((2, 8), (3, 5), (5, 4)):
        n = p**k
        states = range(n)
        update = lambda x, nn=n: x * x % nn
        s, _, _, _ = functional_stats(states, update)
        print_case("A10", f"modulus={p}^{k}", s)

    # A11. Lang quotient x -> x^(q-1) on a finite-field multiplicative group.
    print("\n[A11] lang_power_map")
    for q, m in ((2, 8), (3, 4), (5, 3)):
        n = q**m - 1
        states = range(n + 1)
        update = lambda j, nn=n, qq=q: nn if j == nn else ((qq - 1) * j) % nn
        s, _, _, _ = functional_stats(states, update)
        print_case("A11", f"q={q} m={m} group_order={n}", s)

    # A12. Reciprocal-core map f -> gcd(f,f*) on nonzero-constant monics.
    print("\n[A12] reciprocal_core_polynomials")
    for p, n in ((2, 7), (3, 5)):
        states = tuple(f for f in monic_polynomials(p, n) if f[0] != 0)
        update = lambda f, pp=p: poly_gcd(f, reciprocal_monic(f, pp), pp)
        s, nxt, _, _ = functional_stats(states, update)
        check(all(nxt[nxt[f]] == nxt[f] for f in states))
        print_case("A12", f"p={p} degree_le={n}", s)

    # A13. A subset of C_n maps to its translation stabilizer.
    print("\n[A13] translation_stabilizer_subsets")
    for n in (8, 9, 10):
        states = range(1 << n)
        update = lambda a, nn=n: translation_stabilizer(a, nn)
        s, nxt, _, _ = functional_stats(states, update)
        check(all(nxt[nxt[a]] == nxt[a] for a in states))
        print_case("A13", f"n={n}", s)

    # A14. A subset of C_n maps to the subgroup it generates.
    print("\n[A14] cyclic_generated_subgroup")
    for n in (10, 12, 16):
        states = range(1 << n)
        update = lambda a, nn=n: cyclic_generated_subgroup(a, nn)
        s, nxt, _, _ = functional_stats(states, update)
        check(all(nxt[nxt[a]] == nxt[a] for a in states))
        print_case("A14", f"n={n}", s)

    # A15. Squaring strict upper-triangular matrices over F_2.
    print("\n[A15] strict_upper_triangular_squaring")
    for n in (4, 5):
        states = range(1 << (n * (n - 1) // 2))
        update = lambda a, nn=n: strict_ut_square(a, nn)
        s, _, _, _ = functional_stats(states, update)
        check(s["fixed"] == 1 and s["cycles"] == 1)
        print_case("A15", f"q=2 n={n}", s)

    # A16. g -> [g,(12)] on S_n.
    print("\n[A16] fixed_transposition_commutator")
    for n in (4, 5, 6):
        states = tuple(permutations(range(n)))
        update = commutator_with_transposition
        s, nxt, _, _ = functional_stats(states, update)
        a = tuple([1, 0] + list(range(2, n)))
        marked = defaultdict(Counter)
        for g in states:
            marked[nxt[g]][permutation_fixed_points(g)] += 1
        overlap_polynomials = defaultdict(set)
        for target, counter in marked.items():
            b = perm_compose(target, a)
            support = {i for i in range(n) if b[i] != i}
            check(len(support) == 2)
            overlap = len(support & {0, 1})
            actual = tuple(counter.get(k, 0) for k in range(n + 1))
            while actual and actual[-1] == 0:
                actual = actual[:-1]
            predicted = transposition_conjugator_polynomial(n, overlap)
            check(actual == predicted)
            overlap_polynomials[overlap].add(predicted)
        expected_target_counts = {
            0: comb(n - 2, 2),
            1: 2 * (n - 2),
            2: 1,
        }
        for overlap, expected_count in expected_target_counts.items():
            actual_count = sum(
                1
                for target in marked
                if len({i for i in range(n) if perm_compose(target, a)[i] != i} & {0, 1}) == overlap
            )
            check(actual_count == expected_count)
            if expected_count:
                check(len(overlap_polynomials[overlap]) == 1)
        print_case("A16", f"S_{n}", s)
        print(
            "A16 " + f"S_{n} marked_fibres=" +
            ";".join(f"r={r}:{transposition_conjugator_polynomial(n, r)}" for r in range(3) if n - 4 + r >= 0)
        )

    # A17. Lie-subalgebra hull step U -> U+[U,U] in strict UT_4(F_2).
    print("\n[A17] lie_bracket_hull")
    states = binary_subspaces(6)
    s, nxt, _, _ = functional_stats(states, lie_hull)
    check(all((x & ~nxt[x]) == 0 for x in states))
    print_case("A17", "ut4_F2", s)

    # A18. U -> rad(U) for a symplectic form.
    print("\n[A18] symplectic_radical")
    for m in (4, 6):
        states = binary_subspaces(m)
        update = lambda u, mm=m: symplectic_radical(u, mm)
        s, nxt, _, _ = functional_stats(states, update)
        check(all(nxt[nxt[u]] == nxt[u] for u in states))
        print_case("A18", f"q=2 dimension={m}", s)

    # A19. Schur-square closure of binary codes containing the all-one word.
    print("\n[A19] schur_square_codes")
    for m in (5, 6):
        ones = (1 << m) - 1
        states = tuple(u for u in binary_subspaces(m) if (u >> ones) & 1)
        update = lambda u, mm=m: schur_square(u, mm)
        s, nxt, _, _ = functional_stats(states, update)
        check(all((u & ~nxt[u]) == 0 for u in states))
        print_case("A19", f"q=2 length={m}", s)

    # A20. Nilpotent-module hull U -> U+N(U), N one Jordan block.
    print("\n[A20] nilpotent_module_hull")
    for m in (5, 6):
        states = binary_subspaces(m)
        update = lambda u, mm=m: nilpotent_hull(u, mm)
        s, nxt, _, _ = functional_stats(states, update)
        check(all((u & ~nxt[u]) == 0 for u in states))
        print_case("A20", f"q=2 block={m}", s)

    print(f"\nASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS")


def rotate_left_n(v: int, m: int, t: int) -> int:
    for _ in range(t % m):
        v = rotate_left(v, m)
    return v


def max_prime_exp(n: int) -> int:
    ans = 0
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        ans = max(ans, e)
        p += 1
    if n > 1:
        ans = max(ans, 1)
    return ans


if __name__ == "__main__":
    run()
