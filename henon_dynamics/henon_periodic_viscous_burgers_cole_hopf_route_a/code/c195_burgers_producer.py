#!/usr/bin/env python3
"""Produce the exact C195 periodic viscous-Burgers regression certificate."""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c195_burgers_evidence.json"
SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

C = tuple[Fraction, Fraction]
Laurent = dict[int, C]
ZERO: C = (Fraction(0), Fraction(0))
ONE: C = (Fraction(1), Fraction(0))
IUNIT: C = (Fraction(0), Fraction(1))


def fs(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def cj(value: C) -> list[str]:
    return [fs(value[0]), fs(value[1])]


def c(re: int | Fraction = 0, im: int | Fraction = 0) -> C:
    return Fraction(re), Fraction(im)


def add(left: C, right: C) -> C:
    return left[0] + right[0], left[1] + right[1]


def mul(left: C, right: C) -> C:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def conj(value: C) -> C:
    return value[0], -value[1]


def scale(factor: Fraction, value: C) -> C:
    return factor * value[0], factor * value[1]


def cpow(value: C, exponent: int) -> C:
    if exponent < 0:
        return cpow(conj(value), -exponent)
    answer = ONE
    base = value
    power = exponent
    while power:
        if power & 1:
            answer = mul(answer, base)
        base = mul(base, base)
        power //= 2
    return answer


def circle(parameter: Fraction) -> C:
    denominator = 1 + parameter * parameter
    return (1 - parameter * parameter) / denominator, 2 * parameter / denominator


def clean(poly: Laurent) -> Laurent:
    return {mode: value for mode, value in poly.items() if value != ZERO}


def poly_add(left: Laurent, right: Laurent) -> Laurent:
    answer = dict(left)
    for mode, value in right.items():
        answer[mode] = add(answer.get(mode, ZERO), value)
    return clean(answer)


def poly_scale(factor: Fraction, poly: Laurent) -> Laurent:
    return clean({mode: scale(factor, value) for mode, value in poly.items()})


def poly_mul(left: Laurent, right: Laurent) -> Laurent:
    answer: Laurent = {}
    for left_mode, left_value in left.items():
        for right_mode, right_value in right.items():
            mode = left_mode + right_mode
            answer[mode] = add(answer.get(mode, ZERO), mul(left_value, right_value))
    return clean(answer)


def derivative(poly: Laurent) -> Laurent:
    return clean({mode: mul(c(0, mode), value) for mode, value in poly.items()})


def drift_heat_generator(poly: Laurent, nu: Fraction, mean: Fraction) -> Laurent:
    first = derivative(poly)
    second = derivative(first)
    return poly_add(poly_scale(nu, second), poly_scale(-mean, first))


def generator_residual(poly: Laurent, nu: Fraction, mean: Fraction) -> Laurent:
    """Numerator of u_t+u*u_x-nu*u_xx after multiplying by w^3."""
    first = derivative(poly)
    second = derivative(first)
    third = derivative(second)
    temporal = drift_heat_generator(poly, nu, mean)
    first_temporal = derivative(temporal)

    atw_minus_awt = poly_add(poly_mul(first_temporal, poly), poly_scale(-1, poly_mul(first, temporal)))
    term_time = poly_scale(-2 * nu, poly_mul(atw_minus_awt, poly))

    mw_minus_2nua = poly_add(poly_scale(mean, poly), poly_scale(-2 * nu, first))
    bw_minus_a2 = poly_add(poly_mul(second, poly), poly_scale(-1, poly_mul(first, first)))
    term_transport = poly_scale(-2 * nu, poly_mul(mw_minus_2nua, bw_minus_a2))

    cubic = poly_add(
        poly_add(poly_mul(poly_mul(third, poly), poly), poly_scale(-3, poly_mul(poly_mul(first, second), poly))),
        poly_scale(2, poly_mul(poly_mul(first, first), first)),
    )
    term_viscosity = poly_scale(2 * nu * nu, cubic)
    return poly_add(poly_add(term_time, term_transport), term_viscosity)


def transform(poly: Laurent, rho: Fraction, rotation: C) -> Laurent:
    return clean({
        mode: scale(rho ** (mode * mode), mul(cpow(rotation, mode), value))
        for mode, value in poly.items()
    })


def serialize_poly(poly: Laurent) -> list[dict]:
    return [{"mode": mode, "coefficient": cj(poly[mode])} for mode in sorted(poly)]


def l1_positive_margin(poly: Laurent) -> Fraction:
    constant = poly[0][0]
    return constant - sum(abs(value[0]) + abs(value[1]) for mode, value in poly.items() if mode != 0)


def make_case(case_index: int) -> tuple[Fraction, Fraction, Laurent]:
    viscosities = [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1), Fraction(3, 2), Fraction(2)]
    means = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(1, 2), Fraction(3, 2), Fraction(3)]
    nu = viscosities[case_index % len(viscosities)]
    mean = means[(5 * case_index + 1) % len(means)]
    first_mode = 1 + case_index % 4
    positive_modes = [first_mode, first_mode + 2] if case_index % 2 == 0 else [first_mode, first_mode + 1, first_mode + 3]
    poly: Laurent = {0: c(5 + case_index % 4)}
    for slot, mode in enumerate(positive_modes):
        real = Fraction(1 + (case_index + 2 * slot) % 4, 20 + mode + case_index % 3)
        imag = Fraction(((case_index + mode + slot) % 5) - 2, 31 + mode + slot)
        coefficient = c(real, imag)
        poly[mode] = coefficient
        poly[-mode] = conj(coefficient)
    assert l1_positive_margin(poly) > 0
    return nu, mean, poly


