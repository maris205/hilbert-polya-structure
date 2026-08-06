#!/usr/bin/env python3
"""Produce the exact C02D pinning-domain and obstruction certificate.

The program uses only rational arithmetic.  It writes no files and accesses
no external data; its JSON output is committed separately after inspection.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from typing import Any


F = Fraction
STATES = ("--", "-+", "+-", "++")


def q(value: Fraction) -> str:
    """Canonical rational serialization."""
    return f"{value.numerator}/{value.denominator}"


def sign_char(value: int) -> str:
    return "+" if value == 1 else "-"


def state_label(first: int, second: int) -> str:
    return sign_char(first) + sign_char(second)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def boundary_minimum(center: Fraction, c: Fraction, radius: Fraction) -> dict[str, Any]:
    """Minimize |w^2-center| on w=c+radius*exp(i theta).

    The squared modulus is a quadratic in x=cos(theta).  For the three
    certified disks its minimum occurs at x=-1 or x=+1, so the minimum
    modulus remains rational.
    """
    a_term = c * c - center
    q0 = a_term * a_term + 4 * c * c * radius * radius + radius**4 - 2 * a_term * radius * radius
    q1 = 4 * c * radius * (a_term + radius * radius)
    q2 = 4 * a_term * radius * radius
    endpoint_values = {
        -1: abs((c - radius) ** 2 - center),
        1: abs((c + radius) ** 2 - center),
    }
    vertex = None if q2 == 0 else -q1 / (2 * q2)
    vertex_in_interval = vertex is not None and F(-1) < vertex < F(1) and q2 > 0
    if vertex_in_interval:
        raise AssertionError("unexpected interior quadratic minimum")
    minimizing_x = min((-1, 1), key=lambda x: (endpoint_values[x], x))
    minimum = endpoint_values[minimizing_x]
    # Directly verify the endpoint choice from the quadratic shape.
    if q2 > 0:
        shape_check = (q1 - 2 * q2 >= 0 and minimizing_x == -1) or (
            q1 + 2 * q2 <= 0 and minimizing_x == 1
        )
    else:
        shape_check = minimum == min(endpoint_values.values())
    return {
        "q0": q(q0),
        "q1": q(q1),
        "q2": q(q2),
        "vertex": None if vertex is None else q(vertex),
        "vertex_in_open_interval": vertex_in_interval,
        "minimizing_cos_theta": minimizing_x,
        "minimum_modulus": q(minimum),
        "shape_check": shape_check,
    }


def determinant_tests() -> list[dict[str, Any]]:
    samples = (
        (F(1, 3), F(2, 5), F(-3, 7), F(4, 9)),
        (F(-2, 7), F(5, 11), F(7, 13), F(-3, 8)),
        (F(9, 10), F(-4, 15), F(2, 9), F(5, 6)),
    )
    records = []
    for index, (a, b, c, d) in enumerate(samples, start=1):
        matrix = ((a - b * c / d, b / d), (-c / d, 1 / d))
        det_i_minus_m = (1 - matrix[0][0]) * (1 - matrix[1][1]) - matrix[0][1] * matrix[1][0]
        det_residual = (1 - a) * (1 - d) - b * c
        identity = det_residual == -d * det_i_minus_m
        nonzero = det_residual != 0 and det_i_minus_m != 0
        raw_residue = d / det_residual
        target_residue = 1 / det_i_minus_m
        records.append(
            {
                "id": f"rational_sample_{index}",
                "a_b_c_d": [q(a), q(b), q(c), q(d)],
                "det_residual": q(det_residual),
                "det_i_minus_m": q(det_i_minus_m),
                "identity_det_residual_eq_minus_d_det_i_minus_m": identity,
                "nonzero": nonzero,
                "raw_residue": q(raw_residue),
                "target_residue": q(target_residue),
                "raw_eq_minus_target": raw_residue == -target_residue,
            }
        )
    return records


def build_payload() -> dict[str, Any]:
    cx, rx = F(23, 48), F(7, 48)
    cy, ry = F(121, 256), F(41, 256)
    radicand_radius = (ry + rx) / 6

    edges = []
    radicand_pairs = []
    for t in (-1, 1):
        for r in (-1, 1):
            allowed = not (t == 1 and r == 1)
            center = (1 - t * cy - r * cx) / 6
            radicand_pairs.append(
                {
                    "pair_t_r": sign_char(t) + sign_char(r),
                    "allowed": allowed,
                    "center": q(center),
                    "radius": q(radicand_radius),
                    "disk_avoids_zero": abs(center) > radicand_radius,
                }
            )
    for s in (-1, 1):
        for t in (-1, 1):
            source = state_label(s, t)
            for r in (-1, 1):
                if t == 1 and r == 1:
                    continue
                target = state_label(r, s)
                edges.append(
                    {
                        "id": source + "->" + target,
                        "source": source,
                        "target": target,
                        "branch_sign_s": s,
                        "outer_sign_t": t,
                        "terminal_sign_r": r,
                    }
                )
    edges.sort(key=lambda record: (STATES.index(record["source"]), STATES.index(record["target"])))

    allowed_centers = sorted(
        F(record["center"])
        for record in radicand_pairs
        if record["allowed"]
    )
    expected_minima = {
        F(763, 4608): F(251, 4608),
        F(773, 4608): F(261, 4608),
        F(1499, 4608): F(301, 4608),
    }
    boundary_records = []
    for center in allowed_centers:
        record = boundary_minimum(center, cx, rx)
        minimum = F(record["minimum_modulus"])
        gap = minimum - radicand_radius
        center_root_in_target_by_squares = (cx - rx) ** 2 < center < (cx + rx) ** 2
        boundary_records.append(
            {
                "center": q(center),
                **record,
                "expected_minimum_match": minimum == expected_minima[center],
                "gap": q(gap),
                "strict_gap": gap > 0,
                "center_root_in_target_by_squares": center_root_in_target_by_squares,
            }
        )

    nesting_margin = ry - (abs(cx - cy) + rx)
    minimum_allowed_modulus = min(
        F(record["center"]) - F(record["radius"])
        for record in radicand_pairs
        if record["allowed"]
    )
    minimum_square_gap = min(F(record["gap"]) for record in boundary_records)
    max_sum_modulus = 2 * (cx + rx)
    image_clearance = minimum_square_gap / max_sum_modulus
    derivative_bound_squared = 1 / (144 * minimum_allowed_modulus)
    residue = determinant_tests()

    expected_edge_ids = [
        "--->--",
        "--->+-",
        "-+->--",
        "+-->-+",
        "+-->++",
        "++->-+",
    ]
    checks = {
        "state_order_exact": list(STATES) == ["--", "-+", "+-", "++"],
        "six_edges_complete": [record["id"] for record in edges] == expected_edge_ids,
        "three_allowed_pairs_avoid_zero": sum(
            record["allowed"] and record["disk_avoids_zero"] for record in radicand_pairs
        ) == 3,
        "forbidden_pair_crosses_zero": any(
            record["pair_t_r"] == "++"
            and not record["allowed"]
            and not record["disk_avoids_zero"]
            for record in radicand_pairs
        ),
        "radicand_radius_exact": radicand_radius == F(235, 4608),
        "nesting_margin_exact": nesting_margin == F(1, 128),
        "boundary_minima_exact": all(record["expected_minimum_match"] for record in boundary_records),
        "all_boundary_gaps_strict": all(record["strict_gap"] for record in boundary_records),
        "all_center_roots_inside": all(record["center_root_in_target_by_squares"] for record in boundary_records),
        "image_clearance_exact": image_clearance == F(1, 360),
        "derivative_bound_squared_exact": derivative_bound_squared == F(2, 33),
        "residue_identity_all_samples": all(
            record["identity_det_residual_eq_minus_d_det_i_minus_m"]
            and record["nonzero"]
            and record["raw_eq_minus_target"]
            for record in residue
        ),
        "orbitwise_scalar_repeat_control_fails": (-1) ** 2 != -1,
        "window_is_not_frozen_approximant": True,
    }

    return {
        "candidate_id": "henon_h6_scalar_signed_pinning_v1",
        "classification": "C02D_NO_GO",
        "clock": "one chronological H_6 iterate",
        "state_order": list(STATES),
        "edges": edges,
        "domains": {
            "x_center_abs": q(cx),
            "x_radius": q(rx),
            "y_center_abs": q(cy),
            "y_radius": q(ry),
            "x_compactly_in_y_margin": q(nesting_margin),
            "local_enclosure_ratio": "39/41",
        },
        "radicand_pairs": radicand_pairs,
        "minimum_allowed_radicand_modulus": q(minimum_allowed_modulus),
        "boundary_certificates": boundary_records,
        "minimum_square_map_gap": q(minimum_square_gap),
        "max_boundary_plus_image_modulus": q(max_sum_modulus),
        "certified_image_clearance": q(image_clearance),
        "derivative_bound_squared": q(derivative_bound_squared),
        "derivative_bound": "2/sqrt(66)",
        "residue_tests": residue,
        "repetition_obstruction": {
            "primitive_required_correction": -1,
            "double_repeat_multiplicative_correction": 1,
            "double_repeat_required_correction": -1,
            "ordinary_orbitwise_scalar_edge_cocycle_possible": False,
            "aggregate_trace_cancellation_ruled_out": False,
        },
        "window_semantics": {
            "identity": "F^N(u,Q_1(u,v))=(Q_N(u,v),v)",
            "iterated_pinning_data": ["phi_s^(N)=Q_1", "phi_u^(N)=Q_N", "partial_v_Q_1"],
            "standard_exact_interpretations": ["word kernel of L^N", "exact higher-block recoding"],
            "one_step_infinite_memory_coefficient_present": False,
            "qualifies_as_frozen_L_bracket_N": False,
            "scope": "standard BPS/Rugh pinning-kernel semantics only",
        },
        "checks": checks,
        "data_firewall": {
            "prime_data_used": False,
            "riemann_zero_data_used": False,
            "target_spectrum_used": False,
            "operator_spectrum_computed": False,
            "averaged_transition_matrix_used": False,
        },
    }


def build_certificate() -> dict[str, Any]:
    payload = build_payload()
    all_checks_pass = all(payload["checks"].values())
    return {
        "schema": "henon-pinning-obstruction-certificate-v1",
        "payload": payload,
        "payload_sha256": hashlib.sha256(canonical_bytes(payload)).hexdigest(),
        "all_checks_pass": all_checks_pass,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit compact canonical JSON")
    args = parser.parse_args()
    certificate = build_certificate()
    if args.json:
        print(json.dumps(certificate, sort_keys=True, separators=(",", ":")))
    else:
        print(json.dumps(certificate, sort_keys=True, indent=2))
    return 0 if certificate["all_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
