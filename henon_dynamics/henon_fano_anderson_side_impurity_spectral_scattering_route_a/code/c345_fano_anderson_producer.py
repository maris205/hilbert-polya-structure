#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C345."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c345_fano_anderson_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C345/2026-09-03.yaml"
SOURCE = "1af63b945e19b5f94ac1cb76f93af5ac66d3d562"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "ac793e0ba23eee9154ae2ebacb966aa53289247b5aa847ef8c35ca58588bb056"
EVAL_SEMANTIC = "07c7fb37d0b7452c7adafc64b36ca04fb0fe88104e124310da7aed764dfef490"
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

J_VALUES = [Fraction(1, 2), Fraction(1), Fraction(2)]
EPS_VALUES = [Fraction(-3), Fraction(-2), Fraction(-1), Fraction(0),
              Fraction(1), Fraction(2), Fraction(3)]
G_VALUES = [Fraction(-2), Fraction(-1), Fraction(-1, 2),
            Fraction(1, 2), Fraction(1), Fraction(2)]
G_ABS_VALUES = [Fraction(1, 2), Fraction(1), Fraction(2)]
COS_VALUES = [Fraction(-3, 4), Fraction(-1, 2), Fraction(0),
              Fraction(1, 2), Fraction(3, 4)]


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


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def derivative(poly: list[Fraction]) -> list[Fraction]:
    return trim([Fraction(i) * poly[i] for i in range(1, len(poly))] or [Fraction(0)])


