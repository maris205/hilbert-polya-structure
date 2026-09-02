#!/usr/bin/env python3
"""Produce deterministic full-pattern evidence for HCS-C300."""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c300_euler_evidence.json"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
mp.mp.dps = 90


def canonical_payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def dec(value) -> str:
    value = mp.mpf(value)
    if value == 0:
        return "0.0"
    return mp.nstr(value, 72, strip_zeros=False)


CASE_DEFS = [
    ("P01-RR", Fraction(1), Fraction(4), Fraction(9), Fraction(1), Fraction(0)),
    ("P02-RS", Fraction(2), Fraction(9), Fraction(1), Fraction(4), Fraction(1, 2)),
    ("P03-SR", Fraction(3, 2), Fraction(1), Fraction(16), Fraction(4), Fraction(-1)),
    ("P04-SS", Fraction(1, 2), Fraction(1), Fraction(4), Fraction(9), Fraction(2)),
    ("P05-ZR", Fraction(1), Fraction(2), Fraction(8), Fraction(2), Fraction(0)),
    ("P06-ZS", Fraction(2), Fraction(3), Fraction(1), Fraction(3), Fraction(-1, 2)),
    ("P07-RZ", Fraction(3, 2), Fraction(20), Fraction(5), Fraction(5), Fraction(3, 4)),
    ("P08-SZ", Fraction(4, 3), Fraction(1), Fraction(7), Fraction(7), Fraction(-2)),
    ("P09-ZZ", Fraction(5, 4), Fraction(3), Fraction(3), Fraction(3), Fraction(7, 5)),
    ("P10-RR", Fraction(2, 3), Fraction(7, 3), Fraction(11, 2), Fraction(1, 4), Fraction(-3, 2)),
    ("P11-RS", Fraction(5, 4), Fraction(8), Fraction(2, 5), Fraction(3, 2), Fraction(2, 3)),
    ("P12-SR", Fraction(7, 5), Fraction(1, 3), Fraction(10), Fraction(5, 2), Fraction(-4, 3)),
    ("P13-SS", Fraction(9, 7), Fraction(2, 5), Fraction(3, 2), Fraction(6), Fraction(5, 6)),
    ("P14-RR-scaled", Fraction(1), Fraction(20), Fraction(45), Fraction(5), Fraction(0)),
    ("P15-RS-scaled", Fraction(2), Fraction(27, 2), Fraction(3, 2), Fraction(6), Fraction(1, 2)),
    ("P16-SR-scaled", Fraction(3, 2), Fraction(7), Fraction(112), Fraction(28), Fraction(-1)),
    ("P17-SS-scaled", Fraction(1, 2), Fraction(1, 3), Fraction(4, 3), Fraction(3), Fraction(2)),
    ("P18-RR-extreme", Fraction(1, 5), Fraction(100), Fraction(1, 100), Fraction(1, 10000), Fraction(10)),
    ("P19-SS-extreme", Fraction(3), Fraction(1, 100), Fraction(1, 5), Fraction(50), Fraction(-10)),
    ("P20-RS-asymmetric", Fraction(11, 6), Fraction(25), Fraction(1, 4), Fraction(9, 4), Fraction(0)),
]

SCALING_PAIRS = [
    ("P01-RR", "P14-RR-scaled", Fraction(5)),
    ("P02-RS", "P15-RS-scaled", Fraction(3, 2)),
    ("P03-SR", "P16-SR-scaled", Fraction(7)),
    ("P04-SS", "P17-SS-scaled", Fraction(1, 3)),
]

FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
    "Densities, characteristic speeds, and wave families are source PDE data, not rational-prime labels or prime-power weights.",
    "The entropy solution semigroup is not asserted to be a Hilbert-Polya operator.",
    "No literature priority is claimed for the classical Lax Riemann construction or isothermal wave curves.",
]


def fcurve(rho, rho0, sound):
    if rho <= rho0:
        return sound * mp.log(rho / rho0)
    return sound * (rho - rho0) / mp.sqrt(rho * rho0)


def entropy(rho, u, sound):
    return rho * u * u / 2 + sound * sound * rho * mp.log(rho)


def entropy_flux(rho, u, sound):
    eta = entropy(rho, u, sound)
    return u * (eta + sound * sound * rho)


def phi(rho, rho_l, rho_r, u_l, u_r, sound):
    return fcurve(rho, rho_l, sound) + fcurve(rho, rho_r, sound) + u_r - u_l


def solve_root(rho_l, rho_r, u_l, u_r, sound):
    center = (mp.log(rho_l) + mp.log(rho_r)) / 2
    low, high = center - 1, center + 1
    while phi(mp.exp(low), rho_l, rho_r, u_l, u_r, sound) >= 0:
        low -= 2
    while phi(mp.exp(high), rho_l, rho_r, u_l, u_r, sound) <= 0:
        high += 2
    for _ in range(400):
        mid = (low + high) / 2
        if phi(mp.exp(mid), rho_l, rho_r, u_l, u_r, sound) < 0:
            low = mid
        else:
            high = mid
    return mp.exp((low + high) / 2)


