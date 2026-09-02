#!/usr/bin/env python3
"""Produce the deterministic HCS-C284 Thomson-polygon certificate."""
from __future__ import annotations

import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get(
    "C284_EVIDENCE_OUT", ROOT / "results/c284_point_vortex_evidence.json"
))
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
N_MIN, N_MAX = 3, 64


def qstr(value: Q) -> str:
    return f"{value.numerator}/{value.denominator}"


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(
        clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def block_regime(m: int, q: int, s: int) -> str:
    if m == 0:
        return "rotation_scale_jordan"
    if s > 0:
        return "elliptic"
    if s == 0:
        return "linear_degenerate_nilpotent"
    return "hyperbolic"


def block_rows() -> list[dict]:
    rows: list[dict] = []
    for n in range(N_MIN, N_MAX + 1):
        for m in range(n):
            q = m * (n - m)
            s = 2 * (n - 1) - q
            regime = block_regime(m, q, s)
            if m == 0:
                spectral_pair = "zero_double_nonsemisimple"
                role = "uniform_rotation_and_scale_generalized_mode"
            elif m in (1, n - 1):
                spectral_pair = f"plus_minus_i_sqrt_{q * s}_times_c"
                role = "first_harmonic_translation_isotypic_and_centered_elliptic_complement"
            elif s > 0:
                spectral_pair = f"plus_minus_i_sqrt_{q * s}_times_c"
                role = "shape_mode"
            elif s == 0:
                spectral_pair = "zero_double_nonsemisimple"
                role = "shape_mode"
            else:
                spectral_pair = f"plus_minus_sqrt_{q * (-s)}_times_c"
                role = "shape_mode"
            rows.append({
                "n": n,
                "mode": m,
                "conjugate_mode": (-m) % n,
                "q_m": q,
                "radial_hessian_over_c": s,
                "tangential_hessian_over_c": q,
                "det_hessian_over_c2": q * s,
                "lambda_squared_over_c2": -q * s,
                "regime": regime,
                "reduced_role": role,
                "spectral_pair": spectral_pair,
            })
    return rows


def polygon_rows() -> list[dict]:
    rows: list[dict] = []
    for n in range(N_MIN, N_MAX + 1):
        modes = list(range(n))
        q_values = [m * (n - m) for m in modes]
        s_values = [2 * (n - 1) - q for q in q_values]
        degenerate = [m for m in modes if m != 0 and s_values[m] == 0]
        hyperbolic = [m for m in modes if s_values[m] < 0]
        if n <= 6:
            classification = "reduced_linearly_elliptic"
        elif n == 7:
            classification = "reduced_linearly_degenerate_not_a_nonlinear_claim"
        else:
            classification = "reduced_linearly_hyperbolic_unstable"
        rows.append({
            "n": n,
            "omega_over_c": n - 1,
            "max_q": max(q_values),
            "min_stability_sign": min(s_values),
            "degenerate_modes": degenerate,
            "hyperbolic_modes": hyperbolic,
            "hyperbolic_mode_count": len(hyperbolic),
            "classification": classification,
        })
    return rows


def scale_rows() -> list[dict]:
    rows: list[dict] = []
    for n in (3, 7, 8, 16):
        for gamma in (Q(1, 2), Q(1), Q(2), Q(5)):
            for radius in (Q(1, 2), Q(1), Q(2), Q(4)):
                four_pi_c = gamma / (radius * radius)
                rows.append({
                    "n": n,
                    "gamma": qstr(gamma),
                    "radius": qstr(radius),
                    "four_pi_c": qstr(four_pi_c),
                    "four_pi_omega": qstr((n - 1) * four_pi_c),
                    "stability_class_invariant_under_scale": True,
                })
    return rows


def slice_rows() -> list[dict]:
    """Exact dimension and frequency ledger for the reduced symmetry slice."""
    rows: list[dict] = []
    for n in (3, 4, 6, 7, 8, 16, 64):
        rows.append({
            "n": n,
            "total_dimension": 2 * n,
            "centered_dimension": 2 * n - 2,
            "fixed_impulse_tangent_dimension": 2 * n - 3,
            "reduced_dimension": 2 * n - 4,
            "uniform_mode_removed_dimension": 2,
            "first_harmonic_real_dimension": 4,
            "translation_plane_dimension": 2,
            "centered_first_harmonic_dimension": 2,
            "centered_first_harmonic_frequency_over_c": n - 1,
            "m0_restriction": "removed_by_fixed_impulse_and_rotation",
            "first_harmonic_restriction": (
                "translation_plane_removed_centered_complement_elliptic"
            ),
        })
    return rows


def boundary_rows() -> list[dict]:
    return [
        {
            "face": "n_below_domain",
            "condition": "N<3",
            "status": "excluded; N=1 is trivial and the centered N=2 polygon has no reduced shape degree of freedom",
        },
        {
            "face": "collision",
            "condition": "R=0",
            "status": "excluded logarithmic collision singularity",
        },
        {
            "face": "zero_circulation",
            "condition": "Gamma=0",
            "status": "the weighted symplectic form degenerates; only the zero-velocity limit is recorded",
        },
        {
            "face": "negative_common_circulation",
            "condition": "Gamma<0",
            "status": "time reversal of the positive-circulation convention; stability signs are unchanged",
        },
        {
            "face": "uniform_mode",
            "condition": "m=0",
            "status": "rotation kernel plus scale generalized vector; removed by fixed angular impulse and rotation quotient",
        },
        {
            "face": "first_harmonic",
            "condition": "m=1,N-1",
            "status": "contains the translation plane; after centering, its complementary plane remains elliptic with frequency Omega",
        },
        {
            "face": "heptagon",
            "condition": "N=7,m=3,4",
            "status": "nonzero nilpotent linear blocks; linear degeneracy only and no nonlinear-stability claim",
        },
        {
            "face": "large_radius",
            "condition": "R tends to infinity",
            "status": "all frequencies scale as Gamma/(4*pi*R^2) and tend to zero without changing the sign atlas",
        },
    ]


def main() -> None:
    regression = {
        "block_rows": block_rows(),
        "polygon_rows": polygon_rows(),
        "scale_rows": scale_rows(),
        "slice_rows": slice_rows(),
        "boundary_rows": boundary_rows(),
    }
    regression["counts"] = {
        name: len(rows) for name, rows in regression.items()
    }
    data = {
        "schema": "hcs-c284-thomson-polygon-point-vortex-stability-v1",
        "candidate_id": "HCS-C284",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": (
            "The equal positive point-vortex regular N-gon admits a complete "
            "Cartesian-Hessian/DFT block atlas: N=3..6 is reduced linearly "
            "elliptic, N=7 is linearly degenerate in modes 3 and 4 only, "
            "and every N>=8 has a real hyperbolic pair."
        ),
        "evaluator": {"version": "0.2.0", "sha256": EVAL},
        "audit_contract": {
            "json_policy": (
                "reject duplicate keys, unknown keys, missing keys, nonstandard "
                "constants, and bool-as-int type confusion"
            ),
            "row_policy": (
                "exact key sets, exact types, complete ordered coverage, and "
                "unique semantic keys"
            ),
            "slice_policy": (
                "raw Cartesian Hessian independently checks the m=0 "
                "rotation-scale chain and first-harmonic translation/complement "
                "subspaces"
            ),
        },
        "model_contract": {
            "hamiltonian": "H=-(Gamma^2/(2*pi))*sum_{j<k} log|z_j-z_k|",
            "symplectic_equation": "Gamma*z_j_dot=J*grad_j(H), J=[[0,1],[-1,0]]",
            "polygon": "z_j=R*(cos(2*pi*j/N),sin(2*pi*j/N)), N>=3, Gamma>0, R>0",
            "angular_velocity": "Omega=Gamma*(N-1)/(4*pi*R^2)",
            "augmented_hamiltonian": "G=H+(Gamma*Omega/2)*sum_j |z_j|^2",
            "clock": "physical point-vortex time",
            "scale": "c=Gamma/(4*pi*R^2)",
        },
        "block_contract": {
            "local_dft": "radial-tangential unitary DFT in modes m=0,...,N-1",
            "root_sum": "S_m=sum_{k=1}^{N-1}(1-cos(m*theta_k))/(1-cos(theta_k))=m*(N-m)",
            "hessian_block": "Gamma^(-1)*D^2G_hat_m=c*diag(2*(N-1)-q_m,q_m), q_m=m*(N-m)",
            "linear_block": "L_m=c*[[0,q_m],[-(2*(N-1)-q_m),0]]",
            "square": "L_m^2=-c^2*q_m*(2*(N-1)-q_m)*I",
        },
        "reduction_contract": {
            "center": "fix center of vorticity at zero, removing the physical translation plane inside the first harmonic",
            "rotation_scale": "fix angular impulse and quotient rotations, removing the m=0 scale-rotation Jordan block",
            "first_harmonic_remainder": "the centered complementary first-harmonic plane is elliptic because its Hessian block is c*(N-1)*I",
            "classification": "all remaining signs are governed by 2*(N-1)-m*(N-m)",
        },
        "proof_contract": {
            "status": "PROVABLE AS STATED",
            "dependencies": [
                "direct Cartesian pair-Hessian differentiation",
                "cyclic root-of-unity orthogonality",
                "radial-tangential DFT block diagonalization",
                "Hamiltonian two-by-two spectral classification",
                "explicit symmetry-slice vectors and invariant-subspace residuals",
            ],
            "scope": "equal nonzero point vortices on one finite-radius regular polygon; linearized reduced stability only",
            "heptagon_boundary": "N=7 is asserted only to be linearly degenerate in m=3,4; nonlinear stability is not claimed",
            "novelty_boundary": "classical owner results are reconstructed and executable; no literature-priority claim is made",
        },
        "source_owner_contract": {
            "classical_owner": "J. J. Thomson, A Treatise on the Motion of Vortex Rings (1883)",
            "linear_stability_owner_doi": "10.1080/14786443109461714",
            "later_stability_context_doi": "10.1137/S0036141098302124",
            "polygonal_relative_equilibrium_doi": "10.1063/1.3646115",
            "use_boundary": "sources establish lineage and classical ownership; every displayed proof and executable count is reconstructed in-package",
        },
        "analytic_proof_obligations": [
            "derive Omega directly from the source Hamiltonian",
            "differentiate the raw Cartesian pair Hessian and add the rotating-frame term",
            "derive every DFT block and prove the root-sum identity",
            "separate rotation, scale, translation, and centered first-harmonic directions",
            "verify symmetry-slice dimensions and invariant subspaces from the raw Hessian",
            "prove the N<=6, N=7, and N>=8 sign trichotomy",
            "keep Gamma=0, R=0, N<3, and N=7 nonlinear stability outside the claim",
        ],
        "regression": regression,
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "target_divisor_or_counting_law": False,
            "target_functional_equation": False,
            "target_zero_match": False,
            "hilbert_polya_operator": False,
            "route_b_authorization": False,
        },
        "nonclaims": [
            "No nonlinear stability theorem is claimed for the Thomson heptagon.",
            "No finite N-table is used as a proof of the all-N theorem.",
            "No rational-prime carrier, logarithmic-prime clock, target determinant, or target zero match is obtained.",
            "A single relative-equilibrium family is not a primitive-orbit census.",
            "The package does not claim invention or literature priority for the classical polygon theorem.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C284_PRODUCER_PASS",
        "counts": regression["counts"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
