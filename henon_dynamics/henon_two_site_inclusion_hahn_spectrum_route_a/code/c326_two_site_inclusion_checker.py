#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C326."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c326_two_site_inclusion_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C326/2026-09-03.yaml"
SOURCE = "1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "c85056e422437e7d31135550a458b4095e0a9e33bcbf4c5018f7a46007fe2e79"
YAML_SEMANTIC = "d37c8ed9bedff936bdfa64c5caa85312101ae2531cd043be53985c352761ccb9"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FLAGS = {"claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
         "claims_root_number": False, "claims_automorphy": False,
         "claims_target_divisor_or_counting_law": False,
         "claims_target_functional_equation": False, "claims_target_zero_match": False,
         "claims_hilbert_polya_operator": False, "invokes_route_b": False}


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path: Path):
    value = json.loads(path.read_text(), object_pairs_hook=pairs,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise TypeError("JSON root")
    return value


class Loader(yaml.SafeLoader):
    pass


Loader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    value = yaml.load(raw, Loader=Loader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def need(condition, label):
    if not condition:
        raise AssertionError(label)


def exact_keys(value, keys, label):
    need(type(value) is dict and set(value) == set(keys), f"{label} keys")


def canon(value):
    if type(value) is not str:
        raise TypeError("rational string")
    number = Fraction(value)
    rendered = str(number.numerator) if number.denominator == 1 else f"{number.numerator}/{number.denominator}"
    need(value == rendered, "canonical rational")
    return number


def q(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def pochhammer(a, k):
    answer = Fraction(1)
    for index in range(k):
        answer *= a + index
    return answer


def independent_hahn(n, alpha, degree, x):
    answer = Fraction(0)
    for k in range(degree + 1):
        answer += (pochhammer(-degree, k) * pochhammer(degree + 2 * alpha - 1, k) *
                   pochhammer(-x, k) /
                   (pochhammer(alpha, k) * pochhammer(-n, k) * math.factorial(k)))
    return answer


def leaves(value):
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def main():
    if sys.flags.optimize:
        raise RuntimeError("C326 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    root_keys = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
                 "source_commit", "scope_literal", "evaluator", "model", "theorem_contract",
                 "finite_grid", "parameter_rows", "alpha_zero_rows", "route_a_yaml",
                 "collision_boundary", "route_a", "scope_flags", "nonclaims", "references",
                 "enumeration", "payload_sha256"}
    exact_keys(data, root_keys, "root")
    required = {"schema": "hcs-c326-two-site-inclusion-v1", "candidate_id": "HCS-C326",
                "obstruction_id": "HEN-O310", "evaluation_date": "2026-09-03",
                "fixed_epoch": 1788393600, "source_commit": SOURCE, "scope_literal": SCOPE}
    for key, value in required.items():
        need(data[key] == value, key)
    need(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR,
                                "authority": "flow_systems/skills/route-a-evaluator.md"}, "evaluator")
    body = dict(data); payload = body.pop("payload_sha256")
    need(payload == hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"),
                                             ensure_ascii=False).encode()).hexdigest(), "payload")
    need(data["model"] == {
        "state_space": "x in {0,...,N}, recording site-one occupancy",
        "parameter_domain": "integer N>=0 and real alpha>0",
        "upward_rate": "(N-x)(alpha+x)",
        "downward_rate": "x(alpha+N-x)",
        "clock": "continuous time with the displayed unscaled generator"}, "model")
    need(data["theorem_contract"] == {
        "stationary_law": "unique beta-binomial(alpha,alpha) law when alpha>0",
        "spectrum": "simple eigenvalues j(j-1+2alpha), j=0,...,N",
        "eigenfunctions": "terminating Hahn 3F2 polynomials with exact orthogonality",
        "semigroup": "full finite spectral kernel and sharp L2 decay at gap 2alpha",
        "alpha_zero_face": "absorbing endpoints, coordinate martingale, hit-N probability x/N, all stationary mixtures c delta_0+(1-c) delta_N, and stationary weak limit half endpoints"}, "theorem")
    alpha_grid = [Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)]
    need(data["finite_grid"] == {"N_min": 0, "N_max": 8,
                                  "alpha_values": [q(a) for a in alpha_grid],
                                  "arithmetic": "exact rational"}, "grid")
    coordinates = [(a, n) for a in alpha_grid for n in range(9)]
    need(len(data["parameter_rows"]) == len(coordinates), "parameter length")
    checks = 32
    for row, (alpha, n) in zip(data["parameter_rows"], coordinates):
        exact_keys(row, {"N", "alpha", "stationary", "rate_rows", "spectral_rows"}, "parameter")
        need(row["N"] == n and canon(row["alpha"]) == alpha, "parameter coordinate")
        for sequence in (row["stationary"], row["rate_rows"], row["spectral_rows"]):
            need(len(sequence) == n + 1, "full coordinate range")
        raw_weights = [pochhammer(alpha, x) * pochhammer(alpha, n - x) /
                       (math.factorial(x) * math.factorial(n - x)) for x in range(n + 1)]
        normalizer = pochhammer(2 * alpha, n) / math.factorial(n)
        pi = [weight / normalizer for weight in raw_weights]
        need(sum(pi) == 1, "stationary normalization")
        for x, stationary in enumerate(row["stationary"]):
            exact_keys(stationary, {"x", "probability"}, "stationary cell")
            need(stationary["x"] == x and canon(stationary["probability"]) == pi[x], "stationary")
        for x, rate in enumerate(row["rate_rows"]):
            exact_keys(rate, {"x", "upward", "downward"}, "rate cell")
            up = Fraction(n - x) * (alpha + x); down = Fraction(x) * (alpha + n - x)
            need(rate["x"] == x and canon(rate["upward"]) == up and canon(rate["downward"]) == down, "rate")
            if x < n:
                next_down = Fraction(x + 1) * (alpha + n - x - 1)
                need(pi[x] * up == pi[x + 1] * next_down, "detailed balance")
        vectors = []
        for degree, spectral in enumerate(row["spectral_rows"]):
            exact_keys(spectral, {"degree", "eigenvalue", "hahn_values", "squared_norm"}, "spectral cell")
            need(spectral["degree"] == degree and len(spectral["hahn_values"]) == n + 1, "spectral coordinate")
            eigenvalue = Fraction(degree) * (degree - 1 + 2 * alpha)
            need(canon(spectral["eigenvalue"]) == eigenvalue, "eigenvalue")
            values = [independent_hahn(n, alpha, degree, x) for x in range(n + 1)]
            need([canon(value) for value in spectral["hahn_values"]] == values, "Hahn values")
            for x in range(n + 1):
                up = Fraction(n - x) * (alpha + x); down = Fraction(x) * (alpha + n - x)
                image = (up * (values[x + 1] - values[x]) if x < n else 0)
                image += (down * (values[x - 1] - values[x]) if x > 0 else 0)
                need(image == -eigenvalue * values[x], "difference equation")
            norm = sum(pi[x] * values[x] ** 2 for x in range(n + 1))
            need(norm > 0 and canon(spectral["squared_norm"]) == norm, "norm")
            for earlier in vectors:
                need(sum(pi[x] * values[x] * earlier[x] for x in range(n + 1)) == 0,
                     "orthogonality")
            vectors.append(values)
            checks += 2 * (n + 1) + degree + 3
    need(len(data["alpha_zero_rows"]) == 9, "boundary length")
    for n, row in enumerate(data["alpha_zero_rows"]):
        exact_keys(row, {"N", "rate_rows", "absorption_probability_at_N", "stationary_weak_limit",
                         "stationary_law_family"}, "boundary")
        need(row["N"] == n, "boundary coordinate")
        need(all(len(row[key]) == n + 1 for key in ("rate_rows", "absorption_probability_at_N", "stationary_weak_limit")), "boundary ranges")
        for x, rate in enumerate(row["rate_rows"]):
            exact_keys(rate, {"x", "upward", "downward"}, "boundary rate")
            value = Fraction(x * (n - x))
            need(rate["x"] == x and canon(rate["upward"]) == value and canon(rate["downward"]) == value, "boundary rate value")
        absorption = [Fraction(1)] if n == 0 else [Fraction(x, n) for x in range(n + 1)]
        limit = [Fraction(1)] if n == 0 else [Fraction(1, 2)] + [Fraction(0)] * (n - 1) + [Fraction(1, 2)]
        for key, expected in (("absorption_probability_at_N", absorption), ("stationary_weak_limit", limit)):
            for x, cell in enumerate(row[key]):
                exact_keys(cell, {"x", "probability"}, "boundary probability")
                need(cell["x"] == x and canon(cell["probability"]) == expected[x], "boundary probability value")
        need(row["stationary_law_family"] ==
             ("delta_0" if n == 0 else "c delta_0+(1-c) delta_N for 0<=c<=1"),
             "stationary family")
        checks += 3 * (n + 1) + 1
    evaluation = strict_yaml(args.evaluation)
    yaml_keys = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
                 "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
                 "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
                 "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
                 "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
                 "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
                 "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
                 "source_owner_tokens"}
    exact_keys(evaluation, yaml_keys, "evaluation")
    gate_objects = {
        "a0": {"verdict": "A0_FAIL", "evidence_status": "PROVED",
               "strongest_evidence": "model inputs contain no target arithmetic data",
               "strongest_failure": "no arithmetic target datum is present to reproduce"},
        "a1": {"verdict": "A1_FAIL", "evidence_status": "PROVED",
               "strongest_evidence": "rates depend only on N, alpha, and occupancy",
               "strongest_failure": "no intrinsic arithmetic invariant is encoded"},
        "a2": {"verdict": "A2_FAIL", "evidence_status": "STOP_SCOPED",
               "strongest_evidence": "exact Hahn spectrum and beta-binomial reversibility",
               "strongest_failure": "no target Euler factor or local factor map is defined"},
        "a3": {"verdict": "A3_FAIL", "evidence_status": "STOP_SCOPED",
               "strongest_evidence": "a complete finite semigroup kernel is proved",
               "strongest_failure": "no target divisor, functional equation, or zero set is compared"},
        "a4": {"verdict": "A4_FORMAL_HINT", "evidence_status": "PROVED",
               "strongest_evidence": "self-adjoint Markov generator has explicit finite spectrum",
               "strongest_failure": "finite Markov spectrum is not a Hilbert--Polya construction"},
    }
    for branch, expected_gate in gate_objects.items():
        exact_keys(evaluation[branch], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, branch)
        need(evaluation[branch] == expected_gate, f"{branch} semantics")
    lock = data["route_a_yaml"]
    exact_keys(lock, {"relative_path", "raw_sha256", "semantic_sha256"}, "YAML lock")
    need(lock["relative_path"] == "evaluations/route_a/HCS-C326/2026-09-03.yaml", "YAML path")
    raw = hashlib.sha256(args.evaluation.read_bytes()).hexdigest()
    semantic = hashlib.sha256(json.dumps(evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    need(raw == lock["raw_sha256"] == YAML_RAW and semantic == lock["semantic_sha256"] == YAML_SEMANTIC, "YAML hashes")
    need(evaluation["candidate_id"] == "HCS-C326" and evaluation["obstruction_id"] == "HEN-O310" and
         evaluation["evaluation_date"] == "2026-09-03" and evaluation["source_commit"] == SOURCE and
         evaluation["fixed_epoch"] == 1788393600 and evaluation["scope_literal"] == SCOPE, "YAML identity")
    need(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md" and
         evaluation["evaluator_version"] == "0.2.0" and evaluation["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    route = {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
             "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    need(data["route_a"] == route and evaluation["tuple"] == route["tuple"] and
         evaluation["overall_verdict"] == route["overall"] and evaluation["route_b_invocation_allowed"] is False, "route")
    need([evaluation[b]["verdict"] for b in ("a0", "a1", "a2", "a3", "a4")] == route["tuple"], "branch verdicts")
    need([evaluation[b]["evidence_status"] for b in ("a0", "a1", "a2", "a3", "a4")] ==
         ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "PROVED"], "branch statuses")
    need(evaluation["theorem_status"] == "PROVABLE_AS_STATED" and evaluation["training_data"] == "none" and
         evaluation["source_owner_tokens"] == ["arXiv:0906.4664", "DLMF:18.19", "DLMF:18.20.5",
                                                "DLMF:18.22(ii)"], "YAML semantic locks")
    yaml_literals = {
        "schema": "route-a-evaluation-v0.2.0",
        "title": "Two-site symmetric inclusion process, Hahn diagonalization, and absorbing-face limit",
        "candidate_definition": "finite birth-death chain x in 0..N with inclusion rates (N-x)(alpha+x) and x(alpha+N-x)",
        "family": "conservative interacting-particle birth-death dynamics",
        "phase_space": "integer interval 0..N",
        "dynamics": "continuous-time two-site symmetric inclusion process",
        "parameters": "integer N at least zero and real alpha greater than zero, with alpha down to zero treated separately",
        "parameter_provenance": "theorem parameters, not fitted data",
        "arithmetic_origin": "none",
        "clock": "continuous time with generator rates exactly as displayed",
        "normalization": "state x is site-one occupancy and N-x is site-two occupancy",
        "determinant_convention": "none", "orbit_cutoff": "none",
        "precision": "exact rational evidence on a finite rational grid",
        "forbidden_data": "target local factors, root numbers, automorphy labels, target zeros, or fitted arithmetic data",
        "finite_evidence_role": "exact rational regression audit only, never proof by finite extrapolation",
        "route_b_lock_reason": "Route A failure does not authorize Route B under the scope firewall",
    }
    for key, value in yaml_literals.items():
        need(evaluation[key] == value, f"YAML literal {key}")
    need(evaluation["artifact_paths"] == ["results/c326_two_site_inclusion_evidence.json",
                                          "THEOREM_PACKAGE.md", "paper/main.pdf"], "YAML artifacts")
    checks += 23
    need(data["scope_flags"] == FLAGS and evaluation["scope_flags"] == FLAGS, "scope")
    need(data["collision_boundary"] == {
        "C253": "Moran fixation owns a killed population chain, not reversible inclusion or Hahn diagonalization",
        "C263": "Polya urn reinforcement is discrete-time growth, not fixed-mass continuous-time exchange",
        "C285": "Gordon--Newell owns multisite product form and bottlenecks, not this full two-site spectrum",
        "C322": "Kac sphere collisions use spherical harmonics, not a conservative occupancy chain"}, "collisions")
    need(data["nonclaims"] == [
        "Finite rational diagonalizations audit but do not prove the all-parameter theorem.",
        "No multisite, open-boundary, or condensation-scaling theorem is asserted.",
        "No literature-priority claim is made.",
        "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target zero match, or Hilbert--Polya operator is asserted."], "nonclaims")
    need(data["references"] == [
        {"authors": "Cristian Giardina, Frank Redig, and Kiamars Vafayi",
         "title": "Correlation inequalities for interacting particle systems with duality", "identifier": "10.1007/s10955-010-0055-0; arXiv:0906.4664"},
        {"authors": "NIST Digital Library of Mathematical Functions",
         "title": "Hahn class definitions, explicit representation, and difference equations",
         "identifier": "DLMF:18.19; DLMF:18.20.5; DLMF:18.22(ii)"}], "references")
    exact_keys(data["enumeration"], {"parameter_rows", "state_rows", "spectral_rows", "alpha_zero_rows", "audited_leaf_count"}, "enumeration")
    counted = dict(data); counted.pop("payload_sha256"); enumeration = counted.pop("enumeration")
    need(enumeration == {"parameter_rows": 36, "state_rows": 180, "spectral_rows": 180,
                         "alpha_zero_rows": 9, "audited_leaf_count": leaves(counted)}, "enumeration values")
    print(f"C326 independent checker: PASS ({checks} exact checks, 180 states, 180 Hahn vectors)")


if __name__ == "__main__":
    main()
