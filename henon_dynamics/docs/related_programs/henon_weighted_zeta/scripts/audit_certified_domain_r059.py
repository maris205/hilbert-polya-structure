#!/usr/bin/env python3
"""R059 high-precision symbolic bridge and restricted cycle audit."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

import mpmath as mp
import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from henon_zeta.precision import refine_and_audit  # noqa: E402


PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R059_CERTIFIED_DOMAIN_PROTOCOL.json"
)
PROTOCOL_SHA256 = "f94801f5b7abd5baaebd4c859a3662af4cf6d63954b1f4b18aaa6e8d3596f2b6"
EXPECTED_WORDS = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R059_EXPECTED_SYMBOLIC_WORDS.json"
)
DEFAULT_CATALOG = (
    PROJECT_ROOT / "results" / "complex_root_census_a6_n12_merged.json"
)
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "certified_domain_r059.json"
DEFAULT_CSV = PROJECT_ROOT / "results" / "certified_domain_r059.csv"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, default=PROTOCOL)
    parser.add_argument("--expected-words", type=Path, default=EXPECTED_WORDS)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--preflight-only", action="store_true")
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def portable_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(resolved)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def fraction_mpf(text: str) -> mp.mpf:
    value = Fraction(text)
    return mp.mpf(value.numerator) / value.denominator


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[shift:] + word[:shift] for shift in range(len(word)))


def primitive_period(word: tuple[int, ...]) -> int:
    for period in range(1, len(word) + 1):
        if len(word) % period == 0 and all(
            word[index] == word[index % period]
            for index in range(len(word))
        ):
            return period
    raise AssertionError("finite word has no period")


def classify_interval(
    value: mp.mpf,
    intervals: dict[str, tuple[mp.mpf, mp.mpf]],
) -> str | None:
    for sign in ("-", "+"):
        lower, upper = intervals[sign]
        if lower < value < upper:
            return sign
    return None


def refine_worker(
    row: dict[str, Any],
    dps: int,
    max_iterations: int,
) -> tuple[str, dict[str, Any]]:
    audit = refine_and_audit(
        row["sequence"],
        float(row["a"]),
        dps=dps,
        max_iterations=max_iterations,
    )
    return str(row["orbit_id"]), audit


def polynomial_product(
    factors: Iterable[tuple[int, mp.mpf]],
    max_degree: int,
) -> list[mp.mpf]:
    coefficients = [mp.mpf(0)] * (max_degree + 1)
    coefficients[0] = mp.mpf(1)
    for period, weight in factors:
        updated = list(coefficients)
        for degree in range(period, max_degree + 1):
            updated[degree] -= weight * coefficients[degree - period]
        coefficients = updated
    return coefficients


def repeated_trace(trace: mp.mpf, repetition: int) -> mp.mpf:
    if repetition == 0:
        return mp.mpf(2)
    if repetition == 1:
        return trace
    previous_previous = mp.mpf(2)
    previous = trace
    for _ in range(2, repetition + 1):
        current = trace * previous - previous_previous
        previous_previous, previous = previous, current
    return previous


def perron_fredholm_coefficients(
    selected: list[dict[str, Any]],
    max_degree: int,
) -> list[mp.mpf]:
    traces = [mp.mpf(0)] * (max_degree + 1)
    for row in selected:
        period = int(row["period"])
        primitive_trace = mp.mpf(row["refined_trace"])
        for repetition in range(1, max_degree // period + 1):
            degree = repetition * period
            denominator = abs(mp.mpf(2) - repeated_trace(primitive_trace, repetition))
            if denominator == 0:
                raise ArithmeticError(
                    f"singular repeated orbit {row['orbit_id']} at degree {degree}"
                )
            traces[degree] += mp.mpf(period) / denominator
    coefficients = [mp.mpf(0)] * (max_degree + 1)
    coefficients[0] = mp.mpf(1)
    for degree in range(1, max_degree + 1):
        coefficients[degree] = -mp.fsum(
            traces[index] * coefficients[degree - index]
            for index in range(1, degree + 1)
        ) / degree
    return coefficients


def leading_resonance(coefficients: list[mp.mpf]) -> complex | None:
    values = np.asarray([float(value) for value in coefficients], dtype=float)
    trimmed = np.trim_zeros(values, trim="b")
    if trimmed.size <= 1:
        return None
    roots = np.polynomial.polynomial.polyroots(trimmed)
    roots = roots[np.abs(roots) > 1e-12]
    if roots.size == 0:
        return None
    root = roots[int(np.argmin(np.abs(roots)))]
    return complex(1 / root)


def serialize_complex(value: complex | None) -> list[float] | None:
    if value is None:
        return None
    return [float(value.real), float(value.imag)]


def coefficient_strings(values: Iterable[mp.mpf], digits: int = 80) -> list[str]:
    return [mp.nstr(value, digits) for value in values]


def integrity_checks(
    protocol_path: Path,
    protocol: dict[str, Any],
    expected_path: Path,
    expected: dict[str, Any],
    catalog_path: Path,
    catalog: dict[str, Any],
) -> dict[str, Any]:
    parent_rows = []
    for record in protocol["parent_artifacts"]:
        path = PROJECT_ROOT / record["path"]
        actual = sha256_file(path) if path.exists() else None
        parent_rows.append(
            {
                "path": record["path"],
                "expected_sha256": record["sha256"],
                "actual_sha256": actual,
                "pass": actual == record["sha256"],
            }
        )
    checks = {
        "protocol_sha256": sha256_file(protocol_path) == PROTOCOL_SHA256,
        "protocol_status": protocol.get("status")
        == "FROZEN_AFTER_DISCLOSED_FLOAT64_DEVELOPMENT_PRECHECK_BEFORE_HIGH_PRECISION_AND_OPERATOR_PRODUCTION",
        "all_parent_hashes": all(row["pass"] for row in parent_rows),
        "expected_word_artifact_sha256": sha256_file(expected_path)
        == protocol["symbolic_expectations"]["frozen_word_artifact_sha256"],
        "expected_word_set_sha256": expected["canonical_word_set_sha256"]
        == protocol["symbolic_expectations"]["canonical_word_set_sha256"],
        "catalog_sha256": sha256_file(catalog_path)
        == protocol["catalog"]["sha256"],
        "catalog_record_count": len(catalog["real_primitive_orbits"])
        == protocol["catalog"]["expected_total_primitive_orbits"],
        "catalog_max_period": int(catalog["max_period"])
        == protocol["catalog"]["maximum_period"],
    }
    return {
        "protocol_path": portable_path(protocol_path),
        "protocol_sha256": sha256_file(protocol_path),
        "parent_artifacts": parent_rows,
        "checks": checks,
        "pass": all(checks.values()),
    }


def main() -> None:
    args = parse_args()
    protocol = load_json(args.protocol)
    expected = load_json(args.expected_words)
    catalog = load_json(args.catalog)
    integrity = integrity_checks(
        args.protocol,
        protocol,
        args.expected_words,
        expected,
        args.catalog,
        catalog,
    )
    if not integrity["pass"]:
        raise SystemExit(f"R059 preflight integrity failure: {integrity['checks']}")
    if args.preflight_only:
        print(json.dumps({"integrity": integrity, "pass": True}, indent=2))
        return

    dps = int(protocol["catalog"]["high_precision_dps"])
    max_iterations = int(
        protocol["catalog"]["high_precision_max_newton_iterations"]
    )
    rows = catalog["real_primitive_orbits"]
    audits: dict[str, dict[str, Any]] = {}
    if args.workers <= 1:
        for index, row in enumerate(rows, start=1):
            orbit_id, audit = refine_worker(row, dps, max_iterations)
            audits[orbit_id] = audit
            if index % 50 == 0 or index == len(rows):
                print(f"[high-precision] {index}/{len(rows)} complete", flush=True)
    else:
        with ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(refine_worker, row, dps, max_iterations): row[
                    "orbit_id"
                ]
                for row in rows
            }
            complete = 0
            for future in as_completed(futures):
                orbit_id, audit = future.result()
                audits[orbit_id] = audit
                complete += 1
                if complete % 50 == 0 or complete == len(rows):
                    print(
                        f"[high-precision] {complete}/{len(rows)} complete",
                        flush=True,
                    )

    state_order = tuple(protocol["h_sets"]["state_order"])
    state_index = {label: index for index, label in enumerate(state_order)}
    adjacency = protocol["h_sets"]["adjacency_matrix"]
    threshold = mp.mpf(protocol["catalog"]["endpoint_ambiguity_threshold"])

    with mp.workdps(dps):
        x_intervals = {
            sign: tuple(fraction_mpf(value) for value in endpoints)
            for sign, endpoints in protocol["h_sets"]["x_intervals"].items()
        }
        y_intervals = {
            sign: tuple(fraction_mpf(value) for value in endpoints)
            for sign, endpoints in protocol["h_sets"]["y_intervals"].items()
        }
        all_endpoints = [
            endpoint
            for intervals in (x_intervals, y_intervals)
            for pair in intervals.values()
            for endpoint in pair
        ]

        classified: list[dict[str, Any]] = []
        selected_for_cycles: list[dict[str, Any]] = []
        observed_words: dict[int, dict[str, list[str]]] = defaultdict(
            lambda: defaultdict(list)
        )
        minimum_endpoint_distance: mp.mpf | None = None
        minimum_inside_margin: mp.mpf | None = None

        for row in rows:
            orbit_id = str(row["orbit_id"])
            audit = audits[orbit_id]
            coordinates = [mp.mpf(value) for value in audit["sequence"]]
            endpoint_distance = min(
                abs(value - endpoint)
                for value in coordinates
                for endpoint in all_endpoints
            )
            if minimum_endpoint_distance is None:
                minimum_endpoint_distance = endpoint_distance
            else:
                minimum_endpoint_distance = min(
                    minimum_endpoint_distance,
                    endpoint_distance,
                )

            classification = "NUMERIC_OUTSIDE"
            word_labels: list[str] = []
            transition_pass = False
            word_period = None
            canonical_word = None
            inside_margin = None
            if not audit["passed"]:
                classification = "ROOT_FAILED"
            elif endpoint_distance <= threshold:
                classification = "UNRESOLVED_NEAR_BOUNDARY"
            else:
                phase_margins: list[mp.mpf] = []
                for index, x_value in enumerate(coordinates):
                    y_value = coordinates[(index - 1) % len(coordinates)]
                    x_sign = classify_interval(x_value, x_intervals)
                    y_sign = classify_interval(y_value, y_intervals)
                    if x_sign is None or y_sign is None:
                        word_labels = []
                        break
                    label = x_sign + y_sign
                    word_labels.append(label)
                    x_lower, x_upper = x_intervals[x_sign]
                    y_lower, y_upper = y_intervals[y_sign]
                    phase_margins.extend(
                        (
                            x_value - x_lower,
                            x_upper - x_value,
                            y_value - y_lower,
                            y_upper - y_value,
                        )
                    )
                if len(word_labels) == len(coordinates):
                    classification = "NUMERIC_INSIDE"
                    word_indices = tuple(state_index[label] for label in word_labels)
                    transition_pass = all(
                        adjacency[word_indices[index]][
                            word_indices[(index + 1) % len(word_indices)]
                        ]
                        == 1
                        for index in range(len(word_indices))
                    )
                    word_period = primitive_period(word_indices)
                    canonical_indices = canonical_rotation(word_indices)
                    canonical_word = "|".join(
                        state_order[index] for index in canonical_indices
                    )
                    inside_margin = min(phase_margins)
                    if minimum_inside_margin is None:
                        minimum_inside_margin = inside_margin
                    else:
                        minimum_inside_margin = min(
                            minimum_inside_margin,
                            inside_margin,
                        )
                    observed_words[int(row["period"])][canonical_word].append(
                        orbit_id
                    )
                    trace = mp.mpf(audit["trace"])
                    unstable_modulus = (
                        abs(trace) + mp.sqrt(trace * trace - 4)
                    ) / 2
                    selected_for_cycles.append(
                        {
                            "orbit_id": orbit_id,
                            "period": int(row["period"]),
                            "canonical_word": canonical_word,
                            "refined_trace": mp.nstr(trace, dps - 10),
                            "unstable_modulus": mp.nstr(
                                unstable_modulus,
                                dps - 10,
                            ),
                        }
                    )

            classified.append(
                {
                    "orbit_id": orbit_id,
                    "period": int(row["period"]),
                    "classification": classification,
                    "high_precision_pass": bool(audit["passed"]),
                    "endpoint_distance": mp.nstr(endpoint_distance, dps - 10),
                    "inside_margin": (
                        None
                        if inside_margin is None
                        else mp.nstr(inside_margin, dps - 10)
                    ),
                    "canonical_word": canonical_word,
                    "transition_pass": transition_pass,
                    "state_word_primitive_period": word_period,
                    "refined_sequence": audit["sequence"],
                    "refined_trace": audit["trace"],
                    "scaled_residual_inf": audit["scaled_residual_inf"],
                    "determinant_error": audit["determinant_error"],
                }
            )

        period_comparisons = []
        exact_word_sets_pass = True
        duplicate_witness_count = 0
        for period in range(1, 13):
            expected_set = set(expected["primitive_words"][str(period)])
            observed_map = observed_words.get(period, {})
            observed_set = set(observed_map)
            missing = sorted(expected_set - observed_set)
            extra = sorted(observed_set - expected_set)
            duplicates = {
                word: orbit_ids
                for word, orbit_ids in observed_map.items()
                if len(orbit_ids) > 1
            }
            duplicate_witness_count += sum(
                len(orbit_ids) - 1 for orbit_ids in duplicates.values()
            )
            pass_value = not missing and not extra and not duplicates
            exact_word_sets_pass = exact_word_sets_pass and pass_value
            period_comparisons.append(
                {
                    "period": period,
                    "expected_count": len(expected_set),
                    "observed_count": len(observed_set),
                    "selected_orbit_count": sum(
                        len(orbit_ids) for orbit_ids in observed_map.values()
                    ),
                    "missing_words": missing,
                    "extra_words": extra,
                    "duplicate_witnesses": duplicates,
                    "pass": pass_value,
                }
            )

        classification_counts = Counter(
            row["classification"] for row in classified
        )
        selected_period_counts = Counter(
            row["period"] for row in selected_for_cycles
        )
        expected_period_counts = {
            int(period): int(count)
            for period, count in expected["primitive_orbit_counts"].items()
        }
        trace_count_identity_pass = all(
            int(expected["trace_A_power"][str(period)])
            == sum(
                divisor * expected_period_counts[divisor]
                for divisor in range(1, period + 1)
                if period % divisor == 0
            )
            for period in range(1, 13)
        )
        period_counts_pass = all(
            selected_period_counts.get(period, 0) == expected_count
            for period, expected_count in expected_period_counts.items()
        )
        transition_period_pass = all(
            row["classification"] != "NUMERIC_INSIDE"
            or (
                row["transition_pass"]
                and row["state_word_primitive_period"] == row["period"]
            )
            for row in classified
        )

        max_degree = int(protocol["cycle_block"]["maximum_degree"])
        cycle_cutoffs = []
        previous_fredholm: complex | None = None
        for cutoff in range(1, max_degree + 1):
            selected = [
                row
                for row in selected_for_cycles
                if int(row["period"]) <= cutoff
            ]
            beta_blocks = {}
            for beta_raw in protocol["cycle_block"]["euler_beta_values"]:
                beta = mp.mpf(str(beta_raw))
                factors = [
                    (
                        int(row["period"]),
                        mp.power(mp.mpf(row["unstable_modulus"]), -beta),
                    )
                    for row in selected
                ]
                coefficients = polynomial_product(factors, cutoff)
                beta_blocks[str(beta_raw)] = {
                    "coefficients": coefficient_strings(coefficients),
                    "leading_resonance": serialize_complex(
                        leading_resonance(coefficients)
                    ),
                }
            fredholm = perron_fredholm_coefficients(selected, cutoff)
            fredholm_resonance = leading_resonance(fredholm)
            cycle_cutoffs.append(
                {
                    "cutoff": cutoff,
                    "selected_orbit_count": len(selected),
                    "euler": beta_blocks,
                    "fredholm_coefficients": coefficient_strings(fredholm),
                    "fredholm_resonance": serialize_complex(fredholm_resonance),
                    "fredholm_cutoff_change": (
                        None
                        if previous_fredholm is None or fredholm_resonance is None
                        else abs(fredholm_resonance - previous_fredholm)
                    ),
                }
            )
            if fredholm_resonance is not None:
                previous_fredholm = fredholm_resonance

        beta0_final = [
            mp.mpf(value)
            for value in cycle_cutoffs[-1]["euler"]["0.0"]["coefficients"]
        ]
        expected_beta0 = protocol["symbolic_expectations"][
            "det_I_minus_zA_coefficients_through_12"
        ]
        beta0_tolerance = mp.mpf(
            str(protocol["cycle_block"]["beta0_coefficient_tolerance"])
        )
        beta0_errors = [
            abs(observed - mp.mpf(expected))
            for observed, expected in zip(beta0_final, expected_beta0)
        ]
        beta0_pass = bool(
            len(beta0_final) == len(expected_beta0)
            and max(beta0_errors, default=mp.mpf(0)) <= beta0_tolerance
        )
        final_fredholm_raw = cycle_cutoffs[-1]["fredholm_resonance"]
        final_fredholm = (
            None
            if final_fredholm_raw is None
            else complex(*final_fredholm_raw)
        )
        final_change = cycle_cutoffs[-1]["fredholm_cutoff_change"]
        fredholm_gate = bool(
            final_fredholm is not None
            and 0 < abs(final_fredholm) < 1
            and final_change is not None
            and final_change
            <= float(
                protocol["cycle_block"]["fredholm_final_cutoff_change_max"]
            )
        )

    g0 = bool(
        integrity["pass"]
        and classification_counts["ROOT_FAILED"] == 0
        and classification_counts["UNRESOLVED_NEAR_BOUNDARY"] == 0
        and all(row["high_precision_pass"] for row in classified)
    )
    g1 = bool(
        exact_word_sets_pass
        and period_counts_pass
        and trace_count_identity_pass
        and transition_period_pass
        and duplicate_witness_count == 0
    )
    g2 = bool(beta0_pass and fredholm_gate)
    output = {
        "run_id": "R059_CERTIFIED_DOMAIN_SYMBOLIC_CYCLE",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_path": portable_path(args.protocol),
        "protocol_sha256": sha256_file(args.protocol),
        "expected_words_path": portable_path(args.expected_words),
        "expected_words_sha256": sha256_file(args.expected_words),
        "catalog_path": portable_path(args.catalog),
        "catalog_sha256": sha256_file(args.catalog),
        "integrity": integrity,
        "classification_counts": dict(sorted(classification_counts.items())),
        "minimum_endpoint_distance": (
            None
            if minimum_endpoint_distance is None
            else mp.nstr(minimum_endpoint_distance, dps - 10)
        ),
        "minimum_inside_margin": (
            None
            if minimum_inside_margin is None
            else mp.nstr(minimum_inside_margin, dps - 10)
        ),
        "period_comparisons": period_comparisons,
        "selected_period_counts": {
            str(period): selected_period_counts.get(period, 0)
            for period in range(1, 13)
        },
        "trace_count_identity_pass": trace_count_identity_pass,
        "fixed_point_trace_counts": {
            str(period): int(expected["trace_A_power"][str(period)])
            for period in range(1, 13)
        },
        "primitive_orbit_counts": {
            str(period): int(expected_period_counts[period])
            for period in range(1, 13)
        },
        "primitive_phase_point_counts": {
            str(period): period * int(expected_period_counts[period])
            for period in range(1, 13)
        },
        "beta0_coefficient_audit": {
            "observed": coefficient_strings(beta0_final),
            "expected": expected_beta0,
            "absolute_errors": coefficient_strings(beta0_errors),
            "tolerance": mp.nstr(beta0_tolerance, 30),
            "pass": beta0_pass,
        },
        "selected_orbits": sorted(
            selected_for_cycles,
            key=lambda row: (row["period"], row["canonical_word"]),
        ),
        "orbit_classifications": classified,
        "cycle_cutoffs": cycle_cutoffs,
        "decisions": {
            "g0_high_precision_integrity_pass": g0,
            "g1_symbolic_word_bridge_pass": g1,
            "g2_cycle_algebra_pass": g2,
            "all_symbolic_cycle_gates_pass": g0 and g1 and g2,
            "development_precheck_disclosed": True,
            "interpretation": (
                "HIGH_PRECISION_DEVELOPMENT_CONFIRMATION_AND_CYCLE_BRIDGE_PASS"
                if g0 and g1 and g2
                else "R059_SYMBOLIC_OR_CYCLE_GATE_FAILURE"
            ),
        },
        "scope": (
            "100-digit numerical confirmation of a disclosed float64 catalog "
            "observation plus restricted finite-cycle algebra. Not interval "
            "root/boundary certification, held-out replication, global "
            "catalog completeness, or operator convergence. This numerical "
            "block does not itself establish conjugacy; the exact conjugacy "
            "on the explicit four-h-set survivor is supplied separately by "
            "the R059 symbolic contraction theorem."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    csv_rows = [
        {
            "orbit_id": row["orbit_id"],
            "period": row["period"],
            "classification": row["classification"],
            "high_precision_pass": row["high_precision_pass"],
            "endpoint_distance": row["endpoint_distance"],
            "inside_margin": row["inside_margin"],
            "canonical_word": row["canonical_word"],
            "transition_pass": row["transition_pass"],
            "state_word_primitive_period": row[
                "state_word_primitive_period"
            ],
            "scaled_residual_inf": row["scaled_residual_inf"],
            "determinant_error": row["determinant_error"],
        }
        for row in classified
    ]
    with args.csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(csv_rows[0]))
        writer.writeheader()
        writer.writerows(csv_rows)
    print(
        json.dumps(
            {
                "output": portable_path(args.output),
                "csv": portable_path(args.csv),
                "classification_counts": output["classification_counts"],
                "selected_orbits": len(selected_for_cycles),
                "g0": g0,
                "g1": g1,
                "g2": g2,
            },
            indent=2,
        )
    )
    if not (g0 and g1 and g2):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