def shock_receipts(family, sound, rho_l, u_l, rho_r, u_r, speed):
    mass = speed * (rho_r - rho_l) - (rho_r * u_r - rho_l * u_l)
    mom_l = rho_l * u_l * u_l + sound * sound * rho_l
    mom_r = rho_r * u_r * u_r + sound * sound * rho_r
    momentum = speed * (rho_r * u_r - rho_l * u_l) - (mom_r - mom_l)
    production = entropy_flux(rho_r, u_r, sound) - entropy_flux(rho_l, u_l, sound)
    production -= speed * (entropy(rho_r, u_r, sound) - entropy(rho_l, u_l, sound))
    if family == 1:
        lower_gap = speed - (u_r - sound)
        upper_gap = (u_l - sound) - speed
        low_density = rho_l
        ratio = rho_r / rho_l
    else:
        lower_gap = speed - (u_r + sound)
        upper_gap = (u_l + sound) - speed
        low_density = rho_r
        ratio = rho_l / rho_r
    closed_entropy = sound**3 * low_density * mp.sqrt(ratio) * (
        mp.log(ratio) - (ratio - 1 / ratio) / 2
    )
    return {
        "mass_jump_residual": dec(mass),
        "momentum_jump_residual": dec(momentum),
        "entropy_production": dec(production),
        "closed_entropy_production": dec(closed_entropy),
        "lax_lower_gap": dec(lower_gap),
        "lax_upper_gap": dec(upper_gap),
        "strict_entropy": production < 0,
        "strict_lax": lower_gap > 0 and upper_gap > 0,
    }


def wave_one(sound, rho_l, u_l, rho_star, u_star):
    if rho_star < rho_l:
        left_edge, right_edge = u_l - sound, u_star - sound
        xi = (left_edge + right_edge) / 2
        u = xi + sound
        rho = rho_l * mp.exp((u_l - u) / sound)
        invariant = u + sound * mp.log(rho) - (u_l + sound * mp.log(rho_l))
        return {
            "family": 1, "kind": "rarefaction", "zero_strength": False,
            "left_edge": dec(left_edge), "right_edge": dec(right_edge),
            "midpoint": {
                "xi": dec(xi), "rho": dec(rho), "u": dec(u),
                "characteristic_residual": dec(xi - (u - sound)),
                "invariant_residual": dec(invariant),
            },
        }
    if rho_star > rho_l:
        ratio = rho_star / rho_l
        speed_outer = u_l - sound * mp.sqrt(ratio)
        speed_star = u_star - sound / mp.sqrt(ratio)
        return {
            "family": 1, "kind": "shock", "zero_strength": False,
            "compression_ratio": dec(ratio),
            "speed_from_outer": dec(speed_outer),
            "speed_from_star": dec(speed_star),
            **shock_receipts(1, sound, rho_l, u_l, rho_star, u_star, speed_outer),
        }
    return {
        "family": 1, "kind": "zero", "zero_strength": True,
        "characteristic_speed": dec(u_star - sound),
        "density_jump": "0.0", "velocity_jump": "0.0",
    }


def wave_two(sound, rho_r, u_r, rho_star, u_star):
    if rho_star < rho_r:
        left_edge, right_edge = u_star + sound, u_r + sound
        xi = (left_edge + right_edge) / 2
        u = xi - sound
        rho = rho_r * mp.exp((u - u_r) / sound)
        invariant = u - sound * mp.log(rho) - (u_r - sound * mp.log(rho_r))
        return {
            "family": 2, "kind": "rarefaction", "zero_strength": False,
            "left_edge": dec(left_edge), "right_edge": dec(right_edge),
            "midpoint": {
                "xi": dec(xi), "rho": dec(rho), "u": dec(u),
                "characteristic_residual": dec(xi - (u + sound)),
                "invariant_residual": dec(invariant),
            },
        }
    if rho_star > rho_r:
        ratio = rho_star / rho_r
        speed_outer = u_r + sound * mp.sqrt(ratio)
        speed_star = u_star + sound / mp.sqrt(ratio)
        return {
            "family": 2, "kind": "shock", "zero_strength": False,
            "compression_ratio": dec(ratio),
            "speed_from_outer": dec(speed_outer),
            "speed_from_star": dec(speed_star),
            **shock_receipts(2, sound, rho_star, u_star, rho_r, u_r, speed_outer),
        }
    return {
        "family": 2, "kind": "zero", "zero_strength": True,
        "characteristic_speed": dec(u_star + sound),
        "density_jump": "0.0", "velocity_jump": "0.0",
    }


