#!/usr/bin/env python3
"""Independent exact controls for diagonal-feedback commutator dynamics.

No scouting module or historical verifier is imported.  The program checks
literal arrows, every target fibre, labelled occupation refinements, image
membership and size, the complete depth-two graph, and a nonprime field.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
from math import factorial


ASSERTIONS = 0
DIGEST = sha256()


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


class FiniteField:
    """The prime fields used below and GF(4)=GF(2)[x]/(x^2+x+1)."""

    def __init__(self, order: int) -> None:
        check(order in (2, 3, 4, 5), f"unsupported field order {order}")
        self.order = order

    def sub(self, a: int, b: int) -> int:
        if self.order == 4:
            return a ^ b
        return (a - b) % self.order

    def mul(self, a: int, b: int) -> int:
        if self.order != 4:
            return (a * b) % self.order
        a0, a1 = a & 1, (a >> 1) & 1
        b0, b1 = b & 1, (b >> 1) & 1
        # x^2=x+1 in GF(2)[x]/(x^2+x+1).
        c0 = (a0 & b0) ^ (a1 & b1)
        c1 = (a0 & b1) ^ (a1 & b0) ^ (a1 & b1)
        return c0 | (c1 << 1)


def matrices(n: int, q: int):
    return tuple(product(range(q), repeat=n * n))


def update(a, n: int, field: FiniteField):
    diagonal = tuple(a[i * n + i] for i in range(n))
    return tuple(
        0
        if i == j
        else field.mul(field.sub(diagonal[i], diagonal[j]), a[i * n + j])
        for i in range(n)
        for j in range(n)
    )


def edge_list(n: int):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def support_mask(target, n: int) -> int:
    mask = 0
    for bit, (i, j) in enumerate(edge_list(n)):
        if target[i * n + j] != 0 or target[j * n + i] != 0:
            mask |= 1 << bit
    return mask


def proper(colors, mask: int, n: int) -> bool:
    return all(
        colors[i] != colors[j]
        for bit, (i, j) in enumerate(edge_list(n))
        if (mask >> bit) & 1
    )


def occupation(colors, q: int):
    return tuple(colors.count(alpha) for alpha in range(q))


def equal_ordered_pairs(colors) -> int:
    counts = Counter(colors)
    return sum(value * (value - 1) for value in counts.values())


def weak_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, parts - 1):
            yield (first,) + rest


def multinomial(parts) -> int:
    answer = factorial(sum(parts))
    for part in parts:
        answer //= factorial(part)
    return answer


def verify_box(n: int, q: int) -> None:
    field = FiniteField(q)
    states = matrices(n, q)
    state_set = set(states)
    zero = (0,) * (n * n)
    colors_list = tuple(product(range(q), repeat=n))

    indegree = Counter()
    marked_actual = defaultdict(Counter)
    depths = Counter()
    fixed = 0
    fixed_second = 0
    second_image = Counter()
    arrows = {}

    for source in states:
        target = update(source, n, field)
        check(target in state_set, f"closure n={n} q={q}")
        check(
            all(target[i * n + i] == 0 for i in range(n)),
            f"zero output diagonal n={n} q={q}",
        )
        second = update(target, n, field)
        check(second == zero, f"square zero n={n} q={q}")
        arrows[source] = target
        indegree[target] += 1
        second_image[second] += 1

        colors = tuple(source[i * n + i] for i in range(n))
        marked_actual[target][occupation(colors, q)] += 1
        if source == zero:
            depths[0] += 1
        elif target == zero:
            depths[1] += 1
        else:
            depths[2] += 1
        fixed += source == target
        fixed_second += source == second

        DIGEST.update(f"n={n};q={q};".encode("ascii"))
        DIGEST.update(repr(source).encode("ascii"))
        DIGEST.update(b"->")
        DIGEST.update(repr(target).encode("ascii"))

    check(second_image == Counter({zero: len(states)}), f"second image n={n} q={q}")
    check(fixed == 1, f"unique fixed point n={n} q={q}")
    check(fixed_second == 1, f"unique fixed point of square n={n} q={q}")

    predicted_by_support = {}
    colorable_by_support = {}
    for mask in range(1 << len(edge_list(n))):
        admissible = tuple(colors for colors in colors_list if proper(colors, mask, n))
        colorable_by_support[mask] = bool(admissible)
        predicted_by_support[mask] = sum(
            q ** equal_ordered_pairs(colors) for colors in admissible
        )

    support_fibre = {}
    for target in states:
        diagonal_zero = all(target[i * n + i] == 0 for i in range(n))
        mask = support_mask(target, n)
        predicted_marked = Counter()
        if diagonal_zero:
            for colors in colors_list:
                if proper(colors, mask, n):
                    predicted_marked[occupation(colors, q)] += (
                        q ** equal_ordered_pairs(colors)
                    )
        predicted = sum(predicted_marked.values())
        observed = indegree.get(target, 0)
        check(observed == predicted, f"target fibre n={n} q={q} target={target}")
        check(
            marked_actual.get(target, Counter()) == predicted_marked,
            f"marked target fibre n={n} q={q} target={target}",
        )
        check(
            (observed > 0) == (diagonal_zero and colorable_by_support[mask]),
            f"image membership n={n} q={q} target={target}",
        )
        if diagonal_zero:
            check(
                predicted == predicted_by_support[mask],
                f"support-only fibre n={n} q={q} target={target}",
            )
            previous = support_fibre.setdefault(mask, observed)
            check(previous == observed, f"support consistency n={n} q={q}")

    actual_support_census = Counter(support_mask(target, n) for target in indegree)
    predicted_image = 0
    for mask in range(1 << len(edge_list(n))):
        edge_count = mask.bit_count()
        expected_targets = (q * q - 1) ** edge_count if colorable_by_support[mask] else 0
        check(
            actual_support_census.get(mask, 0) == expected_targets,
            f"support census n={n} q={q} mask={mask}",
        )
        predicted_image += expected_targets
    check(len(indegree) == predicted_image, f"image formula n={n} q={q}")

    kappa = sum(
        multinomial(parts) * q ** sum(part * (part - 1) for part in parts)
        for parts in weak_compositions(n, q)
    )
    check(indegree[zero] == kappa, f"kernel formula n={n} q={q}")
    check(
        depths == Counter({0: 1, 1: kappa - 1, 2: len(states) - kappa}),
        f"depth layers n={n} q={q}",
    )
    check(
        sum(indegree[target] for target in indegree if target != zero)
        == len(states) - kappa,
        f"branched depth-two mass n={n} q={q}",
    )
    maximum = max(indegree.values())
    check(maximum == kappa, f"zero maximum n={n} q={q}")
    check(
        sum(value == maximum for value in indegree.values()) == 1,
        f"unique zero maximum n={n} q={q}",
    )

    fibre_hist = Counter(indegree.values())
    fibre_hist[0] = len(states) - len(indegree)
    height = max(depths)
    print(
        f"BOX n={n} q={q} S={len(states)} I={len(indegree)} F={fixed} "
        f"H={height} kappa={kappa} max_fibre={maximum} "
        f"fibres={tuple(sorted(fibre_hist.items()))} "
        f"depths={tuple(sorted(depths.items()))}"
    )


def main() -> None:
    print("P175_DIAGONAL_FEEDBACK_COMMUTATOR")
    print("external=HOLD_EXTERNAL computation=falsification_not_proof")
    boxes = (
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 2),
        (2, 3),
        (2, 4),
        (2, 5),
        (3, 2),
        (3, 3),
        (3, 4),
        (4, 2),
    )
    for n, q in boxes:
        verify_box(n, q)
    print(f"EDGE_DIGEST={DIGEST.hexdigest()}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()

