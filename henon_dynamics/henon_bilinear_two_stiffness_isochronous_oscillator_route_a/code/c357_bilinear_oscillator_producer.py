#!/usr/bin/env python3
"""Deterministic exact producer for HCS-C357."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT/"results/c357_bilinear_oscillator_evidence.json"
EVALUATION = ROOT/"evaluations/route_a/HCS-C357/2026-09-03.yaml"
SOURCE = "140c8714b74de666d56f441ddfb712026955901a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "da4bf6ccbc6bb5cdeb60df9c4b215d0a2b6e0fae670cdc0e7c1dfd6c804f74c3"
EVAL_SEMANTIC = "83361e1520848f7a132a1b9b008be1f0bed6844449f4fb99b10871149238f4e4"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600

FLAGS = {
    "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
    "claims_root_number": False, "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False, "claims_target_functional_equation": False,
    "claims_target_zero_match": False, "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
MODEL = {
    "classical_hamiltonian": "H=p^2/2+omega_plus^2*(max(x,0))^2/2+omega_minus^2*(min(x,0))^2/2",
    "classical_equation": "x_dot=p; p_dot=-omega_plus^2*x for x>=0 and -omega_minus^2*x for x<=0",
    "action_angle_regularness": "globally C1 and piecewise analytic on the punctured plane, but not C2 across the seam unless the frequencies agree",
    "quantum_operator": "-one_half*d2_dx2+V on L2(R), defined by its Friedrichs quadratic form",
    "wronskian": "F(lambda)=sqrt(omega_plus)*D_nu_plus'(0)*D_nu_minus(0)+sqrt(omega_minus)*D_nu_minus'(0)*D_nu_plus(0), nu_sign=lambda/omega_sign-1/2",
}
THEOREM = {
    "classical_iff": "all nonzero trajectories are bounded periodic with a common least period iff omega_plus and omega_minus are both positive",
    "period_action": "T=pi*(1/omega_plus+1/omega_minus), J=E*(1/omega_plus+1/omega_minus)/2, and Omega=dE/dJ=2/(1/omega_plus+1/omega_minus)",
    "seam_monodromy": "the two seam-to-seam half-flow matrices are minus identity, so the common-period map and its derivative are identity",
    "action_angle": "the punctured plane has a global C1 piecewise-analytic action-angle chart with dx wedge dp=dtheta wedge dJ and theta_dot=Omega; it is not C2 across the seam unless the frequencies agree",
    "quantum": "for positive frequencies the Friedrichs operator is self-adjoint with compact resolvent and simple spectrum, and lambda is an eigenvalue iff the parabolic-cylinder interface Wronskian vanishes",
    "boundaries": "equal frequency, zero energy, one-sided zero stiffness, and the free particle are stated separately",
}
BOUNDARIES = {
    "zero_energy": "for positive frequencies E=0 is only the origin equilibrium",
    "equal_frequency": "omega_plus=omega_minus is the ordinary harmonic oscillator; the Wronskian zeros recover lambda_n=omega*(n+1/2)",
    "one_sided_zero": "a flat half-axis is a continuum of rest equilibria and every other orbit reaching it escapes linearly; quantum compact resolvent is lost and essential spectrum begins at zero",
    "free": "both frequencies zero give the free particle, all p=0 states are equilibria, and nonzero momentum is unbounded",
    "seam": "the force is continuous and globally Lipschitz, while its derivative jumps unless the frequencies agree",
    "smoothness": "the action-angle map is not claimed globally C-infinity across the seam",
}
REFERENCES = [
    {"identifier": "10.1088/0305-4470/38/27/007", "role": "primary study of quantum spectra of isochronous potentials including the asymmetric parabolic well"},
    {"identifier": "https://dlmf.nist.gov/12.2", "role": "NIST authority for the parabolic-cylinder equation, values, derivatives, and Wronskians"},
    {"identifier": "10.1090/gsm/157", "role": "authoritative self-adjoint one-dimensional Schrodinger-operator framework"},
]
COLLISIONS = {
    "C212": "affine impact dynamics resets velocity and has a separate flight-time roof",
    "C232": "Duffing is smooth, amplitude-dependent, and has separatrix chambers",
    "C238": "Coulomb friction is dissipative Filippov dynamics with finite capture",
    "C252": "the relay oscillator changes a discrete guard state and owns an attracting hybrid cycle",
}
NONCLAIMS = [
    "No priority claim is made for asymmetric parabolic isochrony or parabolic-cylinder matching.",
    "Classical isochrony does not imply an equally spaced asymmetric quantum spectrum.",
    "The interface Wronskian is a source spectral equation, not a target determinant.",
    "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route-B input is claimed.",
]
FREQUENCIES = [
    (Q(1), Q(1)), (Q(1), Q(2)), (Q(2), Q(3)), (Q(1, 2), Q(3, 2)),
    (Q(3), Q(5)), (Q(2, 3), Q(4, 3)), (Q(5, 2), Q(7, 2)),
    (Q(4), Q(1)), (Q(3, 4), Q(5, 4)), (Q(7), Q(2)),
]
ENERGIES = (Q(1, 8), Q(1, 2), Q(1), Q(3, 2), Q(2), Q(5))
QFREQ = (Q(1, 2), Q(1), Q(2), Q(5, 2), Q(3))


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def qstr(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def leaves(value):
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def classical_rows():
    rows = []
    minus_i = [["-1", "0"], ["0", "-1"]]
    identity = [["1", "0"], ["0", "1"]]
    for fi, (wp, wm) in enumerate(FREQUENCIES):
        total = 1/wp+1/wm
        Omega = 2/total
        for ei, E in enumerate(ENERGIES):
            J = E*total/2
            rows.append({
                "frequency_index": fi, "energy_index": ei,
                "omega_plus": qstr(wp), "omega_minus": qstr(wm), "energy": qstr(E),
                "k_plus": qstr(wp*wp), "k_minus": qstr(wm*wm),
                "amplitude_plus_squared": qstr(2*E/(wp*wp)),
                "amplitude_minus_squared": qstr(2*E/(wm*wm)),
                "seam_speed_squared": qstr(2*E),
                "right_time_over_pi": qstr(1/wp), "left_time_over_pi": qstr(1/wm),
                "period_over_pi": qstr(total), "action": qstr(J),
                "action_over_energy": qstr(total/2), "loop_area_over_pi": qstr(E*total),
                "Omega": qstr(Omega), "Omega_times_period_over_pi": "2",
                "right_half_matrix": minus_i, "left_half_matrix": minus_i,
                "full_monodromy": identity,
                "right_time_fraction": qstr((1/wp)/total),
                "left_time_fraction": qstr((1/wm)/total),
            })
    return rows


def quantum_rows():
    rows = []
    for fi, omega in enumerate(QFREQ):
        for n in range(17):
            lam = omega*(Q(n)+Q(1, 2))
            rows.append({
                "frequency_index": fi, "level": n, "omega": qstr(omega),
                "lambda": qstr(lam), "nu_plus": str(n), "nu_minus": str(n),
                "parity": "even" if n % 2 == 0 else "odd",
                "vanishing_interface_factor": "D_prime" if n % 2 == 0 else "D_value",
                "wronskian_zero": True,
            })
    return rows


def boundary_rows():
    return [
        {"omega_plus": "0", "omega_minus": "1", "flat_side": "right", "classical": "rest continuum on x>=0 plus linear escape", "quantum_compact_resolvent": False, "essential_lower_edge": "0"},
        {"omega_plus": "1", "omega_minus": "0", "flat_side": "left", "classical": "rest continuum on x<=0 plus linear escape", "quantum_compact_resolvent": False, "essential_lower_edge": "0"},
        {"omega_plus": "0", "omega_minus": "0", "flat_side": "both", "classical": "free particle", "quantum_compact_resolvent": False, "essential_lower_edge": "0"},
    ]


def main():
    if sys.flags.optimize:
        raise RuntimeError("C357 producer refuses optimized Python")
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=OUTPUT); args = parser.parse_args()
    raw_eval = EVALUATION.read_bytes()
    semantic = sha(json.dumps(yaml.safe_load(raw_eval), sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    if sha(raw_eval) != EVAL_RAW or semantic != EVAL_SEMANTIC:
        raise AssertionError("evaluation lock mismatch")
    data = {
        "schema": "hcs-c357-bilinear-oscillator-evidence-v1", "candidate_id": "HCS-C357",
        "obstruction_id": "HEN-O341", "evaluation_date": "2026-09-03",
        "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation_lock": {"relative_path": "evaluations/route_a/HCS-C357/2026-09-03.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC},
        "model": MODEL, "theorem_contract": THEOREM, "boundary_atlas": BOUNDARIES,
        "references": REFERENCES, "collision_boundary": COLLISIONS, "nonclaims": NONCLAIMS,
        "route_a": {"tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b": False},
        "scope_flags": FLAGS,
        "frequency_grid": [[qstr(a), qstr(b)] for a, b in FREQUENCIES],
        "energy_grid": [qstr(e) for e in ENERGIES],
        "classical_rows": classical_rows(), "quantum_equal_frequency_rows": quantum_rows(),
        "zero_stiffness_rows": boundary_rows(),
    }
    data["enumeration"] = {
        "frequency_pairs": len(FREQUENCIES), "energies": len(ENERGIES),
        "classical_rows": len(data["classical_rows"]),
        "quantum_equal_frequency_rows": len(data["quantum_equal_frequency_rows"]),
        "zero_stiffness_rows": len(data["zero_stiffness_rows"]),
        "leaf_count_without_payload_hash": leaves(data),
    }
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha(canonical)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)+"\n")
    print(f"C357_PRODUCER_PASS classical={len(data['classical_rows'])} quantum={len(data['quantum_equal_frequency_rows'])} leaves={leaves(data)} payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