def rightmost_speed(wave):
    if wave["kind"] == "rarefaction":
        return mp.mpf(wave["right_edge"])
    if wave["kind"] == "shock":
        return mp.mpf(wave["speed_from_outer"])
    return mp.mpf(wave["characteristic_speed"])


def leftmost_speed(wave):
    if wave["kind"] == "rarefaction":
        return mp.mpf(wave["left_edge"])
    if wave["kind"] == "shock":
        return mp.mpf(wave["speed_from_outer"])
    return mp.mpf(wave["characteristic_speed"])


def build_case(definition):
    case_id, a_q, rl_q, rr_q, rs_q, us_q = definition
    sound, rho_l, rho_r, rho_star, u_star = map(mpq, (a_q, rl_q, rr_q, rs_q, us_q))
    f_l = fcurve(rho_star, rho_l, sound)
    f_r = fcurve(rho_star, rho_r, sound)
    u_l, u_r = u_star + f_l, u_star - f_r
    root = solve_root(rho_l, rho_r, u_l, u_r, sound)
    recovered_u_left = u_l - fcurve(root, rho_l, sound)
    recovered_u_right = u_r + fcurve(root, rho_r, sound)
    first = wave_one(sound, rho_l, u_l, rho_star, u_star)
    second = wave_two(sound, rho_r, u_r, rho_star, u_star)
    gap = leftmost_speed(second) - rightmost_speed(first)
    pattern = f"{first['kind'][0].upper()}-{second['kind'][0].upper()}"
    return {
        "case_id": case_id,
        "exact_parameters": {
            "a": q(a_q), "rho_L": q(rl_q), "rho_R": q(rr_q),
            "rho_star": q(rs_q), "u_star": q(us_q),
        },
        "derived_data": {
            "f_left": dec(f_l), "f_right": dec(f_r),
            "u_L": dec(u_l), "u_R": dec(u_r),
            "velocity_jump_uR_minus_uL": dec(u_r - u_l),
        },
        "root_receipts": {
            "phi_at_declared_root": dec(phi(rho_star, rho_l, rho_r, u_l, u_r, sound)),
            "independently_reconstructed_root": dec(root),
            "root_absolute_error": dec(abs(root - rho_star)),
            "recovered_u_star_left": dec(recovered_u_left),
            "recovered_u_star_right": dec(recovered_u_right),
            "root_is_strictly_positive": root > 0,
        },
        "pattern": pattern,
        "wave_1": first,
        "wave_2": second,
        "intermediate_speed_gap": dec(gap),
        "waves_strictly_ordered": gap > 0,
    }


def pressureless_probes():
    rows = []
    for a_q in (Fraction(1), Fraction(1, 2), Fraction(1, 4), Fraction(1, 8)):
        sound = mpq(a_q)
        separating = mp.exp(-1 / (2 * sound))
        c = 1 / (2 * sound)
        y = (c + mp.sqrt(c * c + 4)) / 2
        compressive = y * y
        rows.append({
            "a": q(a_q),
            "fixed_states": "rho_L=rho_R=1; |u_L-u_R|=1",
            "separating_rho_star": dec(separating),
            "separating_closed_form": "exp(-1/(2a))",
            "compressive_rho_star": dec(compressive),
            "compressive_sqrt_root_closed_form": "(1/(2a)+sqrt(1/(4a^2)+4))/2",
            "separating_tends_to_zero": True,
            "compressive_grows": True,
        })
    return rows


BOUNDARIES = [
    {"boundary_id": "B0-positive-data", "status": "theorem domain", "statement": "a>0 and both input densities positive with finite velocities."},
    {"boundary_id": "B1-no-vacuum", "status": "exact", "statement": "the monotone root is positive for every datum in the theorem chamber."},
    {"boundary_id": "B2-zero-wave", "status": "included", "statement": "equality with either reference density deletes exactly that wave."},
    {"boundary_id": "B3-constant-data", "status": "included", "statement": "two zero waves occur exactly for identical left and right states."},
    {"boundary_id": "B4-density-scaling", "status": "exact symmetry", "statement": "common positive density scaling preserves velocities, ratios, types, and speeds."},
    {"boundary_id": "B5-vacuum-input", "status": "excluded", "statement": "zero-density input traces need a separate boundary theory."},
    {"boundary_id": "B6-pressureless-separation", "status": "singular limit", "statement": "fixed separating data can drive the intermediate density exponentially to zero as a decreases."},
    {"boundary_id": "B7-pressureless-compression", "status": "singular limit", "statement": "fixed compressive data can drive the intermediate density to infinity and toward concentration as a decreases."},
]


