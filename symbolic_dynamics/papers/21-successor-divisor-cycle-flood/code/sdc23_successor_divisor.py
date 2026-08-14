#!/usr/bin/env python3
"""Deterministic exact certificates for the SD-C23 successor--divisor shift."""

from __future__ import annotations

import argparse
import csv
from functools import lru_cache
from hashlib import sha256
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


CANDIDATE_ID = "SD-C23"
TRACE_MAX_POWER = 32
WEIGHTED_MAX_POWER = 16
WEIGHTED_S_VALUES = (1, 2, 3)
TRACE_FLAG_CUTOFFS = (7, 15, 31, 63)
CONTROL_MAX_POWER = 32
CANONICAL_CHECK_MAX = 2048
SOURCE_AUDIT_CUTOFF = 4096
FAMILY_D_MAX = 16
FAMILY_Q_MAX = 16
S1_SIGMAS = (0.49, 0.50, 0.51, 0.55, 0.60, 0.75, 1.00, 1.50)
S1_CUTOFFS = (64, 128, 256, 512, 1024, 2048, 4096)


def write_csv(path: Path, rows: Sequence[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"refusing to write empty artifact: {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


@lru_cache(maxsize=None)
def divisors(value: int) -> tuple[int, ...]:
    small: list[int] = []
    large: list[int] = []
    for divisor in range(1, math.isqrt(value) + 1):
        if value % divisor:
            continue
        cofactor = value // divisor
        if divisor >= 2:
            small.append(divisor)
        if cofactor != divisor and cofactor >= 2:
            large.append(cofactor)
    return tuple(small + large[::-1])


def quotient(source: int, target: int) -> int:
    if target < 2 or (source + 1) % target:
        raise ValueError("not a successor--divisor edge")
    return (source + 1) // target


@lru_cache(maxsize=None)
def targets(
    source: int,
    quotient_inventory: frozenset[int] | None = None,
    quotient_blacklist: frozenset[int] = frozenset(),
) -> tuple[int, ...]:
    values: list[int] = []
    for target in divisors(source + 1):
        edge_quotient = quotient(source, target)
        if quotient_inventory is not None and edge_quotient not in quotient_inventory:
            continue
        if edge_quotient in quotient_blacklist:
            continue
        values.append(target)
    return tuple(values)


def canonical_cycle(length: int) -> tuple[int, ...]:
    if length < 2:
        raise ValueError("canonical cycle length must be at least two")
    return tuple(range(length, 2 * length))


def quotient_cycle(divisor: int, edge_quotient: int) -> tuple[int, ...]:
    if divisor < 2 or edge_quotient < 2:
        raise ValueError("quotient-cycle parameters must be at least two")
    return tuple(range(divisor, edge_quotient * divisor))


def is_closed_walk(
    word: Sequence[int],
    quotient_inventory: frozenset[int] | None = None,
    quotient_blacklist: frozenset[int] = frozenset(),
) -> bool:
    return bool(word) and all(
        word[(index + 1) % len(word)]
        in targets(word[index], quotient_inventory, quotient_blacklist)
        for index in range(len(word))
    )


def is_simple_cycle(
    word: Sequence[int],
    quotient_inventory: frozenset[int] | None = None,
    quotient_blacklist: frozenset[int] = frozenset(),
) -> bool:
    return (
        bool(word)
        and len(word) == len(set(word))
        and is_closed_walk(word, quotient_inventory, quotient_blacklist)
    )


def cycle_mass(word: Sequence[int]) -> int:
    return math.prod(word)


def cycle_quotients(word: Sequence[int]) -> tuple[int, ...]:
    if not is_closed_walk(word):
        raise ValueError("quotients require a closed word")
    return tuple(
        quotient(word[index], word[(index + 1) % len(word)])
        for index in range(len(word))
    )


def canonical_rotation(word: Sequence[int]) -> tuple[int, ...]:
    candidate = tuple(word)
    return min(candidate[index:] + candidate[:index] for index in range(len(candidate)))


def primitive_root_length(word: Sequence[int]) -> int:
    size = len(word)
    for root in integer_divisors(size):
        if root == size:
            break
        if all(word[index] == word[index % root] for index in range(size)):
            return root
    return size


@lru_cache(maxsize=None)
def graph(
    cutoff: int,
    quotient_inventory: frozenset[int] | None = None,
    quotient_blacklist: frozenset[int] = frozenset(),
    s_integer: int | None = None,
) -> tuple[tuple[int, tuple[tuple[int, Fraction], ...]], ...]:
    rows: list[tuple[int, tuple[tuple[int, Fraction], ...]]] = []
    for source in range(2, cutoff + 1):
        row: list[tuple[int, Fraction]] = []
        for target in targets(source, quotient_inventory, quotient_blacklist):
            if target > cutoff:
                continue
            weight = Fraction(1)
            if s_integer is not None:
                weight = Fraction(1, (source * target) ** s_integer)
            row.append((target, weight))
        rows.append((source, tuple(row)))
    return tuple(rows)


def graph_dict(
    cutoff: int,
    quotient_inventory: frozenset[int] | None = None,
    quotient_blacklist: frozenset[int] = frozenset(),
    s_integer: int | None = None,
) -> dict[int, tuple[tuple[int, Fraction], ...]]:
    return dict(graph(cutoff, quotient_inventory, quotient_blacklist, s_integer))


@lru_cache(maxsize=None)
def power_traces(
    cutoff: int,
    max_power: int,
    quotient_inventory: frozenset[int] | None = None,
    quotient_blacklist: frozenset[int] = frozenset(),
    s_integer: int | None = None,
) -> tuple[Fraction, ...]:
    adjacency = graph_dict(
        cutoff,
        quotient_inventory,
        quotient_blacklist,
        s_integer,
    )
    traces = [Fraction(0) for _ in range(max_power)]
    for start in range(2, cutoff + 1):
        state = {start: Fraction(1)}
        for step in range(1, max_power + 1):
            next_state: dict[int, Fraction] = {}
            for source, amplitude in state.items():
                for target, weight in adjacency[source]:
                    next_state[target] = (
                        next_state.get(target, Fraction(0)) + amplitude * weight
                    )
            state = next_state
            traces[step - 1] += state.get(start, Fraction(0))
    return tuple(traces)


def moebius(value: int) -> int:
    remaining = value
    factors = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            factors += 1
            if remaining % divisor == 0:
                return 0
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors += 1
    return -1 if factors % 2 else 1


@lru_cache(maxsize=None)
def integer_divisors(value: int) -> tuple[int, ...]:
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


def primitive_counts(rooted_traces: Sequence[int]) -> list[int]:
    result: list[int] = []
    for power in range(1, len(rooted_traces) + 1):
        numerator = sum(
            moebius(power // divisor) * rooted_traces[divisor - 1]
            for divisor in integer_divisors(power)
        )
        if numerator % power:
            raise AssertionError("necklace inversion lost integrality")
        result.append(numerator // power)
    return result


def determinant_coefficients(traces: Sequence[Fraction]) -> list[Fraction]:
    """Return coefficients of exp(-sum_r trace_r z^r/r)."""
    coefficients = [Fraction(1)]
    for degree in range(1, len(traces) + 1):
        total = sum(
            traces[power - 1] * coefficients[degree - power]
            for power in range(1, degree + 1)
        )
        coefficients.append(-total / degree)
    return coefficients


@lru_cache(maxsize=None)
def primitive_orbits(
    cutoff: int,
    max_length: int,
    quotient_inventory: frozenset[int] | None = None,
) -> tuple[tuple[int, ...], ...]:
    adjacency = {
        source: tuple(target for target, _ in row)
        for source, row in graph_dict(cutoff, quotient_inventory).items()
    }
    found: set[tuple[int, ...]] = set()

    def extend(start: int, path: list[int], edges_used: int) -> None:
        if edges_used >= max_length:
            return
        source = path[-1]
        for target in adjacency[source]:
            next_edges = edges_used + 1
            path.append(target)
            if target == start:
                word = tuple(path[:-1])
                if primitive_root_length(word) == len(word):
                    found.add(canonical_rotation(word))
            if next_edges < max_length:
                extend(start, path, next_edges)
            path.pop()

    for start in range(2, cutoff + 1):
        extend(start, [start], 0)
    return tuple(sorted(found, key=lambda word: (len(word), word)))


def primitive_product_coefficients(
    orbits: Iterable[Sequence[int]],
    s_integer: int,
    max_degree: int,
) -> list[Fraction]:
    coefficients = [Fraction(1)] + [Fraction(0)] * max_degree
    for orbit in orbits:
        length = len(orbit)
        if length > max_degree:
            continue
        weight = Fraction(1, cycle_mass(orbit) ** (2 * s_integer))
        for degree in range(max_degree, length - 1, -1):
            coefficients[degree] -= weight * coefficients[degree - length]
    return coefficients


def row_nuclear_prefix(cutoff: int, sigma: float) -> float:
    total = 0.0
    for target in range(2, cutoff + 1):
        squared = 0.0
        quotient_value = 1
        while quotient_value * target - 1 < 2:
            quotient_value += 1
        while True:
            source = quotient_value * target - 1
            if source > cutoff:
                break
            squared += (source * target) ** (-2.0 * sigma)
            quotient_value += 1
        total += math.sqrt(squared)
    return total


def successor_s1_prefix(cutoff: int, sigma: float) -> float:
    return sum((source * (source + 1)) ** (-sigma) for source in range(2, cutoff))


def source_edge_certificate(cutoff: int) -> dict[str, object]:
    digest = sha256()
    edge_count = 0
    quotient_max = 0
    successor_count = 0
    for source in range(2, cutoff + 1):
        row = targets(source)
        if source + 1 not in row:
            raise AssertionError("successor edge missing")
        for target in row:
            edge_quotient = quotient(source, target)
            if source + 1 != target * edge_quotient:
                raise AssertionError("semiring witness identity failed")
            if source == target:
                raise AssertionError("loop found")
            edge_count += 1
            quotient_max = max(quotient_max, edge_quotient)
            successor_count += edge_quotient == 1
            digest.update(f"{source},{target},{edge_quotient}\n".encode("ascii"))
    return {
        "candidate_id": CANDIDATE_ID,
        "allowed_graph_operations": [
            "integer_successor",
            "paired_divisor_enumeration",
            "integer_quotient_certificate",
        ],
        "audit_cutoff": cutoff,
        "edge_count": edge_count,
        "edge_ledger_sha256": digest.hexdigest(),
        "graph_frozen_before_target_comparison": True,
        "loop_count": 0,
        "max_exposed_quotient": quotient_max,
        "prime_table_used": False,
        "quotient_identity_mismatches": 0,
        "riemann_zero_data_used": False,
        "successor_edge_count": successor_count,
        "target_feedback_used": False,
    }


def route_tuple() -> list[str]:
    return [
        "A0_STRUCTURAL_ARITHMETIC_RELATION",
        "A1_WEAK",
        "A2_ANALYTIC_DETERMINANT",
        "A3_FAIL",
        "A4_FAIL",
    ]


def generate_artifacts(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)

    full_unweighted = power_traces(
        2 * TRACE_MAX_POWER - 1,
        TRACE_MAX_POWER,
    )
    rooted = [int(value) for value in full_unweighted]
    primitive = primitive_counts(rooted)

    unweighted_rows = []
    for power in range(1, TRACE_MAX_POWER + 1):
        reconstruction = sum(
            divisor * primitive[divisor - 1]
            for divisor in integer_divisors(power)
        )
        unweighted_rows.append(
            {
                "candidate_id": CANDIDATE_ID,
                "graph_variant": "full",
                "cutoff": 2 * TRACE_MAX_POWER - 1,
                "power": power,
                "certified_cutoff": 2 * power - 1,
                "exact_infinite_trace": True,
                "rooted_closed_walks": rooted[power - 1],
                "primitive_rotation_classes": primitive[power - 1],
                "necklace_reconstruction": reconstruction,
                "algorithm": "sparse_dictionary_dynamic_program",
                "source_oracle_free": True,
            }
        )

    cutoff_flag_rows = []
    for cutoff in TRACE_FLAG_CUTOFFS:
        values = power_traces(cutoff, TRACE_MAX_POWER)
        for power, value in enumerate(values, start=1):
            cutoff_flag_rows.append(
                {
                    "candidate_id": CANDIDATE_ID,
                    "graph_variant": "full",
                    "cutoff": cutoff,
                    "power": power,
                    "certified_cutoff": 2 * power - 1,
                    "exact_infinite_trace": cutoff >= 2 * power - 1,
                    "trace_numerator": value.numerator,
                    "trace_denominator": value.denominator,
                    "algorithm": "sparse_dictionary_dynamic_program",
                    "source_oracle_free": True,
                }
            )

    confinement_rows = []
    for power in range(1, TRACE_MAX_POWER + 1):
        certified_cutoff = 2 * power - 1
        exact = power_traces(certified_cutoff, power)[-1]
        plus_one = power_traces(2 * power, power)[-1]
        larger = power_traces(4 * power + 3, power)[-1]
        confinement_rows.append(
            {
                "candidate_id": CANDIDATE_ID,
                "power": power,
                "certified_cutoff": certified_cutoff,
                "trace_at_certified_cutoff": str(exact),
                "trace_at_plus_one": str(plus_one),
                "trace_at_larger_cutoff": str(larger),
                "stabilized_exactly": exact == plus_one == larger,
                "canonical_extremal_cycle": (
                    "" if power == 1 else " ".join(map(str, canonical_cycle(power)))
                ),
                "extremal_cycle_simple_certificate": (
                    power == 1 or is_simple_cycle(canonical_cycle(power))
                ),
            }
        )

    orbit_words = primitive_orbits(
        2 * WEIGHTED_MAX_POWER - 1,
        WEIGHTED_MAX_POWER,
    )
    orbit_rows = []
    for word in orbit_words:
        orbit_rows.append(
            {
                "candidate_id": CANDIDATE_ID,
                "graph_variant": "full",
                "cutoff": 2 * WEIGHTED_MAX_POWER - 1,
                "length": len(word),
                "rotation_canonical_word": " ".join(map(str, word)),
                "primitive_root_length": primitive_root_length(word),
                "repetition_number": 1,
                "orientation_convention": "directed_rotations_only_no_reflection",
                "mass": cycle_mass(word),
                "edge_quotient_word": " ".join(map(str, cycle_quotients(word))),
                "source_oracle_free": True,
            }
        )

    weighted_rows = []
    determinant_rows = []
    for s_integer in WEIGHTED_S_VALUES:
        weighted = power_traces(
            2 * WEIGHTED_MAX_POWER - 1,
            WEIGHTED_MAX_POWER,
            s_integer=s_integer,
        )
        recurrence_coefficients = determinant_coefficients(weighted)
        orbit_coefficients = primitive_product_coefficients(
            orbit_words,
            s_integer,
            WEIGHTED_MAX_POWER,
        )
        for power, value in enumerate(weighted, start=1):
            weighted_rows.append(
                {
                    "candidate_id": CANDIDATE_ID,
                    "graph_variant": "full",
                    "s_integer": s_integer,
                    "cutoff": 2 * WEIGHTED_MAX_POWER - 1,
                    "power": power,
                    "certified_cutoff": 2 * power - 1,
                    "exact_infinite_trace": True,
                    "trace": str(value),
                    "trace_numerator": value.numerator,
                    "trace_denominator": value.denominator,
                    "algorithm": "sparse_fraction_dynamic_program",
                    "source_oracle_free": True,
                }
            )
        for degree, recurrence_value in enumerate(recurrence_coefficients):
            orbit_value = orbit_coefficients[degree]
            determinant_rows.append(
                {
                    "candidate_id": CANDIDATE_ID,
                    "s_integer": s_integer,
                    "z_power": degree,
                    "newton_coefficient": str(recurrence_value),
                    "primitive_product_coefficient": str(orbit_value),
                    "numerator": recurrence_value.numerator,
                    "denominator": recurrence_value.denominator,
                    "exact_match": recurrence_value == orbit_value,
                    "primitive_factor_cutoff": WEIGHTED_MAX_POWER,
                }
            )

    family_rows = []
    for edge_quotient in range(2, FAMILY_Q_MAX + 1):
        for divisor in range(2, FAMILY_D_MAX + 1):
            word = quotient_cycle(divisor, edge_quotient)
            family_rows.append(
                {
                    "candidate_id": CANDIDATE_ID,
                    "q": edge_quotient,
                    "d": divisor,
                    "length": len(word),
                    "predicted_length": divisor * (edge_quotient - 1),
                    "first_vertex": word[0],
                    "last_vertex": word[-1],
                    "simple_cycle": is_simple_cycle(
                        word,
                        frozenset({1, edge_quotient}),
                    ),
                    "primitive_certificate": len(word) == len(set(word)),
                    "closing_quotient": quotient(word[-1], word[0]),
                    "mass": cycle_mass(word),
                }
            )

    control_specs: list[
        tuple[str, frozenset[int] | None, frozenset[int]]
    ] = [
        ("full", None, frozenset()),
        ("q_1_2_spine", frozenset({1, 2}), frozenset()),
        ("successor_only", frozenset({1}), frozenset()),
    ]
    control_specs.extend(
        (f"q_1_{edge_quotient}", frozenset({1, edge_quotient}), frozenset())
        for edge_quotient in range(3, FAMILY_Q_MAX + 1)
    )
    control_specs.extend(
        [
            ("blacklist_q2", None, frozenset({2})),
            ("blacklist_q2_q3", None, frozenset({2, 3})),
            ("blacklist_q2_q3_q4", None, frozenset({2, 3, 4})),
        ]
    )
    control_rows = []
    for name, inventory, blacklist in control_specs:
        values = power_traces(
            2 * CONTROL_MAX_POWER - 1,
            CONTROL_MAX_POWER,
            quotient_inventory=inventory,
            quotient_blacklist=blacklist,
        )
        positive_lengths = [
            power
            for power, value in enumerate(values, start=1)
            if value != 0
        ]
        control_rows.append(
            {
                "candidate_id": CANDIDATE_ID,
                "variant": name,
                "quotient_inventory": (
                    "all" if inventory is None else " ".join(map(str, sorted(inventory)))
                ),
                "quotient_blacklist": " ".join(map(str, sorted(blacklist))),
                "trace_power_one": str(values[0]),
                "trace_vector_1_to_32": " ".join(map(str, values)),
                "positive_length_count_2_to_32": sum(
                    values[power - 1] != 0
                    for power in range(2, CONTROL_MAX_POWER + 1)
                ),
                "first_positive_length": (
                    positive_lengths[0] if positive_lengths else ""
                ),
                "all_lengths_2_to_32": all(
                    values[power - 1] != 0
                    for power in range(2, CONTROL_MAX_POWER + 1)
                ),
                "control_margin_against_full_flood": (
                    0 if name == "q_1_2_spine" else "not_applicable"
                ),
                "strong_connectivity_theorem": (
                    "proved" if name in {"full", "q_1_2_spine"} else "not_claimed"
                ),
            }
        )

    inventory_rows = []
    for inventory_name in ("n", "n_plus_one", "n_squared_plus_one", "two_to_n"):
        for length in range(2, 18):
            word = canonical_cycle(length)
            if inventory_name == "n":
                representation = str(math.prod(word))
            elif inventory_name == "n_plus_one":
                representation = str(math.prod(vertex + 1 for vertex in word))
            elif inventory_name == "n_squared_plus_one":
                representation = str(
                    math.prod(vertex * vertex + 1 for vertex in word)
                )
            else:
                representation = f"2^{sum(word)}"
            inventory_rows.append(
                {
                    "candidate_id": CANDIDATE_ID,
                    "inventory": inventory_name,
                    "cycle_length": length,
                    "simple_cycle": is_simple_cycle(word),
                    "strictly_positive_symbolic_weight": True,
                    "weight_representation": representation,
                    "interpretation": "weight_inventory_control_not_graph_selectivity_control",
                }
            )

    s1_rows = []
    for sigma in S1_SIGMAS:
        previous_row_value: float | None = None
        previous_successor_value: float | None = None
        previous_increment: float | None = None
        for cutoff in S1_CUTOFFS:
            row_value = row_nuclear_prefix(cutoff, sigma)
            successor_value = successor_s1_prefix(cutoff, sigma)
            row_increment = (
                row_value
                if previous_row_value is None
                else row_value - previous_row_value
            )
            successor_increment = (
                successor_value
                if previous_successor_value is None
                else successor_value - previous_successor_value
            )
            local_increment_ratio = (
                ""
                if previous_increment in (None, 0.0)
                else row_increment / previous_increment
            )
            s1_rows.append(
                {
                    "candidate_id": CANDIDATE_ID,
                    "sigma": sigma,
                    "cutoff": cutoff,
                    "row_nuclear_lower_prefix": row_value,
                    "row_dyadic_increment": row_increment,
                    "row_increment_ratio": local_increment_ratio,
                    "successor_s1_prefix": successor_value,
                    "successor_dyadic_increment": successor_increment,
                    "theorem_membership": sigma > 0.5,
                    "theorem_status": "diagnostic_only_exact_threshold_proved_analytically",
                }
            )
            previous_row_value = row_value
            previous_successor_value = successor_value
            previous_increment = row_increment

    oracle = source_edge_certificate(SOURCE_AUDIT_CUTOFF)
    summary = {
        "candidate_id": CANDIDATE_ID,
        "canonical_cycle_check_max": CANONICAL_CHECK_MAX,
        "canonical_cycles_all_pass": all(
            is_simple_cycle(canonical_cycle(length))
            for length in range(2, CANONICAL_CHECK_MAX + 1)
        ),
        "confinement": "every length-r closed walk lies in vertices 2 through 2r-1",
        "determinant_coefficient_max_degree": WEIGHTED_MAX_POWER,
        "determinant_cross_method_all_exact": all(
            row["exact_match"] for row in determinant_rows
        ),
        "first_exact_weighted_formulas": {
            "trace_1_s1": weighted_rows[0]["trace"],
            "trace_2_s1": weighted_rows[1]["trace"],
            "trace_3_s1": weighted_rows[2]["trace"],
            "trace_4_s1": weighted_rows[3]["trace"],
        },
        "first_trace_zero": rooted[0] == 0,
        "graph_rule": "n->d iff d>=2 and d divides n+1",
        "operator": "L_s e_n=sum_(d|n+1,d>=2)(nd)^(-s)e_d",
        "orbit_norm_species": "perfect_squares_of_composite_integer_masses",
        "overall_verdict": "ROUTE_A_REJECTED",
        "primitive_orbit_inventory_through_length_16": len(orbit_rows),
        "q_1_2_spine_all_length_flood": next(
            row["all_lengths_2_to_32"]
            for row in control_rows
            if row["variant"] == "q_1_2_spine"
        ),
        "quotient_family_rows": len(family_rows),
        "route_b_invocation_allowed": False,
        "route_tuple": route_tuple(),
        "source_audit_edge_count": oracle["edge_count"],
        "strongly_connected": True,
        "successor_only_acyclic": next(
            row["first_positive_length"] == ""
            for row in control_rows
            if row["variant"] == "successor_only"
        ),
        "target_zero_data_used": False,
        "topologically_mixing": True,
        "trace_class_iff": "Re(s)>1/2",
        "unweighted_trace_orders": TRACE_MAX_POWER,
        "weighted_integer_s_values": list(WEIGHTED_S_VALUES),
        "weighted_trace_max_power": WEIGHTED_MAX_POWER,
        "weight_inventory_control_rows": len(inventory_rows),
    }

    write_csv(output / "unweighted_trace_primitive.csv", unweighted_rows)
    write_csv(output / "trace_cutoff_flags.csv", cutoff_flag_rows)
    write_csv(output / "confinement_certificates.csv", confinement_rows)
    write_csv(output / "primitive_orbit_inventory.csv", orbit_rows)
    write_csv(output / "weighted_trace_ledger.csv", weighted_rows)
    write_csv(output / "determinant_coefficients.csv", determinant_rows)
    write_csv(output / "quotient_cycle_families.csv", family_rows)
    write_csv(output / "graph_controls.csv", control_rows)
    write_csv(output / "weight_inventory_controls.csv", inventory_rows)
    write_csv(output / "trace_class_diagnostics.csv", s1_rows)
    write_json(output / "source_oracle_certificate.json", oracle)
    write_json(output / "summary.json", summary)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    generate_artifacts(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
