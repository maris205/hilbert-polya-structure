#!/usr/bin/env python3
"""Exact finite-box controls for P193 mutual-best block refinement.

The script uses only the Python standard library.  Its default run exhausts
every permutation through S_9.  The resulting checks are regression and
counterexample pressure; the manuscript proofs are independent of them.
"""

from __future__ import annotations

import argparse
import hashlib
from collections import Counter
from functools import lru_cache
from itertools import permutations
from math import factorial


ASSERTIONS = 0


def require(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def block_intervals(p: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Return half-open intervals of the direct-sum indecomposable blocks."""
    start = 0
    maximum = 0
    answer = []
    for end, value in enumerate(p, 1):
        maximum = max(maximum, value)
        if maximum == end:
            answer.append((start, end))
            start = end
    return tuple(answer)


def component_sizes(p: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(end - start for start, end in block_intervals(p))


def standardize(word: tuple[int, ...]) -> tuple[int, ...]:
    rank = {value: index + 1 for index, value in enumerate(sorted(word))}
    return tuple(rank[value] for value in word)


def literal_active_pairs(p: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Mutually nominated visible inversions, with zero-based positions."""
    active = []
    for left, value in enumerate(p):
        candidates = [right for right in range(left + 1, len(p))
                      if p[right] < value]
        if not candidates:
            continue
        right = min(candidates, key=lambda position: p[position])
        earliest = next(position for position in range(right)
                        if p[position] > p[right])
        if earliest == left:
            active.append((left, right))
    occupied = [position for pair in active for position in pair]
    require(len(occupied) == len(set(occupied)), "active pairs are disjoint")
    return tuple(active)


def block_active_pairs(p: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    answer = []
    for start, end in block_intervals(p):
        if end - start > 1:
            minimum_position = min(range(start, end), key=lambda i: p[i])
            answer.append((start, minimum_position))
    return tuple(answer)


def swap_pairs(p: tuple[int, ...], pairs: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    result = list(p)
    for left, right in pairs:
        result[left], result[right] = result[right], result[left]
    return tuple(result)


def literal_update(p: tuple[int, ...]) -> tuple[int, ...]:
    return swap_pairs(p, literal_active_pairs(p))


def block_update(p: tuple[int, ...]) -> tuple[int, ...]:
    return swap_pairs(p, block_active_pairs(p))


@lru_cache(maxsize=None)
def recursive_height(p: tuple[int, ...]) -> int:
    """The pointwise selection-decomposition height from the paper."""
    if len(p) <= 1:
        return 0
    blocks = block_intervals(p)
    if len(blocks) > 1:
        return max(recursive_height(standardize(p[start:end]))
                   for start, end in blocks)
    image = block_update(p)
    if image[0] != 1:
        raise AssertionError("indecomposable image does not begin with one")
    gamma = tuple(value - 1 for value in image[1:])
    return 1 + recursive_height(gamma)


def orbit_tail(p: tuple[int, ...]) -> int:
    identity = tuple(range(1, len(p) + 1))
    state = p
    seen = set()
    steps = 0
    while state != identity:
        require(state not in seen, "nontrivial directed cycle")
        seen.add(state)
        state = block_update(state)
        steps += 1
        require(steps <= max(0, len(p) - 1), "sharp tail upper bound")
    return steps


def fibre_formula(target: tuple[int, ...]) -> int:
    sizes = component_sizes(target)
    if not sizes or sizes[0] != 1:
        return 0
    answer = sizes[-1]
    for j in range(1, len(sizes)):
        if sizes[j] == 1:
            answer *= 1 + sizes[j - 1]
    return answer


def inverse_series(b: list[int], degree: int) -> list[int]:
    """Coefficients of 1/(1-B), truncated at x^degree."""
    a = [0] * (degree + 1)
    a[0] = 1
    for n in range(1, degree + 1):
        a[n] = sum(b[k] * a[n - k] for k in range(1, n + 1))
    return a


def next_b_series(a: list[int], b: list[int], degree: int) -> list[int]:
    """B_next = x + x^2 A B'."""
    answer = [0] * (degree + 1)
    if degree >= 1:
        answer[1] = 1
    for n in range(2, degree + 1):
        total = 0
        for u in range(n - 1):
            derivative_degree = n - 2 - u
            total += a[u] * (derivative_degree + 1) * b[derivative_degree + 1]
        answer[n] = total
    return answer


def encode_transition(digest: "hashlib._Hash", n: int,
                      source: tuple[int, ...], target: tuple[int, ...]) -> None:
    digest.update(n.to_bytes(2, "big"))
    digest.update(bytes(source))
    digest.update(bytes(target))


def exhaustive_boxes(max_n: int):
    transition_digest = hashlib.sha256()
    depth_tables: dict[int, Counter[int]] = {}
    indecomposable_depth_tables: dict[int, Counter[int]] = {}
    rows = []
    total_transitions = 0

    for n in range(1, max_n + 1):
        states = list(permutations(range(1, n + 1)))
        fibres: Counter[tuple[int, ...]] = Counter()
        depths: Counter[int] = Counter()
        indecomposable_depths: Counter[int] = Counter()
        core_parent_counts: Counter[tuple[int, ...]] = Counter()
        fixed = 0

        for source in states:
            literal_pairs = literal_active_pairs(source)
            structural_pairs = block_active_pairs(source)
            require(literal_pairs == structural_pairs,
                    f"literal/block active-pair mismatch at n={n}, source={source}")
            literal_target = swap_pairs(source, literal_pairs)
            structural_target = block_update(source)
            require(literal_target == structural_target,
                    f"literal/block update mismatch at n={n}, source={source}")
            encode_transition(transition_digest, n, source, literal_target)
            total_transitions += 1
            fibres[literal_target] += 1

            blocks_before = len(block_intervals(source))
            blocks_after = len(block_intervals(literal_target))
            if source == literal_target:
                fixed += 1
                require(source == tuple(range(1, n + 1)), "nonidentity fixed point")
            else:
                require(blocks_after > blocks_before,
                        "direct-sum component count did not increase")

            height = recursive_height(source)
            tail = orbit_tail(source)
            require(height == tail,
                    f"recursive clock mismatch at n={n}, source={source}")
            depths[tail] += 1

            if len(block_intervals(source)) == 1:
                indecomposable_depths[tail] += 1
                if n > 1:
                    require(literal_target[0] == 1,
                            "indecomposable image lacks leading singleton")
                    gamma = tuple(value - 1 for value in literal_target[1:])
                    core_parent_counts[gamma] += 1

        require(fixed == 1, f"fixed count at n={n}")
        maximum_tail = max(depths)
        deepest = depths[maximum_tail]
        require(maximum_tail == n - 1, f"maximum tail at n={n}")
        require(deepest == factorial(n - 1), f"deepest count at n={n}")

        if n > 1:
            for gamma in permutations(range(1, n)):
                expected = component_sizes(gamma)[-1]
                require(core_parent_counts[gamma] == expected,
                        f"indecomposable-parent lemma at n={n}, gamma={gamma}")

        mass = 0
        image_count = 0
        maximum_fibre = 0
        maximum_targets = []
        for target in states:
            actual = fibres[target]
            predicted = fibre_formula(target)
            require(actual == predicted,
                    f"target fibre mismatch at n={n}, target={target}")
            in_image = target[0] == 1
            require((actual > 0) == in_image,
                    f"image criterion at n={n}, target={target}")
            mass += predicted
            image_count += actual > 0
            if actual > maximum_fibre:
                maximum_fibre = actual
                maximum_targets = [target]
            elif actual == maximum_fibre:
                maximum_targets.append(target)

        identity = tuple(range(1, n + 1))
        require(mass == factorial(n), f"fibre mass at n={n}")
        require(image_count == factorial(n - 1), f"image size at n={n}")
        require(maximum_fibre == 2 ** (n - 1), f"maximum fibre at n={n}")
        require(maximum_targets == [identity], f"unique fibre maximizer at n={n}")

        depth_tables[n] = depths
        indecomposable_depth_tables[n] = indecomposable_depths
        depth_string = ",".join(str(depths[t]) for t in range(maximum_tail + 1))
        row = (n, factorial(n), image_count, maximum_tail, deepest,
               maximum_fibre, depth_string)
        rows.append(row)

    b = [0] * (max_n + 1)
    b[1] = 1
    for t in range(max_n):
        a = inverse_series(b, max_n)
        for n in range(1, max_n + 1):
            actual_all = sum(count for depth, count in depth_tables[n].items()
                             if depth <= t)
            actual_ind = sum(count for depth, count
                             in indecomposable_depth_tables[n].items()
                             if depth <= t)
            require(a[n] == actual_all,
                    f"A_t coefficient mismatch at t={t}, n={n}")
            require(b[n] == actual_ind,
                    f"B_t coefficient mismatch at t={t}, n={n}")
        b = next_b_series(a, b, max_n)

    return rows, total_transitions, transition_digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=9)
    args = parser.parse_args()
    if not 1 <= args.max_n <= 9:
        raise SystemExit("--max-n must lie between 1 and 9")

    rows, transitions, digest = exhaustive_boxes(args.max_n)
    print("P193 exact author control")
    for n, states, image, maximum_tail, deepest, maximum_fibre, depths in rows:
        print(f"n={n} states={states} image={image} max_tail={maximum_tail} "
              f"deepest={deepest} max_fibre={maximum_fibre} depths={depths}")
    print(f"complete_range=1..{args.max_n}")
    print(f"transitions={transitions}")
    print(f"assertions={ASSERTIONS}")
    print(f"transition_digest={digest}")
    print("finite_checks_are_not_proof_or_novelty=true")
    print("status=PASS")


if __name__ == "__main__":
    main()
