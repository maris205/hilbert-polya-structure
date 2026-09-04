#!/usr/bin/env python3
"""Independent checker for HCS-C374; deliberately imports no producer code."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c374_kummer_arboreal_evidence.json"
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
LEVELS = range(3, 13)
PRIME_BOUND = 100000


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def strict_json(path: Path) -> dict:
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate JSON key: {key}")
            out[key] = value
        return out

    value = json.loads(
        path.read_text(),
        object_pairs_hook=unique,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite JSON: {token}")),
    )
    if type(value) is not dict:
        raise TypeError("evidence root is not a mapping")
    return value


def character(a: int) -> int:
    return 1 if a % 8 in (1, 7) else -1


def formula_histogram(n: int) -> dict[int, int]:
    order = 2 ** (2 * n - 2)
    hist = {2: 2 ** (2 * n - 4), 2**n: 1}
    for k in range(3, n):
        hist[2**k] = 2 ** (2 * n - 2 * k - 1)
    hist[0] = order - sum(hist.values())
    return dict(sorted(hist.items()))


def independent_enumeration(n: int) -> dict[int, int]:
    modulus = 2**n
    hist: Counter[int] = Counter()
    for a in range(1, modulus, 2):
        wanted = 0 if character(a) == 1 else 1
        divisor = math.gcd(a - 1, modulus)
        for b in range(wanted, modulus, 2):
            count = divisor if (-b) % divisor == 0 else 0
            hist[count] += 1
    return dict(sorted(hist.items()))


def full_affine_enumeration(n: int) -> dict[int, int]:
    modulus = 2**n
    hist: Counter[int] = Counter()
    for a in range(1, modulus, 2):
        divisor = math.gcd(a - 1, modulus)
        for b in range(modulus):
            count = divisor if (-b) % divisor == 0 else 0
            hist[count] += 1
    return dict(sorted(hist.items()))


def odd_primes(bound: int) -> list[int]:
    mark = [True] * (bound + 1)
    mark[0] = mark[1] = False
    for q in range(2, math.isqrt(bound) + 1):
        if mark[q]:
            for multiple in range(q * q, bound + 1, q):
                mark[multiple] = False
    return [q for q in range(3, bound + 1, 2) if mark[q]]


def factorization(value: int) -> list[tuple[int, int]]:
    factors = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 1
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def root_count(p: int, n: int) -> int:
    d = math.gcd(2**n, p - 1)
    return d if pow(2, (p - 1) // d, p) == 1 else 0


def check(path: Path) -> int:
    evidence = strict_json(path)
    checks = 0

    def equal(actual, expected, label):
        nonlocal checks
        if actual != expected:
            raise AssertionError(f"{label}: {actual!r} != {expected!r}")
        checks += 1

    expected_keys = {
        "schema", "candidate_id", "obstruction_id", "source_commit", "fixed_epoch",
        "scope_literal", "model", "analytic_theorem", "group_ledger", "prime_regression",
        "arithmetic_controls", "quantization_boundary", "sources", "ownership_boundary", "collision_boundary", "route_a", "scope_flags",
        "nonclaims", "payload_sha256",
    }
    equal(set(evidence), expected_keys, "top-level keys")
    claimed = evidence.pop("payload_sha256")
    equal(claimed, hashlib.sha256(canonical(evidence)).hexdigest(), "payload digest")
    evidence["payload_sha256"] = claimed
    equal(evidence["schema"], "hcs-c374-kummer-arboreal-evidence-v1", "schema")
    equal(evidence["candidate_id"], "HCS-C374", "candidate")
    equal(evidence["obstruction_id"], "HEN-O358", "obstruction")
    equal(evidence["source_commit"], SOURCE, "source commit")
    equal(evidence["fixed_epoch"], 1788480000, "epoch")
    equal(evidence["scope_literal"], SCOPE, "scope")

    model = evidence["model"]
    equal(model["map"], "f(z)=z^2", "map")
    equal(model["basepoint"], 2, "basepoint")
    equal(model["level_range_theorem"], "all n>=3", "theorem range")
    equal(model["level_range_evidence"], [3, 12], "evidence range")

    theorem = evidence["analytic_theorem"]
    equal(theorem["degree"], "[K_n:Q]=2^(2n-2)", "degree theorem")
    equal(theorem["inverse_limit_index"], 2, "inverse-limit index")
    equal(theorem["forbidden_root_counts"], [1, 4], "forbidden root counts")
    for token in ("intersect Q(zeta_(2^n)) = Q(sqrt(2))", "(-1)^b=(2/a)", "kernel order 4", "limit 7/24"):
        equal(any(token in str(value) for value in theorem.values()), True, f"theorem token {token}")

    route = {
        "tuple": ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
        "overall": "ROUTE_A_EXPLORATORY",
        "route_b_invocation_allowed": False,
        "a1_scope": "the proved affine action and fixed-root law are source-local and do not constitute a complete arithmetic primitive-orbit atlas",
        "a1_missing_requirements": [
            "no all-level primitive-cycle and repetition enumeration with completeness control",
            "no orbit orientation, phase, multiplicity-weight, or monodromy and stability atlas",
            "no intrinsic prime-to-orbit, prime-power, or log(p) period correspondence",
            "mandatory shuffled-period, random-weight, random-phase, same-density-length, neighboring-parameter, and simpler-parent controls are not completed at the A1 orbit layer",
        ],
    }
    equal(evidence["route_a"], route, "route tuple")
    equal(set(evidence["scope_flags"].values()), {False}, "forbidden flags")
    equal(len(evidence["nonclaims"]), 4, "nonclaims")
    control_preflight = evidence["arithmetic_controls"]
    equal(control_preflight["neighboring_basepoint_3"]["status"],
          "PROVED_BY_VALUATION_AND_CAPELLI", "neighbor-control preflight")
    equal(control_preflight["neighboring_basepoint_3"]["shared_Q_sqrt_2_character_entanglement"],
          False, "neighbor-entanglement preflight")
    equal(control_preflight["simpler_parent_full_affine"]["status"],
          "EXECUTED_EXACT", "parent-control preflight")
    equal(control_preflight["simpler_parent_full_affine"]["restores_four_fixed_roots"],
          True, "parent-four-root preflight")
    equal(control_preflight["composite_label_decomposition"]
          ["mixed_composite_has_single_prime_frobenius_owner"],
          False, "mixed-composite-owner preflight")
    equal(control_preflight["empirical_density_earns_a0_credit"], False,
          "density-credit preflight")
    equal("HCS-C12A" in evidence["ownership_boundary"]["inherited"], True, "C12A owner")
    equal(set(evidence["collision_boundary"]), {"nearest_C12A", "nearest_C33_C34_C38_C40", "nearest_C56", "nearest_C179", "nearest_C369"}, "collision ledger")

    sources = evidence["sources"]
    equal([row["doi"] for row in sources], [
        "10.5802/pmb.a-154", "10.1007/978-1-4613-0041-0",
        "10.1007/978-1-4612-1934-7", "10.1007/978-3-662-03983-0",
    ], "source DOI ledger")
    for row in sources:
        equal(row["url"], "https://doi.org/" + row["doi"], f"DOI URL {row['key']}")

    levels = evidence["group_ledger"]
    equal([row["n"] for row in levels], list(LEVELS), "group levels")
    for row in levels:
        n = row["n"]
        expected = formula_histogram(n)
        stored = {int(k): value for k, value in row["fixed_point_histogram"].items()}
        equal(stored, expected, f"formula histogram n={n}")
        equal(row["group_order"], 2 ** (2 * n - 2), f"order n={n}")
        equal(row["ambient_affine_order"], 2 ** (2 * n - 1), f"ambient order n={n}")
        equal(row["image_index"], 2, f"index n={n}")
        equal(row["exhaustive_pairs"], row["group_order"], f"pair count n={n}")
        positive = row["group_order"] - expected[0]
        equal(row["positive_fixed_elements"], positive, f"positive n={n}")
        density = Fraction(7, 24) + Fraction(1, 3 * 4 ** (n - 1))
        equal(row["root_prime_density"], f"{density.numerator}/{density.denominator}", f"density n={n}")
        if n == 3:
            equal(row["restriction_to_previous"], None, "first restriction")
        else:
            equal(row["restriction_to_previous"], {"map": "(a,b) modulo 2^(n-1)", "surjective": True, "kernel_order": 4}, f"restriction n={n}")
        equal(independent_enumeration(n), expected, f"exhaustive image n={n}")

    regression = evidence["prime_regression"]
    equal(regression["prime_bound"], PRIME_BOUND, "prime bound")
    primes = odd_primes(PRIME_BOUND)
    equal(regression["odd_prime_count"], len(primes), "prime count")
    equal(regression["cell_count"], len(primes) * len(list(LEVELS)), "prime cells")
    equal([row["n"] for row in regression["levels"]], list(LEVELS), "prime levels")
    stream = hashlib.sha256()
    for row in regression["levels"]:
        n = row["n"]
        hist: Counter[int] = Counter()
        first = {}
        for p in primes:
            roots = root_count(p, n)
            hist[roots] += 1
            first.setdefault(str(roots), p)
            stream.update(canonical([p, n, roots]) + b"\n")
        stored = {str(k): value for k, value in sorted(hist.items())}
        equal(row["root_histogram"], stored, f"prime histogram n={n}")
        equal(row["first_witness"], dict(sorted(first.items(), key=lambda item: int(item[0]))), f"witnesses n={n}")
        positive = len(primes) - hist[0]
        equal(row["with_root"], positive, f"prime positive n={n}")
        equal(row["empirical_fraction"], f"{positive}/{len(primes)}", f"empirical fraction n={n}")
        equal("1" not in row["root_histogram"] and "4" not in row["root_histogram"], True, f"forbidden counts n={n}")
    equal(regression["row_stream_sha256"], stream.hexdigest(), "prime row stream")
    equal("not proof" in regression["role"], True, "evidence boundary")

    controls = evidence["arithmetic_controls"]
    neighbor = controls["neighboring_basepoint_3"]
    equal(neighbor["status"], "PROVED_BY_VALUATION_AND_CAPELLI", "basepoint-3 control status")
    equal(neighbor["radical_cyclotomic_intersection"],
          "Q(3^(1/2^n)) intersect Q(zeta_(2^n)) = Q for every n>=3",
          "basepoint-3 intersection control")
    equal(neighbor["affine_image"], "full AGL_1(Z/2^n)", "basepoint-3 full image")
    equal(neighbor["shared_Q_sqrt_2_character_entanglement"], False,
          "basepoint-3 entanglement control")
    parent = controls["simpler_parent_full_affine"]
    equal(parent["status"], "EXECUTED_EXACT", "full-affine control status")
    equal([row["n"] for row in parent["level_ledger"]], list(LEVELS), "full-affine levels")
    total_parent = 0
    for row in parent["level_ledger"]:
        n = row["n"]
        expected = full_affine_enumeration(n)
        stored = {int(k): value for k, value in row["fixed_point_histogram"].items()}
        equal(stored, expected, f"full-affine histogram n={n}")
        equal(row["group_order"], 2 ** (2 * n - 1), f"full-affine order n={n}")
        equal(row["four_fixed_elements"], 2 ** (2 * n - 5), f"four-root recovery n={n}")
        equal(row["four_fixed_formula"], "2^(2n-5)", f"four-root formula n={n}")
        total_parent += row["group_order"]
    equal(parent["total_pairs"], total_parent, "full-affine total pairs")
    equal(parent["restores_four_fixed_roots"], True, "full-affine restores four roots")
    composite = controls["composite_label_decomposition"]
    prime_set = set(odd_primes(100))
    expected_composites = [value for value in range(9, 100, 2) if value not in prime_set]
    expected_prime_powers = []
    expected_mixed = []
    for value in expected_composites:
        factors = factorization(value)
        if len(factors) == 1:
            prime, exponent = factors[0]
            expected_prime_powers.append({"value": value, "prime": prime, "exponent": exponent})
        else:
            expected_mixed.append({
                "value": value,
                "distinct_prime_factors": [prime for prime, _ in factors],
            })
    equal(composite["status"], "EXECUTED_EXACT", "composite control status")
    equal(composite["odd_composite_count_below_100"], len(expected_composites),
          "composite control count")
    equal(composite["prime_power_labels"], expected_prime_powers, "prime-power labels")
    equal(composite["prime_power_count"], len(expected_prime_powers), "prime-power count")
    equal(composite["prime_power_owner"],
          "p^r is retained as the conjugacy class of Frob_p^r and as a repetition control",
          "prime-power repetition owner")
    equal(composite["mixed_composite_labels"], expected_mixed, "mixed-composite labels")
    equal(composite["mixed_composite_count"], len(expected_mixed), "mixed-composite count")
    equal(composite["mixed_composite_has_single_prime_frobenius_owner"], False,
          "mixed-composite Frobenius owner")
    equal(controls["empirical_density_earns_a0_credit"], False, "empirical density A0 credit")
    quantization = evidence["quantization_boundary"]
    equal(set(quantization), {
        "finite_hilbert_spaces", "operator", "same_level_and_iterate_clock",
        "canonical_global_time_reversal_to_inverse",
        "nontrivial_orbit_phase_or_weight_package",
        "global_self_adjoint_hamiltonian_owner", "route_a_verdict",
    }, "quantization-boundary keys")
    equal(quantization["finite_hilbert_spaces"], "l2(R_n)", "finite Hilbert spaces")
    equal(quantization["operator"],
          "the real basis-permutation unitary attached to each finite Galois element",
          "finite unitary operator")
    equal(quantization["same_level_and_iterate_clock"], True, "finite clock preservation")
    equal(quantization["canonical_global_time_reversal_to_inverse"], False,
          "global time-reversal boundary")
    equal(quantization["nontrivial_orbit_phase_or_weight_package"], False,
          "phase-weight boundary")
    equal(quantization["global_self_adjoint_hamiltonian_owner"], False,
          "self-adjoint owner boundary")
    equal(quantization["route_a_verdict"], "A4_FORMAL_HINT", "strict A4 verdict")
    return checks


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C374 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT)
    args = parser.parse_args()
    count = check(args.input)
    print(f"C374 independent checker: PASS ({count} assertions)")


if __name__ == "__main__":
    main()
