#!/usr/bin/env python3
"""Generate a complete primitive-orbit catalogue from the certified SFT."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

import mpmath as mp

from henon_roof import (
    build_orbit_catalog,
    compare_prior_catalog,
    exact_clock_audit,
    primitive_counts,
    serialize_catalog,
    symbolic_fixed_point_counts,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PROJECT_ROOT.parent
DEFAULT_PROTOCOL = PROJECT_ROOT / "refine-logs" / "R000_FROZEN_PROTOCOL.json"
DEFAULT_DEPENDENCY_LOCK = (
    PROJECT_ROOT / "refine-logs" / "INHERITED_DEPENDENCIES.json"
)
DEFAULT_PRIOR = (
    REPOSITORY_ROOT
    / "docs"
    / "related_programs"
    / "henon_weighted_zeta"
    / "results"
    / "certified_domain_r059.json"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-period", type=int, required=True)
    parser.add_argument("--parameter", type=str, default="6")
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--label", type=str, required=True)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--prior-catalog", type=Path, default=DEFAULT_PRIOR)
    return parser.parse_args()


def guard_monodromy_determinant_error(record: object, dps: int) -> mp.mpf:
    """Recompute det(DH^n) with guard digits from the persisted orbit coordinates.

    Long hyperbolic products can lose digits when their determinant is obtained
    by subtracting two very large products.  The serialized 80-digit value is
    retained as a transparency diagnostic; this guard calculation is the
    meaningful numerical check of the analytic identity det(DH)=1.
    """

    with mp.workdps(dps + 40):
        a_value = mp.mpf(record.parameter)
        monodromy = mp.eye(2)
        for coordinate_text in record.coordinates:
            coordinate = mp.mpf(coordinate_text)
            jacobian = mp.matrix([[-2 * a_value * coordinate, -1], [1, 0]])
            monodromy = jacobian * monodromy
        determinant = (
            monodromy[0, 0] * monodromy[1, 1]
            - monodromy[0, 1] * monodromy[1, 0]
        )
        return abs(determinant - 1)


def main() -> None:
    args = parse_args()
    if args.max_period < 1:
        raise SystemExit("--max-period must be positive")
    if args.dps < 40:
        raise SystemExit("--dps must be at least 40")
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    protocol_hash = sha256_file(args.protocol)
    dependency_lock = json.loads(
        DEFAULT_DEPENDENCY_LOCK.read_text(encoding="utf-8")
    )

    records = build_orbit_catalog(
        max_period=args.max_period,
        parameter=args.parameter,
        dps=args.dps,
    )
    counts = Counter(record.period for record in records)
    expected_counts = primitive_counts(args.max_period)
    count_match = all(counts.get(period, 0) == count for period, count in expected_counts.items())

    with mp.workdps(args.dps + 40):
        recurrence_residuals = [mp.mpf(record.recurrence_residual) for record in records]
        serialized_determinant_errors = [
            abs(mp.mpf(record.monodromy_determinant) - 1) for record in records
        ]
        guard_determinant_errors = [
            guard_monodromy_determinant_error(record, args.dps) for record in records
        ]
        contraction_bounds = [mp.mpf(record.contraction_error_bound) for record in records]
        hyperbolicity_margins = [
            abs(mp.mpf(record.monodromy_trace)) - 2 for record in records
        ]

    prior_bridge: dict[str, object] | None = None
    if mp.almosteq(mp.mpf(args.parameter), 6) and args.max_period >= 12:
        if not args.prior_catalog.exists():
            raise SystemExit(f"required period-12 bridge is missing: {args.prior_catalog}")
        expected_prior_hash = next(
            row["sha256"]
            for row in dependency_lock["dependencies"]
            if row["path"].endswith("/certified_domain_r059.json")
        )
        if sha256_file(args.prior_catalog) != expected_prior_hash:
            raise SystemExit("period-12 bridge does not match inherited dependency lock")
        prior_bridge = compare_prior_catalog(records, args.prior_catalog)

    payload = {
        "run_id": f"catalog_{args.label}",
        "created_utc": protocol["created_utc"],
        "protocol_path": str(args.protocol.relative_to(PROJECT_ROOT)),
        "protocol_sha256": protocol_hash,
        "candidate_id": protocol["candidate_id"],
        "parameter": args.parameter,
        "max_period": args.max_period,
        "precision_dps": args.dps,
        "scope": "complete primitive orbit ledger for the frozen four-state symbolic survivor; neighboring parameters are numerical continuations only",
        "primitive_counts": {str(period): expected_counts[period] for period in expected_counts},
        "symbolic_fixed_point_counts": {
            str(period): count for period, count in symbolic_fixed_point_counts(args.max_period).items()
        },
        "total_primitive_orbits": len(records),
        "orientation_counts": {str(key): value for key, value in sorted(Counter(record.orientation for record in records).items())},
        "gates": {
            "symbolic_count_match": count_match,
            "all_recurrence_residuals_below_1e_minus_50": all(value < mp.mpf("1e-50") for value in recurrence_residuals),
            "all_determinant_errors_below_1e_minus_50": all(
                value < mp.mpf("1e-50") for value in guard_determinant_errors
            ),
            "all_contraction_bounds_below_1e_minus_50": all(value < mp.mpf("1e-50") for value in contraction_bounds),
            "all_cycles_hyperbolic": all(value > 0 for value in hyperbolicity_margins),
        },
        "metrics": {
            "maximum_recurrence_residual": str(max(recurrence_residuals, default=mp.mpf(0))),
            "maximum_determinant_error": str(
                max(guard_determinant_errors, default=mp.mpf(0))
            ),
            "maximum_serialized_monodromy_determinant_error": str(
                max(serialized_determinant_errors, default=mp.mpf(0))
            ),
            "determinant_error_method": (
                "guard-precision recomputation from persisted coordinates; "
                "serialized 80-dps cancellation error reported separately"
            ),
            "maximum_contraction_error_bound": str(max(contraction_bounds, default=mp.mpf(0))),
            "minimum_hyperbolicity_margin": str(min(hyperbolicity_margins, default=mp.inf)),
            "maximum_contraction_iterations": max(
                (record.contraction_iterations for record in records), default=0
            ),
        },
        "exact_clock_audit": exact_clock_audit() if mp.almosteq(mp.mpf(args.parameter), 6) else None,
        "prior_period12_bridge": prior_bridge,
        "orbits": serialize_catalog(records),
    }

    output_json = PROJECT_ROOT / "results" / f"catalog_{args.label}.json"
    output_csv = PROJECT_ROOT / "results" / f"catalog_{args.label}.csv"
    output_json.write_text(
        json.dumps(payload, allow_nan=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    rows: list[dict[str, object]] = []
    for record in records:
        row = {
            key: value
            for key, value in record.__dict__.items()
            if key != "coordinates"
        }
        row["coordinates"] = ";".join(record.coordinates)
        rows.append(row)
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(
        json.dumps(
            {
                "json": str(output_json),
                "csv": str(output_csv),
                "orbits": len(records),
                "gates": payload["gates"],
                "protocol_sha256": protocol_hash,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
