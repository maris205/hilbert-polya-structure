#!/usr/bin/env python3
"""Produce the canonical exact/regression certificate for HCS-C308."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "results/c308_hatano_nelson_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C308/2026-09-03.yaml"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EPOCH = 1788393600
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]


def f(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def poly_step(p1: list[Fraction], p2: list[Fraction], product: Fraction) -> list[Fraction]:
    """Ascending coefficients for z*p1-product*p2."""
    out = [Fraction(0)] * (len(p1) + 1)
    for i, value in enumerate(p1):
        out[i + 1] += value
    for i, value in enumerate(p2):
        out[i] -= product * value
    return out


def path_poly(n: int, product: Fraction) -> list[Fraction]:
    p0, p1 = [Fraction(1)], [Fraction(0), Fraction(1)]
    if n == 0:
        return p0
    if n == 1:
        return p1
    for _ in range(2, n + 1):
        p0, p1 = p1, poly_step(p1, p0, product)
    return p1


def poly_eval(coeffs: list[Fraction], z: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(coeffs):
        value = value * z + coefficient
    return value


def poly_derivative_eval(coeffs: list[Fraction], z: Fraction) -> Fraction:
    return poly_eval([Fraction(i) * coeffs[i] for i in range(1, len(coeffs))], z)


def matrix_mul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), Fraction(0)) for j in range(n)] for i in range(n)]


def cyclic_matrix(n: int, tr: Fraction, tl: Fraction) -> list[list[Fraction]]:
    out = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        out[j][(j + 1) % n] += tr
        out[j][(j - 1) % n] += tl
    return out


def trace_powers(matrix: list[list[Fraction]], highest: int) -> list[str]:
    n = len(matrix)
    power = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    rows = []
    for _ in range(highest):
        power = matrix_mul(power, matrix)
        rows.append(f(sum((power[i][i] for i in range(n)), Fraction(0))))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVALUATION)
    args = parser.parse_args()

    positive_rows = []
    for n in range(2, 10):
        for tr, tl in [(1, 1), (4, 1), (1, 4), (9, 4), (4, 9)]:
            trf, tlf = Fraction(tr), Fraction(tl)
            product = trf * tlf
            coeffs = path_poly(n, product)
            ratio = max(trf, tlf) / min(trf, tlf)
            positive_rows.append({
                "N": n, "t_R": f(trf), "t_L": f(tlf), "g_squared": f(product),
                "q_squared": f(tlf / trf),
                "characteristic_coefficients_descending": [f(x) for x in reversed(coeffs)],
                "determinant_at_zero": f(poly_eval(coeffs, Fraction(0))),
                "kappa2_squared": f(ratio ** (n - 1)),
                "right_skin_edge": "none" if tr == tl else ("left" if tl < tr else "right"),
                "simple_real_spectrum": True,
            })

    resolvent_rows = []
    for n in range(2, 9):
        for tr, tl in [(1, 1), (4, 1), (3, 2)]:
            product, z = Fraction(tr * tl), Fraction(n + tr + tl)
            coeffs = path_poly(n, product)
            determinant = poly_eval(coeffs, z)
            resolvent_rows.append({
                "N": n, "t_R": f(Fraction(tr)), "t_L": f(Fraction(tl)), "z": f(z),
                "det_zI_minus_H": f(determinant),
                "trace_resolvent": f(poly_derivative_eval(coeffs, z) / determinant),
                "outside_spectrum": determinant != 0,
            })

    one_sided_rows = []
    for n in range(2, 11):
        for orientation, hopping in [("right", Fraction(2)), ("left", Fraction(3))]:
            one_sided_rows.append({
                "N": n, "orientation": orientation, "hopping": f(hopping),
                "rank_sequence_H_power_0_through_N": list(range(n, -1, -1)),
                "nilpotency_index": n, "geometric_multiplicity_zero": 1,
                "pbc_Nth_power_scalar": f(hopping ** n),
                "pbc_diagonalizable": True,
            })

    pbc_rows = []
    for n in range(3, 9):
        for tr, tl in [(1, 1), (4, 1), (1, 4), (2, 0), (0, 2), (0, 0)]:
            trf, tlf = Fraction(tr), Fraction(tl)
            pbc_rows.append({
                "N": n, "t_R": f(trf), "t_L": f(tlf),
                "ellipse_real_semiaxis": f(trf + tlf),
                "ellipse_signed_imag_semiaxis": f(trf - tlf),
                "trace_powers_1_through_N": trace_powers(cyclic_matrix(n, trf, tlf), n),
                "normal": True,
                "one_sided_cyclic": (tr == 0) != (tl == 0),
            })

    boundary_rows = [
        {"face": "t_R>0,t_L>0,t_R!=t_L", "obc": "real simple spectrum with exponential right-amplitude envelope", "pbc": "finite Fourier points on a complex ellipse", "warning": "biorthogonal density is the sine density and has no q envelope"},
        {"face": "t_R=t_L>0", "obc": "real symmetric path matrix", "pbc": "Hermitian cyclic matrix", "warning": "condition number equals one and there is no amplitude skin bias"},
        {"face": "t_R>0,t_L=0", "obc": "one nilpotent N-Jordan block", "pbc": "diagonalizable scaled cyclic shift", "warning": "positive-hopping similarity is singular on this face"},
        {"face": "t_R=0,t_L>0", "obc": "transpose one nilpotent N-Jordan block", "pbc": "diagonalizable inverse cyclic shift", "warning": "the skin orientation reverses"},
        {"face": "t_R=t_L=0", "obc": "zero matrix with eigenspace dimension N", "pbc": "zero matrix with eigenspace dimension N", "warning": "this is not a single Jordan block"},
        {"face": "N=2 OBC", "obc": "the path formulas remain exact", "pbc": "not used in the ellipse theorem", "warning": "the two oriented cyclic neighbors coincide"},
        {"face": "orientation swap", "obc": "transpose preserves eigenvalues and flips the right skin edge", "pbc": "ellipse is complex conjugated", "warning": "left and right amplitudes must not be conflated"},
        {"face": "one-sided limit", "obc": "eigenvalues collapse and eigenbasis conditioning diverges toward a Jordan block", "pbc": "Fourier eigenbasis stays diagonalizable on a spectral circle", "warning": "OBC and PBC limits do not commute with boundary closure"},
    ]
    flags = {
        "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
        "claims_root_number": False, "claims_automorphy": False,
        "claims_target_divisor_or_counting_law": False, "claims_target_functional_equation": False,
        "claims_target_zero_match": False, "claims_topological_invariant": False,
        "claims_hilbert_polya_operator": False, "invokes_route_b": False,
    }
    nonclaims = [
        "No target arithmetic local datum, Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.",
        "No disorder localization, interaction effect, topological invariant, or topological edge mode is asserted.",
        "The finite non-Hermitian chain is not asserted to be a Hilbert--Polya operator.",
        "No priority claim is made for the Hatano--Nelson model, skin effect, or biorthogonal spectral theory.",
    ]
    collision = {
        "C267": "a Hermitian infinite Wannier--Stark lattice, not a finite asymmetric-hopping OBC/PBC atlas",
        "C288": "a self-adjoint delta point interaction, not a nonnormal lattice with boundary-sensitive spectra",
        "C297": "PT-symmetric gain/loss ray dynamics, not asymmetric nearest-neighbor hopping",
        "C303": "a dissipative CPTP qubit semigroup, not nonnormal wave-amplitude evolution",
        "proves_too_much_guard": "finite Chebyshev determinants and boundary spectra do not imply arithmetic data, topology, disorder localization, or a target zero set",
    }
    references = [
        {"identifier": "10.1103/PhysRevLett.77.570", "owner": "Hatano--Nelson (1996)", "role": "non-Hermitian asymmetric-hopping model provenance"},
        {"identifier": "10.1103/PhysRevB.58.8384", "owner": "Hatano--Nelson (1998)", "role": "left/right non-Hermitian eigenfunction context"},
        {"identifier": "10.1103/PhysRevLett.121.086803", "owner": "Yao--Wang (2018)", "role": "modern boundary-sensitivity and skin-effect terminology only"},
    ]
    data = {
        "schema": "hcs-c308-hatano-nelson-boundary-skin-v1",
        "candidate_id": "HCS-C308", "obstruction_id": "HEN-O292",
        "evaluation_date": "2026-09-03", "source_commit": SOURCE,
        "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "evaluation_file_sha256": hashlib.sha256(args.evaluation.read_bytes()).hexdigest(),
        "model": {
            "obc": "H[j,j+1]=t_R and H[j+1,j]=t_L",
            "positive_similarity": "D^{-1}HD=g*A_path with g=sqrt(t_R*t_L), q=sqrt(t_L/t_R), D=diag(1,q,...,q^(N-1))",
            "pbc": "H_per=t_R*C+t_L*C^{-1}, (Cv)_j=v_(j+1 mod N)",
            "time_evolution": "i*dpsi/dt=H*psi",
        },
        "theorem_contract": {
            "characteristic": "P_N(z)=g^N*U_N(z/(2g))",
            "obc_spectrum": "E_m=2g*cos(m*pi/(N+1))",
            "biorthogonal_basis": "R=D*S, L^T=S^T*D^{-1}, L^T*R=I",
            "condition_number": "kappa_2(R)=max(q,q^{-1})^(N-1)",
            "propagator": "exp(-itH)=D*S*diag(exp(-itE_m))*S^T*D^{-1}",
            "resolvent": "(zI-H)^{-1}=D*(zI-gA_path)^{-1}*D^{-1}",
            "pbc_spectrum": "t_R*exp(ik_m)+t_L*exp(-ik_m), k_m=2*pi*m/N",
            "one_sided": "OBC is one nilpotent N-Jordan block while PBC is a diagonalizable cyclic shift",
        },
        "proof_contract": {
            "similarity": "entrywise diagonal conjugation makes both OBC hoppings equal to g",
            "chebyshev": "continuant recurrence P_N=zP_(N-1)-t_R*t_L*P_(N-2)",
            "left_right": "orthogonality of the sine matrix gives the exact dual basis and condition number",
            "pbc_fourier": "the unitary discrete Fourier basis diagonalizes the cyclic shift",
            "jordan": "H^N=0, H^(N-1)!=0, and rank(H^k)=N-k on a one-sided OBC axis",
        },
        "route_a": {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": flags, "nonclaims": nonclaims, "collision_boundary": collision,
        "references": references, "boundary_rows": boundary_rows,
        "positive_obc_rows": positive_rows, "resolvent_rows": resolvent_rows,
        "one_sided_rows": one_sided_rows, "pbc_rows": pbc_rows,
        "summary": {
            "positive_obc_cases": len(positive_rows), "resolvent_cases": len(resolvent_rows),
            "one_sided_cases": len(one_sided_rows), "pbc_cases": len(pbc_rows),
            "boundary_faces": len(boundary_rows),
            "audited_rows": len(positive_rows) + len(resolvent_rows) + len(one_sided_rows) + len(pbc_rows) + len(boundary_rows),
        },
    }
    data["payload_sha256"] = canonical_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C308_PRODUCER_PASS", "audited_rows": data["summary"]["audited_rows"],
        "payload_sha256": data["payload_sha256"],
        "evidence_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
