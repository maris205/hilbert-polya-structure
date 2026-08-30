#!/usr/bin/env python3
"""Produce the exact, source-local C248 Rudin--Shapiro certificate.

The producer deliberately uses integer arithmetic only.  It records the
four-letter constant-length substitution, the two Littlewood polynomials,
their Laurent correlation cocycle, and finite receipts for the limiting
autocorrelation statement.  A separate checker reconstructs every object
instead of importing this module.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
import math
from pathlib import Path

SOURCE_COMMIT = "5f357e2d2b78604f6c286bfbd05da922e1d6791f"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
DATE = "2026-08-30"
FIXED_EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c248_rs_evidence.json"

ALPHABET = ["a", "b", "c", "d"]
RULES = {"a": "ab", "b": "ac", "c": "db", "d": "dc"}
CODING = {"a": 1, "b": 1, "c": -1, "d": -1}


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def substitution_matrix() -> list[list[int]]:
    return [[RULES[src].count(dst) for src in ALPHABET] for dst in ALPHABET]


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def matpow(a: list[list[int]], power: int) -> list[list[int]]:
    out = [[int(i == j) for j in range(len(a))] for i in range(len(a))]
    base = a
    while power:
        if power & 1:
            out = matmul(out, base)
        base = matmul(base, base)
        power //= 2
    return out


def iterate_word(word: str, steps: int) -> str:
    for _ in range(steps):
        word = "".join(RULES[ch] for ch in word)
    return word


def corr(a: list[int], b: list[int]) -> dict[int, int]:
    """Laurent coefficients of A(z)B(z^{-1}), keyed by exponent i-j."""
    out: dict[int, int] = {}
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            lag = i - j
            out[lag] = out.get(lag, 0) + left * right
    return out


def sparse(d: dict[int, int]) -> list[list[int]]:
    return [[lag, d[lag]] for lag in sorted(d)]


def shift(d: dict[int, int], amount: int) -> dict[int, int]:
    return {lag + amount: value for lag, value in d.items()}


def add(*terms: tuple[int, dict[int, int]]) -> dict[int, int]:
    out: dict[int, int] = {}
    for sign, term in terms:
        for lag, value in term.items():
            out[lag] = out.get(lag, 0) + sign * value
    return {lag: value for lag, value in out.items() if value != 0}


def dyadic_rows(max_k: int = 10) -> list[dict]:
    p, q = [1], [1]
    rows = []
    for k in range(max_k + 1):
        n = 1 << k
        rows.append({
            "k": k,
            "N": n,
            "P_coefficients": list(p),
            "Q_coefficients": list(q),
            "P_energy": sum(x * x for x in p),
            "Q_energy": sum(x * x for x in q),
            "energy_sum": sum(x * x for x in p) + sum(x * x for x in q),
            "unit_circle_bound_squared": 2 * n,
            "P_coefficient_sum": sum(p),
            "Q_coefficient_sum": sum(q),
        })
        p, q = p + q, p + [-x for x in q]
    return rows


def frequency_rows(max_k: int = 8) -> list[dict]:
    word = "a"
    rows = []
    for k in range(max_k + 1):
        counts = [word.count(ch) for ch in ALPHABET]
        rows.append({"k": k, "length": len(word), "letter_counts": counts, "frequency_denominator": len(word)})
        word = "".join(RULES[ch] for ch in word)
    return rows


def correlation_rows(max_k: int = 7) -> list[dict]:
    p, q = [1], [1]
    rows = []
    for k in range(max_k + 1):
        n = len(p)
        R, S, T, U = corr(p, p), corr(q, q), corr(p, q), corr(q, p)
        rows.append({
            "k": k,
            "N": n,
            "R": sparse(R),
            "S": sparse(S),
            "T": sparse(T),
            "U": sparse(U),
            "selected_R_lags_0_to_8": [R.get(m, 0) for m in range(9)],
            "max_abs_R_off_zero": max([abs(v) for lag, v in R.items() if lag != 0] or [0]),
        })
        p, q = p + q, p + [-x for x in q]
    return rows


def aperiodicity_rows(prefix: str, limit: int = 64) -> list[dict]:
    rows = []
    for period in range(1, limit + 1):
        mismatch = next(i for i in range(len(prefix) - period) if prefix[i] != prefix[i + period])
        rows.append({"period": period, "first_mismatch_index": mismatch, "left": prefix[mismatch], "right": prefix[mismatch + period]})
    return rows


def build() -> dict:
    matrix = substitution_matrix()
    word = iterate_word("a", 10)  # 1024 letters, enough for all finite receipts
    sign_prefix = [CODING[ch] for ch in word]
    dyadic = dyadic_rows()
    correlations = correlation_rows()
    frequencies = frequency_rows()
    data = {
        "schema": "hcs-c248-rudin-shapiro-diffraction-v1",
        "candidate_id": "HCS-C248",
        "evaluation_date": DATE,
        "fixed_epoch": FIXED_EPOCH,
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The primitive Rudin--Shapiro substitution has an exact dyadic Hadamard cocycle: complementary energy, a square-root sup bound, and a paired Laurent correlation recursion whose van Hove autocorrelation is delta_0 and diffraction is Lebesgue measure.",
        "frozen_object": {
            "alphabet": ALPHABET,
            "substitution": RULES,
            "factor_coding": CODING,
            "seed": "a",
            "length": 2,
            "dyadic_polynomials": "P_0=Q_0=1; P_{k+1}=P_k+z^(2^k)Q_k; Q_{k+1}=P_k-z^(2^k)Q_k",
            "sequence_convention": "one-sided fixed point of a, with the displayed factor in {+1,-1}; the autocorrelation receipt uses the canonical two-sided hull and symmetric Cesaro/van Hove averaging",
            "primitive_periodic_orbit": "none: the substitution hull is aperiodic, so finite blocks are receipts rather than primitive periodic orbits",
            "forbidden_data": "NO_BAD_EULER_OR_ROOT_NUMBER: target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert--Polya operators",
        },
        "theorem": {
            "primitivity": "the substitution matrix has a strictly positive third power and unique frequency (1/4,1/4,1/4,1/4)",
            "aperiodicity": "the fixed point and its substitution hull are aperiodic; no shift-periodic primitive orbit is asserted",
            "factor_match": "coding a,b to +1 and c,d to -1 gives the coefficients of P_k on every dyadic prefix",
            "energy_identity": "|P_{k+1}|^2+|Q_{k+1}|^2=2(|P_k|^2+|Q_k|^2) on |z|=1, hence the sum is 2^(k+1)",
            "sup_bound": "max(|P_k(z)|,|Q_k(z)|)<=sqrt(2^(k+1)) for |z|=1",
            "paired_correlation": "R,S,T,U Laurent products obey the exact four-term shift recursion induced by P'=P+z^NQ and Q'=P-z^NQ",
            "infinite_correlation_recursion": "for a_m=lim(2L+1)^(-1)sum_{n=-L}^L w(n)w(n+m) and b_m=lim(2L+1)^(-1)sum (-1)^n w(n)w(n+m), the eight 4-adic equations in regression are valid for every integer m",
            "autocorrelation": "under the declared symmetric Cesaro/van Hove convention, the binary factor has eta(0)=1 and eta(m)=0 for m != 0",
            "diffraction": "the Fourier transform of delta_0 is Lebesgue measure; this is diffraction, not the full dynamical spectrum",
            "scope": "source-local harmonic/combinatorial statement; no target arithmetic matching",
        },
        "regression": {
            "substitution_matrix": matrix,
            "matrix_power_3": matpow(matrix, 3),
            "primitive_witness_power": 3,
            "frequency_vector": ["1/4", "1/4", "1/4", "1/4"],
            "frequency_rows": frequencies,
            "fixed_point_prefix_letters": word,
            "fixed_point_prefix_signs": sign_prefix,
            "dyadic_rows": dyadic,
            "correlation_rows": correlations,
            "infinite_recursion_receipt": {
                "definitions": [
                    "a_m=lim_{L->infinity}(2L+1)^(-1) sum_{n=-L}^L w(n)w(n+m)",
                    "b_m=lim_{L->infinity}(2L+1)^(-1) sum_{n=-L}^L (-1)^n w(n)w(n+m)",
                ],
                "initial_conditions": ["a_0=1", "b_0=0"],
                "equations": [
                    "a_{4m}=((1+(-1)^m)/2)a_m; a_{4m+2}=0",
                    "a_{4m+1}=((1-(-1)^m)/4)a_m+((-1)^m/4)b_m-(1/4)b_{m+1}",
                    "a_{4m+3}=((1+(-1)^m)/4)a_{m+1}-((-1)^m/4)b_m+(1/4)b_{m+1}",
                    "b_{4m}=0; b_{4m+2}=((-1)^m/2)b_m+(1/2)b_{m+1}",
                    "b_{4m+1}=((1-(-1)^m)/4)a_m-((-1)^m/4)b_m+(1/4)b_{m+1}",
                    "b_{4m+3}=-((1+(-1)^m)/4)a_{m+1}-((-1)^m/4)b_m+(1/4)b_{m+1}",
                ],
                "uniqueness_argument": "the finite base indices -3..3 are forced to zero off 0; induction on absolute index through the four residue classes then forces a_m=b_m=0 for every m!=0",
            },
            "aperiodicity_rows": aperiodicity_rows(word[:512]),
            "parameter_grid": [{"k": k, "N": 1 << k} for k in range(11)],
            "row_counts": {"dyadic": len(dyadic), "frequency": len(frequencies), "correlation": len(correlations), "aperiodicity": 64, "polynomial_coefficients": sum(len(r["P_coefficients"]) + len(r["Q_coefficients"]) for r in dyadic)},
            "integer_arithmetic_only": True,
        },
        "exact_identities": [
            {"name": "substitution_matrix", "formula": "M_{x,y}=#(x in sigma(y)); M^3>0", "status": "proved_and_receipted"},
            {"name": "hadamard_energy", "formula": "R_{k+1}=R_k+S_k+z^{-N}T_k+z^NU_k; S_{k+1}=R_k+S_k-z^{-N}T_k-z^NU_k", "status": "proved_and_receipted"},
            {"name": "cross_correlation_pair", "formula": "T_{k+1}=R_k-S_k-z^{-N}T_k+z^NU_k; U_{k+1}=R_k-S_k+z^{-N}T_k-z^NU_k", "status": "proved_and_receipted"},
            {"name": "diffraction_boundary", "formula": "gamma_RS=delta_0 and Fourier(gamma_RS)=Lebesgue under symmetric Cesaro/van Hove averaging", "status": "source_supported_and_scope_limited"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "Aperiodic primitive substitution, exact dyadic cocycle identities, and source-local diffraction certificate",
            "strongest_failure": "No shift-periodic primitive orbit ledger and no target divisor/zero/arithmetic identification",
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
            {"id": "Rudin1959", "title": "Some theorems on Fourier coefficients", "authors": "Walter Rudin", "venue": "Proceedings of the American Mathematical Society 10, 855--859 (1959)", "doi": "10.1090/S0002-9939-1959-0116184-5", "url": "https://doi.org/10.1090/S0002-9939-1959-0116184-5", "role": "primary source for the Rudin--Shapiro polynomial construction and square-root bound"},
            {"id": "BaakeGrimm2009", "title": "Kinematic diffraction is insufficient to distinguish order from disorder", "authors": "Michael Baake and Uwe Grimm", "venue": "Physical Review B 79, 020203(R) (2009)", "doi": "10.1103/PhysRevB.79.020203", "url": "https://doi.org/10.1103/PhysRevB.79.020203", "role": "primary source directly deriving Rudin--Shapiro autocorrelation delta_0 and Lebesgue diffraction"},
            {"id": "BaakeGrimmErratum2009", "title": "Erratum: Kinematic diffraction is insufficient to distinguish order from disorder", "authors": "Michael Baake and Uwe Grimm", "venue": "Physical Review B 80, 029903(E) (2009)", "doi": "10.1103/PhysRevB.80.029903", "url": "https://doi.org/10.1103/PhysRevB.80.029903", "role": "primary correction of the a_{4m}, a_{4m+3}, and b_{4m+2} recursion signs used here"},
        ],
        "nonclaims": [
            "The finite dyadic rows are exact receipts, not a claim that a finite word is a periodic orbit.",
            "Diffraction is the Fourier transform of the autocorrelation and is not the full dynamical spectrum of the substitution shift.",
            "No primitive shift-periodic orbit, target prime/zero table, Euler factor, root number, automorphy, target divisor, or Hilbert--Polya operator is supplied.",
            "A source-local zeta or arithmetic spectral identification is not inferred from the diffraction measure; A2 and A3 remain FAIL.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C248_PRODUCER_PASS", "output": str(args.output), "payload_sha256": json.loads(args.output.read_text())["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