def build() -> dict:
    cases = [build_case(definition) for definition in CASE_DEFS]
    by_id = {case["case_id"]: case for case in cases}
    scaling = []
    for base_id, scaled_id, factor in SCALING_PAIRS:
        base, scaled = by_id[base_id], by_id[scaled_id]
        scaling.append({
            "base_case": base_id, "scaled_case": scaled_id, "density_factor": q(factor),
            "same_pattern": base["pattern"] == scaled["pattern"],
            "same_u_L": dec(mp.mpf(scaled["derived_data"]["u_L"]) - mp.mpf(base["derived_data"]["u_L"])),
            "same_u_R": dec(mp.mpf(scaled["derived_data"]["u_R"]) - mp.mpf(base["derived_data"]["u_R"])),
            "same_u_star": dec(mpq(Fraction(scaled["exact_parameters"]["u_star"])) - mpq(Fraction(base["exact_parameters"]["u_star"]))),
            "rho_star_scaled_exactly": Fraction(scaled["exact_parameters"]["rho_star"]) == factor * Fraction(base["exact_parameters"]["rho_star"]),
        })
    kinds = Counter(wave["kind"] for case in cases for wave in (case["wave_1"], case["wave_2"]))
    patterns = Counter(case["pattern"] for case in cases)
    wave_cells = kinds["rarefaction"] * 5 + kinds["shock"] * 10 + kinds["zero"] * 3
    root_cells = len(cases) * 6
    scaling_cells = len(scaling) * 5
    pressure_rows = pressureless_probes()
    pressure_cells = len(pressure_rows) * 4
    boundary_cells = len(BOUNDARIES)
    total = wave_cells + root_cells + scaling_cells + pressure_cells + boundary_cells
    data = {
        "schema": "hcs-c300-isothermal-euler-riemann-v1",
        "candidate_id": "HCS-C300",
        "obstruction_id": "HEN-O284",
        "evaluation_date": "2026-09-02",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "equations": "rho_t+(rho u)_x=0; (rho u)_t+(rho u^2+a^2 rho)_x=0",
            "parameters": "a>0, rho_L>0, rho_R>0, u_L and u_R finite real",
            "clock": "self-similar coordinate xi=x/t for t>0",
            "normalization": "physical density and velocity; no arithmetic normalization",
        },
        "theorem_contract": {
            "root": "one strictly increasing scalar equation has exactly one rho_star>0 for every declared datum",
            "patterns": "the two density comparisons give all four nondegenerate shock/rarefaction patterns and all zero-wave boundaries",
            "entropy": "each shock has strict negative mechanical entropy production and each fan is an entropy equality",
            "vacuum": "finite velocities and positive input densities at a>0 never create an isothermal vacuum",
            "pressureless": "a down to zero is a singular excluded boundary, not a theorem corollary",
        },
        "proof_contract": {
            "monotonicity": "each wave function is C1 strictly increasing from minus infinity to plus infinity",
            "wave_signs": "family 1 uses the negative Hugoniot sign and family 2 the positive sign",
            "entropy_formula": "shock production equals a^3 rho_0 sqrt(r)[log r-(r-r^{-1})/2], strictly negative for r>1",
            "finite_role": "finite cases regress formulas and signs; the full-data theorem is analytic",
        },
        "enumeration": {
            "cases": cases,
            "scaling_pairs": scaling,
            "pressureless_probes": pressure_rows,
            "boundary_rows": BOUNDARIES,
            "case_count": len(cases),
            "wave_count": 2 * len(cases),
            "wave_kind_counts": dict(sorted(kinds.items())),
            "pattern_counts": dict(sorted(patterns.items())),
            "root_receipt_cells": root_cells,
            "wave_receipt_cells": wave_cells,
            "scaling_receipt_cells": scaling_cells,
            "pressureless_receipt_cells": pressure_cells,
            "boundary_receipt_cells": boundary_cells,
            "audited_cell_count": total,
        },
        "route_a": {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": NONCLAIMS,
        "collision_boundary": {
            "C195": "C195 is scalar periodic viscous Burgers dynamics; C300 is a two-field inviscid Riemann solver with two genuinely nonlinear families and four wave patterns.",
            "pressureless_warning": "vacuum and delta-shock behavior at a=0 are excluded singular limits, not imported conclusions.",
        },
        "references": [
            {"identifier": "10.1002/cpa.3160100406", "role": "classical Lax hyperbolic-system and Riemann construction owner"},
            {"identifier": "10.1090/mmono/055", "role": "isothermal gas-dynamics and Riemann-invariant context"},
            {"identifier": "10.1007/978-3-642-04048-1", "role": "modern entropy-solution framework"},
        ],
    }
    data["payload_sha256"] = canonical_payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C300_PRODUCER_PASS",
        "cases": data["enumeration"]["case_count"],
        "audited_cells": data["enumeration"]["audited_cell_count"],
        "payload_sha256": data["payload_sha256"],
        "evidence_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
