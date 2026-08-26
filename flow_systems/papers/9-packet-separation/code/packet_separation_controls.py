#!/usr/bin/env python3
"""Deterministic, target-free controls for Paper 9 packet separation.

This module generates finite arithmetic and topology-regression witnesses for
the exact Paper 9 design.  It checks rational CRT residues, real approximation
errors, finite cyclic character values and kernels, the suspension action sign,
the ``p^Z``-only circle control, unit-exponent normalization, exact finite
distinctness witnesses, and an infinite-kernel prefix proxy for several primes.

These finite controls do not prove density, convergence in Deninger's source
topology, packet/orbit indiscreteness, nonclosedness of an equivalence relation,
Hausdorffness of a quotient, or any Paper-8/Route conclusion.

Only the Python standard library is used.  There is no network access,
randomness, external dataset, fitted parameter, target-zero data, or timestamp.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


SCHEMA = "paper9-packet-separation-controls/1"

EXPECTED_ACTIVE_TUPLE_HASHES = {
    "notes/candidate_lock.md": (
        "0e0e2f5e7a557baaf91cf6ca1abf4d17e0743a56d2d30f1364188d853f8f3ded"
    ),
    "notes/phase1_design_amendment.md": (
        "b3a7143b6b213501869467ac78090a6d8ae433f6137185fc6537d99698120cbb"
    ),
    "notes/research_protocol.md": (
        "895b2357d4815d295a8a63f1b6a0c412aaf5afdc34e715b2607d5d25945ad49e"
    ),
}

IMPLEMENTATION_RELATIVE_PATHS = (
    "code/packet_separation_controls.py",
    "code/test_packet_separation_controls.py",
    "code/README.md",
    "experiments/reproduce.sh",
    "experiments/README.md",
    "results/README.md",
)

ARTIFACT_FILENAMES = (
    "simultaneous_approximation.csv",
    "finite_cyclic_characters.csv",
    "action_sign_controls.csv",
    "pz_circle_controls.csv",
    "unit_normalization_controls.csv",
    "distinctness_controls.csv",
    "illegal_kernel_proxy.csv",
    "prime_uniformity_summary.csv",
)

PRIMES = (2, 3, 5, 7, 11)
LEVELS = (1, 2, 3, 4, 5)
ILLEGAL_LEVELS = (1, 2, 3, 4, 5, 6, 7)
NORMALIZATION_FACTORS = (2, 3, 6, 10)
REAL_TARGETS = {
    2: Fraction(137, 100),
    3: Fraction(11, 7),
    5: Fraction(17, 11),
    7: Fraction(23, 13),
    11: Fraction(29, 17),
}


def format_float(value: float) -> str:
    """Return a stable finite round-trippable decimal representation."""

    if not math.isfinite(value):
        raise ValueError("non-finite numeric output is forbidden")
    if value == 0.0:
        value = 0.0
    return format(value, ".17g")


def format_fraction(value: Fraction) -> str:
    """Return an exact rational string."""

    return f"{value.numerator}/{value.denominator}"


def sha256(path: Path) -> str:
    """Return the SHA-256 digest of a local file."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def is_prime(number: int) -> bool:
    """Deterministic primality test for the small control parameters."""

    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def first_primes_excluding(excluded: int, count: int) -> tuple[int, ...]:
    """Return the first ``count`` primes different from ``excluded``."""

    if count < 0:
        raise ValueError("count must be nonnegative")
    primes: list[int] = []
    candidate = 2
    while len(primes) < count:
        if candidate != excluded and is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return tuple(primes)


def product(values: Iterable[int]) -> int:
    """Exact integer product."""

    result = 1
    for value in values:
        result *= value
    return result


def crt_pairwise(residues: Sequence[int], moduli: Sequence[int]) -> tuple[int, int]:
    """Solve pairwise-coprime CRT congruences and return ``(x, modulus)``."""

    if len(residues) != len(moduli) or not moduli:
        raise ValueError("CRT residues and nonempty moduli must have equal length")
    modulus = product(moduli)
    value = 0
    for residue, component_modulus in zip(residues, moduli):
        if component_modulus < 2:
            raise ValueError("CRT component modulus must exceed one")
        complement = modulus // component_modulus
        inverse = pow(complement, -1, component_modulus)
        value = (value + residue * complement * inverse) % modulus
    return value, modulus


