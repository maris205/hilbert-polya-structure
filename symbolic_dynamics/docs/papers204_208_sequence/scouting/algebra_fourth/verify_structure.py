#!/usr/bin/env python3
"""Author structural controls; independent code routes, not independent review."""

from collections import Counter, defaultdict
from itertools import product, permutations
from math import factorial
import json


checks = Counter()


def require(condition, key):
    checks[key] += 1
    assert condition, key


def ec_literal(a):
    return tuple(max(abs(u-v) for v in a) for u in a)


def ec_sources(b, bound):
    """Decode endpoint intervals and branch choices; no forward map calls."""
    width = max(b)
    if width == 0:
        return {tuple([c]*len(b)) for c in range(bound+1)}
    if 2*min(b) < width or b.count(width) < 2:
        return set()
    answer = set()
    for offset in range(bound-width+1):
        choices = [sorted({offset+u, offset+width-u}) for u in b]
        for candidate in product(*choices):
            if min(candidate) == offset and max(candidate) == offset+width:
                answer.add(candidate)
    return answer


def ec_formula(b, bound):
    width = max(b)
    if width == 0:
        return bound+1
    ends = b.count(width)
    if 2*min(b) < width or ends < 2:
        return 0
    middle = sum(2*u == width for u in b)
    return (bound-width+1)*(2**ends-2)*2**(len(b)-ends-middle)


def ec_depth(a):
    """Literal forward trajectory to the claimed absorber, not graph formulas."""
    depth = 0
    seen = set()
    while any(a):
        require(a not in seen, "EC_no_nonzero_cycle")
        seen.add(a)
        a = ec_literal(a)
        depth += 1
    return depth


