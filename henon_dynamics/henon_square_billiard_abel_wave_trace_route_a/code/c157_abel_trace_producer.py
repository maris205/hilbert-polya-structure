#!/usr/bin/env python3
"""Produce exact shell and high-precision Abel trace evidence for HCS-C157."""
from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path

import mpmath as mp


SHELL_CUTOFF = 500
PRIMAL_CUTOFF = 36
DUAL_CUTOFF = 80
SOURCE_COMMIT = "506dead810d67fa58fa7c42b2d9a09bfae161059"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canonical_hash(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def shell_ledgers():
    primitive = defaultdict(list)
    shells = defaultdict(lambda: defaultdict(int))
    for first in range(1, isqrt(SHELL_CUTOFF) + 1):
        for second in range(1, isqrt(SHELL_CUTOFF - first * first) + 1):
            squared_norm = first * first + second * second
            common = gcd(first, second)
            base = (first // common, second // common)
            primitive_squared_norm = base[0] * base[0] + base[1] * base[1]
            shells[squared_norm][(primitive_squared_norm, common)] += 1
            if common == 1:
                primitive[squared_norm].append([first, second])
    primitive_rows = []
    for squared_norm in sorted(primitive):
        directions = sorted(primitive[squared_norm])
        primitive_rows.append({
            "primitive_squared_norm": squared_norm,
            "length_symbol": f"2*sqrt({squared_norm})",
            "ordered_positive_direction_count": len(directions),
            "directions": directions,
        })
    shell_rows = []
    for squared_norm in sorted(shells):
        decompositions = []
        total = 0
        for (base_norm, repetition), multiplicity in sorted(shells[squared_norm].items()):
            assert repetition * repetition * base_norm == squared_norm
            decompositions.append({
                "primitive_squared_norm": base_norm,
                "repetition": repetition,
                "primitive_ordered_multiplicity": multiplicity,
            })
            total += multiplicity
        shell_rows.append({
            "dual_squared_norm": squared_norm,
            "ordered_positive_vector_count": total,
            "sign_lifted_dual_multiplicity": 4 * total,
            "primitive_repetition_decomposition": decompositions,
        })
    return primitive_rows, shell_rows


def beta(value):
    return (mp.zeta(value, mp.mpf(1) / 4) - mp.zeta(value, mp.mpf(3) / 4)) / (4 ** value)


def primal_sum(s, cutoff):
    return mp.fsum(mp.exp(-mp.pi * s * mp.sqrt(first * first + second * second))
                   for first in range(1, cutoff + 1)
                   for second in range(1, cutoff + 1))


def accelerated_dual_sum(s, cutoff):
    epstein_three = 4 * mp.zeta(mp.mpf(3) / 2) * beta(mp.mpf(3) / 2)
    epstein_five = 4 * mp.zeta(mp.mpf(5) / 2) * beta(mp.mpf(5) / 2)
    total = s ** -3 + epstein_three / 8 - 3 * s * s * epstein_five / 64
    remainder = mp.mpc(0)
    for first in range(-cutoff, cutoff + 1):
        for second in range(-cutoff, cutoff + 1):
            if first == second == 0:
                continue
            radius_squared = first * first + second * second
            radius = mp.sqrt(radius_squared)
            remainder += ((s * s + 4 * radius_squared) ** (-mp.mpf(3) / 2)
                          - 1 / (8 * radius ** 3)
                          + 3 * s * s / (64 * radius ** 5))
    total += remainder
    return (s / (2 * mp.pi) * total - mp.mpf(1) / 4
            - 1 / (mp.exp(mp.pi * s) - 1))


def complex_parts(value):
    return {"real": mp.nstr(mp.re(value), 35), "imag": mp.nstr(mp.im(value), 35)}


def numerical_sentinel(real, imag):
    s = mp.mpc(real, imag)
    primal = primal_sum(s, PRIMAL_CUTOFF)
    dual = accelerated_dual_sum(s, DUAL_CUTOFF)
    sigma = mp.re(s)
    geometric = mp.exp(-mp.pi * sigma / mp.sqrt(2))
    primal_error = 2 * geometric ** (PRIMAL_CUTOFF + 2) / (1 - geometric) ** 2
    dual_error = abs(s) ** 5 / (2 * mp.pi * 3 ** (mp.mpf(5) / 2) * DUAL_CUTOFF ** 5)
    difference = abs(primal - dual)
    assert difference <= primal_error + dual_error
    return {
        "s": {"real": str(real), "imag": str(imag)},
        "primal_box_cutoff": PRIMAL_CUTOFF,
        "dual_accelerated_box_cutoff": DUAL_CUTOFF,
        "primal_value": complex_parts(primal),
        "dual_value": complex_parts(dual),
        "absolute_difference": mp.nstr(difference, 20),
        "primal_tail_bound": mp.nstr(primal_error, 20),
        "dual_tail_bound": mp.nstr(dual_error, 20),
        "intervals_overlap": True,
    }


def build_evidence():
    mp.mp.dps = 55
    primitive_rows, shell_rows = shell_ledgers()
    payload = {
        "schema": "hcs-c157-square-billiard-abel-wave-trace-evidence-v1",
        "candidate_id": "HCS-C157",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "source_lock": {
            "object": "Dirichlet Laplacian on the unit square",
            "frequencies": "omega_(j,k)=pi*sqrt(j^2+k^2), j,k>=1",
            "abel_half_wave_trace": "W_D(s)=sum_(j,k>=1) exp(-pi*s*sqrt(j^2+k^2))",
            "domain": "Re(s)>0",
            "clock": "Dirichlet half-wave time, approached by s=epsilon-i*t",
            "ordered_direction_convention": "a,b>=1 with gcd(a,b)=1; coordinate swaps remain distinct",
            "shell_cutoff": SHELL_CUTOFF,
            "precision": "exact integer shell arithmetic and 55-decimal mpmath sentinels with explicit tail bounds",
            "forbidden_data": "target tables, prime tables, arithmetic local or Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "poisson_theorem": {
            "formula": "W_D(s)=s/(2*pi)*sum_(m in Z^2)(s^2+4*|m|^2)^(-3/2)-1/4-1/(exp(pi*s)-1)",
            "fourier_convention": "fhat(m)=integral_R2 f(x)*exp(-2*pi*i*m dot x) dx",
            "radial_transform": "Fourier[exp(-pi*s*|x|)](m)=2*s/(pi*(s^2+4*|m|^2)^(3/2))",
            "branch": "principal power, holomorphic because s^2+4|m|^2 avoids the nonpositive real axis for Re(s)>0",
            "absolute_convergence": "both the primal trace and the dual |m|^(-3) series converge absolutely and locally uniformly on Re(s)>0",
            "proof_route": "Poisson summation for real s>0 by Gaussian regularization, followed by half-plane analytic continuation",
        },
        "geometric_decomposition": {
            "weyl_zero_mode": "1/(2*pi*s^2)",
            "axis_dual_term": "2*s/pi*sum_(r>=1)(s^2+4*r^2)^(-3/2)",
            "boundary_subtraction": "-1/4-1/(exp(pi*s)-1)",
            "nonaxis_primitive_term": "2*s/pi*sum_(a,b>=1,gcd=1) sum_(r>=1)(s^2+r^2*L_(a,b)^2)^(-3/2)",
            "length": "L_(a,b)=2*sqrt(a^2+b^2)",
            "multiplicity_rule": "four sign lifts are already absorbed into coefficient 2*s/pi; ordered positive coordinate swaps remain separate",
            "isolated_orbit_determinant": False,
        },
        "boundary_singularity_theorem": {
            "approach": "s=epsilon-i*t with epsilon down to zero",
            "weyl_zero_mode": "m=0 contributes 1/(2*pi*s^2)",
            "nonaxis_branch_locations": "t=plus_or_minus r*L_(a,b)",
            "axis_branch_locations": "t=plus_or_minus 2*r",
            "boundary_subtraction_poles": "-1/(exp(pi*s)-1) has simple poles at s=2*i*q, equivalently t in 2*Z",
            "overlap_boundary": "axis branch locations can coincide with boundary-subtraction poles, but their singularity types differ and no cancellation is asserted",
            "singularity_type": "boundary branch singularity of power -3/2; no isolated-orbit amplitude is inferred",
            "all_repetitions_retained": True,
            "branch_locations_exhaust_all_boundary_singularities": False,
        },
        "primitive_direction_ledger": primitive_rows,
        "dual_shell_ledger": shell_rows,
        "collision_sentinel": {
            "first_fourfold_ordered_primitive_squared_norm": 65,
            "directions": [[1, 8], [4, 7], [7, 4], [8, 1]],
            "sign_lifted_multiplicity": 16,
        },
        "numerical_method": {
            "primal_tail_bound": "2*q^(J+2)/(1-q)^2 with q=exp(-pi*Re(s)/sqrt(2))",
            "dual_acceleration": "subtract 1/(8|m|^3)-3*s^2/(64|m|^5), add 4*zeta(alpha)*beta(alpha) at alpha=3/2,5/2",
            "complex_remainder_bound": "after two terms, each summand is at most 15*|s|^4/(8*3^(7/2)*|m|^7) for |m|>=M>=|s|",
            "square_shell_bound": "maxnorm shell k has 8*k points and sum_(k>M) k^(-6)<=1/(5*M^5)",
            "dual_tail_bound": "|s|^5/(2*pi*3^(5/2)*M^5), valid for M>=|s|",
            "sentinels": [numerical_sentinel(mp.mpf("0.9"), mp.mpf("0.4")),
                          numerical_sentinel(mp.mpf("1.3"), mp.mpf("0.7"))],
        },
        "formal_lift": {
            "operator": "sqrt(Delta_D) for the unit-square Dirichlet Laplacian",
            "self_adjoint": True,
            "W_D_is_abel_trace_of_exp_minus_s_sqrt_Delta": True,
            "source_derived": True,
            "target_operator_claimed": False,
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "isolated_primitive_orbit_determinant": False,
            "isolated_stability_amplitude": False,
            "target_trace_identity": False,
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] /
                        "results/c157_abel_trace_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "status": "C157_PRODUCER_PASS",
        "payload_sha256": payload["payload_sha256"],
        "primitive_shells": len(payload["primitive_direction_ledger"]),
        "dual_shells": len(payload["dual_shell_ledger"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
