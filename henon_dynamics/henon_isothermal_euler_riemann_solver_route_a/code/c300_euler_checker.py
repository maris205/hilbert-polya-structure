#!/usr/bin/env python3
"""Independent, producer-free checker for the HCS-C300 evidence bundle."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c300_euler_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C300/2026-09-02.yaml"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
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
EXPECTED_CASE_IDS = [
    "P01-RR", "P02-RS", "P03-SR", "P04-SS", "P05-ZR", "P06-ZS",
    "P07-RZ", "P08-SZ", "P09-ZZ", "P10-RR", "P11-RS", "P12-SR",
    "P13-SS", "P14-RR-scaled", "P15-RS-scaled", "P16-SR-scaled",
    "P17-SS-scaled", "P18-RR-extreme", "P19-SS-extreme", "P20-RS-asymmetric",
]
EXPECTED_MODEL = {
    "equations": "rho_t+(rho u)_x=0; (rho u)_t+(rho u^2+a^2 rho)_x=0",
    "parameters": "a>0, rho_L>0, rho_R>0, u_L and u_R finite real",
    "clock": "self-similar coordinate xi=x/t for t>0",
    "normalization": "physical density and velocity; no arithmetic normalization",
}
EXPECTED_THEOREM = {
    "root": "one strictly increasing scalar equation has exactly one rho_star>0 for every declared datum",
    "patterns": "the two density comparisons give all four nondegenerate shock/rarefaction patterns and all zero-wave boundaries",
    "entropy": "each shock has strict negative mechanical entropy production and each fan is an entropy equality",
    "vacuum": "finite velocities and positive input densities at a>0 never create an isothermal vacuum",
    "pressureless": "a down to zero is a singular excluded boundary, not a theorem corollary",
}
EXPECTED_PROOF = {
    "monotonicity": "each wave function is C1 strictly increasing from minus infinity to plus infinity",
    "wave_signs": "family 1 uses the negative Hugoniot sign and family 2 the positive sign",
    "entropy_formula": "shock production equals a^3 rho_0 sqrt(r)[log r-(r-r^{-1})/2], strictly negative for r>1",
    "finite_role": "finite cases regress formulas and signs; the full-data theorem is analytic",
}
EXPECTED_NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
    "Densities, characteristic speeds, and wave families are source PDE data, not rational-prime labels or prime-power weights.",
    "The entropy solution semigroup is not asserted to be a Hilbert-Polya operator.",
    "No literature priority is claimed for the classical Lax Riemann construction or isothermal wave curves.",
]
EXPECTED_COLLISION = {
    "C195": "C195 is scalar periodic viscous Burgers dynamics; C300 is a two-field inviscid Riemann solver with two genuinely nonlinear families and four wave patterns.",
    "pressureless_warning": "vacuum and delta-shock behavior at a=0 are excluded singular limits, not imported conclusions.",
}
EXPECTED_REFERENCES = [
    {"identifier": "10.1002/cpa.3160100406", "role": "classical Lax hyperbolic-system and Riemann construction owner"},
    {"identifier": "10.1090/mmono/055", "role": "isothermal gas-dynamics and Riemann-invariant context"},
    {"identifier": "10.1007/978-3-642-04048-1", "role": "modern entropy-solution framework"},
]
EXPECTED_BOUNDARIES = [
    {"boundary_id": "B0-positive-data", "status": "theorem domain", "statement": "a>0 and both input densities positive with finite velocities."},
    {"boundary_id": "B1-no-vacuum", "status": "exact", "statement": "the monotone root is positive for every datum in the theorem chamber."},
    {"boundary_id": "B2-zero-wave", "status": "included", "statement": "equality with either reference density deletes exactly that wave."},
    {"boundary_id": "B3-constant-data", "status": "included", "statement": "two zero waves occur exactly for identical left and right states."},
    {"boundary_id": "B4-density-scaling", "status": "exact symmetry", "statement": "common positive density scaling preserves velocities, ratios, types, and speeds."},
    {"boundary_id": "B5-vacuum-input", "status": "excluded", "statement": "zero-density input traces need a separate boundary theory."},
    {"boundary_id": "B6-pressureless-separation", "status": "singular limit", "statement": "fixed separating data can drive the intermediate density exponentially to zero as a decreases."},
    {"boundary_id": "B7-pressureless-compression", "status": "singular limit", "statement": "fixed compressive data can drive the intermediate density to infinity and toward concentration as a decreases."},
]


def route_branch(verdict, status, evidence, failure, artifacts):
    return {
        "verdict": verdict, "evidence_status": status, "strongest_evidence": evidence,
        "strongest_failure": failure, "artifacts": artifacts,
    }


EXPECTED_EVALUATION = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C300",
    "title": "Complete positive-density Riemann atlas for one-dimensional isothermal Euler flow",
    "evaluation_date": "2026-09-02",
    "source_commit": SOURCE,
    "fixed_epoch": 1788307200,
    "scope_literal": SCOPE,
    "evaluator_authority": "route-a-evaluator",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O284",
    "candidate_definition": "The self-similar Lax entropy Riemann solver for one-dimensional isothermal Euler flow with positive left and right densities and sound speed a>0.",
    "family": "strictly hyperbolic two-field conservation law and four-pattern Riemann dynamics",
    "phase_space": "positive-density conservative states U=(rho,rho u) separated by one initial discontinuity",
    "dynamics": "rho_t+(rho u)_x=0 and (rho u)_t+(rho u^2+a^2 rho)_x=0",
    "parameters": "a>0; rho_L>0; rho_R>0; u_L,u_R finite real",
    "parameter_provenance": "the theorem covers every datum in the full positive-density finite-velocity chamber",
    "arithmetic_origin": "none; density, velocity, sound speed, shock speed, and entropy production are source PDE data",
    "clock": "physical time t and similarity coordinate xi=x/t",
    "normalization": "physical density and velocity; common positive density scaling is recorded as a symmetry",
    "determinant_convention": "not applicable; the scalar monotone root equation is not a determinant",
    "orbit_cutoff": "one global Riemann theorem; finite patterns are regression evidence only",
    "precision": "exact rational parameters plus 72-digit logarithmic, radical, residual, and entropy receipts",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor laws, target functional equations, target zeros, and Hilbert--Polya operators",
    "artifact_paths": ["results/c300_euler_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "a0": route_branch(
        "A0_FAIL", "exact negative classification",
        "all wave curves and intermediate states are explicit source-side PDE data",
        "no rational-prime local datum or target Euler factor is constructed",
        ["THEOREM_PACKAGE.md", "SOURCE_AUDIT.md"],
    ),
    "a1": route_branch(
        "A1_FAIL", "exact structural mismatch",
        "the entropy solution contains two ordered elementary waves and one intermediate sector",
        "a finite self-similar fan is not a recurrent primitive-periodic-orbit system",
        ["THEOREM_PACKAGE.md", "paper/main.pdf"],
    ),
    "a2": route_branch(
        "A2_FAIL", "exact negative classification",
        "wave speeds order events in the physical similarity coordinate",
        "xi=x/t is not an arithmetic clock or logarithmic rational-prime norm",
        ["THEOREM_PACKAGE.md"],
    ),
    "a3": route_branch(
        "A3_FAIL", "exact negative classification",
        "one monotone scalar equation determines the intermediate density",
        "the scalar root equation is not a target determinant, completed function, or functional equation",
        ["results/c300_euler_evidence.json", "paper/main.pdf"],
    ),
    "a4": route_branch(
        "A4_FAIL", "entropy-semigroup mismatch",
        "a strictly convex mechanical entropy selects compressive shocks",
        "the nonlinear entropy solution semigroup is not a certified self-adjoint Hilbert--Polya operator",
        ["SOURCE_AUDIT.md", "paper/main.pdf"],
    ),
    "tuple": TUPLE,
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no bad-prime, Euler-factor, or root-number datum exists under the frozen scope",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "regression evidence only; monotonicity, wave construction, Lax ordering, entropy production, and no-vacuum are analytic",
    "source_owner_tokens": ["10.1002/cpa.3160100406", "10.1090/mmono/055", "10.1007/978-3-642-04048-1"],
}
mp.mp.dps = 90


def reject_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON token: {value}")


def strict_json(path: Path) -> dict:
    result = json.loads(path.read_text(), object_pairs_hook=reject_duplicates, parse_constant=reject_nonfinite)
    if type(result) is not dict:
        raise TypeError("JSON top level must be an object")
    return result


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge keys are forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str:
            raise TypeError("YAML keys must be strings")
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def strict_yaml(path: Path) -> dict:
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    result = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(result) is not dict:
        raise TypeError("YAML top level must be a mapping")
    return result


def canonical_payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def exact_tree_equal(actual, expected) -> bool:
    if type(actual) is not type(expected):
        return False
    if type(expected) is dict:
        return set(actual) == set(expected) and all(exact_tree_equal(actual[key], expected[key]) for key in expected)
    if type(expected) is list:
        return len(actual) == len(expected) and all(exact_tree_equal(a, e) for a, e in zip(actual, expected))
    return actual == expected


def frac(text):
    if type(text) is not str:
        raise TypeError("exact rational must be a string")
    value = Fraction(text)
    canonical = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if text != canonical:
        raise ValueError(f"noncanonical rational receipt: {text}")
    return value


DECIMAL_RE = re.compile(r"-?(?:0|[1-9][0-9]*)\.[0-9]+(?:e-?[1-9][0-9]*)?")


def decimal(text):
    if type(text) is not str:
        raise TypeError("decimal receipt must be a string")
    if DECIMAL_RE.fullmatch(text) is None:
        raise ValueError(f"noncanonical decimal syntax: {text}")
    value = mp.mpf(text)
    canonical = "0.0" if value == 0 else mp.nstr(value, 72, strip_zeros=False)
    if text != canonical:
        raise ValueError(f"noncanonical decimal receipt: {text}")
    return value


def mpq(value: Fraction):
    return mp.mpf(value.numerator) / value.denominator


def near(left, right, tolerance=mp.mpf("2e-65")):
    left, right = mp.mpf(left), mp.mpf(right)
    return abs(left - right) <= tolerance * max(1, abs(left), abs(right))


def fcurve(rho, rho0, sound):
    if rho <= rho0:
        return sound * mp.log(rho / rho0)
    return sound * (rho - rho0) / mp.sqrt(rho * rho0)


def phi(rho, rho_l, rho_r, u_l, u_r, sound):
    return fcurve(rho, rho_l, sound) + fcurve(rho, rho_r, sound) + u_r - u_l


def solve_root(rho_l, rho_r, u_l, u_r, sound):
    center = (mp.log(rho_l) + mp.log(rho_r)) / 2
    low, high = center - 1, center + 1
    while phi(mp.exp(low), rho_l, rho_r, u_l, u_r, sound) >= 0:
        low -= 2
    while phi(mp.exp(high), rho_l, rho_r, u_l, u_r, sound) <= 0:
        high += 2
    for _ in range(420):
        mid = (low + high) / 2
        if phi(mp.exp(mid), rho_l, rho_r, u_l, u_r, sound) < 0:
            low = mid
        else:
            high = mid
    return mp.exp((low + high) / 2)


def entropy(rho, u, sound):
    return rho * u * u / 2 + sound * sound * rho * mp.log(rho)


def entropy_flux(rho, u, sound):
    return u * (entropy(rho, u, sound) + sound * sound * rho)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C300 checker forbids optimized Python; assertions are release invariants")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVALUATION)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    route_yaml = strict_yaml(args.evaluation)
    count = 0

    def ok(condition, label):
        nonlocal count
        if not bool(condition):
            raise AssertionError(label)
        count += 1

    ok(set(data) == {
        "schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
        "source_commit", "scope_literal", "evaluator", "model", "theorem_contract",
        "proof_contract", "enumeration", "route_a", "scope_flags", "nonclaims",
        "collision_boundary", "references", "payload_sha256",
    }, "exact evidence root keys")
    ok(data["payload_sha256"] == canonical_payload_hash(data), "payload hash")
    ok(type(data["payload_sha256"]) is str and re.fullmatch(r"[0-9a-f]{64}", data["payload_sha256"]) is not None, "payload hash type")
    ok(type(data["schema"]) is str and data["schema"] == "hcs-c300-isothermal-euler-riemann-v1", "schema")
    ok(type(data["candidate_id"]) is str and type(data["obstruction_id"]) is str and data["candidate_id"] == "HCS-C300" and data["obstruction_id"] == "HEN-O284", "IDs")
    ok(type(data["evaluation_date"]) is str and data["evaluation_date"] == "2026-09-02", "date")
    ok(type(data["fixed_epoch"]) is int and data["fixed_epoch"] == 1788307200, "epoch")
    ok(type(data["source_commit"]) is str and type(data["scope_literal"]) is str and data["source_commit"] == SOURCE and data["scope_literal"] == SCOPE, "source/scope")
    ok(exact_tree_equal(data["evaluator"], {"version": "0.2.0", "sha256": EVALUATOR}), "evaluator")
    ok(exact_tree_equal(data["model"], EXPECTED_MODEL), "exact model")
    ok(exact_tree_equal(data["theorem_contract"], EXPECTED_THEOREM), "exact theorem contract")
    ok(exact_tree_equal(data["proof_contract"], EXPECTED_PROOF), "exact proof contract")
    ok(exact_tree_equal(data["route_a"], {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}), "tuple")
    ok(exact_tree_equal(data["scope_flags"], FLAGS), "flags")
    ok(exact_tree_equal(data["nonclaims"], EXPECTED_NONCLAIMS), "exact nonclaims")
    ok(exact_tree_equal(data["collision_boundary"], EXPECTED_COLLISION), "exact collision boundary")
    ok(exact_tree_equal(data["references"], EXPECTED_REFERENCES), "exact references")

    enumeration = data["enumeration"]
    ok(type(enumeration) is dict and set(enumeration) == {
        "cases", "scaling_pairs", "pressureless_probes", "boundary_rows",
        "case_count", "wave_count", "wave_kind_counts", "pattern_counts",
        "root_receipt_cells", "wave_receipt_cells", "scaling_receipt_cells",
        "pressureless_receipt_cells", "boundary_receipt_cells", "audited_cell_count",
    }, "exact enumeration keys")
    cases = enumeration["cases"]
    ok(type(cases) is list and len(cases) == 20, "case count")
    ok([case.get("case_id") for case in cases] == EXPECTED_CASE_IDS and len({case.get("case_id") for case in cases}) == 20, "ordered unique case IDs")
    kinds = Counter()
    patterns = Counter()
    for case in cases:
        ok(type(case) is dict and set(case) == {
            "case_id", "exact_parameters", "derived_data", "root_receipts", "pattern",
            "wave_1", "wave_2", "intermediate_speed_gap", "waves_strictly_ordered",
        }, "exact case keys")
        ok(type(case["case_id"]) is str and type(case["pattern"]) is str, "case string types")
        ok(type(case["waves_strictly_ordered"]) is bool, "case bool type")
        decimal(case["intermediate_speed_gap"])
        exact = case["exact_parameters"]
        ok(type(exact) is dict and set(exact) == {"a", "rho_L", "rho_R", "rho_star", "u_star"}, "exact parameter keys")
        ok(all(type(exact[key]) is str for key in exact), "exact parameter string types")
        a_q, rl_q, rr_q, rs_q, us_q = map(frac, (
            exact["a"], exact["rho_L"], exact["rho_R"], exact["rho_star"], exact["u_star"]
        ))
        sound, rho_l, rho_r, rho_star, u_star = map(mpq, (a_q, rl_q, rr_q, rs_q, us_q))
        ok(sound > 0 and rho_l > 0 and rho_r > 0 and rho_star > 0, "positive chamber")
        derived = case["derived_data"]
        ok(type(derived) is dict and set(derived) == {"f_left", "f_right", "u_L", "u_R", "velocity_jump_uR_minus_uL"}, "derived-data keys")
        ok(all(type(derived[key]) is str for key in derived), "derived-data string types")
        for value in derived.values():
            decimal(value)
        f_l, f_r = fcurve(rho_star, rho_l, sound), fcurve(rho_star, rho_r, sound)
        u_l, u_r = u_star + f_l, u_star - f_r
        ok(near(derived["f_left"], f_l), "left wave curve")
        ok(near(derived["f_right"], f_r), "right wave curve")
        ok(near(derived["u_L"], u_l), "left velocity")
        ok(near(derived["u_R"], u_r), "right velocity")
        ok(near(derived["velocity_jump_uR_minus_uL"], u_r - u_l), "velocity jump")
        root = solve_root(rho_l, rho_r, u_l, u_r, sound)
        receipts = case["root_receipts"]
        ok(type(receipts) is dict and set(receipts) == {
            "phi_at_declared_root", "independently_reconstructed_root", "root_absolute_error",
            "recovered_u_star_left", "recovered_u_star_right", "root_is_strictly_positive",
        }, "root-receipt keys")
        ok(all(type(receipts[key]) is str for key in (
            "phi_at_declared_root", "independently_reconstructed_root", "root_absolute_error",
            "recovered_u_star_left", "recovered_u_star_right",
        )), "root decimal string types")
        for key in ("phi_at_declared_root", "independently_reconstructed_root", "root_absolute_error", "recovered_u_star_left", "recovered_u_star_right"):
            decimal(receipts[key])
        ok(type(receipts["root_is_strictly_positive"]) is bool, "root bool type")
        ok(near(receipts["phi_at_declared_root"], 0), "declared root residual")
        ok(near(receipts["independently_reconstructed_root"], root), "root reconstruction")
        ok(near(root, rho_star), "known/reconstructed root")
        ok(decimal(receipts["root_absolute_error"]) < mp.mpf("1e-65"), "root error")
        ok(near(receipts["recovered_u_star_left"], u_star), "left u star")
        ok(near(receipts["recovered_u_star_right"], u_star), "right u star")
        ok(receipts["root_is_strictly_positive"] is True, "root positivity")

        expected_kinds = [
            "rarefaction" if rho_star < rho_l else "shock" if rho_star > rho_l else "zero",
            "rarefaction" if rho_star < rho_r else "shock" if rho_star > rho_r else "zero",
        ]
        expected_pattern = f"{expected_kinds[0][0].upper()}-{expected_kinds[1][0].upper()}"
        ok(case["pattern"] == expected_pattern, "pattern")
        patterns[expected_pattern] += 1
        waves = (case["wave_1"], case["wave_2"])
        rightmost = leftmost = None
        for family, wave, kind in zip((1, 2), waves, expected_kinds):
            kinds[kind] += 1
            common_keys = {"family", "kind", "zero_strength"}
            rare_keys = common_keys | {"left_edge", "right_edge", "midpoint"}
            shock_keys = common_keys | {
                "compression_ratio", "speed_from_outer", "speed_from_star",
                "mass_jump_residual", "momentum_jump_residual", "entropy_production",
                "closed_entropy_production", "lax_lower_gap", "lax_upper_gap",
                "strict_entropy", "strict_lax",
            }
            zero_keys = common_keys | {"characteristic_speed", "density_jump", "velocity_jump"}
            expected_wave_keys = rare_keys if kind == "rarefaction" else shock_keys if kind == "shock" else zero_keys
            ok(type(wave) is dict and set(wave) == expected_wave_keys, "exact wave keys")
            ok(type(wave["family"]) is int and not isinstance(wave["family"], bool), "wave family integer type")
            ok(type(wave["kind"]) is str and type(wave["zero_strength"]) is bool, "wave tag types")
            ok(wave["family"] == family and wave["kind"] == kind, "wave identity")
            ok(wave["zero_strength"] is (kind == "zero"), "zero flag")
            if family == 1:
                outer_rho, outer_u = rho_l, u_l
            else:
                outer_rho, outer_u = rho_r, u_r
            if kind == "rarefaction":
                ok(type(wave["left_edge"]) is str and type(wave["right_edge"]) is str, "fan edge string types")
                decimal(wave["left_edge"])
                decimal(wave["right_edge"])
                mid = wave["midpoint"]
                ok(type(mid) is dict and set(mid) == {"xi", "rho", "u", "characteristic_residual", "invariant_residual"}, "fan midpoint keys")
                ok(all(type(mid[key]) is str for key in mid), "fan midpoint string types")
                for value in mid.values():
                    decimal(value)
                if family == 1:
                    edge_l, edge_r = u_l - sound, u_star - sound
                    xi = (edge_l + edge_r) / 2
                    mid_u = xi + sound
                    mid_rho = rho_l * mp.exp((u_l - mid_u) / sound)
                    invariant = mid_u + sound * mp.log(mid_rho) - (u_l + sound * mp.log(rho_l))
                else:
                    edge_l, edge_r = u_star + sound, u_r + sound
                    xi = (edge_l + edge_r) / 2
                    mid_u = xi - sound
                    mid_rho = rho_r * mp.exp((mid_u - u_r) / sound)
                    invariant = mid_u - sound * mp.log(mid_rho) - (u_r - sound * mp.log(rho_r))
                ok(near(wave["left_edge"], edge_l) and near(wave["right_edge"], edge_r), "fan edges")
                ok(edge_r > edge_l, "expansive fan")
                ok(near(mid["xi"], xi) and near(mid["u"], mid_u) and near(mid["rho"], mid_rho), "fan midpoint")
                ok(near(mid["characteristic_residual"], 0), "fan characteristic")
                ok(near(mid["invariant_residual"], invariant) and near(invariant, 0), "fan invariant")
                speed = edge_r if family == 1 else edge_l
            elif kind == "shock":
                decimal_keys = (
                    "compression_ratio", "speed_from_outer", "speed_from_star",
                    "mass_jump_residual", "momentum_jump_residual", "entropy_production",
                    "closed_entropy_production", "lax_lower_gap", "lax_upper_gap",
                )
                ok(all(type(wave[key]) is str for key in decimal_keys), "shock decimal string types")
                for key in decimal_keys:
                    decimal(wave[key])
                ok(type(wave["strict_entropy"]) is bool and type(wave["strict_lax"]) is bool, "shock bool types")
                ratio = rho_star / outer_rho
                if family == 1:
                    speed = u_l - sound * mp.sqrt(ratio)
                    alternate = u_star - sound / mp.sqrt(ratio)
                    left_rho, left_u, right_rho, right_u = rho_l, u_l, rho_star, u_star
                    lower_gap = speed - (u_star - sound)
                    upper_gap = (u_l - sound) - speed
                    low_density = rho_l
                else:
                    speed = u_r + sound * mp.sqrt(ratio)
                    alternate = u_star + sound / mp.sqrt(ratio)
                    left_rho, left_u, right_rho, right_u = rho_star, u_star, rho_r, u_r
                    lower_gap = speed - (u_r + sound)
                    upper_gap = (u_star + sound) - speed
                    low_density = rho_r
                ok(near(wave["compression_ratio"], ratio) and ratio > 1, "compression")
                ok(near(wave["speed_from_outer"], speed), "shock speed outer")
                ok(near(wave["speed_from_star"], alternate) and near(speed, alternate), "shock speed star")
                mass = speed * (right_rho - left_rho) - (right_rho * right_u - left_rho * left_u)
                momentum = speed * (right_rho * right_u - left_rho * left_u)
                momentum -= (right_rho * right_u**2 + sound**2 * right_rho) - (left_rho * left_u**2 + sound**2 * left_rho)
                production = entropy_flux(right_rho, right_u, sound) - entropy_flux(left_rho, left_u, sound)
                production -= speed * (entropy(right_rho, right_u, sound) - entropy(left_rho, left_u, sound))
                closed = sound**3 * low_density * mp.sqrt(ratio) * (mp.log(ratio) - (ratio - 1 / ratio) / 2)
                ok(near(wave["mass_jump_residual"], mass) and near(mass, 0), "mass RH")
                ok(near(wave["momentum_jump_residual"], momentum) and near(momentum, 0), "momentum RH")
                ok(near(wave["entropy_production"], production), "entropy direct")
                ok(near(wave["closed_entropy_production"], closed) and near(production, closed), "entropy closed")
                ok(production < 0 and wave["strict_entropy"] is True, "strict entropy")
                ok(near(wave["lax_lower_gap"], lower_gap) and lower_gap > 0, "Lax lower")
                ok(near(wave["lax_upper_gap"], upper_gap) and upper_gap > 0, "Lax upper")
                ok(wave["strict_lax"] is True, "Lax flag")
            else:
                ok(all(type(wave[key]) is str for key in ("characteristic_speed", "density_jump", "velocity_jump")), "zero-wave string types")
                for key in ("characteristic_speed", "density_jump", "velocity_jump"):
                    decimal(wave[key])
                characteristic = u_star - sound if family == 1 else u_star + sound
                ok(near(wave["characteristic_speed"], characteristic), "zero characteristic")
                ok(near(wave["density_jump"], 0) and near(wave["velocity_jump"], 0), "zero jump")
                speed = characteristic
            if family == 1:
                rightmost = speed
            else:
                leftmost = speed
        gap = leftmost - rightmost
        ok(gap > 0 and near(case["intermediate_speed_gap"], gap), "family ordering gap")
        ok(case["waves_strictly_ordered"] is True, "ordering flag")

    expected_kind_counts = {"rarefaction": 17, "shock": 17, "zero": 6}
    expected_pattern_counts = {
        "R-R": 4, "R-S": 4, "R-Z": 1, "S-R": 3, "S-S": 4,
        "S-Z": 1, "Z-R": 1, "Z-S": 1, "Z-Z": 1,
    }
    ok(exact_tree_equal(dict(sorted(kinds.items())), expected_kind_counts) and exact_tree_equal(enumeration["wave_kind_counts"], expected_kind_counts), "wave spectrum")
    ok(exact_tree_equal(dict(sorted(patterns.items())), expected_pattern_counts) and exact_tree_equal(enumeration["pattern_counts"], expected_pattern_counts), "pattern spectrum")
    count_keys = (
        "case_count", "wave_count", "root_receipt_cells", "wave_receipt_cells",
        "scaling_receipt_cells", "pressureless_receipt_cells", "boundary_receipt_cells",
        "audited_cell_count",
    )
    ok(all(type(enumeration[key]) is int and not isinstance(enumeration[key], bool) for key in count_keys), "integer receipt types")
    ok(enumeration["case_count"] == 20 and enumeration["wave_count"] == 40, "case/wave receipts")
    ok(enumeration["root_receipt_cells"] == 120, "root cells")
    ok(enumeration["wave_receipt_cells"] == 273, "wave cells")

    by_id = {case["case_id"]: case for case in cases}
    scaling = enumeration["scaling_pairs"]
    ok(type(scaling) is list and len(scaling) == 4, "scaling pair count")
    for row in scaling:
        ok(type(row) is dict and set(row) == {
            "base_case", "scaled_case", "density_factor", "same_pattern", "same_u_L",
            "same_u_R", "same_u_star", "rho_star_scaled_exactly",
        }, "scaling row keys")
        ok(all(type(row[key]) is str for key in ("base_case", "scaled_case", "density_factor", "same_u_L", "same_u_R", "same_u_star")), "scaling string types")
        ok(type(row["same_pattern"]) is bool and type(row["rho_star_scaled_exactly"]) is bool, "scaling bool types")
        for key in ("same_u_L", "same_u_R", "same_u_star"):
            decimal(row[key])
        base, scaled = by_id[row["base_case"]], by_id[row["scaled_case"]]
        factor = frac(row["density_factor"])
        for name in ("rho_L", "rho_R", "rho_star"):
            ok(frac(scaled["exact_parameters"][name]) == factor * frac(base["exact_parameters"][name]), "scaled density")
        ok(row["same_pattern"] is True and base["pattern"] == scaled["pattern"], "scaled pattern")
        ok(near(row["same_u_L"], 0) and near(row["same_u_R"], 0) and near(row["same_u_star"], 0), "scaled velocities")
        ok(row["rho_star_scaled_exactly"] is True, "scaled root flag")
    ok(enumeration["scaling_receipt_cells"] == 20, "scaling cells")

    probes = enumeration["pressureless_probes"]
    ok(type(probes) is list and len(probes) == 4, "pressureless probe count")
    previous_sep, previous_comp = mp.inf, 0
    for row in probes:
        ok(type(row) is dict and set(row) == {
            "a", "fixed_states", "separating_rho_star", "separating_closed_form",
            "compressive_rho_star", "compressive_sqrt_root_closed_form",
            "separating_tends_to_zero", "compressive_grows",
        }, "pressureless row keys")
        ok(all(type(row[key]) is str for key in (
            "a", "fixed_states", "separating_rho_star", "separating_closed_form",
            "compressive_rho_star", "compressive_sqrt_root_closed_form",
        )), "pressureless string types")
        ok(type(row["separating_tends_to_zero"]) is bool and type(row["compressive_grows"]) is bool, "pressureless bool types")
        ok(row["fixed_states"] == "rho_L=rho_R=1; |u_L-u_R|=1", "pressureless fixed data")
        ok(row["separating_closed_form"] == "exp(-1/(2a))" and row["compressive_sqrt_root_closed_form"] == "(1/(2a)+sqrt(1/(4a^2)+4))/2", "pressureless formula labels")
        decimal(row["separating_rho_star"])
        decimal(row["compressive_rho_star"])
        sound = mpq(frac(row["a"]))
        sep = mp.exp(-1 / (2 * sound))
        c = 1 / (2 * sound)
        y = (c + mp.sqrt(c * c + 4)) / 2
        comp = y * y
        ok(near(row["separating_rho_star"], sep), "separating probe")
        ok(near(row["compressive_rho_star"], comp), "compressive probe")
        ok(sep < previous_sep and comp > previous_comp, "nonuniform directions")
        ok(row["separating_tends_to_zero"] is True and row["compressive_grows"] is True, "pressure flags")
        previous_sep, previous_comp = sep, comp
    ok(enumeration["pressureless_receipt_cells"] == 16, "pressure cells")
    boundaries = enumeration["boundary_rows"]
    ok(exact_tree_equal(boundaries, EXPECTED_BOUNDARIES), "exact boundary ledger")
    ok(enumeration["boundary_receipt_cells"] == 8, "boundary cells")
    ok(enumeration["audited_cell_count"] == 437, "total cells")

    ok(exact_tree_equal(route_yaml, EXPECTED_EVALUATION), "exact YAML semantic tree and types")
    ok(route_yaml["schema"] == "route-a-evaluation-v0.2.0", "YAML schema")
    ok(route_yaml["candidate_id"] == "HCS-C300" and route_yaml["obstruction_id"] == "HEN-O284", "YAML IDs")
    ok(type(route_yaml["fixed_epoch"]) is int and route_yaml["fixed_epoch"] == 1788307200, "YAML epoch")
    ok(route_yaml["source_commit"] == SOURCE and route_yaml["scope_literal"] == SCOPE, "YAML scope")
    ok(route_yaml["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    ok(route_yaml["tuple"] == TUPLE and route_yaml["overall_verdict"] == "ROUTE_A_REJECTED", "YAML tuple")
    ok(route_yaml["route_b_invocation_allowed"] is False and route_yaml["scope_flags"] == FLAGS, "YAML flags")
    ok(route_yaml["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem")
    for index, verdict in enumerate(TUPLE):
        branch = route_yaml[f"a{index}"]
        ok(set(branch) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "artifacts"}, "branch keys")
        ok(branch["verdict"] == verdict and type(branch["artifacts"]) is list and branch["artifacts"], "branch value")

    print(f"C300 independent isothermal-Euler checker: PASS ({count} assertions; producer import forbidden)")


if __name__ == "__main__":
    main()