def divrem(left: list[Fraction], right: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    numerator = trim(left[:])
    denominator = trim(right[:])
    if denominator == [0]:
        raise ZeroDivisionError
    quotient = [Fraction(0)] * max(1, len(numerator) - len(denominator) + 1)
    while numerator != [0] and len(numerator) >= len(denominator):
        degree = len(numerator) - len(denominator)
        coefficient = numerator[-1] / denominator[-1]
        quotient[degree] += coefficient
        for index, value in enumerate(denominator):
            numerator[index + degree] -= coefficient * value
        trim(numerator)
    return trim(quotient), trim(numerator)


def sturm(poly: list[Fraction]) -> list[list[Fraction]]:
    sequence = [trim(poly[:]), derivative(poly)]
    while sequence[-1] != [0]:
        _, remainder = divrem(sequence[-2], sequence[-1])
        if remainder == [0]:
            break
        sequence.append([-value for value in remainder])
    return sequence


def sign_fraction(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def evaluation(poly: list[Fraction], x: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(poly):
        result = result * x + coefficient
    return result


def variations(signs: list[int]) -> int:
    nonzero = [value for value in signs if value]
    return sum(a != b for a, b in zip(nonzero, nonzero[1:]))


def variation_at(sequence: list[list[Fraction]], point) -> int:
    signs = []
    for poly in sequence:
        if point == "-inf":
            signs.append(sign_fraction(poly[-1]) * (-1 if (len(poly) - 1) % 2 else 1))
        elif point == "+inf":
            signs.append(sign_fraction(poly[-1]))
        else:
            signs.append(sign_fraction(evaluation(poly, point)))
    return variations(signs)


def root_count(sequence: list[list[Fraction]], left, right) -> int:
    return variation_at(sequence, left) - variation_at(sequence, right)


def quartic(J: Fraction, epsilon: Fraction, g: Fraction) -> list[Fraction]:
    # Ascending coefficients of (E-epsilon)^2(E^2-4J^2)-g^4.
    return [
        -4 * epsilon * epsilon * J * J - g**4,
        8 * epsilon * J * J,
        epsilon * epsilon - 4 * J * J,
        -2 * epsilon,
        Fraction(1),
    ]


def spectral_rows() -> list[dict]:
    rows = []
    for J in J_VALUES:
        for epsilon in EPS_VALUES:
            for g in G_VALUES:
                coefficients = quartic(J, epsilon, g)
                sequence = sturm(coefficients)
                lower_physical_cut = min(-2 * J, epsilon)
                upper_physical_cut = max(2 * J, epsilon)
                physical_lower = root_count(sequence, "-inf", lower_physical_cut)
                physical_upper = root_count(sequence, upper_physical_cut, "+inf")
                total_real = root_count(sequence, "-inf", "+inf")
                rows.append({
                    "J": qstr(J),
                    "epsilon": qstr(epsilon),
                    "g": qstr(g),
                    "quartic_coefficients_ascending": [qstr(x) for x in coefficients],
                    "physical_lower_interval": f"(-infinity,{qstr(lower_physical_cut)})",
                    "physical_upper_interval": f"({qstr(upper_physical_cut)},infinity)",
                    "physical_lower_root_count": physical_lower,
                    "physical_upper_root_count": physical_upper,
                    "quartic_real_root_count": total_real,
                    "branch_rejected_real_root_count": total_real - physical_lower - physical_upper,
                    "band_root_count": root_count(sequence, -2 * J, 2 * J),
                })
    return rows


def scattering_rows() -> list[dict]:
    rows = []
    for J in J_VALUES:
        for epsilon in EPS_VALUES:
            for g in G_ABS_VALUES:
                for cosine in COS_VALUES:
                    energy = 2 * J * cosine
                    sine_squared = 1 - cosine * cosine
                    channel = 4 * J * J * sine_squared * (energy - epsilon)**2
                    denominator = g**4 + channel
                    density_s2 = 4 * J * J - energy * energy
                    density_denominator = (energy - epsilon)**2 * density_s2 + g**4
                    rows.append({
                        "J": qstr(J), "epsilon": qstr(epsilon), "abs_g": qstr(g),
                        "cos_k": qstr(cosine), "energy": qstr(energy),
                        "sin_squared_k": qstr(sine_squared),
                        "transmission": qstr(channel / denominator),
                        "reflection": qstr(g**4 / denominator),
                        "unitarity_sum": "1",
                        "density_radical_squared": qstr(density_s2),
                        "density_denominator": qstr(density_denominator),
                        "pi_density_divided_by_radical": qstr(g*g / density_denominator),
                    })
    return rows


def fano_rows() -> list[dict]:
    rows = []
    for J in J_VALUES:
        for epsilon in EPS_VALUES:
            if abs(epsilon) < 2 * J:
                location = "interior_exact_zero"
            elif abs(epsilon) == 2 * J:
                location = "band_edge_not_open_channel"
            else:
                location = "outside_band_not_on_shell"
            for g in G_ABS_VALUES:
                rows.append({
                    "J": qstr(J), "epsilon": qstr(epsilon), "abs_g": qstr(g),
                    "location": location,
                    "on_shell_energy": qstr(epsilon) if location == "interior_exact_zero" else None,
                    "transmission_numerator_at_epsilon": "0",
                    "transmission_denominator_at_epsilon": qstr(g**4),
                    "is_continuum_fano_zero": location == "interior_exact_zero",
                })
    return rows


def moment_rows() -> list[dict]:
    rows = []
    for epsilon in EPS_VALUES:
        for g in G_ABS_VALUES:
            rows.append({
                "epsilon": qstr(epsilon), "abs_g": qstr(g),
                "coefficient_z_minus_1": "1",
                "coefficient_z_minus_2": qstr(epsilon),
                "coefficient_z_minus_3": qstr(epsilon*epsilon + g*g),
                "coefficient_z_minus_4": qstr(epsilon**3 + 2*epsilon*g*g),
                "mass_conclusion": "ac_density_plus_two_bound_atoms_has_total_mass_one",
            })
    return rows


def make_data() -> dict:
    evaluation_raw = EVALUATION.read_bytes()
    if sha(evaluation_raw) != EVAL_RAW or semantic_yaml_hash(evaluation_raw) != EVAL_SEMANTIC:
        raise AssertionError("evaluation lock mismatch")
    spectral = spectral_rows()
    scattering = scattering_rows()
    fano = fano_rows()
    moments = moment_rows()
    data = {
        "schema": "hcs-c345-fano-anderson-v2",
        "candidate_id": "HCS-C345",
        "obstruction_id": "HEN-O329",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR,
        },
        "evaluation": {
            "path": "evaluations/route_a/HCS-C345/2026-09-03.yaml",
            "raw_sha256": EVAL_RAW,
            "semantic_sha256": EVAL_SEMANTIC,
        },
        "model": {
            "hilbert_space": "ell2(Z) direct_sum C|d>",
            "chain_action": "(Hu)_n=J(u_{n+1}+u_{n-1})+g*u_d*delta_{n0}",
            "impurity_action": "(Hu)_d=epsilon*u_d+g*u_0",
            "main_domain": "J>0, epsilon real, g real",
            "free_dispersion": "E=2*J*cos(k)",
            "resolvent_branch": "sqrt(z^2-4J^2) is analytic off [-2J,2J] and asymptotic to z",
            "free_origin_m_function": "m(z)=1/sqrt(z^2-4J^2)",
            "impurity_resolvent": "G_dd(z)=1/(z-epsilon-g^2*m(z))",
        },
        "theorem_contract": {
            "spectral_type": "for J>0 and g!=0 the band [-2J,2J] is purely absolutely continuous of multiplicity two almost everywhere, with no singular-continuous spectrum",
            "resolvent_sign": "G_dd(z)=<d,(z-H)^(-1)d> is anti-Herglotz on the upper half-plane, while M_dd(z)=-G_dd(z)=<d,(H-z)^(-1)d> is Herglotz",
            "measure_exclusion": "local-uniform boundary convergence plus Stone inversion gives the full open-band density; off-band meromorphy leaves only two simple atoms; the two edge atom limits vanish",
            "bound_states": "for J>0 and g!=0 there are exactly two simple eigenvalues, one below -2J and one above 2J",
            "physical_branch": "the lower state solves E-epsilon+g^2/sqrt(E^2-4J^2)=0 and the upper solves E-epsilon-g^2/sqrt(E^2-4J^2)=0",
            "quartic_filter": "squaring yields (E-epsilon)^2(E^2-4J^2)-g^4=0 but only branch-compatible roots are eigenvalues",
            "density": "rho_d(E)=g^2*sqrt(4J^2-E^2)/(pi*((E-epsilon)^2*(4J^2-E^2)+g^4)) in the open band",
            "residues": "the two impurity atom weights are 1/(1-g^2*m'(E_pm)) and density plus atoms has mass one",
            "scattering": "T=4J^2*sin(k)^2*(E-epsilon)^2/(g^4+4J^2*sin(k)^2*(E-epsilon)^2), R=1-T",
            "fano_zero": "for g!=0 an exact continuum zero occurs at E=epsilon iff abs(epsilon)<2J",
        },
        "spectral_measure_proof_lock": {
            "cauchy_convention": "G_dd(z)=integral (z-E)^(-1) dmu_d(E) has negative imaginary part for Im(z)>0; M_dd=-G_dd is the standard Herglotz transform",
            "density_sign": "rho_d(E)=-pi^(-1)*Im(G_dd(E+i0)) on the open band",
            "open_band_measure": "on every compact K inside (-2J,2J), G_dd(E+i*eta) converges uniformly to its continuous nonpolar boundary value and Stone inversion gives mu_d restricted to K equals rho_d(E)dE",
            "off_band_measure": "on the real complement of [-2J,2J], G_dd is real analytic except at exactly the two simple physical poles, so the measure there consists exactly of their two atoms",
            "edge_atom_test": "for E0=plus_or_minus 2J, mu_d({E0})=limit eta->0+ of i*eta*G_dd(E0+i*eta)=0 because G_dd=S/((z-epsilon)S-g^2) tends to zero",
            "singular_continuous_exclusion": "compact exhaustion of the open band, the off-band pole classification, and the zero edge atoms leave no support for a singular-continuous remainder",
        },
        "references": [
            {"identifier": "10.1103/PhysRev.124.1866", "role": "primary Fano discrete-continuum interference source"},
            {"identifier": "10.1002/cpa.3160010404", "role": "primary continuous-spectrum perturbation source"},
            {"identifier": "10.1103/RevModPhys.82.2257", "role": "authoritative Fano-resonance review and discrete-model context"},
        ],
        "collision_boundary": {
            "C267": "Wannier--Stark uses a uniform field and a pure-point ladder, not a side impurity or Fano zero",
            "C288": "the continuum delta point interaction has no discrete side level and no two-channel Fano interference",
            "C308": "Hatano--Nelson is non-self-adjoint boundary-sensitive transport, not a self-adjoint finite-rank impurity",
            "C318": "SSH is a dimerized topological finite chain, not a discrete state coupled to a continuum backbone",
        },
        "nonclaims": [
            "No priority claim is made for the Fano--Anderson model, its resolvent, or its scattering formula.",
            "Finite chains are not used to prove the infinite-volume spectrum or spectral type.",
            "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert--Polya operator, or Route-B input is claimed.",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "parameter_grid": {
            "J_values": [qstr(value) for value in J_VALUES],
            "epsilon_values": [qstr(value) for value in EPS_VALUES],
            "g_nonzero_values": [qstr(value) for value in G_VALUES],
            "cos_k_values": [qstr(value) for value in COS_VALUES],
            "evidence_role": "exact finite implementation receipt, not proof by sampling or finite-volume approximation",
        },
        "spectral_rows": spectral,
        "scattering_rows": scattering,
        "fano_zero_rows": fano,
        "resolvent_moment_rows": moments,
        "boundary_rows": {
            "g_zero": "free chain direct_sum isolated impurity; the impurity eigenvalue may be embedded, at a band edge, or outside the band",
            "J_zero": "a two-by-two origin-impurity block with eigenvalues (epsilon plus_or_minus sqrt(epsilon^2+4g^2))/2 plus an infinite-multiplicity zero eigenspace",
            "coupling_sign": "g and -g are unitarily equivalent by changing the impurity phase",
            "epsilon_band_edges": "epsilon=plus_or_minus 2J is not an open-channel Fano zero; for g!=0 neither band edge is an eigenvalue",
            "g_to_zero": "the two physical poles approach the appropriate band edges or the decoupled level non-uniformly; the theorem does not identify the g=0 spectral decomposition by continuity alone",
            "quartic_warning": "branch-rejected real roots of the squared quartic are never promoted to eigenvalues",
        },
        "enumeration": {
            "spectral_rows": len(spectral),
            "scattering_rows": len(scattering),
            "fano_zero_rows": len(fano),
            "resolvent_moment_rows": len(moments),
        },
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data)
    data["payload_sha256"] = sha(json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    return data


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C345 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = make_data()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        "C345_PRODUCER_PASS "
        f"{len(data['spectral_rows'])} spectral "
        f"{len(data['scattering_rows'])} scattering "
        f"{data['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
