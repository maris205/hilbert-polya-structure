#!/usr/bin/env python3
"""Produce the exact HCS-C164 induced-Fredholm-owner certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c164_fredholm_owner_evidence.json"
SOURCE_COMMIT = "4342893ce5e2516924181744bfacc01c12e4959d"
PREFIX_LIMIT = 128
SERIES_LIMIT = 48
TRACE_POWER_LIMIT = 6


def thue_morse(n: int) -> int:
    return n.bit_count() & 1


def convolve(left: list[int], right: list[int], limit: int) -> list[int]:
    result = [0] * (limit + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[: limit + 1 - i]):
            if b:
                result[i + j] += a * b
    return result


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def payload_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build() -> dict:
    tm_prefix = [thue_morse(n) for n in range(PREFIX_LIMIT)]
    s_prefix = [n for n, bit in enumerate(tm_prefix) if bit]
    f_coefficients = [0] + [thue_morse(n - 1) for n in range(1, SERIES_LIMIT + 1)]

    trace_rows = []
    current = [1] + [0] * SERIES_LIMIT
    for power in range(1, TRACE_POWER_LIMIT + 1):
        current = convolve(current, f_coefficients, SERIES_LIMIT)
        trace_rows.append({"power": power, "coefficients": current})

    determinant = [0] * (SERIES_LIMIT + 1)
    determinant[0] = 1
    for n in range(1, SERIES_LIMIT + 1):
        determinant[n] -= f_coefficients[n]
        determinant[n] -= 1 if n == 1 else 0
        determinant[n] += f_coefficients[n - 1]

    branch_rows = [
        {
            "branch_index": index,
            "gap_s": s,
            "code_length": s + 1,
            "rank_one_trace": f"z^{s + 1}",
        }
        for index, s in enumerate(s_prefix[:32])
    ]
    truncation_rows = []
    for cutoff in (8, 16, 32, 64, 128):
        active = [s for s in range(cutoff) if thue_morse(s)]
        truncation_rows.append({
            "gap_cutoff": cutoff,
            "active_branches": len(active),
            "first_gap": active[0],
            "last_gap": active[-1],
            "trace_polynomial_degrees": [s + 1 for s in active],
        })

    return_partial = sum(Fraction(thue_morse(n), 2**n) for n in range(PREFIX_LIMIT))
    return_tail_bound = Fraction(1, 2 ** (PREFIX_LIMIT - 1))
    dyadic_rows = [
        {
            "level": level,
            "root_order": 2**level,
            "vanishing_factor": f"1-z^{2**level}",
            "operator_trace_consequence": "a trace-class meromorphic arc extension would continue F",
        }
        for level in range(1, 9)
    ]

    data = {
        "schema": "HCS-C164-v1",
        "candidate_id": "HCS-C164",
        "date_utc": "2026-08-25",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "the C159 binary Thue--Morse S-gap renewal shift X_S with S={s>=0:t_s=1}",
            "family": "the source first-return code branches 10^s, s in S, together with the separately frozen uninduced renewal adjacency",
            "clock": "one left shift on X_S; a first-return branch 10^s has source duration s+1",
            "normalization": "F(z)=sum_{s in S}z^(s+1), zeta_X(z)^(-1)=(1-z)(1-F(z)), and Fredholm determinants have constant term one",
            "cutoff": "all operator, no-go, and continuation conclusions are all-parameter theorems; 128 source bits and formal degree 48 are sentinels",
            "precision": "exact integer formal coefficients; analytic summability is proved by comparison, not inferred numerically",
            "allowed_data": "the source-defined Thue--Morse parity, renewal branches, and package-local exact symbolic calculations",
            "forbidden_data": "target zero or prime tables, arithmetic/local factors, root numbers, automorphy, Hilbert--Polya claims, and Route-B inputs",
        },
        "induced_owner_theorem": {
            "hilbert_space": "H=l2(S) with its standard orthonormal branch basis e_s",
            "gauge": "q_s=exp(-sqrt(s+1)); u=(q_s)_{s in S}",
            "functional": "ell_z(f)=sum_{s in S}q_s^(-1)z^(s+1)f_s",
            "branch_resolution": "B_s(z)f=q_s^(-1)z^(s+1)f_s u and K_z=sum_{s in S}B_s(z)",
            "operator_family": "K_z f=ell_z(f)u; L_z=[z] direct_sum K_z",
            "trace_norm_holomorphy": "for every rho<1, sum_{s in S}||B_s(z)||_1<=||u||_2 sum_{s in S}exp(sqrt(s+1))rho^(s+1)<infinity uniformly on |z|<=rho",
            "rank_and_trace": "rank(K_z)<=1, Tr(K_z^m)=F(z)^m for every m>=1 and |z|<1",
            "fredholm_identity": "det_F(I-L_z)=(1-z)(1-F(z))=zeta_X(z)^(-1)",
            "gauge_invariance": "every positive subexponential diagonal gauge with u and the coefficient functional square summable gives the same branch traces and Fredholm determinant",
            "owner_status": "natural first-return branch transfer family; not the uninduced time-one adjacency and not evidence from a scalar determinant alone",
        },
        "uninduced_no_go_theorem": {
            "adjacency": "A delta_n=delta_(n+1)+t_n delta_0 on l2(N0,w)",
            "normalized_basis_law": "A e_n=sqrt(w_(n+1)/w_n)e_(n+1)+t_n sqrt(w_0/w_n)e_0",
            "weak_null_test": "compactness would force ||A e_n|| to zero for the weakly null orthonormal basis",
            "shift_consequence": "sqrt(w_(n+1)/w_n)->0, hence eventually w_(n+1)<=w_n/4 and w_n->0",
            "return_consequence": "along the infinite set S, sqrt(w_0/w_n)->0, hence w_n->infinity",
            "contradiction": "the two consequences are incompatible; every bounded realization is noncompact and belongs to no Schatten class S_p, 0<p<infinity",
            "nonempty_control": "w_n=2^n makes A bounded: the shift norm is sqrt(2) and the return row has squared norm sum_{s in S}2^(-s)<infinity",
        },
        "continuation_obstruction": {
            "input": "C159 proves that F, equivalently the Thue--Morse product, has no meromorphic continuation through any unit-circle arc",
            "trace_transfer": "a trace-class meromorphic extension of K_z or L_z through an arc would make its scalar trace F(z) or z+F(z) meromorphic there",
            "conclusion": "the induced trace-class owner exists exactly on the open unit disk and has no trace-class meromorphic extension through any boundary arc",
            "tautological_scalar_boundary": "the equality of one scalar determinant is not operator ownership; ownership here also includes source branch coordinates, trace-norm branch summation, and all trace powers",
        },
        "finite_replay": {
            "tm_prefix_length": PREFIX_LIMIT,
            "tm_prefix": tm_prefix,
            "s_prefix": s_prefix,
            "series_limit": SERIES_LIMIT,
            "F_coefficients": f_coefficients,
            "trace_power_limit": TRACE_POWER_LIMIT,
            "trace_power_rows": trace_rows,
            "determinant_coefficients": determinant,
            "branch_rows": branch_rows,
            "truncation_rows": truncation_rows,
            "bounded_weight_control": {
                "weight": "w_n=2^n",
                "shift_ratio_squared": 2,
                "return_row_squared_norm_partial_128": fraction_record(return_partial),
                "return_row_squared_norm_tail_upper": fraction_record(return_tail_bound),
            },
            "dyadic_boundary_rows": dyadic_rows,
        },
        "progress_and_boundary": {
            "progress": "closes C159's operator-owner gate with a branch-resolved first-return Fredholm family and proves a universal compactness obstruction for every diagonal Hilbert realization of the uninduced adjacency",
            "route_a_obstruction": "the owner is induced and nonunitary, the original time-one adjacency is never compact when bounded, and no target divisor or self-adjoint Hilbert--Polya lift is obtained",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "RECURRENT_THUE_MORSE_RENEWAL_DYNAMICS_WITH_A_SOURCE_BRANCH_TRANSFER_OWNER",
            "A2_qualification": "EXACT_SOURCE_FREDHOLM_DETERMINANT_BUT_NO_TARGET_DIVISOR_COMPARISON",
            "A3_qualification": "SOURCE_TRACE_CLASS_DISK_DOMAIN_AND_PROVED_UNIT_CIRCLE_EXTENSION_OBSTRUCTION_ONLY",
            "A4_qualification": "INDUCED_NONUNITARY_TRANSFER_FAMILY_AND_UNINDUCED_SCHATTEN_NO_GO_WITH_NO_SELF_ADJOINT_LIFT",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "uses_prime_table": False,
            "uses_zero_table": False,
            "claims_arithmetic_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_hilbert_polya": False,
            "uses_route_b_inputs": False,
        },
        "nonclaims": [
            "that the induced first-return family is the uninduced time-one adjacency",
            "that a scalar determinant identity alone establishes operator ownership",
            "a target divisor, functional equation, counting-law match, or arithmetic local factorization",
            "a unitary, Hamiltonian, natural self-adjoint, or Hilbert--Polya operator",
            "Route-B authorization or a solution of the larger program",
        ],
    }
    data["payload_sha256"] = sha256(payload_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C164_PRODUCER_PASS",
        "output": str(args.output),
        "payload_sha256": data["payload_sha256"],
        "source_bits": PREFIX_LIMIT,
        "formal_cells": (TRACE_POWER_LIMIT + 2) * (SERIES_LIMIT + 1),
        "branch_rows": len(data["finite_replay"]["branch_rows"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
