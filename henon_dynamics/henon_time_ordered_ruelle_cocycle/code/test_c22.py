"""Regression and mutation tests for the HCS-C22 T1--T3 package."""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import sys
from copy import deepcopy
from fractions import Fraction
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CODE_DIR.parent


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, CODE_DIR / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


producer = load_module("c22_producer_test_module", "c22_producer.py")
checker = load_module("c22_independent_checker_test_module", "c22_independent_check.py")


def test_t1_exact_common_geometry() -> None:
    result = producer.t1_geometry_certificate()
    assert all(result["decisions"].values())
    assert result["minimum_covering_margin"]["fraction"] == "7/720"
    assert result["minimum_forbidden_gap"]["fraction"] == "217/720"
    assert result["signed_root"]["contraction_squared"]["fraction"] == "240/1003"
    assert result["cone"]["forward_denominator"]["fraction"] == "11371/3360"
    assert result["cone"]["backward_denominator"]["fraction"] == "6361/1968"


def test_joint_counts_and_frozen_hashes() -> None:
    result = producer.joint_combinatorics(10)
    assert result["pass"]
    rows = result["period_rows"]
    assert [row["state_fixed_words"] for row in rows] == [1, 1, 4, 9, 11, 16, 29, 49, 76, 121]
    assert [row["primitive_joint_necklaces"] for row in rows] == [2, 1, 10, 35, 70, 165, 530, 1550, 4320, 12355]
    assert rows[6]["canonical_ids_sha256"] == "3b4c3610a568181e494c5f5302b42c16793840aa6f06e3635443bbd8d408cdfc"
    assert rows[7]["canonical_ids_sha256"] == "65105f5879c1f207c20e46c8198d1eb3881db03d12761f318fa316817a36e51d"
    assert rows[9]["joint_orbits_by_base_least_period"] == {
        "1": 22,
        "2": 24,
        "5": 330,
        "10": 11979,
    }


def test_joint_canonicalization_is_not_separate_canonicalization() -> None:
    witness = None
    for base in itertools.product((0, 1), repeat=5):
        for signs in itertools.product((-1, 1), repeat=5):
            if not producer.admissible_sign_word(signs):
                continue
            joint = producer.joint_canonical(base, signs)
            separate = (min(producer.rotations(base)), min(producer.rotations(signs)))
            if joint != separate:
                witness = (base, signs, joint, separate)
                break
        if witness is not None:
            break
    assert witness is not None


def test_witnesses_are_minimal_and_complete() -> None:
    bigram = producer.minimal_matched_pair(2)
    trigram = producer.minimal_matched_pair(3)
    assert (bigram["period"], bigram["left"], bigram["right"]) == (
        7,
        "0000101",
        "0001001",
    )
    assert (trigram["period"], trigram["left"], trigram["right"]) == (
        8,
        "00101011",
        "00101101",
    )
    assert len(producer.all_admissible_sign_words(7)) == 29
    assert len(producer.all_admissible_sign_words(8)) == 49


def test_reversal_state_formula() -> None:
    signs = (-1, 1, 1, -1, -1, 1, -1)
    states = producer.state_word(signs)
    reversed_signs = signs[::-1]
    reversed_states = producer.state_word(reversed_signs)
    swap = {0: 0, 1: 2, 2: 1, 3: 3}
    expected = tuple(swap[states[-index % len(states)]] for index in range(len(states)))
    assert reversed_states == expected


def test_finite_field_and_t3_controls() -> None:
    finite = producer.finite_field_witness()
    assert finite["pass"]
    assert [record["trace"] for record in finite["records"]] == [15, 18]
    symbolic = producer.t3_symbolic_certificate()
    assert symbolic["pass"]
    assert symbolic["global_unit_numerator_residue_determinant"] == "1"
    assert symbolic["global_unit_numerator_residue_sum"] == "0"
    assert symbolic["local_symbolic_bare_denominator"] == "-(4*z**2 + 1)*(4*z**2 + 2*z - 1)"


def test_released_artifacts_are_hash_bound() -> None:
    certificate_path = PROJECT_ROOT / "results" / "c22_certificate.json"
    checker_path = PROJECT_ROOT / "results" / "c22_independent_check.json"
    assert certificate_path.exists()
    assert checker_path.exists()
    certificate_hash = hashlib.sha256(certificate_path.read_bytes()).hexdigest()
    checker = json.loads(checker_path.read_text(encoding="utf-8"))
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    assert checker["pass"] is True
    assert checker["producer_sha256"] == certificate_hash
    assert certificate["decisions"]["t1_pass"] is True
    assert certificate["decisions"]["t2_pass"] is True
    assert certificate["decisions"]["t3_pass"] is True


def test_fraction_windows_do_not_touch() -> None:
    assert Fraction(59, 10) - Fraction(289, 50) == Fraction(3, 25)
    assert Fraction(99, 16) - Fraction(61, 10) == Fraction(7, 80)
    assert Fraction(59, 10) - Fraction(144, 25) == Fraction(7, 50)
    assert Fraction(51, 8) - Fraction(61, 10) == Fraction(11, 40)


def test_endpoint_outside_certified_window_mutation_fails() -> None:
    geometry = producer.t1_geometry_certificate()
    mutated = deepcopy(geometry)
    mutated["parameter_interval"] = ["144/25", "61/10"]
    checks = checker.check_t1(mutated)
    assert checks["parameter_inside_derived_windows"] is False
    assert not all(checks.values())


def test_chronology_index_mutation_fails_interval_checker() -> None:
    certificate = json.loads(
        (PROJECT_ROOT / "results" / "c22_certificate.json").read_text(encoding="utf-8")
    )
    chronology = deepcopy(certificate["t2_joint_chronology"])
    branch = chronology["sectors"]["0000101"]["branches"][1]
    branch["center"] = list(reversed(branch["center"]))
    branch["coordinate_intervals"] = list(reversed(branch["coordinate_intervals"]))
    checks = checker.check_sectors(
        chronology,
        int(certificate["numerical_policy"]["sqrt_enclosure_decimal_digits"]),
    )
    assert checks["pass"] is False
    assert checks["branch_failure_count"] > 0


def test_deleted_certificate_coverage_fails_closed() -> None:
    certificate = json.loads(
        (PROJECT_ROOT / "results" / "c22_certificate.json").read_text(encoding="utf-8")
    )

    combinatorics = deepcopy(certificate["t2_joint_chronology"]["combinatorics"])
    combinatorics["period_rows"].pop()
    assert checker.check_joint_combinatorics(combinatorics)["period_coverage"] is False

    chronology = deepcopy(certificate["t2_joint_chronology"])
    chronology["comparisons"].pop()
    sector_checks = checker.check_sectors(
        chronology,
        int(certificate["numerical_policy"]["sqrt_enclosure_decimal_digits"]),
    )
    assert sector_checks["comparison_checks"]["comparison_coverage"] is False
    assert sector_checks["pass"] is False

    collapse = deepcopy(certificate["t3_global_collapse"])
    collapse["hill_rows"].pop()
    assert checker.check_t3(collapse)["hill_period_coverage"] is False
    assert not all(checker.check_t3(collapse).values())
