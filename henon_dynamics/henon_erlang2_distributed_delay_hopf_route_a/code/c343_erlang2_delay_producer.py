#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C343."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c343_erlang2_delay_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C343/2026-09-03.yaml"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "7c148a98c804c66d57ed14946fb3e59b945098fe259a55ade3c9054002ab9033"
EVAL_SEMANTIC = "4f804ecbfce827f03931d97aae994fb8a346fd5e9ba064eb3b31f4c6e2067c08"
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


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def semantic_yaml_hash(raw: bytes) -> str:
    value = yaml.safe_load(raw)
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha(canonical)


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(child) for child in value.values())
    if type(value) is list:
        return sum(leaves(child) for child in value)
    return 1


def discriminant(c2: Fraction, c1: Fraction, c0: Fraction) -> Fraction:
    return c2*c2*c1*c1 - 4*c1**3 - 4*c2**3*c0 - 27*c0*c0 + 18*c2*c1*c0


A_VALUES = [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
R_VALUES = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]


def kernel_rows() -> list[dict]:
    rows = []
    for r in [Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5)]:
        rows.append({
            "r": qstr(r),
            "mass": "1",
            "mean": qstr(2/r),
            "second_moment": qstr(6/r**2),
            "variance": qstr(2/r**2),
            "laplace_transform": f"{qstr(r**2)}/(lambda+{qstr(r)})^2",
            "chain_identity": "z1'=r(x-z1); z2'=r(z1-z2)",
        })
    return rows


def routh_rows() -> list[dict]:
    rows = []
    faces = [
        ("zero_feedback", Fraction(0)),
        ("quarter_threshold", Fraction(1, 4)),
        ("below_threshold", Fraction(3, 4)),
        ("hopf_threshold", Fraction(1)),
        ("above_threshold", Fraction(5, 4)),
        ("double_threshold", Fraction(2)),
    ]
    for a in A_VALUES:
        for r in R_VALUES:
            b_h = 2*(a+r)**2/r
            for face, ratio in faces:
                b = ratio*b_h
                c2 = a+2*r
                c1 = r*(r+2*a)
                c0 = r*r*(a+b)
                margin = c2*c1-c0
                if b == 0:
                    classification = "marginal_constant" if a == 0 else "stable_jordan"
                    rhp_roots = 0
                elif b < b_h:
                    classification = "exponentially_stable"
                    rhp_roots = 0
                elif b == b_h:
                    classification = "simple_imaginary_pair"
                    rhp_roots = 0
                else:
                    classification = "two_rhp_roots"
                    rhp_roots = 2
                rows.append({
                    "a": qstr(a), "r": qstr(r), "face": face,
                    "b_over_b_h": qstr(ratio), "b": qstr(b), "b_h": qstr(b_h),
                    "coefficients_c2_c1_c0": [qstr(c2), qstr(c1), qstr(c0)],
                    "routh_margin": qstr(margin),
                    "classification": classification, "rhp_root_count": rhp_roots,
                })
    return rows


def hopf_rows() -> list[dict]:
    rows = []
    for a in A_VALUES:
        for r in R_VALUES:
            c2 = a+2*r
            omega2 = r*(r+2*a)
            b_h = 2*(a+r)**2/r
            derivative_real = r*r/(2*(omega2+c2*c2))
            rows.append({
                "a": qstr(a), "r": qstr(r), "b_h": qstr(b_h),
                "omega_squared": qstr(omega2), "stable_real_root": qstr(-c2),
                "factorization": f"(lambda+{qstr(c2)})(lambda^2+{qstr(omega2)})",
                "crossing_real_derivative": qstr(derivative_real),
                "crossing_direction": "left_to_right_as_b_increases",
            })
    return rows


def repeated_rows() -> list[dict]:
    rows = []
    for a in A_VALUES:
        for r in R_VALUES:
            c2, c1, c0 = a+2*r, r*(r+2*a), r*r*a
            rows.append({
                "a": qstr(a), "r": qstr(r), "face": "zero_feedback",
                "b": "0", "discriminant": qstr(discriminant(c2, c1, c0)),
                "repeated_root": qstr(-r),
                "simple_root": None if a == r else qstr(-a),
                "jordan_sizes": [3] if a == r else [2, 1],
                "minimal_polynomial_degree": 3,
            })
            if a < r:
                b = 4*(r-a)**3/(27*r*r)
                mu = -(r+2*a)/3
                nu = -(4*r-a)/3
                c0 = r*r*(a+b)
                rows.append({
                    "a": qstr(a), "r": qstr(r), "face": "positive_double_root_surface",
                    "b": qstr(b), "discriminant": qstr(discriminant(c2, c1, c0)),
                    "repeated_root": qstr(mu), "simple_root": qstr(nu),
                    "jordan_sizes": [2, 1], "minimal_polynomial_degree": 3,
                })
    return rows


