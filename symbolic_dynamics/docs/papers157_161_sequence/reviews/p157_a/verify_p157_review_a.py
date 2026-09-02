#!/usr/bin/env python3
"""Reviewer-owned hostile exact audit for P157.

This program was written independently of the paper-local verifier.  It
attacks the theorem interfaces named A1--A3 and B1--B4, with separate lanes
for the N=1,2 quotient boundaries, the exact Taylor bit lift, and the 2^v
source-bit multiplicity.  It is finite counterexample pressure owned by
Hostile Review A, not an author control and not an all-parameter proof.
"""

from __future__ import annotations

from collections import Counter
from math import ceil, log2


CHECKS = 0


def demand(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def polynomial(x: int) -> int:
    return 3 * x * x - 2 * x * x * x


def update(x: int, bits: int) -> int:
    return polynomial(x) % (1 << bits)


def valuation(value: int, bits: int) -> int:
    value %= 1 << bits
    if value == 0:
        return bits
    exponent = 0
    while not value & 1:
        exponent += 1
        value >>= 1
    return exponent


def endpoint_error(x: int, bits: int) -> int:
    return x % (1 << bits) if x % 2 == 0 else (1 - x) % (1 << bits)


def odd_map(source_valuation: int, unit: int) -> int:
    return unit * unit * (3 - (1 << (source_valuation + 1)) * unit)


def expected_target_fibre(target: int, bits: int) -> int:
    modulus = 1 << bits
    target %= modulus
    if target in (0, 1):
        return 1 << (bits // 2)
    shadow = target if target % 2 == 0 else (1 - target) % modulus
    output_valuation = valuation(shadow, bits)
    if output_valuation < 2 or output_valuation % 2:
        return 0
    source_valuation = output_valuation // 2
    if 2 * source_valuation >= bits:
        return 0
    quotient_bits = bits - 2 * source_valuation
    normalized = shadow >> (2 * source_valuation)
    if quotient_bits == 1:
        admissible = normalized % 2 == 1
    elif quotient_bits == 2:
        admissible = normalized % 4 == 3
    elif source_valuation == 1:
        admissible = normalized % 8 == 7
    else:
        admissible = normalized % 8 == 3
    if not admissible:
        return 0
    return 1 << (source_valuation + min(quotient_bits - 1, 2))


def algebra_lane() -> None:
    for x in range(-256, 257):
        fx = polynomial(x)
        demand(fx == x * x * (3 - 2 * x), "first factorization")
        demand(1 - fx == (1 - x) ** 2 * (1 + 2 * x), "second factorization")
        demand(polynomial(1 - x) == 1 - fx, "reflection identity")


def temporal_lane() -> None:
    for bits in range(1, 19):
        modulus = 1 << bits
        depths: list[int] = []
        endpoints: list[int] = []
        for x in range(modulus):
            error = endpoint_error(x, bits)
            start_valuation = valuation(error, bits)
            y = update(x, bits)
            demand(y % 2 == x % 2, f"parity bits={bits} x={x}")
            demand(
                valuation(endpoint_error(y, bits), bits)
                == min(bits, 2 * start_valuation),
                f"A1 bits={bits} x={x}",
            )

            current = x
            depth = 0
            while current not in (0, 1):
                current = update(current, bits)
                depth += 1
                demand(depth <= 1 + bits.bit_length(), "orbit guard")
            predicted = 0
            while (1 << predicted) * start_valuation < bits:
                predicted += 1
            demand(depth == predicted, f"A2 bits={bits} x={x}")
            demand(current == x % 2, f"endpoint bits={bits} x={x}")
            depths.append(depth)
            endpoints.append(current)

        maximum = max(depths)
        demand(maximum == ceil(log2(bits)), f"sharp height bits={bits}")
        for time in range(maximum + 3):
            threshold = (bits + (1 << time) - 1) // (1 << time)
            expected = 1 << (bits - threshold + 1)
            observed = sum(depth <= time for depth in depths)
            demand(observed == expected, f"A3 bits={bits} time={time}")
        demand(set(endpoints) == {0, 1}, f"recurrent endpoints bits={bits}")


def unit_and_boundary_lane() -> None:
    for source_valuation in range(1, 9):
        for quotient_bits in range(1, 14):
            modulus = 1 << quotient_bits
            counts = Counter(
                odd_map(source_valuation, unit) % modulus
                for unit in range(1, modulus, 2)
            )
            if quotient_bits == 1:
                image = {1}
                multiplicity = 1
            elif quotient_bits == 2:
                image = {3}
                multiplicity = 2
            else:
                low = 7 if source_valuation == 1 else 3
                image = set(range(low, modulus, 8))
                multiplicity = 4
            demand(set(counts) == image, "B1 normalized image")
            for target in range(1, modulus, 2):
                demand(
                    counts.get(target, 0)
                    == (multiplicity if target in image else 0),
                    "B2 reduced target fibre",
                )


def taylor_lane() -> None:
    for source_valuation in range(1, 9):
        for residue in (1, 3):
            base_value = odd_map(source_valuation, residue)
            for bit in range(12):
                delta = 4 * (1 << bit)
                for z in range(1 << (bit + 1)):
                    w = residue + 4 * z
                    hp = 6 * w * (1 - (1 << source_valuation) * w)
                    hpp = 6 - 6 * (1 << (source_valuation + 1)) * w
                    hppp = -6 * (1 << (source_valuation + 1))
                    difference = odd_map(source_valuation, w + delta) - odd_map(
                        source_valuation, w
                    )
                    demand(
                        6 * difference
                        == 6 * delta * hp
                        + 3 * delta * delta * hpp
                        + delta * delta * delta * hppp,
                        "exact cubic Taylor identity",
                    )
                    demand(valuation(hp, 64) == 1, "Taylor first derivative")
                    demand(valuation(hpp, 64) == 1, "Taylor second derivative")
                    demand(
                        valuation(hppp, 64) == source_valuation + 2,
                        "Taylor third derivative",
                    )
                    demand((odd_map(source_valuation, w) - base_value) % 8 == 0,
                           "Phi integrality")
                    phi_here = (odd_map(source_valuation, w) - base_value) // 8
                    phi_lift = (
                        odd_map(source_valuation, w + delta) - base_value
                    ) // 8
                    demand(
                        (phi_lift - phi_here) % (1 << (bit + 1)) == 1 << bit,
                        "Taylor one-bit toggle",
                    )


def source_multiplicity_lane() -> None:
    for bits in range(3, 19):
        modulus = 1 << bits
        for source_valuation in range(1, (bits - 1) // 2 + 1):
            quotient_bits = bits - 2 * source_valuation
            reduced_modulus = 1 << quotient_bits
            lift_count = 1 << source_valuation
            all_sources: set[int] = set()
            for low_unit in range(1, reduced_modulus, 2):
                target_unit = odd_map(source_valuation, low_unit) % reduced_modulus
                local_sources: set[int] = set()
                for high in range(lift_count):
                    full_unit = low_unit + high * reduced_modulus
                    source = (1 << source_valuation) * full_unit
                    source %= modulus
                    demand(
                        valuation(source, bits) == source_valuation,
                        "source valuation preserved",
                    )
                    demand(
                        (update(source, bits) >> (2 * source_valuation))
                        % reduced_modulus
                        == target_unit,
                        "forgotten source bits preserve target",
                    )
                    local_sources.add(source)
                    all_sources.add(source)
                demand(len(local_sources) == lift_count, "2^v high lifts")
            demand(
                len(all_sources) == 1 << (bits - source_valuation - 1),
                "source stratum exhaustiveness",
            )


def full_inverse_lane() -> list[str]:
    rows: list[str] = []
    for bits in range(1, 19):
        modulus = 1 << bits
        counts = Counter(update(x, bits) for x in range(modulus))
        demand(counts[0] == 1 << (bits // 2), f"B3 zero bits={bits}")
        demand(counts[1] == 1 << (bits // 2), f"B3 one bits={bits}")
        for target in range(modulus):
            demand(
                counts.get(target, 0) == expected_target_fibre(target, bits),
                f"B1/B2 full target bits={bits} y={target}",
            )
        expected_image = 2 + 2 * sum(
            1 << max(0, bits - 2 * source_valuation - 3)
            for source_valuation in range(1, (bits - 1) // 2 + 1)
        )
        demand(len(counts) == expected_image, f"B4 bits={bits}")
        demand(sum(counts.values()) == modulus, f"fibre mass bits={bits}")
        rows.append(
            f"n={bits}:states={modulus},image={len(counts)},"
            f"endpoint_fibre={counts[0]}"
        )
    return rows


def main() -> None:
    algebra_lane()
    temporal_lane()
    unit_and_boundary_lane()
    taylor_lane()
    source_multiplicity_lane()
    rows = full_inverse_lane()
    print("P157_HOSTILE_REVIEW_A_EXACT_V1")
    print("INTERFACES A1_A2_A3 B1_B2_B3_B4")
    print("UNIT_BOUNDARIES v=1..8 N=1..13")
    print("TAYLOR exact_identity_and_bit_toggle j=0..11")
    print("SOURCE_MULTIPLICITY full_2^v_high_lifts n=3..18")
    for row in rows:
        print("ATLAS", row)
    print(f"ASSERTIONS={CHECKS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
