#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C273."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "results/c273_sparre_andersen_evidence.json"
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788134400
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90


def q(n: int) -> Q:
    return Q(math.comb(2 * n, n), 4**n)


def qstr(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def permutation_control(n: int) -> dict:
    """Finite exchangeable/sign-invariant control with no subset-sum ties."""
    magnitudes = tuple(3**j for j in range(n))
    positive_count = Counter()
    maximum_time = Counter()
    survival = 0
    ties = 0
    histories = 0
    for perm in itertools.permutations(magnitudes):
        for signs in itertools.product((-1, 1), repeat=n):
            histories += 1
            sums = [0]
            for magnitude, sign in zip(perm, signs):
                sums.append(sums[-1] + sign * magnitude)
            positive_count[sum(value > 0 for value in sums[1:])] += 1
            maximum = max(sums)
            if sums.count(maximum) != 1:
                ties += 1
            else:
                maximum_time[sums.index(maximum)] += 1
            if all(value > 0 for value in sums[1:]):
                survival += 1
    return {
        "n": n,
        "magnitudes": list(magnitudes),
        "histories": histories,
        "ties": ties,
        "survival_count": survival,
        "positive_count_histogram": [positive_count[k] for k in range(n + 1)],
        "maximum_time_histogram": [maximum_time[k] for k in range(n + 1)],
    }


def atomic_control(n: int) -> dict:
    """Simple symmetric walk: an explicit failure control when ties are possible."""
    strict_count = Counter()
    unique_maximum = Counter()
    tied_maxima = 0
    nonnegative_survival = 0
    strict_survival = 0
    for increments in itertools.product((-1, 1), repeat=n):
        sums = [0]
        for increment in increments:
            sums.append(sums[-1] + increment)
        strict_count[sum(value > 0 for value in sums[1:])] += 1
        maximum = max(sums)
        if sums.count(maximum) == 1:
            unique_maximum[sums.index(maximum)] += 1
        else:
            tied_maxima += 1
        nonnegative_survival += int(all(value >= 0 for value in sums[1:]))
        strict_survival += int(all(value > 0 for value in sums[1:]))
    return {
        "n": n,
        "histories": 2**n,
        "strict_positive_count_histogram": [strict_count[k] for k in range(n + 1)],
        "unique_maximum_time_histogram": [unique_maximum[k] for k in range(n + 1)],
        "tied_maximum_histories": tied_maxima,
        "nonnegative_survival_count": nonnegative_survival,
        "strict_survival_count": strict_survival,
    }


def scaling_receipt(n: int, k: int) -> dict:
    mass = q(k) * q(n - k)
    x = mp.mpf(k) / n
    scaled = mp.mpf(n * mass.numerator) / mass.denominator
    density = 1 / (mp.pi * mp.sqrt(x * (1 - x)))
    return {
        "n": n,
        "k": k,
        "x": f"{k}/{n}",
        "mass": qstr(mass),
        "n_times_mass": mp.nstr(scaled, 70),
        "arcsine_density": mp.nstr(density, 70),
        "absolute_error": mp.nstr(abs(scaled - density), 70),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    q_rows = []
    arcsine_rows = []
    for n in range(41):
        first = Q(0) if n == 0 else q(n - 1) - q(n)
        convolution = sum((q(k) * q(n - k) for k in range(n + 1)), Q(0))
        q_rows.append(
            {
                "n": n,
                "q_n": qstr(q(n)),
                "first_strict_descent_n": qstr(first),
                "arcsine_convolution": qstr(convolution),
            }
        )
        if n <= 32:
            arcsine_rows.append(
                {
                    "n": n,
                    "cells": [qstr(q(k) * q(n - k)) for k in range(n + 1)],
                }
            )

    controls = [permutation_control(n) for n in range(1, 8)]
    atomic = [atomic_control(n) for n in range(1, 9)]
    scaling = [
        scaling_receipt(n, k)
        for n in (64, 128, 256, 512)
        for k in (n // 4, n // 2, 3 * n // 4)
    ]
    history_count = sum(row["histories"] for row in controls)
    arcsine_cells = sum(len(row["cells"]) for row in arcsine_rows)

    data = {
        "schema": "hcs-c273-sparre-andersen-v1",
        "candidate_id": "HCS-C273",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "increments": "iid real-valued, continuous, and symmetric about zero",
            "partial_sums": "S_0=0 and S_n=X_1+...+X_n",
            "no_ties": "P(S_j=S_k for some 0<=j<k<=n)=0 for every finite n",
            "survival": "q_n=P(S_1>0,...,S_n>0), q_0=1",
            "first_descent": "tau_minus=inf{n>=1:S_n<0}",
            "positive_count": "N_n=#{1<=j<=n:S_j>0}",
            "maximum_time": "M_n=the unique argmax of S_0,...,S_n",
        },
        "theorem_contract": {
            "survival": "q_n=binom(2n,n)/4^n",
            "generating_function": "sum_{n>=0}q_n z^n=(1-z)^(-1/2), |z|<1",
            "first_descent": "P(tau_minus>n)=q_n and P(tau_minus=n)=q_{n-1}-q_n=q_{n-1}/(2n)",
            "discrete_arcsine": "P(N_n=k)=P(M_n=k)=q_k q_{n-k}, 0<=k<=n",
            "scaling": "N_n/n and M_n/n converge weakly to Beta(1/2,1/2)",
            "atomic_boundary": "without no-ties, strict/nonnegative conventions and maximum tie rules change the laws",
        },
        "proof_contract": {
            "maximum_factorization": "independent premaximum and postmaximum blocks give P(M_n=k)=q_k q_{n-k}",
            "normalization": "uniqueness of M_n gives sum_k q_k q_{n-k}=1 and hence Q(z)^2=(1-z)^(-1)",
            "positive_count": "the Sparre-Andersen permutation-cycle lemma gives the bivariate generating function",
            "scaling": "central-binomial asymptotics and a bulk Riemann-sum argument give the arcsine density",
            "finite_evidence_role": "regression and convention control only, not proof of distribution-free universality",
        },
        "regression": {
            "q_rows": q_rows,
            "arcsine_rows": arcsine_rows,
            "permutation_controls": controls,
            "atomic_controls": atomic,
            "scaling_receipts": scaling,
            "counts": {
                "q_rows": len(q_rows),
                "arcsine_rows": len(arcsine_rows),
                "arcsine_cells": arcsine_cells,
                "permutation_families": len(controls),
                "permutation_histories": history_count,
                "atomic_families": len(atomic),
                "scaling_receipts": len(scaling),
            },
        },
        "analytic_proof_obligations": [
            "unique maximum under the no-ties hypothesis",
            "pre/post maximum factorization",
            "convolution normalization and square-root branch",
            "Sparre-Andersen permutation-cycle lemma for positive counts",
            "first strict descent telescoping law",
            "arcsine weak limit with endpoint control",
            "atomic-increment counterexample",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "target_divisor": False,
            "functional_equation": False,
            "hilbert_polya_operator": False,
        },
        "nonclaims": [
            "No literature-priority claim is made.",
            "Finite permutation enumeration is not a proof of the universal theorem.",
            "Probability generating functions are not arithmetic Euler products or target determinants.",
        ],
        "source": {
            "author": "Erik Sparre Andersen",
            "title": "On the fluctuations of sums of random variables",
            "journal": "Mathematica Scandinavica",
            "volume": "1",
            "year": 1953,
            "pages": "263--285",
            "doi": "10.7146/math.scand.a-10385",
            "role": "primary fluctuation-theorem source",
        },
    }
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    print(
        "C273_PRODUCER_PASS "
        f"q_rows={len(q_rows)} arcsine_cells={arcsine_cells} "
        f"histories={history_count} payload={data['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
