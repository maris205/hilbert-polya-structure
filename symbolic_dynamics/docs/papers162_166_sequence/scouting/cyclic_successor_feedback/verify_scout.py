#!/usr/bin/env python3
"""Independent exhaustive audit for cyclic successor-feedback (CSF).

This file intentionally imports no project code.  It checks the literal q-ary
map against independently implemented formulae for the first mask fibre, the
binary Rule-34 tail, cyclic-gap inverse polynomials, depths, rooted functional
graph cells, periods, and zeta exponents.
"""

from collections import Counter, defaultdict
from itertools import product
from math import comb, gcd


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def csf(word, q):
    n = len(word)
    return tuple(int((word[(i + 1) % n] - word[i]) % q == 1)
                 for i in range(n))


def binary_tail(bits):
    n = len(bits)
    return tuple((1 - bits[i]) * bits[(i + 1) % n] for i in range(n))


def shift(bits, steps=1):
    n = len(bits)
    steps %= n
    return bits[steps:] + bits[:steps]


def is_binary(word):
    return all(x in (0, 1) for x in word)


def is_independent(word):
    return is_binary(word) and all(not (word[i] and word[(i + 1) % len(word)])
                                   for i in range(len(word)))


def epsilon(n, q):
    return q - 1 if n % q == 0 else -1


def first_fibre(n, q, weight):
    m = n - weight
    return (q - 1) ** m + epsilon(n, q) * ((-1) ** m)


def poly_mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def cyclic_gaps(target):
    ones = [i for i, x in enumerate(target) if x]
    check(bool(ones), "cyclic_gaps called at zero")
    n = len(target)
    if len(ones) == 1:
        return (n,)
    return tuple((ones[(j + 1) % len(ones)] - ones[j]) % n
                 for j in range(len(ones)))


def gap_polynomial(target):
    """Coefficient r counts binary b of weight r with U(b)=target."""
    check(is_independent(target) and any(target), "bad nonzero target")
    out = [1]
    for gap in cyclic_gaps(target):
        check(gap >= 2, "independent target has short gap")
        out = poly_mul(out, [0] + [1] * (gap - 1))
    return out


def poly_eval(coefficients, x):
    return sum(a * (x ** i) for i, a in enumerate(coefficients))


def second_fibre(target, q):
    n = len(target)
    e = epsilon(n, q)
    if not is_independent(target):
        return 0
    if not any(target):
        return (q - 1) ** n + 1 + e * (((-1) ** n) + 1)
    p = gap_polynomial(target)
    # Integer form of (q-1)^n P(1/(q-1)) + e(-1)^n P(-1).
    main = sum(a * ((q - 1) ** (n - r)) for r, a in enumerate(p))
    return main + e * ((-1) ** n) * poly_eval(p, -1)


def binary_preimage_count(target):
    if not is_independent(target):
        return 0
    if not any(target):
        return 2
    return poly_eval(gap_polynomial(target), 1)


