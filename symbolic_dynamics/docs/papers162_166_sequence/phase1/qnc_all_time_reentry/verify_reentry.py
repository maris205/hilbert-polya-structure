#!/usr/bin/env python3
"""Independent exact pressure test for the QNC all-time re-entry contract.

The implementation starts from the literal map on p Z / p^e Z.  It imports
neither an earlier QNC verifier nor a formula table from the scouting record.
All arithmetic is integer arithmetic from the Python standard library.
"""

from collections import Counter


ASSERTIONS = 0


def require(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def valuation(residue, p, exponent):
    """p-adic valuation of a residue modulo p**exponent, clipped at exponent."""
    residue %= p**exponent
    if residue == 0:
        return exponent
    value = 0
    while residue % p == 0:
        residue //= p
        value += 1
    return value


def literal_map(x, p, e):
    return (x * (x + p)) % (p**e)


def iterate(x, t, p, e):
    for _ in range(t):
        x = literal_map(x, p, e)
    return x


def p_recurrence(u, t, p, modulus):
    """P_t(u), reduced only after each exact recurrence step."""
    if t == 0:
        return u % modulus
    value = (u * (u + 1)) % modulus
    for s in range(1, t):
        value = (value + (p**s) * value * value) % modulus
    return value


def b_transport(a, t, p, modulus):
    """B_t(a)=phi_{t-1}...phi_1(a); B_1 is the identity."""
    value = a % modulus
    for s in range(1, t):
        value = (value + (p**s) * value * value) % modulus
    return value


def koenigs_chart(x, p, e, extra_factors=0):
    """Finite reduction of x product_j (1+F^j(x)/p) modulo p^e."""
    modulus = p**e
    value = x % modulus
    orbit = x % modulus
    # e factors already include every factor capable of changing x modulo p^e.
    for _ in range(e + extra_factors):
        require(orbit % p == 0, "Koenigs quotient is integral")
        value = (value * (1 + orbit // p)) % modulus
        orbit = literal_map(orbit, p, e)
    return value


def expected_spectrum(p, e, t):
    """Counter fibre_size -> number of codomain targets for 1<=t<=e-1."""
    carrier_size = p ** (e - 1)
    k = e - t - 1
    if k == 0:
        positive = Counter({p**t: 1})
    else:
        positive = Counter({p ** (t + k // 2): 1})
        for r in range((k - 1) // 2 + 1):
            multiplicity = (p - 1) * p ** (k - 2 * r - 1) // 2
            positive[2 * p ** (t + r)] += multiplicity
    positive[0] = carrier_size - sum(positive.values())
    return positive


def verify_full_carrier(p, e):
    modulus = p**e
    carrier = list(range(0, modulus, p))
    size = p ** (e - 1)
    require(len(carrier) == size, "carrier cardinality")

    # Pointwise temporal boundary: zero is the only cycle and e-1 is sharp.
    depths = []
    for x in carrier:
        seen = set()
        y = x
        depth = 0
        while y != 0:
            require(y not in seen, "nonzero cycle")
            seen.add(y)
            y = literal_map(y, p, e)
            depth += 1
            require(depth <= e - 1, "global absorption bound")
        depths.append(depth)
    require(max(depths) == e - 1, "sharp global height")
    require(depths.count(0) == 1, "unique recurrent state")

    maps = []
    current = {x: x for x in carrier}
    for t in range(e + 2):
        if t:
            current = {x: literal_map(y, p, e) for x, y in current.items()}
        maps.append(current)

    # t=0 is identity, not a k=e-1 instance of the quadratic contract.
    fibres0 = Counter(maps[0].values())
    for y in carrier:
        require(fibres0[y] == 1, "t=0 identity fibre")

    for t in range(1, e):
        k = e - t - 1
        reduced_modulus = p**k
        fibres = Counter(maps[t].values())

        # Literal iterate identity, recurrence factorization, and source lifts.
        for x in carrier:
            u = x // p
            rhs = (p ** (t + 1) * p_recurrence(u, t, p, reduced_modulus)) % modulus
            require(maps[t][x] == rhs, "literal iterate recurrence")
            first = (u * (u + 1)) % reduced_modulus
            require(
                p_recurrence(u, t, p, reduced_modulus)
                == b_transport(first, t, p, reduced_modulus),
                "P_t=B_t o P_1",
            )

        # Each near-identity factor and their composition is a permutation.
        for s in range(1, t):
            factor_values = [
                (a + (p**s) * a * a) % reduced_modulus
                for a in range(reduced_modulus)
            ]
            require(len(set(factor_values)) == reduced_modulus, "phi_s bijective")
        transported = [
            b_transport(a, t, p, reduced_modulus)
            for a in range(reduced_modulus)
        ]
        require(len(set(transported)) == reduced_modulus, "B_t bijective")
        inverse = {b: a for a, b in enumerate(transported)}

        # Independently enumerate every square-root count modulo p^k.
        square_counts = Counter(
            (z * z) % reduced_modulus for z in range(reduced_modulus)
        )
        for y in carrier:
            if y % (p ** (t + 1)):
                predicted = 0
            else:
                b = (y // (p ** (t + 1))) % reduced_modulus
                a = inverse[b]
                delta = (1 + 4 * a) % reduced_modulus
                predicted = (p**t) * square_counts[delta]
            require(fibres[y] == predicted, "every-target all-time fibre")

        actual_spectrum = Counter(fibres[y] for y in carrier)
        require(actual_spectrum == expected_spectrum(p, e, t), "complete spectrum")
        require(sum(actual_spectrum.values()) == size, "spectrum target mass")
        require(
            sum(fibre_size * multiplicity for fibre_size, multiplicity in actual_spectrum.items())
            == size,
            "spectrum source mass",
        )

        if k == 0:
            require(set(fibres) == {0}, "k=0 sole image target")
            require(fibres[0] == p**t == size, "k=0 whole-carrier fibre")
        else:
            image_formula = 1 + (p - 1) * sum(
                p ** (k - 2 * r - 1) for r in range((k - 1) // 2 + 1)
            ) // 2
            require(len(fibres) == image_formula, "image-size formula")
            exceptional_size = p ** (t + k // 2)
            require(actual_spectrum[exceptional_size] == 1, "unique discriminant-zero target")

    # The map is already zero at t=e-1 and remains zero thereafter.  The
    # p^t formula must not be extrapolated beyond that first constant time.
    for t in range(e - 1, e + 2):
        fibres = Counter(maps[t].values())
        require(set(fibres) == {0}, "post-threshold constant image")
        require(fibres[0] == size, "post-threshold whole-carrier fibre")

    return size


def verify_inner_ball(p, e):
    modulus = p**e
    inner = list(range(0, modulus, p**2))
    size = p ** max(0, e - 2)
    require(len(inner) == size, "inner-ball cardinality")

    chart = {x: koenigs_chart(x, p, e) for x in inner}
    require(set(chart.values()) == set(inner), "Koenigs chart is onto inner ball")
    for x in inner:
        require(koenigs_chart(x, p, e, 2) == chart[x], "finite product stabilizes")
        require(
            chart[literal_map(x, p, e)] == (p * chart[x]) % modulus,
            "Koenigs conjugacy",
        )
        require(valuation(chart[x], p, e) == valuation(x, p, e), "chart preserves valuation")

    for x in inner:
        for y in inner:
            require(
                valuation(chart[x] - chart[y], p, e)
                == valuation(x - y, p, e),
                "Koenigs isometry",
            )

    for t in range(e + 2):
        fibres = Counter(iterate(x, t, p, e) for x in inner)
        threshold = min(e, t + 2)
        predicted_size = p ** min(t, max(0, e - 2))
        for y in inner:
            reachable = valuation(y, p, e) >= threshold
            require(
                fibres[y] == (predicted_size if reachable else 0),
                "inner-ball uniform all-time fibre",
            )
        expected_image_size = p ** max(0, e - threshold)
        require(len(fibres) == expected_image_size, "inner-ball image size")

    return size


def main():
    full_boxes = (
        [(3, e) for e in range(2, 9)]
        + [(5, e) for e in range(2, 7)]
        + [(7, e) for e in range(2, 6)]
        + [(11, e) for e in range(2, 5)]
    )
    summaries = []
    for p, e in full_boxes:
        full_size = verify_full_carrier(p, e)
        inner_size = verify_inner_ball(p, e)
        summaries.append(f"p={p},e={e},carrier={full_size},inner={inner_size}")

    print("QNC_ALL_TIME_REENTRY_INDEPENDENT")
    print("BOXES=" + ";".join(summaries))
    print("BOUNDARIES=t0_identity,k0,e2,post_threshold,zero,nondivisible,inner_zero")
    print("CHECKS=literal_iterate,B_transport,target_fibres,spectrum,mass,Koenigs,isometry")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