def target_cylinder(prime: int, level: int) -> dict[str, object]:
    """Build a nested finite cylinder for a non-diagonal profinite unit."""

    if prime not in PRIMES or level not in LEVELS:
        raise ValueError("unsupported prime or level")
    component_primes = first_primes_excluding(prime, level)
    moduli = tuple(ell**level for ell in component_primes)
    residues = tuple((1 + ell) % modulus for ell, modulus in zip(component_primes, moduli))
    target_residue, modulus = crt_pairwise(residues, moduli)
    if math.gcd(target_residue, modulus) != 1:
        raise AssertionError("target cylinder must be a unit")
    return {
        "component_primes": component_primes,
        "component_moduli": moduli,
        "component_residues": residues,
        "target_residue": target_residue,
        "modulus": modulus,
    }


def nearest_congruent_approximant(
    prime: int,
    real_target: Fraction,
    target_residue: int,
    modulus: int,
    level: int,
) -> dict[str, object]:
    """Construct ``m/p^k`` with a fixed rational residue and small real error."""

    if not is_prime(prime) or real_target <= 0 or modulus < 2:
        raise ValueError("invalid approximation parameters")
    if math.gcd(prime, modulus) != 1:
        raise ValueError("modulus must be prime to p")
    if math.gcd(target_residue, modulus) != 1:
        raise ValueError("source target residue must be a unit")
    error_goal = Fraction(1, 10 ** (level + 4))
    exponent = 0
    while True:
        denominator = prime**exponent
        nearest_bound = Fraction(modulus, 2 * denominator)
        if nearest_bound <= error_goal and real_target * denominator > 2 * modulus:
            break
        exponent += 1

    required_numerator_residue = (
        target_residue * pow(prime, exponent, modulus)
    ) % modulus
    scaled_target = real_target * denominator
    quotient_coordinate = Fraction(
        scaled_target - required_numerator_residue, modulus
    )
    translate = (quotient_coordinate + Fraction(1, 2)).numerator // (
        quotient_coordinate + Fraction(1, 2)
    ).denominator
    numerator = required_numerator_residue + translate * modulus
    if numerator <= 0:
        raise AssertionError("constructed numerator must be positive")

    rational_residue = (
        numerator * pow(denominator, -1, modulus)
    ) % modulus
    rational_value = Fraction(numerator, denominator)
    real_error = abs(rational_value - real_target)
    if rational_residue != target_residue:
        raise AssertionError("rational residue construction failed")
    if real_error > nearest_bound or real_error > error_goal:
        raise AssertionError("real approximation bound failed")
    return {
        "prime": prime,
        "level": level,
        "real_target": real_target,
        "target_residue": target_residue,
        "modulus": modulus,
        "denominator_exponent": exponent,
        "denominator": denominator,
        "numerator": numerator,
        "numerator_residue": numerator % modulus,
        "rational_residue": rational_residue,
        "rational_value": rational_value,
        "real_error": real_error,
        "nearest_bound": nearest_bound,
        "error_goal": error_goal,
    }


def approximation_cases() -> list[dict[str, object]]:
    """Return all fixed simultaneous-approximation cases."""

    cases: list[dict[str, object]] = []
    for prime in PRIMES:
        for level in LEVELS:
            cylinder = target_cylinder(prime, level)
            case = nearest_congruent_approximant(
                prime,
                REAL_TARGETS[prime],
                int(cylinder["target_residue"]),
                int(cylinder["modulus"]),
                level,
            )
            case.update(cylinder)
            cases.append(case)
    return cases


def prime_to_p_part(number: int, prime: int) -> int:
    """Return the largest divisor of ``number`` prime to ``prime``."""

    if number < 1:
        raise ValueError("number must be positive")
    while number % prime == 0:
        number //= prime
    return number


def is_fractional_power_of_prime(value: Fraction, prime: int) -> tuple[bool, int | None]:
    """Decide exactly whether a positive rational is ``prime^n`` for integer n."""

    if value <= 0 or not is_prime(prime):
        raise ValueError("invalid power test")
    numerator = value.numerator
    denominator = value.denominator
    numerator_power = 0
    denominator_power = 0
    while numerator % prime == 0:
        numerator //= prime
        numerator_power += 1
    while denominator % prime == 0:
        denominator //= prime
        denominator_power += 1
    if numerator == 1 and denominator == 1:
        return True, numerator_power - denominator_power
    return False, None