def canonical_payload(data: dict) -> bytes:
    body = deepcopy(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def payload_hash(data: dict) -> str:
    return sha256(canonical_payload(data)).hexdigest()


def serialize(data: dict) -> bytes:
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def case_rows() -> list[dict]:
    rho_values = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(4, 5)]
    rotation_parameters = [Fraction(0), Fraction(1, 2), Fraction(-1, 3), Fraction(2, 3)]
    second_rhos = [Fraction(1, 3), Fraction(3, 5), Fraction(5, 7)]
    second_rotation_parameters = [Fraction(1, 4), Fraction(-2, 5), Fraction(3, 7)]
    rows: list[dict] = []
    for case_index in range(24):
        nu, mean, poly = make_case(case_index)
        rho = rho_values[case_index % len(rho_values)]
        rotation = circle(rotation_parameters[case_index % len(rotation_parameters)])
        rho_second = second_rhos[case_index % len(second_rhos)]
        rotation_second = circle(second_rotation_parameters[case_index % len(second_rotation_parameters)])
        first_snapshot = transform(poly, rho, rotation)
        composed_snapshot = transform(first_snapshot, rho_second, rotation_second)
        direct_snapshot = transform(poly, rho * rho_second, mul(rotation, rotation_second))
        residual = generator_residual(poly, nu, mean)
        active_modes = sorted(mode for mode in poly if mode > 0)
        first_mode = active_modes[0]
        next_mode = active_modes[1]
        leading: Laurent = {}
        for mode in (-first_mode, first_mode):
            differentiated = mul(c(0, mode), poly[mode])
            leading[mode] = scale(-2 * nu / poly[0][0], differentiated)
        spectrum = [
            {
                "mode": mode,
                "eigenvalue": cj(c(-nu * mode * mode, -mean * mode)),
                "fixed_mean_leaf": mode != 0,
            }
            for mode in range(-8, 9)
        ]
        rows.append({
            "case_id": f"trig_{case_index:02d}",
            "normalization": "L=2*pi; Fourier basis exp(i*k*x)",
            "nu": fs(nu),
            "mean_m": fs(mean),
            "initial_coefficients": serialize_poly(poly),
            "reality_residual_cells": [
                cj(add(poly[-mode], scale(-1, conj(poly[mode])))) for mode in active_modes
            ],
            "strict_positive_l1_margin": fs(l1_positive_margin(poly)),
            "generator_residual_coefficients": serialize_poly(residual),
            "snapshot_parameters": {"rho": fs(rho), "rotation": cj(rotation)},
            "snapshot_coefficients": serialize_poly(first_snapshot),
            "snapshot_strict_positive_l1_margin": fs(l1_positive_margin(first_snapshot)),
            "second_snapshot_parameters": {"rho": fs(rho_second), "rotation": cj(rotation_second)},
            "composed_snapshot_coefficients": serialize_poly(composed_snapshot),
            "direct_composed_snapshot_coefficients": serialize_poly(direct_snapshot),
            "semigroup_composition_residual_coefficients": serialize_poly(poly_add(composed_snapshot, poly_scale(-1, direct_snapshot))),
            "first_active_mode": first_mode,
            "next_active_mode": next_mode,
            "leading_u_minus_m_coefficients": serialize_poly(leading),
            "exact_decay_exponent": fs(nu * first_mode * first_mode),
            "certified_remainder_exponent": fs(min(2 * nu * first_mode * first_mode, nu * next_mode * next_mode)),
            "linearized_spectrum": spectrum,
        })
    return rows


