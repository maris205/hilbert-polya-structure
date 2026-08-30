#!/usr/bin/env python3
"""Exact scout for simultaneous reversal of even record blocks."""

from collections import Counter
from itertools import permutations


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def record_blocks(permutation):
    if not permutation:
        return ()
    starts = []
    record = -1
    for index, value in enumerate(permutation):
        if value > record:
            starts.append(index)
            record = value
    starts.append(len(permutation))
    return tuple(
        permutation[starts[i] : starts[i + 1]] for i in range(len(starts) - 1)
    )


def phi(permutation):
    image = []
    for block in record_blocks(permutation):
        image.extend(reversed(block) if len(block) % 2 == 0 else block)
    return tuple(image)


def fixed_criterion(permutation):
    return all(len(block) % 2 for block in record_blocks(permutation))


def odd_double_factorial(n):
    if n <= 0:
        return 1
    result = 1
    for value in range(1, n + 1, 2):
        result *= value
    return result


def predicted_fixed(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return odd_double_factorial(n - 1) ** 2
    return odd_double_factorial(n) * odd_double_factorial(n - 2)


EXPECTED_LAYERS = {
    0: [1],
    1: [1],
    2: [1, 1],
    3: [3, 2, 1],
    4: [9, 7, 5, 3],
    5: [45, 33, 20, 14, 8],
    6: [225, 172, 128, 93, 63, 39],
    7: [1575, 1210, 783, 591, 425, 283, 173],
    8: [11025, 8522, 6462, 4878, 3640, 2804, 1822, 1167],
    9: [99225, 78623, 52942, 41238, 30973, 23297, 17843, 11436, 7303],
}


EXPECTED_MAX_INDEGREE = [1, 1, 2, 3, 6, 10, 19, 33, 61, 108]


def main():
    rows = []
    for n in range(10):
        depth = {}
        indegrees = Counter()
        fixed = 0
        layers = Counter()
        for permutation in permutations(range(n)):
            image = phi(permutation)
            indegrees[image] += 1
            check(tuple(sorted(image)) == tuple(range(n)), (n, permutation, "closure"))
            is_fixed = image == permutation
            check(is_fixed == fixed_criterion(permutation), (n, permutation, "fixed criterion"))
            if not is_fixed:
                check(image < permutation, (n, permutation, "strict lex drop"))
                check(image in depth, (n, permutation, "lex induction"))
                value = 1 + depth[image]
            else:
                value = 0
            check(value <= max(0, n - 1), (n, permutation, "depth", value))
            depth[permutation] = value
            layers[value] += 1
            fixed += is_fixed
        layer_list = [layers[i] for i in range(max(layers) + 1)]
        check(fixed == predicted_fixed(n), (n, "fixed", fixed))
        check(layer_list == EXPECTED_LAYERS[n], (n, "layers", layer_list))
        check(max(indegrees.values()) == EXPECTED_MAX_INDEGREE[n], (n, "max indegree"))
        expected_depth = 0 if n == 0 else n - 1
        check(max(layers) == expected_depth, (n, "sharp depth", max(layers)))
        if n >= 1:
            witness = tuple(range(1, n)) + (0,)
            check(depth[witness] == n - 1, (n, "witness", witness, depth[witness]))
        rows.append((n, len(depth), fixed, layer_list, max(indegrees.values())))

    print("even record-block reversal: exhaustive permutation census")
    print("n states fixed exact_depth_layers max_indegree")
    for row in rows:
        print(*row)
    print("fixed_formula even=((n-1)!!)^2; odd=n!!(n-2)!!")
    print("fixed_EGF sqrt((1+x)/(1-x))")
    print("sharp_witness (2,3,...,n,1)")
    print("ASSERTIONS", ASSERTIONS)


if __name__ == "__main__":
    main()
