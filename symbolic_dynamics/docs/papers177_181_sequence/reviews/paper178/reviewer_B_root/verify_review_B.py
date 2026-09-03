#!/usr/bin/env python3
"""Independent integer-encoding review control for P178."""

from collections import Counter
from math import comb


assertions = 0


def ok(value):
    global assertions
    assertions += 1
    if not value:
        raise AssertionError(f"failed assertion {assertions}")


def digits(code, p):
    out = []
    for _ in range(p):
        out.append(code % p)
        code //= p
    return out


def encode(values, p):
    code = 0
    place = 1
    for value in values:
        code += value * place
        place *= p
    return code


def directed_difference(code, step, p):
    values = digits(code, p)
    return encode([(values[(x + step) % p] - values[x]) % p
                   for x in range(p)], p)


def feedback(code, p):
    return directed_difference(code, digits(code, p)[0], p)


def unit_layer(p, t):
    layer = set(range(p**p))
    for _ in range(t):
        layer = {directed_difference(code, 1, p) for code in layer}
    return layer


def literal_box(p):
    size = p**p
    arrows = [feedback(code, p) for code in range(size)]
    ok(all(0 <= target < size for target in arrows))
    endpoints = list(range(size))
    image_rows = []
    zero_rows = []
    for t in range(p + 1):
        fibres = Counter(endpoints)
        layer = unit_layer(p, t)
        ok(set(fibres) == layer)
        ok(len(layer) == p ** (p - t))
        image_rows.append(len(fibres))
        zero_rows.append(fibres[0])
        for target in range(size):
            if t == 0:
                expected = 1
            elif target == 0:
                expected = size - (p ** (p - t) - 1) * (p - 1) ** t
            elif target in layer:
                expected = (p - 1) ** t
            else:
                expected = 0
            ok(fibres[target] == expected)
        if t < p:
            endpoints = [arrows[target] for target in endpoints]

    depths = Counter()
    direction_words = {}
    for source in range(size):
        state = source
        word = []
        while state:
            word.append(digits(state, p)[0])
            next_state = arrows[state]
            if next_state:
                ok(word[-1] != 0)
            state = next_state
            ok(len(word) <= p)
        depths[len(word)] += 1
        direction_words[source] = tuple(word)
    expected_depths = Counter({0: 1})
    for d in range(1, p + 1):
        expected_depths[d] = (p - 1) ** (d - 1) * (p ** (p - d) + p - 2)
    ok(depths == expected_depths)

    # Direction word and final nonzero target uniquely identify a source.
    for t in range(1, p):
        seen = Counter()
        for source in range(size):
            target = source
            word = []
            for _ in range(t):
                word.append(digits(target, p)[0])
                target = arrows[target]
            if target:
                seen[(target, tuple(word))] += 1
        ok(all(count == 1 for count in seen.values()))
        ok(len(seen) == (p ** (p - t) - 1) * (p - 1) ** t)

    blocks = Counter({s: (p - 1) ** 2 * p ** (p - s - 1)
                      for s in range(1, p)})
    blocks[p] = p - 1
    ok(sum(s * count for s, count in blocks.items()) == size - 1)
    for t in range(p + 1):
        rank = sum(max(s - t, 0) * count for s, count in blocks.items())
        ok(rank == p ** (p - t) - 1)

    witness_values = [sum(comb(x, degree) for degree in range(p)) % p
                      for x in range(p)]
    witness = encode(witness_values, p)
    state = witness
    trace = []
    for _ in range(p):
        trace.append(digits(state, p)[0])
        state = arrows[state]
    ok(trace == [1] * p)
    ok(state == 0)
    return size, tuple(image_rows), tuple(zero_rows), tuple(sorted(depths.items()))


def matrix_rank(columns, p):
    if not columns:
        return 0
    a = [list(row) for row in zip(*columns)]
    row = 0
    for column in range(len(a[0])):
        pivot = next((r for r in range(row, len(a)) if a[r][column] % p), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][column] % p, -1, p)
        a[row] = [(value * inv) % p for value in a[row]]
        for r in range(len(a)):
            if r != row and a[r][column] % p:
                scale = a[r][column] % p
                a[r] = [(x - scale * y) % p for x, y in zip(a[r], a[row])]
        row += 1
    return row


def anchor_certificate(p):
    basis = [tuple(comb(x, degree) % p for x in range(p))
             for degree in range(p)]
    ok(matrix_rank(basis, p) == p)
    for step in range(1, p):
        for i in range(p):
            domain = basis[:p - i]
            images = [tuple((v[(x + step) % p] - v[x]) % p for x in range(p))
                      for v in domain]
            ok(matrix_rank(images, p) == p - i - 1)
            graph_columns = [image + (v[0],) for image, v in zip(images, domain)]
            ok(matrix_rank(graph_columns, p) == p - i)


def main():
    rows = [(p, literal_box(p)) for p in (2, 3, 5)]
    for p in (2, 3, 5, 7, 11, 13):
        anchor_certificate(p)
    print("P178_HOSTILE_REVIEW_B_ROOT")
    for p, (size, images, zeros, depths) in rows:
        print(f"p={p} states={size} images={images} zero_fibres={zeros} depths={depths}")
    print(f"ASSERTIONS={assertions}")
    print("REPRESENTATION=base-p integers/direct functional graph/augmented anchor rank")
    print("RESULT=PASS")
    print("RELEASE_SENTINEL=REVIEW_ONLY/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
