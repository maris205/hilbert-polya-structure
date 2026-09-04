#!/usr/bin/env python3
"""Independent exact checker for HCS-C372; never imports the producer."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("C372 checker refuses optimized Python")

import hashlib
import json
import math
import sys
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EV = ROOT / "results/c372_kirchhoff_love_evidence.json"
YML = ROOT / "evaluations/route_a/HCS-C372/2026-09-04.yaml"
RAW = "0df240c2c2e2a8becf27eb76bc7797c532595b2b889296fffd125fee5aa20beb"
SEMANTIC = "49a6fd8fac70ecf15c2118bd64275627567f10feee99b46e65f9538a150ef904"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
ROUTE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
MAX_MODE = 64
BITS = 96
TOP = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal",
    "evaluator", "route_a_yaml", "model", "theorem_contract", "proof_receipts", "finite_evidence_role",
    "finite_grid", "aspect_rows", "critical_thresholds", "rigid_solution_rows", "boundary_atlas",
    "collision_boundary", "references", "nonclaims", "route_a", "scope_flags", "payload_sha256",
}


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
            raise ValueError("YAML merge key")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate/non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_json(path):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError("duplicate JSON key")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=unique, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML alias")
    value = yaml.load(raw, Loader=Loader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def fs(value):
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def same(left, right):
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(same(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(same(a, b) for a, b in zip(left, right))
    return left == right


def keys(value, expected):
    if type(value) is not dict or set(value) != set(expected):
        raise AssertionError("schema drift")


def dimensionless(gamma):
    gamma = F(gamma)
    delta = (gamma - 1) / (gamma + 1)
    kappa = 2 * gamma / (gamma + 1) ** 2
    return delta, kappa, gamma / (gamma + 1) ** 2


def independent_mode(gamma, mode):
    gamma = F(gamma)
    delta, kappa, omega_ratio = dimensionless(gamma)
    direct = (((2 * mode * gamma / (gamma + 1) ** 2) - 1) ** 2 - delta ** (2 * mode)) / 4
    minus = mode * kappa - 1 - delta**mode
    plus = mode * kappa - 1 + delta**mode
    if direct != minus * plus / 4:
        raise AssertionError("factorization inconsistency")
    classification = "oscillatory" if direct > 0 else "critical" if direct == 0 else "exponential"
    return {
        "mode": mode,
        "minus_factor": fs(minus),
        "plus_factor": fs(plus),
        "love_square_coefficient": fs(direct),
        "classification": classification,
        "m1_rotation_identity_residual": fs(direct - omega_ratio**2) if mode == 1 else None,
        "m2_family_identity_residual": fs(direct) if mode == 2 else None,
    }


def rational_aspects():
    values = {
        F(numerator, denominator)
        for denominator in range(1, 17)
        for numerator in range(denominator, 8 * denominator + 1)
        if math.gcd(numerator, denominator) == 1
    }
    return sorted(values)


def critical(mode, delta):
    delta = F(delta)
    return F(mode, 2) * (1 - delta * delta) - 1 - delta**mode


def independent_threshold(mode):
    if mode == 3:
        lower = upper = F(1, 2)
    else:
        denominator = 1 << BITS
        low_integer, high_integer = 0, denominator
        while high_integer - low_integer > 1:
            middle = (low_integer + high_integer) // 2
            if critical(mode, F(middle, denominator)) > 0:
                low_integer = middle
            else:
                high_integer = middle
        lower, upper = F(low_integer, denominator), F(high_integer, denominator)
        if not critical(mode, lower) > 0 > critical(mode, upper):
            raise AssertionError("threshold sign")
    return {
        "mode": mode,
        "delta_lower": fs(lower),
        "delta_upper": fs(upper),
        "aspect_lower": fs((1 + lower) / (1 - lower)),
        "aspect_upper": fs((1 + upper) / (1 - upper)),
        "lower_sign": 0 if lower == upper else 1,
        "upper_sign": 0 if lower == upper else -1,
        "exact": mode == 3,
    }


def expected_rigid(a, b, omega):
    aa, bb, ww = F(a), F(b), F(omega)
    rotation = ww * aa * bb / (aa + bb) ** 2
    circle = a == b
    return {
        "a": a,
        "b": b,
        "vorticity": omega,
        "aspect_ratio": fs(aa / bb),
        "rotation_rate": fs(rotation),
        "area_over_pi": fs(aa * bb),
        "circulation_over_pi": fs(ww * aa * bb),
        "quadratic_vorticity_moment_over_pi": fs(ww * aa * bb * (aa * aa + bb * bb) / 4),
        "patch_minimal_period_over_pi": None if rotation == 0 or circle else fs(1 / abs(rotation)),
        "oriented_axis_period_over_pi": None if rotation == 0 or circle else fs(2 / abs(rotation)),
        "rotation_orientation": "orientation_unobservable" if circle else "counterclockwise" if rotation > 0 else "clockwise" if rotation < 0 else "stationary",
        "patch_motion": "stationary circular shape" if circle else "rotating noncircular shape" if rotation != 0 else "stationary zero-vorticity ellipse",
    }


@lru_cache(maxsize=1)
def expected_aspect_bundle():
    gammas = rational_aspects()
    rows = []
    global_hasher = hashlib.sha256()
    for gamma in gammas:
        delta, kappa, omega_ratio = dimensionless(gamma)
        modes = [independent_mode(gamma, mode) for mode in range(1, MAX_MODE + 1)]
        encoded = canonical(modes)
        global_hasher.update(fs(gamma).encode() + b"|" + encoded + b"\n")
        class_counts = {state: sum(row["classification"] == state for row in modes) for state in ("oscillatory", "critical", "exponential")}
        rows.append({
            "aspect_ratio": fs(gamma), "delta": fs(delta), "kappa": fs(kappa),
            "rotation_rate_over_vorticity": fs(omega_ratio), "mode_count": 64,
            "classification_counts": class_counts, "mode_rows_sha256": hashlib.sha256(encoded).hexdigest(),
            "anchor_modes": [modes[index - 1] for index in (1, 2, 3, 4, 8, 16, 32, 64)],
        })
    return gammas, rows, global_hasher.hexdigest()


@lru_cache(maxsize=1)
def expected_threshold_rows():
    return [independent_threshold(mode) for mode in range(3, 65)]


@lru_cache(maxsize=1)
def expected_rigid_rows():
    return [expected_rigid(a, b, omega) for a in range(1, 13) for b in range(1, a + 1) for omega in (-3, -1, 0, 1, 3)]


def check(evidence=EV, yaml_path=YML):
    count = 0
    value = strict_json(evidence)
    keys(value, TOP)
    count += 1
    claimed = value.pop("payload_sha256")
    if claimed != hashlib.sha256(canonical(value)).hexdigest():
        raise AssertionError("payload hash")
    value["payload_sha256"] = claimed
    count += 1
    metadata = {
        "schema": "hcs-c372-kirchhoff-love-evidence-v2", "candidate_id": "HCS-C372", "obstruction_id": "HEN-O356",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE, "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
    }
    for key, expected in metadata.items():
        if not same(value[key], expected):
            raise AssertionError(f"metadata {key}")
        count += 1
    if not same(value["evaluator"], {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}):
        raise AssertionError("evaluator")
    if not same(value["route_a_yaml"], {"relative_path": "evaluations/route_a/HCS-C372/2026-09-04.yaml", "raw_sha256": RAW, "semantic_sha256": SEMANTIC}):
        raise AssertionError("YAML receipt")
    count += 2
    yml = strict_yaml(yaml_path)
    if hashlib.sha256(yaml_path.read_bytes()).hexdigest() != RAW or hashlib.sha256(canonical(yml)).hexdigest() != SEMANTIC:
        raise AssertionError("YAML hash")
    count += 2
    ykeys = {
        "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal",
        "evaluator_authority", "evaluator_version", "evaluator_authority_sha256", "obstruction_id", "candidate_definition",
        "family", "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock",
        "normalization", "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data",
        "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict",
        "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
        "source_owner_tokens",
    }
    keys(yml, ykeys)
    if yml["candidate_id"] != "HCS-C372" or yml["obstruction_id"] != "HEN-O356" or yml["source_commit"] != SOURCE:
        raise AssertionError("YAML identity")
    if yml["tuple"] != ROUTE or yml["overall_verdict"] != "ROUTE_A_REJECTED" or yml["route_b_invocation_allowed"] is not False:
        raise AssertionError("YAML route")
    if "circle is a shape equilibrium" not in yml["a1"]["strongest_evidence"] or "circular shape has no observable orientation" not in yml["clock"]:
        raise AssertionError("YAML circle convention")
    if yml["source_owner_tokens"] != [
        "DOI:10.1112/plms/s1-25.1.18",
        "DOI:10.1063/1.2912991",
        "DOI:10.1017/S0022112094000339",
        "theorem:Kirchhoff-rigid-ellipse",
        "theorem:Love-mode-dispersion",
    ]:
        raise AssertionError("YAML source-owner lock")
    count += 8
    for gate, verdict in zip(("a0", "a1", "a2", "a3", "a4"), ROUTE):
        keys(yml[gate], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"})
        if yml[gate]["verdict"] != verdict or not yml[gate]["strongest_evidence"] or not yml[gate]["strongest_failure"]:
            raise AssertionError(f"gate {gate}")
        count += 2
    if any(type(flag) is not bool or flag for flag in yml["scope_flags"].values()):
        raise AssertionError("YAML forbidden flag")
    count += len(yml["scope_flags"])

    expected_model = {
        "equation": "partial_t omega+u dot grad omega=0, div u=0, curl u=omega on R2",
        "patch": "omega(x,t)=vorticity*indicator of the rotating ellipse E_t",
        "ellipse": "E_0={x^2/a^2+y^2/b^2<1}, a>=b>0",
        "mode_convention": "boundary Fourier label m is measured relative to the instantaneous ellipse principal axes, and lambda_m is the co-rotating-frame frequency with time dependence exp(-i*lambda_m*t)",
    }
    expected_theorem = {
        "rigid_rotation": "E_t is E_0 rotated through Omega*t, Omega=vorticity*a*b/(a+b)^2",
        "love_dispersion": "lambda_m^2=(vorticity^2/4)*([2*m*a*b/(a+b)^2-1]^2-[(a-b)/(a+b)]^(2*m))",
        "symmetry_modes": "lambda_1^2=Omega^2 and lambda_2^2=0 for every ellipse",
        "critical_equation": "for m>=3, delta_m is the unique root in (0,1) of m*(1-delta^2)/2-1-delta^m=0",
        "threshold_order": "delta_m and gamma_m=(1+delta_m)/(1-delta_m) strictly increase with m",
        "threshold_asymptotic": "if c_star=1+W(exp(-1)), then m*(1-delta_m) tends to c_star and gamma_m/m tends to 2/c_star",
        "sharp_wall": "delta_3=1/2 and gamma_3=3; for nonzero vorticity all m>=3 oscillate for gamma<3, m=3 is critical at 3, and m=3 grows exponentially for gamma>3",
        "scope": "spectral linear mode stability only; no nonlinear stability or post-filamentation theorem",
    }
    expected_proof = {
        "dimensionless_variables": "delta=(a-b)/(a+b), kappa=2ab/(a+b)^2=(1-delta^2)/2",
        "factorization": "4*lambda_m^2=vorticity^2*(m*kappa-1-delta^m)*(m*kappa-1+delta^m)",
        "unique_root": "F_m(delta)=m*(1-delta^2)/2-1-delta^m decreases strictly from m/2-1 to -2",
        "positive_second_factor": "G_m(delta)=m*(1-delta^2)/2-1+delta^m is positive on [0,1) for m>=3 because G_m'=m*delta*(delta^(m-2)-1)<0 and G_m(1)=0",
        "ordered_roots": "F_(m+1)(delta)-F_m(delta)=(1-delta^2)/2+delta^m*(1-delta)>0",
        "scaled_root": "c_m=m*(1-delta_m) lies in (1,2) and satisfies c_m-c_m^2/(2m)=1+(1-c_m/m)^m",
        "m3_factor": "16*lambda_3^2=vorticity^2*(1-delta^2)^2*(1-4*delta^2)",
    }
    if not same(value["model"], expected_model) or not same(value["theorem_contract"], expected_theorem) or not same(value["proof_receipts"], expected_proof):
        raise AssertionError("model/theorem/proof contract")
    count += 3

    gammas, expected_aspects, modal_digest = expected_aspect_bundle()
    if len(gammas) != 561:
        raise AssertionError("independent aspect grid")
    count += 1
    count += 64 * len(gammas)
    if not same(value["aspect_rows"], expected_aspects):
        raise AssertionError("aspect/modal grid")
    count += len(expected_aspects)

    thresholds = expected_threshold_rows()
    if not same(value["critical_thresholds"], thresholds):
        raise AssertionError("threshold ledger")
    for left, right in zip(thresholds, thresholds[1:]):
        if F(left["aspect_upper"]) >= F(right["aspect_lower"]):
            raise AssertionError("threshold order")
        count += 1
    count += len(thresholds)

    rigid = expected_rigid_rows()
    if not same(value["rigid_solution_rows"], rigid):
        raise AssertionError("rigid rows")
    count += len(rigid)
    grid = {
        "max_aspect_ratio": 8, "max_reduced_denominator": 16, "distinct_aspect_ratios": 561,
        "max_mode": 64, "modal_cells": 35904, "modal_cells_sha256": modal_digest,
        "critical_modes": 62, "critical_bisection_bits": 96, "rigid_solution_rows": 390,
    }
    if not same(value["finite_grid"], grid):
        raise AssertionError("finite grid receipt")
    count += 1

    atlas = [
        {"face": "a>b>0 and vorticity nonzero", "classification": "rotating Kirchhoff ellipse", "mode_statement": "Love formula and ordered thresholds apply"},
        {"face": "a=b>0 and vorticity nonzero", "classification": "Rankine circular patch", "mode_statement": "the patch shape is stationary because orientation is undefined; the formula reduces to Kelvin-mode frequencies"},
        {"face": "vorticity=0", "classification": "stationary zero patch", "mode_statement": "Omega and every lambda square vanish after the overall vorticity factor"},
        {"face": "a<b", "classification": "axis-swapped convention", "mode_statement": "swap semiaxes before applying gamma>=1"},
        {"face": "b=0 or a infinite", "classification": "singular strip limit", "mode_statement": "excluded from the bounded ellipse theorem"},
        {"face": "gamma=3", "classification": "first spectral threshold", "mode_statement": "m=3 has zero frequency; no nonlinear conclusion is asserted"},
    ]
    collision = {
        "C284": "finite point-vortex relative equilibria, not a distributed constant-vorticity free boundary",
        "C299": "viscously diffusing Lamb-Oseen vorticity, not an inviscid rotating patch",
        "C368": "Polubarinova-Galin Laplacian growth with source or sink, not area-preserving Euler contour transport",
    }
    references = [
        {"doi": "10.1112/plms/s1-25.1.18", "role": "classical owner of the Love modal dispersion relation"},
        {"doi": "10.1063/1.2912991", "role": "modern co-rotating convention and Love-mode formula audit"},
        {"doi": "10.1017/S0022112094000339", "role": "stratified baroclinic extension used only to delimit the two-dimensional Love-mode scope"},
    ]
    nonclaims = [
        "no nonlinear orbital or Lyapunov stability theorem",
        "no finite-amplitude filamentation, fission, or post-instability prediction",
        "no bounded-domain, compressible, viscous, or three-dimensional extension",
        "no arithmetic prime owner or target determinant",
        "no target continuation, zero match, Hilbert-Polya operator, or Route B",
        "no literature-priority claim for the Kirchhoff or Love results",
    ]
    if not same(value["boundary_atlas"], atlas) or not same(value["collision_boundary"], collision):
        raise AssertionError("boundary/collision atlas")
    if not same(value["references"], references) or not same(value["nonclaims"], nonclaims):
        raise AssertionError("sources/nonclaims")
    count += 4
    route = {"tuple": ROUTE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    if not same(value["route_a"], route) or not same(value["scope_flags"], yml["scope_flags"]) or any(value["scope_flags"].values()):
        raise AssertionError("route/scope")
    count += 3
    return count


def main():
    print(f"C372 independent checker: PASS ({check()} assertions)")


if __name__ == "__main__":
    main()
