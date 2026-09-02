#!/usr/bin/env python3
"""Deterministic finite receipts for the HCS-C304 linear Cahn--Hilliard atlas."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c304_ch_evidence.json"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
mp.mp.dps = 90

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

CASE_SPECS = [
    ("D1-STABLE-NEG", 1, "1", "-1"),
    ("D1-CRITICAL", 1, "1", "1"),
    ("D1-SQUARE-TIE", 1, "1", "5"),
    ("D2-STABLE-HALF", 2, "2", "1"),
    ("D2-CRITICAL", 2, "1", "1"),
    ("D2-FIRST-TIE", 2, "1", "3"),
    ("D3-BIHARMONIC", 3, "1", "0"),
    ("D3-CRITICAL", 3, "1", "1"),
    ("D3-SPINODAL", 3, "2", "7"),
    ("D4-STABLE-NEG", 4, "2", "-1"),
    ("D4-CRITICAL", 4, "2", "2"),
    ("D4-FIRST-TIE", 4, "2", "6"),
    ("D5-STABLE", 5, "3", "2"),
    ("D5-CRITICAL", 5, "3", "3"),
    ("D5-SPINODAL", 5, "3", "15"),
    ("D6-STABLE-NEG", 6, "1", "-2"),
    ("D6-CRITICAL", 6, "1", "1"),
    ("D6-HALF-RATIO", 6, "2", "13"),
]

SUPPORT_SPECS = [
    ("P1-D1-TIED", 1, "1", "5", [(1, "1"), (4, "2"), (9, "-1")]),
    ("P2-D2-TIED", 2, "1", "3", [(1, "2"), (2, "1"), (4, "3")]),
    ("P3-D3-UNIQUE", 3, "2", "7", [(1, "1"), (2, "-2"), (3, "3")]),
    ("P4-D4-STABLE", 4, "2", "-1", [(1, "3"), (2, "1")]),
    ("P5-D5-NEUTRAL", 5, "3", "3", [(1, "2"), (2, "-1")]),
    ("P6-D6-ACTUAL-SUPPORT", 6, "2", "13", [(1, "1"), (3, "4"), (4, "-2"), (5, "1")]),
]


def fraction(text: str) -> Fraction:
    return Fraction(text)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dec(value: mp.mpf) -> str:
    if value == 0:
        return "0.0"
    return mp.nstr(value, 72, strip_zeros=False)


def shell_counts(dimension: int, maximum: int) -> list[int]:
    one = [0] * (maximum + 1)
    radius = int(maximum**0.5)
    for coordinate in range(-radius, radius + 1):
        one[coordinate * coordinate] += 1
    counts = [1] + [0] * maximum
    for _ in range(dimension):
        counts = [sum(counts[n - j] * one[j] for j in range(n + 1)) for n in range(maximum + 1)]
    return counts


def status(eigenvalue: Fraction, multiplicity: int) -> str:
    if multiplicity == 0:
        return "absent"
    if eigenvalue > 0:
        return "unstable"
    if eigenvalue == 0:
        return "neutral"
    return "stable"


def leaf_count(value) -> int:
    if type(value) is dict:
        return sum(leaf_count(item) for item in value.values())
    if type(value) is list:
        return sum(leaf_count(item) for item in value)
    return 1


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def build_case(case_id: str, dimension: int, kappa_text: str, alpha_text: str) -> dict:
    kappa, alpha = fraction(kappa_text), fraction(alpha_text)
    ratio = alpha / kappa
    exhaustion_cutoff = 1 if ratio <= 1 else math.ceil(ratio)
    counts = shell_counts(dimension, max(12, exhaustion_cutoff))
    represented = [n for n in range(1, exhaustion_cutoff + 1) if counts[n] > 0]
    eigenvalues = {n: alpha * n - kappa * n * n for n in represented}
    spectral_bound = max(eigenvalues.values())
    fastest = [n for n in represented if eigenvalues[n] == spectral_bound]
    rows = []
    for n in range(1, 13):
        eigenvalue = alpha * n - kappa * n * n
        multiplicity = counts[n]
        trace_term = mp.mpf(multiplicity) * mp.exp(mp.mpf(eigenvalue.numerator) / eigenvalue.denominator / 3)
        rows.append({
            "n": n,
            "multiplicity": multiplicity,
            "eigenvalue": q(eigenvalue),
            "energy_coefficient": q(kappa * n - alpha),
            "classification": status(eigenvalue, multiplicity),
            "trace_term_t_one_third": dec(trace_term),
        })
    unstable = [n for n in represented if eigenvalues[n] > 0]
    neutral = [n for n in represented if eigenvalues[n] == 0]
    if unstable:
        chamber = "spinodal_unstable"
    elif neutral:
        chamber = "critical_neutral"
    else:
        chamber = "strictly_stable"
    return {
        "case_id": case_id,
        "dimension": dimension,
        "kappa": q(kappa),
        "alpha": q(alpha),
        "ratio_alpha_over_kappa": q(alpha / kappa),
        "analytic_exhaustion_cutoff": exhaustion_cutoff,
        "chamber": chamber,
        "unstable_shells": unstable,
        "neutral_shells": neutral,
        "morse_index": sum(counts[n] for n in unstable),
        "kernel_dimension": sum(counts[n] for n in neutral),
        "fastest_shells": fastest,
        "spectral_bound": q(spectral_bound),
        "shell_rows": rows,
    }


def build_probe(probe_id: str, dimension: int, kappa_text: str, alpha_text: str, support) -> dict:
    kappa, alpha = fraction(kappa_text), fraction(alpha_text)
    counts = shell_counts(dimension, max(n for n, _ in support))
    for n, _ in support:
        if counts[n] == 0:
            raise ValueError(f"unrepresented support shell {n} in dimension {dimension}")
    rates = {n: alpha * n - kappa * n * n for n, _ in support}
    leading_rate = max(rates.values())
    leading = [n for n, _ in support if rates[n] == leading_rate]
    return {
        "probe_id": probe_id,
        "dimension": dimension,
        "kappa": q(kappa),
        "alpha": q(alpha),
        "support": [{"n": n, "coefficient": q(fraction(coefficient)), "rate": q(rates[n])} for n, coefficient in support],
        "leading_shells": leading,
        "leading_rate": q(leading_rate),
        "normalized_limit": "projection_onto_all_leading_supported_shells",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    cases = [build_case(*spec) for spec in CASE_SPECS]
    probes = [build_probe(*spec) for spec in SUPPORT_SPECS]
    kappa_zero = []
    for alpha in (Fraction(-2), Fraction(0), Fraction(2)):
        if alpha < 0:
            classification = "forward_heat_semigroup"
        elif alpha == 0:
            classification = "identity_semigroup"
        else:
            classification = "no_bounded_L2_C0_semigroup"
        kappa_zero.append({
            "alpha": q(alpha),
            "classification": classification,
            "first_four_mode_rates": [q(alpha * n) for n in range(1, 5)],
            "spectrum_bounded_above": alpha <= 0,
        })
    boundaries = [
        {"boundary_id": "B0-constant-mode", "statement": "On full L2 the zero Fourier mode is stationary and equals the conserved spatial mean."},
        {"boundary_id": "B1-critical-shell", "statement": "At alpha=kappa exactly the represented shell n=1 is neutral and has real dimension 2d."},
        {"boundary_id": "B2-shell-tie", "statement": "Every fastest-shell tie is retained as a full spectral projection rather than broken numerically."},
        {"boundary_id": "B3-kappa-zero", "statement": "The kappa=0 face is forward heat for alpha<0, identity for alpha=0, and ill posed as a bounded L2 semigroup for alpha>0."},
        {"boundary_id": "B4-nonlinear-exclusion", "statement": "No cubic Cahn--Hilliard dynamics, nonlinear saturation, phase coarsening, or pattern-selection theorem is claimed."},
        {"boundary_id": "B5-dimension", "statement": "The theorem holds for every finite integer d>=1; finite receipts only audit dimensions one through six."},
    ]
    receipt_cells = leaf_count(cases) + leaf_count(probes) + leaf_count(kappa_zero) + leaf_count(boundaries)
    data = {
        "schema": "hcs-c304-linear-cahn-hilliard-v1",
        "candidate_id": "HCS-C304",
        "obstruction_id": "HEN-O288",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "phase_space": "mean-zero L2 on the 2pi-periodic d-torus for every finite integer d>=1",
            "generator": "A_{kappa,alpha}=-kappa Delta^2-alpha Delta with domain H^4 intersect L2_0",
            "parameters": "kappa>0 and alpha real",
            "clock": "physical semigroup time t>=0",
        },
        "theorem_contract": {
            "semigroup": "self-adjoint analytic trace-class semigroup for every positive time",
            "spectrum": "sigma_n=alpha n-kappa n^2 with multiplicity r_d(n) on every represented shell n=|k|^2>0",
            "energy": "F=one-half integral(kappa|grad u|^2-alpha u^2) and Fdot=-norm(grad chemical_potential)^2",
            "atlas": "strict stability, critical kernel, spinodal Morse index, fastest represented ties, and actual-support long-time projection",
            "recurrence": "every recurrent state is stationary; there is no nonstationary periodic solution",
            "singular_boundary": "at kappa=0: forward heat for alpha<0, identity for alpha=0, no bounded L2 C0 semigroup for alpha>0",
        },
        "proof_contract": {
            "full_dimension": "Fourier diagonalization and lattice-shell multiplicities prove the theorem for every finite d>=1.",
            "fastest_exhaustion": "If alpha/kappa<=1 then shell n=1 is maximal; if alpha/kappa>1 then every n>=alpha/kappa has nonpositive rate while shell n=1 is positive, so only represented n below that bound can maximize.",
            "finite_role": "Finite dimensions and shells are regression receipts only and do not prove the arbitrary-d theorem.",
            "nonlinear_firewall": "The linearized equation does not imply nonlinear saturation, coarsening, or pattern selection.",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "nonclaims": [
            "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
            "Lattice wavevectors and shell multiplicities are source Fourier geometry, not rational-prime labels or target coefficients.",
            "The self-adjoint source generator is not asserted to be a Hilbert--Polya operator.",
            "No literature novelty or priority is claimed for the classical Cahn--Hilliard linearization or Fourier semigroup.",
        ],
        "collision_boundary": {
            "C206_C213_C217_C218_C261_C277": "Earlier Fourier packages have different transport, hyperbolic, dispersive, fractional, or damping generators; C304 is the fourth-order spinodal shell and energy-signature atlas.",
            "C195": "C195 is nonlinear periodic viscous Burgers through Cole--Hopf; C304 is a linear fourth-order conserved gradient flow in every finite dimension.",
        },
        "references": [
            {"identifier": "10.1063/1.1744102", "role": "historical free-energy owner attribution only"},
            {"identifier": "10.1016/0001-6160(61)90182-1", "role": "historical spinodal-decomposition owner attribution only"},
            {"identifier": "10.1007/BF00251803", "role": "classical Cahn--Hilliard analysis context only"},
        ],
        "enumeration": {
            "case_count": len(cases),
            "case_ids": [case["case_id"] for case in cases],
            "shell_rows_per_case": 12,
            "shell_row_count": 12 * len(cases),
            "support_probe_count": len(probes),
            "kappa_zero_rows": len(kappa_zero),
            "boundary_rows": len(boundaries),
            "audited_cell_count": receipt_cells,
        },
        "cases": cases,
        "support_probes": probes,
        "kappa_zero_boundary": kappa_zero,
        "boundaries": boundaries,
    }
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C304_PRODUCER_PASS",
        "cases": len(cases),
        "shell_rows": 12 * len(cases),
        "audited_cells": receipt_cells,
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