def cyclic_subgroup(generator: int, modulus: int) -> tuple[int, ...]:
    """Return the finite subgroup generated by a unit modulo ``modulus``."""

    if modulus < 2 or math.gcd(generator, modulus) != 1:
        raise ValueError("generator must be a modular unit")
    values: list[int] = []
    current = 1
    while current not in values:
        values.append(current)
        current = current * generator % modulus
    if current != 1:
        raise AssertionError("unit powers must return to one")
    return tuple(values)


def transverse_distinctness_witness(prime: int) -> dict[str, object]:
    """Find a finite quotient where a unit lies outside ``<p>``."""

    for modulus in range(3, 200):
        if math.gcd(prime, modulus) != 1:
            continue
        subgroup = cyclic_subgroup(prime % modulus, modulus)
        units = tuple(value for value in range(1, modulus) if math.gcd(value, modulus) == 1)
        outside = tuple(value for value in units if value not in subgroup)
        if outside:
            return {
                "modulus": modulus,
                "subgroup": subgroup,
                "witness": outside[0],
            }
    raise AssertionError("no finite transverse witness found")


def circle_distance_for_ratio(value: Fraction, prime: int) -> tuple[int, float]:
    """Return nearest lattice exponent and positive log-circle separation."""

    logarithm = math.log(value.numerator) - math.log(value.denominator)
    length = math.log(prime)
    center = round(logarithm / length)
    candidates = range(center - 2, center + 3)
    nearest = min(candidates, key=lambda exponent: abs(logarithm - exponent * length))
    return nearest, abs(logarithm - nearest * length)


def write_csv(
    path: Path, fieldnames: Sequence[str], rows: Iterable[dict[str, object]]
) -> int:
    """Write deterministic UTF-8 CSV and return its data-row count."""

    materialized = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(fieldnames),
            lineterminator="\n",
            extrasaction="raise",
        )
        writer.writeheader()
        writer.writerows(materialized)
    return len(materialized)


def _component_description(case: dict[str, object]) -> str:
    primes = tuple(case["component_primes"])
    moduli = tuple(case["component_moduli"])
    residues = tuple(case["component_residues"])
    return ";".join(
        f"{ell}:{residue}(mod {modulus})"
        for ell, residue, modulus in zip(primes, residues, moduli)
    )


def _approximation_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in approximation_cases():
        rows.append(
            {
                "prime": case["prime"],
                "level": case["level"],
                "target_real_exact": format_fraction(case["real_target"]),
                "target_components": _component_description(case),
                "modulus": case["modulus"],
                "target_rational_residue": case["target_residue"],
                "denominator_exponent_k": case["denominator_exponent"],
                "denominator_p_power": case["denominator"],
                "numerator_m": case["numerator"],
                "numerator_residue": case["numerator_residue"],
                "rational_q_residue": case["rational_residue"],
                "profinite_match_exact": "true",
                "real_error_exact": format_fraction(case["real_error"]),
                "real_error_decimal": format_float(float(case["real_error"])),
                "nearest_class_bound_decimal": format_float(float(case["nearest_bound"])),
                "error_goal_decimal": format_float(float(case["error_goal"])),
                "numerator_convergence_assumed": "false",
                "scope": "finite-cylinder witness; not a density proof",
            }
        )
    return rows


def _finite_character_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in approximation_cases():
        prime = int(case["prime"])
        numerator = int(case["numerator"])
        denominator = int(case["denominator"])
        for ell, order, target in zip(
            case["component_primes"],
            case["component_moduli"],
            case["component_residues"],
        ):
            order = int(order)
            q_exponent = numerator * pow(denominator, -1, order) % order
            base_exponent = (1 + 2 * int(ell)) % order
            observed = base_exponent * q_exponent % order
            expected = base_exponent * int(target) % order
            observed_value = complex(
                math.cos(2.0 * math.pi * observed / order),
                math.sin(2.0 * math.pi * observed / order),
            )
            expected_value = complex(
                math.cos(2.0 * math.pi * expected / order),
                math.sin(2.0 * math.pi * expected / order),
            )
            rows.append(
                {
                    "prime": prime,
                    "level": case["level"],
                    "cyclic_component_prime": ell,
                    "cyclic_order": order,
                    "base_unit_exponent": base_exponent,
                    "q_exponent_mod_order": q_exponent,
                    "target_exponent_mod_order": target,
                    "observed_character_exponent": observed,
                    "target_character_exponent": expected,
                    "character_match_exact": str(observed == expected).lower(),
                    "character_value_error": format_float(abs(observed_value - expected_value)),
                    "kernel_on_cyclic_group": math.gcd(q_exponent, order),
                    "global_kernel_order_prime_to_p": prime_to_p_part(numerator, prime),
                    "global_kernel_finite": "true",
                    "source_stage": "one fixed initial p-fibre",
                    "scope": "finite cyclic value/kernel witness; not a source-topology proof",
                }
            )
    return rows


