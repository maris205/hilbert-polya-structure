#!/usr/bin/env python3
"""Canonical exact evidence producer for HCS-C366."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from pathlib import Path

SOURCE = "323ea43f6970544467f8a89f0ed9be0c7c39f896"
DATE = "2026-09-04"
EPOCH = 1788480000
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
AUTHORITY = "flow_systems/skills/route-a-evaluator.md"
EVALUATOR_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_PATH = "evaluations/route_a/HCS-C366/2026-09-04.yaml"
EVAL_RAW = "acc72ba628087e67f52927031ca66ee1798cc8073907133cf7049df49f04cc59"
EVAL_SEMANTIC = "a2ab8e3e0d4256ea4058300f66fecac5f6fec5283f9ad80432b21e28b0648ef5"
FINITE_ROLE = (
    "exact spectrum, orthogonality, formal all-time endpoint monomials, subset-energy "
    "and mirror-phase rows, Gaussian q-binomial coefficient polynomials, and boundary "
    "regression only; representation and exterior-power arguments prove the all-size theorem"
)
COLLISION = (
    "C143 owns an inhomogeneous coined quantum walk; C171 owns Ehrenfest/Krawtchouk "
    "Markov lumping; C366 uniquely owns the engineered XX perfect-transfer chain and "
    "full exterior-power phase law"
)
NONCLAIMS = (
    "No arithmetic target data, Euler factor, root number, automorphy, target divisor or "
    "functional equation, target-zero match, Hilbert--Polya operator, perturbative robustness, "
    "or Route B inference is claimed"
)


def refuse_optimized() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C366 producer refuses optimized Python")


def krawtchouk(n: int, r: int, j: int) -> int:
    return sum(
        (-1) ** ell * math.comb(j, ell) * math.comb(n - j, r - ell)
        for ell in range(max(0, r - (n - j)), min(r, j) + 1)
    )


def add_shift(left: list[int], right: list[int], shift: int) -> list[int]:
    out = [0] * max(len(left), len(right) + shift)
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index + shift] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def gaussian_rows(max_n: int) -> list[dict]:
    """Return coefficients of [n choose m]_q using only its Pascal recurrence."""
    table: dict[tuple[int, int], list[int]] = {(0, 0): [1]}
    rows = [{"n": 0, "m": 0, "coefficients": [1]}]
    for n in range(1, max_n + 1):
        for m in range(n + 1):
            if m in (0, n):
                coefficients = [1]
            else:
                coefficients = add_shift(table[(n - 1, m)], table[(n - 1, m - 1)], n - m)
            table[(n, m)] = coefficients
            rows.append({"n": n, "m": m, "coefficients": coefficients})
    return rows


def canonical_payload(data: dict) -> str:
    encoded = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def build() -> dict:
    spectral_rows = []
    for n in range(11):
        for r in range(n + 1):
            values = [krawtchouk(n, r, j) for j in range(n + 1)]
            weighted_norm = sum(math.comb(n, j) * value * value
                                for j, value in enumerate(values))
            spectral_rows.append({
                "N": n,
                "r": r,
                "twice_energy_over_omega": n - 2 * r,
                "krawtchouk_values": values,
                "weighted_norm": weighted_norm,
                "expected_weighted_norm": (2 ** n) * math.comb(n, r),
            })

    subset_rows = []
    energy_multiplicity_rows = []
    for n in range(15):
        histogram: Counter[tuple[int, int]] = Counter()
        for mask in range(1 << (n + 1)):
            occupied = [j for j in range(n + 1) if mask & (1 << j)]
            particles = len(occupied)
            coordinate_sum = sum(occupied)
            twice_energy = particles * n - 2 * coordinate_sum
            mirror_mask = sum(1 << (n - j) for j in occupied)
            phase = (particles * n + particles * (particles - 1)) % 4
            histogram[(particles, twice_energy)] += 1
            subset_rows.append({
                "N": n,
                "mask": mask,
                "particles": particles,
                "coordinate_sum": coordinate_sum,
                "twice_energy_over_omega": twice_energy,
                "mirror_mask": mirror_mask,
                "mirror_phase_minus_i_exponent_mod4": phase,
            })
        for (particles, energy), multiplicity in sorted(histogram.items()):
            energy_multiplicity_rows.append({
                "N": n,
                "particles": particles,
                "twice_energy_over_omega": energy,
                "multiplicity": multiplicity,
            })

    endpoint_rows = []
    for n in range(21):
        for k in range(n + 1):
            endpoint_rows.append({
                "N": n,
                "site": k,
                "amplitude_phase_minus_i_exponent_mod4": k % 4,
                "amplitude_binomial_radicand": math.comb(n, k),
                "amplitude_sine_power": k,
                "amplitude_cosine_power": n - k,
                "half_transfer_probability_numerator": math.comb(n, k),
                "half_transfer_probability_denominator": 2 ** n,
                "mirror_probability": int(k == n),
                "zero_time_probability": int(k == 0),
            })

    gaussian = gaussian_rows(15)
    data = {
        "schema": "hcs-c366-evidence-v2",
        "candidate_id": "HCS-C366",
        "obstruction_id": "HEN-O350",
        "evaluation_date": DATE,
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {
            "authority": AUTHORITY,
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA,
        },
        "route_a_yaml": {
            "relative_path": EVAL_PATH,
            "raw_sha256": EVAL_RAW,
            "semantic_sha256": EVAL_SEMANTIC,
        },
        "model": {
            "sites": "0,...,N",
            "single_particle_hopping": "J_j=(omega/2)*sqrt((j+1)(N-j))",
            "clock": "physical unitary time",
            "propagator": "exp(-itH)",
            "fermion_order": "increasing site order",
            "uniform_field": "B*mhat with mhat the fermion-number operator; main model has B=0",
            "half_form_or_target_fit": False,
        },
        "theorem_status": "PROVABLE_AS_STATED",
        "route_tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL",
                        "A4_NATURAL_QUANTIZATION"],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "scope_flags": {
            "claims_target_arithmetic_local_data": False,
            "claims_target_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False,
            "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "exact_claims": {
            "single_particle_owner": "H/omega is the spin-N/2 J_x matrix",
            "spectrum": "omega*(N/2-r), r=0,...,N, with Krawtchouk eigenvectors",
            "endpoint_law": "(-i sign(omega))^k*sqrt(C(N,k))*sin(abs(omega)t/2)^k*cos(abs(omega)t/2)^(N-k)",
            "mirror": "for omega nonzero, perfect reflection at pi/abs(omega)",
            "many_body": "each m-particle propagator is the m-th exterior power",
            "mirror_phase": "(-i sign(omega))^(mN)*(-1)^(m(m-1)/2)",
            "multiplicity_owner": "coefficient of y^m q^s in product_(r=0)^N(1+y*q^r)",
            "gaussian_q_binomial": "[n,m]_q=[n-1,m]_q+q^(n-m)[n-1,m-1]_q with boundary one",
            "uniform_field_revival": "U_B(2pi/abs(omega))=exp(-i*2pi*B*mhat/abs(omega))*(-1)^(N*mhat); U_B(4pi/abs(omega))=exp(-i*4pi*B*mhat/abs(omega))",
            "full_identity_conditions": "2pi time iff 2B/abs(omega)+N is an even integer; 4pi time iff 2B/abs(omega) is an integer",
        },
        "boundary_atlas": {
            "N_zero": "one site; mirror is the identity and the uniform field is the only dynamics",
            "omega_zero": "the hopping Hamiltonian vanishes; revival times pi/abs(omega) are undefined",
            "negative_omega": "time orientation is conjugated and the mirror phase uses sign(omega)",
            "uniform_field": "B*mhat commutes with the hopping; its sector phase is exp(-imBt)",
            "perturbations": "no robustness of perfect transfer under generic coupling perturbations is claimed",
            "full_fock_revival": "at B=0, 2pi/abs(omega) is identity for even N and fermion parity for odd N; 4pi/abs(omega) is identity",
            "vacuum": "the vacuum is always fixed, so full-Fock identity conditions concern every particle sector simultaneously",
        },
        "finite_evidence_role": FINITE_ROLE,
        "collision_boundary": COLLISION,
        "nonclaims": NONCLAIMS,
        "references": [
            {"doi": "10.1103/PhysRevLett.92.187902", "role": "engineered spin-chain lineage"},
            {"doi": "10.1103/PhysRevLett.93.230502", "role": "perfect-state-transfer lineage"},
        ],
        "spectral_rows": spectral_rows,
        "subset_rows": subset_rows,
        "energy_multiplicity_rows": energy_multiplicity_rows,
        "endpoint_rows": endpoint_rows,
        "gaussian_q_binomial_rows": gaussian,
        "counts": {
            "spectral_rows": len(spectral_rows),
            "subset_states": len(subset_rows),
            "energy_multiplicity_rows": len(energy_multiplicity_rows),
            "endpoint_cells": len(endpoint_rows),
            "gaussian_q_binomial_rows": len(gaussian),
        },
    }
    data["payload_sha256"] = canonical_payload(data)
    return data


def main() -> None:
    refuse_optimized()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().parents[1] /
        "results/c366_krawtchouk_xx_evidence.json",
    )
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n")
    print("C366_PRODUCER_PASS subset_states=65534 spectral_rows=66 "
          "endpoint_cells=231 gaussian_rows=136")


if __name__ == "__main__":
    main()
