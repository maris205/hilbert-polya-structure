#!/usr/bin/env python3
"""Deterministic producer for the HCS-C37 homogeneous boundary-index gate."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


SCHEMA = "hcs-c37-certificate-v1"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def build_payload(repo_root: Path) -> dict[str, Any]:
    hroot = repo_root / "henon_dynamics"
    sources = {
        "source_henon_pdf": hroot
        / "docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf",
        "c35_theorem_package": hroot
        / "adelic_henon_theta_route/THEOREM_PACKAGE.md",
        "c36_theorem_package": hroot
        / "henon_mellin_parity_obstruction/THEOREM_PACKAGE.md",
        "route_a_evaluator": hroot / "skills/route-a-evaluator.md",
        "candidate_registry": hroot / "docs/candidate_registry.md",
        "obstruction_registry": hroot / "docs/obstruction_registry.md",
    }
    for path in sources.values():
        if not path.is_file():
            raise FileNotFoundError(path)

    # Exact polynomial identities are stored coefficientwise in x^3.
    # d(a;x)=P0(ax)-P0(x)=2(a^3-1)x^3.
    cocycle_lhs = "2*((a*b)^3-1)"
    cocycle_rhs = "2*(a^3-1)*b^3+2*(b^3-1)"
    compatibility_lhs = "2*(a^3-1)*q^3+2*(q^3-1)"
    compatibility_rhs = "2*(q^3-1)*a^3+2*(a^3-1)"

    # Uniform VMO obstruction for n >= 2.  On
    # I_n=[n,n+1/(12n^2)], the rescaled phase equals
    # pi*y + pi*y^2/(12n^3) + pi*y^3/(432n^6).
    error_pi_coefficient_n2 = Fraction(1, 96) + Fraction(1, 27648)
    error_upper = Fraction(22, 7) * error_pi_coefficient_n2
    mean_modulus_upper = Fraction(2, 3) + Fraction(1, 30)
    variance_lower = 1 - mean_modulus_upper * mean_modulus_upper
    if not error_upper < Fraction(1, 30):
        raise AssertionError("VMO error bound failed")
    if mean_modulus_upper != Fraction(7, 10):
        raise AssertionError("mean bound changed")
    if variance_lower != Fraction(51, 100):
        raise AssertionError("variance bound changed")

    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "candidate_id": "HCS-C37",
        "material_passport": {
            "ai_assistance_disclosed": True,
            "artifact_kind": "theorem_and_exact_certificate",
            "evidence_policy": "exact algebra plus an analytic VMO witness; no Riemann zero or prime table",
        },
        "source_lock": {
            key: {
                "path": str(path.relative_to(repo_root)),
                "sha256": sha256_file(path),
            }
            for key, path in sorted(sources.items())
        },
        "conventions": {
            "phase": "P0(x)=2*x^3",
            "henon_map": "H0(q,p)=(-6*q^2-p,q)",
            "chirp": "phi(x)=psi(P0(x)); archimedean phi_R(x)=exp(4*pi*i*x^3)",
            "half_density_dilation": "D_a f(x)=|a|^(1/2) f(a*x)",
            "groupoid_chronology": "later action on the left",
            "poisson_boundary_map": "b0(f)=(f(0), integral(f))",
            "relative_index_convention": "essential codimension Tr(P_K0-P_Ka), equivalently ind(P_Ka restricted to K0)",
        },
        "classical_gate": {
            "jacobian": [[-12, -1], [1, 0]],
            "jacobian_entry_scope": "top-left entry is -12*q",
            "determinant": 1,
            "area_preserving": True,
            "generating_phase_homogeneous_degree": 3,
        },
        "equivariant_coboundary": {
            "increment": "d(a;x)=P0(a*x)-P0(x)=2*(a^3-1)*x^3",
            "cocycle_identity": {
                "lhs_x3_coefficient": cocycle_lhs,
                "rhs_x3_coefficient": cocycle_rhs,
                "expanded_difference": "0",
            },
            "q_star_descent_compatibility": {
                "lhs_x3_coefficient": compatibility_lhs,
                "rhs_x3_coefficient": compatibility_rhs,
                "expanded_difference": "0",
            },
            "twisted_q_action": "q.(x,v)=(q*x,phi(q*x)*phi(x)^(-1)*v)",
            "scaling_lift": "a.(x,v)=(a*x,phi(a*x)*phi(x)^(-1)*v)",
            "simultaneous_gauge": "T(x,v)=(x,phi(x)^(-1)*v)",
            "gauge_transformed_q_action": "q.(x,w)=(q*x,w)",
            "gauge_transformed_scaling_lift": "a.(x,w)=(a*x,w)",
            "groupoid_H1_class": "ZERO",
            "equivariant_line_bundle_class": "TRIVIAL",
        },
        "prime_loop_gate": {
            "r_step_exponent_sum": "sum_(j=0)^(r-1) 2*(p^3-1)*p^(3*j)=2*(p^(3*r)-1)",
            "endpoint_gauge_exponent": "P0(x)-P0(p^r*x)=-2*(p^(3*r)-1)*x^3",
            "closed_gauge_holonomy": 1,
            "all_prime_repetitions": "TRIVIAL_HENON_HOLONOMY",
            "clock_preserved": "ell(C_p)=log(p), inherited from the scaling site",
        },
        "poisson_boundary_pair": {
            "V": "ker(ev_0)",
            "K0": "V intersect ker(Lambda_0)",
            "Ka": "V intersect ker(Lambda_(-P_a))",
            "W": "V intersect ker(Lambda_0) intersect ker(Lambda_(-P_a))",
            "functional_independence_germ": {
                "basis": ["1", "exp(-i*tau*a^3*x^3)"],
                "constant_row": [1, 1],
                "x3_row": [0, "-i*tau*a^3"],
                "determinant": "-i*tau*a^3 != 0 for tau!=0,a>0",
            },
            "dim_K0_mod_W": 1,
            "dim_Ka_mod_W": 1,
            "projection_difference": "P_K0-P_Ka=p_v-p_u is trace class of rank at most 2",
            "essential_codimension": 0,
            "compression_index": "ind(P_Ka|K0)=0",
            "M_phi_preserves_K0": False,
            "intrinsic_quotient_automorphism": "ABSENT",
            "functorial_descended_anomaly": "ZERO_IF_DEFINED",
        },
        "hardy_restricted_gate": {
            "symbol": "phi_R(x)=exp(4*pi*i*x^3)",
            "interval": "I_n=[n,n+1/(12*n^2)]",
            "interval_length_tends_to_zero": True,
            "rescaled_phase_increment": "pi*y+pi*y^2/(12*n^3)+pi*y^3/(432*n^6)",
            "n_scope": "integer n>=2",
            "pi_bounds": "3<pi<22/7",
            "error_pi_coefficient_at_n2": fraction_record(
                error_pi_coefficient_n2
            ),
            "error_upper": fraction_record(error_upper),
            "error_upper_less_than": fraction_record(Fraction(1, 30)),
            "mean_modulus_upper": fraction_record(mean_modulus_upper),
            "l2_mean_oscillation_lower": fraction_record(variance_lower),
            "vmo_status": "NOT_VMO",
            "hardy_commutator_status": "NONCOMPACT_BY_UCHIYAMA_COMPACT_COMMUTATOR_THEOREM",
            "restricted_unitary_status": "NOT_IN_U_RES",
            "toeplitz_determinant_line_from_this_polarization": "UNAVAILABLE",
            "log_scaling_companion": {
                "symbol": "exp(4*pi*i*exp(3*t))",
                "interval": "J_T=[T,T+exp(-3*T)/12]",
                "rescaled_limit": "exp(i*pi*u) uniformly for u in [0,1]",
                "vmo_status": "NOT_VMO",
            },
        },
        "homogeneous_mellin_shadow": {
            "kappa_plus": "(1/3)*(4*pi)^(-z/3)*Gamma(z/3)*exp(i*pi*z/6)",
            "kappa_minus": "(1/3)*(4*pi)^(-z/3)*Gamma(z/3)*exp(-i*pi*z/6)",
            "even_channel": "(2/3)*(4*pi)^(-z/3)*Gamma(z/3)*cos(pi*z/6)",
            "odd_channel": "(2/3)*(4*pi)^(-z/3)*Gamma(z/3)*sin(pi*z/6)",
            "open_strip_zero_or_pole": False,
            "fully_kinematic_normalized_channels": [1, 1],
            "normalized_relative_anomaly": 1,
            "interpretation": "strip safety is exact but the scalar homogeneous increment is gauge transport, not a new determinant",
        },
        "route_a": {
            "tuple": [
                "A1_WEAK",
                "A2_FAIL",
                "A3_PARTIAL_ANALYTIC_STRUCTURE",
                "A4_NATURAL_QUANTIZATION",
            ],
            "overall": "ROUTE_A_REJECTED_FOR_SCALAR_HOMOGENEOUS_ANOMALY",
            "route_b_invocation_allowed": False,
            "decisions": {
                "functorial_poisson_boundary_anomaly": "REFUTED",
                "static_boundary_pair_nonzero_index": "REFUTED",
                "standard_hardy_restricted_index": "REFUTED_AS_UNAVAILABLE",
                "homogeneous_strip_divisor": "SAFE_BUT_TRIVIALIZED",
                "scalar_polynomial_chirp_route": "STOP_SCOPED",
                "next_big_door": "NONSCALAR_Z3_GRADED_KUMMER_TATE_EXTENSION",
            },
        },
        "scope": {
            "proved": [
                "exact equivariant trivialization of the scalar homogeneous chirp lift",
                "trivial holonomy for every scaling-site prime repetition in that lift",
                "zero pre-Poisson relative hyperplane index",
                "failure of the standard Hardy restricted-unitary gate",
            ],
            "not_claimed": [
                "RH or a Hilbert-Polya operator",
                "a no-go for nonscalar graded or projective cocycles",
                "a no-go for every nonfunctorial renormalized quotient",
                "a new proof of the Tate or Connes scaling determinant",
                "a Fredholm theorem for an unspecified polarization",
            ],
            "forbidden_repairs": [
                "declare a coboundary holonomy nontrivial by changing gauge along a closed orbit",
                "call a noncompact Hardy commutator a determinant-class anomaly",
                "import xi and count its divisor as evidence generated by H0",
            ],
        },
    }
    return payload


def make_certificate(repo_root: Path) -> dict[str, Any]:
    payload = build_payload(repo_root)
    return {
        "payload": payload,
        "payload_sha256": hashlib.sha256(canonical_bytes(payload)).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parents[3]
    certificate = make_certificate(repo_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, sort_keys=True, indent=2, ensure_ascii=False)
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