def _action_sign_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in approximation_cases():
        target_ratio = Fraction(case["real_target"])
        u = Fraction(target_ratio.numerator, 1)
        v = Fraction(target_ratio.denominator, 1)
        q_value = Fraction(case["rational_value"])
        correct_time = u / q_value
        wrong_time = u * q_value
        rows.append(
            {
                "prime": case["prime"],
                "level": case["level"],
                "u_exact": format_fraction(u),
                "v_exact": format_fraction(v),
                "required_q_limit_u_over_v": format_fraction(target_ratio),
                "q_exact": format_fraction(q_value),
                "correct_time_u_over_q": format_fraction(correct_time),
                "correct_time_error": format_float(float(abs(correct_time - v))),
                "wrong_time_u_times_q": format_fraction(wrong_time),
                "wrong_time_error": format_float(float(abs(wrong_time - v))),
                "active_action": "(P,u)q=(F_qP,q^-1u)",
                "wrong_action": "(P,u)q=(F_qP,qu)",
                "scope": "orientation regression; persistence of density is not a theorem failure",
            }
        )
    return rows


def _pz_circle_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for prime in PRIMES:
        ratio = REAL_TARGETS[prime]
        in_stabilizer, exponent = is_fractional_power_of_prime(ratio, prime)
        nearest_exponent, distance = circle_distance_for_ratio(ratio, prime)
        rows.append(
            {
                "prime": prime,
                "time_ratio_exact": format_fraction(ratio),
                "ratio_in_pZ": str(in_stabilizer).lower(),
                "exact_stabilizer_exponent": "" if exponent is None else exponent,
                "nearest_log_lattice_exponent": nearest_exponent,
                "standard_circle_distance": format_float(distance),
                "positive_separation_witness": str(distance > 0.0).lower(),
                "acting_group": "p^Z only",
                "away_p_approximation_channel": "absent",
                "expected_topology": "ordinary Hausdorff circle R/(log p)Z",
                "scope": "negative control; finite row does not prove Hausdorffness",
            }
        )
    return rows


def _unit_normalization_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for prime in PRIMES:
        cylinder = target_cylinder(prime, 3)
        modulus = int(cylinder["modulus"])
        unit = int(cylinder["target_residue"])
        base_time = Fraction(prime + 2, prime + 1)
        for factor in NORMALIZATION_FACTORS:
            source_time = factor * base_time
            exponent_after = unit * factor % modulus
            finite_kernel = prime_to_p_part(factor, prime)
            rows.append(
                {
                    "prime": prime,
                    "modulus": modulus,
                    "unit_exponent_a": unit,
                    "unit_gcd_with_modulus": math.gcd(unit, modulus),
                    "finite_kernel_factor_nu": factor,
                    "finite_kernel_order_prime_to_p": finite_kernel,
                    "source_time_nu_u": format_fraction(source_time),
                    "action_q": factor,
                    "time_after_action": format_fraction(source_time / factor),
                    "target_time_u": format_fraction(base_time),
                    "exponent_after_action": exponent_after,
                    "target_finite_exponent": unit * factor % modulus,
                    "time_match_exact": str(source_time / factor == base_time).lower(),
                    "exponent_match_exact": "true",
                    "identity": "[(F_nu P_a,u)]=[(P_a,nu*u)]",
                    "scope": "finite set-normalization witness; not universal exhaustiveness proof",
                }
            )
    return rows


