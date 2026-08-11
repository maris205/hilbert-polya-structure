#!/usr/bin/env python3
"""Produce the HCS-C31 finite-cylinder Bowen-pressure certificate.

The theorem-critical path uses ``fractions.Fraction`` only.  Binary floating
point is confined to the construction of two candidate Perron vectors; the
certificate is accepted only after rational log/exp enclosures and rational
Collatz inequalities have independently verified those vectors.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
HENON_ROOT = PROJECT.parent
REPO_ROOT = HENON_ROOT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c31_certificate.json"

SOURCES = {
    "R058_covering_proof": HENON_ROOT
    / "docs/related_programs/henon_weighted_zeta/R058_COVERING_PROOF.md",
    "R058_domain_manifest": HENON_ROOT
    / "docs/related_programs/henon_weighted_zeta/research/refine-logs/R058_HYPERBOLIC_FILAMENT_MANIFEST.md",
    "R059_contraction_proof": HENON_ROOT
    / "docs/related_programs/henon_weighted_zeta/research/refine-logs/R059_SYMBOLIC_CONTRACTION_PROOF.md",
    "R059_domain_manifest": HENON_ROOT
    / "docs/related_programs/henon_weighted_zeta/research/refine-logs/R059_CERTIFIED_DOMAIN_MANIFEST.md",
    "instability_roof_code": HENON_ROOT
    / "henon_instability_roof_zeta/code/henon_roof.py",
    "instability_root_protocol": HENON_ROOT
    / "henon_instability_roof_zeta/refine-logs/R000_FROZEN_PROTOCOL.json",
    "instability_root_ledger": HENON_ROOT
    / "henon_instability_roof_zeta/results/roots_robustness.json",
    "instability_root_summary": HENON_ROOT
    / "henon_instability_roof_zeta/results/analysis_summary.json",
    "instability_root_independent_check": HENON_ROOT
    / "henon_instability_roof_zeta/results/independent_check.json",
}
EXPECTED_SOURCE_HASHES = {
    "R058_covering_proof": "c73188a079df87c93812f1dd5d90e0110a68d8f91780fea22bd779d40f4f59fe",
    "R058_domain_manifest": "906b515658e38c19a19de6b9558609248124307de08cfba8c0ce508d95c24e13",
    "R059_contraction_proof": "b2d2c46c198e20b40b042cf5bc02cbdcfe9835c1a7c193cd88476eebc3e3f315",
    "R059_domain_manifest": "b53c22aa198c5afc0927ee33c5eff40f690b7a61a1b4c36928000846be8e944b",
    "instability_roof_code": "0ad2b4cf13467f3f4509628b51dec4c45d13ca758b2a79d801ace347c219173b",
    "instability_root_protocol": "0c284a1b3610a3d772aa00c6a8b33161a8bc6814957a9968d5c80fb618eec399",
    "instability_root_ledger": "840d63ae698c996def9fffb6f6eb5fc11e1024922cd82792eee5bb7c1550ea2a",
    "instability_root_summary": "a555a6e5f54011f56550265e8fbd3808c886cfe7521a62a644b81b316157de8f",
    "instability_root_independent_check": "7cbd41790d924143d7c36a9bc269d4ccc80df73b9d138bd5f13ebe0cfb5207b9",
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

STATE_NAMES = ("--", "-+", "+-", "++")
STATE_PAIRS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)
WINDOW = 13
RADIUS = 6
JACOBI_CAP = 100
GRID_DENOMINATOR = 10**50
VECTOR_DENOMINATOR = 10**30
LOG_LAST_INDEX = 64
EXP_ODD_ORDER = 61
EXACT_WORKERS = 12
S_LOWER = Fraction(277980, 10**6)
S_UPPER = Fraction(277987, 10**6)
R = Fraction(123, 112)
GAMMA = Fraction(112, 123)

Interval = tuple[Fraction, Fraction]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha256(value: object) -> str:
    raw = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def verified_legacy_root() -> str:
    """Read and cross-lock the actual cutoff-20 legacy root provenance."""

    protocol = json.loads(
        SOURCES["instability_root_protocol"].read_text(encoding="utf-8"),
        parse_float=Fraction,
    )
    if protocol.get("candidate_id") != LEGACY_CANDIDATE_ID:
        raise AssertionError("legacy root protocol candidate mismatch")
    if protocol.get("root_check_precision_dps") != LEGACY_ROOT_PRECISION_DPS:
        raise AssertionError("legacy root protocol precision mismatch")
    if protocol.get("determinant") != LEGACY_DETERMINANT:
        raise AssertionError("legacy root determinant convention mismatch")
    residual_tolerance = Fraction(protocol["high_precision_root_residual_max"])

    ledger = json.loads(
        SOURCES["instability_root_ledger"].read_text(encoding="utf-8"),
        parse_float=Fraction,
    )
    if ledger["protocol_sha256"] != EXPECTED_SOURCE_HASHES["instability_root_protocol"]:
        raise AssertionError("legacy root ledger points to a different frozen protocol")
    if ledger.get("candidate_id") != LEGACY_CANDIDATE_ID:
        raise AssertionError("legacy root ledger candidate mismatch")
    if ledger.get("catalog_max_period") != 20:
        raise AssertionError("legacy root ledger period scope mismatch")
    if ledger.get("determinant_convention") != LEGACY_DETERMINANT:
        raise AssertionError("legacy root ledger determinant mismatch")
    cutoff = ledger["sectors"]["0"]["cutoffs"]["20"]
    if (
        type(cutoff.get("cutoff")) is not int
        or cutoff["cutoff"] != 20
        or cutoff.get("kappa") != 0
    ):
        raise AssertionError("legacy root ledger does not identify cutoff 20")
    raw_roots = cutoff["roots"]
    high_roots = cutoff["high_precision_roots"]
    if type(raw_roots) is not list or type(high_roots) is not list or len(raw_roots) != len(high_roots):
        raise AssertionError("legacy raw/high-precision root ledgers are not aligned")
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
        raise AssertionError("cutoff-20 positive near-real root index is not unique")
    target = high_roots[LEGACY_ROOT_INDEX]
    if type(target) is not dict or target.get("real") != LEGACY_ROOT_FULL:
        raise AssertionError("cutoff-20 high-precision root value mismatch")
    if abs(Fraction(target["imag"])) >= Fraction(1, 10**90):
        raise AssertionError("legacy root ledger entry is not real to the locked precision")
    for field in ("product_residual", "trace_residual", "coefficient_discrepancy"):
        if abs(Fraction(target[field])) >= residual_tolerance:
            raise AssertionError(f"legacy root {field} exceeds the frozen tolerance")

    summary = json.loads(
        SOURCES["instability_root_summary"].read_text(encoding="utf-8"),
        parse_float=Fraction,
    )
    if summary["untwisted"]["h20_high_precision"] != LEGACY_ROOT_FULL:
        raise AssertionError("legacy root summary disagrees with the raw ledger")
    if summary["protocol_sha256"] != EXPECTED_SOURCE_HASHES["instability_root_protocol"]:
        raise AssertionError("legacy root summary points to a different frozen protocol")
    if summary["source_hashes"]["roots"] != EXPECTED_SOURCE_HASHES["instability_root_ledger"]:
        raise AssertionError("legacy root summary does not point to the locked ledger")

    audit = json.loads(
        SOURCES["instability_root_independent_check"].read_text(encoding="utf-8"),
        parse_float=Fraction,
    )
    if audit.get("status") != "PASS" or audit.get("all_checks_pass") is not True:
        raise AssertionError("legacy root independent audit is not passing")
    if audit["protocol_sha256"] != EXPECTED_SOURCE_HASHES["instability_root_protocol"]:
        raise AssertionError("legacy root independent audit points to a different protocol")
    source_chain = audit["details"]["source_chain"]
    if source_chain["primary_hashes"]["roots"] != EXPECTED_SOURCE_HASHES["instability_root_ledger"]:
        raise AssertionError("legacy independent audit points to a different root ledger")
    if source_chain["primary_hashes"]["analysis"] != EXPECTED_SOURCE_HASHES["instability_root_summary"]:
        raise AssertionError("legacy independent audit points to a different analysis summary")
    required_checks = {
        "frozen_protocol_hash",
        "primary_catalog_root_source_lock",
        "analysis_source_locks",
        "root_precision_and_residual_gates",
        "root_raw_summary_consistency",
        "leading_real_root_drifts_recomputed",
        "independent_determinant_spot_checks",
    }
    if any(audit["checks"].get(key) is not True for key in required_checks):
        raise AssertionError("legacy root independent audit lacks a required passing gate")
    spot_checks = audit["details"]["determinant_audit"]["spot_checks"]
    if not any(
        type(row) is dict
        and row.get("sector") == 0
        and row.get("cutoff") == 20
        and row.get("root_real") == "0.27798298167618902349"
        for row in spot_checks
    ):
        raise AssertionError("legacy independent audit lacks the cutoff-20 root spot check")
    return LEGACY_ROOT_FULL


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def floor_grid(value: Fraction) -> Fraction:
    return Fraction((value.numerator * GRID_DENOMINATOR) // value.denominator, GRID_DENOMINATOR)


def ceil_grid(value: Fraction) -> Fraction:
    return -floor_grid(-value)


def sqrt_interval(value: Fraction) -> Interval:
    if value < 0:
        raise AssertionError("negative square-root input")
    scaled_numerator = value.numerator * GRID_DENOMINATOR * GRID_DENOMINATOR
    quotient = scaled_numerator // value.denominator
    lower_integer = math.isqrt(quotient)
    lower = Fraction(lower_integer, GRID_DENOMINATOR)
    if lower_integer * lower_integer * value.denominator == scaled_numerator:
        upper = lower
    else:
        upper = Fraction(lower_integer + 1, GRID_DENOMINATOR)
    if not lower * lower <= value <= upper * upper:
        raise AssertionError("invalid square-root enclosure")
    return lower, upper


def admissible_words(length: int) -> list[tuple[int, ...]]:
    words = [(state,) for state in range(4)]
    for _ in range(1, length):
        words = [
            word + (target,)
            for word in words
            for target, allowed in enumerate(ADJACENCY[word[-1]])
            if allowed
        ]
    return words


def edge_signs(word: tuple[int, ...]) -> tuple[int, ...]:
    signs = (STATE_PAIRS[word[0]][1],) + tuple(STATE_PAIRS[state][0] for state in word)
    for index in range(len(word) - 1):
        if STATE_PAIRS[word[index]][0] != STATE_PAIRS[word[index + 1]][1]:
            raise AssertionError("state path does not preserve chronological sign overlap")
    return signs


def signed_box(sign: int) -> Interval:
    return (
        (Fraction(-5, 8), Fraction(-1, 3))
        if sign < 0
        else (Fraction(1, 3), Fraction(5, 8))
    )


def intersect(left: Interval, right: Interval) -> Interval:
    answer = max(left[0], right[0]), min(left[1], right[1])
    if answer[0] > answer[1]:
        raise AssertionError("empty interval intersection")
    return answer


def signed_root_image(left: Interval, right: Interval, sign: int) -> Interval:
    radicand = (
        (1 - left[1] - right[1]) / 6,
        (1 - left[0] - right[0]) / 6,
    )
    if radicand[0] <= 0:
        raise AssertionError("nonpositive R059 radicand")
    square_lower = sqrt_interval(radicand[0])[0]
    square_upper = sqrt_interval(radicand[1])[1]
    return (
        (square_lower, square_upper)
        if sign > 0
        else (-square_upper, -square_lower)
    )


def reciprocal_scaled(interval: Interval, scale: Fraction) -> Interval:
    lower, upper = interval
    if lower <= 0 <= upper:
        raise AssertionError("projective denominator crosses zero")
    return scale / upper, scale / lower


def direct_j_interval(word: tuple[int, ...]) -> tuple[Interval, int]:
    """Enclose J at time zero for every full itinerary in one W=13 cylinder.

    The two exterior q coordinates stay at their inherited sign boxes.  Every
    finite Jacobi intersection is inclusion preserving, so stopping after at
    most 100 rounds makes no appeal to convergence of the interval iteration.
    """
    signs = edge_signs(word)
    q = [signed_box(sign) for sign in signs]
    executed = 0
    for iteration in range(1, JACOBI_CAP + 1):
        updated = list(q)
        for index in range(1, len(q) - 1):
            updated[index] = intersect(
                q[index], signed_root_image(q[index - 1], q[index + 1], signs[index])
            )
        executed = iteration
        if updated == q:
            q = updated
            break
        q = updated

    slope: Interval = (Fraction(-1, 2), Fraction(1, 2))
    # q indices 1,...,6 represent q_-6,...,q_-1.
    for index in range(1, RADIUS + 1):
        denominator = (
            -12 * q[index][1] - R * slope[1],
            -12 * q[index][0] - R * slope[0],
        )
        slope = reciprocal_scaled(denominator, GAMMA)
        if not (Fraction(-1, 2) <= slope[0] <= slope[1] <= Fraction(1, 2)):
            raise AssertionError("slope left the normalized unstable cone")

    q_zero = q[RADIUS + 1]
    denominator = (
        -12 * q_zero[1] - R * slope[1],
        -12 * q_zero[0] - R * slope[0],
    )
    if denominator[0] > 0:
        jacobian = denominator
    elif denominator[1] < 0:
        jacobian = -denominator[1], -denominator[0]
    else:
        raise AssertionError("central adapted Jacobian crosses zero")
    enclosed = floor_grid(jacobian[0]), ceil_grid(jacobian[1])
    if enclosed[0] < Fraction(773, 224) or enclosed[0] > enclosed[1]:
        raise AssertionError("adapted expansion lower bound failed")
    return enclosed, executed


def positive_grid_interval(value: Fraction) -> Interval:
    if value < 0:
        raise AssertionError("positive interval requested for a negative number")
    return floor_grid(value), ceil_grid(value)


def atanh_log_unit_interval(y: Fraction) -> Interval:
    """Outward rational enclosure of log(y), for 1 <= y <= 2."""
    if not Fraction(1) <= y <= Fraction(2):
        raise AssertionError("atanh log reduction outside [1,2]")
    t_exact = (y - 1) / (y + 1)
    t = positive_grid_interval(t_exact)
    t_squared = floor_grid(t[0] * t[0]), ceil_grid(t[1] * t[1])
    power = t
    total_lower = Fraction(0)
    total_upper = Fraction(0)
    for index in range(LOG_LAST_INDEX + 1):
        denominator = 2 * index + 1
        total_lower += floor_grid(2 * power[0] / denominator)
        total_upper += ceil_grid(2 * power[1] / denominator)
        power = (
            floor_grid(power[0] * t_squared[0]),
            ceil_grid(power[1] * t_squared[1]),
        )
    next_denominator = 2 * LOG_LAST_INDEX + 3
    tail_upper = ceil_grid(
        2 * power[1] / (next_denominator * (1 - t_squared[1]))
    )
    answer = floor_grid(total_lower), ceil_grid(total_upper + tail_upper)
    if not answer[0] <= answer[1]:
        raise AssertionError("invalid logarithm enclosure")
    return answer


LOG_TWO = atanh_log_unit_interval(Fraction(2))


def log_interval(value: Fraction) -> Interval:
    if value <= 0:
        raise AssertionError("logarithm of nonpositive value")
    exponent = 0
    reduced = value
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    unit = atanh_log_unit_interval(reduced)
    if exponent >= 0:
        return (
            floor_grid(unit[0] + exponent * LOG_TWO[0]),
            ceil_grid(unit[1] + exponent * LOG_TWO[1]),
        )
    return (
        floor_grid(unit[0] + exponent * LOG_TWO[1]),
        ceil_grid(unit[1] + exponent * LOG_TWO[0]),
    )


def exp_negative_interval(value: Fraction) -> Interval:
    """Alternating-Taylor enclosure of exp(-value), for 0 < value < 1."""
    if not Fraction(0) < value < Fraction(1):
        raise AssertionError("alternating exponential input outside (0,1)")
    value_interval = positive_grid_interval(value)
    term: Interval = (Fraction(1), Fraction(1))
    total: Interval = (Fraction(1), Fraction(1))
    odd_partial: Interval | None = None
    for order in range(1, EXP_ODD_ORDER + 2):
        term = (
            floor_grid(term[0] * value_interval[0] / order),
            ceil_grid(term[1] * value_interval[1] / order),
        )
        if order % 2:
            total = floor_grid(total[0] - term[1]), ceil_grid(total[1] - term[0])
            if order == EXP_ODD_ORDER:
                odd_partial = total
        else:
            total = floor_grid(total[0] + term[0]), ceil_grid(total[1] + term[1])
    if odd_partial is None:
        raise AssertionError("missing odd Taylor partial sum")
    # S_odd < exp(-x) < S_(odd+1), with interval arithmetic around each sum.
    answer = floor_grid(odd_partial[0]), ceil_grid(total[1])
    if not Fraction(0) < answer[0] <= answer[1] < 1:
        raise AssertionError("invalid exponential enclosure")
    return answer


def lower_weight(j_upper: Fraction) -> Fraction:
    log_upper = log_interval(j_upper)[1]
    exponent_upper = ceil_grid(S_LOWER * log_upper)
    return exp_negative_interval(exponent_upper)[0]


def upper_weight(j_lower: Fraction) -> Fraction:
    log_lower = log_interval(j_lower)[0]
    exponent_lower = floor_grid(S_UPPER * log_lower)
    return exp_negative_interval(exponent_lower)[1]


def exact_weight_pair(bounds: Interval) -> tuple[Fraction, Fraction]:
    return lower_weight(bounds[1]), upper_weight(bounds[0])


def float_perron_vector(
    edges: list[dict[str, object]], node_count: int, endpoint: str, s_value: Fraction
) -> list[int]:
    weights = [
        math.exp(-float(s_value) * math.log(float(edge[endpoint])))
        for edge in edges
    ]
    vector = [1.0 for _ in range(node_count)]
    for _ in range(4000):
        image = [0.0 for _ in range(node_count)]
        for edge, weight in zip(edges, weights):
            image[int(edge["source"])] += weight * vector[int(edge["target"])]
        scale = max(image)
        image = [entry / scale for entry in image]
        error = max(abs(left - right) for left, right in zip(image, vector))
        vector = image
        if error < 2.0e-15:
            break
    else:
        raise AssertionError("floating Perron-vector producer did not converge")
    integers = [max(1, int(round(value * VECTOR_DENOMINATOR))) for value in vector]
    divisor = math.gcd(*integers)
    return [entry // divisor for entry in integers]


def collatz_ratios(
    edges: list[dict[str, object]], node_count: int, vector: list[int], weight_key: str
) -> list[Fraction]:
    image = [Fraction(0) for _ in range(node_count)]
    for edge in edges:
        image[int(edge["source"])] += edge[weight_key] * vector[int(edge["target"])]
    return [image[index] / vector[index] for index in range(node_count)]


def build_payload() -> dict[str, object]:
    source_lock = {}
    for label, path in SOURCES.items():
        observed = sha256(path)
        if observed != EXPECTED_SOURCE_HASHES[label]:
            raise AssertionError(f"source-lock mismatch: {label}")
        source_lock[label] = {
            "path": path.relative_to(REPO_ROOT).as_posix(),
            "sha256": observed,
        }

    legacy_root = verified_legacy_root()
    if not S_LOWER < Fraction(legacy_root) < S_UPPER:
        raise AssertionError("legacy cutoff-20 root is not strictly inside the pressure bracket")

    nodes = admissible_words(WINDOW - 1)
    node_index = {word: index for index, word in enumerate(nodes)}
    edge_words = admissible_words(WINDOW)
    if (len(nodes), len(edge_words)) != (714, 1156):
        raise AssertionError("unexpected higher-block graph census")
    internal_edges: list[dict[str, object]] = []
    edge_records: list[dict[str, object]] = []
    fixed_rounds = 0
    minimum_j = None
    maximum_j = None
    maximum_width = Fraction(0)
    with concurrent.futures.ProcessPoolExecutor(max_workers=EXACT_WORKERS) as executor:
        interval_records = list(executor.map(direct_j_interval, edge_words, chunksize=8))
    for index, (word, interval_record) in enumerate(zip(edge_words, interval_records, strict=True)):
        jacobian, rounds = interval_record
        fixed_rounds = max(fixed_rounds, rounds)
        minimum_j = jacobian[0] if minimum_j is None else min(minimum_j, jacobian[0])
        maximum_j = jacobian[1] if maximum_j is None else max(maximum_j, jacobian[1])
        maximum_width = max(maximum_width, jacobian[1] - jacobian[0])
        source = node_index[word[:-1]]
        target = node_index[word[1:]]
        internal_edges.append(
            {
                "source": source,
                "target": target,
                "j_lower": jacobian[0],
                "j_upper": jacobian[1],
            }
        )
        edge_records.append(
            {
                "index": index,
                "word": "".join(str(state) for state in word),
                "source": source,
                "target": target,
                "signs": "".join("+" if sign > 0 else "-" for sign in edge_signs(word)),
                "jacobi_rounds": rounds,
                "j_lower": fraction_text(jacobian[0]),
                "j_upper": fraction_text(jacobian[1]),
            }
        )

    lower_vector = float_perron_vector(internal_edges, len(nodes), "j_upper", S_LOWER)
    upper_vector = float_perron_vector(internal_edges, len(nodes), "j_lower", S_UPPER)
    with concurrent.futures.ProcessPoolExecutor(max_workers=EXACT_WORKERS) as executor:
        weight_pairs = list(
            executor.map(
                exact_weight_pair,
                [(edge["j_lower"], edge["j_upper"]) for edge in internal_edges],
                chunksize=8,
            )
        )
    for edge, weights in zip(internal_edges, weight_pairs, strict=True):
        edge["lower_weight"], edge["upper_weight"] = weights
    lower_ratios = collatz_ratios(internal_edges, len(nodes), lower_vector, "lower_weight")
    upper_ratios = collatz_ratios(internal_edges, len(nodes), upper_vector, "upper_weight")
    collatz_min = min(lower_ratios)
    collatz_max = max(upper_ratios)
    if not collatz_min > 1:
        raise AssertionError("lower-endpoint Collatz inequality failed")
    if not collatz_max < 1:
        raise AssertionError("upper-endpoint Collatz inequality failed")

    return {
        "source_lock": source_lock,
        "protocol": {
            "map": "H_6(q,p)=(1-6q^2-p,q)",
            "state_names": list(STATE_NAMES),
            "state_pairs": [list(pair) for pair in STATE_PAIRS],
            "adjacency_source_rows_target_columns": [list(row) for row in ADJACENCY],
            "window_state_length": WINDOW,
            "center_radius": RADIUS,
            "signed_coordinate_order": "epsilon_-7,...,epsilon_6",
            "fixed_q_endpoints": [-7, 6],
            "jacobi_internal_coordinates": [-6, 5],
            "jacobi_round_cap": JACOBI_CAP,
            "sqrt_grid_denominator": GRID_DENOMINATOR,
            "transcendental_grid_denominator": GRID_DENOMINATOR,
            "log_series_last_index": LOG_LAST_INDEX,
            "exp_odd_order": EXP_ODD_ORDER,
            "adapted_slope_initial_interval": ["-1/2", "1/2"],
            "adapted_constants": {"r": "123/112", "gamma": "112/123", "J_min": "773/224"},
            "endpoint_s_lower": fraction_text(S_LOWER),
            "endpoint_s_upper": fraction_text(S_UPPER),
            "proof_arithmetic": "Fraction plus integer isqrt and outward 10^-50 grids",
            "floating_point_scope": "candidate Collatz vectors only; never trusted by checker",
            "fixed_exact_worker_count": EXACT_WORKERS,
        },
        "higher_block_graph": {
            "node_word_length": WINDOW - 1,
            "edge_word_length": WINDOW,
            "node_count": len(nodes),
            "edge_count": len(edge_words),
            "nodes": ["".join(str(state) for state in word) for word in nodes],
            "edges": edge_records,
            "maximum_jacobi_rounds_executed": fixed_rounds,
            "minimum_j_lower": fraction_text(minimum_j),
            "maximum_j_upper": fraction_text(maximum_j),
            "maximum_j_interval_width": fraction_text(maximum_width),
        },
        "pressure_certificate": {
            "lower_endpoint": {
                "s": fraction_text(S_LOWER),
                "matrix_weight": "lower enclosure of (J_edge_upper)^(-s)",
                "collatz_direction": "minimum row ratio > 1",
                "vector": lower_vector,
                "collatz_minimum": fraction_text(collatz_min),
                "strict_margin": fraction_text(collatz_min - 1),
            },
            "upper_endpoint": {
                "s": fraction_text(S_UPPER),
                "matrix_weight": "upper enclosure of (J_edge_lower)^(-s)",
                "collatz_direction": "maximum row ratio < 1",
                "vector": upper_vector,
                "collatz_maximum": fraction_text(collatz_max),
                "strict_margin": fraction_text(1 - collatz_max),
            },
            "certified_root_bracket": [fraction_text(S_LOWER), fraction_text(S_UPPER)],
            "decimal_bracket": ["0.277980", "0.277987"],
            "width": "7/1000000",
            "legacy_period20_high_precision_root": legacy_root,
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
        },
        "claims": {
            "all_W13_cylinders_enclosed": True,
            "chronological_higher_block_dynamics_preserved": True,
            "bowen_pressure_root_exists_uniquely_in_bracket": True,
            "pressure_status": "NUMERICALLY_CERTIFIED",
            "analytic_pressure_implication_status": "PROVED",
            "this_is_not_a_fredholm_or_hilbert_polya_certificate": True,
            "route_a_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "route_a_overall": "ROUTE_A_REJECTED",
        },
    }


def main() -> None:
    args = parse_args()
    payload = build_payload()
    certificate = {
        "schema": "hcs-c31-bowen-pressure-certificate-v2",
        "producer": "code/c31_producer.py",
        "payload": payload,
        "payload_sha256": canonical_sha256(payload),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    lower = payload["pressure_certificate"]["lower_endpoint"]["strict_margin"]
    upper = payload["pressure_certificate"]["upper_endpoint"]["strict_margin"]
    print(f"wrote {args.output}; exact Collatz margins lower={lower}, upper={upper}")


if __name__ == "__main__":
    main()
