#!/usr/bin/env python3
"""Exact producer for HCS-C43.

The released finite-field calculations use FLINT.  No floating-point
eigenvalue computation enters the certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from flint import fmpz_mod_ctx, fmpz_mod_mat


SCHEMA = "hcs-c43-certificate-v1"
CONTROL_PRIMES = (7, 13, 19, 31, 37, 43, 61, 67, 73)


def is_prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_factors(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    assert is_prime(p)
    factors = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise AssertionError("primitive root not found")


def auxiliary_prime(p: int) -> int:
    k = 1
    while True:
        ell = 3 * p * k + 1
        if is_prime(ell):
            return ell
        k += 1


def canonical_json(obj: Any) -> bytes:
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def matrix_rows(mat: fmpz_mod_mat) -> list[list[int]]:
    return [[int(mat[i, j]) for j in range(mat.ncols())] for i in range(mat.nrows())]


def permutation_matrix(p: int, zeta: int, inverse_power: int, ctx: Any) -> fmpz_mod_mat:
    """Matrix f(x) -> f(zeta^{-inverse_power} x)."""
    zin = pow(zeta, -inverse_power, p)
    rows = []
    for x in range(p):
        y = (zin * x) % p
        rows.append([1 if q == y else 0 for q in range(p)])
    return fmpz_mod_mat(rows, ctx)


def orbit_representatives(p: int, zeta: int) -> list[int]:
    unseen = set(range(1, p))
    reps: list[int] = []
    while unseen:
        a = min(unseen)
        orbit = [a, (zeta * a) % p, (zeta * zeta * a) % p]
        assert len(set(orbit)) == 3
        reps.append(a)
        unseen.difference_update(orbit)
    return reps


def sector_basis_and_left_inverse(
    p: int, ell: int, zeta: int, omega: int, k: int, ctx: Any
) -> tuple[fmpz_mod_mat, fmpz_mod_mat]:
    reps = orbit_representatives(p, zeta)
    columns: list[list[int]] = []
    selectors: list[int] = []
    if k == 0:
        delta = [0] * p
        delta[0] = 1
        columns.append(delta)
        selectors.append(0)
    for a in reps:
        col = [0] * p
        x = a
        for j in range(3):
            col[x] = pow(omega, (k * j) % 3, ell)
            x = (zeta * x) % p
        columns.append(col)
        selectors.append(a)
    d = len(columns)
    basis = fmpz_mod_mat(
        [[columns[j][i] for j in range(d)] for i in range(p)], ctx
    )
    left = fmpz_mod_mat(
        [[1 if j == x else 0 for j in range(p)] for x in selectors], ctx
    )
    assert left * basis == fmpz_mod_mat(d, d, [1 if i == j else 0 for i in range(d) for j in range(d)], ctx)
    return basis, left


def polynomial_coefficients(poly: Any) -> list[int]:
    return [int(poly[i]) for i in range(len(poly))]


def build_control(p: int) -> dict[str, Any]:
    assert is_prime(p) and p > 3 and p % 3 == 1
    ell = auxiliary_prime(p)
    gen_p = primitive_root(p)
    gen_ell = primitive_root(ell)
    zeta = pow(gen_p, (p - 1) // 3, p)
    eta = pow(gen_ell, (ell - 1) // p, ell)
    omega = pow(gen_ell, (ell - 1) // 3, ell)
    ctx = fmpz_mod_ctx(ell)

    kernel_rows = [
        [pow(eta, (q * Q + 2 * q * q * q) % p, ell) for q in range(p)]
        for Q in range(p)
    ]
    kernel = fmpz_mod_mat(kernel_rows, ctx)
    # R f(x)=f(zeta*x).  Since zeta^3=1 this is inverse_power=2.
    R = permutation_matrix(p, zeta, 2, ctx)
    Rinv = permutation_matrix(p, zeta, 1, ctx)
    assert kernel * R == Rinv * kernel

    T = (kernel * kernel) * pow(p, -1, ell)
    assert T * R == R * T

    sector_polys = []
    sector_dims = []
    sector_determinants = []
    for k in range(3):
        basis, left = sector_basis_and_left_inverse(p, ell, zeta, omega, k, ctx)
        assert R * basis == basis * pow(omega, k, ell)
        block = left * T * basis
        # The restricted image must reconstruct exactly.
        assert T * basis == basis * block
        poly = block.charpoly()
        sector_dims.append(block.nrows())
        sector_polys.append(poly)
        determinant = ((-1) ** block.nrows() * int(poly[0])) % ell
        sector_determinants.append(determinant)

    assert sector_polys[1] == sector_polys[2]
    gcd01 = sector_polys[0].gcd(sector_polys[1])
    assert polynomial_coefficients(gcd01) == [1]
    expected_det = 1 if ((p - 1) // 6) % 2 == 0 else ell - 1
    assert sector_determinants == [expected_det] * 3

    d0, d1, d2 = sector_dims
    return {
        "prime": p,
        "auxiliary_prime": ell,
        "primitive_root_mod_p": gen_p,
        "primitive_root_mod_auxiliary": gen_ell,
        "zeta_order_3_mod_p": zeta,
        "psi_root_order_p_mod_auxiliary": eta,
        "omega_order_3_mod_auxiliary": omega,
        "sector_dimensions": sector_dims,
        "sector_charpoly_coefficients_low_to_high": [
            polynomial_coefficients(poly) for poly in sector_polys
        ],
        "sector_determinants_mod_auxiliary": sector_determinants,
        "expected_sector_determinant_mod_auxiliary": expected_det,
        "sector_1_equals_sector_2": True,
        "gcd_sector_0_sector_1_coefficients_low_to_high": polynomial_coefficients(gcd01),
        "gcd_sector_0_sector_1_degree": gcd01.degree(),
        "reduced_augmentation_numerator_degree": 2 * d0,
        "reduced_augmentation_denominator_degree": d1 + d2,
        "virtual_degree": 2 * d0 - d1 - d2,
        "exact_matrix_gates": {
            "kernel_R_equals_Rinverse_kernel": True,
            "T_commutes_with_R": True,
            "R_basis_k_equals_omega_power_k_basis_k": True,
            "sector_images_invariant": True,
            "determinant_sign_formula": True,
        },
    }


def p7_conjugation_obstruction() -> dict[str, Any]:
    p = 7
    rho = 2
    histogram = [0] * p
    for x in range(p):
        for y in range(p):
            phase = (2 * x**3 + 2 * y**3 + (rho + 1) * x * y) % p
            histogram[phase] += 1
    expected = [4, 9, 18, 3, 6, 6, 3]
    assert histogram == expected
    difference = [histogram[r] - histogram[(-r) % p] for r in range(p)]
    assert difference == [0, 6, 12, -3, 3, -12, -6]
    # A rational polynomial of degree at most six vanishing at a primitive
    # seventh root must be a scalar multiple of Phi_7.  This vector is not.
    assert len(set(difference)) > 1 and difference[0] == 0 and difference[1] != 0
    return {
        "prime": 7,
        "rho_order_3": rho,
        "twisted_phase": "2*x^3+2*y^3+3*x*y",
        "residue_histogram_0_through_6": histogram,
        "conjugation_difference_coefficients_0_through_6": difference,
        "cyclotomic_minimal_polynomial": "Phi_7(X)=1+X+X^2+X^3+X^4+X^5+X^6",
        "difference_is_multiple_of_Phi_7": False,
        "A_7_1_is_real": False,
        "global_conjugation_symmetry": "REFUTED_FOR_RAW_SINGLE_CHARACTER_PRODUCT",
    }


def source_lock(project_root: Path) -> list[dict[str, str]]:
    henon_root = project_root.parent
    relative = (
        "phase3_hcs_c32_artin_schreier_quantum_trace/THEOREM_PACKAGE.md",
        "phase3_hcs_c32_artin_schreier_quantum_trace/DERIVATION_PACKAGE.md",
        "henon_homogeneous_boundary_index_obstruction/DERIVATION_PACKAGE.md",
        "henon_cubic_cm_frobenius_bridge/results/c41_certificate.json",
        "henon_cm_three_prime_supercancellation_obstruction/results/c42_certificate.json",
        "skills/route-a-evaluator.md",
    )
    rows = []
    for item in relative:
        path = henon_root / item
        if not path.is_file():
            raise FileNotFoundError(path)
        rows.append({"path": f"henon_dynamics/{item}", "sha256": sha256_file(path)})
    return rows


def build_payload(project_root: Path) -> dict[str, Any]:
    controls = [build_control(p) for p in CONTROL_PRIMES]
    return {
        "material_passport": {
            "candidate_id": "HCS-C43",
            "project": "henon_mu3_augmented_euler_superproduct",
            "ai_assistance_disclosed": True,
            "evidence_policy": "exact arithmetic and proved analytic bounds; no zero-table data",
        },
        "source_lock": source_lock(project_root),
        "conventions": {
            "classical_map": "H0(q,p)=(-6q^2-p,q)",
            "generating_kernel": "S0(q,Q)=qQ+2q^3",
            "fourier_character": "exp(2*pi*i*x/p)",
            "quantum_kernel": "U_p(Q,q)=p^(-1/2)*psi_p(qQ+2q^3)",
            "grading_action": "(R_p f)(x)=f(zeta_p*x)",
            "chronological_time": "T_p=U_p^2",
            "augmentation_weights": [2, -1, -1],
            "local_variable": "canonical z_p=p^(-s); optional critical-line display uses p^(1/2-s)",
            "prime_scope": "p>3 and p=1 mod 3",
            "auxiliary_prime_rule": "smallest prime ell=1 mod 3p",
        },
        "theorems": {
            "classical_mu3_relation": "H0*g=g^(-1)*H0",
            "quantum_mu3_relation": "U_p*R_p=R_p^(-1)*U_p",
            "two_step_sector_relation": "[U_p^2,R_p]=0",
            "sector_dimensions": ["(p+2)/3", "(p-1)/3", "(p-1)/3"],
            "nontrivial_sector_equivalence": "T_p|H_1 is unitarily equivalent to T_p|H_2",
            "projector_identity": "2*P_0-P_1-P_2=R_p+R_p^2",
            "sector_determinants": "det(T_p|H_k)=(-1)^((p-1)/6) for k=0,1,2",
            "augmentation_asymptotic": "D_p^aug(z)~z^2 as z tends to infinity",
            "chronological_moment": "A_p,n=Tr((R_p+R_p^2)*U_p^(2n))",
            "moment_bound": "abs(A_p,n)<=2*4^n for every n>=1",
            "euler_half_plane": "product D_p^aug(p^(-s)) converges locally uniformly and is nonzero for Re(s)>1",
            "local_divisor": "all reduced local zeros and poles satisfy abs(z)=1; canonical p^(-s) gives Re(s)=0, optional p^(1/2-s) gives Re(s)=1/2",
            "local_reciprocal_duality": "D_p^aug(z)=z^2*conjugate(D_p^aug(1/conjugate(z)))",
            "global_reciprocal_completion": "OPEN; product of local p^(1-2s) factors diverges",
            "raw_global_conjugation_symmetry": "REFUTED_EXACTLY_AT_THE_FIRST_PRIME_p=7",
            "global_continuation": "OPEN",
        },
        "scalar_kummer_control": {
            "cover": "u^3=2*x^3",
            "trivialization": "t=u/x gives t^3=2",
            "order_3_character_pullback": "chi(2*x^3)=chi(2) on G_m",
            "decision": "STOP_PHASE_INTRINSIC_Z3_KUMMER_LIFT",
        },
        "p7_conjugation_obstruction": p7_conjugation_obstruction(),
        "exact_modular_controls": controls,
        "aggregate_control": {
            "control_primes": list(CONTROL_PRIMES),
            "all_sector_1_equal_sector_2": all(row["sector_1_equals_sector_2"] for row in controls),
            "all_sector_0_sector_1_coprime": all(row["gcd_sector_0_sector_1_degree"] == 0 for row in controls),
            "maximum_certified_reduced_numerator_degree": max(row["reduced_augmentation_numerator_degree"] for row in controls),
            "maximum_certified_reduced_denominator_degree": max(row["reduced_augmentation_denominator_degree"] for row in controls),
            "finite_ledger_does_not_prove_all_prime_coprimality": True,
        },
        "route_a": {
            "A1": "A1_WEAK",
            "A2": "A2_ANALYTIC_DETERMINANT",
            "A3": "A3_FAIL",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "decisions": {
            "intrinsic_full_kernel_mu3_symmetry": "PROVED",
            "integral_augmentation_trace_formula": "PROVED",
            "analytic_nonzero_half_plane": "PROVED",
            "bounded_rank_local_cancellation_from_mu3_symmetry": "REFUTED_ON_FROZEN_CONTROLS",
            "raw_single_character_conjugation_symmetry": "REFUTED",
            "finite_tate_cm_riemann_repair": "CLOSED_BY_HCS_C42_SOURCE_LOCK",
            "global_functional_equation": "OPEN",
            "global_RH_divisor_match": "NOT_TESTABLE",
            "next_gate": "FULL_KERNEL_FIXED_COEFFICIENT_FIELD_THEN_HANKEL_RANK_OR_STOP",
        },
        "scope": {
            "rh_proved": False,
            "hilbert_polya_operator_constructed": False,
            "global_meromorphic_continuation_claimed": False,
            "gamma_factor_claimed": False,
            "riemann_zero_data_used": False,
            "finite_controls_are_not_all_prime_theorem": True,
            "complex_color_determinant_used": False,
        },
    }


def build_certificate(project_root: Path) -> dict[str, Any]:
    payload = build_payload(project_root)
    return {
        "schema": SCHEMA,
        "payload": payload,
        "payload_sha256": hashlib.sha256(canonical_json(payload)).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    project_root = Path(__file__).resolve().parents[1]
    cert = build_certificate(project_root)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {output}")
    print(f"payload_sha256={cert['payload_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
