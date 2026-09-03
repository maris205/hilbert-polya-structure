#!/usr/bin/env python3
"""Reviewer-B reconstruction for P177 using tuple/set coordinates.

This code was written from the literal update and theorem statements after
the Round-0 PDF was frozen.  It does not import or execute author code.
"""

from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, product


checks = 0


def insist(statement):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(f"review check {checks} failed")


def xor(a, b):
    return a.symmetric_difference(b)


def vectors(d):
    return tuple(product((0, 1), repeat=d))


def inner(a, x):
    return sum(u * v for u, v in zip(a, x)) % 2


def powerset(items):
    for size in range(len(items) + 1):
        for choice in combinations(items, size):
            yield frozenset(choice)


def formula(q, t, total_is_zero):
    N = q - 1
    sign = -1 if t % 2 else 1
    numerator = N**t + N * sign if total_is_zero else N**t - sign
    insist(numerator % q == 0)
    return numerator // q


def audit_dimension(d):
    all_vectors = vectors(d)
    zero = (0,) * d
    points = tuple(x for x in all_vectors if x != zero)
    forms = points
    E = frozenset(points)
    codes = {a: frozenset(x for x in points if inner(a, x)) for a in all_vectors}
    masks = {a: frozenset(x for x in points if not inner(a, x)) for a in forms}
    W = {codes[a] for a in all_vectors} | {xor(E, codes[a]) for a in all_vectors}
    q = 2**d
    N = q - 1

    insist(len(codes.values()) == q)
    insist(len(set(codes.values())) == q)
    insist(E not in set(codes.values()))
    insist(len(W) == 2 * q)
    for a in forms:
        insist(masks[a] == xor(E, codes[a]))
        insist(len(masks[a]) == 2 ** (d - 1) - 1)

    # Generate the increment subgroup without code coordinates.
    reached = {frozenset()}
    queue = deque(reached)
    while queue:
        state = queue.popleft()
        for mask in masks.values():
            target = xor(state, mask)
            if target not in reached:
                reached.add(target)
                queue.append(target)
    insist(reached == W)

    # Set-valued histories and the two TV distances.
    max_t = {2: 6, 3: 6, 4: 4, 5: 3}[d]
    for t in range(max_t + 1):
        sum_counts = Counter()
        endpoint_counts = Counter()
        for history in product(forms, repeat=t):
            total = zero
            endpoint = frozenset()
            for form in history:
                total = tuple(x ^ y for x, y in zip(total, form))
                endpoint = xor(endpoint, masks[form])
            sum_counts[total] += 1
            endpoint_counts[endpoint] += 1
            expected = codes[total]
            if t % 2:
                expected = xor(E, expected)
            insist(endpoint == expected)
        insist(sum(sum_counts.values()) == N**t)
        for total in all_vectors:
            expected_count = formula(q, t, total == zero)
            insist(sum_counts[total] == expected_count)
            endpoint = codes[total]
            if t % 2:
                endpoint = xor(E, endpoint)
            insist(endpoint_counts[endpoint] == expected_count)

        if t >= 1:
            probabilities = [Fraction(sum_counts[a], N**t) for a in all_vectors]
            phase_tv = sum(abs(p - Fraction(1, q)) for p in probabilities) / 2
            insist(phase_tv == Fraction(1, q * N ** (t - 1)))
            ordinary = (sum(abs(p - Fraction(1, 2 * q)) for p in probabilities)
                        + Fraction(1, 2)) / 2
            target = Fraction(1, 2) + Fraction(1, 2 * q) if t == 1 else Fraction(1, 2)
            insist(ordinary == target)

    # Full carrier components and character spectrum for tractable dimensions.
    if d <= 3:
        states = tuple(powerset(points))
        unseen = set(states)
        components = []
        while unseen:
            seed = next(iter(unseen))
            component = {seed}
            queue = deque([seed])
            while queue:
                state = queue.popleft()
                for mask in masks.values():
                    target = xor(state, mask)
                    if target not in component:
                        component.add(target)
                        queue.append(target)
            unseen -= component
            components.append(component)
        insist(len(components) == 2 ** (N - d - 1))
        for component in components:
            insist(len(component) == 2 * q)
            for state in component:
                neighbors = {xor(state, mask) for mask in masks.values()}
                insist(len(neighbors) == N)
                insist(neighbors <= component)
                insist(all((len(state) - len(target)) % 2 for target in neighbors))

        eigen_numerators = Counter()
        for S in states:
            numerator = sum(-1 if len(S & mask) % 2 else 1
                            for mask in masks.values())
            eigen_numerators[numerator] += 1
        K = 2 ** (N - d - 1)
        insist(eigen_numerators == Counter({N: K, -N: K, 1: N * K, -1: N * K}))

    insist(N + 1 == 2**d)
    insist((2**N) // (2 * (N + 1)) == 2 ** (N - d - 1))
    return q, N, 2 ** (N - d - 1)


def main():
    # Excluded d=1 boundary: the sole mask is empty and both subsets are fixed.
    point = (1,)
    mask = frozenset(x for x in (point,) if inner(point, x) == 0)
    insist(mask == frozenset())
    rows = [audit_dimension(d) for d in range(2, 6)]
    print("P177_HOSTILE_REVIEW_B_ROOT")
    for q, N, K in rows:
        print(f"q={q} degree={N} components={K}")
    print(f"ASSERTIONS={checks}")
    print("REPRESENTATION=tuple-vectors/frozenset-subsets/direct-history-products")
    print("RESULT=PASS")
    print("RELEASE_SENTINEL=REVIEW_ONLY/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
