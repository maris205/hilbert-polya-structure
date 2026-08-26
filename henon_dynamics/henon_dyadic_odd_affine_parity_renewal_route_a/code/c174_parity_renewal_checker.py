#!/usr/bin/env python3
"""Independent exact checker for the C174 evidence artifact.

This module intentionally imports neither the producer nor any producer helper.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


SOURCE_COMMIT = "100e5f601a0196710d53784bdeef40d2bff89fa8"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATOR_PATH = "flow_systems/skills/route-a-evaluator.md"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
A_VALUES = (-5, -3, -1, 1, 3, 5)
B_VALUES = (-5, -3, -1, 1, 3, 5)
WORD_N_MAX = 8
PREFIX_LENGTH = 8
RETURN_K_MAX = 12
PERIOD_N_MAX = 16
ROOF_N_MAX = 32


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


def canonical_hash(payload: dict) -> str:
    clone = dict(payload)
    clone.pop("payload_sha256", None)
    raw = json.dumps(clone, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def digest_rows(rows: list[str]) -> str:
    return sha256(("\n".join(rows) + "\n").encode()).hexdigest()


def bits_of(word: int, n: int) -> tuple[int, ...]:
    return tuple((word // (2**j)) % 2 for j in range(n))


def dyadic_parity(value: Fraction) -> int:
    if value.denominator % 2 == 0:
        raise AssertionError("non-dyadic rational sentinel")
    return value.numerator % 2


def apply_map(value: Fraction, a: int, b: int) -> Fraction:
    if dyadic_parity(value) == 0:
        return value / 2
    return (a * value + b) / 2


def formula(bits: tuple[int, ...], a: int, b: int) -> tuple[int, int, Fraction]:
    total_ones = sum(bits)
    cumulative = 0
    polynomial = 0
    for position, digit in enumerate(bits):
        cumulative += digit
        if digit == 1:
            polynomial += (2**position) * (a ** (total_ones - cumulative))
    return total_ones, polynomial, Fraction(b * polynomial, 2 ** len(bits) - a**total_ones)


def inverse_finite_tail(bits: tuple[int, ...], a: int, b: int) -> Fraction:
    value = Fraction(0)
    ones_seen = 0
    for j, digit in enumerate(bits):
        ones_seen += digit
        if digit:
            value -= Fraction(b * 2**j, a**ones_seen)
    return value


def mu(n: int) -> int:
    original = n
    prime_count = 0
    p = 2
    while p * p <= original:
        if original % p == 0:
            original //= p
            prime_count += 1
            if original % p == 0:
                return 0
            while original % p == 0:
                original //= p
        p += 1
    if original > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def all_divisors(n: int) -> list[int]:
    return [candidate for candidate in range(1, n + 1) if n % candidate == 0]


def value_2_of_integer(number: int) -> int:
    if number == 0:
        raise ValueError("v_2(0) is infinite")
    count = 0
    number = abs(number)
    while number % 2 == 0:
        number //= 2
        count += 1
    return count


def check_evidence(payload: dict, repo_root: Path) -> int:
    a = Audit()
    a.check(payload["schema"] == "hcs-c174-dyadic-odd-affine-parity-renewal-v1", "schema")
    a.check(payload["candidate_id"] == "HCS-C174", "candidate")
    a.check(payload["evaluation_date"] == "2026-08-26", "date")
    a.check(payload["scope_literal"] == SCOPE, "scope")
    a.check(payload["source_commit"] == SOURCE_COMMIT, "commit")
    a.check(payload["payload_sha256"] == canonical_hash(payload), "payload hash")
    evaluator = payload["evaluator"]
    a.check(evaluator["skill_version"] == "0.2.0", "evaluator version")
    a.check(evaluator["authority_path"] == EVALUATOR_PATH, "evaluator path")
    a.check(evaluator["authority_sha256"] == EVALUATOR_SHA256, "evaluator declared hash")
    authority = repo_root / EVALUATOR_PATH
    a.check(authority.is_file(), "evaluator file exists")
    a.check(sha256(authority.read_bytes()).hexdigest() == EVALUATOR_SHA256, "evaluator file hash")
    a.check(
        payload["artifact_path_base"]
        == "henon_dynamics/henon_dyadic_odd_affine_parity_renewal_route_a",
        "artifact base",
    )

    lock = payload["source_lock"]
    a.check(lock["phase_space"] == "Z_2 with normalized Haar probability mu", "phase space")
    a.check(lock["parameter_family"] == "odd integers a and b, frozen before all validation", "parameters")
    a.check("dyadic local arithmetic" in lock["arithmetic_origin"], "arithmetic origin")
    a.check("one original-clock tick" in lock["clock"], "clock")
    a.check(lock["precision"].startswith("exact integers"), "precision")
    a.check(lock["training_data"] == "none", "training")
    a.check("Euler factors" in lock["forbidden_data"], "forbidden Euler")
    a.check("root numbers" in lock["forbidden_data"], "forbidden roots")
    cutoffs = lock["cutoffs"]
    a.check(tuple(cutoffs["a_values"]) == A_VALUES, "a grid")
    a.check(tuple(cutoffs["b_values"]) == B_VALUES, "b grid")
    a.check(cutoffs["word_n_max"] == WORD_N_MAX, "word cutoff")
    a.check(cutoffs["inverse_prefix_length"] == PREFIX_LENGTH, "prefix cutoff")
    a.check(cutoffs["return_k_max"] == RETURN_K_MAX, "return cutoff")
    a.check(cutoffs["period_n_max"] == PERIOD_N_MAX, "period cutoff")
    a.check(cutoffs["roof_n_max"] == ROOF_N_MAX, "roof cutoff")

    foundation = payload["classical_foundation"]
    a.check("classical prior work" in foundation["ownership"], "prior ownership")
    a.check("not a novelty claim" in foundation["ownership"], "no classical novelty claim")
    a.check(foundation["measure_statement"].endswith("Z_2"), "measure conjugacy")

    theorem = payload["fixed_word_theorem"]
    rows = theorem["aggregate_rows"]
    a.check(len(rows) == len(A_VALUES) * len(B_VALUES) * WORD_N_MAX, "fixed row count")
    row_index = 0
    fixed_words_checked = 0
    for av in A_VALUES:
        for bv in B_VALUES:
            for n in range(1, WORD_N_MAX + 1):
                row = rows[row_index]
                row_index += 1
                a.check((row["a"], row["b"], row["n"]) == (av, bv, n), "fixed row order")
                points: set[Fraction] = set()
                encoded: list[str] = []
                weighted_sum = Fraction(0)
                for word in range(2**n):
                    fixed_words_checked += 1
                    bits = bits_of(word, n)
                    ones, polynomial, point = formula(bits, av, bv)
                    a.check((2**n - av**ones) % 2 != 0, "unit fixed denominator")
                    state = point
                    seen: list[int] = []
                    for bit in bits:
                        actual = dyadic_parity(state)
                        seen.append(actual)
                        a.check(actual == bit, "word realization")
                        state = apply_map(state, av, bv)
                    a.check(state == point, "periodic return")
                    points.add(point)
                    numerator = 2**n - av**ones
                    a.check(value_2_of_integer(numerator) == 0, "stability numerator odd")
                    weighted_sum += Fraction(1, 2**n)
                    encoded.append(f"{word}:{''.join(map(str, bits))}:{ones}:{polynomial}:{point}")
                a.check(len(points) == 2**n, "fixed points distinct")
                a.check(row["fixed_point_count"] == 2**n, "row fixed count")
                a.check(row["expected_fixed_point_count"] == 2**n, "row expected count")
                a.check(Fraction(row["stability_weight_sum"]) == weighted_sum == 1, "weighted sum")
                a.check(row["word_point_digest"] == digest_rows(encoded), "fixed digest")
    a.check(row_index == len(rows), "all fixed rows consumed")
    a.check(theorem["fixed_point_count"] == "#Fix(T^n)=2^n for every n>=1", "global count statement")
    a.check(theorem["artin_mazur_zeta"] == "zeta_AM(z)=1/(1-2*z)", "AM zeta")
    a.check(theorem["parameter_blind"] is True, "unweighted blindness")

    inverse_rows = payload["inverse_conjugacy_sentinels"]["aggregate_rows"]
    a.check(len(inverse_rows) == len(A_VALUES) * len(B_VALUES), "inverse row count")
    inverse_index = 0
    inverse_prefixes_checked = 0
    for av in A_VALUES:
        for bv in B_VALUES:
            row = inverse_rows[inverse_index]
            inverse_index += 1
            a.check((row["a"], row["b"]) == (av, bv), "inverse row order")
            a.check(row["prefix_length"] == PREFIX_LENGTH, "inverse length")
            a.check(row["prefix_count"] == 2**PREFIX_LENGTH, "inverse count")
            encoded = []
            for word in range(2**PREFIX_LENGTH):
                inverse_prefixes_checked += 1
                bits = bits_of(word, PREFIX_LENGTH)
                point = inverse_finite_tail(bits, av, bv)
                state = point
                for bit in bits:
                    a.check(dyadic_parity(state) == bit, "inverse parity")
                    state = apply_map(state, av, bv)
                a.check(state == 0, "inverse zero tail")
                encoded.append(f"{word}:{point}")
            a.check(row["inverse_prefix_digest"] == digest_rows(encoded), "inverse digest")

    period_rows = payload["period_ledger"]
    a.check(len(period_rows) == PERIOD_N_MAX, "period ledger length")
    for n, row in enumerate(period_rows, start=1):
        primitive_points = sum(mu(n // d) * 2**d for d in all_divisors(n))
        a.check(row["n"] == n, "period n")
        a.check(row["fixed_points"] == 2**n, "period fixed count")
        a.check(row["exact_period_points"] == primitive_points, "Mobius inversion")
        a.check(primitive_points % n == 0, "cycle integrality")
        a.check(row["primitive_cycles"] == primitive_points // n, "primitive cycle count")
        a.check(row["stability_weighted_fixed_sum"] == "1", "period weighted sum")

    stability = payload["stability_theorem"]
    a.check(stability["weighted_fixed_sum"].endswith("=1"), "weighted identity")
    a.check(stability["weighted_zeta"] == "zeta_stab(z)=1/(1-z)", "weighted zeta")
    a.check(stability["parameter_blind"] is True, "weighted blindness")

    first = payload["first_return_theorem"]
    a.check("countable, Haar-null" in first["exceptional_set"], "exceptional set")
    a.check("full conditional Haar measure" in first["recurrent_domain"], "recurrent full measure")
    a.check(first["conditional_law"] == "mu_O(tau=k)=2^{-k}", "geometric law")
    a.check(first["ordinary_artin_mazur_status"].startswith("undefined"), "return AM undefined")
    return_rows = first["finite_rows"]
    a.check(len(return_rows) == len(A_VALUES) * len(B_VALUES) * RETURN_K_MAX, "return rows")
    return_index = 0
    for av in A_VALUES:
        for bv in B_VALUES:
            exceptional = Fraction(-bv, av)
            a.check(dyadic_parity(exceptional) == 1, "exceptional odd")
            a.check(apply_map(exceptional, av, bv) == 0, "exceptional maps zero")
            for k in range(1, RETURN_K_MAX + 1):
                row = return_rows[return_index]
                return_index += 1
                point = Fraction(bv, 2**k - av)
                a.check((row["a"], row["b"], row["k"]) == (av, bv, k), "return row order")
                a.check(Fraction(row["fixed_point"]) == point, "return fixed formula")
                image = av * point + bv
                a.check(value_2_of_integer(image.numerator) == k, "return valuation")
                a.check(image / 2**k == point, "return fixed point")
                a.check(row["return_time"] == k, "return time row")
                a.check(row["parity_block"] == "1" + "0" * (k - 1), "return block")
                a.check(Fraction(row["conditional_haar_probability"]) == Fraction(1, 2**k), "return law row")

    roof = payload["original_clock_recovery"]
    a.check(roof["first_return_series"] == "F(z)=sum_{k>=1} z^k=z/(1-z)", "renewal series")
    a.check(roof["roof_zeta"] == "zeta_roof(z)=1/(1-F(z))=(1-z)/(1-2*z)", "roof zeta")
    a.check(roof["recovery_identity"].endswith("=1/(1-2*z)"), "recovery identity")
    roof_rows = roof["finite_rows"]
    a.check(len(roof_rows) == ROOF_N_MAX, "roof rows")
    for n, row in enumerate(roof_rows, start=1):
        a.check(row["n"] == n, "roof n")
        a.check(row["roof_fixed_count"] == 2**n - 1, "roof count")
        a.check(row["zero_orbit_fixed_count"] == 1, "zero count")
        a.check(row["original_fixed_count"] == 2**n, "recovered count")

    operator = payload["operator_boundary"]
    a.check(operator["isometry"] is True and operator["surjective"] is False, "proper isometry")
    a.check(operator["wold_model"] == "U is unitarily equivalent to I_C direct_sum S^{(aleph_0)}", "Wold")
    a.check(operator["spectrum"] == "closed unit disk", "spectrum")
    a.check(operator["point_spectrum"] == ["1"], "point spectrum")
    a.check(operator["compact"] is False, "noncompact")
    a.check(operator["finite_schatten_class"] is False, "non-Schatten")
    a.check(operator["ordinary_fredholm_determinant_available"] is False, "no determinant")
    a.check("changes phase space" in operator["natural_extension"], "extension boundary")

    boundaries = payload["parameter_and_boundary_audit"]
    a.check("conjugates" in boundaries["b_redundancy"], "b conjugacy")
    a.check("leaves Z_2" in boundaries["even_a_boundary"], "even a boundary")
    a.check("leaves Z_2" in boundaries["even_b_boundary"], "even b boundary")
    cycle = boundaries["three_x_plus_one_boundary"]
    states = [Fraction(item) for item in cycle["z2_cycle"]]
    a.check(cycle["parameters"] == [3, 1], "3x+1 parameters")
    a.check(cycle["parity_word"] == "100", "3x+1 word")
    for before, after in zip(states[:-1], states[1:]):
        a.check(apply_map(before, 3, 1) == after, "3x+1 Z2 cycle")
    a.check(states[0] == states[-1], "3x+1 return")
    a.check("no progress" in cycle["claim"], "Collatz nonclaim")
    for av in A_VALUES:
        for bv in B_VALUES:
            for numerator in range(-7, 8, 2):
                y = Fraction(numerator, 15)
                left = apply_map(Fraction(bv) * y, av, bv)
                right = Fraction(bv) * apply_map(y, av, 1)
                a.check(left == right, "b multiplication conjugacy")

    route = payload["route_a"]
    a.check(route["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    a.check(route["overall"] == "ROUTE_A_REJECTED", "overall rejection")
    a.check(route["a0_override_rule"] == "A0 failure forces overall rejection", "A0 override")
    a.check(route["route_b_invocation_allowed"] is False, "no route B")
    claims = payload["claim_boundary"]
    a.check(claims["classical_parity_conjugacy_novelty"] is False, "prior-work boundary")
    a.check(claims["exact_renewal_and_roof_recovery_package"] is True, "main progress")
    for key in (
        "collatz_positive_integer_progress",
        "prime_like_correspondence",
        "target_divisor_matching",
        "target_functional_equation",
        "target_counting_law",
        "arithmetic_local_data",
        "euler_factors",
        "root_numbers",
        "automorphy",
        "hilbert_polya_operator",
    ):
        a.check(claims[key] is False, f"forbidden claim {key}")
    integrity = payload["integrity"]
    a.check(integrity["hard_gate_status"] == "PASS_WITH_ROUTE_A_REJECTION", "hard gate")
    a.check(integrity["external_reviewer_simulated"] is False, "no external review")
    a.check(integrity["acceptance_rate_reported"] is False, "no acceptance rate")

    counts = payload["counts"]
    a.check(counts["parameter_pairs"] == 36, "parameter count")
    a.check(counts["fixed_word_aggregate_rows"] == 288, "fixed aggregate count")
    a.check(counts["fixed_words_checked"] == fixed_words_checked == 18360, "fixed word count")
    a.check(counts["inverse_prefixes_checked"] == inverse_prefixes_checked == 9216, "inverse prefix count")
    a.check(counts["first_return_rows"] == 432, "first return count")
    a.check(counts["period_rows"] == PERIOD_N_MAX, "period count")
    a.check(counts["roof_rows"] == ROOF_N_MAX, "roof count")
    return a.assertions


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--evidence",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c174_parity_renewal_evidence.json",
    )
    args = parser.parse_args()
    payload = json.loads(args.evidence.read_text())
    repo_root = Path(__file__).resolve().parents[3]
    assertions = check_evidence(payload, repo_root)
    print(json.dumps({"status": "C174_CHECKER_PASS", "assertions": assertions}, sort_keys=True))


if __name__ == "__main__":
    main()
