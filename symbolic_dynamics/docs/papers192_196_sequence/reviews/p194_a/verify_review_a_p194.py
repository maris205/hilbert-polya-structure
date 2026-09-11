#!/usr/bin/env python3
"""Process-separated exact control for P194 hostile Review A.

This program imports no author module.  Its deliberately different routes are:

* e_i is found by strict prefix-balance record minima;
* f_i is found by a right-to-left matching scan;
* reverse-RSK shape is recovered from Greene's union-of-chains invariants;
* Schur specializations are computed by Jacobi--Trudi determinants; and
* f^lambda is computed by the Aitken determinant.

Finite controls are counterexample pressure, not proofs or novelty evidence.
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
GREENE_CALLS = 0
JT_CHECKS = 0
Q_ONE_CHECKS = 0
INVOLUTION_PERMUTATIONS_SCANNED = 0


def require(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def replace_letter(word: tuple[int, ...], position: int, value: int) -> tuple[int, ...]:
    return word[:position] + (value,) + word[position + 1 :]


def raising(word: tuple[int, ...], color: int) -> tuple[int, ...] | None:
    """e_color via the last strict prefix-balance record minimum."""
    balance = 0
    minimum = 0
    position: int | None = None
    for index, letter in enumerate(word):
        if letter == color:
            balance += 1
        elif letter == color + 1:
            balance -= 1
            if balance < minimum:
                minimum = balance
                position = index
    if position is None:
        return None
    return replace_letter(word, position, color)


def lowering(word: tuple[int, ...], color: int) -> tuple[int, ...] | None:
    """f_color via an independent right-to-left cancellation scan."""
    available_minuses = 0
    leftmost_unpaired_plus: int | None = None
    for index in range(len(word) - 1, -1, -1):
        letter = word[index]
        if letter == color + 1:
            available_minuses += 1
        elif letter == color:
            if available_minuses:
                available_minuses -= 1
            else:
                leftmost_unpaired_plus = index
    if leftmost_unpaired_plus is None:
        return None
    return replace_letter(word, leftmost_unpaired_plus, color + 1)


def scheduled_step(word: tuple[int, ...], alphabet: int) -> tuple[tuple[int, ...], int | None]:
    for color in range(1, alphabet):
        candidate = raising(word, color)
        if candidate is not None:
            return candidate, color
    return word, None


def is_highest(word: tuple[int, ...], alphabet: int) -> bool:
    return all(raising(word, color) is None for color in range(1, alphabet))


def is_ballot(word: tuple[int, ...], alphabet: int) -> bool:
    counts = [0] * (alphabet + 1)
    for letter in word:
        counts[letter] += 1
        for color in range(1, alphabet):
            if counts[color] < counts[color + 1]:
                return False
    return True


def greene_shape(sequence: tuple[int, ...]) -> tuple[int, ...]:
    """Row-insertion shape from Greene invariants, without inserting rows.

    For each r, dynamic programming finds the largest union of r weakly
    increasing subsequences.  A state is the sorted multiset of their tails;
    zero denotes an empty chain because all letters are positive.
    """
    global GREENE_CALLS
    GREENE_CALLS += 1
    size = len(sequence)
    sums = [0]
    for chain_count in range(1, size + 1):
        states: dict[tuple[int, ...], int] = {(0,) * chain_count: 0}
        for value in sequence:
            new_states = dict(states)
            for tails, used in states.items():
                for index, tail in enumerate(tails):
                    if tail <= value:
                        changed = list(tails)
                        changed[index] = value
                        changed.sort()
                        key = tuple(changed)
                        if used + 1 > new_states.get(key, -1):
                            new_states[key] = used + 1
            states = new_states
        sums.append(max(states.values()))
    rows = tuple(sums[r] - sums[r - 1] for r in range(1, len(sums)))
    rows = tuple(part for part in rows if part)
    require(sum(rows) == size, f"Greene invariants lost entries: {sequence}")
    require(all(rows[i] >= rows[i + 1] for i in range(len(rows) - 1)),
            f"Greene differences are not a partition: {sequence}, {rows}")
    return rows


def component_shape(word: tuple[int, ...]) -> tuple[int, ...]:
    return greene_shape(tuple(reversed(word)))


def partitions(total: int, ceiling: int | None = None):
    if total == 0:
        yield ()
        return
    if ceiling is None or ceiling > total:
        ceiling = total
    for first in range(ceiling, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def standard_tableaux_aitken(shape: tuple[int, ...]) -> int:
    """f^lambda = n! det(1/(lambda_i-i+j)!), with negative entries zero."""
    if not shape:
        return 1
    length = len(shape)
    determinant = Fraction(0, 1)
    for perm in permutations(range(length)):
        term = Fraction(permutation_sign(perm), 1)
        for row, column in enumerate(perm):
            argument = shape[row] - row + column
            if argument < 0:
                term = Fraction(0, 1)
                break
            term /= factorial(argument)
        determinant += term
    answer = factorial(sum(shape)) * determinant
    require(answer.denominator == 1 and answer >= 0,
            f"nonintegral Aitken value for {shape}: {answer}")
    return answer.numerator


def poly_trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(left: list[int], right: list[int], right_sign: int = 1) -> list[int]:
    out = [0] * max(len(left), len(right))
    for degree, coefficient in enumerate(left):
        out[degree] += coefficient
    for degree, coefficient in enumerate(right):
        out[degree] += right_sign * coefficient
    return poly_trim(out)


def poly_multiply(left: list[int], right: list[int]) -> list[int]:
    if left == [0] or right == [0]:
        return [0]
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return poly_trim(out)


def poly_shift(poly: list[int], amount: int) -> list[int]:
    if poly == [0]:
        return [0]
    return [0] * amount + poly


def one_minus(exponent: int) -> list[int]:
    require(exponent >= 1, f"nonpositive hook-content exponent {exponent}")
    out = [0] * (exponent + 1)
    out[0] = 1
    out[exponent] = -1
    return out


def complete_homogeneous(max_degree: int, alphabet: int) -> list[list[int]]:
    """h_r(1,q,...,q^(alphabet-1)) by its generating series."""
    table = [[1]] + [[0] for _ in range(max_degree)]
    for exponent in range(alphabet):
        for degree in range(1, max_degree + 1):
            table[degree] = poly_add(
                table[degree], poly_shift(table[degree - 1], exponent)
            )
    return table


def schur_jacobi_trudi(shape: tuple[int, ...], alphabet: int) -> list[int]:
    global JT_CHECKS
    JT_CHECKS += 1
    length = len(shape)
    maximum = max(shape[row] - row + column
                  for row in range(length) for column in range(length))
    h = complete_homogeneous(maximum, alphabet)
    determinant = [0]
    for perm in permutations(range(length)):
        term = [1]
        for row, column in enumerate(perm):
            index = shape[row] - row + column
            term = poly_multiply(term, [0] if index < 0 else h[index])
        determinant = poly_add(determinant, term, permutation_sign(perm))
    return determinant


def normalized_schur(shape: tuple[int, ...], alphabet: int) -> list[int]:
    raw = schur_jacobi_trudi(shape, alphabet)
    shift = sum(row * length for row, length in enumerate(shape))
    require(all(coefficient == 0 for coefficient in raw[:shift]),
            f"principal specialization has terms below n(lambda): {shape}")
    normalized = poly_trim(raw[shift:] or [0])
    require(all(coefficient >= 0 for coefficient in normalized),
            f"normalized Schur polynomial has a negative coefficient: {shape}")

    numerator = [1]
    denominator = [1]
    for row, row_length in enumerate(shape):
        for column in range(row_length):
            below = sum(other_length > column for other_length in shape[row + 1 :])
            hook = row_length - column + below
            numerator = poly_multiply(numerator, one_minus(alphabet + column - row))
            denominator = poly_multiply(denominator, one_minus(hook))
    require(poly_multiply(normalized, denominator) == numerator,
            f"hook-content q-product mismatch for {shape}, k={alphabet}")
    return normalized


def hook_content_at_one(shape: tuple[int, ...], alphabet: int) -> int:
    global Q_ONE_CHECKS
    Q_ONE_CHECKS += 1
    value = Fraction(1, 1)
    for row, row_length in enumerate(shape):
        for column in range(row_length):
            below = sum(other_length > column for other_length in shape[row + 1 :])
            hook = row_length - column + below
            numerator = alphabet + column - row
            require(numerator > 0,
                    f"q=1 numerator vanished for allowed shape {shape}, k={alphabet}")
            value *= Fraction(numerator, hook)
    require(value.denominator == 1, f"nonintegral hook-content limit: {shape}")
    return value.numerator


def predicted_fibre(target: tuple[int, ...], alphabet: int) -> set[tuple[int, ...]]:
    candidates: set[tuple[int, ...]] = set()
    if is_highest(target, alphabet):
        candidates.add(target)
    for color in range(1, alphabet):
        source = lowering(target, color)
        if source is not None and all(
            raising(source, lower_color) is None
            for lower_color in range(1, color)
        ):
            candidates.add(source)
    return candidates


def orbit(word: tuple[int, ...], alphabet: int) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    seen: set[tuple[int, ...]] = set()
    current = word
    colors: list[int] = []
    while True:
        require(current not in seen, f"directed nontrivial cycle from {word}")
        seen.add(current)
        nxt, color = scheduled_step(current, alphabet)
        if color is None:
            require(nxt == current and is_highest(current, alphabet),
                    f"holding state is not highest: {current}")
            return len(colors), current, tuple(colors)
        require(nxt != current, f"selected color did not move: {current}, {color}")
        require(sum(nxt) == sum(current) - 1,
                f"energy failed to drop by one: {current}, {color}")
        colors.append(color)
        current = nxt


def counter_from_poly(poly: list[int]) -> Counter[int]:
    return Counter({degree: coefficient for degree, coefficient in enumerate(poly)
                    if coefficient})


def add_scaled(target: Counter[int], poly: list[int], scalar: int) -> None:
    for degree, coefficient in enumerate(poly):
        target[degree] += scalar * coefficient


def verify_tensor_and_boundary_attacks(digest) -> tuple[int, int]:
    before = (2, 1)
    after = raising(before, 1)
    require(after == (1, 1), "tensor witness has the wrong e_1 edge")
    reverse_pair = (component_shape(before), component_shape(after))
    ordinary_pair = (greene_shape(before), greene_shape(after))
    require(reverse_pair == ((2,), (2,)), "reverse-RSK fails tensor witness")
    require(ordinary_pair == ((1, 1), (2,)),
            "ordinary RSK unexpectedly preserves tensor witness")

    expected_words = (
        (3, 3, 3), (3, 3, 2), (3, 3, 1), (3, 2, 1),
        (3, 1, 1), (2, 1, 1), (1, 1, 1),
    )
    expected_colors = (2, 1, 2, 1, 2, 1)
    current = expected_words[0]
    observed_words = [current]
    observed_colors: list[int] = []
    while True:
        current, color = scheduled_step(current, 3)
        if color is None:
            break
        observed_colors.append(color)
        observed_words.append(current)
    require(tuple(observed_words) == expected_words, "333 sample orbit differs")
    require(tuple(observed_colors) == expected_colors, "333 color schedule differs")

    boundary_checks = 0
    for alphabet in range(1, 13):
        for letter in range(1, alphabet + 1):
            depth, endpoint, colors = orbit((letter,), alphabet)
            require(depth == letter - 1 and endpoint == (1,),
                    f"n=1 boundary failed: k={alphabet}, letter={letter}")
            require(colors == tuple(range(letter - 1, 0, -1)),
                    f"n=1 color order failed: k={alphabet}, letter={letter}")
            boundary_checks += 1
    for length in range(1, 13):
        only = (1,) * length
        require(scheduled_step(only, 1) == (only, None), "k=1 did not hold")
        require(component_shape(only) == (length,), "k=1 shape failed")
        require(predicted_fibre(only, 1) == {only}, "k=1 fibre failed")
        require(normalized_schur((length,), 1) == [1], "k=1 Schur failed")
        require(hook_content_at_one((length,), 1) == 1, "k=1 q=1 failed")
        boundary_checks += 1

    digest.update(
        f"TENSOR|{before}|{after}|{reverse_pair}|{ordinary_pair}\n".encode()
    )
    digest.update(f"ORBIT333|{expected_words}|{expected_colors}\n".encode())
    return boundary_checks, len(expected_colors)


def verify_complete_word_graphs(digest) -> dict[str, int | str]:
    global TRANSITIONS, TARGETS, COMPONENTS
    totals: dict[str, int | str] = {
        "boxes": 0,
        "states": 0,
        "fixed": 0,
        "empty_fibres": 0,
        "full_fibres": 0,
        "max_fibre": 0,
        "depth_checksum": 0,
        "last_box": "",
    }

    for alphabet in range(1, 6):
        for length in range(1, 7):
            words = [tuple(word) for word in product(range(1, alphabet + 1), repeat=length)]
            word_set = set(words)
            incoming: dict[tuple[int, ...], set[tuple[int, ...]]] = {
                word: set() for word in words
            }
            depths: dict[tuple[int, ...], int] = {}
            endpoints: dict[tuple[int, ...], tuple[int, ...]] = {}
            shapes: dict[tuple[int, ...], tuple[int, ...]] = {}
            global_hist: Counter[int] = Counter()

            for word in words:
                for color in range(1, alphabet):
                    up = raising(word, color)
                    down = lowering(word, color)
                    if up is not None:
                        require(lowering(up, color) == word,
                                f"f_i e_i inverse failed: {word}, {color}")
                    if down is not None:
                        require(raising(down, color) == word,
                                f"e_i f_i inverse failed: {word}, {color}")

                nxt, selected = scheduled_step(word, alphabet)
                require(nxt in word_set, f"update left [k]^n: {word}")
                incoming[nxt].add(word)
                TRANSITIONS += 1

                depth, endpoint, colors = orbit(word, alphabet)
                shape = component_shape(word)
                endpoint_shape = component_shape(endpoint)
                baseline = sum((row + 1) * part for row, part in enumerate(shape))
                require(shape == endpoint_shape, f"shape changed along orbit: {word}")
                require(depth == sum(word) - baseline,
                        f"pointwise clock failed: {(length, alphabet, word)}")
                require(is_highest(word, alphabet) == is_ballot(word, alphabet),
                        f"highest/ballot mismatch: {(length, alphabet, word)}")
                require((selected is None) == is_highest(word, alphabet),
                        f"scheduler hold mismatch: {(length, alphabet, word)}")
                depths[word] = depth
                endpoints[word] = endpoint
                shapes[word] = shape
                global_hist[depth] += 1
                digest.update(
                    f"W|{length}|{alphabet}|{word}|{selected}|{nxt}|{shape}|{depth}|{colors}\n".encode()
                )

            box_empty = 0
            box_full = 0
            box_max_fibre = 0
            for target in words:
                actual = incoming[target]
                proposed = predicted_fibre(target, alphabet)
                TARGETS += 1
                require(actual == proposed,
                        f"every-target atlas failed: {(length, alphabet, target, actual, proposed)}")
                require(len(actual) <= alphabet, f"fibre bound failed: {target}")
                require(sum(scheduled_step(source, alphabet)[0] == target for source in proposed)
                        == len(proposed), f"listed source maps elsewhere: {target}")
                if not actual:
                    box_empty += 1
                if len(actual) == alphabet:
                    box_full += 1
                    require(is_highest(target, alphabet), "full fibre lacks self/highest target")
                    content = Counter(target)
                    require(all(content[color] > content[color + 1]
                                for color in range(1, alphabet)),
                            f"full fibre highest content is not strict: {target}")
                    require(length >= alphabet * (alphabet - 1) // 2,
                            f"full fibre below staircase threshold: {target}")
                box_max_fibre = max(box_max_fibre, len(actual))
                digest.update(
                    f"P|{length}|{alphabet}|{target}|{tuple(sorted(actual))}\n".encode()
                )
            require(sum(map(len, incoming.values())) == len(words),
                    f"fibre mass failed: {(length, alphabet)}")

            expected_full_exists = (
                alphabet == 1
                or length >= alphabet * (alphabet - 1) // 2
            )
            require((box_max_fibre == alphabet) == expected_full_exists,
                    f"stable threshold iff failed in complete box {(length, alphabet)}")

            maximum_depth = max(depths.values())
            deepest = [word for word in words if depths[word] == maximum_depth]
            require(maximum_depth == length * (alphabet - 1),
                    f"sharp tail failed: {(length, alphabet)}")
            require(deepest == [(alphabet,) * length],
                    f"deepest state is not unique k^n: {(length, alphabet)}")

            unseen = set(words)
            component_counts: Counter[tuple[int, ...]] = Counter()
            fixed_by_shape: Counter[tuple[int, ...]] = Counter()
            polynomial_cache: dict[tuple[int, ...], list[int]] = {}
            while unseen:
                start = min(unseen)
                unseen.remove(start)
                queue = deque([start])
                component = {start}
                while queue:
                    word = queue.popleft()
                    for color in range(1, alphabet):
                        for neighbor in (raising(word, color), lowering(word, color)):
                            if neighbor is None:
                                continue
                            require(neighbor in word_set, "crystal edge left the carrier")
                            if neighbor not in component:
                                component.add(neighbor)
                                if neighbor in unseen:
                                    unseen.remove(neighbor)
                                queue.append(neighbor)

                component_shapes = {shapes[word] for word in component}
                component_endpoints = {endpoints[word] for word in component}
                highest = [word for word in component if is_highest(word, alphabet)]
                require(len(component_shapes) == 1, "Greene shape changes on a crystal component")
                require(len(component_endpoints) == 1 and len(highest) == 1,
                        "component does not have one scheduled highest endpoint")
                require(next(iter(component_endpoints)) == highest[0],
                        "scheduled endpoint differs from component highest")
                shape = next(iter(component_shapes))
                content = Counter(highest[0])
                require(tuple(content[i] for i in range(1, alphabet + 1))
                        == shape + (0,) * (alphabet - len(shape)),
                        f"highest content/shape mismatch: {highest[0]}, {shape}")
                if shape not in polynomial_cache:
                    polynomial_cache[shape] = normalized_schur(shape, alphabet)
                component_hist = Counter(depths[word] for word in component)
                require(component_hist == counter_from_poly(polynomial_cache[shape]),
                        f"component depth polynomial failed: {shape}, k={alphabet}")
                component_counts[shape] += 1
                fixed_by_shape[shape] += 1
                COMPONENTS += 1

            predicted_global: Counter[int] = Counter()
            expected_fixed = 0
            expected_total_at_one = 0
            allowed_shapes = [shape for shape in partitions(length) if len(shape) <= alphabet]
            require(set(component_counts) == set(allowed_shapes),
                    f"missing or extra component shapes: {(length, alphabet)}")
            for shape in allowed_shapes:
                multiplicity = standard_tableaux_aitken(shape)
                require(component_counts[shape] == multiplicity,
                        f"reverse-RSK multiplicity failed: {shape}, k={alphabet}")
                require(fixed_by_shape[shape] == multiplicity,
                        f"fixed/component multiplicity failed: {shape}, k={alphabet}")
                polynomial = polynomial_cache[shape]
                limit = hook_content_at_one(shape, alphabet)
                require(sum(polynomial) == limit,
                        f"q=1 limit failed: {shape}, k={alphabet}")
                expected_fixed += multiplicity
                expected_total_at_one += multiplicity * limit
                add_scaled(predicted_global, polynomial, multiplicity)
            require(predicted_global == global_hist,
                    f"global Schur layer sum failed: {(length, alphabet)}")
            require(expected_total_at_one == alphabet**length,
                    f"q=1 global mass is not k^n: {(length, alphabet)}")
            actual_fixed = sum(is_highest(word, alphabet) for word in words)
            require(actual_fixed == expected_fixed,
                    f"fixed census failed: {(length, alphabet)}")

            totals["boxes"] = int(totals["boxes"]) + 1
            totals["states"] = int(totals["states"]) + len(words)
            totals["fixed"] = int(totals["fixed"]) + actual_fixed
            totals["empty_fibres"] = int(totals["empty_fibres"]) + box_empty
            totals["full_fibres"] = int(totals["full_fibres"]) + box_full
            totals["max_fibre"] = max(int(totals["max_fibre"]), box_max_fibre)
            totals["depth_checksum"] = int(totals["depth_checksum"]) + maximum_depth
            totals["last_box"] = (
                f"k{alphabet}_n{length}_states{len(words)}_fixed{actual_fixed}_"
                f"maxdepth{maximum_depth}_maxfibre{box_max_fibre}_"
                f"empty{box_empty}_full{box_full}"
            )

    return totals


def longest_decreasing_subsequence(perm: tuple[int, ...]) -> int:
    lengths = [1] * len(perm)
    for right in range(len(perm)):
        for left in range(right):
            if perm[left] > perm[right]:
                lengths[right] = max(lengths[right], lengths[left] + 1)
    return max(lengths, default=0)


def telephone_formula(length: int) -> int:
    return sum(
        factorial(length) // (2**pairs * factorial(pairs) * factorial(length - 2 * pairs))
        for pairs in range(length // 2 + 1)
    )


def verify_involution_census(digest) -> dict[str, int]:
    global INVOLUTION_PERMUTATIONS_SCANNED
    totals = {"involutions": 0, "shape_checks": 0, "height_checks": 0}
    previous_two = 1  # I_0
    previous_one = 1  # I_1, replaced at n=1 after the check
    require(telephone_formula(0) == 1, "telephone q=0 term failed")
    for length in range(1, 9):
        shapes: Counter[tuple[int, ...]] = Counter()
        for perm in permutations(range(1, length + 1)):
            INVOLUTION_PERMUTATIONS_SCANNED += 1
            if all(perm[perm[index] - 1] == index + 1 for index in range(length)):
                shape = greene_shape(perm)
                require(len(shape) == longest_decreasing_subsequence(perm),
                        f"Schensted row/LDS boundary failed: {perm}, {shape}")
                shapes[shape] += 1
                totals["involutions"] += 1
        for shape in partitions(length):
            require(shapes[shape] == standard_tableaux_aitken(shape),
                    f"involution/SYT shape census failed: {length}, {shape}")
            totals["shape_checks"] += 1
        for alphabet in range(1, length + 2):
            observed = sum(count for shape, count in shapes.items() if len(shape) <= alphabet)
            predicted = sum(standard_tableaux_aitken(shape) for shape in partitions(length)
                            if len(shape) <= alphabet)
            require(observed == predicted,
                    f"bounded-height involution census failed: {length}, {alphabet}")
            if alphabet >= length:
                require(observed == telephone_formula(length),
                        f"stable involution/telephone range failed: {length}, {alphabet}")
            totals["height_checks"] += 1
        current = sum(shapes.values())
        require(current == telephone_formula(length), f"telephone formula failed: {length}")
        if length >= 2:
            require(current == previous_one + (length - 1) * previous_two,
                    f"telephone recurrence failed: {length}")
        previous_two, previous_one = previous_one, current
        digest.update(f"I|{length}|{tuple(sorted(shapes.items()))}\n".encode())
    return totals


def staircase_target(alphabet: int, surplus: int) -> tuple[int, ...]:
    if alphabet == 1:
        return (1,) * (surplus + 1)
    blocks = [alphabet - letter for letter in range(1, alphabet + 1)]
    blocks[0] += surplus
    return tuple(letter for letter, count in enumerate(blocks, 1) for _ in range(count))


def verify_stable_threshold_witnesses(digest) -> int:
    witnesses = 0
    for alphabet in range(1, 11):
        for surplus in range(4):
            target = staircase_target(alphabet, surplus)
            threshold = alphabet * (alphabet - 1) // 2
            if alphabet == 1:
                require(len(target) >= 1, "k=1 boundary target is empty")
            else:
                require(len(target) == threshold + surplus,
                        f"staircase length failed: {alphabet}, {surplus}")
            require(is_highest(target, alphabet), f"staircase is not ballot: {target}")
            fibre = predicted_fibre(target, alphabet)
            require(len(fibre) == alphabet,
                    f"staircase does not attain full fibre: {alphabet}, {surplus}")
            for source in fibre:
                require(scheduled_step(source, alphabet)[0] == target,
                        f"staircase source maps elsewhere: {source}, {target}")
            if alphabet >= 2:
                padded = tuple(Counter(target)[i] for i in range(1, alphabet + 1))
                require(all(padded[i] > padded[i + 1]
                            for i in range(alphabet - 1)),
                        f"staircase content not strictly decreasing: {padded}")
                require(sum(padded) >= sum(range(alphabet)),
                        f"strict partition violates threshold: {padded}")
            digest.update(
                f"S|{alphabet}|{surplus}|{target}|{tuple(sorted(fibre))}\n".encode()
            )
            witnesses += 1
    return witnesses


def main() -> None:
    digest = sha256()
    boundary_checks, sample_steps = verify_tensor_and_boundary_attacks(digest)
    totals = verify_complete_word_graphs(digest)
    involution = verify_involution_census(digest)
    stable_witnesses = verify_stable_threshold_witnesses(digest)

    print("P194_HOSTILE_REVIEW_A_EXACT_CONTROL")
    print("REPRESENTATION=prefix_record_minima_reverse_scan_greene_jacobi_trudi_aitken")
    print("AUTHOR_CODE_IMPORTED=false")
    print("WORD_BOXES=k1..5_n1..6")
    print(f"BOX_COUNT={totals['boxes']}")
    print(f"STATES={totals['states']}")
    print(f"TRANSITIONS={TRANSITIONS}")
    print(f"TARGETS={TARGETS}")
    print(f"FIXED_STATES={totals['fixed']}")
    print(f"CRYSTAL_COMPONENTS={COMPONENTS}")
    print(f"EMPTY_FIBRES={totals['empty_fibres']}")
    print(f"FULL_FIBRES={totals['full_fibres']}")
    print(f"LARGEST_OBSERVED_FIBRE={totals['max_fibre']}")
    print(f"DEPTH_MAXIMA_CHECKSUM={totals['depth_checksum']}")
    print(f"LAST_BOX={totals['last_box']}")
    print(f"GREENE_CALLS={GREENE_CALLS}")
    print(f"JACOBI_TRUDI_CHECKS={JT_CHECKS}")
    print(f"Q_ONE_LIMIT_CHECKS={Q_ONE_CHECKS}")
    print(f"INVOLUTION_PERMUTATIONS_SCANNED={INVOLUTION_PERMUTATIONS_SCANNED}")
    print(f"INVOLUTIONS_N1_TO_8={involution['involutions']}")
    print(f"INVOLUTION_SHAPE_CHECKS={involution['shape_checks']}")
    print(f"INVOLUTION_HEIGHT_CHECKS={involution['height_checks']}")
    print(f"STABLE_WITNESSES={stable_witnesses}")
    print(f"BOUNDARY_CHECKS={boundary_checks}")
    print(f"SAMPLE_333_STEPS={sample_steps}")
    print("TENSOR_WITNESS=21_to_11_reverse_shape_2_to_2_ordinary_shape_11_to_2")
    print(f"ASSERTIONS={ASSERTIONS}")
    print(f"CONTROL_DIGEST={digest.hexdigest()}")
    print("CRITICAL_FINDINGS=0")
    print("MAJOR_FINDINGS=0")
    print("MINOR_FINDINGS=0")
    print("VERDICT=PROVABLE_AS_STATED")
    print("OWNER_GATE=OWNER_AMBER")
    print("EXTERNAL_STATE=HOLD_EXTERNAL")
    print("FINITE_CONTROL_IS_NOT_PROOF_OR_NOVELTY=true")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
