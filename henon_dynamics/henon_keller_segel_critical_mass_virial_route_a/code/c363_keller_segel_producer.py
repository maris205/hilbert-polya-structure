#!/usr/bin/env python3
"""Canonical finite-evidence producer for HCS-C363 Keller--Segel."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c363_keller_segel_evidence.json"
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


def strict_yaml(path: Path):
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


def virial_rows():
    rows = []
    for raw_q in MASS_RATIOS:
        q = F(raw_q)
        for raw_i in MOMENTS:
            moment = F(raw_i)
            rows.append({
                "mass_ratio_M_over_8pi": s(q), "initial_second_moment": s(moment),
                "regime": regime(q), "M_over_pi": s(8*q),
                "virial_slope_over_pi": s(32*q*(1-q)),
                "pi_times_forced_breakdown_bound": (
                    s(moment/(32*q*(q-1))) if q > 1 else "not_applicable"),
                "finite_moment_hypothesis": True,
            })
    return rows


def scaling_rows():
    rows = []
    for raw_q in MASS_RATIOS:
        q = F(raw_q)
        coefficient = 16*q*(1-q)
        for raw_scale in SCALES:
            scale = F(raw_scale)
            sign = 0 if coefficient == 0 else (1 if coefficient > 0 else -1)
            log_sign = -1 if scale < 1 else 1
            product = sign*log_sign
            rows.append({
                "mass_ratio_M_over_8pi": s(q), "dilation_lambda": s(scale),
                "free_energy_shift_coefficient_over_pi_log_lambda": s(coefficient),
                "energy_shift_sign": "zero" if product == 0 else ("positive" if product > 0 else "negative"),
                "regime": regime(q),
            })
    return rows


def profile_rows():
    rows = []
    for raw_lam in LAMBDAS:
        lam = F(raw_lam)
        for raw_r in RADII:
            radius = F(raw_r)
            den = lam*lam+radius*radius
            rho = 8*lam*lam/den**2
            derivative = -4*radius/den
            laplacian_c = -8*lam*lam/den**2
            rows.append({
                "lambda": s(lam), "radius": s(radius), "density": s(rho),
                "c_radial": s(derivative), "log_rho_radial": s(derivative),
                "minus_laplacian_c": s(-laplacian_c), "poisson_residual": s(-laplacian_c-rho),
                "mass_inside_radius_over_pi": s(8*radius*radius/den),
                "stationary_flux_radial": s(rho*(derivative-derivative)),
            })
    return rows


def radial_rows():
    rows = []
    for raw_lam in LAMBDAS:
        lam = F(raw_lam)
        for raw_r in RADII:
            radius = F(raw_r)
            den = lam*lam+radius*radius
            n = 4*radius*radius/den
            nr = 8*radius*lam*lam/den**2
            nrr = 8*lam*lam*(lam*lam-3*radius*radius)/den**3
            diffusion = nrr-nr/radius
            attraction = n*nr/radius
            rows.append({
                "lambda": s(lam), "radius": s(radius),
                "normalized_cumulative_n": s(n), "n_r": s(nr), "n_rr": s(nrr),
                "diffusion_term": s(diffusion), "attraction_term": s(attraction),
                "stationary_radial_residual": s(diffusion+attraction),
            })
    return rows


def boundary_rows():
    return [
        {"boundary": "M=0", "classification": "zero density is stationary; the logarithmic dissipation identity is not invoked"},
        {"boundary": "0<M<8pi", "classification": "finite-moment virial slope is positive while a classical solution exists; no convergence theorem is claimed"},
        {"boundary": "M=8pi", "classification": "scale-invariant free energy and the translated critical stationary family"},
        {"boundary": "M>8pi", "classification": "finite-moment classical persistence is impossible beyond the virial upper bound"},
        {"boundary": "lambda_to_0", "classification": "critical profiles concentrate weakly to an 8pi Dirac mass outside the smooth phase space"},
        {"boundary": "lambda_to_infinity", "classification": "critical profiles spread and converge pointwise to zero while retaining total mass"},
        {"boundary": "infinite_second_moment", "classification": "every critical stationary profile lies outside the finite-second-moment virial hypothesis"},
    ]


def build(evaluation: Path):
    raw = evaluation.read_bytes()
    semantic = strict_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw hash")
    if hashlib.sha256(canonical(semantic)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic hash")
    virial = virial_rows()
    scaling = scaling_rows()
    profiles = profile_rows()
    radial = radial_rows()
    boundaries = boundary_rows()
    body = {
        "schema": "hcs-c363-keller-segel-evidence-v1",
        "candidate_id": "HCS-C363", "obstruction_id": "HEN-O347",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE,
        "fixed_epoch": 1788480000, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C363/2026-09-04.yaml",
                         "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {
            "pde": "rho_t=Delta rho-div(rho grad c); -Delta c=rho on R^2",
            "potential": "c(x)=-(1/(2pi)) integral rho(y) log|x-y| dy",
            "mass": "M=integral rho", "classical_domain": "assertion-specific C1-time C2-space nonnegative finite-mass density with justified flux and cutoff limits",
        },
        "theorem_contract": {
            "hypotheses": "finite first moment for barycenter; strict positivity and finite entropy interaction and dissipation for energy; finite second moment for virial",
            "conservation": "mass is constant and barycenter is constant when the first moment is finite",
            "energy": "for positive finite-energy data with finite dissipation, F=int rho log rho-(1/2)int rho c dissipates as -int rho|grad(log rho-c)|^2",
            "scaling": "F[rho_lambda]-F[rho]=2M(1-M/(8pi))log lambda",
            "virial": "I'=4M(1-M/(8pi)) for finite-second-moment classical solutions",
            "supercritical": "if M>8pi classical persistence cannot exceed 2pi I0/[M(M-8pi)]",
            "critical_family": "rho=8lambda^2/(lambda^2+|x-a|^2)^2 is stationary with mass 8pi and infinite second moment",
            "radial": "for r>0 n=m/(2pi) satisfies n_t=n_rr-n_r/r+n n_r/r, with m(0)=m_r(0)=0 and regular origin limit",
            "boundaries": "zero mass, three mass regimes, translations, scale limits, and singular Dirac limits are explicit",
        },
        "collision_boundary": {
            "C231": "porous-medium Barenblatt scaling, not chemotactic logarithmic attraction",
            "C260": "one-dimensional aggregation equation, not the two-dimensional eight-pi threshold",
            "C318": "nonlocal Fisher-KPP fronts, not mass-critical drift diffusion",
            "C347": "noisy Kuramoto phase density, not parabolic-elliptic chemotaxis",
        },
        "nonclaims": [
            "no full weak-solution construction or measure-valued continuation after concentration",
            "no theorem that all subcritical solutions converge to a stationary density",
            "no classification of nonradial critical dynamics beyond the displayed stationary family",
            "no target arithmetic local data, Euler factors, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route B",
        ],
        "references": [
            {"identifier": "DOI:10.1016/0022-5193(70)90092-5", "role": "original Keller-Segel model lineage"},
            {"identifier": "EJDE:2006/44", "role": "two-dimensional critical-mass analysis context"},
        ],
        "virial_rows": virial, "scaling_rows": scaling,
        "profile_rows": profiles, "radial_rows": radial,
        "boundary_rows": boundaries,
        "section_hashes": {name: digest(value) for name, value in (
            ("virial_rows", virial), ("scaling_rows", scaling),
            ("profile_rows", profiles), ("radial_rows", radial),
            ("boundary_rows", boundaries))},
        "enumeration": {"virial_rows": len(virial), "scaling_rows": len(scaling),
                        "profile_rows": len(profiles), "radial_rows": len(radial),
                        "boundary_rows": len(boundaries),
                        "finite_evidence_proves_pde_theorem": False},
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {"claims_target_arithmetic_local_data": False,
                        "claims_target_euler_factors": False,
                        "claims_root_number": False, "claims_automorphy": False,
                        "claims_target_divisor_or_counting_law": False,
                        "claims_target_functional_equation": False,
                        "claims_target_zero_match": False,
                        "claims_hilbert_polya_operator": False,
                        "invokes_route_b": False},
    }
    body["payload_sha256"] = hashlib.sha256(canonical(body)).hexdigest()
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C363 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(f"C363 producer: PASS {data['payload_sha256']}")


if __name__ == "__main__":
    main()
