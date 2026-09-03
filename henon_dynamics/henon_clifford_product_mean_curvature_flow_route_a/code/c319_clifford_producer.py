#!/usr/bin/env python3
"""Produce deterministic receipts for HCS-C319."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c319_clifford_evidence.json"
SOURCE = "1ccbfe2d759fe007c6b53c9646e1ab031878b34a"
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


def frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def dec(x: mp.mpf) -> str:
    return mp.nstr(x, 72, strip_zeros=False)


def harmonic_dimension(d: int, ell: int) -> int:
    if ell == 0:
        return 1
    return math.comb(d + ell, ell) - (math.comb(d + ell - 2, ell - 2) if ell >= 2 else 0)


def branch(p: int, q: int, side: str, slot: int) -> dict:
    n = p + q
    star = Fraction(q, n)
    alpha = Fraction(slot, 4)
    if side == "left":
        y0 = alpha * star
        exp2nt = Fraction(q, q - n * y0)
        collapse = f"S^{p}"
        cylinder = f"S^{q}(sqrt(2*{q})) x R^{p}"
        radius2 = 2 * q
    else:
        y0 = star + alpha * (1 - star)
        exp2nt = Fraction(p, n * y0 - q)
        collapse = f"S^{q}"
        cylinder = f"S^{p}(sqrt(2*{p})) x R^{q}"
        radius2 = 2 * p
    time = mp.log(mp.mpf(exp2nt.numerator) / exp2nt.denominator) / (2 * n)
    h0_num = n * y0 - q
    h0sq = h0_num * h0_num / (y0 * (1 - y0))
    area_ratio = ((mp.mpf(y0.numerator) / y0.denominator) / (mp.mpf(star.numerator) / star.denominator)) ** (mp.mpf(q) / 2)
    area_ratio *= ((1 - mp.mpf(y0.numerator) / y0.denominator) / (1 - mp.mpf(star.numerator) / star.denominator)) ** (mp.mpf(p) / 2)
    return {
        "side": side,
        "slot": slot,
        "y0": frac(y0),
        "exp_2nT": frac(exp2nt),
        "collapse_time": dec(time),
        "collapse_focal_submanifold": collapse,
        "parabolic_cylinder": cylinder,
        "cylinder_radius_squared": radius2,
        "type_I_A2_residue": "1/2",
        "initial_H_squared": frac(h0sq),
        "area_to_minimal_ratio": dec(area_ratio),
    }


def pq_row(p: int, q: int) -> dict:
    n = p + q
    star = Fraction(q, n)
    spectra = []
    negative_count = 0
    nullity = 0
    for ell in range(6):
        for m in range(6):
            lam = Fraction(n * ell * (ell + p - 1), p) + Fraction(n * m * (m + q - 1), q)
            mult = harmonic_dimension(p, ell) * harmonic_dimension(q, m)
            relation = "below_2n" if lam < 2 * n else "equal_2n" if lam == 2 * n else "above_2n"
            if relation == "below_2n":
                negative_count += mult
            elif relation == "equal_2n":
                nullity += mult
            spectra.append({"ell": ell, "m": m, "minus_laplacian_eigenvalue": frac(lam), "multiplicity": mult, "relation": relation})
    return {
        "p": p,
        "q": q,
        "n": n,
        "minimal_y": frac(star),
        "principal_curvature_square_first": frac(Fraction(q, p)),
        "principal_curvature_square_second": frac(Fraction(p, q)),
        "minimal_A_squared": n,
        "jacobi_potential": 2 * n,
        "morse_index": n + 3,
        "nullity": (p + 1) * (q + 1),
        "enumerated_negative_count": negative_count,
        "enumerated_nullity": nullity,
        "branches": [branch(p, q, side, slot) for side in ("left", "right") for slot in (1, 2, 3)],
        "spectrum_cells": spectra,
    }


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C319 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    rows = [pq_row(p, q) for p in range(1, 11) for q in range(1, 11)]
    data = {
        "schema": "hcs-c319-clifford-product-mcf-v1",
        "candidate_id": "HCS-C319",
        "obstruction_id": "HEN-O303",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "family": "S^p(cos(theta)) x S^q(sin(theta)) in the unit S^(p+q+1)",
            "dimensions": "integers p,q>=1",
            "coordinate": "y=sin(theta)^2 in (0,1)",
            "flow_sign": "mean-curvature vector is the negative area gradient",
        },
        "theorem_contract": {
            "reduction": "y'=2*((p+q)*y-q), with the minimal leaf y=q/(p+q)",
            "lifespan": "every nonminimal leaf is ancient and collapses at the exact stated finite forward time",
            "singularity": "both focal collapses are Type I with the stated round-cylinder parabolic limits",
            "area": "area is strictly decreasing off the minimal leaf with logarithmic derivative -H^2",
            "minimal_spectrum": "Jacobi operator is Delta+2n, with index n+3 and nullity (p+1)(q+1)",
        },
        "pq_rows": rows,
        "boundary_atlas": [
            {"face": "p,q>=1", "status": "main smooth hypersurface family"},
            {"face": "y=q/(p+q)", "status": "stationary minimal Clifford product"},
            {"face": "y=0 or y=1", "status": "focal submanifold, not a regular product hypersurface"},
            {"face": "p=0 or q=0", "status": "excluded degenerate sphere/double-cover geometry"},
            {"face": "t=-infinity", "status": "minimal backward limit, not an added finite slice"},
        ],
        "collision_boundary": {
            "C281": "intrinsic homogeneous Ricci flow, not extrinsic spherical mean-curvature flow",
            "C314": "planar curve shortening, not an isoparametric hypersurface flow",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "No priority is claimed for Clifford products, isoparametric mean-curvature flow, or their classical spectra.",
            "No classification beyond the declared two-factor product family is claimed.",
            "The Jacobi operator is source-local and is not a Hilbert--Polya operator.",
            "No target arithmetic local data, Euler factors, root numbers, automorphy, target divisor, functional equation, or target-zero match is asserted.",
        ],
        "references": [
            {"doi": "10.1090/proc/14178", "role": "parallel isoparametric mean-curvature-flow source"},
            {"doi": "10.1215/00127094-2009-009", "role": "isoparametric submanifold flow source"},
        ],
    }
    data["enumeration"] = {
        "pq_rows": len(rows),
        "branch_rows": sum(len(row["branches"]) for row in rows),
        "spectrum_cells": sum(len(row["spectrum_cells"]) for row in rows),
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data) + 1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C319_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
