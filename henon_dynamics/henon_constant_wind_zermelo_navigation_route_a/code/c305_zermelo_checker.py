#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C305."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c305_zermelo_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C305/2026-09-03.yaml"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
mp.mp.dps = 90

FLAGS = {
    "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
    "claims_root_number": False, "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False, "claims_target_functional_equation": False,
    "claims_target_zero_match": False, "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
MODEL = {
    "state_space": "R^d for every finite integer d>=1",
    "dynamics": "xdot=W+u with constant W and measurable control satisfying norm(u)<=c",
    "parameters": "W in R^d and c>=0",
    "target_data": "displacement y in R^d from the origin",
}
THEOREM = {
    "fixed_time_geometry": "the exact-time reachable set is Wt+c t closed_unit_ball",
    "three_chambers": "weak, critical, and strong wind have complete reachability and minimum-time formulas",
    "optimizer": "every nonzero reachable target has a unique almost-everywhere constant time-optimal control",
    "time_sets": "all attainable time sets are lower rays, closed strong-wind windows, singleton zero, or empty",
    "value_geometry": "positive homogeneity, rotation equivariance, velocity scaling, and HJB hold on the finite-value interior",
    "boundaries": "zero wind, zero cap, zero target, critical half-space, and strong Mach cone are explicit",
}
PROOF = {
    "quadratic": "reachability is exactly the scalar inequality (w_squared-c_squared)t_squared-2pt+r_squared<=0",
    "root_choice": "minimum time is the sole positive root in weak and critical wind and the smaller positive root in strong wind",
    "uniqueness": "equality in the average-control norm bound forces the saturated optimal control to be constant almost everywhere",
    "hjb": "for c>0 implicit differentiation gives the HJB identity; the one-dimensional c=0 interior is checked directly",
    "finite_role": "finite cases are regression receipts only; the proof covers all finite d and all parameters",
}
NONCLAIMS = [
    "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
    "Wind, control speeds, cones, and travel times are source navigation data rather than rational-prime labels or target coefficients.",
    "The value function and HJB equation are not asserted to define a Hilbert--Polya operator.",
    "No novelty or priority is claimed for classical Zermelo navigation or constant-drift minimum-time control.",
]
COLLISION = {
    "C222": "C222 studies second-order double-integrator bang-bang switching; C305 is first-order constant-drift navigation with Euclidean ball-valued controls in every finite dimension.",
    "C270": "C270 studies Heisenberg sub-Riemannian control; C305 has translation-invariant Euclidean velocity balls and no noncommutative horizontal geometry.",
    "C268": "C268 is an uncontrolled constant-electromagnetic-field Lorentz flow; C305 is a controlled first-order navigation problem with norm-bounded inputs.",
}
REFERENCES = [
    {"identifier": "10.1002/zamm.19310110205", "role": "historical Zermelo navigation owner attribution only"},
    {"identifier": "10.4310/jdg/1098137838", "role": "navigation and Randers geometric context only"},
]
BOUNDARIES = [
    {"boundary_id": "B0-zero-target", "statement": "The zero target has minimum time zero; positive-time feasibility depends on whether the wind can be cancelled."},
    {"boundary_id": "B1-zero-wind", "statement": "For W=0 and c>0 the value is Euclidean distance divided by c."},
    {"boundary_id": "B2-zero-cap", "statement": "For c=0 only the nonnegative wind ray is reachable, with no control freedom."},
    {"boundary_id": "B3-critical", "statement": "At w=c>0 a nonzero target is reachable exactly when p>0 and T=r_squared/(2p)."},
    {"boundary_id": "B4-mach-cone", "statement": "For w>c the full finite-value domain, including the origin, is the closed forward Mach cone; its nonzero boundary has a double time root."},
    {"boundary_id": "B5-regularity", "statement": "The value is smooth on each finite-value interior away from zero and has square-root loss at a nontrivial strong-wind cone boundary."},
    {"boundary_id": "B6-symmetry", "statement": "The value is rotation equivariant, degree-one in target displacement, and inverse degree-one under common velocity scaling."},
    {"boundary_id": "B7-exclusion", "statement": "No variable wind, obstacle, state constraint, manifold navigation, or global strong-wind Finsler norm is claimed."},
]
CASE_SPECS = [
    ("W0-D1", ["0"], "2", ["3"]), ("W0-D2-345", ["0", "0"], "3", ["3", "4"]),
    ("WEAK-DOWNWIND", ["1", "0"], "2", ["3", "0"]), ("WEAK-UPWIND", ["1", "0"], "2", ["-3", "0"]),
    ("WEAK-CROSSWIND", ["1", "0"], "2", ["0", "2"]), ("WEAK-PYTHAGOREAN", ["3", "4"], "6", ["1", "2"]),
    ("WEAK-D3", ["1", "0", "0"], "2", ["1", "1", "1"]), ("WEAK-NEAR-CRITICAL", ["3", "4"], "26/5", ["-2", "1"]),
    ("CRIT-D1-FORWARD", ["1"], "1", ["3"]), ("CRIT-D2-FORWARD", ["1", "0"], "1", ["1", "1"]),
    ("CRIT-TANGENT-NO", ["1", "0"], "1", ["0", "1"]), ("CRIT-BACKWARD-NO", ["1", "0"], "1", ["-1", "0"]),
    ("CRIT-34-DOWNWIND", ["3", "4"], "5", ["3", "4"]), ("CRIT-D3-FORWARD", ["0", "0", "2"], "2", ["1", "0", "2"]),
    ("STRONG-D1-FORWARD", ["2"], "1", ["3"]), ("STRONG-D1-BACKWARD-NO", ["2"], "1", ["-1"]),
    ("STRONG-AXIS", ["5", "0"], "3", ["4", "0"]), ("STRONG-MACH-BOUNDARY", ["5", "0"], "3", ["4", "3"]),
    ("STRONG-OUTSIDE-NO", ["5", "0"], "3", ["3", "4"]), ("STRONG-BACKWARD-NO", ["5", "0"], "3", ["-1", "0"]),
    ("STRONG-D3-BOUNDARY", ["0", "0", "5"], "4", ["4", "0", "3"]), ("STRONG-D3-INTERIOR", ["0", "0", "5"], "4", ["1", "2", "5"]),
    ("CZERO-RAY", ["2", "0"], "0", ["4", "0"]), ("CZERO-OFF-RAY-NO", ["2", "0"], "0", ["4", "1"]),
    ("DEGENERATE-ZERO", ["0", "0"], "0", ["0", "0"]), ("DEGENERATE-NONZERO-NO", ["0", "0"], "0", ["1", "0"]),
    ("WEAK-ZERO-TARGET", ["1", "0"], "2", ["0", "0"]), ("CRIT-ZERO-TARGET", ["1", "0"], "1", ["0", "0"]),
    ("STRONG-ZERO-TARGET", ["2", "0"], "1", ["0", "0"]),
]
HJB_IDS = ["W0-D1", "W0-D2-345", "WEAK-DOWNWIND", "WEAK-UPWIND", "WEAK-CROSSWIND", "WEAK-PYTHAGOREAN", "CRIT-D1-FORWARD", "CRIT-D2-FORWARD", "CRIT-D3-FORWARD", "STRONG-D1-FORWARD", "STRONG-AXIS", "STRONG-D3-INTERIOR"]


def branch(verdict, status, evidence, failure, artifacts):
    return {"verdict": verdict, "evidence_status": status, "strongest_evidence": evidence, "strongest_failure": failure, "artifacts": artifacts}


EXPECTED_EVALUATION = {
    "schema": "route-a-evaluation-v0.2.0", "candidate_id": "HCS-C305",
    "title": "All-dimensional constant-wind Zermelo reachability and value atlas",
    "evaluation_date": "2026-09-03", "source_commit": SOURCE, "fixed_epoch": EPOCH,
    "scope_literal": SCOPE, "evaluator_authority": "route-a-evaluator", "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR, "obstruction_id": "HEN-O289",
    "candidate_definition": "Translation-invariant minimum-time control xdot=W+u on R^d for every finite d>=1, constant W, and measurable controls with norm(u)<=c.",
    "family": "constant-wind Zermelo navigation and convex minimum-time control",
    "phase_space": "R^d for every finite integer d>=1", "dynamics": "xdot=W+u with constant W and measurable norm-bounded control",
    "parameters": "W in R^d, c>=0, target displacement y in R^d",
    "parameter_provenance": "all vectors, speeds, cones, and times are source control-system data",
    "arithmetic_origin": "none; no rational-prime labels or target coefficients occur", "clock": "physical travel time t>=0",
    "normalization": "Euclidean control ball; translation places the initial point at the origin",
    "determinant_convention": "none; no target or source determinant is constructed",
    "orbit_cutoff": "one all-parameter analytic theorem; finite cases are regression receipts only",
    "precision": "canonical rational invariants and 72-digit radical/value receipts", "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor laws, target functional equations, target zeros, and Hilbert--Polya operators",
    "artifact_paths": ["results/c305_zermelo_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "a0": branch("A0_FAIL", "exact negative classification", "reachability and travel-time data are source Euclidean control geometry", "no rational-prime local datum or target Euler factor is constructed", ["THEOREM_PACKAGE.md", "SOURCE_AUDIT.md"]),
    "a1": branch("A1_FAIL", "exact optimizer classification", "every nonzero reachable target has one constant time-optimal control", "point-to-point optimal arcs do not supply a primitive periodic-orbit ledger", ["THEOREM_PACKAGE.md", "paper/main.pdf"]),
    "a2": branch("A2_FAIL", "exact negative classification", "the value is homogeneous in Euclidean displacement", "physical travel time is not a logarithmic rational-prime clock", ["THEOREM_PACKAGE.md"]),
    "a3": branch("A3_FAIL", "exact negative classification", "the value function is an explicit quadratic radical", "no target determinant, completed function, or functional equation is constructed", ["results/c305_zermelo_evidence.json", "paper/main.pdf"]),
    "a4": branch("A4_FAIL", "no operator candidate", "the HJB equation exactly characterizes the source value function", "no self-adjoint Hilbert--Polya operator or target-zero correspondence is present", ["SOURCE_AUDIT.md", "paper/main.pdf"]),
    "tuple": TUPLE, "overall_verdict": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no bad-prime, Euler-factor, or root-number datum exists under the frozen scope",
    "scope_flags": FLAGS, "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "regression evidence only; reachability, value, optimizer, HJB, regularity, and boundaries are proved analytically",
    "source_owner_tokens": ["10.1002/zamm.19310110205", "10.4310/jdg/1098137838"],
}


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"] for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge keys are forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("non-string or duplicate YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be a mapping")
    return value


def duplicate_rejector(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate_rejector, parse_constant=reject_nonfinite)
    if type(value) is not dict:
        raise TypeError("JSON root must be an object")
    return value


def exact_tree(actual, expected):
    if type(actual) is not type(expected):
        return False
    if type(expected) is dict:
        return set(actual) == set(expected) and all(exact_tree(actual[key], expected[key]) for key in expected)
    if type(expected) is list:
        return len(actual) == len(expected) and all(exact_tree(a, e) for a, e in zip(actual, expected))
    return actual == expected


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


RATIONAL_RE = re.compile(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?")
DECIMAL_RE = re.compile(r"-?(?:0|[1-9][0-9]*)\.[0-9]+(?:e[+-]?[1-9][0-9]*)?")


def canonical_fraction(text):
    if type(text) is not str or RATIONAL_RE.fullmatch(text) is None:
        raise ValueError(f"invalid rational receipt: {text!r}")
    value = Fraction(text)
    canonical = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if text != canonical:
        raise ValueError(f"noncanonical rational receipt: {text}")
    return value


def mpf(value):
    return mp.mpf(value.numerator) / value.denominator


def canonical_decimal(text, expected):
    if type(text) is not str or DECIMAL_RE.fullmatch(text) is None:
        raise ValueError(f"invalid decimal receipt: {text!r}")
    canonical = "0.0" if expected == 0 else mp.nstr(expected, 72, strip_zeros=False)
    if text != canonical:
        raise ValueError(f"noncanonical decimal receipt: {text}")
    return mp.mpf(text)


def dot(left, right):
    return sum((x * y for x, y in zip(left, right)), Fraction(0))


def leaves(value):
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C305 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVALUATION)
    args = parser.parse_args()
    data, evaluation = strict_json(args.evidence), strict_yaml(args.evaluation)
    count = 0

    def ok(condition, label):
        nonlocal count
        if not bool(condition):
            raise AssertionError(label)
        count += 1

    ok(set(data) == {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "model", "theorem_contract", "proof_contract", "route_a", "scope_flags", "nonclaims", "collision_boundary", "references", "enumeration", "cases", "hjb_probes", "boundaries", "payload_sha256"}, "exact evidence root keys")
    ok(data["payload_sha256"] == payload_hash(data), "payload self-hash")
    ok(type(data["payload_sha256"]) is str and re.fullmatch(r"[0-9a-f]{64}", data["payload_sha256"]) is not None, "payload hash type")
    for key, expected in (("schema", "hcs-c305-constant-wind-zermelo-v1"), ("candidate_id", "HCS-C305"), ("obstruction_id", "HEN-O289"), ("evaluation_date", "2026-09-03"), ("source_commit", SOURCE), ("scope_literal", SCOPE)):
        ok(type(data[key]) is str and data[key] == expected, key)
    ok(type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH, "epoch")
    ok(exact_tree(data["evaluator"], {"version": "0.2.0", "sha256": EVALUATOR}), "evaluator")
    ok(exact_tree(data["model"], MODEL), "exact model tree")
    ok(exact_tree(data["theorem_contract"], THEOREM), "exact theorem tree")
    ok(exact_tree(data["proof_contract"], PROOF), "exact proof tree")
    ok(exact_tree(data["route_a"], {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}), "route tree")
    ok(exact_tree(data["scope_flags"], FLAGS), "scope flags")
    ok(exact_tree(data["nonclaims"], NONCLAIMS), "nonclaims")
    ok(exact_tree(data["collision_boundary"], COLLISION), "collision")
    ok(exact_tree(data["references"], REFERENCES), "references")
    ok(exact_tree(data["boundaries"], BOUNDARIES), "boundaries")

    enumeration = data["enumeration"]
    ids = [spec[0] for spec in CASE_SPECS]
    ok(type(enumeration) is dict and set(enumeration) == {"case_count", "case_ids", "hjb_probe_count", "boundary_rows", "audited_cell_count"}, "enumeration keys")
    ok(type(enumeration["case_count"]) is int and enumeration["case_count"] == 29, "case count")
    ok(type(enumeration["case_ids"]) is list and enumeration["case_ids"] == ids and len(set(ids)) == 29, "ordered unique case ids")
    ok(type(enumeration["hjb_probe_count"]) is int and enumeration["hjb_probe_count"] == 12, "HJB count")
    ok(type(enumeration["boundary_rows"]) is int and enumeration["boundary_rows"] == 8, "boundary count")

    cases = data["cases"]
    ok(type(cases) is list and len(cases) == 29 and [case.get("case_id") for case in cases] == ids, "case list and IDs")
    solutions = {}
    for case, spec in zip(cases, CASE_SPECS):
        case_id, W_text, c_text, y_text = spec
        ok(type(case) is dict and set(case) == {"attainable_time_interval", "case_id", "chamber", "dimension", "discriminant", "formula_branch", "minimum_time", "optimal_control", "optimal_speed", "p", "quadratic_coefficient", "r_squared", "reachable", "speed_cap", "target", "terminal_residual", "w_squared", "wind"}, f"{case_id} keys")
        ok(type(case["case_id"]) is str and case["case_id"] == case_id, f"{case_id} id")
        W, c, target = [Fraction(item) for item in W_text], Fraction(c_text), [Fraction(item) for item in y_text]
        ok(type(case["dimension"]) is int and not isinstance(case["dimension"], bool) and case["dimension"] == len(W), f"{case_id} dimension")
        ok(type(case["wind"]) is list and [canonical_fraction(item) for item in case["wind"]] == W, f"{case_id} wind")
        ok(canonical_fraction(case["speed_cap"]) == c and c >= 0, f"{case_id} cap")
        ok(type(case["target"]) is list and [canonical_fraction(item) for item in case["target"]] == target, f"{case_id} target")
        w2, p, r2 = dot(W, W), dot(W, target), dot(target, target)
        a, discriminant = w2 - c * c, p * p - (w2 - c * c) * r2
        ok(canonical_fraction(case["w_squared"]) == w2, f"{case_id} w2")
        ok(canonical_fraction(case["p"]) == p, f"{case_id} p")
        ok(canonical_fraction(case["r_squared"]) == r2, f"{case_id} r2")
        ok(canonical_fraction(case["quadratic_coefficient"]) == a, f"{case_id} a")
        ok(canonical_fraction(case["discriminant"]) == discriminant, f"{case_id} discriminant")
        chamber = "degenerate_zero_velocity" if w2 == 0 and c == 0 else "weak_wind" if a < 0 else "critical_wind" if a == 0 else "strong_wind"
        reachable = True if r2 == 0 else False if chamber == "degenerate_zero_velocity" else True if a < 0 else p > 0 if a == 0 else p > 0 and discriminant >= 0
        ok(type(case["chamber"]) is str and case["chamber"] == chamber, f"{case_id} chamber")
        ok(type(case["reachable"]) is bool and case["reachable"] is reachable, f"{case_id} reachability")
        T = upper = None
        if r2 == 0:
            T, formula = mp.mpf("0"), "zero_target"
            interval_kind = "all_nonnegative_times" if w2 <= c * c else "singleton_zero"
            upper = None if w2 <= c * c else mp.mpf("0")
        elif not reachable:
            formula, interval_kind = "unreachable", "empty"
        elif a < 0:
            T = (mp.sqrt(mpf(discriminant)) - mpf(p)) / mpf(-a)
            formula, interval_kind = "weak_radical", "lower_ray"
        elif a == 0:
            T = mpf(r2) / (2 * mpf(p))
            formula, interval_kind = "critical_parabolic", "lower_ray"
        else:
            root = mp.sqrt(mpf(discriminant))
            T, upper = (mpf(p) - root) / mpf(a), (mpf(p) + root) / mpf(a)
            formula, interval_kind = "strong_smaller_root", "closed_window"
        ok(type(case["formula_branch"]) is str and case["formula_branch"] == formula, f"{case_id} formula")
        interval = case["attainable_time_interval"]
        ok(type(interval) is dict and set(interval) == {"kind", "lower", "upper"} and type(interval["kind"]) is str and interval["kind"] == interval_kind, f"{case_id} interval")
        if T is None:
            ok(case["minimum_time"] is None and interval["lower"] is None and interval["upper"] is None, f"{case_id} unreachable times")
            ok(case["optimal_control"] is None and case["optimal_speed"] is None and case["terminal_residual"] is None, f"{case_id} unreachable optimizer")
        else:
            canonical_decimal(case["minimum_time"], T); ok(True, f"{case_id} T")
            canonical_decimal(interval["lower"], T); ok(True, f"{case_id} interval lower")
            if upper is None:
                ok(interval["upper"] is None, f"{case_id} unbounded interval")
            else:
                canonical_decimal(interval["upper"], upper); ok(True, f"{case_id} interval upper")
            if r2 == 0:
                ok(case["optimal_control"] is None and case["optimal_speed"] is None and case["terminal_residual"] is None, f"{case_id} zero target optimizer")
            else:
                control = [mpf(target[i]) / T - mpf(W[i]) for i in range(len(W))]
                ok(type(case["optimal_control"]) is list and len(case["optimal_control"]) == len(W), f"{case_id} control shape")
                for observed, expected in zip(case["optimal_control"], control):
                    canonical_decimal(observed, expected); ok(True, f"{case_id} control")
                speed = mp.sqrt(sum(item * item for item in control))
                residual = mp.sqrt(sum((mpf(W[i]) * T + control[i] * T - mpf(target[i])) ** 2 for i in range(len(W))))
                canonical_decimal(case["optimal_speed"], speed); ok(True, f"{case_id} speed")
                canonical_decimal(case["terminal_residual"], residual); ok(True, f"{case_id} residual")
        solutions[case_id] = (W, c, target, a, p, T)

    probes = data["hjb_probes"]
    ok(type(probes) is list and len(probes) == 12 and [probe.get("case_id") for probe in probes] == HJB_IDS, "HJB probe list")
    for probe in probes:
        case_id = probe["case_id"]
        ok(type(probe) is dict and set(probe) == {"case_id", "gradient", "hjb_lhs", "target_scale_three_time", "velocity_scale_two_time"}, f"{case_id} HJB keys")
        ok(type(case_id) is str and case_id in HJB_IDS, f"{case_id} HJB id")
        W, c, target, a, p, T = solutions[case_id]
        denominator = mpf(p) - mpf(a) * T
        gradient = [(mpf(target[i]) - mpf(W[i]) * T) / denominator for i in range(len(W))]
        ok(type(probe["gradient"]) is list and len(probe["gradient"]) == len(W), f"{case_id} gradient shape")
        for observed, expected in zip(probe["gradient"], gradient):
            canonical_decimal(observed, expected); ok(True, f"{case_id} gradient")
        lhs = sum(mpf(W[i]) * gradient[i] for i in range(len(W))) + mpf(c) * mp.sqrt(sum(item * item for item in gradient))
        canonical_decimal(probe["hjb_lhs"], lhs); ok(True, f"{case_id} HJB")
        canonical_decimal(probe["target_scale_three_time"], 3 * T); ok(True, f"{case_id} target scale")
        canonical_decimal(probe["velocity_scale_two_time"], T / 2); ok(True, f"{case_id} velocity scale")

    audited = leaves(cases) + leaves(probes) + leaves(data["boundaries"])
    ok(type(enumeration["audited_cell_count"]) is int and enumeration["audited_cell_count"] == audited == 744, "audited cells")
    ok(exact_tree(evaluation, EXPECTED_EVALUATION), "full EXPECTED_EVALUATION exact tree")
    print(f"C305 independent Zermelo checker: PASS ({count} assertions; producer import forbidden)")


if __name__ == "__main__":
    main()
