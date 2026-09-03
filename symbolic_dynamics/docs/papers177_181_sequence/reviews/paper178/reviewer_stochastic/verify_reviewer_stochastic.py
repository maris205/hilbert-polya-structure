#!/usr/bin/env python3
"""Hostile exact audit for P178, written independently of author code.

Functions on F_p are represented by coefficients in the falling-binomial
basis, never by their tables of values.  In these coordinates evaluation at
zero is the zeroth coefficient and translation is obtained from Vandermonde's
identity.  A separate GF(4) table audit guards the manuscript's prime-only
scope.  Standard-library exact arithmetic only; no paper or scouting module
is imported.
"""

from collections import Counter
from hashlib import sha256
from itertools import product
from math import comb


ASSERTIONS = 0
EDGE_HASH = sha256()


def check(statement, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(label)


def mmul(left, right, p):
    if not left or not right:
        return []
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right))) % p
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def madd(left, right, p):
    return [
        [(left[i][j] + right[i][j]) % p for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def mscale(scale, matrix, p):
    return [[scale * entry % p for entry in row] for row in matrix]


def mpow(matrix, exponent, p):
    n = len(matrix)
    answer = [[int(i == j) for j in range(n)] for i in range(n)]
    base = [row[:] for row in matrix]
    while exponent:
        if exponent & 1:
            answer = mmul(answer, base, p)
        base = mmul(base, base, p)
        exponent //= 2
    return answer


def rank_mod(matrix, p):
    if not matrix:
        return 0
    work = [[entry % p for entry in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((r for r in range(row, len(work)) if work[r][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], -1, p)
        work[row] = [entry * inverse % p for entry in work[row]]
        for r in range(len(work)):
            if r != row and work[r][column]:
                multiplier = work[r][column]
                work[r] = [
                    (x - multiplier * y) % p for x, y in zip(work[r], work[row])
                ]
        row += 1
        if row == len(work):
            break
    return row


def d_matrix(p, direction):
    """Matrix of tau_direction-I in binomial coefficient coordinates."""
    return [
        [
            (comb(direction, j - k) if j > k else 0) % p
            for j in range(p)
        ]
        for k in range(p)
    ]


def directed_difference(coefficients, direction, p):
    return tuple(
        sum(
            comb(direction, j - k) * coefficients[j]
            for j in range(k + 1, p)
        )
        % p
        for k in range(p)
    )


def feedback(coefficients, p):
    # binom(0,j)=0 for j>0, so f(0) is exactly coefficient zero.
    return directed_difference(coefficients, coefficients[0], p)


def fixed_unit_power(coefficients, time):
    return tuple(coefficients[time:]) + (0,) * time


def layer_member(coefficients, time):
    return all(entry == 0 for entry in coefficients[len(coefficients) - time :])


def compact(counter):
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def jordan_blocks(p):
    blocks = {
        size: (p - 1) ** 2 * p ** (p - size - 1)
        for size in range(1, p)
    }
    blocks[p] = p - 1
    return blocks


def exhaustive_prime(p):
    states = tuple(product(range(p), repeat=p))
    zero = (0,) * p
    arrows = {}
    for source in states:
        target = feedback(source, p)
        arrows[source] = target
        EDGE_HASH.update(f"{p}:{source}>{target}\n".encode("ascii"))
        check(len(target) == p, f"closure p={p}")

    endpoints = {source: source for source in states}
    images = []
    zero_fibres = []
    layers = []
    for time in range(p + 1):
        fibre = Counter(endpoints.values())
        layer = {fixed_unit_power(source, time) for source in states}
        images.append(len(fibre))
        zero_fibres.append(fibre[zero])
        layers.append(layer)
        check(set(fibre) == layer, f"image flag p={p} t={time}")
        check(len(layer) == p ** (p - time), f"flag dimension p={p} t={time}")
        for target in states:
            if time == 0:
                expected = 1
            elif target == zero:
                expected = p**p - (p ** (p - time) - 1) * (p - 1) ** time
            elif layer_member(target, time):
                expected = (p - 1) ** time
            else:
                expected = 0
            check(fibre[target] == expected, f"fibre p={p} t={time} g={target}")
        check(sum(fibre.values()) == p**p, f"mass p={p} t={time}")
        if time < p:
            endpoints = {source: arrows[target] for source, target in endpoints.items()}

    # The trajectory itself must recover every nonzero anchor word.
    lifted = [Counter() for _ in range(p + 1)]
    for source in states:
        current = source
        word = []
        for time in range(1, p + 1):
            word.append(current[0])
            current = arrows[current]
            if current != zero:
                lifted[time][(current, tuple(word))] += 1
                check(all(word), f"zero letter before nonzero endpoint p={p} t={time}")
    for time in range(1, p):
        expected_keys = 0
        for target in layers[time]:
            if target == zero:
                continue
            for word in product(range(1, p), repeat=time):
                expected_keys += 1
                check(
                    lifted[time][(target, word)] == 1,
                    f"anchored history p={p} t={time}",
                )
        check(len(lifted[time]) == expected_keys, f"extra history p={p} t={time}")

    depths = Counter()
    for source in states:
        current = source
        depth = 0
        while current != zero:
            current = arrows[current]
            depth += 1
            check(depth <= p, f"clock overflow p={p}")
        depths[depth] += 1
    expected_depths = Counter({0: 1})
    for depth in range(1, p + 1):
        expected_depths[depth] = (p - 1) ** (depth - 1) * (
            p ** (p - depth) + p - 2
        )
    check(depths == expected_depths, f"depth census p={p}")

    witness = (1,) * p
    current = witness
    directions = []
    for _ in range(p):
        directions.append(current[0])
        current = arrows[current]
    check(directions == [1] * p, f"sharp anchors p={p}")
    check(current == zero, f"sharp endpoint p={p}")

    blocks = jordan_blocks(p)
    check(sum(s * count for s, count in blocks.items()) == p**p - 1, f"J dim p={p}")
    for time in range(p + 1):
        nil_rank = sum(max(size - time, 0) * count for size, count in blocks.items())
        check(nil_rank == images[time] - 1, f"J rank p={p} t={time}")
    # P^p=P^(p+1), with a singleton image, directly certifies the rank-one
    # recurrent projector used in the proof.
    check(images[p] == 1, f"rank-one terminal image p={p}")
    check(all(arrows[endpoints[source]] == endpoints[source] for source in states), f"Pp idempotent p={p}")

    return images, zero_fibres, depths, blocks


def algebraic_prime(p):
    identity = [[int(i == j) for j in range(p)] for i in range(p)]
    nilpotent = [[int(j == i + 1) for j in range(p)] for i in range(p)]
    one_plus_n = madd(identity, nilpotent, p)

    for direction in range(1, p):
        direct = d_matrix(p, direction)
        translated = mpow(one_plus_n, direction, p)
        translated_minus_identity = madd(translated, mscale(-1, identity, p), p)
        check(direct == translated_minus_identity, f"translation factor p={p} a={direction}")

        unit = [[0] * p for _ in range(p)]
        power = identity
        for exponent in range(1, direction + 1):
            unit = madd(unit, mscale(comb(direction, exponent), power, p), p)
            power = mmul(power, nilpotent, p)
        check(rank_mod(unit, p) == p, f"unit invertibility p={p} a={direction}")
        check(mmul(nilpotent, unit, p) == direct, f"NU factor p={p} a={direction}")

        for layer in range(p):
            dimension = p - layer
            restricted = [row[:dimension] for row in direct[: dimension - 1]]
            check(
                rank_mod(restricted, p) == dimension - 1,
                f"layer surjection p={p} a={direction} i={layer}",
            )
            anchored = restricted + [[1] + [0] * (dimension - 1)]
            check(
                rank_mod(anchored, p) == dimension,
                f"anchor bijection p={p} a={direction} i={layer}",
            )

            # In the small boxes, enumerate the entire augmented map rather
            # than trusting rank alone.
            if p <= 5:
                seen = Counter()
                for coefficients in product(range(p), repeat=dimension):
                    image = tuple(
                        sum(restricted[row][column] * coefficients[column] for column in range(dimension)) % p
                        for row in range(dimension - 1)
                    )
                    seen[(image, coefficients[0])] += 1
                check(len(seen) == p**dimension, f"anchor onto p={p} a={direction} i={layer}")
                check(all(count == 1 for count in seen.values()), f"anchor unique p={p} a={direction} i={layer}")

    # The fixed unit difference is one nilpotent block, not just a matrix of
    # the correct rank at a few powers.
    for time in range(p + 1):
        power = mpow(nilpotent, time, p)
        check(rank_mod(power, p) == p - time, f"single N-block p={p} t={time}")


def extension_scope_guard():
    # GF(4) is represented additively as F_2^2.  Multiplication is irrelevant
    # to this literal map: x+f(0) and subtraction are both XOR operations.
    q = 4
    states = tuple(product(range(q), repeat=q))
    zero = (0,) * q

    def update(table):
        anchor = table[0]
        return tuple(table[x ^ anchor] ^ table[x] for x in range(q))

    arrows = {state: update(state) for state in states}
    endpoints = {state: state for state in states}
    profile = []
    zero_profile = []
    for time in range(4):
        fibres = Counter(endpoints.values())
        profile.append(len(fibres))
        zero_profile.append(fibres[zero])
        if time < 3:
            endpoints = {source: arrows[target] for source, target in endpoints.items()}
    check(tuple(profile) == (256, 40, 4, 1), "GF4 image scope guard")
    check(tuple(zero_profile) == (1, 76, 184, 256), "GF4 zero-fibre scope guard")
    check(tuple(profile) != tuple(q ** (q - t) for t in range(4)), "prime formula must not extend to GF4")
    return profile, zero_profile


def main():
    print("P178_REVIEWER_STOCHASTIC")
    for p in (2, 3, 5):
        images, zeros, depths, blocks = exhaustive_prime(p)
        print(
            f"prime={p} states={p**p} images={'/'.join(map(str, images))} "
            f"zero_fibres={'/'.join(map(str, zeros))} depths={compact(depths)} "
            f"J0={compact(Counter(blocks))}"
        )
    algebra_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
    for p in algebra_primes:
        algebraic_prime(p)
    gf4_images, gf4_zeros = extension_scope_guard()
    print("algebraic_primes=" + ",".join(map(str, algebra_primes)) + " factor/anchor/Jordan=PASS")
    print(
        "GF4_SCOPE_GUARD images=" + "/".join(map(str, gf4_images))
        + " zero_fibres=" + "/".join(map(str, gf4_zeros))
        + " prime_tower_formula=FALSE_AS_REQUIRED"
    )
    print(f"ASSERTIONS={ASSERTIONS}")
    print(f"EDGE_SHA256={EDGE_HASH.hexdigest()}")
    print("RESULT=PASS")
    print("RELEASE_SENTINEL=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