def ec_boxes():
    reports = []
    for n in range(1, 6):
        for bound in range(6):
            carrier = list(product(range(bound+1), repeat=n))
            inverse = defaultdict(set)
            depths = Counter()
            for a in carrier:
                b = ec_literal(a)
                inverse[b].add(a)
                alpha, beta = min(a), max(a)
                require(b == tuple(max(u-alpha, beta-u) for u in a), "EC_endpoint_adapter")
                require(max(b)-min(b) <= (beta-alpha)//2, "EC_diameter_contraction")
                if alpha < beta:
                    require(len(set(b)) < len(set(a)), "EC_support_contraction")
                depths[ec_depth(a)] += 1
            for b in carrier:
                require(ec_sources(b, bound) == inverse[b], "EC_full_source_set")
                require(ec_formula(b, bound) == len(inverse[b]), "EC_fibre_formula")
            expected_height = 0 if bound == 0 else min(n, bound.bit_length()+1)
            require(max(depths) == expected_height, "EC_sharp_height")
            expected_image = 1 if n == 1 else 1+sum(
                (r//2+1)**n-(r//2)**n-n*(r//2)**(n-1)
                for r in range(1, bound+1))
            require(sum(bool(v) for v in inverse.values()) == expected_image, "EC_image_census")
            peak = max(map(len, inverse.values()))
            actual_maxima = {b for b, sources in inverse.items() if len(sources) == peak}
            if n == 1 or bound == 0:
                expected_maxima = {(0,)*n}
                expected_peak = bound+1
            elif (n, bound) == (2, 1):
                expected_maxima = {(0, 0), (1, 1)}
                expected_peak = 2
            else:
                expected_maxima = {(1,)*n}
                expected_peak = bound*(2**n-2)
            require(actual_maxima == expected_maxima and peak == expected_peak, "EC_all_extremizers")
            reports.append({"n": n, "bound": bound, "states": len(carrier),
                            "height": max(depths), "image": expected_image})
    bounds = [0, 1, 2, 3, 7, 8, 15, 16, 31, 32, 255, 256, 2**30-1, 2**30]
    for n in range(1, 34):
        for bound in bounds:
            height = 0 if bound == 0 else min(n, bound.bit_length()+1)
            if bound == 0:
                witness = (0,)*n
            elif n == 1:
                witness = (1,)
            else:
                support = [0]+[2**j for j in range(height-1)]
                witness = tuple(support+[0]*(n-height))
            require(len(witness) == n and max(witness) <= bound, "EC_witness_domain")
            require(ec_depth(witness) == height, "EC_large_symbolic_witness")
    return reports


def parking_literal(a):
    used = set()
    output = []
    for u in a:
        steps = 0
        while (u+steps) % len(a) in used:
            steps += 1
        used.add((u+steps) % len(a))
        output.append(steps)
    return tuple(output)


def parking_sources(b):
    n = len(b)
    result = set()
    for placement in permutations(range(n)):
        previous = set()
        valid = True
        for i, site in enumerate(placement):
            if any((site-j) % n not in previous for j in range(1, b[i]+1)):
                valid = False
                break
            previous.add(site)
        if valid:
            result.add(tuple((placement[i]-b[i]) % n for i in range(n)))
    return result


def rank_literal(a):
    return tuple(a[:i].count(a[i]) for i in range(len(a)))


def rank_sources(b):
    n = len(b)
    result = set()
    def extend(prefix, counts):
        i = len(prefix)
        if i == n:
            result.add(tuple(prefix))
            return
        for colour in range(n):
            if counts[colour] == b[i]:
                counts[colour] += 1
                extend(prefix+[colour], counts)
                counts[colour] -= 1
    extend([], [0]*n)
    return result


def rank_formula(b):
    n = len(b)
    counts = [0]*(n+1)
    value = 1
    for level in b:
        value *= n-counts[0] if level == 0 else counts[level-1]-counts[level]
        counts[level] += 1
        if value == 0:
            return 0
    return value


def rowword_is_tableau(b):
    rows = [[] for _ in b]
    for i, row in enumerate(b):
        rows[row].append(i)
    for row in range(len(b)-1):
        if len(rows[row]) < len(rows[row+1]):
            return False
        if any(rows[row][j] > u for j, u in enumerate(rows[row+1])):
            return False
    return True


def normalizer_boxes():
    reports = []
    involutions = [1, 1]
    for n in range(2, 6):
        involutions.append(involutions[-1]+(n-1)*involutions[-2])
    for n in range(1, 6):
        carrier = list(product(range(n), repeat=n))
        parking_inverse, rank_inverse = defaultdict(set), defaultdict(set)
        for a in carrier:
            parking_inverse[parking_literal(a)].add(a)
            rank_inverse[rank_literal(a)].add(a)
        for b in carrier:
            require(parking_sources(b) == parking_inverse[b], "CP_full_permutation_adapter")
            require(rank_sources(b) == rank_inverse[b], "OR_full_chain_decoder")
            require(rank_formula(b) == len(rank_inverse[b]), "OR_static_chain_count")
            lattice = rowword_is_tableau(b)
            require(bool(rank_inverse[b]) == lattice, "OR_image_SYT_rowwords")
            if lattice:
                column_word = tuple(sum(b[j] == b[i] for j in range(i)) for i in range(n))
                require(rowword_is_tableau(column_word), "OR_transposed_tableau")
                require(rank_literal(column_word) == b, "OR_transpose_involution")
            if all(b[i] <= i for i in range(n)):
                require(parking_literal(b) == tuple(i-b[i] for i in range(n)), "CP_complement_clock")
        require(sum(bool(x) for x in rank_inverse.values()) == involutions[n], "OR_classical_involution_census")
        maxima = {b for b, sources in parking_inverse.items() if len(sources) == factorial(n)}
        require(maxima == {(0,)*(n-1)+(j,) for j in range(n)}, "CP_all_maxima")
        reports.append({"n": n, "states": len(carrier), "OR_image": involutions[n],
                        "CP_image": factorial(n), "CP_maximum_targets": len(maxima)})
    return reports


def main():
    ec = ec_boxes()
    normalizers = normalizer_boxes()
    print(json.dumps({"status": "AUTHOR_STRUCTURAL_CHECKS_PASS_NOT_REVIEW",
                      "EC_boxes": ec, "normalizer_boxes": normalizers,
                      "checks": dict(sorted(checks.items())), "total_checks": sum(checks.values())},
                     sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
