#!/usr/bin/env python3
"""Exact rational covering and cone audit for frozen R058.

This producer verifies local h-set crossing, forbidden transitions, the exact
symbolic adjacency matrix, and two-sided cone bounds.  It deliberately does
not turn those local checks into an entropy claim by itself: the separate
bi-infinite itinerary-realization theorem audit remains a required gate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R058_HYPERBOLIC_FILAMENT_PROTOCOL.json"
)
PROTOCOL_SHA256 = "bdd851ac14fb5cbe89ce4592b4f0e9f6cbe4fa4b76778530a2e19e7e0f1dd6f3"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "hyperbolic_covering_r058.json"
THEOREM_AUDIT = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R058_HYPERBOLIC_THEOREM_AUDIT.md"
)
THEOREM_AUDIT_SHA256 = (
    "947d4b094b6fdcc898440cea43ae7b043b606ea943b4627cd2b01d5ddafb0a38"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, default=PROTOCOL)
    parser.add_argument("--theorem-audit", type=Path, default=THEOREM_AUDIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def portable_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(resolved)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_payload(value: Fraction) -> dict[str, object]:
    return {"fraction": fraction_text(value), "float": float(value)}


def interval_payload(interval: tuple[Fraction, Fraction]) -> list[str]:
    return [fraction_text(interval[0]), fraction_text(interval[1])]


def parse_interval(values: list[str]) -> tuple[Fraction, Fraction]:
    lower, upper = (Fraction(value) for value in values)
    if not lower < upper:
        raise ValueError(f"invalid interval: {values}")
    return lower, upper


def interval_image_x(
    x_value: Fraction,
    y_interval: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    base = Fraction(1) - 6 * x_value * x_value
    y_lower, y_upper = y_interval
    return base - y_upper, base - y_lower


def intervals_disjoint(
    first: tuple[Fraction, Fraction],
    second: tuple[Fraction, Fraction],
) -> bool:
    return first[1] < second[0] or second[1] < first[0]


def strict_inside(
    inner: tuple[Fraction, Fraction],
    outer: tuple[Fraction, Fraction],
) -> tuple[bool, Fraction]:
    margin = min(inner[0] - outer[0], outer[1] - inner[1])
    return margin > 0, margin


def covering_record(
    source: str,
    target: str,
    x_intervals: dict[str, tuple[Fraction, Fraction]],
    y_intervals: dict[str, tuple[Fraction, Fraction]],
) -> dict[str, Any]:
    source_x_sign, source_y_sign = source
    target_x_sign, target_y_sign = target
    source_x = x_intervals[source_x_sign]
    source_y = y_intervals[source_y_sign]
    target_x = x_intervals[target_x_sign]
    target_y = y_intervals[target_y_sign]

    left_image = interval_image_x(source_x[0], source_y)
    right_image = interval_image_x(source_x[1], source_y)
    stable_inside, stable_margin = strict_inside(source_x, target_y)

    increasing_crossing = (
        left_image[1] < target_x[0] and right_image[0] > target_x[1]
    )
    decreasing_crossing = (
        right_image[1] < target_x[0] and left_image[0] > target_x[1]
    )
    if increasing_crossing:
        crossing_margin = min(
            target_x[0] - left_image[1],
            right_image[0] - target_x[1],
        )
        degree = 1
    elif decreasing_crossing:
        crossing_margin = min(
            target_x[0] - right_image[1],
            left_image[0] - target_x[1],
        )
        degree = -1
    else:
        crossing_margin = Fraction(0)
        degree = 0

    pass_value = (
        target_y_sign == source_x_sign
        and stable_inside
        and (increasing_crossing or decreasing_crossing)
        and degree != 0
    )
    return {
        "source": source,
        "target": target,
        "source_x": interval_payload(source_x),
        "source_y": interval_payload(source_y),
        "target_x": interval_payload(target_x),
        "target_y": interval_payload(target_y),
        "left_exit_image_x": interval_payload(left_image),
        "right_exit_image_x": interval_payload(right_image),
        "entry_strict_inside": stable_inside,
        "entry_margin": fraction_payload(stable_margin),
        "crossing_orientation": (
            "increasing"
            if increasing_crossing
            else "decreasing"
            if decreasing_crossing
            else "none"
        ),
        "crossing_margin": fraction_payload(crossing_margin),
        "covering_degree": degree,
        "pass": pass_value,
    }


def forbidden_record(
    source: str,
    target: str,
    x_intervals: dict[str, tuple[Fraction, Fraction]],
    y_intervals: dict[str, tuple[Fraction, Fraction]],
) -> dict[str, Any]:
    source_x_sign, source_y_sign = source
    target_x_sign, target_y_sign = target
    source_x = x_intervals[source_x_sign]
    source_y = y_intervals[source_y_sign]
    target_x = x_intervals[target_x_sign]
    target_y = y_intervals[target_y_sign]

    if target_y_sign != source_x_sign:
        separated = intervals_disjoint(source_x, target_y)
        if source_x[1] < target_y[0]:
            gap = target_y[0] - source_x[1]
        else:
            gap = source_x[0] - target_y[1]
        reason = "image_y_equals_source_x_and_misses_target_entry_interval"
        pass_value = separated and gap > 0
        witness = {
            "image_y_interval": interval_payload(source_x),
            "target_y_interval": interval_payload(target_y),
            "separation_gap": fraction_payload(gap),
        }
    else:
        candidates = [
            interval_image_x(source_x[0], source_y),
            interval_image_x(source_x[1], source_y),
        ]
        maximum_image_x = max(interval[1] for interval in candidates)
        gap = target_x[0] - maximum_image_x
        reason = "source_positive_y_cannot_reach_positive_target_x"
        pass_value = (
            source_y_sign == "+"
            and target_x_sign == "+"
            and maximum_image_x < target_x[0]
        )
        witness = {
            "maximum_image_x": fraction_payload(maximum_image_x),
            "target_x_lower": fraction_payload(target_x[0]),
            "separation_gap": fraction_payload(gap),
        }
    return {
        "source": source,
        "target": target,
        "reason": reason,
        "witness": witness,
        "pass": pass_value,
    }


def validate_protocol(
    path: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    actual_hash = sha256_file(path)
    checks = {
        "protocol_sha256": actual_hash == PROTOCOL_SHA256,
        "run_id": payload.get("run_id") == "R058_HYPERBOLIC_FILAMENT",
        "status": payload.get("status") == "FROZEN_BEFORE_R058_PRODUCTION",
        "a": Fraction(payload["map"]["a"]) == 6,
        "c": Fraction(payload["map"]["c"]) == 1,
        "kappa": Fraction(payload["cone"]["kappa"]) == Fraction(1, 2),
        "heldout_count": len(payload["heldout_configurations"]) == 9,
        "refinement_count": len(payload["nested_refinements"]) == 6,
    }
    parent_hashes: dict[str, dict[str, object]] = {}
    for item in payload["parent_artifacts"]:
        artifact = PROJECT_ROOT / item["path"]
        actual = sha256_file(artifact)
        parent_hashes[item["role"]] = {
            "path": item["path"],
            "expected_sha256": item["sha256"],
            "actual_sha256": actual,
            "pass": actual == item["sha256"],
        }
    checks["parent_hashes"] = all(
        bool(item["pass"]) for item in parent_hashes.values()
    )
    if not all(checks.values()):
        raise SystemExit(f"R058 protocol integrity failure: {checks}")
    return payload, {
        "protocol_path": portable_path(path),
        "protocol_sha256": actual_hash,
        "checks": checks,
        "parent_artifacts": parent_hashes,
        "pass": True,
    }


def validate_theorem_audit(path: Path) -> dict[str, object]:
    content = path.read_text(encoding="utf-8")
    normalized = " ".join(content.split())
    actual_hash = sha256_file(path)
    checks = {
        "sha256": actual_hash == THEOREM_AUDIT_SHA256,
        "status": "PROVABLE AS STATED" in content,
        "continuous_surjection": "continuous surjection" in normalized,
        "uniform_hyperbolicity": "uniformly hyperbolic" in normalized,
        "entropy_lower_bound": r"h_{\mathrm{top}}(H|_\Lambda)" in content,
        "semiconjugacy_boundary": "not injectivity" in normalized,
        "no_conjugacy": "does not justify topological conjugacy" in normalized,
    }
    return {
        "path": portable_path(path),
        "sha256": actual_hash,
        "expected_sha256": THEOREM_AUDIT_SHA256,
        "checks": checks,
        "pass": all(checks.values()),
        "status": "PROVABLE AS STATED" if all(checks.values()) else "AUDIT_MISMATCH",
    }


def main() -> None:
    args = parse_args()
    protocol, integrity = validate_protocol(args.protocol)
    theorem_audit = validate_theorem_audit(args.theorem_audit)
    h_sets = protocol["h_sets"]
    x_intervals = {
        "-": parse_interval(h_sets["x_negative"]),
        "+": parse_interval(h_sets["x_positive"]),
    }
    y_intervals = {
        "-": parse_interval(h_sets["y_negative"]),
        "+": parse_interval(h_sets["y_positive"]),
    }
    state_order = list(h_sets["state_order"])
    allowed = {
        (source, target)
        for source, target in protocol["symbolic_graph"]["allowed_edges"]
    }

    pairwise_disjoint = intervals_disjoint(
        x_intervals["-"], x_intervals["+"]
    ) and intervals_disjoint(y_intervals["-"], y_intervals["+"])
    x_inside_y = {
        sign: strict_inside(x_intervals[sign], y_intervals[sign])
        for sign in ("-", "+")
    }

    covering_records = [
        covering_record(source, target, x_intervals, y_intervals)
        for source, target in sorted(allowed)
    ]
    forbidden_records = [
        forbidden_record(source, target, x_intervals, y_intervals)
        for source in state_order
        for target in state_order
        if (source, target) not in allowed
    ]

    observed_matrix = [
        [
            int((source, target) in allowed)
            for target in state_order
        ]
        for source in state_order
    ]
    matrix = sp.Matrix(observed_matrix)
    variable = sp.symbols("lambda")
    characteristic = sp.factor(matrix.charpoly(variable).as_expr())
    expected_characteristic = (variable**2 - variable - 1) * (
        variable**2 + 1
    )
    characteristic_pass = sp.expand(characteristic - expected_characteristic) == 0

    x_half_width = Fraction(protocol["cone"]["x_half_width"])
    y_half_width = Fraction(protocol["cone"]["y_half_width"])
    kappa = Fraction(protocol["cone"]["kappa"])
    minimum_abs_x = min(abs(x_intervals["+"][0]), abs(x_intervals["-"][1]))
    minimum_abs_y = min(abs(y_intervals["+"][0]), abs(y_intervals["-"][1]))

    forward_denominator = (
        12 * minimum_abs_x - (y_half_width / x_half_width) * kappa
    )
    forward_slope = (x_half_width / y_half_width) / forward_denominator
    backward_denominator = (
        12 * minimum_abs_y - (x_half_width / y_half_width) * kappa
    )
    backward_slope = (y_half_width / x_half_width) / backward_denominator
    input_norm_squared = Fraction(1) + kappa * kappa
    forward_expansion_squared = (
        forward_denominator * forward_denominator / input_norm_squared
    )
    backward_expansion_squared = (
        backward_denominator * backward_denominator / input_norm_squared
    )
    cone_checks = {
        "x_half_width_match": x_half_width
        == (x_intervals["+"][1] - x_intervals["+"][0]) / 2,
        "y_half_width_match": y_half_width
        == (y_intervals["+"][1] - y_intervals["+"][0]) / 2,
        "forward_slope_match": fraction_text(forward_slope)
        == protocol["cone"]["forward_unstable_slope_upper_bound"],
        "backward_slope_match": fraction_text(backward_slope)
        == protocol["cone"]["backward_stable_slope_upper_bound"],
        "forward_cone_strict": forward_slope < kappa,
        "backward_cone_strict": backward_slope < kappa,
        "forward_expansion_strict": forward_expansion_squared > 1,
        "backward_expansion_strict": backward_expansion_squared > 1,
    }

    minimum_crossing_margin = min(
        Fraction(record["crossing_margin"]["fraction"])
        for record in covering_records
    )
    minimum_entry_margin = min(
        Fraction(record["entry_margin"]["fraction"])
        for record in covering_records
    )
    covering_checks = {
        "pairwise_disjoint_h_sets": pairwise_disjoint,
        "x_inside_same_sign_y": all(value[0] for value in x_inside_y.values()),
        "allowed_edge_count": len(covering_records) == 6,
        "all_allowed_coverings": all(record["pass"] for record in covering_records),
        "forbidden_edge_count": len(forbidden_records) == 10,
        "all_forbidden_excluded": all(record["pass"] for record in forbidden_records),
        "minimum_crossing_margin_match": minimum_crossing_margin
        == Fraction(protocol["theory_gates"]["b1_covering"][
            "minimum_exit_crossing_margin"
        ]),
        "minimum_entry_margin_match": minimum_entry_margin
        == Fraction(protocol["theory_gates"]["b1_covering"][
            "minimum_entry_interior_margin"
        ]),
        "adjacency_matrix_match": observed_matrix
        == protocol["symbolic_graph"]["adjacency_matrix"],
        "characteristic_polynomial_match": characteristic_pass,
    }
    local_exact_pass = all(covering_checks.values()) and all(cone_checks.values())
    full_primary_pass = local_exact_pass and bool(theorem_audit["pass"])

    output = {
        "run_id": "R058_HYPERBOLIC_COVERING",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_integrity": integrity,
        "theorem_audit": theorem_audit,
        "h_sets": {
            "x_intervals": {
                sign: interval_payload(interval)
                for sign, interval in x_intervals.items()
            },
            "y_intervals": {
                sign: interval_payload(interval)
                for sign, interval in y_intervals.items()
            },
            "same_sign_x_inside_y": {
                sign: {
                    "pass": value[0],
                    "margin": fraction_payload(value[1]),
                }
                for sign, value in x_inside_y.items()
            },
        },
        "covering_records": covering_records,
        "forbidden_transition_records": forbidden_records,
        "symbolic_graph": {
            "state_order": state_order,
            "adjacency_matrix": observed_matrix,
            "characteristic_polynomial": str(characteristic),
            "characteristic_polynomial_match": characteristic_pass,
            "spectral_radius_exact": "(1+sqrt(5))/2",
            "entropy_lower_bound_exact_if_theorem_gate_passes": "log((1+sqrt(5))/2)",
        },
        "cone_certificate": {
            "coordinate_system": protocol["cone"]["coordinate_system"],
            "kappa": fraction_payload(kappa),
            "x_half_width": fraction_payload(x_half_width),
            "y_half_width": fraction_payload(y_half_width),
            "forward_denominator_lower_bound": fraction_payload(
                forward_denominator
            ),
            "forward_unstable_slope_upper_bound": fraction_payload(
                forward_slope
            ),
            "forward_expansion_factor_squared_lower_bound": fraction_payload(
                forward_expansion_squared
            ),
            "backward_denominator_lower_bound": fraction_payload(
                backward_denominator
            ),
            "backward_stable_slope_upper_bound": fraction_payload(
                backward_slope
            ),
            "backward_expansion_factor_squared_lower_bound": fraction_payload(
                backward_expansion_squared
            ),
            "checks": cone_checks,
            "pass": all(cone_checks.values()),
        },
        "decisions": {
            "b0_integrity_pass": integrity["pass"],
            "b1_exact_covering_pass": all(covering_checks.values()),
            "b2_local_cone_pass": all(cone_checks.values()),
            "local_exact_certificate_pass": local_exact_pass,
            "bi_infinite_itinerary_realization_theorem_audit_pass": theorem_audit[
                "pass"
            ],
            "full_primary_claim_enabled": full_primary_pass,
            "entropy_claim_enabled": full_primary_pass,
            "interpretation": (
                "FULL_PRIMARY_CLAIM_CERTIFIED"
                if full_primary_pass
                else "LOCAL_EXACT_GATES_PASS_THEOREM_AUDIT_FAILED"
                if local_exact_pass
                else "LOCAL_EXACT_GATE_FAILURE"
            ),
        },
        "scope": (
            "Certified conservative uniformly hyperbolic survivor with a "
            "continuous surjective symbolic factor and entropy lower bound; "
            "no conjugacy, entropy equality, Markov partition, graph limit, "
            "operator convergence, zeta, or number-theory claim."
            if full_primary_pass
            else "Exact local h-set covering and cone arithmetic only; the "
            "separate theorem audit did not pass."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": portable_path(args.output),
                "protocol_sha256": integrity["protocol_sha256"],
                "local_exact_certificate_pass": local_exact_pass,
                "theorem_audit_pass": theorem_audit["pass"],
                "full_primary_claim_enabled": full_primary_pass,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
