#!/usr/bin/env python3
"""Independent exact breadth verifier for the P177--P181 algebra lane.

Only the Python standard library is used.  Eleven raw maps are executed.  Two
of them are retained as explicit rediscovery sentinels after the repository
firewall found exact earlier literals, so the fresh breadth count is nine.
No author, earlier scout, or paper verifier is imported.  Enumeration is
evidence and falsification pressure, not proof of an all-parameter statement
or an ownership certificate.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()
DIGEST = sha256()
TRANSITIONS = 0
TRANSITIONS_BY_TAG: Counter[str] = Counter()


def digest_edge(tag: str, box: tuple[int, ...], source: int, target: int) -> None:
    global TRANSITIONS
    TRANSITIONS += 1
    TRANSITIONS_BY_TAG[tag] += 1
    DIGEST.update(f"{tag}|{box}|{source}|{target}\n".encode())


def compact_counter(counter: Counter[int]) -> str:
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def graph_stats(successor: list[int]) -> dict[str, object]:
    """Direct functional-graph decomposition, independent of formulas."""
    size = len(successor)
    incoming = Counter(successor)
    depth: list[int | None] = [None] * size
    period: list[int | None] = [None] * size
    cycles: Counter[int] = Counter()
    for start in range(size):
        if depth[start] is not None:
            continue
        path: list[int] = []
        position: dict[int, int] = {}
        current = start
        while depth[current] is None and current not in position:
            position[current] = len(path)
            path.append(current)
            current = successor[current]
        if depth[current] is None:
            split = position[current]
            cycle_length = len(path) - split
            cycles[cycle_length] += 1
            for vertex in path[split:]:
                depth[vertex] = 0
                period[vertex] = cycle_length
            for vertex in reversed(path[:split]):
                depth[vertex] = depth[successor[vertex]] + 1  # type: ignore[operator]
                period[vertex] = cycle_length
        else:
            for vertex in reversed(path):
                depth[vertex] = depth[successor[vertex]] + 1  # type: ignore[operator]
                period[vertex] = period[successor[vertex]]
    AUDIT.check(all(value is not None for value in depth), "unassigned depth")
    AUDIT.check(all(value is not None for value in period), "unassigned period")
    for source, target in enumerate(successor):
        AUDIT.check(0 <= target < size, "successor outside carrier")
        if depth[source] == 0:
            AUDIT.check(depth[target] == 0, "recurrent state left recurrent core")
        else:
            AUDIT.check(depth[target] == depth[source] - 1, "depth did not drop")
    return {
        "N": size,
        "image": len(incoming),
        "fixed": sum(source == target for source, target in enumerate(successor)),
        "periods": tuple(sorted(cycles)),
        "cycles": cycles,
        "height": max(depth),
        "depths": Counter(depth),
        "fibres": Counter(incoming.get(target, 0) for target in range(size)),
        "max_fibre": max(incoming.values()),
    }


def digits_base(value: int, base: int, length: int) -> tuple[int, ...]:
    out = []
    for _ in range(length):
        out.append(value % base)
        value //= base
    return tuple(out)


def encode_base(values: tuple[int, ...], base: int) -> int:
    answer = 0
    scale = 1
    for value in values:
        answer += value * scale
        scale *= base
    return answer


def state_selected_difference(value: int, prime: int) -> int:
    function = digits_base(value, prime, prime)
    step = function[0]
    image = tuple(
        (function[(point + step) % prime] - function[point]) % prime
        for point in range(prime)
    )
    return encode_base(image, prime)


def binomial_polynomial_value(point: int, degree: int, prime: int) -> int:
    answer = 1
    for offset in range(degree):
        answer = answer * (point - offset) * pow(offset + 1, -1, prime) % prime
    return answer


def check_sfd() -> list[str]:
    """C01: f -> (x |-> f(x+f(0))-f(x)) on all F_p-valued functions."""
    rows = []
    for prime in (2, 3, 5, 7):
        size = prime**prime
        successor = [0] * size
        for source in range(size):
            target = state_selected_difference(source, prime)
            successor[source] = target
            digest_edge("SFD", (prime,), source, target)
            target_digits = digits_base(target, prime, prime)
            AUDIT.check(sum(target_digits) % prime == 0, "SFD image not zero-sum")

        current = list(range(size))
        image_profile = []
        zero_fibres = []
        cdf = []
        for time in range(prime + 1):
            fibres = Counter(current)
            expected_image = prime ** (prime - time) if time <= prime else 1
            AUDIT.check(len(fibres) == expected_image, "SFD image tower mismatch")
            image_profile.append(len(fibres))
            zero_fibres.append(fibres[0])
            cdf.append(fibres[0])
            if time == 0:
                AUDIT.check(set(fibres.values()) == {1}, "SFD time-zero fibres")
            elif time < prime:
                regular = (prime - 1) ** time
                expected_zero = size - (expected_image - 1) * regular
                AUDIT.check(fibres[0] == expected_zero, "SFD zero fibre mismatch")
                for target, multiplicity in fibres.items():
                    if target != 0:
                        AUDIT.check(multiplicity == regular, "SFD nonzero fibre mismatch")
            else:
                AUDIT.check(fibres == Counter({0: size}), "SFD p-nilpotence failed")
            if time < prime:
                current = [successor[value] for value in current]

        depth_histogram = Counter({0: 1})
        for depth in range(1, prime + 1):
            observed = cdf[depth] - cdf[depth - 1]
            predicted = (prime - 1) ** (depth - 1) * (
                prime ** (prime - depth) + prime - 2
            )
            AUDIT.check(observed == predicted, "SFD depth shell mismatch")
            depth_histogram[depth] = observed

        jordan_blocks = Counter()
        for block_size in range(1, prime):
            jordan_blocks[block_size] = (
                (prime - 1) ** 2 * prime ** (prime - block_size - 1)
            )
        jordan_blocks[prime] = prime - 1
        AUDIT.check(
            sum(size * multiplicity for size, multiplicity in jordan_blocks.items())
            == size - 1,
            "SFD nilpotent Jordan dimension mismatch",
        )
        for time in range(prime + 1):
            rank_from_blocks = sum(
                max(block_size - time, 0) * multiplicity
                for block_size, multiplicity in jordan_blocks.items()
            )
            AUDIT.check(
                rank_from_blocks == prime ** (prime - time) - 1,
                "SFD Jordan rank sequence mismatch",
            )

        witness = tuple(
            sum(
                binomial_polynomial_value(point, degree, prime)
                for degree in range(prime)
            )
            % prime
            for point in range(prime)
        )
        witness_state = encode_base(witness, prime)
        direction_trace = []
        current_state = witness_state
        for _ in range(prime):
            direction_trace.append(digits_base(current_state, prime, prime)[0])
            current_state = successor[current_state]
        AUDIT.check(direction_trace == [1] * prime, "SFD sharp witness directions")
        AUDIT.check(current_state == 0, "SFD sharp witness endpoint")
        rows.append(
            f"p={prime} N={size} images={'/'.join(map(str, image_profile))} "
            f"depths={compact_counter(depth_histogram)} "
            f"zero_fibres={'/'.join(map(str, zero_fibres))} "
            f"J0={compact_counter(jordan_blocks)} witness=PASS"
        )
    return rows


def determinant_mod(matrix: tuple[int, ...], order: int, prime: int) -> int:
    work = [list(matrix[row * order : (row + 1) * order]) for row in range(order)]
    answer = 1
    for column in range(order):
        pivot = next(
            (row for row in range(column, order) if work[row][column] % prime),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer
        diagonal = work[column][column] % prime
        answer = answer * diagonal % prime
        inverse = pow(diagonal, -1, prime)
        for row in range(column + 1, order):
            scale = work[row][column] * inverse % prime
            for entry in range(column, order):
                work[row][entry] = (
                    work[row][entry] - scale * work[column][entry]
                ) % prime
    return answer % prime


def scalar_translate(
    matrix: tuple[int, ...], scalar: int, order: int, prime: int
) -> tuple[int, ...]:
    return tuple(
        (value + (scalar if index // order == index % order else 0)) % prime
        for index, value in enumerate(matrix)
    )


def series_product(
    left: list[Fraction], right: list[Fraction], degree: int
) -> list[Fraction]:
    out = [Fraction(0)] * (degree + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                out[i + j] += a * b
    return out


def series_inverse(series: list[Fraction], degree: int) -> list[Fraction]:
    AUDIT.check(series[0] != 0, "series inversion with zero constant")
    out = [Fraction(0)] * (degree + 1)
    out[0] = 1 / series[0]
    for index in range(1, degree + 1):
        out[index] = -sum(
            series[offset] * out[index - offset]
            for offset in range(1, index + 1)
        ) / series[0]
    return out


def series_power(series: list[Fraction], exponent: int, degree: int) -> list[Fraction]:
    if exponent < 0:
        return series_power(series_inverse(series, degree), -exponent, degree)
    out = [Fraction(1)] + [Fraction(0)] * degree
    base = list(series)
    power = exponent
    while power:
        if power & 1:
            out = series_product(out, base, degree)
        base = series_product(base, base, degree)
        power //= 2
    return out


def general_linear_order(order: int, field_order: int) -> int:
    answer = 1
    for index in range(order):
        answer *= field_order**order - field_order**index
    return answer


def fixed_root_set_matrix_count(
    field_order: int, characteristic: int, order: int, root_count: int
) -> int:
    """Cycle-index coefficient for one prescribed exact F_p-root set."""
    local = [Fraction(1)]
    denominator = 1
    for degree in range(1, order + 1):
        denominator *= field_order**degree - 1
        local.append(
            Fraction(field_order ** (degree * (degree - 1) // 2), denominator)
        )
    full_without_selected = series_product(
        [Fraction(1)] * (order + 1),
        series_power(local, 1 - characteristic, order),
        order,
    )
    nonempty_local = list(local)
    nonempty_local[0] -= 1
    series = series_product(
        full_without_selected,
        series_power(nonempty_local, root_count, order),
        order,
    )
    answer = series[order] * general_linear_order(order, field_order)
    AUDIT.check(answer.denominator == 1, "nonintegral matrix cycle-index count")
    return answer.numerator


def check_sst() -> list[str]:
    """C02: A -> A+I when A is invertible, and A -> A when singular."""
    rows = []
    boxes = ((2, 1), (3, 1), (5, 1), (2, 2), (3, 2), (5, 2), (2, 3), (3, 3))
    for prime, order in boxes:
        states = list(product(range(prime), repeat=order * order))
        index = {state: number for number, state in enumerate(states)}
        determinants = {
            state: determinant_mod(state, order, prime) for state in states
        }
        successor = []
        roots_by_state: dict[tuple[int, ...], tuple[int, ...]] = {}
        exact_root_sets: defaultdict[int, Counter[tuple[int, ...]]] = defaultdict(Counter)
        for number, state in enumerate(states):
            target = (
                scalar_translate(state, 1, order, prime)
                if determinants[state]
                else state
            )
            successor.append(index[target])
            digest_edge("SST", (prime, order), number, index[target])
            roots = tuple(
                scalar
                for scalar in range(prime)
                if determinant_mod(
                    scalar_translate(state, -scalar, order, prime), order, prime
                )
                == 0
            )
            roots_by_state[state] = roots
            exact_root_sets[len(roots)][roots] += 1

        stats = graph_stats(successor)
        AUDIT.check(stats["height"] == prime - 1, "SST sharp height mismatch")
        AUDIT.check(set(stats["periods"]).issubset({1, prime}), "SST bad period")
        incoming = Counter(successor)
        for number, target in enumerate(states):
            predecessor = scalar_translate(target, -1, order, prime)
            expected = (
                (1 if determinants[target] == 0 else 0)
                + (1 if determinants[predecessor] != 0 else 0)
            )
            AUDIT.check(incoming[number] == expected, "SST one-step fibre mismatch")

        iterated = list(range(len(states)))
        observed_image_profile = []
        for time in range(2 * prime + 2):
            observed_fibres = Counter(iterated)
            observed_image_profile.append(len(observed_fibres))
            for number, target in enumerate(states):
                if time == 0:
                    expected = 1
                elif determinants[target] == 0:
                    preceding_gap = 0
                    while (
                        preceding_gap < prime - 1
                        and determinants[
                            scalar_translate(
                                target, -(preceding_gap + 1), order, prime
                            )
                        ]
                        != 0
                    ):
                        preceding_gap += 1
                    expected = 1 + min(time, preceding_gap)
                else:
                    expected = int(
                        all(
                            determinants[
                                scalar_translate(target, -step, order, prime)
                            ]
                            != 0
                            for step in range(1, time + 1)
                        )
                    )
                AUDIT.check(
                    observed_fibres[number] == expected,
                    "SST every-time target fibre mismatch",
                )
            iterated = [successor[value] for value in iterated]

        line_count = 0
        empty_lines = 0
        positive_gap_histogram: Counter[int] = Counter()
        for state in states:
            line = tuple(
                scalar_translate(state, scalar, order, prime)
                for scalar in range(prime)
            )
            if state != min(line):
                continue
            line_count += 1
            singular = [determinants[point] == 0 for point in line]
            if not any(singular):
                empty_lines += 1
                for point in line:
                    AUDIT.check(
                        successor[index[point]] == index[scalar_translate(point, 1, order, prime)],
                        "SST empty line not a cycle",
                    )
            else:
                for position, point in enumerate(line):
                    if singular[position]:
                        AUDIT.check(successor[index[point]] == index[point], "SST singular not fixed")
                        gap = 0
                        cursor = (position - 1) % prime
                        while not singular[cursor]:
                            gap += 1
                            cursor = (cursor - 1) % prime
                        if gap:
                            positive_gap_histogram[gap] += 1
        AUDIT.check(line_count * prime == len(states), "SST central-line partition")
        AUDIT.check(empty_lines == stats["cycles"].get(prime, 0), "SST p-cycle census")
        AUDIT.check(
            stats["fixed"] == len(states) - general_linear_order(order, prime),
            "SST singular fixed census",
        )

        root_cardinality_totals = Counter()
        per_fixed_subset = {}
        for root_count in range(prime + 1):
            predicted = fixed_root_set_matrix_count(prime, prime, order, root_count)
            values = []
            for subset in combinations(range(prime), root_count):
                observed = exact_root_sets[root_count][subset]
                AUDIT.check(observed == predicted, "SST exact root-set cycle-index mismatch")
                values.append(observed)
            per_fixed_subset[root_count] = predicted
            root_cardinality_totals[root_count] = sum(values)
        AUDIT.check(sum(root_cardinality_totals.values()) == len(states), "SST root-set mass")
        predicted_empty_lines = per_fixed_subset[0] // prime
        AUDIT.check(predicted_empty_lines == empty_lines, "SST empty-line coefficient mismatch")
        AUDIT.check(
            sum(
                comb(prime - 1, root_count - 1) * per_fixed_subset[root_count]
                for root_count in range(1, prime + 1)
            )
            == stats["fixed"],
            "SST prescribed-root coefficients do not recover singular matrices",
        )

        predicted_gap_histogram: Counter[int] = Counter()
        if prime >= 2:
            predicted_gap_histogram[prime - 1] += per_fixed_subset[1]
        for root_count in range(2, min(order, prime) + 1):
            weight = per_fixed_subset[root_count]
            for gap in range(1, prime - root_count + 1):
                predicted_gap_histogram[gap] += weight * comb(
                    prime - gap - 2, root_count - 2
                )
        AUDIT.check(
            positive_gap_histogram == predicted_gap_histogram,
            "SST zero-Jordan gap histogram mismatch",
        )
        positive_gap_count = sum(positive_gap_histogram.values())
        AUDIT.check(
            stats["image"] == len(states) - positive_gap_count,
            "SST image versus positive gaps mismatch",
        )
        AUDIT.check(
            stats["fibres"].get(0, 0) == positive_gap_count
            and stats["fibres"].get(2, 0) == positive_gap_count,
            "SST fibre histogram versus positive gaps mismatch",
        )
        AUDIT.check(
            stats["fixed"]
            + prime * empty_lines
            + sum(gap * count for gap, count in positive_gap_histogram.items())
            == len(states),
            "SST functional-graph vertex mass mismatch",
        )
        for time, observed_image in enumerate(observed_image_profile):
            predicted_image = (
                stats["fixed"]
                + prime * empty_lines
                + sum(
                    max(gap - time, 0) * count
                    for gap, count in positive_gap_histogram.items()
                )
            )
            AUDIT.check(
                observed_image == predicted_image,
                "SST all-time image profile mismatch",
            )
        rows.append(
            f"p={prime} n={order} N={len(states)} image={stats['image']} "
            f"fixed={stats['fixed']} periods={','.join(map(str, stats['periods']))} "
            f"height={stats['height']} fibres={compact_counter(stats['fibres'])} "
            f"root_cards={compact_counter(root_cardinality_totals)} "
            f"J0_gaps={compact_counter(positive_gap_histogram)}"
        )
    return rows


def least_nonsquare(prime: int) -> int:
    return next(
        value
        for value in range(2, prime)
        if pow(value, (prime - 1) // 2, prime) == prime - 1
    )


def fp2_add(
    left: tuple[int, int], right: tuple[int, int], prime: int
) -> tuple[int, int]:
    return ((left[0] + right[0]) % prime, (left[1] + right[1]) % prime)


def fp2_neg(value: tuple[int, int], prime: int) -> tuple[int, int]:
    return ((-value[0]) % prime, (-value[1]) % prime)


def fp2_mul(
    left: tuple[int, int], right: tuple[int, int], prime: int, nonsquare: int
) -> tuple[int, int]:
    return (
        (left[0] * right[0] + nonsquare * left[1] * right[1]) % prime,
        (left[0] * right[1] + left[1] * right[0]) % prime,
    )


def fp2_power(
    value: tuple[int, int], exponent: int, prime: int, nonsquare: int
) -> tuple[int, int]:
    answer = (1, 0)
    base = value
    while exponent:
        if exponent & 1:
            answer = fp2_mul(answer, base, prime, nonsquare)
        base = fp2_mul(base, base, prime, nonsquare)
        exponent //= 2
    return answer


def fp2_inverse(
    value: tuple[int, int], prime: int, nonsquare: int
) -> tuple[int, int]:
    AUDIT.check(value != (0, 0), "inverse of zero in Fp2")
    return fp2_power(value, prime * prime - 2, prime, nonsquare)


def fp2_norm(value: tuple[int, int], prime: int, nonsquare: int) -> int:
    return (value[0] * value[0] - nonsquare * value[1] * value[1]) % prime


def quadratic_root_count(discriminant: int, prime: int) -> int:
    discriminant %= prime
    if discriminant == 0:
        return 1
    return 2 if pow(discriminant, (prime - 1) // 2, prime) == 1 else 0


def unit_circle_trace_root_count(discriminant: int, prime: int) -> int:
    """Roots of u^2-au+1 inside the norm-one subgroup of F_(p^2)."""
    discriminant %= prime
    if discriminant == 0:
        return 1
    return 2 if pow(discriminant, (prime - 1) // 2, prime) == prime - 1 else 0


def check_uct() -> list[str]:
    """C03: x -> x^(p-1)+x^(1-p) on F_(p^2), with zero fixed."""
    rows = []
    for prime in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        nonsquare = least_nonsquare(prime)
        states = list(product(range(prime), repeat=2))
        index = {state: number for number, state in enumerate(states)}
        successor = []
        for number, state in enumerate(states):
            if state == (0, 0):
                target = state
            else:
                unit = fp2_power(state, prime - 1, prime, nonsquare)
                target = fp2_add(
                    unit, fp2_inverse(unit, prime, nonsquare), prime
                )
            AUDIT.check(target[1] == 0, "UCT failed to descend to base field")
            successor.append(index[target])
            digest_edge("UCT", (prime,), number, index[target])
        stats = graph_stats(successor)
        AUDIT.check(stats["fixed"] == 2, "UCT fixed census")
        AUDIT.check(stats["periods"] == (1,), "UCT unexpected nontrivial cycle")
        AUDIT.check(stats["height"] == 2, "UCT height")
        incoming = Counter(successor)
        for number, target in enumerate(states):
            if target[1]:
                expected = 0
            else:
                value = target[0]
                roots = unit_circle_trace_root_count(value * value - 4, prime)
                expected = (prime - 1) * roots + (1 if value == 0 else 0)
            AUDIT.check(incoming[number] == expected, "UCT fibre formula")
        second = Counter(successor[successor[source]] for source in range(len(states)))
        zero_fibre = 1 + (
            2 * (prime - 1)
            if pow(prime - 1, (prime - 1) // 2, prime) == prime - 1
            else 0
        )
        AUDIT.check(second[index[(0, 0)]] == zero_fibre, "UCT time-two zero fibre")
        AUDIT.check(
            second[index[(2 % prime, 0)]] == prime * prime - zero_fibre,
            "UCT time-two two fibre",
        )
        AUDIT.check(len(second) == 2, "UCT second image")
        rows.append(
            f"p={prime} d={nonsquare} N={prime*prime} image={stats['image']} "
            f"fixed=2 height=2 depths={compact_counter(stats['depths'])} "
            f"fibres={compact_counter(stats['fibres'])} time2=0:{zero_fibre},2:{prime*prime-zero_fibre}"
        )
    return rows


def check_vieta() -> list[str]:
    """C04: (x,y) -> (x+y,xy) on F_p^2."""
    rows = []
    for prime in (2, 3, 5, 7, 11, 13, 17, 19):
        states = list(product(range(prime), repeat=2))
        index = {state: number for number, state in enumerate(states)}
        successor = []
        for number, (left, right) in enumerate(states):
            target = ((left + right) % prime, left * right % prime)
            successor.append(index[target])
            digest_edge("VTM", (prime,), number, index[target])
        stats = graph_stats(successor)
        incoming = Counter(successor)
        if prime > 2:
            for number, (summed, multiplied) in enumerate(states):
                expected = quadratic_root_count(
                    summed * summed - 4 * multiplied, prime
                )
                AUDIT.check(incoming[number] == expected, "Vieta discriminant fibre")
            AUDIT.check(stats["image"] == prime * (prime + 1) // 2, "Vieta image")
        rows.append(
            f"p={prime} N={prime*prime} image={stats['image']} fixed={stats['fixed']} "
            f"periods={','.join(map(str, stats['periods']))} height={stats['height']} "
            f"fibres={compact_counter(stats['fibres'])}"
        )
    return rows


def matrix_inverse_mod(
    matrix: tuple[int, ...], order: int, prime: int
) -> tuple[int, ...] | None:
    work = [
        list(matrix[row * order : (row + 1) * order])
        + [1 if row == column else 0 for column in range(order)]
        for row in range(order)
    ]
    for column in range(order):
        pivot = next(
            (row for row in range(column, order) if work[row][column] % prime),
            None,
        )
        if pivot is None:
            return None
        work[column], work[pivot] = work[pivot], work[column]
        inverse = pow(work[column][column] % prime, -1, prime)
        work[column] = [value * inverse % prime for value in work[column]]
        for row in range(order):
            if row == column:
                continue
            scale = work[row][column] % prime
            work[row] = [
                (work[row][entry] - scale * work[column][entry]) % prime
                for entry in range(2 * order)
            ]
    return tuple(
        work[row][order + column]
        for row in range(order)
        for column in range(order)
    )


def check_zmi() -> list[str]:
    """C05: zero-totalized inversion on the full matrix algebra."""
    rows = []
    for prime, order in ((2, 2), (3, 2), (5, 2), (7, 2), (2, 3), (3, 3)):
        states = list(product(range(prime), repeat=order * order))
        index = {state: number for number, state in enumerate(states)}
        zero = (0,) * (order * order)
        inverses = {state: matrix_inverse_mod(state, order, prime) for state in states}
        successor = []
        for number, state in enumerate(states):
            target = inverses[state] if inverses[state] is not None else zero
            successor.append(index[target])
            digest_edge("ZMI", (prime, order), number, index[target])
        stats = graph_stats(successor)
        invertible = general_linear_order(order, prime)
        singular = len(states) - invertible
        AUDIT.check(stats["image"] == invertible + 1, "ZMI image")
        AUDIT.check(stats["height"] == 1, "ZMI height")
        AUDIT.check(set(stats["periods"]).issubset({1, 2}), "ZMI periods")
        incoming = Counter(successor)
        for number, target in enumerate(states):
            if target == zero:
                expected = singular
            elif inverses[target] is not None:
                expected = 1
            else:
                expected = 0
            AUDIT.check(incoming[number] == expected, "ZMI fibre atlas")
        rows.append(
            f"p={prime} n={order} N={len(states)} image={stats['image']} "
            f"fixed={stats['fixed']} periods={','.join(map(str, stats['periods']))} "
            f"height=1 fibres={compact_counter(stats['fibres'])}"
        )
    return rows


def permutation_compose(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


def permutation_inverse(value: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * len(value)
    for source, target in enumerate(value):
        answer[target] = source
    return tuple(answer)


def check_pcm() -> list[str]:
    """C06: (x,y) -> (xy,[x,y]) on S_n^2."""
    rows = []
    for order in (2, 3, 4, 5):
        group = list(permutations(range(order)))
        index = {element: number for number, element in enumerate(group)}
        group_size = len(group)
        successor = []
        for left_number, left in enumerate(group):
            left_inverse = permutation_inverse(left)
            for right_number, right in enumerate(group):
                product_value = permutation_compose(left, right)
                commutator = permutation_compose(
                    permutation_compose(
                        permutation_compose(left_inverse, permutation_inverse(right)),
                        left,
                    ),
                    right,
                )
                source = left_number * group_size + right_number
                target = index[product_value] * group_size + index[commutator]
                successor.append(target)
                digest_edge("PCM", (order,), source, target)
        stats = graph_stats(successor)
        AUDIT.check(stats["fixed"] == group_size, "PCM fixed census")
        rows.append(
            f"n={order} N={group_size*group_size} image={stats['image']} "
            f"fixed={stats['fixed']} periods={','.join(map(str, stats['periods']))} "
            f"height={stats['height']} fibres={compact_counter(stats['fibres'])}"
        )
    return rows


def check_self_power() -> list[str]:
    """C07: canonical-residue self power x -> x^x modulo p, with zero fixed."""
    rows = []
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        successor = [0 if value == 0 else pow(value, value, prime) for value in range(prime)]
        for source, target in enumerate(successor):
            digest_edge("SPR", (prime,), source, target)
            AUDIT.check(target == (0 if source == 0 else pow(source, source, prime)), "SPR literal")
        stats = graph_stats(successor)
        rows.append(
            f"p={prime} image={stats['image']} fixed={stats['fixed']} "
            f"periods={','.join(map(str, stats['periods']))} height={stats['height']} "
            f"fibres={compact_counter(stats['fibres'])}"
        )
    return rows


def check_p_derivation() -> list[str]:
    """C08: arithmetic p-derivation (x-x^p)/p from Z/p^2Z into F_p."""
    rows = []
    for prime in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        size = prime * prime
        successor = [((value - pow(value, prime)) // prime) % prime for value in range(size)]
        for source, target in enumerate(successor):
            digest_edge("APD", (prime,), source, target)
            residue = source % prime
            digit = source // prime
            reduced = (digit + (residue - pow(residue, prime)) // prime) % prime
            AUDIT.check(target == reduced, "p-derivation digit formula")
        stats = graph_stats(successor)
        incoming = Counter(successor)
        for target in range(size):
            AUDIT.check(
                incoming[target] == (prime if target < prime else 0),
                "p-derivation uniform first fibre",
            )
        rows.append(
            f"p={prime} N={size} image={stats['image']} fixed={stats['fixed']} "
            f"periods={','.join(map(str, stats['periods']))} height={stats['height']} "
            f"fibres={compact_counter(stats['fibres'])}"
        )
    return rows


def check_frobenius_reciprocal() -> list[str]:
    """C09: x -> x^p-x^(-1) on F_(p^2), with zero fixed."""
    rows = []
    for prime in (3, 5, 7, 11, 13, 17, 19):
        nonsquare = least_nonsquare(prime)
        states = list(product(range(prime), repeat=2))
        index = {state: number for number, state in enumerate(states)}
        successor = []
        for number, state in enumerate(states):
            if state == (0, 0):
                target = state
            else:
                target = fp2_add(
                    fp2_power(state, prime, prime, nonsquare),
                    fp2_neg(fp2_inverse(state, prime, nonsquare), prime),
                    prime,
                )
                source_norm = fp2_norm(state, prime, nonsquare)
                if source_norm == 1:
                    AUDIT.check(target == (0, 0), "FRD norm-one collapse")
                else:
                    target_norm = fp2_norm(target, prime, nonsquare)
                    predicted_norm = (
                        (source_norm - 1) ** 2 * pow(source_norm, -1, prime)
                    ) % prime
                    AUDIT.check(target_norm == predicted_norm, "FRD norm quotient")
                    source_unit = fp2_power(state, prime - 1, prime, nonsquare)
                    target_unit = fp2_power(target, prime - 1, prime, nonsquare)
                    AUDIT.check(
                        target_unit == fp2_inverse(source_unit, prime, nonsquare),
                        "FRD unit-coordinate inversion",
                    )
            successor.append(index[target])
            digest_edge("FRD", (prime,), number, index[target])
        stats = graph_stats(successor)
        incoming = Counter(successor)
        for number, target in enumerate(states):
            if target == (0, 0):
                expected = prime + 2
            else:
                norm = fp2_norm(target, prime, nonsquare)
                expected = quadratic_root_count(norm * (norm + 4), prime)
            AUDIT.check(incoming[number] == expected, "FRD norm-discriminant fibre")
        rows.append(
            f"p={prime} d={nonsquare} N={prime*prime} image={stats['image']} "
            f"fixed={stats['fixed']} periods={','.join(map(str, stats['periods']))} "
            f"height={stats['height']} fibres={compact_counter(stats['fibres'])}"
        )
    return rows


def factor_integer(value: int) -> Counter[int]:
    factors: Counter[int] = Counter()
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] += 1
            value //= divisor
        divisor += 1
    if value > 1:
        factors[value] += 1
    return factors


def euler_phi(value: int) -> int:
    answer = value
    for prime in factor_integer(value):
        answer = answer // prime * (prime - 1)
    return answer


def multiplicative_order_mod(value: int, prime: int) -> int:
    AUDIT.check(value % prime != 0, "multiplicative order requested at zero")
    order = prime - 1
    for factor in factor_integer(prime - 1):
        while order % factor == 0 and pow(value, order // factor, prime) == 1:
            order //= factor
    AUDIT.check(pow(value, order, prime) == 1, "bad multiplicative order")
    return order


def check_order_return() -> list[str]:
    """C10: 0 -> 0 and x -> ord_p(x), using canonical integer residues."""
    rows = []
    primes = (3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 61, 73, 89, 97)
    for prime in primes:
        successor = [0] + [
            multiplicative_order_mod(value, prime) % prime
            for value in range(1, prime)
        ]
        for source, target in enumerate(successor):
            digest_edge("MOR", (prime,), source, target)
            AUDIT.check(0 <= target < prime, "MOR escaped prime carrier")
        incoming = Counter(successor)
        AUDIT.check(incoming[0] == 1, "MOR zero fibre")
        for target in range(1, prime):
            expected = euler_phi(target) if (prime - 1) % target == 0 else 0
            AUDIT.check(incoming[target] == expected, "MOR order census")
        stats = graph_stats(successor)
        rows.append(
            f"p={prime} image={stats['image']} fixed={stats['fixed']} "
            f"periods={','.join(map(str, stats['periods']))} height={stats['height']} "
            f"fibres={compact_counter(stats['fibres'])}"
        )
    return rows


def check_factorial_residue() -> list[str]:
    """C11: x -> x! mod p on canonical residues, with 0! read as 0 here."""
    rows = []
    primes = (3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 61, 73, 89, 97)
    for prime in primes:
        successor = [0]
        factorial = 1
        for value in range(1, prime):
            factorial = factorial * value % prime
            successor.append(factorial)
        for source, target in enumerate(successor):
            digest_edge("FAC", (prime,), source, target)
            expected = 0 if source == 0 else 1
            for factor in range(1, source + 1):
                expected = expected * factor % prime
            AUDIT.check(target == expected, "FAC literal mismatch")
        AUDIT.check(successor[prime - 1] == prime - 1, "FAC Wilson endpoint")
        stats = graph_stats(successor)
        rows.append(
            f"p={prime} image={stats['image']} fixed={stats['fixed']} "
            f"periods={','.join(map(str, stats['periods']))} height={stats['height']} "
            f"fibres={compact_counter(stats['fibres'])}"
        )
    return rows


def emit_section(title: str, rows: list[str]) -> None:
    print(title)
    for row in rows:
        print(row)


def main() -> None:
    print("P177--P181 ALGEBRA/FINITE-FIELD/NUMBER-THEORY BREADTH CONTROL")
    print("STATUS SCOUT_ONLY / HOLD_EXTERNAL")
    print("INDEPENDENCE standard-library fresh implementation; no project code imported")
    emit_section("C01_SFD_STATE_SELECTED_DIFFERENCE", check_sfd())
    emit_section("C02_SST_SINGULARITY_STOPPED_TRANSLATION", check_sst())
    emit_section("C03_UCT_UNIT_CIRCLE_TRACE_COLLAPSE", check_uct())
    emit_section("C04_VTM_REDISCOVERY_SENTINEL_VIETA_COEFFICIENT_MAP", check_vieta())
    emit_section("C05_ZMI_ZERO_TOTALIZED_MATRIX_INVERSION", check_zmi())
    emit_section("C06_PCM_REDISCOVERY_SENTINEL_PRODUCT_COMMUTATOR_MAP", check_pcm())
    emit_section("C07_SPR_SELF_POWER_RESIDUES", check_self_power())
    emit_section("C08_APD_ARITHMETIC_P_DERIVATION", check_p_derivation())
    emit_section("C09_FRD_FROBENIUS_RECIPROCAL_DEFECT", check_frobenius_reciprocal())
    emit_section("C10_MOR_MULTIPLICATIVE_ORDER_RETURN", check_order_return())
    emit_section("C11_FAC_FACTORIAL_RESIDUE_RETURN", check_factorial_residue())
    print(f"TRANSITION_DIGEST={DIGEST.hexdigest()}")
    print(f"TRANSITIONS={TRANSITIONS}")
    print(
        "FRESH_TRANSITIONS="
        f"{TRANSITIONS-TRANSITIONS_BY_TAG['VTM']-TRANSITIONS_BY_TAG['PCM']}"
    )
    print("RAW_BOXES=104")
    print("FRESH_BOXES=92")
    print(f"ASSERTIONS={AUDIT.assertions}")
    print("RAW_CANDIDATES=11")
    print("FRESH_CANDIDATES=9")
    print("REDISCOVERY_SENTINELS=2")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
