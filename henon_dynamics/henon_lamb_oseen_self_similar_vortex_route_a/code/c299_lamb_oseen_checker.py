#!/usr/bin/env python3
"""Independent, producer-free checker for the HCS-C299 evidence bundle."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c299_lamb_oseen_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C299/2026-09-02.yaml"
SOURCE = "83c058259c02707d004fca2d6b1a4ebaf5036094"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
EXPECTED_FLAGS = {
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
EXPECTED_BOUNDARY_IDS = [f"B{i}-{name}" for i, name in enumerate([
    "zero-circulation", "positive-age", "zero-age", "positive-viscosity",
    "inviscid-limit", "origin-particle", "long-time-angle",
    "no-fluid-recurrence", "infinite-kinetic-energy",
])]
EXPECTED_NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
    "The circulation Gamma and Gaussian moments are fluid-mechanical source data, not rational-prime labels or prime-power weights.",
    "The Navier-Stokes generator is not asserted to be a Hilbert-Polya operator.",
    "No literature priority is claimed for the classical Lamb-Oseen formula or its standard radial reduction.",
]
EXPECTED_COLLISION = {
    "C206": "C206 studies Couette advection-diffusion Fourier shearing on T times R; C299 classifies radial nonlinear-vorticity self-similarity on R^2, whose advection cancels geometrically.",
    "C207": "C207 classifies Barenblatt profiles for scalar nonlinear diffusion; C299 reconstructs velocity by Biot-Savart and audits circulation, particle angles, enstrophy, and the point-vortex boundary.",
    "energy_warning": "nonzero circulation gives logarithmically divergent whole-plane kinetic energy; only enstrophy and palinstrophy are claimed finite.",
}
EXPECTED_REFERENCES = [
    {
        "identifier": "Oseen-1912-Arkiv-7-no14",
        "role": "classical source owner for the viscous line-vortex profile",
        "verification": "bibliographic metadata cross-checked; no priority claim made",
    },
    {
        "identifier": "10.1007/s00220-004-1254-9",
        "role": "published mathematical context for two-dimensional Oseen-vortex stability",
        "verification": "DOI metadata returned title, authors, journal, volume, pages, and year",
    },
]
EXPECTED_BOUNDARIES = [
    {"boundary_id": "B0-zero-circulation", "status": "exact", "statement": "Gamma=0 gives omega=u=0 for every positive age."},
    {"boundary_id": "B1-positive-age", "status": "exact", "statement": "tau_0>0 gives a smooth finite-enstrophy initial profile."},
    {"boundary_id": "B2-zero-age", "status": "measure boundary", "statement": "tau_0=0 starts from Gamma delta_0 weakly and is smooth only for t>0."},
    {"boundary_id": "B3-positive-viscosity", "status": "domain", "statement": "the classical Gaussian theorem assumes nu>0."},
    {"boundary_id": "B4-inviscid-limit", "status": "weak boundary", "statement": "as nu decreases to zero, omega converges weakly to Gamma delta_0 and u converges off the origin to the point vortex."},
    {"boundary_id": "B5-origin-particle", "status": "exact", "statement": "the continuous velocity extension fixes the particle at r=0."},
    {"boundary_id": "B6-long-time-angle", "status": "asymptotic", "statement": "for Gamma nonzero and r>0, theta(t)=Gamma log(tau)/(8 pi nu)+O(1)."},
    {"boundary_id": "B7-no-fluid-recurrence", "status": "exact obstruction", "statement": "for Gamma nonzero every finite p>1 norm decreases strictly with age, excluding recurrent vorticity states."},
    {"boundary_id": "B8-infinite-kinetic-energy", "status": "exact warning", "statement": "for Gamma nonzero the whole-plane kinetic energy diverges logarithmically at spatial infinity."},
]
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
    value = json.loads(
        path.read_text(), object_pairs_hook=reject_duplicates,
        parse_constant=reject_nonfinite,
    )
    if type(value) is not dict:
        raise TypeError("JSON top level must be an object")
    return value


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


UniqueSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping
)


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


def frac(text: str) -> Fraction:
    if type(text) is not str:
        raise TypeError("rational receipt must be a string")
    value = Fraction(text)
    canonical = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if text != canonical:
        raise ValueError(f"noncanonical rational receipt: {text}")
    return value


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def near(left, right, tolerance=mp.mpf("1e-65")) -> bool:
    left, right = mp.mpf(left), mp.mpf(right)
    return abs(left - right) <= tolerance * max(1, abs(left), abs(right))


def primitive(b, tau):
    return tau * (1 - mp.exp(-b / tau)) - b * mp.ei(-b / tau)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVALUATION)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    route_yaml = strict_yaml(args.evaluation)
    count = 0

    def ok(condition, label):
        nonlocal count
        assert condition, label
        count += 1

    ok(set(data) == {
        "schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
        "source_commit", "scope_literal", "evaluator", "model", "theorem_contract",
        "proof_contract", "enumeration", "route_a", "scope_flags", "nonclaims",
        "collision_boundary", "references", "payload_sha256",
    }, "exact evidence root keys")

    ok(data["payload_sha256"] == canonical_payload_hash(data), "payload digest")
    ok(data["schema"] == "hcs-c299-lamb-oseen-self-similar-vortex-v1", "schema")
    ok(data["candidate_id"] == "HCS-C299", "candidate")
    ok(data["obstruction_id"] == "HEN-O283", "obstruction")
    ok(data["evaluation_date"] == "2026-09-02", "date")
    ok(type(data["fixed_epoch"]) is int and data["fixed_epoch"] == 1788307200, "epoch")
    ok(data["source_commit"] == SOURCE, "source")
    ok(data["scope_literal"] == SCOPE, "scope")
    ok(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    ok(data["route_a"] == {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "route tuple")
    ok(data["scope_flags"] == EXPECTED_FLAGS, "scope flags")
    ok(exact_tree_equal(data["nonclaims"], EXPECTED_NONCLAIMS), "exact nonclaims")
    ok(exact_tree_equal(data["collision_boundary"], EXPECTED_COLLISION), "exact collision ledger")
    ok(exact_tree_equal(data["references"], EXPECTED_REFERENCES), "exact reference ledger")
    ok(set(data["model"]) == {"equation", "closure", "ansatz", "parameters", "clock", "normalization"}, "model keys")
    ok(set(data["theorem_contract"]) == {"classification", "velocity", "lagrangian", "moments", "dissipation", "boundaries"}, "theorem keys")
    ok("continuous real-lift angle" in data["theorem_contract"]["lagrangian"], "unwrapped-angle guard")
    ok(set(data["proof_contract"]) == {"radial_reduction", "uniqueness_ode", "normalization", "lagrangian_primitive", "dissipation", "finite_role"}, "proof keys")
    ok("bounded-at-origin" in data["theorem_contract"]["classification"], "declared-class guard")
    ok("C=0" in data["proof_contract"]["uniqueness_ode"], "integration constant guard")
    ok("finite rows regress" in data["proof_contract"]["finite_role"], "finite-evidence role")

    enumeration = data["enumeration"]
    ok(set(enumeration) == {
        "field_cases", "lagrangian_cases", "boundary_rows", "field_case_count",
        "point_receipt_cells", "moment_receipt_cells", "lp_receipt_cells",
        "lagrangian_receipt_cells", "boundary_receipt_cells", "audited_cell_count",
    }, "enumeration keys")
    fields = enumeration["field_cases"]
    ok(type(fields) is list and len(fields) == 8, "field count")
    point_cells = moment_cells = lp_cells = 0
    for case in fields:
        ok(set(case) == {
            "case_id", "Gamma", "nu", "tau", "core_radius_squared", "point_rows",
            "moment_rows", "lp_rows", "enstrophy_times_8pi_nu_tau",
            "palinstrophy_times_16pi_nu2_tau2", "far_field_energy_log_coefficient_times_4pi",
            "zero_circulation",
        }, "field row keys")
        gamma, nu, tau = map(frac, (case["Gamma"], case["nu"], case["tau"]))
        ok(nu > 0 and tau > 0, "positive domain")
        ok(frac(case["core_radius_squared"]) == 4 * nu * tau, "core scale")
        ok(case["zero_circulation"] is (gamma == 0), "zero circulation convention")
        ok(frac(case["enstrophy_times_8pi_nu_tau"]) == gamma * gamma, "enstrophy receipt")
        ok(frac(case["palinstrophy_times_16pi_nu2_tau2"]) == gamma * gamma, "palinstrophy receipt")
        ok(frac(case["far_field_energy_log_coefficient_times_4pi"]) == gamma * gamma, "energy receipt")
        rows = case["point_rows"]
        ok(type(rows) is list and len(rows) == 9, "point grid")
        for index, row in enumerate(rows):
            ok(set(row) == {
                "x_equals_r2_over_4nu_tau", "r_squared", "exp_minus_x",
                "enclosed_circulation_fraction", "normalized_vorticity_shape",
                "normalized_time_derivative_shape", "normalized_radial_laplacian_shape",
                "advection_term_is_zero", "origin_row",
            }, "point row keys")
            x = frac(row["x_equals_r2_over_4nu_tau"])
            expected_exp = mp.exp(-mpq(x))
            expected_shape = (mpq(x) - 1) * expected_exp
            ok(frac(row["r_squared"]) == 4 * nu * tau * x, "radius receipt")
            ok(near(row["exp_minus_x"], expected_exp), "Gaussian shape")
            ok(near(row["enclosed_circulation_fraction"], 1 - expected_exp), "enclosed circulation")
            ok(near(row["normalized_vorticity_shape"], expected_exp), "normalized vorticity")
            ok(near(row["normalized_time_derivative_shape"], expected_shape), "time derivative")
            ok(near(row["normalized_radial_laplacian_shape"], expected_shape), "radial Laplacian")
            ok(row["advection_term_is_zero"] is True, "radial advection")
            ok(row["origin_row"] is (index == 0 and x == 0), "origin convention")
            point_cells += 1
        moments = case["moment_rows"]
        ok([row["k"] for row in moments] == list(range(9)), "moment orders")
        for row in moments:
            ok(set(row) == {"k", "radial_moment_over_gamma"}, "moment row keys")
            k = row["k"]
            ok(type(k) is int, "integer moment order")
            ok(frac(row["radial_moment_over_gamma"]) == Fraction(math.factorial(k)) * (4 * nu * tau) ** k, "moment")
            moment_cells += 1
        lp_rows = case["lp_rows"]
        ok([row["p"] for row in lp_rows] == list(range(1, 7)), "Lp orders")
        for row in lp_rows:
            ok(set(row) == {"p", "scaled_lp_power_coefficient"}, "Lp row keys")
            p = row["p"]
            ok(frac(row["scaled_lp_power_coefficient"]) == abs(gamma) ** p / p, "Lp coefficient")
            lp_cells += 1

    lagrangian = enumeration["lagrangian_cases"]
    ok(type(lagrangian) is list and len(lagrangian) == 12, "Lagrangian count")
    for row in lagrangian:
        ok(set(row) == {
            "case_id", "Gamma", "nu", "tau_start", "tau_end", "radius_squared",
            "b_equals_r2_over_4nu", "primitive_delta", "direct_quadrature",
            "angle_increment", "radius_is_constant",
        }, "Lagrangian row keys")
        gamma, nu, start, end, r2 = map(frac, (
            row["Gamma"], row["nu"], row["tau_start"], row["tau_end"], row["radius_squared"]
        ))
        b = r2 / (4 * nu)
        bm, sm, tm = mpq(b), mpq(start), mpq(end)
        delta = primitive(bm, tm) - primitive(bm, sm)
        quadrature = mp.quad(lambda z: 1 - mp.exp(-bm / z), [sm, tm])
        angle = mpq(gamma) * delta / (2 * mp.pi * mpq(r2))
        ok(start > 0 and end > start and r2 > 0 and nu > 0, "Lagrangian domain")
        ok(frac(row["b_equals_r2_over_4nu"]) == b, "b receipt")
        ok(near(row["primitive_delta"], delta), "primitive difference")
        ok(near(row["direct_quadrature"], quadrature), "quadrature")
        ok(near(row["primitive_delta"], row["direct_quadrature"]), "primitive/quadrature agreement")
        ok(near(row["angle_increment"], angle), "angle")
        ok(row["radius_is_constant"] is True, "constant radius")

    boundaries = enumeration["boundary_rows"]
    ok([row["boundary_id"] for row in boundaries] == EXPECTED_BOUNDARY_IDS, "boundary IDs")
    ok(exact_tree_equal(boundaries, EXPECTED_BOUNDARIES), "exact boundary ledger")
    ok(enumeration["field_case_count"] == 8, "field count receipt")
    ok(enumeration["point_receipt_cells"] == point_cells == 72, "point count receipt")
    ok(enumeration["moment_receipt_cells"] == moment_cells == 72, "moment count receipt")
    ok(enumeration["lp_receipt_cells"] == lp_cells == 48, "Lp count receipt")
    ok(enumeration["lagrangian_receipt_cells"] == len(lagrangian) == 12, "Lagrangian count receipt")
    ok(enumeration["boundary_receipt_cells"] == len(boundaries) == 9, "boundary count receipt")
    ok(enumeration["audited_cell_count"] == 213, "total count")

    expected_yaml_keys = {
        "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
        "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
        "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
        "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
        "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths",
        "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict",
        "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status",
        "finite_evidence_role", "source_owner_tokens",
    }
    ok(set(route_yaml) == expected_yaml_keys, "exact YAML root keys")
    ok(route_yaml["schema"] == "route-a-evaluation-v0.2.0", "YAML schema")
    ok(route_yaml["candidate_id"] == "HCS-C299" and route_yaml["obstruction_id"] == "HEN-O283", "YAML IDs")
    ok(type(route_yaml["fixed_epoch"]) is int and route_yaml["fixed_epoch"] == 1788307200, "YAML epoch type")
    ok(route_yaml["source_commit"] == SOURCE and route_yaml["scope_literal"] == SCOPE, "YAML scope")
    ok(route_yaml["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    ok(route_yaml["tuple"] == TUPLE and route_yaml["overall_verdict"] == "ROUTE_A_REJECTED", "YAML tuple")
    ok(route_yaml["route_b_invocation_allowed"] is False, "YAML Route-B lock")
    ok(route_yaml["scope_flags"] == EXPECTED_FLAGS, "YAML flags")
    ok(route_yaml["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem status")
    for index, verdict in enumerate(TUPLE):
        branch = route_yaml[f"a{index}"]
        ok(set(branch) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "artifacts"}, f"A{index} keys")
        ok(branch["verdict"] == verdict, f"A{index} verdict")
        ok(type(branch["artifacts"]) is list and branch["artifacts"], f"A{index} artifacts")

    print(f"C299 independent Lamb-Oseen checker: PASS ({count} assertions; producer import forbidden)")


if __name__ == "__main__":
    main()
