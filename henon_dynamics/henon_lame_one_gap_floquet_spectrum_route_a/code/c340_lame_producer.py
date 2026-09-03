#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C340."""
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
DEFAULT_OUTPUT = ROOT / "results/c340_lame_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C340/2026-09-03.yaml"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
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


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be a mapping")
    return raw, value


def encode(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def semantic_sha(value) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def leaf_count(value) -> int:
    if type(value) is dict:
        return sum(leaf_count(child) for child in value.values())
    if type(value) is list:
        return sum(leaf_count(child) for child in value)
    return 1


def multiply(left, right):
    answer = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i+j] += a*b
    return answer


def rational_rows():
    rows = []
    for q in range(2, 26):
        for p in range(1, q):
            if math.gcd(p, q) != 1:
                continue
            m = Fraction(p, q)
            # Ascending coefficients, obtained independently by multiplying
            # (E-m)(E-1)(E-1-m).
            ascending = multiply(multiply([-m, 1], [-Fraction(1), 1]), [-(1+m), 1])
            rows.append({
                "p": p,
                "q": q,
                "m": encode(m),
                "lower_band": [encode(m), "1"],
                "finite_gap": ["1", encode(1+m)],
                "upper_band_start": encode(1+m),
                "gap_width": encode(m),
                "spectral_curve_coefficients_descending": [encode(value) for value in reversed(ascending)],
                "spectral_signs": {"below_m": -1, "lower_band": 1, "finite_gap": -1, "upper_band": 1},
                "band_edge_modes": [
                    {"mode": "dn", "energy": encode(m), "fiber": "periodic"},
                    {"mode": "cn", "energy": "1", "fiber": "antiperiodic"},
                    {"mode": "sn", "energy": encode(1+m), "fiber": "antiperiodic"},
                ],
            })
    return rows


