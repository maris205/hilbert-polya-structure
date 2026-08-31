#!/usr/bin/env python3
"""Deterministic exact/high-precision evidence for the C261 Airy--Talbot atlas."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from math import gcd
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "98782afe1e754c311ad0736f72ce09dcc7c85c77"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c261_airy_evidence.json"
mp.mp.dps = 90


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def dec(value: mp.mpf) -> str:
    return mp.nstr(value, 68, strip_zeros=False)


def factorint(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def fixed_stride(q: int) -> int:
    out = 1
    for prime, exponent in factorint(q).items():
        out *= prime ** ((exponent + 2) // 3)
    return out


def phase_digest(p: int, q: int) -> str:
    raw = ",".join(str((p * n**3) % q) for n in range(q)).encode()
    return sha256(raw).hexdigest()


def modular_rows() -> list[dict]:
    rows: list[dict] = []
    for q in range(1, 97):
        ps = [0] if q == 1 else [p for p in range(1, q) if gcd(p, q) == 1]
        stride = fixed_stride(q)
        for p in ps:
            fixed_window = sum(1 for n in range(-512, 513) if (p * n**3) % q == 0)
            rows.append({
                "row_id": f"R{len(rows)+1:04d}",
                "p": p,
                "q": q,
                "phase_exponent_sha256": phase_digest(p, q),
                "strobe_order": q,
                "fixed_mode_stride": stride,
                "fixed_mode_density": f"1/{stride}",
                "fixed_modes_in_minus512_to_512": fixed_window,
            })
    return rows


def dft_row(p: int, q: int) -> dict:
    coeffs: list[dict] = []
    max_inverse = mp.mpf("0")
    for r in range(q):
        total = mp.mpc(0)
        for s in range(q):
            total += mp.e ** (2j * mp.pi * ((p * s**3 - s * r) % q) / q)
        total /= q
        coeffs.append({"r": r, "re": dec(mp.re(total)), "im": dec(mp.im(total))})
    parseval = sum(mp.mpf(c["re"])**2 + mp.mpf(c["im"])**2 for c in coeffs)
    for n in range(q):
        reconstructed = mp.mpc(0)
        for c in coeffs:
            reconstructed += mp.mpc(c["re"], c["im"]) * mp.e ** (2j * mp.pi * n * c["r"] / q)
        target = mp.e ** (2j * mp.pi * ((p * n**3) % q) / q)
        max_inverse = max(max_inverse, abs(reconstructed - target))
    return {
        "row_id": f"D{p}_{q}", "p": p, "q": q,
        "coefficients": coeffs,
        "nonzero_coefficients_at_1e_minus_55": sum(
            1 for c in coeffs if abs(mp.mpc(c["re"], c["im"])) > mp.mpf("1e-55")
        ),
        "parseval_residual": dec(abs(parseval - 1)),
        "max_inverse_dft_residual": dec(max_inverse),
    }


SUPPORTS = [
    [-1, 1], [1, 2], [2, 4], [3, 6, 9], [-5, 0, 10],
    [1, 3, 5], [2, 3, 6], [4, 6, 10], [-7, -2, 5], [6, 12, 18],
]


def support_rows() -> list[dict]:
    rows = []
    for idx, support in enumerate(SUPPORTS, 1):
        values = [abs(n) ** 3 for n in support if n]
        d = 0
        for value in values:
            d = gcd(d, value)
        rows.append({
            "row_id": f"S{idx:02d}", "fourier_support": support,
            "gcd_nonzero_cubic_frequencies": d,
            "minimal_positive_period": f"2*pi/{d}",
            "return_phase_integer_multiples": [n**3 // d for n in support],
        })
    return rows


def build() -> dict:
    modular = modular_rows()
    dft = [dft_row(p, q) for q in range(2, 19) for p in range(1, q) if gcd(p, q) == 1]
    data = {
        "schema": "hcs-c261-airy-talbot-revival-v1",
        "candidate_id": "HCS-C261",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE_COMMIT,
        "fixed_epoch": FIXED_EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The periodic Airy group has an exact all-rational-time cubic-DFT revival atlas, a minimal full-space period, and complete sampled fixed-mode and finite-support period laws.",
        "frozen_object": {
            "equation": "u_t+u_xxx=0 on R/(2*pi*Z)",
            "fourier_action": "U(t)e_n=exp(i*n^3*t)e_n",
            "phase_space": "L^2(T), with Sobolev domains for powers of the cubic generator",
            "clock": "physical PDE time t",
            "arithmetic_origin": "none; modular cubic phases enter only after a chosen rational sampling time",
            "determinant_convention": "no infinite-dimensional determinant; finite DFT identities are source receipts only",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert--Polya operators",
        },
        "theorem": {
            "unitary_group": "U(t) is a strongly continuous unitary group with self-adjoint Fourier generator D^3, D=-i*d/dx.",
            "minimal_full_period": "U(t)=I on all L^2(T) exactly for t in 2*pi*Z; hence the least positive full-space period is 2*pi.",
            "rational_revival": "For gcd(p,q)=1, U(2*pi*p/q)=sum_{r=0}^{q-1} A_r tau_{2*pi*r/q}, where A_r=q^{-1} sum_s exp(2*pi*i*(p*s^3-s*r)/q).",
            "strobe_order": "The rational strobe U(2*pi*p/q) has exact global order q.",
            "fixed_modes": "Its fixed subspace is the closed span of e_n with q dividing n^3, equivalently L(q) divides n where L(q)=product ell^ceil(v_ell(q)/3).",
            "state_period": "A state with nonzero finite Fourier support S has least positive continuous period 2*pi/gcd{|n|^3:n in S}; constants are fixed for every time.",
            "irrational_sampling": "If t/(2*pi) is irrational, the fixed subspace of U(t) consists exactly of constants.",
            "operator_boundary": "Every U(t) is unitary but noncompact on infinite-dimensional L^2(T), so it is neither trace class nor a target Fredholm determinant input.",
        },
        "receipts": {
            "modular_rows": modular,
            "modular_row_count": len(modular),
            "q_max": 96,
            "fixed_mode_window": [-512, 512],
            "dft_rows": dft,
            "dft_row_count": len(dft),
            "dft_q_max": 18,
            "support_rows": support_rows(),
            "support_row_count": len(SUPPORTS),
            "working_decimal_digits": 90,
            "printed_significant_digits": 68,
            "finite_receipt_boundary": "Finite modular and DFT rows verify conventions; the all-time Hilbert-space theorem is proof-driven.",
        },
        "exact_identities": [
            {"id": "mode_solution", "formula": "U(t)e_n=exp(i*n^3*t)e_n"},
            {"id": "cubic_periodicity", "formula": "(n+q)^3-n^3=q*(3*n^2+3*n*q+q^2)"},
            {"id": "dft_coefficients", "formula": "A_r=q^-1*sum_s exp(2*pi*i*(p*s^3-s*r)/q)"},
            {"id": "parseval", "formula": "sum_r abs(A_r)^2=1"},
            {"id": "full_period", "formula": "min{t>0:U(t)=I}=2*pi"},
            {"id": "strobe_order", "formula": "ord(U(2*pi*p/q))=q when gcd(p,q)=1"},
            {"id": "fixed_stride", "formula": "q|n^3 iff product_l l^ceil(v_l(q)/3) divides n"},
            {"id": "support_period", "formula": "T_S=2*pi/gcd{|n|^3:n in S,n!=0}"},
            {"id": "noncompact", "formula": "unitary images of the Fourier basis have no norm-convergent subsequence"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "A canonical self-adjoint cubic Fourier generator controls the exact unitary group and every rational Talbot strobe.",
            "strongest_failure": "There is no intrinsic arithmetic owner, rational-prime primitive-orbit dictionary, target determinant, or target global analytic structure.",
        },
        "scope_flags": {k: False for k in [
            "uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors",
            "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation",
            "claims_hilbert_polya_operator", "invokes_route_b",
        ]},
        "citations": [
            {"key": "PelloniSmith2024", "claim": "Airy revival and boundary-condition context", "source": "B. Pelloni and D. A. Smith, Studies in Applied Mathematics 153 (2024), e12699", "url": "https://doi.org/10.1111/sapm.12699"},
            {"key": "BoultonFarmakisPelloni2021", "claim": "finite translated-copy revival for periodic linear dispersive problems", "source": "L. Boulton, G. Farmakis, and B. Pelloni, Proceedings of the Royal Society A 477 (2021), 20210241", "url": "https://doi.org/10.1098/rspa.2021.0241"},
        ],
        "nonclaims": [
            "a nonlinear KdV theorem or classification of nonperiodic Airy boundary conditions",
            "closed formulas for every cubic Gauss sum at every modulus",
            "compactness, trace class, or an infinite-dimensional Fredholm determinant for U(t)",
            "an arithmetic Euler product, target divisor, counting law, or functional equation",
            "a Hilbert--Polya operator, target zero match, or Route-B input",
            "literature priority for the classical periodic revival identity",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C261_PRODUCER_PASS",
        "modular_rows": data["receipts"]["modular_row_count"],
        "dft_rows": data["receipts"]["dft_row_count"],
        "support_rows": data["receipts"]["support_row_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
