#!/usr/bin/env python3
"""Produce the deterministic HCS-C202 Fisher--KPP wave-atlas evidence.

The all-speed theorem is analytic and source-attributed.  The finite ledger
only regression-tests scaling, phase-plane signs, tail classifications,
Hamiltonian levels, the trapping boundary, and the Ablowitz--Zeppetella
control.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c202_fisher_kpp_evidence.json"
SOURCE_COMMIT = "d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SPEEDS = tuple(F(value, 2) for value in range(-8, 9))
PHASE_U = (F(1, 10), F(1, 4), F(1, 2), F(3, 4), F(9, 10))
PHASE_V = (F(-2, 3), F(-1, 4), F(1, 4), F(2, 3))
OVAL_ENERGIES = (F(1, 96), F(1, 48), F(1, 24), F(1, 12), F(1, 8), F(5, 32))
AZ_Y = (F(1, 16), F(1, 9), F(1, 4), F(1, 2), F(1), F(2), F(4), F(9), F(16))
PHYSICAL = (
    (F(1), F(1)), (F(1, 2), F(3, 2)), (F(2), F(1, 3)),
    (F(3, 2), F(5, 2)), (F(5, 3), F(7, 4)), (F(7, 5), F(11, 6)),
)


def qtext(value: F | int) -> str:
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def m(value: F | int) -> mp.mpf:
    value = F(value)
    return mp.mpf(value.numerator) / value.denominator


def fmt(value: mp.mpf) -> str:
    return mp.nstr(value, 82, strip_zeros=False)


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def bisect_root(function, left: mp.mpf, right: mp.mpf) -> mp.mpf:
    f_left = function(left)
    f_right = function(right)
    if f_left == 0:
        return left
    if f_right == 0:
        return right
    if f_left * f_right >= 0:
        raise AssertionError((left, right, f_left, f_right))
    for _ in range(420):
        middle = (left + right) / 2
        f_middle = function(middle)
        if f_left * f_middle <= 0:
            right, f_right = middle, f_middle
        else:
            left, f_left = middle, f_middle
    return (left + right) / 2


def speed_class(speed: F) -> tuple[str, str, str]:
    if speed > 2:
        return "positive_supercritical", "stable_node", "decreasing_1_to_0"
    if speed == 2:
        return "positive_critical", "degenerate_stable_node", "decreasing_1_to_0"
    if speed > 0:
        return "positive_subcritical", "stable_focus", "none_in_unit_interval"
    if speed == 0:
        return "stationary_hamiltonian", "center", "none_in_unit_interval"
    if speed > -2:
        return "negative_subcritical", "unstable_focus", "none_in_unit_interval"
    if speed == -2:
        return "negative_critical", "degenerate_unstable_node", "increasing_0_to_1"
    return "negative_supercritical", "unstable_node", "increasing_0_to_1"


def build_speed_row(speed: F) -> dict:
    s = m(speed)
    saddle_disc = mp.sqrt(s * s + 4)
    saddle_positive = (-s + saddle_disc) / 2
    saddle_negative = (-s - saddle_disc) / 2
    tail_discriminant = speed * speed - 4
    family, zero_type, front = speed_class(speed)
    if tail_discriminant > 0:
        root = mp.sqrt(m(tail_discriminant))
        zero_spectral = {
            "kind": "real",
            "lambda_slow": fmt((-s + root) / 2),
            "lambda_fast": fmt((-s - root) / 2),
        }
    elif tail_discriminant == 0:
        zero_spectral = {"kind": "repeated_real", "lambda": fmt(-s / 2)}
    else:
        zero_spectral = {
            "kind": "complex_pair",
            "real_part": fmt(-s / 2),
            "imaginary_part_magnitude": fmt(mp.sqrt(-m(tail_discriminant)) / 2),
        }
    return {
        "dimensionless_speed": qtext(speed),
        "speed_family": family,
        "tail_discriminant": qtext(tail_discriminant),
        "zero_equilibrium_type": zero_type,
        "admissible_unit_interval_front": front,
        "divergence": qtext(-speed),
        "energy_derivative_sign": "decreasing" if speed > 0 else "increasing" if speed < 0 else "conserved",
        "saddle_positive_rate": fmt(saddle_positive),
        "saddle_negative_rate": fmt(saddle_negative),
        "zero_spectral_data": zero_spectral,
    }


def build() -> dict:
    mp.mp.dps = 110
    speed_rows = [build_speed_row(speed) for speed in SPEEDS]

    phase_rows = []
    for speed in SPEEDS:
        for u in PHASE_U:
            for v in PHASE_V:
                phase_rows.append({
                    "speed": qtext(speed),
                    "U": qtext(u),
                    "V": qtext(v),
                    "U_prime": qtext(v),
                    "V_prime": qtext(-speed * v - u * (1 - u)),
                    "energy_derivative": qtext(-speed * v * v),
                    "divergence": qtext(-speed),
                })

    trapping_rows = []
    for speed in (F(2), F(5, 2), F(3), F(7, 2), F(4)):
        s = m(speed)
        q = (s - mp.sqrt(s * s - 4)) / 2
        for u in PHASE_U:
            trapping_rows.append({
                "speed": qtext(speed),
                "U": qtext(u),
                "slow_slope_q": fmt(q),
                "quadratic_residual_abs": fmt(abs(q * q - s * q + 1)),
                "boundary_G_prime": qtext(u * u),
                "triangle": "0<=U<=1 and -qU<=V<=0",
            })

    potential = lambda x: x * x / 2 - x * x * x / 3
    oval_rows = []
    for energy in OVAL_ENERGIES:
        h = m(energy)
        function = lambda x, h=h: potential(x) - h
        negative = bisect_root(function, mp.mpf(-2), mp.mpf(0))
        inner = bisect_root(function, mp.mpf(0), mp.mpf(1))
        outer_right = mp.mpf(2)
        while function(outer_right) > 0:
            outer_right *= 2
        outer = bisect_root(function, mp.mpf(1), outer_right)
        oval_rows.append({
            "energy": qtext(energy),
            "negative_turning_point": fmt(negative),
            "inner_positive_turning_point": fmt(inner),
            "outer_unbounded_component_root": fmt(outer),
            "negative_residual_abs": fmt(abs(function(negative))),
            "inner_residual_abs": fmt(abs(function(inner))),
            "outer_residual_abs": fmt(abs(function(outer))),
            "periodic_oval_component": "negative_to_inner_positive",
        })

    az_rows = []
    for y in AZ_Y:
        denominator = (1 + y)
        profile = 1 / denominator**2
        derivative_coefficient = -2 * y / denominator**3
        second = -y * (1 - 2 * y) / (3 * denominator**4)
        speed_times_first = -5 * y / (3 * denominator**3)
        reaction = profile * (1 - profile)
        residual = second + speed_times_first + reaction
        if residual != 0:
            raise AssertionError((y, residual))
        az_rows.append({
            "exponential_coordinate_y": qtext(y),
            "U": qtext(profile),
            "U_xi_coefficient_over_sqrt6": qtext(derivative_coefficient),
            "U_xixi": qtext(second),
            "speed_times_U_xi": qtext(speed_times_first),
            "reaction_U_one_minus_U": qtext(reaction),
            "ode_residual": qtext(residual),
            "strictly_decreasing": derivative_coefficient < 0,
        })

    physical_rows = []
    for diffusion, growth in PHYSICAL:
        scale = mp.sqrt(m(diffusion * growth))
        physical_rows.append({
            "D": qtext(diffusion),
            "r": qtext(growth),
            "length_scale_sqrt_D_over_r": fmt(mp.sqrt(m(diffusion / growth))),
            "minimal_speed_2sqrt_Dr": fmt(2 * scale),
            "az_speed_5sqrt_Dr_over_sqrt6": fmt(5 * scale / mp.sqrt(6)),
            "az_inverse_length_sqrt_r_over_6D": fmt(mp.sqrt(m(growth / (6 * diffusion)))),
        })

    data = {
        "schema": "hcs-c202-fisher-kpp-wave-atlas-v1",
        "candidate_id": "HCS-C202",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": (
            "The Fisher--KPP traveling-wave ODE has a complete all-speed phase atlas: "
            "positive monotone fronts exist exactly at and above the pulled threshold, "
            "negative speeds are reflections, and every remaining speed has a certified obstruction"
        ),
        "source_lock": {
            "pde": "u_t=D*u_xx+r*u*(1-u) on the real line",
            "parameters": "D>0 and r>0",
            "traveling_coordinate": "z=x-c*t and u(x,t)=U(z)",
            "profile_ode": "D*U''+c*U'+r*U*(1-U)=0",
            "dimensionless_coordinate": "xi=sqrt(r/D)*z",
            "dimensionless_speed": "s=c/sqrt(D*r)",
            "dimensionless_system": "U'=V, V'=-s*V-U*(1-U)",
            "front_orientation": "for c>0, U(-infinity)=1 and U(+infinity)=0; c<0 uses spatial reflection",
            "allowed_data": "exact rational phase-plane controls and high-precision source-native algebra",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, and Route B",
        },
        "source_registry": [
            {
                "key": "Fisher1937",
                "authors": "R. A. Fisher",
                "title": "The Wave of Advance of Advantageous Genes",
                "journal": "Annals of Eugenics 7(4), 355--369",
                "year": 1937,
                "doi": "10.1111/j.1469-1809.1937.tb02153.x",
                "role": "historical Fisher equation and wave-speed argument",
            },
            {
                "key": "KPP1937",
                "authors": "A. N. Kolmogorov, I. G. Petrovskii, N. S. Piskunov",
                "title": "Etude de l'equation de la diffusion avec croissance de la quantite de matiere et son application a un probleme biologique",
                "journal": "Bulletin de l'Universite d'Etat a Moscou, Serie Internationale A 1, 1--25",
                "year": 1937,
                "translation_locator": "Selected Works of A. N. Kolmogorov I, Kluwer 1991, pp. 242--270, translated by V. M. Volosov",
                "role": "classical existence, monotonicity, uniqueness up to translation, and minimal-speed theorem",
            },
            {
                "key": "AblowitzZeppetella1979",
                "authors": "M. J. Ablowitz, A. Zeppetella",
                "title": "Explicit solutions of Fisher's equation for a special wave speed",
                "journal": "Bulletin of Mathematical Biology 41, 835--840",
                "year": 1979,
                "doi": "10.1007/BF02462380",
                "role": "closed-form profile at dimensionless speed 5/sqrt(6)",
            },
        ],
        "attribution": {
            "status": "CLASSICAL_FISHER_KPP_THEOREM_WITH_SOURCE_LOCKED_PHASE_PORTRAIT_SYNTHESIS",
            "classical_owner": "Fisher 1937 and Kolmogorov--Petrovskii--Piskunov 1937 own the front and minimal-speed theory",
            "exact_control_owner": "Ablowitz--Zeppetella 1979 own the displayed special-speed solution",
            "package_increment": "one convention-locked proof package closes every real speed, both orientations, all local tails, no-cycle identities, and the stationary Hamiltonian boundary",
            "finite_evidence_role": "finite rows regression-test formulas and code; they do not prove continuous shooting, trapping, or all-speed existence",
            "novelty_claimed": False,
            "external_review_claimed": False,
        },
        "theorem": {
            "positive_front": "for every c>=2*sqrt(D*r), exactly one translation class has 0<U<1, U'<0, U(-infinity)=1, and U(+infinity)=0",
            "reflected_front": "for every c<=-2*sqrt(D*r), spatial reflection gives exactly one translation class with 0<U<1 increasing from 0 to 1",
            "subcritical_obstruction": "for 0<abs(c)<2*sqrt(D*r), the zero-state eigenvalues are a nonreal pair and every nonzero tail approaching that state changes sign, so no [0,1] front exists",
            "stationary_boundary": "at c=0 the Hamiltonian has periodic ovals around (0,0), but H(1,0)=r/6 differs from H(0,0)=0 and therefore no 1-to-0 heteroclinic exists",
            "energy": "E=D*(U')^2/2+r*(U^2/2-U^3/3) satisfies E'=-c*(U')^2",
            "divergence": "the dimensionless planar divergence is -s, so no nonconstant periodic orbit exists when c!=0",
            "positive_tail": "at U=1 the departing exponent is (sqrt(c^2+4*D*r)-c)/(2*D)",
            "supercritical_tail": "for c>2*sqrt(D*r), U is asymptotic to B*exp(lambda_slow*z), lambda_slow=(-c+sqrt(c^2-4*D*r))/(2*D)",
            "critical_tail": "at c=2*sqrt(D*r), U is asymptotic to (A*z+B)*exp(-sqrt(r/D)*z) with A>0",
            "subcritical_tail": "for 0<c<2*sqrt(D*r), a nontrivial zero tail is an exponentially damped sinusoid with frequency sqrt(4*D*r-c^2)/(2*D)",
            "az_control": "at c=5*sqrt(D*r/6), U(z)=(1+exp(sqrt(r/D)*(z-z0)/sqrt(6)))^(-2)",
        },
        "proof_boundary": {
            "existence_mechanism": "for s>=2, q=(s-sqrt(s^2-4))/2 and the triangle 0<=U<=1, -qU<=V<=0 is forward invariant; the inward derivative on V=-qU is U^2",
            "uniqueness_mechanism": "the saddle (1,0) has one unstable branch entering the triangle; any admissible front is that orbit, and translation only changes its parametrization",
            "limit_mechanism": "constant negative divergence excludes cycles and the compact trapping triangle leaves (0,0) as the omega limit",
            "subcritical_mechanism": "Hartman linearization at the focus forces angular winding and sign changes; it is an obstruction, not a numerical shooting observation",
            "stationary_mechanism": "Hamiltonian level geometry supplies periodic ovals but endpoint energies rule out the requested heteroclinic",
            "regression_ceiling": "the finite certificate cannot establish an all-parameter heteroclinic or literature priority",
        },
        "finite_regression": {
            "speed_rows": speed_rows,
            "phase_rows": phase_rows,
            "trapping_rows": trapping_rows,
            "hamiltonian_oval_rows": oval_rows,
            "az_rows": az_rows,
            "physical_scalings": physical_rows,
        },
        "summary": {
            "speed_case_count": len(speed_rows),
            "phase_vector_field_row_count": len(phase_rows),
            "trapping_boundary_row_count": len(trapping_rows),
            "hamiltonian_oval_count": len(oval_rows),
            "az_exact_sample_count": len(az_rows),
            "physical_scaling_count": len(physical_rows),
            "precision_decimal_digits": 100,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "A0_qualification": "diffusion, growth, wave speed, and continuous phase coordinates have no intrinsic rational-prime origin",
            "A1_qualification": "the admissible fronts are heteroclinic translation classes, not a primitive periodic-orbit carrier",
            "A2_qualification": "the profile ODE supplies no source zeta, Euler product, or target divisor",
            "A3_qualification": "no target continuation, functional equation, counting law, or Weil compression follows",
            "A4_qualification": "the dissipative traveling-wave reduction has no source-native same-clock unitary or self-adjoint lift relevant to the target",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "uses_target_zero_table": False,
            "uses_target_prime_table": False,
            "uses_arithmetic_local_data": False,
            "claims_euler_factor": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor": False,
            "claims_target_functional_equation": False,
            "claims_hilbert_polya_operator": False,
            "claims_classical_novelty": False,
            "claims_external_peer_review": False,
            "invokes_route_b": False,
        },
        "nonclaims": [
            "priority for the Fisher equation, the KPP minimal-speed theorem, or the Ablowitz--Zeppetella profile",
            "an all-speed existence theorem inferred from the finite phase-plane rows",
            "a primitive periodic-orbit model, Artin--Mazur or Ruelle zeta, or rational-prime carrier",
            "a target divisor, target functional equation, continuation theorem, counting law, or Weil compression",
            "a Hilbert--Polya operator, Route-B authorization, global literature priority, external peer review, or acceptance score",
        ],
    }
    data["payload_sha256"] = canonical_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C202_PRODUCER_PASS",
        "speed_cases": data["summary"]["speed_case_count"],
        "phase_rows": data["summary"]["phase_vector_field_row_count"],
        "trapping_rows": data["summary"]["trapping_boundary_row_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
