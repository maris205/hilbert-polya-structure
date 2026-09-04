#!/usr/bin/env python3
"""Independent exact checker for HCS-C363; imports no producer code."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c363_keller_segel_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C363/2026-09-04.yaml"
SOURCE = "05ca5f96b2c69a6ad6ba153d1084df750d7722c0"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "aa52111eaa5c48cb46a895a7ff4c4b0ebcfed5a91d8f3a37ef8b9a083a04488a"
YAML_SEMANTIC = "7914a5f2d01e7ca45e1619289dd962bbf29638bd70734fdc4923c461115120a9"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
MASS_RATIOS = ("1/4", "1/2", "3/4", "1", "5/4", "3/2", "2")
MOMENTS = ("1/2", "1", "3")
SCALES = ("1/2", "2", "3")
LAMBDAS = ("1/2", "1", "2")
RADII = ("1/2", "1", "3")
TOP_KEYS = {"schema", "candidate_id", "obstruction_id", "evaluation_date",
            "source_commit", "fixed_epoch", "scope_literal", "evaluator",
            "route_a_yaml", "model", "theorem_contract", "collision_boundary",
            "nonclaims", "references", "virial_rows", "scaling_rows",
            "profile_rows", "radial_rows", "boundary_rows", "section_hashes",
            "enumeration", "route_a", "scope_flags", "payload_sha256"}
YAML_KEYS = {"schema", "candidate_id", "title", "evaluation_date", "source_commit",
             "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
             "evaluator_authority_sha256", "obstruction_id", "candidate_definition",
             "family", "phase_space", "dynamics", "parameters", "parameter_provenance",
             "arithmetic_origin", "clock", "normalization", "determinant_convention",
             "orbit_cutoff", "precision", "training_data", "forbidden_data",
             "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple",
             "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason",
             "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
FALSE_FLAGS = {"claims_target_arithmetic_local_data", "claims_target_euler_factors",
               "claims_root_number", "claims_automorphy",
               "claims_target_divisor_or_counting_law",
               "claims_target_functional_equation", "claims_target_zero_match",
               "claims_hilbert_polya_operator", "invokes_route_b"}
MODEL = {
    "pde": "rho_t=Delta rho-div(rho grad c); -Delta c=rho on R^2",
    "potential": "c(x)=-(1/(2pi)) integral rho(y) log|x-y| dy",
    "mass": "M=integral rho", "classical_domain": "assertion-specific C1-time C2-space nonnegative finite-mass density with justified flux and cutoff limits",
}
THEOREM = {
    "hypotheses": "finite first moment for barycenter; strict positivity and finite entropy interaction and dissipation for energy; finite second moment for virial",
    "conservation": "mass is constant and barycenter is constant when the first moment is finite",
    "energy": "for positive finite-energy data with finite dissipation, F=int rho log rho-(1/2)int rho c dissipates as -int rho|grad(log rho-c)|^2",
    "scaling": "F[rho_lambda]-F[rho]=2M(1-M/(8pi))log lambda",
    "virial": "I'=4M(1-M/(8pi)) for finite-second-moment classical solutions",
    "supercritical": "if M>8pi classical persistence cannot exceed 2pi I0/[M(M-8pi)]",
    "critical_family": "rho=8lambda^2/(lambda^2+|x-a|^2)^2 is stationary with mass 8pi and infinite second moment",
    "radial": "for r>0 n=m/(2pi) satisfies n_t=n_rr-n_r/r+n n_r/r, with m(0)=m_r(0)=0 and regular origin limit",
    "boundaries": "zero mass, three mass regimes, translations, scale limits, and singular Dirac limits are explicit",
}
COLLISIONS = {
    "C231": "porous-medium Barenblatt scaling, not chemotactic logarithmic attraction",
    "C260": "one-dimensional aggregation equation, not the two-dimensional eight-pi threshold",
    "C318": "nonlocal Fisher-KPP fronts, not mass-critical drift diffusion",
    "C347": "noisy Kuramoto phase density, not parabolic-elliptic chemotaxis",
}
NONCLAIMS = [
    "no full weak-solution construction or measure-valued continuation after concentration",
    "no theorem that all subcritical solutions converge to a stationary density",
    "no classification of nonradial critical dynamics beyond the displayed stationary family",
    "no target arithmetic local data, Euler factors, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route B",
]
REFERENCES = [
    {"identifier": "DOI:10.1016/0022-5193(70)90092-5", "role": "original Keller-Segel model lineage"},
    {"identifier": "EJDE:2006/44", "role": "two-dimensional critical-mass analysis context"},
]
BOUNDARIES = [
    {"boundary": "M=0", "classification": "zero density is stationary; the logarithmic dissipation identity is not invoked"},
    {"boundary": "0<M<8pi", "classification": "finite-moment virial slope is positive while a classical solution exists; no convergence theorem is claimed"},
    {"boundary": "M=8pi", "classification": "scale-invariant free energy and the translated critical stationary family"},
    {"boundary": "M>8pi", "classification": "finite-moment classical persistence is impossible beyond the virial upper bound"},
    {"boundary": "lambda_to_0", "classification": "critical profiles concentrate weakly to an 8pi Dirac mass outside the smooth phase space"},
    {"boundary": "lambda_to_infinity", "classification": "critical profiles spread and converge pointwise to zero while retaining total mass"},
    {"boundary": "infinite_second_moment", "classification": "every critical stationary profile lies outside the finite-second-moment virial hypothesis"},
]


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values
          if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("merge key")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate/non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                             strict_mapping)


def load_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode()


def s(value):
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def regime(q):
    return "subcritical" if q < 1 else ("critical" if q == 1 else "supercritical")


def expected_virial():
    answer = []
    for qq in MASS_RATIOS:
        q = F(qq)
        for ii in MOMENTS:
            moment = F(ii)
            answer.append({"mass_ratio_M_over_8pi": s(q), "initial_second_moment": s(moment),
                           "regime": regime(q), "M_over_pi": s(8*q),
                           "virial_slope_over_pi": s(32*q*(1-q)),
                           "pi_times_forced_breakdown_bound": s(moment/(32*q*(q-1))) if q > 1 else "not_applicable",
                           "finite_moment_hypothesis": True})
    return answer


def expected_scaling():
    answer = []
    for qq in MASS_RATIOS:
        q = F(qq)
        coefficient = 16*q*(1-q)
        for ll in SCALES:
            scale = F(ll)
            sign = 0 if coefficient == 0 else (1 if coefficient > 0 else -1)
            product = sign*(-1 if scale < 1 else 1)
            answer.append({"mass_ratio_M_over_8pi": s(q), "dilation_lambda": s(scale),
                           "free_energy_shift_coefficient_over_pi_log_lambda": s(coefficient),
                           "energy_shift_sign": "zero" if product == 0 else ("positive" if product > 0 else "negative"),
                           "regime": regime(q)})
    return answer


def expected_profiles():
    answer = []
    for ll in LAMBDAS:
        lam = F(ll)
        for rr in RADII:
            radius = F(rr)
            den = lam**2+radius**2
            rho = 8*lam**2/den**2
            derivative = -4*radius/den
            minus_lap = 8*lam**2/den**2
            answer.append({"lambda": s(lam), "radius": s(radius), "density": s(rho),
                           "c_radial": s(derivative), "log_rho_radial": s(derivative),
                           "minus_laplacian_c": s(minus_lap),
                           "poisson_residual": s(minus_lap-rho),
                           "mass_inside_radius_over_pi": s(8*radius**2/den),
                           "stationary_flux_radial": s(rho*(derivative-derivative))})
    return answer


def expected_radial():
    answer = []
    for ll in LAMBDAS:
        lam = F(ll)
        for rr in RADII:
            radius = F(rr)
            den = lam**2+radius**2
            n = 4*radius**2/den
            nr = 8*radius*lam**2/den**2
            nrr = 8*lam**2*(lam**2-3*radius**2)/den**3
            diffusion = nrr-nr/radius
            attraction = n*nr/radius
            answer.append({"lambda": s(lam), "radius": s(radius),
                           "normalized_cumulative_n": s(n), "n_r": s(nr), "n_rr": s(nrr),
                           "diffusion_term": s(diffusion), "attraction_term": s(attraction),
                           "stationary_radial_residual": s(diffusion+attraction)})
    return answer


def check(path, evaluation):
    count = 0
    data = json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(data) is not dict or set(data) != TOP_KEYS:
        raise AssertionError("evidence top-level schema")
    body = dict(data)
    claimed = body.pop("payload_sha256")
    if claimed != hashlib.sha256(canonical(body)).hexdigest():
        raise AssertionError("payload hash")
    count += 2
    identity = (data["schema"], data["candidate_id"], data["obstruction_id"],
                data["evaluation_date"], data["source_commit"], data["fixed_epoch"], data["scope_literal"])
    if identity != ("hcs-c363-keller-segel-evidence-v1", "HCS-C363", "HEN-O347",
                    "2026-09-04", SOURCE, 1788480000, SCOPE):
        raise AssertionError("identity")
    count += 7
    if data["evaluator"] != {"authority": "flow_systems/skills/route-a-evaluator.md",
                             "version": "0.2.0", "sha256": EVALUATOR}:
        raise AssertionError("evaluator")
    if data["route_a_yaml"] != {"relative_path": "evaluations/route_a/HCS-C363/2026-09-04.yaml",
                                 "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC}:
        raise AssertionError("yaml receipt")
    count += 2
    raw = evaluation.read_bytes()
    yml = load_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW or hashlib.sha256(canonical(yml)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation digest")
    if set(yml) != YAML_KEYS:
        raise AssertionError("evaluation keys")
    if (yml["schema"], yml["candidate_id"], yml["obstruction_id"], yml["evaluation_date"],
            yml["source_commit"], yml["fixed_epoch"], yml["scope_literal"]) != (
            "route-a-evaluation-v0.2.0", "HCS-C363", "HEN-O347", "2026-09-04",
            SOURCE, 1788480000, SCOPE):
        raise AssertionError("evaluation identity")
    route_tuple = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
    if yml["tuple"] != route_tuple or yml["overall_verdict"] != "ROUTE_A_REJECTED" or yml["route_b_invocation_allowed"] is not False:
        raise AssertionError("evaluation route")
    if set(yml["scope_flags"]) != FALSE_FLAGS or any(yml["scope_flags"].values()):
        raise AssertionError("evaluation flags")
    if yml["artifact_paths"] != ["results/c363_keller_segel_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"]:
        raise AssertionError("evaluation artifacts")
    count += 7
    if data["model"] != MODEL or data["theorem_contract"] != THEOREM:
        raise AssertionError("model/theorem")
    if data["collision_boundary"] != COLLISIONS or data["nonclaims"] != NONCLAIMS or data["references"] != REFERENCES:
        raise AssertionError("fixed narrative fields")
    count += 5
    sections = {"virial_rows": expected_virial(), "scaling_rows": expected_scaling(),
                "profile_rows": expected_profiles(), "radial_rows": expected_radial(),
                "boundary_rows": BOUNDARIES}
    for name, expected in sections.items():
        if data[name] != expected:
            raise AssertionError(name)
        if data["section_hashes"].get(name) != digest(expected):
            raise AssertionError(name+" hash")
        count += len(expected)+1
    if set(data["section_hashes"]) != set(sections):
        raise AssertionError("section hashes")
    counts = {name: len(value) for name, value in sections.items()}
    counts["finite_evidence_proves_pde_theorem"] = False
    if data["enumeration"] != counts:
        raise AssertionError("enumeration")
    if data["route_a"] != {"tuple": route_tuple, "overall": "ROUTE_A_REJECTED",
                            "route_b_invocation_allowed": False}:
        raise AssertionError("route A")
    if set(data["scope_flags"]) != FALSE_FLAGS or any(data["scope_flags"].values()):
        raise AssertionError("scope flags")
    count += 4
    return count


def main():
    if sys.flags.optimize:
        raise RuntimeError("C363 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    print(f"C363 independent checker: PASS {check(args.evidence, args.evaluation)} checks")


if __name__ == "__main__":
    main()
