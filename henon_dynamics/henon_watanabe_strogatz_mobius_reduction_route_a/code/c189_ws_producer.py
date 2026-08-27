#!/usr/bin/env python3
"""Produce the exact C189 Watanabe--Strogatz regression certificate."""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from math import isqrt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c189_ws_evidence.json"
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

Q = tuple[Fraction, Fraction]
ZERO: Q = (Fraction(0), Fraction(0))
ONE: Q = (Fraction(1), Fraction(0))
IUNIT: Q = (Fraction(0), Fraction(1))


def fs(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def q(re: int | Fraction = 0, im: int | Fraction = 0) -> Q:
    return Fraction(re), Fraction(im)


def qadd(a: Q, b: Q) -> Q:
    return a[0] + b[0], a[1] + b[1]


def qneg(a: Q) -> Q:
    return -a[0], -a[1]


def qsub(a: Q, b: Q) -> Q:
    return qadd(a, qneg(b))


def qmul(a: Q, b: Q) -> Q:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def qconj(a: Q) -> Q:
    return a[0], -a[1]


def qabs2(a: Q) -> Fraction:
    return a[0] * a[0] + a[1] * a[1]


def qdiv(a: Q, b: Q) -> Q:
    den = qabs2(b)
    if den == 0:
        raise ZeroDivisionError
    num = qmul(a, qconj(b))
    return num[0] / den, num[1] / den


def qscale(x: Fraction, a: Q) -> Q:
    return x * a[0], x * a[1]


def qjson(a: Q) -> list[str]:
    return [fs(a[0]), fs(a[1])]


def circle_point(t: Fraction) -> Q:
    den = 1 + t * t
    return (1 - t * t) / den, 2 * t / den


def cross_ratio(a: Q, b: Q, c: Q, d: Q) -> Q:
    return qdiv(qmul(qsub(a, c), qsub(b, d)), qmul(qsub(a, d), qsub(b, c)))


def mobius(z: Q, alpha: Q, rotation: Q) -> Q:
    return qdiv(qmul(rotation, qadd(z, alpha)), qadd(ONE, qmul(qconj(alpha), z)))


def ordered_unique(points: list[Q]) -> list[Q]:
    out: list[Q] = []
    for point in points:
        if point not in out:
            out.append(point)
    return out


def partition(points: list[Q]) -> list[int]:
    return sorted(Counter(points).values(), reverse=True)


def canonical_payload(data: dict) -> bytes:
    body = deepcopy(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def payload_hash(data: dict) -> str:
    return sha256(canonical_payload(data)).hexdigest()


def serialize(data: dict) -> bytes:
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


POINT_PARAMETERS = [
    Fraction(-4), Fraction(-2), Fraction(-1), Fraction(-1, 2),
    Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1),
    Fraction(3, 2), Fraction(3), Fraction(5),
]
POINTS = [circle_point(t) for t in POINT_PARAMETERS]

TRANSFORMS = [
    (q(0, 0), circle_point(Fraction(0))),
    (q(Fraction(1, 3), Fraction(1, 5)), circle_point(Fraction(1, 2))),
    (q(Fraction(-1, 4), Fraction(1, 6)), circle_point(Fraction(-2, 3))),
    (q(Fraction(2, 7), Fraction(-1, 7)), circle_point(Fraction(3, 4))),
]


def local_rows() -> list[dict]:
    frequencies = [Fraction(-3), Fraction(0), Fraction(5, 2)]
    forcings = [q(0, 0), q(1, 2), q(Fraction(-3, 2), Fraction(1, 3)), q(Fraction(5, 4), Fraction(-2, 3))]
    rows = []
    for fi, frequency in enumerate(frequencies):
        for hi, forcing in enumerate(forcings):
            for zi, z in enumerate(POINTS[:8]):
                phase_velocity = frequency + qmul(forcing, qconj(z))[1]
                phase_form = qmul(IUNIT, qscale(phase_velocity, z))
                riccati = qadd(
                    qscale(frequency, qmul(IUNIT, z)),
                    qscale(Fraction(1, 2), qsub(forcing, qmul(qconj(forcing), qmul(z, z)))),
                )
                tangent = qadd(qmul(qconj(z), riccati), qmul(z, qconj(riccati)))[0]
                rows.append({
                    "row_id": f"f{fi}_H{hi}_z{zi}",
                    "frequency_f": fs(frequency),
                    "forcing_H": qjson(forcing),
                    "circle_point_z": qjson(z),
                    "phase_velocity": fs(phase_velocity),
                    "riccati_velocity": qjson(riccati),
                    "phase_to_riccati_residual": qjson(qsub(phase_form, riccati)),
                    "circle_tangent_residual": fs(tangent),
                    "circle_equation_residual": fs(qabs2(z) - 1),
                })
    return rows


def action_row(row_id: str, points: list[Q], alpha: Q, rotation: Q, kind: str) -> dict:
    images = [mobius(z, alpha, rotation) for z in points]
    reps = ordered_unique(points)
    image_reps = [mobius(z, alpha, rotation) for z in reps]
    invariants = []
    if len(reps) >= 4:
        for j in range(3, len(reps)):
            before = cross_ratio(reps[j], reps[0], reps[1], reps[2])
            after = cross_ratio(image_reps[j], image_reps[0], image_reps[1], image_reps[2])
            invariants.append({
                "cluster_index": j,
                "initial_value": fs(before[0]),
                "image_value": fs(after[0]),
                "initial_imaginary_residual": fs(before[1]),
                "image_imaginary_residual": fs(after[1]),
            })
    first_indices = [points.index(rep) for rep in reps[:3]] if len(reps) >= 3 else []
    coeffs = [rotation, qmul(rotation, alpha), qconj(alpha), ONE]
    return {
        "row_id": row_id,
        "kind": kind,
        "N": len(points),
        "alpha": qjson(alpha),
        "rotation": qjson(rotation),
        "alpha_disk_margin": fs(1 - qabs2(alpha)),
        "projective_coefficients_a_b_c_d": [qjson(x) for x in coeffs],
        "initial_points": [qjson(x) for x in points],
        "image_points": [qjson(x) for x in images],
        "initial_circle_residuals": [fs(qabs2(x) - 1) for x in points],
        "image_circle_residuals": [fs(qabs2(x) - 1) for x in images],
        "initial_collision_partition": partition(points),
        "image_collision_partition": partition(images),
        "distinct_clusters": len(reps),
        "group_orbit_dimension": min(len(reps), 3),
        "quotient_invariant_count": max(len(reps) - 3, 0),
        "landmark_indices": first_indices,
        "three_landmark_reconstruction": len(reps) >= 3,
        "cross_ratio_invariants": invariants,
    }


def action_rows() -> list[dict]:
    rows = []
    for map_index, (alpha, rotation) in enumerate(TRANSFORMS):
        assert qabs2(alpha) < 1 and qabs2(rotation) == 1
        for n in range(4, 11):
            rows.append(action_row(f"generic_N{n}_map{map_index}", POINTS[:n], alpha, rotation, "generic"))
        strata = {
            "sync": [8],
            "two_cluster": [4, 4],
            "three_cluster": [3, 3, 2],
            "four_cluster": [3, 2, 2, 1],
            "six_cluster": [2, 2, 1, 1, 1, 1],
        }
        for name, counts in strata.items():
            points = [POINTS[i] for i, count in enumerate(counts) for _ in range(count)]
            rows.append(action_row(f"stratum_{name}_map{map_index}", points, alpha, rotation, "collision_stratum"))
    return rows


CONSTANT_CASES = [
    ("identity", Fraction(0), q(0, 0)),
    ("elliptic_real", Fraction(5), q(3, 0)),
    ("elliptic_complex_positive", Fraction(13), q(3, 4)),
    ("elliptic_complex_negative", Fraction(-13), q(3, 4)),
    ("parabolic_positive", Fraction(5), q(3, 4)),
    ("parabolic_negative", Fraction(-5), q(3, 4)),
    ("hyperbolic_real", Fraction(3), q(5, 0)),
    ("hyperbolic_complex", Fraction(-3), q(4, 3)),
]


def exact_square_root(value: Fraction) -> Fraction:
    if value < 0:
        raise ValueError(value)
    rn, rd = isqrt(value.numerator), isqrt(value.denominator)
    if rn * rn != value.numerator or rd * rd != value.denominator:
        raise ValueError(f"not a rational square: {value}")
    return Fraction(rn, rd)


def constant_rows() -> list[dict]:
    rows = []
    for name, omega, forcing in CONSTANT_CASES:
        delta = omega * omega - qabs2(forcing)
        roots: list[Q] = []
        period: str | None = None
        if omega == 0 and forcing == ZERO:
            kind = "identity"
            boundary_fixed_count: int | str = "all"
        elif delta > 0:
            kind = "elliptic"
            nu = exact_square_root(delta)
            roots = [qdiv(q(0, omega + sign * nu), qconj(forcing)) for sign in (1, -1)]
            period = fs(Fraction(2, 1) / nu)
            boundary_fixed_count = 0
        elif delta == 0:
            kind = "parabolic"
            roots = [qdiv(q(0, omega), qconj(forcing))]
            boundary_fixed_count = 1
        else:
            kind = "hyperbolic"
            kappa = exact_square_root(-delta)
            roots = [qdiv(q(sign * kappa, omega), qconj(forcing)) for sign in (1, -1)]
            boundary_fixed_count = 2
        root_rows = []
        for root in roots:
            polynomial = qsub(qsub(qmul(qconj(forcing), qmul(root, root)), qscale(2 * omega, qmul(IUNIT, root))), forcing)
            root_rows.append({
                "z": qjson(root),
                "modulus_square": fs(qabs2(root)),
                "fixed_polynomial_residual": qjson(polynomial),
            })
        rows.append({
            "case_id": name,
            "omega": fs(omega),
            "H": qjson(forcing),
            "delta_equals_omega2_minus_absH2": fs(delta),
            "generator_square_scalar": fs(-delta / 4),
            "classification": kind,
            "boundary_fixed_point_count": boundary_fixed_count,
            "fixed_roots": root_rows,
            "elliptic_projective_period_pi_coefficient": period,
        })
    return rows


def build_evidence() -> dict:
    local = local_rows()
    actions = action_rows()
    constants = constant_rows()
    cross_ratio_cells = sum(len(row["cross_ratio_invariants"]) for row in actions)
    reconstruction_rows = sum(bool(row["three_landmark_reconstruction"]) for row in actions)
    circle_residual_cells = sum(len(row["initial_points"]) + len(row["image_points"]) for row in actions)
    data = {
        "schema": "hcs-c189-ws-mobius-v1",
        "metadata": {
            "candidate_id": "HCS-C189",
            "evaluation_date": "2026-08-27",
            "source_commit": SOURCE_COMMIT,
            "scope_literal": SCOPE,
            "precision": "exact rational complex arithmetic",
            "training_data": "none",
            "target_tables_used": 0,
            "primary_sources": [
                {"authors": "Watanabe--Strogatz", "doi": "10.1016/0167-2789(94)90196-1", "role": "original constants-of-motion reduction"},
                {"authors": "Marvel--Mirollo--Strogatz", "doi": "10.1063/1.3247089", "arxiv": "0904.1680", "role": "Mobius group action"},
                {"authors": "Pikovsky--Rosenblum", "doi": "10.1103/PhysRevLett.101.264103", "role": "partial integrability"},
            ],
        },
        "theorem": {
            "family": "all N>=3 and all continuous common f:I->R, H:I->C",
            "phase_equation": "theta_dot_j=f(t)+Im(H(t)*exp(-i*theta_j))",
            "riccati_equation": "z_dot=i*f*z+(H-conj(H)*z^2)/2",
            "lift": "G_dot=A(t)G with A=(1/2)[[if,H],[conj(H),-if]] in su(1,1)",
            "projective_action": "M(z)=(a*z+b)/(conj(b)*z+conj(a))=exp(i*psi)*(z+alpha)/(1+conj(alpha)*z)",
            "generic_invariants": "N-3 independent real cross ratios [z_j,z_1;z_2,z_3], j=4,...,N",
            "collision_strata": "the labelled collision partition is invariant; orbit dimension is 1,2,3 for 1,2,at least 3 distinct clusters",
            "constant_classification": "identity separately; Delta=omega^2-|H|^2 positive elliptic, zero nonzero parabolic, negative hyperbolic",
            "elliptic_projective_period": "2*pi/sqrt(omega^2-|H|^2)",
            "ordinary_zeta_boundary": "rational elliptic strobes fix positive-dimensional configuration strata",
        },
        "local_riccati_rows": local,
        "mobius_action_rows": actions,
        "constant_generator_rows": constants,
        "route_a": {
            "A0": "A0_FAIL",
            "A1": "A1_WEAK",
            "A2": "A2_FAIL",
            "A3": "A3_FAIL",
            "A4": "A4_FORMAL_HINT",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "qualification": "exact PSU(1,1) reduction and clean periodic families have no intrinsic rational-prime origin, logarithmic prime clock, or target divisor",
        },
        "summary": {
            "local_riccati_rows": len(local),
            "mobius_action_rows": len(actions),
            "generic_configuration_rows": sum(row["kind"] == "generic" for row in actions),
            "collision_stratum_rows": sum(row["kind"] == "collision_stratum" for row in actions),
            "cross_ratio_cells": cross_ratio_cells,
            "three_landmark_reconstruction_rows": reconstruction_rows,
            "circle_residual_cells": circle_residual_cells,
            "constant_generator_rows": len(constants),
            "all_parameter_theorem_status": "PROVED_IN_THEOREM_PACKAGE",
            "finite_rows_role": "REGRESSION_ONLY",
        },
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    data = build_evidence()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(serialize(data))
    print(json.dumps({
        "status": "C189_PRODUCER_PASS",
        **data["summary"],
        "payload_sha256": data["payload_sha256"],
        "evidence_sha256": sha256(OUTPUT.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
