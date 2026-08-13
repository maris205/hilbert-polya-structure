#!/usr/bin/env python3
"""Independent, type-strict checker for HCS-C43.

This checker does not import the producer and does not use FLINT.  It rebuilds
the frozen matrices with Python integer arithmetic, computes characteristic
polynomials by Faddeev--LeVerrier, and computes polynomial gcds independently.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable


SCHEMA = "hcs-c43-certificate-v1"
CONTROL_PRIMES = (7, 13, 19, 31, 37, 43, 61, 67, 73)


class GateFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def canonical_json(obj: Any) -> bytes:
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def strict_equal(a: Any, b: Any) -> bool:
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return set(a) == set(b) and all(strict_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(strict_equal(x, y) for x, y in zip(a, b))
    return a == b


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


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


def factors(n: int) -> list[int]:
    ans: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        ans.append(n)
    return ans


def primitive_root(p: int) -> int:
    qs = factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in qs):
            return g
    raise GateFailure("primitive root not found")


def auxiliary_prime(p: int) -> int:
    k = 1
    while True:
        ell = 3 * p * k + 1
        if is_prime(ell):
            return ell
        k += 1


def eye(n: int) -> list[list[int]]:
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matmul(a: list[list[int]], b: list[list[int]], modulus: int) -> list[list[int]]:
    n = len(a)
    k = len(b)
    require(n >= 1 and k >= 1, "empty matrix")
    require(len(a[0]) == k, "matrix shape mismatch")
    m = len(b[0])
    out = [[0] * m for _ in range(n)]
    # ikj order is materially faster for these dense but small matrices.
    for i in range(n):
        for t in range(k):
            coeff = a[i][t] % modulus
            if coeff:
                bt = b[t]
                for j in range(m):
                    out[i][j] = (out[i][j] + coeff * bt[j]) % modulus
    return out


def scalar_matrix(a: list[list[int]], scalar: int, modulus: int) -> list[list[int]]:
    return [[scalar * x % modulus for x in row] for row in a]


def charpoly_faddeev(a: list[list[int]], modulus: int) -> list[int]:
    """Return det(xI-A), low coefficient first."""
    n = len(a)
    require(all(len(row) == n for row in a), "charpoly requires square matrix")
    b = eye(n)
    high = [1]
    for k in range(1, n + 1):
        ab = matmul(a, b, modulus)
        trace = sum(ab[i][i] for i in range(n)) % modulus
        ck = (-trace * pow(k, -1, modulus)) % modulus
        for i in range(n):
            ab[i][i] = (ab[i][i] + ck) % modulus
        b = ab
        high.append(ck)
    return list(reversed(high))


def poly_trim(a: list[int]) -> list[int]:
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_divmod(a: list[int], b: list[int], modulus: int) -> tuple[list[int], list[int]]:
    a = poly_trim([x % modulus for x in a])
    b = poly_trim([x % modulus for x in b])
    require(b != [0], "polynomial division by zero")
    if len(a) < len(b):
        return [0], a
    q = [0] * (len(a) - len(b) + 1)
    inv = pow(b[-1], -1, modulus)
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        c = a[-1] * inv % modulus
        q[shift] = c
        for i in range(len(b)):
            a[i + shift] = (a[i + shift] - c * b[i]) % modulus
        a = poly_trim(a)
    return poly_trim(q), a


def poly_gcd(a: list[int], b: list[int], modulus: int) -> list[int]:
    a = poly_trim(a)
    b = poly_trim(b)
    while b != [0]:
        _, r = poly_divmod(a, b, modulus)
        a, b = b, r
    inv = pow(a[-1], -1, modulus)
    return [(x * inv) % modulus for x in a]


def orbit_reps(p: int, zeta: int) -> list[int]:
    pending = set(range(1, p))
    reps: list[int] = []
    while pending:
        a = min(pending)
        orbit = {a, zeta * a % p, zeta * zeta * a % p}
        require(len(orbit) == 3, "nonfree nonzero zeta orbit")
        reps.append(a)
        pending -= orbit
    return reps


def basis_data(
    p: int, ell: int, zeta: int, omega: int, k: int
) -> tuple[list[list[int]], list[int]]:
    reps = orbit_reps(p, zeta)
    columns: list[list[int]] = []
    selectors: list[int] = []
    if k == 0:
        v = [0] * p
        v[0] = 1
        columns.append(v)
        selectors.append(0)
    for a in reps:
        v = [0] * p
        x = a
        for j in range(3):
            v[x] = pow(omega, (k * j) % 3, ell)
            x = zeta * x % p
        columns.append(v)
        selectors.append(a)
    basis = [[columns[j][i] for j in range(len(columns))] for i in range(p)]
    return basis, selectors


def rebuild_control(p: int) -> dict[str, Any]:
    require(is_prime(p) and p > 3 and p % 3 == 1, "invalid control prime")
    ell = auxiliary_prime(p)
    gp = primitive_root(p)
    ge = primitive_root(ell)
    zeta = pow(gp, (p - 1) // 3, p)
    eta = pow(ge, (ell - 1) // p, ell)
    omega = pow(ge, (ell - 1) // 3, ell)

    kernel = [
        [pow(eta, (q * Q + 2 * q * q * q) % p, ell) for q in range(p)]
        for Q in range(p)
    ]
    R = [[0] * p for _ in range(p)]
    Rinv = [[0] * p for _ in range(p)]
    for x in range(p):
        R[x][pow(zeta, -2, p) * x % p] = 1
        Rinv[x][pow(zeta, -1, p) * x % p] = 1
    require(matmul(kernel, R, ell) == matmul(Rinv, kernel, ell), "UR relation failed")

    T = scalar_matrix(matmul(kernel, kernel, ell), pow(p, -1, ell), ell)
    require(matmul(T, R, ell) == matmul(R, T, ell), "T-R commutator failed")

    dimensions: list[int] = []
    polynomials: list[list[int]] = []
    sector_determinants: list[int] = []
    for k in range(3):
        basis, selectors = basis_data(p, ell, zeta, omega, k)
        require(
            matmul(R, basis, ell) == scalar_matrix(basis, pow(omega, k, ell), ell),
            "sector basis has wrong R eigenvalue",
        )
        image = matmul(T, basis, ell)
        block = [image[x] for x in selectors]
        require(matmul(basis, block, ell) == image, "sector invariance failed")
        dimensions.append(len(selectors))
        poly = charpoly_faddeev(block, ell)
        polynomials.append(poly)
        sector_determinants.append(((-1) ** len(selectors) * poly[0]) % ell)

    require(polynomials[1] == polynomials[2], "paired sector polynomials differ")
    gcd01 = poly_gcd(polynomials[0], polynomials[1], ell)
    require(gcd01 == [1], "sector gcd is not monic one")
    expected_det = 1 if ((p - 1) // 6) % 2 == 0 else ell - 1
    require(sector_determinants == [expected_det] * 3, "determinant sign formula")
    d0, d1, d2 = dimensions
    return {
        "prime": p,
        "auxiliary_prime": ell,
        "primitive_root_mod_p": gp,
        "primitive_root_mod_auxiliary": ge,
        "zeta_order_3_mod_p": zeta,
        "psi_root_order_p_mod_auxiliary": eta,
        "omega_order_3_mod_auxiliary": omega,
        "sector_dimensions": dimensions,
        "sector_charpoly_coefficients_low_to_high": polynomials,
        "sector_determinants_mod_auxiliary": sector_determinants,
        "expected_sector_determinant_mod_auxiliary": expected_det,
        "sector_1_equals_sector_2": True,
        "gcd_sector_0_sector_1_coefficients_low_to_high": gcd01,
        "gcd_sector_0_sector_1_degree": len(gcd01) - 1,
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
            histogram[(2 * x**3 + 2 * y**3 + 3 * x * y) % p] += 1
    difference = [histogram[r] - histogram[(-r) % p] for r in range(p)]
    require(histogram == [4, 9, 18, 3, 6, 6, 3], "p7 histogram")
    require(difference == [0, 6, 12, -3, 3, -12, -6], "p7 conjugation vector")
    require(len(set(difference)) > 1, "difference could be Phi7 multiple")
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
    return [
        {"path": f"henon_dynamics/{item}", "sha256": sha256_file(henon_root / item)}
        for item in relative
    ]


def expected_payload(project_root: Path) -> dict[str, Any]:
    controls = [rebuild_control(p) for p in CONTROL_PRIMES]
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
            "all_sector_1_equal_sector_2": True,
            "all_sector_0_sector_1_coprime": True,
            "maximum_certified_reduced_numerator_degree": max(r["reduced_augmentation_numerator_degree"] for r in controls),
            "maximum_certified_reduced_denominator_degree": max(r["reduced_augmentation_denominator_degree"] for r in controls),
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


def audit_certificate(cert: Any, project_root: Path) -> tuple[list[dict[str, str]], bool]:
    results: list[dict[str, str]] = []

    def gate(name: str, fn: Callable[[], None]) -> None:
        try:
            fn()
            results.append({"gate": name, "status": "PASS"})
        except GateFailure as exc:
            results.append({"gate": name, "status": "FAIL", "detail": str(exc)})
        except Exception as exc:  # unexpected checker errors are never semantic rejection
            results.append({"gate": name, "status": "ERROR", "detail": f"{type(exc).__name__}: {exc}"})

    def g0() -> None:
        require(type(cert) is dict, "certificate must be object")
        require(set(cert) == {"schema", "payload", "payload_sha256"}, "top-level keys")
        require(type(cert["schema"]) is str and cert["schema"] == SCHEMA, "schema")
        require(type(cert["payload_sha256"]) is str, "payload digest type")
        digest = hashlib.sha256(canonical_json(cert["payload"])).hexdigest()
        require(digest == cert["payload_sha256"], "payload digest")

    expected_box: dict[str, Any] = {}

    def get_expected() -> dict[str, Any]:
        if "payload" not in expected_box:
            expected_box["payload"] = expected_payload(project_root)
        return expected_box["payload"]

    def block_gate(key: str) -> Callable[[], None]:
        def check() -> None:
            require(type(cert.get("payload")) is dict, "payload object")
            expected = get_expected()
            require(key in cert["payload"], f"missing {key}")
            require(strict_equal(cert["payload"][key], expected[key]), f"{key} mismatch")
        return check

    gate("G0_SCHEMA_AND_PAYLOAD_HASH", g0)
    gate("G1_MATERIAL_AND_SOURCE_LOCK", lambda: (
        block_gate("material_passport")(), block_gate("source_lock")()
    ))
    gate("G2_CONVENTIONS", block_gate("conventions"))
    gate("G3_THEOREM_CONTRACT", block_gate("theorems"))
    gate("G4_SCALAR_KUMMER_CONTROL", block_gate("scalar_kummer_control"))
    gate("G5_P7_CONJUGATION_OBSTRUCTION", block_gate("p7_conjugation_obstruction"))
    gate("G6_EXACT_MATRIX_AND_SECTOR_REPLAY", block_gate("exact_modular_controls"))
    gate("G7_AGGREGATE_COPRIMALITY", block_gate("aggregate_control"))
    gate("G8_ROUTE_A", block_gate("route_a"))
    gate("G9_DECISIONS", block_gate("decisions"))
    gate("G10_SCOPE", block_gate("scope"))
    gate("G11_FULL_PAYLOAD", lambda: require(
        strict_equal(cert.get("payload"), get_expected()), "full payload mismatch"
    ))
    return results, all(row["status"] == "PASS" for row in results)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    cert_path = Path(args.certificate)
    cert = json.loads(cert_path.read_text(encoding="utf-8"))
    project_root = Path(__file__).resolve().parents[1]
    gates, passed = audit_certificate(cert, project_root)
    report = {
        "schema": "hcs-c43-independent-check-v1",
        "certificate_sha256": sha256_file(cert_path),
        "gates": gates,
        "passed_gates": sum(row["status"] == "PASS" for row in gates),
        "total_gates": len(gates),
        "all_pass": passed,
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{report['passed_gates']}/{report['total_gates']} gates PASS")
    if not passed:
        for row in gates:
            if row["status"] != "PASS":
                print(f"{row['gate']}: {row['status']} {row.get('detail', '')}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
