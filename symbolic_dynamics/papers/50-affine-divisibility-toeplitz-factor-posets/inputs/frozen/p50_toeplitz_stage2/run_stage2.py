#!/usr/bin/env python3
"""Deterministic Stage-2 evidence generator and test runner."""

from __future__ import annotations

import argparse
import hashlib
import json
from math import lcm
from pathlib import Path

import impl_formula as formula
import impl_holefill as holefill


AS_OF_DATE = "2026-08-20"
EXPECTED_STAGE1_MANIFEST_SHA256 = (
    "7fd51d53d077e3d7e0af905eda6bf2d15ee9aa64d6459bf3dcfa1dc282d97ec8"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def freeze_stage1(stage1: Path) -> dict:
    manifest = stage1 / "SHA256SUMS.txt"
    manifest_sha = sha256(manifest)
    if manifest_sha != EXPECTED_STAGE1_MANIFEST_SHA256:
        raise AssertionError((manifest_sha, EXPECTED_STAGE1_MANIFEST_SHA256))
    entries: list[dict[str, str]] = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        expected, name = line.split(maxsplit=1)
        name = name.lstrip("*")
        path = stage1 / name
        actual = sha256(path)
        if actual != expected:
            raise AssertionError(f"Stage-1 hash mismatch: {name}")
        entries.append({"path": name, "sha256": actual})
    return {
        "input_directory": str(stage1),
        "manifest_path": "SHA256SUMS.txt",
        "manifest_sha256": manifest_sha,
        "files": entries,
        "verification": "ALL_MATCH",
    }


def smallest_prime_divisor(n: int) -> int:
    for d in range(2, n + 1):
        if n % d == 0 and all(d % q for q in range(2, int(d**0.5) + 1)):
            return d
    raise AssertionError("no prime divisor")


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


def falling_factorial(q: int, k: int) -> int:
    value = 1
    for j in range(k):
        value *= q - j
    return value


def validate_declared_map(
    source_p: int,
    target_p: int,
    source: tuple[int, ...],
    target: tuple[int, ...],
    letter_map: dict[int, int],
    declared_target_alphabet: set[int],
    pointed: bool,
) -> str:
    if source_p != target_p:
        return "REJECT_WRONG_BASE_OUT_OF_SCOPE"
    if not pointed:
        return "REJECT_NONPOINTED_OUT_OF_SCOPE"
    if set(letter_map) != set(source):
        return "REJECT_INCOMPLETE_LETTER_MAP_DOMAIN"
    if set(letter_map.values()) != declared_target_alphabet:
        return "REJECT_LETTER_MAP_NOT_SURJECTIVE"
    if set(target) != declared_target_alphabet:
        return "REJECT_TARGET_NOT_EXACT_SUPPORT"
    horizon = lcm(len(source), len(target))
    if any(
        target[n % len(target)] != letter_map[source[n % len(source)]]
        for n in range(horizon)
    ):
        return "REJECT_DIRECTIVE_NOT_LETTER_IMAGE"
    if any(target[i] == target[(i + 1) % len(target)] for i in range(len(target))):
        return "REJECT_QUOTIENT_NOT_CYCLIC_NEIGHBOR_DISTINCT"
    if formula.least_period(target) < 2:
        return "REJECT_TARGET_LEAST_PERIOD_LT_2"
    return "ACCEPT_FROZEN_FAMILY_POINTED_FACTOR"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage1", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    evidence_dir = args.output / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)

    input_lock = freeze_stage1(args.stage1)
    write_json(evidence_dir / "input_hashes.json", input_lock)

    assertions: list[str] = []
    controls = ((0, 1), (0, 1, 2), (0, 1, 0, 2), (0, 1, 2, 1))

    # Independent point evaluation.
    point_comparisons = 0
    for p in range(3, 11):
        for directive in controls:
            for k in range(-1000, 1001):
                if formula.value(p, directive, k) != holefill.fill_value(p, directive, k):
                    raise AssertionError(("point", p, directive, k))
                point_comparisons += 1
            for n in range(19):
                center_a = formula.hole_residue(p, n)
                center_b = holefill.center_by_recurrence(p, n)
                if center_a != center_b:
                    raise AssertionError(("center", p, n))
                for offset in range(-3, 4):
                    if formula.value(p, directive, center_a + offset) != holefill.fill_value(
                        p, directive, center_b + offset
                    ):
                        raise AssertionError(("center-value", p, directive, n, offset))
                    point_comparisons += 1
    assertions.append("direct_formula_equals_nested_hole_fill")

    # Exact skeleton formula with independent finite observations.
    skeleton_cases: list[dict] = []
    skeleton_residues = 0
    for p in range(3, 11):
        directive = (0, 1, 2)
        for n in range(1, 5):
            direct = formula.skeleton_certificate(p, directive, n)
            nested = holefill.skeleton_sample(p, directive, n)
            for field in ("N", "hole_residue", "modulus", "periodic_residue_count"):
                if direct[field] != nested[field]:
                    raise AssertionError(("skeleton", p, n, field))
            skeleton_residues += direct["modulus"]
            skeleton_cases.append(
                {
                    "N": n,
                    "hole_residue": direct["hole_residue"],
                    "modulus": direct["modulus"],
                    "p": p,
                }
            )
    assertions.append("exact_unique_hole_residue_reproduced")

    # High-center identity, including composite bases and negative offsets.
    center_lemma_cases = 0
    for p in range(3, 11):
        for j in range(-40, 41):
            if j == 0:
                continue
            e = formula.divexp(p, j)
            for n in (e + 1, e + 2, e + 5):
                if not formula.center_lemma_holds(p, j, n):
                    raise AssertionError(("center-lemma", p, j, n))
                center = formula.hole_residue(p, n)
                expected = (0, 1, 2)[e % 3]
                if formula.value(p, (0, 1, 2), center + j) != expected:
                    raise AssertionError(("center-formula", p, j, n))
                if holefill.fill_value(p, (0, 1, 2), center + j) != expected:
                    raise AssertionError(("center-holefill", p, j, n))
                center_lemma_cases += 1
    assertions.append("high_center_identity_prime_and_composite")

    # Prime constructiveness: every smaller candidate period gets an exact witness.
    prime_specs = {3: 4, 5: 3, 7: 3}
    prime_rejections = 0
    prime_common_period_samples = 0
    prime_case_records: list[dict] = []
    for p, max_n in prime_specs.items():
        if not is_prime(p):
            raise AssertionError(p)
        for n in range(1, max_n + 1):
            rejected_here = 0
            for q in range(1, p ** (n + 1)):
                witness = formula.prime_smaller_period_witness(p, (0, 1, 2), n, q)
                c = witness["center"]
                t = witness["multiplier"]
                if holefill.fill_value(p, (0, 1, 2), c) == holefill.fill_value(
                    p, (0, 1, 2), c + t * q
                ):
                    raise AssertionError(("independent-prime-witness", p, n, q))
                prime_rejections += 1
                rejected_here += 1
            common = p ** (n + 1)
            prime_common_period_samples += formula.block_common_period_sample(
                p, (0, 1, 2), n, common, -2, 2
            )
            prime_case_records.append(
                {
                    "N": n,
                    "least_common_period": common,
                    "p": p,
                    "smaller_candidates_rejected": rejected_here,
                }
            )
    assertions.append("prime_constructive_period_witnesses_complete_within_bounds")

    # Composite counterperiods: ell*p**N is strictly below p**(N+1).
    composite_records: list[dict] = []
    composite_comparisons = 0
    composite_nested_fill_comparisons = 0
    for p in (4, 6, 8, 9, 10, 12):
        ell = smallest_prime_divisor(p)
        for n in range(1, 4):
            q = ell * p**n
            if not q < p ** (n + 1):
                raise AssertionError((p, n, q))
            comparisons = formula.block_common_period_sample(
                p, (0, 1, 2), n, q, -(p * p), p * p
            )
            for k in range(p**n):
                expected = holefill.fill_value(p, (0, 1, 2), k)
                for t in range(-10, 11):
                    if holefill.fill_value(p, (0, 1, 2), k + t * q) != expected:
                        raise AssertionError(("composite-holefill", p, n, k, t))
                    composite_nested_fill_comparisons += 1
            composite_comparisons += comparisons
            composite_records.append(
                {
                    "N": n,
                    "counterperiod": q,
                    "p": p,
                    "prime_divisor": ell,
                    "strictly_below_next_power": True,
                }
            )
    assertions.append("composite_constructiveness_counterperiods")

    # Directive and admissible-partition enumeration by independent algorithms.
    directives_a = formula.enumerate_directives(6, 4)
    directives_b = holefill.enumerate_directives(6, 4)
    if directives_a != directives_b:
        raise AssertionError("directive enumerators disagree")
    partition_checks = 0
    admissible_partition_total = 0
    chromatic_q_evaluations = 0
    graphical_summary: list[dict] = []
    for directive in directives_a:
        n = max(directive) + 1
        partitions_a = formula.enumerate_partitions(n)
        partitions_b = holefill.enumerate_partitions(n)
        if partitions_a != partitions_b:
            raise AssertionError(("partition-enumeration", directive))
        counts_a = formula.graphical_stirling_counts(directive)
        counts_b = holefill.graphical_stirling_counts(directive)
        if counts_a != counts_b:
            raise AssertionError(("graphical-stirling", directive))
        for partition in partitions_a:
            admissible = formula.partition_is_admissible(directive, partition)
            if admissible:
                quotient = formula.quotient_directive(directive, partition)
                if not formula.is_frozen_directive(quotient):
                    raise AssertionError(("bad-admissible-quotient", directive, partition))
                admissible_partition_total += 1
            partition_checks += 1
        chromatic_values: dict[str, int] = {}
        for q in range(7):
            chromatic_q_evaluations += 1
            direct_colorings = formula.proper_coloring_count(directive, q)
            recursive_colorings = holefill.proper_coloring_count(directive, q)
            stirling_expansion = sum(
                count * falling_factorial(q, k) for k, count in counts_a.items()
            )
            if direct_colorings != recursive_colorings:
                raise AssertionError(("proper-coloring-implementations", directive, q))
            if direct_colorings != stirling_expansion:
                raise AssertionError(("chromatic-stirling-identity", directive, q))
            chromatic_values[str(q)] = direct_colorings
        chromatic = min(counts_a)
        binary_exists = 2 in counts_a
        if binary_exists != (chromatic == 2):
            raise AssertionError(("binary-chromatic", directive))
        graphical_summary.append(
            {
                "alphabet_size": n,
                "chromatic_number": chromatic,
                "chromatic_polynomial_values_q_0_through_6": chromatic_values,
                "directive": list(directive),
                "graphical_stirling": {str(k): v for k, v in counts_a.items()},
            }
        )
    assertions.append("directive_partition_and_graphical_counts_independent")
    assertions.append("graphical_stirling_chromatic_identity_bounded")

    # Exhaustive bounded local-rule constraints over all frozen directives in bounds.
    local_a = [d for d in directives_a if len(d) <= 5 and max(d) + 1 <= 3]
    local_b = holefill.enumerate_directives(5, 3)
    if local_a != local_b:
        raise AssertionError("bounded local directive enumerators disagree")
    local_cases = 0
    local_consistent = 0
    local_quotients = 0
    max_observed_windows = 0
    for p in (3, 4, 5):
        for radius in range(4):
            for source in local_a:
                for target in local_a:
                    depth = max(16, 2 * lcm(len(source), len(target)) + radius + 2)
                    result_a = formula.local_constraint(
                        p, source, target, radius, 128, depth
                    )
                    result_b = holefill.local_constraint(
                        p, source, target, radius, 128, depth
                    )
                    if result_a != result_b:
                        raise AssertionError(("local-implementations", p, radius, source, target))
                    if result_a["consistent"] != result_a["is_surjective_letter_quotient"]:
                        raise AssertionError(("local-rigidity", p, radius, source, target, result_a))
                    local_cases += 1
                    local_consistent += int(result_a["consistent"])
                    local_quotients += int(result_a["is_surjective_letter_quotient"])
                    max_observed_windows = max(
                        max_observed_windows, result_a["observed_window_count"]
                    )
    assertions.append("bounded_local_rules_match_exact_letter_quotients")

    # Typed negative controls.
    negative_controls: list[dict] = []
    reason = validate_declared_map(
        3,
        3,
        (0, 1, 2),
        (0, 1, 1),
        {0: 0, 1: 1, 2: 1},
        {0, 1, 2},
        True,
    )
    negative_controls.append({"control": "non_surjective_map", "result": reason})
    reason = validate_declared_map(
        3,
        3,
        (0, 1, 2),
        (0, 0, 1),
        {0: 0, 1: 0, 2: 1},
        {0, 1},
        True,
    )
    negative_controls.append({"control": "adjacent_letter_merge", "result": reason})
    reason = validate_declared_map(
        3, 4, (0, 1), (0, 1), {0: 0, 1: 1}, {0, 1}, True
    )
    wrong_base_witness = next(
        k
        for k in range(-100, 101)
        if formula.value(3, (0, 1), k) != formula.value(4, (0, 1), k)
    )
    negative_controls.append(
        {
            "control": "wrong_base",
            "mismatch_coordinate": wrong_base_witness,
            "result": reason,
        }
    )
    reason = validate_declared_map(
        3, 3, (0, 1), (0, 1), {0: 0, 1: 1}, {0, 1}, False
    )
    shift_witness = next(
        k
        for k in range(-100, 101)
        if formula.value(3, (0, 1), k + 1) != formula.value(3, (0, 1), k)
    )
    negative_controls.append(
        {
            "control": "nonpointed_shift",
            "basepoint_mismatch_coordinate": shift_witness,
            "result": reason,
        }
    )
    expected_reasons = {
        "REJECT_LETTER_MAP_NOT_SURJECTIVE",
        "REJECT_NONPOINTED_OUT_OF_SCOPE",
        "REJECT_QUOTIENT_NOT_CYCLIC_NEIGHBOR_DISTINCT",
        "REJECT_WRONG_BASE_OUT_OF_SCOPE",
    }
    if {item["result"] for item in negative_controls} != expected_reasons:
        raise AssertionError(negative_controls)
    assertions.append("typed_negative_controls_rejected_for_exact_reasons")

    evidence = {
        "as_of_date": AS_OF_DATE,
        "constructiveness": {
            "composite_block_comparisons": composite_comparisons,
            "composite_nested_fill_comparisons": composite_nested_fill_comparisons,
            "composite_counterperiod_cases": composite_records,
            "prime_block_period_sample_comparisons": prime_common_period_samples,
            "prime_cases": prime_case_records,
            "prime_smaller_period_candidates_rejected": prime_rejections,
        },
        "directive_and_partition_enumeration": {
            "admissible_partition_total_across_directives": admissible_partition_total,
            "chromatic_q_0_through_6_evaluations": chromatic_q_evaluations,
            "directive_count": len(directives_a),
            "graphical_summary": graphical_summary,
            "max_alphabet": 4,
            "max_directive_period": 6,
            "partition_checks": partition_checks,
        },
        "high_center": {"identity_cases": center_lemma_cases},
        "independent_implementations": {
            "formula_module": "impl_formula.py",
            "hole_fill_module": "impl_holefill.py",
            "point_value_comparisons": point_comparisons,
        },
        "local_rule_search": {
            "candidate_directive_count": len(local_a),
            "consistent_cases": local_consistent,
            "dense_radius": 128,
            "false_negative_count": local_quotients - local_consistent,
            "false_positive_count": local_consistent - local_quotients,
            "max_directive_period": 5,
            "max_observed_window_count": max_observed_windows,
            "p_values": [3, 4, 5],
            "quotient_cases": local_quotients,
            "radii": [0, 1, 2, 3],
            "source_target_radius_base_cases": local_cases,
        },
        "negative_controls": negative_controls,
        "skeleton": {
            "cases": skeleton_cases,
            "p_values": list(range(3, 11)),
            "residue_classes_checked": skeleton_residues,
        },
        "scope": {
            "cross_base": "EXCLUDED",
            "nonpointed": "EXCLUDED",
            "object": "same-base pointed p-divisibility simple-Toeplitz family",
        },
    }
    test_results = {
        "assertion_count": len(assertions),
        "assertions": assertions,
        "status": "PASS",
    }
    write_json(evidence_dir / "canonical_evidence.json", evidence)
    write_json(evidence_dir / "test_results.json", test_results)
    print(json.dumps({"status": "PASS", "summary": evidence, "tests": test_results}, sort_keys=True))


if __name__ == "__main__":
    main()
