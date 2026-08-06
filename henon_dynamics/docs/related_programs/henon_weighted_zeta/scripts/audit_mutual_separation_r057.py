#!/usr/bin/env python3
"""Audit the exact R057 mutual-outer boundary separation criterion.

The production object is a finite exact-rational cell-incidence certificate.
Every pass/fail decision uses :class:`fractions.Fraction`; float fields are
display-only.  See ``R057_MUTUAL_SEPARATION_MANIFEST.md`` for the frozen scope.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import json
import platform
import sys
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.audit_exact_closed_cover import (  # noqa: E402
    exact_abs_extrema,
    exact_edge_vector,
    uncapped_adaptive_subdivisions_exact,
)


PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R057_MUTUAL_SEPARATION_PROTOCOL.json"
)
PROTOCOL_SHA256 = "4eb540372ad29568054cdaa05b7c3f605913dfcf358855c98f45594c78af0a91"
MAX_SUBDIVISIONS = 64


@dataclass(frozen=True)
class Configuration:
    panel_id: str
    configuration_id: str
    role: str
    grid: int
    grid_offset: Fraction
    a: Fraction
    c: Fraction
    radius: Fraction
    eta: Fraction
    fresh_discovery_eligible: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-stem", default="mutual_separation_r057")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results")
    parser.add_argument("--workers", type=int, default=1)
    return parser.parse_args()


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_or_infinity_text(value: Fraction | None) -> str:
    return "inf" if value is None else fraction_text(value)


def fraction_or_none_float(value: Fraction | None) -> float | None:
    return None if value is None else float(value)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _slug(value: Fraction) -> str:
    sign = "m" if value < 0 else "p" if value > 0 else "z"
    magnitude = abs(value)
    return f"{sign}{magnitude.numerator}_{magnitude.denominator}"


def load_and_validate_protocol() -> dict[str, object]:
    if not PROTOCOL.is_file():
        raise SystemExit(f"missing frozen R057 protocol: {PROTOCOL}")
    actual_hash = _sha256(PROTOCOL)
    if actual_hash != PROTOCOL_SHA256:
        raise SystemExit(
            "R057 protocol hash mismatch: "
            f"expected {PROTOCOL_SHA256}, observed {actual_hash}"
        )
    payload = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    defaults = payload["default_constants"]
    checks = {
        "run_id": payload.get("run_id") == "R057_MUTUAL_SEPARATION",
        "status": payload.get("status") == "FROZEN_BEFORE_PRODUCTION",
        "maximum_subdivisions": int(defaults["maximum_subdivisions"])
        == MAX_SUBDIVISIONS,
        "panel_count": len(payload["production_panels"]) == 4,
        "shifted_control_count": len(payload["shifted_prior_pass_controls"]) == 4,
    }
    if not all(checks.values()):
        raise SystemExit(f"R057 code/protocol mismatch: {checks}")
    return payload


def expand_configurations(payload: dict[str, object]) -> list[Configuration]:
    jobs: list[Configuration] = []

    for item in payload["shifted_prior_pass_controls"]:
        jobs.append(
            Configuration(
                panel_id="shifted_prior_pass_controls",
                configuration_id=str(item["configuration_id"]),
                role="development_prior_pass_control",
                grid=int(item["grid"]),
                grid_offset=Fraction(str(item["grid_offset"])),
                a=Fraction(str(item["a"])),
                c=Fraction(str(item["c"])),
                radius=Fraction(str(item["radius"])),
                eta=Fraction(str(item["eta"])),
                fresh_discovery_eligible=False,
            )
        )

    for panel in payload["production_panels"]:
        panel_id = str(panel["panel_id"])
        role = str(panel["role"])
        radius = Fraction(str(panel["radius"]))
        c = Fraction(str(panel["c"]))
        offsets = [Fraction(str(value)) for value in panel["grid_offsets"]]

        if panel_id == "centered_resolution_scan":
            a = Fraction(str(panel["a"]))
            eta = Fraction(str(panel["eta"]))
            excluded = {int(value) for value in panel["fresh_discovery_exclusions"]}
            grids = range(
                int(panel["grid_min"]),
                int(panel["grid_max"]) + 1,
                int(panel["grid_step"]),
            )
            for grid in grids:
                for offset in offsets:
                    jobs.append(
                        Configuration(
                            panel_id=panel_id,
                            configuration_id=f"centered_n{grid}_d{_slug(offset)}",
                            role=role,
                            grid=grid,
                            grid_offset=offset,
                            a=a,
                            c=c,
                            radius=radius,
                            eta=eta,
                            fresh_discovery_eligible=grid not in excluded,
                        )
                    )
        elif panel_id == "rational_phase_stress":
            a = Fraction(str(panel["a"]))
            eta = Fraction(str(panel["eta"]))
            for grid in (int(value) for value in panel["grids"]):
                for offset in offsets:
                    jobs.append(
                        Configuration(
                            panel_id=panel_id,
                            configuration_id=f"phase_n{grid}_d{_slug(offset)}",
                            role=role,
                            grid=grid,
                            grid_offset=offset,
                            a=a,
                            c=c,
                            radius=radius,
                            eta=eta,
                            fresh_discovery_eligible=True,
                        )
                    )
        elif panel_id == "eta_stress":
            a = Fraction(str(panel["a"]))
            for grid in (int(value) for value in panel["grids"]):
                for offset in offsets:
                    for eta in (Fraction(str(value)) for value in panel["etas"]):
                        jobs.append(
                            Configuration(
                                panel_id=panel_id,
                                configuration_id=(
                                    f"eta_n{grid}_d{_slug(offset)}_e{_slug(eta)}"
                                ),
                                role=role,
                                grid=grid,
                                grid_offset=offset,
                                a=a,
                                c=c,
                                radius=radius,
                                eta=eta,
                                fresh_discovery_eligible=True,
                            )
                        )
        elif panel_id == "a_stress":
            eta = Fraction(str(panel["eta"]))
            for grid in (int(value) for value in panel["grids"]):
                for offset in offsets:
                    for a in (Fraction(str(value)) for value in panel["a_values"]):
                        jobs.append(
                            Configuration(
                                panel_id=panel_id,
                                configuration_id=(
                                    f"a_n{grid}_d{_slug(offset)}_a{_slug(a)}"
                                ),
                                role=role,
                                grid=grid,
                                grid_offset=offset,
                                a=a,
                                c=c,
                                radius=radius,
                                eta=eta,
                                fresh_discovery_eligible=True,
                            )
                        )
        else:
            raise AssertionError(f"unknown frozen R057 panel: {panel_id}")

    expected_counts = {
        "shifted_prior_pass_controls": 4,
        "centered_resolution_scan": 352,
        "rational_phase_stress": 48,
        "eta_stress": 64,
        "a_stress": 49,
    }
    observed_counts = {
        panel_id: sum(job.panel_id == panel_id for job in jobs)
        for panel_id in expected_counts
    }
    if observed_counts != expected_counts:
        raise AssertionError(
            f"frozen R057 panel expansion mismatch: {observed_counts}"
        )
    if len({job.configuration_id for job in jobs}) != len(jobs):
        raise AssertionError("R057 configuration ids are not unique")
    return jobs


def quadratic_range(
    lower: Fraction, upper: Fraction, a: Fraction
) -> tuple[Fraction, Fraction]:
    if a <= 0:
        raise ValueError("R057 requires a>0")
    minimum_abs, maximum_abs = exact_abs_extrema(lower, upper)
    return a * minimum_abs**2, a * maximum_abs**2


def intervals_intersect(
    first: tuple[Fraction, Fraction], second: tuple[Fraction, Fraction]
) -> bool:
    return max(first[0], second[0]) <= min(first[1], second[1])


def _endpoint_tables(
    edges: Sequence[Fraction], c: Fraction
) -> tuple[
    list[Fraction],
    dict[Fraction, tuple[int, int]],
    list[Fraction],
    dict[Fraction, tuple[int, int]],
]:
    grid = len(edges) - 1
    lower_witness: dict[Fraction, tuple[int, int]] = {}
    upper_witness: dict[Fraction, tuple[int, int]] = {}
    for j in range(grid):
        for k in range(grid):
            lower = c - edges[k + 1] - edges[j + 1]
            upper = c - edges[k] - edges[j]
            pair = (j, k)
            if lower not in lower_witness or pair < lower_witness[lower]:
                lower_witness[lower] = pair
            if upper not in upper_witness or pair < upper_witness[upper]:
                upper_witness[upper] = pair
    return (
        sorted(lower_witness),
        lower_witness,
        sorted(upper_witness),
        upper_witness,
    )


def _nearest_above(
    values: Sequence[Fraction],
    witnesses: dict[Fraction, tuple[int, int]],
    point: Fraction,
) -> tuple[Fraction | None, Fraction | None, tuple[int, int] | None]:
    index = bisect.bisect_right(values, point)
    if index == len(values):
        return None, None, None
    endpoint = values[index]
    return endpoint - point, endpoint, witnesses[endpoint]


def _nearest_below(
    values: Sequence[Fraction],
    witnesses: dict[Fraction, tuple[int, int]],
    point: Fraction,
) -> tuple[Fraction | None, Fraction | None, tuple[int, int] | None]:
    index = bisect.bisect_left(values, point) - 1
    if index < 0:
        return None, None, None
    endpoint = values[index]
    return point - endpoint, endpoint, witnesses[endpoint]


def _failure_witness(
    *,
    configuration: Configuration,
    edges: Sequence[Fraction],
    boundary_index: int,
    side: str,
    pair: tuple[int, int],
    coefficient_interval: tuple[Fraction, Fraction],
    q_boundary: Fraction,
    left_slab: tuple[Fraction, Fraction],
    right_slab: tuple[Fraction, Fraction],
    left_q_range: tuple[Fraction, Fraction],
    right_q_range: tuple[Fraction, Fraction],
) -> dict[str, object]:
    grid = configuration.grid
    j, k = pair
    i = boundary_index - 1
    ell = boundary_index
    source_id = j * grid + i
    target_id = ell * grid + k
    true_closed = coefficient_interval[0] <= q_boundary <= coefficient_interval[1]
    forward_outer = intervals_intersect(left_q_range, coefficient_interval)
    inverse_reverse_outer = intervals_intersect(right_q_range, coefficient_interval)
    return {
        "failure_side": side,
        "boundary_index": boundary_index,
        "shared_boundary_fraction": fraction_text(edges[boundary_index]),
        "q_boundary_fraction": fraction_text(q_boundary),
        "source_indices": {"x": i, "y": j},
        "target_indices": {"x": k, "y": ell},
        "source_id": source_id,
        "target_id": target_id,
        "coefficient_indices": {"j": j, "k": k},
        "coefficient_interval_fraction": [
            fraction_text(coefficient_interval[0]),
            fraction_text(coefficient_interval[1]),
        ],
        "source_x_interval_fraction": [
            fraction_text(edges[i]),
            fraction_text(edges[i + 1]),
        ],
        "source_y_interval_fraction": [
            fraction_text(edges[j]),
            fraction_text(edges[j + 1]),
        ],
        "target_x_interval_fraction": [
            fraction_text(edges[k]),
            fraction_text(edges[k + 1]),
        ],
        "target_y_interval_fraction": [
            fraction_text(edges[ell]),
            fraction_text(edges[ell + 1]),
        ],
        "left_boundary_slab_fraction": [
            fraction_text(left_slab[0]),
            fraction_text(left_slab[1]),
        ],
        "right_boundary_slab_fraction": [
            fraction_text(right_slab[0]),
            fraction_text(right_slab[1]),
        ],
        "left_q_range_fraction": [
            fraction_text(left_q_range[0]),
            fraction_text(left_q_range[1]),
        ],
        "right_q_range_fraction": [
            fraction_text(right_q_range[0]),
            fraction_text(right_q_range[1]),
        ],
        "true_closed_present": true_closed,
        "forward_outer_present": forward_outer,
        "inverse_reverse_outer_present": inverse_reverse_outer,
        "mutual_outer_present": forward_outer and inverse_reverse_outer,
        "forward_outer_positive": False,
        "inverse_reverse_outer_positive": False,
        "exact_false_mutual_witness_pass": (
            not true_closed and forward_outer and inverse_reverse_outer
        ),
    }


def _boundary_hash(rows: Iterable[dict[str, object]]) -> str:
    digest = hashlib.sha256()
    fields = (
        "boundary_index",
        "boundary_fraction",
        "q_boundary_fraction",
        "left_k",
        "right_k",
        "omega_plus_fraction",
        "delta_plus_fraction",
        "margin_plus_fraction",
        "omega_minus_fraction",
        "delta_minus_fraction",
        "margin_minus_fraction",
        "plus_pass",
        "minus_pass",
    )
    for row in rows:
        digest.update(
            ("|".join(str(row[field]) for field in fields) + "\n").encode("ascii")
        )
    return digest.hexdigest()


def summarize_configuration(
    configuration: Configuration,
) -> tuple[dict[str, object], list[dict[str, object]]]:
    edges = exact_edge_vector(
        configuration.radius, configuration.grid, configuration.grid_offset
    )
    if len(edges) != configuration.grid + 1:
        raise AssertionError("unexpected edge-vector length")
    edges_strict = all(upper > lower for lower, upper in zip(edges, edges[1:]))
    minimum_width = min(upper - lower for lower, upper in zip(edges, edges[1:]))
    uncapped_k_values = [
        uncapped_adaptive_subdivisions_exact(
            edges[index],
            edges[index + 1],
            minimum_width,
            a_value=configuration.a,
            eta=configuration.eta,
        )
        for index in range(configuration.grid)
    ]
    k_values = [min(MAX_SUBDIVISIONS, value) for value in uncapped_k_values]
    cap_active_count = sum(value >= MAX_SUBDIVISIONS for value in uncapped_k_values)

    (
        lower_values,
        lower_witnesses,
        upper_values,
        upper_witnesses,
    ) = _endpoint_tables(edges, configuration.c)

    boundary_rows: list[dict[str, object]] = []
    failure_witnesses: list[dict[str, object]] = []
    finite_margins: list[tuple[Fraction, int, str]] = []
    finite_headroom_ratios: list[tuple[Fraction, int, str]] = []

    for boundary_index in range(1, configuration.grid):
        boundary = edges[boundary_index]
        left_width = (edges[boundary_index] - edges[boundary_index - 1]) / k_values[
            boundary_index - 1
        ]
        right_width = (edges[boundary_index + 1] - edges[boundary_index]) / k_values[
            boundary_index
        ]
        left_slab = (boundary - left_width, boundary)
        right_slab = (boundary, boundary + right_width)
        left_q_range = quadratic_range(*left_slab, configuration.a)
        right_q_range = quadratic_range(*right_slab, configuration.a)
        q_boundary = configuration.a * boundary**2
        if not (
            left_q_range[0] <= q_boundary <= left_q_range[1]
            and right_q_range[0] <= q_boundary <= right_q_range[1]
        ):
            raise AssertionError("boundary quadratic range lost its endpoint")

        omega_plus = min(left_q_range[1], right_q_range[1]) - q_boundary
        omega_minus = q_boundary - max(left_q_range[0], right_q_range[0])
        if omega_plus < 0 or omega_minus < 0:
            raise AssertionError("common overshoot must be nonnegative")

        delta_plus, lower_endpoint, plus_pair = _nearest_above(
            lower_values, lower_witnesses, q_boundary
        )
        delta_minus, upper_endpoint, minus_pair = _nearest_below(
            upper_values, upper_witnesses, q_boundary
        )
        margin_plus = None if delta_plus is None else delta_plus - omega_plus
        margin_minus = None if delta_minus is None else delta_minus - omega_minus
        plus_pass = delta_plus is None or omega_plus < delta_plus
        minus_pass = delta_minus is None or omega_minus < delta_minus

        if margin_plus is not None:
            finite_margins.append((margin_plus, boundary_index, "upper"))
            if omega_plus > 0:
                finite_headroom_ratios.append(
                    (delta_plus / omega_plus, boundary_index, "upper")
                )
        if margin_minus is not None:
            finite_margins.append((margin_minus, boundary_index, "lower"))
            if omega_minus > 0:
                finite_headroom_ratios.append(
                    (delta_minus / omega_minus, boundary_index, "lower")
                )

        plus_pair_payload = "" if plus_pair is None else f"{plus_pair[0]}:{plus_pair[1]}"
        minus_pair_payload = (
            "" if minus_pair is None else f"{minus_pair[0]}:{minus_pair[1]}"
        )
        row = {
            "panel_id": configuration.panel_id,
            "configuration_id": configuration.configuration_id,
            "fresh_discovery_eligible": configuration.fresh_discovery_eligible,
            "grid": configuration.grid,
            "grid_offset_fraction": fraction_text(configuration.grid_offset),
            "a_fraction": fraction_text(configuration.a),
            "c_fraction": fraction_text(configuration.c),
            "radius_fraction": fraction_text(configuration.radius),
            "eta_fraction": fraction_text(configuration.eta),
            "boundary_index": boundary_index,
            "boundary_fraction": fraction_text(boundary),
            "q_boundary_fraction": fraction_text(q_boundary),
            "left_k": k_values[boundary_index - 1],
            "right_k": k_values[boundary_index],
            "left_boundary_slab_fraction": (
                f"{fraction_text(left_slab[0])}:{fraction_text(left_slab[1])}"
            ),
            "right_boundary_slab_fraction": (
                f"{fraction_text(right_slab[0])}:{fraction_text(right_slab[1])}"
            ),
            "left_q_range_fraction": (
                f"{fraction_text(left_q_range[0])}:{fraction_text(left_q_range[1])}"
            ),
            "right_q_range_fraction": (
                f"{fraction_text(right_q_range[0])}:{fraction_text(right_q_range[1])}"
            ),
            "omega_plus_fraction": fraction_text(omega_plus),
            "delta_plus_fraction": fraction_or_infinity_text(delta_plus),
            "margin_plus_fraction": fraction_or_infinity_text(margin_plus),
            "headroom_plus": (
                "inf"
                if delta_plus is None or omega_plus == 0
                else fraction_text(delta_plus / omega_plus)
            ),
            "plus_witness_jk": plus_pair_payload,
            "plus_pass": plus_pass,
            "omega_minus_fraction": fraction_text(omega_minus),
            "delta_minus_fraction": fraction_or_infinity_text(delta_minus),
            "margin_minus_fraction": fraction_or_infinity_text(margin_minus),
            "headroom_minus": (
                "inf"
                if delta_minus is None or omega_minus == 0
                else fraction_text(delta_minus / omega_minus)
            ),
            "minus_witness_jk": minus_pair_payload,
            "minus_pass": minus_pass,
            "boundary_pass": plus_pass and minus_pass,
        }
        boundary_rows.append(row)

        if not plus_pass:
            if plus_pair is None or lower_endpoint is None:
                raise AssertionError("missing upper-side failure witness")
            j, k = plus_pair
            coefficient_interval = (
                lower_endpoint,
                configuration.c - edges[k] - edges[j],
            )
            failure_witnesses.append(
                _failure_witness(
                    configuration=configuration,
                    edges=edges,
                    boundary_index=boundary_index,
                    side="upper",
                    pair=plus_pair,
                    coefficient_interval=coefficient_interval,
                    q_boundary=q_boundary,
                    left_slab=left_slab,
                    right_slab=right_slab,
                    left_q_range=left_q_range,
                    right_q_range=right_q_range,
                )
            )
        if not minus_pass:
            if minus_pair is None or upper_endpoint is None:
                raise AssertionError("missing lower-side failure witness")
            j, k = minus_pair
            coefficient_interval = (
                configuration.c - edges[k + 1] - edges[j + 1],
                upper_endpoint,
            )
            failure_witnesses.append(
                _failure_witness(
                    configuration=configuration,
                    edges=edges,
                    boundary_index=boundary_index,
                    side="lower",
                    pair=minus_pair,
                    coefficient_interval=coefficient_interval,
                    q_boundary=q_boundary,
                    left_slab=left_slab,
                    right_slab=right_slab,
                    left_q_range=left_q_range,
                    right_q_range=right_q_range,
                )
            )

    worst_margin = min(finite_margins) if finite_margins else None
    minimum_headroom = (
        min(finite_headroom_ratios) if finite_headroom_ratios else None
    )
    failure_boundary_count = sum(not row["boundary_pass"] for row in boundary_rows)
    upper_failure_count = sum(not row["plus_pass"] for row in boundary_rows)
    lower_failure_count = sum(not row["minus_pass"] for row in boundary_rows)
    certificate_pass = failure_boundary_count == 0
    all_witnesses_pass = all(
        bool(witness["exact_false_mutual_witness_pass"])
        for witness in failure_witnesses
    )

    summary = {
        **{
            key: (
                fraction_text(value)
                if isinstance(value, Fraction)
                else value
            )
            for key, value in asdict(configuration).items()
        },
        "cell_count": configuration.grid**2,
        "internal_boundary_count": configuration.grid - 1,
        "edge_vector_strict_pass": edges_strict,
        "minimum_cell_width_fraction": fraction_text(minimum_width),
        "uncapped_k_min": min(uncapped_k_values),
        "uncapped_k_max": max(uncapped_k_values),
        "cap_active_count": cap_active_count,
        "k_gate_pass": cap_active_count == 0,
        "distinct_coefficient_lower_endpoint_count": len(lower_values),
        "distinct_coefficient_upper_endpoint_count": len(upper_values),
        "certificate_pass": certificate_pass,
        "failure_boundary_count": failure_boundary_count,
        "upper_failure_count": upper_failure_count,
        "lower_failure_count": lower_failure_count,
        "failure_witness_count": len(failure_witnesses),
        "all_failure_witnesses_replay_pass": all_witnesses_pass,
        "first_failure_witness": failure_witnesses[0] if failure_witnesses else None,
        "failure_witnesses": failure_witnesses,
        "minimum_signed_margin_fraction": (
            None if worst_margin is None else fraction_text(worst_margin[0])
        ),
        "minimum_signed_margin": (
            None if worst_margin is None else float(worst_margin[0])
        ),
        "minimum_margin_boundary_index": (
            None if worst_margin is None else worst_margin[1]
        ),
        "minimum_margin_side": None if worst_margin is None else worst_margin[2],
        "minimum_headroom_ratio_fraction": (
            None if minimum_headroom is None else fraction_text(minimum_headroom[0])
        ),
        "minimum_headroom_ratio": (
            None if minimum_headroom is None else float(minimum_headroom[0])
        ),
        "minimum_headroom_boundary_index": (
            None if minimum_headroom is None else minimum_headroom[1]
        ),
        "minimum_headroom_side": (
            None if minimum_headroom is None else minimum_headroom[2]
        ),
        "fresh_counterexample": (
            configuration.fresh_discovery_eligible and not certificate_pass
        ),
        "boundary_record_sha256": _boundary_hash(boundary_rows),
    }
    return summary, boundary_rows


def _find_record(
    records: Sequence[dict[str, object]],
    *,
    panel_id: str,
    grid: int | None = None,
    configuration_id: str | None = None,
) -> dict[str, object]:
    matches = [
        record
        for record in records
        if record["panel_id"] == panel_id
        and (grid is None or int(record["grid"]) == grid)
        and (
            configuration_id is None
            or record["configuration_id"] == configuration_id
        )
    ]
    if len(matches) != 1:
        raise AssertionError(
            f"expected one R057 record, found {len(matches)} for "
            f"panel={panel_id}, grid={grid}, id={configuration_id}"
        )
    return matches[0]


def _n60_witness_pass(record: dict[str, object]) -> bool:
    for witness in record["failure_witnesses"]:
        if (
            witness["boundary_index"] == 30
            and witness["failure_side"] == "upper"
            and witness["source_id"] == 2789
            and witness["target_id"] == 1859
            and witness["exact_false_mutual_witness_pass"]
        ):
            return True
    return False


def build_decisions(
    records: Sequence[dict[str, object]], payload: dict[str, object]
) -> dict[str, object]:
    centered = {
        int(record["grid"]): record
        for record in records
        if record["panel_id"] == "centered_resolution_scan"
    }
    known_failures = set(
        int(value)
        for value in payload["development_observations_seen_before_freeze"][
            "centered_fail_grids"
        ]
    )
    prior_centered_passes = set(
        int(value)
        for value in payload["development_observations_seen_before_freeze"][
            "prior_pass_anchors"
        ]
    )
    n60 = centered[60]
    neighbor_pass = centered[58]["certificate_pass"] and centered[62][
        "certificate_pass"
    ]
    known_failure_replay = all(
        not bool(centered[grid]["certificate_pass"]) for grid in known_failures
    )
    centered_anchor_pass = all(
        bool(centered[grid]["certificate_pass"]) for grid in prior_centered_passes
    )
    shifted_anchor_records = [
        record
        for record in records
        if record["panel_id"] == "shifted_prior_pass_controls"
    ]
    shifted_anchor_pass = all(
        bool(record["certificate_pass"]) for record in shifted_anchor_records
    )
    fresh_counterexamples = [
        record for record in records if record["fresh_counterexample"]
    ]
    panel_ids = sorted({str(record["panel_id"]) for record in records})
    panel_summary = {}
    for panel_id in panel_ids:
        panel_records = [record for record in records if record["panel_id"] == panel_id]
        fail_count = sum(not bool(record["certificate_pass"]) for record in panel_records)
        panel_summary[panel_id] = {
            "configuration_count": len(panel_records),
            "pass_count": len(panel_records) - fail_count,
            "fail_count": fail_count,
            "failure_rate": fail_count / len(panel_records),
            "fresh_counterexample_count": sum(
                bool(record["fresh_counterexample"]) for record in panel_records
            ),
        }

    exact_witness_integrity = all(
        bool(record["edge_vector_strict_pass"])
        and bool(record["all_failure_witnesses_replay_pass"])
        for record in records
    )
    strict_g1_integrity = exact_witness_integrity and all(
        bool(record["k_gate_pass"]) for record in records
    )
    cap_active_records = [
        record for record in records if not bool(record["k_gate_pass"])
    ]
    cap_free_records = [
        record for record in records if bool(record["k_gate_pass"])
    ]
    cap_free_integrity = all(
        bool(record["edge_vector_strict_pass"])
        and bool(record["all_failure_witnesses_replay_pass"])
        for record in cap_free_records
    )
    return {
        "protocol_sha256_pass": _sha256(PROTOCOL) == PROTOCOL_SHA256,
        "configuration_count": len(records),
        "expected_configuration_count": 517,
        "panel_expansion_pass": len(records) == 517,
        "g0_protocol_and_exact_arithmetic_pass": exact_witness_integrity,
        "g1_certificate_and_witness_integrity_pass": strict_g1_integrity,
        "g1_cap_free_subset_pass": cap_free_integrity,
        "g1_cap_active_configuration_count": len(cap_active_records),
        "g1_cap_active_configuration_ids": [
            str(record["configuration_id"]) for record in cap_active_records
        ],
        "g1_cap_free_configuration_count": len(cap_free_records),
        "g2_n60_constructive_counterexample_pass": (
            not bool(n60["certificate_pass"]) and _n60_witness_pass(n60)
        ),
        "g2_neighbor_controls_pass": bool(neighbor_pass),
        "g2_known_failure_replay_pass": known_failure_replay,
        "g2_centered_prior_pass_certificate_pass": centered_anchor_pass,
        "g2_shifted_prior_pass_certificate_pass": shifted_anchor_pass,
        "g2_all_theory_controls_pass": (
            not bool(n60["certificate_pass"])
            and _n60_witness_pass(n60)
            and bool(neighbor_pass)
            and known_failure_replay
            and centered_anchor_pass
            and shifted_anchor_pass
        ),
        "fresh_counterexample_count": len(fresh_counterexamples),
        "fresh_counterexample_configuration_ids": [
            str(record["configuration_id"]) for record in fresh_counterexamples
        ],
        "total_pass_count": sum(bool(record["certificate_pass"]) for record in records),
        "total_fail_count": sum(not bool(record["certificate_pass"]) for record in records),
        "panel_summary": panel_summary,
        "production_complete": True,
        "strict_all_frozen_integrity_gates_pass": strict_g1_integrity,
        "cap_free_panel_interpretation_enabled": cap_free_integrity,
        "theorem_and_counterexample_interpretation_enabled": (
            exact_witness_integrity
            and not bool(n60["certificate_pass"])
            and _n60_witness_pass(n60)
            and known_failure_replay
            and centered_anchor_pass
            and shifted_anchor_pass
        ),
        "interpretation_enabled": strict_g1_integrity,
        "no_all_pass_gate_applied": True,
    }


BOUNDARY_FIELDS = [
    "panel_id",
    "configuration_id",
    "fresh_discovery_eligible",
    "grid",
    "grid_offset_fraction",
    "a_fraction",
    "c_fraction",
    "radius_fraction",
    "eta_fraction",
    "boundary_index",
    "boundary_fraction",
    "q_boundary_fraction",
    "left_k",
    "right_k",
    "left_boundary_slab_fraction",
    "right_boundary_slab_fraction",
    "left_q_range_fraction",
    "right_q_range_fraction",
    "omega_plus_fraction",
    "delta_plus_fraction",
    "margin_plus_fraction",
    "headroom_plus",
    "plus_witness_jk",
    "plus_pass",
    "omega_minus_fraction",
    "delta_minus_fraction",
    "margin_minus_fraction",
    "headroom_minus",
    "minus_witness_jk",
    "minus_pass",
    "boundary_pass",
]


def _global_boundary_hash(records: Sequence[dict[str, object]]) -> str:
    digest = hashlib.sha256()
    for record in records:
        digest.update(
            (
                f"{record['configuration_id']}|"
                f"{record['boundary_record_sha256']}\n"
            ).encode("ascii")
        )
    return digest.hexdigest()


def main() -> None:
    args = parse_args()
    if args.workers <= 0:
        raise SystemExit("--workers must be positive")
    payload = load_and_validate_protocol()
    configurations = expand_configurations(payload)

    if args.workers == 1:
        outputs = [summarize_configuration(item) for item in configurations]
    else:
        with ProcessPoolExecutor(max_workers=args.workers) as executor:
            outputs = list(executor.map(summarize_configuration, configurations))

    records = [summary for summary, _ in outputs]
    boundary_rows = [row for _, rows in outputs for row in rows]
    decisions = build_decisions(records, payload)
    result = {
        "run_id": "R057_MUTUAL_SEPARATION",
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_path": str(PROTOCOL.relative_to(PROJECT_ROOT)),
        "protocol_sha256": PROTOCOL_SHA256,
        "python_version": platform.python_version(),
        "workers": args.workers,
        "arithmetic": "fractions.Fraction for all decisions; floats display-only",
        "boundary_row_count": len(boundary_rows),
        "boundary_records_sha256": _global_boundary_hash(records),
        "decisions": decisions,
        "records": records,
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / f"{args.output_stem}.json"
    csv_name = (
        "mutual_separation_boundaries_r057.csv"
        if args.output_stem == "mutual_separation_r057"
        else f"{args.output_stem}_boundaries.csv"
    )
    csv_path = args.output_dir / csv_name
    json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=BOUNDARY_FIELDS)
        writer.writeheader()
        writer.writerows(boundary_rows)

    print(
        json.dumps(
            {
                "json": str(json_path),
                "boundary_csv": str(csv_path),
                "configuration_count": len(records),
                "boundary_row_count": len(boundary_rows),
                "total_pass_count": decisions["total_pass_count"],
                "total_fail_count": decisions["total_fail_count"],
                "fresh_counterexample_count": decisions[
                    "fresh_counterexample_count"
                ],
                "all_theory_controls_pass": decisions[
                    "g2_all_theory_controls_pass"
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
