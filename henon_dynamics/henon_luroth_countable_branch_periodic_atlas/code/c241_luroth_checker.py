#!/usr/bin/env python3
"""Producer-independent checker for the C241 Lüroth certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import itertools
import json
import math
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "results/c241_luroth_evidence.json"
SOURCE_COMMIT = "489506cf92bfed721f94f22dd0444a60427f90a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90

TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
FROZEN_KEYS = {"map", "branches", "inverse_branch", "partition", "phase_space", "parameters", "clock", "primitive_periodic_orbit", "weight", "forbidden_data"}
THEOREM_KEYS = {"branch_partition", "word_inverse", "unique_fixed_point", "multiplier", "itinerary", "primitive_necklaces", "countable_branches", "weighted_truncation", "full_limit", "euler_product_domain", "meromorphic_extension", "telescoping_boundary", "scope"}
REG_KEYS = {"branch_rows", "word_rows", "necklace_rows", "weighted_rows", "limit_rows", "finite_product_rows", "row_counts", "working_decimal_digits", "serialized_significant_digits"}
BRANCH_KEYS = {"branch_m", "interval_left", "interval_right", "slope", "inverse_at_zero", "inverse_at_one", "weight_s1"}
WORD_KEYS = {"word", "length", "canonical_word", "primitive", "primitive_period", "branch_product", "affine_u_num", "affine_u_den", "affine_v_num", "affine_v_den", "fixed_x_num", "fixed_x_den", "fixed_x_decimal", "multiplier", "itinerary", "return_x_num", "return_x_den", "orientation", "weight_s1_num", "weight_s1_den"}
NECK_KEYS = {"cutoff_M", "alphabet_size", "length", "primitive_necklaces", "all_words"}
WEIGHT_KEYS = {"cutoff_M", "s", "z", "A_M_real", "A_M_imag", "Z_M_real", "Z_M_imag", "finite_convergence_condition", "full_product_condition", "full_A_status", "s_one_telescoping"}
LIMIT_KEYS = {"s", "sigma", "partial_cutoff_M", "partial_sum_real", "tail_upper_bound", "limit_value_if_exact", "absolute_convergence_claim", "telescoping_at_s_one"}
FINITE_KEYS = {"cutoff_M", "max_series_length", "series_product_coefficients_s1", "closed_form_coefficients_s1", "primitive_factor_counts_by_length", "identity"}
ROUTE_KEYS = {"tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def branch_slope(m: int) -> int:
    return m * (m - 1)


def affine_word(word: tuple[int, ...]) -> tuple[Fraction, Fraction]:
    u, v = Fraction(1), Fraction(0)
    for m in reversed(word):
        a = branch_slope(m)
        u, v = u / a, (v + m - 1) / a
    return u, v


def branch_index(x: Fraction) -> int:
    assert x > 0
    return x.denominator // x.numerator + 1


def map_branch(x: Fraction, m: int) -> Fraction:
    return branch_slope(m) * x - (m - 1)


def itinerary(x: Fraction, length: int) -> tuple[int, ...]:
    y, out = x, []
    for _ in range(length):
        m = branch_index(y)
        out.append(m)
        y = map_branch(y, m)
    return tuple(out)


def rotations(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [word[j:] + word[:j] for j in range(len(word))]


def canonical(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotations(word))


def primitive_period(word: tuple[int, ...]) -> int:
    for d in range(1, len(word) + 1):
        if len(word) % d == 0 and word == word[:d] * (len(word) // d):
            return d
    raise AssertionError


def independent_word_expected(word: tuple[int, ...]) -> dict:
    u, v = affine_word(word)
    x = v / (1 - u)
    product = math.prod(branch_slope(m) for m in word)
    orbit = itinerary(x, len(word))
    assert orbit == word
    return {
        "word": list(word), "length": len(word), "canonical_word": list(canonical(word)),
        "primitive": primitive_period(word) == len(word), "primitive_period": primitive_period(word),
        "branch_product": product, "affine_u_num": u.numerator, "affine_u_den": u.denominator,
        "affine_v_num": v.numerator, "affine_v_den": v.denominator, "fixed_x_num": x.numerator,
        "fixed_x_den": x.denominator, "fixed_x_decimal": mp.nstr(mp.mpf(x.numerator) / x.denominator, 64, strip_zeros=False, min_fixed=-70, max_fixed=70),
        "multiplier": product, "itinerary": list(orbit), "return_x_num": x.numerator,
        "return_x_den": x.denominator, "orientation": "forward", "weight_s1_num": 1,
        "weight_s1_den": product,
    }


def mobius(value: int) -> int:
    if value == 1:
        return 1
    x, sign, p = value, 1, 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            sign = -sign
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1 if p == 2 else 2
    return sign * (-1 if x > 1 else 1)


def necklace_count(q: int, r: int) -> int:
    return sum(mobius(d) * q ** (r // d) for d in range(1, r + 1) if r % d == 0) // r


def frac_parse(text: str) -> Fraction:
    return Fraction(text)


def frac_series_product(M: int, max_length: int) -> tuple[list[str], list[str], list[int]]:
    alphabet = list(range(2, M + 1))
    primitive_words: dict[int, set[tuple[int, ...]]] = {r: set() for r in range(1, max_length + 1)}
    for r in range(1, max_length + 1):
        for word in itertools.product(alphabet, repeat=r):
            if primitive_period(word) == r:
                primitive_words[r].add(canonical(word))
    coeff = [Fraction(1)] + [Fraction(0)] * max_length
    for r, words in primitive_words.items():
        for word in words:
            weight = Fraction(1, math.prod(branch_slope(m) for m in word))
            factor = [Fraction(0)] * (max_length + 1)
            for q in range(max_length // r + 1):
                factor[q * r] = weight ** q
            nxt = [Fraction(0)] * (max_length + 1)
            for a, va in enumerate(coeff):
                for b, vb in enumerate(factor[: max_length - a + 1]):
                    nxt[a + b] += va * vb
            coeff = nxt
    S = sum(Fraction(1, branch_slope(m)) for m in alphabet)
    return [ftext(x) for x in coeff], [ftext(S ** j) for j in range(max_length + 1)], [len(primitive_words[r]) for r in range(1, max_length + 1)]


def close(a: str, b: mp.mpf, tol: mp.mpf = mp.mpf("1e-51")) -> bool:
    return abs(mp.mpf(a) - b) <= tol * max(mp.mpf(1), abs(b))


def check_keys(obj: dict, expected: set[str], where: str) -> int:
    assert set(obj) == expected, f"{where} keys mismatch: {sorted(set(obj) ^ expected)}"
    return 1


def validate(data: dict) -> int:
    count = 0
    count += check_keys(data, TOP_KEYS, "top")
    for key, value in (("schema", "hcs-c241-luroth-countable-branch-v1"), ("candidate_id", "HCS-C241"), ("evaluation_date", "2026-08-30"), ("source_commit", SOURCE_COMMIT), ("scope_literal", SCOPE)):
        assert data[key] == value, key; count += 1
    assert data["payload_sha256"] == payload_hash(data); count += 1
    assert data["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}; count += 1

    frozen = data["frozen_object"]
    count += check_keys(frozen, FROZEN_KEYS, "frozen")
    expected_frozen = {
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
    }
    for key, value in expected_frozen.items():
        assert frozen[key] == value, key; count += 1

    theorem = data["theorem"]
    count += check_keys(theorem, THEOREM_KEYS, "theorem")
    fragments = {
        "branch_partition": "maps each I_m affinely onto (0,1]",
        "word_inverse": "every finite word",
        "unique_fixed_point": "unique fixed point",
        "multiplier": "prod_j w_j(w_j-1)",
        "itinerary": "cyclic rotations",
        "primitive_necklaces": "Primitive words modulo cyclic rotation",
        "countable_branches": "countably infinitely many",
        "weighted_truncation": "Z_M(z,s)=1/(1-z sum_{m=2}^M",
        "full_limit": "absolutely for Re(s)>1/2",
        "euler_product_domain": "only when Re(s)>1/2 and |z| A(Re(s))<1",
        "meromorphic_extension": "meromorphic continuation away from denominator zeros",
        "telescoping_boundary": "A(1)=sum_{m=2}^infinity",
        "scope": "no target divisor",
    }
    for key, fragment in fragments.items():
        assert fragment.lower() in theorem[key].lower(), (key, fragment); count += 1
    assert "broader than the absolute product domain" in theorem["meromorphic_extension"]; count += 1
    assert "z=1" in theorem["telescoping_boundary"]; count += 1

    reg = data["regression"]
    count += check_keys(reg, REG_KEYS, "regression")
    assert reg["working_decimal_digits"] == 90 and reg["serialized_significant_digits"] == 64; count += 1
    assert reg["row_counts"] == {"branches": 11, "words": 780, "necklaces": 30, "weighted": 88, "limits": 3, "finite_products": 2}; count += 1

    branches = reg["branch_rows"]
    assert len(branches) == 11; count += 1
    for idx, row in enumerate(branches, start=2):
        count += check_keys(row, BRANCH_KEYS, "branch row")
        assert row["branch_m"] == idx; count += 1
        assert row["interval_left"] == ftext(Fraction(1, idx)); count += 1
        assert row["interval_right"] == ftext(Fraction(1, idx - 1)); count += 1
        a = branch_slope(idx)
        assert row["slope"] == a and row["inverse_at_zero"] == ftext(Fraction(idx - 1, a)) and row["inverse_at_one"] == ftext(Fraction(idx, a)); count += 1
        assert row["weight_s1"] == ftext(Fraction(1, a)); count += 1

    words = reg["word_rows"]
    expected_words = [word for r in range(1, 5) for word in itertools.product(range(2, 7), repeat=r)]
    assert len(words) == len(expected_words); count += 1
    for row, word in zip(words, expected_words):
        count += check_keys(row, WORD_KEYS, "word row")
        expected = independent_word_expected(word)
        for key, value in expected.items():
            if key == "fixed_x_decimal":
                assert close(row[key], mp.mpf(value)); count += 1
            else:
                assert row[key] == value, (word, key, row[key], value); count += 1
        # Reconstruct the affine intercept independently from the fixed-point
        # equation v=x(1-u); this catches numerator/denominator swaps that the
        # direct field comparisons above would otherwise hide.
        uu = Fraction(row["affine_u_num"], row["affine_u_den"])
        vv = Fraction(row["affine_v_num"], row["affine_v_den"])
        xx = Fraction(row["fixed_x_num"], row["fixed_x_den"])
        assert vv == xx * (1 - uu); count += 1
        assert Fraction(row["fixed_x_num"], row["fixed_x_den"]) > 0; count += 1

    necklaces = reg["necklace_rows"]
    assert len(necklaces) == 30; count += 1
    expected_necklaces = [{"cutoff_M": M, "alphabet_size": M - 1, "length": r, "primitive_necklaces": necklace_count(M - 1, r), "all_words": (M - 1) ** r} for M in range(3, 9) for r in range(1, 6)]
    assert necklaces == expected_necklaces; count += 1
    for row in necklaces:
        count += check_keys(row, NECK_KEYS, "necklace row")
        assert row["primitive_necklaces"] >= 0 and row["primitive_necklaces"] * row["length"] <= row["all_words"]; count += 1

    weighted = reg["weighted_rows"]
    assert len(weighted) == 88; count += 1
    for row in weighted:
        count += check_keys(row, WEIGHT_KEYS, "weighted row")
        M, s, z = row["cutoff_M"], frac_parse(row["s"]), frac_parse(row["z"])
        A = sum(mp.power(branch_slope(m), -mp.mpf(s.numerator) / s.denominator) for m in range(2, M + 1))
        Z = 1 / (1 - mp.mpf(z.numerator) / z.denominator * A)
        assert close(row["A_M_real"], A) and row["A_M_imag"] == "0.0"; count += 1
        assert close(row["Z_M_real"], Z) and row["Z_M_imag"] == "0.0"; count += 1
        assert row["finite_convergence_condition"] == "|z|*A_M(Re(s))<1"; count += 1
        if s == Fraction(1, 2):
            assert row["full_product_condition"] == "not applicable: A(Re(s)) diverges at Re(s)=1/2"; count += 1
            assert row["full_A_status"] == "diverges at Re(s)=1/2"; count += 1
        else:
            assert row["full_product_condition"] == "|z|*A(Re(s))<1"; count += 1
            assert row["full_A_status"] == "absolutely convergent for Re(s)>1/2"; count += 1
        assert row["s_one_telescoping"] is (s == 1); count += 1

    limits = reg["limit_rows"]
    assert len(limits) == 3; count += 1
    for row in limits:
        count += check_keys(row, LIMIT_KEYS, "limit row")
        s = frac_parse(row["s"]); sigma = mp.mpf(s.numerator) / s.denominator; M = row["partial_cutoff_M"]
        partial = sum(mp.power(branch_slope(m), -sigma) for m in range(2, M + 1))
        bound = mp.mpf(1) / M if s == 1 else mp.power(M - 1, 1 - 2 * sigma) / (2 * sigma - 1)
        assert close(row["sigma"], sigma) and close(row["partial_sum_real"], partial) and close(row["tail_upper_bound"], bound); count += 1
        assert row["absolute_convergence_claim"] == "Re(s)>1/2"; count += 1
        if s == 1:
            assert close(row["limit_value_if_exact"], mp.mpf(1)) and row["telescoping_at_s_one"] is True; count += 1
        else:
            assert row["limit_value_if_exact"] == "not_serialized" and row["telescoping_at_s_one"] is False; count += 1

    finite = reg["finite_product_rows"]
    assert len(finite) == 2; count += 1
    for row in finite:
        count += check_keys(row, FINITE_KEYS, "finite product row")
        M = row["cutoff_M"]
        expected = frac_series_product(M, row["max_series_length"])
        assert row["series_product_coefficients_s1"] == expected[0] and row["closed_form_coefficients_s1"] == expected[1] and row["primitive_factor_counts_by_length"] == expected[2]; count += 1
        assert "1/(1-z sum_m" in row["identity"]; count += 1

    ids = data["exact_identities"]
    assert len(ids) == 10 and all(set(item) == {"name", "formula"} for item in ids); count += 1
    names = {item["name"] for item in ids}
    assert names == {"branch_slope", "inverse_branch", "affine_contraction", "fixed_point", "multiplier", "primitive_necklace", "truncated_weighted_zeta", "full_convergence", "product_domain", "s_one_telescoping"}; count += 1
    expected_formulas = {"branch_slope": "a_m=m(m-1)", "inverse_branch": "phi_m(y)=(y+m-1)/a_m", "affine_contraction": "|Phi_w'|=prod_j a_{w_j}^{-1}<1", "fixed_point": "x_w=v_w/(1-u_w) for Phi_w(y)=u_w y+v_w", "multiplier": "(T^r)'(x_w)=prod_j a_{w_j}", "primitive_necklace": "N_r(q)=(1/r)sum_{d|r}mu(d)q^{r/d}", "truncated_weighted_zeta": "Z_M(z,s)=1/(1-z sum_{m=2}^M a_m^{-s})", "full_convergence": "A(s) absolutely converges for Re(s)>1/2", "product_domain": "absolute primitive product requires |z|A(Re(s))<1", "s_one_telescoping": "A(1)=sum_{m=2}^infinity(1/(m-1)-1/m)=1"}
    for item in ids:
        assert item["formula"] == expected_formulas[item["name"]]; count += 1

    route = data["route_a"]
    count += check_keys(route, ROUTE_KEYS, "route")
    assert route["tuple"] == ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]; count += 1
    assert route["overall"] == "ROUTE_A_REJECTED" and route["route_b_invocation_allowed"] is False; count += 1
    assert "countably infinite" in route["strongest_failure"]; count += 1
    flags = data["scope_flags"]
    count += check_keys(flags, SCOPE_KEYS, "scope flags")
    assert all(value is False for value in flags.values()); count += 1
    citations = data["citations"]
    assert len(citations) == 2; count += 1
    expected_citations = {
        "BarrionuevoBurtonDajaniKraaikamp1996": {"title": "Ergodic properties of generalized Lüroth series", "authors": "Jose Barrionuevo, Robert M. Burton, Karma Dajani, Cor Kraaikamp", "venue": "Acta Arithmetica 74(4), 311--327", "year": 1996, "doi": "10.4064/aa-74-4-311-327", "url": "https://doi.org/10.4064/aa-74-4-311-327", "role": "classical Lüroth map and countable branch expansion"},
        "Galambos1972": {"title": "Some remarks on the Lüroth expansion", "authors": "János Galambos", "venue": "Czechoslovak Mathematical Journal 22(2), 266--271", "year": 1972, "doi": "10.21136/CMJ.1972.101097", "url": "https://dml.cz/dmlcz/101097", "role": "classical Lüroth expansion and endpoint/series conventions"},
    }
    for item in citations:
        assert set(item) == {"id", "title", "authors", "venue", "year", "doi", "url", "role"}; count += 1
        assert item["id"] in expected_citations and {k: item[k] for k in expected_citations[item["id"]]} == expected_citations[item["id"]]; count += 1
    assert len(data["nonclaims"]) == 5; count += 1
    text = json.dumps(data, ensure_ascii=False).lower()
    for phrase in ("target primes", "euler factors", "root numbers", "hilbert-polya", "route-b", "absolute primitive-product domain"):
        assert phrase in text; count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()
    assertions = validate(json.loads(args.input.read_text()))
    print(f"C241 independent checker: PASS ({assertions} assertions)")


if __name__ == "__main__":
    main()
