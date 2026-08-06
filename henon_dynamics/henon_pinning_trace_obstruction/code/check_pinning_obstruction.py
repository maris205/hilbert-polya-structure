#!/usr/bin/env python3
"""Independent checker for the C02D exact obstruction certificate.

This file deliberately does not import the producer.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


F = Fraction
EXPECTED_STATES = ["--", "-+", "+-", "++"]
EXPECTED_EDGE_IDS = [
    "--->--",
    "--->+-",
    "-+->--",
    "+-->-+",
    "+-->++",
    "++->-+",
]
EXPECTED_PAIR_IDS = ["--", "-+", "+-", "++"]
EXPECTED_BOUNDARY_CENTERS = [F(763, 4608), F(773, 4608), F(1499, 4608)]
EXPECTED_MINIMA = [F(251, 4608), F(261, 4608), F(301, 4608)]
EXPECTED_MINIMIZERS = [-1, -1, 1]


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def frac(value: str) -> Fraction:
    return F(value)


def char(value: int) -> str:
    return "+" if value == 1 else "-"


def expected_edges() -> list[dict[str, Any]]:
    records = []
    for source in EXPECTED_STATES:
        s = 1 if source[0] == "+" else -1
        t = 1 if source[1] == "+" else -1
        for r in (-1, 1):
            if t == r == 1:
                continue
            target = char(r) + char(s)
            records.append(
                {
                    "id": source + "->" + target,
                    "source": source,
                    "target": target,
                    "branch_sign_s": s,
                    "outer_sign_t": t,
                    "terminal_sign_r": r,
                }
            )
    return records


def validate(certificate: dict[str, Any]) -> dict[str, bool]:
    checks: dict[str, bool] = {}
    checks["top_level_keys_exact"] = set(certificate) == {
        "schema",
        "payload",
        "payload_sha256",
        "all_checks_pass",
    }
    if not checks["top_level_keys_exact"] or not isinstance(certificate.get("payload"), dict):
        return checks

    payload = certificate["payload"]
    checks["schema_exact"] = certificate["schema"] == "henon-pinning-obstruction-certificate-v1"
    checks["payload_hash_exact"] = certificate["payload_sha256"] == hashlib.sha256(canonical_bytes(payload)).hexdigest()
    checks["producer_pass_flag_true"] = certificate["all_checks_pass"] is True
    checks["candidate_and_classification_exact"] = (
        payload.get("candidate_id") == "henon_h6_scalar_signed_pinning_v1"
        and payload.get("classification") == "C02D_NO_GO"
        and payload.get("clock") == "one chronological H_6 iterate"
    )
    checks["state_order_exact"] = payload.get("state_order") == EXPECTED_STATES

    edges = payload.get("edges", [])
    checks["edge_records_exact_and_ordered"] = edges == expected_edges()
    checks["edge_ids_exact"] = [record.get("id") for record in edges] == EXPECTED_EDGE_IDS

    cx, rx = F(23, 48), F(7, 48)
    cy, ry = F(121, 256), F(41, 256)
    domains = payload.get("domains", {})
    nesting_margin = ry - abs(cx - cy) - rx
    checks["domain_constants_exact"] = (
        frac(domains.get("x_center_abs", "0")) == cx
        and frac(domains.get("x_radius", "0")) == rx
        and frac(domains.get("y_center_abs", "0")) == cy
        and frac(domains.get("y_radius", "0")) == ry
        and frac(domains.get("x_compactly_in_y_margin", "0")) == nesting_margin == F(1, 128)
        and domains.get("local_enclosure_ratio") == "39/41"
    )

    pair_records = payload.get("radicand_pairs", [])
    independently_built_pairs = []
    common_radius = (ry + rx) / 6
    for t in (-1, 1):
        for r in (-1, 1):
            center = (1 - t * cy - r * cx) / 6
            independently_built_pairs.append(
                {
                    "pair_t_r": char(t) + char(r),
                    "allowed": not (t == r == 1),
                    "center": f"{center.numerator}/{center.denominator}",
                    "radius": f"{common_radius.numerator}/{common_radius.denominator}",
                    "disk_avoids_zero": abs(center) > common_radius,
                }
            )
    checks["radicand_records_exact_and_ordered"] = pair_records == independently_built_pairs
    checks["radicand_pair_ids_exact"] = [record.get("pair_t_r") for record in pair_records] == EXPECTED_PAIR_IDS
    checks["forbidden_control_crosses_zero"] = (
        frac(pair_records[-1]["center"]) <= frac(pair_records[-1]["radius"])
        if len(pair_records) == 4
        else False
    )
    checks["minimum_allowed_modulus_exact"] = frac(payload.get("minimum_allowed_radicand_modulus", "0")) == F(11, 96)

    boundary = payload.get("boundary_certificates", [])
    boundary_ok = len(boundary) == 3
    for index, record in enumerate(boundary):
        if index >= 3:
            boundary_ok = False
            break
        center = frac(record["center"])
        a_term = cx * cx - center
        q0 = a_term * a_term + 4 * cx * cx * rx * rx + rx**4 - 2 * a_term * rx * rx
        q1 = 4 * cx * rx * (a_term + rx * rx)
        q2 = 4 * a_term * rx * rx
        endpoint = EXPECTED_MINIMIZERS[index]
        minimum = abs((cx + endpoint * rx) ** 2 - center)
        gap = minimum - common_radius
        vertex = -q1 / (2 * q2)
        boundary_ok = boundary_ok and all(
            (
                center == EXPECTED_BOUNDARY_CENTERS[index],
                frac(record["q0"]) == q0,
                frac(record["q1"]) == q1,
                frac(record["q2"]) == q2,
                frac(record["vertex"]) == vertex,
                record["vertex_in_open_interval"] is False,
                record["minimizing_cos_theta"] == endpoint,
                frac(record["minimum_modulus"]) == minimum == EXPECTED_MINIMA[index],
                frac(record["gap"]) == gap > 0,
                record["shape_check"] is True,
                record["strict_gap"] is True,
                record["expected_minimum_match"] is True,
                record["center_root_in_target_by_squares"] is True,
                (cx - rx) ** 2 < center < (cx + rx) ** 2,
            )
        )
    checks["boundary_certificates_independent"] = boundary_ok
    checks["clearance_and_derivative_exact"] = (
        frac(payload.get("minimum_square_map_gap", "0")) == F(1, 288)
        and frac(payload.get("max_boundary_plus_image_modulus", "0")) == F(5, 4)
        and frac(payload.get("certified_image_clearance", "0")) == F(1, 360)
        and frac(payload.get("derivative_bound_squared", "0")) == F(2, 33)
        and payload.get("derivative_bound") == "2/sqrt(66)"
    )

    residue_records = payload.get("residue_tests", [])
    residue_ok = [record.get("id") for record in residue_records] == [
        "rational_sample_1",
        "rational_sample_2",
        "rational_sample_3",
    ]
    for record in residue_records:
        a, b, c, d = map(frac, record["a_b_c_d"])
        m00, m01, m10, m11 = a - b * c / d, b / d, -c / d, 1 / d
        det_i = (1 - m00) * (1 - m11) - m01 * m10
        det_r = (1 - a) * (1 - d) - b * c
        residue_ok = residue_ok and all(
            (
                det_r != 0,
                det_i != 0,
                det_r == -d * det_i,
                frac(record["det_residual"]) == det_r,
                frac(record["det_i_minus_m"]) == det_i,
                frac(record["raw_residue"]) == d / det_r,
                frac(record["target_residue"]) == 1 / det_i,
                d / det_r == -(1 / det_i),
                record["identity_det_residual_eq_minus_d_det_i_minus_m"] is True,
                record["raw_eq_minus_target"] is True,
                record["nonzero"] is True,
            )
        )
    checks["residue_records_independent"] = residue_ok

    repetition = payload.get("repetition_obstruction", {})
    checks["repetition_obstruction_exact"] = repetition == {
        "primitive_required_correction": -1,
        "double_repeat_multiplicative_correction": 1,
        "double_repeat_required_correction": -1,
        "ordinary_orbitwise_scalar_edge_cocycle_possible": False,
        "aggregate_trace_cancellation_ruled_out": False,
    }
    semantics = payload.get("window_semantics", {})
    checks["window_semantics_scoped_no_go"] = (
        semantics.get("identity") == "F^N(u,Q_1(u,v))=(Q_N(u,v),v)"
        and semantics.get("standard_exact_interpretations") == [
            "word kernel of L^N",
            "exact higher-block recoding",
        ]
        and semantics.get("one_step_infinite_memory_coefficient_present") is False
        and semantics.get("qualifies_as_frozen_L_bracket_N") is False
        and semantics.get("scope") == "standard BPS/Rugh pinning-kernel semantics only"
    )
    producer_checks = payload.get("checks", {})
    checks["producer_checks_complete_and_true"] = (
        len(producer_checks) == 14 and all(value is True for value in producer_checks.values())
    )
    firewall = payload.get("data_firewall", {})
    checks["data_firewall_closed"] = set(firewall) == {
        "prime_data_used",
        "riemann_zero_data_used",
        "target_spectrum_used",
        "operator_spectrum_computed",
        "averaged_transition_matrix_used",
    } and all(value is False for value in firewall.values())
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--json", action="store_true", help="emit compact JSON")
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    certificate = json.loads(raw)
    checks = validate(certificate)

    tamper_controls: dict[str, bool] = {}
    mutations = {}
    missing_edge = copy.deepcopy(certificate)
    missing_edge["payload"]["edges"].pop()
    mutations["missing_edge_rejected"] = missing_edge
    wrong_clearance = copy.deepcopy(certificate)
    wrong_clearance["payload"]["certified_image_clearance"] = "1/359"
    mutations["wrong_clearance_rejected"] = wrong_clearance
    false_scalar_repair = copy.deepcopy(certificate)
    false_scalar_repair["payload"]["repetition_obstruction"]["ordinary_orbitwise_scalar_edge_cocycle_possible"] = True
    mutations["false_orbitwise_scalar_repair_rejected"] = false_scalar_repair
    wrong_hash = copy.deepcopy(certificate)
    wrong_hash["payload_sha256"] = "0" * 64
    mutations["wrong_payload_hash_rejected"] = wrong_hash
    for name, mutated in mutations.items():
        tamper_controls[name] = not all(validate(mutated).values())

    all_checks_pass = all(checks.values()) and all(tamper_controls.values())
    output = {
        "schema": "henon-pinning-obstruction-independent-check-v1",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "payload_sha256": certificate.get("payload_sha256"),
        "checks": checks,
        "tamper_controls": tamper_controls,
        "all_checks_pass": all_checks_pass,
    }
    if args.json:
        print(json.dumps(output, sort_keys=True, separators=(",", ":")))
    else:
        print(json.dumps(output, sort_keys=True, indent=2))
    return 0 if all_checks_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