def _distinctness_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for prime in PRIMES:
        ratio = REAL_TARGETS[prime]
        in_stabilizer, exponent = is_fractional_power_of_prime(ratio, prime)
        rows.append(
            {
                "prime": prime,
                "witness_type": "time_distinct",
                "modulus": "",
                "a_residue": "",
                "b_residue": "",
                "p_power_exponent": "" if exponent is None else exponent,
                "p_power_subgroup": "",
                "time_ratio": format_fraction(ratio),
                "equivalent_under_locked_relation": str(in_stabilizer).lower(),
                "distinct_exact": str(not in_stabilizer).lower(),
                "reason": "same P but u/v is not in exact stabilizer p^Z",
            }
        )

        witness = transverse_distinctness_witness(prime)
        modulus = int(witness["modulus"])
        subgroup = tuple(witness["subgroup"])
        outside = int(witness["witness"])
        rows.append(
            {
                "prime": prime,
                "witness_type": "transverse_distinct",
                "modulus": modulus,
                "a_residue": 1,
                "b_residue": outside,
                "p_power_exponent": "",
                "p_power_subgroup": ";".join(str(value) for value in subgroup),
                "time_ratio": "1/1",
                "equivalent_under_locked_relation": "false",
                "distinct_exact": "true",
                "reason": "b/a lies outside the finite image of p^Zhat",
            }
        )

        power_exponent = 1
        inside = pow(prime, power_exponent, modulus)
        rows.append(
            {
                "prime": prime,
                "witness_type": "galois_equivalent_control",
                "modulus": modulus,
                "a_residue": 1,
                "b_residue": inside,
                "p_power_exponent": power_exponent,
                "p_power_subgroup": ";".join(str(value) for value in subgroup),
                "time_ratio": "1/1",
                "equivalent_under_locked_relation": "true",
                "distinct_exact": "false",
                "reason": "b/a is the displayed p-power in the finite quotient",
            }
        )
    return rows


def _illegal_kernel_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for prime in PRIMES:
        prior_illegal_bound = 1
        for level in ILLEGAL_LEVELS:
            components = first_primes_excluding(prime, level)
            illegal_bound = product(components)
            rows.append(
                {
                    "prime": prime,
                    "profile": "illegal_uniformizer_components",
                    "prefix_level": level,
                    "component_primes": ";".join(str(value) for value in components),
                    "kernel_lower_bound": illegal_bound,
                    "kernel_bound_strictly_grows": str(illegal_bound > prior_illegal_bound).lower(),
                    "component_kernel_rule": "a_ell=ell gives an ell-element kernel",
                    "full_endpoint_in_Ef": "false",
                    "finite_prefix_only": "true",
                    "scope": "growing prefix proxy for an excluded infinite-kernel endpoint",
                }
            )
            prior_illegal_bound = illegal_bound
            rows.append(
                {
                    "prime": prime,
                    "profile": "legal_unit_components",
                    "prefix_level": level,
                    "component_primes": ";".join(str(value) for value in components),
                    "kernel_lower_bound": 1,
                    "kernel_bound_strictly_grows": "false",
                    "component_kernel_rule": "a_ell=1+ell is an ell-adic unit",
                    "full_endpoint_in_Ef": "true",
                    "finite_prefix_only": "true",
                    "scope": "unit-target domain control; not a source-convergence proof",
                }
            )
    return rows


def _prime_summary_rows() -> list[dict[str, object]]:
    approximation = _approximation_rows()
    characters = _finite_character_rows()
    actions = _action_sign_rows()
    circles = {int(row["prime"]): row for row in _pz_circle_rows()}
    normalizations = _unit_normalization_rows()
    distinctness = _distinctness_rows()
    illegal = _illegal_kernel_rows()
    rows: list[dict[str, object]] = []
    for prime in PRIMES:
        p_approx = [row for row in approximation if int(row["prime"]) == prime]
        p_char = [row for row in characters if int(row["prime"]) == prime]
        p_action = [row for row in actions if int(row["prime"]) == prime]
        p_norm = [row for row in normalizations if int(row["prime"]) == prime]
        p_distinct = [row for row in distinctness if int(row["prime"]) == prime]
        p_illegal = [
            row
            for row in illegal
            if int(row["prime"]) == prime
            and row["profile"] == "illegal_uniformizer_components"
        ]
        rows.append(
            {
                "prime": prime,
                "levels_tested": len(p_approx),
                "all_rational_residues_match": str(all(row["profinite_match_exact"] == "true" for row in p_approx)).lower(),
                "max_real_error": format_float(max(float(row["real_error_decimal"]) for row in p_approx)),
                "finite_cyclic_rows": len(p_char),
                "all_character_values_match": str(all(row["character_match_exact"] == "true" for row in p_char)).lower(),
                "max_character_value_error": format_float(max(float(row["character_value_error"]) for row in p_char)),
                "max_correct_action_time_error": format_float(max(float(row["correct_time_error"]) for row in p_action)),
                "final_wrong_action_time_error": p_action[-1]["wrong_time_error"],
                "pz_circle_distance": circles[prime]["standard_circle_distance"],
                "all_unit_normalizations_match": str(all(row["time_match_exact"] == "true" and row["exponent_match_exact"] == "true" for row in p_norm)).lower(),
                "exact_distinctness_rows": sum(row["distinct_exact"] == "true" for row in p_distinct),
                "illegal_kernel_final_lower_bound": p_illegal[-1]["kernel_lower_bound"],
                "theorem_uniformity_claimed": "false",
                "statistical_evidence_claimed": "false",
                "scope": "same target-free control family across several p",
            }
        )
    return rows


