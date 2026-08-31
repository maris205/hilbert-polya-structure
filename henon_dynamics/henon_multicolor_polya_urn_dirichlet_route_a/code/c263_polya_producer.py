#!/usr/bin/env python3
"""Deterministic exact certificate for the multicolor classical Polya urn."""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

SOURCE = "98782afe1e754c311ad0736f72ce09dcc7c85c77"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c263_polya_evidence.json"

CASES = [
    ("single", (3,), 1, 6),
    ("binary_symmetric", (1, 1), 1, 8),
    ("binary_asymmetric", (1, 2), 1, 8),
    ("binary_scaled", (2, 3), 2, 7),
    ("ternary_zero_face", (0, 2, 1), 1, 7),
    ("ternary_symmetric", (1, 1, 1), 1, 7),
    ("ternary_fractional_alpha", (1, 2, 3), 2, 6),
    ("four_color", (2, 1, 1, 3), 1, 5),
    ("five_color", (1, 1, 1, 1, 1), 1, 4),
    ("iid_binary", (1, 3), 0, 8),
    ("iid_zero_face", (0, 2, 1), 0, 7),
    ("iid_four_color", (1, 2, 1, 2), 0, 5),
]


def frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def rising(x: Fraction, r: int) -> Fraction:
    ans = Fraction(1)
    for j in range(r):
        ans *= x + j
    return ans


def falling(n: int, r: int) -> int:
    ans = 1
    for j in range(r):
        ans *= n - j
    return ans


def compositions(n: int, k: int):
    if k == 1:
        yield (n,)
        return
    for first in range(n + 1):
        for rest in compositions(n - first, k - 1):
            yield (first,) + rest


def multiindices(k: int, max_degree: int):
    for degree in range(1, max_degree + 1):
        yield from compositions(degree, k)


def multinomial(n: int, counts: tuple[int, ...]) -> int:
    out = math.factorial(n)
    for value in counts:
        out //= math.factorial(value)
    return out


def word_probability(word: tuple[int, ...], masses: tuple[int, ...], c: int) -> Fraction:
    total = sum(masses)
    counts = [0] * len(masses)
    ans = Fraction(1)
    for t, color in enumerate(word):
        ans *= Fraction(masses[color] + c * counts[color], total + c * t)
        counts[color] += 1
    return ans


def closed_count_probability(n: int, counts: tuple[int, ...], masses: tuple[int, ...], c: int) -> Fraction:
    total = sum(masses)
    if c == 0:
        ans = Fraction(multinomial(n, counts), 1)
        for mass, value in zip(masses, counts):
            ans *= Fraction(mass, total) ** value
        return ans
    alpha = [Fraction(mass, c) for mass in masses]
    A = sum(alpha)
    ans = Fraction(multinomial(n, counts), 1)
    for parameter, value in zip(alpha, counts):
        ans *= rising(parameter, value)
    return ans / rising(A, n)


def recursive_distributions(masses: tuple[int, ...], c: int, max_n: int):
    levels = [{(0,) * len(masses): Fraction(1)}]
    total = sum(masses)
    for n in range(max_n):
        nxt: dict[tuple[int, ...], Fraction] = {}
        for counts, probability in levels[-1].items():
            for color in range(len(masses)):
                predictive = Fraction(masses[color] + c * counts[color], total + c * n)
                target = list(counts)
                target[color] += 1
                key = tuple(target)
                nxt[key] = nxt.get(key, Fraction(0)) + probability * predictive
        levels.append(nxt)
    return levels


def beta_binomial(n: int, x: int, mass: int, total: int, c: int) -> Fraction:
    if c == 0:
        return Fraction(math.comb(n, x), 1) * Fraction(mass, total) ** x * Fraction(total - mass, total) ** (n - x)
    a = Fraction(mass, c)
    b = Fraction(total - mass, c)
    return Fraction(math.comb(n, x), 1) * rising(a, x) * rising(b, n - x) / rising(a + b, n)


def factorial_closed(n: int, r: tuple[int, ...], masses: tuple[int, ...], c: int) -> Fraction:
    R = sum(r)
    total = sum(masses)
    ans = Fraction(falling(n, R), 1)
    if c == 0:
        for mass, degree in zip(masses, r):
            ans *= Fraction(mass, total) ** degree
        return ans
    alpha = [Fraction(mass, c) for mass in masses]
    for parameter, degree in zip(alpha, r):
        ans *= rising(parameter, degree)
    return ans / rising(sum(alpha), R)


