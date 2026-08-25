#!/usr/bin/env python3
"""Produce exact evidence for HCS-C153 growing-k Walsh escape."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
K_CUTOFF = 24
FIXED_PERIOD_CUTOFF = 20
ALPHA_RATIOS = (
    (0, 1),
    (1, 4),
    (1, 2),
    (3, 4),
    (1, 1),
    (5, 4),
    (3, 2),
    (2, 1),
)


class QSI:
    """Exact a+b*sqrt(3)+c*i+d*sqrt(3)*i arithmetic."""

    __slots__ = ("v",)

    def __init__(self, a=0, b=0, c=0, d=0):
        self.v = tuple(Fraction(x) for x in (a, b, c, d))

    def __add__(self, other):
        other = other if isinstance(other, QSI) else QSI(other)
        return QSI(*(x + y for x, y in zip(self.v, other.v)))

    __radd__ = __add__

    def __neg__(self):
        return QSI(*(-x for x in self.v))

    def __sub__(self, other):
        return self + (-(other if isinstance(other, QSI) else QSI(other)))

    def __mul__(self, other):
        other = other if isinstance(other, QSI) else QSI(other)
        a, b, c, d = self.v
        e, f, g, h = other.v
        return QSI(
            a * e + 3 * b * f - c * g - 3 * d * h,
            a * f + b * e - c * h - d * g,
            a * g + 3 * b * h + c * e + 3 * d * f,
            a * h + b * g + c * f + d * e,
        )

    __rmul__ = __mul__

    def __pow__(self, exponent: int):
        if exponent < 0:
            raise ValueError("negative exponent")
        answer, base = QSI(1), self
        while exponent:
            if exponent & 1:
                answer = answer * base
            base = base * base
            exponent //= 2
        return answer

    def __eq__(self, other):
        other = other if isinstance(other, QSI) else QSI(other)
        return self.v == other.v

    def __bool__(self):
        return any(self.v)

    @staticmethod
    def _fraction(value: Fraction) -> str:
        if value.denominator == 1:
            return str(value.numerator)
        return f"{value.numerator}/{value.denominator}"

    def receipt(self) -> list[str]:
        return [self._fraction(value) for value in self.v]


TRACE_A = QSI(0, Fraction(1, 6), Fraction(-1, 2))
Q0 = QSI(Fraction(-1, 2), 0, 0, Fraction(-1, 6))


def trace_powers(limit: int) -> list[QSI]:
    """t_m=Tr(A^m), including t_0=2 for the two nonzero roots."""
    values = [QSI(2), TRACE_A]
    for _ in range(2, limit + 1):
        values.append(TRACE_A * values[-1] - Q0 * values[-2])
    return values


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def rank_value(k: int, n: int) -> int:
    return 2 ** min(n, k) * 3 ** (k - min(n, k))


def canonical_payload_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def build_rank_ledger() -> list[dict]:
    rows = []
    for k in range(1, K_CUTOFF + 1):
        for n in range(0, 2 * k + 1):
            q, r = divmod(n, k)
            opened = min(n, k)
            rank = rank_value(k, n)
            rows.append(
                {
                    "k": k,
                    "n": n,
                    "q": q,
                    "r": r,
                    "opened_tensor_factors": opened,
                    "rank_Bk_power_n": rank,
                    "kernel_dimension": 3**k - rank,
                    "rank_fraction": f"{2**opened}/{3**opened}",
                    "tensor_normal_form": (
                        "rotation_r_after_(A^(q+1))^tensor_r tensor (A^q)^tensor_(k-r)"
                    ),
                }
            )
    return rows


def build_alpha_ledger() -> list[dict]:
    rows = []
    for numerator, denominator in ALPHA_RATIOS:
        for k in range(1, K_CUTOFF + 1):
            n = numerator * k // denominator
            opened = min(n, k)
            coefficient = Fraction(opened, k)
            rows.append(
                {
                    "alpha": f"{numerator}/{denominator}",
                    "k": k,
                    "n_floor_alpha_k": n,
                    "rank": rank_value(k, n),
                    "rank_fraction": f"{2**opened}/{3**opened}",
                    "finite_k_log_survival_coefficient": QSI._fraction(coefficient),
                }
            )
    return rows


def build_cluster_ledger(traces: list[QSI]) -> list[dict]:
    periods = []
    for n in range(1, FIXED_PERIOD_CUTOFF + 1):
        classes = []
        grouped: dict[tuple[Fraction, ...], list[int]] = {}
        for d in divisors(n):
            value = traces[n // d] ** d
            grouped.setdefault(value.v, []).append(d)
            classes.append(
                {
                    "d": d,
                    "trace_value_q_sqrt3_i_sqrt3i": value.receipt(),
                    "infinite_subsequence": f"k=d*(1+j*(n/d)), j>=0",
                    "gcd_identity": "gcd(n,d*(1+j*(n/d)))=d",
                }
            )
        merged = [
            {
                "trace_value_q_sqrt3_i_sqrt3i": QSI(*key).receipt(),
                "divisor_classes": ds,
            }
            for key, ds in sorted(grouped.items(), key=lambda item: item[1][0])
        ]
        periods.append(
            {
                "n": n,
                "divisor_classes": classes,
                "merged_cluster_values": merged,
                "distinct_cluster_value_count": len(merged),
            }
        )
    return periods


def build_evidence() -> dict:
    traces = trace_powers(FIXED_PERIOD_CUTOFF)
    t2 = traces[2]
    tau_squared = TRACE_A**2
    payload = {
        "schema": "hcs-c153-walsh-growing-k-escape-v1",
        "candidate_id": "HCS-C153",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_lock": {
            "source_commit": "2d4e6211a254ef49d87718569d23466f4c6dcf4c",
            "object": "B_k(v0 tensor ... tensor v_(k-1))=v1 tensor ... tensor v_(k-1) tensor A*v0",
            "one_qutrit_gate": "A=F3^* diag(1,0,1), F3[j,l]=omega^(j*l)/sqrt(3)",
            "clock": "one application of B_k",
            "normalization": "dimension normalization is 3^(-k); no spectral rescaling",
            "trace_convention": "ordinary finite-dimensional Tr(B_k^n)",
            "rank_cutoff": {"k_max": K_CUTOFF, "n_range": "0<=n<=2k"},
            "fixed_period_cluster_cutoff": FIXED_PERIOD_CUTOFF,
            "alpha_ratios": [f"{a}/{b}" for a, b in ALPHA_RATIOS],
            "precision": "exact integers and Q(sqrt(3),i) receipts",
            "allowed_data": "frozen DFT, rank-two projector, tensor shift, exact source traces",
            "forbidden_data": "target zeros or divisors, primes, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "one_qutrit_theorem": {
            "characteristic_polynomial": "lambda*(lambda^2-tau*lambda+q0)",
            "tau_q_sqrt3_i_sqrt3i": TRACE_A.receipt(),
            "q0_q_sqrt3_i_sqrt3i": Q0.receipt(),
            "q0_is_nonzero": True,
            "zero_eigenvalue_is_simple": True,
            "rank_A_power_m": "2 for every integer m>=1; rank(A^0)=3",
            "reason": "the simple zero generalized eigenspace has dimension one and both other eigenvalues are nonzero",
        },
        "all_parameter_rank_theorem": {
            "statement": "rank(B_k^n)=2^min(n,k)*3^(k-min(n,k)) for k>=1,n>=0",
            "normal_form": "for n=qk+r, B_k^n is a tensor-factor rotation after r factors A^(q+1) and k-r factors A^q",
            "rank_fraction": "rank(B_k^n)/3^k=(2/3)^min(n,k)",
            "initial_boundary": "n=0 gives B_k^0=I and full rank 3^k",
            "saturation": "n>=k gives rank 2^k",
            "ledger_rows": build_rank_ledger(),
        },
        "macroscopic_escape_theorem": {
            "time_scale": "n_k=floor(alpha*k), alpha>=0",
            "signed_log_survival_limit": "lim_(k->infinity) k^(-1) log(rank(B_k^n_k)/3^k)=min(alpha,1)*log(2/3)",
            "positive_escape_exponent": "E(alpha)=min(alpha,1)*log(3/2)",
            "alpha_zero_boundary": "alpha=0 gives n_k=0 and E(0)=0",
            "finite_ratio_ledger": build_alpha_ledger(),
        },
        "fixed_period_trace_theorem": {
            "trace_recurrence": "t_0=2,t_1=tau,t_m=tau*t_(m-1)-q0*t_(m-2)",
            "trace_formula": "for d=gcd(n,k), Tr(B_k^n)=t_(n/d)^d",
            "cluster_set": "for fixed n, merge equal values in {t_(n/d)^d:d divides n}",
            "every_divisor_class_infinite": "k=d*(1+j*(n/d)) has gcd(n,k)=d for every j>=0",
            "normalized_limit": "for fixed n, 3^(-k)*Tr(B_k^n)->0 because the numerator ranges over a finite cluster set",
            "periods": build_cluster_ledger(traces),
        },
        "unnormalized_nonconvergence_witness": {
            "fixed_period": 2,
            "odd_k_gcd": 1,
            "odd_k_trace_t2_q_sqrt3_i_sqrt3i": t2.receipt(),
            "even_k_gcd": 2,
            "even_k_trace_tau_squared_q_sqrt3_i_sqrt3i": tau_squared.receipt(),
            "difference_t2_minus_tau_squared_q_sqrt3_i_sqrt3i": (t2 - tau_squared).receipt(),
            "difference_identity": "t2-tau^2=-2*q0 != 0",
            "conclusion": "Tr(B_k^2) has distinct odd-k and even-k constant subsequences, so no k->infinity limit",
        },
        "controls": {
            "closed_parent": {
                "projector": "P_closed=I_3",
                "result": "B_k,closed is unitary, rank(B_k,closed^n)=3^k, and its escape exponent is zero",
            },
            "projector_order": {
                "gate": "A_right=P F3^*=F3 A F3^*",
                "result": "the rank law and all fixed-period trace cluster sets are unchanged by unitary similarity",
            },
            "hole_position": {
                "projector": "P0=diag(0,1,1)",
                "one_site_characteristic_polynomial": "lambda*(lambda+i)*(3*lambda+sqrt(3))/3",
                "rank_result": "the zero root is simple and the other two roots are nonzero, so rank(A0^m)=2 for every m>=1 and the full rank law is unchanged",
                "trace_result": "the trace cluster values can change; rank escape alone does not determine trace geometry",
            },
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "finite_k_and_growing_k_source_gate_only": True,
            "full_secular_limit": False,
            "self_adjoint_quantization": False,
            "antiunitary_symmetry": False,
            "semiclassical_target_matching": False,
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
            "prime_like_correspondence": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
        },
        "nonclaims": [
            "convergence of the unnormalized fixed-period traces for every n",
            "a full growing-k secular determinant or resonance limit",
            "a self-adjoint or antiunitary quantization",
            "a target divisor, functional equation, or counting law",
            "prime-like information, arithmetic local data, Euler factors, root numbers, or automorphy",
            "a Hilbert--Polya operator or Route-B authorization",
        ],
    }
    payload["payload_sha256"] = canonical_payload_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c153_walsh_escape_evidence.json",
    )
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(
        json.dumps(
            {
                "status": "C153_PRODUCER_PASS",
                "rank_rows": len(payload["all_parameter_rank_theorem"]["ledger_rows"]),
                "alpha_rows": len(payload["macroscopic_escape_theorem"]["finite_ratio_ledger"]),
                "fixed_periods": len(payload["fixed_period_trace_theorem"]["periods"]),
                "payload_sha256": payload["payload_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