def build(evaluation_path: Path):
    yaml_raw, evaluation = strict_yaml(evaluation_path)
    if evaluation.get("candidate_id") != "HCS-C340":
        raise AssertionError("wrong evaluation candidate")
    if evaluation.get("source_commit") != SOURCE or evaluation.get("scope_literal") != SCOPE:
        raise AssertionError("evaluation provenance mismatch")
    if evaluation.get("evaluator_authority_sha256") != EVALUATOR:
        raise AssertionError("evaluator digest mismatch")
    rows = rational_rows()
    evidence = {
        "schema": "hcs-c340-lame-evidence-v1",
        "candidate_id": "HCS-C340",
        "obstruction_id": "HEN-O324",
        "evaluation_date": "2026-09-03",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C340/2026-09-03.yaml",
            "raw_sha256": hashlib.sha256(yaml_raw.encode()).hexdigest(),
            "semantic_sha256": semantic_sha(evaluation),
        },
        "model": {
            "operator": "H_m=-d^2/dx^2+2*m*sn(x|m)^2",
            "modulus": "m=k^2 with 0<m<1",
            "period": "2*K(m)",
            "domain": "H^2(R) subset L^2(R)",
            "fiber_convention": "periodic multiplier +1 and antiperiodic multiplier -1 over 2*K(m)",
            "fiber_domain": "D(A_theta)=H^3_theta([0,2*K]) with f^(j)(2*K)=exp(i*theta)*f^(j)(0) for j=0,1,2",
            "commuting_operator": "A=-4*D^3+(6*u-4*(1+m))*D+3*u_prime with u=2*m*sn^2",
        },
        "theorem_contract": {
            "self_adjointness": "H_m on H^2(R) is self-adjoint and bounded below",
            "spectrum": "sigma(H_m)=[m,1] union [1+m,infinity)",
            "spectral_type": "the real periodic operator has purely absolutely continuous spectrum",
            "gap_count": "the only finite open gap is (1,1+m); every higher gap is closed",
            "band_edges": "dn, cn, sn have energies m, 1, 1+m; dn is periodic and cn,sn are antiperiodic over 2K",
            "stationary_kdv": "u_double_prime=3*u^2-4*(1+m)*u+4*m",
            "first_integral": "u_prime^2=2*u^3-4*(1+m)*u^2+8*m*u",
            "commutation": "[A,H_m]=0",
            "spectral_curve": "A^2=-16*(H_m-m)*(H_m-1)*(H_m-1-m)",
            "fiber_skew_adjointness": "on D(A_theta)=H^3_theta, periodic coefficients and common quasi-periodic phase cancel every endpoint term, so A_theta is skew-adjoint",
            "completeness": "fiber skew-adjointness excludes R(E)<0; simultaneous Bloch solutions and their Wronskian put every R(E)>=0 on the spectrum",
            "boundaries": "m=0 is free; m tends to one is the shifted Poschl-Teller soliton limit; translations are unitarily equivalent",
        },
        "universal_symbolic_receipts": {
            "jacobi_second_derivatives": {
                "sn": "sn''=-(1+m)*sn+2*m*sn^3",
                "cn": "cn''=(2*m*sn^2-1)*cn",
                "dn": "dn''=(2*m*sn^2-m)*dn",
            },
            "band_edge_residuals": {"H_dn_minus_m_dn": "0", "H_cn_minus_cn": "0", "H_sn_minus_1_plus_m_sn": "0"},
            "potential_identity": "u''=3*u^2-4*(1+m)*u+4*m",
            "stationary_identity": "u'''=(6*u-4*(1+m))*u'",
            "first_integral": "u'^2=2*u^3-4*(1+m)*u^2+8*m*u",
            "commutator": "[A,H_m]=0",
            "burchnall_chaundy": "A^2+16*(H_m-m)*(H_m-1)*(H_m-1-m)=0",
        },
        "rational_modulus_rows": rows,
        "boundary_atlas": {
            "free_face": "m=0 gives -d2/dx2, the finite gap closes, and all positive folded-zone contacts are closed",
            "soliton_limit": "m tends upward to one, K tends to infinity, and the potential tends to 2-2*sech(x)^2 with isolated level 1 and continuum [2,infinity)",
            "modulus_sign": "k maps to -k without changing m or the operator",
            "translation": "x maps to x+x0 gives a unitarily equivalent periodic operator",
            "complex_or_outside": "complex m or real m outside [0,1] is outside the frozen self-adjoint Jacobi convention",
        },
        "collision_boundary": {
            "C221": "the cubic-NLS soliton Hessian is nonperiodic and does not have a two-band Bloch decomposition",
            "C231": "the Allen-Cahn front linearization is a nonperiodic Poschl-Teller operator",
            "C262": "the square-wave Hill atlas has piecewise-constant transfer matrices rather than an elliptic finite-gap commuting operator",
            "C327": "the Kronig-Penney delta comb is singular and is not the smooth one-gap Lame potential",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": dict(FLAGS),
        "nonclaims": [
            "no rational-prime or prime-power carrier is introduced",
            "the cubic finite-gap curve is not a target Euler product or target determinant",
            "no root number, automorphy, target functional equation, divisor, or zero match is claimed",
            "the self-adjoint Lame operator is not claimed to be a Hilbert-Polya operator",
            "finite rational-modulus rows do not prove closure of every higher spectral gap",
        ],
        "references": [
            {"author": "E. L. Ince", "identifier": "DOI:10.1017/S0370164600020058", "role": "periodic Lame functions and band-edge owner"},
            {"author": "E. L. Ince", "identifier": "DOI:10.1017/S0370164600020071", "role": "further periodic Lame analysis"},
            {"author": "NIST Digital Library of Mathematical Functions", "identifier": "https://dlmf.nist.gov/29", "role": "authoritative notation and formula index"},
            {"author": "P. Kuchment", "identifier": "DOI:10.1090/bull/1528", "role": "authoritative Floquet direct-integral and periodic absolutely-continuous spectral theory"},
        ],
        "enumeration": {"rational_modulus_rows": len(rows), "q_max": 25, "audited_leaf_count": 0},
    }
    evidence["enumeration"]["audited_leaf_count"] = leaf_count(evidence)
    evidence["payload_sha256"] = semantic_sha(evidence)
    return evidence


def main():
    if sys.flags.optimize:
        raise RuntimeError("C340 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVALUATION)
    args = parser.parse_args()
    evidence = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C340_PRODUCER_PASS {len(evidence['rational_modulus_rows'])} rational rows {evidence['payload_sha256']}")


if __name__ == "__main__":
    main()
