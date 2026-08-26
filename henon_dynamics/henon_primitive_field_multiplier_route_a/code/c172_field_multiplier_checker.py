#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C172."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


Q_VALUES = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32]
N_MAX = 24
EXPECTED_TOP = {"schema", "candidate_id", "evaluation_date", "scope_literal", "source_commit", "source_lock",
                "orbit_theorem", "zeta_theorem", "koopman_theorem", "reversal_theorem", "arithmetic_controls",
                "finite_ledgers", "route_a", "claim_boundary", "integrity", "payload_sha256"}


def digest(data: dict) -> str:
    work = dict(data)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def prime_power(Q: int) -> tuple[int, int]:
    for p in range(2, Q+1):
        prime = all(p % r for r in range(2, int(p**0.5)+1))
        if not prime:
            continue
        value, e = 1, 0
        while value < Q:
            value *= p
            e += 1
        if value == Q:
            return p, e
    raise AssertionError(f"not a prime power: {Q}")


def h_control(N: int) -> int:
    if N == 1:
        return 1
    return next(h for h in range(2,N+1) if gcd(h,N)>1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1] / "results/c172_field_multiplier_evidence.json")
    parser.add_argument("--mutation-fast", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    assertions = 0

    def check(condition: bool, label: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(label)

    check(set(data) == EXPECTED_TOP, "top keys")
    check(data["payload_sha256"] == digest(data), "payload hash")
    check(data["schema"] == "hcs-c172-primitive-field-multiplier-v1", "schema")
    check(data["candidate_id"] == "HCS-C172", "candidate")
    check(data["evaluation_date"] == "2026-08-26", "date")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["source_commit"] == "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f", "commit")
    lock = data["source_lock"]
    check(set(lock) == {"object", "parameters", "arithmetic_origin", "clock", "normalization", "determinant_convention",
                        "cutoff", "precision", "allowed_data", "forbidden_data"}, "lock keys")
    check(lock["object"].startswith("T_a(x)=a*x on F_Q"), "object")
    check(lock["parameters"] == "prime power Q>=2 and an arbitrary primitive generator a; no fitted parameter", "parameters")
    check("no rational-prime orbit dictionary" in lock["arithmetic_origin"], "arithmetic boundary")
    check(lock["clock"] == "one multiplication by a is one discrete step", "clock")
    check(lock["cutoff"] == {"Q_values": Q_VALUES, "n_max": N_MAX}, "cutoff")
    check(lock["precision"] == "exact integers and finite cyclic-group identities", "precision")
    check("global Euler products" in lock["forbidden_data"] and "Route B" in lock["forbidden_data"], "forbidden")

    orbit = data["orbit_theorem"]
    check(set(orbit) == {"decomposition", "coordinate_proof", "fixed_points", "primitive_inventory", "all_prime_powers"}, "orbit keys")
    check(orbit["decomposition"] == "{0} is fixed and F_Q^times is one cycle of length N=Q-1", "orbit decomposition")
    check(orbit["all_prime_powers"] is True, "all Q")
    zeta = data["zeta_theorem"]
    check(set(zeta) == {"definition", "formula", "proof", "formal_and_analytic_domain"}, "zeta keys")
    check(zeta["formula"] == "zeta_T(z)=1/((1-z)(1-z^N))", "zeta formula")
    koop = data["koopman_theorem"]
    check(set(koop) == {"operator", "unitary", "spectrum", "determinant", "relation_to_zeta", "self_adjoint_iff"}, "Koopman keys")
    check(koop["unitary"] is True and koop["self_adjoint_iff"] == "Q<=3, equivalently N<=2", "Koopman boundary")
    rev = data["reversal_theorem"]
    check(set(rev) == {"involution", "identity", "antiunitary", "same_clock"}, "reversal keys")
    check(rev["identity"] == "I T_a I=T_a^(-1)" and rev["same_clock"] is True, "reversal")
    controls = data["arithmetic_controls"]
    check(len(controls) == 4, "control count")
    check([c["name"] for c in controls] == ["composite cyclic surrogate", "nonprimitive multiplier",
                                               "same-cycle random permutation", "neighboring prime powers"], "controls")

    rows = data["finite_ledgers"]
    check(len(rows) == len(Q_VALUES), "row count")
    for Q, row in zip(Q_VALUES, rows):
        keys = {"Q", "characteristic_prime", "extension_degree", "N", "orbit_inventory", "fix_counts_n_1_to_24",
                "zeta_inverse_factors", "koopman_determinant", "koopman_eigenvalue_description",
                "eigenvalue_one_multiplicity", "self_adjoint", "nonprimitive_control_exponent_h",
                "nonprimitive_control_cycle_count", "nonprimitive_control_cycle_length"}
        check(set(row) == keys, f"Q={Q} keys")
        p,e = prime_power(Q)
        N = Q-1
        check(row["Q"] == Q and row["characteristic_prime"] == p and row["extension_degree"] == e and row["N"] == N, f"Q={Q} provenance")
        inventory = ([{"period":1,"primitive_orbits":2}] if N==1 else
                     [{"period":1,"primitive_orbits":1},{"period":N,"primitive_orbits":1}])
        check(row["orbit_inventory"] == inventory, f"Q={Q} inventory")
        fixes = [Q if n%N==0 else 1 for n in range(1,N_MAX+1)]
        check(row["fix_counts_n_1_to_24"] == fixes, f"Q={Q} fixes")
        check(row["zeta_inverse_factors"] == [{"factor":"1-z","exponent":1},{"factor":f"1-z^{N}","exponent":1}], f"Q={Q} zeta")
        check(row["koopman_determinant"] == f"(1-z)*(1-z^{N})", f"Q={Q} determinant")
        check(row["koopman_eigenvalue_description"] == f"one extra eigenvalue 1 plus every {N}-th root of unity once", f"Q={Q} spectrum")
        check(row["eigenvalue_one_multiplicity"] == 2 and row["self_adjoint"] is (N<=2), f"Q={Q} self-adjoint")
        h = h_control(N)
        g = gcd(h,N)
        check(row["nonprimitive_control_exponent_h"] == h, f"Q={Q} h")
        check(row["nonprimitive_control_cycle_count"] == g and row["nonprimitive_control_cycle_length"] == N//g, f"Q={Q} h cycles")
        if not args.mutation_fast:
            # Abstract primitive coordinates: star is fixed, k -> k+1 mod N.
            for n in range(1,N_MAX+1):
                fixed = 1 + sum(1 for k in range(N) if (k+n)%N == k)
                check(fixed == fixes[n-1], f"Q={Q},n={n} cycle enumeration")
            seen, cycles = set(), []
            for k in range(N):
                if k in seen:
                    continue
                cycle, x = [], k
                while x not in seen:
                    seen.add(x); cycle.append(x); x=(x+h)%N
                cycles.append(cycle)
            check(len(cycles)==g and all(len(c)==N//g for c in cycles), f"Q={Q} nonprimitive enumeration")

    route = data["route_a"]
    check(route == {"tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
                    "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False}, "route")
    boundary = data["claim_boundary"]
    check(set(boundary) == {"all_prime_power_orbit_theorem", "all_prime_power_zeta_and_koopman_theorem",
                            "finite_ledgers_are_proof", "prime_phase_space_is_prime_orbit_dictionary",
                            "log_p_clock_or_von_mangoldt_weight", "target_divisor_matching",
                            "target_functional_equation_or_counting_law", "arithmetic_local_data",
                            "global_euler_product_or_local_factor", "root_numbers", "automorphy", "hilbert_polya_operator"}, "boundary keys")
    check(boundary["all_prime_power_orbit_theorem"] and boundary["all_prime_power_zeta_and_koopman_theorem"], "positive claims")
    check(not any(boundary[k] for k in boundary if k not in {"all_prime_power_orbit_theorem", "all_prime_power_zeta_and_koopman_theorem"}), "negative claims")
    integrity = data["integrity"]
    check(integrity["hard_gate_status"] == "PASS" and integrity["pivot_required"] is False, "gate")
    check(integrity["registered_citation_population"] == 0 and integrity["external_reviewer_simulated"] is False, "integrity")
    print(json.dumps({"status": "C172_CHECKER_PASS", "assertions": assertions}, sort_keys=True))


if __name__ == "__main__":
    main()
