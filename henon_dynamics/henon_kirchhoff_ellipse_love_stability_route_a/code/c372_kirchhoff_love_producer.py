#!/usr/bin/env python3
"""Canonical exact evidence producer for HCS-C372."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("C372 producer refuses optimized Python")

import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c372_kirchhoff_love_evidence.json"
YML = ROOT / "evaluations/route_a/HCS-C372/2026-09-04.yaml"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "0df240c2c2e2a8becf27eb76bc7797c532595b2b889296fffd125fee5aa20beb"
YAML_SEMANTIC = "49a6fd8fac70ecf15c2118bd64275627567f10feee99b46e65f9538a150ef904"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
MAX_DENOMINATOR = 16
MAX_ASPECT = 8
MAX_MODE = 64
BISECTION_BITS = 96


class Loader(yaml.SafeLoader):
    pass


Loader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge keys are forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate or non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases are forbidden")
    value = yaml.load(raw, Loader=Loader)
    if type(value) is not dict:
        raise TypeError("YAML root must be a mapping")
    return value


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(value) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def fs(value: F) -> str:
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def geometry(gamma: F):
    gamma = F(gamma)
    delta = (gamma - 1) / (gamma + 1)
    kappa = 2 * gamma / (gamma + 1) ** 2
    omega_ratio = gamma / (gamma + 1) ** 2
    assert kappa == (1 - delta * delta) / 2
    assert omega_ratio == kappa / 2
    return delta, kappa, omega_ratio


def mode_data(gamma: F, mode: int):
    delta, kappa, omega_ratio = geometry(gamma)
    minus = mode * kappa - 1 - delta**mode
    plus = mode * kappa - 1 + delta**mode
    square = minus * plus / 4
    state = "oscillatory" if square > 0 else "critical" if square == 0 else "exponential"
    return {
        "mode": mode,
        "minus_factor": fs(minus),
        "plus_factor": fs(plus),
        "love_square_coefficient": fs(square),
        "classification": state,
        "m1_rotation_identity_residual": fs(square - omega_ratio**2) if mode == 1 else None,
        "m2_family_identity_residual": fs(square) if mode == 2 else None,
    }


def critical_function(mode: int, delta: F) -> F:
    return F(mode, 2) * (1 - delta * delta) - 1 - delta**mode


def critical_bracket(mode: int):
    if mode == 3:
        low = high = F(1, 2)
    else:
        low, high = F(0), F(1)
        for _ in range(BISECTION_BITS):
            middle = (low + high) / 2
            if critical_function(mode, middle) > 0:
                low = middle
            else:
                high = middle
        assert critical_function(mode, low) > 0 > critical_function(mode, high)
    gamma_low = (1 + low) / (1 - low)
    gamma_high = (1 + high) / (1 - high)
    return {
        "mode": mode,
        "delta_lower": fs(low),
        "delta_upper": fs(high),
        "aspect_lower": fs(gamma_low),
        "aspect_upper": fs(gamma_high),
        "lower_sign": 0 if low == high else 1,
        "upper_sign": 0 if low == high else -1,
        "exact": mode == 3,
    }


def aspect_rows():
    gammas = sorted(
        {
            F(numerator, denominator)
            for denominator in range(1, MAX_DENOMINATOR + 1)
            for numerator in range(denominator, MAX_ASPECT * denominator + 1)
        }
    )
    rows = []
    global_hasher = hashlib.sha256()
    cells = 0
    for gamma in gammas:
        delta, kappa, omega_ratio = geometry(gamma)
        modes = [mode_data(gamma, mode) for mode in range(1, MAX_MODE + 1)]
        encoded = canonical(modes)
        global_hasher.update(fs(gamma).encode() + b"|" + encoded + b"\n")
        cells += len(modes)
        counts = {
            name: sum(row["classification"] == name for row in modes)
            for name in ("oscillatory", "critical", "exponential")
        }
        rows.append(
            {
                "aspect_ratio": fs(gamma),
                "delta": fs(delta),
                "kappa": fs(kappa),
                "rotation_rate_over_vorticity": fs(omega_ratio),
                "mode_count": len(modes),
                "classification_counts": counts,
                "mode_rows_sha256": hashlib.sha256(encoded).hexdigest(),
                "anchor_modes": [modes[index - 1] for index in (1, 2, 3, 4, 8, 16, 32, 64)],
            }
        )
    return gammas, rows, cells, global_hasher.hexdigest()


def rigid_rows():
    rows = []
    for a in range(1, 13):
        for b in range(1, a + 1):
            for omega in (-3, -1, 0, 1, 3):
                a0, b0, w = F(a), F(b), F(omega)
                rotation = w * a0 * b0 / (a0 + b0) ** 2
                rows.append(
                    {
                        "a": a,
                        "b": b,
                        "vorticity": omega,
                        "aspect_ratio": fs(a0 / b0),
                        "rotation_rate": fs(rotation),
                        "area_over_pi": fs(a0 * b0),
                        "circulation_over_pi": fs(w * a0 * b0),
                        "quadratic_vorticity_moment_over_pi": fs(w * a0 * b0 * (a0 * a0 + b0 * b0) / 4),
                        "patch_minimal_period_over_pi": None if rotation == 0 or a == b else fs(1 / abs(rotation)),
                        "oriented_axis_period_over_pi": None if rotation == 0 or a == b else fs(2 / abs(rotation)),
                        "rotation_orientation": "orientation_unobservable" if a == b else "counterclockwise" if rotation > 0 else "clockwise" if rotation < 0 else "stationary",
                        "patch_motion": "stationary circular shape" if a == b else "rotating noncircular shape" if rotation != 0 else "stationary zero-vorticity ellipse",
                    }
                )
    return rows


def build(evaluation_path: Path):
    raw = evaluation_path.read_bytes()
    semantic = strict_yaml(evaluation_path)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw digest drift")
    if digest(semantic) != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic digest drift")
    gammas, aspects, modal_cells, modal_digest = aspect_rows()
    thresholds = [critical_bracket(mode) for mode in range(3, MAX_MODE + 1)]
    for left, right in zip(thresholds, thresholds[1:]):
        if F(left["aspect_upper"]) >= F(right["aspect_lower"]):
            raise ArithmeticError("critical aspects are not strictly increasing")
    rigid = rigid_rows()
    flags = {
        key: False
        for key in (
            "claims_target_arithmetic_local_data",
            "claims_target_euler_factors",
            "claims_root_number",
            "claims_automorphy",
            "claims_target_divisor_or_counting_law",
            "claims_target_functional_equation",
            "claims_target_zero_match",
            "claims_hilbert_polya_operator",
            "invokes_route_b",
        )
    }
    body = {
        "schema": "hcs-c372-kirchhoff-love-evidence-v2",
        "candidate_id": "HCS-C372",
        "obstruction_id": "HEN-O356",
        "evaluation_date": "2026-09-04",
        "source_commit": SOURCE,
        "fixed_epoch": 1788480000,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C372/2026-09-04.yaml", "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {
            "equation": "partial_t omega+u dot grad omega=0, div u=0, curl u=omega on R2",
            "patch": "omega(x,t)=vorticity*indicator of the rotating ellipse E_t",
            "ellipse": "E_0={x^2/a^2+y^2/b^2<1}, a>=b>0",
            "mode_convention": "boundary Fourier label m is measured relative to the instantaneous ellipse principal axes, and lambda_m is the co-rotating-frame frequency with time dependence exp(-i*lambda_m*t)",
        },
        "theorem_contract": {
            "rigid_rotation": "E_t is E_0 rotated through Omega*t, Omega=vorticity*a*b/(a+b)^2",
            "love_dispersion": "lambda_m^2=(vorticity^2/4)*([2*m*a*b/(a+b)^2-1]^2-[(a-b)/(a+b)]^(2*m))",
            "symmetry_modes": "lambda_1^2=Omega^2 and lambda_2^2=0 for every ellipse",
            "critical_equation": "for m>=3, delta_m is the unique root in (0,1) of m*(1-delta^2)/2-1-delta^m=0",
            "threshold_order": "delta_m and gamma_m=(1+delta_m)/(1-delta_m) strictly increase with m",
            "threshold_asymptotic": "if c_star=1+W(exp(-1)), then m*(1-delta_m) tends to c_star and gamma_m/m tends to 2/c_star",
            "sharp_wall": "delta_3=1/2 and gamma_3=3; for nonzero vorticity all m>=3 oscillate for gamma<3, m=3 is critical at 3, and m=3 grows exponentially for gamma>3",
            "scope": "spectral linear mode stability only; no nonlinear stability or post-filamentation theorem",
        },
        "proof_receipts": {
            "dimensionless_variables": "delta=(a-b)/(a+b), kappa=2ab/(a+b)^2=(1-delta^2)/2",
            "factorization": "4*lambda_m^2=vorticity^2*(m*kappa-1-delta^m)*(m*kappa-1+delta^m)",
            "unique_root": "F_m(delta)=m*(1-delta^2)/2-1-delta^m decreases strictly from m/2-1 to -2",
            "positive_second_factor": "G_m(delta)=m*(1-delta^2)/2-1+delta^m is positive on [0,1) for m>=3 because G_m'=m*delta*(delta^(m-2)-1)<0 and G_m(1)=0",
            "ordered_roots": "F_(m+1)(delta)-F_m(delta)=(1-delta^2)/2+delta^m*(1-delta)>0",
            "scaled_root": "c_m=m*(1-delta_m) lies in (1,2) and satisfies c_m-c_m^2/(2m)=1+(1-c_m/m)^m",
            "m3_factor": "16*lambda_3^2=vorticity^2*(1-delta^2)^2*(1-4*delta^2)",
        },
        "finite_evidence_role": "exact rational modal and invariant regression plus certified root isolation; analytic monotonicity proves all aspects and modes",
        "finite_grid": {
            "max_aspect_ratio": MAX_ASPECT,
            "max_reduced_denominator": MAX_DENOMINATOR,
            "distinct_aspect_ratios": len(gammas),
            "max_mode": MAX_MODE,
            "modal_cells": modal_cells,
            "modal_cells_sha256": modal_digest,
            "critical_modes": len(thresholds),
            "critical_bisection_bits": BISECTION_BITS,
            "rigid_solution_rows": len(rigid),
        },
        "aspect_rows": aspects,
        "critical_thresholds": thresholds,
        "rigid_solution_rows": rigid,
        "boundary_atlas": [
            {"face": "a>b>0 and vorticity nonzero", "classification": "rotating Kirchhoff ellipse", "mode_statement": "Love formula and ordered thresholds apply"},
            {"face": "a=b>0 and vorticity nonzero", "classification": "Rankine circular patch", "mode_statement": "the patch shape is stationary because orientation is undefined; the formula reduces to Kelvin-mode frequencies"},
            {"face": "vorticity=0", "classification": "stationary zero patch", "mode_statement": "Omega and every lambda square vanish after the overall vorticity factor"},
            {"face": "a<b", "classification": "axis-swapped convention", "mode_statement": "swap semiaxes before applying gamma>=1"},
            {"face": "b=0 or a infinite", "classification": "singular strip limit", "mode_statement": "excluded from the bounded ellipse theorem"},
            {"face": "gamma=3", "classification": "first spectral threshold", "mode_statement": "m=3 has zero frequency; no nonlinear conclusion is asserted"},
        ],
        "collision_boundary": {
            "C284": "finite point-vortex relative equilibria, not a distributed constant-vorticity free boundary",
            "C299": "viscously diffusing Lamb-Oseen vorticity, not an inviscid rotating patch",
            "C368": "Polubarinova-Galin Laplacian growth with source or sink, not area-preserving Euler contour transport",
        },
        "references": [
            {"doi": "10.1112/plms/s1-25.1.18", "role": "classical owner of the Love modal dispersion relation"},
            {"doi": "10.1063/1.2912991", "role": "modern co-rotating convention and Love-mode formula audit"},
            {"doi": "10.1017/S0022112094000339", "role": "stratified baroclinic extension used only to delimit the two-dimensional Love-mode scope"},
        ],
        "nonclaims": [
            "no nonlinear orbital or Lyapunov stability theorem",
            "no finite-amplitude filamentation, fission, or post-instability prediction",
            "no bounded-domain, compressible, viscous, or three-dimensional extension",
            "no arithmetic prime owner or target determinant",
            "no target continuation, zero match, Hilbert-Polya operator, or Route B",
            "no literature-priority claim for the Kirchhoff or Love results",
        ],
        "route_a": {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": flags,
    }
    body["payload_sha256"] = digest(body)
    return body


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    parser.add_argument("--evaluation", type=Path, default=YML)
    args = parser.parse_args()
    evidence = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    grid = evidence["finite_grid"]
    print(
        "C372_PRODUCER_PASS "
        f"{evidence['payload_sha256']} aspects={grid['distinct_aspect_ratios']} "
        f"modal_cells={grid['modal_cells']} thresholds={grid['critical_modes']} "
        f"rigid={grid['rigid_solution_rows']}"
    )


if __name__ == "__main__":
    main()