def _artifact_record(path: Path, rows: int) -> dict[str, int | str]:
    return {"bytes": path.stat().st_size, "rows": rows, "sha256": sha256(path)}


def _hash_relative_files(paper_dir: Path, paths: Sequence[str]) -> dict[str, str]:
    records: dict[str, str] = {}
    for relative in paths:
        path = paper_dir / relative
        if not path.is_file():
            raise FileNotFoundError(f"required file missing: {relative}")
        records[relative] = sha256(path)
    return records


def _validate_active_tuple(paper_dir: Path) -> dict[str, str]:
    current = _hash_relative_files(paper_dir, tuple(sorted(EXPECTED_ACTIVE_TUPLE_HASHES)))
    if current != EXPECTED_ACTIVE_TUPLE_HASHES:
        raise ValueError(
            "active tuple SHA-256 mismatch; controls are locked to the Paper 9 "
            "protocol/candidate/amendment bytes"
        )
    return current


def _csv_row_count(path: Path) -> int:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return max(0, sum(1 for _ in csv.reader(handle)) - 1)


def _metrics_from_rows(table_rows: dict[str, list[dict[str, object]]]) -> dict[str, object]:
    approximation = table_rows["simultaneous_approximation.csv"]
    characters = table_rows["finite_cyclic_characters.csv"]
    actions = table_rows["action_sign_controls.csv"]
    circles = table_rows["pz_circle_controls.csv"]
    final_actions = [row for row in actions if int(row["level"]) == max(LEVELS)]
    return {
        "total_csv_rows": sum(len(rows) for rows in table_rows.values()),
        "max_simultaneous_real_error": format_float(max(float(row["real_error_decimal"]) for row in approximation)),
        "max_finite_character_value_error": format_float(max(float(row["character_value_error"]) for row in characters)),
        "max_correct_action_time_error": format_float(max(float(row["correct_time_error"]) for row in actions)),
        "min_final_wrong_action_time_error": format_float(min(float(row["wrong_time_error"]) for row in final_actions)),
        "min_pz_circle_separation": format_float(min(float(row["standard_circle_distance"]) for row in circles)),
        "all_rational_residues_match": all(row["profinite_match_exact"] == "true" for row in approximation),
        "all_finite_character_values_match": all(row["character_match_exact"] == "true" for row in characters),
    }


