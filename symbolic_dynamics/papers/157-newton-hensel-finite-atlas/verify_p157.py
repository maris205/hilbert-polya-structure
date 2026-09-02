#!/usr/bin/env python3
"""Exact falsifier for P157 Newton--Hensel finite dynamics.

The executable compares literal state iteration with the temporal formula and
the every-target inverse atlas.  A separate normalized-unit loop tests the
delicate four-to-one lemma, including its small-modulus truncations.  Finite
enumeration is counterexample pressure, not an all-parameter proof or an
ownership or release certificate.
"""

from __future__ import annotations

from collections import Counter


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def v2(value: int, cap: int) -> int:
    value %= 1 << cap
    if value == 0:
        return cap
    answer = 0
    while value % 2 == 0:
        answer += 1
        value //= 2
    return answer


def step(x: int, n: int) -> int:
    return (3 * x * x - 2 * x * x * x) % (1 << n)


def selected_error(x: int, n: int) -> int:
    modulus = 1 << n
    return x if x % 2 == 0 else (1 - x) % modulus


def ceiling_steps(n: int, valuation: int) -> int:
    time = 0
    while (1 << time) * valuation < n:
        time += 1
    return time


def predicted_fibre(y: int, n: int) -> int:
    modulus = 1 << n
    y %= modulus
    if y in (0, 1):
        return 1 << (n // 2)

    even_shadow = y if y % 2 == 0 else (1 - y) % modulus
    valuation = v2(even_shadow, n)
    if valuation < 2 or valuation % 2:
        return 0
    source_valuation = valuation // 2
    if 2 * source_valuation >= n:
        return 0

    quotient_bits = n - 2 * source_valuation
    unit = even_shadow >> (2 * source_valuation)
    local_modulus = 1 << min(3, quotient_bits)
    required = 7 if source_valuation == 1 else 3
    if unit % local_modulus != required % local_modulus:
        return 0
    return 1 << (source_valuation + min(quotient_bits - 1, 2))


def normalized_unit_checks() -> list[str]:
    signatures: list[str] = []
    for source_valuation in range(1, 7):
        for quotient_bits in range(1, 12):
            modulus = 1 << quotient_bits
            fibres = Counter(
                (
                    u
                    * u
                    * (3 - (1 << (source_valuation + 1)) * u)
                )
                % modulus
                for u in range(1, modulus, 2)
            )
            if quotient_bits == 1:
                required = 1
                expected_fibre = 1
            elif quotient_bits == 2:
                required = 3
                expected_fibre = 2
            else:
                required = 7 if source_valuation == 1 else 3
                expected_fibre = 4
            expected_image = {
                y
                for y in range(1, modulus, 2)
                if y % (1 << min(3, quotient_bits))
                == required % (1 << min(3, quotient_bits))
            }
            check(set(fibres) == expected_image, "normalized-unit image mismatch")
            for target in expected_image:
                check(
                    fibres[target] == expected_fibre,
                    "normalized-unit fibre mismatch",
                )
        signatures.append(
            f"v={source_valuation}:N1-11=small1,small2,four_to_one"
        )
    return signatures


def full_atlas_checks() -> list[str]:
    signatures: list[str] = []
    for n in range(1, 18):
        modulus = 1 << n
        values = [step(x, n) for x in range(modulus)]
        fibres = Counter(values)
        check(
            [x for x, image in enumerate(values) if x == image] == [0, 1],
            f"fixed-point mismatch n={n}",
        )
        check(fibres[0] == 1 << (n // 2), f"zero fibre mismatch n={n}")
        check(fibres[1] == 1 << (n // 2), f"one fibre mismatch n={n}")

        depths: list[int] = []
        for x in range(modulus):
            image = values[x]
            check(image % 2 == x % 2, f"parity mismatch n={n}, x={x}")
            check(
                step((1 - x) % modulus, n) == (1 - image) % modulus,
                f"reflection mismatch n={n}, x={x}",
            )
            error = selected_error(x, n)
            valuation = v2(error, n)
            next_valuation = v2(selected_error(image, n), n)
            check(
                next_valuation == min(n, 2 * valuation),
                f"valuation doubling mismatch n={n}, x={x}",
            )

            predicted_depth = 0 if valuation == n else ceiling_steps(n, valuation)
            current = x
            depth = 0
            while current not in (0, 1):
                current = step(current, n)
                depth += 1
                check(depth <= 1 + n.bit_length(), "termination guard failed")
            check(current == x % 2, f"endpoint mismatch n={n}, x={x}")
            check(
                depth == predicted_depth,
                f"pointwise depth mismatch n={n}, x={x}",
            )
            depths.append(depth)

        maximum_depth = max(depths)
        for time in range(maximum_depth + 1):
            threshold = (n + (1 << time) - 1) // (1 << time)
            predicted_count = 1 << (n - threshold + 1)
            check(
                sum(depth <= time for depth in depths) == predicted_count,
                f"temporal CDF mismatch n={n}, t={time}",
            )

        for target in range(modulus):
            check(
                fibres.get(target, 0) == predicted_fibre(target, n),
                f"target fibre mismatch n={n}, y={target}",
            )

        predicted_image = 2 + 2 * sum(
            1 << max(0, n - 2 * source_valuation - 3)
            for source_valuation in range(1, (n - 1) // 2 + 1)
        )
        check(len(fibres) == predicted_image, f"image size mismatch n={n}")
        check(sum(fibres.values()) == modulus, f"fibre mass mismatch n={n}")
        signatures.append(
            f"n={n}:states={modulus},image={len(fibres)},"
            f"height={maximum_depth},"
            f"fibre_spectrum={','.join(map(str, sorted(set(fibres.values()))))}"
        )
    return signatures


def main() -> None:
    unit_signatures = normalized_unit_checks()
    atlas_signatures = full_atlas_checks()
    print("NHI_FOCUSED_EXACT_V1")
    for row in unit_signatures:
        print("UNIT", row)
    for row in atlas_signatures:
        print("ATLAS", row)
    print("TEMPORAL valuation_selected_error_doubles")
    print("INVERSE normalized_unit_strata_and_every_target_fibres")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
