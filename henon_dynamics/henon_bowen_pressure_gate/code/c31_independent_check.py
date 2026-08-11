#!/usr/bin/env python3
"""Independent, type-strict checker for the HCS-C31 pressure certificate.

This module does not import the producer.  It reconstructs all 714 vertices,
all 1156 chronological edges, every finite R059 interval iteration, every
rational transcendental enclosure, and both Collatz inequalities.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import functools
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
HENON_ROOT = PROJECT.parent
REPO_ROOT = HENON_ROOT.parent
DEFAULT_CERTIFICATE = PROJECT / "results" / "c31_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c31_independent_check.json"

SOURCE_SPECS = {
    "R058_covering_proof": (
        "henon_dynamics/docs/related_programs/henon_weighted_zeta/R058_COVERING_PROOF.md",
        "c73188a079df87c93812f1dd5d90e0110a68d8f91780fea22bd779d40f4f59fe",
    ),
    "R058_domain_manifest": (
        "henon_dynamics/docs/related_programs/henon_weighted_zeta/research/refine-logs/R058_HYPERBOLIC_FILAMENT_MANIFEST.md",
        "906b515658e38c19a19de6b9558609248124307de08cfba8c0ce508d95c24e13",
    ),
    "R059_contraction_proof": (
        "henon_dynamics/docs/related_programs/henon_weighted_zeta/research/refine-logs/R059_SYMBOLIC_CONTRACTION_PROOF.md",
        "b2d2c46c198e20b40b042cf5bc02cbdcfe9835c1a7c193cd88476eebc3e3f315",
    ),
    "R059_domain_manifest": (
        "henon_dynamics/docs/related_programs/henon_weighted_zeta/research/refine-logs/R059_CERTIFIED_DOMAIN_MANIFEST.md",
        "b53c22aa198c5afc0927ee33c5eff40f690b7a61a1b4c36928000846be8e944b",
    ),
    "instability_roof_code": (
        "henon_dynamics/henon_instability_roof_zeta/code/henon_roof.py",
        "0ad2b4cf13467f3f4509628b51dec4c45d13ca758b2a79d801ace347c219173b",
    ),
    "instability_root_protocol": (
        "henon_dynamics/henon_instability_roof_zeta/refine-logs/R000_FROZEN_PROTOCOL.json",
        "0c284a1b3610a3d772aa00c6a8b33161a8bc6814957a9968d5c80fb618eec399",
    ),
    "instability_root_ledger": (
        "henon_dynamics/henon_instability_roof_zeta/results/roots_robustness.json",
        "840d63ae698c996def9fffb6f6eb5fc11e1024922cd82792eee5bb7c1550ea2a",
    ),
    "instability_root_summary": (
        "henon_dynamics/henon_instability_roof_zeta/results/analysis_summary.json",
        "a555a6e5f54011f56550265e8fbd3808c886cfe7521a62a644b81b316157de8f",
    ),
    "instability_root_independent_check": (
        "henon_dynamics/henon_instability_roof_zeta/results/independent_check.json",
        "7cbd41790d924143d7c36a9bc269d4ccc80df73b9d138bd5f13ebe0cfb5207b9",
    ),
}

LEGACY_ROOT_FULL = (
    "0.27798298167618902348832311683180466042471613147972330864936381175446226192981557"
)
LEGACY_ROOT_DISPLAY = "0.277982981676189"
LEGACY_ROOT_INDEX = 21
LEGACY_ROOT_PRECISION_DPS = 80
LEGACY_CANDIDATE_ID = "henon_h6_instability_roof_v1"
LEGACY_DETERMINANT = (
    "D_{kappa,N}(s) = degree-N-in-z cycle section of product_p "
    "(1 - sigma_p^kappa exp(-s T_p) z^n_p), evaluated at z=1"
)

NAMES = ("--", "-+", "+-", "++")
PAIRS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
GRAPH = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)
W = 13
L = 6
ITERATION_LIMIT = 100
DECIMAL_SCALE = 10**50
PERRON_SCALE = 10**30
LOG_INDEX = 64
EXP_ORDER = 61
WORKERS = 12
LEFT_S = Fraction(277980, 10**6)
RIGHT_S = Fraction(277987, 10**6)
SLOPE_R = Fraction(123, 112)
SLOPE_GAMMA = Fraction(112, 123)

Interval = tuple[Fraction, Fraction]


class GateFailure(Exception):
    pass


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def object_hash(value: object) -> str:
    raw = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def verified_legacy_root() -> str:
    """Independently replay the cutoff-20 root provenance chain."""

    def source_json(label: str) -> object:
        relative, _ = SOURCE_SPECS[label]
        return json.loads(
            (REPO_ROOT / relative).read_text(encoding="utf-8"),
            parse_float=Fraction,
        )

    protocol = source_json("instability_root_protocol")
    if type(protocol) is not dict or protocol.get("candidate_id") != LEGACY_CANDIDATE_ID:
        raise GateFailure("legacy root protocol candidate mismatch")
    if protocol.get("root_check_precision_dps") != LEGACY_ROOT_PRECISION_DPS:
        raise GateFailure("legacy root protocol precision mismatch")
    if protocol.get("determinant") != LEGACY_DETERMINANT:
        raise GateFailure("legacy root determinant convention mismatch")
    try:
        residual_tolerance = Fraction(protocol["high_precision_root_residual_max"])
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as exc:
        raise GateFailure("legacy root protocol residual tolerance is invalid") from exc

    ledger = source_json("instability_root_ledger")
    if type(ledger) is not dict:
        raise GateFailure("legacy root ledger is not an object")
    if ledger.get("protocol_sha256") != SOURCE_SPECS["instability_root_protocol"][1]:
        raise GateFailure("legacy root ledger points to a different frozen protocol")
    if ledger.get("candidate_id") != LEGACY_CANDIDATE_ID:
        raise GateFailure("legacy root ledger candidate mismatch")
    if ledger.get("catalog_max_period") != 20:
        raise GateFailure("legacy root ledger period scope mismatch")
    if ledger.get("determinant_convention") != LEGACY_DETERMINANT:
        raise GateFailure("legacy root ledger determinant mismatch")
    try:
        cutoff = ledger["sectors"]["0"]["cutoffs"]["20"]
    except (KeyError, TypeError) as exc:
        raise GateFailure("legacy root ledger cutoff-20 path is missing") from exc
    if (
        type(cutoff) is not dict
        or type(cutoff.get("cutoff")) is not int
        or cutoff["cutoff"] != 20
        or cutoff.get("kappa") != 0
    ):
        raise GateFailure("legacy root ledger cutoff field mismatch")
    raw_roots = cutoff.get("roots")
    high_roots = cutoff.get("high_precision_roots")
    if (
        type(raw_roots) is not list
        or type(high_roots) is not list
        or len(raw_roots) != len(high_roots)
    ):
        raise GateFailure("legacy raw/high-precision root ledgers are not aligned")
    positive_real_indices = [
        index
        for index, row in enumerate(raw_roots)
        if type(row) is list
        and len(row) == 2
        and type(row[0]) is Fraction
        and type(row[1]) is Fraction
        and row[0] > 0
        and abs(row[1]) < Fraction(1, 10**12)
    ]
    if positive_real_indices != [LEGACY_ROOT_INDEX]:
        raise GateFailure("legacy cutoff-20 positive near-real root index is not unique")
    target = high_roots[LEGACY_ROOT_INDEX]
    if type(target) is not dict or target.get("real") != LEGACY_ROOT_FULL:
        raise GateFailure("legacy cutoff-20 high-precision root value mismatch")
    if type(target.get("imag")) is not str or abs(Fraction(target["imag"])) >= Fraction(1, 10**90):
        raise GateFailure("legacy cutoff-20 root is not real to locked precision")
    for field in ("product_residual", "trace_residual", "coefficient_discrepancy"):
        if type(target.get(field)) is not str or abs(Fraction(target[field])) >= residual_tolerance:
            raise GateFailure(f"legacy root {field} exceeds the frozen tolerance")

    summary = source_json("instability_root_summary")
    try:
        summary_root = summary["untwisted"]["h20_high_precision"]
        summary_hash = summary["source_hashes"]["roots"]
    except (KeyError, TypeError) as exc:
        raise GateFailure("legacy root summary path is missing") from exc
    if summary_root != LEGACY_ROOT_FULL:
        raise GateFailure("legacy root summary disagrees with raw ledger")
    if summary.get("protocol_sha256") != SOURCE_SPECS["instability_root_protocol"][1]:
        raise GateFailure("legacy root summary points to a different frozen protocol")
    if summary_hash != SOURCE_SPECS["instability_root_ledger"][1]:
        raise GateFailure("legacy root summary points to a different ledger")

    audit = source_json("instability_root_independent_check")
    if (
        type(audit) is not dict
        or audit.get("status") != "PASS"
        or audit.get("all_checks_pass") is not True
    ):
        raise GateFailure("legacy root independent audit is not passing")
    if audit.get("protocol_sha256") != SOURCE_SPECS["instability_root_protocol"][1]:
        raise GateFailure("legacy root independent audit points to a different protocol")
    try:
        source_chain = audit["details"]["source_chain"]
        spot_checks = audit["details"]["determinant_audit"]["spot_checks"]
    except (KeyError, TypeError) as exc:
        raise GateFailure("legacy root independent-audit path is missing") from exc
    if source_chain["primary_hashes"]["roots"] != SOURCE_SPECS["instability_root_ledger"][1]:
        raise GateFailure("legacy independent audit points to a different ledger")
    if source_chain["primary_hashes"]["analysis"] != SOURCE_SPECS["instability_root_summary"][1]:
        raise GateFailure("legacy independent audit points to a different analysis summary")
    required_checks = {
        "frozen_protocol_hash",
        "primary_catalog_root_source_lock",
        "analysis_source_locks",
        "root_precision_and_residual_gates",
        "root_raw_summary_consistency",
        "leading_real_root_drifts_recomputed",
        "independent_determinant_spot_checks",
    }
    checks = audit.get("checks")
    if type(checks) is not dict or any(checks.get(key) is not True for key in required_checks):
        raise GateFailure("legacy root independent audit lacks a required passing gate")
    if type(spot_checks) is not list or not any(
        type(row) is dict
        and row.get("sector") == 0
        and row.get("cutoff") == 20
        and row.get("root_real") == "0.27798298167618902349"
        for row in spot_checks
    ):
        raise GateFailure("legacy independent audit lacks the cutoff-20 spot check")
    if not LEFT_S < Fraction(LEGACY_ROOT_FULL) < RIGHT_S:
        raise GateFailure("legacy cutoff-20 root is outside the pressure bracket")
    return LEGACY_ROOT_FULL


def exact_equal(observed: object, expected: object, location: str) -> None:
    if type(observed) is not type(expected):
        raise GateFailure(
            f"{location}: type {type(observed).__name__} != {type(expected).__name__}"
        )
    if isinstance(expected, dict):
        if set(observed) != set(expected):
            raise GateFailure(f"{location}: key set mismatch")
        for key in sorted(expected):
            exact_equal(observed[key], expected[key], f"{location}.{key}")
        return
    if isinstance(expected, list):
        if len(observed) != len(expected):
            raise GateFailure(f"{location}: list length mismatch")
        for index, (left, right) in enumerate(zip(observed, expected, strict=True)):
            exact_equal(left, right, f"{location}[{index}]")
        return
    if observed != expected:
        raise GateFailure(f"{location}: value mismatch")


def qtext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def parse_q(value: object, location: str) -> Fraction:
    if type(value) is not str:
        raise GateFailure(f"{location}: rational must be a string")
    try:
        parsed = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise GateFailure(f"{location}: malformed rational") from exc
    if qtext(parsed) != value:
        raise GateFailure(f"{location}: rational is not canonical")
    return parsed


def down(value: Fraction) -> Fraction:
    return Fraction((value.numerator * DECIMAL_SCALE) // value.denominator, DECIMAL_SCALE)


def up(value: Fraction) -> Fraction:
    return -down(-value)


def rational_sqrt_box(value: Fraction) -> Interval:
    if value < 0:
        raise GateFailure("negative radicand")
    numerator = value.numerator * DECIMAL_SCALE * DECIMAL_SCALE
    quotient = numerator // value.denominator
    integer = math.isqrt(quotient)
    lower = Fraction(integer, DECIMAL_SCALE)
    exact = integer * integer * value.denominator == numerator
    upper = lower if exact else Fraction(integer + 1, DECIMAL_SCALE)
    if lower * lower > value or upper * upper < value:
        raise GateFailure("isqrt enclosure failure")
    return lower, upper


def state_paths(length: int) -> list[tuple[int, ...]]:
    paths = [(letter,) for letter in range(4)]
    for _ in range(1, length):
        paths = [
            path + (child,)
            for path in paths
            for child in range(4)
            if GRAPH[path[-1]][child]
        ]
    return paths


def signs_of(path: tuple[int, ...]) -> tuple[int, ...]:
    signs = (PAIRS[path[0]][1],) + tuple(PAIRS[letter][0] for letter in path)
    for index in range(len(path) - 1):
        if PAIRS[path[index]][0] != PAIRS[path[index + 1]][1]:
            raise GateFailure("chronological sign mismatch")
    return signs


def initial_coordinate(sign: int) -> Interval:
    if sign == -1:
        return Fraction(-5, 8), Fraction(-1, 3)
    if sign == 1:
        return Fraction(1, 3), Fraction(5, 8)
    raise GateFailure("nonbinary sign")


def meet(a: Interval, b: Interval) -> Interval:
    result = max(a[0], b[0]), min(a[1], b[1])
    if result[0] > result[1]:
        raise GateFailure("empty R059 meet")
    return result


def root_step(a: Interval, b: Interval, sign: int) -> Interval:
    radicand = (Fraction(1) - a[1] - b[1]) / 6, (Fraction(1) - a[0] - b[0]) / 6
    if radicand[0] <= 0:
        raise GateFailure("R059 domain escaped")
    low = rational_sqrt_box(radicand[0])[0]
    high = rational_sqrt_box(radicand[1])[1]
    return (low, high) if sign > 0 else (-high, -low)


def scaled_inverse(box: Interval, scale: Fraction) -> Interval:
    if box[0] <= 0 <= box[1]:
        raise GateFailure("projective pole in interval")
    return scale / box[1], scale / box[0]


def cylinder_j(path: tuple[int, ...]) -> tuple[Interval, int]:
    signs = signs_of(path)
    coordinates = [initial_coordinate(sign) for sign in signs]
    count = 0
    for count in range(1, ITERATION_LIMIT + 1):
        next_coordinates = list(coordinates)
        for index in range(1, len(coordinates) - 1):
            next_coordinates[index] = meet(
                coordinates[index],
                root_step(coordinates[index - 1], coordinates[index + 1], signs[index]),
            )
        if next_coordinates == coordinates:
            coordinates = next_coordinates
            break
        coordinates = next_coordinates

    mu: Interval = (Fraction(-1, 2), Fraction(1, 2))
    for index in range(1, L + 1):
        denominator = (
            -12 * coordinates[index][1] - SLOPE_R * mu[1],
            -12 * coordinates[index][0] - SLOPE_R * mu[0],
        )
        mu = scaled_inverse(denominator, SLOPE_GAMMA)
        if mu[0] < Fraction(-1, 2) or mu[1] > Fraction(1, 2):
            raise GateFailure("unstable cone escape")

    q0 = coordinates[L + 1]
    denominator = (
        -12 * q0[1] - SLOPE_R * mu[1],
        -12 * q0[0] - SLOPE_R * mu[0],
    )
    if denominator[0] > 0:
        jacobian = denominator
    elif denominator[1] < 0:
        jacobian = -denominator[1], -denominator[0]
    else:
        raise GateFailure("central Jacobian changes orientation")
    answer = down(jacobian[0]), up(jacobian[1])
    if answer[0] < Fraction(773, 224) or answer[0] > answer[1]:
        raise GateFailure("adapted expansion certificate failed")
    return answer, count


def positive_box(value: Fraction) -> Interval:
    if value < 0:
        raise GateFailure("positive-box precondition failed")
    return down(value), up(value)


def log_reduced(y: Fraction) -> Interval:
    if not Fraction(1) <= y <= Fraction(2):
        raise GateFailure("log reduction failure")
    t = positive_box((y - 1) / (y + 1))
    square = down(t[0] * t[0]), up(t[1] * t[1])
    power = t
    low = Fraction(0)
    high = Fraction(0)
    for index in range(LOG_INDEX + 1):
        divisor = 2 * index + 1
        low += down(2 * power[0] / divisor)
        high += up(2 * power[1] / divisor)
        power = down(power[0] * square[0]), up(power[1] * square[1])
    tail = up(2 * power[1] / ((2 * LOG_INDEX + 3) * (1 - square[1])))
    return down(low), up(high + tail)


CHECK_LOG_TWO = log_reduced(Fraction(2))


def rational_log(value: Fraction) -> Interval:
    if value <= 0:
        raise GateFailure("nonpositive logarithm input")
    exponent = 0
    y = value
    while y >= 2:
        y /= 2
        exponent += 1
    while y < 1:
        y *= 2
        exponent -= 1
    base = log_reduced(y)
    if exponent >= 0:
        return down(base[0] + exponent * CHECK_LOG_TWO[0]), up(
            base[1] + exponent * CHECK_LOG_TWO[1]
        )
    return down(base[0] + exponent * CHECK_LOG_TWO[1]), up(
        base[1] + exponent * CHECK_LOG_TWO[0]
    )


def rational_exp_minus(x: Fraction) -> Interval:
    if not Fraction(0) < x < Fraction(1):
        raise GateFailure("alternating exponential precondition failed")
    x_box = positive_box(x)
    term: Interval = Fraction(1), Fraction(1)
    total: Interval = Fraction(1), Fraction(1)
    odd: Interval | None = None
    for order in range(1, EXP_ORDER + 2):
        term = down(term[0] * x_box[0] / order), up(term[1] * x_box[1] / order)
        if order % 2:
            total = down(total[0] - term[1]), up(total[1] - term[0])
            if order == EXP_ORDER:
                odd = total
        else:
            total = down(total[0] + term[0]), up(total[1] + term[1])
    if odd is None:
        raise GateFailure("missing odd Taylor sum")
    result = down(odd[0]), up(total[1])
    if not Fraction(0) < result[0] <= result[1] < 1:
        raise GateFailure("exponential enclosure failure")
    return result


def certified_weights(bounds: Interval) -> tuple[Fraction, Fraction]:
    lower_exponent = up(LEFT_S * rational_log(bounds[1])[1])
    upper_exponent = down(RIGHT_S * rational_log(bounds[0])[0])
    return rational_exp_minus(lower_exponent)[0], rational_exp_minus(upper_exponent)[1]


@functools.lru_cache(maxsize=1)
def reconstruct_graph() -> tuple[
    tuple[str, ...], tuple[dict[str, object], ...], tuple[tuple[int, int, Fraction, Fraction], ...]
]:
    node_paths = state_paths(W - 1)
    edge_paths = state_paths(W)
    if len(node_paths) != 714 or len(edge_paths) != 1156:
        raise GateFailure("higher-block census mismatch")
    node_id = {path: index for index, path in enumerate(node_paths)}
    with concurrent.futures.ProcessPoolExecutor(max_workers=WORKERS) as executor:
        interval_rows = list(executor.map(cylinder_j, edge_paths, chunksize=8))
    records = []
    internal = []
    for index, (path, interval_row) in enumerate(zip(edge_paths, interval_rows, strict=True)):
        bounds, rounds = interval_row
        source = node_id[path[:-1]]
        target = node_id[path[1:]]
        records.append(
            {
                "index": index,
                "word": "".join(str(letter) for letter in path),
                "source": source,
                "target": target,
                "signs": "".join("+" if sign > 0 else "-" for sign in signs_of(path)),
                "jacobi_rounds": rounds,
                "j_lower": qtext(bounds[0]),
                "j_upper": qtext(bounds[1]),
            }
        )
        internal.append((source, target, bounds[0], bounds[1]))
    return (
        tuple("".join(str(letter) for letter in path) for path in node_paths),
        tuple(records),
        tuple(internal),
    )


@functools.lru_cache(maxsize=1)
def reconstruct_weights() -> tuple[tuple[Fraction, Fraction], ...]:
    bounds = [(row[2], row[3]) for row in reconstruct_graph()[2]]
    with concurrent.futures.ProcessPoolExecutor(max_workers=WORKERS) as executor:
        return tuple(executor.map(certified_weights, bounds, chunksize=8))


def expected_protocol() -> dict[str, object]:
    return {
        "map": "H_6(q,p)=(1-6q^2-p,q)",
        "state_names": list(NAMES),
        "state_pairs": [list(pair) for pair in PAIRS],
        "adjacency_source_rows_target_columns": [list(row) for row in GRAPH],
        "window_state_length": W,
        "center_radius": L,
        "signed_coordinate_order": "epsilon_-7,...,epsilon_6",
        "fixed_q_endpoints": [-7, 6],
        "jacobi_internal_coordinates": [-6, 5],
        "jacobi_round_cap": ITERATION_LIMIT,
        "sqrt_grid_denominator": DECIMAL_SCALE,
        "transcendental_grid_denominator": DECIMAL_SCALE,
        "log_series_last_index": LOG_INDEX,
        "exp_odd_order": EXP_ORDER,
        "adapted_slope_initial_interval": ["-1/2", "1/2"],
        "adapted_constants": {"r": "123/112", "gamma": "112/123", "J_min": "773/224"},
        "endpoint_s_lower": qtext(LEFT_S),
        "endpoint_s_upper": qtext(RIGHT_S),
        "proof_arithmetic": "Fraction plus integer isqrt and outward 10^-50 grids",
        "floating_point_scope": "candidate Collatz vectors only; never trusted by checker",
        "fixed_exact_worker_count": WORKERS,
    }


def validate_vector(value: object, location: str) -> list[int]:
    if type(value) is not list or len(value) != 714:
        raise GateFailure(f"{location}: expected 714-entry list")
    if any(type(entry) is not int or entry <= 0 for entry in value):
        raise GateFailure(f"{location}: vector entries must be positive exact integers")
    if math.gcd(*value) != 1:
        raise GateFailure(f"{location}: vector is not primitive")
    return value


def exact_collatz(vector: list[int], lower: bool) -> Fraction:
    graph = reconstruct_graph()[2]
    weights = reconstruct_weights()
    image = [Fraction(0) for _ in range(714)]
    for row, pair in zip(graph, weights, strict=True):
        source, target = row[0], row[1]
        weight = pair[0] if lower else pair[1]
        image[source] += weight * vector[target]
    ratios = [image[index] / vector[index] for index in range(714)]
    return min(ratios) if lower else max(ratios)


class Audit:
    def __init__(self, certificate: object):
        self.certificate = certificate
        self.payload: dict[str, object] = {}
        self.rows: list[dict[str, str]] = []

    def gate(self, name: str, action) -> None:
        try:
            detail = action()
        except GateFailure as exc:
            self.rows.append({"gate": name, "status": "FAIL", "detail": str(exc)})
        except Exception as exc:  # implementation defects never masquerade as semantic rejection
            self.rows.append(
                {
                    "gate": name,
                    "status": "ERROR",
                    "detail": f"{type(exc).__name__}: {exc}",
                }
            )
        else:
            self.rows.append({"gate": name, "status": "PASS", "detail": detail})

    def envelope(self) -> str:
        if type(self.certificate) is not dict:
            raise GateFailure("certificate is not an object")
        if set(self.certificate) != {"schema", "producer", "payload", "payload_sha256"}:
            raise GateFailure("certificate key set mismatch")
        if self.certificate["schema"] != "hcs-c31-bowen-pressure-certificate-v2":
            raise GateFailure("schema mismatch")
        if self.certificate["producer"] != "code/c31_producer.py":
            raise GateFailure("producer path mismatch")
        if type(self.certificate["payload"]) is not dict:
            raise GateFailure("payload is not an object")
        if type(self.certificate["payload_sha256"]) is not str:
            raise GateFailure("payload hash is not a string")
        if object_hash(self.certificate["payload"]) != self.certificate["payload_sha256"]:
            raise GateFailure("stale payload hash")
        self.payload = self.certificate["payload"]
        if set(self.payload) != {
            "source_lock",
            "protocol",
            "higher_block_graph",
            "pressure_certificate",
            "claims",
        }:
            raise GateFailure("payload key set mismatch")
        return "schema, exact key sets, and canonical payload hash pass"

    def sources(self) -> str:
        expected = {}
        for label, (relative, digest) in SOURCE_SPECS.items():
            path = REPO_ROOT / relative
            if file_hash(path) != digest:
                raise GateFailure(f"live source drift: {label}")
            expected[label] = {"path": relative, "sha256": digest}
        exact_equal(self.payload["source_lock"], expected, "payload.source_lock")
        verified_legacy_root()
        return "nine inherited sources and the cutoff-20 root provenance chain are byte locked"

    def protocol(self) -> str:
        exact_equal(self.payload["protocol"], expected_protocol(), "payload.protocol")
        return "W=13 chronology, finite Jacobi, cone, and rational rounding contract pass"

    def graph(self) -> str:
        node_names, edge_rows, internal = reconstruct_graph()
        expected = {
            "node_word_length": 12,
            "edge_word_length": 13,
            "node_count": 714,
            "edge_count": 1156,
            "nodes": list(node_names),
            "edges": list(edge_rows),
            "maximum_jacobi_rounds_executed": max(int(row["jacobi_rounds"]) for row in edge_rows),
            "minimum_j_lower": qtext(min(row[2] for row in internal)),
            "maximum_j_upper": qtext(max(row[3] for row in internal)),
            "maximum_j_interval_width": qtext(max(row[3] - row[2] for row in internal)),
        }
        exact_equal(self.payload["higher_block_graph"], expected, "payload.higher_block_graph")
        indegree = [0] * 714
        outdegree = [0] * 714
        for source, target, _, _ in internal:
            outdegree[source] += 1
            indegree[target] += 1
        if min(indegree) < 1 or min(outdegree) < 1:
            raise GateFailure("higher-block graph has a dead vertex")
        return "714 vertices, 1156 edges, chronology, and every direct J interval pass"

    def pressure(self) -> str:
        pressure = self.payload["pressure_certificate"]
        if type(pressure) is not dict or set(pressure) != {
            "lower_endpoint",
            "upper_endpoint",
            "certified_root_bracket",
            "decimal_bracket",
            "width",
            "legacy_period20_high_precision_root",
            "legacy_root_display",
            "legacy_root_provenance",
            "legacy_root_is_strictly_contained",
        }:
            raise GateFailure("pressure certificate key set mismatch")
        lower = pressure["lower_endpoint"]
        upper = pressure["upper_endpoint"]
        if type(lower) is not dict or set(lower) != {
            "s", "matrix_weight", "collatz_direction", "vector", "collatz_minimum", "strict_margin"
        }:
            raise GateFailure("lower endpoint key set mismatch")
        if type(upper) is not dict or set(upper) != {
            "s", "matrix_weight", "collatz_direction", "vector", "collatz_maximum", "strict_margin"
        }:
            raise GateFailure("upper endpoint key set mismatch")
        expected_scalars = {
            "lower_s": qtext(LEFT_S),
            "upper_s": qtext(RIGHT_S),
            "lower_weight": "lower enclosure of (J_edge_upper)^(-s)",
            "upper_weight": "upper enclosure of (J_edge_lower)^(-s)",
            "lower_direction": "minimum row ratio > 1",
            "upper_direction": "maximum row ratio < 1",
        }
        observed_scalars = {
            "lower_s": lower["s"],
            "upper_s": upper["s"],
            "lower_weight": lower["matrix_weight"],
            "upper_weight": upper["matrix_weight"],
            "lower_direction": lower["collatz_direction"],
            "upper_direction": upper["collatz_direction"],
        }
        exact_equal(observed_scalars, expected_scalars, "pressure.endpoint_contract")
        lower_vector = validate_vector(lower["vector"], "lower.vector")
        upper_vector = validate_vector(upper["vector"], "upper.vector")
        minimum = exact_collatz(lower_vector, True)
        maximum = exact_collatz(upper_vector, False)
        if minimum <= 1 or maximum >= 1:
            raise GateFailure("strict rational Collatz signs do not bracket a root")
        exact_equal(lower["collatz_minimum"], qtext(minimum), "lower.collatz_minimum")
        exact_equal(lower["strict_margin"], qtext(minimum - 1), "lower.strict_margin")
        exact_equal(upper["collatz_maximum"], qtext(maximum), "upper.collatz_maximum")
        exact_equal(upper["strict_margin"], qtext(1 - maximum), "upper.strict_margin")
        expected_metadata = {
            "certified_root_bracket": [qtext(LEFT_S), qtext(RIGHT_S)],
            "decimal_bracket": ["0.277980", "0.277987"],
            "width": "7/1000000",
            "legacy_period20_high_precision_root": verified_legacy_root(),
            "legacy_root_display": LEGACY_ROOT_DISPLAY,
            "legacy_root_provenance": {
                "cutoff": 20,
                "sector": 0,
                "root_index": LEGACY_ROOT_INDEX,
                "precision_dps": LEGACY_ROOT_PRECISION_DPS,
                "evidence_status": "NUMERICAL_OBSERVATION",
                "ledger_source_label": "instability_root_ledger",
                "summary_source_label": "instability_root_summary",
                "independent_check_source_label": "instability_root_independent_check",
            },
            "legacy_root_is_strictly_contained": True,
        }
        exact_equal(
            {key: pressure[key] for key in expected_metadata},
            expected_metadata,
            "pressure.metadata",
        )
        return "pure-rational lower Collatz >1 and upper Collatz <1 certify [0.277980,0.277987]"

    def claims(self) -> str:
        expected = {
            "all_W13_cylinders_enclosed": True,
            "chronological_higher_block_dynamics_preserved": True,
            "bowen_pressure_root_exists_uniquely_in_bracket": True,
            "pressure_status": "NUMERICALLY_CERTIFIED",
            "analytic_pressure_implication_status": "PROVED",
            "this_is_not_a_fredholm_or_hilbert_polya_certificate": True,
            "route_a_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "route_a_overall": "ROUTE_A_REJECTED",
        }
        exact_equal(self.payload["claims"], expected, "payload.claims")
        return "pressure theorem passes; Route-A remains rejected with A2/A3 failures"

    def run(self) -> dict[str, object]:
        self.gate("G0_ENVELOPE_AND_HASH", self.envelope)
        if not self.payload:
            return self.report()
        self.gate("G1_SOURCE_LOCK", self.sources)
        self.gate("G2_TYPE_STRICT_PROTOCOL", self.protocol)
        self.gate("G3_ALL_CYLINDER_GRAPH", self.graph)
        self.gate("G4_RATIONAL_COLLATZ_BRACKET", self.pressure)
        self.gate("G5_SCOPE_AND_ROUTE_A", self.claims)
        return self.report()

    def report(self) -> dict[str, object]:
        passed = sum(row["status"] == "PASS" for row in self.rows)
        return {
            "schema": "hcs-c31-independent-check-v1",
            "checker": "code/c31_independent_check.py",
            "certificate_payload_sha256": (
                self.certificate.get("payload_sha256", "")
                if type(self.certificate) is dict
                else ""
            ),
            "all_pass": passed == len(self.rows) and len(self.rows) == 6,
            "passed": passed,
            "total": len(self.rows),
            "gates": self.rows,
        }


def main() -> None:
    args = cli()
    try:
        certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"cannot read certificate: {exc}") from exc
    report = Audit(certificate).run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(f"checked {args.certificate}: {report['passed']}/{report['total']} gates pass")
    if not report["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