def build_evidence() -> dict:
    rows = case_rows()
    data = {
        "schema": "hcs-c195-periodic-burgers-v1",
        "metadata": {
            "candidate_id": "HCS-C195",
            "evaluation_date": "2026-08-27",
            "source_commit": SOURCE_COMMIT,
            "scope_literal": SCOPE,
            "evaluator_sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
            "target_tables_used": 0,
            "primary_sources": [
                {
                    "authors": "Eberhard Hopf",
                    "title": "The partial differential equation u_t + u u_x = mu u_xx",
                    "doi": "10.1002/cpa.3160030302",
                    "role": "classical transformation and viscous Burgers analysis",
                },
                {
                    "authors": "Julian D. Cole",
                    "title": "On a quasi-linear parabolic equation occurring in aerodynamics",
                    "journal": "Quarterly of Applied Mathematics 9 (1951), 225--236",
                    "jstor": "43633894",
                    "role": "classical Cole transformation",
                },
            ],
        },
        "theorem": {
            "phase_leaf": "X_m^s={u in H^s(T_L;R):mean(u)=m}, s>3/2, nu>0, L>0",
            "positive_projective_cone": "P_+^{s+1}={w in H^{s+1}(T_L;R):min(w)>0}/R_{>0}",
            "cole_hopf_map": "Phi_m([w])=m-2*nu*d_x(log w)",
            "inverse": "[w]=[exp(-V/(2*nu))], V_x=u-m, mean(V)=0",
            "autonomous_conjugacy": "S_t Phi_m([w])=Phi_m([exp(t*(nu*d_x^2-m*d_x))w])",
            "galilean_heat_relation": "K_t w(x)=(exp(nu*t*d_x^2)w)(x-m*t)",
            "algebraic_snapshot_oracle": "rational (rho,zeta) rows probe the universal two-parameter heat/translation multiplier; the physical one-parameter curve rho=exp(-nu*t), zeta=exp(-i*m*t) is included analytically, but a rational sentinel need not lie on that curve",
            "asymptotic_exponent": "nu*(2*pi*r/L)^2 for the first nonzero Fourier mode r of the positive Cole-Hopf representative",
            "linearized_spectrum": "lambda_k=-nu*(2*pi*k/L)^2-i*m*(2*pi*k/L), k in Z; omit k=0 on X_m^s",
            "recurrence": "the only equilibrium, periodic point, or recurrent point on X_m^s is u identically m",
        },
        "regression_rows": rows,
        "route_a": {
            "A0": "A0_FAIL",
            "A1": "A1_FAIL",
            "A2": "A2_FAIL",
            "A3": "A3_FAIL",
            "A4": "A4_FORMAL_HINT",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "qualification": "the positive projective heat lift is a source PDE linearization with no intrinsic rational-prime carrier, periodic-orbit divisor, target analytic structure, or Hilbert--Polya semantics",
        },
        "summary": {
            "regression_cases": len(rows),
            "generator_residual_rows": sum(not row["generator_residual_coefficients"] for row in rows),
            "reality_residual_cells": sum(len(row["reality_residual_cells"]) for row in rows),
            "positive_margin_rows": sum(Fraction(row["strict_positive_l1_margin"]) > 0 for row in rows),
            "snapshot_positive_margin_rows": sum(Fraction(row["snapshot_strict_positive_l1_margin"]) > 0 for row in rows),
            "semigroup_identity_rows": sum(not row["semigroup_composition_residual_coefficients"] for row in rows),
            "leading_mode_rows": len(rows),
            "linear_spectrum_cells": sum(len(row["linearized_spectrum"]) for row in rows),
            "all_parameter_theorem_status": "PROVED_IN_THEOREM_PACKAGE",
            "finite_rows_role": "REGRESSION_ONLY_NOT_PROOF",
        },
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    data = build_evidence()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(serialize(data))
    print(json.dumps({
        "status": "C195_PRODUCER_PASS",
        **data["summary"],
        "payload_sha256": data["payload_sha256"],
        "evidence_sha256": sha256(OUTPUT.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
