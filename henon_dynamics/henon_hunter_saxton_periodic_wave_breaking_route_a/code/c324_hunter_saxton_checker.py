#!/usr/bin/env python3
"""Producer-independent checker for HCS-C324."""
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
DEFAULT = ROOT / "results/c324_hunter_saxton_evidence.json"
DEFAULT_EVAL = ROOT / "evaluations/route_a/HCS-C324/2026-09-03.yaml"
SOURCE = "1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVAL_RAW = "10becdeeecc683514b331994ed85b1def0eecaddb0c9ba32d12ba3886123b2ce"
EVAL_SEMANTIC = "5f3078d80b634bc13c6e705c0414e4e5add2c42a3999a6ce82c153073807f9f7"
PARAMETERS = (
    (3, 4, 1), (5, 12, 2), (8, 15, 3), (7, 24, 4),
    (20, 21, 5), (9, 40, 6), (12, 35, 7), (11, 60, 8),
    (28, 45, 9), (33, 56, 10), (16, 63, 11), (48, 55, 12),
)
ASYMMETRIC_PARAMETERS = ((1, 1), (1, 2), (1, 3), (-1, 1), (-1, 2), (-1, 3))
TAUS = (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4))
RATIOS = (Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(1))
mp.mp.dps = 100


def object_pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def strict_json(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=object_pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate/non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    return yaml.load(raw, Loader=UniqueLoader)


def semantic_hash(value) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return semantic_hash(body)


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def canonical_fraction(text: str) -> Fraction:
    if type(text) is not str or not re.fullmatch(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?", text):
        raise AssertionError("noncanonical rational syntax")
    value = Fraction(text)
    expected = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if text != expected:
        raise AssertionError("non-reduced rational")
    return value


def canonical_decimal(text: str) -> mp.mpf:
    if type(text) is not str:
        raise AssertionError("decimal is not a string")
    value = mp.mpf(text)
    if not mp.isfinite(value):
        raise AssertionError("nonfinite decimal")
    expected = mp.nstr(value, 72, strip_zeros=False, min_fixed=-90, max_fixed=90)
    if text != expected:
        raise AssertionError("noncanonical decimal")
    return value


def close_decimal(text: str, expected: mp.mpf, tol=mp.mpf("3e-70")) -> None:
    value = canonical_decimal(text)
    if abs(value - expected) > tol * max(1, abs(expected)):
        raise AssertionError("decimal mismatch")


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C324 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVAL)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    evaluation = strict_yaml(args.evaluation)
    checks = 0

    raw_eval = hashlib.sha256(args.evaluation.read_bytes()).hexdigest()
    sem_eval = semantic_hash(evaluation)
    if (raw_eval, sem_eval) != (EVAL_RAW, EVAL_SEMANTIC):
        raise AssertionError("evaluation digest")
    if payload_hash(data) != data.get("payload_sha256"):
        raise AssertionError("payload digest")
    checks += 3

    top = {
        "schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
        "source_commit", "scope_literal", "evaluator", "evaluation_lock", "model",
        "theorem_contract", "profiles", "asymmetric_profiles", "boundary_atlas", "collision_boundary", "route_a",
        "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256",
    }
    if set(data) != top:
        raise AssertionError("top-level schema")
    identity = (data["schema"], data["candidate_id"], data["obstruction_id"], data["evaluation_date"],
                data["fixed_epoch"], data["source_commit"], data["scope_literal"])
    if identity != ("hcs-c324-hunter-saxton-wave-breaking-v1", "HCS-C324", "HEN-O308",
                    "2026-09-03", 1788393600, SOURCE, SCOPE):
        raise AssertionError("identity")
    if data["evaluator"] != {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}:
        raise AssertionError("evaluator")
    if data["evaluation_lock"] != {
            "relative_path": "evaluations/route_a/HCS-C324/2026-09-03.yaml",
            "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC}:
        raise AssertionError("evaluation lock")
    expected_model = {
        "domain": "unit circle R/Z",
        "equation": "u_tx+u*u_xx+(u_x)^2/2=-E/2 with E=integral_0^1 (u_x)^2 dx",
        "regularity": "C2 initial profile and once-integrated classical formulation before characteristic degeneration",
        "gauge": "an additive spatial constant fixes characteristic translation but does not affect the slope theorem",
    }
    expected_contract = {
        "jacobian": "eta_x=(cos(sqrt(E)t/2)+(u0_x/sqrt(E))sin(sqrt(E)t/2))^2",
        "slope": "u_x along eta is the logarithmic time derivative of eta_x",
        "positive_lifespan": "T_plus=2/sqrt(E)*atan(sqrt(E)/(-min u0_x))",
        "breaking_set": "the first positive breaking labels are exactly the minimizers of u0_x",
        "universal_rate": "u_x(t,eta(t,x))=-2/(T_plus-t)+O(1) at every first breaking label",
        "negative_boundary": "T_minus=-2/sqrt(E)*atan(sqrt(E)/(max u0_x))",
        "energy": "integral (u_x along eta)^2 eta_x dx equals E before breaking",
    }
    expected_boundary = [
        {"face": "E=0", "status": "u0 is spatially constant and no wave breaking occurs"},
        {"face": "multiple global minima", "status": "all minimizing labels break simultaneously at T_plus"},
        {"face": "negative time", "status": "the first backward endpoint is T_minus and is controlled by max u0_x"},
        {"face": "t=T_plus", "status": "eta_x vanishes and the classical diffeomorphism chart ends"},
        {"face": "t beyond first breaking", "status": "weak, conservative, and dissipative continuations are outside scope"},
        {"face": "unintegrated third-order equation", "status": "only distributionally inferred; C2 data are handled in the integrated formulation"},
    ]
    expected_collision = {
        "C195": "viscous Burgers has parabolic smoothing rather than Hunter--Saxton slope focusing",
        "C256": "KdV cnoidal waves are dispersive traveling waves rather than arbitrary-data breaking",
        "C278": "Camassa--Holm two-peakons form a finite-dimensional weak-solution manifold rather than this C2 pre-breaking theorem",
    }
    expected_nonclaims = [
        "No priority is claimed for the Hunter--Saxton equation, its geometric formulation, or classical wave breaking.",
        "No solution continuation after first breaking is constructed or selected.",
        "Finite harmonic-profile receipts do not prove the all-initial-data theorem.",
        "The geometric formulation is not a Hilbert--Polya operator or a Route-B authorization.",
        "No target arithmetic local data, Euler factors, root numbers, automorphy, target divisor, functional equation, or target-zero match is asserted.",
    ]
    expected_references = [
        {"doi": "10.1137/0151075", "role": "original Hunter--Saxton equation and finite-time breakdown source"},
        {"doi": "10.1137/050647451", "role": "periodic geometric formulation and explicit characteristic source"},
        {"doi": "10.1137/S0036141003425672", "role": "periodic strong-solution structure and blow-up source"},
    ]
    if (data["model"], data["theorem_contract"], data["boundary_atlas"],
            data["collision_boundary"], data["nonclaims"], data["references"]) != (
            expected_model, expected_contract, expected_boundary, expected_collision,
            expected_nonclaims, expected_references):
        raise AssertionError("static theorem/source boundary")
    expected_route = {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                      "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    if data["route_a"] != expected_route:
        raise AssertionError("Route-A")
    expected_flags = {
        "claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number",
        "claims_automorphy", "claims_target_divisor_or_counting_law",
        "claims_target_functional_equation", "claims_target_zero_match",
        "claims_hilbert_polya_operator", "invokes_route_b",
    }
    if set(data["scope_flags"]) != expected_flags or any(type(v) is not bool or v for v in data["scope_flags"].values()):
        raise AssertionError("scope flags")
    checks += 14

    eval_top = {
        "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
        "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
        "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics",
        "parameters", "parameter_provenance", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data",
        "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict",
        "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status",
        "finite_evidence_role", "source_owner_tokens",
    }
    if set(evaluation) != eval_top:
        raise AssertionError("evaluation schema")
    layer_keys = {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}
    if any(type(evaluation[name]) is not dict or set(evaluation[name]) != layer_keys for name in ("a0", "a1", "a2", "a3", "a4")):
        raise AssertionError("evaluation layer schema")
    if evaluation["artifact_paths"] != ["results/c324_hunter_saxton_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"]:
        raise AssertionError("artifact paths")
    expected_layers = {
        "a0": {"verdict": "A0_FAIL", "evidence_status": "PROVED",
               "strongest_evidence": "no arithmetic source exists",
               "strongest_failure": "initial slope functions and characteristic clocks do not intrinsically encode rational primes"},
        "a1": {"verdict": "A1_FAIL", "evidence_status": "PROVED",
               "strongest_evidence": "the exact pre-breaking characteristic portrait is complete",
               "strongest_failure": "every nonconstant periodic classical solution reaches characteristic degeneration before a nonconstant periodic orbit can close"},
        "a2": {"verdict": "A2_FAIL", "evidence_status": "STOP_SCOPED",
               "strongest_evidence": "none",
               "strongest_failure": "no primitive-orbit zeta or target determinant is defined"},
        "a3": {"verdict": "A3_FAIL", "evidence_status": "STOP_SCOPED",
               "strongest_evidence": "exact Riccati and energy identities only",
               "strongest_failure": "the source integrability does not supply the target functional equation or Weil compression"},
        "a4": {"verdict": "A4_FORMAL_HINT", "evidence_status": "PROVED",
               "strongest_evidence": "the equation is the geodesic equation of the homogeneous H1 metric on a diffeomorphism quotient",
               "strongest_failure": "no prime-carrying unitary quantization with the same clock and weights is constructed"},
    }
    if any(evaluation[name] != expected_layers[name] for name in expected_layers):
        raise AssertionError("evaluation layer semantics")
    if (evaluation["schema"], evaluation["candidate_id"], evaluation["obstruction_id"],
            evaluation["evaluation_date"], evaluation["source_commit"], evaluation["fixed_epoch"],
            evaluation["scope_literal"], evaluation["evaluator_authority"], evaluation["evaluator_version"],
            evaluation["evaluator_authority_sha256"], evaluation["tuple"],
            evaluation["overall_verdict"], evaluation["route_b_invocation_allowed"],
            evaluation["scope_flags"], evaluation["theorem_status"],
            evaluation["finite_evidence_role"], evaluation["source_owner_tokens"]) != (
            "route-a-evaluation-v0.2.0", "HCS-C324", "HEN-O308", "2026-09-03", SOURCE,
            1788393600, SCOPE, "flow_systems/skills/route-a-evaluator.md", "0.2.0", EVALUATOR,
            expected_route["tuple"], "ROUTE_A_REJECTED", False, data["scope_flags"],
            "PROVABLE_AS_STATED", "convention and implementation receipt, not proof",
            ["10.1137/0151075", "10.1137/050647451"]):
        raise AssertionError("evaluation semantics")
    checks += 38

    profiles = data["profiles"]
    if type(profiles) is not list or len(profiles) != len(PARAMETERS):
        raise AssertionError("profile count")
    row_keys = {
        "profile_id", "cosine_amplitude", "sine_amplitude", "frequency", "amplitude",
        "energy", "minimum_slope", "maximum_slope", "positive_lifespan",
        "negative_lifespan", "breaking_multiplicity", "minimum_points", "maximum_points", "samples",
    }
    sample_keys = {"time_fraction", "initial_slope_ratio", "time", "characteristic_factor",
                   "jacobian", "transported_slope", "transformed_energy_density"}
    for row, (a, b, k) in zip(profiles, PARAMETERS):
        if type(row) is not dict or set(row) != row_keys:
            raise AssertionError("profile schema")
        if (row["profile_id"], row["cosine_amplitude"], row["sine_amplitude"], row["frequency"],
                row["breaking_multiplicity"]) != (f"harmonic-{k:02d}-{a}-{b}", a, b, k, k):
            raise AssertionError("profile identity")
        radius = mp.sqrt(a * a + b * b)
        energy_q = Fraction(a * a + b * b, 2)
        energy = mp.mpf(energy_q.numerator) / energy_q.denominator
        root_energy = mp.sqrt(energy)
        phase = mp.atan2(b, a)
        lifespan = 2 * mp.atan(root_energy / radius) / root_energy
        close_decimal(row["amplitude"], radius)
        if canonical_fraction(row["energy"]) != energy_q:
            raise AssertionError("energy")
        close_decimal(row["minimum_slope"], -radius)
        close_decimal(row["maximum_slope"], radius)
        close_decimal(row["positive_lifespan"], lifespan)
        close_decimal(row["negative_lifespan"], -lifespan)
        expected_min = [(phase + mp.pi + 2 * mp.pi * j) / (2 * mp.pi * k) for j in range(k)]
        expected_max = [(phase + 2 * mp.pi * j) / (2 * mp.pi * k) for j in range(k)]
        if len(row["minimum_points"]) != k or len(row["maximum_points"]) != k:
            raise AssertionError("breaking labels")
        for text, expected in zip(row["minimum_points"], expected_min):
            close_decimal(text, expected)
        for text, expected in zip(row["maximum_points"], expected_max):
            close_decimal(text, expected)
        expected_coords = [(tau, ratio) for tau in TAUS for ratio in RATIOS]
        if len(row["samples"]) != len(expected_coords):
            raise AssertionError("sample count")
        for sample, (tau, ratio) in zip(row["samples"], expected_coords):
            if type(sample) is not dict or set(sample) != sample_keys:
                raise AssertionError("sample schema")
            if canonical_fraction(sample["time_fraction"]) != tau or canonical_fraction(sample["initial_slope_ratio"]) != ratio:
                raise AssertionError("sample coordinates")
            time = mp.mpf(tau.numerator) / tau.denominator * lifespan
            angle = root_energy * time / 2
            initial = radius * mp.mpf(ratio.numerator) / ratio.denominator
            factor = mp.cos(angle) + initial * mp.sin(angle) / root_energy
            numerator = -root_energy * mp.sin(angle) + initial * mp.cos(angle)
            close_decimal(sample["time"], time)
            close_decimal(sample["characteristic_factor"], factor)
            close_decimal(sample["jacobian"], factor * factor)
            close_decimal(sample["transported_slope"], numerator / factor)
            close_decimal(sample["transformed_energy_density"], numerator * numerator)
            if factor <= 0 or canonical_decimal(sample["jacobian"]) <= 0:
                raise AssertionError("pre-breaking positivity")
            checks += 12
        # Independent phase average of the transformed energy density.
        for tau in TAUS:
            angle = root_energy * (mp.mpf(tau.numerator) / tau.denominator * lifespan) / 2
            average = energy * mp.sin(angle) ** 2 + (radius * radius / 2) * mp.cos(angle) ** 2
            if abs(average - energy) > mp.mpf("1e-90"):
                raise AssertionError("energy conservation")
        checks += 15 + 3 * k

    asymmetric = data["asymmetric_profiles"]
    if type(asymmetric) is not list or len(asymmetric) != len(ASYMMETRIC_PARAMETERS):
        raise AssertionError("asymmetric profile count")
    asymmetric_keys = {
        "profile_id", "sign", "frequency", "definition", "energy", "minimum_slope",
        "maximum_slope", "positive_lifespan", "negative_lifespan",
        "positive_breaking_multiplicity", "negative_breaking_multiplicity",
        "minimum_points", "maximum_points", "samples",
    }
    asymmetric_sample_keys = {
        "time_fraction", "initial_slope", "time", "characteristic_factor", "jacobian",
        "transported_slope", "transformed_energy_density",
    }
    asymmetric_positive_labels = asymmetric_negative_labels = asymmetric_samples = 0
    for row, (sign, k) in zip(asymmetric, ASYMMETRIC_PARAMETERS):
        if type(row) is not dict or set(row) != asymmetric_keys:
            raise AssertionError("asymmetric profile schema")
        if (row["profile_id"], row["sign"], row["frequency"], row["definition"]) != (
                f"asymmetric-{'plus' if sign > 0 else 'minus'}-{k:02d}", sign, k,
                "sign*(cos(2*pi*k*x)+cos(4*pi*k*x)/2)"):
            raise AssertionError("asymmetric identity")
        if canonical_fraction(row["energy"]) != Fraction(5, 8):
            raise AssertionError("asymmetric energy")
        if sign == 1:
            minimum, maximum = Fraction(-3, 4), Fraction(3, 2)
            min_points = sorted(Fraction(j, k) + offset / k for j in range(k)
                                for offset in (Fraction(1, 3), Fraction(2, 3)))
            max_points = [Fraction(j, k) for j in range(k)]
            slopes = (minimum, Fraction(-1, 2), Fraction(0), Fraction(1, 2), maximum)
        else:
            minimum, maximum = Fraction(-3, 2), Fraction(3, 4)
            min_points = [Fraction(j, k) for j in range(k)]
            max_points = sorted(Fraction(j, k) + offset / k for j in range(k)
                                for offset in (Fraction(1, 3), Fraction(2, 3)))
            slopes = (minimum, Fraction(-1, 2), Fraction(0), Fraction(1, 2), maximum)
        if canonical_fraction(row["minimum_slope"]) != minimum or canonical_fraction(row["maximum_slope"]) != maximum:
            raise AssertionError("asymmetric extrema")
        expected_min = [str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}" for x in min_points]
        expected_max = [str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}" for x in max_points]
        if row["minimum_points"] != expected_min or row["maximum_points"] != expected_max:
            raise AssertionError("asymmetric extremizing labels")
        if (row["positive_breaking_multiplicity"], row["negative_breaking_multiplicity"]) != (len(min_points), len(max_points)):
            raise AssertionError("asymmetric multiplicity")
        root_energy = mp.sqrt(mp.mpf(5) / 8)
        positive = 2 * mp.atan(root_energy / (-mpq(minimum))) / root_energy
        negative = -2 * mp.atan(root_energy / mpq(maximum)) / root_energy
        close_decimal(row["positive_lifespan"], positive)
        close_decimal(row["negative_lifespan"], negative)
        if abs(positive + negative) < mp.mpf("1e-20"):
            raise AssertionError("asymmetric lane did not separate min and max")
        expected_coords = [(tau, slope) for tau in TAUS for slope in slopes]
        if len(row["samples"]) != len(expected_coords):
            raise AssertionError("asymmetric sample count")
        for sample, (tau, slope) in zip(row["samples"], expected_coords):
            if type(sample) is not dict or set(sample) != asymmetric_sample_keys:
                raise AssertionError("asymmetric sample schema")
            if canonical_fraction(sample["time_fraction"]) != tau or canonical_fraction(sample["initial_slope"]) != slope:
                raise AssertionError("asymmetric sample coordinates")
            time = mpq(tau) * positive
            angle = root_energy * time / 2
            slope_mp = mpq(slope)
            factor = mp.cos(angle) + slope_mp * mp.sin(angle) / root_energy
            numerator = -root_energy * mp.sin(angle) + slope_mp * mp.cos(angle)
            close_decimal(sample["time"], time)
            close_decimal(sample["characteristic_factor"], factor)
            close_decimal(sample["jacobian"], factor * factor)
            close_decimal(sample["transported_slope"], numerator / factor)
            close_decimal(sample["transformed_energy_density"], numerator * numerator)
            if factor <= 0:
                raise AssertionError("asymmetric pre-breaking factor")
            checks += 12
        asymmetric_positive_labels += len(min_points)
        asymmetric_negative_labels += len(max_points)
        asymmetric_samples += len(expected_coords)
        checks += 18 + len(min_points) + len(max_points)

    enumeration = data["enumeration"]
    enumeration_keys = {
        "profiles", "breaking_labels", "sample_rows", "asymmetric_profiles",
        "asymmetric_positive_breaking_labels", "asymmetric_negative_breaking_labels",
        "asymmetric_sample_rows", "audited_leaf_count",
    }
    if set(enumeration) != enumeration_keys:
        raise AssertionError("enumeration schema")
    if (enumeration["profiles"], enumeration["breaking_labels"], enumeration["sample_rows"],
            enumeration["asymmetric_profiles"], enumeration["asymmetric_positive_breaking_labels"],
            enumeration["asymmetric_negative_breaking_labels"], enumeration["asymmetric_sample_rows"]) != (
            12, 78, 180, 6, asymmetric_positive_labels, asymmetric_negative_labels, asymmetric_samples):
        raise AssertionError("enumeration")
    body = dict(data)
    body.pop("payload_sha256")
    if enumeration["audited_leaf_count"] != leaves(body):
        raise AssertionError("leaf count")
    checks += 4
    print(f"C324 independent checker: PASS ({checks} checks)")


if __name__ == "__main__":
    main()