def make_data() -> dict:
    evaluation_raw = EVALUATION.read_bytes()
    if sha(evaluation_raw) != EVAL_RAW or semantic_yaml_hash(evaluation_raw) != EVAL_SEMANTIC:
        raise AssertionError("evaluation lock mismatch")
    kernels = kernel_rows()
    routh = routh_rows()
    hopf = hopf_rows()
    repeated = repeated_rows()
    data = {
        "schema": "hcs-c343-erlang2-delay-v1",
        "candidate_id": "HCS-C343",
        "obstruction_id": "HEN-O327",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR,
        },
        "evaluation": {
            "path": "evaluations/route_a/HCS-C343/2026-09-03.yaml",
            "raw_sha256": EVAL_RAW,
            "semantic_sha256": EVAL_SEMANTIC,
        },
        "model": {
            "equation": "x'(t)=-a*x(t)-b*integral_0^infinity r^2*s*exp(-r*s)*x(t-s) ds",
            "domain": "a>=0, b>=0, r>0 with compatible fading-memory histories",
            "kernel": "K_r(s)=r^2*s*exp(-r*s) for s>=0",
            "chain": "x'=-a*x-b*z2; z1'=r*(x-z1); z2'=r*(z1-z2)",
            "generator": "[[-a,0,-b],[r,-r,0],[0,r,-r]]",
            "characteristic": "(lambda+a)*(lambda+r)^2+b*r^2",
        },
        "theorem_contract": {
            "linear_chain": "the distributed-delay equation equals the three-state chain for compatible histories",
            "stability": "for b>0 exponential stability holds iff b<2*(a+r)^2/r",
            "hopf": "at equality the roots are -(a+2r) and plus/minus i*sqrt(r*(r+2a)), with positive crossing speed",
            "unstable_count": "for b above threshold the cubic has exactly two open-right-half-plane roots",
            "repeated_roots": "b=0 gives the -r Jordan boundary; a<r also gives one positive-feedback double-root surface",
            "nonlinear_boundary": "a simple imaginary crossing is proved; no nonlinear periodic-orbit existence is claimed",
        },
        "references": [
            {"identifier": "10.1007/s00285-019-01412-w", "role": "official linear-chain-trick source"},
            {"identifier": "10.1016/0022-247X(89)90081-4", "role": "primary gamma-delay stability source"},
            {"identifier": "10.1007/978-3-642-93107-9", "role": "source monograph on distributed lags"},
        ],
        "collision_boundary": {
            "C210": "a scalar discrete retarded delay with an infinite Lambert-W root ladder, not a distributed Erlang memory",
            "C218": "a Kelvin-Voigt damped wave PDE, not a finite Markov realization of distributed delay",
            "C272": "an Erlang age-transport renewal PDE, not a scalar negative-feedback delay and Hopf/Jordan atlas",
        },
        "nonclaims": [
            "No nonlinear limit cycle, Hopf periodic branch, or global nonlinear bifurcation is claimed.",
            "No priority claim is made for the linear-chain trick, gamma-delay stability, or Routh-Hurwitz theory.",
            "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route-B input is claimed.",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "parameter_grid": {
            "a_values": [qstr(value) for value in A_VALUES],
            "r_values": [qstr(value) for value in R_VALUES],
            "routh_faces": ["0", "b_h/4", "3*b_h/4", "b_h", "5*b_h/4", "2*b_h"],
            "evidence_role": "exact finite receipt, not proof by sampling",
        },
        "kernel_rows": kernels,
        "routh_rows": routh,
        "hopf_rows": hopf,
        "repeated_root_rows": repeated,
        "boundary_rows": {
            "a_zero_b_positive": "stable for 0<b<2r, simple imaginary pair at b=2r, two RHP roots for b>2r",
            "a_zero_b_zero": "one constant x mode and one size-two Jordan block at -r",
            "b_zero_a_positive": "exponentially stable despite a size-two Jordan block at -r",
            "a_equals_r_b_zero": "one size-three Jordan block at -r",
            "r_zero": "excluded because the displayed Erlang density ceases to be a normalized kernel",
            "large_r": "the memory transfer r^2/(lambda+r)^2 tends to one; the reduced slow rate tends to -(a+b)",
            "history_compatibility": "arbitrary chain states are not asserted to encode a prescribed prehistory; initial z1,z2 are the two kernel integrals",
        },
        "enumeration": {
            "kernel_rows": len(kernels),
            "routh_rows": len(routh),
            "hopf_rows": len(hopf),
            "repeated_root_rows": len(repeated),
        },
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data)
    data["payload_sha256"] = sha(json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    return data


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C343 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    raw = json.dumps(make_data(), sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(raw)
    print(f"C343_PRODUCER_PASS {sha(raw.encode())}")


if __name__ == "__main__":
    main()
