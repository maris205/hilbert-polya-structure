#!/usr/bin/env python3
"""Produce the deterministic HCS-C228 product-kernel gelation certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import math
import os
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "489672bd36abd3a4f6da92d1446a0af575917959"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c228_coagulation_evidence.json"
mp.mp.dps = 90

PRE_TIMES = [Fraction(0), Fraction(1, 10), Fraction(1, 2), Fraction(9, 10), Fraction(1)]
POST_TIMES = [Fraction(6, 5), Fraction(2), Fraction(5), Fraction(10)]
SERIALIZED_K = 20
COEFFICIENT_K = 40
TAIL_K = [20, 50, 100, 200, 500]


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def dec(value: mp.mpf, digits: int = 64) -> str:
    if abs(value) < mp.mpf("1e-82"):
        return "0.0"
    return mp.nstr(value, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def a(k: int) -> Fraction:
    if k == 1:
        return Fraction(1)
    return Fraction(k ** (k - 2), math.factorial(k))


def amp_a(k: int) -> mp.mpf:
    value = a(k)
    return mp.mpf(value.numerator) / value.denominator


def pre_or_flory_c(k: int, t: mp.mpf) -> mp.mpf:
    if t == 0:
        return mp.mpf(1) if k == 1 else mp.mpf(0)
    return amp_a(k) * t ** (k - 1) * mp.exp(-k * t)


def smol_c(k: int, t: mp.mpf) -> mp.mpf:
    return amp_a(k) * mp.exp(-k) / t


def flory_q(t: mp.mpf) -> mp.mpf:
    if t <= 1:
        return mp.mpf(1)
    rooted = -mp.lambertw(-t * mp.exp(-t), 0)
    return mp.re(rooted) / t


def residual_max(t: mp.mpf, branch: str, mass: mp.mpf) -> mp.mpf:
    worst = mp.mpf(0)
    for k in range(1, SERIALIZED_K + 1):
        if branch == "smoluchowski_postgel":
            ck = smol_c(k, t)
            derivative = -ck / t
            getter = smol_c
        else:
            ck = pre_or_flory_c(k, t)
            derivative = ck * ((k - 1) / t - k) if t else (mp.mpf(-1) if k == 1 else (mp.mpf(1) / 2 if k == 2 else mp.mpf(0)))
            getter = pre_or_flory_c
        gain = mp.fsum(mp.mpf(i * (k - i)) * getter(i, t) * getter(k - i, t) for i in range(1, k)) / 2
        loss_mass = mp.mpf(1) if branch == "flory_postgel" else mass
        rhs = gain - k * ck * loss_mass
        worst = max(worst, abs(derivative - rhs))
    return worst


def coefficient_rows() -> list[dict]:
    rows = []
    for k in range(1, COEFFICIENT_K + 1):
        ak = a(k)
        if k == 1:
            recurrence_rhs = Fraction(0)
            recurrence_lhs = Fraction(0)
        else:
            recurrence_rhs = sum((Fraction(i * (k - i), 2) * a(i) * a(k - i) for i in range(1, k)), Fraction(0))
            recurrence_lhs = (k - 1) * ak
        rows.append({
            "k": k,
            "a_k": ftext(ak),
            "recurrence_lhs": ftext(recurrence_lhs),
            "recurrence_rhs": ftext(recurrence_rhs),
        })
    return rows


def pre_row(tq: Fraction) -> dict:
    t = mpq(tq)
    if t < 1:
        moment2 = dec(1 / (1 - t))
        moment3 = dec(1 / (1 - t) ** 3)
        regime = "initial" if t == 0 else "pregel"
    else:
        moment2 = "infinity"
        moment3 = "infinity"
        regime = "critical"
    return {
        "time": ftext(tq),
        "regime": regime,
        "number_density_M0": dec(1 - t / 2),
        "sol_mass_M1": "1.000000000000000000000000000000000000000000000000000000000000000",
        "second_moment_M2": moment2,
        "third_moment_M3": moment3,
        "coefficients_k1_to_20": [dec(pre_or_flory_c(k, t)) for k in range(1, SERIALIZED_K + 1)],
        "ode_residual_max_k20": dec(residual_max(t, "pregel", mp.mpf(1))) if t > 0 else "boundary_t0_exact",
    }


def smol_row(tq: Fraction) -> dict:
    t = mpq(tq)
    mass = 1 / t
    return {
        "time": ftext(tq),
        "branch": "Smoluchowski_Stockmayer",
        "number_density_M0": dec(1 / (2 * t)),
        "sol_mass_M1": dec(mass),
        "gel_fraction": dec(1 - mass),
        "second_moment_M2": "infinity",
        "coefficients_k1_to_20": [dec(smol_c(k, t)) for k in range(1, SERIALIZED_K + 1)],
        "ode_residual_max_k20": dec(residual_max(t, "smoluchowski_postgel", mass)),
        "loss_mass_used": dec(mass),
    }


def flory_row(tq: Fraction) -> dict:
    t = mpq(tq)
    q = flory_q(t)
    rooted = t * q
    return {
        "time": ftext(tq),
        "branch": "Flory_gel_reactive",
        "small_root_r": dec(rooted),
        "sol_mass_q": dec(q),
        "fixed_point_residual": dec(q - mp.exp(-t * (1 - q))),
        "number_density_M0": dec(q - t * q * q / 2),
        "gel_fraction": dec(1 - q),
        "second_moment_M2": dec(q / (1 - rooted)),
        "third_moment_M3": dec(q / (1 - rooted) ** 3),
        "coefficients_k1_to_20": [dec(pre_or_flory_c(k, t)) for k in range(1, SERIALIZED_K + 1)],
        "modified_ode_residual_max_k20": dec(residual_max(t, "flory_postgel", q)),
        "loss_mass_used": "1.000000000000000000000000000000000000000000000000000000000000000",
    }


def build() -> dict:
    critical_rows = []
    for k in TAIL_K:
        ck = amp_a(k) * mp.exp(-k)
        scaled = mp.sqrt(2 * mp.pi) * k ** (mp.mpf(5) / 2) * ck
        critical_rows.append({"k": k, "c_k_at_t1": dec(ck), "scaled_tail_ratio": dec(scaled)})
    data = {
        "schema": "hcs-c228-product-kernel-gelation-v1",
        "candidate_id": "HCS-C228",
        "evaluation_date": "2026-08-29",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The monodisperse product-kernel coagulation equation has an exact tree-function pregel law, a k^-5/2 gel point, and two rigorously separated postgel closures: Smoluchowski/Stockmayer and gel-reactive Flory.",
        "frozen_object": {
            "smoluchowski_equation": "c_k'=1/2 sum_{i+j=k} i j c_i c_j-k c_k M1(t), M1=sum_j j c_j",
            "flory_equation": "same gain but postgel loss -k c_k M1(0), so finite clusters continue to react with gel",
            "kernel": "K(i,j)=i j",
            "initial_data": "c_1(0)=1 and c_k(0)=0 for k>1",
            "normalization": "unordered gain carries 1/2; gel time is t_g=1",
            "clock": "coagulation time t>=0",
            "tree_functions": "T(u)=sum k^(k-1)u^k/k!, T=u exp(T); U=T-T^2/2",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert-Polya operators",
        },
        "theorem": {
            "pregel_coefficients": "for 0<t<=1, c_k=k^(k-2)t^(k-1)e^(-kt)/k!; at t=0 the continuous convention is c_1=1 and c_k=0 for k>1",
            "pregel_generating_functions": "as formal power series in z, G=sum k c_k z^k=T(t z e^-t)/t and C=sum c_k z^k=U(t z e^-t)/t; analytically these hold on the principal convergence disk, including 0<=z<=1, with continuous t=0 limits",
            "pregel_moments": "M0=1-t/2, M1=1, M2=(1-t)^-1, M3=(1-t)^-3 for t<1",
            "gel_point": "t_g=1 and c_k(1)~(2 pi)^(-1/2) k^(-5/2), hence M2 diverges",
            "subcritical_tail": "c_k(t)~[1/(sqrt(2 pi)t)] k^(-5/2)[t exp(1-t)]^k for 0<t<1",
            "smoluchowski_postgel": "one explicit Stockmayer continuation is c_k=k^(k-2)e^(-k)/(k! t), t>=1; it solves loss mass M1=1/t and has M0=1/(2t), M1=1/t, M2=infinity",
            "flory_postgel": "the gel-reactive continuation is c_k=k^(k-2)t^(k-1)e^(-kt)/k!, with q=M1 in (0,1) solving q=exp[-t(1-q)] and modified loss mass M1(0)=1",
            "flory_moments": "if r=tq=-W_0(-t e^-t), then M0=q-tq^2/2, M2=q/(1-r), M3=q/(1-r)^3",
            "closure_boundary": "the two postgel formulas coincide at t=1 but solve different loss terms for t>1; neither is substituted for the other",
            "uniqueness_scope": "the released algebra verifies the displayed continuations; it does not claim uniqueness among every weak postgel solution",
        },
        "coefficient_ledger": {"rows": coefficient_rows(), "row_count": COEFFICIENT_K},
        "regression": {
            "pregel_and_critical_rows": [pre_row(t) for t in PRE_TIMES],
            "smoluchowski_postgel_rows": [smol_row(t) for t in POST_TIMES],
            "flory_postgel_rows": [flory_row(t) for t in POST_TIMES],
            "critical_tail_rows": critical_rows,
            "serialized_cluster_cutoff": SERIALIZED_K,
            "working_decimal_digits": 90,
            "serialized_significant_digits": 64,
        },
        "exact_identities": [
            {"name": "Cayley_recurrence", "formula": "(k-1)a_k=1/2 sum_{i+j=k}ij a_i a_j, a_k=k^(k-2)/k!"},
            {"name": "tree_equation", "formula": "T=u exp(T)"},
            {"name": "unrooted_tree", "formula": "U=T-T^2/2 and u U'(u)=T"},
            {"name": "moment_ODE", "formula": "M2'=M2^2 and M3'=3 M2 M3 while M1=1"},
            {"name": "critical_tail", "formula": "Stirling gives a_k e^-k~(2pi)^-1/2 k^-5/2"},
            {"name": "Stockmayer_balance", "formula": "gain=(k-1)c_k/t and loss=k c_k/t, hence c_k'=-c_k/t"},
            {"name": "Flory_balance", "formula": "gain=(k-1)c_k/t and gel-reactive loss=k c_k, matching c_k'=((k-1)/t-k)c_k"},
            {"name": "branch_separation", "formula": "for t>1, 1/t differs from q=-W0(-t e^-t)/t and the loss masses differ"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "an exact infinite-dimensional nonlinear coefficient law with gelation and a sharp postgel model boundary",
            "strongest_failure": "cluster size is not an arithmetic primitive owner and the tree generating functions are not a target determinant or analytic target",
        },
        "scope_flags": {
            "uses_target_zero_table": False, "uses_prime_table": False,
            "claims_arithmetic_local_data": False, "claims_euler_factors": False,
            "claims_root_numbers": False, "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False,
            "claims_hilbert_polya_operator": False, "invokes_route_b": False,
        },
        "citations": [
            {"id": "McLeod1962I", "doi": "10.1093/qmath/13.1.119", "role": "classical infinite coagulation equations and exact-solution context"},
            {"id": "McLeod1962II", "doi": "10.1093/qmath/13.1.193", "role": "continuation of the classical analysis"},
            {"id": "ZiffStell1980", "doi": "10.1063/1.440502", "role": "kinetics of polymer gelation and postgel conventions"},
            {"id": "NormandZambotti2011", "doi": "10.1016/j.anihpc.2010.10.005", "role": "global Smoluchowski and Flory solution theory"},
            {"id": "Norris1999", "doi": "10.1214/aoap/1029962598", "role": "uniqueness, nonuniqueness and hydrodynamic-limit boundary"},
        ],
        "nonclaims": [
            "The classical tree coefficients and gelation law are not claimed as new discoveries.",
            "The pregel coefficient formula is not silently continued as a solution of the postgel Smoluchowski loss term.",
            "The explicit Stockmayer continuation is not promoted to uniqueness among all weak postgel solutions.",
            "Finite coefficient regression is not used as a proof of the infinite tail or gel point.",
            "No target arithmetic, Euler product, target functional equation, Hilbert-Polya operator, or Route-B input is claimed.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    tmp = args.output.with_name(args.output.name + ".tmp")
    tmp.write_text(raw)
    os.replace(tmp, args.output)
    print(json.dumps({"status": "C228_PRODUCER_PASS", "coefficient_rows": COEFFICIENT_K,
                      "branch_rows": len(PRE_TIMES) + 2 * len(POST_TIMES),
                      "payload_sha256": data["payload_sha256"],
                      "evidence_sha256": sha256(raw.encode()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