def run(output_dir: Path, *, paper_dir: Path | None = None) -> dict[str, object]:
    """Generate all deterministic CSV artifacts and the hash manifest."""

    resolved_paper = Path(__file__).resolve().parents[1] if paper_dir is None else paper_dir.resolve()
    active_tuple = _validate_active_tuple(resolved_paper)
    output_dir.mkdir(parents=True, exist_ok=True)
    unexpected_csv = {path.name for path in output_dir.glob("*.csv")} - set(ARTIFACT_FILENAMES)
    if unexpected_csv:
        raise ValueError(f"unexpected CSV artifact(s): {sorted(unexpected_csv)}")

    table_specs: tuple[
        tuple[str, Sequence[str], list[dict[str, object]]], ...
    ] = (
        (
            "simultaneous_approximation.csv",
            (
                "prime", "level", "target_real_exact", "target_components", "modulus",
                "target_rational_residue", "denominator_exponent_k", "denominator_p_power",
                "numerator_m", "numerator_residue", "rational_q_residue",
                "profinite_match_exact", "real_error_exact", "real_error_decimal",
                "nearest_class_bound_decimal", "error_goal_decimal",
                "numerator_convergence_assumed", "scope",
            ),
            _approximation_rows(),
        ),
        (
            "finite_cyclic_characters.csv",
            (
                "prime", "level", "cyclic_component_prime", "cyclic_order",
                "base_unit_exponent", "q_exponent_mod_order", "target_exponent_mod_order",
                "observed_character_exponent", "target_character_exponent",
                "character_match_exact", "character_value_error", "kernel_on_cyclic_group",
                "global_kernel_order_prime_to_p", "global_kernel_finite", "source_stage", "scope",
            ),
            _finite_character_rows(),
        ),
        (
            "action_sign_controls.csv",
            (
                "prime", "level", "u_exact", "v_exact", "required_q_limit_u_over_v",
                "q_exact", "correct_time_u_over_q", "correct_time_error",
                "wrong_time_u_times_q", "wrong_time_error", "active_action", "wrong_action", "scope",
            ),
            _action_sign_rows(),
        ),
        (
            "pz_circle_controls.csv",
            (
                "prime", "time_ratio_exact", "ratio_in_pZ", "exact_stabilizer_exponent",
                "nearest_log_lattice_exponent", "standard_circle_distance",
                "positive_separation_witness", "acting_group", "away_p_approximation_channel",
                "expected_topology", "scope",
            ),
            _pz_circle_rows(),
        ),
        (
            "unit_normalization_controls.csv",
            (
                "prime", "modulus", "unit_exponent_a", "unit_gcd_with_modulus",
                "finite_kernel_factor_nu", "finite_kernel_order_prime_to_p",
                "source_time_nu_u", "action_q", "time_after_action", "target_time_u",
                "exponent_after_action", "target_finite_exponent", "time_match_exact",
                "exponent_match_exact", "identity", "scope",
            ),
            _unit_normalization_rows(),
        ),
        (
            "distinctness_controls.csv",
            (
                "prime", "witness_type", "modulus", "a_residue", "b_residue",
                "p_power_exponent", "p_power_subgroup", "time_ratio",
                "equivalent_under_locked_relation", "distinct_exact", "reason",
            ),
            _distinctness_rows(),
        ),
        (
            "illegal_kernel_proxy.csv",
            (
                "prime", "profile", "prefix_level", "component_primes", "kernel_lower_bound",
                "kernel_bound_strictly_grows", "component_kernel_rule", "full_endpoint_in_Ef",
                "finite_prefix_only", "scope",
            ),
            _illegal_kernel_rows(),
        ),
        (
            "prime_uniformity_summary.csv",
            (
                "prime", "levels_tested", "all_rational_residues_match", "max_real_error",
                "finite_cyclic_rows", "all_character_values_match", "max_character_value_error",
                "max_correct_action_time_error", "final_wrong_action_time_error",
                "pz_circle_distance", "all_unit_normalizations_match", "exact_distinctness_rows",
                "illegal_kernel_final_lower_bound", "theorem_uniformity_claimed",
                "statistical_evidence_claimed", "scope",
            ),
            _prime_summary_rows(),
        ),
    )

    table_rows = {filename: rows for filename, _, rows in table_specs}
    artifacts: dict[str, dict[str, int | str]] = {}
    for filename, fieldnames, rows in table_specs:
        path = output_dir / filename
        row_count = write_csv(path, fieldnames, rows)
        artifacts[filename] = _artifact_record(path, row_count)
    if set(artifacts) != set(ARTIFACT_FILENAMES):
        raise AssertionError("generated artifact set does not match frozen filenames")

    implementation_files = _hash_relative_files(resolved_paper, IMPLEMENTATION_RELATIVE_PATHS)
    metrics = _metrics_from_rows(table_rows)
    manifest: dict[str, object] = {
        "schema": SCHEMA,
        "regression_status": "PASS",
        "active_tuple_files": active_tuple,
        "implementation_files": implementation_files,
        "artifacts": artifacts,
        "metrics": metrics,
        "parameters": {
            "primes": list(PRIMES),
            "approximation_levels": list(LEVELS),
            "illegal_kernel_prefix_levels": list(ILLEGAL_LEVELS),
            "real_targets_exact": {str(prime): format_fraction(REAL_TARGETS[prime]) for prime in PRIMES},
            "profinite_unit_components": "a_ell=1+ell in Z_ell^x",
            "normalization_factors": list(NORMALIZATION_FACTORS),
        },
        "controls": [
            "q=m*p^-k simultaneous finite-cylinder residues and exact real errors",
            "finite cyclic character convergence and finite-kernel ledger",
            "inverse right-action sign versus deliberately wrong sign",
            "p^Z-only ordinary Hausdorff-circle negative control",
            "finite unit-exponent/time normalization identity",
            "time and transverse distinctness modulo p^Z and finite images of p^Zhat",
            "illegal infinite-kernel growing-prefix proxy versus unit endpoints",
            "same target-free controls for p=2,3,5,7,11",
        ],
        "determinism": {
            "network": False,
            "randomness": False,
            "external_datasets": False,
            "target_zero_data": False,
            "fitting": False,
            "timestamps": False,
            "python_dependencies": "standard_library_only",
        },
        "interpretation_boundary": (
            "Finite exact arithmetic and floating regression witnesses only. These artifacts "
            "are not mathematical proofs of density, source-topology convergence, "
            "indiscreteness, nonclosedness, Hausdorffness, Paper-8 supersession, or Route credit."
        ),
        "object_boundary": (
            "Raw finite cyclic characters, Galois/colimit topology, the actual inherited packet, "
            "the intrinsic quotient Q_p, Morishita C_p, and the standard-circle proxy remain "
            "separate objects; no topology, measure, completion, trace, or Route field is transported."
        ),
        "forbidden_evidence_not_used": [
            "Riemann-zero tables",
            "Euler-product target matching",
            "fitted clocks or residues",
            "fitted packet weights or transverse probabilities",
            "external network or package data",
        ],
    }
    manifest_path = output_dir / "packet_separation_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return manifest


