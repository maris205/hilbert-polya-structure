#!/usr/bin/env python3
"""Deterministic exact/高精度 certificate for the classical Lüroth map.

The branch indexed by m>=2 is
    I_m=(1/m,1/(m-1)],  T(x)=m(m-1)x-(m-1),
with inverse phi_m(y)=(y+m-1)/(m(m-1)).  Finite words have affine inverse
branches and therefore one exact periodic point and a product multiplier.
The alphabet is countable; finite-M rows are regression slices only.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import itertools
import json
import math
import os
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "489506cf92bfed721f94f22dd0444a60427f90a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c241_luroth_evidence.json"
mp.mp.dps = 90


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mpmath_fraction(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def decimal(value: mp.mpf | Fraction | int, digits: int = 64) -> str:
    x = mpmath_fraction(value) if isinstance(value, Fraction) else mp.mpf(value)
    if abs(x) < mp.mpf("1e-82"):
        return "0.0"
    return mp.nstr(x, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def branch_slope(m: int) -> int:
    return m * (m - 1)


def inverse_affine(m: int, y: Fraction) -> Fraction:
    return (y + (m - 1)) / branch_slope(m)


def affine_word(word: tuple[int, ...]) -> tuple[Fraction, Fraction]:
    """Return (u,v) for Phi_word(y)=u*y+v."""
    u, v = Fraction(1), Fraction(0)
    for m in reversed(word):
        a = branch_slope(m)
        u, v = u / a, (v + (m - 1)) / a
    return u, v


def fixed_point(word: tuple[int, ...]) -> tuple[Fraction, Fraction, Fraction]:
    u, v = affine_word(word)
    x = v / (1 - u)
    product = math.prod(branch_slope(m) for m in word)
    return x, u, Fraction(product)


def branch_index(x: Fraction) -> int:
    assert x > 0
    return x.denominator // x.numerator + 1


def map_branch(x: Fraction, m: int) -> Fraction:
    return branch_slope(m) * x - (m - 1)


def itinerary(x: Fraction, length: int) -> tuple[int, ...]:
    y = x
    out: list[int] = []
    for _ in range(length):
        m = branch_index(y)
        out.append(m)
        y = map_branch(y, m)
    return tuple(out)


def rotations(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [word[j:] + word[:j] for j in range(len(word))]


def canonical_word(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotations(word))


def primitive_period(word: tuple[int, ...]) -> int:
    r = len(word)
    for d in range(1, r + 1):
        if r % d == 0 and word == word[:d] * (r // d):
            return d
    raise AssertionError("period missing")


def primitive(word: tuple[int, ...]) -> bool:
    return primitive_period(word) == len(word)


def word_row(word: tuple[int, ...]) -> dict:
    x, u, product = fixed_point(word)
    orbit = itinerary(x, len(word))
    assert orbit == word and map_branch(x, word[0]) >= 0
    return {
        "word": list(word),
        "length": len(word),
        "canonical_word": list(canonical_word(word)),
        "primitive": primitive(word),
        "primitive_period": primitive_period(word),
        "branch_product": product.numerator,
        "affine_u_num": u.numerator,
        "affine_u_den": u.denominator,
        "affine_v_num": (x * (1 - u)).numerator,
        "affine_v_den": (x * (1 - u)).denominator,
        "fixed_x_num": x.numerator,
        "fixed_x_den": x.denominator,
        "fixed_x_decimal": decimal(x),
        "multiplier": product.numerator,
        "itinerary": list(orbit),
        "return_x_num": x.numerator,
        "return_x_den": x.denominator,
        "orientation": "forward",
        "weight_s1_num": 1,
        "weight_s1_den": product.numerator,
    }


def branch_rows() -> list[dict]:
    rows = []
    for m in range(2, 13):
        a = branch_slope(m)
        rows.append({
            "branch_m": m,
            "interval_left": ftext(Fraction(1, m)),
            "interval_right": ftext(Fraction(1, m - 1)),
            "slope": a,
            "inverse_at_zero": ftext(inverse_affine(m, Fraction(0))),
            "inverse_at_one": ftext(inverse_affine(m, Fraction(1))),
            "weight_s1": ftext(Fraction(1, a)),
        })
    return rows


def necklace_count(alphabet_size: int, length: int) -> int:
    # Primitive necklaces over q symbols, by Möbius inversion.
    total = 0
    for d in range(1, length + 1):
        if length % d == 0:
            # mu(d) without importing the producer's helper into checkers
            x, squarefree, sign, p = d, True, 1, 2
            while p * p <= x:
                if x % p == 0:
                    x //= p
                    sign = -sign
                    if x % p == 0:
                        squarefree = False
                    while x % p == 0:
                        x //= p
                p += 1 if p == 2 else 2
            if x > 1:
                sign = -sign
            mu = sign if squarefree else 0
            total += mu * alphabet_size ** (length // d)
    return total // length


def necklace_rows() -> list[dict]:
    rows = []
    for M in range(3, 9):
        q = M - 1
        for r in range(1, 6):
            rows.append({"cutoff_M": M, "alphabet_size": q, "length": r, "primitive_necklaces": necklace_count(q, r), "all_words": q ** r})
    return rows


def weighted_rows() -> list[dict]:
    rows = []
    s_values = [Fraction(1), Fraction(3, 2), Fraction(3, 4), Fraction(1, 2)]
    z_values = [Fraction(1, 3), Fraction(1, 2)]
    for M in range(2, 13):
        for s in s_values:
            sigma = mpmath_fraction(s)
            A = mp.mpf("0")
            for m in range(2, M + 1):
                A += mp.power(branch_slope(m), -sigma)
            for z in z_values:
                zz = mpmath_fraction(z)
                Z = 1 / (1 - zz * A)
                rows.append({
                    "cutoff_M": M,
                    "s": ftext(s),
                    "z": ftext(z),
                    "A_M_real": decimal(A),
                    "A_M_imag": "0.0",
                    "Z_M_real": decimal(Z),
                    "Z_M_imag": "0.0",
                    "finite_convergence_condition": "|z|*A_M(Re(s))<1",
                    "full_product_condition": ("not applicable: A(Re(s)) diverges at Re(s)=1/2"
                                                if s == Fraction(1, 2)
                                                else "|z|*A(Re(s))<1"),
                    "full_A_status": ("diverges at Re(s)=1/2"
                                       if s == Fraction(1, 2)
                                       else "absolutely convergent for Re(s)>1/2"),
                    "s_one_telescoping": s == 1,
                })
    return rows


def limit_rows() -> list[dict]:
    rows = []
    M = 12
    for s in (Fraction(1), Fraction(3, 4), Fraction(3, 2)):
        sigma = mpmath_fraction(s)
        partial = sum(mp.power(branch_slope(m), -sigma) for m in range(2, M + 1))
        if s == 1:
            # sum_{m=M+1}^infinity 1/[m(m-1)] = 1/M exactly.
            tail = mp.mpf(1) / M
            limit = mp.mpf(1)
            telescoping = True
        else:
            tail = mp.power(M - 1, 1 - 2 * sigma) / (2 * sigma - 1)
            limit = mp.mpf("nan")
            telescoping = False
        rows.append({
            "s": ftext(s),
            "sigma": decimal(sigma),
            "partial_cutoff_M": M,
            "partial_sum_real": decimal(partial),
            "tail_upper_bound": decimal(tail),
            "limit_value_if_exact": decimal(limit) if s == 1 else "not_serialized",
            "absolute_convergence_claim": "Re(s)>1/2",
            "telescoping_at_s_one": telescoping,
        })
    return rows


def frac_series_product(M: int, max_length: int) -> tuple[list[str], list[str], list[int]]:
    alphabet = list(range(2, M + 1))
    primitive_words: dict[int, set[tuple[int, ...]]] = {r: set() for r in range(1, max_length + 1)}
    for r in range(1, max_length + 1):
        for word in itertools.product(alphabet, repeat=r):
            if primitive(word):
                primitive_words[r].add(canonical_word(word))
    # Multiply truncated geometric factors exactly at s=1.
    coeff = [Fraction(1)] + [Fraction(0)] * max_length
    for r, words in primitive_words.items():
        for word in words:
            weight = Fraction(1, math.prod(branch_slope(m) for m in word))
            nxt = coeff[:]
            factor = [Fraction(0)] * (max_length + 1)
            for q in range(max_length // r + 1):
                factor[q * r] = weight ** q
            nxt = [Fraction(0)] * (max_length + 1)
            for a, va in enumerate(coeff):
                for b, vb in enumerate(factor[: max_length - a + 1]):
                    nxt[a + b] += va * vb
            coeff = nxt
    S = sum(Fraction(1, branch_slope(m)) for m in alphabet)
    closed = [S ** j for j in range(max_length + 1)]
    return [ftext(x) for x in coeff], [ftext(x) for x in closed], [len(primitive_words[r]) for r in range(1, max_length + 1)]


def build() -> dict:
    alphabet = tuple(range(2, 7))
    words = [word_row(word) for r in range(1, 5) for word in itertools.product(alphabet, repeat=r)]
    finite_products = []
    for M in (3, 4):
        product_coeff, closed_coeff, primitive_counts = frac_series_product(M, 4)
        finite_products.append({
            "cutoff_M": M,
            "max_series_length": 4,
            "series_product_coefficients_s1": product_coeff,
            "closed_form_coefficients_s1": closed_coeff,
            "primitive_factor_counts_by_length": primitive_counts,
            "identity": "prod_primitive(1-z^r A_w^-s)^-1 = 1/(1-z sum_m a_m^-s)",
        })
    data = {
        "schema": "hcs-c241-luroth-countable-branch-v1",
        "candidate_id": "HCS-C241",
        "evaluation_date": "2026-08-30",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The classical Lüroth map has one exact periodic point and product multiplier for every finite branch word; primitive necklaces are explicit, while the countable alphabet makes every period countably infinite.",
        "frozen_object": {
            "map": "T_L(x)=floor(1/x)(floor(1/x)+1)x-floor(1/x) for x>0, T_L(0)=0",
            "branches": "m>=2 with I_m=(1/m,1/(m-1)] and slope a_m=m(m-1)",
            "inverse_branch": "phi_m(y)=(y+m-1)/(m(m-1))",
            "partition": "the intervals I_m cover (0,1] up to the declared half-open endpoint convention",
            "phase_space": "[0,1] with countably many branches on (0,1] and the isolated fixed endpoint 0",
            "parameters": "branch cutoff M>=2 for finite receipts; the mathematical map has alphabet {2,3,...}",
            "clock": "physical iterate count r; branch-word orientation is forward itinerary order",
            "primitive_periodic_orbit": "a primitive cyclic word in the countable branch alphabet, with its unique fixed point of the inverse composition",
            "weight": "w_m(s)=[m(m-1)]^{-s}; word weight is the product over symbols",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert-Polya operators",
        },
        "theorem": {
            "branch_partition": "T_L maps each I_m affinely onto (0,1] with derivative a_m=m(m-1); 0 is reached only as the excluded left endpoint limit",
            "word_inverse": "For every finite word w, Phi_w=phi_{w_1} compose ... compose phi_{w_r} is affine with contraction product a_{w_j}^{-1}",
            "unique_fixed_point": "Every finite word has a unique fixed point x_w in its coded cylinder; endpoint ambiguities are confined to the declared countable boundary convention",
            "multiplier": "(T_L^r)'(x_w)=A_w=prod_j w_j(w_j-1)",
            "itinerary": "The forward itinerary of x_w is w and cyclic rotations describe the same oriented periodic orbit",
            "primitive_necklaces": "Primitive words modulo cyclic rotation are primitive necklaces; finite cutoff q=M-1 has (1/r) sum_{d|r} mu(d) q^{r/d} necklaces of length r",
            "countable_branches": "Because the alphabet is countably infinite, every positive period has countably infinitely many coded words and periodic points (with the endpoint convention isolated)",
            "weighted_truncation": "For finite M, Z_M(z,s)=1/(1-z sum_{m=2}^M [m(m-1)]^{-s}) and its primitive-word product agrees where |z| A_M(Re(s))<1",
            "full_limit": "A(s)=sum_{m=2}^infinity [m(m-1)]^{-s} converges absolutely for Re(s)>1/2 by comparison with sum (m-1)^(-2 Re(s))",
            "euler_product_domain": "The countable primitive Euler product/log expansion is absolutely convergent only when Re(s)>1/2 and |z| A(Re(s))<1",
            "meromorphic_extension": "Within Re(s)>1/2, 1/(1-z A(s)) is the meromorphic continuation away from denominator zeros; this is broader than the absolute product domain",
            "telescoping_boundary": "At s=1, A(1)=sum_{m=2}^infinity(1/(m-1)-1/m)=1, so z=1 is a denominator pole/boundary",
            "scope": "This is a source-local countable-branch theorem; no target divisor, zero correspondence, or arithmetic prime semantics is asserted",
        },
        "regression": {
            "branch_rows": branch_rows(),
            "word_rows": words,
            "necklace_rows": necklace_rows(),
            "weighted_rows": weighted_rows(),
            "limit_rows": limit_rows(),
            "finite_product_rows": finite_products,
            "row_counts": {"branches": 11, "words": len(words), "necklaces": 30, "weighted": 88, "limits": 3, "finite_products": 2},
            "working_decimal_digits": 90,
            "serialized_significant_digits": 64,
        },
        "exact_identities": [
            {"name": "branch_slope", "formula": "a_m=m(m-1)"},
            {"name": "inverse_branch", "formula": "phi_m(y)=(y+m-1)/a_m"},
            {"name": "affine_contraction", "formula": "|Phi_w'|=prod_j a_{w_j}^{-1}<1"},
            {"name": "fixed_point", "formula": "x_w=v_w/(1-u_w) for Phi_w(y)=u_w y+v_w"},
            {"name": "multiplier", "formula": "(T^r)'(x_w)=prod_j a_{w_j}"},
            {"name": "primitive_necklace", "formula": "N_r(q)=(1/r)sum_{d|r}mu(d)q^{r/d}"},
            {"name": "truncated_weighted_zeta", "formula": "Z_M(z,s)=1/(1-z sum_{m=2}^M a_m^{-s})"},
            {"name": "full_convergence", "formula": "A(s) absolutely converges for Re(s)>1/2"},
            {"name": "product_domain", "formula": "absolute primitive product requires |z|A(Re(s))<1"},
            {"name": "s_one_telescoping", "formula": "A(1)=sum_{m=2}^infinity(1/(m-1)-1/m)=1"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "exact countable-branch word/point/multiplier theorem, primitive-necklace ledger, and correctly separated weighted-product and meromorphic domains",
            "strongest_failure": "the branch alphabet and physical iterate clock have no intrinsic rational-prime carrier; every period has countably infinite points",
        },
        "scope_flags": {
            "uses_target_zero_table": False,
            "uses_prime_table": False,
            "claims_arithmetic_local_data": False,
            "claims_euler_factors": False,
            "claims_root_numbers": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {"id": "BarrionuevoBurtonDajaniKraaikamp1996", "title": "Ergodic properties of generalized Lüroth series", "authors": "Jose Barrionuevo, Robert M. Burton, Karma Dajani, Cor Kraaikamp", "venue": "Acta Arithmetica 74(4), 311--327", "year": 1996, "doi": "10.4064/aa-74-4-311-327", "url": "https://doi.org/10.4064/aa-74-4-311-327", "role": "classical Lüroth map and countable branch expansion"},
            {"id": "Galambos1972", "title": "Some remarks on the Lüroth expansion", "authors": "János Galambos", "venue": "Czechoslovak Mathematical Journal 22(2), 266--271", "year": 1972, "doi": "10.21136/CMJ.1972.101097", "url": "https://dml.cz/dmlcz/101097", "role": "classical Lüroth expansion and endpoint/series conventions"},
        ],
        "nonclaims": [
            "Finite cutoff rows are reproducibility slices; the countable alphabet is the mathematical object and gives countably many points at every positive period.",
            "The weighted source identity and its meromorphic continuation are not a target Euler product, divisor, functional equation, or zero correspondence; A2 and A3 are FAIL.",
            "The absolute primitive-product domain |z|A(Re(s))<1 is distinct from the larger half-plane where 1/(1-zA(s)) is meromorphic away from denominator zeros.",
            "The branch labels and multipliers are not rational primes, prime powers, von Mangoldt weights, or logarithmic lengths.",
            "No arithmetic local datum, root number, automorphy statement, Hilbert-Polya operator, or Route-B input is claimed.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    tmp = args.output.with_name(args.output.name + ".tmp")
    tmp.write_text(raw)
    os.replace(tmp, args.output)
    print(json.dumps({"status": "C241_PRODUCER_PASS", "payload_sha256": data["payload_sha256"], "evidence_sha256": sha256(raw.encode()).hexdigest(), "branch_rows": len(data["regression"]["branch_rows"]), "word_rows": len(data["regression"]["word_rows"]), "weighted_rows": len(data["regression"]["weighted_rows"])}, sort_keys=True))


if __name__ == "__main__":
    main()
