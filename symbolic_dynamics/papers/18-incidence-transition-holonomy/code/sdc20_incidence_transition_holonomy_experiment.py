#!/usr/bin/env python3
"""Generate byte-deterministic exact authority artifacts for SD-C20."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import sys

import sympy

from sdc20_incidence_transition_holonomy_core import (
    SCREENING_PRIMES,
    exact_audit_summary,
    exact_group_audit,
    explicit_s3_certificate,
    incidence_orbit_rows,
    incidence_orbit_summary,
    inventory_control_rows,
    primitive_holonomy_rows,
    trace_class_gate_rows,
    transition_control_rows,
)


FROZEN = {
    "candidate_id": "SD-C20",
    "primary_group": "S3",
    "cocycle": "alpha(S,T)=r if S proper-subset T; t if T proper-subset S; e otherwise",
    "two_atom_table_order": ["a", "c", "h", "u", "v"],
    "incidence_atom_cutoff": 4,
    "exhaustive_groups": ["S3", "D4", "Q8"],
    "group_table_power": 5,
    "screening_primes": list(SCREENING_PRIMES),
    "control_seeds": list(range(18_001, 18_006)),
    "coefficient_ring": "Z[x,y] with exact CRT certification",
    "target_zero_data_used": False,
}


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            extrasaction="raise",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
    )
    args = parser.parse_args()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)

    orbit_rows = incidence_orbit_rows(max_atoms=4)
    orbit_summary = incidence_orbit_summary(max_atoms=4)
    write_csv(output / "incidence_orbits.csv", orbit_rows)
    write_csv(output / "incidence_orbit_summary.csv", orbit_summary)

    group_certificates = {
        group_name: exact_group_audit(group_name)
        for group_name in FROZEN["exhaustive_groups"]
    }
    group_rows = [
        {
            "group": certificate["group"],
            "group_order": certificate["group_order"],
            "tables": certificate["tables"],
            "one_dimensional_clean": certificate["one_dimensional_clean"],
            "all_irrep_clean": certificate["all_irrep_clean"],
            "gauge_power_clean": certificate["gauge_power_clean"],
            "nongauge_clean": certificate["nongauge_clean"],
            "faithful_representation": certificate["faithful_representation"],
            "faithful_dimension": certificate["faithful_dimension"],
            "modular_determinant_evaluations": certificate["modular_determinant_evaluations"],
            "all_irrep_clean_equals_gauge": certificate["all_irrep_clean_equals_gauge"],
            "crt_bound_strict": certificate["exact_certification"]["crt_bound_strict"],
            "full_rectangular_grid_certification": certificate["exact_certification"]["survivors_passed_full_rectangular_grids"],
            "exhaustive": True,
        }
        for certificate in group_certificates.values()
    ]
    write_csv(output / "group_enumeration_summary.csv", group_rows)
    write_json(output / "group_exact_certificates.json", group_certificates)

    explicit = explicit_s3_certificate()
    write_json(output / "s3_exact_certificate.json", explicit)
    primitive_rows = primitive_holonomy_rows()
    write_csv(output / "primitive_holonomy_ledger.csv", primitive_rows)

    transition_rows = transition_control_rows()
    write_csv(output / "transition_controls.csv", transition_rows)
    inventory_rows = inventory_control_rows(FROZEN["control_seeds"])
    write_csv(output / "inventory_controls.csv", inventory_rows)
    trace_rows = trace_class_gate_rows()
    write_csv(output / "trace_class_gates.csv", trace_rows)

    summary = exact_audit_summary()
    gates = {
        "GO_GENUINE_TRANSITION_HOLONOMY": (
            explicit["four_cycle_holonomy_nonidentity"] is True
            and explicit["four_cycle_character_gap"] == 3
        ),
        "GO_SAME_OBJECT_ARTIN_BLOCKS": (
            explicit["trivial_exact"] is True
            and explicit["sign_exact"] is True
            and explicit["standard_formula_exact"] is True
        ),
        "GO_TRIVIAL_EULER_FACTOR": (
            explicit["trivial_exact"] is True and explicit["sign_exact"] is True
        ),
        "GO_TRACE_CLASS_RE_GT_2": any(
            row["block"] == "nontrivial_symmetric_incidence"
            and row["threshold"] == 2
            and row["evidence_status"] == "PROVED"
            for row in trace_rows
        ),
        "STOP_NONABELIAN_CLEAN_FACTOR": (
            explicit["trace_log_coefficients"]["x^2y^1"] == "-3"
            and explicit["trace_log_coefficients"]["x^1y^2"] == "-3"
            and explicit["trace_log_coefficients"]["x^2y^2"] == "-6"
        ),
        "STOP_ONE_DIMENSIONAL_CHARACTER_AUDIT": (
            group_certificates["Q8"]["one_dimensional_clean"] == 512
            and group_certificates["Q8"]["all_irrep_clean"] == 64
        ),
        "STOP_ARITHMETIC_SELECTIVITY": all(
            row["trivial_euler_ledger_exact"] is True
            and row["standard_leakage_persists"] is True
            for row in inventory_rows
        ),
        "PROVES_TOO_MUCH": all(
            row["inventory_blind_symbolic_rule"] is True for row in inventory_rows
        ),
        "NO_TARGET_ZERO_DATA": True,
    }
    payload = {
        "candidate_id": "SD-C20",
        "runtime": {
            "python_implementation": sys.implementation.name,
            "python_version": ".".join(str(value) for value in sys.version_info[:3]),
            "sympy_version": sympy.__version__,
        },
        "frozen_parameters": FROZEN,
        "row_counts": {
            "incidence_orbits": len(orbit_rows),
            "incidence_orbit_summary": len(orbit_summary),
            "group_enumeration_summary": len(group_rows),
            "primitive_holonomy_ledger": len(primitive_rows),
            "transition_controls": len(transition_rows),
            "inventory_controls": len(inventory_rows),
            "trace_class_gates": len(trace_rows),
        },
        "exact_summary": summary,
        "predeclared_gates": gates,
        "claim_boundaries": {
            "all_character_determinants_classify_gauge": False,
            "finite_group_rigidity_universalized": False,
            "one_dimensional_characters_sufficient": False,
            "unmarked_x3y3_isolated_commutator": False,
            "trivial_trace_class_half_plane": "Re(s)>1",
            "nontrivial_trace_class_half_plane": "Re(s)>2",
            "meromorphic_continuation_claimed": False,
            "route_tuple": [
                "A0_ANALYTIC_ARITHMETIC_ORIGIN",
                "A1_WEAK",
                "A2_ANALYTIC_DETERMINANT",
                "A3_FAIL",
                "A4_FAIL",
            ],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "target_zero_data_used": False,
    }
    write_json(output / "run_summary.json", payload)

    failed = [name for name, passed in gates.items() if passed is not True]
    if failed:
        print("FAILED GATES: " + ", ".join(failed), file=sys.stderr)
        return 1
    print(json.dumps(payload["row_counts"], indent=2, sort_keys=True))
    print("all preregistered exact gates passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