def _read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def verify(output_dir: Path, *, paper_dir: Path | None = None) -> dict[str, object]:
    """Verify hashes, rows, metrics, active tuple, and implementation files."""

    resolved_paper = Path(__file__).resolve().parents[1] if paper_dir is None else paper_dir.resolve()
    active_tuple = _validate_active_tuple(resolved_paper)
    manifest_path = output_dir / "packet_separation_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != SCHEMA:
        raise ValueError("manifest schema mismatch")
    if manifest.get("regression_status") != "PASS":
        raise ValueError("manifest regression status mismatch")
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, dict) or set(artifacts) != set(ARTIFACT_FILENAMES):
        raise ValueError("manifest artifact set mismatch")
    table_rows: dict[str, list[dict[str, object]]] = {}
    for filename in ARTIFACT_FILENAMES:
        path = output_dir / filename
        if not path.is_file():
            raise FileNotFoundError(f"artifact missing: {filename}")
        record = artifacts[filename]
        if not isinstance(record, dict):
            raise ValueError("invalid artifact record")
        if sha256(path) != record.get("sha256"):
            raise ValueError(f"artifact SHA-256 mismatch: {filename}")
        if path.stat().st_size != record.get("bytes"):
            raise ValueError(f"artifact byte-size mismatch: {filename}")
        if _csv_row_count(path) != record.get("rows"):
            raise ValueError(f"artifact row-count mismatch: {filename}")
        table_rows[filename] = _read_csv_rows(path)
    if manifest.get("active_tuple_files") != active_tuple:
        raise ValueError("manifest active tuple mismatch")
    implementation = _hash_relative_files(resolved_paper, IMPLEMENTATION_RELATIVE_PATHS)
    if manifest.get("implementation_files") != implementation:
        raise ValueError("implementation SHA-256 mismatch")
    current_metrics = _metrics_from_rows(table_rows)
    if manifest.get("metrics") != current_metrics:
        raise ValueError("manifest metrics mismatch")
    determinism = manifest.get("determinism")
    if not isinstance(determinism, dict) or any(
        determinism.get(key) is not False
        for key in ("network", "randomness", "external_datasets", "target_zero_data", "fitting", "timestamps")
    ):
        raise ValueError("determinism boundary mismatch")
    if determinism.get("python_dependencies") != "standard_library_only":
        raise ValueError("dependency boundary mismatch")
    if "not mathematical proofs" not in str(manifest.get("interpretation_boundary")):
        raise ValueError("interpretation boundary missing")
    return manifest


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
        help="directory for generated CSVs and manifest",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="verify existing artifacts without rewriting them",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    manifest = verify(args.output_dir) if args.verify_only else run(args.output_dir)
    metrics = manifest["metrics"]
    print(
        "PASS: "
        f"{metrics['total_csv_rows']} CSV rows; "
        f"max real error={metrics['max_simultaneous_real_error']}; "
        f"max character error={metrics['max_finite_character_value_error']}; "
        f"max correct-time error={metrics['max_correct_action_time_error']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
