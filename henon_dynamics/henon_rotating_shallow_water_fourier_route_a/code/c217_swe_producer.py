#!/usr/bin/env python3
"""Produce the deterministic C217 rotating shallow-water certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import math
import os
from pathlib import Path

import numpy as np
from scipy.linalg import expm

SOURCE_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c217_swe_evidence.json"
MODES = [(i, j) for i in range(-3, 4) for j in range(-3, 4)]
CASES = [
    ("balanced", Fraction(1), Fraction(1)),
    ("fast_rotation", Fraction(2), Fraction(1)),
    ("fast_gravity", Fraction(1), Fraction(2)),
    ("anisotropic_rates", Fraction(3, 2), Fraction(5, 4)),
    ("zero_rotation", Fraction(0), Fraction(1)),
    ("zero_gravity", Fraction(1), Fraction(0)),
    ("fully_zero", Fraction(0), Fraction(0)),
    ("retrograde_rotation", Fraction(-1), Fraction(1)),
]
TIMES = (1.0 / 7.0, 1.0)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def ffloat(q: Fraction) -> float:
    return q.numerator / q.denominator


def cfmt(z: complex) -> str:
    # Fixed significant digits make replay independent of locale.
    return format(float(z), ".17g")


def mat(f: float, c: float, n: tuple[int, int]) -> np.ndarray:
    nx, ny = n
    return np.array([
        [0.0, f, -1j * c * nx],
        [-f, 0.0, -1j * c * ny],
        [-1j * c * nx, -1j * c * ny, 0.0],
    ], dtype=np.complex128)


def shell_count(q: int) -> int:
    return sum(1 for i, j in ((i, j) for i in range(-20, 21) for j in range(-20, 21))
               if i * i + j * j == q)


def divisor_shell_count(q: int) -> int:
    if q == 0:
        return 1
    d1 = sum(1 for d in range(1, q + 1) if q % d == 0 and d % 4 == 1)
    d3 = sum(1 for d in range(1, q + 1) if q % d == 0 and d % 4 == 3)
    return 4 * (d1 - d3)


def mode_record(f: float, c: float, n: tuple[int, int]) -> dict:
    G = mat(f, c, n)
    rho = n[0] * n[0] + n[1] * n[1]
    omega = math.sqrt(f * f + c * c * rho)
    skew = np.linalg.norm(G.conj().T + G)
    cubic = np.linalg.norm(np.linalg.matrix_power(G, 3) + omega * omega * G)
    if abs(c) > 1e-14:
        qrow = np.array([-1j*n[1], 1j*n[0], -f/c], dtype=complex)
        pv_residual = np.linalg.norm(qrow @ G)
    else:
        pv_residual = 0.0
    if omega > 1e-14:
        P0 = np.eye(3, dtype=complex) + (G @ G) / (omega * omega)
        Pp = 0.5 * (-G @ G / (omega * omega) - 1j * G / omega)
        Pm = 0.5 * (-G @ G / (omega * omega) + 1j * G / omega)
        proj = max(np.linalg.norm(P0 @ P0 - P0),
                   np.linalg.norm(Pp @ Pp - Pp),
                   np.linalg.norm(Pm @ Pm - Pm),
                   np.linalg.norm(P0 @ Pp), np.linalg.norm(Pp @ Pm),
                   np.linalg.norm(P0 + Pp + Pm - np.eye(3)))
        rank_zero = int(round(np.linalg.matrix_rank(P0, tol=1e-9)))
        trows = []
        for t in TIMES:
            closed = P0 + math.cos(omega * t) * (np.eye(3) - P0) + math.sin(omega * t) / omega * G
            direct = expm(t * G)
            trows.append({
                "t": cfmt(t),
                "formula_residual": cfmt(np.linalg.norm(closed - direct)),
                "unitarity_residual": cfmt(np.linalg.norm(direct.conj().T @ direct - np.eye(3))),
            })
    else:
        proj = 0.0
        rank_zero = 3
        trows = [{"t": cfmt(t), "formula_residual": "0.0", "unitarity_residual": "0.0"} for t in TIMES]
    return {
        "n": [n[0], n[1]],
        "rho": rho,
        "omega": cfmt(omega),
        "skew_residual": cfmt(skew),
        "cubic_residual": cfmt(cubic),
        "pv_residual": cfmt(pv_residual),
        "projector_residual": cfmt(proj),
        "zero_projector_rank": rank_zero,
        "times": trows,
    }


def build() -> dict:
    rows = []
    for case_id, fq, cq in CASES:
        f, c = ffloat(fq), ffloat(cq)
        modes = [mode_record(f, c, n) for n in MODES]
        rows.append({
            "case_id": case_id,
            "f": str(fq),
            "c": str(cq),
            "mode_count": len(modes),
            "modes": modes,
            "shell_counts": [{"q": q, "enumerated": shell_count(q), "formula": divisor_shell_count(q)}
                             for q in range(0, 19)],
        })
    data = {
        "schema": "hcs-c217-rotating-shallow-water-v1",
        "candidate_id": "HCS-C217",
        "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": "Constant-f rotating shallow-water flow has an exact lattice-mode projector atlas, finite-support periodicity criterion, and sharp unitary noncompactness boundary.",
        "frozen_object": {
            "system": "u_t+f J u+c grad(phi)=0; phi_t+c div(u)=0 on T^2_{2pi}",
            "clock": "physical continuous time t",
            "energy": "||u||_L2^2+||phi||_L2^2",
            "Fourier_block": "G_n=[[-fJ,-i c n],[-i c n^T,0]]",
            "parameters": "real f and c>=0; boundary faces f=0,c=0,n=0 retained",
            "forbidden_data": "beta-plane Rossby claims, target primes/zeros, local arithmetic, Euler factors, root numbers, automorphy, Hilbert-Polya operators",
        },
        "theorem": {
            "minimal_polynomial": "G_n^3+(f^2+c^2|n|^2)G_n=0",
            "frequency": "omega_n=sqrt(f^2+c^2|n|^2)",
            "projectors": "P0=I+G^2/omega^2; P+=(-G^2/omega^2-iG/omega)/2; P-=(-G^2/omega^2+iG/omega)/2",
            "exponential": "exp(tG)=P0+cos(omega t)(I-P0)+sin(omega t)G/omega",
            "branches": "zero geostrophic/PV branch and plus/minus inertia-gravity branches",
            "shell_multiplicity": "r2(q)=4(d1(q)-d3(q)); q=|n|^2",
            "periodicity": "finite Fourier support is T-periodic iff omega_n*T is in 2*pi*Z for every participating nonzero branch",
            "operator_boundary": "global group is unitary and, for every t including t=0, is neither compact nor Schatten",
            "pv_invariant": "for c>0, qhat_n=(-i n_y, i n_x, -f/c) dot (u1hat,u2hat,phihat) is stationary",
            "degenerate_faces": "n=0 has 0, plus/minus i|f| when f != 0; f=0,c=0 gives the full zero block",
        },
        "regression": {
            "cases": rows,
            "case_count": len(rows),
            "modes_per_case": len(MODES),
            "shells_per_case": 19,
            "times": [cfmt(t) for t in TIMES],
            "working_precision": "float64 cross-check plus exact integer shell ledger",
        },
        "exact_identities": [
            {"name": "skew_hermitian", "formula": "G_n^*+G_n=0"},
            {"name": "cubic", "formula": "G_n^3+(f^2+c^2|n|^2)G_n=0"},
            {"name": "projector_sum", "formula": "P0+P++P-=I when omega>0"},
            {"name": "projector_orthogonality", "formula": "Pi Pj=delta_ij Pj"},
            {"name": "shell_formula", "formula": "r2(q)=4(d1(q)-d3(q))"},
            {"name": "energy", "formula": "d/dt (||u||^2+||phi||^2)=0"},
            {"name": "linear_pv", "formula": "zeta_t=-(f) div u and phi_t=-(c) div u, hence (zeta-(f/c)phi)_t=0 for c>0"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "A source-native skew-Hermitian Fourier PDE admits a complete same-clock projector and shell atlas.",
            "strongest_failure": "The lattice is a spatial Fourier index, not an arithmetic primitive-orbit owner, and no target determinant is present.",
        },
        "scope_flags": {
            "uses_target_zero_table": False,
            "uses_prime_table": False,
            "claims_arithmetic_local_data": False,
            "claims_euler_factors": False,
            "claims_root_numbers": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {"key": "MohebalhojehDritschel2001", "claim": "f-plane doubly-periodic shallow-water normal-mode context", "title": "Hierarchies of Balance Conditions for the f-Plane Shallow-Water Equations", "authors": "A. R. Mohebalhojeh and D. G. Dritschel", "venue": "Journal of the Atmospheric Sciences", "year": 2001, "doi": "10.1175/1520-0469(2001)058<2411:HOBCFT>2.0.CO;2"},
            {"key": "Salmon1988", "claim": "Hamiltonian projection context", "title": "Semigeostrophic theory as a Dirac-bracket projection", "authors": "R. Salmon", "venue": "Journal of Fluid Mechanics", "year": 1988, "doi": "10.1017/S0022112088002733"},
        ],
        "nonclaims": [
            "no beta-plane or Rossby-wave conclusion",
            "no target prime/zero law, Euler factor, root number, automorphy, functional equation, or Hilbert-Polya operator",
            "no claim that the Fourier shell index is an arithmetic primitive owner",
            "no target compactness or trace-class promotion beyond the stated source-local noncompact/non-Schatten theorem",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(os.environ.get("C217_OUTPUT", DEFAULT_OUTPUT)))
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C217 producer: wrote {args.output}")


if __name__ == "__main__":
    main()
