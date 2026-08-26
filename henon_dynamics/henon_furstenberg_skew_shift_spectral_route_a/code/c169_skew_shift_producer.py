#!/usr/bin/env python3
"""Produce the exact HCS-C169 Furstenberg skew-shift certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c169_skew_shift_evidence.json"
SOURCE_COMMIT = "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f"
N_MAX = 32
M_MAX = 12
FOURIER_K_MAX = 8
SECTOR_K_MAX = 12


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    iterate_rows = []
    for n in range(1, N_MAX + 1):
        iterate_rows.append({
            "n": n,
            "x_coefficient_x": 1,
            "x_coefficient_alpha": n,
            "y_coefficient_y": 1,
            "y_coefficient_x": n,
            "y_coefficient_alpha": comb(n, 2),
            "fixed_points": 0,
        })

    fourier_rows = []
    for k in range(-FOURIER_K_MAX, FOURIER_K_MAX + 1):
        for m in range(-M_MAX, M_MAX + 1):
            fourier_rows.append({
                "m": m,
                "k": k,
                "phase_alpha_coefficient": m,
                "output_m": m + k,
                "output_k": k,
                "sector": "pure_point" if k == 0 else "lebesgue_shift",
            })

    sector_rows = []
    for k in list(range(-SECTOR_K_MAX, 0)) + list(range(1, SECTOR_K_MAX + 1)):
        residues = list(range(abs(k)))
        sector_rows.append({
            "k": k,
            "residues_mod_abs_k": residues,
            "bilateral_shift_copies": abs(k),
            "spectral_type": "Lebesgue",
        })

    data = {
        "schema": "HCS-C169-v1",
        "candidate_id": "HCS-C169",
        "date_utc": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "Furstenberg skew shift T_alpha(x,y)=(x+alpha,y+x) on the two-torus",
            "family": "every irrational alpha modulo one",
            "arithmetic_origin": "none; alpha is an arbitrary irrational source parameter and no prime or prime-power structure is intrinsic",
            "clock": "one application of T_alpha",
            "normalization": "normalized Haar measure and Fourier basis e_(m,k)=exp(2*pi*i*(m*x+k*y))",
            "determinant_convention": "Artin--Mazur zeta from finite fixed-point counts; ordinary Fredholm determinant only when defined",
            "cutoff": "all-parameter proof; finite exact regression uses n<=32, |m|<=12 and |k|<=8 on the Fourier grid, plus 0<|k|<=12 in the sector sentinel",
            "precision": "exact integer affine coefficients and formal irrational alpha",
            "allowed_data": "the frozen toral affine map and source-derived Fourier indices",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
        },
        "iterate_theorem": {
            "formula": "T_alpha^n(x,y)=(x+n*alpha, y+n*x+binom(n,2)*alpha) mod 1 for every n>=1",
            "fixed_point_obstruction": "a fixed point of T_alpha^n would force n*alpha=0 mod 1, impossible for irrational alpha",
            "fixed_counts": "#Fix(T_alpha^n)=0 for every n>=1",
            "artin_mazur_zeta": "zeta_AM(z)=exp(sum_(n>=1) #Fix(T^n) z^n/n)=1",
        },
        "haar_and_fourier_theorem": {
            "haar": "T_alpha is an invertible determinant-one affine toral map and preserves normalized Haar measure",
            "koopman_convention": "U f=f after T_alpha",
            "basis_action": "U e_(m,k)=exp(2*pi*i*m*alpha)e_(m+k,k)",
            "pure_point_sector": "k=0 is spanned by eigenvectors e_(m,0) with eigenvalues exp(2*pi*i*m*alpha)",
            "shift_sectors": "for k!=0, residues m mod |k| give |k| invariant weighted bilateral shifts, each unitarily equivalent to the bilateral shift",
            "global_spectrum": "the orthogonal complement of k=0 has Lebesgue spectrum of countably infinite multiplicity",
        },
        "reversibility_and_operator_boundary": {
            "reversor": "R(x,y)=(alpha-x,y) mod 1 is involutive and R*T_alpha*R=T_alpha^(-1)",
            "antiunitary": "Theta f=conjugate(f after R) is involutive and Theta*U*Theta=U^(-1)",
            "unitary": "U is the same-clock Haar Koopman unitary",
            "noncompact": "U maps a Fourier orthonormal basis bijectively to another orthonormal basis and is not compact",
            "schatten": "U belongs to no finite Schatten class",
            "fredholm_boundary": "zU is not trace class for z!=0, so the ordinary Fredholm determinant det(I-zU) is unavailable",
        },
        "finite_replay": {
            "n_max": N_MAX,
            "m_max": M_MAX,
            "fourier_k_max": FOURIER_K_MAX,
            "sector_k_max": SECTOR_K_MAX,
            "iterate_rows": iterate_rows,
            "fourier_rows": fourier_rows,
            "sector_rows": sector_rows,
            "iterate_cell_count": len(iterate_rows),
            "fourier_cell_count": len(fourier_rows),
            "sector_cell_count": len(sector_rows),
        },
        "progress_and_boundary": {
            "progress": "proves an all-irrational-parameter iterate law, empty periodic ledger, complete Fourier-sector spectral decomposition, exact reversor, and sharp determinant obstruction",
            "route_a_obstruction": "the empty periodic data make zeta_AM=1; there is no primitive-orbit carrier, target divisor comparison, or target global analytic comparison",
            "sentinel_boundary": "finite rows only regression-test formulas proved symbolically; they do not establish irrationality or extrapolate the theorem",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "A0_qualification": "NO_INTRINSIC_ARITHMETIC_ORIGIN_OR_PRIME_CORRESPONDENCE",
            "A1_qualification": "ALL_POSITIVE_FIXED_SETS_EMPTY_SO_NO_PRIMITIVE_PERIODIC_ORBITS",
            "A2_qualification": "TRIVIAL_SOURCE_ARTIN_MAZUR_ZETA_WITH_NO_TARGET_DIVISOR",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4_qualification": "SAME_CLOCK_HAAR_KOOPMAN_UNITARY_WITH_EXPLICIT_ANTIUNITARY_REVERSAL",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "used_arithmetic_local_data": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_hilbert_polya": False,
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "prime-like primitive orbits from an empty periodic ledger",
            "an ordinary Fredholm determinant for the non-trace-class Koopman operator",
            "a target divisor, functional equation, counting law, or continuation match",
            "arithmetic local factors, Euler factors, root numbers, or automorphy",
            "a Hilbert--Polya operator, Route-B authorization, novelty priority, or external peer review",
        ],
    }
    data["payload_sha256"] = sha256(canonical_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C169_PRODUCER_PASS",
        "iterate_rows": len(data["finite_replay"]["iterate_rows"]),
        "fourier_rows": len(data["finite_replay"]["fourier_rows"]),
        "sector_rows": len(data["finite_replay"]["sector_rows"]),
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
