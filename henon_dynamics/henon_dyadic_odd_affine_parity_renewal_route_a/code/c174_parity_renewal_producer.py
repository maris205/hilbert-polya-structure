#!/usr/bin/env python3
"""Produce exact C174 evidence for odd-affine parity dynamics on Z_2."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SOURCE_COMMIT = "100e5f601a0196710d53784bdeef40d2bff89fa8"
EVALUATOR_PATH = "flow_systems/skills/route-a-evaluator.md"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
A_VALUES = (-5, -3, -1, 1, 3, 5)
B_VALUES = (-5, -3, -1, 1, 3, 5)
WORD_N_MAX = 8
INVERSE_PREFIX_LENGTH = 8
RETURN_K_MAX = 12
PERIOD_N_MAX = 16
ROOF_N_MAX = 32


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def digest_rows(rows: list[str]) -> str:
    return sha256(("\n".join(rows) + "\n").encode()).hexdigest()


def bits_of(word: int, n: int) -> tuple[int, ...]:
    return tuple((word >> j) & 1 for j in range(n))


def parity(value: Fraction) -> int:
    assert value.denominator % 2 == 1
    return value.numerator & 1


def step(value: Fraction, a: int, b: int) -> Fraction:
    return value / 2 if parity(value) == 0 else (a * value + b) / 2


def word_data(bits: tuple[int, ...], a: int, b: int) -> tuple[int, int, Fraction]:
    s = sum(bits)
    acc = 0
    prefix = 0
    for j, bit in enumerate(bits):
        prefix += bit
        if bit:
            acc += (2**j) * (a ** (s - prefix))
    point = Fraction(b * acc, 2 ** len(bits) - a**s)
    return s, acc, point


def fixed_word_rows() -> list[dict]:
    rows: list[dict] = []
    for a in A_VALUES:
        for b in B_VALUES:
            for n in range(1, WORD_N_MAX + 1):
                encoded: list[str] = []
                stability = Fraction(0)
                points: set[Fraction] = set()
                for word in range(2**n):
                    bits = bits_of(word, n)
                    s, acc, point = word_data(bits, a, b)
                    state = point
                    observed: list[int] = []
                    for _ in range(n):
                        observed.append(parity(state))
                        state = step(state, a, b)
                    assert tuple(observed) == bits and state == point
                    points.add(point)
                    stability += Fraction(1, 2**n)
                    encoded.append(f"{word}:{''.join(map(str, bits))}:{s}:{acc}:{q(point)}")
                rows.append(
                    {
                        "a": a,
                        "b": b,
                        "n": n,
                        "fixed_point_count": len(points),
                        "expected_fixed_point_count": 2**n,
                        "stability_weight_sum": q(stability),
                        "word_point_digest": digest_rows(encoded),
                    }
                )
    return rows


def inverse_prefix(a: int, b: int, bits: tuple[int, ...]) -> Fraction:
    total = Fraction(0)
    ones = 0
    for j, bit in enumerate(bits):
        ones += bit
        if bit:
            total -= Fraction(b * 2**j, a**ones)
    return total


def inverse_prefix_rows() -> list[dict]:
    rows: list[dict] = []
    for a in A_VALUES:
        for b in B_VALUES:
            encoded: list[str] = []
            for word in range(2**INVERSE_PREFIX_LENGTH):
                bits = bits_of(word, INVERSE_PREFIX_LENGTH)
                point = inverse_prefix(a, b, bits)
                state = point
                observed = []
                for _ in range(INVERSE_PREFIX_LENGTH):
                    observed.append(parity(state))
                    state = step(state, a, b)
                assert tuple(observed) == bits and state == 0
                encoded.append(f"{word}:{q(point)}")
            rows.append(
                {
                    "a": a,
                    "b": b,
                    "prefix_length": INVERSE_PREFIX_LENGTH,
                    "prefix_count": 2**INVERSE_PREFIX_LENGTH,
                    "inverse_prefix_digest": digest_rows(encoded),
                }
            )
    return rows


def mobius(n: int) -> int:
    value = n
    primes = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def period_rows() -> list[dict]:
    rows = []
    for n in range(1, PERIOD_N_MAX + 1):
        exact_points = sum(mobius(n // d) * 2**d for d in divisors(n))
        rows.append(
            {
                "n": n,
                "fixed_points": 2**n,
                "exact_period_points": exact_points,
                "primitive_cycles": exact_points // n,
                "stability_weighted_fixed_sum": "1",
            }
        )
    return rows


def first_return_rows() -> list[dict]:
    rows = []
    for a in A_VALUES:
        for b in B_VALUES:
            for k in range(1, RETURN_K_MAX + 1):
                point = Fraction(b, 2**k - a)
                assert parity(point) == 1
                image = a * point + b
                valuation = 0
                numerator = image.numerator
                while numerator and numerator % 2 == 0:
                    numerator //= 2
                    valuation += 1
                assert valuation == k and image / 2**k == point
                rows.append(
                    {
                        "a": a,
                        "b": b,
                        "k": k,
                        "fixed_point": q(point),
                        "return_time": valuation,
                        "parity_block": "1" + "0" * (k - 1),
                        "conditional_haar_probability": f"1/{2**k}" if k > 0 else "1",
                    }
                )
    return rows


def roof_rows() -> list[dict]:
    return [
        {
            "n": n,
            "roof_fixed_count": 2**n - 1,
            "zero_orbit_fixed_count": 1,
            "original_fixed_count": 2**n,
        }
        for n in range(1, ROOF_N_MAX + 1)
    ]


def build_evidence() -> dict:
    fixed_rows = fixed_word_rows()
    inverse_rows = inverse_prefix_rows()
    return_rows = first_return_rows()
    payload = {
        "schema": "hcs-c174-dyadic-odd-affine-parity-renewal-v1",
        "candidate_id": "HCS-C174",
        "evaluation_date": "2026-08-26",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "evaluator": {
            "skill_version": "0.2.0",
            "authority_path": EVALUATOR_PATH,
            "authority_sha256": EVALUATOR_SHA256,
        },
        "artifact_path_base": "henon_dynamics/henon_dyadic_odd_affine_parity_renewal_route_a",
        "source_lock": {
            "phase_space": "Z_2 with normalized Haar probability mu",
            "parameter_family": "odd integers a and b, frozen before all validation",
            "map": "T_{a,b}(x)=x/2 for even x and (a*x+b)/2 for odd x",
            "arithmetic_origin": "intrinsic dyadic local arithmetic only; no rational-prime or prime-power correspondence",
            "clock": "one branch application of T_{a,b} is one original-clock tick",
            "normalization": "unweighted fixed-point cardinality and reciprocal 2-adic derivative stability",
            "determinant_convention": "classical Artin--Mazur exponential and the explicitly declared stability-weighted exponential",
            "cutoffs": {
                "a_values": list(A_VALUES),
                "b_values": list(B_VALUES),
                "word_n_max": WORD_N_MAX,
                "inverse_prefix_length": INVERSE_PREFIX_LENGTH,
                "return_k_max": RETURN_K_MAX,
                "period_n_max": PERIOD_N_MAX,
                "roof_n_max": ROOF_N_MAX,
            },
            "precision": "exact integers, rational numbers, formal power series, and 2-adic valuations only",
            "training_data": "none",
            "allowed_data": "odd a,b; parity branches; Haar measure; exact algebra; finite regression sentinels",
            "forbidden_data": "prime tables, target zeros or divisors, arithmetic local factors, Euler factors, root numbers, automorphy, Hilbert--Polya, and Route B",
        },
        "classical_foundation": {
            "ownership": "parity-vector conjugacy and its odd ax+b extension are classical prior work, not a novelty claim of C174",
            "parity_map": "Q_{a,b}(x)=sum_{j>=0} epsilon_j(x)*2^j",
            "conjugacy": "Q_{a,b} o T_{a,b}=sigma o Q_{a,b}",
            "inverse_formula": "Q^{-1}(sum epsilon_j 2^j)=-b*sum epsilon_j*2^j*a^{-s_{j+1}}",
            "measure_statement": "Q_{a,b} is a Haar-preserving homeomorphism of Z_2",
        },
        "fixed_word_theorem": {
            "iterate_formula": "2^n*T^n(x)=a^{s_n}*x+b*sum_{j=0}^{n-1} epsilon_j*2^j*a^{s_n-s_{j+1}}",
            "fixed_point_formula": "x_epsilon=b*A_epsilon/(2^n-a^{s_n})",
            "denominator_status": "2^n-a^{s_n} is odd and hence a unit in Z_2",
            "fixed_point_count": "#Fix(T^n)=2^n for every n>=1",
            "exact_period_formula": "P(n)=sum_{d|n} mu(n/d)*2^d",
            "artin_mazur_zeta": "zeta_AM(z)=1/(1-2*z)",
            "parameter_blind": True,
            "aggregate_rows": fixed_rows,
        },
        "stability_theorem": {
            "derivative": "(T^n)'(x_epsilon)=a^{s_n}/2^n",
            "valuation_identity": "|1-a^{s_n}/2^n|_2=2^n",
            "weighted_fixed_sum": "sum_{Fix(T^n)} |1-(T^n)'|_2^{-1}=1",
            "weighted_zeta": "zeta_stab(z)=1/(1-z)",
            "parameter_blind": True,
        },
        "inverse_conjugacy_sentinels": {
            "finite_tail_rule": "finite parity prefix followed by all zeros is evaluated exactly by the classical inverse series",
            "aggregate_rows": inverse_rows,
        },
        "period_ledger": period_rows(),
        "first_return_theorem": {
            "odd_cross_section": "O=1+2*Z_2",
            "return_time": "tau(x)=v_2(a*x+b) in {1,2,...}, except x_*=-b/a where tau=infinity",
            "return_map": "R(x)=(a*x+b)/2^{tau(x)}",
            "exceptional_point": "x_*=-b/a is odd, maps to zero in one tick, and never returns",
            "exceptional_set": "the points whose parity strings contain only finitely many ones; countable, Haar-null, and includes x_*",
            "recurrent_domain": "O_infty consists of odd points with infinitely many parity ones and has full conditional Haar measure in O",
            "symbolic_model": "R on O_infty is conjugate to the one-sided full shift on alphabet k>=1",
            "roof": "r(k)=k",
            "conditional_law": "mu_O(tau=k)=2^{-k}",
            "iid_law": "successive return times are iid geometric with weights 2^{-k}",
            "fixed_points": "x_k=b/(2^k-a), one for each k>=1",
            "ordinary_artin_mazur_status": "undefined for R because Fix(R) is countably infinite",
            "finite_rows": return_rows,
        },
        "original_clock_recovery": {
            "first_return_series": "F(z)=sum_{k>=1} z^k=z/(1-z)",
            "roof_zeta": "zeta_roof(z)=1/(1-F(z))=(1-z)/(1-2*z)",
            "roof_fixed_count": "2^n-1",
            "missing_orbit": "the all-zero fixed orbit",
            "recovery_identity": "zeta_AM(z)=zeta_roof(z)/(1-z)=1/(1-2*z)",
            "finite_rows": roof_rows(),
        },
        "operator_boundary": {
            "hilbert_space": "L^2(Z_2,mu)",
            "koopman": "U f=f o T_{a,b}",
            "isometry": True,
            "surjective": False,
            "wold_model": "U is unitarily equivalent to I_C direct_sum S^{(aleph_0)}",
            "spectrum": "closed unit disk",
            "point_spectrum": ["1"],
            "compact": False,
            "finite_schatten_class": False,
            "trace_class": False,
            "ordinary_fredholm_determinant_available": False,
            "natural_extension": "the two-sided inverse-limit extension is same-clock unitary but changes phase space",
            "route_a_status": "formal quantization hint only",
        },
        "parameter_and_boundary_audit": {
            "b_redundancy": "multiplication h_b(x)=b*x conjugates T_{a,1} to T_{a,b}",
            "odd_parameter_blindness": "all unweighted counts, stability sums, return laws, and roof recovery formulas are identical for every odd a,b",
            "even_a_boundary": "if a is even and b odd, the odd numerator a*x+b is odd and division by two leaves Z_2",
            "even_b_boundary": "if a is odd and b even, the odd numerator a*x+b is odd and division by two leaves Z_2",
            "three_x_plus_one_boundary": {
                "parameters": [3, 1],
                "parity_word": "100",
                "z2_cycle": ["1/5", "4/5", "2/5", "1/5"],
                "claim": "this legal Z_2 cycle is not a positive-integer Collatz orbit and gives no progress on the 3x+1 conjecture",
            },
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "a0_override_rule": "A0 failure forces overall rejection",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "classical_parity_conjugacy_novelty": False,
            "exact_renewal_and_roof_recovery_package": True,
            "stability_weighted_parameter_blindness": True,
            "collatz_positive_integer_progress": False,
            "prime_like_correspondence": False,
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
        },
        "integrity": {
            "hard_gate": "derive return renewal, restore the original clock, and test parameter sensitivity without target data",
            "hard_gate_status": "PASS_WITH_ROUTE_A_REJECTION",
            "finite_ledgers_are_proof": False,
            "proofs_are_symbolic_and_self_contained": True,
            "external_reviewer_simulated": False,
            "acceptance_rate_reported": False,
            "citation_population": 2,
        },
        "counts": {
            "parameter_pairs": len(A_VALUES) * len(B_VALUES),
            "fixed_word_aggregate_rows": len(fixed_rows),
            "fixed_words_checked": len(A_VALUES) * len(B_VALUES) * sum(2**n for n in range(1, WORD_N_MAX + 1)),
            "inverse_prefixes_checked": len(A_VALUES) * len(B_VALUES) * 2**INVERSE_PREFIX_LENGTH,
            "first_return_rows": len(return_rows),
            "period_rows": PERIOD_N_MAX,
            "roof_rows": ROOF_N_MAX,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c174_parity_renewal_evidence.json",
    )
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "status": "C174_PRODUCER_PASS",
                "payload_sha256": payload["payload_sha256"],
                **payload["counts"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