def case_ledger(case_id: str, masses: tuple[int, ...], c: int, max_n: int):
    K = len(masses)
    total = sum(masses)
    levels = recursive_distributions(masses, c, max_n)
    composition_rows = []
    marginal_rows = []
    moment_rows = []
    martingale_rows = []
    de_finetti_rows = []
    for n, distribution in enumerate(levels):
        for counts in sorted(distribution):
            recursive = distribution[counts]
            closed = closed_count_probability(n, counts, masses, c)
            composition_rows.append({
                "case_id": case_id, "n": n, "counts": list(counts),
                "recursive_probability": frac(recursive), "closed_probability": frac(closed),
                "multiplicity": multinomial(n, counts),
            })
        for color in range(K):
            for x in range(n + 1):
                observed = sum(p for counts, p in distribution.items() if counts[color] == x)
                marginal_rows.append({
                    "case_id": case_id, "n": n, "color": color, "x": x,
                    "observed": frac(observed),
                    "closed": frac(beta_binomial(n, x, masses[color], total, c)),
                    "family": "binomial" if c == 0 else "beta_binomial",
                })
        mean = []
        covariance = []
        for i in range(K):
            mean_i = sum(Fraction(counts[i]) * p for counts, p in distribution.items())
            mean.append(frac(mean_i))
            row = []
            for j in range(K):
                second = sum(Fraction(counts[i] * counts[j]) * p for counts, p in distribution.items())
                mean_j = sum(Fraction(counts[j]) * p for counts, p in distribution.items())
                row.append(frac(second - mean_i * mean_j))
            covariance.append(row)
        moment_rows.append({"case_id": case_id, "n": n, "mean": mean, "covariance": covariance})
        if n < max_n:
            for counts in sorted(distribution):
                denom = total + c * n
                for i in range(K):
                    current = Fraction(masses[i] + c * counts[i], denom)
                    expected_next = Fraction(0)
                    for color in range(K):
                        predictive = Fraction(masses[color] + c * counts[color], denom)
                        numerator = masses[i] + c * (counts[i] + int(color == i))
                        expected_next += predictive * Fraction(numerator, denom + c)
                    martingale_rows.append({
                        "case_id": case_id, "n": n, "counts": list(counts), "color": i,
                        "current": frac(current), "expected_next": frac(expected_next),
                    })
    factorial_rows = []
    for n, distribution in enumerate(levels):
        for r in multiindices(K, min(4, n)):
            observed = sum(
                Fraction(math.prod(falling(counts[i], r[i]) for i in range(K))) * probability
                for counts, probability in distribution.items()
            )
            factorial_rows.append({
                "case_id": case_id, "n": n, "multiindex": list(r),
                "observed": frac(observed), "closed": frac(factorial_closed(n, r, masses, c)),
            })
    words = []
    aggregate: dict[tuple[int, ...], list[Fraction]] = {}
    for word in itertools.product(range(K), repeat=max_n):
        probability = word_probability(word, masses, c)
        counts = tuple(word.count(i) for i in range(K))
        aggregate.setdefault(counts, []).append(probability)
        words.append({
            "case_id": case_id, "word": list(word), "counts": list(counts),
            "probability": frac(probability),
        })
    exchangeability_rows = []
    for counts, probabilities in sorted(aggregate.items()):
        per_word = probabilities[0]
        exchangeability_rows.append({
            "case_id": case_id, "counts": list(counts),
            "word_count": len(probabilities), "distinct_probabilities": len(set(probabilities)),
            "per_word_probability": frac(per_word),
            "aggregate_probability": frac(sum(probabilities)),
        })
        if c > 0:
            alpha = [Fraction(mass, c) for mass in masses]
            mixture = Fraction(1)
            for parameter, value in zip(alpha, counts):
                mixture *= rising(parameter, value)
            mixture /= rising(sum(alpha), max_n)
            de_finetti_rows.append({
                "case_id": case_id, "counts": list(counts),
                "ordered_word_probability": frac(per_word),
                "dirichlet_monomial_moment": frac(mixture),
            })
    return {
        "case": {
            "case_id": case_id, "K": K, "initial_masses": list(masses), "reinforcement": c,
            "max_n": max_n, "active_colors": sum(m > 0 for m in masses),
            "normalization": None if c == 0 else [frac(Fraction(m, c)) for m in masses],
        },
        "composition_rows": composition_rows,
        "marginal_rows": marginal_rows,
        "moment_rows": moment_rows,
        "factorial_rows": factorial_rows,
        "martingale_rows": martingale_rows,
        "ordered_word_rows": words,
        "exchangeability_rows": exchangeability_rows,
        "de_finetti_rows": de_finetti_rows,
    }


