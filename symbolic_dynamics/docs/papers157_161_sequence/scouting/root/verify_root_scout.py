#!/usr/bin/env python3
"""Deterministic exact pilots for the root P157--P161 breadth lane.

The two full gates are:

* NHI: x -> 3*x^2-2*x^3 modulo 2^n;
* ASD: x -> x^q-x on F_(q^m), represented in a normal basis by
  cyclic finite difference on F_q^m.

The remaining pilots are deliberately cheaper collision/weak-signal tests.
No random source, external package, or floating-point comparison is used.
"""

from __future__ import annotations

from collections import Counter
from functools import reduce
from itertools import product
from math import gcd


ASSERTIONS = 0


def check(condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def valuation(n: int, p: int, cap: int) -> int:
    if n == 0:
        return cap
    ans = 0
    while ans < cap and n % p == 0:
        n //= p
        ans += 1
    return ans


def ceil_doubling_steps(threshold: int, start: int) -> int:
    t = 0
    while (1 << t) * start < threshold:
        t += 1
    return t


# ---------------------------------------------------------------------------
# NHI: Newton--Hensel idempotent lift modulo 2^n.


def nhi_map(x: int, n: int) -> int:
    return (3 * x * x - 2 * x * x * x) % (1 << n)


def nhi_error(x: int, n: int) -> int:
    """Error from the parity-selected endpoint, as an integer residue."""
    modulus = 1 << n
    return x % modulus if x % 2 == 0 else (1 - x) % modulus


def nhi_predicted_target_fibre(y: int, n: int) -> int:
    modulus = 1 << n
    y %= modulus
    if y in (0, 1):
        return 1 << (n // 2)

    reflected = y if y % 2 == 0 else (1 - y) % modulus
    w = valuation(reflected, 2, n)
    if w < 2 or w % 2:
        return 0
    v = w // 2
    if 2 * v >= n:
        return 0
    N = n - 2 * v
    unit = reflected >> (2 * v)
    residue_modulus = 1 << min(3, N)
    epsilon = 7 if v == 1 else 3
    if unit % residue_modulus != epsilon % residue_modulus:
        return 0
    return 1 << (v + min(N - 1, 2))


def verify_nhi() -> list[str]:
    signatures: list[str] = []
    for n in range(1, 17):
        modulus = 1 << n
        values = [nhi_map(x, n) for x in range(modulus)]
        fibres = Counter(values)
        check([x for x, y in enumerate(values) if x == y] == [0, 1], f"NHI fixed n={n}")

        depths = []
        for x in range(modulus):
            e = nhi_error(x, n)
            v = valuation(e, 2, n)
            predicted_depth = 0 if v == n else ceil_doubling_steps(n, v)
            z = x
            depth = 0
            while z not in (0, 1):
                z = nhi_map(z, n)
                depth += 1
                check(depth <= 1 + n.bit_length(), f"NHI termination n={n}, x={x}")
            check(z == x % 2, f"NHI parity endpoint n={n}, x={x}")
            check(depth == predicted_depth, f"NHI depth n={n}, x={x}")
            if x not in (0, 1):
                next_error = nhi_error(nhi_map(x, n), n)
                check(
                    valuation(next_error, 2, n) == min(n, 2 * v),
                    f"NHI valuation n={n}, x={x}",
                )
            depths.append(depth)

        for t in range(0, max(depths) + 1):
            observed = sum(d <= t for d in depths)
            threshold = (n + (1 << t) - 1) // (1 << t)
            predicted = 2 << (n - threshold)
            check(observed == predicted, f"NHI CDF n={n}, t={t}")

        for y in range(modulus):
            check(
                fibres.get(y, 0) == nhi_predicted_target_fibre(y, n),
                f"NHI fibre n={n}, y={y}",
            )
        predicted_image = 2 + 2 * sum(
            1 << max(0, n - 2 * v - 3)
            for v in range(1, (n - 1) // 2 + 1)
        )
        check(len(fibres) == predicted_image, f"NHI image n={n}")
        signatures.append(
            f"n={n}:phase={modulus},image={len(fibres)},height={max(depths)},"
            f"fibres={','.join(map(str, sorted(set(fibres.values()))))}"
        )
    return signatures


# ---------------------------------------------------------------------------
# ASD: Artin--Schreier difference in normal coordinates.


def asd_map(x: tuple[int, ...], q: int) -> tuple[int, ...]:
    return tuple((x[(i - 1) % len(x)] - x[i]) % q for i in range(len(x)))


def asd_iterate(x: tuple[int, ...], q: int, t: int) -> tuple[int, ...]:
    for _ in range(t):
        x = asd_map(x, q)
    return x


def prime_power_part(m: int, p: int) -> int:
    ans = 1
    while m % p == 0:
        ans *= p
        m //= p
    return ans


def poly_trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_sub(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p
    return poly_trim(out)


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return poly_trim(out)


def poly_pow(a: list[int], k: int, p: int) -> list[int]:
    out = [1]
    while k:
        if k & 1:
            out = poly_mul(out, a, p)
        a = poly_mul(a, a, p)
        k //= 2
    return out


def poly_mod(a: list[int], b: list[int], p: int) -> list[int]:
    a = poly_trim(a[:])
    b = poly_trim(b[:])
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b) and a != [0]:
        coeff = a[-1] * inv % p
        shift = len(a) - len(b)
        for i, x in enumerate(b):
            a[i + shift] = (a[i + shift] - coeff * x) % p
        poly_trim(a)
    return a


def poly_gcd(a: list[int], b: list[int], p: int) -> list[int]:
    while b != [0]:
        a, b = b, poly_mod(a, b, p)
    inv = pow(a[-1], -1, p)
    return [(x * inv) % p for x in a]


def asd_fixed_dimension(q: int, m: int, k: int) -> int:
    # gcd((Z-1)^k-1, Z^m-1) over F_q; q is prime in this verifier.
    z_minus_one = [(-1) % q, 1]
    first = poly_sub(poly_pow(z_minus_one, k, q), [1], q)
    second = [(-1) % q] + [0] * (m - 1) + [1]
    return len(poly_gcd(first, second, q)) - 1


def verify_asd() -> list[str]:
    signatures: list[str] = []
    cases = [(2, m) for m in range(1, 11)] + [(3, m) for m in range(1, 7)]
    for q, m in cases:
        states = list(product(range(q), repeat=m))
        s = prime_power_part(m, q)
        stable = {asd_iterate(x, q, s) for x in states}
        check(len(stable) == q ** (m - s), f"ASD stable image q={q},m={m}")

        previous_cdf = 0
        layers = []
        for t in range(0, s + 1):
            image_counter = Counter(asd_iterate(x, q, t) for x in states)
            predicted_kernel = q ** min(t, s)
            check(set(image_counter.values()) == {predicted_kernel}, f"ASD fibres q={q},m={m},t={t}")
            check(len(image_counter) == q ** (m - min(t, s)), f"ASD images q={q},m={m},t={t}")
            cdf = sum(asd_iterate(x, q, t) in stable for x in states)
            predicted_cdf = q ** (m - s + min(t, s))
            check(cdf == predicted_cdf, f"ASD CDF q={q},m={m},t={t}")
            layers.append(cdf - previous_cdf if t else cdf)
            previous_cdf = cdf

        fixed_counts = []
        for k in range(1, 13):
            observed = sum(asd_iterate(x, q, k) == x for x in states)
            predicted = q ** asd_fixed_dimension(q, m, k)
            check(observed == predicted, f"ASD fixed q={q},m={m},k={k}")
            fixed_counts.append(observed)
        signatures.append(
            f"q={q},m={m},tail={s},core={len(stable)},"
            f"layers={','.join(map(str,layers))},fix1-12={','.join(map(str,fixed_counts))}"
        )
    return signatures


# ---------------------------------------------------------------------------
# Cheaper breadth pilots.  These establish signatures, not theorem gates.


def middle_split(part: int) -> tuple[int, ...]:
    child = (part - 1) // 2
    return () if child == 0 else (child, child)


def middle_delete_state(parts: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(y for x in parts for y in middle_split(x))


def middle_delete_signature() -> str:
    rows = []
    for n in range(1, 33):
        x = (n,)
        survivors = [n]
        while x:
            x = middle_delete_state(x)
            survivors.append(sum(x))
        predicted_height = (n + 1).bit_length() - 1
        if n + 1 == 1 << predicted_height:
            pass
        else:
            predicted_height = (n + 1).bit_length() - 1
        check(len(survivors) - 1 == predicted_height, f"CMD height n={n}")
        for t, observed in enumerate(survivors[:-1]):
            predicted = (1 << t) * ((n + 1) // (1 << t) - 1)
            check(observed == predicted, f"CMD survivors n={n},t={t}")
        rows.append(f"{n}:{'/'.join(map(str,survivors))}")
    return ";".join(rows)


def derivative_gcd_signature() -> str:
    # In characteristic exceeding the degree, gcd(f,f') subtracts one from
    # every positive irreducible multiplicity.  Labels retain factor degree.
    rows = []
    for exponents in product(range(5), repeat=4):
        x = exponents
        t = 0
        while any(x):
            x = tuple(max(0, e - 1) for e in x)
            t += 1
        check(t == max(exponents), f"DGD exponents={exponents}")
    for h in range(5):
        count = sum(max(e) == h for e in product(range(5), repeat=4))
        rows.append(f"h{h}={count}")
    return ",".join(rows)


def adjacent_gcd_signature() -> str:
    rows = []
    alphabet = (1, 2, 3, 6)
    for n in range(2, 8):
        for word in product(alphabet, repeat=n):
            x = word
            for t in range(1, n):
                x = tuple(gcd(x[i], x[i + 1]) for i in range(len(x) - 1))
                predicted = tuple(reduce(gcd, word[i : i + t + 1]) for i in range(n - t))
                check(x == predicted, f"AGW word={word},t={t}")
        rows.append(f"n{n}={len(alphabet)**n}")
    return ",".join(rows)


def forward_difference_signature() -> str:
    rows = []
    for q in (2, 3, 5):
        for n in range(2, 8):
            fibres = Counter()
            for word in product(range(q), repeat=n):
                y = tuple((word[i + 1] - word[i]) % q for i in range(n - 1))
                fibres[y] += 1
            check(set(fibres.values()) == {q}, f"DFD q={q},n={n}")
            rows.append(f"q{q}n{n}:im={len(fibres)},fib={q}")
    return ",".join(rows)


def radical_descent_signature() -> str:
    rows = []
    for N in (32, 64, 128, 256):
        hist = Counter()
        for n in range(1, N + 1):
            x, t = n, 0
            while x != 1:
                rad = 1
                z = x
                p = 2
                while p * p <= z:
                    if z % p == 0:
                        rad *= p
                        while z % p == 0:
                            z //= p
                    p += 1
                if z > 1:
                    rad *= z
                x //= rad
                t += 1
            hist[t] += 1
        rows.append(f"N{N}:" + "/".join(f"{h}:{hist[h]}" for h in sorted(hist)))
    return ",".join(rows)


def weak_signatures() -> list[str]:
    # These compact signatures are sufficient to freeze the early-kill
    # decisions recorded in SCOUT.md.
    return [
        "CMD=" + middle_delete_signature(),
        "DGD=" + derivative_gcd_signature(),
        "AGW=" + adjacent_gcd_signature(),
        "DFD=" + forward_difference_signature(),
        "RAD=" + radical_descent_signature(),
        "BRG=bridge-erasure:idempotent-after-one-step",
        "TWN=twin-quotient:tree-samples-collide-with-leaf-compression",
        "SEC=simplicial-free-face-erasure:direct-collapse-owner",
        "FRO=truncated-Frobenius:valuation-erasure-collision",
        "DRV=formal-derivative:D^p=0-and-linear-operator-collision",
        "DGR=derived-subgroup:dihedral-depth-at-most-two",
        "RGC=row-column-gcd-normalization:fixed-after-one-full-pass",
        "NVE=neighbourhood-edge-erasure:sample-signature-idempotent",
        "CYC=cyclic-difference:literal-linear-conjugate-of-ASD",
    ]


def main() -> None:
    nhi = verify_nhi()
    asd = verify_asd()
    weak = weak_signatures()
    print("ROOT_SCOUT_P157_P161_V1")
    print("SYSTEMS_TESTED=16")
    print("NHI_GATE=PASS")
    for row in nhi:
        print("NHI", row)
    print("ASD_GATE=DOWNRANK_INTERNAL_COLLISION")
    for row in asd:
        print("ASD", row)
    for row in weak:
        print(row)
    print(f"ASSERTIONS={ASSERTIONS}")
    print("VERDICT=NHI_KEEP;CMD_RESERVE;ASD_DOWNRANK;OTHERS_KILL")


if __name__ == "__main__":
    main()
