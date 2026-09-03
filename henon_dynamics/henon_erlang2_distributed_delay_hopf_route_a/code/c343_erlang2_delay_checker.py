#!/usr/bin/env python3
"""Producer-independent strict checker for HCS-C343."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml
from yaml.tokens import AliasToken, AnchorToken


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c343_erlang2_delay_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C343/2026-09-03.yaml"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "7c148a98c804c66d57ed14946fb3e59b945098fe259a55ade3c9054002ab9033"
EVAL_SEMANTIC = "4f804ecbfce827f03931d97aae994fb8a346fd5e9ba064eb3b31f4c6e2067c08"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
AUDITED_LEAVES = 2017

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
MODEL = {
    "equation": "x'(t)=-a*x(t)-b*integral_0^infinity r^2*s*exp(-r*s)*x(t-s) ds",
    "domain": "a>=0, b>=0, r>0 with compatible fading-memory histories",
    "kernel": "K_r(s)=r^2*s*exp(-r*s) for s>=0",
    "chain": "x'=-a*x-b*z2; z1'=r*(x-z1); z2'=r*(z1-z2)",
    "generator": "[[-a,0,-b],[r,-r,0],[0,r,-r]]",
    "characteristic": "(lambda+a)*(lambda+r)^2+b*r^2",
}
THEOREM = {
    "linear_chain": "the distributed-delay equation equals the three-state chain for compatible histories",
    "stability": "for b>0 exponential stability holds iff b<2*(a+r)^2/r",
    "hopf": "at equality the roots are -(a+2r) and plus/minus i*sqrt(r*(r+2a)), with positive crossing speed",
    "unstable_count": "for b above threshold the cubic has exactly two open-right-half-plane roots",
    "repeated_roots": "b=0 gives the -r Jordan boundary; a<r also gives one positive-feedback double-root surface",
    "nonlinear_boundary": "a simple imaginary crossing is proved; no nonlinear periodic-orbit existence is claimed",
}
REFERENCES = [
    {"identifier": "10.1007/s00285-019-01412-w", "role": "official linear-chain-trick source"},
    {"identifier": "10.1016/0022-247X(89)90081-4", "role": "primary gamma-delay stability source"},
    {"identifier": "10.1007/978-3-642-93107-9", "role": "source monograph on distributed lags"},
]
COLLISIONS = {
    "C210": "a scalar discrete retarded delay with an infinite Lambert-W root ladder, not a distributed Erlang memory",
    "C218": "a Kelvin-Voigt damped wave PDE, not a finite Markov realization of distributed delay",
    "C272": "an Erlang age-transport renewal PDE, not a scalar negative-feedback delay and Hopf/Jordan atlas",
}
NONCLAIMS = [
    "No nonlinear limit cycle, Hopf periodic branch, or global nonlinear bifurcation is claimed.",
    "No priority claim is made for the linear-chain trick, gamma-delay stability, or Routh-Hurwitz theory.",
    "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route-B input is claimed.",
]
GRID = {
    "a_values": ["0", "1/2", "1", "2", "3"],
    "r_values": ["1/2", "1", "2", "3"],
    "routh_faces": ["0", "b_h/4", "3*b_h/4", "b_h", "5*b_h/4", "2*b_h"],
    "evidence_role": "exact finite receipt, not proof by sampling",
}
BOUNDARIES = {
    "a_zero_b_positive": "stable for 0<b<2r, simple imaginary pair at b=2r, two RHP roots for b>2r",
    "a_zero_b_zero": "one constant x mode and one size-two Jordan block at -r",
    "b_zero_a_positive": "exponentially stable despite a size-two Jordan block at -r",
    "a_equals_r_b_zero": "one size-three Jordan block at -r",
    "r_zero": "excluded because the displayed Erlang density ceases to be a normalized kernel",
    "large_r": "the memory transfer r^2/(lambda+r)^2 tends to one; the reduced slow rate tends to -(a+b)",
    "history_compatibility": "arbitrary chain states are not asserted to encode a prescribed prehistory; initial z1,z2 are the two kernel integrals",
}
TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "evaluation", "model", "theorem_contract",
    "references", "collision_boundary", "nonclaims", "route_a", "scope_flags",
    "parameter_grid", "kernel_rows", "routh_rows", "hopf_rows",
    "repeated_root_rows", "boundary_rows", "enumeration", "payload_sha256",
}
EVAL_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths",
    "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict",
    "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status",
    "finite_evidence_role", "source_owner_tokens",
}
EVAL_FIXED = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C343",
    "title": "Erlang-2 distributed-delay negative-feedback Hopf and Jordan atlas",
    "evaluation_date": "2026-09-03",
    "source_commit": SOURCE,
    "fixed_epoch": EPOCH,
    "scope_literal": SCOPE,
    "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O327",
    "candidate_definition": "scalar linear negative feedback through the normalized Erlang shape-two kernel r squared times s times exp(-r s)",
    "family": "distributed-delay equations with a finite linear-chain realization",
    "phase_space": "compatible fading-memory scalar histories, represented by a three-dimensional real linear-chain state",
    "dynamics": "autonomous distributed-memory feedback and its exact Erlang-2 Markov realization",
    "parameters": "nonnegative damping a, nonnegative feedback b, and positive Erlang rate r",
    "parameter_provenance": "source-local damping, feedback, and memory-rate parameters only, never target-fitted",
    "arithmetic_origin": "none",
    "clock": "source physical continuous time",
    "normalization": "the Erlang-2 kernel r squared s exp(-r s) has unit mass, mean 2/r, and variance 2/r squared",
    "determinant_convention": "only the cubic characteristic polynomial of the linear generator is used; no dynamical Euler product or target determinant is defined",
    "orbit_cutoff": "all-time analytic linear theorem; finite rational parameter grids are implementation receipts only",
    "precision": "exact rational and symbolic polynomial identities with no fitted or target-derived constants",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor or functional equation, target zeros, Hilbert-Polya operators, and Route B",
    "artifact_paths": ["results/c343_erlang2_delay_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no arithmetic source, prime clock, target Euler factor, target divisor, or natural target-zero quantization exists",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "kernel, characteristic, Routh, crossing, root-count, discriminant, Jordan, and implementation receipt only; analytic arguments prove the parameter-continuum theorem",
    "source_owner_tokens": [
        "10.1007/s00285-019-01412-w",
        "10.1016/0022-247X(89)90081-4",
        "10.1007/978-3-642-93107-9",
    ],
}
GATES = {
    "a0": {
        "verdict": "A0_FAIL", "evidence_status": "PROVED",
        "strongest_evidence": "the delay kernel, linear chain, stability threshold, and Jordan atlas are derived exactly from source parameters",
        "strongest_failure": "the model has no intrinsic rational-prime or prime-power payload and no arithmetic source",
    },
    "a1": {
        "verdict": "A1_FAIL", "evidence_status": "PROVED",
        "strongest_evidence": "the complete modal and semigroup dynamics are explicit",
        "strongest_failure": "linear modes and a Hopf crossing are not an arithmetic primitive-periodic-orbit ledger with repetition weights",
    },
    "a2": {
        "verdict": "A2_FAIL", "evidence_status": "STOP_SCOPED",
        "strongest_evidence": "the cubic characteristic polynomial and exact spectral projectors are source-local",
        "strongest_failure": "no primitive-orbit Euler product, Fredholm determinant, or target divisor is defined",
    },
    "a3": {
        "verdict": "A3_FAIL", "evidence_status": "STOP_SCOPED",
        "strongest_evidence": "all stable, crossing, unstable, and repeated-root parameter faces are covered analytically",
        "strongest_failure": "the theorem supplies no target functional equation, continuation, counting law, or Weil compression",
    },
    "a4": {
        "verdict": "A4_FAIL", "evidence_status": "STOP_SCOPED",
        "strongest_evidence": "the finite linear-chain generator is canonical for the frozen distributed delay",
        "strongest_failure": "no natural unitary, Hamiltonian, scattering, or self-adjoint quantization tied to target zeros is supplied",
    },
}


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in values if tag != "tag:yaml.org,2002:timestamp"]
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


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def duplicate_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path: Path):
    value = json.loads(
        path.read_text(), object_pairs_hook=duplicate_pairs,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )
    if type(value) is not dict:
        raise ValueError("evidence root must be an object")
    return value


def strict_yaml(path: Path):
    raw = path.read_bytes()
    tokens = list(yaml.scan(raw.decode()))
    if any(isinstance(token, (AliasToken, AnchorToken)) for token in tokens):
        raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw.decode(), Loader=UniqueLoader)
    if type(value) is not dict:
        raise ValueError("evaluation root must be a mapping")
    return raw, value


def canonical_hash(value) -> str:
    return sha(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def q(value: str) -> Fraction:
    if type(value) is not str:
        raise ValueError("rational encoding is not a string")
    return Fraction(value)


def leaf_count(value) -> int:
    if type(value) is dict:
        return sum(leaf_count(child) for child in value.values())
    if type(value) is list:
        return sum(leaf_count(child) for child in value)
    return 1


def disc(c2: Fraction, c1: Fraction, c0: Fraction) -> Fraction:
    return c2*c2*c1*c1 - 4*c1**3 - 4*c2**3*c0 - 27*c0*c0 + 18*c2*c1*c0


def check_evaluation(path: Path, evidence: dict) -> int:
    raw, value = strict_yaml(path)
    if sha(raw) != EVAL_RAW or canonical_hash(value) != EVAL_SEMANTIC:
        raise AssertionError("evaluation raw/semantic lock mismatch")
    if set(value) != EVAL_KEYS:
        raise AssertionError("evaluation key schema mismatch")
    for key, expected in EVAL_FIXED.items():
        if value.get(key) != expected:
            raise AssertionError(f"evaluation field mismatch: {key}")
    for key, expected in GATES.items():
        if value.get(key) != expected:
            raise AssertionError(f"evaluation gate mismatch: {key}")
    if evidence["evaluation"] != {
        "path": "evaluations/route_a/HCS-C343/2026-09-03.yaml",
        "raw_sha256": EVAL_RAW,
        "semantic_sha256": EVAL_SEMANTIC,
    }:
        raise AssertionError("nested evaluation carrier mismatch")
    return leaf_count(value)


def check_payload(data: dict) -> int:
    if set(data) != TOP_KEYS:
        raise AssertionError("top-level evidence schema mismatch")
    body = dict(data)
    claimed = body.pop("payload_sha256")
    if type(claimed) is not str or len(claimed) != 64 or canonical_hash(body) != claimed:
        raise AssertionError("evidence payload hash mismatch")
    fixed = {
        "schema": "hcs-c343-erlang2-delay-v1",
        "candidate_id": "HCS-C343",
        "obstruction_id": "HEN-O327",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL,
        "theorem_contract": THEOREM,
        "references": REFERENCES,
        "collision_boundary": COLLISIONS,
        "nonclaims": NONCLAIMS,
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "parameter_grid": GRID,
        "boundary_rows": BOUNDARIES,
    }
    for key, expected in fixed.items():
        if data[key] != expected:
            raise AssertionError(f"fixed evidence field mismatch: {key}")
    return 1


def check_kernels(rows: list) -> int:
    rates = [Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5)]
    if type(rows) is not list or len(rows) != len(rates):
        raise AssertionError("kernel row count")
    checks = 0
    for row, r in zip(rows, rates):
        expected = {
            "r": qstr(r), "mass": "1", "mean": qstr(2/r),
            "second_moment": qstr(6/r**2), "variance": qstr(2/r**2),
            "laplace_transform": f"{qstr(r**2)}/(lambda+{qstr(r)})^2",
            "chain_identity": "z1'=r(x-z1); z2'=r(z1-z2)",
        }
        if row != expected:
            raise AssertionError(f"kernel row {r}")
        if q(row["second_moment"])-q(row["mean"])**2 != q(row["variance"]):
            raise AssertionError("kernel variance")
        checks += 9
    return checks


def check_routh(rows: list) -> int:
    a_values = [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
    r_values = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
    faces = [
        ("zero_feedback", Fraction(0)),
        ("quarter_threshold", Fraction(1, 4)),
        ("below_threshold", Fraction(3, 4)),
        ("hopf_threshold", Fraction(1)),
        ("above_threshold", Fraction(5, 4)),
        ("double_threshold", Fraction(2)),
    ]
    if type(rows) is not list or len(rows) != 120:
        raise AssertionError("Routh row count")
    checks = 0
    index = 0
    for a in a_values:
        for r in r_values:
            b_h = 2*(a+r)**2/r
            for face, ratio in faces:
                b = ratio*b_h
                c2, c1, c0 = a+2*r, r*(r+2*a), r*r*(a+b)
                margin = c2*c1-c0
                if b == 0:
                    classification = "marginal_constant" if a == 0 else "stable_jordan"
                    rhp = 0
                elif b < b_h:
                    classification, rhp = "exponentially_stable", 0
                elif b == b_h:
                    classification, rhp = "simple_imaginary_pair", 0
                else:
                    classification, rhp = "two_rhp_roots", 2
                expected = {
                    "a": qstr(a), "r": qstr(r), "face": face,
                    "b_over_b_h": qstr(ratio), "b": qstr(b), "b_h": qstr(b_h),
                    "coefficients_c2_c1_c0": [qstr(c2), qstr(c1), qstr(c0)],
                    "routh_margin": qstr(margin),
                    "classification": classification, "rhp_root_count": rhp,
                }
                if rows[index] != expected:
                    raise AssertionError(f"Routh row {index}")
                if margin != r*(2*(a+r)**2-b*r):
                    raise AssertionError("Routh identity")
                index += 1
                checks += 15
    return checks


def check_hopf(rows: list) -> int:
    a_values = [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
    r_values = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
    if type(rows) is not list or len(rows) != 20:
        raise AssertionError("Hopf row count")
    checks = 0
    index = 0
    for a in a_values:
        for r in r_values:
            c2 = a+2*r
            omega2 = r*(r+2*a)
            b_h = 2*(a+r)**2/r
            derivative = r*r/(2*(omega2+c2*c2))
            expected = {
                "a": qstr(a), "r": qstr(r), "b_h": qstr(b_h),
                "omega_squared": qstr(omega2), "stable_real_root": qstr(-c2),
                "factorization": f"(lambda+{qstr(c2)})(lambda^2+{qstr(omega2)})",
                "crossing_real_derivative": qstr(derivative),
                "crossing_direction": "left_to_right_as_b_increases",
            }
            if rows[index] != expected or derivative <= 0:
                raise AssertionError(f"Hopf row {index}")
            index += 1
            checks += 11
    return checks


def check_repeated(rows: list) -> int:
    a_values = [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
    r_values = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
    if type(rows) is not list or len(rows) != 30:
        raise AssertionError("repeated-root row count")
    checks = 0
    index = 0
    for a in a_values:
        for r in r_values:
            c2, c1, c0 = a+2*r, r*(r+2*a), r*r*a
            expected = {
                "a": qstr(a), "r": qstr(r), "face": "zero_feedback", "b": "0",
                "discriminant": qstr(disc(c2, c1, c0)), "repeated_root": qstr(-r),
                "simple_root": None if a == r else qstr(-a),
                "jordan_sizes": [3] if a == r else [2, 1],
                "minimal_polynomial_degree": 3,
            }
            if rows[index] != expected or disc(c2, c1, c0) != 0:
                raise AssertionError(f"zero-feedback repeated row {index}")
            index += 1
            checks += 12
            if a < r:
                b = 4*(r-a)**3/(27*r*r)
                mu, nu = -(r+2*a)/3, -(4*r-a)/3
                c0 = r*r*(a+b)
                expected = {
                    "a": qstr(a), "r": qstr(r), "face": "positive_double_root_surface",
                    "b": qstr(b), "discriminant": qstr(disc(c2, c1, c0)),
                    "repeated_root": qstr(mu), "simple_root": qstr(nu),
                    "jordan_sizes": [2, 1], "minimal_polynomial_degree": 3,
                }
                if rows[index] != expected or disc(c2, c1, c0) != 0 or not b > 0:
                    raise AssertionError(f"positive repeated row {index}")
                index += 1
                checks += 14
    return checks


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C343 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    checks = check_payload(data)
    yaml_leaves = check_evaluation(args.evaluation, data)
    checks += check_kernels(data["kernel_rows"])
    checks += check_routh(data["routh_rows"])
    checks += check_hopf(data["hopf_rows"])
    checks += check_repeated(data["repeated_root_rows"])
    expected_enumeration = {
        "kernel_rows": 6, "routh_rows": 120, "hopf_rows": 20,
        "repeated_root_rows": 30, "audited_leaf_count": AUDITED_LEAVES,
    }
    if data["enumeration"] != expected_enumeration:
        raise AssertionError("enumeration mismatch")
    count_body = copy.deepcopy(data)
    count_body.pop("payload_sha256")
    count_body["enumeration"].pop("audited_leaf_count")
    if leaf_count(count_body) != data["enumeration"]["audited_leaf_count"]:
        raise AssertionError("audited leaf count mismatch")
    checks += data["enumeration"]["audited_leaf_count"] + yaml_leaves
    print(f"C343 independent Erlang-delay checker: PASS {checks} assertions {yaml_leaves} evaluator leaves")


if __name__ == "__main__":
    main()
