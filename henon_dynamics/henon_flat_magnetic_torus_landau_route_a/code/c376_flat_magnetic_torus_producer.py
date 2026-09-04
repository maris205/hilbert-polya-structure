#!/usr/bin/env python3
"""Canonical exact evidence producer for HCS-C376."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c376 producer refuses optimized Python")

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c376_flat_magnetic_torus_evidence.json"
EVAL = ROOT / "evaluations/route_a/HCS-C376/2026-09-04.yaml"
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW_SHA = "f1a920fc208186a02d4a5cafcf5cefbb554825699e503b7061dc8b0b29306287"
YAML_SEMANTIC_SHA = "9580d0e0d6fc1664cb701964c8bf5c82db6faecb1ec69c044dd50797f4990915"


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(value) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def frac(value: Fraction):
    return {"numerator": value.numerator, "denominator": value.denominator}


def classical_rows():
    b_values = [Fraction(1, 2), Fraction(2, 3), Fraction(1), Fraction(3, 2)]
    q_values = [
        (Fraction(0), Fraction(0)),
        (Fraction(1, 5), Fraction(1, 7)),
        (Fraction(2, 5), Fraction(3, 7)),
        (Fraction(4, 5), Fraction(6, 7)),
    ]
    p_values = [(Fraction(x), Fraction(y)) for x in (-2, -1, 1, 2) for y in (-2, -1, 1, 2)]
    rows = []
    for b in b_values:
        for qx, qy in q_values:
            for px, py in p_values:
                center = (qx - py / b, qy + px / b)
                quarter_states = []
                for k, (pkx, pky) in enumerate(((px, py), (-py, px), (-px, -py), (py, -px), (px, py))):
                    qkx = center[0] + pky / b
                    qky = center[1] - pkx / b
                    quarter_states.append({
                        "quarter": k,
                        "q_lift": [frac(qkx), frac(qky)],
                        "p": [frac(pkx), frac(pky)],
                        "center": [frac(qkx - pky / b), frac(qky + pkx / b)],
                    })
                rows.append({
                    "abs_B": frac(b),
                    "q0_lift": [frac(qx), frac(qy)],
                    "p0": [frac(px), frac(py)],
                    "energy": frac((px * px + py * py) / 2),
                    "center": [frac(center[0]), frac(center[1])],
                    "least_period_over_pi": frac(2 / b),
                    "quarter_states": quarter_states,
                    "return_derivative": "identity_on_T(T2xR2)",
                })
    assert len(rows) == 256
    return rows


def flux_rows():
    areas = [Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2)]
    rows = []
    for index, n in enumerate(tuple(range(-64, 0)) + tuple(range(1, 65))):
        area = areas[index % len(areas)]
        rows.append({
            "N": n,
            "area": frac(area),
            "B_over_2pi": frac(Fraction(n, 1) / area),
            "chern_integral": n,
            "degree_abs": abs(n),
            "chirality": "positive" if n > 0 else "negative_conjugate",
            "landau_multiplicity": abs(n),
            "flat_holonomy_changes_spectrum": False,
        })
    assert len(rows) == 128
    return rows


def landau_rows():
    rows = []
    for n_flux in tuple(range(-64, 0)) + tuple(range(1, 65)):
        for level in range(129):
            rows.append({
                "N": n_flux,
                "level": level,
                "energy_over_abs_B": frac(Fraction(2 * level + 1, 2)),
                "multiplicity": abs(n_flux),
                "raising_gap_over_abs_B": 1,
            })
    assert len(rows) == 16512
    return rows


def translation_rows():
    rows = []
    for flux_sign in (-1, 1):
        for order in range(1, 65):
            for j in range(order):
                rows.append({
                    "flux_sign": flux_sign,
                    "ordered_positive_division_vectors": ["(Lx/M,0)", "(0,Ly/M)"],
                    "order": order,
                    "basis_index": j,
                    "U_image_index": (j + 1) % order,
                    "V_phase_exponent_mod_order": (-flux_sign * j) % order,
                    "UV_over_VU_phase_exponent_mod_order": flux_sign % order,
                    "U_power_order_is_identity": True,
                    "V_power_order_is_identity": True,
                })
    assert len(rows) == 4160
    return rows


def heat_rows():
    rows = []
    for order in range(1, 65):
        for denominator in range(2, 18):
            q = Fraction(1, denominator)
            rows.append({
                "abs_N": order,
                "q": frac(q),
                "trace_divided_by_sqrt_q": frac(Fraction(order, 1) / (1 - q)),
                "tail_ratio": frac(q),
            })
    assert len(rows) == 1024
    return rows


def determinant_rows():
    rows = []
    for order in range(1, 65):
        rows.append({
            "abs_N": order,
            "zeta_at_zero": 0,
            "zeta_prime_at_zero_log2_coefficient": frac(Fraction(-order, 2)),
            "determinant_base": 2,
            "determinant_exponent": frac(Fraction(order, 2)),
            "independent_of_abs_B": True,
        })
    return rows


def revival_rows():
    rows = []
    for level in range(129):
        rows.append({
            "level": level,
            "phase_at_classical_period": "-1",
            "phase_at_double_period": "+1",
            "relative_phase_exponent_at_scalar_period": level,
            "identity_exponent_at_double_period": 2 * level + 1,
        })
    return rows


BOUNDARY_ROWS = [
    {"case": "B_nonzero_E_positive", "classical": "common least period 2*pi/abs(B)", "quantum": "requires integral flux"},
    {"case": "B_nonzero_E_zero", "classical": "zero-section equilibria", "quantum": "positive lowest Landau energy"},
    {"case": "integral_flux_positive", "classical": "unchanged", "quantum": "degree N line bundle and positive chirality"},
    {"case": "integral_flux_negative", "classical": "opposite orientation", "quantum": "complex-conjugate chirality and abs(N) multiplicity"},
    {"case": "abs_N_one", "classical": "unchanged", "quantum": "one-dimensional magnetic-translation representation"},
    {"case": "nonintegral_flux", "classical": "well-defined twisted flow", "quantum": "no global Hermitian line bundle with stipulated curvature"},
    {
        "case": "B_zero",
        "classical": "q(t)=q0+t*p modulo (Lx*Z direct_sum Ly*Z)",
        "closure_criterion": "there exists t>0 with p_x*t in Lx*Z and p_y*t in Ly*Z",
        "nonaxial_criterion": "p_y*Lx/(p_x*Ly) is rational",
        "x_axis_nonzero": "closed with least period Lx/abs(p_x)",
        "y_axis_nonzero": "closed with least period Ly/abs(p_y)",
        "zero_velocity": "stationary with no positive least period",
        "nonaxial_irrational_normalized_slope": "dense orbit",
        "quantum": "flat-holonomy shifted torus Laplacian; Landau theorem not continued",
    },
]


FLAGS = {
    key: False
    for key in (
        "claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number",
        "claims_automorphy", "claims_target_divisor_or_counting_law",
        "claims_target_functional_equation", "claims_target_zero_match",
        "claims_hilbert_polya_operator", "invokes_route_b",
    )
}


def build():
    raw = EVAL.read_bytes()
    evaluation = yaml.safe_load(raw)
    assert hashlib.sha256(raw).hexdigest() == YAML_RAW_SHA
    assert digest(evaluation) == YAML_SEMANTIC_SHA
    sections = {
        "classical_rows": classical_rows(),
        "flux_rows": flux_rows(),
        "landau_rows": landau_rows(),
        "translation_rows": translation_rows(),
        "heat_rows": heat_rows(),
        "determinant_rows": determinant_rows(),
        "revival_rows": revival_rows(),
        "boundary_rows": BOUNDARY_ROWS,
    }
    evidence = {
        "schema": "hcs-c376-evidence-v1",
        "candidate_id": "HCS-C376",
        "obstruction_id": "HEN-O360",
        "evaluation_date": "2026-09-04",
        "source_commit": SOURCE,
        "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": AUTHORITY_SHA,
        },
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C376/2026-09-04.yaml",
            "raw_sha256": YAML_RAW_SHA,
            "semantic_sha256": YAML_SEMANTIC_SHA,
        },
        "conventions": {
            "torus": "R2/(Lx*Z direct_sum Ly*Z), A=Lx*Ly",
            "classical_symplectic": "dx wedge dp_x + dy wedge dp_y + B dx wedge dy",
            "classical_hamiltonian": "(p_x^2+p_y^2)/2",
            "rotation": "J(px,py)=(-py,px), pdot=B*J*p, center=q+J*p/B",
            "quantum_curvature": "F_nabla=-i*B*dx wedge dy",
            "kinetic_commutator": "[Pi_x,Pi_y]=i*B",
            "quantum_hamiltonian": "H_B=(Pi_x^2+Pi_y^2)/2=(1/2)nabla_star_nabla",
            "magnetic_translation_orientation": "U,V lift the fixed ordered positive vectors (Lx/M,0),(0,Ly/M), so UV=zeta_M^sgn(N)*VU",
            "zeta_determinant": "exp(-zeta_H_prime(0)) over the full positive spectrum",
        },
        "theorem_contract": {
            "classical": "for B nonzero and E positive every orbit has least period 2*pi/abs(B); returns are maximally clean",
            "integrality": "a global curvature line bundle exists iff N=B*A/(2*pi) is an integer",
            "spectrum": "E_n=abs(B)*(n+1/2), each with multiplicity abs(N), independent of flat holonomy",
            "translations": "for fixed ordered positive division vectors each eigenspace carries UV=zeta_M^sgn(N)*VU and the signed order-abs(N) irreducible clock-shift representation",
            "heat": "Tr(exp(-beta*H_B))=abs(N)*exp(-beta*abs(B)/2)/(1-exp(-beta*abs(B)))",
            "zeta": "zeta_H(s)=abs(N)*abs(B)^(-s)*zeta(s,1/2)",
            "determinant": "det_zeta(H_B)=2^(abs(N)/2)",
            "revival": "least scalar time is 2*pi/abs(B) with propagator -I; least identity time is 4*pi/abs(B)",
            "boundaries": "E=0, sign B, abs(N)=1, nonintegral flux, and the exact lattice-normalized B=0 closure faces are separated",
        },
        "finite_grid": {
            "classical_quarter_return_cell_count": 256,
            "flux_case_count": 128,
            "landau_label_cell_count": 16512,
            "translation_basis_cell_count": 4160,
            "heat_cell_count": 1024,
            "determinant_control_count": 64,
            "revival_level_count": 129,
            "boundary_case_count": 7,
        },
        "collision_boundary": {
            "C274": "Penning trap owns confined planar electric-plus-magnetic normal modes, not compact flux bundles",
            "C289": "hyperbolic magnetic flow owns curvature-dependent Anosov and horocycle regimes",
            "C293": "magnetic Grushin owns singular sub-Riemannian separation",
            "C331": "Dirac monopole owns spherical flux and monopole harmonics",
            "C371": "Harper owns lattice Bloch Chambers polynomials",
            "C156": "abstract finite Heisenberg algebra is background only; C376 owns the joint flat-torus theorem",
        },
        "nonclaims": [
            "no global novelty claim beyond this package ownership boundary",
            "no isolated primitive-orbit or arithmetic-prime interpretation of the clean orbit family",
            "no dynamical-zeta interpretation of the Hurwitz spectral zeta",
            "no target arithmetic local data, Euler factors, root number, automorphy, divisor, functional equation, or zero match",
            "no Hilbert-Polya operator and no Route B",
        ],
        "references": [
            {"authors": "M. H. Al-Hashimi and U.-J. Wiese", "title": "Discrete Accidental Symmetry for a Particle in a Constant Magnetic Field on a Torus", "doi": "10.1016/j.aop.2008.07.006", "arxiv": "0807.0630"},
            {"authors": "E. Onofri", "title": "Landau levels on a torus", "journal": "International Journal of Theoretical Physics 40 (2001), 537-549", "doi": "10.1023/A:1004115827959", "arxiv": "quant-ph/0007055"},
            {"authors": "I. Burban and S. Klevtsov", "title": "Algebraic Geometry of the Multilayer Model of the Fractional Quantum Hall Effect on a Torus", "doi": "10.1007/s00220-025-05267-9", "normalization_warning": "its holomorphic ground-space convention is not substituted for the physical Bochner half-shift"},
        ],
        "scope_flags": FLAGS,
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "theorem_status": "PROVABLE_AS_STATED",
        },
        "finite_evidence_role": "exact regression receipt only; analytic proofs establish every theorem",
        **sections,
        "section_sha256": {name: digest(value) for name, value in sections.items()},
    }
    evidence["payload_sha256"] = digest(evidence)
    return evidence


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args()
    value = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False).encode() + b"\n")
    print(
        "C376 producer PASS: classical=256 landau=16512 translations=4160 "
        "heat=1024 determinant=64 payload=" + value["payload_sha256"]
    )


if __name__ == "__main__":
    main()
