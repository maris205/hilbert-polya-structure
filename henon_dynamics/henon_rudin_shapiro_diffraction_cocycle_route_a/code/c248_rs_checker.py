#!/usr/bin/env python3
"""Producer-independent validator for the C248 exact certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "results/c248_rs_evidence.json"
SOURCE_COMMIT = "5f357e2d2b78604f6c286bfbd05da922e1d6791f"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
DATE = "2026-08-30"
FIXED_EPOCH = 1788048000
ALPHABET = ["a", "b", "c", "d"]
RULES = {"a": "ab", "b": "ac", "c": "db", "d": "dc"}
CODING = {"a": 1, "b": 1, "c": -1, "d": -1}


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def assert_keys(obj: dict, keys: set[str], where: str) -> int:
    assert isinstance(obj, dict), where
    assert set(obj) == keys, f"{where}: key mismatch {set(obj) ^ keys}"
    return 1


def matrix() -> list[list[int]]:
    return [[RULES[src].count(dst) for src in ALPHABET] for dst in ALPHABET]


def multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][t] * b[t][j] for t in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def word_after(steps: int) -> str:
    word = "a"
    for _ in range(steps):
        word = "".join(RULES[x] for x in word)
    return word


def correlation(a: list[int], b: list[int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for i in range(len(a)):
        for j in range(len(b)):
            out[i - j] = out.get(i - j, 0) + a[i] * b[j]
    return out


def parse_sparse(items: list[list[int]]) -> dict[int, int]:
    assert all(isinstance(x, list) and len(x) == 2 and isinstance(x[0], int) and isinstance(x[1], int) for x in items)
    ans = {x[0]: x[1] for x in items}
    assert len(ans) == len(items)
    return ans


def shifted(d: dict[int, int], amount: int) -> dict[int, int]:
    return {i + amount: v for i, v in d.items()}


def combine(*terms: tuple[int, dict[int, int]]) -> dict[int, int]:
    out: dict[int, int] = {}
    for sign, d in terms:
        for i, v in d.items():
            out[i] = out.get(i, 0) + sign * v
    return {i: v for i, v in out.items() if v != 0}


def clean(d: dict[int, int]) -> dict[int, int]:
    return {i: v for i, v in d.items() if v != 0}


def validate(data: dict) -> int:
    checks = 0
    top = {"schema", "candidate_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
    checks += assert_keys(data, top, "top")
    for key, expected in (("schema", "hcs-c248-rudin-shapiro-diffraction-v1"), ("candidate_id", "HCS-C248"), ("evaluation_date", DATE), ("fixed_epoch", FIXED_EPOCH), ("source_commit", SOURCE_COMMIT), ("scope_literal", SCOPE)):
        assert data[key] == expected, key
        checks += 1
    assert data["payload_sha256"] == payload_hash(data); checks += 1
    assert data["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}; checks += 1

    frozen_keys = {"alphabet", "substitution", "factor_coding", "seed", "length", "dyadic_polynomials", "sequence_convention", "primitive_periodic_orbit", "forbidden_data"}
    checks += assert_keys(data["frozen_object"], frozen_keys, "frozen")
    frozen = data["frozen_object"]
    assert frozen["alphabet"] == ALPHABET and frozen["substitution"] == RULES and frozen["factor_coding"] == CODING; checks += 1
    assert frozen["seed"] == "a" and frozen["length"] == 2; checks += 1
    assert "P_{k+1}=P_k+z^(2^k)Q_k" in frozen["dyadic_polynomials"]; checks += 1
    assert "symmetric Cesaro/van Hove" in frozen["sequence_convention"]; checks += 1
    assert "none" in frozen["primitive_periodic_orbit"].lower() and "aperiodic" in frozen["primitive_periodic_orbit"].lower(); checks += 1
    assert SCOPE in frozen["forbidden_data"] and "Euler" in frozen["forbidden_data"]; checks += 1

    theorem_keys = {"primitivity", "aperiodicity", "factor_match", "energy_identity", "sup_bound", "paired_correlation", "infinite_correlation_recursion", "autocorrelation", "diffraction", "scope"}
    checks += assert_keys(data["theorem"], theorem_keys, "theorem")
    theorem = data["theorem"]
    for phrase in ("positive third power", "frequency", "aperiodic", "coefficients of P_k", "2^(k+1)", "sqrt", "Laurent", "every integer m", "delta_0", "Lebesgue", "not the full dynamical spectrum"):
        assert phrase.lower() in " ".join(theorem.values()).lower(), phrase
        checks += 1

    reg_keys = {"substitution_matrix", "matrix_power_3", "primitive_witness_power", "frequency_vector", "frequency_rows", "fixed_point_prefix_letters", "fixed_point_prefix_signs", "dyadic_rows", "correlation_rows", "infinite_recursion_receipt", "aperiodicity_rows", "parameter_grid", "row_counts", "integer_arithmetic_only"}
    checks += assert_keys(data["regression"], reg_keys, "regression")
    reg = data["regression"]
    M = matrix()
    assert reg["substitution_matrix"] == M; checks += 1
    m3 = multiply(multiply(M, M), M)
    assert reg["matrix_power_3"] == m3 and all(x > 0 for row in m3 for x in row); checks += 1
    assert reg["primitive_witness_power"] == 3 and reg["frequency_vector"] == ["1/4"] * 4; checks += 1
    assert reg["integer_arithmetic_only"] is True; checks += 1

    expected_word = word_after(10)
    assert reg["fixed_point_prefix_letters"] == expected_word and len(expected_word) == 1024; checks += 1
    expected_signs = [CODING[x] for x in expected_word]
    assert reg["fixed_point_prefix_signs"] == expected_signs; checks += 1

    freq_rows = reg["frequency_rows"]
    assert len(freq_rows) == 9; checks += 1
    for k, row in enumerate(freq_rows):
        assert set(row) == {"k", "length", "letter_counts", "frequency_denominator"}; checks += 1
        w = word_after(k)
        assert row == {"k": k, "length": len(w), "letter_counts": [w.count(x) for x in ALPHABET], "frequency_denominator": len(w)}; checks += 1
    assert sum(freq_rows[-1]["letter_counts"]) == freq_rows[-1]["length"]; checks += 1

    # Reconstruct the Hadamard polynomial cocycle independently.
    p, q = [1], [1]
    dyadic = reg["dyadic_rows"]
    assert len(dyadic) == 11; checks += 1
    for k, row in enumerate(dyadic):
        expected_keys = {"k", "N", "P_coefficients", "Q_coefficients", "P_energy", "Q_energy", "energy_sum", "unit_circle_bound_squared", "P_coefficient_sum", "Q_coefficient_sum"}
        checks += assert_keys(row, expected_keys, f"dyadic[{k}]")
        N = 1 << k
        assert row["k"] == k and row["N"] == N and row["P_coefficients"] == p and row["Q_coefficients"] == q; checks += 1
        assert p == expected_signs[:N]; checks += 1
        ep, eq = sum(v * v for v in p), sum(v * v for v in q)
        assert row["P_energy"] == ep == N and row["Q_energy"] == eq == N and row["energy_sum"] == 2 * N; checks += 1
        assert row["unit_circle_bound_squared"] == 2 * N; checks += 1
        assert row["P_coefficient_sum"] == sum(p) and row["Q_coefficient_sum"] == sum(q); checks += 1
        p, q = p + q, p + [-v for v in q]

    # Check all four Laurent products and the exact shift recursion.
    corr_rows = reg["correlation_rows"]
    assert len(corr_rows) == 8; checks += 1
    p, q = [1], [1]
    for k, row in enumerate(corr_rows):
        expected_keys = {"k", "N", "R", "S", "T", "U", "selected_R_lags_0_to_8", "max_abs_R_off_zero"}
        checks += assert_keys(row, expected_keys, f"correlation[{k}]")
        R, S, T, U = correlation(p, p), correlation(q, q), correlation(p, q), correlation(q, p)
        assert row["k"] == k and row["N"] == len(p); checks += 1
        for key, expected in (("R", R), ("S", S), ("T", T), ("U", U)):
            got = parse_sparse(row[key]); assert got == expected, (k, key); checks += 1
        assert row["selected_R_lags_0_to_8"] == [R.get(i, 0) for i in range(9)]; checks += 1
        assert row["max_abs_R_off_zero"] == max([abs(v) for lag, v in R.items() if lag] or [0]); checks += 1
        if k < len(corr_rows) - 1:
            N = len(p)
            Rn, Sn, Tn, Un = (clean(correlation(p + q, p + q)), clean(correlation(p + [-v for v in q], p + [-v for v in q])), clean(correlation(p + q, p + [-v for v in q])), clean(correlation(p + [-v for v in q], p + q)))
            assert Rn == combine((1, R), (1, S), (1, shifted(T, -N)), (1, shifted(U, N))); checks += 1
            assert Sn == combine((1, R), (1, S), (-1, shifted(T, -N)), (-1, shifted(U, N))); checks += 1
            assert Tn == combine((1, R), (-1, S), (-1, shifted(T, -N)), (1, shifted(U, N))); checks += 1
            assert Un == combine((1, R), (-1, S), (1, shifted(T, -N)), (-1, shifted(U, N))); checks += 1
        p, q = p + q, p + [-v for v in q]

    # The infinite-volume 4-adic recursion is kept as literal text so that a
    # repaired payload cannot silently replace it by a finite-block slogan.
    inf = reg["infinite_recursion_receipt"]
    assert set(inf) == {"definitions", "initial_conditions", "equations", "uniqueness_argument"}; checks += 1
    assert inf["definitions"] == [
        "a_m=lim_{L->infinity}(2L+1)^(-1) sum_{n=-L}^L w(n)w(n+m)",
        "b_m=lim_{L->infinity}(2L+1)^(-1) sum_{n=-L}^L (-1)^n w(n)w(n+m)",
    ]; checks += 1
    assert inf["initial_conditions"] == ["a_0=1", "b_0=0"]; checks += 1
    expected_equations = [
        "a_{4m}=((1+(-1)^m)/2)a_m; a_{4m+2}=0",
        "a_{4m+1}=((1-(-1)^m)/4)a_m+((-1)^m/4)b_m-(1/4)b_{m+1}",
        "a_{4m+3}=((1+(-1)^m)/4)a_{m+1}-((-1)^m/4)b_m+(1/4)b_{m+1}",
        "b_{4m}=0; b_{4m+2}=((-1)^m/2)b_m+(1/2)b_{m+1}",
        "b_{4m+1}=((1-(-1)^m)/4)a_m-((-1)^m/4)b_m+(1/4)b_{m+1}",
        "b_{4m+3}=-((1+(-1)^m)/4)a_{m+1}-((-1)^m/4)b_m+(1/4)b_{m+1}",
    ]
    assert inf["equations"] == expected_equations; checks += 1
    assert "base indices -3..3" in inf["uniqueness_argument"] and "every m!=0" in inf["uniqueness_argument"]; checks += 1

    # Finite aperiodicity receipts and exact row counts.
    ap = reg["aperiodicity_rows"]
    assert len(ap) == 64; checks += 1
    prefix = expected_word[:512]
    for period, row in enumerate(ap, start=1):
        assert set(row) == {"period", "first_mismatch_index", "left", "right"}; checks += 1
        idx = next(i for i in range(len(prefix) - period) if prefix[i] != prefix[i + period])
        assert row == {"period": period, "first_mismatch_index": idx, "left": prefix[idx], "right": prefix[idx + period]}; checks += 1
    assert reg["parameter_grid"] == [{"k": k, "N": 1 << k} for k in range(11)]; checks += 1
    assert reg["row_counts"] == {"dyadic": 11, "frequency": 9, "correlation": 8, "aperiodicity": 64, "polynomial_coefficients": 4094}; checks += 1

    identities = data["exact_identities"]
    assert isinstance(identities, list) and len(identities) == 4; checks += 1
    assert [x["name"] for x in identities] == ["substitution_matrix", "hadamard_energy", "cross_correlation_pair", "diffraction_boundary"]; checks += 1
    assert all(set(x) == {"name", "formula", "status"} and x["status"] in {"proved_and_receipted", "source_supported_and_scope_limited"} for x in identities); checks += 1
    assert "delta_0" in identities[-1]["formula"] and "Lebesgue" in identities[-1]["formula"]; checks += 1

    route = data["route_a"]
    assert set(route) == {"tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"}; checks += 1
    assert route["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]; checks += 1
    assert route["overall"] == "ROUTE_A_REJECTED" and route["route_b_invocation_allowed"] is False; checks += 1
    assert "no shift-periodic" in route["strongest_failure"].lower() and "target" in route["strongest_failure"].lower(); checks += 1

    scope = data["scope_flags"]
    expected_scope = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}
    checks += assert_keys(scope, expected_scope, "scope")
    assert all(value is False for value in scope.values()); checks += 1

    citations = data["citations"]
    assert len(citations) == 3; checks += 1
    expected_citations = {
        "Rudin1959": ("10.1090/S0002-9939-1959-0116184-5", "https://doi.org/10.1090/S0002-9939-1959-0116184-5"),
        "BaakeGrimm2009": ("10.1103/PhysRevB.79.020203", "https://doi.org/10.1103/PhysRevB.79.020203"),
        "BaakeGrimmErratum2009": ("10.1103/PhysRevB.80.029903", "https://doi.org/10.1103/PhysRevB.80.029903"),
    }
    for item in citations:
        assert set(item) == {"id", "title", "authors", "venue", "doi", "url", "role"}; checks += 1
        assert item["id"] in expected_citations and (item["doi"], item["url"]) == expected_citations[item["id"]]; checks += 1
    assert {x["id"] for x in citations} == set(expected_citations); checks += 1
    assert "autocorrelation" in citations[1]["role"].lower() and "diffraction" in citations[1]["role"].lower(); checks += 1
    assert "correction" in citations[2]["role"].lower() and all(token in citations[2]["role"] for token in ("a_{4m}", "a_{4m+3}", "b_{4m+2}")); checks += 1

    assert isinstance(data["nonclaims"], list) and len(data["nonclaims"]) == 4; checks += 1
    joined_nonclaims = " ".join(data["nonclaims"]).lower()
    for phrase in ("finite word", "diffraction", "primitive", "euler", "hilbert"):
        assert phrase in joined_nonclaims; checks += 1
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    checks = validate(data)
    print(f"C248 independent checker: PASS ({checks} assertions)")


if __name__ == "__main__":
    main()
