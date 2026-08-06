#!/usr/bin/env python3
"""Independent checker for the frozen R057 mutual-separation audit.

The checker deliberately imports no R053--R057 producer geometry,
certificate, incidence, target-indexing, or witness helper.  Every decision is
reconstructed with :class:`fractions.Fraction` from the frozen protocol.

G3 coverage:

* exhaustive complete-graph true/mutual/positive comparisons on four frozen
  microgrids;
* an independent boundary-certificate calculation and certificate-iff-graph
  equality check on each microgrid;
* exact replay of the frozen N=60 false-mutual witness;
* persisted JSON/CSV schema, canonical boundary hashes, strict-margin logic,
  and every reported failure witness.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R057_MUTUAL_SEPARATION_PROTOCOL.json"
)
RESULT_PATH = PROJECT_ROOT / "results" / "mutual_separation_r057.json"
BOUNDARY_CSV_PATH = (
    PROJECT_ROOT / "results" / "mutual_separation_boundaries_r057.csv"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "results"
    / "mutual_separation_independent_check_r057.json"
)
PROTOCOL_SHA256 = "4eb540372ad29568054cdaa05b7c3f605913dfcf358855c98f45594c78af0a91"

BOUNDARY_FIELDS = (
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
)
BOUNDARY_HASH_FIELDS = (
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


def portable_path(path: Path) -> str:
    """Return a repository-relative path when the artifact lives in-tree."""

    resolved = path.resolve()
    try:
        return str(resolved.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(resolved)


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
    maximum_subdivisions: int
    fresh_discovery_eligible: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, default=PROTOCOL_PATH)
    parser.add_argument("--input", type=Path, default=RESULT_PATH)
    parser.add_argument("--boundary-csv", type=Path, default=BOUNDARY_CSV_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    return parser.parse_args()


def fraction_text(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def parse_fraction(value: object) -> Fraction:
    return Fraction(str(value))


def parse_fraction_or_infinity(value: object) -> Fraction | None:
    return None if str(value) == "inf" else parse_fraction(value)


def parse_bool(value: object) -> bool:
    if value is True or str(value) == "True":
        return True
    if value is False or str(value) == "False":
        return False
    raise AssertionError(f"invalid persisted boolean: {value!r}")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def edge_hash(edges: Iterable[tuple[int, int]]) -> str:
    digest = hashlib.sha256()
    for source, target in sorted(edges):
        digest.update(f"{source},{target}\n".encode("ascii"))
    return digest.hexdigest()


def slug(value: Fraction) -> str:
    sign = "m" if value < 0 else "p" if value > 0 else "z"
    magnitude = abs(value)
    return f"{sign}{magnitude.numerator}_{magnitude.denominator}"


def load_protocol(path: Path = PROTOCOL_PATH) -> dict[str, object]:
    if sha256_file(path) != PROTOCOL_SHA256:
        raise AssertionError("R057 frozen protocol SHA-256 mismatch")
    payload = json.loads(path.read_text(encoding="utf-8"))
    defaults = payload.get("default_constants")
    g3 = payload.get("frozen_gates", {}).get("g3_independent_checker")  # type: ignore[union-attr]
    if payload.get("run_id") != "R057_MUTUAL_SEPARATION":
        raise AssertionError("unexpected R057 protocol run_id")
    if payload.get("status") != "FROZEN_BEFORE_PRODUCTION":
        raise AssertionError("R057 protocol is not frozen before production")
    if not isinstance(defaults, Mapping) or not isinstance(g3, Mapping):
        raise AssertionError("R057 default constants or G3 block missing")
    if g3.get("may_import_producer_certificate_or_incidence_helpers") is not False:
        raise AssertionError("R057 independent-import policy changed")
    expected_microgrids = [
        (5, Fraction(0), Fraction(1, 4)),
        (6, Fraction(0), Fraction(1, 2)),
        (7, Fraction(1, 3), Fraction(1, 4)),
        (8, Fraction(-1, 3), Fraction(1, 8)),
    ]
    observed = [
        (
            int(item["grid"]),
            parse_fraction(item["grid_offset"]),
            parse_fraction(item["eta"]),
        )
        for item in g3.get("full_graph_microgrids", [])
    ]
    if observed != expected_microgrids:
        raise AssertionError("R057 frozen microgrid panel changed")
    return payload


def expand_configurations(protocol: Mapping[str, object]) -> list[Configuration]:
    defaults = protocol["default_constants"]  # type: ignore[index]
    maximum = int(defaults["maximum_subdivisions"])
    output: list[Configuration] = []

    for item in protocol["shifted_prior_pass_controls"]:  # type: ignore[index]
        output.append(
            Configuration(
                panel_id="shifted_prior_pass_controls",
                configuration_id=str(item["configuration_id"]),
                role="development_prior_pass_control",
                grid=int(item["grid"]),
                grid_offset=parse_fraction(item["grid_offset"]),
                a=parse_fraction(item["a"]),
                c=parse_fraction(item["c"]),
                radius=parse_fraction(item["radius"]),
                eta=parse_fraction(item["eta"]),
                maximum_subdivisions=maximum,
                fresh_discovery_eligible=False,
            )
        )

    for panel in protocol["production_panels"]:  # type: ignore[index]
        panel_id = str(panel["panel_id"])
        role = str(panel["role"])
        radius = parse_fraction(panel["radius"])
        c_value = parse_fraction(panel["c"])
        offsets = [parse_fraction(value) for value in panel["grid_offsets"]]
        if panel_id == "centered_resolution_scan":
            excluded = {int(value) for value in panel["fresh_discovery_exclusions"]}
            for grid in range(
                int(panel["grid_min"]),
                int(panel["grid_max"]) + 1,
                int(panel["grid_step"]),
            ):
                for offset in offsets:
                    output.append(
                        Configuration(
                            panel_id=panel_id,
                            configuration_id=f"centered_n{grid}_d{slug(offset)}",
                            role=role,
                            grid=grid,
                            grid_offset=offset,
                            a=parse_fraction(panel["a"]),
                            c=c_value,
                            radius=radius,
                            eta=parse_fraction(panel["eta"]),
                            maximum_subdivisions=maximum,
                            fresh_discovery_eligible=grid not in excluded,
                        )
                    )
        elif panel_id == "rational_phase_stress":
            for grid in map(int, panel["grids"]):
                for offset in offsets:
                    output.append(
                        Configuration(
                            panel_id=panel_id,
                            configuration_id=f"phase_n{grid}_d{slug(offset)}",
                            role=role,
                            grid=grid,
                            grid_offset=offset,
                            a=parse_fraction(panel["a"]),
                            c=c_value,
                            radius=radius,
                            eta=parse_fraction(panel["eta"]),
                            maximum_subdivisions=maximum,
                            fresh_discovery_eligible=True,
                        )
                    )
        elif panel_id == "eta_stress":
            for grid in map(int, panel["grids"]):
                for offset in offsets:
                    for eta in map(parse_fraction, panel["etas"]):
                        output.append(
                            Configuration(
                                panel_id=panel_id,
                                configuration_id=(
                                    f"eta_n{grid}_d{slug(offset)}_e{slug(eta)}"
                                ),
                                role=role,
                                grid=grid,
                                grid_offset=offset,
                                a=parse_fraction(panel["a"]),
                                c=c_value,
                                radius=radius,
                                eta=eta,
                                maximum_subdivisions=maximum,
                                fresh_discovery_eligible=True,
                            )
                        )
        elif panel_id == "a_stress":
            for grid in map(int, panel["grids"]):
                for offset in offsets:
                    for a_value in map(parse_fraction, panel["a_values"]):
                        output.append(
                            Configuration(
                                panel_id=panel_id,
                                configuration_id=(
                                    f"a_n{grid}_d{slug(offset)}_a{slug(a_value)}"
                                ),
                                role=role,
                                grid=grid,
                                grid_offset=offset,
                                a=a_value,
                                c=c_value,
                                radius=radius,
                                eta=parse_fraction(panel["eta"]),
                                maximum_subdivisions=maximum,
                                fresh_discovery_eligible=True,
                            )
                        )
        else:
            raise AssertionError(f"unknown R057 panel {panel_id}")

    counts = {
        panel_id: sum(item.panel_id == panel_id for item in output)
        for panel_id in {
            "shifted_prior_pass_controls",
            "centered_resolution_scan",
            "rational_phase_stress",
            "eta_stress",
            "a_stress",
        }
    }
    expected = {
        "shifted_prior_pass_controls": 4,
        "centered_resolution_scan": 352,
        "rational_phase_stress": 48,
        "eta_stress": 64,
        "a_stress": 49,
    }
    if counts != expected or len(output) != 517:
        raise AssertionError(f"independent panel expansion mismatch: {counts}")
    if len({item.configuration_id for item in output}) != len(output):
        raise AssertionError("independent R057 configuration IDs are not unique")
    return output


def make_edges(
    radius: Fraction, grid: int, offset: Fraction
) -> tuple[Fraction, ...]:
    if grid <= 0 or not Fraction(-1, 2) <= offset <= Fraction(1, 2):
        raise ValueError("invalid grid or offset")
    width = 2 * radius / grid
    edges = [-radius]
    edges.extend(
        -radius + (Fraction(index) + offset) * width
        for index in range(1, grid)
    )
    edges.append(radius)
    if any(right <= left for left, right in zip(edges, edges[1:])):
        raise AssertionError("independent edge vector is not strictly increasing")
    return tuple(edges)


def quadratic_range(
    lower: Fraction, upper: Fraction, a_value: Fraction
) -> tuple[Fraction, Fraction]:
    if a_value <= 0 or upper < lower:
        raise ValueError("R057 requires a>0 and ordered endpoints")
    minimum_square = (
        Fraction(0)
        if lower <= 0 <= upper
        else min(lower * lower, upper * upper)
    )
    maximum_square = max(lower * lower, upper * upper)
    return a_value * minimum_square, a_value * maximum_square


def exact_ceiling(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def adaptive_count(
    lower: Fraction,
    upper: Fraction,
    minimum_width: Fraction,
    a_value: Fraction,
    eta: Fraction,
) -> int:
    maximum_abs = max(abs(lower), abs(upper))
    numerator = 2 * a_value * maximum_abs * (upper - lower)
    if numerator == 0:
        return 1
    return max(1, exact_ceiling(numerator / (eta * minimum_width)))


def grid_geometry(
    configuration: Configuration,
) -> tuple[tuple[Fraction, ...], tuple[int, ...], tuple[int, ...]]:
    edges = make_edges(
        configuration.radius, configuration.grid, configuration.grid_offset
    )
    widths = [right - left for left, right in zip(edges, edges[1:])]
    minimum_width = min(widths)
    uncapped = tuple(
        adaptive_count(
            edges[index],
            edges[index + 1],
            minimum_width,
            configuration.a,
            configuration.eta,
        )
        for index in range(configuration.grid)
    )
    capped = tuple(min(configuration.maximum_subdivisions, value) for value in uncapped)
    return edges, uncapped, capped


def interval_intersection(
    first: tuple[Fraction, Fraction], second: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction] | None:
    lower = max(first[0], second[0])
    upper = min(first[1], second[1])
    return None if upper < lower else (lower, upper)


def positive_interval_overlap(
    first: tuple[Fraction, Fraction], second: tuple[Fraction, Fraction]
) -> bool:
    return min(first[1], second[1]) > max(first[0], second[0])


def coefficient_interval(
    edges: Sequence[Fraction], j: int, k: int, c_value: Fraction
) -> tuple[Fraction, Fraction]:
    return (
        c_value - edges[k + 1] - edges[j + 1],
        c_value - edges[k] - edges[j],
    )


def cell_slabs(
    edges: Sequence[Fraction],
    cell_index: int,
    subdivisions: int,
    a_value: Fraction,
) -> tuple[
    tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]], ...
]:
    lower, upper = edges[cell_index], edges[cell_index + 1]
    width = (upper - lower) / subdivisions
    output = []
    for slab_index in range(subdivisions):
        slab = (
            lower + slab_index * width,
            lower + (slab_index + 1) * width,
        )
        output.append((slab, quadratic_range(*slab, a_value)))
    return tuple(output)


def true_class(
    edges: Sequence[Fraction],
    i: int,
    j: int,
    k: int,
    ell: int,
    a_value: Fraction,
    c_value: Fraction,
) -> bool | None:
    parameter = interval_intersection(
        (edges[i], edges[i + 1]), (edges[ell], edges[ell + 1])
    )
    if parameter is None:
        return None
    q_interval = quadratic_range(*parameter, a_value)
    coefficient = coefficient_interval(edges, j, k, c_value)
    if interval_intersection(q_interval, coefficient) is None:
        return None
    return positive_interval_overlap(parameter, parameter) and positive_interval_overlap(
        q_interval, coefficient
    )


def outer_direction_class(
    slabs: Sequence[
        tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
    ],
    other_cell: tuple[Fraction, Fraction],
    coefficient: tuple[Fraction, Fraction],
) -> bool | None:
    touch = False
    for slab, q_interval in slabs:
        parameter_intersection = interval_intersection(slab, other_cell)
        q_intersection = interval_intersection(q_interval, coefficient)
        if parameter_intersection is None or q_intersection is None:
            continue
        if positive_interval_overlap(slab, other_cell) and positive_interval_overlap(
            q_interval, coefficient
        ):
            return True
        touch = True
    return False if touch else None


def enumerate_complete_graphs(configuration: Configuration) -> dict[str, set[tuple[int, int]]]:
    edges, _, k_values = grid_geometry(configuration)
    grid = configuration.grid
    cells = tuple(zip(edges, edges[1:]))
    slabs = tuple(
        cell_slabs(edges, index, k_values[index], configuration.a)
        for index in range(grid)
    )
    graphs = {
        "true_closed": set(),
        "mutual_outer": set(),
        "true_positive": set(),
        "outer_forward_positive": set(),
        "outer_reverse_positive": set(),
    }
    for j in range(grid):
        for i in range(grid):
            source_id = j * grid + i
            for ell in range(grid):
                if interval_intersection(cells[i], cells[ell]) is None:
                    continue
                for k in range(grid):
                    target_id = ell * grid + k
                    coefficient = coefficient_interval(edges, j, k, configuration.c)
                    true = true_class(
                        edges, i, j, k, ell, configuration.a, configuration.c
                    )
                    forward = outer_direction_class(slabs[i], cells[ell], coefficient)
                    reverse = outer_direction_class(slabs[ell], cells[i], coefficient)
                    edge = (source_id, target_id)
                    if true is not None:
                        graphs["true_closed"].add(edge)
                    if forward is not None and reverse is not None:
                        graphs["mutual_outer"].add(edge)
                    if true is True:
                        graphs["true_positive"].add(edge)
                    if forward is True:
                        graphs["outer_forward_positive"].add(edge)
                    if reverse is True:
                        graphs["outer_reverse_positive"].add(edge)
    return graphs


def endpoint_tables(
    edges: Sequence[Fraction], c_value: Fraction
) -> tuple[
    list[Fraction],
    dict[Fraction, tuple[int, int]],
    list[Fraction],
    dict[Fraction, tuple[int, int]],
]:
    grid = len(edges) - 1
    lower_witnesses: dict[Fraction, tuple[int, int]] = {}
    upper_witnesses: dict[Fraction, tuple[int, int]] = {}
    for j in range(grid):
        for k in range(grid):
            lower, upper = coefficient_interval(edges, j, k, c_value)
            pair = (j, k)
            if pair < lower_witnesses.get(lower, pair):
                lower_witnesses[lower] = pair
            else:
                lower_witnesses.setdefault(lower, pair)
            if pair < upper_witnesses.get(upper, pair):
                upper_witnesses[upper] = pair
            else:
                upper_witnesses.setdefault(upper, pair)
    return (
        sorted(lower_witnesses),
        lower_witnesses,
        sorted(upper_witnesses),
        upper_witnesses,
    )


def nearest_above(
    values: Sequence[Fraction],
    witnesses: Mapping[Fraction, tuple[int, int]],
    point: Fraction,
) -> tuple[Fraction | None, tuple[int, int] | None]:
    index = bisect.bisect_right(values, point)
    if index == len(values):
        return None, None
    endpoint = values[index]
    return endpoint - point, witnesses[endpoint]


def nearest_below(
    values: Sequence[Fraction],
    witnesses: Mapping[Fraction, tuple[int, int]],
    point: Fraction,
) -> tuple[Fraction | None, tuple[int, int] | None]:
    index = bisect.bisect_left(values, point) - 1
    if index < 0:
        return None, None
    endpoint = values[index]
    return point - endpoint, witnesses[endpoint]


def certificate_rows(configuration: Configuration) -> list[dict[str, object]]:
    edges, uncapped, k_values = grid_geometry(configuration)
    lower_values, lower_witnesses, upper_values, upper_witnesses = endpoint_tables(
        edges, configuration.c
    )
    rows = []
    for boundary_index in range(1, configuration.grid):
        boundary = edges[boundary_index]
        left_width = (boundary - edges[boundary_index - 1]) / k_values[
            boundary_index - 1
        ]
        right_width = (edges[boundary_index + 1] - boundary) / k_values[
            boundary_index
        ]
        left_slab = (boundary - left_width, boundary)
        right_slab = (boundary, boundary + right_width)
        left_q = quadratic_range(*left_slab, configuration.a)
        right_q = quadratic_range(*right_slab, configuration.a)
        q_boundary = configuration.a * boundary**2
        omega_plus = min(left_q[1], right_q[1]) - q_boundary
        omega_minus = q_boundary - max(left_q[0], right_q[0])
        delta_plus, plus_pair = nearest_above(
            lower_values, lower_witnesses, q_boundary
        )
        delta_minus, minus_pair = nearest_below(
            upper_values, upper_witnesses, q_boundary
        )
        rows.append(
            {
                "boundary_index": boundary_index,
                "boundary": boundary,
                "q_boundary": q_boundary,
                "left_slab": left_slab,
                "right_slab": right_slab,
                "left_q": left_q,
                "right_q": right_q,
                "left_k": k_values[boundary_index - 1],
                "right_k": k_values[boundary_index],
                "omega_plus": omega_plus,
                "delta_plus": delta_plus,
                "margin_plus": (
                    None if delta_plus is None else delta_plus - omega_plus
                ),
                "plus_pair": plus_pair,
                "plus_pass": delta_plus is None or omega_plus < delta_plus,
                "omega_minus": omega_minus,
                "delta_minus": delta_minus,
                "margin_minus": (
                    None if delta_minus is None else delta_minus - omega_minus
                ),
                "minus_pair": minus_pair,
                "minus_pass": delta_minus is None or omega_minus < delta_minus,
                "uncapped_k_max": max(uncapped),
            }
        )
    return rows


def microgrid_configuration(
    item: Mapping[str, object], protocol: Mapping[str, object]
) -> Configuration:
    defaults = protocol["default_constants"]  # type: ignore[index]
    return Configuration(
        panel_id="g3_microgrid",
        configuration_id=(
            f"micro_n{int(item['grid'])}_d{slug(parse_fraction(item['grid_offset']))}"
            f"_e{slug(parse_fraction(item['eta']))}"
        ),
        role="independent_full_graph",
        grid=int(item["grid"]),
        grid_offset=parse_fraction(item["grid_offset"]),
        a=parse_fraction(defaults["a"]),
        c=parse_fraction(defaults["c"]),
        radius=parse_fraction(defaults["radius"]),
        eta=parse_fraction(item["eta"]),
        maximum_subdivisions=int(defaults["maximum_subdivisions"]),
        fresh_discovery_eligible=False,
    )


def run_microgrid_checks(protocol: Mapping[str, object]) -> list[dict[str, object]]:
    g3 = protocol["frozen_gates"]["g3_independent_checker"]  # type: ignore[index]
    output = []
    for item in g3["full_graph_microgrids"]:
        configuration = microgrid_configuration(item, protocol)
        edges, uncapped, capped = grid_geometry(configuration)
        graphs = enumerate_complete_graphs(configuration)
        rows = certificate_rows(configuration)
        certificate_pass = all(
            bool(row["plus_pass"]) and bool(row["minus_pass"]) for row in rows
        )
        closed_equal = graphs["true_closed"] == graphs["mutual_outer"]
        true_subset = graphs["true_closed"] <= graphs["mutual_outer"]
        forward_positive_equal = (
            graphs["true_positive"] == graphs["outer_forward_positive"]
        )
        reverse_positive_equal = (
            graphs["true_positive"] == graphs["outer_reverse_positive"]
        )
        output.append(
            {
                "configuration_id": configuration.configuration_id,
                "grid": configuration.grid,
                "grid_offset_fraction": fraction_text(configuration.grid_offset),
                "eta_fraction": fraction_text(configuration.eta),
                "source_target_pair_count": configuration.grid**4,
                "uncapped_k_max": max(uncapped),
                "capped_k_max": max(capped),
                "cap_active_count": sum(
                    value >= configuration.maximum_subdivisions for value in uncapped
                ),
                "edge_counts": {
                    key: len(value) for key, value in graphs.items()
                },
                "edge_hashes": {
                    key: edge_hash(value) for key, value in graphs.items()
                },
                "true_closed_subset_mutual_outer_pass": true_subset,
                "true_closed_equals_mutual_outer_pass": closed_equal,
                "certificate_pass": certificate_pass,
                "certificate_iff_complete_graph_equality_pass": (
                    certificate_pass == closed_equal
                ),
                "outer_forward_positive_equals_true_positive_pass": (
                    forward_positive_equal
                ),
                "outer_reverse_positive_equals_true_positive_pass": (
                    reverse_positive_equal
                ),
                "pass": all(
                    (
                        true_subset,
                        certificate_pass == closed_equal,
                        forward_positive_equal,
                        reverse_positive_equal,
                        edges[0] == -configuration.radius,
                        edges[-1] == configuration.radius,
                    )
                ),
            }
        )
    return output


def replay_witness(
    configuration: Configuration,
    *,
    i: int,
    j: int,
    k: int,
    ell: int,
) -> dict[str, object]:
    edges, _, k_values = grid_geometry(configuration)
    coefficient = coefficient_interval(edges, j, k, configuration.c)
    left_to_right = i + 1 == ell
    right_to_left = ell + 1 == i
    if not (left_to_right or right_to_left):
        raise AssertionError("R057 failure witness must use adjacent cells")
    boundary_index = max(i, ell)
    boundary = edges[boundary_index]
    left_index, right_index = boundary_index - 1, boundary_index
    left_width = (edges[left_index + 1] - edges[left_index]) / k_values[left_index]
    right_width = (edges[right_index + 1] - edges[right_index]) / k_values[right_index]
    left_slab = (boundary - left_width, boundary)
    right_slab = (boundary, boundary + right_width)
    left_q = quadratic_range(*left_slab, configuration.a)
    right_q = quadratic_range(*right_slab, configuration.a)
    q_boundary = configuration.a * boundary**2
    true = true_class(
        edges, i, j, k, ell, configuration.a, configuration.c
    )
    source_slabs = cell_slabs(edges, i, k_values[i], configuration.a)
    target_y_slabs = cell_slabs(edges, ell, k_values[ell], configuration.a)
    forward = outer_direction_class(
        source_slabs, (edges[ell], edges[ell + 1]), coefficient
    )
    reverse = outer_direction_class(
        target_y_slabs, (edges[i], edges[i + 1]), coefficient
    )
    return {
        "failure_side": (
            "upper"
            if coefficient[0] > q_boundary
            else "lower"
            if coefficient[1] < q_boundary
            else "contains_boundary"
        ),
        "boundary_index": boundary_index,
        "shared_boundary_fraction": fraction_text(boundary),
        "q_boundary_fraction": fraction_text(q_boundary),
        "source_indices": {"x": i, "y": j},
        "target_indices": {"x": k, "y": ell},
        "source_id": j * configuration.grid + i,
        "target_id": ell * configuration.grid + k,
        "coefficient_indices": {"j": j, "k": k},
        "coefficient_interval_fraction": list(map(fraction_text, coefficient)),
        "source_x_interval_fraction": list(
            map(fraction_text, (edges[i], edges[i + 1]))
        ),
        "source_y_interval_fraction": list(
            map(fraction_text, (edges[j], edges[j + 1]))
        ),
        "target_x_interval_fraction": list(
            map(fraction_text, (edges[k], edges[k + 1]))
        ),
        "target_y_interval_fraction": list(
            map(fraction_text, (edges[ell], edges[ell + 1]))
        ),
        "left_boundary_slab_fraction": list(map(fraction_text, left_slab)),
        "right_boundary_slab_fraction": list(map(fraction_text, right_slab)),
        "left_q_range_fraction": list(map(fraction_text, left_q)),
        "right_q_range_fraction": list(map(fraction_text, right_q)),
        "true_closed_present": true is not None,
        "forward_outer_present": forward is not None,
        "inverse_reverse_outer_present": reverse is not None,
        "mutual_outer_present": forward is not None and reverse is not None,
        "forward_outer_positive": forward is True,
        "inverse_reverse_outer_positive": reverse is True,
        "exact_false_mutual_witness_pass": (
            true is None and forward is not None and reverse is not None
        ),
    }


def n60_configuration(protocol: Mapping[str, object]) -> Configuration:
    defaults = protocol["default_constants"]  # type: ignore[index]
    return Configuration(
        panel_id="centered_resolution_scan",
        configuration_id="centered_n60_dz0_1",
        role="development theorem counterexample",
        grid=60,
        grid_offset=Fraction(0),
        a=parse_fraction(defaults["a"]),
        c=parse_fraction(defaults["c"]),
        radius=parse_fraction(defaults["radius"]),
        eta=parse_fraction(defaults["eta"]),
        maximum_subdivisions=int(defaults["maximum_subdivisions"]),
        fresh_discovery_eligible=False,
    )


def run_n60_check(protocol: Mapping[str, object]) -> dict[str, object]:
    frozen = protocol["development_observations_seen_before_freeze"][  # type: ignore[index]
        "constructive_witness"
    ]
    configuration = n60_configuration(protocol)
    source_x, source_y = map(int, frozen["source_indices"])
    target_x, target_y = map(int, frozen["target_indices"])
    replay = replay_witness(
        configuration,
        i=source_x,
        j=source_y,
        k=target_x,
        ell=target_y,
    )
    rows = certificate_rows(configuration)
    boundary = rows[int(frozen["boundary_index"]) - 1]
    pass_checks = {
        "source_id": replay["source_id"] == int(frozen["source_id"]),
        "target_id": replay["target_id"] == int(frozen["target_id"]),
        "boundary_index": replay["boundary_index"]
        == int(frozen["boundary_index"]),
        "boundary": replay["shared_boundary_fraction"] == str(frozen["boundary"]),
        "failure_side": replay["failure_side"] == frozen["failure_side"],
        "false_mutual": replay["exact_false_mutual_witness_pass"] is True,
        "certificate_side_failure": boundary["plus_pass"] is False,
        "certificate_global_failure": not all(
            bool(row["plus_pass"]) and bool(row["minus_pass"]) for row in rows
        ),
    }
    return {
        "configuration_id": configuration.configuration_id,
        "recomputed_witness": replay,
        "checks": pass_checks,
        "pass": all(pass_checks.values()),
    }


def configuration_from_record(record: Mapping[str, object], maximum: int) -> Configuration:
    return Configuration(
        panel_id=str(record["panel_id"]),
        configuration_id=str(record["configuration_id"]),
        role=str(record["role"]),
        grid=int(record["grid"]),
        grid_offset=parse_fraction(record["grid_offset"]),
        a=parse_fraction(record["a"]),
        c=parse_fraction(record["c"]),
        radius=parse_fraction(record["radius"]),
        eta=parse_fraction(record["eta"]),
        maximum_subdivisions=maximum,
        fresh_discovery_eligible=bool(record["fresh_discovery_eligible"]),
    )


def witness_fields_match(
    expected: Mapping[str, object], observed: Mapping[str, object]
) -> bool:
    fields = (
        "failure_side",
        "boundary_index",
        "shared_boundary_fraction",
        "q_boundary_fraction",
        "source_indices",
        "target_indices",
        "source_id",
        "target_id",
        "coefficient_indices",
        "coefficient_interval_fraction",
        "source_x_interval_fraction",
        "source_y_interval_fraction",
        "target_x_interval_fraction",
        "target_y_interval_fraction",
        "left_boundary_slab_fraction",
        "right_boundary_slab_fraction",
        "left_q_range_fraction",
        "right_q_range_fraction",
        "true_closed_present",
        "forward_outer_present",
        "inverse_reverse_outer_present",
        "mutual_outer_present",
        "forward_outer_positive",
        "inverse_reverse_outer_positive",
        "exact_false_mutual_witness_pass",
    )
    return all(expected.get(field) == observed.get(field) for field in fields)


def replay_persisted_witnesses(
    records: Sequence[Mapping[str, object]], maximum: int
) -> dict[str, object]:
    checked = 0
    first_mismatch = None
    for record in records:
        configuration = configuration_from_record(record, maximum)
        witnesses = record.get("failure_witnesses")
        if not isinstance(witnesses, list):
            raise AssertionError("record failure_witnesses must be a list")
        for witness in witnesses:
            if not isinstance(witness, Mapping):
                raise AssertionError("persisted witness must be an object")
            source = witness["source_indices"]
            target = witness["target_indices"]
            recomputed = replay_witness(
                configuration,
                i=int(source["x"]),
                j=int(source["y"]),
                k=int(target["x"]),
                ell=int(target["y"]),
            )
            checked += 1
            if not witness_fields_match(recomputed, witness) and first_mismatch is None:
                first_mismatch = {
                    "configuration_id": configuration.configuration_id,
                    "observed": witness,
                    "recomputed": recomputed,
                }
    return {
        "witness_count": checked,
        "first_mismatch": first_mismatch,
        "pass": first_mismatch is None,
    }


def split_fraction_pair(value: str) -> tuple[Fraction, Fraction]:
    lower, upper = value.split(":", 1)
    return parse_fraction(lower), parse_fraction(upper)


def validate_boundary_row_arithmetic(row: Mapping[str, str]) -> bool:
    boundary = parse_fraction(row["boundary_fraction"])
    q_boundary = parse_fraction(row["q_boundary_fraction"])
    a_value = parse_fraction(row["a_fraction"])
    if q_boundary != a_value * boundary**2:
        return False
    left_slab = split_fraction_pair(row["left_boundary_slab_fraction"])
    right_slab = split_fraction_pair(row["right_boundary_slab_fraction"])
    left_q = split_fraction_pair(row["left_q_range_fraction"])
    right_q = split_fraction_pair(row["right_q_range_fraction"])
    if left_q != quadratic_range(*left_slab, a_value):
        return False
    if right_q != quadratic_range(*right_slab, a_value):
        return False
    if left_slab[1] != boundary or right_slab[0] != boundary:
        return False
    omega_plus = parse_fraction(row["omega_plus_fraction"])
    omega_minus = parse_fraction(row["omega_minus_fraction"])
    if omega_plus != min(left_q[1], right_q[1]) - q_boundary:
        return False
    if omega_minus != q_boundary - max(left_q[0], right_q[0]):
        return False
    delta_plus = parse_fraction_or_infinity(row["delta_plus_fraction"])
    delta_minus = parse_fraction_or_infinity(row["delta_minus_fraction"])
    margin_plus = parse_fraction_or_infinity(row["margin_plus_fraction"])
    margin_minus = parse_fraction_or_infinity(row["margin_minus_fraction"])
    plus_pass = parse_bool(row["plus_pass"])
    minus_pass = parse_bool(row["minus_pass"])
    if delta_plus is None:
        if margin_plus is not None or not plus_pass:
            return False
    elif margin_plus != delta_plus - omega_plus or plus_pass != (omega_plus < delta_plus):
        return False
    if delta_minus is None:
        if margin_minus is not None or not minus_pass:
            return False
    elif margin_minus != delta_minus - omega_minus or minus_pass != (omega_minus < delta_minus):
        return False
    return parse_bool(row["boundary_pass"]) == (plus_pass and minus_pass)


def audit_boundary_csv(
    path: Path, records: Sequence[Mapping[str, object]]
) -> dict[str, object]:
    by_name = {str(record["configuration_id"]): record for record in records}
    digests = {name: hashlib.sha256() for name in by_name}
    counts = {name: 0 for name in by_name}
    upper_failures = {name: 0 for name in by_name}
    lower_failures = {name: 0 for name in by_name}
    boundary_failures = {name: 0 for name in by_name}
    arithmetic_failures = 0
    first_arithmetic_failure = None
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != BOUNDARY_FIELDS:
            raise AssertionError("R057 boundary CSV header mismatch")
        for row_number, row in enumerate(reader, start=2):
            name = row["configuration_id"]
            record = by_name.get(name)
            if record is None:
                raise AssertionError(f"unknown boundary CSV configuration {name}")
            counts[name] += 1
            digests[name].update(
                ("|".join(str(row[field]) for field in BOUNDARY_HASH_FIELDS) + "\n").encode(
                    "ascii"
                )
            )
            plus_pass = parse_bool(row["plus_pass"])
            minus_pass = parse_bool(row["minus_pass"])
            upper_failures[name] += int(not plus_pass)
            lower_failures[name] += int(not minus_pass)
            boundary_failures[name] += int(not (plus_pass and minus_pass))
            if not validate_boundary_row_arithmetic(row):
                arithmetic_failures += 1
                if first_arithmetic_failure is None:
                    first_arithmetic_failure = {
                        "row_number": row_number,
                        "configuration_id": name,
                        "boundary_index": row["boundary_index"],
                    }

    record_checks = {}
    all_records_pass = True
    global_digest = hashlib.sha256()
    for record in records:
        name = str(record["configuration_id"])
        observed_hash = digests[name].hexdigest()
        checks = {
            "boundary_count": counts[name] == int(record["internal_boundary_count"]),
            "boundary_hash": observed_hash == record["boundary_record_sha256"],
            "upper_failure_count": upper_failures[name]
            == int(record["upper_failure_count"]),
            "lower_failure_count": lower_failures[name]
            == int(record["lower_failure_count"]),
            "failure_boundary_count": boundary_failures[name]
            == int(record["failure_boundary_count"]),
            "certificate_pass": bool(record["certificate_pass"])
            == (boundary_failures[name] == 0),
        }
        record_pass = all(checks.values())
        all_records_pass = all_records_pass and record_pass
        record_checks[name] = {"checks": checks, "pass": record_pass}
        global_digest.update(f"{name}|{observed_hash}\n".encode("ascii"))
    return {
        "row_count": sum(counts.values()),
        "record_count": len(records),
        "arithmetic_failure_count": arithmetic_failures,
        "first_arithmetic_failure": first_arithmetic_failure,
        "global_boundary_sha256": global_digest.hexdigest(),
        "record_checks": record_checks,
        "pass": all_records_pass and arithmetic_failures == 0,
    }


def validate_record_geometry(
    configuration: Configuration, record: Mapping[str, object]
) -> dict[str, bool]:
    edges, uncapped, _ = grid_geometry(configuration)
    widths = [right - left for left, right in zip(edges, edges[1:])]
    checks = {
        "panel_id": record["panel_id"] == configuration.panel_id,
        "configuration_id": record["configuration_id"]
        == configuration.configuration_id,
        "role": record["role"] == configuration.role,
        "grid": int(record["grid"]) == configuration.grid,
        "grid_offset": parse_fraction(record["grid_offset"])
        == configuration.grid_offset,
        "a": parse_fraction(record["a"]) == configuration.a,
        "c": parse_fraction(record["c"]) == configuration.c,
        "radius": parse_fraction(record["radius"]) == configuration.radius,
        "eta": parse_fraction(record["eta"]) == configuration.eta,
        "fresh_discovery_eligible": bool(record["fresh_discovery_eligible"])
        == configuration.fresh_discovery_eligible,
        "cell_count": int(record["cell_count"]) == configuration.grid**2,
        "internal_boundary_count": int(record["internal_boundary_count"])
        == configuration.grid - 1,
        "edge_vector_strict_pass": bool(record["edge_vector_strict_pass"]),
        "minimum_cell_width": parse_fraction(record["minimum_cell_width_fraction"])
        == min(widths),
        "uncapped_k_min": int(record["uncapped_k_min"]) == min(uncapped),
        "uncapped_k_max": int(record["uncapped_k_max"]) == max(uncapped),
        "cap_active_count": int(record["cap_active_count"])
        == sum(value >= configuration.maximum_subdivisions for value in uncapped),
        "k_gate_pass": bool(record["k_gate_pass"])
        == all(value < configuration.maximum_subdivisions for value in uncapped),
    }
    return checks


def recompute_decisions(
    records: Sequence[Mapping[str, object]], protocol: Mapping[str, object]
) -> dict[str, object]:
    centered = {
        int(record["grid"]): record
        for record in records
        if record["panel_id"] == "centered_resolution_scan"
    }
    development = protocol["development_observations_seen_before_freeze"]  # type: ignore[index]
    known_failures = set(map(int, development["centered_fail_grids"]))
    prior_passes = set(map(int, development["prior_pass_anchors"]))
    panel_ids = sorted({str(record["panel_id"]) for record in records})
    panel_summary = {}
    for panel_id in panel_ids:
        selected = [record for record in records if record["panel_id"] == panel_id]
        fail_count = sum(not bool(record["certificate_pass"]) for record in selected)
        panel_summary[panel_id] = {
            "configuration_count": len(selected),
            "pass_count": len(selected) - fail_count,
            "fail_count": fail_count,
            "failure_rate": fail_count / len(selected),
            "fresh_counterexample_count": sum(
                bool(record["fresh_counterexample"]) for record in selected
            ),
        }
    fresh = [record for record in records if record["fresh_counterexample"]]
    return {
        "configuration_count": len(records),
        "expected_configuration_count": 517,
        "panel_expansion_pass": len(records) == 517,
        "g2_neighbor_controls_pass": bool(centered[58]["certificate_pass"])
        and bool(centered[62]["certificate_pass"]),
        "g2_known_failure_replay_pass": all(
            not bool(centered[grid]["certificate_pass"]) for grid in known_failures
        ),
        "g2_centered_prior_pass_certificate_pass": all(
            bool(centered[grid]["certificate_pass"]) for grid in prior_passes
        ),
        "g2_shifted_prior_pass_certificate_pass": all(
            bool(record["certificate_pass"])
            for record in records
            if record["panel_id"] == "shifted_prior_pass_controls"
        ),
        "fresh_counterexample_count": len(fresh),
        "fresh_counterexample_configuration_ids": [
            str(record["configuration_id"]) for record in fresh
        ],
        "total_pass_count": sum(bool(record["certificate_pass"]) for record in records),
        "total_fail_count": sum(not bool(record["certificate_pass"]) for record in records),
        "panel_summary": panel_summary,
    }


def audit_persisted_result(
    result_path: Path,
    boundary_csv_path: Path,
    protocol: Mapping[str, object],
) -> tuple[dict[str, object], list[Mapping[str, object]]]:
    payload = json.loads(result_path.read_text(encoding="utf-8"))
    if payload.get("run_id") != "R057_MUTUAL_SEPARATION":
        raise AssertionError("unexpected persisted R057 run_id")
    if payload.get("protocol_sha256") != PROTOCOL_SHA256:
        raise AssertionError("persisted R057 protocol hash mismatch")
    records = payload.get("records")
    if not isinstance(records, list) or len(records) != 517:
        raise AssertionError("persisted R057 record panel is incomplete")
    configurations = expand_configurations(protocol)
    if [record.get("configuration_id") for record in records] != [
        item.configuration_id for item in configurations
    ]:
        raise AssertionError("persisted R057 configuration order/panel mismatch")

    geometry_checks = {}
    for configuration, record in zip(configurations, records):
        checks = validate_record_geometry(configuration, record)
        if not all(checks.values()):
            raise AssertionError(
                f"persisted geometry summary mismatch: {configuration.configuration_id}"
            )
        geometry_checks[configuration.configuration_id] = checks

    csv_audit = audit_boundary_csv(boundary_csv_path, records)
    if csv_audit["row_count"] != int(payload.get("boundary_row_count", -1)):
        raise AssertionError("persisted boundary row count mismatch")
    if csv_audit["global_boundary_sha256"] != payload.get(
        "boundary_records_sha256"
    ):
        raise AssertionError("persisted global boundary hash mismatch")
    if not csv_audit["pass"]:
        raise AssertionError("persisted boundary CSV arithmetic/schema audit failed")

    witness_audit = replay_persisted_witnesses(
        records,
        int(protocol["default_constants"]["maximum_subdivisions"]),  # type: ignore[index]
    )
    if not witness_audit["pass"]:
        raise AssertionError("persisted R057 witness replay failed")

    recomputed = recompute_decisions(records, protocol)
    observed_decisions = payload.get("decisions")
    if not isinstance(observed_decisions, Mapping):
        raise AssertionError("persisted R057 decisions object missing")
    decision_checks = {
        key: observed_decisions.get(key) == value
        for key, value in recomputed.items()
    }
    if not all(decision_checks.values()):
        raise AssertionError("persisted R057 aggregate decisions mismatch")

    cap_records = [
        str(record["configuration_id"])
        for record in records
        if not bool(record["k_gate_pass"])
    ]
    return (
        {
            "result_path": portable_path(result_path),
            "boundary_csv_path": portable_path(boundary_csv_path),
            "protocol_sha256_pass": True,
            "configuration_count": len(records),
            "geometry_record_count": len(geometry_checks),
            "boundary_csv": csv_audit,
            "witness_replay": witness_audit,
            "aggregate_decision_checks": decision_checks,
            "cap_gate_failure_count": len(cap_records),
            "cap_gate_failure_configuration_ids": cap_records,
            "producer_g0_pass": bool(
                observed_decisions.get("g0_protocol_and_exact_arithmetic_pass")
            ),
            "producer_g1_pass": bool(
                observed_decisions.get("g1_certificate_and_witness_integrity_pass")
            ),
            "producer_interpretation_enabled": bool(
                observed_decisions.get("interpretation_enabled")
            ),
            "schema_hash_witness_pass": True,
            "pass": True,
        },
        records,
    )


def main() -> None:
    args = parse_args()
    protocol = load_protocol(args.protocol)
    microgrids = run_microgrid_checks(protocol)
    n60 = run_n60_check(protocol)
    persisted, records = audit_persisted_result(
        args.input, args.boundary_csv, protocol
    )
    n60_record = next(
        record
        for record in records
        if record["panel_id"] == "centered_resolution_scan"
        and int(record["grid"]) == 60
    )
    persisted_n60_match = witness_fields_match(
        n60["recomputed_witness"], n60_record["first_failure_witness"]
    )
    g3_pass = all(item["pass"] for item in microgrids) and bool(n60["pass"]) and bool(
        persisted["pass"]
    ) and persisted_n60_match
    issues = []
    if persisted["cap_gate_failure_count"]:
        issues.append(
            {
                "issue": "frozen production panel violates the strict uncapped-K<64 gate",
                "configuration_count": persisted["cap_gate_failure_count"],
                "configuration_ids": persisted[
                    "cap_gate_failure_configuration_ids"
                ],
            }
        )
    capped_microgrids = [
        item["configuration_id"]
        for item in microgrids
        if int(item["cap_active_count"]) > 0
    ]
    if capped_microgrids:
        issues.append(
            {
                "issue": "frozen G3 microgrid also activates the default K=64 cap",
                "configuration_ids": capped_microgrids,
            }
        )
    producer_integrity = bool(persisted["producer_g0_pass"]) and bool(
        persisted["producer_g1_pass"]
    )
    output = {
        "run_id": "R057_MUTUAL_SEPARATION_INDEPENDENT_CHECK",
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_path": portable_path(args.protocol),
        "protocol_sha256": PROTOCOL_SHA256,
        "checker_imports_producer_certificate_or_incidence_helpers": False,
        "microgrid_full_graph_checks": microgrids,
        "n60_constructive_witness": n60,
        "persisted_n60_witness_match": persisted_n60_match,
        "persisted_result_audit": persisted,
        "issues": issues,
        "g3_independent_checker_pass": g3_pass,
        "producer_integrity_gates_pass": producer_integrity,
        "strict_all_frozen_gates_pass": g3_pass and producer_integrity,
        "all_checks_pass": g3_pass,
        "scope": (
            "independent exact finite-grid certificate and incidence audit only; "
            "no invariant-set, graph-limit, operator, zeta, or number-theory claim"
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "output": str(args.output),
                "g3_independent_checker_pass": g3_pass,
                "producer_integrity_gates_pass": producer_integrity,
                "strict_all_frozen_gates_pass": output[
                    "strict_all_frozen_gates_pass"
                ],
                "all_checks_pass": output["all_checks_pass"],
                "issue_count": len(issues),
            },
            indent=2,
        )
    )
    if not g3_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