def independent_coefficients(n):
    """Number of labelled cyclic independent sets at each cardinality."""
    return tuple((n * comb(n - r, r)) // (n - r)
                 for r in range(n // 2 + 1))


def lucas(n):
    if n == 0:
        return 2
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    primes = 0
    p = 2
    value = n
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def exact_period_points(d):
    return sum(mobius(d // e) * lucas(e) for e in divisors(d))


def depth(word, q):
    if is_independent(word):
        return 0
    first = csf(word, q)
    if is_independent(first):
        return 1
    return 2


def orbit_representative(target):
    return min(shift(target, j) for j in range(len(target)))


def orbit_length(target):
    for d in divisors(len(target)):
        if shift(target, d) == target:
            return d
    raise AssertionError("no rotation period")


def exhaustive_box(n, q):
    zero = (0,) * n
    all_binary = list(product((0, 1), repeat=n))
    core = [b for b in all_binary if is_independent(b)]
    first_counts = Counter()
    second_counts = Counter()
    third_counts = Counter()
    fourth_counts = Counter()
    wrap_counts = Counter()
    depths = Counter()
    root_layers = Counter()
    root_binary_layers = Counter()
    component_layers = Counter()
    fixed_direct = 0
    states = q ** n

    for word in product(range(q), repeat=n):
        b = csf(word, q)
        c = csf(b, q)
        d3 = csf(c, q)
        d4 = csf(d3, q)
        check(is_binary(b), f"nonbinary first image n={n} q={q}")
        check(c == binary_tail(b), f"tail identity n={n} q={q} word={word}")
        check(is_independent(c), f"non-independent second image n={n} q={q}")
        check(csf(c, q) == shift(c), f"core shift n={n} q={q} c={c}")
        first_counts[b] += 1
        second_counts[c] += 1
        third_counts[d3] += 1
        fourth_counts[d4] += 1
        wrap_counts[shift(c, n)] += 1
        dep = depth(word, q)
        depths[dep] += 1
        root = word if dep == 0 else (b if dep == 1 else c)
        check(is_independent(root), f"bad recurrent root n={n} q={q}")
        root_layers[(root, dep)] += 1
        root_binary_layers[(root, dep, is_binary(word))] += 1
        component_layers[(orbit_representative(root), dep)] += 1
        fixed_direct += int(csf(word, q) == word)

    # First image, exact support holes, and all target fibres.
    support_expected = 2 ** n - (n if n % q == 0 else 1)
    check(len(first_counts) == support_expected,
          f"first image size n={n} q={q}")
    for b in all_binary:
        expected = first_fibre(n, q, sum(b))
        check(first_counts[b] == expected,
              f"first fibre n={n} q={q} b={b}")
        if n % q == 0:
            check((expected == 0) == (sum(b) == n - 1),
                  f"q|n hole n={n} q={q} b={b}")
        else:
            check((expected == 0) == (sum(b) == n),
                  f"q!|n hole n={n} q={q} b={b}")

    # Stable image and every-target fibres at all representative times.
    check(set(second_counts) == set(core), f"second image n={n} q={q}")
    check(set(third_counts) == set(core), f"third image n={n} q={q}")
    check(set(fourth_counts) == set(core), f"fourth image n={n} q={q}")
    check(set(wrap_counts) == set(core), f"wrapped image n={n} q={q}")
    for target in all_binary:
        expected = second_fibre(target, q)
        check(second_counts[target] == expected,
              f"two-step fibre n={n} q={q} c={target}")
        check(third_counts[target] == expected,
              f"three-step fibre n={n} q={q} c={target}")
        check(fourth_counts[target] == expected,
              f"four-step fibre n={n} q={q} c={target}")
        check(wrap_counts[target] == expected,
              f"(n+2)-step fibre n={n} q={q} c={target}")

    # Depth census and exact sharpness.
    coeff = independent_coefficients(n)
    check(sum(coeff) == lucas(n), f"Lucas core n={n}")
    cdf1 = sum(coeff[r] * first_fibre(n, q, r)
               for r in range(len(coeff)))
    expected_depths = Counter({0: lucas(n), 1: cdf1 - lucas(n),
                               2: states - cdf1})
    check(depths == expected_depths, f"depth census n={n} q={q}")
    check(depths[2] > 0, f"height not sharp n={n} q={q}")
    if n % q == 0:
        witness = (1,) * n
    else:
        witness = (1, 1) + (0,) * (n - 2)
    check(first_counts[witness] > 0 and not is_independent(witness),
          f"depth-two witness n={n} q={q}")

    # The complete rooted-cell description at each recurrent vertex.
    for target in core:
        k = sum(target)
        k_first = first_fibre(n, q, k)
        b_count = binary_preimage_count(target)
        f_count = second_fibre(target, q)
        check(root_layers[(target, 0)] == 1,
              f"root layer0 n={n} q={q} c={target}")
        check(root_layers[(target, 1)] == k_first - 1,
              f"root layer1 n={n} q={q} c={target}")
        check(root_layers[(target, 2)] == f_count - k_first,
              f"root layer2 n={n} q={q} c={target}")
        check(root_binary_layers[(target, 1, True)] == b_count - 1,
              f"binary transient children n={n} q={q} c={target}")
        check(root_binary_layers[(target, 1, False)] == k_first - b_count,
              f"q-ary transient children n={n} q={q} c={target}")
        check(root_binary_layers[(target, 2, True)] == 0,
              f"binary depth-two source n={n} q={q} c={target}")
        check(root_binary_layers[(target, 2, False)] == f_count - k_first,
              f"nonbinary depth-two leaves n={n} q={q} c={target}")
        check(sum(root_layers[(target, j)] for j in range(3)) == f_count,
              f"rooted cell mass n={n} q={q} c={target}")

    # Rotation components and zeta data.
    orbits = defaultdict(list)
    for target in core:
        orbits[orbit_representative(target)].append(target)
    actual_cycle_lengths = Counter()
    for rep, orbit in orbits.items():
        d = orbit_length(rep)
        check(len(orbit) == d, f"orbit size n={n} rep={rep}")
        actual_cycle_lengths[d] += 1
        f_count = second_fibre(rep, q)
        k_first = first_fibre(n, q, sum(rep))
        check(component_layers[(rep, 0)] == d,
              f"component core n={n} q={q} rep={rep}")
        check(component_layers[(rep, 1)] == d * (k_first - 1),
              f"component depth1 n={n} q={q} rep={rep}")
        check(component_layers[(rep, 2)] == d * (f_count - k_first),
              f"component depth2 n={n} q={q} rep={rep}")
        check(sum(component_layers[(rep, j)] for j in range(3)) == d * f_count,
              f"component mass n={n} q={q} rep={rep}")
    for d in divisors(n):
        expected_cycles = exact_period_points(d) // d
        check(actual_cycle_lengths[d] == expected_cycles,
              f"cycle count n={n} d={d}")
        fixed_m = sum(length * count for length, count in actual_cycle_lengths.items()
                      if d % length == 0)
        check(fixed_m == lucas(gcd(n, d)), f"Fix(T^{d}) n={n}")
    check(fixed_direct == 1, f"unique fixed point n={n} q={q}")
    check(sum(second_counts.values()) == states, f"second-fibre mass n={n} q={q}")
    check(sum(first_counts.values()) == states, f"first-fibre mass n={n} q={q}")

    cycle_text = ",".join(f"{d}:{actual_cycle_lengths[d]}"
                          for d in sorted(actual_cycle_lengths))
    return (f"BOX n={n} q={q} states={states} eps={epsilon(n,q)} "
            f"images={len(first_counts)}/{len(second_counts)} "
            f"depth={depths[0]},{depths[1]},{depths[2]} "
            f"cycles={cycle_text} maxF2={max(second_counts.values())}")


def gap_controls():
    lines = []
    for n in range(3, 16):
        grouped = defaultdict(Counter)
        for b in product((0, 1), repeat=n):
            grouped[binary_tail(b)][sum(b)] += 1
        core = [c for c in product((0, 1), repeat=n) if is_independent(c)]
        check(set(grouped) == set(core), f"gap support n={n}")
        for c in core:
            if any(c):
                p = gap_polynomial(c)
                actual = grouped[c]
                for r in range(n + 1):
                    expected = p[r] if r < len(p) else 0
                    check(actual[r] == expected,
                          f"gap coefficient n={n} c={c} r={r}")
                expected_alt = ((-1) ** sum(c)
                                if all(g % 2 == 0 for g in cyclic_gaps(c)) else 0)
                check(poly_eval(p, -1) == expected_alt,
                      f"alternating gap value n={n} c={c}")
            else:
                check(grouped[c] == Counter({0: 1, n: 1}),
                      f"zero binary preimages n={n}")
        lines.append(f"GAPS n={n} core={len(core)} masks={2**n}")
    return lines


def excluded_controls():
    # The advertised q>=3 domain is necessary: at q=2 the first q-ary state
    # is already binary, so the depth classification and rooted-cell formula
    # need not hold.  Record exact failures rather than silently extrapolate.
    n, q = 4, 2
    counts = Counter(csf(w, q) for w in product(range(q), repeat=n))
    check(len(counts) == 8, "q=2 first-image sentinel")
    predicted = 2 ** n - n
    check(len(counts) != predicted, "q=2 must violate q|n support law")
    # n=2 is excluded in the brief.  Some formulas happen to persist, but the
    # cycle graph has doubled neighbours; we do not claim that degenerate case.
    n, q = 2, 3
    core = [b for b in product((0, 1), repeat=n) if is_independent(b)]
    check(len(core) == 3, "n=2 doubled-edge core sentinel")
    return ["BOUNDARY q=2 n=4 image=8 (q>=3 essential)",
            "BOUNDARY n=2 q=3 core=3 (excluded doubled-neighbour cycle)"]


def selected_gap_lines():
    rows = []
    examples = [
        (6, (1, 0, 0, 1, 0, 0)),      # gaps (3,3)
        (7, (1, 0, 1, 0, 0, 0, 0)),   # gaps (2,5)
        (8, (1, 0, 0, 0, 1, 0, 0, 0)),  # gaps (4,4)
        (9, (1, 0, 1, 0, 0, 1, 0, 0, 0)),  # gaps (2,3,4)
    ]
    for n, c in examples:
        p = gap_polynomial(c)
        values = ",".join(f"q{q}={second_fibre(c,q)}" for q in (3, 4, 5))
        rows.append(f"EXAMPLE n={n} c={''.join(map(str,c))} "
                    f"gaps={','.join(map(str,cyclic_gaps(c)))} "
                    f"P={','.join(map(str,p))} {values}")
    return rows


def main():
    print("CSF INDEPENDENT EXACT AUDIT")
    print("domain n,q>=3; HOLD_EXTERNAL")
    boxes = ([(n, 3) for n in range(3, 10)]
             + [(n, 4) for n in range(3, 9)]
             + [(n, 5) for n in range(3, 8)]
             + [(n, 6) for n in range(3, 7)]
             + [(n, 7) for n in range(3, 7)])
    total_states = 0
    for n, q in boxes:
        print(exhaustive_box(n, q))
        total_states += q ** n
    for line in gap_controls():
        print(line)
    for line in selected_gap_lines():
        print(line)
    for line in excluded_controls():
        print(line)
    print(f"boxes={len(boxes)} literal_states={total_states}")
    print(f"assertions={ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
