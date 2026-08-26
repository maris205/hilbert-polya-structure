#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C179 evidence."""
from __future__ import annotations

import argparse
from hashlib import sha256
from math import gcd
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c179_zsigmondy_return_evidence.json"
SOURCE_COMMIT = "bbb809ee198bc9ad5f196383baab1e3d9de38e43"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    blob = json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return sha256(blob).hexdigest()


def is_prime(value: int) -> bool:
    """Deterministic Miller--Rabin on the 64-bit sentinel range."""
    if value < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    if value in small:
        return True
    if any(value % prime == 0 for prime in small):
        return False
    odd = value - 1
    power = 0
    while odd % 2 == 0:
        power += 1
        odd //= 2
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        witness = pow(base, odd, value)
        if witness in (1, value - 1):
            continue
        for _ in range(power - 1):
            witness = witness * witness % value
            if witness == value - 1:
                break
        else:
            return False
    return True


def trial_factors(value: int) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            exponent += 1
            remaining //= divisor
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def independent_phi(value: int) -> int:
    if value == 1:
        return 1
    return sum(1 for candidate in range(1, value + 1) if gcd(candidate, value) == 1)


def phi_by_factors(value: int) -> int:
    if value == 1:
        return 1
    result = value
    for prime, _ in trial_factors(value):
        result = result // prime * (prime - 1)
    return result


