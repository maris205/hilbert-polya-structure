#!/usr/bin/env python3
"""Produce the exact HCS-C177 expanding-circle certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c177_expanding_circle_evidence.json"
SOURCE_COMMIT = "100e5f601a0196710d53784bdeef40d2bff89fa8"
B_MIN, B_MAX = 2, 12
N_MAX = 12
MODE_MAX = 72
CORRELATION_N_MAX = 8
SOBOLEV_S_MAX = 4


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    primes = 0
    p = 2
    value = n
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    periodic_rows = []
    for b in range(B_MIN, B_MAX + 1):
        for n in range(1, N_MAX + 1):
            fixed = b**n - 1
            exact = sum(mobius(n // d) * (b**d - 1) for d in divisors(n))
            assert exact % n == 0
            periodic_rows.append({
                "b": b,
                "n": n,
                "fixed_points": fixed,
                "exact_period_points": exact,
                "primitive_cycles": exact // n,
            })

    wold_rows = []
    for b in range(B_MIN, B_MAX + 1):
        for m in range(-MODE_MAX, MODE_MAX + 1):
            if m == 0:
                root, level, sector = 0, 0, "constant"
            else:
                root, level = m, 0
                while root % b == 0:
                    root //= b
                    level += 1
                sector = "unilateral_shift"
            wold_rows.append({
                "b": b,
                "input_mode": m,
                "output_mode": b * m,
                "chain_root": root,
                "chain_level": level,
                "output_chain_level": 0 if m == 0 else level + 1,
                "adjoint_output": m // b if m % b == 0 else None,
                "sector": sector,
            })

    correlation_rows = []
    for b in range(B_MIN, B_MAX + 1):
        for n in range(1, CORRELATION_N_MAX + 1):
            for s in range(1, SOBOLEV_S_MAX + 1):
                correlation_rows.append({
                    "b": b,
                    "n": n,
                    "s": s,
                    "sharp_test_f_mode": b**n,
                    "sharp_test_g_mode": 1,
                    "normalized_correlation_numerator": 1,
                    "normalized_correlation_denominator": b ** (n * s),
                })

    data = {
        "schema": "HCS-C177-v1",
        "candidate_id": "HCS-C177",
        "date_utc": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        },
        "source_lock": {
            "object": "integer expanding circle endomorphism T_b(x)=b*x modulo one",
            "family": "every integer b>=2 on R/Z",
            "clock": "one application of T_b",
            "measure": "normalized Haar measure",
            "fourier_convention": "e_m(x)=exp(2*pi*i*m*x) and U_b f=f after T_b",
            "zeta_convention": "ordinary Artin--Mazur zeta from finite fixed-point counts",
            "cutoff": "all-parameter proof; exact regression uses 2<=b<=12, 1<=n<=12, and |m|<=72",
            "allowed_data": "the frozen circle map, Haar measure, Fourier integers, and source-derived identities",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
        },
        "periodic_theorem": {
            "fixed_points": "#Fix(T_b^n)=b^n-1 for every b>=2 and n>=1",
            "exact_period_points": "P_b(n)=sum_(d|n) mu(n/d)*(b^d-1)",
            "primitive_cycles": "C_b(n)=P_b(n)/n",
            "artin_mazur_zeta": "zeta_AM,b(z)=(1-z)/(1-b*z)",
            "euler_product": "zeta_AM,b(z)=product_(n>=1)(1-z^n)^(-C_b(n)) coefficientwise",
        },
        "operator_theorem": {
            "basis_action": "U_b e_m=e_(b*m)",
            "wold_decomposition": "L2(T)=C*1 direct_sum over nonzero r with b not dividing r of closure span{e_(r*b^j):j>=0}",
            "shift_multiplicity": "countably infinite copies of the unilateral shift",
            "spectrum": "closed unit disk; the only Koopman eigenvalue is 1 on constants",
            "adjoint": "U_b^* e_m=e_(m/b) when b divides m and zero otherwise",
            "ownership": "U_b is a proper isometry, not unitary, noncompact, in no finite Schatten class, and has no ordinary Fredholm determinant det(I-z*U_b) for z!=0",
        },
        "correlation_theorem": {
            "homogeneous_norm": "||f||_dotH^s^2=sum_(m!=0)|m|^(2s)|f_hat(m)|^2",
            "bound": "for mean-zero f in dotH^s and g in L2, |<f,U_b^n g>|<=b^(-n*s)||f||_dotH^s||g||_2",
            "sharpness": "e_(b^n) against e_1 attains the normalized factor b^(-n*s)",
            "transfer": "the Perron operator is U_b^* and erases modes not divisible by b",
        },
        "finite_replay": {
            "b_min": B_MIN,
            "b_max": B_MAX,
            "n_max": N_MAX,
            "mode_max": MODE_MAX,
            "correlation_n_max": CORRELATION_N_MAX,
            "sobolev_s_max": SOBOLEV_S_MAX,
            "periodic_rows": periodic_rows,
            "wold_rows": wold_rows,
            "correlation_rows": correlation_rows,
            "periodic_row_count": len(periodic_rows),
            "wold_row_count": len(wold_rows),
            "correlation_row_count": len(correlation_rows),
        },
        "progress_and_boundary": {
            "progress": "unifies all-b periodic coordinates, primitive cycles, rational zeta, exact Wold chains, Perron action, and a sharp Sobolev correlation law",
            "parameter_blindness": "prime and composite b obey the same degree-only formulas and operator model",
            "natural_extension": "the inverse-limit extension is a unitary dilation on a changed phase space, not a physical quantization of the original endomorphism",
            "evidence_boundary": "finite rows regression-test exact formulas; all-parameter conclusions rest on written proofs",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "A0_qualification": "DEGREE_PARAMETER_HAS_NO_INTRINSIC_PRIME_OR_ARITHMETIC_ORIGIN",
            "A1_qualification": "COMPLETE_PRIMITIVE_ORBIT_LEDGER_BUT_ONLY_GENERIC_DEGREE_DATA",
            "A2_qualification": "RATIONAL_SOURCE_ZETA_HAS_NO_TARGET_DIVISOR_MATCH",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4_qualification": "PROPER_KOOPMAN_ISOMETRY_AND_UNITARY_DILATION_ONLY_AFTER_CHANGING_PHASE_SPACE",
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
            "novelty or priority for classical expanding-map formulas",
            "prime semantics for the arbitrary degree b",
            "an ordinary Fredholm determinant for the non-trace-class Koopman isometry",
            "a target divisor, functional equation, counting law, or continuation match",
            "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
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
        "status": "C177_PRODUCER_PASS",
        "periodic_rows": len(data["finite_replay"]["periodic_rows"]),
        "wold_rows": len(data["finite_replay"]["wold_rows"]),
        "correlation_rows": len(data["finite_replay"]["correlation_rows"]),
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
