#!/usr/bin/env python3
"""Producer-independent checker for the HCS-C314 evidence contract."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c314_angenent_evidence.json"
DEFAULT_EVAL = ROOT / "evaluations/route_a/HCS-C314/2026-09-03.yaml"
SOURCE = "1938bae19e5a92f9ce2411aafdc68323bd641bd0"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATION_SEMANTIC_SHA256 = "3693ad2d8e0832465ea07701c94cfc55df176c1b74d9f9a2347931578564e4c2"
EVALUATION_RAW_SHA256 = "fdcfeb38069d8a86730b28cc5bcb8aee314bcddffb9eaf3652912fdef7590dd2"
R_VALUES = ["1/64", "1/32", "1/16", "1/12", "1/10", "1/8", "1/6", "1/5", "1/4", "1/3", "2/5", "1/2", "3/5", "2/3", "3/4", "4/5", "7/8", "9/10", "15/16", "31/32"]
mp.mp.dps = 90


def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def strict_json(path: Path):
    value = json.loads(path.read_text(), object_pairs_hook=pairs, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(f"nonfinite {x}")))
    if type(value) is not dict:
        raise TypeError("JSON root must be object")
    return value


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {key: [(tag, pattern) for tag, pattern in vals if tag != "tag:yaml.org,2002:timestamp"] for key, vals in yaml.SafeLoader.yaml_implicit_resolvers.items()}


def mapping(loader, node, deep=False):
    out = {}
    for key_node, val_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate/non-string YAML key")
        out[key] = loader.construct_object(val_node, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be mapping")
    return value


def digest(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def close(receipt, expected, tol=mp.mpf("2e-66")):
    if type(receipt) is not str:
        raise AssertionError("decimal is not string")
    actual = mp.mpf(receipt)
    if not mp.isfinite(actual) or abs(actual - expected) > tol * max(1, abs(expected)):
        raise AssertionError(f"decimal mismatch {receipt} != {expected}")


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C314 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVAL)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    evaluation = strict_yaml(args.evaluation)
    checks = 0
    evaluation_digest = hashlib.sha256(json.dumps(evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    if evaluation_digest != EVALUATION_SEMANTIC_SHA256:
        raise AssertionError("evaluation semantic digest mismatch")
    checks += 1
    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest() != EVALUATION_RAW_SHA256:
        raise AssertionError("evaluation raw-byte digest mismatch")
    checks += 1
    if digest(data) != data.get("payload_sha256"):
        raise AssertionError("payload hash mismatch")
    checks += 1
    expected_top = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "model", "theorem_contract", "parameter_rows", "extinction_rows", "grim_rows", "boundary_atlas", "collision_boundary", "route_a", "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256"}
    if set(data) != expected_top:
        raise AssertionError("top-level key set")
    if (data["schema"], data["candidate_id"], data["obstruction_id"], data["source_commit"], data["scope_literal"], data["fixed_epoch"]) != ("hcs-c314-angenent-oval-v1", "HCS-C314", "HEN-O298", SOURCE, SCOPE, 1788393600):
        raise AssertionError("identity/provenance")
    if data["evaluation_date"] != "2026-09-03" or data["evaluator"] != {"version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}:
        raise AssertionError("date/evaluator")
    checks += 7
    expected_model = {"flow": "planar curve-shortening flow with inward normal velocity equal to curvature", "time_domain": "-infinity<t<0", "implicit_curve": "central component {cos(x)=exp(t) cosh(y), |x|<pi/2}; the unrestricted level set is the disjoint union of its 2pi-translates", "arrival_time": "T(x,y)=log(cos(x))-log(cosh(y)) on |x|<pi/2"}
    if data["model"] != expected_model:
        raise AssertionError("model contract")
    expected_theorem = {
        "solution": "the central component is a smooth embedded strictly convex compact ancient solution with extinction at t=0; the unrestricted periodic level set is not a single curve",
        "geometry": "width, height, curvature extrema, area, and elliptic-integral length are exact",
        "foliation": "the central negative-time ovals foliate the open strip minus the origin; the extinction point is the zero-time leaf, and the arrival equation holds away from it",
        "forward_limit": "parabolic extinction rescaling converges smoothly to the unit circle",
        "backward_limit": "the two tips converge after translation to opposite Grim-Reaper profiles on compact sub-strips",
    }
    if data["theorem_contract"] != expected_theorem:
        raise AssertionError("theorem contract")
    if data["route_a"] != {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}:
        raise AssertionError("Route-A contract")
    if len(data["scope_flags"]) != 9 or any(type(v) is not bool or v for v in data["scope_flags"].values()):
        raise AssertionError("scope firewall")
    boundary = [
        {"face": "t=0", "status": "single extinction point, not a smooth timeslice"},
        {"face": "t=-infinity", "status": "strip and two-tip asymptotic limit, not an added timeslice"},
        {"face": "classification", "status": "the package does not reprove the literature-wide classification of convex ancient solutions"},
        {"face": "dimension", "status": "planar curve shortening only; no higher-dimensional ancient-oval theorem"},
    ]
    collision = {"C281": "homogeneous Ricci flow on products of spheres, not a planar embedded curve flow", "C299": "a radial Navier--Stokes self-similar vortex, not ancient curve shortening", "C304": "a periodic linear Cahn--Hilliard semigroup; its idea report reserved but did not package the Grim Reaper"}
    nonclaims = ["No novelty or priority is claimed for the Angenent oval or its classical formulas.", "No all-solution classification, nonlinear stability theorem, or higher-dimensional extension is claimed.", "No target arithmetic datum, Euler factor, root number, automorphy, divisor law, functional equation, zero match, or Hilbert--Polya operator is asserted."]
    references = [{"doi": "10.1007/978-1-4612-0393-3_2", "role": "Angenent 1992 explicit oval-formula ownership"}, {"arxiv": "0806.1757", "role": "compact convex ancient-solution classification boundary"}, {"arxiv": "1903.02022", "role": "modern convex ancient-solution classification and explicit equation"}]
    if data["boundary_atlas"] != boundary or data["collision_boundary"] != collision or data["nonclaims"] != nonclaims or data["references"] != references:
        raise AssertionError("static boundary/source contract")
    checks += 16
    required_eval = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    if set(evaluation) != required_eval:
        raise AssertionError("evaluation key set")
    if (evaluation["schema"], evaluation["candidate_id"], evaluation["obstruction_id"], evaluation["source_commit"], evaluation["fixed_epoch"], evaluation["scope_literal"]) != ("route-a-evaluation-v0.2.0", "HCS-C314", "HEN-O298", SOURCE, 1788393600, SCOPE):
        raise AssertionError("evaluation identity")
    if evaluation["tuple"] != data["route_a"]["tuple"] or evaluation["overall_verdict"] != "ROUTE_A_REJECTED" or evaluation["route_b_invocation_allowed"] is not False or evaluation["scope_flags"] != data["scope_flags"] or evaluation["theorem_status"] != "PROVABLE_AS_STATED":
        raise AssertionError("evaluation contract")
    for key, verdict in zip(("a0", "a1", "a2", "a3", "a4"), data["route_a"]["tuple"]):
        if type(evaluation[key]) is not dict or evaluation[key].get("verdict") != verdict:
            raise AssertionError("evaluation branch")
    checks += 22
    if [row["r"] for row in data["parameter_rows"]] != R_VALUES:
        raise AssertionError("parameter order")
    for text, row in zip(R_VALUES, data["parameter_rows"]):
        if set(row) != {"r", "time", "horizontal_width", "vertical_height", "area_formula", "area_quadrature", "length_formula", "length_quadrature", "curvature_min", "curvature_max", "point_rows"}:
            raise AssertionError("parameter row keys")
        q = Fraction(text); r = mp.mpf(q.numerator) / q.denominator
        t = mp.log(r); a = mp.sqrt(1-r*r); alpha = mp.acos(r)
        close(row["time"], t); close(row["horizontal_width"], 2*alpha); close(row["vertical_height"], 2*mp.acosh(1/r)); close(row["area_formula"], -2*mp.pi*t)
        area = mp.re(4*mp.quad(lambda xx: mp.acosh(max(mp.mpf(1),mp.cos(xx)/r)), [0, alpha]))
        close(row["area_quadrature"], area, mp.mpf("5e-65"))
        length = 4*a*mp.ellipk(a*a)
        close(row["length_formula"], length); close(row["length_quadrature"], length, mp.mpf("5e-65")); close(row["curvature_min"], r/a); close(row["curvature_max"], 1/a)
        checks += 10
        if len(row["point_rows"]) != 11:
            raise AssertionError("point count")
        for j, point in enumerate(row["point_rows"]):
            if set(point) != {"point_index", "cos_x", "x", "y_upper", "level_residual", "gradient_norm_squared", "curvature", "inward_speed", "arrival_time", "arrival_pde_lhs"} or point["point_index"] != j:
                raise AssertionError("point structure")
            c = r+(1-r)*j/10; x=mp.acos(c); y=mp.acosh(c/r); k=c/a
            close(point["cos_x"], c); close(point["x"], x); close(point["y_upper"], y); close(point["level_residual"], 0); close(point["gradient_norm_squared"], 1-r*r); close(point["curvature"], k); close(point["inward_speed"], k); close(point["arrival_time"], t); close(point["arrival_pde_lhs"], 1)
            checks += 10
    if len(data["extinction_rows"]) != 8 or len(data["grim_rows"]) != 7:
        raise AssertionError("asymptotic row counts")
    for row, k in zip(data["extinction_rows"], (4,5,6,7,8,9,10,12)):
        if set(row) != {"tau", "scaled_curvature_min", "scaled_curvature_max", "max_distance_from_one"}:raise AssertionError("extinction keys")
        tau=mp.mpf(2)**(-k); r=mp.e**(-tau); vals=[mp.sqrt(2*tau*(1/(1-r*r)-mp.sin(2*mp.pi*j/17)**2)) for j in range(17)]
        close(row["tau"],tau);close(row["scaled_curvature_min"],min(vals));close(row["scaled_curvature_max"],max(vals));close(row["max_distance_from_one"],max(abs(v-1) for v in vals));checks+=4
    for row, k in zip(data["grim_rows"], (4,6,8,10,12,16,20)):
        if set(row) != {"r", "samples"}:raise AssertionError("grim keys")
        r=mp.mpf(2)**(-k);close(row["r"],r);checks+=1
        if len(row["samples"])!=5:raise AssertionError("grim samples")
        for rec,x in zip(row["samples"],map(mp.mpf,("0","0.25","0.5","0.75","1.0"))):
            if set(rec) != {"x", "centered_upper", "grim_target", "error"}:raise AssertionError("grim sample keys")
            centered=mp.acosh(mp.cos(x)/r)-mp.acosh(1/r);target=mp.log(mp.cos(x))
            close(rec["x"],x);close(rec["centered_upper"],centered);close(rec["grim_target"],target);close(rec["error"],centered-target);checks+=4
    enum=data["enumeration"]
    if (enum["parameter_rows"],enum["point_rows"],enum["extinction_rows"],enum["grim_parameter_rows"],enum["grim_sample_rows"])!=(20,220,8,7,35):raise AssertionError("enumeration")
    if set(enum) != {"parameter_rows","point_rows","extinction_rows","grim_parameter_rows","grim_sample_rows","audited_leaf_count"}:raise AssertionError("enumeration keys")
    body=dict(data);body.pop("payload_sha256")
    if enum["audited_leaf_count"] != leaves(body):raise AssertionError("audited leaf count")
    checks += 5
    print(f"C314 independent checker: PASS ({checks} checks)")


if __name__ == "__main__":
    main()
