#!/usr/bin/env python3
"""Independent checker for the R059 high-precision symbolic bridge.

The producer performs Newton refinement and cycle algebra.  This checker does
not import those helpers: it independently enumerates the frozen SFT words,
reclassifies the persisted high-precision coordinates, and verifies the
period-by-period witness ledger and count identities.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = PROJECT_ROOT / "research" / "refine-logs" / "R059_CERTIFIED_DOMAIN_PROTOCOL.json"
EXPECTED = PROJECT_ROOT / "research" / "refine-logs" / "R059_EXPECTED_SYMBOLIC_WORDS.json"
CATALOG = PROJECT_ROOT / "results" / "complex_root_census_a6_n12_merged.json"
INPUT = PROJECT_ROOT / "results" / "certified_domain_r059.json"
OUTPUT = PROJECT_ROOT / "results" / "certified_domain_r059_check.json"
PROTOCOL_SHA256 = "f94801f5b7abd5baaebd4c859a3662af4cf6d63954b1f4b18aaa6e8d3596f2b6"
STATE_ORDER = ("--", "-+", "+-", "++")
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, default=PROTOCOL)
    parser.add_argument("--expected", type=Path, default=EXPECTED)
    parser.add_argument("--catalog", type=Path, default=CATALOG)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def portable(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path.resolve())


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[shift:] + word[:shift] for shift in range(len(word)))


def primitive_period(word: tuple[int, ...]) -> int:
    for period in range(1, len(word) + 1):
        if len(word) % period == 0 and all(
            word[index] == word[index % period] for index in range(len(word))
        ):
            return period
    raise AssertionError("finite word has no period")


def closed_words(period: int) -> list[tuple[int, ...]]:
    words: list[tuple[int, ...]] = []
    for first in range(4):
        stack = [(first, (first,))]
        while stack:
            current, word = stack.pop()
            if len(word) == period:
                if ADJACENCY[current][first]:
                    words.append(word)
                continue
            for target in range(3, -1, -1):
                if ADJACENCY[current][target]:
                    stack.append((target, word + (target,)))
    return words


def independent_words() -> tuple[dict[str, list[str]], dict[str, int], dict[str, int]]:
    words: dict[str, list[str]] = {}
    traces: dict[str, int] = {}
    counts: dict[str, int] = {}
    for period in range(1, 13):
        closed = closed_words(period)
        primitive = sorted(
            {
                canonical_rotation(word)
                for word in closed
                if primitive_period(word) == period
            }
        )
        words[str(period)] = [
            "|".join(STATE_ORDER[state] for state in word) for word in primitive
        ]
        traces[str(period)] = len(closed)
        counts[str(period)] = len(primitive)
    return words, traces, counts


def decimal_fraction(text: str) -> Decimal:
    value = Fraction(text)
    return Decimal(value.numerator) / Decimal(value.denominator)


def canonical_decimal(value: Decimal) -> str:
    return format(value, "f")


def classify(value: Decimal, intervals: dict[str, tuple[Decimal, Decimal]]) -> str | None:
    for sign in ("-", "+"):
        lower, upper = intervals[sign]
        if lower < value < upper:
            return sign
    return None


def main() -> None:
    getcontext().prec = 140
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    expected = json.loads(args.expected.read_text(encoding="utf-8"))
    catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    payload = json.loads(args.input.read_text(encoding="utf-8"))

    parent_checks = {
        "protocol_sha256": sha256_file(args.protocol) == PROTOCOL_SHA256,
        "expected_sha256": sha256_file(args.expected)
        == protocol["symbolic_expectations"]["frozen_word_artifact_sha256"],
        "catalog_sha256": sha256_file(args.catalog)
        == protocol["catalog"]["sha256"],
        "input_protocol_sha256": payload.get("protocol_sha256") == PROTOCOL_SHA256,
        "input_run_id": payload.get("run_id") == "R059_CERTIFIED_DOMAIN_SYMBOLIC_CYCLE",
    }

    words, traces, primitive_counts = independent_words()
    canonical_payload = json.dumps(
        words, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    symbolic_checks = {
        "word_sets_hash": hashlib.sha256(canonical_payload).hexdigest()
        == protocol["symbolic_expectations"]["canonical_word_set_sha256"],
        "word_artifact_matches": words == expected["primitive_words"],
        "trace_table_matches": traces == expected["trace_A_power"],
        "primitive_count_table_matches": primitive_counts
        == expected["primitive_orbit_counts"],
    }

    interval_data = protocol["h_sets"]
    x_intervals = {
        sign: (decimal_fraction(values[0]), decimal_fraction(values[1]))
        for sign, values in interval_data["x_intervals"].items()
    }
    y_intervals = {
        sign: (decimal_fraction(values[0]), decimal_fraction(values[1]))
        for sign, values in interval_data["y_intervals"].items()
    }
    threshold = Decimal(protocol["catalog"]["endpoint_ambiguity_threshold"])
    all_endpoints = [
        endpoint
        for mapping in (x_intervals, y_intervals)
        for pair in mapping.values()
        for endpoint in pair
    ]

    catalog_rows = {str(row["orbit_id"]): row for row in catalog["real_primitive_orbits"]}
    classifications = payload.get("orbit_classifications", [])
    observed_words: dict[int, dict[str, list[str]]] = defaultdict(
        lambda: defaultdict(list)
    )
    independently_inside: set[str] = set()
    reclassification_rows: list[dict[str, Any]] = []
    reclassification_pass = True
    classification_ids: set[str] = set()
    catalog_alignment_pass = True
    minimum_endpoint_distance: Decimal | None = None
    for record in classifications:
        orbit_id = str(record["orbit_id"])
        classification_ids.add(orbit_id)
        catalog_row = catalog_rows.get(orbit_id)
        catalog_alignment_pass = catalog_alignment_pass and bool(
            catalog_row is not None
            and int(catalog_row["period"]) == int(record["period"])
            and len(catalog_row["sequence"]) == len(record["refined_sequence"])
        )
        sequence = [Decimal(value) for value in record["refined_sequence"]]
        endpoint_distance = min(
            abs(value - endpoint) for value in sequence for endpoint in all_endpoints
        )
        minimum_endpoint_distance = (
            endpoint_distance
            if minimum_endpoint_distance is None
            else min(minimum_endpoint_distance, endpoint_distance)
        )
        if not bool(record["high_precision_pass"]):
            classification = "ROOT_FAILED"
            canonical_word = None
            transition_pass = False
            word_period = None
        elif endpoint_distance <= threshold:
            classification = "UNRESOLVED_NEAR_BOUNDARY"
            canonical_word = None
            transition_pass = False
            word_period = None
        else:
            labels: list[str] = []
            for index, x_value in enumerate(sequence):
                y_value = sequence[(index - 1) % len(sequence)]
                x_sign = classify(x_value, x_intervals)
                y_sign = classify(y_value, y_intervals)
                if x_sign is None or y_sign is None:
                    labels = []
                    break
                labels.append(x_sign + y_sign)
            if len(labels) != len(sequence):
                classification = "NUMERIC_OUTSIDE"
                canonical_word = None
                transition_pass = False
                word_period = None
            else:
                classification = "NUMERIC_INSIDE"
                indices = tuple(STATE_ORDER.index(label) for label in labels)
                transition_pass = all(
                    ADJACENCY[indices[index]][indices[(index + 1) % len(indices)]]
                    == 1
                    for index in range(len(indices))
                )
                word_period = primitive_period(indices)
                canonical = canonical_rotation(indices)
                canonical_word = "|".join(STATE_ORDER[index] for index in canonical)
                observed_words[int(record["period"])][canonical_word].append(orbit_id)
                independently_inside.add(orbit_id)
        passed = (
            classification == record["classification"]
            and canonical_word == record["canonical_word"]
            and transition_pass == bool(record["transition_pass"])
            and word_period == record["state_word_primitive_period"]
        )
        reclassification_pass = reclassification_pass and passed
        reclassification_rows.append(
            {
                "orbit_id": orbit_id,
                "period": int(record["period"]),
                "producer_classification": record["classification"],
                "independent_classification": classification,
                "producer_word": record["canonical_word"],
                "independent_word": canonical_word,
                "endpoint_distance": canonical_decimal(endpoint_distance),
                "pass": passed,
            }
        )

    period_rows = []
    word_set_pass = True
    duplicate_count = 0
    for period in range(1, 13):
        expected_set = set(words[str(period)])
        observed = observed_words.get(period, {})
        observed_set = set(observed)
        duplicates = {
            word: ids for word, ids in observed.items() if len(ids) > 1
        }
        duplicate_count += sum(len(ids) - 1 for ids in duplicates.values())
        passed = (
            expected_set == observed_set
            and not duplicates
            and len(observed_set) == primitive_counts[str(period)]
        )
        word_set_pass = word_set_pass and passed
        period_rows.append(
            {
                "period": period,
                "expected_count": len(expected_set),
                "observed_count": len(observed_set),
                "missing": sorted(expected_set - observed_set),
                "extra": sorted(observed_set - expected_set),
                "duplicates": duplicates,
                "pass": passed,
            }
        )

    classification_counts = Counter(
        row["independent_classification"] for row in reclassification_rows
    )
    expected_counts = {
        "NUMERIC_INSIDE": 79,
        "NUMERIC_OUTSIDE": 668,
        "UNRESOLVED_NEAR_BOUNDARY": 0,
        "ROOT_FAILED": 0,
    }
    trace_identity = all(
        int(traces[str(period)])
        == sum(
            divisor * primitive_counts[str(divisor)]
            for divisor in range(1, period + 1)
            if period % divisor == 0
        )
        for period in range(1, 13)
    )
    checks = {
        **parent_checks,
        **symbolic_checks,
        "catalog_record_count": len(catalog_rows) == 747,
        "classification_record_count": len(classifications) == 747,
        "classification_ids_unique": len(classification_ids) == len(classifications),
        "catalog_alignment": catalog_alignment_pass
        and classification_ids == set(catalog_rows),
        "classification_counts": all(
            classification_counts.get(label, 0) == count
            for label, count in expected_counts.items()
        ),
        "reclassification": reclassification_pass,
        "word_sets": word_set_pass,
        "duplicate_witness_count": duplicate_count == 0,
        "trace_primitive_identity": trace_identity,
        "selected_ids_match": independently_inside
        == {str(row["orbit_id"]) for row in payload.get("selected_orbits", [])}
        and len(payload.get("selected_orbits", [])) == len(independently_inside),
    }
    output = {
        "run_id": "R059_CERTIFIED_DOMAIN_INDEPENDENT_CHECK",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_path": portable(args.protocol),
        "protocol_sha256": sha256_file(args.protocol),
        "input_path": portable(args.input),
        "input_sha256": sha256_file(args.input),
        "parent_checks": parent_checks,
        "symbolic_checks": symbolic_checks,
        "classification_counts": {
            label: classification_counts.get(label, 0) for label in expected_counts
        },
        "period_rows": period_rows,
        "reclassification_rows": reclassification_rows,
        "minimum_endpoint_distance": (
            None
            if minimum_endpoint_distance is None
            else canonical_decimal(minimum_endpoint_distance)
        ),
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "status": "PASS" if all(checks.values()) else "FAIL",
        "scope": (
            "Independent re-enumeration and reclassification of the R059 "
            "high-precision symbolic bridge; it does not certify interval "
            "root completeness or continuous operator convergence."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": portable(args.output),
                "status": output["status"],
                "all_checks_pass": output["all_checks_pass"],
            },
            indent=2,
        )
    )
    if not output["all_checks_pass"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