def independent_order(value: int, modulus: int) -> int:
    phi = phi_by_factors(modulus)
    order = phi
    for prime, _ in trial_factors(phi):
        while order % prime == 0 and pow(value, order // prime, modulus) == 1:
            order //= prime
    return order


def factors_to_divisors(entries: list[dict]) -> list[int]:
    result = [1]
    for entry in entries:
        prime = entry["prime"]
        exponent = entry["exponent"]
        result = [base * prime**power for base in result for power in range(exponent + 1)]
    return sorted(result)


def small_mobius(value: int) -> int:
    if value == 1:
        return 1
    factors = trial_factors(value)
    if any(exponent > 1 for _, exponent in factors):
        return 0
    return -1 if len(factors) % 2 else 1


def pairs(limit: int) -> list[tuple[int, int]]:
    return [
        (a, b)
        for a in range(2, limit + 1)
        for b in range(1, a)
        if gcd(a, b) == 1
    ]


def exception_label(a: int, b: int, n: int) -> str | None:
    if (a, b, n) == (2, 1, 6):
        return "exceptional_triple_2_1_6"
    if n == 2 and a + b > 0 and (a + b) & (a + b - 1) == 0:
        return "n_2_and_a_plus_b_power_of_two"
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    assertions = 0

    def check(condition: bool, label: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(label)

    check(data["payload_sha256"] == canonical_hash(data), "canonical hash")
    check(data["schema"] == "hcs-c179-zsigmondy-congruence-return-v1", "schema")
    check(data["candidate_id"] == "HCS-C179", "candidate")
    check(data["evaluation_date"] == "2026-08-26", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["evaluator"]["skill"] == "route-a-evaluator", "evaluator skill")
    check(data["evaluator"]["version"] == "0.2.0", "evaluator version")
    check(data["evaluator"]["sha256"] == EVALUATOR_SHA256, "evaluator hash")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope literal")

    lock_expected = {
        "object": "for coprime integers a>b>=1 and N>=2 with gcd(N,ab)=1, R_(a,b,N)(x)=a*b^(-1)*x on U_N=(Z/NZ)^times, marked at x=1",
        "arithmetic_origin": "the integer divisibility sequence a^n-b^n and its congruence first-return moduli",
        "parameter_domain": "all coprime integers a>b>=1; every admissible finite modulus N; odd primitive primes and all their powers",
        "clock": "one multiplication by a*b^(-1) is one discrete source step; no log-prime roof is assigned",
        "normalization": "finite-fiber fixed-point cardinality and unweighted Artin--Mazur convention",
        "determinant_convention": "zeta_N=exp(sum_(t>=1)#Fix(R_N^t)z^t/t) and the finite Koopman determinant det(I-zU_N)",
        "globalizations": "the disjoint union over finite unit fibers and the profinite inverse limit are kept as distinct constructions",
        "precision": "exact integer factorization, modular order, valuation, permutation, and formal power-series algebra",
        "training_data": "none",
        "allowed_data": "integers generated from a,b; exact congruence reductions and factorization used only as deterministic sentinels",
        "forbidden_data": "target zero or prime tables, local Euler factors, root numbers, automorphy, prime-weighted global products, log-p roofs, fitted target data, Hilbert--Polya claims, and Route B",
    }
    check(set(data["source_lock"]) == set(lock_expected), "source-lock key set")
    for key, expected in lock_expected.items():
        check(data["source_lock"][key] == expected, f"source lock {key}")

    references = data["attribution_registry"]
    expected_references = [
        {
            "id": "zsigmondy1892",
            "claim_scope": "classical primitive-divisor existence theorem and exact exceptions",
            "status": "EXTERNAL_THEOREM_ATTRIBUTED_NOT_NEW",
            "author": "Karl Zsigmondy",
            "title": "Zur Theorie der Potenzreste",
            "year": 1892,
            "venue": "Monatshefte fuer Mathematik und Physik 3, 265--284",
            "doi": "10.1007/BF01692444",
        },
        {
            "id": "birkhoff_vandiver1904",
            "claim_scope": "classical arithmetic of integral and primitive divisors of a^n-b^n",
            "status": "HISTORICAL_CONTEXT_ATTRIBUTED",
            "author": "George D. Birkhoff and Harry S. Vandiver",
            "title": "On the Integral Divisors of a^n-b^n",
            "year": 1904,
            "venue": "Annals of Mathematics 5(4), 173--180",
            "doi": "10.2307/2007263",
        },
        {
            "id": "artin_mazur1965",
            "claim_scope": "Artin--Mazur fixed-point zeta convention",
            "status": "DEFINITIONAL_SOURCE_ATTRIBUTED",
            "author": "Michael Artin and Barry Mazur",
            "title": "On Periodic Points",
            "year": 1965,
            "venue": "Annals of Mathematics 81(1), 82--99",
            "doi": "10.2307/1970384",
        },
        {
            "id": "silverman2013",
            "claim_scope": "modern arithmetic-dynamics context for dynamical Zsigmondy sets",
            "status": "CONTEXT_ONLY_NOT_USED_AS_PROOF",
            "author": "Joseph H. Silverman",
            "title": "Primitive Divisors, Dynamical Zsigmondy Sets, and Vojta's Conjecture",
            "year": 2013,
            "venue": "Journal of Number Theory 133(9), 2948--2963",
            "doi": "10.1016/j.jnt.2013.03.005",
        },
    ]
    expected_reference_by_id = {entry["id"]: entry for entry in expected_references}
    check(len(references) == 4, "reference count")
    check([entry["id"] for entry in references] == [entry["id"] for entry in expected_references], "reference order and ids")
    for entry in references:
        expected = expected_reference_by_id[entry["id"]]
        check(entry["doi"] == expected["doi"], f"DOI {entry['id']}")
        check(entry["year"] == expected["year"], f"year {entry['id']}")
        check(entry == expected, f"exact attribution map {entry['id']}")

    theorem = data["theorem_ledger"]
    theorem_expected = {
        "primitive_return_equivalence": "p is primitive for a^n-b^n iff the marked point 1 has least return n under R_(a,b,p)",
        "zsigmondy_scope": "for n>=2 a primitive return prime exists except (2,1,6) and n=2 with a+b a power of two; this is the attributed classical theorem",
        "prime_power_lift": "for an odd primitive p with e=v_p(a^n-b^n), ord_(p^k)(a*b^(-1))=n*p^max(0,k-e)",
        "finite_fiber": "with L_N=ord_N(a*b^(-1)), U_N is phi(N)/L_N cycles of length L_N, zeta_N=(1-z^L_N)^(-phi(N)/L_N), and inversion reverses time",
        "disjoint_union": "including the singleton N=1 fiber, the finite-fiber disjoint union has #Fix at time n equal to sum_(N|a^n-b^n)phi(N)=a^n-b^n and zeta=(1-bz)/(1-az)",
        "profinite_limit": "translation by a/b on the inverse limit of the U_N has no positive-time fixed point and source zeta 1",
        "owner_nonuniqueness": "finite congruence fibers admit two source-natural globalizations with incompatible fixed ledgers, so the fiber data do not select a single global determinant owner",
    }
    check(theorem == theorem_expected, "exact theorem ledger map")
    check(theorem["primitive_return_equivalence"] == theorem_expected["primitive_return_equivalence"], "primitive theorem")
    check(theorem["zsigmondy_scope"] == theorem_expected["zsigmondy_scope"], "attribution theorem")
    check(theorem["prime_power_lift"] == theorem_expected["prime_power_lift"], "lift theorem")
    check(theorem["finite_fiber"] == theorem_expected["finite_fiber"], "fiber theorem")
    check(theorem["disjoint_union"] == theorem_expected["disjoint_union"], "disjoint theorem")
    check(theorem["profinite_limit"] == theorem_expected["profinite_limit"], "profinite theorem")

    finite = data["finite_regression_sentinels"]
    check(finite["sentinels_are_proof"] is False, "sentinel boundary")
    check(finite["pair_a_max"] == 14, "pair range")
    check(finite["fiber_a_max"] == 10, "fiber range")
    check(finite["time_max"] == 10, "time range")
    check(finite["modulus_max"] == 120, "modulus range")
    check(finite["fixed_prefix_max"] == 12, "fixed prefix range")
    check(finite["lift_prime_max"] == 257, "lift prime range")
    check(finite["lift_k_max"] == 4, "lift power range")
    all_pairs = pairs(14)
    fiber_pairs = pairs(10)
    check(finite["parameter_pair_count"] == len(all_pairs), "pair count")
    check(finite["fiber_pair_count"] == len(fiber_pairs), "fiber pair count")

    zrows = finite["zsigmondy_rows"]
    check(len(zrows) == len(all_pairs) * 9, "Zsigmondy row count")
    position = 0
    zrow_index: dict[tuple[int, int, int], dict] = {}
    for a, b in all_pairs:
        for n in range(2, 11):
            row = zrows[position]
            position += 1
            zrow_index[(a, b, n)] = row
            check((row["a"], row["b"], row["n"]) == (a, b, n), f"z indices {position}")
            difference = a**n - b**n
            check(row["difference"] == difference, f"z difference {position}")
            product = 1
            reconstructed_primitive = []
            last_prime = 1
            for entry in row["factors"]:
                prime, exponent = entry["prime"], entry["exponent"]
                check(prime > last_prime, f"factor order {position},{prime}")
                last_prime = prime
                check(is_prime(prime), f"factor primality {position},{prime}")
                check(exponent >= 1, f"factor exponent {position},{prime}")
                product *= prime**exponent
                ratio = a * pow(b, -1, prime) % prime
                order = independent_order(ratio, prime) if prime > 2 else 1
                check(entry["multiplicative_order"] == order, f"order {position},{prime}")
                primitive = order == n
                check(entry["primitive_at_n"] is primitive, f"primitive bool {position},{prime}")
                prior_hit = any((a**time - b**time) % prime == 0 for time in range(1, n))
                check(primitive is ((difference % prime == 0) and not prior_hit), f"first occurrence {position},{prime}")
                if primitive:
                    reconstructed_primitive.append(prime)
            check(product == difference, f"factor completeness {position}")
            check(row["primitive_primes"] == reconstructed_primitive, f"primitive list {position}")
            exception = exception_label(a, b, n)
            check(row["exception"] == exception, f"exception {position}")
            check(row["existence_expected"] is (exception is None), f"exist expected {position}")
            check(row["existence_observed"] is bool(reconstructed_primitive), f"exist observed {position}")
            check(row["existence_observed"] is row["existence_expected"], f"Zsigmondy sentinel {position}")

    grows = finite["global_rows"]
    check(len(grows) == len(all_pairs) * 10, "global row count")
    position = 0
    for a, b in all_pairs:
        for n in range(1, 11):
            row = grows[position]
            position += 1
            check((row["a"], row["b"], row["n"]) == (a, b, n), f"global indices {position}")
            difference = a**n - b**n
            check(row["difference"] == difference, f"global difference {position}")
            factor_product = 1
            for entry in row["factorization"]:
                check(is_prime(entry["prime"]), f"global prime {position}")
                factor_product *= entry["prime"] ** entry["exponent"]
            check(factor_product == difference, f"global factorization {position}")
            divisor_sum = sum(phi_by_factors(divisor) for divisor in factors_to_divisors(row["factorization"]))
            check(divisor_sum == difference, f"divisor phi identity {position}")
            check(row["disjoint_union_fixed_count"] == divisor_sum, f"disjoint fixed {position}")
            witness = 2
            while gcd(witness, a * b) != 1 or difference % witness == 0:
                witness += 1
            check(pow(a * pow(b, -1, witness), n, witness) != 1, f"profinite witness {position}")
            check(row["profinite_fixed_count"] == 0, f"profinite fixed {position}")
            orbit_numerator = 0
            for divisor in range(1, n + 1):
                if n % divisor == 0:
                    orbit_numerator += small_mobius(n // divisor) * (a**divisor - b**divisor)
            check(orbit_numerator % n == 0, f"orbit divisibility {position}")
            check(row["primitive_cycle_count"] == orbit_numerator // n, f"orbit count {position}")
            check(row["primitive_cycle_count"] >= 0, f"orbit nonnegative {position}")

    frows = finite["finite_fiber_rows"]
    expected_fiber_rows = sum(
        1
        for a, b in fiber_pairs
        for modulus in range(2, 121)
        if gcd(modulus, a * b) == 1
    )
    check(len(frows) == expected_fiber_rows, "finite fiber row count")
    position = 0
    for a, b in fiber_pairs:
        for modulus in range(2, 121):
            if gcd(modulus, a * b) != 1:
                continue
            row = frows[position]
            position += 1
            check((row["a"], row["b"], row["modulus"]) == (a, b, modulus), f"fiber indices {position}")
            multiplier = a * pow(b, -1, modulus) % modulus
            units = [value for value in range(modulus) if gcd(value, modulus) == 1]
            phi = len(units)
            order = independent_order(multiplier, modulus)
            check(row["multiplier"] == multiplier, f"fiber multiplier {position}")
            check(row["phi"] == phi == independent_phi(modulus), f"fiber phi {position}")
            check(row["order"] == order, f"fiber order {position}")
            check(row["cycle_count"] == phi // order, f"fiber cycles {position}")
            check(row["cycle_length_set"] == [order], f"fiber length set {position}")
            check(row["zeta_factor"] == f"(1-z^{order})^(-{phi // order})", f"fiber zeta {position}")
            check(row["koopman_determinant_factor"] == f"(1-z^{order})^{phi // order}", f"fiber determinant {position}")
            for value in units:
                cursor = value
                for _ in range(order):
                    cursor = multiplier * cursor % modulus
                check(cursor == value, f"fiber orbit closes {position},{value}")
                if order > 1:
                    cursor = value
                    returned_early = False
                    for _ in range(1, order):
                        cursor = multiplier * cursor % modulus
                        if cursor == value:
                            returned_early = True
                            break
                    check(not returned_early, f"fiber least order {position},{value}")
                inverse_value = pow(value, -1, modulus)
                lhs = pow(multiplier * inverse_value % modulus, -1, modulus)
                rhs = pow(multiplier, -1, modulus) * value % modulus
                check(lhs == rhs, f"fiber reversor {position},{value}")
            fixed_prefix = []
            for time in range(1, 13):
                fixed = sum(1 for value in units if pow(multiplier, time, modulus) * value % modulus == value)
                fixed_prefix.append(fixed)
                check(fixed == (phi if time % order == 0 else 0), f"fiber fixed {position},{time}")
            check(row["fixed_prefix"] == fixed_prefix, f"fiber prefix {position}")
            check(row["inversion_reversor_verified"] is True, f"fiber reversor flag {position}")

    lift_rows = finite["prime_power_lift_rows"]
    expected_lift_count = sum(
        4
        for row in zrows
        for prime in row["primitive_primes"]
        if prime <= 257
    )
    check(len(lift_rows) == expected_lift_count, "lift row count")
    position = 0
    for zrow in zrows:
        exponent_by_prime = {entry["prime"]: entry["exponent"] for entry in zrow["factors"]}
        for prime in zrow["primitive_primes"]:
            if prime > 257:
                continue
            for k in range(1, 5):
                row = lift_rows[position]
                position += 1
                a, b, n = zrow["a"], zrow["b"], zrow["n"]
                exponent = exponent_by_prime[prime]
                check((row["a"], row["b"], row["n"], row["prime"], row["k"]) == (a, b, n, prime, k), f"lift indices {position}")
                check(prime % 2 == 1 and is_prime(prime), f"lift odd prime {position}")
                valuation = 0
                quotient = a**n - b**n
                while quotient % prime == 0:
                    valuation += 1
                    quotient //= prime
                check(row["base_valuation"] == valuation == exponent, f"lift valuation {position}")
                modulus = prime**k
                ratio = a * pow(b, -1, modulus) % modulus
                predicted = n * prime ** max(0, k - valuation)
                observed = independent_order(ratio, modulus)
                check(row["modulus"] == modulus, f"lift modulus {position}")
                check(row["predicted_order"] == predicted, f"lift prediction {position}")
                check(row["observed_order"] == observed == predicted, f"lift order {position}")
                check(pow(ratio, predicted, modulus) == 1, f"lift closes {position}")
                for divisor_prime, _ in trial_factors(predicted):
                    check(pow(ratio, predicted // divisor_prime, modulus) != 1, f"lift minimal {position},{divisor_prime}")
                phi = phi_by_factors(modulus)
                check(row["phi"] == phi, f"lift phi {position}")
                check(row["cycle_count"] == phi // observed, f"lift cycles {position}")

    route = data["route_a"]
    route_expected = {
        "tuple": [
            "A0_WEAK_ARITHMETIC_RELATION",
            "A1_WEAK",
            "A2_FAIL",
            "A3_FAIL",
            "A4_NATURAL_QUANTIZATION",
        ],
        "A0_qualification": "RATIONAL_PRIMES_EMERGE_AS_FIRST_RETURN_MODULI_BUT_NO_SINGLE_GLOBAL_PRIME_ORBIT_OWNER_OR_LOG_P_CLOCK",
        "A1_qualification": "EVERY_FINITE_FIBER_IS_EXACT_BUT_THE_TWO_NATURAL_GLOBALIZATIONS_HAVE_INCOMPATIBLE_PRIMITIVE_LEDGERS",
        "A2_qualification": "SOURCE_ZETAS_ARE_EXACT_BUT_NO_TARGET_DIVISOR_OR_FROZEN_VALIDATION_PROTOCOL_EXISTS",
        "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
        "A4_qualification": "FINITE_PERMUTATION_AND_PROFINITE_HAAR_KOOPMAN_LIFTS_ARE_NATURAL_SAME_CLOCK_UNITARIES",
        "overall": "ROUTE_A_EXPLORATORY",
        "route_b_invocation_allowed": False,
    }
    check(route == route_expected, "exact Route-A map")
    check(route["tuple"] == route_expected["tuple"], "Route tuple")
    check(route["A0_qualification"] == route_expected["A0_qualification"], "A0 qualification")
    check(route["A1_qualification"] == route_expected["A1_qualification"], "A1 qualification")
    check(route["A2_qualification"] == route_expected["A2_qualification"], "A2 qualification")
    check(route["A3_qualification"] == route_expected["A3_qualification"], "A3 qualification")
    check(route["A4_qualification"] == route_expected["A4_qualification"], "A4 qualification")
    check(route["route_b_invocation_allowed"] is False, "Route B")

    scope_expected = {
        "assigned_log_p_roof": False,
        "built_prime_weighted_global_product": False,
        "claimed_automorphy": False,
        "claimed_hilbert_polya": False,
        "claimed_local_euler_factor": False,
        "claimed_root_number": False,
        "claimed_target_counting_law": False,
        "claimed_target_divisor_match": False,
        "claimed_target_functional_equation": False,
        "route_b_invocation_allowed": False,
        "used_target_prime_table": False,
        "used_target_zero_table": False,
    }
    check(data["scope_flags"] == scope_expected, "exact scope-flags map")
    for key in list(scope_expected)[1:]:
        check(data["scope_flags"][key] is False, f"scope flag {key}")

    integrity = data["integrity"]
    integrity_expected = {
        "citation_population": 4,
        "external_reviewer_simulated": False,
        "finite_ledgers_are_proof": False,
        "global_owner_uniqueness_claimed": False,
        "model_rejected_as_primary_route_a_candidate": False,
        "order_lift_proved_in_package": True,
        "reference_population": 4,
        "zsigmondy_theorem_claimed_new": False,
    }
    check(integrity == integrity_expected, "exact integrity map")
    check(integrity["finite_ledgers_are_proof"] is False, "finite proof boundary")
    check(integrity["zsigmondy_theorem_claimed_new"] is False, "novelty boundary")
    check(integrity["order_lift_proved_in_package"] is True, "lift proof status")
    check(integrity["citation_population"] == 4, "citation population")
    check(integrity["reference_population"] == 4, "reference population")
    check(integrity["external_reviewer_simulated"] is False, "review boundary")
    check(integrity["global_owner_uniqueness_claimed"] is False, "owner boundary")

    print(json.dumps({"status": "C179_CHECKER_PASS", "assertions": assertions}, sort_keys=True))


if __name__ == "__main__":
    main()
