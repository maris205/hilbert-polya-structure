#!/usr/bin/env python3
"""Producer-independent exact and high-precision checker for HCS-C157."""
from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path

import mpmath as mp


def canonical_payload_hash(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def independent_shells(cutoff):
    primitive_rows = []
    shell_rows = []
    for squared_norm in range(2, cutoff + 1):
        solutions = []
        for first in range(1, isqrt(squared_norm) + 1):
            remainder = squared_norm - first * first
            if remainder <= 0:
                continue
            second = isqrt(remainder)
            if second >= 1 and second * second == remainder:
                solutions.append((first, second))
        if not solutions:
            continue
        primitive = [[first, second] for first, second in solutions if gcd(first, second) == 1]
        if primitive:
            primitive_rows.append({
                "primitive_squared_norm": squared_norm,
                "length_symbol": f"2*sqrt({squared_norm})",
                "ordered_positive_direction_count": len(primitive),
                "directions": primitive,
            })
        grouped = defaultdict(int)
        for first, second in solutions:
            repetition = gcd(first, second)
            base_norm = squared_norm // (repetition * repetition)
            grouped[(base_norm, repetition)] += 1
        decompositions = [{
            "primitive_squared_norm": base_norm,
            "repetition": repetition,
            "primitive_ordered_multiplicity": multiplicity,
        } for (base_norm, repetition), multiplicity in sorted(grouped.items())]
        shell_rows.append({
            "dual_squared_norm": squared_norm,
            "ordered_positive_vector_count": len(solutions),
            "sign_lifted_dual_multiplicity": 4 * len(solutions),
            "primitive_repetition_decomposition": decompositions,
        })
    return primitive_rows, shell_rows


def dirichlet_beta(value):
    quarter = mp.mpf(1) / 4
    return (mp.zeta(value, quarter) - mp.zeta(value, 3 * quarter)) / (4 ** value)


def primal(s, cutoff):
    total = mp.mpc(0)
    for first in range(1, cutoff + 1):
        for second in range(1, cutoff + 1):
            total += mp.exp(-mp.pi * s * mp.sqrt(first * first + second * second))
    return total


def dual_accelerated(s, cutoff):
    e3 = 4 * mp.zeta(mp.mpf(3) / 2) * dirichlet_beta(mp.mpf(3) / 2)
    e5 = 4 * mp.zeta(mp.mpf(5) / 2) * dirichlet_beta(mp.mpf(5) / 2)
    total = s ** -3 + e3 / 8 - 3 * s * s * e5 / 64
    for first in range(-cutoff, cutoff + 1):
        for second in range(-cutoff, cutoff + 1):
            radius_squared = first * first + second * second
            if not radius_squared:
                continue
            radius = mp.sqrt(radius_squared)
            total += ((s * s + 4 * radius_squared) ** (-mp.mpf(3) / 2)
                      - 1 / (8 * radius ** 3) + 3 * s * s / (64 * radius ** 5))
    return s / (2 * mp.pi) * total - mp.mpf(1) / 4 - 1 / (mp.exp(mp.pi * s) - 1)


def parse_complex(parts):
    return mp.mpc(parts["real"], parts["imag"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1] /
                        "results/c157_abel_trace_evidence.json")
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    mp.mp.dps = 55
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    expected_top = {
        "schema", "candidate_id", "evaluation_date", "scope_literal", "source_commit",
        "source_lock", "poisson_theorem", "geometric_decomposition",
        "boundary_singularity_theorem", "primitive_direction_ledger", "dual_shell_ledger",
        "collision_sentinel", "numerical_method", "formal_lift", "route_a",
        "claim_boundary", "payload_sha256",
    }
    check(set(data) == expected_top, "top-level closure")
    check(data["schema"] == "hcs-c157-square-billiard-abel-wave-trace-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C157", "candidate")
    check(data["evaluation_date"] == "2026-08-25", "date")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["source_commit"] == "506dead810d67fa58fa7c42b2d9a09bfae161059", "commit")
    check(data["payload_sha256"] == canonical_payload_hash(data), "payload hash")
    lock = data["source_lock"]
    check(set(lock) == {
        "object", "frequencies", "abel_half_wave_trace", "clock", "domain",
        "ordered_direction_convention", "shell_cutoff", "precision", "forbidden_data",
    }, "source-lock closure")
    check(lock["object"] == "Dirichlet Laplacian on the unit square", "object")
    check(lock["frequencies"] == "omega_(j,k)=pi*sqrt(j^2+k^2), j,k>=1", "frequencies")
    check(lock["abel_half_wave_trace"] ==
          "W_D(s)=sum_(j,k>=1) exp(-pi*s*sqrt(j^2+k^2))", "trace definition")
    check(lock["clock"] == "Dirichlet half-wave time, approached by s=epsilon-i*t", "clock")
    check(lock["domain"] == "Re(s)>0", "domain")
    check(lock["ordered_direction_convention"] ==
          "a,b>=1 with gcd(a,b)=1; coordinate swaps remain distinct",
          "direction convention")
    check(lock["shell_cutoff"] == 500, "shell cutoff")
    check(lock["precision"] ==
          "exact integer shell arithmetic and 55-decimal mpmath sentinels with explicit tail bounds",
          "precision")
    check(lock["forbidden_data"] ==
          "target tables, prime tables, arithmetic local or Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
          "forbidden data")

    poisson = data["poisson_theorem"]
    check(set(poisson) == {
        "formula", "radial_transform", "fourier_convention", "branch",
        "absolute_convergence", "proof_route",
    }, "Poisson-theorem closure")
    check(poisson["formula"] ==
          "W_D(s)=s/(2*pi)*sum_(m in Z^2)(s^2+4*|m|^2)^(-3/2)-1/4-1/(exp(pi*s)-1)",
          "Poisson formula")
    check(poisson["radial_transform"] ==
          "Fourier[exp(-pi*s*|x|)](m)=2*s/(pi*(s^2+4*|m|^2)^(3/2))",
          "Fourier constant")
    check(poisson["fourier_convention"] ==
          "fhat(m)=integral_R2 f(x)*exp(-2*pi*i*m dot x) dx",
          "Fourier convention")
    check(poisson["branch"] ==
          "principal power, holomorphic because s^2+4|m|^2 avoids the nonpositive real axis for Re(s)>0",
          "branch")
    check(poisson["absolute_convergence"] ==
          "both the primal trace and the dual |m|^(-3) series converge absolutely and locally uniformly on Re(s)>0",
          "convergence")
    check(poisson["proof_route"] ==
          "Poisson summation for real s>0 by Gaussian regularization, followed by half-plane analytic continuation",
          "proof route")

    geometry = data["geometric_decomposition"]
    check(set(geometry) == {
        "weyl_zero_mode", "axis_dual_term", "boundary_subtraction",
        "nonaxis_primitive_term", "length", "multiplicity_rule",
        "isolated_orbit_determinant",
    }, "geometric-decomposition closure")
    check(geometry["weyl_zero_mode"] == "1/(2*pi*s^2)", "Weyl mode")
    check(geometry["axis_dual_term"] == "2*s/pi*sum_(r>=1)(s^2+4*r^2)^(-3/2)", "axis")
    check(geometry["boundary_subtraction"] == "-1/4-1/(exp(pi*s)-1)", "boundary subtraction")
    check(geometry["nonaxis_primitive_term"] ==
          "2*s/pi*sum_(a,b>=1,gcd=1) sum_(r>=1)(s^2+r^2*L_(a,b)^2)^(-3/2)",
          "nonaxis coefficient")
    check(geometry["length"] == "L_(a,b)=2*sqrt(a^2+b^2)", "length")
    check(geometry["multiplicity_rule"] ==
          "four sign lifts are already absorbed into coefficient 2*s/pi; ordered positive coordinate swaps remain separate",
          "multiplicity rule")
    check(geometry["isolated_orbit_determinant"] is False, "no determinant")

    singularity = data["boundary_singularity_theorem"]
    check(set(singularity) == {
        "approach", "weyl_zero_mode", "nonaxis_branch_locations",
        "axis_branch_locations", "boundary_subtraction_poles", "overlap_boundary",
        "singularity_type", "all_repetitions_retained",
        "branch_locations_exhaust_all_boundary_singularities",
    }, "boundary-singularity closure")
    check(singularity["approach"] == "s=epsilon-i*t with epsilon down to zero", "boundary approach")
    check(singularity["weyl_zero_mode"] == "m=0 contributes 1/(2*pi*s^2)", "singularity Weyl mode")
    check(singularity["nonaxis_branch_locations"] == "t=plus_or_minus r*L_(a,b)", "branch locations")
    check(singularity["axis_branch_locations"] == "t=plus_or_minus 2*r", "axis branches")
    check(singularity["boundary_subtraction_poles"] ==
          "-1/(exp(pi*s)-1) has simple poles at s=2*i*q, equivalently t in 2*Z",
          "boundary poles")
    check(singularity["overlap_boundary"] ==
          "axis branch locations can coincide with boundary-subtraction poles, but their singularity types differ and no cancellation is asserted",
          "noncancellation boundary")
    check(singularity["singularity_type"] ==
          "boundary branch singularity of power -3/2; no isolated-orbit amplitude is inferred",
          "branch singularity type")
    check(singularity["all_repetitions_retained"] is True, "repetitions")
    check(singularity["branch_locations_exhaust_all_boundary_singularities"] is False,
          "nonexhaustive branch list")

    primitive, shells = independent_shells(500)
    check(len(primitive) == len(data["primitive_direction_ledger"]), "primitive row count")
    check(len(shells) == len(data["dual_shell_ledger"]), "shell row count")
    for expected, frozen in zip(primitive, data["primitive_direction_ledger"]):
        check(frozen == expected, f"primitive shell {expected['primitive_squared_norm']}")
        for direction in expected["directions"]:
            check(gcd(direction[0], direction[1]) == 1, f"primitive direction {direction}")
            check(direction[0] ** 2 + direction[1] ** 2 == expected["primitive_squared_norm"],
                  f"direction norm {direction}")
    for expected, frozen in zip(shells, data["dual_shell_ledger"]):
        check(frozen == expected, f"dual shell {expected['dual_squared_norm']}")
        for decomposition in expected["primitive_repetition_decomposition"]:
            check(decomposition["repetition"] ** 2 * decomposition["primitive_squared_norm"] ==
                  expected["dual_squared_norm"], f"repetition decomposition {expected['dual_squared_norm']}")
    collision = data["collision_sentinel"]
    check(collision == {
        "first_fourfold_ordered_primitive_squared_norm": 65,
        "directions": [[1, 8], [4, 7], [7, 4], [8, 1]],
        "sign_lifted_multiplicity": 16,
    }, "collision sentinel")
    check(all(row["ordered_positive_direction_count"] < 4
              for row in primitive if row["primitive_squared_norm"] < 65), "first fourfold")

    numerical = data["numerical_method"]
    check(set(numerical) == {
        "primal_tail_bound", "dual_acceleration", "complex_remainder_bound",
        "square_shell_bound", "dual_tail_bound", "sentinels",
    }, "numerical-method closure")
    check(numerical["primal_tail_bound"] ==
          "2*q^(J+2)/(1-q)^2 with q=exp(-pi*Re(s)/sqrt(2))", "primal bound")
    check(numerical["dual_acceleration"] ==
          "subtract 1/(8|m|^3)-3*s^2/(64|m|^5), add 4*zeta(alpha)*beta(alpha) at alpha=3/2,5/2",
          "dual acceleration")
    check(numerical["complex_remainder_bound"] ==
          "after two terms, each summand is at most 15*|s|^4/(8*3^(7/2)*|m|^7) for |m|>=M>=|s|",
          "complex remainder bound")
    check(numerical["square_shell_bound"] ==
          "maxnorm shell k has 8*k points and sum_(k>M) k^(-6)<=1/(5*M^5)",
          "square shell bound")
    check(numerical["dual_tail_bound"] ==
          "|s|^5/(2*pi*3^(5/2)*M^5), valid for M>=|s|", "dual bound")
    # The exact shell count and constants close the claimed dual error bound.
    for shell_radius in range(1, 31):
        shell = [(first, second)
                 for first in range(-shell_radius, shell_radius+1)
                 for second in range(-shell_radius, shell_radius+1)
                 if max(abs(first), abs(second)) == shell_radius]
        check(len(shell) == 8*shell_radius, f"maxnorm shell cardinality {shell_radius}")
    check(mp.almosteq((mp.mpf(15)/8)*8*(mp.mpf(1)/5)/3**(mp.mpf(7)/2),
                      1/3**(mp.mpf(5)/2)), "dual tail constant")
    expected_sentinels = [
        {
            "s": {"real": "0.9", "imag": "0.4"},
            "primal_box_cutoff": 36,
            "dual_accelerated_box_cutoff": 80,
            "primal_value": {
                "real": "-0.0076321437064629039954521260991522977",
                "imag": "-0.01869596658965606501888184449819036",
            },
            "dual_value": {
                "real": "-0.0076321437062053476877197554878503766",
                "imag": "-0.018695966590105578539036774426575851",
            },
            "absolute_difference": "5.1807109208564048627e-13",
            "primal_tail_bound": "2.7079827227518389643e-33",
            "dual_tail_bound": "2.8873298155339220507e-12",
            "intervals_overlap": True,
        },
        {
            "s": {"real": "1.3", "imag": "0.7"},
            "primal_box_cutoff": 36,
            "dual_accelerated_box_cutoff": 80,
            "primal_value": {
                "real": "-0.0030430596230243189797276191751722059",
                "imag": "0.00011051189152135618023330834402775077",
            },
            "dual_value": {
                "real": "-0.003043059619954280536663123210181077",
                "imag": "0.00011051188907940928223731322898590267",
            },
            "absolute_difference": "3.9227848136911789319e-12",
            "primal_tail_bound": "4.9166831806549027987e-48",
            "dual_tail_bound": "2.1862926457085843577e-11",
            "intervals_overlap": True,
        },
    ]
    check(numerical["sentinels"] == expected_sentinels,
          "frozen sentinel sequence and values")
    check(len(numerical["sentinels"]) == 2, "sentinel count")
    for sentinel in numerical["sentinels"]:
        check(set(sentinel) == {
            "s", "primal_box_cutoff", "dual_accelerated_box_cutoff",
            "primal_value", "dual_value", "absolute_difference",
            "primal_tail_bound", "dual_tail_bound", "intervals_overlap",
        }, "sentinel closure")
        check(set(sentinel["s"]) == {"real", "imag"}, "sentinel-s closure")
        check(set(sentinel["primal_value"]) == {"real", "imag"},
              "primal-complex closure")
        check(set(sentinel["dual_value"]) == {"real", "imag"},
              "dual-complex closure")
        check(sentinel["primal_box_cutoff"] == 36, "primal cutoff")
        check(sentinel["dual_accelerated_box_cutoff"] == 80, "dual cutoff")
        check(sentinel["intervals_overlap"] is True, "overlap receipt")
        frozen_primal = parse_complex(sentinel["primal_value"])
        frozen_dual = parse_complex(sentinel["dual_value"])
        frozen_primal_error = mp.mpf(sentinel["primal_tail_bound"])
        frozen_dual_error = mp.mpf(sentinel["dual_tail_bound"])
        frozen_s = mp.mpc(sentinel["s"]["real"], sentinel["s"]["imag"])
        expected_dual_error = (abs(frozen_s)**5 /
                               (2*mp.pi*3**(mp.mpf(5)/2)*80**5))
        check(sentinel["dual_tail_bound"] == mp.nstr(expected_dual_error, 20),
              "frozen dual bound formula and 20-digit serialization")
        check(abs(frozen_primal - frozen_dual) <= frozen_primal_error + frozen_dual_error,
              "frozen analytic-tail-envelope overlap")
        if not args.quick:
            mp.mp.dps = 55
            s = frozen_s
            independent_primal = primal(s, 38)
            independent_dual = dual_accelerated(s, 90)
            q = mp.exp(-mp.pi * mp.re(s) / mp.sqrt(2))
            new_primal_error = 2 * q ** 40 / (1 - q) ** 2
            new_dual_error = abs(s) ** 5 / (2 * mp.pi * 3 ** (mp.mpf(5) / 2) * 90 ** 5)
            serialization_rounding = mp.mpf("1e-34")
            check(abs(frozen_primal - independent_primal) <=
                  frozen_primal_error + new_primal_error + serialization_rounding,
                  "independent primal")
            check(abs(frozen_dual - independent_dual) <=
                  frozen_dual_error + new_dual_error + serialization_rounding,
                  "independent dual")
            check(abs(independent_primal - independent_dual) <=
                  new_primal_error + new_dual_error, "independent tail-envelope overlap")

    formal_lift = data["formal_lift"]
    check(set(formal_lift) == {
        "operator", "self_adjoint", "W_D_is_abel_trace_of_exp_minus_s_sqrt_Delta",
        "source_derived", "target_operator_claimed",
    }, "formal-lift closure")
    check(formal_lift == {
        "operator": "sqrt(Delta_D) for the unit-square Dirichlet Laplacian",
        "self_adjoint": True,
        "W_D_is_abel_trace_of_exp_minus_s_sqrt_Delta": True,
        "source_derived": True,
        "target_operator_claimed": False,
    }, "natural quantization")
    route_a = data["route_a"]
    check(set(route_a) == {"tuple", "overall", "route_b_invocation_allowed"},
          "Route-A closure")
    check(route_a == {
        "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
        "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False,
    }, "Route A tuple")
    claim_boundary = data["claim_boundary"]
    expected_claim_boundary = {
        "arithmetic_local_data": False,
        "automorphy": False,
        "euler_factors": False,
        "hilbert_polya_operator": False,
        "isolated_primitive_orbit_determinant": False,
        "isolated_stability_amplitude": False,
        "root_numbers": False,
        "target_counting_law": False,
        "target_divisor_matching": False,
        "target_functional_equation": False,
        "target_trace_identity": False,
    }
    check(set(claim_boundary) == set(expected_claim_boundary), "claim-boundary closure")
    check(claim_boundary == expected_claim_boundary, "claim boundary exact values")
    print(json.dumps({
        "status": "C157_CHECKER_PASS", "mode": "quick" if args.quick else "full",
        "assertions": checks,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
