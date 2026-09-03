#!/usr/bin/env python3
"""Independent hostile-review verifier for P175 over prime fields.

The implementation enumerates matrices as flat tuples, constructs the
feedback commutator literally, and derives the comparison value by a
separate graph-colouring loop.  It imports no author or scouting code.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from math import factorial


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def matrices(n: int, q: int):
    return product(range(q), repeat=n * n)


def phi(matrix, n: int, q: int):
    diagonal = tuple(matrix[i * n + i] for i in range(n))
    answer = []
    for i in range(n):
        for j in range(n):
            answer.append(((diagonal[i] - diagonal[j]) * matrix[i * n + j]) % q)
    return tuple(answer)


def support_edges(target, n: int):
    return frozenset(
        (i, j) for i in range(n) for j in range(i + 1, n)
        if target[i * n + j] or target[j * n + i]
    )


def occupation(colouring, q: int):
    counts = [0] * q
    for colour in colouring:
        counts[colour] += 1
    return tuple(counts)


def colour_fibre(target, n: int, q: int):
    if any(target[i * n + i] for i in range(n)):
        return 0, Counter()
    edges = support_edges(target, n)
    total = 0
    marked = Counter()
    for colouring in product(range(q), repeat=n):
        if any(colouring[i] == colouring[j] for i, j in edges):
            continue
        profile = occupation(colouring, q)
        free = sum(count * (count - 1) for count in profile)
        weight = q ** free
        total += weight
        marked[profile] += weight
    return total, marked


def multinomial(parts) -> int:
    total = sum(parts)
    answer = factorial(total)
    for part in parts:
        answer //= factorial(part)
    return answer


def compositions(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, length - 1):
            yield (first,) + rest


def predicted_kernel(n: int, q: int) -> int:
    return sum(
        multinomial(profile)
        * q ** sum(count * (count - 1) for count in profile)
        for profile in compositions(n, q)
    )


def graph_colourable(mask: int, n: int, q: int) -> bool:
    edges = tuple(
        (i, j) for index, (i, j) in enumerate(
            (pair for i in range(n) for pair in ((i, j) for j in range(i + 1, n)))
        ) if (mask >> index) & 1
    )
    return any(
        all(colouring[i] != colouring[j] for i, j in edges)
        for colouring in product(range(q), repeat=n)
    )


def predicted_image(n: int, q: int) -> int:
    edge_count = n * (n - 1) // 2
    answer = 0
    for mask in range(1 << edge_count):
        if graph_colourable(mask, n, q):
            answer += (q * q - 1) ** mask.bit_count()
    return answer


def audit_box(n: int, q: int) -> None:
    zero = (0,) * (n * n)
    fibres = Counter()
    marked_actual = defaultdict(Counter)
    states = q ** (n * n)

    for source in matrices(n, q):
        target = phi(source, n, q)
        fibres[target] += 1
        profile = occupation(tuple(source[i * n + i] for i in range(n)), q)
        marked_actual[target][profile] += 1
        check(phi(target, n, q) == zero, f"square zero n={n} q={q}")

    maximum = fibres[zero]
    maximizers = []
    for target in matrices(n, q):
        expected, marked_expected = colour_fibre(target, n, q)
        check(fibres[target] == expected, f"every target n={n} q={q} B={target}")
        check(marked_actual[target] == marked_expected,
              f"occupation mark n={n} q={q} B={target}")
        if fibres[target] == maximum:
            maximizers.append(target)
        has_zero_diagonal = all(target[i * n + i] == 0 for i in range(n))
        colourable = expected > 0 if has_zero_diagonal else False
        check((target in fibres) == (has_zero_diagonal and colourable),
              f"image criterion n={n} q={q} B={target}")

    check(maximizers == [zero], f"unique maximum n={n} q={q}")
    check(maximum == predicted_kernel(n, q), f"kernel formula n={n} q={q}")
    check(len(fibres) == predicted_image(n, q), f"image graph sum n={n} q={q}")
    check(sum(fibres.values()) == states, f"fibre mass n={n} q={q}")
    check(sum(count for target, count in fibres.items() if target != zero)
          == states - maximum, f"depth-two mass n={n} q={q}")
    check((states - maximum == 0) == (n == 1), f"sharp height n={n} q={q}")
    print(f"n={n} q={q} states={states} image={len(fibres)} kernel={maximum} PASS")


def main() -> None:
    print("P175 HOSTILE REVIEW A INDEPENDENT CONTROL")
    print("STATUS HOLD_EXTERNAL")
    for n, q in ((1, 2), (1, 3), (1, 5), (2, 2), (2, 3), (2, 5),
                 (3, 2), (3, 3), (4, 2)):
        audit_box(n, q)
    print(f"ASSERTIONS {ASSERTIONS}")
    print("RESULT PASS")


if __name__ == "__main__":
    main()
