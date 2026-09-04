#!/usr/bin/env python3
"""Independent finite control for P194.

The script uses no scouting or prior-paper code.  It constructs the literal
word map, its complete functional graph on a fixed small grid, the type-A
crystal components, reverse-word RSK shapes, semistandard tableaux, standard
tableau counts, and the proposed inverse atlas by separate routines.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
from math import factorial


ASSERTIONS = 0
TRANSITIONS = 0
TARGETS = 0
COMPONENTS = 0
SSYT = 0
SYT_RECURRENCES = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def signature(word: tuple[int, ...], i: int) -> tuple[list[int], list[int]]:
    """Return unmatched minus and plus positions after deleting +- pairs."""
    unmatched_plus: list[int] = []
    unmatched_minus: list[int] = []
    for pos, letter in enumerate(word):
        if letter == i:
            unmatched_plus.append(pos)
        elif letter == i + 1:
            if unmatched_plus:
                unmatched_plus.pop()
            else:
                unmatched_minus.append(pos)
    return unmatched_minus, unmatched_plus


def e_op(word: tuple[int, ...], i: int) -> tuple[int, ...] | None:
    minus, _ = signature(word, i)
    if not minus:
        return None
    out = list(word)
    out[minus[-1]] = i
    return tuple(out)


def f_op(word: tuple[int, ...], i: int) -> tuple[int, ...] | None:
    _, plus = signature(word, i)
    if not plus:
        return None
    out = list(word)
    out[plus[0]] = i + 1
    return tuple(out)


def update(word: tuple[int, ...], k: int) -> tuple[int, ...]:
    for i in range(1, k):
        raised = e_op(word, i)
        if raised is not None:
            return raised
    return word


def is_highest(word: tuple[int, ...], k: int) -> bool:
    return all(e_op(word, i) is None for i in range(1, k))


def is_ballot(word: tuple[int, ...], k: int) -> bool:
    counts = [0] * (k + 1)
    for letter in word:
        counts[letter] += 1
        if any(counts[i] < counts[i + 1] for i in range(1, k)):
            return False
    return True


def rsk_shape(sequence: tuple[int, ...]) -> tuple[int, ...]:
    rows: list[list[int]] = []
    for value in sequence:
        carry = value
        row_index = 0
        while True:
            if row_index == len(rows):
                rows.append([carry])
                break
            row = rows[row_index]
            bump = next((j for j, entry in enumerate(row) if entry > carry), None)
            if bump is None:
                row.append(carry)
                break
            row[bump], carry = carry, row[bump]
            row_index += 1
    return tuple(len(row) for row in rows)


def crystal_shape(word: tuple[int, ...]) -> tuple[int, ...]:
    # The paper's tensor/signature convention corresponds to row insertion of
    # the reversed word.
    return rsk_shape(tuple(reversed(word)))


def partitions(total: int, max_part: int | None = None) -> list[tuple[int, ...]]:
    if total == 0:
        return [()]
    if max_part is None or max_part > total:
        max_part = total
    out: list[tuple[int, ...]] = []
    for first in range(max_part, 0, -1):
        for tail in partitions(total - first, first):
            out.append((first,) + tail)
    return out


def cells(shape: tuple[int, ...]) -> list[tuple[int, int]]:
    return [(r, c) for r, length in enumerate(shape) for c in range(length)]


def hook_lengths(shape: tuple[int, ...]) -> list[int]:
    out: list[int] = []
    for r, c in cells(shape):
        below = sum(1 for rr in range(r + 1, len(shape)) if shape[rr] > c)
        out.append(shape[r] - c + below)
    return out


def f_hook(shape: tuple[int, ...]) -> int:
    denominator = 1
    for hook in hook_lengths(shape):
        denominator *= hook
    return factorial(sum(shape)) // denominator


def syt_count_recursive(shape: tuple[int, ...], memo: dict[tuple[int, ...], int]) -> int:
    global SYT_RECURRENCES
    if shape in memo:
        return memo[shape]
    SYT_RECURRENCES += 1
    total = 0
    for r, length in enumerate(shape):
        if r + 1 == len(shape) or shape[r + 1] < length:
            reduced = list(shape)
            reduced[r] -= 1
            if reduced[r] == 0:
                reduced.pop(r)
            total += syt_count_recursive(tuple(reduced), memo)
    memo[shape] = total
    return total


def ssyt_depth_hist(shape: tuple[int, ...], k: int) -> Counter[int]:
    global SSYT
    order = cells(shape)
    values: dict[tuple[int, int], int] = {}
    baseline = sum((r + 1) * length for r, length in enumerate(shape))
    hist: Counter[int] = Counter()

    def visit(index: int, weight: int) -> None:
        global SSYT
        if index == len(order):
            depth = weight - baseline
            check(depth >= 0, f"negative tableau depth for {shape}, {k}")
            hist[depth] += 1
            SSYT += 1
            return
        r, c = order[index]
        lower = 1
        if c:
            lower = max(lower, values[(r, c - 1)])
        if r and c < shape[r - 1]:
            lower = max(lower, values[(r - 1, c)] + 1)
        for value in range(lower, k + 1):
            values[(r, c)] = value
            visit(index + 1, weight + value)
        values.pop((r, c), None)

    visit(0, 0)
    return hist


def multiply_one_minus(poly: list[int], exponent: int) -> list[int]:
    out = poly + [0] * exponent
    for degree, coefficient in enumerate(poly):
        out[degree + exponent] -= coefficient
    return out


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def exact_poly_division(numerator: list[int], denominator: list[int]) -> list[int]:
    numerator = trim(numerator[:])
    denominator = trim(denominator[:])
    check(denominator[0] == 1, "polynomial denominator must have constant one")
    quotient_degree = len(numerator) - len(denominator)
    check(quotient_degree >= 0, "negative quotient degree")
    quotient = [0] * (quotient_degree + 1)
    for degree in range(quotient_degree + 1):
        value = numerator[degree]
        for j in range(1, min(degree, len(denominator) - 1) + 1):
            value -= denominator[j] * quotient[degree - j]
        quotient[degree] = value
    reconstructed = [0] * (len(quotient) + len(denominator) - 1)
    for i, a in enumerate(quotient):
        for j, b in enumerate(denominator):
            reconstructed[i + j] += a * b
    check(trim(reconstructed) == trim(numerator), "non-exact principal specialization")
    return trim(quotient)


def principal_specialization(shape: tuple[int, ...], k: int) -> Counter[int]:
    numerator = [1]
    denominator = [1]
    for r, c in cells(shape):
        content = c - r
        hook = shape[r] - c + sum(
            1 for rr in range(r + 1, len(shape)) if shape[rr] > c
        )
        numerator = multiply_one_minus(numerator, k + content)
        denominator = multiply_one_minus(denominator, hook)
    quotient = exact_poly_division(numerator, denominator)
    return Counter({degree: coefficient for degree, coefficient in enumerate(quotient) if coefficient})


def hook_content_dimension(shape: tuple[int, ...], k: int) -> int:
    value = Fraction(1, 1)
    for r, c in cells(shape):
        hook = shape[r] - c + sum(
            1 for rr in range(r + 1, len(shape)) if shape[rr] > c
        )
        value *= Fraction(k + c - r, hook)
    check(value.denominator == 1, f"nonintegral hook-content value for {shape}, {k}")
    return value.numerator


def predicted_predecessors(target: tuple[int, ...], k: int) -> set[tuple[int, ...]]:
    out: set[tuple[int, ...]] = set()
    if is_highest(target, k):
        out.add(target)
    for i in range(1, k):
        source = f_op(target, i)
        if source is not None and all(e_op(source, j) is None for j in range(1, i)):
            out.add(source)
    return out


def depth_by_iteration(word: tuple[int, ...], k: int) -> tuple[int, tuple[int, ...]]:
    seen: set[tuple[int, ...]] = set()
    current = word
    depth = 0
    while True:
        check(current not in seen, f"nontrivial cycle from {word}")
        seen.add(current)
        nxt = update(current, k)
        if nxt == current:
            return depth, current
        check(sum(nxt) == sum(current) - 1, "raising step did not lower letter sum by one")
        current = nxt
        depth += 1


def stable_maximum_witness(k: int, surplus: int = 0) -> tuple[int, ...]:
    if k == 1:
        return (1,) * surplus
    lengths = [k - i for i in range(1, k + 1)]
    lengths[0] += surplus
    return tuple(letter for letter, length in enumerate(lengths, 1) for _ in range(length))


def verify_word_grid(digest) -> dict[str, int]:
    global TRANSITIONS, TARGETS, COMPONENTS
    totals = {
        "words": 0,
        "fixed": 0,
        "components": 0,
        "max_depth_sum": 0,
        "max_fibre": 0,
    }
    syt_memo: dict[tuple[int, ...], int] = {(): 1}

    for k in range(1, 5):
        for n in range(1, 8):
            universe = [tuple(word) for word in product(range(1, k + 1), repeat=n)]
            universe_set = set(universe)
            actual_predecessors: dict[tuple[int, ...], set[tuple[int, ...]]] = {
                word: set() for word in universe
            }
            depths: dict[tuple[int, ...], int] = {}
            endpoints: dict[tuple[int, ...], tuple[int, ...]] = {}
            shapes: dict[tuple[int, ...], tuple[int, ...]] = {}

            for word in universe:
                nxt = update(word, k)
                check(nxt in universe_set, "update left carrier")
                actual_predecessors[nxt].add(word)
                TRANSITIONS += 1
                TARGETS += 1
                depth, endpoint = depth_by_iteration(word, k)
                shape = crystal_shape(word)
                baseline = sum((i + 1) * part for i, part in enumerate(shape))
                check(depth == sum(word) - baseline, f"clock mismatch at {(n, k, word)}")
                check(is_highest(endpoint, k), "endpoint is not highest")
                check(is_highest(word, k) == is_ballot(word, k), "highest/ballot mismatch")
                depths[word] = depth
                endpoints[word] = endpoint
                shapes[word] = shape
                digest.update(f"W|{n}|{k}|{word}|{nxt}|{shape}|{depth}\n".encode())

            for target in universe:
                predicted = predicted_predecessors(target, k)
                check(predicted == actual_predecessors[target], f"fibre mismatch at {(n, k, target)}")
                check(len(predicted) <= k, "uniform fibre bound failed")
                for source in predicted:
                    check(update(source, k) == target, "listed predecessor maps elsewhere")
                digest.update(
                    f"P|{n}|{k}|{target}|{tuple(sorted(predicted))}\n".encode()
                )

            fixed_words = [word for word in universe if update(word, k) == word]
            max_depth = max(depths.values())
            deepest = [word for word in universe if depths[word] == max_depth]
            max_fibre = max(len(value) for value in actual_predecessors.values())
            check(max_depth == n * (k - 1), "sharp global depth failed")
            check(deepest == [(k,) * n], "deepest word is not unique k^n")

            expected_fixed = 0
            shape_tableau_hist: dict[tuple[int, ...], Counter[int]] = {}
            for shape in partitions(n):
                if len(shape) > k:
                    continue
                recursive = syt_count_recursive(shape, syt_memo)
                hook = f_hook(shape)
                check(recursive == hook, f"hook formula mismatch for {shape}")
                expected_fixed += hook
                ssyt_hist = ssyt_depth_hist(shape, k)
                product_hist = principal_specialization(shape, k)
                check(ssyt_hist == product_hist, f"Schur specialization mismatch for {shape}, {k}")
                check(sum(ssyt_hist.values()) == hook_content_dimension(shape, k), "hook-content mismatch")
                shape_tableau_hist[shape] = ssyt_hist
            check(len(fixed_words) == expected_fixed, "fixed/component census mismatch")

            unseen = set(universe)
            components_by_shape: Counter[tuple[int, ...]] = Counter()
            while unseen:
                start = min(unseen)
                queue = deque([start])
                component: set[tuple[int, ...]] = {start}
                unseen.remove(start)
                while queue:
                    word = queue.popleft()
                    for i in range(1, k):
                        for neighbor in (e_op(word, i), f_op(word, i)):
                            if neighbor is None:
                                continue
                            check(neighbor in universe_set, "crystal edge left carrier")
                            if neighbor not in component:
                                component.add(neighbor)
                                unseen.remove(neighbor)
                                queue.append(neighbor)
                component_shapes = {shapes[word] for word in component}
                check(len(component_shapes) == 1, "RSK shape changed inside crystal component")
                shape = next(iter(component_shapes))
                highest = [word for word in component if is_highest(word, k)]
                check(len(highest) == 1, "component lacks a unique highest word")
                content = Counter(highest[0])
                check(
                    all(content[i] == (shape[i - 1] if i <= len(shape) else 0) for i in range(1, k + 1)),
                    "highest content differs from shape",
                )
                component_hist = Counter(depths[word] for word in component)
                check(component_hist == shape_tableau_hist[shape], "component layer polynomial mismatch")
                components_by_shape[shape] += 1
                COMPONENTS += 1
            for shape, count in components_by_shape.items():
                check(count == f_hook(shape), f"shape multiplicity mismatch for {shape}")

            totals["words"] += len(universe)
            totals["fixed"] += len(fixed_words)
            totals["components"] += sum(components_by_shape.values())
            totals["max_depth_sum"] += max_depth
            totals["max_fibre"] = max(totals["max_fibre"], max_fibre)
            check(sum(len(v) for v in actual_predecessors.values()) == len(universe), "fibre mass failed")

    return totals


def verify_involution_census(digest) -> int:
    checked = 0
    for n in range(1, 9):
        involution_shapes: Counter[tuple[int, ...]] = Counter()
        for perm in permutations(range(1, n + 1)):
            inverse = [0] * n
            for position, value in enumerate(perm, 1):
                inverse[value - 1] = position
            if tuple(inverse) == perm:
                involution_shapes[rsk_shape(perm)] += 1
        for shape in partitions(n):
            check(involution_shapes[shape] == f_hook(shape), f"involution/SYT mismatch for {shape}")
        for k in range(1, n + 2):
            left = sum(count for shape, count in involution_shapes.items() if len(shape) <= k)
            right = sum(f_hook(shape) for shape in partitions(n) if len(shape) <= k)
            check(left == right, "bounded-height involution census mismatch")
        digest.update(f"I|{n}|{tuple(sorted(involution_shapes.items()))}\n".encode())
        checked += sum(involution_shapes.values())
    return checked


def verify_stable_fibre_witnesses(digest) -> int:
    checked = 0
    for k in range(1, 10):
        threshold = k * (k - 1) // 2
        for surplus in range(0, 4):
            if k == 1 and surplus == 0:
                continue
            highest = stable_maximum_witness(k, surplus)
            n = len(highest)
            check(n == threshold + surplus, "staircase witness has wrong length")
            check(is_highest(highest, k), "staircase witness is not highest")
            predicted = predicted_predecessors(highest, k)
            check(len(predicted) == k, f"stable maximum fibre failed for {(n, k)}")
            for source in predicted:
                check(update(source, k) == highest, "stable predecessor fails literally")
            digest.update(f"S|{n}|{k}|{highest}|{tuple(sorted(predicted))}\n".encode())
            checked += 1
    return checked


def main() -> None:
    digest = sha256()
    totals = verify_word_grid(digest)
    involutions = verify_involution_census(digest)
    stable = verify_stable_fibre_witnesses(digest)
    print("P194 least-raising crystal-word verifier")
    print("signature=i:+,i+1:-; delete +-; e=rightmost-unpaired-minus; f=leftmost-unpaired-plus")
    print("scheduler=least available raising colour")
    print("word_grid=k=1..4,n=1..7")
    print("involution_grid=n=1..8")
    print("stable_fibre_grid=k=1..9,surplus=0..3")
    print(f"words={totals['words']}")
    print(f"transitions={TRANSITIONS}")
    print(f"targets={TARGETS}")
    print(f"fixed_words={totals['fixed']}")
    print(f"crystal_components={COMPONENTS}")
    print(f"ssyt={SSYT}")
    print(f"syt_recurrence_states={SYT_RECURRENCES}")
    print(f"involutions={involutions}")
    print(f"stable_witnesses={stable}")
    print(f"largest_observed_fibre={totals['max_fibre']}")
    print(f"depth_maxima_checksum={totals['max_depth_sum']}")
    print(f"assertions={ASSERTIONS}")
    print(f"transition_digest={digest.hexdigest()}")
    print("status=PASS")


if __name__ == "__main__":
    main()
