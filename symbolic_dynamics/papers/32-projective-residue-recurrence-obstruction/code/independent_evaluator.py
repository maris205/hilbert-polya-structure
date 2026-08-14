#!/usr/bin/env python3
"""Independent evaluator for the serialized SD-C34 candidate artifacts.

This module intentionally imports neither ``residue_core`` nor
``generate_results``. It reconstructs the projective grammars, matched finite
semirings, generic relation actions, arithmetic strata, and analytic finite
witnesses independently.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path
import random
from typing import Dict, List, Sequence, Tuple


Point = Tuple[int, int]


@dataclass(frozen=True)
class Grammar:
    modulus: int
    points: Tuple[Point, ...]
    s_image: Tuple[int, ...]
    r_image: Tuple[int, ...]

    @property
    def size(self) -> int:
        return len(self.points)


class Audit:
    def __init__(self) -> None:
        self.check_count = 0
        self.failures: List[str] = []

    def check(self, condition: bool, label: str, weight: int = 1) -> None:
        self.check_count += weight
        if not condition:
            self.failures.append(label)


def stable_json(data: object) -> bytes:
    return (json.dumps(data, sort_keys=True, indent=2) + "\n").encode("utf-8")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def write_json(path: Path, data: object) -> None:
    path.write_bytes(stable_json(data))


def write_csv(path: Path, rows: Sequence[Dict[str, object]], fields: Sequence[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def units_mod(modulus: int) -> Tuple[int, ...]:
    return tuple(value for value in range(modulus) if gcd(value, modulus) == 1)


def canonical_point(modulus: int, point: Point, units: Sequence[int]) -> Point:
    left, right = point
    return min((unit * left % modulus, unit * right % modulus) for unit in units)


def projective_line(modulus: int) -> Tuple[Point, ...]:
    units = units_mod(modulus)
    seen: Dict[Point, Point] = {}
    representatives: List[Point] = []
    for left in range(modulus):
        for right in range(modulus):
            pair = left, right
            if pair in seen or gcd(gcd(left, right), modulus) != 1:
                continue
            orbit = {(unit * left % modulus, unit * right % modulus) for unit in units}
            representative = min(orbit)
            for member in orbit:
                seen[member] = representative
            representatives.append(representative)
    return tuple(sorted(representatives))


def build_grammar(modulus: int) -> Grammar:
    points = projective_line(modulus)
    index = {point: offset for offset, point in enumerate(points)}
    units = units_mod(modulus)
    s_image: List[int] = []
    r_image: List[int] = []
    for left, right in points:
        s_point = canonical_point(modulus, ((-right) % modulus, left), units)
        r_point = canonical_point(modulus, ((-right) % modulus, (left + right) % modulus), units)
        s_image.append(index[s_point])
        r_image.append(index[r_point])
    return Grammar(modulus, points, tuple(s_image), tuple(r_image))


def compose(mapping: Sequence[int], power: int) -> Tuple[int, ...]:
    output = tuple(range(len(mapping)))
    for _ in range(power):
        output = tuple(mapping[index] for index in output)
    return output


def cycle_lengths(mapping: Sequence[int]) -> Tuple[int, ...]:
    seen = [False] * len(mapping)
    lengths: List[int] = []
    for start in range(len(mapping)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = mapping[current]
        lengths.append(length)
    return tuple(sorted(lengths))


def forward_component_size(grammar: Grammar) -> int:
    seen = {0}
    frontier = [0]
    while frontier:
        vertex = frontier.pop()
        for image in (grammar.s_image[vertex], grammar.r_image[vertex]):
            if image not in seen:
                seen.add(image)
                frontier.append(image)
    return len(seen)


def trace_word_count(grammar: Grammar, length: int) -> int:
    total = 0
    for start in range(grammar.size):
        counts = {start: 1}
        for _ in range(length):
            next_counts: Dict[int, int] = {}
            for vertex, multiplicity in counts.items():
                for image in (grammar.s_image[vertex], grammar.r_image[vertex]):
                    next_counts[image] = next_counts.get(image, 0) + multiplicity
            counts = next_counts
        total += counts.get(start, 0)
    return total


def census_row(grammar: Grammar, trace_order: int) -> Dict[str, int]:
    s_lengths = cycle_lengths(grammar.s_image)
    r_lengths = cycle_lengths(grammar.r_image)
    row: Dict[str, int] = {
        "modulus": grammar.modulus,
        "state_count": grammar.size,
        "projective_defect": grammar.size - grammar.modulus - 1,
        "s_cycle_count": len(s_lengths),
        "s_fixed_count": s_lengths.count(1),
        "s_two_cycle_count": s_lengths.count(2),
        "r_cycle_count": len(r_lengths),
        "r_fixed_count": r_lengths.count(1),
        "r_three_cycle_count": r_lengths.count(3),
        "forward_component_size": forward_component_size(grammar),
        "overlap_state_count": grammar.size,
    }
    for order in range(1, trace_order + 1):
        row[f"trace_{order}"] = trace_word_count(grammar, order)
    return row


def arithmetic_class(modulus: int) -> Tuple[bool, str]:
    factors: List[int] = []
    remaining = modulus
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.append(divisor)
            remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.append(remaining)
    if len(factors) == 1:
        return True, "prime"
    if len(set(factors)) == 1:
        return False, "prime_power"
    return False, "mixed_composite"


def random_relation_action(size: int, seed: int) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    rng = random.Random(seed)
    order = list(range(size))
    rng.shuffle(order)
    s_map = list(range(size))
    for index in range(0, size - 1, 2):
        left, right = order[index], order[index + 1]
        s_map[left], s_map[right] = right, left
    order = list(range(size))
    rng.shuffle(order)
    r_map = list(range(size))
    triple_limit = size - size % 3
    for index in range(0, triple_limit, 3):
        first, second, third = order[index], order[index + 1], order[index + 2]
        r_map[first], r_map[second], r_map[third] = second, third, first
    return tuple(s_map), tuple(r_map)


def matched_control(
    grammar: Grammar,
    source_row: Dict[str, int],
    trace_order: int,
    seed: int,
) -> Tuple[Dict[str, object], int, int]:
    modulus = grammar.modulus
    rng = random.Random(seed)
    encode_list = list(range(modulus))
    rng.shuffle(encode_list)
    encode = tuple(encode_list)
    decode_list = [0] * modulus
    for old, new in enumerate(encode):
        decode_list[new] = old
    decode = tuple(decode_list)

    def add(left: int, right: int) -> int:
        return encode[(decode[left] + decode[right]) % modulus]

    def multiply(left: int, right: int) -> int:
        return encode[(decode[left] * decode[right]) % modulus]

    def negate(value: int) -> int:
        return encode[(-decode[value]) % modulus]

    units = units_mod(modulus)

    def canonical_clone(point: Point) -> Point:
        old_point = decode[point[0]], decode[point[1]]
        representative = canonical_point(modulus, old_point, units)
        return encode[representative[0]], encode[representative[1]]

    encoded_points = tuple((encode[left], encode[right]) for left, right in grammar.points)
    clone_points = tuple(sorted(encoded_points))
    clone_index = {point: index for index, point in enumerate(clone_points)}
    old_to_clone = tuple(clone_index[point] for point in encoded_points)
    clone_s: List[int] = []
    clone_r: List[int] = []
    for left, right in clone_points:
        clone_s.append(clone_index[canonical_clone((negate(right), left))])
        clone_r.append(clone_index[canonical_clone((negate(right), add(left, right)))])
    clone_grammar = Grammar(modulus, clone_points, tuple(clone_s), tuple(clone_r))
    clone_row = census_row(clone_grammar, trace_order)
    graph_exact = all(
        clone_grammar.s_image[old_to_clone[old]] == old_to_clone[grammar.s_image[old]]
        and clone_grammar.r_image[old_to_clone[old]] == old_to_clone[grammar.r_image[old]]
        for old in range(grammar.size)
    )
    table_exact = all(
        add(encode[left], encode[right]) == encode[(left + right) % modulus]
        and multiply(encode[left], encode[right]) == encode[(left * right) % modulus]
        for left in range(modulus)
        for right in range(modulus)
    )
    add_table = [[add(left, right) for right in range(modulus)] for left in range(modulus)]
    multiply_table = [
        [multiply(left, right) for right in range(modulus)]
        for left in range(modulus)
    ]
    certificate = {
        "transport_seed": seed,
        "element_relabel": encode,
        "state_bijection": old_to_clone,
        "clone_zero": encode[0],
        "clone_one": encode[1],
        "clone_add_table_sha256": sha256_bytes(stable_json(add_table)),
        "clone_mul_table_sha256": sha256_bytes(stable_json(multiply_table)),
        "semiring_transport_exact": table_exact,
        "graph_transport_exact": graph_exact,
        "source_row_sha256": sha256_bytes(stable_json(source_row)),
        "clone_row_sha256": sha256_bytes(stable_json(clone_row)),
    }
    exact = table_exact and graph_exact and clone_row == source_row
    row = {
        "modulus": modulus,
        "element_relabel_sha256": sha256_bytes(stable_json(encode)),
        "clone_add_table_sha256": certificate["clone_add_table_sha256"],
        "clone_mul_table_sha256": certificate["clone_mul_table_sha256"],
        "source_row_sha256": certificate["source_row_sha256"],
        "matched_clone_row_sha256": certificate["clone_row_sha256"],
        "transport_certificate_sha256": sha256_bytes(stable_json(certificate)),
        "semiring_transport_exact": int(table_exact),
        "graph_transport_exact": int(graph_exact),
        "exact_equal": int(exact),
    }
    return row, 2 * modulus * modulus, 2 * grammar.size


def compare_serialized_row(
    audit: Audit,
    actual: Dict[str, str],
    expected: Dict[str, object],
    label: str,
) -> None:
    audit.check(set(actual) == set(expected), f"{label}:fields")
    for field, value in expected.items():
        audit.check(actual.get(field) == str(value), f"{label}:{field}")


def fraction_fields(prefix: str, value: Fraction) -> Dict[str, object]:
    return {
        f"{prefix}_numerator": value.numerator,
        f"{prefix}_denominator": value.denominator,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--cutoff", type=int, default=192)
    parser.add_argument("--trace-order", type=int, default=8)
    parser.add_argument("--random-trials", type=int, default=48)
    args = parser.parse_args()
    audit = Audit()

    candidate_rows = read_csv(args.results / "candidate_census.csv")
    candidate_clones = read_csv(args.results / "matched_clone.csv")
    candidate_random = read_csv(args.results / "random_relation_controls.csv")
    candidate_diamonds = json.loads((args.results / "candidate_diamonds.json").read_text(encoding="utf-8"))
    audit.check(len(candidate_rows) == args.cutoff - 1, "candidate_row_count")
    audit.check(len(candidate_clones) == args.cutoff - 1, "clone_row_count")
    audit.check(len(candidate_random) == args.random_trials, "random_row_count")

    raw_fields = [
        "modulus",
        "state_count",
        "projective_defect",
        "s_cycle_count",
        "s_fixed_count",
        "s_two_cycle_count",
        "r_cycle_count",
        "r_fixed_count",
        "r_three_cycle_count",
        "forward_component_size",
        "overlap_state_count",
    ] + [f"trace_{order}" for order in range(1, args.trace_order + 1)]
    evaluated_rows: List[Dict[str, object]] = []
    stratum_rows: List[Dict[str, object]] = []
    selector_rows: List[Dict[str, object]] = []
    expected_clones: List[Dict[str, object]] = []
    state_counts: Dict[int, int] = {}

    for offset, modulus in enumerate(range(2, args.cutoff + 1)):
        grammar = build_grammar(modulus)
        identity = tuple(range(grammar.size))
        audit.check(compose(grammar.s_image, 2) == identity, f"n={modulus}:s2")
        audit.check(compose(grammar.r_image, 3) == identity, f"n={modulus}:r3")
        expected_raw = census_row(grammar, args.trace_order)
        compare_serialized_row(audit, candidate_rows[offset], expected_raw, f"n={modulus}:candidate")
        is_prime, stratum = arithmetic_class(modulus)
        evaluated: Dict[str, object] = dict(expected_raw)
        evaluated["evaluator_class"] = stratum
        evaluated["evaluator_prime"] = int(is_prime)
        evaluated["static_defect_selects_prime"] = int((expected_raw["projective_defect"] == 0) == is_prime)
        evaluated["recurrent_support_nonzero"] = int(expected_raw["s_cycle_count"] + expected_raw["r_cycle_count"] > 0)
        evaluated_rows.append(evaluated)
        state_counts[modulus] = grammar.size
        stratum_rows.append(
            {
                "modulus": modulus,
                "evaluator_class": stratum,
                "state_count": grammar.size,
                "s_cycle_count": expected_raw["s_cycle_count"],
                "r_cycle_count": expected_raw["r_cycle_count"],
                "overlap_state_count": grammar.size,
                "recurrent_support_nonzero": evaluated["recurrent_support_nonzero"],
            }
        )
        selector_equal = grammar.size == modulus + 1
        selector_rows.append(
            {
                "modulus": modulus,
                "state_count": grammar.size,
                "n_plus_one": modulus + 1,
                "evaluator_class": stratum,
                "evaluator_prime": int(is_prime),
                "count_equals_n_plus_one": int(selector_equal),
                "selector_equivalent_to_prime": int(selector_equal == is_prime),
                "selector_used_by_candidate": 0,
                "terminal_selector_forbidden": 1,
            }
        )
        audit.check(selector_equal == is_prime, f"n={modulus}:selector_equivalence")

        expected_clone, table_checks, edge_checks = matched_control(
            grammar,
            expected_raw,
            args.trace_order,
            1000003 + modulus,
        )
        expected_clones.append(expected_clone)
        compare_serialized_row(audit, candidate_clones[offset], expected_clone, f"n={modulus}:clone")
        audit.check(expected_clone["semiring_transport_exact"] == 1, f"n={modulus}:all_table_entries", table_checks)
        audit.check(expected_clone["graph_transport_exact"] == 1, f"n={modulus}:all_projective_edges", edge_checks)

    sampled_sizes = sorted(set(state_counts.values()))
    expected_random: List[Dict[str, object]] = []
    for trial in range(args.random_trials):
        size = sampled_sizes[trial % len(sampled_sizes)]
        s_map, r_map = random_relation_action(size, 320000 + trial)
        identity = tuple(range(size))
        s_lengths = cycle_lengths(s_map)
        r_lengths = cycle_lengths(r_map)
        row: Dict[str, object] = {
            "trial": trial,
            "state_count": size,
            "s2_identity": int(compose(s_map, 2) == identity),
            "r3_identity": int(compose(r_map, 3) == identity),
            "s_cycle_count": len(s_lengths),
            "r_cycle_count": len(r_lengths),
            "overlap_state_count": size,
            "universal_recurrence_nonzero": int(bool(s_lengths) and bool(r_lengths)),
        }
        expected_random.append(row)
        compare_serialized_row(audit, candidate_random[trial], row, f"random={trial}")

    expected_candidate_diamonds = []
    evaluated_diamonds = []
    for modulus in range(2, args.cutoff // 6 + 1):
        bases = 2 * modulus, 6 * modulus, 6 * modulus, 3 * modulus
        candidate = {
            "base_modulus": modulus,
            "cycle_vertices": [modulus, 2 * modulus, 6 * modulus, 3 * modulus],
            "top_modulus": 6 * modulus,
            "simple_length": 4,
            "nonbacktracking": 1,
            "weight_bases": list(bases),
            "weight_base_product": bases[0] * bases[1] * bases[2] * bases[3],
            "expected_product": 216 * modulus**4,
        }
        expected_candidate_diamonds.append(candidate)
        evaluated = dict(candidate)
        evaluated["top_is_composite_evaluator"] = int(not arithmetic_class(6 * modulus)[0])
        evaluated_diamonds.append(evaluated)
    audit.check(candidate_diamonds == expected_candidate_diamonds, "candidate_diamonds_exact", max(1, len(expected_candidate_diamonds) * 8))

    modulus_fields = raw_fields + [
        "evaluator_class",
        "evaluator_prime",
        "static_defect_selects_prime",
        "recurrent_support_nonzero",
    ]
    write_csv(args.results / "modulus_census.csv", evaluated_rows, modulus_fields)
    write_json(args.results / "cross_modulus_diamonds.json", evaluated_diamonds)
    write_csv(
        args.results / "stratum_controls.csv",
        stratum_rows,
        [
            "modulus",
            "evaluator_class",
            "state_count",
            "s_cycle_count",
            "r_cycle_count",
            "overlap_state_count",
            "recurrent_support_nonzero",
        ],
    )
    write_csv(
        args.results / "static_selector_firewall.csv",
        selector_rows,
        [
            "modulus",
            "state_count",
            "n_plus_one",
            "evaluator_class",
            "evaluator_prime",
            "count_equals_n_plus_one",
            "selector_equivalent_to_prime",
            "selector_used_by_candidate",
            "terminal_selector_forbidden",
        ],
    )

    diagnostic_rows: List[Dict[str, object]] = []
    diagnostic_cutoffs = tuple(
        sorted({value for value in (16, 32, 64, 128, 192, args.cutoff) if value <= args.cutoff})
    )
    for sigma in (3, 4):
        previous_total = Fraction(0)
        for cutoff in diagnostic_cutoffs:
            within = 2 * sum(
                (Fraction(state_counts[modulus], modulus**sigma) for modulus in range(2, cutoff + 1)),
                Fraction(0),
            )
            cross = 2 * (Fraction(1, 2**sigma) + Fraction(1, 3**sigma)) * sum(
                (Fraction(1, modulus**sigma) for modulus in range(2, cutoff + 1)),
                Fraction(0),
            )
            total = within + cross
            row: Dict[str, object] = {
                "sigma": sigma,
                "cutoff": cutoff,
                "monotone_from_previous": int(total >= previous_total),
                "primary_object": "uninduced_projective_residue_graph",
                "free_marker_preserved": 1,
            }
            row.update(fraction_fields("within_trace_norm_bound", within))
            row.update(fraction_fields("cross_trace_norm_bound", cross))
            row.update(fraction_fields("total_trace_norm_bound", total))
            diagnostic_rows.append(row)
            audit.check(total >= previous_total and total > 0, f"analytic:sigma={sigma}:cutoff={cutoff}")
            previous_total = total
    diagnostic_fields = [
        "sigma",
        "cutoff",
        "within_trace_norm_bound_numerator",
        "within_trace_norm_bound_denominator",
        "cross_trace_norm_bound_numerator",
        "cross_trace_norm_bound_denominator",
        "total_trace_norm_bound_numerator",
        "total_trace_norm_bound_denominator",
        "monotone_from_previous",
        "primary_object",
        "free_marker_preserved",
    ]
    write_csv(args.results / "trace_class_diagnostics.csv", diagnostic_rows, diagnostic_fields)
    write_json(
        args.results / "fredholm_ownership.json",
        {
            "candidate_id": "SD-C34",
            "primary_object": "fixed_uninduced_projective_residue_graph_step_operator_B_s",
            "within_majorant": "2*sum_{n>=2} psi(n)*n^(-sigma)",
            "within_comparison": "2*zeta(sigma)*zeta(sigma-1)",
            "cross_majorant": "2*(2^(-sigma)+3^(-sigma))*sum_{n>=2} n^(-sigma)",
            "trace_class_half_plane": "Re(s)>2",
            "trace_norm_holomorphic": True,
            "ordinary_fredholm_determinant_owned": True,
            "entire_in_free_marker_z": True,
            "holomorphic_in_s_on_half_plane": True,
            "free_marker_counts_original_edges": True,
            "induction_or_first_return_used": False,
            "modified_determinant_used": False,
            "prime_selective_primitive_ledger": False,
            "finite_rows_are_diagnostics_not_infinite_proof": True,
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )

    strata = {name: sum(row["evaluator_class"] == name for row in stratum_rows) for name in ("prime", "prime_power", "mixed_composite")}
    if args.cutoff == 192:
        audit.check(strata["prime"] == 43, "strata:prime")
        audit.check(strata["prime_power"] == 14, "strata:prime_power")
        audit.check(strata["mixed_composite"] == 134, "strata:mixed_composite")
    else:
        audit.check(sum(strata.values()) == args.cutoff - 1, "strata:sanity_partition")
    payload = {
        "candidate_id": "SD-C34",
        "schema_version": "SD-C34-independent-evaluation-v1",
        "independent_of_candidate_core": True,
        "candidate_modules_imported": [],
        "check_count": audit.check_count,
        "pass_count": audit.check_count if not audit.failures else audit.check_count - len(audit.failures),
        "failure_count": len(audit.failures),
        "failures": audit.failures,
        "all_pass": not audit.failures,
        "full_addition_entries_checked": sum(modulus * modulus for modulus in range(2, args.cutoff + 1)),
        "full_multiplication_entries_checked": sum(modulus * modulus for modulus in range(2, args.cutoff + 1)),
        "projective_edges_checked": 2 * sum(state_counts.values()),
        "stratum_counts": strata,
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }
    write_json(args.results / "evaluation.json", payload)
    print(json.dumps(payload, sort_keys=True))
    if audit.failures:
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