def build() -> dict:
    ledgers = [case_ledger(case_id, masses, c, max_n) for case_id, masses, c, max_n in CASES]
    regression = {
        "cases": [entry["case"] for entry in ledgers],
        "composition_rows": sum((entry["composition_rows"] for entry in ledgers), []),
        "marginal_rows": sum((entry["marginal_rows"] for entry in ledgers), []),
        "moment_rows": sum((entry["moment_rows"] for entry in ledgers), []),
        "factorial_rows": sum((entry["factorial_rows"] for entry in ledgers), []),
        "martingale_rows": sum((entry["martingale_rows"] for entry in ledgers), []),
        "ordered_word_rows": sum((entry["ordered_word_rows"] for entry in ledgers), []),
        "exchangeability_rows": sum((entry["exchangeability_rows"] for entry in ledgers), []),
        "de_finetti_rows": sum((entry["de_finetti_rows"] for entry in ledgers), []),
    }
    regression["counts"] = {key: len(value) for key, value in regression.items() if key.endswith("_rows")}
    data = {
        "schema": "hcs-c263-multicolor-polya-dirichlet-v1",
        "candidate_id": "HCS-C263",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVAL},
        "headline": (
            "The K-color classical Polya urn closes exchangeable ordered words, the full "
            "Dirichlet-multinomial finite-time law, every factorial moment, and the Dirichlet limit."
        ),
        "frozen_object": {
            "state": "K nonnegative masses with strictly positive total mass",
            "update": "draw proportionally to mass, replace, and add c>=0 mass to the drawn color",
            "clock": "one draw and reinforcement update",
            "c_positive_normalization": "alpha_i=a_i/c; A=sum_i alpha_i",
            "c_zero_policy": "iid draws with probabilities a_i/sum_j a_j; alpha is not defined",
            "zero_mass_policy": "a zero-mass color is never drawn and the law reduces to the active face",
            "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor or Hilbert--Polya operator",
        },
        "theorem": {
            "ordered_words": "For c>0, every word with color counts n_i has probability prod_i (alpha_i)_{n_i}/(A)_n; order is immaterial.",
            "counts": "The count vector is Dirichlet-multinomial: n!/prod n_i! times the ordered-word probability.",
            "marginals": "Each color count is beta-binomial with parameters n, alpha_i, A-alpha_i.",
            "means": "E N_i=n alpha_i/A.",
            "covariance": "Var N_i=n alpha_i(A-alpha_i)(A+n)/(A^2(A+1)); Cov(N_i,N_j)=-n alpha_i alpha_j(A+n)/(A^2(A+1)).",
            "factorial_moments": "E prod_i (N_i)_[r_i]=(n)_[R] prod_i (alpha_i)_(r_i)/(A)_(R).",
            "martingale": "P_i(n)=(alpha_i+N_i(n))/(A+n) is a bounded martingale.",
            "limit": "P(n) converges almost surely and in every finite Lp to a Dirichlet(alpha) vector on the active face.",
            "de_finetti": "The finite word law equals the Dirichlet mixture of iid categorical words; conversely this mixture reproduces the predictive urn rule.",
            "boundaries": "c=0 is iid multinomial and uses no alpha; zero masses delete colors; K=1 is deterministic.",
            "route_boundary": "The increasing-mass chain has no source periodic-orbit clock and supplies no target arithmetic or spectral identification.",
        },
        "regression": regression,
        "exact_identities": [
            {"identity_id": "exchangeability", "formula": "Pr(word)=prod_i (alpha_i)_(n_i)/(A)_n"},
            {"identity_id": "dirichlet_multinomial", "formula": "Pr(N=n)=multinomial(n;n_i)Pr(word)"},
            {"identity_id": "vandermonde", "formula": "sum_{sum n_i=n} multinomial prod_i(alpha_i)_(n_i)=(A)_n"},
            {"identity_id": "predictive", "formula": "Pr(X_{n+1}=i|N(n))=(alpha_i+N_i)/(A+n)"},
            {"identity_id": "martingale", "formula": "E[P_i(n+1)|F_n]=P_i(n)"},
            {"identity_id": "factorial", "formula": "E prod_i(N_i)_[r_i]=(n)_[R]prod_i(alpha_i)_(r_i)/(A)_(R)"},
            {"identity_id": "de_finetti", "formula": "E_Dirichlet prod_i Theta_i^(n_i)=prod_i(alpha_i)_(n_i)/(A)_n"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "A complete finite-time and limiting probability theorem with an exact directing measure.",
            "decisive_obstruction": "Total mass grows with source time, so no nontrivial recurrence or primitive source-orbit ledger exists.",
        },
        "scope_flags": {
            "uses_target_local_data": False,
            "claims_euler_factor": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor": False,
            "claims_target_functional_equation": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "nonclaims": [
            "No workspace novelty label is a literature-priority claim.",
            "No finite regression prefix replaces the all-parameter proof.",
            "No alpha parameter is assigned on the c=0 face.",
            "No source probability identity is promoted to target arithmetic data.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    counts = data["regression"]["counts"]
    print(
        "C263_PRODUCER_PASS "
        f"cases={len(data['regression']['cases'])} words={counts['ordered_word_rows']} "
        f"compositions={counts['composition_rows']} factorial={counts['factorial_rows']} "
        f"payload_sha256={data['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
