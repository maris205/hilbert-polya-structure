#!/usr/bin/env python3
"""Independent exact evaluator for generated SD-C31 artifacts.

This file deliberately does not import `counterterm_core` or
`generate_results`; it re-derives the decisive rational identities from the
serialized ledgers.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def as_fraction(record: dict[str, object]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def squarefree_split(value: int) -> tuple[int, int]:
    square = 1
    radical = 1
    factor = 2
    remainder = value
    while factor * factor <= remainder:
        exponent = 0
        while remainder % factor == 0:
            remainder //= factor
            exponent += 1
        square *= factor ** (exponent // 2)
        if exponent % 2:
            radical *= factor
        factor += 1
    if remainder > 1:
        radical *= remainder
    return square, radical


class Audit:
    def __init__(self) -> None:
        self.checks: list[dict[str, object]] = []

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        self.checks.append({"name": name, "pass": bool(condition), "detail": detail})

    def payload(self) -> dict[str, object]:
        failures = [row for row in self.checks if not row["pass"]]
        return {
            "schema_version": "SD-C31-independent-evaluation-v1",
            "candidate_id": "SD-C31",
            "independent_of_candidate_core": True,
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
            "check_count": len(self.checks),
            "pass_count": len(self.checks) - len(failures),
            "failure_count": len(failures),
            "all_pass": not failures,
            "failures": failures,
            "checks": self.checks,
        }


def evaluate(results: Path) -> dict[str, object]:
    audit = Audit()
    baseline = read_json(results / "baseline_cutoffs.json")
    schemes = read_json(results / "scheme_shifts.json")
    controls = read_json(results / "control_ledgers.json")
    coefficients = read_json(results / "coefficient_search.json")
    incidence = read_json(results / "incidence_checks.json")
    determinant = read_json(results / "determinant_ownership.json")
    summary = read_json(results / "summary.json")

    for name, payload in (
        ("baseline", baseline),
        ("schemes", schemes),
        ("controls", controls),
        ("coefficients", coefficients),
        ("incidence", incidence),
        ("determinant", determinant),
        ("summary", summary),
    ):
        audit.check(f"{name}:schema", payload["schema_version"] == "SD-C31-exact-v1")
        audit.check(f"{name}:candidate", payload["candidate"] == "SD-C31")
        audit.check(f"{name}:no_target_zero_data", payload["target_zero_data_used"] is False)
        audit.check(f"{name}:route_b_false", payload["route_b_used"] is False)

    # Recompute every baseline diagonal and pair coefficient.
    previous_atoms: list[int] = []
    previous_h = Fraction(0)
    for cutoff_row in baseline["cutoffs"]:
        cutoff = int(cutoff_row["cutoff"])
        atoms = [int(value) for value in cutoff_row["atom_weights"]]
        audit.check(f"baseline:{cutoff}:atoms_in_range", all(1 < p <= cutoff for p in atoms))
        audit.check(
            f"baseline:{cutoff}:nested_atoms",
            set(previous_atoms).issubset(atoms),
        )
        h = 2 * sum((Fraction(1, p) for p in atoms), Fraction(0))
        s0 = 2 * sum((Fraction(1, p**5) for p in atoms), Fraction(0))
        s1 = 2 * sum((Fraction(1, p**6) for p in atoms), Fraction(0))
        s2 = 2 * sum((Fraction(1, p**7) for p in atoms), Fraction(0))
        d = 2 * sum((Fraction(1, p) + Fraction(1, p**5) for p in atoms), Fraction(0))
        audit.check(f"baseline:{cutoff}:H_recomputed", as_fraction(cutoff_row["leading_H"]) == h)
        audit.check(f"baseline:{cutoff}:S0_recomputed", as_fraction(cutoff_row["shifts"]["S0"]) == s0)
        audit.check(f"baseline:{cutoff}:S1_recomputed", as_fraction(cutoff_row["shifts"]["S1"]) == s1)
        audit.check(f"baseline:{cutoff}:S2_recomputed", as_fraction(cutoff_row["shifts"]["S2"]) == s2)
        audit.check(f"baseline:{cutoff}:D_recomputed", as_fraction(cutoff_row["diagonal_D"]) == d)
        audit.check(f"baseline:{cutoff}:D_equals_H_plus_S0", d == h + s0)
        audit.check(f"baseline:{cutoff}:H_increases", h > previous_h)
        expected_pair_count = len(atoms) * (len(atoms) - 1) // 2
        audit.check(f"baseline:{cutoff}:mixed_pair_count", len(cutoff_row["mixed_ledger"]) == expected_pair_count)
        audit.check(f"baseline:{cutoff}:B4_pair_count", len(cutoff_row["b4_pair_ledger"]) == expected_pair_count)
        mixed_map = {tuple(row["atom_weights"]): row for row in cutoff_row["mixed_ledger"]}
        b4_map = {tuple(row["atom_weights"]): row for row in cutoff_row["b4_pair_ledger"]}
        for left_index, p in enumerate(atoms):
            for q in atoms[left_index + 1 :]:
                key = (min(p, q), max(p, q))
                g = Fraction(1, (p**4 + 1) * (q**4 + 1))
                mrow = mixed_map[key]
                brow = b4_map[key]
                audit.check(f"baseline:{cutoff}:gram:{p}:{q}", as_fraction(mrow["gram"]) == g)
                square, radical = squarefree_split(p * q)
                expected_rational = 4 * g / (square * radical)
                audit.check(
                    f"baseline:{cutoff}:mixed_radical:{p}:{q}",
                    int(mrow["cos_amplitude"]["squarefree_radicand"]) == radical
                    and as_fraction(mrow["cos_amplitude"]["rational_coefficient"]) == expected_rational,
                )
                expected_b4 = 4 * g * g / (p * q)
                audit.check(f"baseline:{cutoff}:B4:{p}:{q}", as_fraction(brow["coefficient"]) == expected_b4)
                audit.check(f"baseline:{cutoff}:pair_positive:{p}:{q}", g > 0 and expected_b4 > 0)
        previous_atoms = atoms
        previous_h = h

    # Serialized naturality and cutoff compiler claims must all independently expose PASS.
    for index, row in enumerate(incidence["sanity_rows"]):
        audit.check(f"incidence:sanity:{index}:all_pass", row["all_pass"] is True)
        for field in (
            "zeta_mobius_two_sided_inverse",
            "pairwise_idempotent_relations",
            "partition_of_identity",
            "gram_symmetric",
        ):
            audit.check(f"incidence:sanity:{index}:{field}", row[field] is True)
    for index, row in enumerate(incidence["cutoff_embedding_rows"]):
        audit.check(f"incidence:cutoff:{index}:q", row["compiled_q_restrictions_equal"] is True)
        audit.check(f"incidence:cutoff:{index}:atoms", row["source_atom_prefix_equal"] is True)
    for index, row in enumerate(incidence["baseline_relabel_rows"]):
        audit.check(f"incidence:relabel:{index}:q", row["compiled_projectors_transport"] is True)
        audit.check(f"incidence:relabel:{index}:ledger", row["canonical_analytic_ledgers_equal"] is True)
    audit.check("incidence:generic_relabel", incidence["generic_relabel"]["all_pass"] is True)
    audit.check("incidence:morphism_scope_not_all_monotone", incidence["ordinary_monotone_maps_claimed"] is False)

    # Recompute the direct-control pair ledgers from their serialized Gram matrices.
    for control in controls["controls"]:
        name = str(control["name"])
        weights = [int(value) for value in control["atom_weights"]]
        gram = [[as_fraction(value) for value in row] for row in control["gram"]]
        audit.check(f"control:{name}:gram_symmetric", all(gram[i][j] == gram[j][i] for i in range(len(weights)) for j in range(len(weights))))
        mixed_map = {tuple(row["atom_weights"]): row for row in control["mixed_ledger"]}
        b4_map = {tuple(row["atom_weights"]): row for row in control["b4_pair_ledger"]}
        nonzero = 0
        positive_b4 = 0
        for i, p in enumerate(weights):
            for j in range(i + 1, len(weights)):
                q = weights[j]
                key = (min(p, q), max(p, q))
                g = gram[i][j]
                nonzero += int(g != 0)
                expected_b4 = 4 * g * g / (p * q)
                positive_b4 += int(expected_b4 > 0)
                audit.check(f"control:{name}:gram_ledger:{p}:{q}", as_fraction(mixed_map[key]["gram"]) == g)
                audit.check(f"control:{name}:B4_ledger:{p}:{q}", as_fraction(b4_map[key]["coefficient"]) == expected_b4)
        audit.check(f"control:{name}:nonzero_count", nonzero == int(control["nonzero_mixed_count"]))
        audit.check(f"control:{name}:B4_count", positive_b4 == int(control["positive_b4_count"]))
        audit.check(f"control:{name}:nontrivial", nonzero > 0 or positive_b4 > 0)
        audit.check(f"control:{name}:shared_pair_type", control["pointed_pair_type"] == "two_incomparable_covers_sharing_bottom")
    audit.check("controls:proves_too_much", controls["proves_too_much_certificate"]["status"] == "PROVES_TOO_MUCH")
    audit.check("controls:no_numeric_prime_oracle", controls["proves_too_much_certificate"]["numeric_prime_oracle_used"] is False)

    # Scheme freedom and coefficient contradiction.
    audit.check("schemes:full_and_lead", schemes["classification"]["full_and_lead_both_admissible"] is True)
    audit.check("schemes:finite_parts_distinct", schemes["classification"]["finite_parts_distinct"] is True)
    audit.check("schemes:not_zeta_trace", schemes["classification"]["not_a_zeta_trace"] is True)
    for index, row in enumerate(schemes["cutoff_increment_checks"]):
        audit.check(f"schemes:prefix:{index}", row["all_pass"] is True)
    for family in schemes["frozen_shift_family"]:
        audit.check(
            f"schemes:family:{family['cutoff']}:{','.join(family['coefficients'])}",
            family["is_atom_local"] is True
            and family["is_isomorphism_natural"] is True
            and family["is_prefix_additive"] is True,
        )
    search = coefficients["search"]
    recomputed_solutions = 0
    for row in search["rows"]:
        alpha = Fraction(row["diagonal_coefficient"])
        beta = Fraction(row["pair_coefficient"])
        expected = alpha == 1 and beta == 0 and beta == 1
        recomputed_solutions += int(expected)
        audit.check(
            f"coefficient:grid:{row['diagonal_coefficient']}:{row['pair_coefficient']}",
            row["selective_solution"] is expected,
        )
    audit.check("coefficient:no_grid_solution", recomputed_solutions == 0 == int(search["solution_count"]))
    audit.check("coefficient:symbolic_contradiction", search["symbolic_constraints"]["contradiction"] == "beta=0 and beta=1")
    audit.check("coefficient:global_scope_caveat", "global" in coefficients["scope_caveat"])

    # Determinant ownership and final route lock.
    power_status = {int(row["power"]): row["status"] for row in determinant["log_det3_power_ledger"]}
    audit.check("determinant:power2_deleted_whole", "including_diagonal_and_mixed" in power_status[2])
    audit.check("determinant:power3_zero", "trace_zero" in power_status[3])
    audit.check("determinant:power4_first", "first_visible" in power_status[4])
    ren = determinant["renormalized_functional"]
    audit.check("determinant:new_functional", "new_scheme_dependent" in ren["ownership"])
    audit.check("determinant:not_ordinary", determinant["ordinary_fredholm_determinant_available"] is False and determinant["det2_available"] is False)
    audit.check("determinant:scheme_ratio_nontrivial", ren["ratio_nontrivial"] is True)
    audit.check("determinant:holomorphic", ren["finite_cutoff_holomorphic_in_s_and_z"] is True and ren["infinite_mixed_holomorphic_on_det3_strip"] is True)
    audit.check("determinant:reflection", ren["reflection_preserved"] is True)
    audit.check("summary:route_tuple", summary["route_tuple"] == ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_FAIL", "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL"])
    audit.check("summary:overall_rejected", summary["overall_status"] == "REJECTED_AS_RH_COMPLETION")
    audit.check("summary:claims_all_true", all(bool(value) for value in summary["claims"].values()))
    audit.check("summary:route_b_false", summary["route_b"] is False)
    return audit.payload()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, required=True)
    args = parser.parse_args()
    payload = evaluate(args.results)
    (args.results / "evaluation.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not payload["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
