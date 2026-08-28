#!/usr/bin/env python3
"""Canonical exact/numerical certificate for the Kingman coalescent."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

SOURCE_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c215_kingman_evidence.json"
N_MAX = 12
TIME_VALUES = [F(0), F(1, 5), F(1), F(2)]
S_VALUES = [F(0), F(1, 5), F(1), F(3)]
ELL_VALUES = [F(0), F(1, 5), F(1), F(2), F(4)]
WORKING_DECIMAL_DIGITS = 100
SERIALIZED_SIGNIFICANT_DIGITS = 82


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(value: F) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def fmt(value: mp.mpf) -> str:
    return mp.nstr(value, SERIALIZED_SIGNIFICANT_DIGITS, strip_zeros=False)


def rate(k: int) -> F:
    return F(k * (k - 1), 2)


def hypo_transition(i: int, j: int, t: F) -> mp.mpf:
    """Pure-death transition from i blocks to j blocks."""
    if j < 1 or j > i:
        return mp.mpf(0)
    if t == 0:
        return mp.mpf(1) if i == j else mp.mpf(0)
    if i == j:
        return mp.exp(-mpq(rate(i)) * mpq(t))
    numerator = mp.mpf(1)
    for m in range(j + 1, i + 1):
        numerator *= mpq(rate(m))
    total = mp.mpf(0)
    for ell in range(j, i + 1):
        denominator = mp.mpf(1)
        for m in range(j, i + 1):
            if m != ell:
                denominator *= mpq(rate(m) - rate(ell))
        total += mp.exp(-mpq(rate(ell)) * mpq(t)) / denominator
    return numerator * total


def mrca_lt(n: int, s: F) -> mp.mpf:
    value = mp.mpf(1)
    for k in range(2, n + 1):
        value *= mpq(rate(k)) / (mpq(rate(k)) + mpq(s))
    return value


def mrca_mean(n: int) -> mp.mpf:
    return sum((1 / mpq(rate(k)) for k in range(2, n + 1)), mp.mpf(0))


def mrca_variance(n: int) -> mp.mpf:
    return sum((1 / (mpq(rate(k)) ** 2) for k in range(2, n + 1)), mp.mpf(0))


def branch_lt(n: int, s: F) -> mp.mpf:
    value = mp.mpf(1)
    for j in range(1, n):
        rr = mp.mpf(j) / 2
        value *= rr / (rr + mpq(s))
    return value


def branch_cdf(n: int, ell: F) -> mp.mpf:
    if n == 1:
        return mp.mpf(1)
    return (1 - mp.exp(-mpq(ell) / 2)) ** (n - 1)


def harmonic(n: int, order: int = 1) -> mp.mpf:
    return sum((mp.mpf(1) / (j ** order) for j in range(1, n + 1)), mp.mpf(0))


def partitions(items: tuple[int, ...]) -> list[tuple[tuple[int, ...], ...]]:
    """Small canonical set-partition enumerator for Bell-number regression."""
    if not items:
        return [tuple()]
    first, rest = items[0], items[1:]
    out: list[tuple[tuple[int, ...], ...]] = []
    for part in partitions(rest):
        # Put first into a new block.
        out.append(((first,),) + part)
        # Or insert into each existing block, preserving canonical order.
        for idx in range(len(part)):
            blocks = [tuple(block) for block in part]
            blocks[idx] = tuple(sorted((first,) + blocks[idx]))
            out.append(tuple(blocks))
    return out


def build() -> dict:
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    transition_rows = []
    for i in range(1, N_MAX + 1):
        for j in range(1, i + 1):
            for t in TIME_VALUES:
                transition_rows.append({
                    "case_id": f"i{i}_j{j}_t{t}", "i": i, "j": j, "t": str(t),
                    "probability": fmt(hypo_transition(i, j, t)),
                })

    holding_rows = []
    for k in range(1, N_MAX + 1):
        if k == 1:
            holding_rows.append({"case_id": "k1_absorbing", "k": 1, "lambda": "0", "mean": "0", "variance": "0", "pair_count": 0, "pair_probability": "0"})
        else:
            lam = rate(k)
            holding_rows.append({
                "case_id": f"k{k}", "k": k, "lambda": str(lam),
                "mean": fmt(1 / mpq(lam)), "variance": fmt(1 / (mpq(lam) ** 2)),
                "pair_count": k * (k - 1) // 2, "pair_probability": fmt(mp.mpf(1) / (k * (k - 1) // 2)),
            })

    mrca_rows = []
    for n in range(1, N_MAX + 1):
        for s in S_VALUES:
            mrca_rows.append({
                "case_id": f"n{n}_s{s}", "n": n, "s": str(s),
                "laplace": fmt(mrca_lt(n, s)), "mean": fmt(mrca_mean(n)), "variance": fmt(mrca_variance(n)),
            })

    branch_rows = []
    for n in range(1, N_MAX + 1):
        for ell in ELL_VALUES:
            branch_rows.append({
                "case_id": f"n{n}_ell{ell}", "n": n, "ell": str(ell),
                "laplace_at_one": fmt(branch_lt(n, F(1))), "cdf": fmt(branch_cdf(n, ell)),
                "mean": fmt(2 * harmonic(n - 1)), "variance": fmt(4 * harmonic(n - 1, 2)),
            })

    partition_rows = []
    for n in range(1, 9):
        count = len(partitions(tuple(range(n))))
        pair_count = n * (n - 1) // 2
        partition_rows.append({
            "case_id": f"n{n}", "n": n, "bell_number": count,
            "pair_count_at_n": pair_count,
            "uniform_pair_probability": "0" if pair_count == 0 else fmt(mp.mpf(1) / pair_count),
        })

    infinite_variance = 4 * (2 * mp.zeta(2) - 3)
    limit_rows = [{
        "case_id": "n_to_infinity", "absorption_probability": "1", "mrca_mean_limit": "2",
        "mrca_variance_limit": fmt(infinite_variance),
        "mrca_laplace_limit": "product_{k=2}^infinity lambda_k/(lambda_k+s)",
        "coupling_statement": "under the standard projective coupling T_n increases to a finite T_infinity almost surely",
    }]

    data = {
        "schema": "hcs-c215-kingman-coalescent-v1", "candidate_id": "HCS-C215", "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The partition-valued Kingman coalescent has an exact all-n genealogy, hypoexponential block transitions and branch-length laws",
        "frozen_object": {
            "phase_space": "partitions of [n] for every n>=1, with projective restriction maps",
            "process": "each unordered pair of current blocks merges at rate 1; the block-counting state is K_t",
            "generator": "Q_{k,k-1}=lambda_k=C(k,2), Q_{k,k}=-lambda_k for k>=2, and Q_{1,1}=0",
            "parameters": "sample size n>=1 and physical time t>=0",
            "clock": "physical elapsed time; no fitted or logarithmic clock",
            "normalization": "probability on labelled partitions; conditional on k blocks each merger pair is uniform",
            "determinant_convention": "none; finite Markov transition determinants are not Artin--Mazur zeta functions",
            "arithmetic_origin": "none; this is a scope-locked non-arithmetic genealogical process",
            "allowed_data": "exact integer block rates, rational time/Laplace sentinels and source-local partition combinatorics",
            "forbidden_data": "prime/zero tables, target labels, fitted rates, Euler factors and external observations",
        },
        "theorem": {
            "partition_owner": "Kingman n-coalescent on labelled set partitions, consistent under restriction from n+1 to n",
            "block_rates": "K_t is pure death k->k-1 with lambda_k=C(k,2), k>=2, and state 1 absorbing",
            "hypoexponential_transition": "p_{ij}(t)=prod_{m=j+1}^i lambda_m * sum_{ell=j}^i exp(-lambda_ell*t)/prod_{m=j,m!=ell}^i(lambda_m-lambda_ell), with p_{ii}=exp(-lambda_i*t)",
            "independent_holdings": "holding times E_k are independent Exp(lambda_k), independent of the uniform pair-merger jump chain",
            "mrca_laplace": "E[exp(-s T_n)]=prod_{k=2}^n lambda_k/(lambda_k+s)",
            "mrca_moments": "E[T_n]=sum_{k=2}^n 1/lambda_k=2(1-1/n), Var(T_n)=sum_{k=2}^n 1/lambda_k^2",
            "infinite_absorption": "under projective coupling T_n increases to finite T_infinity almost surely; mean limit 2 and variance limit 4*(2*zeta(2)-3)",
            "total_branch_length": "L_n=sum_{k=2}^n k E_k is a sum of independent Exp((k-1)/2) variables; LT=prod_{j=1}^{n-1}(j/2)/(j/2+s), mean=2 H_{n-1}, variance=4 H_{n-1}^{(2)}",
            "branch_cdf": "P(L_n<=ell)=(1-exp(-ell/2))^(n-1) for ell>=0, with the n=1 convention L_1=0",
            "n1_boundary": "n=1 has one partition, K_t=1, T_1=L_1=0 and all transforms equal 1",
            "determinant_boundary": "a finite Markov matrix determinant or trace-log is not an Artin--Mazur dynamical zeta and is not used as one",
        },
        "regression": {
            "n_max": N_MAX, "time_values": [str(x) for x in TIME_VALUES], "s_values": [str(x) for x in S_VALUES], "ell_values": [str(x) for x in ELL_VALUES],
            "transition_rows": transition_rows, "holding_rows": holding_rows, "mrca_rows": mrca_rows, "branch_rows": branch_rows, "partition_rows": partition_rows, "limit_rows": limit_rows,
        },
        "summary": {
            "transition_row_count": len(transition_rows), "holding_row_count": len(holding_rows), "mrca_row_count": len(mrca_rows), "branch_row_count": len(branch_rows), "partition_row_count": len(partition_rows), "limit_row_count": len(limit_rows),
            "n_max": N_MAX, "serialized_decimal_digits": SERIALIZED_SIGNIFICANT_DIGITS,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "A source-locked partition genealogy closes all-n block transitions, independent holding times, MRCA and total-branch-length laws including exact CDF.",
            "strongest_failure": "There is no intrinsic rational-prime carrier, primitive periodic-orbit clock, arithmetic divisor, or natural Hilbert-Polya lift.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [{"key": "Kingman1982", "claim": "partition-valued coalescent and pure-death block-counting construction", "title": "The coalescent", "authors": "John F. C. Kingman", "venue": "Stochastic Processes and their Applications 13, 235--248", "date": "1982", "url": "https://doi.org/10.1016/0304-4149(82)90011-4", "persistent_url": "https://doi.org/10.1016/0304-4149(82)90011-4"}],
        "nonclaims": [
            "priority or novelty for the Kingman coalescent or its classical distribution formulae",
            "a finite n grid proves the all-n projective theorem",
            "a Markov transition determinant, trace-log, or Laplace product is an Artin--Mazur zeta, Euler factor, or target determinant",
            "genealogical block counts or branch lengths have arithmetic-prime meaning",
            "a Hilbert-Polya operator, target divisor, Euler factor, root number, automorphy, external review, or Route-B authorization",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    out = ap.parse_args().output; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    obj = json.loads(out.read_text())
    print(json.dumps({"status": "C215_PRODUCER_PASS", "output": str(out), "payload_sha256": obj["payload_sha256"], "transition_rows": obj["summary"]["transition_row_count"], "branch_rows": obj["summary"]["branch_row_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
